"""Local CPU compression backend built on embedded llama.cpp."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ctxsift.models.base import (
    BackendUnavailableError,
    ModelBackend,
    ModelCompressionInput,
    ModelOutputRejectedError,
)
from ctxsift.models.hf_hub_cache import resolve_or_download_hf_file
from ctxsift.models.local_runtime import (
    required_gguf_filename,
    recommended_llama_threads,
    should_apply_soft_length_hint,
)
from ctxsift.models.text_model_profiles import resolve_text_model_profile
from ctxsift.models.text_profile_common import (
    apply_soft_length_hint,
    build_validation_failure_message,
    build_cpu_protection_messages,
    build_cpu_protection_repair_messages,
    build_repair_messages,
    choose_preferred_candidate,
    normalize_cpu_protection_output,
    recover_scaffold_prefixed_output,
    selected_candidate_index,
    should_attempt_repair,
    validate_instruction_aware_output,
)
from ctxsift.types import LocalModelConfig

DEFAULT_LLAMA_CONTEXT_WINDOW = 8192
DEFAULT_LLAMA_BATCH_SIZE = 512
DEFAULT_LLAMA_TEMPERATURE = 0.0
DEFAULT_LLAMA_STOP_SEQUENCES = ("<|assistant|>", "<|user|>", "<|system|>")


def resolved_llama_context_window(config: LocalModelConfig) -> int:
    """Return the configured llama.cpp context window or the repo default."""
    return config.llama_context_window or DEFAULT_LLAMA_CONTEXT_WINDOW


@dataclass(frozen=True)
class LlamaRuntime:
    """Loaded llama.cpp runtime and the GGUF source it was opened from."""

    model: Any
    model_path: Path


class LlamaCppBackend(ModelBackend):
    """Async local compression backend for CPU llama.cpp inference."""

    provider_name = "llama_cpp"

    def __init__(self, config: LocalModelConfig) -> None:
        self._config = config
        self.model_name = config.model
        self._profile = resolve_text_model_profile(config.model)
        self._runtime: LlamaRuntime | None = None
        self._runtime_lock = asyncio.Lock()
        self._use_soft_length_hint = should_apply_soft_length_hint(
            config,
            provider_name=self.provider_name,
        )

    @property
    def cache_model_id(self) -> str:
        return f"{self.model_name}::{required_gguf_filename(self._config)}"

    async def compress(self, request: ModelCompressionInput) -> str:
        runtime = await self._get_runtime()
        return await asyncio.to_thread(self._generate_text, runtime, request)

    async def preload(self) -> None:
        await self._get_runtime()

    async def shutdown(self) -> None:
        self._runtime = None

    async def _get_runtime(self) -> LlamaRuntime:
        if self._runtime is None:
            async with self._runtime_lock:
                if self._runtime is None:
                    self._runtime = await asyncio.to_thread(self._build_runtime)
        return self._runtime

    def _build_runtime(self) -> LlamaRuntime:
        llama_class = _load_llama_class()
        model_path = _resolve_gguf_path(self._config)
        try:
            model = llama_class(
                model_path=str(model_path),
                n_ctx=resolved_llama_context_window(self._config),
                n_batch=DEFAULT_LLAMA_BATCH_SIZE,
                n_threads=recommended_llama_threads(),
                n_gpu_layers=0,
                verbose=False,
            )
        except Exception as error:
            raise BackendUnavailableError(
                f"Could not load llama.cpp model from {model_path}: {error}"
            ) from error
        return LlamaRuntime(model=model, model_path=model_path)

    def _generate_text(self, runtime: LlamaRuntime, request: ModelCompressionInput) -> str:
        first_raw_text, first_output = self._run_generation(
            runtime,
            request,
            self._build_messages(request),
        )
        first_pass = self._recover_candidate_before_validation(request, first_output)
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

        repair_raw_text, repair_output = self._run_generation(
            runtime,
            request,
            self._build_repair_messages(request, first_pass),
        )
        repaired_output = self._recover_candidate_before_validation(request, repair_output)
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
                self._profile.family_name,
                first_validation,
                first_pass,
                repair_validation,
                repaired_output,
            )
        )

    def _run_generation(
        self,
        runtime: LlamaRuntime,
        request: ModelCompressionInput,
        messages: list[dict[str, str]],
    ) -> tuple[str, str]:
        chat_output = _try_chat_completion(
            runtime.model,
            messages=messages,
            max_output_tokens=request.max_output_tokens,
        )
        if chat_output is None:
            prompt_text = _fallback_prompt(messages)
            chat_output = _run_text_completion(
                runtime.model,
                prompt=prompt_text,
                max_output_tokens=request.max_output_tokens,
            )
        raw_text = chat_output.strip()
        normalized = self._normalize_output(request, raw_text)
        if not normalized:
            raise BackendUnavailableError("llama.cpp backend returned empty output.")
        return raw_text, normalized

    def _recover_candidate_before_validation(
        self,
        request: ModelCompressionInput,
        text: str,
    ) -> str:
        return recover_scaffold_prefixed_output(
            request,
            text,
            normalize_output=self._normalize_output,
        )

    def _build_messages(self, request: ModelCompressionInput) -> list[dict[str, str]]:
        if self._uses_fallback_profile():
            messages = self._profile.build_text_messages(request)
        else:
            messages = build_cpu_protection_messages(request)
        return self._prepare_messages(request, messages)

    def _build_repair_messages(
        self,
        request: ModelCompressionInput,
        invalid_output: str,
    ) -> list[dict[str, str]]:
        if self._uses_fallback_profile():
            messages = build_repair_messages(request, invalid_output)
        else:
            messages = build_cpu_protection_repair_messages(request, invalid_output)
        return self._prepare_messages(request, messages)

    def _normalize_output(self, request: ModelCompressionInput, text: str) -> str:
        if self._uses_fallback_profile():
            return self._profile.normalize_output(request, text)
        return normalize_cpu_protection_output(request, text)

    def _uses_fallback_profile(self) -> bool:
        return self._profile.family_name == "fallback"

    def _prepare_messages(
        self,
        request: ModelCompressionInput,
        messages: list[dict[str, str]],
    ) -> list[dict[str, str]]:
        if not self._use_soft_length_hint:
            return messages
        return apply_soft_length_hint(messages, request)


def _selected_index_output(candidates: list[str], selected_index: int | None) -> str:
    if selected_index is None:
        return ""
    if not 0 <= selected_index < len(candidates):
        return ""
    return candidates[selected_index]


def preload_gguf_artifact(config: LocalModelConfig) -> Path:
    """Download the configured GGUF artifact without loading the model into memory."""
    return _resolve_gguf_path(config)


def _resolve_gguf_path(config: LocalModelConfig) -> Path:
    filename = required_gguf_filename(config)
    try:
        downloaded_path = resolve_or_download_hf_file(
            repo_id=config.model,
            filename=filename,
            cache_dir=config.model_cache_path,
        )
    except RuntimeError as error:  # pragma: no cover - dependency comes from transformers
        raise BackendUnavailableError(str(error)) from error
    except Exception as error:
        raise BackendUnavailableError(
            f"Could not resolve GGUF artifact {config.model}/{filename}: {error}"
        ) from error
    return downloaded_path


def _load_llama_class() -> Any:
    try:
        from llama_cpp import Llama
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("llama-cpp-python is not installed.") from error
    return Llama


def _run_text_completion(model: Any, *, prompt: str, max_output_tokens: int) -> str:
    try:
        response = model.create_completion(
            prompt=prompt,
            max_tokens=max_output_tokens,
            temperature=DEFAULT_LLAMA_TEMPERATURE,
            echo=False,
            stop=list(DEFAULT_LLAMA_STOP_SEQUENCES),
        )
    except Exception as error:
        raise BackendUnavailableError(f"llama.cpp text completion failed: {error}") from error
    text = _extract_completion_text(response)
    if text is None:
        raise BackendUnavailableError("llama.cpp text completion returned no text.")
    return text


def _try_chat_completion(
    model: Any,
    *,
    messages: list[dict[str, str]],
    max_output_tokens: int,
) -> str | None:
    try:
        response = model.create_chat_completion(
            messages=messages,
            max_tokens=max_output_tokens,
            temperature=DEFAULT_LLAMA_TEMPERATURE,
            stream=False,
            stop=list(DEFAULT_LLAMA_STOP_SEQUENCES),
        )
    except Exception:
        return None
    return _extract_chat_text(response)


def _extract_chat_text(response: Any) -> str | None:
    if not isinstance(response, dict):
        return None
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        return None
    first_choice = choices[0]
    if not isinstance(first_choice, dict):
        return None
    message = first_choice.get("message")
    if isinstance(message, dict):
        content = message.get("content")
        if isinstance(content, str):
            return content
    text = first_choice.get("text")
    if isinstance(text, str):
        return text
    return None


def _extract_completion_text(response: Any) -> str | None:
    if not isinstance(response, dict):
        return None
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        return None
    first_choice = choices[0]
    if not isinstance(first_choice, dict):
        return None
    text = first_choice.get("text")
    if isinstance(text, str):
        return text
    return None


def _fallback_prompt(messages: list[dict[str, str]]) -> str:
    lines: list[str] = []
    for message in messages:
        role = message.get("role", "user").strip().casefold()
        content = message.get("content", "").strip()
        if not content:
            continue
        lines.append(f"<|{role}|>\n{content}")
    lines.append("<|assistant|>")
    return "\n\n".join(lines)
