"""Background daemon worker server and batching services."""

from __future__ import annotations

import asyncio
from concurrent.futures import Future
from dataclasses import dataclass
import gc
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
from queue import Empty, Queue
import threading
import time
from typing import Any

from rich.console import Console
from rich.panel import Panel

from ctxsift.daemon.registry import (
    delete_registry_record_if_owned,
    write_registry_record,
)
from ctxsift.daemon.types import (
    CompressRequestPayload,
    CompressResponsePayload,
    DaemonLaunchPayload,
    DaemonRegistryRecord,
    DaemonRole,
    EmbedDocumentsRequestPayload,
    EmbedDocumentsResponsePayload,
    EmbedQueryRequestPayload,
    EmbedQueryResponsePayload,
    HealthResponse,
    JsonErrorPayload,
)
from ctxsift.embeddings.base import (
    DocumentEmbeddingRequest,
    EmbeddingBackend,
    QueryEmbeddingRequest,
)
from ctxsift.embeddings.factory import create_in_process_embedding_backend
from ctxsift.models.local_runtime import resolve_local_runtime
from ctxsift.models.base import ModelBackend, ModelCompressionInput
from ctxsift.models.factory import create_local_backend

AUTH_HEADER = "X-Ctxsift-Token"
SERVER_POLL_INTERVAL_SECONDS = 0.5


@dataclass(frozen=True)
class CompressionTask:
    """One compression task queued inside the compression daemon."""

    request: CompressRequestPayload
    future: Future[str]


@dataclass(frozen=True)
class QueryEmbeddingTask:
    """One query embedding task queued inside the embedding daemon."""

    request: QueryEmbeddingRequest
    future: Future[EmbedQueryResponsePayload]


@dataclass(frozen=True)
class DocumentEmbeddingTask:
    """One document embedding task queued inside the embedding daemon."""

    request: DocumentEmbeddingRequest
    future: Future[EmbedDocumentsResponsePayload]


class CompressionRuntimeService:
    """Queued, serialized compression service."""

    def __init__(self, backend: ModelBackend) -> None:
        self._backend = backend
        self._queue: Queue[CompressionTask | None] = Queue()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self) -> None:
        self._thread.start()

    def submit(self, request: CompressRequestPayload) -> str:
        future: Future[str] = Future()
        self._queue.put(CompressionTask(request=request, future=future))
        return future.result()

    def queue_depth(self) -> int:
        return self._queue.qsize()

    def close(self) -> None:
        self._queue.put(None)
        self._thread.join(timeout=5)
        asyncio.run(self._backend.shutdown())

    def _run(self) -> None:
        while True:
            task = self._queue.get()
            if task is None:
                return
            try:
                result = asyncio.run(
                    self._backend.compress(
                        ModelCompressionInput(
                            intent=task.request.intent,
                            instruction=task.request.instruction,
                            raw_input=task.request.raw_input,
                            extracted_signal=task.request.extracted_signal,
                            max_output_tokens=task.request.max_output_tokens,
                            recovery_enabled=task.request.recovery_enabled,
                        )
                    )
                )
            except Exception as error:
                task.future.set_exception(error)
            else:
                task.future.set_result(result)


