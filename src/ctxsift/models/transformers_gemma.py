"""Local Gemma compression backend built on Transformers."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any

from ctxsift.compression_prompt import build_messages
from ctxsift.models.base import BackendUnavailableError, ModelBackend, ModelCompressionInput
from ctxsift.types import LocalModelConfig


@dataclass(frozen=True)
class ResolvedDevice:
    """Resolved pipeline device settings."""

    pipeline_device: int | str
    label: str


class TransformersGemmaBackend(ModelBackend):
    """Async local compression backend for Gemma via Transformers."""

    provider_name = "transformers"

    def __init__(self, config: LocalModelConfig) -> None:
        self._config = config
        self.model_name = config.model
        self._pipeline: Any | None = None

    @property
    def cache_model_id(self) -> str:
        return self.model_name

    async def compress(self, request: ModelCompressionInput) -> str:
        pipe = await self._get_pipeline()
        messages = build_messages(request)
        generate_kwargs = {"max_new_tokens": request.max_output_tokens}
        result = await asyncio.to_thread(
            pipe,
            messages,
            return_full_text=False,
            generate_kwargs=generate_kwargs,
        )
        text = _generated_text(result)
        if not text:
            raise BackendUnavailableError("Transformers backend returned empty output.")
        return text

    async def _get_pipeline(self) -> Any:
        if self._pipeline is None:
            self._pipeline = await asyncio.to_thread(self._build_pipeline)
        return self._pipeline

    def _build_pipeline(self) -> Any:
        pipeline = _load_transformers_pipeline()
        torch_module = _load_torch_module()
        resolved_device = _resolve_device(self._config.device, torch_module)
        torch_dtype = _resolve_torch_dtype(self._config.dtype, torch_module)
        try:
            return pipeline(
                task=_pipeline_task(self.model_name),
                model=self.model_name,
                device=resolved_device.pipeline_device,
                torch_dtype=torch_dtype,
            )
        except Exception as error:  # pragma: no cover - exercised through mocks and fallback behavior
            raise BackendUnavailableError(str(error)) from error


def _pipeline_task(model_name: str) -> str:
    if "gemma-4" in model_name.casefold():
        return "any-to-any"
    return "text-generation"


def _resolve_device(device_name: str, torch_module: Any) -> ResolvedDevice:
    normalized = device_name.strip().casefold()
    cuda_available = bool(torch_module.cuda.is_available())
    if normalized == "cpu":
        return ResolvedDevice(pipeline_device=-1, label="cpu")
    if normalized in {"auto", "cuda"}:
        if cuda_available:
            return ResolvedDevice(pipeline_device=0, label="cuda:0")
        return ResolvedDevice(pipeline_device=-1, label="cpu")
    if normalized.startswith("cuda:"):
        if cuda_available:
            suffix = normalized.split(":", 1)[1]
            if suffix.isdigit():
                return ResolvedDevice(pipeline_device=int(suffix), label=f"cuda:{suffix}")
            return ResolvedDevice(pipeline_device=device_name, label=device_name)
        return ResolvedDevice(pipeline_device=-1, label="cpu")
    return ResolvedDevice(pipeline_device=-1, label="cpu")


def _resolve_torch_dtype(dtype_name: str, torch_module: Any) -> Any:
    normalized = dtype_name.strip().casefold()
    if normalized == "auto":
        return "auto"
    attribute_name = normalized.replace(".", "")
    torch_dtype = getattr(torch_module, attribute_name, None)
    if torch_dtype is None:
        raise BackendUnavailableError(f"Unsupported torch dtype '{dtype_name}'.")
    return torch_dtype


def _generated_text(result: Any) -> str:
    if isinstance(result, list) and result:
        first_item = result[0]
        if isinstance(first_item, dict):
            generated_text = first_item.get("generated_text")
            if isinstance(generated_text, str):
                return generated_text.strip()
    if isinstance(result, str):
        return result.strip()
    return ""


def _load_transformers_pipeline() -> Any:
    try:
        from transformers import pipeline
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("Transformers is not installed.") from error
    return pipeline


def _load_torch_module() -> Any:
    try:
        import torch
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("PyTorch is not installed.") from error
    return torch
