"""Local text-model compression backend built on Transformers."""

from __future__ import annotations

import asyncio
import inspect
import logging
import os
from dataclasses import dataclass
from typing import Any

from ctxsift.acceleration import text_attention_choice
from ctxsift.models.base import (
    BackendUnavailableError,
    ModelBackend,
    ModelCompressionInput,
    ModelOutputRejectedError,
)
from ctxsift.models.local_runtime import ResolvedLocalDevice, resolve_local_device
from ctxsift.models.local_runtime import should_apply_soft_length_hint
from ctxsift.models.text_model_profiles import resolve_text_model_profile
from ctxsift.models.text_profile_common import (
    apply_soft_length_hint,
    build_validation_failure_message,
    build_repair_messages,
    choose_preferred_candidate,
    recover_scaffold_prefixed_output,
    selected_candidate_index,
    should_attempt_repair,
    validate_instruction_aware_output,
)
from ctxsift.models.text_profile_types import TextModelProfile
from ctxsift.models.quantized_model_cache import (
    cached_model_source,
    has_persisted_quantized_model,
    persist_quantized_model_cache,
    resolve_quantized_model_cache,
)
from ctxsift.models.transformers_quantization import build_transformers_load_options
from ctxsift.types import LocalModelConfig


@dataclass(frozen=True)
class TextRuntime:
    """Loaded text-only Transformers runtime."""

    model: Any
    tokenizer: Any
    input_device: str


@dataclass(frozen=True)
class LoadedModelArtifacts:
    """Loaded model plus the tokenizer source that matches it."""

    model: Any
    tokenizer_source: str
    loaded_from_cache: bool


