"""Semantic quality scoring for benchmark cases."""

from __future__ import annotations

import json
import math
from typing import Any, Sequence

from benchmark.schemas import BenchmarkCase
from benchmark.scoring import summary_quality_ratio
from ctxsift.compression.intent import CompressionIntent, canonical_mode_for_intent
from ctxsift.embeddings import create_in_process_embedding_backend
from ctxsift.embeddings.base import DocumentEmbeddingRequest, EmbeddingBackendUnavailableError
from ctxsift.types import EmbeddingConfig

yaml_module: Any | None
try:  # pragma: no cover - optional dependency in some environments
    import yaml as _yaml
except ImportError:  # pragma: no cover - optional dependency in some environments
    yaml_module = None
else:  # pragma: no cover - optional dependency in some environments
    yaml_module = _yaml


_EMBEDDING_BATCH_SIZE = 64


class BenchmarkSemanticScorer:
    """Compute semantic quality using the configured embedding model when possible."""

    def __init__(self, config: EmbeddingConfig) -> None:
        self._config = config
        self._backend = create_in_process_embedding_backend(config)
        self._available = True
        self._warning: str | None = None

    @property
    def warning(self) -> str | None:
        return self._warning

    async def preload(self) -> None:
        if not self._available:
            return
        try:
            await self._backend.preload()
        except EmbeddingBackendUnavailableError as error:
            self._available = False
            self._warning = str(error)

    async def score_cases(
        self,
        cases: Sequence[BenchmarkCase],
        outputs: Sequence[str],
    ) -> list[float]:
        lexical_scores = [
            summary_quality_ratio(output, case.scoring_target, case.anchor_tokens)
            for case, output in zip(cases, outputs, strict=True)
        ]
        if not self._available:
            return lexical_scores
        await self.preload()
        if not self._available:
            return lexical_scores

        plans = [_semantic_plan(case, output) for case, output in zip(cases, outputs, strict=True)]
        texts: list[str] = []
        text_index_by_case: dict[int, tuple[int, int]] = {}
        for index, plan in enumerate(plans):
            if plan.embedding_output_text is None or plan.embedding_expected_text is None:
                continue
            start = len(texts)
            texts.extend((plan.embedding_output_text, plan.embedding_expected_text))
            text_index_by_case[index] = (start, start + 1)

        similarities: dict[int, float] = {}
        if texts:
            try:
                embeddings = await self._embed_texts(texts)
            except EmbeddingBackendUnavailableError as error:
                self._available = False
                self._warning = str(error)
                return lexical_scores
            for case_index, (output_index, expected_index) in text_index_by_case.items():
                similarities[case_index] = _cosine_similarity(
                    embeddings[output_index],
                    embeddings[expected_index],
                )

        semantic_scores: list[float] = []
        for index, plan in enumerate(plans):
            fallback = lexical_scores[index]
            embedding_similarity = similarities.get(index)
            semantic_scores.append(plan.semantic_score(embedding_similarity, fallback))
        return semantic_scores

    async def _embed_texts(self, texts: Sequence[str]) -> list[list[float]]:
        batches = [
            list(texts[start_index : start_index + _EMBEDDING_BATCH_SIZE])
            for start_index in range(0, len(texts), _EMBEDDING_BATCH_SIZE)
        ]
        requests = [
            DocumentEmbeddingRequest(texts=batch, max_length=self._config.max_length)
            for batch in batches
        ]
        batched_embeddings = await self._backend.embed_documents_batch(requests)
        flattened: list[list[float]] = []
        for batch in batched_embeddings:
            flattened.extend(batch)
        return flattened


class _SemanticPlan:
    """One case's semantic-scoring plan."""

    def __init__(
        self,
        *,
        base_score: float,
        embedding_output_text: str | None,
        embedding_expected_text: str | None,
        blend_weight: float,
    ) -> None:
        self._base_score = base_score
        self.embedding_output_text = embedding_output_text
        self.embedding_expected_text = embedding_expected_text
        self._blend_weight = blend_weight

    def semantic_score(self, embedding_similarity: float | None, fallback_score: float) -> float:
        score = self._base_score if self._base_score >= 0.0 else fallback_score
        if embedding_similarity is None:
            return _clamp_ratio(score)
        if score < 0.0:
            return _clamp_ratio(embedding_similarity)
        return _clamp_ratio(
            ((1.0 - self._blend_weight) * score) + (self._blend_weight * embedding_similarity)
        )


