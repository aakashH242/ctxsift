"""Typed schemas for benchmark datasets, scenarios, and results."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from ctxsift.compression.intent import CompressionIntent


@dataclass(frozen=True)
class BenchmarkJudgement:
    """Explicit per-case scoring constraints."""

    format_check: str = "none"
    anchor_check: str = "required"
    max_extra_tokens: int = 24
    pass_rule: str = ""


@dataclass(frozen=True)
class BenchmarkCase:
    """One benchmark corpus case."""

    case_id: str
    domain: str
    title: str
    instruction: str
    raw_input: str
    must_preserve_tokens: tuple[str, ...]
    ideal_summary: str
    tags: tuple[str, ...] = ()
    family: str = "summary"
    intent: CompressionIntent = CompressionIntent.SUMMARY
    ecosystem: str = ""
    difficulty: str = "medium"
    output_mode: str = "plain_text"
    expected_output: str = ""
    required_anchors: tuple[str, ...] = ()
    forbidden_content: tuple[str, ...] = ()
    judgement: BenchmarkJudgement = field(default_factory=BenchmarkJudgement)
    rationale: str = ""

    @property
    def anchor_tokens(self) -> tuple[str, ...]:
        return self.required_anchors or self.must_preserve_tokens

    @property
    def scoring_target(self) -> str:
        return self.expected_output or self.ideal_summary


@dataclass(frozen=True)
class BenchmarkScenario:
    """One model/quantization configuration to benchmark."""

    name: str
    track: str
    phase: str
    model: str
    quantization: str
    device: str
    gguf_filename: str | None = None
    dtype: str = "auto"
    attn_implementation: str = "auto"
    max_output_tokens: int = 256
    concurrency: int = 1
    enabled: bool = True


@dataclass(frozen=True)
class CaseMetrics:
    """Per-case metrics and output details."""

    case_id: str
    title: str
    domain: str
    instruction: str
    expected_output: str
    inference_ms: float
    cpu_rss_bytes: int | None
    gpu_peak_bytes: int | None
    output: str
    exact_preservation_ratio: float
    summary_quality_ratio: float
    format_adherence_score: float = 0.0
    instruction_following_score: float = 0.0
    validation_status: str = "accepted"
    validation_flags: tuple[str, ...] = ()
    missing_tokens: tuple[str, ...] = ()
    error: str | None = None
    brevity_ratio: float = 1.0
    family: str = "summary"
    thought_leakage_density: float = 0.0
    thought_marker_count: int = 0
    case_score: float = 0.0
    raw_view: OutputViewMetrics = field(default_factory=lambda: OutputViewMetrics())


@dataclass(frozen=True)
class WarmupMetrics:
    """Cold-start and model-load metrics for one scenario."""

    load_ms: float
    cpu_rss_bytes: int | None
    gpu_peak_bytes: int | None
    torch_num_threads: int | None = None
    torch_num_interop_threads: int | None = None
    omp_num_threads: str | None = None
    mkl_num_threads: str | None = None


@dataclass(frozen=True)
class OutputViewMetrics:
    """One scored view of one case output."""

    output: str = ""
    exact_preservation_ratio: float = 0.0
    summary_quality_ratio: float = 0.0
    format_adherence_score: float = 0.0
    instruction_following_score: float = 0.0
    validation_status: str = "rejected"
    validation_flags: tuple[str, ...] = ()
    missing_tokens: tuple[str, ...] = ()
    brevity_ratio: float = 0.0
    thought_leakage_density: float = 0.0
    thought_marker_count: int = 0
    case_score: float = 0.0


@dataclass(frozen=True)
class ScoreViewSummary:
    """Scenario-level aggregate metrics for one output view."""

    case_count: int = 0
    success_count: int = 0
    accepted_count: int = 0
    soft_accepted_count: int = 0
    rejected_count: int = 0
    exact_pass_count: int = 0
    avg_exact_preservation_ratio: float = 0.0
    avg_summary_quality_ratio: float = 0.0
    avg_format_adherence_score: float = 0.0
    avg_instruction_following_score: float = 0.0
    avg_brevity_ratio: float = 0.0
    avg_thought_leakage_density: float = 0.0
    avg_thought_marker_count: float = 0.0
    avg_case_score: float = 0.0
    p10_case_score: float = 0.0
    quality_core: float = 0.0
    final_score: float = 0.0


@dataclass(frozen=True)
class ScenarioSummary:
    """Scenario-level aggregate metrics."""

    case_count: int
    success_count: int
    accepted_count: int
    soft_accepted_count: int
    rejected_count: int
    exact_pass_count: int
    avg_inference_ms: float
    p95_inference_ms: float
    avg_exact_preservation_ratio: float
    avg_summary_quality_ratio: float
    avg_format_adherence_score: float = 0.0
    avg_instruction_following_score: float = 0.0
    avg_brevity_ratio: float = 1.0
    avg_thought_leakage_density: float = 0.0
    avg_thought_marker_count: float = 0.0
    avg_case_score: float = 0.0
    p10_case_score: float = 0.0
    quality_core: float = 0.0
    latency_factor: float = 0.85
    final_score: float = 0.0
    peak_cpu_rss_bytes: int | None = None
    peak_gpu_bytes: int | None = None
    raw_view: ScoreViewSummary = field(default_factory=ScoreViewSummary)


@dataclass(frozen=True)
class ScenarioResult:
    """Complete persisted result for one benchmark scenario."""

    scenario: BenchmarkScenario
    warmup: WarmupMetrics
    summary: ScenarioSummary
    cases: tuple[CaseMetrics, ...]

    def to_dict(self) -> dict[str, Any]:
        """Convert result into a JSON-serializable dictionary."""
        return {
            "scenario": asdict(self.scenario),
            "warmup": asdict(self.warmup),
            "summary": asdict(self.summary),
            "cases": [asdict(case) for case in self.cases],
        }


@dataclass(frozen=True)
class BenchmarkManifest:
    """Loaded dataset and scenario collection."""

    cases: tuple[BenchmarkCase, ...] = field(default_factory=tuple)
    scenarios: tuple[BenchmarkScenario, ...] = field(default_factory=tuple)
