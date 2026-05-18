"""Benchmark runner for local compression model scenarios."""

from __future__ import annotations

import argparse
import asyncio
from datetime import UTC, datetime
import ast
import os
from pathlib import Path
import re
from statistics import mean
import sys
import time
from typing import Awaitable, Iterable, TypeVar

from benchmark.loader import load_manifest
from benchmark.metrics import (
    current_process_rss_bytes,
    gpu_peak_memory_bytes,
    reset_gpu_peak_memory,
    thread_env_value,
    torch_module_or_none,
    torch_num_interop_threads,
    torch_num_threads,
)
from benchmark.report import write_result_files
from benchmark.scoring import (
    brevity_ratio,
    case_benchmark_score,
    exact_ratio,
    final_benchmark_score,
    format_adherence_score,
    instruction_following_score,
    latency_factor_score,
    missing_tokens,
    quality_core_score,
    summary_quality_ratio,
)
from benchmark.schemas import (
    BenchmarkCase,
    BenchmarkScenario,
    CaseMetrics,
    ScenarioResult,
    ScenarioSummary,
    WarmupMetrics,
)
from benchmark.stats import percentile
from ctxsift.extraction import ExtractionContext, extract_signal
from ctxsift.models import create_local_backend
from ctxsift.models.base import (
    BackendUnavailableError,
    ModelBackend,
    ModelCompressionInput,
    ModelOutputRejectedError,
)
from ctxsift.models.text_profile_common import (
    validate_instruction_aware_output,
    validation_flags,
)
from ctxsift.types import LocalModelConfig, LocalQuantizationMode
from ctxsift.workspace import detect_workspace_context


