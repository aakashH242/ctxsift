"""Tests for the LiteLLM remote compression backend."""

import asyncio
import logging
from types import SimpleNamespace

import pytest

from ctxsift.compression.intent import CompressionIntent
from ctxsift.models.base import BackendUnavailableError, ModelCompressionInput, RemoteBackendOptions
from ctxsift.models.litellm_remote import (
    LiteLLMRemoteBackend,
    _LiteLLMLoggingWorkerErrorFilter,
    _configure_litellm_runtime,
    _reasoning_effort,
)
from ctxsift.types import ExtractedSignal


def test_litellm_remote_backend_uses_async_completion(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    async def fake_acompletion(**kwargs):
        captured.update(kwargs)
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="Remote summary"))]
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
                intent=CompressionIntent.SUMMARY,
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
                    intent=CompressionIntent.SUMMARY,
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
                    intent=CompressionIntent.SUMMARY,
                    instruction="Summarize",
                    raw_input="text",
                    extracted_signal=ExtractedSignal(),
                    max_output_tokens=32,
                )
            )
        )


@pytest.mark.parametrize(
    ("model_name", "expected"),
    [
        ("o3-mini", "medium"),
        ("openai/gpt-5-mini", "medium"),
        ("openrouter/openai/gpt-5.1-codex", "medium"),
        ("novita/deepseek/deepseek-r1", "medium"),
        ("gemini-2.5-pro", "medium"),
        ("claude-sonnet-4-20250514", "medium"),
        ("gpt-5-chat", None),
        ("gpt-5-instant", None),
        ("gpt-4o-mini", None),
        ("deepseek-chat", None),
        ("claude-3-5-haiku-20241022", None),
    ],
)
def test_reasoning_effort_auto_detects_reasoning_model_families(
    model_name: str,
    expected: str | None,
) -> None:
    assert _reasoning_effort("auto", model_name) == expected


def test_reasoning_effort_true_and_false_override_model_detection() -> None:
    assert _reasoning_effort("true", "gpt-4o-mini") == "medium"
    assert _reasoning_effort("false", "o3-mini") == "none"


def test_litellm_runtime_configuration_suppresses_logging_worker_noise() -> None:
    logger = logging.getLogger("LiteLLM")
    original_filters = list(logger.filters)
    original_marker = getattr(logger, "_ctxsift_logging_worker_filter_installed", None)
    if original_marker is not None:
        delattr(logger, "_ctxsift_logging_worker_filter_installed")
    logger.filters = []
    try:
        fake_litellm = SimpleNamespace(suppress_debug_info=False)
        _configure_litellm_runtime(fake_litellm)

        assert fake_litellm.suppress_debug_info is True
        assert len(logger.filters) == 1
        assert isinstance(logger.filters[0], _LiteLLMLoggingWorkerErrorFilter)

        record = logging.LogRecord(
            name="LiteLLM",
            level=logging.ERROR,
            pathname="logging_worker.py",
            lineno=103,
            msg="LoggingWorker error: %s",
            args=(TimeoutError(),),
            exc_info=None,
        )
        assert logger.filters[0].filter(record) is False

        normal_record = logging.LogRecord(
            name="LiteLLM",
            level=logging.ERROR,
            pathname="litellm_remote.py",
            lineno=1,
            msg="Remote backend request failed",
            args=(),
            exc_info=None,
        )
        assert logger.filters[0].filter(normal_record) is True

        _configure_litellm_runtime(fake_litellm)
        assert len(logger.filters) == 1
    finally:
        logger.filters = original_filters
        if original_marker is None:
            if hasattr(logger, "_ctxsift_logging_worker_filter_installed"):
                delattr(logger, "_ctxsift_logging_worker_filter_installed")
        else:
            setattr(logger, "_ctxsift_logging_worker_filter_installed", original_marker)
