"""Tests for daemon runtime signatures and sharing keys."""

import pytest

from ctxsift.daemon.signatures import (
    build_compression_signature,
    build_embedding_signature,
    signature_hash,
)
from ctxsift.types import EmbeddingConfig, LocalModelConfig


def test_identical_local_configs_share_one_compression_signature() -> None:
    first = build_compression_signature(LocalModelConfig())
    second = build_compression_signature(LocalModelConfig())

    assert first == second
    assert signature_hash(first) == signature_hash(second)


def test_changed_local_runtime_config_changes_compression_signature(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base = build_compression_signature(LocalModelConfig())
    monkeypatch.setattr(
        "ctxsift.daemon.signatures.resolve_local_runtime",
        lambda config: type(
            "RuntimeSelection",
            (),
            {
                "uses_llama_cpp": False,
                "resolved_device": type("ResolvedDevice", (), {"label": "cuda:0"})(),
                "provider_name": "transformers",
            },
        )(),
    )
    gpu = build_compression_signature(
        LocalModelConfig(
            model="Qwen/Qwen3.5-0.8B",
            device="cuda",
            quantization="bnb-8bit",
            gguf_filename=None,
        )
    )

    assert signature_hash(base) != signature_hash(gpu)


def test_changed_cpu_gguf_identity_changes_compression_signature() -> None:
    base = build_compression_signature(LocalModelConfig())
    changed = build_compression_signature(
        LocalModelConfig(gguf_filename="smollm2-360m-instruct-q4_k_m.gguf")
    )

    assert signature_hash(base) != signature_hash(changed)


def test_identical_embedding_configs_share_one_embedding_signature() -> None:
    first = build_embedding_signature(EmbeddingConfig())
    second = build_embedding_signature(EmbeddingConfig())

    assert first == second
    assert signature_hash(first) == signature_hash(second)


def test_embedding_prompt_changes_change_embedding_signature() -> None:
    base = build_embedding_signature(EmbeddingConfig())
    custom = build_embedding_signature(
        EmbeddingConfig(query_prompt="Instruct: retrieve fixes\nQuery: ")
    )

    assert signature_hash(base) != signature_hash(custom)
