"""Shared file-match helpers for recall."""

from __future__ import annotations

from ctxsift.types import RecallStorageRecord


def file_values(record: RecallStorageRecord) -> list[str]:
    """Return normalized file-path values for one record."""
    values = [item.path.casefold().replace("\\", "/") for item in record.referenced_files]
    values.extend(
        item.abs_path.casefold().replace("\\", "/")
        for item in record.referenced_files
        if item.abs_path
    )
    return values


def path_match_strength(value: str, normalized_query: str, search_terms: list[str]) -> int:
    """Score one file-path match against the query surface."""
    strength = 0
    if normalized_query:
        if value == normalized_query:
            strength += 12
        elif value.endswith(f"/{normalized_query}"):
            strength += 10
        elif normalized_query in value:
            strength += 6
    for term in search_terms:
        if term == normalized_query:
            continue
        if value == term:
            strength += 6
        elif value.endswith(f"/{term}"):
            strength += 5
        elif term in value:
            strength += 2
    return strength


def file_filters_match(record: RecallStorageRecord, file_filters: list[str]) -> bool:
    """Return whether one record matches any requested file filter."""
    if not file_filters:
        return True
    values = file_values(record)
    return any(path_match_strength(value, query, [query]) > 0 for value in values for query in file_filters)
