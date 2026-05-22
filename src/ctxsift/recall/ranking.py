"""Ranking helpers for recall search results."""

from __future__ import annotations

from dataclasses import dataclass

from ctxsift.recall.matches import file_filters_match, file_values, path_match_strength
from ctxsift.recall.temporal import recent_query_bonus
from ctxsift.shared.timestamps import parse_created_at
from ctxsift.types import RecallStorageRecord

RANK_FUSION_OFFSET = 50
RANK_SCORE_SCALE = 1000

SOURCE_WEIGHTS = {
    "fts": 5.0,
    "instruction": 3.0,
    "compressed_output": 3.0,
    "command": 2.5,
    "file_paths": 4.0,
    "extracted_terms": 4.5,
}


@dataclass(frozen=True)
class RankingRequest:
    """Inputs required to rank recall candidates."""

    records: list[RecallStorageRecord]
    fts_ranks: dict[int, int]
    normalized_query: str
    search_terms: list[str]
    file_filters: list[str]
    recency_weight: float
    prefer_recent: bool


def rank_records(request: RankingRequest) -> list[RecallStorageRecord]:
    """Rank recall candidates using evidence-specific rankings plus recency."""
    rankings = _source_rankings(request)
    filtered_records = _filtered_records(request.records, request.file_filters)
    scored_records: list[RecallStorageRecord] = []
    for record in filtered_records:
        matched_fields = _matched_fields(
            record,
            request.normalized_query,
            request.search_terms,
            request.fts_ranks,
        )
        if request.file_filters and "file_paths" not in matched_fields:
            matched_fields.append("file_paths")
        total_score = _fusion_score(record.record_id, rankings, request.recency_weight)
        total_score += _coverage_bonus(matched_fields)
        if request.file_filters:
            total_score += 0.08
        total_score += recent_query_bonus(
            rankings["recency"].get(record.record_id),
            request.prefer_recent,
        )
        score = int(round(total_score * RANK_SCORE_SCALE))
        scored_records.append(
            record.model_copy(
                update={
                    "matched_fields": matched_fields,
                    "score": score,
                }
            )
        )
    scored_records.sort(
        key=lambda item: (
            item.score,
            _created_at_timestamp(item.created_at),
            item.record_id,
        ),
        reverse=True,
    )
    return scored_records


def _source_rankings(request: RankingRequest) -> dict[str, dict[int, int]]:
    rankings = {
        "fts": _fts_rankings(request.fts_ranks),
        "instruction": _field_rankings(
            request.records,
            lambda item: _text_match_strength(
                request.normalized_query,
                request.search_terms,
                item.instruction,
            ),
        ),
        "compressed_output": _field_rankings(
            request.records,
            lambda item: _text_match_strength(
                request.normalized_query,
                request.search_terms,
                item.compressed_output,
            ),
        ),
        "command": _field_rankings(
            request.records,
            lambda item: _text_match_strength(
                request.normalized_query,
                request.search_terms,
                item.command or "",
            ),
        ),
        "file_paths": _field_rankings(
            request.records,
            lambda item: _file_match_strength(
                request.normalized_query,
                request.search_terms,
                item,
            ),
        ),
        "extracted_terms": _field_rankings(
            request.records,
            lambda item: _term_match_strength(
                request.normalized_query,
                request.search_terms,
                item,
            ),
        ),
        "recency": _recency_rankings(request.records),
    }
    return rankings


def _fts_rankings(fts_ranks: dict[int, int]) -> dict[int, int]:
    return {record_id: rank for record_id, rank in fts_ranks.items()}


def _field_rankings(
    records: list[RecallStorageRecord],
    strength_for_record,
) -> dict[int, int]:
    ranked = [(record, strength_for_record(record)) for record in records]
    ranked = [(record, strength) for record, strength in ranked if strength > 0]
    ranked.sort(
        key=lambda item: (
            item[1],
            _created_at_timestamp(item[0].created_at),
            item[0].record_id,
        ),
        reverse=True,
    )
    return {record.record_id: index for index, (record, _) in enumerate(ranked, start=1)}


def _recency_rankings(records: list[RecallStorageRecord]) -> dict[int, int]:
    ordered = sorted(
        records,
        key=lambda item: (_created_at_timestamp(item.created_at), item.record_id),
        reverse=True,
    )
    return {record.record_id: index for index, record in enumerate(ordered, start=1)}


def _fusion_score(
    record_id: int,
    rankings: dict[str, dict[int, int]],
    recent_weight: float,
) -> float:
    total = 0.0
    for source_name, record_ranks in rankings.items():
        rank = record_ranks.get(record_id)
        if rank is None:
            continue
        total += _source_weight(source_name, recent_weight) / (RANK_FUSION_OFFSET + rank)
    return total


def _source_weight(source_name: str, recent_weight: float) -> float:
    if source_name == "recency":
        return recent_weight
    return SOURCE_WEIGHTS[source_name]


def _coverage_bonus(matched_fields: list[str]) -> float:
    coverage = len(matched_fields)
    if coverage <= 1:
        return 0.0
    return min(coverage - 1, 4) * 0.06


def _matched_fields(
    record: RecallStorageRecord,
    normalized_query: str,
    search_terms: list[str],
    fts_ranks: dict[int, int],
) -> list[str]:
    matched_fields: list[str] = []
    if record.record_id in fts_ranks:
        matched_fields.append("fts")
    if _text_match_strength(normalized_query, search_terms, record.instruction) > 0:
        matched_fields.append("instruction")
    if _text_match_strength(normalized_query, search_terms, record.compressed_output) > 0:
        matched_fields.append("compressed_output")
    if _text_match_strength(normalized_query, search_terms, record.command or "") > 0:
        matched_fields.append("command")
    if _file_match_strength(normalized_query, search_terms, record) > 0:
        matched_fields.append("file_paths")
    if _term_match_strength(normalized_query, search_terms, record) > 0:
        matched_fields.append("extracted_terms")
    return matched_fields


def _filtered_records(
    records: list[RecallStorageRecord],
    file_filters: list[str],
) -> list[RecallStorageRecord]:
    if not file_filters:
        return records
    filtered: list[RecallStorageRecord] = []
    for record in records:
        if file_filters_match(record, file_filters):
            filtered.append(record)
    return filtered


def _text_match_strength(normalized_query: str, search_terms: list[str], value: str) -> int:
    normalized_value = value.casefold()
    if not normalized_value:
        return 0
    strength = 0
    if normalized_query and normalized_query in normalized_value:
        strength += 8
    for term in search_terms:
        if term == normalized_query:
            continue
        if term in normalized_value:
            strength += 2
    return strength


def _file_match_strength(
    normalized_query: str,
    search_terms: list[str],
    record: RecallStorageRecord,
) -> int:
    values = file_values(record)
    strengths = [path_match_strength(value, normalized_query, search_terms) for value in values]
    return max(strengths, default=0)


def _term_match_strength(
    normalized_query: str,
    search_terms: list[str],
    record: RecallStorageRecord,
) -> int:
    values = [item.term.casefold() for item in record.extracted_terms]
    if not values:
        return 0
    strength = 0
    if normalized_query and normalized_query in values:
        strength += 10
    for term in search_terms:
        if term == normalized_query:
            continue
        if term in values:
            strength += 3
    return strength


def _created_at_timestamp(created_at: str) -> float:
    return parse_created_at(created_at).timestamp()
