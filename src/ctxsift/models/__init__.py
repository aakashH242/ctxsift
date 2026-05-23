"""Model backend package."""

from __future__ import annotations

from importlib import import_module
from types import ModuleType
from typing import Any

_MODULE_EXPORTS = {
    "hf_hub_cache": "ctxsift.models.hf_hub_cache",
    "litellm_remote": "ctxsift.models.litellm_remote",
    "quantized_model_cache": "ctxsift.models.quantized_model_cache",
    "transformers_backend": "ctxsift.models.transformers_backend",
    "transformers_quantization": "ctxsift.models.transformers_quantization",
}

__all__ = [
    "create_compression_backend",
    "create_local_backend",
    *sorted(_MODULE_EXPORTS),
]


def create_compression_backend(*args: Any, **kwargs: Any):
    """Lazily import the compression backend factory."""
    from ctxsift.models.factory import create_compression_backend as _create_compression_backend

    return _create_compression_backend(*args, **kwargs)


def create_local_backend(*args: Any, **kwargs: Any):
    """Lazily import the local backend factory."""
    from ctxsift.models.factory import create_local_backend as _create_local_backend

    return _create_local_backend(*args, **kwargs)


def __getattr__(name: str) -> ModuleType:
    """Lazily expose selected model submodules."""
    module_path = _MODULE_EXPORTS.get(name)
    if module_path is None:
        raise AttributeError(f"module 'ctxsift.models' has no attribute {name!r}")
    module = import_module(module_path)
    globals()[name] = module
    return module
