"""Model backend contracts for compression."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from ctxsift.types import ExtractedSignal


class BackendUnavailableError(RuntimeError):
    """Raised when a configured backend cannot be used."""


@dataclass(frozen=True)
class ModelCompressionInput:
    """Structured input passed to one model backend."""

    instruction: str
    raw_input: str
    extracted_signal: ExtractedSignal
    max_output_tokens: int


class ModelBackend(ABC):
    """Async compression backend interface."""

    provider_name: str
    model_name: str

    @property
    @abstractmethod
    def cache_model_id(self) -> str:
        """Stable model identifier used in cache keys."""

    @abstractmethod
    async def compress(self, request: ModelCompressionInput) -> str:
        """Produce one compressed output string."""

    @staticmethod
    def text_content(text: str) -> dict[str, Any]:
        """Build one chat-content item."""
        return {"type": "text", "text": text}
