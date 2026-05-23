"""Quantized load helpers for the local Transformers backend."""

from __future__ import annotations

from dataclasses import dataclass
import importlib
from typing import Any

from ctxsift.models.base import BackendUnavailableError
from ctxsift.types import LocalModelConfig, LocalQuantizationMode

_BITSANDBYTES_MODES = {
    LocalQuantizationMode.BNB_8BIT,
    LocalQuantizationMode.BNB_4BIT_FP4,
    LocalQuantizationMode.BNB_4BIT_NF4,
}


@dataclass(frozen=True)
class TransformersLoadOptions:
    """Resolved load options for one Transformers model load."""

    model_kwargs: dict[str, Any]
    move_to_device: bool


def build_transformers_load_options(
    config: LocalModelConfig,
    resolved_torch_device: str,
    torch_dtype: Any,
    attention_backend: str | None,
) -> TransformersLoadOptions:
    """Build the `from_pretrained` kwargs for the configured local model."""
    model_kwargs: dict[str, Any] = {"dtype": torch_dtype}
    if attention_backend:
        model_kwargs["attn_implementation"] = attention_backend
    if config.quantization is LocalQuantizationMode.NONE:
        return TransformersLoadOptions(model_kwargs=model_kwargs, move_to_device=True)
    model_kwargs["quantization_config"] = _build_quantization_config(
        config.quantization,
        torch_dtype,
    )
    model_kwargs["device_map"] = _device_map_for_quantized_load(
        configured_device=config.device,
        resolved_torch_device=resolved_torch_device,
    )
    # Quantized backends expect device placement to be decided during
    # `from_pretrained(...)`, so we skip the generic post-load `.to(...)` step.
    return TransformersLoadOptions(model_kwargs=model_kwargs, move_to_device=False)


def _build_quantization_config(
    quantization: LocalQuantizationMode,
    torch_dtype: Any,
) -> Any:
    if quantization in _BITSANDBYTES_MODES:
        config_class = _load_bitsandbytes_config_class()
        return config_class(**_bitsandbytes_kwargs(quantization, torch_dtype))
    raise BackendUnavailableError(f"Unsupported quantization mode '{quantization.value}'.")


def _bitsandbytes_kwargs(
    quantization: LocalQuantizationMode,
    torch_dtype: Any,
) -> dict[str, Any]:
    if quantization is LocalQuantizationMode.BNB_8BIT:
        return {"load_in_8bit": True}
    quant_type = "nf4"
    if quantization is LocalQuantizationMode.BNB_4BIT_FP4:
        quant_type = "fp4"
    kwargs: dict[str, Any] = {
        "load_in_4bit": True,
        "bnb_4bit_quant_type": quant_type,
    }
    if torch_dtype != "auto":
        kwargs["bnb_4bit_compute_dtype"] = torch_dtype
    return kwargs


def _device_map_for_quantized_load(
    configured_device: str,
    resolved_torch_device: str,
) -> str:
    normalized = configured_device.strip().casefold()
    if normalized == "auto" and resolved_torch_device.startswith("cuda:"):
        return "auto"
    return resolved_torch_device


def _load_bitsandbytes_config_class() -> Any:
    _require_module(
        "bitsandbytes",
        "Bitsandbytes quantization requires the optional `bitsandbytes` package.",
    )
    _require_module(
        "accelerate",
        "Bitsandbytes quantization requires the optional `accelerate` package.",
    )
    try:
        from transformers import BitsAndBytesConfig
    except ImportError as error:
        raise BackendUnavailableError(
            "Transformers BitsAndBytesConfig support is unavailable."
        ) from error
    return BitsAndBytesConfig


def _require_module(module_name: str, message: str) -> None:
    if not _module_available(module_name):
        raise BackendUnavailableError(message)


def _module_available(module_name: str) -> bool:
    try:
        importlib.import_module(module_name)
    except ImportError:
        return False
    return True
