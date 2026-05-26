"""Local CPU compression backend built on embedded llama.cpp."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from ctxsift.models.base import (
    BackendUnavailableError,
    ModelBackend,
    ModelCompressionInput,
    ModelOutputRejectedError,
)
from ctxsift.models.hf_hub_cache import resolve_or_download_hf_file
from ctxsift.models.local_model_strategy import (
    LocalModelStrategy,
    PromptRenderMode,
    StrategySource,
    llama_completion_options,
    persist_runtime_strategy,
    probe_candidate_strategies,
    render_nonchat_prompt_with_strategy,
    render_prompt_with_strategy,
    resolve_local_model_strategy,
)
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
    tokenizer: Any | None
    strategy: LocalModelStrategy


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
        strategy = resolve_local_model_strategy(
            self._config,
            backend=self.provider_name,
        )
        tokenizer = _load_optional_tokenizer(self._config, self._profile, strategy=strategy)
        if tokenizer is not None:
            strategy = resolve_local_model_strategy(
                self._config,
                backend=self.provider_name,
                tokenizer=tokenizer,
            )
        return LlamaRuntime(
            model=model,
            model_path=model_path,
            tokenizer=tokenizer,
            strategy=strategy,
        )

    def _generate_text(self, runtime: LlamaRuntime, request: ModelCompressionInput) -> str:
        primary_error: Exception | None = None
        for strategy in self._candidate_strategies(runtime):
            runtime_for_strategy = replace(runtime, strategy=strategy)
            try:
                output, effective_strategy = self._generate_text_once(runtime_for_strategy, request)
            except (BackendUnavailableError, ModelOutputRejectedError) as error:
                if primary_error is None:
                    primary_error = error
                continue
            self._persist_successful_strategy(runtime, effective_strategy)
            return output
        if primary_error is not None:
            raise primary_error
        raise BackendUnavailableError("llama.cpp backend returned no viable strategy.")

    def _generate_text_once(
        self,
        runtime: LlamaRuntime,
        request: ModelCompressionInput,
    ) -> tuple[str, LocalModelStrategy]:
        first_raw_text, first_output, effective_strategy = self._run_generation(
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
            return first_pass, effective_strategy

        repair_raw_text, repair_output, _ = self._run_generation(
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
            return preferred_candidate.output, effective_strategy

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

    def _candidate_strategies(self, runtime: LlamaRuntime) -> list[LocalModelStrategy]:
        if runtime.strategy.source is not StrategySource.DEFAULT:
            return [runtime.strategy]
        return probe_candidate_strategies(runtime.tokenizer, runtime.strategy)

    def _persist_successful_strategy(
        self,
        runtime: LlamaRuntime,
        strategy: LocalModelStrategy,
    ) -> None:
        persisted = persist_runtime_strategy(
            self._config,
            backend=self.provider_name,
            strategy=strategy,
        )
        if self._runtime is runtime:
            self._runtime = replace(runtime, strategy=persisted)

    def _run_generation(
        self,
        runtime: LlamaRuntime,
        request: ModelCompressionInput,
        messages: list[dict[str, str]],
    ) -> tuple[str, str, LocalModelStrategy]:
        chat_output, effective_strategy = _generate_with_runtime_strategy(
            runtime=runtime,
            messages=messages,
            max_output_tokens=request.max_output_tokens,
        )
        raw_text = chat_output.strip()
        normalized = self._normalize_output(request, raw_text)
        if not normalized:
            raise BackendUnavailableError("llama.cpp backend returned empty output.")
        return raw_text, normalized, effective_strategy

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


def _run_text_completion(
    model: Any,
    *,
    prompt: str,
    max_output_tokens: int,
    strategy: LocalModelStrategy,
) -> str:
    try:
        response = model.create_completion(
            prompt=prompt,
            **llama_completion_options(
                max_output_tokens=max_output_tokens,
                strategy=strategy,
            ),
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


def _generate_with_runtime_strategy(
    *,
    runtime: LlamaRuntime,
    messages: list[dict[str, str]],
    max_output_tokens: int,
) -> tuple[str, LocalModelStrategy]:
    if runtime.strategy.prompt_renderer is PromptRenderMode.CHAT_TEMPLATE_TEXT:
        prompt_text, effective_strategy = _strategy_prompt_text(runtime, messages)
        return (
            _run_text_completion(
                runtime.model,
                prompt=prompt_text,
                max_output_tokens=max_output_tokens,
                strategy=runtime.strategy,
            ),
            effective_strategy,
        )
    if runtime.strategy.prompt_renderer is PromptRenderMode.ALPACA_INSTRUCTION:
        return (
            _run_text_completion(
                runtime.model,
                prompt=render_nonchat_prompt_with_strategy(messages, runtime.strategy),
                max_output_tokens=max_output_tokens,
                strategy=runtime.strategy,
            ),
            runtime.strategy,
        )
    chat_output = _try_chat_completion(
        runtime.model,
        messages=messages,
        max_output_tokens=max_output_tokens,
    )
    if chat_output is not None:
        return chat_output, runtime.strategy
    return (
        _run_text_completion(
            runtime.model,
            prompt=_fallback_prompt(messages),
            max_output_tokens=max_output_tokens,
            strategy=runtime.strategy,
        ),
        runtime.strategy,
    )


def _strategy_prompt_text(
    runtime: LlamaRuntime,
    messages: list[dict[str, str]],
) -> tuple[str, LocalModelStrategy]:
    if runtime.tokenizer is None:
        return _fallback_prompt(messages), _fallback_prompt_strategy(runtime.strategy)
    try:
        return (
            render_prompt_with_strategy(
                runtime.tokenizer,
                messages,
                runtime.strategy,
            ),
            runtime.strategy,
        )
    except ValueError as error:
        if _is_missing_chat_template_error(error):
            return _fallback_prompt(messages), _fallback_prompt_strategy(runtime.strategy)
        raise


def _load_optional_tokenizer(
    config: LocalModelConfig,
    profile: Any,
    *,
    strategy: LocalModelStrategy,
) -> Any | None:
    if (
        strategy.prompt_renderer is not PromptRenderMode.CHAT_TEMPLATE_TEXT
        and strategy.source is not StrategySource.DEFAULT
    ):
        return None
    try:
        from transformers import AutoTokenizer
    except ImportError:
        return None
    tokenizer_kwargs: dict[str, Any] = {"padding_side": "left"}
    if getattr(profile, "trust_remote_code", False):
        tokenizer_kwargs["trust_remote_code"] = True
    try:
        return AutoTokenizer.from_pretrained(config.model, **tokenizer_kwargs)
    except Exception:
        return None


def _is_missing_chat_template_error(error: ValueError) -> bool:
    message = str(error)
    return "chat_template" in message and "not set" in message


def _fallback_prompt_strategy(strategy: LocalModelStrategy) -> LocalModelStrategy:
    updated_source = (
        StrategySource.USER_OVERRIDE
        if strategy.source is StrategySource.USER_OVERRIDE
        else StrategySource.DISCOVERED
    )
    return strategy.model_copy(
        update={
            "prompt_renderer": PromptRenderMode.BACKEND_DEFAULT,
            "source": updated_source,
        }
    )
