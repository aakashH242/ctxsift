"""LiteLLM remote compression backend."""

from __future__ import annotations

import logging
import re
from typing import Any

from ctxsift.models.base import (
    BackendUnavailableError,
    ModelBackend,
    ModelCompressionInput,
    ModelOutputRejectedError,
    RemoteBackendOptions,
)
from ctxsift.models.text_profile_common import (
    apply_soft_length_hint,
    build_validation_failure_message,
    build_repair_messages,
    build_standard_text_messages,
    choose_preferred_candidate,
    recover_scaffold_prefixed_output,
    selected_candidate_index,
    should_attempt_repair,
    normalize_instruction_aware_output,
    validate_instruction_aware_output,
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
        first_raw_text, first_pass = await self._generate_candidate(
            request,
            self._prepare_messages(request, build_standard_text_messages(request)),
        )
        if request.trace is not None:
            request.trace.record_first_pass(
                raw_output=first_raw_text,
                recovered_output=first_pass,
            )
        first_validation = validate_instruction_aware_output(request, first_pass)
        if not should_attempt_repair(first_validation):
            if request.trace is not None:
                request.trace.record_selected_outputs(
                    raw_output=first_raw_text,
                    recovered_output=first_pass,
                )
            return first_pass

        repair_raw_text, repaired_output = await self._generate_candidate(
            request,
            self._prepare_messages(request, build_repair_messages(request, first_pass)),
        )
        if request.trace is not None:
            request.trace.record_repair_pass(
                raw_output=repair_raw_text,
                recovered_output=repaired_output,
            )
        preferred_candidate = choose_preferred_candidate(request, [first_pass, repaired_output])
        if request.trace is not None:
            selected_index = selected_candidate_index(request, [first_pass, repaired_output])
            request.trace.record_selected_outputs(
                raw_output=_selected_index_output(
                    [first_raw_text, repair_raw_text], selected_index
                ),
                recovered_output=_selected_index_output(
                    [first_pass, repaired_output], selected_index
                ),
            )
        if preferred_candidate is not None:
            return preferred_candidate.output

        repair_validation = validate_instruction_aware_output(request, repaired_output)
        raise ModelOutputRejectedError(
            build_validation_failure_message(
                "litellm",
                first_validation,
                first_pass,
                repair_validation,
                repaired_output,
            )
        )

    async def _generate_candidate(
        self,
        request: ModelCompressionInput,
        messages: list[dict[str, str]],
    ) -> tuple[str, str]:
        raw_text = await self._complete_text(request, messages)
        normalized = normalize_instruction_aware_output(request, raw_text)
        recovered = recover_scaffold_prefixed_output(
            request,
            normalized,
            normalize_output=normalize_instruction_aware_output,
        )
        return raw_text.strip(), recovered

    async def _complete_text(
        self,
        request: ModelCompressionInput,
        messages: list[dict[str, str]],
    ) -> str:
        acompletion = _load_litellm_acompletion()
        try:
            response = await acompletion(
                model=self.model_name,
                messages=messages,
                api_base=self._options.base_url,
                api_key=self._options.api_key or None,
                api_version=self._options.api_version or None,
                max_tokens=request.max_output_tokens,
                timeout=self._options.timeout_ms / 1000,
                num_retries=self._options.retries,
                reasoning_effort=_reasoning_effort(
                    self._options.reasoning_mode,
                    self.model_name,
                ),
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

    def _prepare_messages(
        self,
        request: ModelCompressionInput,
        messages: list[dict[str, str]],
    ) -> list[dict[str, str]]:
        return apply_soft_length_hint(messages, request)


def _selected_index_output(candidates: list[str], selected_index: int | None) -> str:
    if selected_index is None:
        return ""
    if not 0 <= selected_index < len(candidates):
        return ""
    return candidates[selected_index]


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


_OPENAI_O_SERIES_RE = re.compile(r"^o\d+(?:$|[-._])")
_EXPLICIT_REASONING_MARKERS = ("reasoner", "reasoning", "thinking", "qwq")
_ANTHROPIC_REASONING_PREFIXES = (
    "claude-opus-4",
    "claude-sonnet-4",
    "claude-3-7-sonnet",
)
_GEMINI_REASONING_PREFIXES = ("gemini-2.5-",)
_DEEPSEEK_REASONING_PREFIXES = ("deepseek-r1", "deepseek-reasoner")


def _reasoning_effort(reasoning_mode: str, model_name: str) -> str | None:
    normalized = reasoning_mode.strip().casefold()
    if normalized == "auto":
        return "medium" if _is_auto_reasoning_model(model_name) else None
    if normalized == "true":
        return "medium"
    if normalized == "false":
        return "none"
    raise BackendUnavailableError(f"Unsupported remote reasoning mode '{reasoning_mode}'.")


def _is_auto_reasoning_model(model_name: str) -> bool:
    return any(_is_reasoning_model_alias(alias) for alias in _model_aliases(model_name))


def _model_aliases(model_name: str) -> tuple[str, ...]:
    normalized = model_name.strip().casefold().replace("_", "-")
    if not normalized:
        return ()
    slash_segments = tuple(segment for segment in normalized.split("/") if segment)
    return (normalized, *slash_segments)


def _is_reasoning_model_alias(alias: str) -> bool:
    return (
        _is_openai_reasoning_alias(alias)
        or alias.startswith(_DEEPSEEK_REASONING_PREFIXES)
        or alias.startswith(_GEMINI_REASONING_PREFIXES)
        or alias.startswith(_ANTHROPIC_REASONING_PREFIXES)
        or any(marker in alias for marker in _EXPLICIT_REASONING_MARKERS)
    )


def _is_openai_reasoning_alias(alias: str) -> bool:
    if _OPENAI_O_SERIES_RE.match(alias) is not None:
        return True
    if not alias.startswith("gpt-5"):
        return False
    return not (
        alias.startswith("gpt-5-chat") or alias.startswith("gpt-5-instant") or "chatgpt" in alias
    )


def _load_litellm_acompletion():
    try:
        import litellm
        from litellm import acompletion
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("LiteLLM is not installed.") from error
    _configure_litellm_runtime(litellm)
    return acompletion


def _configure_litellm_runtime(litellm_module: Any) -> None:
    # LiteLLM prints a generic "Give Feedback / Get Help" banner on exceptions.
    # Keep that suppressed and let ctxsift surface the actual error text itself.
    litellm_module.suppress_debug_info = True
    _install_logging_worker_filter(logging.getLogger("LiteLLM"))


def _install_logging_worker_filter(logger: logging.Logger) -> None:
    if getattr(logger, "_ctxsift_logging_worker_filter_installed", False):
        return
    logger.addFilter(_LiteLLMLoggingWorkerErrorFilter())
    logger._ctxsift_logging_worker_filter_installed = True  # type: ignore[attr-defined]


class _LiteLLMLoggingWorkerErrorFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.getMessage().startswith("LoggingWorker error:")
