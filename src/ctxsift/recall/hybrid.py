"""Hybrid fusion for lexical and vector recall."""

from __future__ import annotations

from dataclasses import dataclass

from ctxsift.recall.matches import file_filters_match
from ctxsift.shared.dedupe import dedupe
from ctxsift.shared.timestamps import parse_created_at
from ctxsift.types import (
    ExtractedTermRecord,
    FreshnessStatus,
    RecallRecord,
    RecallStorageRecord,
    VectorSearchHit,
)

RRF_OFFSET = 50
LEXICAL_WEIGHT = 1.0
VECTOR_WEIGHT = 0.85
RANK_SCORE_SCALE = 1000
FILE_FILTER_BONUS = 0.09
MATCHED_FIELD_BONUS = 0.02
EXACT_FILE_HIT_BONUS = 0.08
EXACT_SYMBOL_HIT_BONUS = 0.07
EXACT_TEST_HIT_BONUS = 0.07

FRESHNESS_ADJUSTMENTS = {
    FreshnessStatus.FRESH: 0.06,
    FreshnessStatus.UNKNOWN: 0.0,
    FreshnessStatus.UNVERIFIABLE: -0.01,
    FreshnessStatus.STALE_CHANGED: -0.07,
    FreshnessStatus.STALE_DELETED: -0.12,
}


@dataclass(frozen=True)
class HybridRecallRequest:
    """Inputs needed to fuse lexical and vector recall results."""

    lexical_records: list[RecallStorageRecord]
    all_records: list[RecallStorageRecord]
    vector_hits: list[VectorSearchHit]
    freshness_by_record_id: dict[int, FreshnessStatus]
    file_filters: list[str]
    limit: int
    normalized_query: str
    search_terms: list[str]
    max_vector_distance: float
    min_score: int
    weak_fallback_min_score: int
    weak_fallback_limit: int


def build_hybrid_records(request: HybridRecallRequest) -> list[RecallRecord]:
    """Fuse lexical and vector recall results with weighted RRF."""
    record_map = {record.record_id: record for record in request.all_records}
    lexical_ranks = _rank_positions([record.record_id for record in request.lexical_records])
    vector_ranks = _rank_positions(
        [
            hit.record_id
            for hit in request.vector_hits
            if _vector_hit_allowed(hit, lexical_ranks, request.max_vector_distance)
        ]
    )
    candidate_ids = _candidate_ids(lexical_ranks, vector_ranks, record_map)
    recall_records = [
        _build_recall_record(record_map[record_id], request, lexical_ranks, vector_ranks)
        for record_id in candidate_ids
    ]
    filtered_records = _post_filter_file_matches(recall_records, request.file_filters)
    filtered_records.sort(
        key=lambda item: (
            item.score,
            parse_created_at(item.created_at).timestamp(),
            item.record_id,
        ),
        reverse=True,
    )
    return _apply_score_thresholds(filtered_records, request)


def _candidate_ids(
    lexical_ranks: dict[int, int],
    vector_ranks: dict[int, int],
    record_map: dict[int, RecallStorageRecord],
) -> list[int]:
    return [
        record_id for record_id in {*(lexical_ranks), *(vector_ranks)} if record_id in record_map
    ]


def _vector_hit_allowed(
    hit: VectorSearchHit,
    lexical_ranks: dict[int, int],
    max_vector_distance: float,
) -> bool:
    if hit.record_id in lexical_ranks:
        return True
    return hit.distance <= max_vector_distance


def _build_recall_record(
    record: RecallStorageRecord,
    request: HybridRecallRequest,
    lexical_ranks: dict[int, int],
    vector_ranks: dict[int, int],
) -> RecallRecord:
    matched_fields = list(record.matched_fields)
    if record.record_id in vector_ranks:
        matched_fields.append("vector")
    matched_fields = dedupe(matched_fields)
    score = _hybrid_score(
        record_id=record.record_id,
        lexical_ranks=lexical_ranks,
        vector_ranks=vector_ranks,
        freshness=request.freshness_by_record_id[record.record_id],
        matched_fields=matched_fields,
        file_filter_match=file_filters_match(record, request.file_filters),
        exact_file_hit=_exact_file_hit(record, request.normalized_query, request.search_terms),
        exact_symbol_hit=_exact_term_hit(
            record.extracted_terms,
            request.normalized_query,
            request.search_terms,
            "symbol",
        ),
        exact_test_hit=_exact_term_hit(
            record.extracted_terms,
            request.normalized_query,
            request.search_terms,
            "test",
        ),
    )
    return RecallRecord(
        record_id=record.record_id,
        created_at=record.created_at,
        freshness_status=request.freshness_by_record_id[record.record_id],
        instruction=record.instruction,
        compressed_output=record.compressed_output,
        command=record.command,
        command_exit_code=record.command_exit_code,
        referenced_files=[item.path for item in record.referenced_files],
        matched_fields=matched_fields,
        score=score,
    )