def build_semantic_scorer(config: EmbeddingConfig) -> BenchmarkSemanticScorer | None:
    """Create the benchmark semantic scorer, or return None when unavailable."""
    if not config.model.strip():
        return None
    try:
        return BenchmarkSemanticScorer(config)
    except EmbeddingBackendUnavailableError:
        return None


def _semantic_plan(case: BenchmarkCase, output: str) -> _SemanticPlan:
    cleaned_output = output.strip()
    if not cleaned_output:
        return _SemanticPlan(
            base_score=0.0,
            embedding_output_text=None,
            embedding_expected_text=None,
            blend_weight=0.0,
        )
    canonical_mode = canonical_mode_for_intent(case.intent)
    if canonical_mode == "structured":
        return _structured_semantic_plan(case, cleaned_output)
    if case.intent is CompressionIntent.EXACT_LINES:
        return _exact_lines_semantic_plan(case, cleaned_output)
    if case.intent is CompressionIntent.EXACT_FORMAT:
        return _exact_format_semantic_plan(case, cleaned_output)
    return _plain_text_semantic_plan(case, cleaned_output)


def _plain_text_semantic_plan(case: BenchmarkCase, output: str) -> _SemanticPlan:
    return _SemanticPlan(
        base_score=-1.0,
        embedding_output_text=output,
        embedding_expected_text=case.scoring_target.strip() or case.ideal_summary.strip(),
        blend_weight=1.0,
    )


def _exact_lines_semantic_plan(case: BenchmarkCase, output: str) -> _SemanticPlan:
    return _SemanticPlan(
        base_score=summary_quality_ratio(output, case.scoring_target, case.anchor_tokens),
        embedding_output_text=None,
        embedding_expected_text=None,
        blend_weight=0.0,
    )


def _exact_format_semantic_plan(case: BenchmarkCase, output: str) -> _SemanticPlan:
    return _SemanticPlan(
        base_score=summary_quality_ratio(output, case.scoring_target, case.anchor_tokens),
        embedding_output_text=output,
        embedding_expected_text=case.scoring_target.strip() or case.ideal_summary.strip(),
        blend_weight=0.35,
    )


def _structured_semantic_plan(case: BenchmarkCase, output: str) -> _SemanticPlan:
    expected = case.scoring_target.strip()
    actual_value = _parse_structured_payload(
        output,
        intent=case.intent,
        output_mode=case.output_mode,
        format_check=case.judgement.format_check,
    )
    expected_value = _parse_structured_payload(
        expected,
        intent=case.intent,
        output_mode=case.output_mode,
        format_check=case.judgement.format_check,
    )
    if actual_value is None or expected_value is None:
        return _SemanticPlan(
            base_score=summary_quality_ratio(output, expected, case.anchor_tokens),
            embedding_output_text=output,
            embedding_expected_text=expected or case.ideal_summary.strip(),
            blend_weight=0.25,
        )
    base_score = _structured_value_similarity(expected_value, actual_value)
    return _SemanticPlan(
        base_score=base_score,
        embedding_output_text=_structured_embedding_text(actual_value),
        embedding_expected_text=_structured_embedding_text(expected_value),
        blend_weight=0.20,
    )


def _parse_structured_payload(
    text: str,
    *,
    intent: CompressionIntent,
    output_mode: str,
    format_check: str,
) -> object | None:
    normalized_mode = output_mode.strip().casefold().replace("-", "_")
    normalized_format = format_check.strip().casefold()
    if normalized_format == "json_shape" or normalized_mode == "json":
        return _parse_json(text)
    if normalized_format == "yaml_shape" or normalized_mode == "yaml":
        return _parse_yaml(text)
    if normalized_format == "table_shape" or normalized_mode == "table":
        return _parse_markdown_table(text)
    if normalized_format == "bullet_shape" or normalized_mode == "bullet_list":
        return _parse_bullet_list(text)
    if canonical_mode_for_intent(intent) == "structured" and intent is CompressionIntent.BULLET_LIST:
        return _parse_bullet_list(text)
    return None


