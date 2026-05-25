"""Qwen3-specific compression prompt, generation, cleanup, and validation."""

from __future__ import annotations

from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.text_profile_common import (
    LEAKED_REASONING_TAGS,
    build_standard_text_messages,
    deterministic_generation_kwargs,
    normalize_profile_output,
    strip_reasoning_blocks,
)
from ctxsift.models.text_profile_types import TextModelProfile


def matches_model_name(model_name: str) -> bool:
    """Return whether the configured model should use the Qwen3 profile."""
    normalized = model_name.strip().casefold()
    return normalized.startswith("qwen/qwen3-") or normalized.startswith("qwen3-")


def build_text_messages(request: ModelCompressionInput) -> list[dict[str, str]]:
    """Build a Qwen3-specific plain-text chat history."""
    return build_standard_text_messages(request)


def generation_kwargs(tokenizer: object, max_output_tokens: int) -> dict[str, int | bool]:
    """Return deterministic no-thinking generation kwargs for Qwen3 compression."""
    return deterministic_generation_kwargs(tokenizer, max_output_tokens)


def normalize_output(request: ModelCompressionInput, text: str) -> str:
    """Apply Qwen3-specific cleanup to generated text."""
    without_reasoning = strip_reasoning_blocks(text, *LEAKED_REASONING_TAGS)
    return normalize_profile_output(request, without_reasoning)


PROFILE = TextModelProfile(
    family_name="qwen3",
    matches_model_name=matches_model_name,
    build_text_messages=build_text_messages,
    generation_kwargs=generation_kwargs,
    normalize_output=normalize_output,
)
