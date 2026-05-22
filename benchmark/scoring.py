"""Scoring helpers for benchmark preservation, quality, and instruction checks."""

from __future__ import annotations

from collections import Counter
import json
import re
from typing import Any, Sequence

from benchmark.stats import percentile
from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.text_profile_common import (
    has_requested_structure,
    instruction_output_mode,
    is_plain_text_contract,
    validate_instruction_aware_output,
)

yaml_module: Any | None
try:  # pragma: no cover - optional dependency in some environments
    import yaml as _yaml
except ImportError:  # pragma: no cover - optional dependency in some environments
    yaml_module = None
else:  # pragma: no cover - optional dependency in some environments
    yaml_module = _yaml


_TOKEN_RE = re.compile(r"[A-Za-z0-9_./:-]+")
_WORD_CHAR_RE = re.compile(r"[A-Za-z0-9_]")
_EXCEPTION_RE = re.compile(r"(?:Error|Exception|BackOff|Timeout|NotFound|Failure)$")
_ERROR_CODE_RE = re.compile(r"^(?:[A-Z]+\d+[A-Z0-9-]*|[A-Z]{2,}_?[A-Z0-9_]+|\d{3,5}(?:/EXEC)?)$")
_FIRST_LINES_RE = re.compile(r"\bfirst\s+(\d+)\s+lines?\b")
_NEXT_LINES_RE = re.compile(r"\bnext\s+(\d+)\s+lines?\b")
_REGEX_PASS_RULE_RE = re.compile(r"\bmust match\s+(.+?)\s+exactly\.?$", re.IGNORECASE)
_COMMAND_PREFIXES = (
    "python ",
    "python -m ",
    "pytest ",
    "mypy ",
    "ruff ",
    "black ",
    "pylint ",
    "npm ",
    "pnpm ",
    "npx ",
    "tsc ",
    "eslint ",
    "docker ",
    "kubectl ",
    "terraform ",
    "git ",
    "curl ",
    "ssh ",
    "go ",
    "cargo ",
    "make ",
    "sudo ",
    "mysql ",
    "psql ",
    "redis-cli ",
    "ansible-playbook ",
    "javac ",
    "mvn ",
    "./",
)

_FAMILY_WEIGHTS: dict[str, tuple[float, float, float, float]] = {
    "recall": (0.45, 0.25, 0.20, 0.10),
    "summary": (0.25, 0.40, 0.20, 0.15),
    "explanation": (0.20, 0.50, 0.20, 0.10),
    "structured": (0.20, 0.30, 0.40, 0.10),
    "instruction_following": (0.20, 0.30, 0.40, 0.10),
    "exact_format": (0.15, 0.10, 0.70, 0.05),
}
_DEFAULT_FAMILY_WEIGHTS = _FAMILY_WEIGHTS["summary"]
_LATENCY_TARGET_MS = 2000.0


def missing_tokens(output: str, required_tokens: tuple[str, ...]) -> tuple[str, ...]:
    """Return required exact tokens missing from one model output."""
    return tuple(token for token in required_tokens if not _contains_exact_token(output, token))


def exact_ratio(required_tokens: tuple[str, ...], missing: tuple[str, ...]) -> float:
    """Return the fraction of required exact tokens preserved verbatim."""
    if not required_tokens:
        return 1.0
    missing_set = set(missing)
    total_weight = sum(_preservation_weight(token) for token in required_tokens)
    if total_weight == 0:
        return 1.0
    preserved_weight = sum(
        _preservation_weight(token)
        for token in required_tokens
        if token not in missing_set
    )
    return preserved_weight / total_weight


def summary_quality_ratio(output: str, ideal_summary: str, exact_tokens: tuple[str, ...]) -> float:
    """Measure how much non-anchor summary content aligns with the ideal summary.

    The benchmark already scores exact anchor preservation separately. This metric
    removes those anchors first, then compares the remaining narrative tokens with
    a bag-of-words F1 score so anchor-only outputs do not look high quality.
    """
    expected_tokens = _quality_tokens(ideal_summary, exact_tokens)
    actual_tokens = _quality_tokens(output, exact_tokens)
    if not expected_tokens:
        return 1.0 if not actual_tokens else 0.0
    if not actual_tokens:
        return 0.0
    expected_counts = Counter(expected_tokens)
    actual_counts = Counter(actual_tokens)
    overlap = sum((expected_counts & actual_counts).values())
    if overlap == 0:
        return 0.0
    precision = overlap / sum(actual_counts.values())
    recall = overlap / sum(expected_counts.values())
    return (2 * precision * recall) / (precision + recall)


