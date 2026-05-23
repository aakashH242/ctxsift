"""Tests for small remaining helpers needed by the CI coverage gate."""

from __future__ import annotations

import asyncio
from pathlib import Path
from types import ModuleType

import pytest

import ctxsift.acceleration as acceleration
import ctxsift.compression as compression_package
from ctxsift.embeddings.base import (
    DocumentEmbeddingRequest,
    EmbeddingBackend,
    QueryEmbeddingRequest,
)
from ctxsift.shared.db_path import resolved_db_path
from ctxsift.shared.hashing import sha256_if_reasonable, sha256_text


class FakeEmbeddingBackend(EmbeddingBackend):
    """Minimal concrete embedding backend for default-method tests."""

    provider_name = "fake"
    model_name = "fake/model"

    async def embedding_dimension(self) -> int:
        return 2

    async def embed_query(self, request: QueryEmbeddingRequest) -> list[float]:
        return [float(len(request.text)), float(request.max_length)]

    async def embed_documents(self, request: DocumentEmbeddingRequest) -> list[list[float]]:
        return [[float(len(text)), float(request.max_length)] for text in request.texts]


def test_flash_attention_availability_checks_known_module_names(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        acceleration,
        "_module_available",
        lambda module_name: module_name == "kernels",
    )

    assert acceleration.flash_attention_available() is True


def test_onnxruntime_availability_helpers_reflect_installed_modules(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        acceleration,
        "_module_available",
        lambda module_name: module_name in {"onnxruntime", "onnxruntime.capi"},
    )

    assert acceleration.onnxruntime_available() is True
    assert acceleration.onnxruntime_gpu_available() is True


def test_text_attention_choice_prefers_flash_attention_on_cuda(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(acceleration, "flash_attention_available", lambda: True)

    assert (
        acceleration.text_attention_choice("cuda:0", "auto") == acceleration.FLASH_ATTENTION_BACKEND
    )
    assert (
        acceleration.gemma_attention_choice("cuda:0", "auto")
        == acceleration.FLASH_ATTENTION_BACKEND
    )


def test_text_attention_choice_rejects_flash_attention_on_cpu() -> None:
    assert acceleration.text_attention_choice("cpu", acceleration.FLASH_ATTENTION_BACKEND) is None
    assert acceleration.text_attention_choice("cpu", "sdpa") == "sdpa"
    assert acceleration.text_attention_choice("cpu", "unknown") is None


def test_embedding_backend_choice_prefers_onnx_for_harrier_cpu(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(acceleration, "onnxruntime_available", lambda: True)

    backend = acceleration.embedding_backend_choice(
        "cpu",
        "auto",
        "microsoft/harrier-oss-v1-0.6b",
    )

    assert backend == "onnx"


def test_embedding_backend_choice_respects_manual_overrides(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(acceleration, "flash_attention_available", lambda: False)

    assert acceleration.embedding_backend_choice("cuda:0", "onnx", "demo/model") == "onnx"
    assert acceleration.embedding_backend_choice("cuda:0", "auto", "demo/model") == "torch"
    assert acceleration.embedding_attention_choice("cuda:0", "sdpa") == "sdpa"
    assert (
        acceleration.embedding_attention_choice("cpu", acceleration.FLASH_ATTENTION_BACKEND) is None
    )


def test_embedding_backend_choice_defaults_to_torch_for_unknown_manual_value() -> None:
    assert acceleration.embedding_backend_choice("cpu", "custom", "demo/model") == "torch"


def test_embedding_attention_choice_prefers_flash_attention_on_cuda(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(acceleration, "flash_attention_available", lambda: True)

    assert (
        acceleration.embedding_attention_choice("cuda:0", "auto")
        == acceleration.FLASH_ATTENTION_BACKEND
    )


def test_embedding_attention_choice_returns_none_for_unknown_manual_value() -> None:
    assert acceleration.embedding_attention_choice("cpu", "custom") is None


def test_compression_package_lazy_getattr_imports_supported_exports(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_module = ModuleType("fake")
    compression_intent_export = object()
    compress_input_export = object()
    render_run_payload_export = object()
    setattr(fake_module, "CompressionIntent", compression_intent_export)
    setattr(fake_module, "compress_input", compress_input_export)
    setattr(fake_module, "render_run_payload", render_run_payload_export)

    monkeypatch.setattr(compression_package, "import_module", lambda module_name: fake_module)

    assert compression_package.__getattr__("CompressionIntent") is compression_intent_export
    assert compression_package.__getattr__("compress_input") is compress_input_export
    assert compression_package.__getattr__("render_run_payload") is render_run_payload_export


def test_compression_package_lazy_getattr_rejects_unknown_exports() -> None:
    with pytest.raises(AttributeError, match="missing"):
        compression_package.__getattr__("missing")


def test_embedding_backend_default_batch_helpers_delegate_to_single_request_methods() -> None:
    backend = FakeEmbeddingBackend()

    query_vectors = asyncio.run(
        backend.embed_queries(
            [
                QueryEmbeddingRequest(text="ab", max_length=4),
                QueryEmbeddingRequest(text="hello", max_length=8),
            ]
        )
    )
    document_vectors = asyncio.run(
        backend.embed_documents_batch(
            [
                DocumentEmbeddingRequest(texts=["ab"], max_length=4),
                DocumentEmbeddingRequest(texts=["hello", "world"], max_length=8),
            ]
        )
    )

    assert query_vectors == [[2.0, 4.0], [5.0, 8.0]]
    assert document_vectors == [[[2.0, 4.0]], [[5.0, 8.0], [5.0, 8.0]]]


def test_embedding_backend_default_lifecycle_hooks_are_noops() -> None:
    backend = FakeEmbeddingBackend()

    preload_result = asyncio.run(backend.preload())
    shutdown_result = asyncio.run(backend.shutdown())

    assert preload_result is None
    assert shutdown_result is None


def test_resolved_db_path_prefers_config_override(tmp_path: Path) -> None:
    path = resolved_db_path(
        str(tmp_path / "workspace.db"),
        str(tmp_path / "config.db"),
        tmp_path,
    )

    assert path == (tmp_path / "config.db")


def test_resolved_db_path_resolves_relative_override_from_workspace_root(tmp_path: Path) -> None:
    path = resolved_db_path(
        str(tmp_path / "workspace.db"),
        ".ctxsift/custom.db",
        tmp_path,
    )

    assert path == tmp_path / ".ctxsift" / "custom.db"


def test_resolved_db_path_requires_some_source() -> None:
    with pytest.raises(ValueError, match="Could not resolve"):
        resolved_db_path(None, None, Path.cwd())


def test_sha256_helpers_cover_text_small_files_and_large_files(tmp_path: Path) -> None:
    small_file = tmp_path / "small.txt"
    small_file.write_text("hello", encoding="utf-8")
    large_file = tmp_path / "large.txt"
    large_file.write_bytes(b"x" * (2 * 1024 * 1024 + 1))

    assert sha256_text("hello") == sha256_if_reasonable(small_file)
    assert sha256_if_reasonable(large_file) is None
    assert sha256_if_reasonable(None) is None
