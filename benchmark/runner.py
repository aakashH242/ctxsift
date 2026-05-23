"""Benchmark runner for local compression model scenarios."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import replace
from datetime import UTC, datetime
import ast
import os
from pathlib import Path
import re
from statistics import mean
import sys
import time
from typing import Awaitable, Iterable, Literal, Mapping, TypeVar, cast

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
from benchmark.semantic_quality import build_semantic_scorer
from benchmark.schemas import (
    BenchmarkCase,
    BenchmarkScenario,
    CaseMetrics,
    ScenarioResult,
    ScenarioSummary,
    WarmupMetrics,
)
from benchmark.stats import percentile
from ctxsift.compression.intent import CompressionIntent
from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.extraction import ExtractionContext, extract_signal
from ctxsift.models import create_compression_backend, create_local_backend
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
from ctxsift.types import AppConfig, LocalModelConfig, LocalQuantizationMode
from ctxsift.workspace import detect_workspace_context


_AwaitableResult = TypeVar("_AwaitableResult")
_RUN_NAME_RE = re.compile(r"[^A-Za-z0-9._-]+")
_VALIDATION_STATUS_RE = re.compile(
    r"\b(?:first_pass_status|repair_status)=(accepted|soft_accepted|rejected)\b"
)
_VALIDATION_FLAGS_RE = re.compile(r"\b(?:first_pass_flags|repair_flags)=(\[[^\]]*\])")
_ANSI_RESET = "\x1b[0m"
_ANSI_BLUE = "\x1b[34m"
_ANSI_GREEN = "\x1b[32m"
_ANSI_RED = "\x1b[31m"


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for benchmark execution."""
    parser = argparse.ArgumentParser(description="Run ctxsift model benchmarks.")
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
        help=(
            "Run only scenarios from the named phase. Can be passed multiple times. "
            "With --remote, synthesized scenarios use phase=remote-screen."
        ),
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
    parser.add_argument(
        "--remote",
        action="store_true",
        help="Run the benchmark against the configured remote LiteLLM backend instead of local models.",
    )
    parser.add_argument(
        "--env-file",
        default=".env",
        help="Env file to load before resolving remote benchmark config. Used only with --remote.",
    )
    return parser


async def main() -> int:
    """Run the configured benchmark scenarios."""
    parser = build_parser()
    args = parser.parse_args()
    manifest = load_manifest(Path(args.dataset), Path(args.matrix))
    requested_names = set(args.scenario)
    requested_phases = set(args.phase)
    remote_enabled = _should_enable_remote_mode(
        manifest.scenarios,
        remote_requested=args.remote,
        names=requested_names,
        phases=requested_phases,
    )
    remote_config = _remote_listing_config(manifest.scenarios, remote_enabled, args.list_scenarios)
    if remote_config is None:
        remote_config = _resolve_remote_benchmark_config(
            env_file=Path(args.env_file),
            enabled=remote_enabled,
        )
    scenarios_for_mode = _scenarios_for_mode(
        manifest.scenarios,
        remote_config=remote_config,
    )
    cases = select_cases(
        manifest.cases,
        case_ids=set(args.case_id),
        max_cases=args.max_cases,
    )
    scenarios = select_scenarios(
        scenarios_for_mode,
        names=requested_names,
        phases=requested_phases,
    )
    if args.list_scenarios:
        _print_scenarios(scenarios)
        return 0
    if not scenarios:
        parser.error(
            build_scenario_filter_error(
                scenarios_for_mode,
                names=requested_names,
                phases=requested_phases,
            )
        )
    if not cases:
        parser.error("No benchmark cases matched the requested filters.")
    semantic_scorer = build_semantic_scorer(_benchmark_embedding_config(remote_config))
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_root = Path(args.output_dir)
    named_run_output_dir = output_root / build_run_directory_name(timestamp, args.name)
    total_scenarios = len(scenarios)
    output_label = (
        str(named_run_output_dir) if args.name.strip() else f"{output_root} (per-scenario folders)"
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
            remote_config=remote_config,
            semantic_scorer=semantic_scorer,
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
    remote_config: AppConfig | None = None,
    semantic_scorer=None,
) -> ScenarioResult:
    """Run one benchmark scenario with one shared loaded backend."""
    workspace = detect_workspace_context()
    context = ExtractionContext(
        cwd=Path(workspace.cwd),
        workspace_root=Path(workspace.workspace_root),
    )
    backend = _create_benchmark_backend(scenario, remote_config)
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
    case_results = await _run_scenario_cases(
        scenario=scenario,
        cases=cases,
        backend=backend,
        context=context,
        torch_module=torch_module,
        show_output=show_output,
    )
    case_results = await _apply_semantic_quality_scores(
        cases=cases,
        case_results=case_results,
        semantic_scorer=semantic_scorer,
    )
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


