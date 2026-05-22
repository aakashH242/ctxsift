"""Recall search: orchestration, hybrid fusion, ranking, and freshness."""

from ctxsift.recall.freshness import assess_record_freshness
from ctxsift.recall.hybrid import HybridRecallRequest, build_hybrid_records
from ctxsift.recall.matches import file_filters_match, file_values, path_match_strength
from ctxsift.recall.ranking import RankingRequest, rank_records

__all__ = [
    "HybridRecallRequest",
    "RankingRequest",
    "assess_record_freshness",
    "build_hybrid_records",
    "file_filters_match",
    "file_values",
    "path_match_strength",
    "rank_records",
]


def recall_records(*args, **kwargs):
    """Lazy import to avoid circular dependency with storage/retention."""
    from ctxsift.recall.orchestrator import recall_records as _recall_records

    return _recall_records(*args, **kwargs)


def render_recall_records(*args, **kwargs):
    """Lazy import to avoid circular dependency with storage/retention."""
    from ctxsift.recall.orchestrator import render_recall_records as _render_recall_records

    return _render_recall_records(*args, **kwargs)
