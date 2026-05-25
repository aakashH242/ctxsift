"""Tests for daemon-backed compression and embedding wrappers."""

from __future__ import annotations

import asyncio

import pytest

from ctxsift.compression.intent import CompressionIntent
import ctxsift.embeddings.daemon_backend as embedding_daemon
import ctxsift.models.daemon_backend as compression_daemon
from ctxsift.daemon.client import DaemonClientError
from ctxsift.daemon.types import (
    CompressResponsePayload,
    DaemonRegistryRecord,
    DaemonRole,
    EmbedQueryResponsePayload,
)
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError, QueryEmbeddingRequest
from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.daemon_backend import DaemonCompressionBackend
from ctxsift.types import AppConfig, EmbeddingConfig, ExtractedSignal
from ctxsift.embeddings.daemon_backend import DaemonEmbeddingBackend


def test_daemon_compression_backend_retries_once_after_transport_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash="abc",
        model="fake/compression",
        device="cpu",
        pid=123,
        port=4040,
        auth_token="token",
    )
    attempts: list[str] = []
    forgotten: list[str] = []

    monkeypatch.setattr(compression_daemon, "ensure_daemon", lambda spec: record)

    def fake_request(record_arg, payload, timeout_ms):
        attempts.append(payload.raw_input)
        if len(attempts) == 1:
            raise DaemonClientError("connection reset")
        return CompressResponsePayload(compressed_output="compressed output")

    monkeypatch.setattr(compression_daemon, "request_compress", fake_request)
    monkeypatch.setattr(
        compression_daemon,
        "forget_daemon",
        lambda spec: forgotten.append(spec.signature_hash),
    )
    monkeypatch.setattr(compression_daemon, "tail_log_text", lambda path: "")
    backend = DaemonCompressionBackend(AppConfig())

    result = asyncio.run(
        backend.compress(
            ModelCompressionInput(
                intent=CompressionIntent.SUMMARY,
                instruction="compress",
                raw_input="stderr here",
                extracted_signal=ExtractedSignal(),
                max_output_tokens=32,
            )
        )
    )

    assert result == "compressed output"
    assert attempts == ["stderr here", "stderr here"]
    assert forgotten == [
        compression_daemon.compression_daemon_spec(
            backend._config.local, backend._config.daemon
        ).signature_hash
    ]


def test_daemon_compression_backend_forwards_recovery_flag(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash="abc",
        model="fake/compression",
        device="cpu",
        pid=123,
        port=4040,
        auth_token="token",
    )
    captured: dict[str, bool] = {}

    monkeypatch.setattr(compression_daemon, "ensure_daemon", lambda spec: record)

    def fake_request(record_arg, payload, timeout_ms):
        del record_arg, timeout_ms
        captured["recovery_enabled"] = payload.recovery_enabled
        return CompressResponsePayload(compressed_output="compressed output")

    monkeypatch.setattr(compression_daemon, "request_compress", fake_request)
    backend = DaemonCompressionBackend(AppConfig())

    asyncio.run(
        backend.compress(
            ModelCompressionInput(
                intent=CompressionIntent.SUMMARY,
                instruction="compress",
                raw_input="stderr here",
                extracted_signal=ExtractedSignal(),
                max_output_tokens=32,
                recovery_enabled=False,
            )
        )
    )

    assert captured["recovery_enabled"] is False


