"""HTML viewer for benchmark result JSON files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import UTC, datetime
import html
import json
from pathlib import Path
import re
from typing import Any, Iterable, Sequence
import webbrowser

from benchmark.loader import load_cases
from benchmark.scoring import final_benchmark_score, latency_factor_score, quality_core_score
from benchmark.stats import percentile


@dataclass(slots=True)
class LoadedResult:
    source_path: Path
    scenario: dict[str, Any]
    warmup: dict[str, Any]
    summary: dict[str, Any]
    cases: list[dict[str, Any]]


@dataclass(frozen=True, slots=True)
class CaseReference:
    instruction: str
    expected_output: str


_FIRST_PASS_PREVIEW_RE = re.compile(r"\bfirst_pass='([^']*)'")
_REPAIR_PASS_PREVIEW_RE = re.compile(r"\brepair_pass='([^']*)'")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Benchmark result file(s) or result directory roots.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output HTML path. Defaults next to the input root.",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the rendered HTML in the default browser.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    input_paths = _normalize_input_paths(args.paths)
    results = load_results(input_paths)
    if not results:
        parser.error("no benchmark result JSON files were found")

    output_path = resolve_output_path(input_paths, args.output)
    html_report = render_html_report(
        source_path=input_paths,
        results=results,
        mode="collective",
    )
    output_path.write_text(html_report, encoding="utf-8")
    print(f"rendered {len(results)} result files to {output_path}")

    if args.open:
        webbrowser.open(output_path.resolve().as_uri())
    return 0


def _normalize_input_paths(input_path: Path | Sequence[Path]) -> list[Path]:
    if isinstance(input_path, Path):
        paths = [input_path]
    else:
        paths = list(input_path)
    if not paths:
        raise ValueError("at least one input path is required")
    return [path.expanduser().resolve() for path in paths]


def _iter_result_paths(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return
    if not root.exists():
        return
    for candidate in sorted(root.rglob("*.json")):
        yield candidate


def _try_load_result_payload(path: Path) -> dict[str, Any] | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(payload, dict):
        return None
    required_keys = {"scenario", "warmup", "summary", "cases"}
    if not required_keys.issubset(payload):
        return None
    return payload


def load_results(input_path: Path | Sequence[Path]) -> list[LoadedResult]:
    results: list[LoadedResult] = []
    for root in _normalize_input_paths(input_path):
        for candidate in _iter_result_paths(root):
            payload = _try_load_result_payload(candidate)
            if not payload:
                continue
            cases = payload.get("cases")
            if not isinstance(cases, list):
                continue
            results.append(
                LoadedResult(
                    source_path=candidate,
                    scenario=dict(payload.get("scenario") or {}),
                    warmup=dict(payload.get("warmup") or {}),
                    summary=dict(payload.get("summary") or {}),
                    cases=[item for item in cases if isinstance(item, dict)],
                )
            )
    return results


def load_case_reference_index() -> dict[str, CaseReference]:
    dataset_path = Path(__file__).resolve().with_name("dataset.jsonl")
    if not dataset_path.exists():
        return {}
    try:
        cases = load_cases(dataset_path)
    except (OSError, ValueError, json.JSONDecodeError):
        return {}
    return {
        case.case_id: CaseReference(
            instruction=case.instruction,
            expected_output=case.scoring_target,
        )
        for case in cases
    }


def resolve_output_path(
    input_path: Path | Sequence[Path],
    requested_output: Path | None,
) -> Path:
    if requested_output is not None:
        return requested_output.expanduser().resolve()

    input_paths = _normalize_input_paths(input_path)
    if len(input_paths) > 1:
        parent = input_paths[0] if input_paths[0].is_dir() else input_paths[0].parent
        return parent / "viewer-multi.html"

    only_path = input_paths[0]
    if only_path.is_dir():
        return only_path / "viewer.html"
    return only_path.with_name("viewer.html")


def _format_source_label(source_path: Path | Sequence[Path]) -> str:
    input_paths = _normalize_input_paths(source_path)
    if len(input_paths) == 1:
        return str(input_paths[0])
    return " | ".join(str(path) for path in input_paths)


def _safe_str(value: Any, default: str = "n/a") -> str:
    if value is None:
        return default
    text = str(value).strip()
    return text or default


def _preview_text(value: Any, *, limit: int = 320) -> str:
    text = _safe_str(value, default="")
    if not text:
        return ""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 3] + "..."


def _rejected_output_preview(error: str) -> str:
    if not error:
        return ""
    previews: list[str] = []
    for pattern in (_FIRST_PASS_PREVIEW_RE, _REPAIR_PASS_PREVIEW_RE):
        match = pattern.search(error)
        if not match:
            continue
        preview = _preview_text(match.group(1), limit=220)
        if preview and preview not in previews:
            previews.append(preview)
    if not previews:
        return ""
    if len(previews) == 1:
        return previews[0]
    return "\n---\n".join(previews)


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _median(values: Sequence[float]) -> float:
  return percentile(values, 0.5)


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _source_run_label(result_path: Path) -> str:
    parent = result_path.parent
    for candidate in [parent.name, parent.parent.name if parent.parent else ""]:
        if candidate:
            return candidate
    return result_path.stem


def _scenario_family(scenario: dict[str, Any]) -> str:
  candidates = [
    scenario.get("track"),
    scenario.get("phase"),
    scenario.get("name"),
    scenario.get("device"),
  ]
  normalized = " ".join(str(value or "").casefold() for value in candidates)
  if "remote" in normalized:
    return "remote"
  if "gpu" in normalized or "cuda" in normalized:
    return "gpu"
  if "cpu" in normalized:
    return "cpu"
  return "other"


def build_case_row(case: dict[str, Any]) -> dict[str, Any]:
    error = _safe_str(case.get("error") or "", default="")
    case_id = _safe_str(case.get("case_id") or case.get("id"))
    return {
        "caseId": case_id,
        "title": _safe_str(case.get("title") or case.get("prompt") or case.get("query")),
        "domain": _safe_str(case.get("domain"), default="general"),
        "inferenceMs": _as_float(case.get("inference_ms") or case.get("latency_ms")),
        "exactPreservationRatio": _as_float(
            case.get("exact_preservation_ratio")
            or case.get("preservation_ratio")
            or case.get("exact_ratio")
        ),
        "summaryQualityRatio": _as_float(
            case.get("summary_quality_ratio")
            or case.get("quality_ratio")
        ),
        "formatAdherenceScore": _as_float(case.get("format_adherence_score")),
        "instructionFollowingScore": _as_float(
            case.get("instruction_following_score")
            or case.get("instructionFollowingScore")
        ),
        "brevityRatio": _as_float(case.get("brevity_ratio"), 1.0),
        "validationStatus": _safe_str(case.get("validation_status"), default="accepted"),
        "family": _safe_str(case.get("family"), default="summary"),
        "caseScore": _as_float(case.get("case_score")),
        "hasCaseScore": "case_score" in case,
        "error": error,
        "status": "error" if error else "ok",
    }


def _failed_case_detail_key(scenario_key: str, case_id: str) -> str:
    return f"{scenario_key}::{case_id}"


def build_scenario_row(
    result: LoadedResult,
    *,
    index: int,
    multi_source: bool,
    case_reference_index: dict[str, CaseReference],
    failed_case_details: dict[str, dict[str, str]],
) -> dict[str, Any]:
    scenario = result.scenario
    summary = result.summary
    warmup = result.warmup
    run_label = _source_run_label(result.source_path)
    name = _safe_str(scenario.get("name") or scenario.get("id") or result.source_path.stem)
    key = f"{run_label}::{name}::{index}"
    cases: list[dict[str, Any]] = []
    for case in result.cases:
        row = build_case_row(case)
        if row["status"] == "error":
            case_id = row["caseId"]
            reference = case_reference_index.get(case_id)
            expected_output = _preview_text(case.get("expected_output"), limit=220)
            if not expected_output and reference is not None:
                expected_output = _preview_text(reference.expected_output, limit=220)
            actual_output = _preview_text(case.get("output"), limit=320)
            if not actual_output:
                actual_output = _rejected_output_preview(row["error"])
            detail_key = _failed_case_detail_key(key, case_id)
            failed_case_details[detail_key] = {
                "expectedOutput": expected_output,
                "actualOutput": actual_output,
            }
            row["detailKey"] = detail_key
        cases.append(row)
    inference_values = [row["inferenceMs"] for row in cases if row["inferenceMs"] > 0]
    preservation_values = [row["exactPreservationRatio"] for row in cases]
    quality_values = [row["summaryQualityRatio"] for row in cases]
    format_values = [row["formatAdherenceScore"] for row in cases]
    instruction_values = [row["instructionFollowingScore"] for row in cases]
    brevity_values = [row["brevityRatio"] for row in cases]
    case_scores = [row["caseScore"] for row in cases if row["hasCaseScore"]]
    exact_hits = sum(1 for row in cases if row["exactPreservationRatio"] >= 0.999)
    error_count = sum(1 for row in cases if row["error"])
    case_count = len(cases)
    success_count = case_count - error_count
    avg_inference_ms = _as_float(summary.get("avg_inference_ms"), _mean(inference_values))
    p95_inference_ms = _as_float(summary.get("p95_inference_ms"), percentile(inference_values, 0.95))
    avg_preservation_ratio = _as_float(summary.get("avg_exact_preservation_ratio"), _mean(preservation_values))
    avg_quality_ratio = _as_float(summary.get("avg_summary_quality_ratio"), _mean(quality_values))
    avg_format_ratio = _as_float(summary.get("avg_format_adherence_score"), _mean(format_values))
    avg_instruction_ratio = _as_float(
      summary.get("avg_instruction_following_score"),
      _mean(instruction_values),
    )
    avg_brevity_ratio = _as_float(summary.get("avg_brevity_ratio"), _mean(brevity_values))
    avg_case_score = _as_float(summary.get("avg_case_score"), _mean(case_scores))
    p10_case_score = _as_float(summary.get("p10_case_score"), percentile(case_scores, 0.10))
    latency_factor = _as_float(
        summary.get("latency_factor"),
        latency_factor_score(avg_inference_ms) if inference_values else 0.85,
    )
    max_preservation_ratio = _as_float(summary.get("max_exact_preservation_ratio"), max(preservation_values, default=0.0))
    warmup_ms = _as_float(warmup.get("duration_ms") or warmup.get("warmup_ms"))
    success_rate = _as_float(summary.get("success_rate"), success_count / case_count if case_count else 0.0)
    exact_pass_rate = _as_float(summary.get("exact_pass_rate"), exact_hits / case_count if case_count else 0.0)
    exact_pass_count = _as_int(summary.get("exact_pass_count"), exact_hits)
    family = _scenario_family(scenario)
    case_scores_for_formula = case_scores if case_scores else None
    final_score = _as_float(
      summary.get("final_score"),
      final_benchmark_score(
        case_count=case_count,
        success_count=success_count,
        avg_exact_preservation_ratio=avg_preservation_ratio,
        avg_summary_quality_ratio=avg_quality_ratio,
        avg_instruction_following_score=avg_instruction_ratio,
        avg_brevity_ratio=avg_brevity_ratio,
        accepted_count=_as_int(summary.get("accepted_count"), success_count),
        soft_accepted_count=_as_int(summary.get("soft_accepted_count"), 0),
        avg_inference_ms=avg_inference_ms,
        p95_inference_ms=p95_inference_ms,
        case_scores=case_scores_for_formula,
        observed_latency_ms=avg_inference_ms,
      ),
    )
    quality_core = _as_float(
        summary.get("quality_core"),
        (final_score / (100.0 * max(latency_factor, 1e-12))) if final_score > 0.0 else quality_core_score(case_scores),
    )
    return {
        "key": key,
        "name": name,
        "runLabel": run_label,
        "sourcePath": result.source_path.as_posix(),
        "model": _safe_str(scenario.get("model")),
        "family": family,
        "track": _safe_str(scenario.get("track"), default="benchmark"),
        "phase": _safe_str(scenario.get("phase"), default="run"),
        "quantization": _safe_str(scenario.get("quantization"), default="none"),
        "device": _safe_str(scenario.get("device"), default="cpu"),
        "dtype": _safe_str(scenario.get("dtype"), default="auto"),
        "warmupMs": warmup_ms,
        "avgInferenceMs": avg_inference_ms,
        "p95InferenceMs": p95_inference_ms,
        "avgPreservationRatio": avg_preservation_ratio,
        "avgQualityRatio": avg_quality_ratio,
        "avgFormatRatio": avg_format_ratio,
        "avgInstructionRatio": avg_instruction_ratio,
        "avgBrevityRatio": avg_brevity_ratio,
        "avgCaseScore": avg_case_score,
        "p10CaseScore": p10_case_score,
        "qualityCore": quality_core,
        "latencyFactor": latency_factor,
        "finalScore": final_score,
        "maxPreservationRatio": max_preservation_ratio,
        "successRate": success_rate,
        "exactPassRate": exact_pass_rate,
        "caseCount": case_count,
        "successCount": success_count,
        "errorCount": error_count,
        "exactPassCount": exact_pass_count,
        "multiSource": multi_source,
        "cases": cases,
    }


def build_dashboard_data(results: Sequence[LoadedResult], *, mode: str) -> dict[str, Any]:
    source_roots = {result.source_path.parent.as_posix() for result in results}
    multi_source = len(source_roots) > 1
    case_reference_index = load_case_reference_index()
    failed_case_details: dict[str, dict[str, str]] = {}
    scenario_rows = [
        build_scenario_row(
            result,
            index=index,
            multi_source=multi_source,
            case_reference_index=case_reference_index,
            failed_case_details=failed_case_details,
        )
        for index, result in enumerate(results)
    ]
    scenario_rows.sort(key=lambda item: (item["name"], item["runLabel"], item["track"]))
    return {
        "mode": mode,
        "multiSource": multi_source,
        "scenarioCount": len(scenario_rows),
        "failedCaseDetails": failed_case_details,
        "scenarios": scenario_rows,
    }


def render_html_report(
    *,
    source_path: Path | Sequence[Path],
    results: Sequence[LoadedResult],
    mode: str = "standard",
) -> str:
    data = build_dashboard_data(results, mode=mode)
    data_json = json.dumps(data).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ctxsift Benchmark Viewer</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Fira+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      color-scheme: dark;
      --bg: #000000;
      --panel: #030608;
      --panel-strong: #071015;
      --panel-soft: rgba(255, 176, 32, 0.08);
      --text: #f2fff8;
      --muted: #7d9b8f;
      --accent: #ffb020;
      --accent-strong: #ffd36a;
      --accent-soft: rgba(255, 176, 32, 0.12);
      --success: #22c55e;
      --success-strong: #7bf0a5;
      --success-soft: rgba(34, 197, 94, 0.14);
      --warn: #ffd24a;
      --warn-soft: rgba(255, 210, 74, 0.12);
      --danger: #ff5b6b;
      --danger-soft: rgba(255, 91, 107, 0.14);
      --exact: #3bd4ff;
      --info: #3bd4ff;
      --border: #3a2a0e;
      --shadow: 0 0 0 1px rgba(58, 42, 14, 0.45);
      --radius: 12px;
      --mono: "Fira Code", "JetBrains Mono", "Cascadia Code", Consolas, monospace;
      --sans: "Fira Sans", "Segoe UI", sans-serif;
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      font-family: var(--sans);
      font-size: 14px;
      color: var(--text);
      background: var(--bg);
    }

    .shell {
      width: min(1440px, calc(100vw - 32px));
      margin: 16px auto 32px;
      display: grid;
      gap: 16px;
    }

    .hero,
    .panel,
    .compare-panel {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }

    .hero {
      padding: 18px 20px;
    }

    .hero::after {
      display: none;
    }

    .hero-top {
      display: flex;
      justify-content: space-between;
      gap: 14px;
      align-items: start;
      flex-wrap: wrap;
    }

    h1, h2, h3, strong, label, th { letter-spacing: 0; }
    h1 {
      margin: 0;
      font-size: 1.2rem;
      line-height: 1.2;
      font-weight: 700;
      text-transform: uppercase;
    }

    h2 {
      margin: 0 0 6px;
      font-size: 0.82rem;
      font-weight: 700;
    }

    p { margin: 0; }

    .hero-subtitle {
      display: none;
    }

    .meta-grid {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      justify-content: flex-end;
      align-items: flex-start;
      color: var(--muted);
      font-size: 0.78rem;
    }

    .meta-grid strong {
      font-weight: 600;
      color: var(--text);
      margin-right: 6px;
    }

    .mono {
      font-family: var(--mono);
      font-size: 0.87rem;
    }

    .tooltip-hint {
      display: inline-flex;
      align-items: center;
      margin-left: 8px;
      padding: 1px 6px;
      border: 1px dashed var(--border);
      border-radius: 999px;
      color: var(--muted);
      font-size: 11px;
      line-height: 1.4;
      text-transform: uppercase;
    }

    .grid {
      display: grid;
      gap: 14px;
    }

    .kpis {
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
    }

    .two-up {
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    }

    .panel {
      padding: 16px;
    }

    .hero-kicker {
      margin-bottom: 6px;
      color: var(--accent-strong);
      font-family: var(--mono);
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .panel-note,
    .chart-footnote,
    .empty-copy,
    .legend span,
    .detail-item small,
    .scenario-subtitle,
    .scatter-legend span,
    .toolbar-note {
      color: var(--muted);
    }

    .kpi {
      display: grid;
      gap: 4px;
      padding: 12px;
      border-radius: 4px;
      background: transparent;
      border: 1px solid var(--border);
    }

    .kpi-label {
      font-size: 0.72rem;
      color: var(--muted);
    }

    .kpi-value {
      font-size: 1.05rem;
      font-weight: 700;
    }

    .compare-panel {
      padding: 16px;
      display: grid;
      gap: 12px;
    }

    .compare-toolbar,
    .toolbar {
      display: flex;
      gap: 10px;
      justify-content: space-between;
      align-items: start;
      flex-wrap: wrap;
    }

    .compare-toolbar > div:first-child {
      flex: 1 1 360px;
      min-width: 0;
    }

    .compare-actions,
    .control-row {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
    }

    .compare-toolbar-right {
      display: flex;
      gap: 10px;
      align-items: start;
      flex-wrap: wrap;
      justify-content: flex-end;
      margin-left: auto;
      flex: 0 1 auto;
    }

    .compare-toolbar-right .control {
      min-width: 160px;
    }

    .compare-body[hidden] {
      display: none;
    }

    .compare-controls {
      display: grid;
      gap: 12px;
      grid-template-columns: minmax(0, 1fr) 150px minmax(0, 1fr);
      align-items: end;
    }

    .compare-controls .control {
      min-width: 0;
    }

    .compare-controls .control.compare-spacer {
      visibility: hidden;
      pointer-events: none;
    }

    .compare-head-grid {
      display: grid;
      gap: 12px;
      grid-template-columns: minmax(0, 1fr) 150px minmax(0, 1fr);
      align-items: stretch;
    }

    .compare-card {
      display: grid;
      gap: 8px;
      padding: 12px;
      border-radius: 4px;
      border: 1px solid var(--border);
      background: transparent;
    }

    .compare-card-top {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      align-items: start;
    }

    .compare-card-title {
      font-family: var(--mono);
      font-size: 0.9rem;
      word-break: break-word;
    }

    .compare-card-score {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-strong);
    }

    .compare-card-copy {
      display: grid;
      gap: 4px;
    }

    .compare-card-meta {
      color: var(--muted);
      font-size: 0.76rem;
    }

    .compare-versus {
      display: grid;
      place-items: center;
      border: 1px solid var(--border);
      border-radius: 4px;
      color: var(--muted);
      font-family: var(--mono);
      font-size: 0.82rem;
      text-transform: uppercase;
    }

    .headtohead-metrics {
      display: grid;
      gap: 8px;
    }

    .headtohead-row {
      display: grid;
      gap: 12px;
      grid-template-columns: minmax(0, 1fr) 180px minmax(0, 1fr);
      align-items: center;
      padding-top: 8px;
      border-top: 1px solid rgba(18, 49, 38, 0.4);
    }

    .headtohead-label {
      color: var(--muted);
      font-size: 0.75rem;
      text-align: center;
      text-transform: uppercase;
    }

    .headtohead-value {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      align-items: center;
      min-width: 0;
      padding: 10px 12px;
      border-radius: 4px;
      border: 1px solid var(--border);
      background: transparent;
      font-family: var(--mono);
    }

    .headtohead-value.is-better {
      border-color: var(--success);
      background: var(--success-soft);
      color: var(--success-strong);
    }

    .headtohead-value.is-worse {
      opacity: 0.78;
    }

    .headtohead-value.is-tie {
      border-color: rgba(59, 212, 255, 0.5);
    }

    .headtohead-value small {
      color: var(--muted);
      font-size: 0.72rem;
      text-transform: uppercase;
    }

    button,
    select {
      font: inherit;
      color: var(--text);
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--panel);
      transition: background 150ms ease, border-color 150ms ease, color 150ms ease;
    }

    button {
      padding: 8px 12px;
      cursor: pointer;
    }

    button:hover,
    select:hover,
    .scenario-option:hover,
    .hit-row:hover {
      border-color: var(--accent);
      background: var(--accent-soft);
    }

    button[data-active="true"] {
      background: var(--accent-soft);
      border-color: var(--accent);
      color: var(--accent);
    }

    select {
      min-width: 0;
      width: 100%;
      padding: 8px 10px;
    }

    .scenario-picker {
      display: grid;
      gap: 10px;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    }

    .scenario-option {
      display: grid;
      gap: 8px;
      padding: 12px;
      border-radius: 4px;
      border: 1px solid var(--border);
      background: transparent;
      cursor: pointer;
    }

    .scenario-option.active {
      background: var(--accent-soft);
      border-color: var(--accent);
    }

    .scenario-option-head {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: start;
    }

    .scenario-option-title {
      font-family: var(--mono);
      font-size: 0.88rem;
      word-break: break-word;
    }

    .badge-row {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 2px 6px;
      border-radius: 3px;
      font-size: 0.72rem;
      border: 1px solid var(--border);
      background: transparent;
    }

    .badge.accent { background: var(--success-soft); }
    .badge.warn { background: var(--warn-soft); }
    .badge.danger { background: var(--danger-soft); }

    .bars,
    .quality-stacks,
    .domain-bars {
      display: grid;
      gap: 8px;
      margin-top: 12px;
    }

    .bar-row,
    .stack-row,
    .domain-row {
      display: grid;
      gap: 10px;
      align-items: center;
      grid-template-columns: minmax(170px, 1.3fr) minmax(200px, 4fr) auto;
    }

    .bar-label,
    .stack-label,
    .domain-label {
      display: grid;
      gap: 2px;
    }

    .bar-label strong,
    .stack-label strong,
    .domain-label strong,
    .collective-best-name {
      font-family: var(--mono);
      font-size: 0.86rem;
      font-weight: 500;
    }

    .bar-label span,
    .stack-label span,
    .domain-label span {
      font-size: 0.78rem;
    }

    .metric-rail {
      position: relative;
      height: 6px;
      border-radius: 2px;
      background: rgba(255,255,255,0.08);
      overflow: hidden;
    }

    .metric-fill {
      position: absolute;
      inset: 0 auto 0 0;
      height: 100%;
      border-radius: inherit;
      background: var(--accent);
      opacity: 0.65;
    }

    .metric-marker {
      position: absolute;
      top: -2px;
      width: 1px;
      height: 10px;
      border-radius: 0;
      background: rgba(255,255,255,0.9);
    }

    .stack-fill {
      height: 100%;
      float: left;
    }

    .stack-fill.success { background: color-mix(in srgb, var(--success) 72%, transparent); }
    .stack-fill.error { background: rgba(248, 81, 73, 0.75); }
    .stack-fill.exact {
      position: absolute;
      inset: 0 auto 0 0;
      background: rgba(88, 166, 255, 0.48);
      border-right: 1px solid rgba(13, 17, 23, 0.6);
    }

    .legend {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 10px;
      font-size: 0.8rem;
    }

    .legend i {
      display: inline-block;
      width: 10px;
      height: 10px;
      border-radius: 2px;
      margin-right: 5px;
      vertical-align: middle;
    }

    .table-wrap {
      overflow: auto;
      margin-top: 12px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      min-width: 720px;
    }

    th,
    td {
      padding: 8px 12px;
      border-bottom: 1px solid var(--border);
      text-align: left;
      vertical-align: top;
      font-size: 0.82rem;
    }

    thead th {
      position: sticky;
      top: 0;
      background: var(--panel-strong);
      z-index: 1;
    }

    tbody tr:hover,
    tbody tr.active-row {
      background: rgba(255,255,255,0.04);
    }

    .click-row { cursor: pointer; }
    .status-ok { color: var(--success); }
    .status-error { color: var(--danger); }

    .sort-button {
      all: unset;
      display: inline-flex;
      gap: 6px;
      align-items: center;
      cursor: pointer;
      color: inherit;
    }

    .sort-button::after {
      content: "↕";
      font-size: 0.82rem;
      color: var(--muted);
    }

    th[aria-sort="ascending"] .sort-button::after { content: "↑"; color: var(--accent); }
    th[aria-sort="descending"] .sort-button::after { content: "↓"; color: var(--warn); }

    .detail-grid {
      display: grid;
      gap: 10px;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      margin-top: 12px;
    }

    .detail-item {
      padding: 10px 12px;
      border-radius: 4px;
      background: transparent;
      border: 1px solid var(--border);
      display: grid;
      gap: 4px;
    }

    .empty-state {
      padding: 14px;
      border-radius: 4px;
      background: transparent;
      border: 1px dashed var(--border);
      margin-top: 12px;
    }

    .collective-best-card {
      display: grid;
      gap: 8px;
      margin-top: 10px;
      padding: 12px;
      border-radius: 4px;
      background: transparent;
      border: 1px solid var(--border);
    }

    .collective-best-title {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: start;
      flex-wrap: wrap;
    }

    .collective-best-rule {
      color: var(--warn);
      font-size: 0.72rem;
    }

    .collective-best-stats {
      display: grid;
      gap: 8px;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    }

    .hit-compare {
      display: grid;
      gap: 8px;
      margin-top: 10px;
    }

    .hit-row {
      display: grid;
      gap: 10px;
      grid-template-columns: minmax(160px, 1.4fr) minmax(210px, 2.6fr);
      align-items: center;
      padding: 8px 10px;
      border-radius: 4px;
      background: transparent;
      border: 1px solid var(--border);
    }

    .hit-name {
      display: grid;
      gap: 2px;
    }

    .hit-name strong {
      font-family: var(--mono);
      font-size: 0.84rem;
      font-weight: 500;
    }

    .hit-name span {
      color: var(--muted);
      font-size: 0.76rem;
    }

    .hit-metrics {
      display: grid;
      gap: 6px;
      grid-template-columns: auto minmax(120px, 1fr) auto;
      align-items: center;
    }

    .hit-chip,
    .hit-value {
      font-family: var(--mono);
      font-size: 0.78rem;
      color: var(--text);
      white-space: nowrap;
    }

    .hit-chip {
      padding: 2px 6px;
      border-radius: 3px;
      border: 1px solid var(--border);
      background: transparent;
    }

    .panel-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
    }

    .panel-head h2 {
      margin-bottom: 0;
    }

    .panel-head select {
      min-width: 0;
      font-size: 0.78rem;
      padding: 4px 8px;
    }

    .panel-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
    }

    .panel-head h2 {
      margin-bottom: 0;
    }

    .panel-head select {
      min-width: 0;
      font-size: 0.78rem;
      padding: 4px 8px;
    }

    .track-cards {
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    }

    .winner-card,
    .model-head,
    .detail-strip {
      display: grid;
      gap: 14px;
      padding: 14px;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: rgba(4, 10, 12, 0.92);
    }

    .winner-card {
      width: 100%;
      text-align: left;
    }

    .winner-top,
    .model-head-top,
    .leaderboard-main {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: flex-start;
      flex-wrap: wrap;
    }

    .track-chip,
    .score-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 8px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: rgba(0, 255, 156, 0.06);
      color: var(--accent-strong);
      font-family: var(--mono);
      font-size: 0.75rem;
      white-space: nowrap;
    }

    .score-chip.warn {
      color: var(--warn);
      background: var(--warn-soft);
    }

    .score-stack {
      display: grid;
      justify-items: end;
      gap: 6px;
    }

    .score-formula {
      max-width: 280px;
      color: var(--muted);
      font-size: 0.68rem;
      line-height: 1.35;
      text-align: right;
    }

    .winner-scenario,
    .leaderboard-scenario,
    .model-head-kicker {
      color: var(--accent-strong);
      font-family: var(--mono);
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .winner-model,
    .leaderboard-model,
    .model-head-name {
      font-family: var(--sans);
      font-size: 1.02rem;
      font-weight: 600;
      line-height: 1.3;
      overflow-wrap: anywhere;
    }

    .winner-stats,
    .detail-grid {
      display: grid;
      gap: 10px;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    }

    .segmented-toggle {
      display: inline-flex;
      gap: 6px;
      padding: 4px;
      border: 1px solid var(--border);
      border-radius: 999px;
      background: rgba(4, 10, 12, 0.98);
    }

    .segmented-toggle button {
      min-width: 62px;
      padding: 6px 10px;
      border-radius: 999px;
      border: 1px solid transparent;
      background: transparent;
    }

    .segmented-toggle button:disabled {
      cursor: default;
      opacity: 0.35;
    }

    .leaderboard-list {
      display: grid;
      gap: 10px;
      margin-top: 14px;
    }

    .leaderboard-row {
      width: 100%;
      display: grid;
      gap: 12px;
      grid-template-columns: minmax(0, 1.5fr) minmax(180px, 2.8fr) auto;
      align-items: center;
      padding: 12px 14px;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: rgba(4, 10, 12, 0.92);
      text-align: left;
    }

    .leaderboard-copy {
      display: grid;
      gap: 4px;
      min-width: 0;
    }

    .leaderboard-copy strong,
    .leaderboard-copy span,
    .detail-item strong,
    .bar-label strong,
    .stack-label strong,
    .domain-label strong,
    .collective-best-name {
      overflow-wrap: anywhere;
    }

    .leaderboard-meta {
      color: var(--muted);
      font-size: 0.78rem;
      overflow-wrap: anywhere;
    }

    .leaderboard-rail-wrap {
      display: grid;
      gap: 8px;
      min-width: 0;
    }

    .leaderboard-rail-caption {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      color: var(--muted);
      font-size: 0.76rem;
    }

    .distribution-rail {
      position: relative;
      height: 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.06);
      overflow: hidden;
    }

    .distribution-segment,
    .distribution-band {
      position: absolute;
      top: 0;
      bottom: 0;
    }

    .distribution-segment.success { background: color-mix(in srgb, var(--success) 72%, transparent); }
    .distribution-segment.error { background: rgba(255, 91, 107, 0.8); }
    .distribution-band {
      width: 4px;
      transform: translateX(-50%);
      border-radius: 2px;
    }

    .distribution-band.exact   { background: rgba(59, 212, 255, 0.95); }
    .distribution-band.preserve { background: rgba(179, 127, 255, 0.92); }
    .distribution-band.instruction { background: rgba(255, 210, 74, 0.95); }
    .distribution-band.quality { background: rgba(255, 255, 255, 0.88); }

    .leaderboard-value {
      font-family: var(--mono);
      font-size: 1rem;
      white-space: nowrap;
      color: var(--accent-strong);
    }

    .leaderboard-value.dim {
      color: var(--text);
    }

    .detail-toolbar {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: end;
      flex-wrap: wrap;
    }

    .detail-toolbar .control {
      min-width: 0;
    }

    .detail-toolbar .control:first-child {
      flex: 1 1 320px;
    }

    .detail-shell .table-wrap {
      margin-top: 14px;
    }

    .model-head-score {
      font-family: var(--mono);
      font-size: 1.18rem;
      color: var(--accent-strong);
      white-space: nowrap;
    }

    #kpis,
    #standard-summary,
    #standard-analysis { display: none; }

    @media (max-width: 900px) {
      .shell { width: min(100vw - 18px, 100%); margin-top: 10px; }
      .hero, .panel, .compare-panel { border-radius: 4px; }
      .compare-controls,
      .compare-head-grid,
      .headtohead-row { grid-template-columns: 1fr; }
      .compare-toolbar-right {
        width: 100%;
        margin-left: 0;
        justify-content: stretch;
      }
      .compare-controls .control.compare-spacer { display: none; }
      .bar-row, .stack-row, .domain-row { grid-template-columns: 1fr; }
      .meta-grid { justify-items: start; }
      .hit-row,
      .hit-metrics,
      .leaderboard-row,
      .winner-top,
      .model-head-top,
      .detail-toolbar { grid-template-columns: 1fr; }
      .leaderboard-row { grid-template-columns: 1fr; }
      .segmented-toggle { width: 100%; justify-content: stretch; }
      .segmented-toggle button { flex: 1 1 0; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { transition: none !important; }
    }
  </style>
</head>
<body data-mode="__MODE__">
  <div class="shell">
    <section class="hero">
      <div class="hero-top">
        <div>
          <div class="hero-kicker">CtxSift // Benchmark Command Deck</div>
          <h1>Ctxsift Benchmark Viewer</h1>
        </div>
        <div class="meta-grid">
          <div><strong>Source</strong><span class="mono">__SOURCE__</span></div>
          <div><strong>Generated</strong><span class="mono">__GENERATED__</span></div>
        </div>
      </div>
    </section>

      <section class="compare-panel">
        <div class="compare-toolbar">
          <div>
            <h2>Head-to-Head</h2>
          </div>
          <div class="compare-toolbar-right">
            <div class="control">
              <label>Track</label>
              <div class="segmented-toggle" id="compare-track-toggle"></div>
            </div>
            <div class="compare-actions">
              <button type="button" id="compare-collapse-toggle">Collapse</button>
            </div>
          </div>
        </div>
        <div class="compare-body" id="compare-body">
          <div class="compare-controls">
            <div class="control">
              <label for="compare-left-select">Left model</label>
              <select id="compare-left-select"></select>
            </div>
            <div class="control compare-spacer" aria-hidden="true"></div>
            <div class="control">
              <label for="compare-right-select">Right model</label>
              <select id="compare-right-select"></select>
            </div>
          </div>
          <div id="head-to-head-summary"></div>
        </div>
      </section>

    <section class="grid two-up mode-collective" id="collective-overview">
      <div class="panel">
        <div class="panel-head">
          <div>
            <h2>CPU Top Score</h2>
          </div>
        </div>
        <div id="cpu-best-card"></div>
      </div>
      <div class="panel">
        <div class="panel-head">
          <div>
            <h2>GPU Top Score</h2>
          </div>
        </div>
        <div id="gpu-best-card"></div>
      </div>
    </section>

    <section class="grid two-up" id="leaderboards">
      <div class="panel">
        <div class="panel-head">
          <div>
            <h2>Latency Leaderboard</h2>
          </div>
          <div class="segmented-toggle" id="latency-track-toggle"></div>
        </div>
        <div class="leaderboard-list" id="latency-bars"></div>
      </div>
      <div class="panel">
        <div class="panel-head">
          <div>
            <h2>Score Leaderboard</h2>
          </div>
          <div class="segmented-toggle" id="score-track-toggle"></div>
        </div>
        <div class="leaderboard-list" id="quality-stacks"></div>
        <div class="legend">
          <span><i style="background: var(--success);"></i>Success</span>
          <span><i style="background: var(--danger);"></i>Error</span>
          <span><i style="background: var(--exact);"></i>Exact pass</span>
          <span><i style="background: rgba(179, 127, 255, 0.92);"></i>Preserve</span>
          <span><i style="background: var(--warn);"></i>Instruction</span>
          <span><i style="background: #ffffff;"></i>Quality</span>
        </div>
      </div>
    </section>

    <section class="grid two-up" id="standard-summary" hidden>
      <div class="panel">
        <h2>Latency By Category</h2>
        <div class="panel-note">Bar = average ask latency in seconds. White marker = p95 latency for that category.</div>
        <div class="domain-bars" id="domain-latency-bars"></div>
        <div class="chart-footnote">Categories are derived from benchmark case domains across the selected scenarios.</div>
      </div>
      <div class="panel">
        <h2>Scenario Summary</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th data-sort-table="scenario" data-sort-key="label">Scenario</th>
                <th data-sort-table="scenario" data-sort-key="track">Track</th>
                <th data-sort-table="scenario" data-sort-key="warmupMs">Warmup</th>
                <th data-sort-table="scenario" data-sort-key="avgInferenceMs">Avg s</th>
                <th data-sort-table="scenario" data-sort-key="p95InferenceMs">P95 s</th>
                <th data-sort-table="scenario" data-sort-key="finalScore">Final score</th>
                <th data-sort-table="scenario" data-sort-key="avgPreservationRatio">Avg preserve</th>
                <th data-sort-table="scenario" data-sort-key="avgQualityRatio">Avg quality</th>
                <th data-sort-table="scenario" data-sort-key="avgInstructionRatio">Avg instruction</th>
                <th data-sort-table="scenario" data-sort-key="maxPreservationRatio">Max preserve</th>
                <th data-sort-table="scenario" data-sort-key="successRate">Success</th>
                <th data-sort-table="scenario" data-sort-key="exactPassRate">Exact</th>
              </tr>
            </thead>
            <tbody id="scenario-table"></tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="grid two-up" id="standard-analysis" hidden>
      <div class="panel">
        <h2>Domain Breakdown</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th data-sort-table="domain" data-sort-key="domain">Domain</th>
                <th data-sort-table="domain" data-sort-key="caseCount">Cases</th>
                <th data-sort-table="domain" data-sort-key="errorCount">Errors</th>
                <th data-sort-table="domain" data-sort-key="avgInferenceMs">Avg s</th>
                <th data-sort-table="domain" data-sort-key="medianInferenceMs">Median s</th>
                <th data-sort-table="domain" data-sort-key="p95InferenceMs">P95 s</th>
                <th data-sort-table="domain" data-sort-key="avgPreservationRatio">Avg preserve</th>
                <th data-sort-table="domain" data-sort-key="avgQualityRatio">Avg quality</th>
                <th data-sort-table="domain" data-sort-key="avgInstructionRatio">Avg instruction</th>
              </tr>
            </thead>
            <tbody id="domain-table"></tbody>
          </table>
        </div>
      </div>
      <div class="panel">
        <h2>Slowest Asks Across Selection</h2>
        <div class="panel-note">The highest-latency asks across every selected scenario, useful for spotting worst-case prompts and domains.</div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th data-sort-table="slowest" data-sort-key="scenarioLabel">Scenario</th>
                <th data-sort-table="slowest" data-sort-key="caseLabel">Ask</th>
                <th data-sort-table="slowest" data-sort-key="domain">Domain</th>
                <th data-sort-table="slowest" data-sort-key="inferenceMs">Latency (s)</th>
                <th data-sort-table="slowest" data-sort-key="exactPreservationRatio">Preserve</th>
                <th data-sort-table="slowest" data-sort-key="summaryQualityRatio">Quality</th>
                <th data-sort-table="slowest" data-sort-key="instructionFollowingScore">Instruction</th>
                <th data-sort-table="slowest" data-sort-key="status">Status</th>
              </tr>
            </thead>
            <tbody id="slowest-case-table"></tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="panel detail-shell">
      <div class="detail-toolbar">
        <div class="control">
          <label for="scenario-select">Model detail</label>
          <select id="scenario-select"></select>
        </div>
        <div class="control">
          <label>Track</label>
          <div class="segmented-toggle" id="detail-track-toggle"></div>
        </div>
        <div class="control">
          <label>Case view</label>
          <div class="control-row" id="case-mode-buttons"></div>
        </div>
      </div>
      <div id="detail-model-header"></div>
      <div id="scenario-details"></div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th data-sort-table="cases" data-sort-key="caseLabel">Ask</th>
              <th data-sort-table="cases" data-sort-key="domain">Domain</th>
              <th data-sort-table="cases" data-sort-key="inferenceMs">Latency (s)</th>
              <th data-sort-table="cases" data-sort-key="exactPreservationRatio">Preserve</th>
              <th data-sort-table="cases" data-sort-key="summaryQualityRatio">Quality</th>
              <th data-sort-table="cases" data-sort-key="instructionFollowingScore">Instruction</th>
              <th data-sort-table="cases" data-sort-key="status">Status</th>
            </tr>
          </thead>
          <tbody id="case-table"></tbody>
        </table>
      </div>
    </section>
  </div>

  <script type="application/json" id="viewer-data">__DATA__</script>
  <script>
    const data = JSON.parse(document.getElementById("viewer-data").textContent);
    const allScenarios = data.scenarios || [];
    const failedCaseDetails = data.failedCaseDetails || {};
      const state = {
        activeScenarioKey: allScenarios[0]?.key ?? null,
        caseMode: "all",
        compareFamily: "cpu",
        compareCollapsed: false,
        compareLeftKey: null,
        compareRightKey: null,
        latencyFamily: "cpu",
        scoreFamily: "cpu",
        detailFamily: "cpu",
      tableSorts: {
        scenario: { key: null, direction: "none" },
        domain: { key: null, direction: "none" },
        slowest: { key: null, direction: "none" },
        cases: { key: null, direction: "none" },
      },
    };

    function isCollectiveMode() {
      return true;
    }

    function isMultiSourceMode() {
      return Boolean(data.multiSource);
    }

    function fmtPct(value) {
      return `${(Number(value || 0) * 100).toFixed(1)}%`;
    }

    function fmtLatency(ms) {
      return `${(Number(ms || 0) / 1000).toFixed(2)}s`;
    }

    function fmtSeconds(ms) {
      return `${(Number(ms || 0) / 1000).toFixed(2)}s`;
    }

    function fmtInt(value) {
      return new Intl.NumberFormat("en-US").format(Number(value || 0));
    }

    function fmtScore(value) {
      return Number(value || 0).toFixed(2);
    }

    function renderFatalError(error) {
      const shell = document.querySelector(".shell");
      if (!shell) {
        return;
      }
      const panel = document.createElement("section");
      panel.className = "panel";
      panel.style.borderColor = "var(--danger)";
      panel.style.padding = "16px";
      const title = document.createElement("div");
      title.style.fontWeight = "700";
      title.style.marginBottom = "8px";
      title.textContent = "Viewer bootstrap failed";
      const body = document.createElement("pre");
      body.style.whiteSpace = "pre-wrap";
      body.style.margin = "0";
      body.style.color = "var(--danger)";
      body.textContent = String(error && error.stack ? error.stack : error);
      panel.append(title, body);
      shell.prepend(panel);
    }

    function buildCaseTooltip(item) {
      const detail = failedCaseDetails[item.detailKey || ""];
      if (!detail) {
        return "";
      }
      const sections = [];
      if (detail.expectedOutput) {
        sections.push(`Expected output:\n${detail.expectedOutput}`);
      }
      if (detail.actualOutput) {
        sections.push(`Actual output:\n${detail.actualOutput}`);
      }
      if (!sections.length) {
        return "";
      }
      return sections.join("\\n\\n");
    }

    function percentile(values, fraction) {
      if (!values.length) {
        return 0;
      }
      const ordered = [...values].sort((left, right) => left - right);
      if (ordered.length === 1) {
        return ordered[0];
      }
      const rank = (ordered.length - 1) * fraction;
      const lower = Math.floor(rank);
      const upper = Math.min(lower + 1, ordered.length - 1);
      if (lower === upper) {
        return ordered[lower];
      }
      const step = rank - lower;
      return ordered[lower] + (ordered[upper] - ordered[lower]) * step;
    }

    function median(values) {
      return percentile(values, 0.5);
    }

    function scenarioLabel(scenario) {
      return scenario.name;
    }

    function displayModelName(model) {
      const value = String(model || "").trim();
      if (!value) {
        return "Unknown model";
      }
      const parts = value.split("/").filter(Boolean);
      return parts[parts.length - 1] || value;
    }

    function emptyState(message) {
      const wrap = document.createElement("div");
      wrap.className = "empty-state";
      const copy = document.createElement("div");
      copy.className = "empty-copy";
      copy.textContent = message;
      wrap.append(copy);
      return wrap;
    }

    function emptyRow(message, colspan) {
      const row = document.createElement("tr");
      const cell = document.createElement("td");
      cell.colSpan = colspan;
      cell.append(emptyState(message));
      row.append(cell);
      return row;
    }

    function textCell(value, className) {
      const cell = document.createElement("td");
      cell.textContent = value;
      if (className) {
        cell.className = className;
      }
      return cell;
    }

    function buildBadge(label, tone) {
      const badge = document.createElement("span");
      badge.className = `badge${tone ? ` ${tone}` : ""}`;
      badge.textContent = label;
      return badge;
    }

    function compareValues(left, right) {
      if (typeof left === "number" && typeof right === "number") {
        return left - right;
      }
      return String(left ?? "").localeCompare(String(right ?? ""), undefined, { numeric: true, sensitivity: "base" });
    }

    function sortRows(rows, tableId, accessors) {
      const sortState = state.tableSorts[tableId];
      if (!sortState || !sortState.key || sortState.direction === "none") {
        return [...rows];
      }
      const accessor = accessors[sortState.key];
      if (!accessor) {
        return [...rows];
      }
      const multiplier = sortState.direction === "ascending" ? 1 : -1;
      return [...rows].sort((left, right) => {
        const primary = compareValues(accessor(left), accessor(right));
        if (primary !== 0) {
          return primary * multiplier;
        }
        return compareValues(JSON.stringify(left), JSON.stringify(right));
      });
    }

    function cycleSort(tableId, key) {
      const sortState = state.tableSorts[tableId];
      if (sortState.key !== key) {
        sortState.key = key;
        sortState.direction = "ascending";
      } else if (sortState.direction === "ascending") {
        sortState.direction = "descending";
      } else if (sortState.direction === "descending") {
        sortState.direction = "none";
        sortState.key = null;
      } else {
        sortState.direction = "ascending";
      }
      renderDashboard();
    }

    function initSortableHeaders() {
      document.querySelectorAll("th[data-sort-table][data-sort-key]").forEach((header) => {
        if (header.dataset.sortInit === "true") {
          return;
        }
        header.dataset.sortInit = "true";
        header.setAttribute("aria-sort", "none");
        const tableId = header.dataset.sortTable;
        const key = header.dataset.sortKey;
        const label = header.textContent;
        header.replaceChildren();
        const button = document.createElement("button");
        button.type = "button";
        button.className = "sort-button";
        button.textContent = label;
        button.addEventListener("click", () => cycleSort(tableId, key));
        header.append(button);
      });
    }

    function renderSortableHeaders() {
      document.querySelectorAll("th[data-sort-table][data-sort-key]").forEach((header) => {
        const sortState = state.tableSorts[header.dataset.sortTable];
        if (sortState.key === header.dataset.sortKey) {
          header.setAttribute("aria-sort", sortState.direction);
        } else {
          header.setAttribute("aria-sort", "none");
        }
      });
    }

    function familyLabel(family) {
      return String(family || "other").toUpperCase();
    }

    function availableFamilies() {
      return ["cpu", "gpu", "remote"].filter((family) => allScenarios.some((scenario) => scenario.family === family));
    }

    function normalizeFamily(family) {
      const families = availableFamilies();
      if (families.includes(family)) {
        return family;
      }
      return families[0] || "cpu";
    }

    function familyScenarios(family, allowFallback = true) {
      const resolved = allowFallback ? normalizeFamily(family) : family;
      return allScenarios.filter((scenario) => scenario.family === resolved);
    }

    function rankedFamilyScenarios(family) {
      return [...familyScenarios(family)].sort((left, right) => compareScenariosByRule(left, right, "final-score"));
    }

    function getCompareScenarios() {
      return rankedFamilyScenarios(state.compareFamily);
    }

    function getDetailScenarios() {
      return familyScenarios(state.detailFamily);
    }

    function ensureActiveScenario() {
      state.compareFamily = normalizeFamily(state.compareFamily);
      state.latencyFamily = normalizeFamily(state.latencyFamily);
      state.scoreFamily = normalizeFamily(state.scoreFamily);
      state.detailFamily = normalizeFamily(state.detailFamily);
      const visibleKeys = new Set(getDetailScenarios().map((scenario) => scenario.key));
      if (state.activeScenarioKey && visibleKeys.has(state.activeScenarioKey)) {
        return;
      }
      const best = [...getDetailScenarios()].sort((left, right) => compareScenariosByRule(left, right, "final-score"))[0];
      state.activeScenarioKey = best?.key ?? null;
    }

    function ensureHeadToHeadSelection(preferredSide = "left") {
      const scenarios = getCompareScenarios();
      if (!scenarios.length) {
        state.compareLeftKey = null;
        state.compareRightKey = null;
        return;
      }
      const availableKeys = new Set(scenarios.map((scenario) => scenario.key));
      if (!state.compareLeftKey || !availableKeys.has(state.compareLeftKey)) {
        state.compareLeftKey = scenarios[0]?.key ?? null;
      }
      if (scenarios.length < 2) {
        state.compareRightKey = null;
        return;
      }
      if (!state.compareRightKey || !availableKeys.has(state.compareRightKey)) {
        state.compareRightKey = scenarios.find((scenario) => scenario.key !== state.compareLeftKey)?.key ?? null;
      }
      if (state.compareLeftKey === state.compareRightKey) {
        if (preferredSide === "right") {
          state.compareLeftKey = scenarios.find((scenario) => scenario.key !== state.compareRightKey)?.key ?? state.compareLeftKey;
        } else {
          state.compareRightKey = scenarios.find((scenario) => scenario.key !== state.compareLeftKey)?.key ?? state.compareRightKey;
        }
      }
    }

    function setActiveScenario(scenario) {
      if (!scenario) {
        return;
      }
      state.detailFamily = normalizeFamily(scenario.family);
      state.activeScenarioKey = scenario.key;
      renderDashboard();
    }

    function scenarioOptionLabel(scenario) {
      if (isMultiSourceMode()) {
        return `${scenarioLabel(scenario)} • ${scenario.runLabel}`;
      }
      return scenarioLabel(scenario);
    }

    function compareScenariosByRule(left, right, rule) {
      const comparisons = {
        "exact-first": [
          [right.exactPassRate, left.exactPassRate],
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.successRate, left.successRate],
          [left.avgInferenceMs, right.avgInferenceMs],
        ],
        "final-score": [
          [right.finalScore, left.finalScore],
          [right.avgPreservationRatio, left.avgPreservationRatio],
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.successRate, left.successRate],
          [left.avgInferenceMs, right.avgInferenceMs],
        ],
        "success-first": [
          [right.successRate, left.successRate],
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.exactPassRate, left.exactPassRate],
          [left.avgInferenceMs, right.avgInferenceMs],
        ],
        "instruction-first": [
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.exactPassRate, left.exactPassRate],
          [right.successRate, left.successRate],
          [left.avgInferenceMs, right.avgInferenceMs],
        ],
        "quality-first": [
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.exactPassRate, left.exactPassRate],
          [right.successRate, left.successRate],
          [left.avgInferenceMs, right.avgInferenceMs],
        ],
        "latency-first": [
          [left.avgInferenceMs, right.avgInferenceMs],
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.exactPassRate, left.exactPassRate],
          [right.successRate, left.successRate],
        ],
        "max-preserve-first": [
          [right.maxPreservationRatio, left.maxPreservationRatio],
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.exactPassRate, left.exactPassRate],
          [right.successRate, left.successRate],
        ],
        "preserve-first": [
          [right.avgPreservationRatio, left.avgPreservationRatio],
          [right.avgInstructionRatio, left.avgInstructionRatio],
          [right.avgQualityRatio, left.avgQualityRatio],
          [right.exactPassRate, left.exactPassRate],
          [right.successRate, left.successRate],
        ],
      };
      const pairList = comparisons[rule] || comparisons["exact-first"];
      for (const [first, second] of pairList) {
        const delta = compareValues(first, second);
        if (delta !== 0) {
          return delta;
        }
      }
      return scenarioLabel(left).localeCompare(scenarioLabel(right), undefined, { numeric: true, sensitivity: "base" });
    }

    function pickBestScenario(scenarios, rule = "final-score") {
      if (!scenarios.length) {
        return null;
      }
      return [...scenarios].sort((left, right) => compareScenariosByRule(left, right, rule))[0];
    }

    function rankLatencyRows(scenarios) {
      return [...scenarios].sort((left, right) => compareValues(left.avgInferenceMs, right.avgInferenceMs) || scenarioLabel(left).localeCompare(scenarioLabel(right)));
    }

    function rankAccuracyRows(scenarios) {
      return [...scenarios].sort((left, right) => compareValues(right.avgInstructionRatio, left.avgInstructionRatio) || compareValues(right.avgQualityRatio, left.avgQualityRatio) || compareValues(right.exactPassRate, left.exactPassRate) || compareValues(right.successRate, left.successRate) || scenarioLabel(left).localeCompare(scenarioLabel(right)));
    }

    function computeKpis(scenarios) {
      const caseCount = scenarios.reduce((sum, scenario) => sum + scenario.caseCount, 0);
      const errorCount = scenarios.reduce((sum, scenario) => sum + scenario.errorCount, 0);
      const exactHits = scenarios.reduce((sum, scenario) => sum + scenario.exactPassCount, 0);
      const avgLatencyMs = scenarios.length ? scenarios.reduce((sum, scenario) => sum + scenario.avgInferenceMs, 0) / scenarios.length : 0;
      const avgQuality = scenarios.length ? scenarios.reduce((sum, scenario) => sum + scenario.avgQualityRatio, 0) / scenarios.length : 0;
      return [
        ["Active scenarios", fmtInt(scenarios.length)],
        ["Total asks", fmtInt(caseCount)],
        ["Average latency", fmtLatency(avgLatencyMs)],
        ["Average quality", fmtPct(avgQuality)],
        ["Errors", fmtInt(errorCount)],
        ["Exact hits", fmtInt(exactHits)],
      ];
    }

    function computeDomainRows(scenarios) {
      const domainMap = new Map();
      scenarios.forEach((scenario) => {
        scenario.cases.forEach((item) => {
          if (!domainMap.has(item.domain)) {
            domainMap.set(item.domain, { domain: item.domain, cases: [] });
          }
          domainMap.get(item.domain).cases.push(item);
        });
      });
      return [...domainMap.values()].map((entry) => {
        const inference = entry.cases.map((item) => item.inferenceMs).filter((value) => value > 0);
        const preserve = entry.cases.map((item) => item.exactPreservationRatio);
        const quality = entry.cases.map((item) => item.summaryQualityRatio);
        const instruction = entry.cases.map((item) => item.instructionFollowingScore);
        const errorCount = entry.cases.filter((item) => item.error).length;
        return {
          domain: entry.domain,
          caseCount: entry.cases.length,
          errorCount,
          avgInferenceMs: inference.length ? inference.reduce((sum, value) => sum + value, 0) / inference.length : 0,
          medianInferenceMs: median(inference),
          p95InferenceMs: percentile(inference, 0.95),
          avgPreservationRatio: preserve.length ? preserve.reduce((sum, value) => sum + value, 0) / preserve.length : 0,
          avgQualityRatio: quality.length ? quality.reduce((sum, value) => sum + value, 0) / quality.length : 0,
          avgInstructionRatio: instruction.length ? instruction.reduce((sum, value) => sum + value, 0) / instruction.length : 0,
        };
      }).sort((left, right) => compareValues(right.avgInferenceMs, left.avgInferenceMs));
    }

    function computeSlowestCases(scenarios) {
      return scenarios.flatMap((scenario) => scenario.cases.map((item) => ({
        scenarioKey: scenario.key,
        scenarioLabel: scenarioLabel(scenario),
        scenarioTrack: scenario.track,
        runLabel: scenario.runLabel,
        caseId: item.caseId,
        title: item.title,
        domain: item.domain,
        inferenceMs: item.inferenceMs,
        exactPreservationRatio: item.exactPreservationRatio,
        summaryQualityRatio: item.summaryQualityRatio,
        instructionFollowingScore: item.instructionFollowingScore,
        error: item.error,
        status: item.status,
      }))).sort((left, right) => compareValues(right.inferenceMs, left.inferenceMs)).slice(0, 14);
    }

    function renderScenarioPicker() {
      const picker = document.getElementById("scenario-picker");
      picker.replaceChildren(...allScenarios.map((scenario) => {
        const label = document.createElement("label");
        const isSelected = state.selectedScenarioKeys.has(scenario.key);
        label.className = `scenario-option${isSelected ? " active" : ""}`;

        const head = document.createElement("div");
        head.className = "scenario-option-head";
        const titleWrap = document.createElement("div");
        const title = document.createElement("div");
        title.className = "scenario-option-title";
        title.textContent = scenarioLabel(scenario);
        const subtitle = document.createElement("div");
        subtitle.className = "scenario-subtitle";
        subtitle.textContent = `${displayModelName(scenario.model)} • ${scenario.track} • ${scenario.phase}`;
        titleWrap.append(title, subtitle);

        const toggle = document.createElement("input");
        toggle.type = "checkbox";
        toggle.checked = isSelected;
        toggle.setAttribute("aria-label", `Compare ${scenarioLabel(scenario)}`);
        toggle.addEventListener("change", () => {
          const next = new Set(state.selectedScenarioKeys);
          if (toggle.checked) {
            next.add(scenario.key);
          } else {
            next.delete(scenario.key);
          }
          setScenarioSelection(next);
        });

        head.append(titleWrap, toggle);
        const badges = document.createElement("div");
        badges.className = "badge-row";
        const badgeNodes = [
          buildBadge(scenario.track, "accent"),
          isMultiSourceMode() ? buildBadge(scenario.runLabel) : null,
          buildBadge(scenario.quantization),
          buildBadge(fmtLatency(scenario.avgInferenceMs), "warn"),
          buildBadge(`${fmtPct(scenario.successRate)} success`, scenario.errorCount ? "danger" : "accent"),
        ].filter(Boolean);
        badges.append(...badgeNodes);
        label.append(head, badges);
        return label;
      }));
    }

    function headToHeadMetrics() {
      return [
        { label: "Final score", key: "finalScore", kind: "higher", format: fmtScore },
        { label: "Quality core", key: "qualityCore", kind: "higher", format: fmtPct },
        { label: "Latency factor", key: "latencyFactor", kind: "higher", format: (value) => Number(value || 0).toFixed(3) },
        { label: "Warmup", key: "warmupMs", kind: "lower", format: fmtSeconds },
        { label: "Avg latency", key: "avgInferenceMs", kind: "lower", format: fmtLatency },
        { label: "P95 latency", key: "p95InferenceMs", kind: "lower", format: fmtLatency },
        { label: "Avg preserve", key: "avgPreservationRatio", kind: "higher", format: fmtPct },
        { label: "Avg quality", key: "avgQualityRatio", kind: "higher", format: fmtPct },
        { label: "Avg format", key: "avgFormatRatio", kind: "higher", format: fmtPct },
        { label: "Avg instruction", key: "avgInstructionRatio", kind: "higher", format: fmtPct },
        { label: "Avg brevity", key: "avgBrevityRatio", kind: "higher", format: fmtPct },
        { label: "Avg case score", key: "avgCaseScore", kind: "higher", format: fmtPct },
        { label: "P10 case score", key: "p10CaseScore", kind: "higher", format: fmtPct },
        { label: "Success", key: "successRate", kind: "higher", format: fmtPct },
        { label: "Exact", key: "exactPassRate", kind: "higher", format: fmtPct },
        { label: "Errors", key: "errorCount", kind: "lower", format: fmtInt },
        { label: "Case volume", key: "caseCount", kind: "neutral", format: fmtInt },
      ];
    }

    function renderHeadToHeadSelectors() {
      renderTrackToggle("compare-track-toggle", "compareFamily");
      const scenarios = getCompareScenarios();
      const leftSelect = document.getElementById("compare-left-select");
      const rightSelect = document.getElementById("compare-right-select");

      if (!scenarios.length) {
        const leftOption = document.createElement("option");
        leftOption.textContent = "No scenario available";
        leftOption.disabled = true;
        leftOption.selected = true;
        const rightOption = leftOption.cloneNode(true);
        leftSelect.replaceChildren(leftOption);
        rightSelect.replaceChildren(rightOption);
        leftSelect.disabled = true;
        rightSelect.disabled = true;
        return;
      }

      leftSelect.disabled = false;
      rightSelect.disabled = scenarios.length < 2;

      leftSelect.replaceChildren(...scenarios.map((scenario) => {
        const option = document.createElement("option");
        option.value = scenario.key;
        option.selected = scenario.key === state.compareLeftKey;
        option.textContent = scenarioOptionLabel(scenario);
        return option;
      }));

      if (scenarios.length < 2) {
        const option = document.createElement("option");
        option.textContent = "Need a second scenario";
        option.disabled = true;
        option.selected = true;
        rightSelect.replaceChildren(option);
        return;
      }

      rightSelect.replaceChildren(...scenarios.map((scenario) => {
        const option = document.createElement("option");
        option.value = scenario.key;
        option.selected = scenario.key === state.compareRightKey;
        option.textContent = scenarioOptionLabel(scenario);
        return option;
      }));
    }

    function renderCompareCollapse() {
      const toggle = document.getElementById("compare-collapse-toggle");
      const body = document.getElementById("compare-body");
      if (!toggle || !body) {
        return;
      }
      body.hidden = state.compareCollapsed;
      toggle.textContent = state.compareCollapsed ? "Expand" : "Collapse";
      toggle.setAttribute("aria-expanded", String(!state.compareCollapsed));
    }

    function compareWinnerClass(leftValue, rightValue, kind) {
      if (kind === "neutral") {
        return ["is-tie", "is-tie"];
      }
      if (leftValue === rightValue) {
        return ["is-tie", "is-tie"];
      }
      const leftWins = kind === "lower" ? leftValue < rightValue : leftValue > rightValue;
      return leftWins ? ["is-better", "is-worse"] : ["is-worse", "is-better"];
    }

    function buildCompareCard(scenario, sideLabel) {
      const card = document.createElement("div");
      card.className = "compare-card";

      const top = document.createElement("div");
      top.className = "compare-card-top";

      const copy = document.createElement("div");
      copy.className = "compare-card-copy";
      const title = document.createElement("div");
      title.className = "compare-card-title";
      title.textContent = displayModelName(scenario.model);
      copy.append(title);

      const score = document.createElement("div");
      score.className = "compare-card-score";
      score.textContent = fmtScore(scenario.finalScore);

      top.append(copy, score);

      const badges = document.createElement("div");
      badges.className = "badge-row";
      badges.append(
        buildBadge(`${fmtPct(scenario.successRate)} success`, scenario.errorCount ? "danger" : "accent"),
        buildBadge(`${fmtPct(scenario.exactPassRate)} exact`, ""),
        buildBadge(fmtLatency(scenario.avgInferenceMs), "warn"),
      );

      card.append(top, badges);
      return card;
    }

    function renderHeadToHead() {
      renderHeadToHeadSelectors();
      const root = document.getElementById("head-to-head-summary");
      const scenarios = getCompareScenarios();
      if (scenarios.length < 2) {
        root.replaceChildren(emptyState("Pick a track with at least two scenarios to compare head-to-head."));
        return;
      }

      const left = scenarios.find((scenario) => scenario.key === state.compareLeftKey);
      const right = scenarios.find((scenario) => scenario.key === state.compareRightKey);
      if (!left || !right) {
        root.replaceChildren(emptyState("Select two scenarios to compare."));
        return;
      }

      const wrap = document.createElement("div");
      wrap.className = "grid";

      const header = document.createElement("div");
      header.className = "compare-head-grid";
      const versus = document.createElement("div");
      versus.className = "compare-versus";
      versus.textContent = "vs";
      header.append(
        buildCompareCard(left, "Left"),
        versus,
        buildCompareCard(right, "Right"),
      );

      const metrics = document.createElement("div");
      metrics.className = "headtohead-metrics";
      metrics.append(...headToHeadMetrics().map((metric) => {
        const row = document.createElement("div");
        row.className = "headtohead-row";
        const [leftClass, rightClass] = compareWinnerClass(left[metric.key], right[metric.key], metric.kind);

        const leftValue = document.createElement("div");
        leftValue.className = `headtohead-value ${leftClass}`;
        const leftSmall = document.createElement("small");
        leftSmall.textContent = scenarioLabel(left);
        const leftStrong = document.createElement("strong");
        leftStrong.textContent = metric.format(left[metric.key]);
        leftValue.append(leftSmall, leftStrong);

        const label = document.createElement("div");
        label.className = "headtohead-label";
        label.textContent = metric.label;

        const rightValue = document.createElement("div");
        rightValue.className = `headtohead-value ${rightClass}`;
        const rightSmall = document.createElement("small");
        rightSmall.textContent = scenarioLabel(right);
        const rightStrong = document.createElement("strong");
        rightStrong.textContent = metric.format(right[metric.key]);
        rightValue.append(rightSmall, rightStrong);

        row.append(leftValue, label, rightValue);
        return row;
      }));

      wrap.append(header, metrics);
      root.replaceChildren(wrap);
    }

    function renderScenarioPicker() {
      return null;
    }

    function renderKpis(scenarios) {
      const root = document.getElementById("kpis");
      root.replaceChildren(...computeKpis(scenarios).map(([label, value]) => {
        const card = document.createElement("div");
        card.className = "kpi";
        const labelNode = document.createElement("div");
        labelNode.className = "kpi-label";
        labelNode.textContent = label;
        const valueNode = document.createElement("div");
        valueNode.className = "kpi-value";
        valueNode.textContent = value;
        card.append(labelNode, valueNode);
        return card;
      }));
    }

    function renderTrackToggle(rootId, stateKey) {
      const root = document.getElementById(rootId);
      const families = ["cpu", "gpu", "remote"];
      root.replaceChildren(...families.map((family) => {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = familyLabel(family);
        button.disabled = !allScenarios.some((scenario) => scenario.family === family);
        button.dataset.active = String(state[stateKey] === family);
        button.addEventListener("click", () => {
          if (button.disabled) {
            return;
          }
          state[stateKey] = family;
          ensureActiveScenario();
          renderDashboard();
        });
        return button;
      }));
    }

    function renderTrackWinner(rootId, family) {
      const root = document.getElementById(rootId);
      const scenarios = familyScenarios(family, false);
      const best = pickBestScenario(scenarios, "final-score");
      if (!best) {
        root.replaceChildren(emptyState(`No ${familyLabel(family)} scenarios were found in this result set.`));
        return;
      }

      const card = document.createElement("div");
      card.className = "winner-card";
      card.addEventListener("click", () => setActiveScenario(best));

      const top = document.createElement("div");
      top.className = "winner-top";
      const copy = document.createElement("div");
      const scenarioKicker = document.createElement("div");
      scenarioKicker.className = "winner-scenario";
      scenarioKicker.textContent = scenarioLabel(best);
      const model = document.createElement("div");
      model.className = "winner-model";
      model.textContent = displayModelName(best.model);
      copy.append(scenarioKicker, model);

      const scoreStack = document.createElement("div");
      scoreStack.className = "score-stack";
      const score = document.createElement("div");
      score.className = "score-chip warn";
      score.textContent = `Score ${fmtScore(best.finalScore)}`;
      const scoreFormula = document.createElement("div");
      scoreFormula.className = "score-formula";
      scoreFormula.textContent = "100 x quality_core x latency, where quality_core = 0.80 x mean(case_score) + 0.20 x p10(case_score)";
      scoreStack.append(score, scoreFormula);
      top.append(copy, scoreStack);

      const stats = document.createElement("div");
      stats.className = "winner-stats";
      [
        ["Success / exact", `${fmtPct(best.successRate)} / ${fmtPct(best.exactPassRate)}`],
        ["Avg / p95 latency", `${fmtLatency(best.avgInferenceMs)} / ${fmtLatency(best.p95InferenceMs)}`],
        ["Preserve", `${fmtPct(best.avgPreservationRatio)} avg • ${fmtPct(best.maxPreservationRatio)} max`],
        ["Quality core / latency", `${fmtPct(best.qualityCore)} / ${best.latencyFactor.toFixed(3)}`],
        ["Quality / format", `${fmtPct(best.avgQualityRatio)} / ${fmtPct(best.avgFormatRatio)}`],
        ["Instruction / brevity", `${fmtPct(best.avgInstructionRatio)} / ${fmtPct(best.avgBrevityRatio)}`],
      ].forEach(([label, value]) => {
        const item = document.createElement("div");
        item.className = "detail-item";
        const small = document.createElement("small");
        small.textContent = label;
        const strong = document.createElement("strong");
        strong.textContent = value;
        item.append(small, strong);
        stats.append(item);
      });
      card.append(top, stats);
      root.replaceChildren(card);
    }

    function renderCollectiveOverview() {
      renderTrackWinner("cpu-best-card", "cpu");
      renderTrackWinner("gpu-best-card", "gpu");
    }

    function renderLatencyBars() {
      renderTrackToggle("latency-track-toggle", "latencyFamily");
      const root = document.getElementById("latency-bars");
      const scenarios = familyScenarios(state.latencyFamily);
      if (!scenarios.length) {
        root.replaceChildren(emptyState("No scenarios selected."));
        return;
      }
      const ordered = rankLatencyRows(scenarios);
      const maxP95 = Math.max(...ordered.map((item) => item.p95InferenceMs), 1);
      root.replaceChildren(...ordered.map((scenario) => {
        const row = document.createElement("button");
        row.type = "button";
        row.className = "leaderboard-row";
        row.title = scenarioLabel(scenario);
        row.addEventListener("click", () => setActiveScenario(scenario));

        const copy = document.createElement("div");
        copy.className = "leaderboard-copy";
        const model = document.createElement("strong");
        model.className = "leaderboard-model";
        model.textContent = displayModelName(scenario.model);
        const meta = document.createElement("span");
        meta.className = "leaderboard-meta";
        meta.textContent = scenarioLabel(scenario);
        copy.append(model, meta);

        const railWrap = document.createElement("div");
        railWrap.className = "leaderboard-rail-wrap";
        const rail = document.createElement("div");
        rail.className = "metric-rail";
        const fill = document.createElement("div");
        fill.className = "metric-fill";
        fill.style.width = `${Math.max(2, (scenario.avgInferenceMs / maxP95) * 100)}%`;
        const marker = document.createElement("div");
        marker.className = "metric-marker";
        marker.style.left = `${Math.max(2, (scenario.p95InferenceMs / maxP95) * 100)}%`;
        rail.append(fill, marker);

        const caption = document.createElement("div");
        caption.className = "leaderboard-rail-caption";
        caption.replaceChildren(
          buildBadge(`${fmtPct(scenario.successRate)} success`, scenario.errorCount ? "danger" : "accent"),
          buildBadge(`${fmtPct(scenario.exactPassRate)} exact`, ""),
        );
        railWrap.append(rail, caption);

        const value = document.createElement("div");
        value.className = "leaderboard-value dim";
        value.textContent = `${fmtLatency(scenario.avgInferenceMs)} / ${fmtLatency(scenario.p95InferenceMs)}`;
        row.append(copy, railWrap, value);
        return row;
      }));
    }

    function renderQualityStacks() {
      renderTrackToggle("score-track-toggle", "scoreFamily");
      const root = document.getElementById("quality-stacks");
      const scenarios = familyScenarios(state.scoreFamily);
      if (!scenarios.length) {
        root.replaceChildren(emptyState("No scenarios selected."));
        return;
      }
      const ordered = [...scenarios].sort((left, right) => compareScenariosByRule(left, right, "final-score"));
      root.replaceChildren(...ordered.map((scenario) => {
        const row = document.createElement("button");
        row.type = "button";
        row.className = "leaderboard-row";
        row.title = scenarioLabel(scenario);
        row.addEventListener("click", () => setActiveScenario(scenario));

        const copy = document.createElement("div");
        copy.className = "leaderboard-copy";
        const model = document.createElement("strong");
        model.className = "leaderboard-model";
        model.textContent = displayModelName(scenario.model);
        const meta = document.createElement("span");
        meta.className = "leaderboard-meta";
        meta.textContent = scenarioLabel(scenario);
        copy.append(model, meta);

        const railWrap = document.createElement("div");
        railWrap.className = "leaderboard-rail-wrap";
        const rail = document.createElement("div");
        rail.className = "distribution-rail";

        const successFill = document.createElement("div");
        successFill.className = "distribution-segment success";
        successFill.style.left = "0%";
        successFill.style.width = `${Math.max(0, scenario.successRate * 100)}%`;

        const errorFill = document.createElement("div");
        errorFill.className = "distribution-segment error";
        errorFill.style.left = `${Math.max(0, scenario.successRate * 100)}%`;
        errorFill.style.width = `${Math.max(0, (1 - scenario.successRate) * 100)}%`;

        const exactBand = document.createElement("div");
        exactBand.className = "distribution-band exact";
        exactBand.style.left = `${Math.max(0, scenario.exactPassRate * 100)}%`;

        const preserveBand = document.createElement("div");
        preserveBand.className = "distribution-band preserve";
        preserveBand.style.left = `${Math.max(0, scenario.avgPreservationRatio * 100)}%`;

        const instructionBand = document.createElement("div");
        instructionBand.className = "distribution-band instruction";
        instructionBand.style.left = `${Math.max(0, scenario.avgInstructionRatio * 100)}%`;

        const qualityBand = document.createElement("div");
        qualityBand.className = "distribution-band quality";
        qualityBand.style.left = `${Math.max(0, scenario.avgQualityRatio * 100)}%`;

        rail.append(successFill, errorFill, exactBand, preserveBand, instructionBand, qualityBand);

        const caption = document.createElement("div");
        caption.className = "leaderboard-rail-caption";
        [
          `preserve ${fmtPct(scenario.avgPreservationRatio)}`,
          `instruction ${fmtPct(scenario.avgInstructionRatio)}`,
          `quality ${fmtPct(scenario.avgQualityRatio)}`,
        ].forEach((text) => {
          const span = document.createElement("span");
          span.textContent = text;
          caption.append(span);
        });
        railWrap.append(rail, caption);

        const value = document.createElement("div");
        value.className = "leaderboard-value";
        value.textContent = fmtScore(scenario.finalScore);
        row.append(copy, railWrap, value);
        return row;
      }));
    }

    function renderDomainLatencyBars(scenarios) {
      const root = document.getElementById("domain-latency-bars");
      const rows = computeDomainRows(scenarios);
      if (!rows.length) {
        root.replaceChildren(emptyState("No domain data available for the current selection."));
        return;
      }
      const maxP95 = Math.max(...rows.map((item) => item.p95InferenceMs), 1);
      root.replaceChildren(...rows.map((item) => {
        const row = document.createElement("div");
        row.className = "domain-row";
        const label = document.createElement("div");
        label.className = "domain-label";
        const name = document.createElement("strong");
        name.textContent = item.domain;
        const meta = document.createElement("span");
        meta.textContent = `${item.caseCount} asks • ${item.errorCount} errors`;
        label.append(name, meta);

        const rail = document.createElement("div");
        rail.className = "metric-rail";
        const fill = document.createElement("div");
        fill.className = "metric-fill";
        fill.style.width = `${Math.max(2, (item.avgInferenceMs / maxP95) * 100)}%`;
        const marker = document.createElement("div");
        marker.className = "metric-marker";
        marker.style.left = `${Math.max(2, (item.p95InferenceMs / maxP95) * 100)}%`;
        rail.append(fill, marker);

        const value = document.createElement("div");
        value.className = "mono";
        value.textContent = `${fmtLatency(item.avgInferenceMs)} • ${fmtLatency(item.p95InferenceMs)}`;
        row.append(label, rail, value);
        return row;
      }));
    }

    function renderScenarioTable(scenarios) {
      const root = document.getElementById("scenario-table");
      if (!scenarios.length) {
        root.replaceChildren(emptyRow("No scenarios selected for comparison.", 11));
        return;
      }
      const rows = sortRows(scenarios, "scenario", {
        label: (item) => scenarioLabel(item),
        track: (item) => item.track,
        warmupMs: (item) => item.warmupMs,
        avgInferenceMs: (item) => item.avgInferenceMs,
        p95InferenceMs: (item) => item.p95InferenceMs,
        finalScore: (item) => item.finalScore,
        avgPreservationRatio: (item) => item.avgPreservationRatio,
        avgQualityRatio: (item) => item.avgQualityRatio,
        avgInstructionRatio: (item) => item.avgInstructionRatio,
        maxPreservationRatio: (item) => item.maxPreservationRatio,
        successRate: (item) => item.successRate,
        exactPassRate: (item) => item.exactPassRate,
      });
      root.replaceChildren(...rows.map((item) => {
        const row = document.createElement("tr");
        row.className = `click-row${item.key === state.activeScenarioKey ? " active-row" : ""}`;
        row.tabIndex = 0;
        row.addEventListener("click", () => {
          state.activeScenarioKey = item.key;
          renderScenarioTable(scenarios);
          renderScenarioSelector();
          renderScenarioDetail();
        });
        row.addEventListener("keydown", (event) => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            row.click();
          }
        });
        row.append(
          textCell(scenarioLabel(item), "mono"),
          textCell(item.track),
          textCell(fmtSeconds(item.warmupMs)),
          textCell(fmtLatency(item.avgInferenceMs)),
          textCell(fmtLatency(item.p95InferenceMs)),
          textCell(fmtScore(item.finalScore)),
          textCell(fmtPct(item.avgPreservationRatio)),
          textCell(fmtPct(item.avgQualityRatio)),
          textCell(fmtPct(item.avgInstructionRatio)),
          textCell(fmtPct(item.maxPreservationRatio)),
          textCell(fmtPct(item.successRate)),
          textCell(fmtPct(item.exactPassRate)),
        );
        return row;
      }));
    }

    function renderDomainTable(scenarios) {
      const root = document.getElementById("domain-table");
      const rows = computeDomainRows(scenarios);
      if (!rows.length) {
        root.replaceChildren(emptyRow("No domain data available for the current selection.", 9));
        return;
      }
      const sorted = sortRows(rows, "domain", {
        domain: (item) => item.domain,
        caseCount: (item) => item.caseCount,
        errorCount: (item) => item.errorCount,
        avgInferenceMs: (item) => item.avgInferenceMs,
        medianInferenceMs: (item) => item.medianInferenceMs,
        p95InferenceMs: (item) => item.p95InferenceMs,
        avgPreservationRatio: (item) => item.avgPreservationRatio,
        avgQualityRatio: (item) => item.avgQualityRatio,
        avgInstructionRatio: (item) => item.avgInstructionRatio,
      });
      root.replaceChildren(...sorted.map((item) => {
        const row = document.createElement("tr");
        row.append(
          textCell(item.domain, "mono"),
          textCell(fmtInt(item.caseCount)),
          textCell(fmtInt(item.errorCount)),
          textCell(fmtLatency(item.avgInferenceMs)),
          textCell(fmtLatency(item.medianInferenceMs)),
          textCell(fmtLatency(item.p95InferenceMs)),
          textCell(fmtPct(item.avgPreservationRatio)),
          textCell(fmtPct(item.avgQualityRatio)),
          textCell(fmtPct(item.avgInstructionRatio)),
        );
        return row;
      }));
    }

    function renderSlowestCasesTable(scenarios) {
      const root = document.getElementById("slowest-case-table");
      const rows = computeSlowestCases(scenarios);
      if (!rows.length) {
        root.replaceChildren(emptyRow("No case data available for the current selection.", 8));
        return;
      }
      const sorted = sortRows(rows, "slowest", {
        scenarioLabel: (item) => item.scenarioLabel,
        caseLabel: (item) => `${item.caseId} ${item.title}`,
        domain: (item) => item.domain,
        inferenceMs: (item) => item.inferenceMs,
        exactPreservationRatio: (item) => item.exactPreservationRatio,
        summaryQualityRatio: (item) => item.summaryQualityRatio,
        instructionFollowingScore: (item) => item.instructionFollowingScore,
        status: (item) => item.status,
      });
      root.replaceChildren(...sorted.map((item) => {
        const row = document.createElement("tr");
        const scenarioCell = document.createElement("td");
        const scenarioName = document.createElement("div");
        scenarioName.className = "mono";
        scenarioName.textContent = item.scenarioLabel;
        const scenarioTrack = document.createElement("div");
        scenarioTrack.style.color = "var(--muted)";
        scenarioTrack.textContent = item.runLabel ? `${item.scenarioTrack} • ${item.runLabel}` : item.scenarioTrack;
        scenarioCell.append(scenarioName, scenarioTrack);

        const askCell = document.createElement("td");
        const askId = document.createElement("div");
        askId.className = "mono";
        askId.textContent = item.caseId;
        const askTitle = document.createElement("div");
        askTitle.style.color = "var(--muted)";
        askTitle.textContent = item.title;
        askCell.append(askId, askTitle);

        row.append(
          scenarioCell,
          askCell,
          textCell(item.domain, "mono"),
          textCell(fmtLatency(item.inferenceMs)),
          textCell(fmtPct(item.exactPreservationRatio)),
          textCell(fmtPct(item.summaryQualityRatio)),
          textCell(fmtPct(item.instructionFollowingScore)),
          textCell(item.error ? "error" : "ok", item.error ? "status-error" : "status-ok"),
        );
        return row;
      }));
    }

    function renderScenarioSelector() {
      const select = document.getElementById("scenario-select");
      const scenarios = [...getDetailScenarios()].sort((left, right) => compareScenariosByRule(left, right, "final-score"));
      if (!scenarios.length) {
        const option = document.createElement("option");
        option.textContent = "No scenario selected";
        option.disabled = true;
        option.selected = true;
        select.replaceChildren(option);
        select.disabled = true;
        return;
      }
      select.disabled = false;
      select.replaceChildren(...scenarios.map((scenario, index) => {
        const option = document.createElement("option");
        option.value = scenario.key;
        option.selected = scenario.key === state.activeScenarioKey;
        option.textContent = `${index + 1}. ${scenarioLabel(scenario)}`;
        return option;
      }));
    }

    function renderCaseModeButtons() {
      const root = document.getElementById("case-mode-buttons");
      const modes = [["all", "All cases"], ["failed", "Failed only"]];
      root.replaceChildren(...modes.map(([value, label]) => {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = label;
        button.dataset.active = String(state.caseMode === value);
        button.addEventListener("click", () => {
          state.caseMode = value;
          renderCaseModeButtons();
          renderScenarioDetail();
        });
        return button;
      }));
    }

    function renderScenarioDetail() {
      renderTrackToggle("detail-track-toggle", "detailFamily");
      const scenario = getDetailScenarios().find((item) => item.key === state.activeScenarioKey);
      const modelRoot = document.getElementById("detail-model-header");
      const detailRoot = document.getElementById("scenario-details");
      const caseRoot = document.getElementById("case-table");
      if (!scenario) {
        modelRoot.replaceChildren(emptyState("No scenario is available for the selected track."));
        detailRoot.replaceChildren(emptyState("Select a scenario above to inspect its per-case results."));
        caseRoot.replaceChildren(emptyRow("No case data for the current selection.", 7));
        return;
      }

      const modelHead = document.createElement("div");
      modelHead.className = "model-head";
      const headTop = document.createElement("div");
      headTop.className = "model-head-top";
      const headCopy = document.createElement("div");
      const kicker = document.createElement("div");
      kicker.className = "model-head-kicker";
      kicker.textContent = `${familyLabel(scenario.family)} • ${scenarioLabel(scenario)}`;
      const name = document.createElement("div");
      name.className = "model-head-name";
      name.textContent = displayModelName(scenario.model);
      headCopy.append(kicker, name);
      const score = document.createElement("div");
      score.className = "model-head-score";
      score.textContent = fmtScore(scenario.finalScore);
      headTop.append(headCopy, score);
      modelHead.append(headTop);
      modelRoot.replaceChildren(modelHead);

      const visibleCases = state.caseMode === "failed"
        ? scenario.cases.filter((item) => item.error)
        : scenario.cases;
      const sortedCases = sortRows(visibleCases, "cases", {
        caseLabel: (item) => `${item.caseId} ${item.title}`,
        domain: (item) => item.domain,
        inferenceMs: (item) => item.inferenceMs,
        exactPreservationRatio: (item) => item.exactPreservationRatio,
        summaryQualityRatio: (item) => item.summaryQualityRatio,
        instructionFollowingScore: (item) => item.instructionFollowingScore,
        status: (item) => item.status,
      });

      const detailGrid = document.createElement("div");
      detailGrid.className = "detail-strip";
      const statGrid = document.createElement("div");
      statGrid.className = "detail-grid";
      [
        ["Scenario", scenarioLabel(scenario)],
        ["Final score", fmtScore(scenario.finalScore)],
        ["Summary", `${fmtPct(scenario.successRate)} success • ${fmtPct(scenario.exactPassRate)} exact`],
        ["Avg instruction", fmtPct(scenario.avgInstructionRatio)],
        ["Avg quality", fmtPct(scenario.avgQualityRatio)],
        ["Avg format", fmtPct(scenario.avgFormatRatio)],
        ["Avg preserve", fmtPct(scenario.avgPreservationRatio)],
        ["Avg brevity", fmtPct(scenario.avgBrevityRatio)],
        ["Avg / p10 case score", `${fmtPct(scenario.avgCaseScore)} / ${fmtPct(scenario.p10CaseScore)}`],
        ["Quality core / latency", `${fmtPct(scenario.qualityCore)} / ${scenario.latencyFactor.toFixed(3)}`],
        ["Max preserve", fmtPct(scenario.maxPreservationRatio)],
        ["Avg / p95 latency", `${fmtLatency(scenario.avgInferenceMs)} / ${fmtLatency(scenario.p95InferenceMs)}`],
        ["Case volume", `${fmtInt(scenario.caseCount)} asks • ${fmtInt(scenario.errorCount)} errors`],
      ].forEach(([label, value]) => {
        const item = document.createElement("div");
        item.className = "detail-item";
        const small = document.createElement("small");
        small.textContent = label;
        const strong = document.createElement("strong");
        strong.textContent = value;
        item.append(small, strong);
        statGrid.append(item);
      });
      detailGrid.append(statGrid);
      detailRoot.replaceChildren(detailGrid);

      if (!sortedCases.length) {
        caseRoot.replaceChildren(emptyRow("No cases match the current detail filters.", 7));
        return;
      }
      caseRoot.replaceChildren(...sortedCases.map((item) => {
        const row = document.createElement("tr");
        const askCell = document.createElement("td");
        const askId = document.createElement("div");
        askId.className = "mono";
        askId.textContent = item.caseId;
        if (item.status === "error" && item.detailKey) {
          const hint = document.createElement("span");
          hint.className = "tooltip-hint";
          hint.textContent = "peek";
          askId.append(hint);
          askCell.addEventListener("mouseenter", () => {
            if (askCell.dataset.tooltipLoaded === "true") {
              return;
            }
            const tooltipText = buildCaseTooltip(item);
            if (tooltipText) {
              askCell.title = tooltipText;
            }
            askCell.dataset.tooltipLoaded = "true";
          }, { once: true });
        }
        const askTitle = document.createElement("div");
        askTitle.style.color = "var(--muted)";
        askTitle.textContent = item.title;
        askCell.append(askId, askTitle);
        row.append(
          askCell,
          textCell(item.domain, "mono"),
          textCell(fmtLatency(item.inferenceMs)),
          textCell(fmtPct(item.exactPreservationRatio)),
          textCell(fmtPct(item.summaryQualityRatio)),
          textCell(fmtPct(item.instructionFollowingScore)),
          textCell(item.error ? "error" : "ok", item.error ? "status-error" : "status-ok"),
        );
        return row;
      }));
    }

    function renderDashboard() {
      ensureActiveScenario();
      ensureHeadToHeadSelection();
      renderSortableHeaders();
      renderCompareCollapse();
      renderHeadToHead();
      renderCollectiveOverview();
      renderLatencyBars();
      renderQualityStacks();
      renderScenarioSelector();
      renderCaseModeButtons();
      renderScenarioDetail();
    }

    try {
      document.getElementById("scenario-select").addEventListener("change", (event) => {
        state.activeScenarioKey = event.target.value;
        renderScenarioDetail();
      });

      document.getElementById("compare-left-select").addEventListener("change", (event) => {
        state.compareLeftKey = event.target.value;
        ensureHeadToHeadSelection("left");
        renderDashboard();
      });

      document.getElementById("compare-right-select").addEventListener("change", (event) => {
        state.compareRightKey = event.target.value;
        ensureHeadToHeadSelection("right");
        renderDashboard();
      });

      document.getElementById("compare-collapse-toggle").addEventListener("click", () => {
        state.compareCollapsed = !state.compareCollapsed;
        renderCompareCollapse();
      });

      initSortableHeaders();
      renderDashboard();
    } catch (error) {
      renderFatalError(error);
      throw error;
    }
  </script>
</body>
</html>
"""
    return (
        template.replace("__SOURCE__", html.escape(_format_source_label(source_path)))
        .replace("__GENERATED__", html.escape(datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%SZ")))
        .replace("__MODE__", html.escape(mode))
        .replace("__DATA__", data_json)
    )


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
