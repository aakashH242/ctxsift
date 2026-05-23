"""Load benchmark datasets and scenario matrices from disk."""

from __future__ import annotations

import json
from pathlib import Path

from benchmark.schemas import BenchmarkCase, BenchmarkJudgement, BenchmarkManifest, BenchmarkScenario


def load_manifest(dataset_path: Path, matrix_path: Path) -> BenchmarkManifest:
    """Load benchmark cases and scenarios from disk."""
    return BenchmarkManifest(
        cases=tuple(load_cases(dataset_path)),
        scenarios=tuple(load_scenarios(matrix_path)),
    )


def load_cases(dataset_path: Path) -> list[BenchmarkCase]:
    """Load the benchmark dataset from a JSONL file."""
    cases: list[BenchmarkCase] = []
    for line in dataset_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        payload = json.loads(stripped)
        cases.append(
            BenchmarkCase(
                case_id=payload["case_id"],
                domain=payload["domain"],
                title=payload["title"],
                instruction=payload["instruction"],
                raw_input=payload["raw_input"],
                must_preserve_tokens=tuple(payload["must_preserve_tokens"]),
                ideal_summary=payload["ideal_summary"],
                tags=tuple(payload.get("tags", [])),
                family=str(payload.get("family", "summary")),
                ecosystem=str(payload.get("ecosystem", "")),
                difficulty=str(payload.get("difficulty", "medium")),
                output_mode=str(payload.get("output_mode", "plain_text")),
                expected_output=str(payload.get("expected_output", payload["ideal_summary"])),
                required_anchors=tuple(payload.get("required_anchors", payload["must_preserve_tokens"])),
                forbidden_content=tuple(payload.get("forbidden_content", [])),
                judgement=_load_judgement(payload.get("judgement")),
                rationale=str(payload.get("rationale", "")),
            )
        )
    return cases


def _load_judgement(payload: object) -> BenchmarkJudgement:
    if not isinstance(payload, dict):
        return BenchmarkJudgement()
    return BenchmarkJudgement(
        format_check=str(payload.get("format_check", "none")),
        anchor_check=str(payload.get("anchor_check", "required")),
        max_extra_tokens=int(payload.get("max_extra_tokens", 24)),
        pass_rule=str(payload.get("pass_rule", "")),
    )


def load_scenarios(matrix_path: Path) -> list[BenchmarkScenario]:
    """Load benchmark scenarios from a JSON file."""
    payload = json.loads(matrix_path.read_text(encoding="utf-8"))
    scenarios = payload.get("scenarios", [])
    return [
        BenchmarkScenario(
            name=item["name"],
            track=item["track"],
            phase=item["phase"],
            model=item["model"],
            quantization=item["quantization"],
            device=item["device"],
            gguf_filename=item.get("gguf_filename"),
            dtype=item.get("dtype", "auto"),
            attn_implementation=item.get("attn_implementation", "auto"),
            max_output_tokens=item.get("max_output_tokens", 768),
            concurrency=item.get("concurrency", 1),
            enabled=item.get("enabled", True),
        )
        for item in scenarios
    ]
