"""Shared daemon transport, registry, and signature models."""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any

from pydantic import Field

from ctxsift.embeddings.base import DocumentEmbeddingRequest, QueryEmbeddingRequest
from ctxsift.types import (
    DaemonConfig,
    EmbeddingConfig,
    ExtractedSignal,
    LocalModelConfig,
    StrictModel,
)


class DaemonRole(str, Enum):
    """Supported local daemon roles."""

    COMPRESSION = "compression"
    EMBEDDING = "embedding"


class CompressionRuntimeSignature(StrictModel):
    """Compression daemon sharing key."""

    role: DaemonRole = DaemonRole.COMPRESSION
    provider: str
    model: str
    gguf_filename: str | None = None
    device: str
    dtype: str | None = None
    attn_implementation: str | None = None
    quantization: str | None = None


class EmbeddingRuntimeSignature(StrictModel):
    """Embedding daemon sharing key."""

    role: DaemonRole = DaemonRole.EMBEDDING
    backend: str
    model: str
    device: str
    dtype: str
    attn_implementation: str
    query_prompt_name: str
    query_prompt: str
    document_prompt_name: str
    max_length: int


class DaemonLaunchPayload(StrictModel):
    """Worker launch payload written before process bootstrap."""

    role: DaemonRole
    signature_hash: str
    port: int
    auth_token: str
    registry_path: str
    log_path: str
    daemon: DaemonConfig
    local: LocalModelConfig | None = None
    embedding: EmbeddingConfig | None = None


class DaemonRegistryRecord(StrictModel):
    """One persisted daemon registry entry."""

    role: DaemonRole
    signature_hash: str
    model: str
    device: str
    pid: int
    port: int
    auth_token: str
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DaemonStatus(StrictModel):
    """One daemon status row for CLI rendering."""

    role: DaemonRole
    signature_hash: str
    model: str
    device: str
    pid: int | None = None
    port: int | None = None
    healthy: bool = False
    detail: str = ""


class HealthResponse(StrictModel):
    """Health payload returned by one daemon."""

    role: DaemonRole
    signature_hash: str
    pid: int
    model: str
    device: str
    queue_depth: int = 0


class CompressRequestPayload(StrictModel):
    """Compression daemon request payload."""

    instruction: str
    raw_input: str
    extracted_signal: ExtractedSignal
    max_output_tokens: int


class CompressResponsePayload(StrictModel):
    """Compression daemon response payload."""

    compressed_output: str


class EmbedQueryRequestPayload(StrictModel):
    """Embedding daemon query request payload."""

    request: QueryEmbeddingRequest


class EmbedQueryResponsePayload(StrictModel):
    """Embedding daemon query response payload."""

    vector: list[float]
    model_name: str
    dimension: int


class EmbedDocumentsRequestPayload(StrictModel):
    """Embedding daemon document request payload."""

    request: DocumentEmbeddingRequest


class EmbedDocumentsResponsePayload(StrictModel):
    """Embedding daemon document response payload."""

    vectors: list[list[float]]
    model_name: str
    dimension: int


class JsonErrorPayload(StrictModel):
    """Structured daemon error payload."""

    error: str
    detail: str = ""


RuntimeSignature = CompressionRuntimeSignature | EmbeddingRuntimeSignature


def signature_json(signature: RuntimeSignature) -> dict[str, Any]:
    """Return a JSON-safe signature mapping."""
    return signature.model_dump(mode="json")