def _create_benchmark_backend(
    scenario: BenchmarkScenario,
    remote_config: AppConfig | None,
) -> ModelBackend:
    if remote_config is not None:
        return create_compression_backend(_remote_config_for_scenario(remote_config, scenario))
    return create_local_backend(_local_model_config(scenario))


async def _run_scenario_cases(
    *,
    scenario: BenchmarkScenario,
    cases: tuple[BenchmarkCase, ...],
    backend: ModelBackend,
    context: ExtractionContext,
    torch_module: object | None,
    show_output: bool,
) -> list[CaseMetrics]:
    if _is_remote_scenario(scenario):
        return await _run_cases_concurrently(
            scenario=scenario,
            cases=cases,
            backend=backend,
            context=context,
            torch_module=torch_module,
            show_output=show_output,
            concurrency=16,
        )
    return await _run_cases_sequentially(
        scenario=scenario,
        cases=cases,
        backend=backend,
        context=context,
        torch_module=torch_module,
        show_output=show_output,
        concurrency=max(1, scenario.concurrency),
    )


async def _run_cases_sequentially(
    *,
    scenario: BenchmarkScenario,
    cases: tuple[BenchmarkCase, ...],
    backend: ModelBackend,
    context: ExtractionContext,
    torch_module: object | None,
    show_output: bool,
    concurrency: int,
) -> list[CaseMetrics]:
    semaphore = asyncio.Semaphore(concurrency)
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
    return case_results


async def _run_cases_concurrently(
    *,
    scenario: BenchmarkScenario,
    cases: tuple[BenchmarkCase, ...],
    backend: ModelBackend,
    context: ExtractionContext,
    torch_module: object | None,
    show_output: bool,
    concurrency: int,
) -> list[CaseMetrics]:
    total_cases = len(cases)
    _print_benchmark_line(
        f"    starting {total_cases} remote case(s) with concurrency={concurrency}",
        color=_ANSI_BLUE,
    )
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [
        asyncio.create_task(
            _run_indexed_case(
                index=index,
                case=case,
                backend=backend,
                scenario=scenario,
                context=context,
                semaphore=semaphore,
                torch_module=torch_module,
            )
        )
        for index, case in enumerate(cases, start=1)
    ]
    indexed_results = await _await_with_periodic_status(
        "remote case batch",
        asyncio.gather(*tasks),
        prefix="    ",
    )
    ordered = sorted(indexed_results, key=lambda item: item[0])
    case_results = [result for _, result in ordered]
    _print_remote_backend_error_summary(case_results)
    for case_index, result in enumerate(case_results, start=1):
        _print_case_progress(result, case_index, total_cases, show_output=show_output)
    return case_results


async def _run_indexed_case(
    *,
    index: int,
    case: BenchmarkCase,
    backend: ModelBackend,
    scenario: BenchmarkScenario,
    context: ExtractionContext,
    semaphore: asyncio.Semaphore,
    torch_module: object | None,
) -> tuple[int, CaseMetrics]:
    return (
        index,
        await _run_case(
            case=case,
            backend=backend,
            scenario=scenario,
            context=context,
            semaphore=semaphore,
            torch_module=torch_module,
        ),
    )


def _resolve_remote_benchmark_config(
    *,
    env_file: Path,
    enabled: bool,
) -> AppConfig | None:
    if not enabled:
        return None
    merged_env = dict(_load_env_file(env_file))
    merged_env.update(os.environ)
    resolved = resolve_config(
        ConfigResolutionRequest(
            cwd=Path.cwd(),
            env=merged_env,
        )
    )
    config = resolved.config
    if not config.remote.base_url.strip():
        raise SystemExit(
            "Remote benchmark mode requires remote.base_url. "
            f"Set CTXSIFT_LLM_BASE_URL in {env_file} or the current environment."
        )
    if not config.remote.model_name.strip():
        raise SystemExit(
            "Remote benchmark mode requires remote.model_name. "
            f"Set CTXSIFT_LLM_MODEL in {env_file} or the current environment."
        )
    return config


