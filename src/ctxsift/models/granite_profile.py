"""Granite-specific compression prompt, generation, cleanup, and validation."""

from __future__ import annotations

import re

from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.text_profile_common import (
    build_standard_text_messages,
    deterministic_generation_kwargs,
    normalize_profile_output,
    strip_reasoning_blocks,
)
from ctxsift.models.text_profile_types import TextModelProfile

GRANITE_REASONING_TAGS = ("think", "thinking", "thought", "analysis", "reasoning")


def matches_model_name(model_name: str) -> bool:
    """Return whether the configured model should use the Granite profile."""
    normalized = model_name.strip().casefold()
    return normalized.startswith("ibm-granite/") or normalized.startswith("granite-")


def build_text_messages(request: ModelCompressionInput) -> list[dict[str, str]]:
    """Build a Granite-specific plain-text chat history."""
    return build_standard_text_messages(request)


def generation_kwargs(tokenizer: object, max_output_tokens: int) -> dict[str, int | bool]:
    """Return deterministic generation kwargs for Granite compression."""
    return deterministic_generation_kwargs(tokenizer, max_output_tokens)


def normalize_output(request: ModelCompressionInput, text: str) -> str:
    """Apply Granite-specific cleanup to generated text."""
    without_think = strip_reasoning_blocks(text, *GRANITE_REASONING_TAGS)
    without_response_wrapper = re.sub(r"</?response>", "", without_think, flags=re.IGNORECASE)
    return normalize_profile_output(request, without_response_wrapper)


PROFILE = TextModelProfile(
    family_name="granite",
    matches_model_name=matches_model_name,
    build_text_messages=build_text_messages,
    generation_kwargs=generation_kwargs,
    normalize_output=normalize_output,
)
