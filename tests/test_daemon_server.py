"""Tests for daemon runtime services."""

from __future__ import annotations

import threading
import time

from ctxsift.daemon.server import CompressionRuntimeService, EmbeddingRuntimeService
from ctxsift.daemon.types import CompressRequestPayload
from ctxsift.embeddings.base import DocumentEmbeddingRequest, QueryEmbeddingRequest
from ctxsift.models.base import ModelCompressionInput
from ctxsift.types import ExtractedSignal


class FakeCompressionBackend:
    provider_name = "transformers"
    model_name = "fake/compression"
    cache_model_id = "fake/compression"

    def __init__(self) -> None:
        self.calls: list[str] = []

    async def compress(self, request: ModelCompressionInput) -> str:
        self.calls.append(request.raw_input)
        time.sleep(0.01)
        return f"compressed:{request.raw_input}"

    async def shutdown(self) -> None:
        return None


class FakeEmbeddingBackend:
    provider_name = "sentence_transformers"
    model_name = "fake/embeddings"

    def __init__(self) -> None:
        self.query_batches: list[list[str]] = []
        self.document_batches: list[list[list[str]]] = []

    async def embedding_dimension(self) -> int:
        return 3

    async def embed_query(self, request: QueryEmbeddingRequest) -> list[float]:
        return [1.0, 0.0, 0.0]

    async def embed_documents(self, request: DocumentEmbeddingRequest) -> list[list[float]]:
        return [[1.0, 0.0, 0.0] for _ in request.texts]

    async def embed_queries(self, requests: list[QueryEmbeddingRequest]) -> list[list[float]]:
        self.query_batches.append([request.text for request in requests])
        return [[float(index + 1), 0.0, 0.0] for index, _ in enumerate(requests)]

    async def embed_documents_batch(
        self,
        requests: list[DocumentEmbeddingRequest],
    ) -> list[list[list[float]]]:
        self.document_batches.append([request.texts for request in requests])
        return [[[1.0, 0.0, 0.0] for _ in request.texts] for request in requests]

    async def shutdown(self) -> None:
        return None


def test_compression_runtime_service_serializes_requests_without_mixing_outputs() -> None:
    backend = FakeCompressionBackend()
    service = CompressionRuntimeService(backend)
    service.start()
    try:
        results: list[str] = ["", ""]

        def submit(index: int, text: str) -> None:
            results[index] = service.submit(
                CompressRequestPayload(
                    instruction="compress",
                    raw_input=text,
                    extracted_signal=ExtractedSignal(),
                    max_output_tokens=64,
                )
            )

        first = threading.Thread(target=submit, args=(0, "first"))
        second = threading.Thread(target=submit, args=(1, "second"))
        first.start()
        second.start()
        first.join()
        second.join()
    finally:
        service.close()

    assert results == ["compressed:first", "compressed:second"]
    assert backend.calls == ["first", "second"]


def test_embedding_runtime_service_batches_query_requests() -> None:
    backend = FakeEmbeddingBackend()
    service = EmbeddingRuntimeService(backend, batch_window_ms=50, max_batch_size=8)
    service.start()
    try:
        results: list[list[float]] = [[], []]

        def submit(index: int, text: str) -> None:
            results[index] = service.submit_query(
                QueryEmbeddingRequest(text=text, max_length=128)
            ).vector

        first = threading.Thread(target=submit, args=(0, "first query"))
        second = threading.Thread(target=submit, args=(1, "second query"))
        first.start()
        second.start()
        first.join()
        second.join()
    finally:
        service.close()

    assert backend.query_batches == [["first query", "second query"]]
    assert results == [[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]]


def test_embedding_runtime_service_batches_document_requests() -> None:
    backend = FakeEmbeddingBackend()
    service = EmbeddingRuntimeService(backend, batch_window_ms=50, max_batch_size=8)
    service.start()
    try:
        outputs: list[list[list[float]]] = [[], []]

        def submit(index: int, texts: list[str]) -> None:
            outputs[index] = service.submit_documents(
                DocumentEmbeddingRequest(texts=texts, max_length=128)
            ).vectors

        first = threading.Thread(target=submit, args=(0, ["one"]))
        second = threading.Thread(target=submit, args=(1, ["two", "three"]))
        first.start()
        second.start()
        first.join()
        second.join()
    finally:
        service.close()

    assert backend.document_batches == [[["one"], ["two", "three"]]]
    assert outputs[0] == [[1.0, 0.0, 0.0]]
    assert outputs[1] == [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
