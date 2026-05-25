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


@dataclass(slots=True)
class CompressionTrace:
    """Optional benchmark trace for raw and recovered candidate outputs."""

    first_pass_raw_output: str = ""
    first_pass_recovered_output: str = ""
    repair_pass_raw_output: str = ""
    repair_pass_recovered_output: str = ""
    raw_selected_output: str = ""
    recovered_selected_output: str = ""

    def record_first_pass(self, *, raw_output: str, recovered_output: str) -> None:
        self.first_pass_raw_output = raw_output
        self.first_pass_recovered_output = recovered_output

    def record_repair_pass(self, *, raw_output: str, recovered_output: str) -> None:
        self.repair_pass_raw_output = raw_output
        self.repair_pass_recovered_output = recovered_output

    def record_selected_outputs(self, *, raw_output: str, recovered_output: str) -> None:
        self.raw_selected_output = raw_output
        self.recovered_selected_output = recovered_output


@dataclass(frozen=True)
class ModelCompressionInput:
    """Structured input passed to one model backend."""

    intent: CompressionIntent
    instruction: str
    raw_input: str
    extracted_signal: ExtractedSignal
    max_output_tokens: int
    required_anchors: tuple[str, ...] = ()
    recovery_enabled: bool = True
    evaluation_context: Literal["prod", "benchmark"] = "prod"
    trace: CompressionTrace | None = None


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
