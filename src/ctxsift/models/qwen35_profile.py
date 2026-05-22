"""Qwen3.5-specific compression prompt, generation, cleanup, and validation."""

from __future__ import annotations

from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.text_profile_common import (
    build_standard_text_messages,
    deterministic_generation_kwargs,
    normalize_profile_output,
    validate_instruction_aware_output,
)
from ctxsift.models.text_profile_types import TextModelProfile


def matches_model_name(model_name: str) -> bool:
    """Return whether the configured model should use the Qwen3.5 profile."""
    normalized = model_name.strip().casefold()
    return normalized.startswith("qwen/qwen3.5-") or normalized.startswith("qwen3.5-")


def build_text_messages(request: ModelCompressionInput) -> list[dict[str, str]]:
    """Build a Qwen3.5-specific text-only chat history."""
    return build_standard_text_messages(request)


def generation_kwargs(tokenizer: object, max_output_tokens: int) -> dict[str, int | bool]:
    """Return deterministic generation kwargs for Qwen3.5 compression."""
    return deterministic_generation_kwargs(tokenizer, max_output_tokens)


def normalize_output(request: ModelCompressionInput | str, text: str | None = None) -> str:
    """Apply Qwen3.5-specific cleanup to generated text."""
    if text is None:
        return normalize_profile_output(str(request))
    if isinstance(request, str):
        raise TypeError("request context is required when text is provided")
    return normalize_profile_output(request, text)


def is_valid_output(request: ModelCompressionInput, text: str) -> bool:
    """Backward-compatible boolean validation shim for the shared validator."""
    normalized = normalize_output(request, text)
    return validate_instruction_aware_output(request, normalized).status != "rejected"


PROFILE = TextModelProfile(
    family_name="qwen3.5",
    matches_model_name=matches_model_name,
    build_text_messages=build_text_messages,
    generation_kwargs=generation_kwargs,
    normalize_output=normalize_output,
)
