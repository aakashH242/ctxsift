"""Tests for benchmark dataset loading and report writing."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.loader import load_cases, load_scenarios
from benchmark.report import render_markdown_report
from benchmark.scoring import (
    brevity_ratio,
    final_benchmark_score,
    instruction_following_score,
    summary_quality_ratio,
)
from benchmark.runner import (
    _ANSI_BLUE,
    _ANSI_GREEN,
    _should_enable_remote_mode,
    _warmup_backend,
    _print_benchmark_line,
    _print_case_progress,
    build_scenario_filter_error,
    build_run_directory_name,
    sanitize_run_name,
    select_scenarios,
)
from benchmark.schemas import (
    BenchmarkScenario,
    CaseMetrics,
    ScenarioResult,
    ScenarioSummary,
    WarmupMetrics,
)
from benchmark.viewer import LoadedResult, render_html_report
from ctxsift.compression.intent import CompressionIntent
from ctxsift.extraction import ExtractionContext
from ctxsift.models.base import (
    BackendUnavailableError,
    ModelBackend,
    ModelCompressionInput,
    ModelOutputRejectedError,
)
from ctxsift.types import ExtractedSignal


class _ProbeFailingBackend(ModelBackend):
    provider_name = "test"
    model_name = "probe-failing"

    def __init__(self) -> None:
        self.preload_calls = 0
        self.compress_calls = 0

    @property
    def cache_model_id(self) -> str:
        return self.model_name

    async def preload(self) -> None:
        self.preload_calls += 1

    async def compress(self, request: ModelCompressionInput) -> str:
        del request
        self.compress_calls += 1
        raise ModelOutputRejectedError("fallback output validation failed")


class _PreloadFailingBackend(ModelBackend):
    provider_name = "test"
    model_name = "preload-failing"

    @property
    def cache_model_id(self) -> str:
        return self.model_name

    async def preload(self) -> None:
        raise BackendUnavailableError("could not load test backend")

    async def compress(self, request: ModelCompressionInput) -> str:
        del request
        raise AssertionError("compress should not run after preload failure")


def test_load_cases_reads_starter_dataset() -> None:
    dataset_path = Path("benchmark/dataset.jsonl")
    cases = load_cases(dataset_path)

    assert len(cases) >= 10
    assert cases[0].case_id == "python-01"
    assert len(cases[0].must_preserve_tokens) >= 3
    assert cases[0].domain == "python"


def test_load_scenarios_reads_matrix() -> None:
    matrix_path = Path("benchmark/matrix.json")
    scenarios = load_scenarios(matrix_path)

    assert any(scenario.name == "cpu-smollm2-360m-no-quant" for scenario in scenarios)
    assert any(scenario.name == "gpu-qwen3-1.7b-no-quant" for scenario in scenarios)
    assert any(scenario.phase == "gpu-screen" for scenario in scenarios)


def test_select_scenarios_filters_by_name_and_phase() -> None:
    scenarios = (
        BenchmarkScenario(
            name="cpu-a",
            track="cpu",
            phase="cpu-screen",
            model="a",
            quantization="none",
            device="cpu",
        ),
        BenchmarkScenario(
            name="gpu-b",
            track="gpu",
            phase="gpu-screen",
            model="b",
            quantization="none",
            device="cuda",
        ),
    )

    selected = select_scenarios(scenarios, names={"gpu-b"}, phases=set())
    assert [scenario.name for scenario in selected] == ["gpu-b"]

    selected = select_scenarios(scenarios, names=set(), phases={"cpu-screen"})
    assert [scenario.name for scenario in selected] == ["cpu-a"]


def test_should_enable_remote_mode_for_remote_phase_selection() -> None:
    scenarios = (
        BenchmarkScenario(
            name="cpu-a",
            track="cpu",
            phase="cpu-screen",
            model="a",
            quantization="none",
            device="cpu",
        ),
        BenchmarkScenario(
            name="remote-b",
            track="remote",
            phase="remote-screen",
            model="b",
            quantization="none",
            device="remote",
        ),
    )

    assert (
        _should_enable_remote_mode(
            scenarios,
            remote_requested=False,
            names=set(),
            phases={"remote-screen"},
        )
        is True
    )


def test_should_enable_remote_mode_for_remote_named_selection() -> None:
    scenarios = (
        BenchmarkScenario(
            name="cpu-a",
            track="cpu",
            phase="cpu-screen",
            model="a",
            quantization="none",
            device="cpu",
        ),
        BenchmarkScenario(
            name="remote-b",
            track="remote",
            phase="remote-screen",
            model="b",
            quantization="none",
            device="remote",
        ),
    )

    assert (
        _should_enable_remote_mode(
            scenarios,
            remote_requested=False,
            names={"remote-b"},
            phases=set(),
        )
        is True
    )


def test_should_not_enable_remote_mode_for_mixed_or_local_selection() -> None:
    scenarios = (
        BenchmarkScenario(
            name="cpu-a",
            track="cpu",
            phase="cpu-screen",
            model="a",
            quantization="none",
            device="cpu",
        ),
        BenchmarkScenario(
            name="remote-b",
            track="remote",
            phase="remote-screen",
            model="b",
            quantization="none",
            device="remote",
        ),
    )

    assert (
        _should_enable_remote_mode(
            scenarios,
            remote_requested=False,
            names=set(),
            phases={"cpu-screen"},
        )
        is False
    )
    assert (
        _should_enable_remote_mode(
            scenarios,
            remote_requested=False,
            names={"cpu-a", "remote-b"},
            phases=set(),
        )
        is False
    )


def test_build_scenario_filter_error_reports_phase_mismatch() -> None:
    scenarios = (
        BenchmarkScenario(
            name="gpu-qwen3.5-2b-no-quant",
            track="gpu",
            phase="gpu-second-wave",
            model="Qwen/Qwen3.5-2B",
            quantization="none",
            device="cuda",
        ),
    )

    message = build_scenario_filter_error(
        scenarios,
        names={"gpu-qwen3.5-2b-no-quant"},
        phases={"gpu-screen"},
    )

    assert "gpu-qwen3.5-2b-no-quant exists but is phase=gpu-second-wave" in message
    assert "gpu-screen" in message


def test_build_scenario_filter_error_reports_missing_named_scenario() -> None:
    scenarios = (
        BenchmarkScenario(
            name="cpu-a",
            track="cpu",
            phase="cpu-screen",
            model="a",
            quantization="none",
            device="cpu",
        ),
    )

    message = build_scenario_filter_error(
        scenarios,
        names={"missing-scenario"},
        phases=set(),
    )

    assert message == "No benchmark scenarios matched the requested names: missing-scenario."


def test_render_markdown_report_includes_summary_and_case_rows() -> None:
    scenario = BenchmarkScenario(
        name="cpu-qwen-test",
        track="cpu",
        phase="cpu-screen",
        model="ibm-granite/granite-4.0-350m-GGUF",
        gguf_filename="smollm2-360m-instruct-q8_0.gguf",
        quantization="none",
        device="cpu",
    )
    result = ScenarioResult(
        scenario=scenario,
        warmup=WarmupMetrics(
            load_ms=100.0,
            cpu_rss_bytes=1234,
            gpu_peak_bytes=None,
            torch_num_threads=8,
            torch_num_interop_threads=2,
            omp_num_threads="8",
            mkl_num_threads="8",
        ),
        summary=ScenarioSummary(
            case_count=1,
            success_count=1,
            accepted_count=1,
            soft_accepted_count=0,
            rejected_count=0,
            exact_pass_count=1,
            avg_inference_ms=42.0,
            p95_inference_ms=42.0,
            avg_exact_preservation_ratio=1.0,
            avg_summary_quality_ratio=1.0,
            avg_instruction_following_score=1.0,
            avg_brevity_ratio=1.0,
            final_score=95.99,
            peak_cpu_rss_bytes=1234,
            peak_gpu_bytes=None,
        ),
        cases=(
            CaseMetrics(
                case_id="python-traceback-01",
                title="traceback",
                domain="python",
                instruction="Summarize the traceback.",
                expected_output="AuthError in src/auth.py line 42.",
                inference_ms=42.0,
                cpu_rss_bytes=1234,
                gpu_peak_bytes=None,
                output="AuthError in src/auth.py line 42.",
                exact_preservation_ratio=1.0,
                summary_quality_ratio=1.0,
                instruction_following_score=1.0,
                validation_status="accepted",
                validation_flags=(),
                missing_tokens=(),
                brevity_ratio=1.0,
            ),
        ),
    )

    report = render_markdown_report(result)

    assert "# cpu-qwen-test" in report
    assert "avg_inference_ms" in report
    assert "avg_summary_quality_ratio" in report
    assert "final_score" in report
    assert "torch_num_threads" in report
    assert "`python-traceback-01`" in report
    assert result.to_dict()["summary"]["final_score"] == 95.99


def test_summary_quality_ratio_penalizes_anchor_only_output() -> None:
    ideal_summary = (
        "pytest tests/api/test_users.py -q failed in "
        "tests/api/test_users.py::test_create_user_rejects_duplicate[email]; "
        "tests/api/test_users.py:47 raised AssertionError with 500 == 409."
    )
    exact_tokens = (
        "pytest tests/api/test_users.py -q",
        "tests/api/test_users.py::test_create_user_rejects_duplicate[email]",
        "tests/api/test_users.py:47",
        "AssertionError",
        "500 == 409",
    )
    anchor_only_output = (
        "pytest tests/api/test_users.py -q "
        "tests/api/test_users.py::test_create_user_rejects_duplicate[email] "
        "tests/api/test_users.py:47 AssertionError 500 == 409"
    )

    assert summary_quality_ratio(anchor_only_output, ideal_summary, exact_tokens) == 0.0
    assert summary_quality_ratio(ideal_summary, ideal_summary, exact_tokens) == 1.0


def test_brevity_ratio_penalizes_excess_residual_tokens() -> None:
    exact_tokens = ("python app.py", "ValueError")
    expected_output = "python app.py failed with ValueError in settings loader."
    verbose_output = (
        "python app.py failed with ValueError in settings loader. "
        "This adds many extra retrieval-irrelevant filler tokens beyond the allowed budget "
        "and keeps rambling after the useful summary is already complete."
    )

    assert brevity_ratio(expected_output, expected_output, exact_tokens, 16) == 1.0
    assert brevity_ratio(verbose_output, expected_output, exact_tokens, 4) < 1.0


def test_instruction_following_score_respects_output_modes() -> None:
    plain_request = ModelCompressionInput(
        intent=CompressionIntent.RECALL,
        instruction="Return a concise plain-text recall summary.",
        raw_input="alpha\nbeta\ngamma",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )
    structured_request = ModelCompressionInput(
        intent=CompressionIntent.BULLET_LIST,
        instruction="Return a bullet list for later recall.",
        raw_input="alpha\nbeta\ngamma",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )
    exact_request = ModelCompressionInput(
        intent=CompressionIntent.EXACT_LINES,
        instruction="Quote the first 2 lines exactly.",
        raw_input="alpha\nbeta\ngamma",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )

    assert instruction_following_score(plain_request, "short plain summary") == 1.0
    assert instruction_following_score(plain_request, "- short\n- plain") == 0.5
    assert instruction_following_score(structured_request, "- alpha\n- beta") == 1.0
    assert instruction_following_score(structured_request, "alpha beta") == 0.0
    assert instruction_following_score(exact_request, "alpha\nbeta") == 1.0
    assert instruction_following_score(exact_request, "alpha\nparaphrased beta") == 0.5
    assert instruction_following_score(exact_request, "paraphrase only") == 0.0
    assert (
        instruction_following_score(
            plain_request,
            "short plain summary with too many extra tokens appended after the useful answer",
            output_mode="plain_text",
            expected_output="short plain summary",
            required_anchors=(),
            max_extra_tokens=2,
        )
        < 1.0
    )


def test_final_benchmark_score_prioritizes_preservation_and_instruction() -> None:
    robust_score = final_benchmark_score(
        case_count=10,
        success_count=10,
        avg_exact_preservation_ratio=0.95,
        avg_summary_quality_ratio=0.75,
        avg_instruction_following_score=0.95,
        avg_brevity_ratio=0.9,
        accepted_count=9,
        soft_accepted_count=1,
        avg_inference_ms=400.0,
        p95_inference_ms=800.0,
    )
    pretty_but_unreliable_score = final_benchmark_score(
        case_count=10,
        success_count=10,
        avg_exact_preservation_ratio=0.45,
        avg_summary_quality_ratio=0.95,
        avg_instruction_following_score=0.55,
        avg_brevity_ratio=0.9,
        accepted_count=5,
        soft_accepted_count=3,
        avg_inference_ms=400.0,
        p95_inference_ms=800.0,
    )

    assert robust_score > pretty_but_unreliable_score
    assert 0.0 <= pretty_but_unreliable_score <= 100.0
    assert 0.0 <= robust_score <= 100.0


def test_warmup_backend_ignores_probe_failures_after_preload() -> None:
    backend = _ProbeFailingBackend()
    scenario = BenchmarkScenario(
        name="cpu-probe-failure",
        track="cpu",
        phase="cpu-screen",
        model="test/model",
        quantization="none",
        device="cpu",
    )
    context = ExtractionContext(cwd=Path.cwd(), workspace_root=Path.cwd())

    warmup = asyncio.run(
        _warmup_backend(
            backend=backend,
            scenario=scenario,
            torch_module=None,
            context=context,
        )
    )

    assert warmup.load_ms >= 0.0
    assert backend.preload_calls == 1
    assert backend.compress_calls == 1


def test_model_output_rejected_error_is_a_backend_unavailable_error() -> None:
    error = ModelOutputRejectedError("invalid summary")

    assert isinstance(error, BackendUnavailableError)


def test_warmup_backend_still_fails_when_preload_fails() -> None:
    backend = _PreloadFailingBackend()
    scenario = BenchmarkScenario(
        name="cpu-preload-failure",
        track="cpu",
        phase="cpu-screen",
        model="test/model",
        quantization="none",
        device="cpu",
    )
    context = ExtractionContext(cwd=Path.cwd(), workspace_root=Path.cwd())

    try:
        asyncio.run(
            _warmup_backend(
                backend=backend,
                scenario=scenario,
                torch_module=None,
                context=context,
            )
        )
    except BackendUnavailableError as error:
        assert str(error) == "could not load test backend"
    else:
        raise AssertionError("expected preload failure to abort warmup")


def test_render_html_report_uses_streamlined_track_dashboard() -> None:
    cpu_result = LoadedResult(
        source_path=Path("benchmark/results/run/cpu-qwen-test.json"),
        scenario={
            "name": "cpu-qwen-test",
            "track": "cpu",
            "phase": "cpu-screen",
            "model": "ibm-granite/granite-4.0-350m-GGUF",
            "quantization": "none",
            "device": "cpu",
        },
        warmup={"load_ms": 100.0},
        summary={
            "case_count": 1,
            "success_count": 1,
            "exact_pass_count": 1,
            "avg_inference_ms": 42.0,
            "p95_inference_ms": 42.0,
            "final_score": 88.8,
            "avg_exact_preservation_ratio": 1.0,
            "avg_summary_quality_ratio": 0.75,
            "avg_instruction_following_score": 0.5,
            "max_exact_preservation_ratio": 1.0,
        },
        cases=[
            {
                "case_id": "python-traceback-01",
                "title": "traceback",
                "domain": "python",
                "inference_ms": 42.0,
                "exact_preservation_ratio": 1.0,
                "summary_quality_ratio": 0.75,
                "instruction_following_score": 0.5,
                "error": None,
            }
        ],
    )
    gpu_result = LoadedResult(
        source_path=Path("benchmark/results/run/gpu-qwen-test.json"),
        scenario={
            "name": "gpu-qwen-test",
            "track": "gpu",
            "phase": "gpu-screen",
            "model": "Qwen/Qwen3.5-2B-Instruct",
            "quantization": "none",
            "device": "cuda",
        },
        warmup={"load_ms": 240.0},
        summary={
            "case_count": 1,
            "success_count": 1,
            "exact_pass_count": 1,
            "avg_inference_ms": 24.0,
            "p95_inference_ms": 24.0,
            "final_score": 93.5,
            "avg_exact_preservation_ratio": 1.0,
            "avg_summary_quality_ratio": 0.82,
            "avg_instruction_following_score": 0.91,
            "max_exact_preservation_ratio": 1.0,
        },
        cases=[
            {
                "case_id": "python-traceback-02",
                "title": "traceback gpu",
                "domain": "python",
                "inference_ms": 24.0,
                "exact_preservation_ratio": 1.0,
                "summary_quality_ratio": 0.82,
                "instruction_following_score": 0.91,
                "error": None,
            }
        ],
    )

    html_report = render_html_report(
        source_path=Path("benchmark/results/run"),
        results=[cpu_result, gpu_result],
        mode="collective",
    )

    assert "CPU Top Score" in html_report
    assert "GPU Top Score" in html_report
    assert "Latency Leaderboard" in html_report
    assert "Score Leaderboard" in html_report
    assert "detail-track-toggle" in html_report
    assert "latency-track-toggle" in html_report
    assert "score-track-toggle" in html_report
    assert "renderTrackWinner" in html_report
    assert "displayModelName" in html_report
    assert "distribution-band instruction" in html_report
    assert "distribution-band preserve" in html_report
    assert "model-head-score" in html_report
    assert "finalScore" in html_report
    assert "summaryQualityRatio" in html_report
    assert "instructionFollowingScore" in html_report
    assert (
        "100 x quality_core x latency, where quality_core = 0.80 x mean(case_score) + 0.20 x p10(case_score)"
        in html_report
    )
    assert "Highest final score across CPU scenarios." not in html_report
    assert "Highest final score across GPU scenarios." not in html_report
    assert "Avg and p95 only. Click a row to inspect that scenario below." not in html_report
    assert (
        "Rail = success and failure base. Markers = exact, preserve, instruction, quality. Score stays on the right."
        not in html_report
    )


def test_print_case_progress_show_output_includes_stats(capsys) -> None:
    result = CaseMetrics(
        case_id="python-traceback-01",
        title="traceback",
        domain="python",
        instruction="Summarize the traceback.",
        expected_output="AuthError in src/auth.py line 42.",
        inference_ms=42.0,
        cpu_rss_bytes=1024 * 1024,
        gpu_peak_bytes=None,
        output="AuthError in src/auth.py line 42.",
        exact_preservation_ratio=0.5,
        summary_quality_ratio=0.25,
        instruction_following_score=0.75,
        validation_status="soft_accepted",
        validation_flags=("missing_exact_anchors",),
        missing_tokens=("AuthError",),
        brevity_ratio=0.8,
    )

    _print_case_progress(result, 1, 2, show_output=True)

    captured = capsys.readouterr().out
    assert "cpu_rss=1.0 MiB" in captured
    assert "quality=0.250" in captured
    assert "instruction=0.750" in captured
    assert "validation_flags: missing_exact_anchors" in captured
    assert "missing_tokens: AuthError" in captured
    assert "output: AuthError in src/auth.py line 42." in captured


def test_print_benchmark_line_wraps_tty_output_in_ansi_color(capsys, monkeypatch) -> None:
    monkeypatch.setattr("benchmark.runner._supports_ansi_color", lambda: True)

    _print_benchmark_line("hello", color=_ANSI_BLUE)

    captured = capsys.readouterr().out
    assert captured == f"{_ANSI_BLUE}hello\x1b[0m\n"


def test_print_case_progress_colors_success_lines_when_tty(capsys, monkeypatch) -> None:
    monkeypatch.setattr("benchmark.runner._supports_ansi_color", lambda: True)
    result = CaseMetrics(
        case_id="python-traceback-01",
        title="traceback",
        domain="python",
        instruction="Summarize the traceback.",
        expected_output="AuthError in src/auth.py line 42.",
        inference_ms=42.0,
        cpu_rss_bytes=1024 * 1024,
        gpu_peak_bytes=None,
        output="AuthError in src/auth.py line 42.",
        exact_preservation_ratio=0.5,
        summary_quality_ratio=0.25,
        instruction_following_score=0.75,
        validation_status="soft_accepted",
        validation_flags=("missing_exact_anchors",),
        missing_tokens=("AuthError",),
        brevity_ratio=0.8,
    )

    _print_case_progress(result, 1, 2, show_output=False)

    captured = capsys.readouterr().out
    assert captured.startswith(_ANSI_GREEN)
    assert "[1/2] python-traceback-01 ok" in captured


def test_build_run_directory_name_uses_optional_name_prefix() -> None:
    assert build_run_directory_name("20260516T120000Z", "") == "20260516T120000Z"
    assert build_run_directory_name("20260516T120000Z", "cpu-smoke") == "cpu-smoke-20260516T120000Z"


def test_sanitize_run_name_normalizes_path_unsafe_characters() -> None:
    assert sanitize_run_name(" cpu smoke / quick ") == "cpu-smoke-quick"
    assert sanitize_run_name("...") == ""