def brevity_ratio(
    output: str,
    expected_output: str,
    exact_tokens: tuple[str, ...],
    max_extra_tokens: int,
) -> float:
    """Score whether one output stays near the configured extra-token budget."""
    actual_tokens = _quality_tokens(output, exact_tokens)
    expected_tokens = _quality_tokens(expected_output, exact_tokens)
    budget = max(1, len(expected_tokens) + max(0, max_extra_tokens))
    actual_count = len(actual_tokens)
    if actual_count <= budget:
        return 1.0
    overflow = actual_count - budget
    return budget / (budget + overflow)


def instruction_following_score(
    request: ModelCompressionInput,
    output: str,
    *,
    family: str | None = None,
    output_mode: str | None = None,
    expected_output: str | None = None,
    required_anchors: tuple[str, ...] = (),
    format_check: str = "none",
    pass_rule: str = "",
    max_extra_tokens: int | None = None,
) -> float:
    """Score how well one output followed the requested output form."""
    cleaned = output.strip()
    if not cleaned:
        return 0.0
    validation = validate_instruction_aware_output(request, cleaned)
    if validation.status == "rejected":
        return 0.0
    mode = _normalized_output_mode(output_mode or instruction_output_mode(request.instruction))
    base_score = format_adherence_score(
        request,
        cleaned,
        family=family or "",
        output_mode=mode,
        expected_output=expected_output or "",
        format_check=format_check,
        pass_rule=pass_rule,
    )
    if expected_output is None or max_extra_tokens is None:
        return base_score
    length_score = brevity_ratio(
        cleaned,
        expected_output,
        required_anchors,
        max_extra_tokens,
    )
    return base_score * (0.7 + (0.3 * length_score))


def format_adherence_score(
    request: ModelCompressionInput,
    output: str,
    *,
    family: str = "",
    output_mode: str = "",
    expected_output: str = "",
    format_check: str = "none",
    pass_rule: str = "",
) -> float:
    """Return how well one output matches the declared dataset format contract."""
    cleaned = output.strip()
    if not cleaned:
        return 0.0
    mode = _normalized_output_mode(output_mode or instruction_output_mode(request.instruction))
    normalized_format = format_check.strip().casefold()
    if normalized_format == "exact_match":
        return _exact_match_score(cleaned, expected_output)
    if normalized_format == "regex":
        return _regex_shape_score(cleaned, expected_output, pass_rule)
    if normalized_format == "json_shape":
        return _json_shape_score(cleaned, expected_output)
    if normalized_format == "yaml_shape":
        return _yaml_shape_score(cleaned, expected_output)
    if normalized_format == "table_shape":
        return _table_shape_score(cleaned, expected_output)
    if normalized_format == "bullet_shape":
        return _bullet_shape_score(cleaned, expected_output)
    if mode == "exact_lines":
        return _verbatim_excerpt_ratio(request, cleaned)
    if mode == "single_line":
        return 1.0 if len([line for line in cleaned.splitlines() if line.strip()]) == 1 else 0.0
    if mode == "bullet_list":
        return _bullet_shape_score(cleaned, expected_output)
    if mode == "json":
        return _json_shape_score(cleaned, expected_output)
    if mode == "yaml":
        return _yaml_shape_score(cleaned, expected_output)
    if mode == "table":
        return _table_shape_score(cleaned, expected_output)
    if mode == "regex_constrained":
        return _regex_shape_score(cleaned, expected_output, pass_rule)
    if mode == "structured" or family.strip().casefold() in {"structured", "exact_format"}:
        return 1.0 if has_requested_structure(cleaned) else 0.5
    return 1.0 if is_plain_text_contract(cleaned) else 0.5


def case_benchmark_score(
    *,
    validation_status: str,
    family: str,
    anchor_score: float,
    semantic_score: float,
    format_score: float,
    brevity_score: float,
) -> float:
    """Return the per-case benchmark score before scenario aggregation."""
    validation_factor = _validation_factor(validation_status)
    if validation_factor <= 0.0:
        return 0.0
    w_anchor, w_semantic, w_format, w_brevity = _family_weights(family)
    blended = (
        (w_anchor * _clamp_ratio(anchor_score))
        + (w_semantic * _clamp_ratio(semantic_score))
        + (w_format * _clamp_ratio(format_score))
        + (w_brevity * _clamp_ratio(brevity_score))
    )
    return validation_factor * blended


