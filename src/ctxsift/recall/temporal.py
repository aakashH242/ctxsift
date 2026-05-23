"""Temporal helpers for recall ranking and rendering."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from ctxsift.shared.timestamps import parse_created_at

RECENT_QUERY_TERMS = frozenset(
    {
        "current",
        "latest",
        "newest",
        "recent",
        "today",
        "yesterday",
    }
)

BASE_RECENCY_WEIGHT = 0.75
RECENT_QUERY_RECENCY_WEIGHT = 2.0
RECENT_QUERY_MAX_BONUS = 0.18
RECENT_QUERY_BONUS_STEP = 0.02


def recency_weight(normalized_query: str, search_terms: list[str]) -> float:
    """Return the recency weight to use for this recall query."""
    if prefers_recent_records(normalized_query, search_terms):
        return RECENT_QUERY_RECENCY_WEIGHT
    return BASE_RECENCY_WEIGHT


def prefers_recent_records(normalized_query: str, search_terms: list[str]) -> bool:
    """Return whether the query explicitly asks for recent results."""
    if _contains_recent_term(normalized_query):
        return True
    return any(term in RECENT_QUERY_TERMS for term in search_terms)


def render_capture_time(created_at: str, now: datetime | None = None) -> str:
    """Render one capture timestamp line for recall output."""
    captured_at = parse_created_at(created_at)
    current_time = now or datetime.now(timezone.utc)
    relative_age = _relative_age(captured_at, current_time)
    suffix = "" if relative_age == "just now" else " ago"
    return (
        f"Captured at: {captured_at.isoformat().replace('+00:00', 'Z')}"
        f" ({relative_age}{suffix})"
    )


def recent_query_bonus(recency_rank: int | None, prefer_recent: bool) -> float:
    """Return an explicit bonus for recency-focused queries."""
    if not prefer_recent or recency_rank is None:
        return 0.0
    return max(0.0, RECENT_QUERY_MAX_BONUS - ((recency_rank - 1) * RECENT_QUERY_BONUS_STEP))


def _contains_recent_term(normalized_query: str) -> bool:
    query = f" {normalized_query} "
    return any(f" {term} " in query for term in RECENT_QUERY_TERMS)


def _relative_age(captured_at: datetime, current_time: datetime) -> str:
    if current_time < captured_at:
        return "just now"
    delta = current_time - captured_at
    if delta < timedelta(minutes=1):
        return "just now"
    if delta < timedelta(hours=1):
        minutes = max(int(delta.total_seconds() // 60), 1)
        return _pluralized(minutes, "minute")
    if delta < timedelta(days=1):
        hours = max(int(delta.total_seconds() // 3600), 1)
        return _pluralized(hours, "hour")
    days = max(delta.days, 1)
    return _pluralized(days, "day")


def _pluralized(value: int, unit: str) -> str:
    suffix = "" if value == 1 else "s"
    return f"{value} {unit}{suffix}"
