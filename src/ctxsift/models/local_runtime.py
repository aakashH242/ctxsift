"""Shared runtime-selection helpers for local compression backends."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Any

from ctxsift.models.base import BackendUnavailableError
from ctxsift.types import LocalModelConfig, LocalQuantizationMode

LLAMA_CPP_PROVIDER = "llama_cpp"
TRANSFORMERS_PROVIDER = "transformers"
SMALL_MODEL_MAX_BILLIONS = 2.0
MODEL_SIZE_RE = re.compile(r"(?:^|[-_ /])(\d+(?:\.\d+)?)([bm])(?:[-_ /.]|$)", re.IGNORECASE)


@dataclass(frozen=True)
class ResolvedLocalDevice:
    """Resolved local device label used across local runtime decisions."""

    torch_device: str
    label: str


@dataclass(frozen=True)
class LocalRuntimeSelection:
    """Selected local runtime family for one resolved local config."""

    provider_name: str
    resolved_device: ResolvedLocalDevice

    @property
    def uses_transformers(self) -> bool:
        return self.provider_name == TRANSFORMERS_PROVIDER

    @property
    def uses_llama_cpp(self) -> bool:
        return self.provider_name == LLAMA_CPP_PROVIDER


def resolve_local_runtime(
    config: LocalModelConfig,
    *,
    torch_module: Any | None = None,
) -> LocalRuntimeSelection:
    """Resolve whether the local config should use llama.cpp or Transformers."""
    if _prefers_llama_cpp_auto(config):
        _validate_llama_cpp_config(config)
        return LocalRuntimeSelection(
            provider_name=LLAMA_CPP_PROVIDER,
            resolved_device=ResolvedLocalDevice(torch_device="cpu", label="cpu"),
        )
    resolved_device = resolve_local_device(config.device, torch_module=torch_module)
    if resolved_device.label.startswith("cuda"):
        return LocalRuntimeSelection(
            provider_name=TRANSFORMERS_PROVIDER,
            resolved_device=resolved_device,
        )
    _validate_llama_cpp_config(config)
    return LocalRuntimeSelection(
        provider_name=LLAMA_CPP_PROVIDER,
        resolved_device=ResolvedLocalDevice(torch_device="cpu", label="cpu"),
    )


def resolve_local_device(
    device_name: str,
    *,
    torch_module: Any | None = None,
) -> ResolvedLocalDevice:
    """Resolve one configured local device against CUDA availability."""
    normalized = device_name.strip().casefold()
    if normalized == "cpu":
        return ResolvedLocalDevice(torch_device="cpu", label="cpu")
    if normalized == "auto":
        torch_runtime = _optional_torch_module(torch_module)
        if torch_runtime is None:
            return ResolvedLocalDevice(torch_device="cpu", label="cpu")
        if bool(torch_runtime.cuda.is_available()):
            return ResolvedLocalDevice(torch_device="cuda:0", label="cuda:0")
        return ResolvedLocalDevice(torch_device="cpu", label="cpu")
    if normalized == "cuda":
        torch_runtime = torch_module or _load_torch_module()
        if bool(torch_runtime.cuda.is_available()):
            return ResolvedLocalDevice(torch_device="cuda:0", label="cuda:0")
        raise BackendUnavailableError(
            "local.device is set to cuda but CUDA is not available. "
            "Use local.device=cpu for llama.cpp or install a working CUDA runtime."
        )
    if normalized.startswith("cuda:"):
        torch_runtime = torch_module or _load_torch_module()
        if bool(torch_runtime.cuda.is_available()):
            suffix = normalized.split(":", 1)[1]
            if suffix.isdigit():
                return ResolvedLocalDevice(torch_device=f"cuda:{suffix}", label=f"cuda:{suffix}")
            return ResolvedLocalDevice(torch_device=device_name.strip(), label=device_name.strip())
        raise BackendUnavailableError(
            f"local.device is set to {device_name.strip()} but CUDA is not available. "
            "Use local.device=cpu for llama.cpp or install a working CUDA runtime."
        )
    raise BackendUnavailableError(
        "Unsupported local.device value. Use one of: cpu, auto, cuda, cuda:<index>."
    )


def local_cache_model_id(config: LocalModelConfig) -> str:
    """Return the stable model identifier used for exact-cache keys."""
    runtime = resolve_local_runtime(config)
    if runtime.uses_llama_cpp:
        return f"{config.model.strip()}::{required_gguf_filename(config)}"
    if config.quantization is LocalQuantizationMode.NONE:
        return config.model.strip()
    return f"{config.model.strip()}[{config.quantization.value}]"


def local_provider_name(config: LocalModelConfig) -> str:
    """Return the provider name exposed to compression callers."""
    return resolve_local_runtime(config).provider_name


def required_gguf_filename(config: LocalModelConfig) -> str:
    """Return the configured GGUF filename or raise when it is missing."""
    filename = (config.gguf_filename or "").strip()
    if not filename:
        raise BackendUnavailableError(
            "local.gguf_filename is required when local compression resolves to CPU llama.cpp."
        )
    return filename


def recommended_llama_threads() -> int:
    """Return a pragmatic CPU thread count for llama.cpp loads."""
    psutil_module: Any | None
    try:
        import psutil as _psutil
    except ImportError:
        psutil_module = None
    else:
        psutil_module = _psutil
    if psutil_module is not None:
        count = psutil_module.cpu_count(logical=False)
        if isinstance(count, int) and count > 0:
            return count
    cpu_count = os.cpu_count() or 1
    return max(1, cpu_count)


def estimated_model_size_billions(
    model_name: str, artifact_name: str | None = None
) -> float | None:
    """Estimate parameter count in billions from one repo or artifact name."""
    for candidate in (artifact_name or "", model_name):
        match = MODEL_SIZE_RE.search(candidate)
        if match is None:
            continue
        magnitude = float(match.group(1))
        unit = match.group(2).casefold()
        if unit == "m":
            return magnitude / 1000.0
        return magnitude
    return None


def should_apply_soft_length_hint(
    config: LocalModelConfig,
    *,
    provider_name: str,
) -> bool:
    """Return whether one local runtime should get soft length guidance."""
    if provider_name == LLAMA_CPP_PROVIDER:
        return True
    estimated_size = estimated_model_size_billions(config.model)
    if estimated_size is None:
        return False
    return estimated_size <= SMALL_MODEL_MAX_BILLIONS


def _validate_llama_cpp_config(config: LocalModelConfig) -> None:
    required_gguf_filename(config)
    if config.quantization is not LocalQuantizationMode.NONE:
        raise BackendUnavailableError(
            "local.quantization must be `none` when local compression resolves to CPU llama.cpp."
        )


def _prefers_llama_cpp_auto(config: LocalModelConfig) -> bool:
    normalized_device = config.device.strip().casefold()
    if normalized_device != "auto":
        return False
    model_name = config.model.strip().casefold()
    filename = (config.gguf_filename or "").strip().casefold()
    return model_name.endswith("-gguf") and filename.endswith(".gguf")


def _optional_torch_module(torch_module: Any | None) -> Any | None:
    if torch_module is not None:
        return torch_module
    try:
        import torch
    except ImportError:
        return None
    return torch


def _load_torch_module() -> Any:
    try:
        import torch
    except ImportError as error:  # pragma: no cover - depends on local environment
        raise BackendUnavailableError("PyTorch is not installed.") from error
    return torch
