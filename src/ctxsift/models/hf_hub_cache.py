"""Helpers for cache-first Hugging Face Hub artifact resolution."""

from __future__ import annotations

from os import PathLike
from pathlib import Path


def default_hf_cache_dir() -> Path:
    """Return the effective default Hugging Face cache root for artifact downloads."""
    try:
        from huggingface_hub import constants as hub_constants
    except ImportError:
        return Path.home() / ".cache" / "huggingface" / "hub"
    return Path(hub_constants.HF_HUB_CACHE).expanduser()


def resolve_cached_hf_file(
    *,
    repo_id: str,
    filename: str,
    cache_dir: str | None,
) -> Path | None:
    """Return a cached Hub file path when it already exists locally."""
    try:
        from huggingface_hub import try_to_load_from_cache
    except ImportError:
        return None
    cached_path = try_to_load_from_cache(
        repo_id=repo_id,
        filename=filename,
        cache_dir=cache_dir,
    )
    if cached_path is None or not isinstance(cached_path, (str, PathLike)):
        return None
    path = Path(cached_path)
    if not path.exists():
        return None
    return path


def resolve_or_download_hf_file(
    *,
    repo_id: str,
    filename: str,
    cache_dir: str | None,
) -> Path:
    """Use an already cached Hub artifact when present, else download it."""
    cached_path = resolve_cached_hf_file(
        repo_id=repo_id,
        filename=filename,
        cache_dir=cache_dir,
    )
    if cached_path is not None:
        return cached_path
    try:
        from huggingface_hub import hf_hub_download
    except ImportError as error:
        raise RuntimeError("huggingface_hub is not installed.") from error
    downloaded_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        cache_dir=cache_dir,
    )
    return Path(downloaded_path)
