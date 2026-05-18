"""Helpers for persisted quantized Transformers checkpoints."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
from typing import Any

from ctxsift.types import LocalModelConfig, LocalQuantizationMode


_CACHE_METADATA_FILE = "ctxsift-quantized-model.json"
_TOKENIZER_FILE_NAMES = (
    "tokenizer.json",
    "tokenizer_config.json",
    "special_tokens_map.json",
)


@dataclass(frozen=True)
class QuantizedModelCache:
    """Resolved cache paths for one quantized model variant."""

    root_dir: Path
    model_dir: Path
    metadata_path: Path


def resolve_quantized_model_cache(
    config: LocalModelConfig,
    model_name: str,
) -> QuantizedModelCache | None:
    """Resolve the persisted cache location for one quantized model variant."""
    if config.quantization is LocalQuantizationMode.NONE:
        return None
    root_dir = _cache_root(config.model_cache_path)
    directory_name = _cache_directory_name(
        model_name=model_name,
        quantization=config.quantization.value,
        dtype=config.dtype,
    )
    model_dir = root_dir / directory_name
    return QuantizedModelCache(
        root_dir=root_dir,
        model_dir=model_dir,
        metadata_path=model_dir / _CACHE_METADATA_FILE,
    )


def has_persisted_quantized_model(cache: QuantizedModelCache) -> bool:
    """Return whether a saved quantized checkpoint is present."""
    return (
        cache.metadata_path.exists()
        and (cache.model_dir / "config.json").exists()
        and any((cache.model_dir / file_name).exists() for file_name in _TOKENIZER_FILE_NAMES)
    )


def persist_quantized_model_cache(
    cache: QuantizedModelCache,
    *,
    model: Any,
    tokenizer: Any,
    model_name: str,
    config: LocalModelConfig,
) -> None:
    """Persist one loaded quantized model and minimal metadata."""
    if not _quantized_model_is_serializable(model):
        return
    cache.model_dir.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(cache.model_dir)
    tokenizer.save_pretrained(cache.model_dir)
    metadata = {
        "source_model": model_name,
        "quantization": config.quantization.value,
        "dtype": config.dtype,
    }
    cache.metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def _quantized_model_is_serializable(model: Any) -> bool:
    hf_quantizer = getattr(model, "hf_quantizer", None)
    is_serializable = getattr(hf_quantizer, "is_serializable", None)
    if not callable(is_serializable):
        return True
    return bool(is_serializable())


def cached_model_source(cache: QuantizedModelCache) -> str:
    """Return the on-disk load source for a persisted checkpoint."""
    return str(cache.model_dir)


def _cache_root(configured_path: str | None) -> Path:
    if configured_path and configured_path.strip():
        return Path(configured_path).expanduser() / "model" / "files"
    return _default_cache_base() / "model_quants" / "model" / "files"


def _default_cache_base() -> Path:
    base = _env_cache_base()
    if base is not None:
        return base
    base = _huggingface_cache_base()
    if base is not None:
        return base
    return _home_cache_base()


def _home_cache_base() -> Path:
    return Path.home() / ".cache"


def _env_cache_base() -> Path | None:
    candidates = (
        ("SENTENCE_TRANSFORMERS_HOME", False),
        ("HF_HOME", False),
        ("HF_HUB_CACHE", True),
        ("TRANSFORMERS_CACHE", True),
    )
    for env_name, use_parent in candidates:
        raw_value = os.environ.get(env_name)
        if not raw_value:
            continue
        path = Path(raw_value).expanduser()
        return path.parent if use_parent else path
    return None


def _huggingface_cache_base() -> Path | None:
    try:
        from huggingface_hub import constants as hub_constants
    except ImportError:
        return None
    cache_path = Path(hub_constants.HF_HUB_CACHE).expanduser()
    return cache_path.parent


def _cache_directory_name(model_name: str, quantization: str, dtype: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", model_name.casefold()).strip("-") or "model"
    slug = slug[:48]
    payload = json.dumps(
        {
            "dtype": dtype,
            "model": model_name,
            "quantization": quantization,
        },
        sort_keys=True,
    )
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
    return f"{slug}-{quantization}-{digest}"
