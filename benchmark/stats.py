"""Shared statistical helpers for benchmark summaries and viewer fallbacks."""

from __future__ import annotations

from typing import Sequence


def percentile(values: Sequence[float], fraction: float) -> float:
    """Return a linearly interpolated percentile for one numeric sequence."""
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = (len(ordered) - 1) * fraction
    lower = int(rank)
    upper = min(lower + 1, len(ordered) - 1)
    if lower == upper:
        return ordered[lower]
    step = rank - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * step