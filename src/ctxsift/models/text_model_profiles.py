"""Registry for local text-model compression profiles."""

from __future__ import annotations

from ctxsift.models.granite_profile import PROFILE as GRANITE_PROFILE
from ctxsift.models.gemma_profile import PROFILE as GEMMA_PROFILE
from ctxsift.models.phi_profile import PROFILE as PHI_PROFILE
from ctxsift.models.qwen25_profile import PROFILE as QWEN25_PROFILE
from ctxsift.models.qwen3_profile import PROFILE as QWEN3_PROFILE
from ctxsift.models.qwen35_profile import PROFILE as QWEN35_PROFILE
from ctxsift.models.smollm2_profile import PROFILE as SMOLLM2_PROFILE
from ctxsift.models.text_profile_common import (
    build_standard_text_messages,
    deterministic_generation_kwargs,
    normalize_instruction_aware_output,
)
from ctxsift.models.text_profile_types import TextModelProfile


def _matches_fallback(model_name: str) -> bool:
    del model_name
    return True


FALLBACK_PROFILE = TextModelProfile(
    family_name="fallback",
    matches_model_name=_matches_fallback,
    build_text_messages=build_standard_text_messages,
    generation_kwargs=deterministic_generation_kwargs,
    normalize_output=normalize_instruction_aware_output,
)

REGISTERED_TEXT_MODEL_PROFILES: tuple[TextModelProfile, ...] = (
    GEMMA_PROFILE,
    QWEN25_PROFILE,
    QWEN3_PROFILE,
    QWEN35_PROFILE,
    SMOLLM2_PROFILE,
    GRANITE_PROFILE,
    PHI_PROFILE,
)


def resolve_text_model_profile(model_name: str) -> TextModelProfile:
    """Resolve the configured text-model profile by model name."""
    for profile in REGISTERED_TEXT_MODEL_PROFILES:
        if profile.matches_model_name(model_name):
            return profile
    return FALLBACK_PROFILE
