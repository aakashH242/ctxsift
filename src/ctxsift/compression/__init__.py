"""Compression pipeline exports and intent taxonomy."""

from __future__ import annotations

from importlib import import_module
from typing import Any

__all__ = [
    "CanonicalCompressionMode",
    "CompressionIntent",
    "StructuredIntentKind",
    "canonical_mode_for_intent",
    "compress_input",
    "intent_prefers_recall_wording",
    "intent_requires_strict_validation",
    "normalize_instruction",
    "render_run_payload",
    "structured_kind_for_intent",
    "summarize_deterministically",
]


def __getattr__(name: str) -> Any:
    if name in {
        "CanonicalCompressionMode",
        "CompressionIntent",
        "StructuredIntentKind",
        "canonical_mode_for_intent",
        "intent_prefers_recall_wording",
        "intent_requires_strict_validation",
        "structured_kind_for_intent",
    }:
        module = import_module("ctxsift.compression.intent")
        return getattr(module, name)
    if name in {"compress_input", "normalize_instruction", "summarize_deterministically"}:
        module = import_module("ctxsift.compression.pipeline")
        return getattr(module, name)
    if name == "render_run_payload":
        module = import_module("ctxsift.compression.run_payload")
        return getattr(module, name)
    raise AttributeError(name)
