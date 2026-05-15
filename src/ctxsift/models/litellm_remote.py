"""LiteLLM remote compression backend."""

from __future__ import annotations

from typing import Any

from ctxsift.compression_prompt import build_messages
from ctxsift.models.base import (
    BackendUnavailableError,
    ModelBackend,
    ModelCompressionInput,
    RemoteBackendOptions,
)


class LiteLLMRemoteBackend(ModelBackend):
    """Async remote compression backend via LiteLLM chat completions."""

    provider_name = "litellm"

    def __init__(self, options: RemoteBackendOptions) -> None:
        self._options = options
        self.model_name = options.model_name

    @property
    def cache_model_id(self) -> str:
        return f"litellm:{self.model_name}@{self._options.base_url}"

    async def compress(self, request: ModelCompressionInput) -> str:
        acompletion = _load_litellm_acompletion()
        try:
            response = await acompletion(
                model=self.model_name,
                messages=build_messages(request),
                api_base=self._options.base_url,
                api_key=self._options.api_key or None,
                api_version=self._options.api_version or None,
                max_tokens=request.max_output_tokens,
                timeout=self._options.timeout_ms / 1000,
                num_retries=self._options.retries,
                reasoning_effort=_reasoning_effort(self._options.reasoning_mode),
            )
        except BackendUnavailableError:
            raise
        except Exception as error:
            raise BackendUnavailableError(
                f"LiteLLM remote backend request failed: {error}"
            ) from error
        text = _response_text(response)
        if not text:
            raise BackendUnavailableError("LiteLLM backend returned empty output.")
        return text


def _response_text(response: Any) -> str:
    try:
        message = response.choices[0].message
    except (AttributeError, IndexError, TypeError) as error:
        raise BackendUnavailableError("LiteLLM response did not contain a chat message.") from error
    content = getattr(message, "content", None)
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        text_parts = [
            item.get("text", "").strip()
            for item in content
            if isinstance(item, dict) and item.get("type") == "text"
        ]
        return "\n".join(part for part in text_parts if part).strip()
    return ""


def _reasoning_effort(reasoning_mode: str) -> str | None:
    normalized = reasoning_mode.strip().casefold()
    if normalized == "auto":
        return None
    if normalized == "true":
        return "medium"
    if normalized == "false":
        return "none"
    raise BackendUnavailableError(f"Unsupported remote reasoning mode '{reasoning_mode}'.")


def _load_litellm_acompletion():
    try:
        from litellm import acompletion
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("LiteLLM is not installed.") from error
    return acompletion
