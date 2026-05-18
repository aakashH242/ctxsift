"""Acceleration-policy helpers for optional inference backends."""

from __future__ import annotations

import importlib.util


FLASH_ATTENTION_BACKEND = "flash_attention_2"


def flash_attention_available() -> bool:
    """Return whether a known Flash Attention provider is installed."""
    return _module_available("flash_attn") or _module_available("kernels")


def onnxruntime_available() -> bool:
    """Return whether ONNX Runtime is installed."""
    return _module_available("onnxruntime")


def onnxruntime_gpu_available() -> bool:
    """Return whether ONNX Runtime GPU support is installed."""
    return _module_available("onnxruntime") and _module_available("onnxruntime.capi")


def text_attention_choice(device_label: str, configured_value: str) -> str | None:
    """Resolve the desired text-model attention backend with safe defaults."""
    normalized = configured_value.strip().casefold()
    if normalized in {"", "auto"}:
        if device_label.startswith("cuda") and flash_attention_available():
            return FLASH_ATTENTION_BACKEND
        return None
    if normalized == FLASH_ATTENTION_BACKEND:
        return FLASH_ATTENTION_BACKEND if device_label.startswith("cuda") else None
    if normalized == "sdpa":
        return "sdpa"
    return None


def gemma_attention_choice(device_label: str, configured_value: str) -> str | None:
    """Backward-compatible alias for the text-model attention policy."""
    return text_attention_choice(device_label, configured_value)


def embedding_backend_choice(device_label: str, configured_value: str, model_name: str) -> str:
    """Resolve the preferred embedding backend for the current environment."""
    normalized = configured_value.strip().casefold()
    if normalized in {"", "auto"}:
        if device_label == "cpu" and _is_harrier_model(model_name) and onnxruntime_available():
            return "onnx"
        return "torch"
    if normalized == "onnx":
        return "onnx"
    return "torch"


def embedding_attention_choice(device_label: str, configured_value: str) -> str | None:
    """Resolve the desired embedding attention backend for torch inference."""
    normalized = configured_value.strip().casefold()
    if normalized in {"", "auto"}:
        if device_label.startswith("cuda") and flash_attention_available():
            return FLASH_ATTENTION_BACKEND
        return None
    if normalized == FLASH_ATTENTION_BACKEND:
        return FLASH_ATTENTION_BACKEND if device_label.startswith("cuda") else None
    if normalized == "sdpa":
        return "sdpa"
    return None


def _is_harrier_model(model_name: str) -> bool:
    return model_name.casefold().startswith("microsoft/harrier-oss")


def _module_available(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None
