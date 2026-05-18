"""Recall embedding indexing pipeline."""

from __future__ import annotations

from pathlib import Path

from ctxsift.embedding_text import build_record_embedding_text
from ctxsift.embeddings import create_embedding_backend
from ctxsift.embeddings.base import (
    DocumentEmbeddingRequest,
    EmbeddingBackendUnavailableError,
)
from ctxsift.types import (
    DaemonConfig,
    EmbeddingConfig,
    ExtractedTermRecord,
    ReferencedFileRecord,
    StoredRecord,
)
from ctxsift.vector_store import upsert_record_embedding


async def index_record_embedding(
    db_path: Path,
    record_id: int,
    record: StoredRecord,
    referenced_files: list[ReferencedFileRecord],
    extracted_terms: list[ExtractedTermRecord],
    config: EmbeddingConfig,
    daemon_config: DaemonConfig | None = None,
    timeout_ms: int = 90000,
) -> None:
    """Index one stored record into sqlite-vec when the backend is available."""
    try:
        backend = _embedding_backend(config, daemon_config, timeout_ms)
        dimension = await backend.embedding_dimension()
        document_text = build_record_embedding_text(record, referenced_files, extracted_terms)
        embeddings = await backend.embed_documents(
            DocumentEmbeddingRequest(
                texts=[document_text],
                max_length=config.max_length,
            )
        )
    except EmbeddingBackendUnavailableError:
        return
    await upsert_record_embedding(
        db_path=db_path,
        record_id=record_id,
        vector=embeddings[0],
        model_name=backend.model_name,
        dimension=dimension,
    )


def _embedding_backend(
    config: EmbeddingConfig,
    daemon_config: DaemonConfig | None,
    timeout_ms: int,
):
    if daemon_config is None or not daemon_config.enabled:
        return create_embedding_backend(config)
    return create_embedding_backend(config, daemon=daemon_config, timeout_ms=timeout_ms)