def test_daemon_compression_backend_resolves_current_spec_per_request(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = AppConfig()
    backend = DaemonCompressionBackend(config)
    seen_hashes: list[str] = []

    def fake_ensure(spec):
        seen_hashes.append(spec.signature_hash)
        return DaemonRegistryRecord(
            role=DaemonRole.COMPRESSION,
            signature_hash=spec.signature_hash,
            model=spec.model,
            device=spec.device,
            pid=123,
            port=4040,
            auth_token="token",
        )

    monkeypatch.setattr(compression_daemon, "ensure_daemon", fake_ensure)
    monkeypatch.setattr(
        compression_daemon,
        "request_compress",
        lambda record_arg, payload, timeout_ms: CompressResponsePayload(compressed_output="ok"),
    )

    asyncio.run(
        backend.compress(
            ModelCompressionInput(
                intent=CompressionIntent.SUMMARY,
                instruction="compress",
                raw_input="before",
                extracted_signal=ExtractedSignal(),
                max_output_tokens=32,
            )
        )
    )
    config.local.model = "HuggingFaceTB/SmolLM2-360M-Instruct-GGUF"
    config.local.gguf_filename = "smollm2-360m-instruct-q8_0.gguf"
    asyncio.run(
        backend.compress(
            ModelCompressionInput(
                intent=CompressionIntent.SUMMARY,
                instruction="compress",
                raw_input="after",
                extracted_signal=ExtractedSignal(),
                max_output_tokens=32,
            )
        )
    )

    assert len(seen_hashes) == 2
    assert seen_hashes[0] != seen_hashes[1]


def test_daemon_embedding_backend_raises_unavailable_after_retry_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    record = DaemonRegistryRecord(
        role=DaemonRole.EMBEDDING,
        signature_hash="def",
        model="fake/embeddings",
        device="cpu",
        pid=123,
        port=5050,
        auth_token="token",
    )
    attempts = 0

    monkeypatch.setattr(embedding_daemon, "ensure_daemon", lambda spec: record)

    def fail_request(record_arg, payload, timeout_ms):
        nonlocal attempts
        attempts += 1
        raise DaemonClientError("down")

    monkeypatch.setattr(embedding_daemon, "request_embed_query", fail_request)
    monkeypatch.setattr(embedding_daemon, "forget_daemon", lambda spec: None)
    monkeypatch.setattr(embedding_daemon, "tail_log_text", lambda path: "")
    backend = DaemonEmbeddingBackend(EmbeddingConfig(model="fake/embeddings"), AppConfig().daemon)

    with pytest.raises(EmbeddingBackendUnavailableError):
        asyncio.run(backend.embed_query(QueryEmbeddingRequest(text="AuthError", max_length=64)))

    assert attempts == 2


def test_daemon_embedding_backend_returns_dimension_from_daemon_response(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    record = DaemonRegistryRecord(
        role=DaemonRole.EMBEDDING,
        signature_hash="xyz",
        model="fake/embeddings",
        device="cpu",
        pid=123,
        port=5050,
        auth_token="token",
    )
    monkeypatch.setattr(embedding_daemon, "ensure_daemon", lambda spec: record)
    monkeypatch.setattr(
        embedding_daemon,
        "request_embed_query",
        lambda record_arg, payload, timeout_ms: EmbedQueryResponsePayload(
            vector=[0.1, 0.2, 0.3],
            model_name="fake/embeddings",
            dimension=3,
        ),
    )
    backend = DaemonEmbeddingBackend(EmbeddingConfig(model="fake/embeddings"), AppConfig().daemon)

    dimension = asyncio.run(backend.embedding_dimension())
    vector = asyncio.run(backend.embed_query(QueryEmbeddingRequest(text="query", max_length=64)))

    assert dimension == 3
    assert vector == [0.1, 0.2, 0.3]


def test_daemon_embedding_backend_resolves_current_spec_per_request(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = EmbeddingConfig(model="fake/embeddings")
    backend = DaemonEmbeddingBackend(config, AppConfig().daemon)
    seen_hashes: list[str] = []

    def fake_ensure(spec):
        seen_hashes.append(spec.signature_hash)
        return DaemonRegistryRecord(
            role=DaemonRole.EMBEDDING,
            signature_hash=spec.signature_hash,
            model=spec.model,
            device=spec.device,
            pid=123,
            port=5050,
            auth_token="token",
        )

    monkeypatch.setattr(embedding_daemon, "ensure_daemon", fake_ensure)
    monkeypatch.setattr(
        embedding_daemon,
        "request_embed_query",
        lambda record_arg, payload, timeout_ms: EmbedQueryResponsePayload(
            vector=[0.1, 0.2, 0.3],
            model_name="fake/embeddings",
            dimension=3,
        ),
    )

    asyncio.run(backend.embed_query(QueryEmbeddingRequest(text="query", max_length=64)))
    config.model = "microsoft/harrier-oss-v1-0.6b"
    asyncio.run(backend.embed_query(QueryEmbeddingRequest(text="query", max_length=64)))

    assert len(seen_hashes) == 2
    assert seen_hashes[0] != seen_hashes[1]
