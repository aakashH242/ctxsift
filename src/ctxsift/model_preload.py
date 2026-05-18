"""Model preload helpers used during guided configuration."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass

from ctxsift.embeddings import create_in_process_embedding_backend
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError
from ctxsift.models.llama_cpp_backend import preload_gguf_artifact
from ctxsift.models.local_runtime import resolve_local_runtime
from ctxsift.models.base import BackendUnavailableError
from ctxsift.models.factory import create_local_backend
from ctxsift.types import AppConfig

create_embedding_backend = create_in_process_embedding_backend


@dataclass(frozen=True)
class ModelPreloadResult:
    """One preload outcome for configure."""

    label: str
    ok: bool
    detail: str


async def preload_configured_models(config: AppConfig) -> list[ModelPreloadResult]:
    """Download or warm configured local models that ctxsift will need later."""
    results = [await _preload_embedding_model(config)]
    if not config.remote.base_url.strip():
        results.append(await _preload_local_compression_model(config))
    return results


async def _preload_embedding_model(config: AppConfig) -> ModelPreloadResult:
    label = f"embedding model {config.embedding.model}"
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


async def _preload_local_compression_model(config: AppConfig) -> ModelPreloadResult:
    label = f"local compression model {config.local.model}"
    try:
        runtime = resolve_local_runtime(config.local)
        if runtime.uses_llama_cpp:
            gguf_path = await asyncio.to_thread(preload_gguf_artifact, config.local)
            return ModelPreloadResult(
                label=label,
                ok=True,
                detail=f"Preloaded {label} ({gguf_path.name}).",
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
