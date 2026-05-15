"""Tests for the Sentence Transformers embedding backend."""

import asyncio
from types import SimpleNamespace

import numpy as np
import pytest

from ctxsift.embeddings.base import DEFAULT_RECALL_QUERY_PROMPT, QueryEmbeddingRequest
from ctxsift.embeddings.sentence_transformers_backend import SentenceTransformersBackend
from ctxsift.types import EmbeddingConfig


class FakeSentenceTransformerModel:
    """Minimal fake model for prompt-behavior tests."""

    def __init__(self) -> None:
        self.query_calls: list[tuple[str, dict]] = []
        self.document_calls: list[tuple[list[str], dict]] = []
        self.max_seq_length = 0

    def get_sentence_embedding_dimension(self) -> int:
        return 3

    def encode_query(self, text: str, **kwargs):
        self.query_calls.append((text, kwargs))
        return np.array([1.0, 2.0, 3.0], dtype=np.float32)

    def encode_document(self, texts: list[str], **kwargs):
        self.document_calls.append((texts, kwargs))
        return np.array([[1.0, 2.0, 3.0]], dtype=np.float32)


def test_embedding_backend_uses_custom_default_prompt_for_harrier() -> None:
    model = FakeSentenceTransformerModel()
    backend = SentenceTransformersBackend(EmbeddingConfig(model="microsoft/harrier-oss-v1-0.6b"))
    backend._model = model

    result = asyncio.run(
        backend.embed_query(QueryEmbeddingRequest(text="AuthError in login", max_length=1024))
    )

    assert result == [1.0, 2.0, 3.0]
    assert model.query_calls[0][1]["prompt"] == DEFAULT_RECALL_QUERY_PROMPT
    assert "prompt_name" not in model.query_calls[0][1]


def test_embedding_backend_prefers_explicit_prompt_name_override() -> None:
    model = FakeSentenceTransformerModel()
    backend = SentenceTransformersBackend(
        EmbeddingConfig(
            model="microsoft/harrier-oss-v1-0.6b",
            query_prompt_name="my_query_prompt",
            query_prompt="Instruct: ignored\nQuery: ",
        )
    )
    backend._model = model

    asyncio.run(backend.embed_query(QueryEmbeddingRequest(text="BillingError", max_length=1024)))

    assert model.query_calls[0][1]["prompt_name"] == "my_query_prompt"
    assert "prompt" not in model.query_calls[0][1]


def test_embedding_backend_skips_default_prompt_for_non_harrier_models() -> None:
    model = FakeSentenceTransformerModel()
    backend = SentenceTransformersBackend(EmbeddingConfig(model="sentence-transformers/all-MiniLM-L6-v2"))
    backend._model = model

    asyncio.run(backend.embed_query(QueryEmbeddingRequest(text="plain query", max_length=256)))

    assert "prompt" not in model.query_calls[0][1]
    assert "prompt_name" not in model.query_calls[0][1]


def test_embedding_backend_forces_cpu_when_cuda_unavailable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("ctxsift.embeddings.sentence_transformers_backend.torch", SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: False),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    ))
    backend = SentenceTransformersBackend(
        EmbeddingConfig(
            model="microsoft/harrier-oss-v1-0.6b",
            device="cuda:0",
        )
    )

    assert backend._resolved_device() == "cpu"


def test_embedding_backend_prefers_onnx_for_harrier_on_cpu_when_available(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    class FakeSentenceTransformer:
        def __init__(self, model_name, **kwargs):
            captured["model_name"] = model_name
            captured["kwargs"] = kwargs
            self.max_seq_length = 0

        def get_sentence_embedding_dimension(self) -> int:
            return 3

    backend = SentenceTransformersBackend(
        EmbeddingConfig(model="microsoft/harrier-oss-v1-0.6b", device="cpu")
    )
    monkeypatch.setattr(
        "ctxsift.embeddings.sentence_transformers_backend.embedding_backend_choice",
        lambda device, configured_value, model_name: "onnx",
    )

    model = backend._load_sentence_transformer(FakeSentenceTransformer)  # type: ignore[arg-type]

    assert model is not None
    assert captured["kwargs"]["backend"] == "onnx"
    assert captured["kwargs"]["model_kwargs"]["provider"] == "CPUExecutionProvider"


def test_embedding_backend_falls_back_to_torch_when_onnx_load_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    attempts: list[dict[str, object]] = []

    class FakeSentenceTransformer:
        def __init__(self, model_name, **kwargs):
            attempts.append(kwargs)
            if kwargs["backend"] == "onnx":
                raise RuntimeError("onnx export unavailable")
            self.max_seq_length = 0

        def get_sentence_embedding_dimension(self) -> int:
            return 3

    backend = SentenceTransformersBackend(
        EmbeddingConfig(model="microsoft/harrier-oss-v1-0.6b", device="cpu")
    )
    monkeypatch.setattr(
        "ctxsift.embeddings.sentence_transformers_backend.embedding_backend_choice",
        lambda device, configured_value, model_name: "onnx",
    )

    model = backend._load_sentence_transformer(FakeSentenceTransformer)  # type: ignore[arg-type]

    assert model is not None
    assert attempts[0]["backend"] == "onnx"
    assert attempts[1]["backend"] == "torch"


def test_embedding_backend_enables_flash_attention_on_gpu_torch_path(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    class FakeSentenceTransformer:
        def __init__(self, model_name, **kwargs):
            captured["kwargs"] = kwargs
            self.max_seq_length = 0

        def get_sentence_embedding_dimension(self) -> int:
            return 3

    monkeypatch.setattr("ctxsift.embeddings.sentence_transformers_backend.torch", SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: True),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    ))
    monkeypatch.setattr(
        "ctxsift.embeddings.sentence_transformers_backend.embedding_attention_choice",
        lambda device, configured_value: "flash_attention_2",
    )
    backend = SentenceTransformersBackend(
        EmbeddingConfig(model="microsoft/harrier-oss-v1-0.6b", device="cuda")
    )

    model = backend._load_sentence_transformer(FakeSentenceTransformer)  # type: ignore[arg-type]

    assert model is not None
    assert captured["kwargs"]["backend"] == "torch"
    assert captured["kwargs"]["model_kwargs"]["attn_implementation"] == "flash_attention_2"
