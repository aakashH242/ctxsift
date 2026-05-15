"""Local Gemma compression backend built on Transformers."""

from __future__ import annotations

import asyncio
import inspect
import logging
import os
import re
from dataclasses import dataclass
from typing import Any

from ctxsift.acceleration import gemma_attention_choice
from ctxsift.compression_prompt import build_text_messages
from ctxsift.models.base import BackendUnavailableError, ModelBackend, ModelCompressionInput
from ctxsift.models.transformers_quantization import build_transformers_load_options
from ctxsift.types import LocalModelConfig


@dataclass(frozen=True)
class ResolvedDevice:
    """Resolved model device settings."""

    torch_device: str
    label: str


@dataclass(frozen=True)
class GemmaTextRuntime:
    """Loaded text-only Gemma runtime."""

    model: Any
    tokenizer: Any
    input_device: str


class TransformersGemmaBackend(ModelBackend):
    """Async local compression backend for Gemma via Transformers."""

    provider_name = "transformers"

    def __init__(self, config: LocalModelConfig) -> None:
        self._config = config
        self.model_name = config.model
        self._runtime: GemmaTextRuntime | None = None

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

    async def _get_runtime(self) -> GemmaTextRuntime:
        if self._runtime is None:
            self._runtime = await asyncio.to_thread(self._build_runtime)
        return self._runtime

    def _build_runtime(self) -> GemmaTextRuntime:
        auto_model, auto_tokenizer = _load_transformers_components()
        torch_module = _load_torch_module()
        resolved_device = _resolve_device(self._config.device, torch_module)
        torch_dtype = _resolve_torch_dtype(self._config.dtype, torch_module)
        attention_backend = gemma_attention_choice(
            resolved_device.label,
            self._config.attn_implementation,
        )
        try:
            return _create_text_runtime(
                auto_model=auto_model,
                auto_tokenizer=auto_tokenizer,
                config=self._config,
                model_name=self.model_name,
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
                    resolved_device=resolved_device,
                    torch_dtype=torch_dtype,
                    attention_backend=None,
                )
            except Exception as fallback_error:  # pragma: no cover - exercised through fallback behavior
                raise BackendUnavailableError(str(fallback_error)) from fallback_error

    def _generate_text(self, runtime: GemmaTextRuntime, request: ModelCompressionInput) -> str:
        messages = build_text_messages(request)
        prompt_text = _apply_text_chat_template(runtime.tokenizer, messages)
        inputs = runtime.tokenizer(prompt_text, return_tensors="pt").to(runtime.input_device)
        input_len = _input_length(inputs["input_ids"])
        outputs = runtime.model.generate(**inputs, max_new_tokens=request.max_output_tokens)
        decoded = runtime.tokenizer.decode(outputs[0][input_len:], skip_special_tokens=False)
        return _normalize_generated_text(decoded)


def _resolve_device(device_name: str, torch_module: Any) -> ResolvedDevice:
    normalized = device_name.strip().casefold()
    cuda_available = bool(torch_module.cuda.is_available())
    if normalized == "cpu":
        return ResolvedDevice(torch_device="cpu", label="cpu")
    if normalized in {"auto", "cuda"}:
        if cuda_available:
            return ResolvedDevice(torch_device="cuda:0", label="cuda:0")
        return ResolvedDevice(torch_device="cpu", label="cpu")
    if normalized.startswith("cuda:"):
        if cuda_available:
            suffix = normalized.split(":", 1)[1]
            if suffix.isdigit():
                return ResolvedDevice(torch_device=f"cuda:{suffix}", label=f"cuda:{suffix}")
            return ResolvedDevice(torch_device=device_name, label=device_name)
        return ResolvedDevice(torch_device="cpu", label="cpu")
    return ResolvedDevice(torch_device="cpu", label="cpu")


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
        from huggingface_hub.utils import disable_progress_bars
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from transformers.utils import logging as transformers_logging
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("Transformers is not installed.") from error
    os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
    os.environ.setdefault("TRANSFORMERS_NO_ADVISORY_WARNINGS", "1")
    disable_progress_bars()
    transformers_logging.set_verbosity_error()
    transformers_logging.disable_progress_bar()
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
    resolved_device: ResolvedDevice,
    torch_dtype: Any,
    attention_backend: str | None,
) -> GemmaTextRuntime:
    load_options = build_transformers_load_options(
        config=config,
        resolved_torch_device=resolved_device.torch_device,
        torch_dtype=torch_dtype,
        attention_backend=attention_backend,
    )
    model = auto_model.from_pretrained(model_name, **load_options.model_kwargs)
    if load_options.move_to_device:
        model.to(resolved_device.torch_device)
    model.eval()
    tokenizer = auto_tokenizer.from_pretrained(model_name, padding_side="left")
    input_device = _runtime_input_device(model, resolved_device.torch_device)
    return GemmaTextRuntime(model=model, tokenizer=tokenizer, input_device=input_device)


def _runtime_input_device(model: Any, fallback_device: str) -> str:
    embedding_device = _input_embedding_device(model)
    if embedding_device not in {None, "meta"}:
        return embedding_device
    hf_device_map = getattr(model, "hf_device_map", None)
    if isinstance(hf_device_map, dict):
        for device in hf_device_map.values():
            normalized_device = _normalize_runtime_device(device)
            if normalized_device not in {None, "disk", "meta"}:
                return normalized_device
    model_device = _normalize_runtime_device(getattr(model, "device", None))
    if model_device not in {None, "meta"}:
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
    signature = inspect.signature(tokenizer.apply_chat_template)
    if "enable_thinking" in signature.parameters:
        kwargs["enable_thinking"] = False
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


def _normalize_generated_text(text: str) -> str:
    cleaned = text.strip()
    while True:
        updated = _strip_edge_tag(cleaned)
        if updated == cleaned:
            return cleaned
        cleaned = updated


def _strip_edge_tag(text: str) -> str:
    leading = re.sub(r"^\s*<[^>\n]{1,16}>\s*", "", text, count=1)
    trailing = re.sub(r"\s*<[^>\n]{1,16}>\s*$", "", leading, count=1)
    return trailing.strip()