def quality_core_score(case_scores: Sequence[float]) -> float:
    """Blend mean and p10 so weak tails still matter."""
    if not case_scores:
        return 0.0
    clamped = [_clamp_ratio(score) for score in case_scores]
    return (0.80 * (sum(clamped) / len(clamped))) + (0.20 * percentile(clamped, 0.10))


def latency_factor_score(observed_latency_ms: float) -> float:
    """Return the narrow latency modifier used by the final score."""
    return _latency_factor(observed_latency_ms)


def final_benchmark_score(
    *,
    case_count: int,
    success_count: int,
    avg_exact_preservation_ratio: float = 0.0,
    avg_summary_quality_ratio: float = 0.0,
    avg_instruction_following_score: float = 0.0,
    avg_brevity_ratio: float = 1.0,
    accepted_count: int | None = None,
    soft_accepted_count: int = 0,
    avg_inference_ms: float = 0.0,
    p95_inference_ms: float = 0.0,
    case_scores: Sequence[float] | None = None,
    observed_latency_ms: float | None = None,
) -> float:
    """Collapse scenario metrics into one headline score.

    Prefer `case_scores` for the current formula. Aggregate-only inputs remain as a
    legacy fallback for older persisted results.
    """
    if case_count <= 0:
        return 0.0
    if case_scores is None:
        case_scores = _legacy_case_scores(
            case_count=case_count,
            success_count=success_count,
            avg_exact_preservation_ratio=avg_exact_preservation_ratio,
            avg_summary_quality_ratio=avg_summary_quality_ratio,
            avg_instruction_following_score=avg_instruction_following_score,
            avg_brevity_ratio=avg_brevity_ratio,
            accepted_count=accepted_count,
            soft_accepted_count=soft_accepted_count,
        )
    quality_core = quality_core_score(case_scores)
    latency_factor = latency_factor_score(
        observed_latency_ms if observed_latency_ms is not None else avg_inference_ms
    )
    score = 100.0 * quality_core * latency_factor
    return max(0.0, min(100.0, score))


def _quality_tokens(text: str, exact_tokens: tuple[str, ...]) -> tuple[str, ...]:
    residual = _strip_exact_tokens(text, exact_tokens)
    return tuple(
        token.casefold()
        for token in _TOKEN_RE.findall(residual)
        if len(token) > 1 or token.isdigit()
    )


def _clamp_ratio(value: float) -> float:
    return max(0.0, min(1.0, value))


def _family_weights(family: str) -> tuple[float, float, float, float]:
    normalized = family.strip().casefold().replace("-", "_")
    return _FAMILY_WEIGHTS.get(normalized, _DEFAULT_FAMILY_WEIGHTS)


def _validation_factor(validation_status: str) -> float:
    normalized = validation_status.strip().casefold()
    if normalized == "accepted":
        return 1.0
    if normalized == "soft_accepted":
        return 0.85
    return 0.0


def _normalized_output_mode(value: str) -> str:
    return value.strip().casefold().replace("-", "_")


def _normalized_exact_text(text: str) -> str:
    return text.strip().replace("\r\n", "\n")


def _normalized_expected_lines(text: str) -> list[str]:
    return [line.rstrip() for line in _normalized_exact_text(text).split("\n")]


def _exact_match_score(output: str, expected_output: str) -> float:
    if _normalized_exact_text(output) == _normalized_exact_text(expected_output):
        return 1.0
    return _ordered_line_match_ratio(
        _normalized_expected_lines(expected_output),
        _normalized_expected_lines(output),
    )


def _regex_shape_score(output: str, expected_output: str, pass_rule: str) -> float:
    pattern = _regex_pattern_from_pass_rule(pass_rule)
    if pattern is None:
        return 1.0 if _normalized_exact_text(output) == _normalized_exact_text(expected_output) else 0.0
    return 1.0 if pattern.fullmatch(output.strip()) else 0.0


def _regex_pattern_from_pass_rule(pass_rule: str) -> re.Pattern[str] | None:
    match = _REGEX_PASS_RULE_RE.search(pass_rule.strip())
    if match is None:
        return None
    body = match.group(1).strip()
    try:
        return re.compile(body)
    except re.error:
        return None