def _hybrid_score(
    record_id: int,
    lexical_ranks: dict[int, int],
    vector_ranks: dict[int, int],
    freshness: FreshnessStatus,
    matched_fields: list[str],
    file_filter_match: bool,
    exact_file_hit: bool,
    exact_symbol_hit: bool,
    exact_test_hit: bool,
) -> int:
    score = 0.0
    lexical_rank = lexical_ranks.get(record_id)
    if lexical_rank is not None:
        score += LEXICAL_WEIGHT / (RRF_OFFSET + lexical_rank)
    vector_rank = vector_ranks.get(record_id)
    if vector_rank is not None:
        score += VECTOR_WEIGHT / (RRF_OFFSET + vector_rank)
    score += FRESHNESS_ADJUSTMENTS[freshness]
    score += min(len(matched_fields), 5) * MATCHED_FIELD_BONUS
    if file_filter_match:
        score += FILE_FILTER_BONUS
    if exact_file_hit:
        score += EXACT_FILE_HIT_BONUS
    if exact_symbol_hit:
        score += EXACT_SYMBOL_HIT_BONUS
    if exact_test_hit:
        score += EXACT_TEST_HIT_BONUS
    return int(round(score * RANK_SCORE_SCALE))


def _post_filter_file_matches(
    records: list[RecallRecord],
    file_filters: list[str],
) -> list[RecallRecord]:
    if not file_filters:
        return records
    matches = [
        record for record in records if _recall_record_matches_file_filter(record, file_filters)
    ]
    if matches:
        return matches
    return records


def _apply_score_thresholds(
    records: list[RecallRecord],
    request: HybridRecallRequest,
) -> list[RecallRecord]:
    strong_matches = [record for record in records if record.score >= request.min_score]
    if strong_matches:
        return strong_matches[: request.limit]
    if request.weak_fallback_limit <= 0:
        return []
    weak_matches = [record for record in records if record.score >= request.weak_fallback_min_score]
    if not weak_matches:
        return []
    allowed_limit = min(request.limit, request.weak_fallback_limit)
    return weak_matches[:allowed_limit]


def _recall_record_matches_file_filter(record: RecallRecord, file_filters: list[str]) -> bool:
    values = [path.casefold().replace("\\", "/") for path in record.referenced_files]
    for value in values:
        for file_filter in file_filters:
            normalized_filter = file_filter.casefold().replace("\\", "/")
            if (
                value == normalized_filter
                or value.endswith(f"/{normalized_filter}")
                or normalized_filter in value
            ):
                return True
    return False


def _rank_positions(record_ids: list[int]) -> dict[int, int]:
    return {record_id: index for index, record_id in enumerate(record_ids, start=1)}


def _exact_file_hit(
    record: RecallStorageRecord,
    normalized_query: str,
    search_terms: list[str],
) -> bool:
    values = [
        path.casefold().replace("\\", "/")
        for path in [item.path for item in record.referenced_files]
    ]
    for value in values:
        if normalized_query and (
            value == normalized_query or value.endswith(f"/{normalized_query}")
        ):
            return True
        for term in search_terms:
            if value == term or value.endswith(f"/{term}"):
                return True
    return False


def _exact_term_hit(
    extracted_terms: list[ExtractedTermRecord],
    normalized_query: str,
    search_terms: list[str],
    kind: str,
) -> bool:
    terms = [item.term.casefold() for item in extracted_terms if item.kind == kind]
    if normalized_query and normalized_query in terms:
        return True
    return any(term in terms for term in search_terms)
