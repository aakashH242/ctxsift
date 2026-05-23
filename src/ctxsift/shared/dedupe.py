"""Order-preserving deduplication for string lists."""

from __future__ import annotations


def dedupe(values: list[str]) -> list[str]:
    """Remove duplicate strings while preserving insertion order."""
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result
