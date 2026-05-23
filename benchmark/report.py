"""Result writers for benchmark runs."""

from __future__ import annotations

import json
from pathlib import Path

from benchmark.schemas import ScenarioResult


def write_result_files(output_dir: Path, result: ScenarioResult) -> tuple[Path, Path]:
    """Write one scenario result to JSON and Markdown files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = result.scenario.name
    json_path = output_dir / f"{stem}.json"
    md_path = output_dir / f"{stem}.md"
    json_path.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")
    md_path.write_text(render_markdown_report(result), encoding="utf-8")
    return json_path, md_path


def render_markdown_report(result: ScenarioResult) -> str:
    """Render a human-readable Markdown report for one scenario."""
    lines = [
        f"# {result.scenario.name}",
        "",
        "## Scenario",
        "",
        f"- track: `{result.scenario.track}`",
        f"- phase: `{result.scenario.phase}`",
        f"- model: `{result.scenario.model}`",
        f"- quantization: `{result.scenario.quantization}`",
        f"- device: `{result.scenario.device}`",
        f"- dtype: `{result.scenario.dtype}`",
        f"- max_output_tokens: `{result.scenario.max_output_tokens}`",
        f"- concurrency: `{result.scenario.concurrency}`",
        "",
        "## Warmup",
        "",
        f"- load_ms: `{result.warmup.load_ms:.2f}`",
        f"- cpu_rss_bytes: `{_fmt_optional_int(result.warmup.cpu_rss_bytes)}`",
        f"- gpu_peak_bytes: `{_fmt_optional_int(result.warmup.gpu_peak_bytes)}`",
        f"- torch_num_threads: `{_fmt_optional_int(result.warmup.torch_num_threads)}`",
        f"- torch_num_interop_threads: `{_fmt_optional_int(result.warmup.torch_num_interop_threads)}`",
        f"- OMP_NUM_THREADS: `{result.warmup.omp_num_threads or 'null'}`",
        f"- MKL_NUM_THREADS: `{result.warmup.mkl_num_threads or 'null'}`",
        "",
        "## Summary",
        "",
        f"- case_count: `{result.summary.case_count}`",
        f"- success_count: `{result.summary.success_count}`",
        f"- accepted_count: `{result.summary.accepted_count}`",
        f"- soft_accepted_count: `{result.summary.soft_accepted_count}`",
        f"- rejected_count: `{result.summary.rejected_count}`",
        f"- exact_pass_count: `{result.summary.exact_pass_count}`",
        f"- avg_inference_ms: `{result.summary.avg_inference_ms:.2f}`",
        f"- p95_inference_ms: `{result.summary.p95_inference_ms:.2f}`",
        f"- avg_exact_preservation_ratio: `{result.summary.avg_exact_preservation_ratio:.3f}`",
        f"- avg_summary_quality_ratio: `{result.summary.avg_summary_quality_ratio:.3f}`",
        f"- avg_format_adherence_score: `{result.summary.avg_format_adherence_score:.3f}`",
        f"- avg_instruction_following_score: `{result.summary.avg_instruction_following_score:.3f}`",
        f"- avg_brevity_ratio: `{result.summary.avg_brevity_ratio:.3f}`",
        f"- avg_case_score: `{result.summary.avg_case_score:.3f}`",
        f"- p10_case_score: `{result.summary.p10_case_score:.3f}`",
        f"- quality_core: `{result.summary.quality_core:.3f}`",
        f"- latency_factor: `{result.summary.latency_factor:.3f}`",
        f"- final_score: `{result.summary.final_score:.2f}`",
        f"- peak_cpu_rss_bytes: `{_fmt_optional_int(result.summary.peak_cpu_rss_bytes)}`",
        f"- peak_gpu_bytes: `{_fmt_optional_int(result.summary.peak_gpu_bytes)}`",
        "",
        "## Cases",
        "",
        "| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for case in result.cases:
        flags = ", ".join(case.validation_flags) if case.validation_flags else "-"
        missing = ", ".join(case.missing_tokens) if case.missing_tokens else "-"
        error = case.error or "-"
        lines.append(
            f"| `{case.case_id}` | `{case.family}` | `{case.domain}` | `{case.inference_ms:.2f}` | "
            f"`{case.case_score:.3f}` | "
            f"`{case.exact_preservation_ratio:.3f}` | `{case.summary_quality_ratio:.3f}` | "
            f"`{case.format_adherence_score:.3f}` | `{case.instruction_following_score:.3f}` | "
            f"`{case.brevity_ratio:.3f}` | `{case.validation_status}` | "
            f"{flags} | {missing} | {error} |"
        )
    return "\n".join(lines) + "\n"


def _fmt_optional_int(value: int | None) -> str:
    return "null" if value is None else str(value)
