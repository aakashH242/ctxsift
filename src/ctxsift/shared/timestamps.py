"""Timestamp parsing shared across recall modules."""

from __future__ import annotations

from datetime import datetime, timezone


def parse_created_at(created_at: str) -> datetime:
    """Parse a stored created_at timestamp into a timezone-aware UTC datetime."""
    try:
        parsed = datetime.fromisoformat(created_at)
    except ValueError:
        parsed = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)