class TransformersTextBackend(ModelBackend):
    """Async local compression backend for supported text models via Transformers."""

    provider_name = "transformers"

    def __init__(self, config: LocalModelConfig) -> None:
        self._config = config
        self.model_name = config.model
        self._runtime: TextRuntime | None = None
        self._profile = resolve_text_model_profile(config.model)
        self._use_soft_length_hint = should_apply_soft_length_hint(
            config,
            provider_name=self.provider_name,
        )

    @property
    def cache_model_id(self) -> str:
        if self._config.quantization.value == "none":
            return self.model_name
        return f"{self.model_name}[{self._config.quantization.value}]"

    async def compress(self, request: ModelCompressionInput) -> str:
        runtime = await self._get_runtime()
        text = await asyncio.to_thread(self._generate_text, runtime, request)
        if not text:
            raise BackendUnavailableError("Transformers backend returned empty output.")
        return text

    async def preload(self) -> None:
        await self._get_runtime()

    async def shutdown(self) -> None:
        self._runtime = None

    async def _get_runtime(self) -> TextRuntime:
        if self._runtime is None:
            self._runtime = await asyncio.to_thread(self._build_runtime)
        return self._runtime

    def _build_runtime(self) -> TextRuntime:
        auto_model, auto_tokenizer = _load_transformers_components()
        torch_module = _load_torch_module()
        resolved_device = resolve_local_device(self._config.device, torch_module=torch_module)
        torch_dtype = _resolve_torch_dtype(self._config.dtype, torch_module)
        attention_backend = text_attention_choice(
            resolved_device.label,
            self._config.attn_implementation,
        )
        try:
            return _create_text_runtime(
                auto_model=auto_model,
                auto_tokenizer=auto_tokenizer,
                config=self._config,
                model_name=self.model_name,
                profile=self._profile,
                resolved_device=resolved_device,
                torch_dtype=torch_dtype,
                attention_backend=attention_backend,
            )
        except BackendUnavailableError:
            raise
        except Exception as error:
            if not attention_backend:
                raise BackendUnavailableError(str(error)) from error
            try:
                return _create_text_runtime(
                    auto_model=auto_model,
                    auto_tokenizer=auto_tokenizer,
                    config=self._config,
                    model_name=self.model_name,
                    profile=self._profile,
                    resolved_device=resolved_device,
                    torch_dtype=torch_dtype,
                    attention_backend=None,
                )
            except (
                Exception
            ) as fallback_error:  # pragma: no cover - exercised through fallback behavior
                raise BackendUnavailableError(str(fallback_error)) from fallback_error

    def _generate_text(self, runtime: TextRuntime, request: ModelCompressionInput) -> str:
        first_raw_text, first_output = self._run_generation(
            runtime,
            request,
            self._prepare_messages(request, self._profile.build_text_messages(request)),
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
            self._prepare_messages(request, build_repair_messages(request, first_pass)),
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

    def _recover_candidate_before_validation(
        self,
        request: ModelCompressionInput,
        text: str,
    ) -> str:
        return recover_scaffold_prefixed_output(
            request,
            text,
            normalize_output=self._profile.normalize_output,
        )

    def _run_generation(
        self,
        runtime: TextRuntime,
        request: ModelCompressionInput,
        messages: list[dict[str, str]],
    ) -> tuple[str, str]:
        prompt_text = _apply_text_chat_template(runtime.tokenizer, messages)
        inputs = runtime.tokenizer(prompt_text, return_tensors="pt").to(runtime.input_device)
        input_len = _input_length(inputs["input_ids"])
        outputs = runtime.model.generate(
            **inputs,
            **self._profile.generation_kwargs(runtime.tokenizer, request.max_output_tokens),
        )
        raw_text = runtime.tokenizer.decode(
            outputs[0][input_len:], skip_special_tokens=False
        ).strip()
        normalized = self._profile.normalize_output(request, raw_text)
        return raw_text, normalized

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


TransformersGemmaBackend = TransformersTextBackend


def _resolve_device(device_name: str, torch_module: Any) -> ResolvedLocalDevice:
    """Backward-compatible wrapper around the shared local-device resolver."""
    return resolve_local_device(device_name, torch_module=torch_module)


def _resolve_torch_dtype(dtype_name: str, torch_module: Any) -> Any:
    normalized = dtype_name.strip().casefold()
    if normalized == "auto":
        return "auto"
    attribute_name = normalized.replace(".", "")
    torch_dtype = getattr(torch_module, attribute_name, None)
    if torch_dtype is None:
        raise BackendUnavailableError(f"Unsupported torch dtype '{dtype_name}'.")
    return torch_dtype


def _load_transformers_components() -> tuple[Any, Any]:
    try:
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from transformers.utils import logging as transformers_logging
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("Transformers is not installed.") from error
    os.environ.setdefault("TRANSFORMERS_NO_ADVISORY_WARNINGS", "1")
    transformers_logging.set_verbosity_error()
    logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
    logging.getLogger("transformers").setLevel(logging.ERROR)
    return AutoModelForCausalLM, AutoTokenizer


def _load_torch_module() -> Any:
    try:
        import torch
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("PyTorch is not installed.") from error
    return torch


def _create_text_runtime(
    auto_model: Any,
    auto_tokenizer: Any,
    config: LocalModelConfig,
    model_name: str,
    profile: TextModelProfile,
    resolved_device: ResolvedLocalDevice,
    torch_dtype: Any,
    attention_backend: str | None,
) -> TextRuntime:
    load_options = build_transformers_load_options(
        config=config,
        resolved_torch_device=resolved_device.torch_device,
        torch_dtype=torch_dtype,
        attention_backend=attention_backend,
    )
    cache = resolve_quantized_model_cache(config, model_name)
    artifacts = _load_model(
        auto_model=auto_model,
        model_name=model_name,
        load_options=load_options,
        cache=cache,
        trust_remote_code=profile.trust_remote_code,
    )
    model = artifacts.model
    if load_options.move_to_device:
        model.to(resolved_device.torch_device)
    model.eval()
    tokenizer_kwargs: dict[str, Any] = {"padding_side": "left"}
    if profile.trust_remote_code:
        tokenizer_kwargs["trust_remote_code"] = True
    tokenizer = auto_tokenizer.from_pretrained(artifacts.tokenizer_source, **tokenizer_kwargs)
    if cache is not None and not artifacts.loaded_from_cache:
        try:
            persist_quantized_model_cache(
                cache,
                model=model,
                tokenizer=tokenizer,
                model_name=model_name,
                config=config,
            )
        except Exception as error:
            logging.getLogger(__name__).warning(
                "Failed to persist quantized checkpoint to %s: %s",
                cache.model_dir,
                error,
            )
    input_device = _runtime_input_device(model, resolved_device.torch_device)
    return TextRuntime(model=model, tokenizer=tokenizer, input_device=input_device)


def _load_model(
    auto_model: Any,
    model_name: str,
    load_options: Any,
    cache: Any,
    trust_remote_code: bool = False,
) -> LoadedModelArtifacts:
    if cache is not None and has_persisted_quantized_model(cache):
        cache_source = cached_model_source(cache)
        try:
            model = auto_model.from_pretrained(
                cache_source,
                **_cached_model_kwargs(load_options.model_kwargs, trust_remote_code),
            )
            return LoadedModelArtifacts(
                model=model,
                tokenizer_source=cache_source,
                loaded_from_cache=True,
            )
        except Exception as error:
            logging.getLogger(__name__).warning(
                "Failed to load persisted quantized checkpoint from %s: %s",
                cache.model_dir,
                error,
            )
    model_kwargs = dict(load_options.model_kwargs)
    if trust_remote_code:
        model_kwargs["trust_remote_code"] = True
    model = auto_model.from_pretrained(model_name, **model_kwargs)
    return LoadedModelArtifacts(
        model=model,
        tokenizer_source=model_name,
        loaded_from_cache=False,
    )


def _cached_model_kwargs(model_kwargs: dict[str, Any], trust_remote_code: bool) -> dict[str, Any]:
    cached_kwargs = dict(model_kwargs)
    cached_kwargs.pop("quantization_config", None)
    if trust_remote_code:
        cached_kwargs["trust_remote_code"] = True
    return cached_kwargs


def _runtime_input_device(model: Any, fallback_device: str) -> str:
    embedding_device = _input_embedding_device(model)
    if embedding_device is not None and embedding_device != "meta":
        return embedding_device
    hf_device_map = getattr(model, "hf_device_map", None)
    if isinstance(hf_device_map, dict):
        for device in hf_device_map.values():
            normalized_device = _normalize_runtime_device(device)
            if normalized_device is not None and normalized_device not in {"disk", "meta"}:
                return normalized_device
    model_device = _normalize_runtime_device(getattr(model, "device", None))
    if model_device is not None and model_device != "meta":
        return model_device
    return fallback_device


def _input_embedding_device(model: Any) -> str | None:
    get_input_embeddings = getattr(model, "get_input_embeddings", None)
    if not callable(get_input_embeddings):
        return None
    try:
        embeddings = get_input_embeddings()
    except Exception:
        return None
    weight = getattr(embeddings, "weight", None)
    return _normalize_runtime_device(getattr(weight, "device", None))


def _normalize_runtime_device(device: Any) -> str | None:
    if device is None:
        return None
    if isinstance(device, int):
        return f"cuda:{device}"
    if isinstance(device, str):
        return device
    device_type = getattr(device, "type", None)
    if isinstance(device_type, str):
        device_index = getattr(device, "index", None)
        if device_index is None:
            return device_type
        return f"{device_type}:{device_index}"
    return str(device)


def _apply_text_chat_template(tokenizer: Any, messages: list[dict[str, str]]) -> str:
    kwargs = {"tokenize": False, "add_generation_prompt": True}
    try:
        signature = inspect.signature(tokenizer.apply_chat_template)
    except (TypeError, ValueError):
        signature = None
    if signature is not None:
        if "enable_thinking" in signature.parameters:
            kwargs["enable_thinking"] = False
        if "thinking" in signature.parameters:
            kwargs["thinking"] = False
    return tokenizer.apply_chat_template(messages, **kwargs)


def _input_length(input_ids: Any) -> int:
    shape = getattr(input_ids, "shape", None)
    if shape is not None:
        return int(shape[-1])
    if isinstance(input_ids, list) and input_ids:
        first_item = input_ids[0]
        if isinstance(first_item, list):
            return len(first_item)
    return len(input_ids)