def _load_env_file(env_file: Path) -> Mapping[str, str]:
    if not env_file.exists():
        return {}
    values: dict[str, str] = {}
    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            continue
        values[key] = _parse_env_value(value.strip())
    return values


def _parse_env_value(value: str) -> str:
    if not value:
        return ""
    if value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _remote_benchmark_scenario(
    scenario: BenchmarkScenario,
    config: AppConfig | None,
) -> BenchmarkScenario:
    if config is None:
        return scenario
    model_name = scenario.model if _is_remote_scenario(scenario) else config.remote.model_name
    phase = scenario.phase if _is_remote_scenario(scenario) else "remote-screen"
    track = scenario.track if _is_remote_scenario(scenario) else "remote"
    return BenchmarkScenario(
        name=scenario.name,
        track=track,
        phase=phase,
        model=model_name,
        quantization="none",
        device="remote",
        gguf_filename=None,
        dtype="remote",
        attn_implementation="remote",
        max_output_tokens=scenario.max_output_tokens,
        concurrency=scenario.concurrency,
        enabled=scenario.enabled,
    )


def _should_enable_remote_mode(
    scenarios: tuple[BenchmarkScenario, ...],
    *,
    remote_requested: bool,
    names: set[str],
    phases: set[str],
) -> bool:
    if remote_requested:
        return True
    selected = select_scenarios(scenarios, names=names, phases=phases)
    if not selected:
        return False
    return all(_is_remote_scenario(scenario) for scenario in selected)


def _scenarios_for_mode(
    scenarios: tuple[BenchmarkScenario, ...],
    *,
    remote_config: AppConfig | None,
) -> tuple[BenchmarkScenario, ...]:
    if remote_config is None:
        return scenarios
    explicit_remote = tuple(scenario for scenario in scenarios if _is_remote_scenario(scenario))
    source = explicit_remote or scenarios
    return tuple(_remote_benchmark_scenario(scenario, remote_config) for scenario in source)


def _is_remote_scenario(scenario: BenchmarkScenario) -> bool:
    normalized = " ".join(
        [
            scenario.track.strip().casefold(),
            scenario.phase.strip().casefold(),
            scenario.device.strip().casefold(),
        ]
    )
    return "remote" in normalized


def _remote_config_for_scenario(
    config: AppConfig,
    scenario: BenchmarkScenario,
) -> AppConfig:
    remote = config.remote.model_copy(update={"model_name": scenario.model})
    return config.model_copy(update={"remote": remote})


def _benchmark_embedding_config(remote_config: AppConfig | None):
    if remote_config is not None:
        return remote_config.embedding
    resolved = resolve_config(ConfigResolutionRequest(cwd=Path.cwd(), env=os.environ))
    return resolved.config.embedding


def _remote_listing_config(
    scenarios: tuple[BenchmarkScenario, ...],
    remote_enabled: bool,
    list_scenarios: bool,
) -> AppConfig | None:
    if not (remote_enabled and list_scenarios):
        return None
    if not any(_is_remote_scenario(scenario) for scenario in scenarios):
        return None
    return AppConfig()


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
        family="recall",
        output_mode="plain_text",
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
            family=case.family,
            output_mode=case.output_mode,
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
            instruction=case.instruction,
            expected_output=case.scoring_target,
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


async def _apply_semantic_quality_scores(
    *,
    cases: tuple[BenchmarkCase, ...],
    case_results: list[CaseMetrics],
    semantic_scorer,
) -> list[CaseMetrics]:
    if semantic_scorer is None or not case_results:
        return case_results
    semantic_scores = await semantic_scorer.score_cases(
        cases,
        [case_result.output for case_result in case_results],
    )
    updated_results: list[CaseMetrics] = []
    for benchmark_case, case_result, semantic_score in zip(
        cases,
        case_results,
        semantic_scores,
        strict=True,
    ):
        updated_results.append(
            replace(
                case_result,
                summary_quality_ratio=semantic_score,
                case_score=case_benchmark_score(
                    validation_status=case_result.validation_status,
                    family=benchmark_case.family,
                    anchor_score=case_result.exact_preservation_ratio,
                    semantic_score=semantic_score,
                    format_score=case_result.format_adherence_score,
                    brevity_score=case_result.brevity_ratio,
                ),
            )
        )
    return updated_results


