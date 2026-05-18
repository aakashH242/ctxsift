"""Daemon-backed embedding backend."""

from __future__ import annotations

import asyncio

from ctxsift.daemon.client import (
    DaemonClientError,
    request_embed_documents,
    request_embed_query,
)
from ctxsift.daemon.manager import embedding_daemon_spec, ensure_daemon, forget_daemon
from ctxsift.daemon.registry import tail_log_text
from ctxsift.daemon.types import EmbedDocumentsRequestPayload, EmbedQueryRequestPayload
from ctxsift.embeddings.base import (
    DocumentEmbeddingRequest,
    EmbeddingBackend,
    EmbeddingBackendUnavailableError,
    QueryEmbeddingRequest,
)
from ctxsift.types import DaemonConfig, EmbeddingConfig


class DaemonEmbeddingBackend(EmbeddingBackend):
    """Embedding backend that delegates to a background daemon."""

    provider_name = "sentence_transformers"

    def __init__(self, config: EmbeddingConfig, daemon: DaemonConfig, timeout_ms: int = 90000) -> None:
        self._config = config
        self._daemon = daemon
        self._timeout_ms = timeout_ms
        self.model_name = config.model

    async def embedding_dimension(self) -> int:
        response = await self._query_dimension()
        return response.dimension

    async def embed_query(self, request: QueryEmbeddingRequest) -> list[float]:
        response = await self._query_dimension(request)
        return response.vector

    async def embed_documents(self, request: DocumentEmbeddingRequest) -> list[list[float]]:
        response = await self._documents_response(request)
        return response.vectors

    async def preload(self) -> None:
        await asyncio.to_thread(ensure_daemon, self._current_spec())

    async def shutdown(self) -> None:
        return None

    async def _query_dimension(
        self,
        request: QueryEmbeddingRequest | None = None,
    ):
        request = request or QueryEmbeddingRequest(
            text="ctxsift daemon dimension probe",
            max_length=self._config.max_length,
        )
        payload = EmbedQueryRequestPayload(request=request)
        spec = self._current_spec()
        try:
            return await self._query_once(spec, payload)
        except (DaemonClientError, RuntimeError):
            forget_daemon(spec)
            try:
                return await self._query_once(spec, payload)
            except (DaemonClientError, RuntimeError) as error:
                raise EmbeddingBackendUnavailableError(self._error_detail(spec, error)) from error

    async def _documents_response(self, request: DocumentEmbeddingRequest):
        payload = EmbedDocumentsRequestPayload(request=request)
        spec = self._current_spec()
        try:
            return await self._documents_once(spec, payload)
        except (DaemonClientError, RuntimeError):
            forget_daemon(spec)
            try:
                return await self._documents_once(spec, payload)
            except (DaemonClientError, RuntimeError) as error:
                raise EmbeddingBackendUnavailableError(self._error_detail(spec, error)) from error

    async def _query_once(self, spec, payload: EmbedQueryRequestPayload):
        record = await asyncio.to_thread(ensure_daemon, spec)
        return await asyncio.to_thread(
            request_embed_query,
            record,
            payload,
            self._timeout_ms,
        )

    async def _documents_once(self, spec, payload: EmbedDocumentsRequestPayload):
        record = await asyncio.to_thread(ensure_daemon, spec)
        return await asyncio.to_thread(
            request_embed_documents,
            record,
            payload,
            self._timeout_ms,
        )

    def _current_spec(self):
        return embedding_daemon_spec(self._config, self._daemon)

    def _error_detail(self, spec, error: Exception) -> str:
        log_tail = tail_log_text(self._log_path(spec)).strip()
        if log_tail:
            return f"{error}. Log tail: {log_tail}"
        return str(error)

    def _log_path(self, spec):
        from ctxsift.daemon.registry import log_path

        return log_path(spec.role, spec.signature_hash)