def _bullet_shape_score(output: str, expected_output: str) -> float:
    actual_lines = [line.strip() for line in output.splitlines() if line.strip()]
    if not actual_lines or any(not line.startswith("- ") for line in actual_lines):
        return 0.0
    expected_lines = [line.strip() for line in expected_output.splitlines() if line.strip()]
    expected_bullets = [line for line in expected_lines if line.startswith("- ")]
    if not expected_bullets:
        return 1.0
    if len(actual_lines) == len(expected_bullets):
        return 1.0
    return min(len(actual_lines), len(expected_bullets)) / max(len(actual_lines), len(expected_bullets))


def _json_shape_score(output: str, expected_output: str) -> float:
    try:
        actual = json.loads(output)
    except json.JSONDecodeError:
        return 0.0
    try:
        expected = json.loads(expected_output)
    except json.JSONDecodeError:
        return 1.0
    return _shape_similarity(expected, actual)


def _yaml_shape_score(output: str, expected_output: str) -> float:
    if yaml_module is None:
        return _fallback_yaml_shape_score(output, expected_output)
    try:
        actual = yaml_module.safe_load(output)
    except Exception:
        return 0.0
    try:
        expected = yaml_module.safe_load(expected_output)
    except Exception:
        return 1.0
    return _shape_similarity(expected, actual)


def _fallback_yaml_shape_score(output: str, expected_output: str) -> float:
    actual_lines = [line.rstrip() for line in output.splitlines() if line.strip()]
    expected_lines = [line.rstrip() for line in expected_output.splitlines() if line.strip()]
    if not actual_lines:
        return 0.0
    root_expected = expected_lines[0].split(":", 1)[0].strip() if expected_lines else ""
    root_actual = actual_lines[0].split(":", 1)[0].strip()
    if root_expected and root_actual != root_expected:
        return 0.0
    if any(line.lstrip().startswith("- ") for line in expected_lines):
        return 1.0 if any(line.lstrip().startswith("- ") for line in actual_lines) else 0.5
    return 1.0


def _table_shape_score(output: str, expected_output: str) -> float:
    actual_rows = _markdown_table_rows(output)
    expected_rows = _markdown_table_rows(expected_output)
    if len(actual_rows) < 2:
        return 0.0
    if len(expected_rows) < 2:
        return 1.0
    expected_header = expected_rows[0]
    actual_header = actual_rows[0]
    if actual_header != expected_header:
        return 0.5 if len(actual_header) == len(expected_header) else 0.0
    column_count = len(expected_header)
    if any(len(row) != column_count for row in actual_rows[1:]):
        return 0.0
    return 1.0


def _markdown_table_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def _shape_similarity(expected: object, actual: object) -> float:
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return 0.0
        expected_keys = set(expected)
        actual_keys = set(actual)
        if not expected_keys and not actual_keys:
            return 1.0
        key_score = len(expected_keys & actual_keys) / max(len(expected_keys | actual_keys), 1)
        child_scores = [
            _shape_similarity(expected[key], actual[key])
            for key in expected_keys & actual_keys
        ]
        child_score = sum(child_scores) / len(child_scores) if child_scores else 0.0
        return (0.5 * key_score) + (0.5 * child_score)
    if isinstance(expected, list):
        if not isinstance(actual, list):
            return 0.0
        if not expected:
            return 1.0
        if not actual:
            return 0.0
        exemplar = expected[0]
        child_scores = [_shape_similarity(exemplar, item) for item in actual]
        length_score = min(len(actual), len(expected)) / max(len(actual), len(expected), 1)
        return (0.7 * (sum(child_scores) / len(child_scores))) + (0.3 * length_score)
    if expected is None:
        return 1.0 if actual is None else 0.0
    return 1.0 if type(expected) is type(actual) else 0.0


def _latency_factor(observed_latency_ms: float) -> float:
    observed = max(observed_latency_ms, 1.0)
    factor = (_LATENCY_TARGET_MS / observed) ** 0.15
    return max(0.85, min(1.0, factor))


def _legacy_case_scores(
    *,
    case_count: int,
    success_count: int,
    avg_exact_preservation_ratio: float,
    avg_summary_quality_ratio: float,
    avg_instruction_following_score: float,
    avg_brevity_ratio: float,
    accepted_count: int | None,
    soft_accepted_count: int,
) -> list[float]:
    if case_count <= 0:
        return []
    success_rate = _clamp_ratio(success_count / case_count)
    if accepted_count is None:
        validation_factor = success_rate
    else:
        validation_factor = _clamp_ratio(
            (accepted_count + (0.85 * max(0, soft_accepted_count))) / case_count
        )
    approximate_case_score = validation_factor * (
        (0.25 * _clamp_ratio(avg_exact_preservation_ratio))
        + (0.40 * _clamp_ratio(avg_summary_quality_ratio))
        + (0.20 * _clamp_ratio(avg_instruction_following_score))
        + (0.15 * _clamp_ratio(avg_brevity_ratio))
    )
    return [approximate_case_score] * case_count