def _parse_json(text: str) -> object | None:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def _parse_yaml(text: str) -> object | None:
    if yaml_module is None:
        return None
    try:
        return yaml_module.safe_load(text)
    except Exception:
        return None


def _parse_markdown_table(text: str) -> list[dict[str, str]] | None:
    rows: list[list[str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    if len(rows) < 2:
        return None
    headers = rows[0]
    divider = rows[1]
    if len(divider) != len(headers):
        return None
    if not all(set(cell) <= {"-", ":"} for cell in divider):
        return None
    parsed: list[dict[str, str]] = []
    for row in rows[2:]:
        if len(row) != len(headers):
            return None
        parsed.append(dict(zip(headers, row, strict=True)))
    return parsed


def _parse_bullet_list(text: str) -> list[str] | None:
    items = [line.strip()[2:].strip() for line in text.splitlines() if line.strip()]
    if not items:
        return None
    if any(not line.strip().startswith("- ") for line in text.splitlines() if line.strip()):
        return None
    return items


def _structured_value_similarity(expected: object, actual: object) -> float:
    expected_pairs = dict(_flatten_structure(expected))
    actual_pairs = dict(_flatten_structure(actual))
    if not expected_pairs:
        return 1.0 if not actual_pairs else 0.0
    expected_keys = set(expected_pairs)
    actual_keys = set(actual_pairs)
    field_score = len(expected_keys & actual_keys) / len(expected_keys)
    if not expected_keys:
        return field_score
    value_scores = [
        _value_similarity(expected_pairs[key], actual_pairs.get(key, ""))
        for key in expected_keys
    ]
    value_score = sum(value_scores) / len(value_scores) if value_scores else 0.0
    return _clamp_ratio((0.55 * field_score) + (0.45 * value_score))


def _flatten_structure(value: object, prefix: str = "") -> list[tuple[str, str]]:
    if isinstance(value, dict):
        flattened: list[tuple[str, str]] = []
        for key in sorted(value):
            next_prefix = f"{prefix}.{key}" if prefix else str(key)
            flattened.extend(_flatten_structure(value[key], next_prefix))
        return flattened
    if isinstance(value, list):
        flattened_items: list[tuple[str, str]] = []
        for index, item in enumerate(value):
            next_prefix = f"{prefix}[{index}]" if prefix else f"[{index}]"
            flattened_items.extend(_flatten_structure(item, next_prefix))
        return flattened_items
    normalized_value = "" if value is None else str(value).strip()
    return [(prefix or "$", normalized_value)]


def _structured_embedding_text(value: object) -> str:
    return "\n".join(f"{path}={payload}" for path, payload in _flatten_structure(value))


def _value_similarity(expected: str, actual: str) -> float:
    expected_text = expected.strip()
    actual_text = actual.strip()
    if not expected_text:
        return 1.0 if not actual_text else 0.0
    if not actual_text:
        return 0.0
    if expected_text == actual_text:
        return 1.0
    expected_tokens = _value_tokens(expected_text)
    actual_tokens = _value_tokens(actual_text)
    if not expected_tokens or not actual_tokens:
        return 0.0
    expected_set = set(expected_tokens)
    actual_set = set(actual_tokens)
    overlap = len(expected_set & actual_set)
    if overlap == 0:
        return 0.0
    precision = overlap / len(actual_set)
    recall = overlap / len(expected_set)
    return (2 * precision * recall) / (precision + recall)


def _value_tokens(text: str) -> tuple[str, ...]:
    return tuple(token.casefold() for token in text.replace("\n", " ").split() if token)


def _cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    numerator = sum(a * b for a, b in zip(left, right, strict=True))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return _clamp_ratio((numerator / (left_norm * right_norm) + 1.0) / 2.0)


def _clamp_ratio(value: float) -> float:
    return max(0.0, min(1.0, value))
