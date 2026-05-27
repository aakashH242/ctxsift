"""Tests for guided model preloading."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import types

import pytest

import ctxsift.model_preload as model_preload
from ctxsift.models import hf_hub_cache
from ctxsift.models.base import BackendUnavailableError
from ctxsift.types import AppConfig
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError


class FakeEmbeddingBackend:
    async def preload(self) -> None:
        return None


class FakeLocalBackend:
    async def preload(self) -> None:
        return None


def test_preload_configured_models_warms_embedding_and_downloads_cpu_gguf(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured_show_progress: list[bool] = []

    def fake_preload_gguf_artifact(
        config: AppConfig,
        *,
        show_progress: bool = False,
    ) -> Path:
        del config
        captured_show_progress.append(show_progress)
        return Path("D:/cache/smollm2-360m-instruct-q8_0.gguf")

    monkeypatch.setattr(
        model_preload, "create_embedding_backend", lambda config: FakeEmbeddingBackend()
    )
    monkeypatch.setattr(
        model_preload,
        "preload_gguf_artifact",
        fake_preload_gguf_artifact,
    )

    results = asyncio.run(model_preload.preload_configured_models(AppConfig()))

    assert len(results) == 2
    assert all(result.ok for result in results)
    assert "embedding model microsoft/harrier-oss-v1-0.6b" in results[0].detail
    assert "local compression model ibm-granite/granite-4.0-350m-GGUF" in results[1].detail
    assert "smollm2-360m-instruct-q8_0.gguf" in results[1].detail
    assert captured_show_progress == [True]


def test_preload_configured_models_skips_local_model_in_remote_mode(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        model_preload, "create_embedding_backend", lambda config: FakeEmbeddingBackend()
    )
    monkeypatch.setattr(model_preload, "create_local_backend", lambda config: FakeLocalBackend())

    config = AppConfig.model_validate(
        {
            "remote": {
                "base_url": "http://localhost:4000",
                "model_name": "gpt-4o-mini",
            }
        }
    )
    results = asyncio.run(model_preload.preload_configured_models(config))

    assert len(results) == 1
    assert "embedding model" in results[0].detail


def test_preload_configured_models_returns_warning_results_on_failures(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class BrokenEmbeddingBackend:
        async def preload(self) -> None:
            raise EmbeddingBackendUnavailableError("embedding failed")

    class BrokenLocalBackend:
        async def preload(self) -> None:
            raise BackendUnavailableError("local failed")

    monkeypatch.setattr(
        model_preload,
        "create_embedding_backend",
        lambda config: BrokenEmbeddingBackend(),
    )
    monkeypatch.setattr(
        model_preload,
        "preload_gguf_artifact",
        lambda config, *, show_progress=False: (_ for _ in ()).throw(
            BackendUnavailableError("local failed")
        ),
    )

    results = asyncio.run(model_preload.preload_configured_models(AppConfig()))

    assert len(results) == 2
    assert results[0].ok is False
    assert results[1].ok is False
    assert "embedding failed" in results[0].detail
    assert "local failed" in results[1].detail


def test_preload_configured_models_uses_transformers_path_for_local_gpu(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        model_preload, "create_embedding_backend", lambda config: FakeEmbeddingBackend()
    )
    monkeypatch.setattr(model_preload, "create_local_backend", lambda config: FakeLocalBackend())
    monkeypatch.setattr(
        model_preload,
        "resolve_local_runtime",
        lambda config: type(
            "RuntimeSelection",
            (),
            {"uses_llama_cpp": False},
        )(),
    )

    results = asyncio.run(
        model_preload.preload_configured_models(
            AppConfig.model_validate(
                {"local": {"device": "cuda", "model": "Qwen/Qwen3.5-0.8B", "gguf_filename": None}}
            )
        )
    )

    assert len(results) == 2
    assert all(result.ok for result in results)
    assert results[1].detail == "Preloaded local compression model Qwen/Qwen3.5-0.8B."


def test_resolve_or_download_hf_file_prefers_cached_artifact(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cached_file = tmp_path / "cached.gguf"
    cached_file.write_text("cached", encoding="utf-8")

    calls: list[tuple[str, str, str | None]] = []

    hub_module = types.ModuleType("huggingface_hub")
    setattr(
        hub_module, "try_to_load_from_cache", lambda repo_id, filename, cache_dir=None: cached_file
    )

    def fake_hf_hub_download(*, repo_id: str, filename: str, cache_dir: str | None = None) -> str:
        calls.append((repo_id, filename, cache_dir))
        return str(tmp_path / "downloaded.gguf")

    setattr(hub_module, "hf_hub_download", fake_hf_hub_download)

    constants_module = types.ModuleType("huggingface_hub.constants")
    setattr(constants_module, "_CACHED_NO_EXIST", object())

    monkeypatch.setitem(sys.modules, "huggingface_hub", hub_module)
    monkeypatch.setitem(sys.modules, "huggingface_hub.constants", constants_module)

    resolved = hf_hub_cache.resolve_or_download_hf_file(
        repo_id="ibm-granite/granite-4.0-350m-GGUF",
        filename="smollm2-360m-instruct-q8_0.gguf",
        cache_dir=None,
    )

    assert resolved == cached_file
    assert calls == []


def test_resolve_or_download_hf_file_can_use_snapshot_download_with_progress(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    snapshot_dir = tmp_path / "snapshot"
    snapshot_dir.mkdir(parents=True)
    downloaded_file = snapshot_dir / "model.gguf"
    downloaded_file.write_text("downloaded", encoding="utf-8")

    hub_module = types.ModuleType("huggingface_hub")
    setattr(hub_module, "try_to_load_from_cache", lambda repo_id, filename, cache_dir=None: None)
    setattr(
        hub_module,
        "snapshot_download",
        lambda **kwargs: str(snapshot_dir),
    )
    setattr(
        hub_module,
        "hf_hub_download",
        lambda **kwargs: (_ for _ in ()).throw(AssertionError("hf_hub_download should not run")),
    )

    utils_module = types.ModuleType("huggingface_hub.utils")
    progress_calls: list[str] = []
    setattr(utils_module, "enable_progress_bars", lambda: progress_calls.append("enabled"))

    monkeypatch.setitem(sys.modules, "huggingface_hub", hub_module)
    monkeypatch.setitem(sys.modules, "huggingface_hub.utils", utils_module)

    resolved = hf_hub_cache.resolve_or_download_hf_file(
        repo_id="repo/model",
        filename="model.gguf",
        cache_dir=None,
        show_progress=True,
    )

    assert resolved == downloaded_file
    assert progress_calls == ["enabled"]
