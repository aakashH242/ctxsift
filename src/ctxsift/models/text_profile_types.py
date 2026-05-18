"""Shared contract for local text-model compression profiles."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from ctxsift.models.base import ModelCompressionInput


@dataclass(frozen=True)
class TextModelProfile:
    """One model-family profile used by the local Transformers text backend."""

    family_name: str
    matches_model_name: Callable[[str], bool]
    build_text_messages: Callable[[ModelCompressionInput], list[dict[str, str]]]
    generation_kwargs: Callable[[object, int], dict[str, Any]]
    normalize_output: Callable[[ModelCompressionInput, str], str]
    trust_remote_code: bool = False

    def is_valid_output(self, request: ModelCompressionInput, text: str) -> bool:
        """Backward-compatible boolean view over the shared validator core."""
        from ctxsift.models.text_profile_common import validate_instruction_aware_output

        normalized = self.normalize_output(request, text)
        return validate_instruction_aware_output(request, normalized).status != "rejected"
