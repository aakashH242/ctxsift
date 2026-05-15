"""Tests for compression backend factory selection."""

import pytest

from ctxsift.models.base import BackendUnavailableError
from ctxsift.models.factory import create_compression_backend
from ctxsift.models.litellm_remote import LiteLLMRemoteBackend
from ctxsift.models.transformers_gemma import TransformersGemmaBackend
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

    assert isinstance(backend, TransformersGemmaBackend)


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
