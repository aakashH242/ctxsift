"""Tests for the Transformers Gemma backend and prompt builder."""

import asyncio
from types import SimpleNamespace

import pytest

from ctxsift.compression_prompt import build_messages
from ctxsift.models.base import BackendUnavailableError, ModelCompressionInput
from ctxsift.models.transformers_gemma import TransformersGemmaBackend, _resolve_device
from ctxsift.types import ExtractedSignal, LocalModelConfig


def test_build_messages_preserves_exact_signal_values() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input='File "src/auth.py", line 9, in login\nAuthError: login failed',
        extracted_signal=ExtractedSignal(
            referenced_files=["src/auth.py"],
            traceback_frames=["src/auth.py:9 in login"],
            symbols=["AuthError"],
            command_terms=["pytest"],
            error_lines=["AuthError: login failed"],
        ),
        max_output_tokens=128,
    )

    messages = build_messages(request)
    user_text = messages[1]["content"][0]["text"]

    assert "src/auth.py" in user_text
    assert "src/auth.py:9 in login" in user_text
    assert "AuthError" in user_text
    assert "pytest" in user_text


def test_resolve_device_forces_cpu_when_cuda_unavailable() -> None:
    torch_module = SimpleNamespace(cuda=SimpleNamespace(is_available=lambda: False))

    resolved = _resolve_device("cuda", torch_module)

    assert resolved.pipeline_device == -1
    assert resolved.label == "cpu"


def test_transformers_backend_uses_pipeline_async(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    def fake_pipeline(**kwargs):
        captured["init"] = kwargs

        def run(messages, return_full_text, generate_kwargs):
            captured["messages"] = messages
            captured["return_full_text"] = return_full_text
            captured["generate_kwargs"] = generate_kwargs
            return [{"generated_text": "Model answer"}]

        return run

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: False),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_transformers_pipeline",
        lambda: fake_pipeline,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_torch_module",
        lambda: fake_torch,
    )
    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cuda",
            dtype="auto",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="AuthError: login failed",
        extracted_signal=ExtractedSignal(symbols=["AuthError"]),
        max_output_tokens=128,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert captured["init"]["task"] == "any-to-any"
    assert captured["init"]["device"] == -1
    assert captured["init"]["torch_dtype"] == "auto"
    assert captured["return_full_text"] is False
    assert captured["generate_kwargs"] == {"max_new_tokens": 128}
    assert "AuthError" in captured["messages"][1]["content"][0]["text"]


def test_transformers_backend_rejects_unknown_dtype(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_torch = SimpleNamespace(cuda=SimpleNamespace(is_available=lambda: False))
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_torch_module",
        lambda: fake_torch,
    )
    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            dtype="not-a-dtype",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="AuthError: login failed",
        extracted_signal=ExtractedSignal(symbols=["AuthError"]),
        max_output_tokens=128,
    )

    with pytest.raises(BackendUnavailableError):
        asyncio.run(backend.compress(request))
