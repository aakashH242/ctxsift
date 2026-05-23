"""Tests for compression backend factory selection."""

import importlib
import sys

import pytest

from ctxsift.models.base import BackendUnavailableError
from ctxsift.models.daemon_backend import DaemonCompressionBackend
from ctxsift.models.factory import create_compression_backend
from ctxsift.models.llama_cpp_backend import LlamaCppBackend
from ctxsift.models.litellm_remote import LiteLLMRemoteBackend
from ctxsift.models.transformers_backend import TransformersTextBackend
from ctxsift.types import AppConfig


def test_factory_prefers_litellm_when_base_url_is_set() -> None:
    backend = create_compression_backend(
        AppConfig.model_validate(
            {
                "remote": {
                    "base_url": "http://localhost:4000",
                    "model_name": "gpt-5-mini",
                }
            }
        )
    )

    assert isinstance(backend, LiteLLMRemoteBackend)


def test_factory_uses_local_backend_when_remote_base_url_is_empty() -> None:
    backend = create_compression_backend(AppConfig())

    assert isinstance(backend, DaemonCompressionBackend)


def test_factory_uses_in_process_local_backend_when_daemon_is_disabled() -> None:
    backend = create_compression_backend(AppConfig.model_validate({"daemon": {"enabled": False}}))

    assert isinstance(backend, LlamaCppBackend)


def test_factory_uses_transformers_for_local_gpu_runtime_when_daemon_is_disabled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.factory.resolve_local_runtime",
        lambda config: type(
            "RuntimeSelection",
            (),
            {"uses_llama_cpp": False, "uses_transformers": True},
        )(),
    )
    backend = create_compression_backend(
        AppConfig.model_validate({"daemon": {"enabled": False}, "local": {"device": "cuda"}})
    )

    assert isinstance(backend, TransformersTextBackend)


def test_factory_rejects_remote_base_url_without_model_name() -> None:
    with pytest.raises(BackendUnavailableError):
        create_compression_backend(
            AppConfig.model_validate(
                {
                    "remote": {
                        "base_url": "http://localhost:4000",
                        "model_name": "",
                    }
                }
            )
        )


def test_importing_model_factory_does_not_hit_embedding_daemon_cycle() -> None:
    modules_to_clear = [
        "ctxsift.models",
        "ctxsift.models.factory",
        "ctxsift.models.daemon_backend",
        "ctxsift.daemon.client",
        "ctxsift.daemon.types",
        "ctxsift.embeddings",
        "ctxsift.embeddings.base",
        "ctxsift.embeddings.factory",
        "ctxsift.embeddings.daemon_backend",
    ]
    for module_name in modules_to_clear:
        sys.modules.pop(module_name, None)

    module = importlib.import_module("ctxsift.models.factory")

    assert hasattr(module, "create_local_backend")
    assert hasattr(module, "create_compression_backend")