def _model_request(
    *,
    instruction: str,
    raw_input: str,
    max_output_tokens: int,
    context: ExtractionContext,
    family: str = "summary",
    output_mode: str = "plain_text",
    required_anchors: tuple[str, ...] = (),
    evaluation_context: Literal["benchmark"] = "benchmark",
) -> ModelCompressionInput:
    signal = extract_signal(raw_input, context)
    return ModelCompressionInput(
        intent=_benchmark_intent(
            family=family,
            output_mode=output_mode,
            instruction=instruction,
        ),
        instruction=instruction,
        raw_input=raw_input,
        extracted_signal=signal,
        max_output_tokens=max_output_tokens,
        required_anchors=required_anchors,
        evaluation_context=evaluation_context,
    )


def _benchmark_intent(
    *,
    family: str,
    output_mode: str,
    instruction: str,
) -> CompressionIntent:
    normalized_output_mode = output_mode.strip().casefold().replace("_", "-")
    if normalized_output_mode == "json":
        return CompressionIntent.JSON
    if normalized_output_mode == "yaml":
        return CompressionIntent.YAML
    if normalized_output_mode == "table":
        return CompressionIntent.TABLE
    if normalized_output_mode == "bullet-list":
        return CompressionIntent.BULLET_LIST
    if normalized_output_mode == "exact-lines":
        return CompressionIntent.EXACT_LINES
    if normalized_output_mode in {"regex-constrained", "single-line"}:
        return CompressionIntent.EXACT_FORMAT
    if family == "recall":
        return CompressionIntent.RECALL

    normalized = instruction.casefold()
    if any(token in normalized for token in ("json", "valid json only")):
        return CompressionIntent.JSON
    if "yaml" in normalized:
        return CompressionIntent.YAML
    if "table" in normalized:
        return CompressionIntent.TABLE
    if "bullet" in normalized or "bullets" in normalized:
        return CompressionIntent.BULLET_LIST
    if any(
        token in normalized
        for token in (
            "quote exactly",
            "verbatim",
            "exact lines",
            "exact line",
            "copy the lines",
            "extract the lines",
        )
    ):
        return CompressionIntent.EXACT_LINES
    if any(
        token in normalized
        for token in (
            "return only",
            "output only",
            "single line",
            "exact match",
            "regex-constrained",
            "no prose, bullets, backticks, or extra whitespace",
        )
    ):
        return CompressionIntent.EXACT_FORMAT
    if "recall" in normalized:
        return CompressionIntent.RECALL
    return CompressionIntent.SUMMARY


def _rejected_validation_from_error(error: str):
    flags = _validation_flags_from_error(error)
    if not flags:
        return None
    statuses = _VALIDATION_STATUS_RE.findall(error)
    status = cast(
        Literal["accepted", "soft_accepted", "rejected"],
        "rejected" if "rejected" in statuses else (statuses[-1] if statuses else "rejected"),
    )
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


def _print_remote_backend_error_summary(case_results: list[CaseMetrics]) -> None:
    error_counts: dict[str, int] = {}
    for case_result in case_results:
        if not case_result.error:
            continue
        if "LiteLLM remote backend request failed:" not in case_result.error:
            continue
        error_counts[case_result.error] = error_counts.get(case_result.error, 0) + 1
    if not error_counts:
        return
    unique_error_count = len(error_counts)
    total_error_count = sum(error_counts.values())
    _print_benchmark_line(
        f"    remote backend errors: {total_error_count} case(s), {unique_error_count} unique",
        color=_ANSI_RED,
    )
    for error, count in sorted(
        error_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )[:3]:
        _print_benchmark_line(
            f"      x{count} {_preview_error_text(error)}",
            color=_ANSI_RED,
        )
    if unique_error_count > 3:
        _print_benchmark_line(
            f"      ... {unique_error_count - 3} more unique remote backend error(s)",
            color=_ANSI_RED,
        )


def _preview_error_text(error: str, limit: int = 220) -> str:
    normalized = " ".join(error.split())
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 3] + "..."


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
            instruction=case.instruction,
            expected_output=case.scoring_target,
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
    task = asyncio.ensure_future(awaitable)
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
