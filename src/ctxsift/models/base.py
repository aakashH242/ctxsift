"""Model backend contracts for compression."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Literal

from ctxsift.compression.intent import CompressionIntent
from ctxsift.types import ExtractedSignal


class BackendUnavailableError(RuntimeError):
    """Raised when a configured backend cannot be used."""


class ModelOutputRejectedError(BackendUnavailableError):
    """Raised when a backend runs but its output fails the compression contract."""


@dataclass(frozen=True)
class ModelCompressionInput:
    """Structured input passed to one model backend."""

    intent: CompressionIntent
    instruction: str
    raw_input: str
    extracted_signal: ExtractedSignal
    max_output_tokens: int
    required_anchors: tuple[str, ...] = ()
    evaluation_context: Literal["prod", "benchmark"] = "prod"


@dataclass(frozen=True)
class RemoteBackendOptions:
    """Configuration needed for the LiteLLM remote backend."""

    base_url: str
    api_key: str
    api_version: str
    model_name: str
    reasoning_mode: str
    timeout_ms: int
    retries: int


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

    async def preload(self) -> None:
        """Warm the backend and ensure required model assets are locally available."""
        return None

    async def shutdown(self) -> None:
        """Release heavy runtime state before process shutdown."""
        return None

    @staticmethod
    def text_content(text: str) -> dict[str, Any]:
        """Build one chat-content item."""
        return {"type": "text", "text": text}
