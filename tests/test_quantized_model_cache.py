"""Tests for persisted quantized model cache helpers."""

from pathlib import Path

import pytest

from ctxsift.models.quantized_model_cache import (
    QuantizedModelCache,
    has_persisted_quantized_model,
    persist_quantized_model_cache,
    resolve_quantized_model_cache,
)
from ctxsift.types import LocalModelConfig, LocalQuantizationMode


def test_resolve_quantized_model_cache_uses_home_cache_fallback(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.quantized_model_cache._env_cache_base",
        lambda: None,
    )
    monkeypatch.setattr(
        "ctxsift.models.quantized_model_cache._huggingface_cache_base",
        lambda: None,
    )
    monkeypatch.setattr(
        "ctxsift.models.quantized_model_cache._home_cache_base",
        lambda: tmp_path / ".cache",
    )

    cache = resolve_quantized_model_cache(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cuda",
            gguf_filename=None,
            quantization=LocalQuantizationMode.BNB_8BIT,
        ),
        "google/gemma-4-E2B-it",
    )

    assert cache is not None
    assert cache.root_dir == tmp_path / ".cache" / "model_quants" / "model" / "files"


def test_has_persisted_quantized_model_requires_tokenizer_artifacts(tmp_path: Path) -> None:
    cache_dir = tmp_path / "quantized"
    cache_dir.mkdir(parents=True)
    cache = QuantizedModelCache(
        root_dir=tmp_path,
        model_dir=cache_dir,
        metadata_path=cache_dir / "ctxsift-quantized-model.json",
    )
    cache.metadata_path.write_text("{}", encoding="utf-8")
    (cache_dir / "config.json").write_text("{}", encoding="utf-8")

    assert has_persisted_quantized_model(cache) is False

    (cache_dir / "tokenizer_config.json").write_text("{}", encoding="utf-8")

    assert has_persisted_quantized_model(cache) is True


def test_persist_quantized_model_cache_skips_nonserializable_quantizers(tmp_path: Path) -> None:
    cache_dir = tmp_path / "quantized"
    cache = QuantizedModelCache(
        root_dir=tmp_path,
        model_dir=cache_dir,
        metadata_path=cache_dir / "ctxsift-quantized-model.json",
    )

    class FakeQuantizer:
        def is_serializable(self) -> bool:
            return False

    class FakeModel:
        hf_quantizer = FakeQuantizer()

        def save_pretrained(self, save_directory: Path) -> None:
            raise AssertionError("non-serializable quantized model should not be saved")

    class FakeTokenizer:
        def save_pretrained(self, save_directory: Path) -> None:
            raise AssertionError("tokenizer save should be skipped with model persistence")

    persist_quantized_model_cache(
        cache,
        model=FakeModel(),
        tokenizer=FakeTokenizer(),
        model_name="Qwen/Qwen2.5-0.5B-Instruct",
        config=LocalModelConfig(
            device="cuda",
            gguf_filename=None,
            quantization=LocalQuantizationMode.BNB_8BIT,
        ),
    )

    assert cache.model_dir.exists() is False
    assert cache.metadata_path.exists() is False