class EmbeddingRuntimeService:
    """Batching embedding service for queries and documents."""

    def __init__(
        self,
        backend: EmbeddingBackend,
        batch_window_ms: int,
        max_batch_size: int,
    ) -> None:
        self._backend = backend
        self._batch_window_seconds = max(batch_window_ms, 0) / 1000
        self._max_batch_size = max(max_batch_size, 1)
        self._query_queue: Queue[QueryEmbeddingTask | None] = Queue()
        self._documents_queue: Queue[DocumentEmbeddingTask | None] = Queue()
        self._query_thread = threading.Thread(target=self._run_query_batches, daemon=True)
        self._documents_thread = threading.Thread(target=self._run_document_batches, daemon=True)
        self._dimension: int | None = None
        self._dimension_lock = threading.Lock()

    def start(self) -> None:
        self._query_thread.start()
        self._documents_thread.start()

    def submit_query(self, request: QueryEmbeddingRequest) -> EmbedQueryResponsePayload:
        future: Future[EmbedQueryResponsePayload] = Future()
        self._query_queue.put(QueryEmbeddingTask(request=request, future=future))
        return future.result()

    def submit_documents(
        self,
        request: DocumentEmbeddingRequest,
    ) -> EmbedDocumentsResponsePayload:
        future: Future[EmbedDocumentsResponsePayload] = Future()
        self._documents_queue.put(DocumentEmbeddingTask(request=request, future=future))
        return future.result()

    def queue_depth(self) -> int:
        return self._query_queue.qsize() + self._documents_queue.qsize()

    def close(self) -> None:
        self._query_queue.put(None)
        self._documents_queue.put(None)
        self._query_thread.join(timeout=5)
        self._documents_thread.join(timeout=5)
        asyncio.run(self._backend.shutdown())

    def _run_query_batches(self) -> None:
        while True:
            tasks = self._drain_query_batch()
            if tasks is None:
                return
            if not tasks:
                continue
            try:
                requests = [task.request for task in tasks]
                vectors = asyncio.run(self._backend.embed_queries(requests))
                dimension = self._dimension_value()
                for task, vector in zip(tasks, vectors, strict=True):
                    task.future.set_result(
                        EmbedQueryResponsePayload(
                            vector=vector,
                            model_name=self._backend.model_name,
                            dimension=dimension,
                        )
                    )
            except Exception as error:
                for task in tasks:
                    task.future.set_exception(error)

    def _run_document_batches(self) -> None:
        while True:
            tasks = self._drain_document_batch()
            if tasks is None:
                return
            if not tasks:
                continue
            try:
                requests = [task.request for task in tasks]
                vectors = asyncio.run(self._backend.embed_documents_batch(requests))
                dimension = self._dimension_value()
                for task, vector_batch in zip(tasks, vectors, strict=True):
                    task.future.set_result(
                        EmbedDocumentsResponsePayload(
                            vectors=vector_batch,
                            model_name=self._backend.model_name,
                            dimension=dimension,
                        )
                    )
            except Exception as error:
                for task in tasks:
                    task.future.set_exception(error)

    def _drain_query_batch(self) -> list[QueryEmbeddingTask] | None:
        first = self._query_queue.get()
        if first is None:
            return None
        tasks = [first]
        deadline = time.monotonic() + self._batch_window_seconds
        while len(tasks) < self._max_batch_size:
            timeout = deadline - time.monotonic()
            if timeout <= 0:
                break
            try:
                item = self._query_queue.get(timeout=timeout)
            except Empty:
                break
            if item is None:
                self._query_queue.put(None)
                break
            tasks.append(item)
        return tasks

    def _drain_document_batch(self) -> list[DocumentEmbeddingTask] | None:
        first = self._documents_queue.get()
        if first is None:
            return None
        tasks = [first]
        deadline = time.monotonic() + self._batch_window_seconds
        while len(tasks) < self._max_batch_size:
            timeout = deadline - time.monotonic()
            if timeout <= 0:
                break
            try:
                item = self._documents_queue.get(timeout=timeout)
            except Empty:
                break
            if item is None:
                self._documents_queue.put(None)
                break
            tasks.append(item)
        return tasks

    def _dimension_value(self) -> int:
        if self._dimension is not None:
            return self._dimension
        with self._dimension_lock:
            if self._dimension is None:
                self._dimension = int(asyncio.run(self._backend.embedding_dimension()))
        return self._dimension