_AwaitableResult = TypeVar("_AwaitableResult")
_RUN_NAME_RE = re.compile(r"[^A-Za-z0-9._-]+")
_VALIDATION_STATUS_RE = re.compile(r"\b(?:first_pass_status|repair_status)=(accepted|soft_accepted|rejected)\b")
_VALIDATION_FLAGS_RE = re.compile(r"\b(?:first_pass_flags|repair_flags)=(\[[^\]]*\])")
_ANSI_RESET = "\x1b[0m"
_ANSI_BLUE = "\x1b[34m"
_ANSI_GREEN = "\x1b[32m"
_ANSI_RED = "\x1b[31m"


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for benchmark execution."""
    parser = argparse.ArgumentParser(description="Run local ctxsift model benchmarks.")
    parser.add_argument(
        "--dataset",
        default="benchmark/dataset.jsonl",
        help="Path to the benchmark dataset JSONL file.",
    )
    parser.add_argument(
        "--matrix",
        default="benchmark/matrix.json",
        help="Path to the benchmark scenario matrix JSON file.",
    )
    parser.add_argument(
        "--output-dir",
        default="benchmark/results",
        help="Directory where per-scenario reports are written.",
    )
    parser.add_argument(
        "--name",
        default="",
        help="Optional run name prefix for the timestamped output folder.",
    )
    parser.add_argument(
        "--scenario",
        action="append",
        default=[],
        help="Run only the named scenario. Can be passed multiple times.",
    )
    parser.add_argument(
        "--phase",
        action="append",
        default=[],
        help="Run only scenarios from the named phase. Can be passed multiple times.",
    )
    parser.add_argument(
        "--show-output",
        action="store_true",
        help="Print each case output inline while the benchmark runs.",
    )
    parser.add_argument(
        "--list-scenarios",
        action="store_true",
        help="List available benchmark scenarios and exit.",
    )
    parser.add_argument(
        "--case-id",
        action="append",
        default=[],
        help="Run only the named benchmark case. Can be passed multiple times.",
    )
    parser.add_argument(
        "--max-cases",
        type=int,
        default=0,
        help="Run only the first N benchmark cases after any case-id filtering.",
    )
    return parser


async def main() -> int:
    """Run the configured benchmark scenarios."""
    parser = build_parser()
    args = parser.parse_args()
    manifest = load_manifest(Path(args.dataset), Path(args.matrix))
    cases = select_cases(
        manifest.cases,
        case_ids=set(args.case_id),
        max_cases=args.max_cases,
    )
    scenarios = select_scenarios(
        manifest.scenarios,
        names=set(args.scenario),
        phases=set(args.phase),
    )
    if args.list_scenarios:
        _print_scenarios(scenarios)
        return 0
    if not scenarios:
        parser.error(
            build_scenario_filter_error(
                manifest.scenarios,
                names=set(args.scenario),
                phases=set(args.phase),
            )
        )
    if not cases:
        parser.error("No benchmark cases matched the requested filters.")
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_root = Path(args.output_dir)
    named_run_output_dir = output_root / build_run_directory_name(timestamp, args.name)
    total_scenarios = len(scenarios)
    output_label = (
        str(named_run_output_dir)
        if args.name.strip()
        else f"{output_root} (per-scenario folders)"
    )
    print(
        f"Running {total_scenarios} benchmark scenario(s) across {len(cases)} case(s). "
        f"Output dir: {output_label}"
    )
    for scenario_index, scenario in enumerate(scenarios, start=1):
        scenario_output_dir = resolve_run_output_dir(
            output_root=output_root,
            timestamp=timestamp,
            run_name=args.name,
            scenario_name=scenario.name,
        )
        print(
            f"[scenario {scenario_index}/{total_scenarios}] {scenario.name} "
            f"model={scenario.model} quant={scenario.quantization} device={scenario.device} "
            f"remaining={total_scenarios - scenario_index}"
        )
        result = await run_scenario(
            scenario,
            cases,
            show_output=args.show_output,
        )
        write_result_files(scenario_output_dir, result)
        print(f"Wrote {scenario.name} results to {scenario_output_dir}")
    return 0


def select_scenarios(
    scenarios: tuple[BenchmarkScenario, ...],
    *,
    names: set[str],
    phases: set[str],
) -> list[BenchmarkScenario]:
    """Filter enabled scenarios by name and phase."""
    selected: list[BenchmarkScenario] = []
    for scenario in scenarios:
        if not scenario.enabled:
            continue
        if names and scenario.name not in names:
            continue
        if phases and scenario.phase not in phases:
            continue
        selected.append(scenario)
    return selected


def select_cases(
    cases: tuple[BenchmarkCase, ...],
    *,
    case_ids: set[str],
    max_cases: int,
) -> tuple[BenchmarkCase, ...]:
    """Filter benchmark cases by id and count."""
    selected = [case for case in cases if not case_ids or case.case_id in case_ids]
    if max_cases > 0:
        selected = selected[:max_cases]
    return tuple(selected)


def build_scenario_filter_error(
    scenarios: tuple[BenchmarkScenario, ...],
    *,
    names: set[str],
    phases: set[str],
) -> str:
    """Build a clearer scenario-filter error message."""
    if not names:
        return "No benchmark scenarios matched the requested filters."
    requested = sorted(names)
    available_by_name = {
        scenario.name: scenario
        for scenario in scenarios
        if scenario.enabled and scenario.name in names
    }
    if not available_by_name:
        requested_text = ", ".join(requested)
        return f"No benchmark scenarios matched the requested names: {requested_text}."
    if not phases:
        return "No benchmark scenarios matched the requested filters."
    mismatches: list[str] = []
    for scenario_name in requested:
        scenario = available_by_name.get(scenario_name)
        if scenario is None:
            continue
        if scenario.phase not in phases:
            requested_phases = ", ".join(sorted(phases))
            mismatches.append(
                f"{scenario.name} exists but is phase={scenario.phase}, not one of: {requested_phases}"
            )
    if mismatches:
        return "No benchmark scenarios matched the requested filters. " + " ; ".join(mismatches)
    return "No benchmark scenarios matched the requested filters."


def build_run_directory_name(timestamp: str, run_name: str) -> str:
    """Build the output directory name for one benchmark run."""
    sanitized = sanitize_run_name(run_name)
    if not sanitized:
        return timestamp
    return f"{sanitized}-{timestamp}"


def resolve_run_output_dir(
    *,
    output_root: Path,
    timestamp: str,
    run_name: str,
    scenario_name: str,
) -> Path:
    """Resolve the output folder for one scenario run."""
    sanitized_run_name = sanitize_run_name(run_name)
    if sanitized_run_name:
        return output_root / build_run_directory_name(timestamp, sanitized_run_name)
    return output_root / build_run_directory_name(timestamp, scenario_name)


def sanitize_run_name(run_name: str) -> str:
    """Sanitize a user-supplied benchmark run name for filesystem use."""
    cleaned = _RUN_NAME_RE.sub("-", run_name.strip())
    cleaned = cleaned.strip("-.")
    return cleaned


async def run_scenario(
    scenario: BenchmarkScenario,
    cases: tuple[BenchmarkCase, ...],
    *,
    show_output: bool = False,
) -> ScenarioResult:
    """Run one benchmark scenario with one shared loaded backend."""
    workspace = detect_workspace_context()
    context = ExtractionContext(
        cwd=Path(workspace.cwd),
        workspace_root=Path(workspace.workspace_root),
    )
    backend = create_local_backend(_local_model_config(scenario))
    torch_module = torch_module_or_none()
    try:
        print("  warmup starting: loading model and running one probe request")
        warmup = await _await_with_periodic_status(
            "warmup",
            _warmup_backend(
                backend=backend,
                scenario=scenario,
                torch_module=torch_module,
                context=context,
            ),
            prefix="  ",
        )
    except BackendUnavailableError as error:
        print(f"  scenario failed during warmup: {error}")
        return _failed_scenario_result(scenario, cases, str(error))
    print(
        f"  warmup load_ms={warmup.load_ms:.2f} "
        f"cpu_rss={_fmt_optional_bytes(warmup.cpu_rss_bytes)} "
        f"gpu_peak={_fmt_optional_bytes(warmup.gpu_peak_bytes)} "
        f"torch_threads={_fmt_optional_int(warmup.torch_num_threads)} "
        f"torch_interop={_fmt_optional_int(warmup.torch_num_interop_threads)} "
        f"OMP_NUM_THREADS={warmup.omp_num_threads or 'null'} "
        f"MKL_NUM_THREADS={warmup.mkl_num_threads or 'null'}"
    )
    semaphore = asyncio.Semaphore(max(1, scenario.concurrency))
    case_results: list[CaseMetrics] = []
    total_cases = len(cases)
    for case_index, case in enumerate(cases, start=1):
        _print_benchmark_line(
            f"    [{case_index}/{total_cases}] starting {case.case_id} "
            f"domain={case.domain} title={case.title}",
            color=_ANSI_BLUE,
        )
        result = await _await_with_periodic_status(
            f"case {case.case_id}",
            _run_case(
                case=case,
                backend=backend,
                scenario=scenario,
                context=context,
                semaphore=semaphore,
                torch_module=torch_module,
            ),
            prefix="    ",
        )
        case_results.append(result)
        _print_case_progress(result, case_index, total_cases, show_output=show_output)
    summary = _summarize(case_results)
    print(
        "  summary "
        f"success={summary.success_count}/{summary.case_count} "
        f"accepted={summary.accepted_count} "
        f"soft={summary.soft_accepted_count} "
        f"rejected={summary.rejected_count} "
        f"exact_pass={summary.exact_pass_count} "
        f"avg_ms={summary.avg_inference_ms:.2f} "
        f"p95_ms={summary.p95_inference_ms:.2f} "
        f"avg_preserve={summary.avg_exact_preservation_ratio:.3f} "
        f"avg_quality={summary.avg_summary_quality_ratio:.3f} "
        f"avg_format={summary.avg_format_adherence_score:.3f} "
        f"avg_instruction={summary.avg_instruction_following_score:.3f} "
        f"quality_core={summary.quality_core:.3f} "
        f"latency_factor={summary.latency_factor:.3f} "
        f"final_score={summary.final_score:.2f}"
    )
    return ScenarioResult(
        scenario=scenario,
        warmup=warmup,
        summary=summary,
        cases=tuple(case_results),
    )


def _local_model_config(scenario: BenchmarkScenario) -> LocalModelConfig:
    return LocalModelConfig(
        model=scenario.model,
        gguf_filename=scenario.gguf_filename,
        device=scenario.device,
        dtype=scenario.dtype,
        attn_implementation=scenario.attn_implementation,
        quantization=LocalQuantizationMode(scenario.quantization),
    )


async def _warmup_backend(
    *,
    backend: ModelBackend,
    scenario: BenchmarkScenario,
    torch_module: object | None,
    context: ExtractionContext,
) -> WarmupMetrics:
    request = _model_request(
        instruction="Summarize the failure for later recall.",
        raw_input="pytest failed in tests/test_auth.py::test_login\nE AuthError: invalid token",
        max_output_tokens=scenario.max_output_tokens,
        context=context,
    )
    reset_gpu_peak_memory(torch_module)
    started = time.perf_counter()
    await backend.preload()
    try:
        await backend.compress(request)
    except BackendUnavailableError as error:
        print(f"  warmup probe ignored error: {error}")
    elapsed_ms = (time.perf_counter() - started) * 1000
    return WarmupMetrics(
        load_ms=elapsed_ms,
        cpu_rss_bytes=current_process_rss_bytes(),
        gpu_peak_bytes=gpu_peak_memory_bytes(torch_module),
        torch_num_threads=torch_num_threads(torch_module),
        torch_num_interop_threads=torch_num_interop_threads(torch_module),
        omp_num_threads=thread_env_value("OMP_NUM_THREADS"),
        mkl_num_threads=thread_env_value("MKL_NUM_THREADS"),
    )


async def _run_case(
    *,
    case: BenchmarkCase,
    backend: ModelBackend,
    scenario: BenchmarkScenario,
    context: ExtractionContext,
    semaphore: asyncio.Semaphore,
    torch_module: object | None,
) -> CaseMetrics:
    async with semaphore:
        request = _model_request(
            instruction=case.instruction,
            raw_input=case.raw_input,
            max_output_tokens=scenario.max_output_tokens,
            context=context,
            required_anchors=case.anchor_tokens,
        )
        reset_gpu_peak_memory(torch_module)
        started = time.perf_counter()
        rejected_validation = None
        try:
            output = await backend.compress(request)
            error = None
        except ModelOutputRejectedError as rejected_error:
            output = ""
            error = str(rejected_error)
            rejected_validation = _rejected_validation_from_error(error)
        except BackendUnavailableError as backend_error:
            output = ""
            error = str(backend_error)
        validation = (
            rejected_validation
            if rejected_validation is not None
            else validate_instruction_aware_output(request, output)
        )
        elapsed_ms = (time.perf_counter() - started) * 1000
        missing = missing_tokens(output, case.anchor_tokens)
        preserve_ratio = exact_ratio(case.anchor_tokens, missing)
        quality_ratio = summary_quality_ratio(output, case.scoring_target, case.anchor_tokens)
        format_ratio = format_adherence_score(
            request,
            output,
            family=case.family,
            output_mode=case.output_mode,
            expected_output=case.scoring_target,
            format_check=case.judgement.format_check,
            pass_rule=case.judgement.pass_rule,
        )
        brevity = brevity_ratio(
            output,
            case.scoring_target,
            case.anchor_tokens,
            case.judgement.max_extra_tokens,
        )
        instruction_ratio = instruction_following_score(
            request,
            output,
            family=case.family,
            output_mode=case.output_mode,
            expected_output=case.scoring_target,
            required_anchors=case.anchor_tokens,
            format_check=case.judgement.format_check,
            pass_rule=case.judgement.pass_rule,
            max_extra_tokens=case.judgement.max_extra_tokens,
        )
        case_score = case_benchmark_score(
            validation_status=validation.status,
            family=case.family,
            anchor_score=preserve_ratio,
            semantic_score=quality_ratio,
            format_score=format_ratio,
            brevity_score=brevity,
        )
        return CaseMetrics(
            case_id=case.case_id,
            title=case.title,
            domain=case.domain,
            inference_ms=elapsed_ms,
            cpu_rss_bytes=current_process_rss_bytes(),
            gpu_peak_bytes=gpu_peak_memory_bytes(torch_module),
            output=output,
            exact_preservation_ratio=preserve_ratio,
            summary_quality_ratio=quality_ratio,
            format_adherence_score=format_ratio,
            instruction_following_score=instruction_ratio,
            validation_status=validation.status,
            validation_flags=validation_flags(validation),
            missing_tokens=missing,
            error=error,
            brevity_ratio=brevity,
            family=case.family,
            case_score=case_score,
        )


def _model_request(
    *,
    instruction: str,
    raw_input: str,
    max_output_tokens: int,
    context: ExtractionContext,
    required_anchors: tuple[str, ...] = (),
    evaluation_context: str = "benchmark",
) -> ModelCompressionInput:
    signal = extract_signal(raw_input, context)
    return ModelCompressionInput(
        instruction=instruction,
        raw_input=raw_input,
        extracted_signal=signal,
        max_output_tokens=max_output_tokens,
        required_anchors=required_anchors,
        evaluation_context=evaluation_context,
    )


def _rejected_validation_from_error(error: str):
    flags = _validation_flags_from_error(error)
    if not flags:
        return None
    statuses = _VALIDATION_STATUS_RE.findall(error)
    status = "rejected" if "rejected" in statuses else (statuses[-1] if statuses else "rejected")
    from ctxsift.models.text_profile_common import TextValidationResult

    return TextValidationResult(
        status=status,
        hard_fail_reasons=tuple(flags),
        quality_flags=(),
        anchor_hits=0,
    )


def _validation_flags_from_error(error: str) -> tuple[str, ...]:
    flags: list[str] = []
    seen: set[str] = set()
    for raw_list in _VALIDATION_FLAGS_RE.findall(error):
        try:
            parsed = ast.literal_eval(raw_list)
        except (SyntaxError, ValueError):
            continue
        if not isinstance(parsed, list):
            continue
        for item in parsed:
            if not isinstance(item, str) or item in seen:
                continue
            seen.add(item)
            flags.append(item)
    return tuple(flags)


def _summarize(cases: list[CaseMetrics]) -> ScenarioSummary:
    case_count = len(cases)
    success_cases = [case for case in cases if case.error is None]
    accepted_cases = [case for case in cases if case.validation_status == "accepted"]
    soft_accepted_cases = [case for case in cases if case.validation_status == "soft_accepted"]
    rejected_cases = [case for case in cases if case.validation_status == "rejected"]
    inference_times = [case.inference_ms for case in success_cases]
    exact_scores = [case.exact_preservation_ratio for case in cases]
    quality_scores = [case.summary_quality_ratio for case in cases]
    format_scores = [case.format_adherence_score for case in cases]
    instruction_scores = [case.instruction_following_score for case in cases]
    brevity_scores = [case.brevity_ratio for case in cases]
    case_scores = [case.case_score for case in cases]
    success_count = len(success_cases)
    avg_inference_ms = mean(inference_times) if inference_times else 0.0
    p95_inference_ms = percentile(inference_times, 0.95)
    avg_exact_preservation_ratio = mean(exact_scores) if exact_scores else 0.0
    avg_summary_quality_ratio = mean(quality_scores) if quality_scores else 0.0
    avg_format_adherence_score = mean(format_scores) if format_scores else 0.0
    avg_instruction_following_score = mean(instruction_scores) if instruction_scores else 0.0
    avg_brevity_ratio = mean(brevity_scores) if brevity_scores else 0.0
    avg_case_score = mean(case_scores) if case_scores else 0.0
    p10_case_score = percentile(case_scores, 0.10)
    quality_core = quality_core_score(case_scores)
    latency_factor = latency_factor_score(avg_inference_ms) if inference_times else 0.85
    peak_cpu = _max_optional(case.cpu_rss_bytes for case in cases)
    peak_gpu = _max_optional(case.gpu_peak_bytes for case in cases)
    return ScenarioSummary(
        case_count=case_count,
        success_count=success_count,
        accepted_count=len(accepted_cases),
        soft_accepted_count=len(soft_accepted_cases),
        rejected_count=len(rejected_cases),
        exact_pass_count=sum(1 for case in cases if case.exact_preservation_ratio == 1.0),
        avg_inference_ms=avg_inference_ms,
        p95_inference_ms=p95_inference_ms,
        avg_exact_preservation_ratio=avg_exact_preservation_ratio,
        avg_summary_quality_ratio=avg_summary_quality_ratio,
        avg_format_adherence_score=avg_format_adherence_score,
        avg_instruction_following_score=avg_instruction_following_score,
        avg_brevity_ratio=avg_brevity_ratio,
        avg_case_score=avg_case_score,
        p10_case_score=p10_case_score,
        quality_core=quality_core,
        latency_factor=latency_factor,
        final_score=final_benchmark_score(
            case_count=case_count,
            success_count=success_count,
            case_scores=case_scores,
            observed_latency_ms=avg_inference_ms,
        ),
        peak_cpu_rss_bytes=peak_cpu,
        peak_gpu_bytes=peak_gpu,
    )


def _failed_scenario_result(
    scenario: BenchmarkScenario,
    cases: tuple[BenchmarkCase, ...],
    error: str,
) -> ScenarioResult:
    case_results = tuple(
        CaseMetrics(
            case_id=case.case_id,
            title=case.title,
            domain=case.domain,
            inference_ms=0.0,
            cpu_rss_bytes=current_process_rss_bytes(),
            gpu_peak_bytes=None,
            output="",
            exact_preservation_ratio=0.0,
            summary_quality_ratio=0.0,
            format_adherence_score=0.0,
            instruction_following_score=0.0,
            validation_status="rejected",
            validation_flags=("warmup_failed",),
            missing_tokens=case.anchor_tokens,
            error=error,
            brevity_ratio=0.0,
            family=case.family,
            case_score=0.0,
        )
        for case in cases
    )
    summary = ScenarioSummary(
        case_count=len(cases),
        success_count=0,
        accepted_count=0,
        soft_accepted_count=0,
        rejected_count=len(cases),
        exact_pass_count=0,
        avg_inference_ms=0.0,
        p95_inference_ms=0.0,
        avg_exact_preservation_ratio=0.0,
        avg_summary_quality_ratio=0.0,
        avg_format_adherence_score=0.0,
        avg_instruction_following_score=0.0,
        avg_brevity_ratio=0.0,
        avg_case_score=0.0,
        p10_case_score=0.0,
        quality_core=0.0,
        latency_factor=0.85,
        final_score=0.0,
        peak_cpu_rss_bytes=current_process_rss_bytes(),
        peak_gpu_bytes=None,
    )
    return ScenarioResult(
        scenario=scenario,
        warmup=WarmupMetrics(
            load_ms=0.0,
            cpu_rss_bytes=current_process_rss_bytes(),
            gpu_peak_bytes=None,
            torch_num_threads=torch_num_threads(torch_module_or_none()),
            torch_num_interop_threads=torch_num_interop_threads(torch_module_or_none()),
            omp_num_threads=thread_env_value("OMP_NUM_THREADS"),
            mkl_num_threads=thread_env_value("MKL_NUM_THREADS"),
        ),
        summary=summary,
        cases=case_results,
    )


def _max_optional(values: Iterable[int | None]) -> int | None:
    filtered = [value for value in values if value is not None]
    return max(filtered) if filtered else None


def _print_case_progress(
    result: CaseMetrics,
    case_index: int,
    total_cases: int,
    *,
    show_output: bool,
) -> None:
    status = "ok" if result.error is None else "error"
    _print_benchmark_line(
        f"    [{case_index}/{total_cases}] {result.case_id} {status} "
        f"ms={result.inference_ms:.2f} preserve={result.exact_preservation_ratio:.3f} "
        f"quality={result.summary_quality_ratio:.3f} instruction={result.instruction_following_score:.3f} "
        f"format={result.format_adherence_score:.3f} case_score={result.case_score:.3f} "
        f"validation={result.validation_status} "
        f"cpu_rss={_fmt_optional_bytes(result.cpu_rss_bytes)} "
        f"gpu_peak={_fmt_optional_bytes(result.gpu_peak_bytes)} "
        f"remaining={total_cases - case_index}",
        color=_ANSI_GREEN if result.error is None else _ANSI_RED,
    )
    if result.error is not None:
        print(f"      error: {result.error}")
        return
    if show_output:
        print(f"      title: {result.title}")
        print(f"      domain: {result.domain}")
        if result.validation_flags:
            print(f"      validation_flags: {', '.join(result.validation_flags)}")
        if result.missing_tokens:
            print(f"      missing_tokens: {', '.join(result.missing_tokens)}")
        print(f"      output: {result.output}")


async def _await_with_periodic_status(
    label: str,
    awaitable: Awaitable[_AwaitableResult],
    *,
    prefix: str,
    interval_seconds: float = 5.0,
) -> _AwaitableResult:
    task = asyncio.create_task(awaitable)
    started = time.perf_counter()
    while True:
        try:
            return await asyncio.wait_for(asyncio.shield(task), timeout=interval_seconds)
        except asyncio.TimeoutError:
            elapsed_seconds = time.perf_counter() - started
            print(f"{prefix}{label} still running... elapsed={elapsed_seconds:.1f}s")


def _fmt_optional_bytes(value: int | None) -> str:
    if value is None:
        return "null"
    return f"{value / (1024 * 1024):.1f} MiB"


def _fmt_optional_int(value: int | None) -> str:
    return "null" if value is None else str(value)


def _print_benchmark_line(message: str, *, color: str | None = None) -> None:
    if not color or not _supports_ansi_color():
        print(message)
        return
    print(f"{color}{message}{_ANSI_RESET}")


def _supports_ansi_color() -> bool:
    if os.getenv("NO_COLOR"):
        return False
    stream = sys.stdout
    is_a_tty = getattr(stream, "isatty", None)
    return bool(is_a_tty and is_a_tty())


def _print_scenarios(scenarios: list[BenchmarkScenario]) -> None:
    print(f"Available scenarios: {len(scenarios)}")
    for scenario in scenarios:
        print(
            f"- {scenario.name} | phase={scenario.phase} | track={scenario.track} | "
            f"model={scenario.model} | quant={scenario.quantization} | device={scenario.device}"
        )


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
