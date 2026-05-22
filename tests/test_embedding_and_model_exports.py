"""Tests for lightweight embedding and model export helpers."""

from __future__ import annotations

from types import ModuleType

import pytest

import ctxsift.embeddings as embeddings_package
import ctxsift.models as models_package
from ctxsift.embedding_text import build_record_embedding_text
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError
from ctxsift.embeddings.factory import create_embedding_backend, create_in_process_embedding_backend
from ctxsift.types import (
    DaemonConfig,
    EmbeddingConfig,
    ExtractedTermRecord,
    ReferencedFileRecord,
    StoredRecord,
)


def test_create_in_process_embedding_backend_returns_sentence_transformer(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_backend = object()
    monkeypatch.setattr(
        "ctxsift.embeddings.factory.SentenceTransformersBackend",
        lambda config: fake_backend,
    )

    backend = create_in_process_embedding_backend(EmbeddingConfig(model="demo/embed"))

    assert backend is fake_backend


def test_create_in_process_embedding_backend_requires_model() -> None:
    with pytest.raises(EmbeddingBackendUnavailableError, match="No embedding model is configured"):
        create_in_process_embedding_backend(EmbeddingConfig(model=""))


def test_create_embedding_backend_prefers_daemon_backend(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_backend = object()
    monkeypatch.setattr(
        "ctxsift.embeddings.factory.DaemonEmbeddingBackend",
        lambda config, daemon, timeout_ms: fake_backend,
    )

    backend = create_embedding_backend(
        EmbeddingConfig(model="demo/embed"),
        daemon=DaemonConfig(enabled=True),
        timeout_ms=321,
    )

    assert backend is fake_backend


def test_create_embedding_backend_falls_back_to_in_process(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_backend = object()
    monkeypatch.setattr(
        "ctxsift.embeddings.factory.create_in_process_embedding_backend",
        lambda config: fake_backend,
    )

    backend = create_embedding_backend(
        EmbeddingConfig(model="demo/embed"), daemon=DaemonConfig(enabled=False)
    )

    assert backend is fake_backend


def test_embeddings_package_exports_factory_helpers(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ctxsift.embeddings.factory.create_embedding_backend",
        lambda *args, **kwargs: ("daemon", args, kwargs),
    )
    monkeypatch.setattr(
        "ctxsift.embeddings.factory.create_in_process_embedding_backend",
        lambda *args, **kwargs: ("local", args, kwargs),
    )

    daemon_result = embeddings_package.create_embedding_backend("config")
    local_result = embeddings_package.create_in_process_embedding_backend("config")

    assert daemon_result[0] == "daemon"
    assert local_result[0] == "local"


def test_models_package_exports_factory_helpers(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ctxsift.models.factory.create_compression_backend",
        lambda *args, **kwargs: ("compression", args, kwargs),
    )
    monkeypatch.setattr(
        "ctxsift.models.factory.create_local_backend",
        lambda *args, **kwargs: ("local", args, kwargs),
    )

    compression_result = models_package.create_compression_backend("config")
    local_result = models_package.create_local_backend("config")

    assert compression_result[0] == "compression"
    assert local_result[0] == "local"


def test_models_package_lazy_getattr_imports_and_caches_module(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    imported_module = ModuleType("ctxsift.models.fake")
    monkeypatch.setattr(models_package, "import_module", lambda module_path: imported_module)

    module = models_package.__getattr__("hf_hub_cache")

    assert module is imported_module
    assert models_package.hf_hub_cache is imported_module


def test_models_package_lazy_getattr_rejects_unknown_attribute() -> None:
    with pytest.raises(AttributeError, match="has no attribute 'missing'"):
        models_package.__getattr__("missing")


def test_build_record_embedding_text_includes_optional_sections() -> None:
    text = build_record_embedding_text(
        StoredRecord(
            instruction="Summarize failures",
            normalized_instruction="summarize failures",
            compressed_output="AuthError in src/app.py",
            raw_input_hash="abc",
            mode="pipe",
            command="uv run pytest",
        ),
        referenced_files=[ReferencedFileRecord(path="src/app.py", exists_at_capture=True)],
        extracted_terms=[ExtractedTermRecord(term="AuthError")],
    )

    assert "Instruction: Summarize failures" in text
    assert "Command: uv run pytest" in text
    assert "Files: src/app.py" in text
    assert "Terms: AuthError" in text


def test_build_record_embedding_text_omits_empty_optional_sections() -> None:
    text = build_record_embedding_text(
        StoredRecord(
            instruction="Summarize failures",
            normalized_instruction="summarize failures",
            compressed_output="AuthError in src/app.py",
            raw_input_hash="abc",
            mode="pipe",
        ),
        referenced_files=[],
        extracted_terms=[],
    )

    assert text == "Instruction: Summarize failures\nSummary: AuthError in src/app.py"