class DaemonApp:
    """Owns worker lifecycle, HTTP handling, and idle shutdown."""

    def __init__(self, payload: DaemonLaunchPayload) -> None:
        self.payload = payload
        self._registry_path = Path(payload.registry_path)
        self._idle_timeout_seconds = payload.daemon.idle_timeout_seconds
        self._last_activity = time.monotonic()
        self._lock = threading.Lock()
        self._inflight_requests = 0
        self._stop_requested = threading.Event()
        self._service = self._build_service()
        self._service.start()

    def serve(self) -> None:
        handler = self._handler_class()
        with ThreadingHTTPServer(("127.0.0.1", self.payload.port), handler) as server:
            server.timeout = SERVER_POLL_INTERVAL_SECONDS
            server.daemon_threads = True
            server.ctxsift_app = self  # type: ignore[attr-defined]
            self._write_registry_record()
            try:
                while not self._stop_requested.is_set():
                    server.handle_request()
                    if self._should_exit_for_idle():
                        break
            finally:
                self._cleanup()

    def health_response(self) -> HealthResponse:
        return HealthResponse(
            role=self.payload.role,
            signature_hash=self.payload.signature_hash,
            pid=os.getpid(),
            model=self._model_name(),
            device=self._device_name(),
            queue_depth=self._service.queue_depth(),
        )

    def handle_compress(self, payload: CompressRequestPayload) -> CompressResponsePayload:
        self._begin_request()
        try:
            result = self._compression_service().submit(payload)
            return CompressResponsePayload(compressed_output=result)
        finally:
            self._end_request()

    def handle_embed_query(self, payload: EmbedQueryRequestPayload) -> EmbedQueryResponsePayload:
        self._begin_request()
        try:
            return self._embedding_service().submit_query(payload.request)
        finally:
            self._end_request()

    def handle_embed_documents(
        self,
        payload: EmbedDocumentsRequestPayload,
    ) -> EmbedDocumentsResponsePayload:
        self._begin_request()
        try:
            return self._embedding_service().submit_documents(payload.request)
        finally:
            self._end_request()

    def request_stop(self) -> None:
        self._stop_requested.set()

    def is_authorized(self, token: str | None) -> bool:
        return bool(token) and token == self.payload.auth_token

    def _begin_request(self) -> None:
        with self._lock:
            self._inflight_requests += 1
            self._last_activity = time.monotonic()

    def _end_request(self) -> None:
        with self._lock:
            self._inflight_requests = max(self._inflight_requests - 1, 0)
            self._last_activity = time.monotonic()

    def _should_exit_for_idle(self) -> bool:
        with self._lock:
            if self._inflight_requests > 0:
                return False
            idle_for = time.monotonic() - self._last_activity
        return idle_for >= self._idle_timeout_seconds and self._service.queue_depth() == 0

    def _cleanup(self) -> None:
        try:
            self._service.close()
        finally:
            self._release_gpu_memory()
            delete_registry_record_if_owned(self._registry_path, os.getpid())

    def _release_gpu_memory(self) -> None:
        gc.collect()
        try:
            import torch
        except Exception:
            return
        if torch.cuda.is_available():
            try:
                torch.cuda.empty_cache()
            except Exception:
                return

    def _build_service(self) -> CompressionRuntimeService | EmbeddingRuntimeService:
        if self.payload.role is DaemonRole.COMPRESSION:
            if self.payload.local is None:
                raise RuntimeError("Compression daemon launch payload is missing local config.")
            return CompressionRuntimeService(create_local_backend(self.payload.local))
        if self.payload.embedding is None:
            raise RuntimeError("Embedding daemon launch payload is missing embedding config.")
        return EmbeddingRuntimeService(
            backend=create_in_process_embedding_backend(self.payload.embedding),
            batch_window_ms=self.payload.daemon.embedding_batch_window_ms,
            max_batch_size=self.payload.daemon.embedding_max_batch_size,
        )

    def _compression_service(self) -> CompressionRuntimeService:
        if not isinstance(self._service, CompressionRuntimeService):
            raise RuntimeError("Compression request received by embedding daemon.")
        return self._service

    def _embedding_service(self) -> EmbeddingRuntimeService:
        if not isinstance(self._service, EmbeddingRuntimeService):
            raise RuntimeError("Embedding request received by compression daemon.")
        return self._service

    def _write_registry_record(self) -> None:
        record = DaemonRegistryRecord(
            role=self.payload.role,
            signature_hash=self.payload.signature_hash,
            model=self._model_name(),
            device=self._device_name(),
            pid=os.getpid(),
            port=self.payload.port,
            auth_token=self.payload.auth_token,
        )
        write_registry_record(self._registry_path, record)

    def _model_name(self) -> str:
        if self.payload.role is DaemonRole.COMPRESSION:
            assert self.payload.local is not None
            return self.payload.local.model
        assert self.payload.embedding is not None
        return self.payload.embedding.model

    def _device_name(self) -> str:
        if self.payload.role is DaemonRole.COMPRESSION:
            assert self.payload.local is not None
            return resolve_local_runtime(self.payload.local).resolved_device.label
        assert self.payload.embedding is not None
        return self.payload.embedding.device

    def _handler_class(self):
        app = self

        class DaemonRequestHandler(BaseHTTPRequestHandler):
            """HTTP handler bound to one daemon app instance."""

            server_version = "ctxsift-daemon/1"

            def do_GET(self) -> None:  # noqa: N802
                if not app.is_authorized(self.headers.get(AUTH_HEADER)):
                    self._write_json(
                        HTTPStatus.UNAUTHORIZED, JsonErrorPayload(error="Unauthorized")
                    )
                    return
                if self.path != "/health":
                    self._write_json(HTTPStatus.NOT_FOUND, JsonErrorPayload(error="Not found"))
                    return
                self._write_json(HTTPStatus.OK, app.health_response())

            def do_POST(self) -> None:  # noqa: N802
                if not app.is_authorized(self.headers.get(AUTH_HEADER)):
                    self._write_json(
                        HTTPStatus.UNAUTHORIZED, JsonErrorPayload(error="Unauthorized")
                    )
                    return
                try:
                    if self.path == "/compress":
                        compress_payload = CompressRequestPayload.model_validate_json(
                            self._read_body()
                        )
                        self._write_json(HTTPStatus.OK, app.handle_compress(compress_payload))
                        return
                    if self.path == "/embed_query":
                        query_payload = EmbedQueryRequestPayload.model_validate_json(
                            self._read_body()
                        )
                        self._write_json(HTTPStatus.OK, app.handle_embed_query(query_payload))
                        return
                    if self.path == "/embed_documents":
                        documents_payload = EmbedDocumentsRequestPayload.model_validate_json(
                            self._read_body()
                        )
                        self._write_json(
                            HTTPStatus.OK,
                            app.handle_embed_documents(documents_payload),
                        )
                        return
                    if self.path == "/stop":
                        app.request_stop()
                        self._write_json(HTTPStatus.OK, {"stopping": True})
                        return
                    self._write_json(HTTPStatus.NOT_FOUND, JsonErrorPayload(error="Not found"))
                except Exception as error:
                    self._write_json(
                        HTTPStatus.SERVICE_UNAVAILABLE,
                        JsonErrorPayload(error=type(error).__name__, detail=str(error)),
                    )

            def log_message(self, format: str, *args: object) -> None:  # noqa: A003
                return None

            def _read_body(self) -> str:
                length = int(self.headers.get("Content-Length", "0"))
                return self.rfile.read(length).decode("utf-8")

            def _write_json(self, status: HTTPStatus, payload: Any) -> None:
                if hasattr(payload, "model_dump_json"):
                    raw = payload.model_dump_json().encode("utf-8")
                else:
                    raw = json.dumps(payload).encode("utf-8")
                self.send_response(int(status))
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

        return DaemonRequestHandler


def run_daemon(payload: DaemonLaunchPayload) -> None:
    """Run one daemon worker until stopped or idle timeout is reached."""
    _print_startup_notice(payload)
    DaemonApp(payload).serve()


def _print_startup_notice(payload: DaemonLaunchPayload) -> None:
    if payload.role is DaemonRole.COMPRESSION:
        if payload.local is None:
            raise RuntimeError("Compression daemon launch payload is missing local config.")
        model_name = payload.local.model
        device_name = payload.local.device
    else:
        if payload.embedding is None:
            raise RuntimeError("Embedding daemon launch payload is missing embedding config.")
        model_name = payload.embedding.model
        device_name = payload.embedding.device
    body = "\n".join(
        [
            f"CtxSift daemon started for {payload.role.value} requests.",
            f"Model: {model_name}",
            f"Device: {device_name}",
            f"Port: {payload.port}",
            f"Log file: {payload.log_path}",
            "Do not close this process while clients are using the daemon.",
        ]
    )
    Console().print(Panel(body, title="CtxSift Daemon", border_style="cyan"))
