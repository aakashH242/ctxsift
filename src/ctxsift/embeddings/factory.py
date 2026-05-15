"""Factories for configured embedding backends."""

from __future__ import annotations

from ctxsift.embeddings.base import EmbeddingBackend, EmbeddingBackendUnavailableError
from ctxsift.embeddings.sentence_transformers_backend import SentenceTransformersBackend
from ctxsift.types import EmbeddingConfig


def create_embedding_backend(config: EmbeddingConfig) -> EmbeddingBackend:
    """Create one configured embedding backend."""
    if config.model:
        return SentenceTransformersBackend(config)
    raise EmbeddingBackendUnavailableError("No embedding model is configured.")
