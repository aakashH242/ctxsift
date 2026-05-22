"""Model preload helpers used during guided configuration."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from dataclasses import dataclass

from ctxsift.embeddings import create_in_process_embedding_backend
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError
from ctxsift.models.hf_hub_cache import resolve_cached_hf_file
from ctxsift.models.llama_cpp_backend import preload_gguf_artifact
from ctxsift.models.local_runtime import resolve_local_runtime
from ctxsift.models.base import BackendUnavailableError
from ctxsift.models.factory import create_local_backend
from ctxsift.models.local_runtime import required_gguf_filename
from ctxsift.types import AppConfig

create_embedding_backend = create_in_process_embedding_backend


@dataclass(frozen=True)
class ModelPreloadResult:
    """One preload outcome for configure."""

    label: str
    ok: bool
    detail: str


async def preload_configured_models(
    config: AppConfig,
    progress: Callable[[str], None] | None = None,
) -> list[ModelPreloadResult]:
    """Download or warm configured local models that ctxsift will need later."""
    results = [await _preload_embedding_model(config, progress)]
    if not config.remote.base_url.strip():
        results.append(await _preload_local_compression_model(config, progress))
    return results


async def _preload_embedding_model(
    config: AppConfig,
    progress: Callable[[str], None] | None = None,
) -> ModelPreloadResult:
    label = f"embedding model {config.embedding.model}"
    _report_progress(
        progress,
        f"Preparing {label}. This may still take time even if artifacts are already cached.",
    )
    try:
        backend = create_embedding_backend(config.embedding)
        await backend.preload()
    except EmbeddingBackendUnavailableError as error:
        return ModelPreloadResult(
            label=label,
            ok=False,
            detail=f"Could not preload {label}: {error}",
        )
    return ModelPreloadResult(
        label=label,
        ok=True,
        detail=f"Preloaded {label}.",
    )


async def _preload_local_compression_model(
    config: AppConfig,
    progress: Callable[[str], None] | None = None,
) -> ModelPreloadResult:
    label = f"local compression model {config.local.model}"
    try:
        runtime = resolve_local_runtime(config.local)
        if runtime.uses_llama_cpp:
            cached_gguf = resolve_cached_hf_file(
                repo_id=config.local.model,
                filename=required_gguf_filename(config.local),
                cache_dir=config.local.model_cache_path,
            )
            if cached_gguf is None:
                _report_progress(
                    progress,
                    f"Preparing {label}. Downloading GGUF artifact because it is not cached yet.",
                )
            else:
                _report_progress(
                    progress,
                    f"Preparing {label}. Using cached GGUF artifact {cached_gguf.name}.",
                )
            gguf_path = await asyncio.to_thread(preload_gguf_artifact, config.local)
            return ModelPreloadResult(
                label=label,
                ok=True,
                detail=f"Preloaded {label} ({gguf_path.name}).",
            )
        _report_progress(
            progress,
            f"Preparing {label}. This may still take time even if artifacts are already cached.",
        )
        backend = create_local_backend(config.local)
        await backend.preload()
    except BackendUnavailableError as error:
        return ModelPreloadResult(
            label=label,
            ok=False,
            detail=f"Could not preload {label}: {error}",
        )
    return ModelPreloadResult(
        label=label,
        ok=True,
        detail=f"Preloaded {label}.",
    )


def _report_progress(progress: Callable[[str], None] | None, message: str) -> None:
    if progress is not None:
        progress(message)
