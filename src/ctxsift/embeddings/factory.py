"""Factories for configured embedding backends."""

from __future__ import annotations

from ctxsift.embeddings.daemon_backend import DaemonEmbeddingBackend
from ctxsift.embeddings.base import EmbeddingBackend, EmbeddingBackendUnavailableError
from ctxsift.embeddings.sentence_transformers_backend import SentenceTransformersBackend
from ctxsift.types import DaemonConfig, EmbeddingConfig


def create_in_process_embedding_backend(config: EmbeddingConfig) -> EmbeddingBackend:
    """Create one in-process embedding backend."""
    if config.model:
        return SentenceTransformersBackend(config)
    raise EmbeddingBackendUnavailableError("No embedding model is configured.")


def create_embedding_backend(
    config: EmbeddingConfig,
    daemon: DaemonConfig | None = None,
    timeout_ms: int = 90000,
) -> EmbeddingBackend:
    """Create one configured embedding backend."""
    if daemon is not None and daemon.enabled:
        return DaemonEmbeddingBackend(config, daemon, timeout_ms=timeout_ms)
    return create_in_process_embedding_backend(config)
