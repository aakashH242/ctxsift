"""Normalize benchmark dataset case ids."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


FIELD_ORDER = (
    ("case_id", "string"),
    ("domain", "string"),
    ("title", "string"),
    ("instruction", "string"),
    ("raw_input", "string"),
    ("must_preserve_tokens", "array"),
    ("ideal_summary", "string"),
    ("tags", "array"),
)

DOMAIN_SLUGS = {
    "python runtime / traceback": "python",
    "pytest": "pytest",
    "mypy": "mypy",
    "ruff": "ruff",
    "pylint": "pylint",
    "black": "black",
    "npm": "npm",
    "pnpm": "pnpm",
    "typescript / tsc": "typescript",
    "eslint": "eslint",
    "docker build / run": "docker",
    "docker compose": "docker-compose",
    "kubectl / kubernetes": "kubectl",
    "terraform": "terraform",
    "mixed stdout/stderr generic command runs": "mixed",
}

SLUG_RE = re.compile(r"[^a-z0-9]+")


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for dataset normalization."""
    parser = argparse.ArgumentParser(description="Normalize benchmark dataset case ids.")
    parser.add_argument(
        "--dataset",
        default="benchmark/dataset.jsonl",
        help="Path to the benchmark dataset JSONL file.",
    )
    return parser


def main() -> int:
    """Normalize case ids in-place."""
    args = build_parser().parse_args()
    dataset_path = Path(args.dataset)
    rows = load_rows(dataset_path)
    normalized_rows = normalize_case_ids(rows)
    write_rows(dataset_path, normalized_rows)
    print(f"Normalized {len(normalized_rows)} case ids in {dataset_path}")
    return 0


def load_rows(dataset_path: Path) -> list[dict[str, object]]:
    """Load dataset rows from JSONL."""
    rows: list[dict[str, object]] = []
    for line in dataset_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        rows.append(load_row(stripped))
    return rows


def load_row(payload: str) -> dict[str, object]:
    """Load one dataset row, repairing malformed JSON when needed."""
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return repair_row(payload)


def repair_row(payload: str) -> dict[str, object]:
    """Repair one malformed JSONL dataset row using the fixed schema order."""
    repaired: dict[str, object] = {}
    for index, (field_name, field_kind) in enumerate(FIELD_ORDER):
        next_field = FIELD_ORDER[index + 1][0] if index + 1 < len(FIELD_ORDER) else None
        raw_value = extract_field_value(payload, field_name, next_field)
        if field_kind == "string":
            repaired[field_name] = decode_text_value(raw_value)
        else:
            repaired[field_name] = decode_array_value(raw_value)
    return repaired


def extract_field_value(payload: str, field_name: str, next_field: str | None) -> str:
    """Extract one raw field slice from the fixed-schema JSON-like line."""
    marker = f'"{field_name}":'
    start = payload.find(marker)
    if start == -1:
        raise ValueError(f"Missing field marker for {field_name!r}.")
    value_start = start + len(marker)
    if next_field is None:
        value_end = payload.rfind("}")
        if value_end == -1:
            raise ValueError("Missing closing object brace.")
    else:
        next_marker = f',"{next_field}":'
        value_end = payload.find(next_marker, value_start)
        if value_end == -1:
            raise ValueError(f"Missing next field marker for {next_field!r}.")
    return payload[value_start:value_end].strip()


def decode_text_value(raw_value: str) -> str:
    """Decode one raw JSON-like string field."""
    value = raw_value
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    return (
        value.replace("\\\\", "\\")
        .replace('\\"', '"')
        .replace("\\n", "\n")
        .replace("\\r", "\r")
        .replace("\\t", "\t")
    )


def decode_array_value(raw_value: str) -> list[str]:
    """Decode one raw JSON-like string array field."""
    value = raw_value.strip()
    if value == "[]":
        return []
    if not (value.startswith("[") and value.endswith("]")):
        raise ValueError(f"Expected array field, got {raw_value!r}.")
    inner = value[1:-1]
    if not inner:
        return []
    parts = inner.split('","')
    normalized_parts: list[str] = []
    for index, part in enumerate(parts):
        cleaned = part
        if index == 0 and cleaned.startswith('"'):
            cleaned = cleaned[1:]
        if index == len(parts) - 1 and cleaned.endswith('"'):
            cleaned = cleaned[:-1]
        normalized_parts.append(decode_text_value(cleaned))
    return normalized_parts


def normalize_case_ids(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Rewrite case ids to short stable per-domain ids."""
    domain_counts: dict[str, int] = {}
    normalized_rows: list[dict[str, object]] = []
    for row in rows:
        domain = str(row["domain"]).strip()
        domain_slug = slugify_domain(domain)
        domain_counts[domain_slug] = domain_counts.get(domain_slug, 0) + 1
        normalized = dict(row)
        normalized["domain"] = domain_slug
        normalized["case_id"] = f"{domain_slug}-{domain_counts[domain_slug]:02d}"
        normalized_rows.append(normalized)
    return normalized_rows


def slugify_domain(domain: str) -> str:
    """Map one domain label to its stable case-id slug."""
    normalized = domain.strip().casefold()
    mapped = DOMAIN_SLUGS.get(normalized)
    if mapped is not None:
        return mapped
    slug = SLUG_RE.sub("-", normalized).strip("-")
    return slug or "case"


def write_rows(dataset_path: Path, rows: list[dict[str, object]]) -> None:
    """Write normalized rows back to JSONL."""
    payload = "\n".join(json.dumps(row, ensure_ascii=False) for row in rows)
    dataset_path.write_text(payload + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
