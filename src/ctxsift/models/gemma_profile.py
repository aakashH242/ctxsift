"""Gemma-specific compression prompt, generation, cleanup, and validation."""

from __future__ import annotations

from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.text_profile_common import (
    build_standard_text_messages,
    deterministic_generation_kwargs,
    normalize_profile_output,
)
from ctxsift.models.text_profile_types import TextModelProfile


def matches_model_name(model_name: str) -> bool:
    """Return whether the configured model should use the Gemma profile."""
    normalized = model_name.strip().casefold()
    return normalized.startswith("google/gemma-") or normalized.startswith("gemma-")


def build_text_messages(request: ModelCompressionInput) -> list[dict[str, str]]:
    """Build a Gemma-specific plain-text chat history."""
    return build_standard_text_messages(request)


def generation_kwargs(tokenizer: object, max_output_tokens: int) -> dict[str, int | bool]:
    """Return deterministic generation kwargs for Gemma compression."""
    return deterministic_generation_kwargs(tokenizer, max_output_tokens)


def normalize_output(request: ModelCompressionInput, text: str) -> str:
    """Apply Gemma-specific cleanup to generated text."""
    return normalize_profile_output(request, text)


PROFILE = TextModelProfile(
    family_name="gemma",
    matches_model_name=matches_model_name,
    build_text_messages=build_text_messages,
    generation_kwargs=generation_kwargs,
    normalize_output=normalize_output,
)
