"""Tests for the LiteLLM remote compression backend."""

import asyncio
from types import SimpleNamespace

import pytest

from ctxsift.models.base import BackendUnavailableError, ModelCompressionInput, RemoteBackendOptions
from ctxsift.models.litellm_remote import LiteLLMRemoteBackend
from ctxsift.types import ExtractedSignal


def test_litellm_remote_backend_uses_async_completion(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    async def fake_acompletion(**kwargs):
        captured.update(kwargs)
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content="Remote summary"
                    )
                )
            ]
        )

    monkeypatch.setattr(
        "ctxsift.models.litellm_remote._load_litellm_acompletion",
        lambda: fake_acompletion,
    )
    backend = LiteLLMRemoteBackend(
        RemoteBackendOptions(
            base_url="http://localhost:4000",
            api_key="sk-test",
            api_version="2025-01-01",
            model_name="gpt-5-mini",
            reasoning_mode="true",
            timeout_ms=45000,
            retries=2,
        )
    )

    result = asyncio.run(
        backend.compress(
            ModelCompressionInput(
                instruction="Summarize failures",
                raw_input="AuthError: login failed",
                extracted_signal=ExtractedSignal(symbols=["AuthError"]),
                max_output_tokens=128,
            )
        )
    )

    assert result == "Remote summary"
    assert captured["model"] == "gpt-5-mini"
    assert captured["api_base"] == "http://localhost:4000"
    assert captured["api_key"] == "sk-test"
    assert captured["api_version"] == "2025-01-01"
    assert captured["timeout"] == 45
    assert captured["num_retries"] == 2
    assert captured["reasoning_effort"] == "medium"
    assert captured["max_tokens"] == 128


def test_litellm_remote_backend_rejects_empty_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def fake_acompletion(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=""))])

    monkeypatch.setattr(
        "ctxsift.models.litellm_remote._load_litellm_acompletion",
        lambda: fake_acompletion,
    )
    backend = LiteLLMRemoteBackend(
        RemoteBackendOptions(
            base_url="http://localhost:4000",
            api_key="",
            api_version="",
            model_name="gpt-5-mini",
            reasoning_mode="auto",
            timeout_ms=1000,
            retries=0,
        )
    )

    with pytest.raises(BackendUnavailableError):
        asyncio.run(
            backend.compress(
                ModelCompressionInput(
                    instruction="Summarize",
                    raw_input="text",
                    extracted_signal=ExtractedSignal(),
                    max_output_tokens=32,
                )
            )
        )


def test_litellm_remote_backend_wraps_provider_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def fake_acompletion(**kwargs):
        raise RuntimeError("401 invalid key")

    monkeypatch.setattr(
        "ctxsift.models.litellm_remote._load_litellm_acompletion",
        lambda: fake_acompletion,
    )
    backend = LiteLLMRemoteBackend(
        RemoteBackendOptions(
            base_url="http://localhost:4000",
            api_key="sk-test",
            api_version="",
            model_name="gpt-5-mini",
            reasoning_mode="auto",
            timeout_ms=1000,
            retries=0,
        )
    )

    with pytest.raises(BackendUnavailableError, match="LiteLLM remote backend request failed"):
        asyncio.run(
            backend.compress(
                ModelCompressionInput(
                    instruction="Summarize",
                    raw_input="text",
                    extracted_signal=ExtractedSignal(),
                    max_output_tokens=32,
                )
            )
        )