def _strip_exact_tokens(text: str, exact_tokens: tuple[str, ...]) -> str:
    residual = text
    for token in sorted(exact_tokens, key=len, reverse=True):
        if token:
            residual = residual.replace(token, " ")
    return residual


def _contains_exact_token(output: str, token: str) -> bool:
    normalized_token = " ".join(token.split())
    if not normalized_token:
        return True
    pattern = _token_pattern(normalized_token)
    return bool(pattern.search(output))


def _token_pattern(token: str) -> re.Pattern[str]:
    pieces = [re.escape(part) for part in token.split()]
    body = r"\s+".join(pieces)
    prefix = r"(?<![A-Za-z0-9_])" if _needs_boundary(token[0]) else ""
    suffix = r"(?![A-Za-z0-9_])" if _needs_boundary(token[-1]) else ""
    return re.compile(f"{prefix}{body}{suffix}", re.MULTILINE)


def _needs_boundary(character: str) -> bool:
    return bool(_WORD_CHAR_RE.fullmatch(character))


def _preservation_weight(token: str) -> float:
    stripped = token.strip()
    lowered = stripped.casefold()
    if lowered.startswith(_COMMAND_PREFIXES) or " --" in stripped or stripped.startswith("GIT_SSH_COMMAND="):
        return 3.0
    if _looks_path_or_location(stripped) or "::" in stripped:
        return 2.5
    if _EXCEPTION_RE.search(stripped) or _ERROR_CODE_RE.fullmatch(stripped):
        return 2.0
    if "failed" in lowered or "warning" in lowered or "error" in lowered:
        return 1.75
    return 1.0


def _looks_path_or_location(token: str) -> bool:
    return any(marker in token for marker in ("/", "\\", ".py:", ".ts:", ".js:", ".tf:", "Dockerfile:", "line ", "(", ":"))


def _verbatim_excerpt_ratio(request: ModelCompressionInput, output: str) -> float:
    output_lines = [
        normalized
        for line in output.splitlines()
        if (normalized := _normalize_verbatim_line(line))
    ]
    if not output_lines:
        return 0.0
    expected_lines = _expected_exact_lines(request)
    if expected_lines is not None:
        return _ordered_line_match_ratio(expected_lines, output_lines)
    raw_lines = {
        normalized
        for line in request.raw_input.splitlines()
        if (normalized := _normalize_verbatim_line(line))
    }
    if not raw_lines:
        return 0.0
    preserved_count = sum(1 for line in output_lines if line in raw_lines)
    requested_count = _requested_exact_line_count(request.instruction)
    denominator = max(len(output_lines), requested_count or 0)
    if denominator == 0:
        return 0.0
    return preserved_count / denominator


def _expected_exact_lines(request: ModelCompressionInput) -> list[str] | None:
    instruction = request.instruction.casefold()
    match = _FIRST_LINES_RE.search(instruction)
    if match is None:
        if "first line" not in instruction:
            return None
        requested_count = 1
    else:
        requested_count = int(match.group(1))
    raw_lines = [
        normalized
        for line in request.raw_input.splitlines()
        if (normalized := _normalize_verbatim_line(line))
    ]
    return raw_lines[:requested_count]


def _requested_exact_line_count(instruction: str) -> int | None:
    normalized = instruction.casefold()
    for pattern in (_FIRST_LINES_RE, _NEXT_LINES_RE):
        match = pattern.search(normalized)
        if match is not None:
            return int(match.group(1))
    if "first line" in normalized or "next line" in normalized or "exact line" in normalized:
        return 1
    return None


def _ordered_line_match_ratio(expected_lines: list[str], output_lines: list[str]) -> float:
    if not expected_lines:
        return 0.0
    match_count = sum(
        1
        for expected, actual in zip(expected_lines, output_lines)
        if expected == actual
    )
    return match_count / max(len(expected_lines), len(output_lines))


def _normalize_verbatim_line(line: str) -> str:
    cleaned = line.strip()
    if cleaned.startswith(">"):
        cleaned = cleaned[1:].strip()
    if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {'"', "'", "`"}:
        cleaned = cleaned[1:-1].strip()
    return cleaned


