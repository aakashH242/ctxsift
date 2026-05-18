"""Runtime signature helpers for daemon reuse."""

from __future__ import annotations

import hashlib
import json

from ctxsift.daemon.types import CompressionRuntimeSignature, DaemonRole, EmbeddingRuntimeSignature, RuntimeSignature
from ctxsift.models.local_runtime import required_gguf_filename, resolve_local_runtime
from ctxsift.types import EmbeddingConfig, LocalModelConfig


def build_compression_signature(config: LocalModelConfig) -> CompressionRuntimeSignature:
    """Build the daemon sharing key for local compression."""
    runtime = resolve_local_runtime(config)
    if runtime.uses_llama_cpp:
        return CompressionRuntimeSignature(
            role=DaemonRole.COMPRESSION,
            provider=runtime.provider_name,
            model=config.model.strip(),
            gguf_filename=required_gguf_filename(config),
            device=runtime.resolved_device.label,
        )
    return CompressionRuntimeSignature(
        role=DaemonRole.COMPRESSION,
        provider=runtime.provider_name,
        model=config.model.strip(),
        device=runtime.resolved_device.label,
        dtype=config.dtype,
        attn_implementation=config.attn_implementation,
        quantization=config.quantization.value,
    )


def build_embedding_signature(config: EmbeddingConfig) -> EmbeddingRuntimeSignature:
    """Build the daemon sharing key for embeddings."""
    return EmbeddingRuntimeSignature(
        role=DaemonRole.EMBEDDING,
        backend=config.backend,
        model=config.model,
        device=config.device,
        dtype=config.dtype,
        attn_implementation=config.attn_implementation,
        query_prompt_name=config.query_prompt_name,
        query_prompt=config.query_prompt,
        document_prompt_name=config.document_prompt_name,
        max_length=config.max_length,
    )


def signature_hash(signature: RuntimeSignature) -> str:
    """Return a stable hash for one runtime signature."""
    payload = json.dumps(signature.model_dump(mode="json"), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
