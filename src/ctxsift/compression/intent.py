"""Public compression intents and canonical output-contract mapping."""

from __future__ import annotations

from enum import Enum
from typing import Literal


class CompressionIntent(str, Enum):
    """Public output contracts that callers can request explicitly."""

    SUMMARY = "summary"
    RECALL = "recall"
    EXACT_LINES = "exact-lines"
    EXACT_FORMAT = "exact-format"
    JSON = "json"
    YAML = "yaml"
    TABLE = "table"
    BULLET_LIST = "bullet-list"


CanonicalCompressionMode = Literal["plain-text", "structured", "exact-lines", "exact-format"]
StructuredIntentKind = Literal["json", "yaml", "table", "bullet-list"]


def canonical_mode_for_intent(intent: CompressionIntent) -> CanonicalCompressionMode:
    """Map one public intent onto the shared internal validator/prompt contract."""
    if intent in {CompressionIntent.SUMMARY, CompressionIntent.RECALL}:
        return "plain-text"
    if intent is CompressionIntent.EXACT_LINES:
        return "exact-lines"
    if intent is CompressionIntent.EXACT_FORMAT:
        return "exact-format"
    return "structured"


def structured_kind_for_intent(intent: CompressionIntent) -> StructuredIntentKind | None:
    """Return the structured subtype when the intent requires one."""
    if intent is CompressionIntent.JSON:
        return "json"
    if intent is CompressionIntent.YAML:
        return "yaml"
    if intent is CompressionIntent.TABLE:
        return "table"
    if intent is CompressionIntent.BULLET_LIST:
        return "bullet-list"
    return None


def intent_prefers_recall_wording(intent: CompressionIntent) -> bool:
    """Return whether the prompt should emphasize later recall usefulness."""
    return intent is CompressionIntent.RECALL


def intent_requires_strict_validation(intent: CompressionIntent) -> bool:
    """Return whether the intent should use strict mode-aware hard rejection."""
    return canonical_mode_for_intent(intent) != "plain-text"
