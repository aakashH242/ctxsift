"""Tests for the Transformers Gemma backend and prompt builder."""

import asyncio
from types import SimpleNamespace
from typing import Any, cast

import pytest

from ctxsift.compression_prompt import build_messages
from ctxsift.models.base import BackendUnavailableError, ModelCompressionInput
from ctxsift.models.transformers_gemma import (
    TransformersGemmaBackend,
    _normalize_generated_text,
    _resolve_device,
    _runtime_input_device,
)
from ctxsift.models.transformers_quantization import build_transformers_load_options
from ctxsift.types import ExtractedSignal, LocalModelConfig


class FakeInputs(dict):
    """Small tensor container that tracks device transfer calls."""

    def to(self, device: Any) -> "FakeInputs":
        self["device"] = device
        return self


class FakeTokenizer:
    """Text-only tokenizer stub."""

    def __init__(self) -> None:
        self.last_messages: list[dict[str, str]] | None = None

    def apply_chat_template(self, messages, tokenize, add_generation_prompt, enable_thinking=False):
        self.last_messages = messages
        return "templated prompt"

    def __call__(self, text: str, return_tensors: str) -> FakeInputs:
        return FakeInputs({"input_ids": [[1, 2, 3]], "text": text, "return_tensors": return_tensors})

    def decode(self, tokens, skip_special_tokens: bool) -> str:
        return "Model answer"

class FakeModel:
    """Generation model stub."""

    def __init__(self) -> None:
        self.device = "cpu"
        self.hf_device_map: dict[str, str] | None = None
        self.to_device: str | None = None
        self.generate_calls: list[dict[str, Any]] = []
        self.eval_called = False

    def to(self, device: str) -> None:
        self.device = device
        self.to_device = device

    def eval(self) -> None:
        self.eval_called = True

    def generate(self, **kwargs):
        self.generate_calls.append(kwargs)
        return [[1, 2, 3, 4]]


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
    user_text = cast(str, cast(list[dict[str, Any]], messages[1]["content"])[0]["text"])

    assert "src/auth.py" in user_text
    assert "src/auth.py:9 in login" in user_text
    assert "AuthError" in user_text
    assert "pytest" in user_text


def test_resolve_device_forces_cpu_when_cuda_unavailable() -> None:
    torch_module = SimpleNamespace(cuda=SimpleNamespace(is_available=lambda: False))

    resolved = _resolve_device("cuda", torch_module)

    assert resolved.torch_device == "cpu"
    assert resolved.label == "cpu"


def test_transformers_backend_uses_text_runtime_async(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}
    fake_model = FakeModel()
    fake_tokenizer = FakeTokenizer()

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            captured["model_name"] = model_name
            captured["model_kwargs"] = kwargs
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            captured["tokenizer_name"] = model_name
            captured["tokenizer_kwargs"] = kwargs
            return fake_tokenizer

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: False),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_transformers_components",
        lambda: (FakeAutoModel, FakeAutoTokenizer),
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
    assert captured["model_name"] == "google/gemma-4-E2B-it"
    assert captured["model_kwargs"]["dtype"] == "auto"
    assert captured["tokenizer_kwargs"]["padding_side"] == "left"
    assert fake_model.to_device == "cpu"
    assert fake_model.eval_called is True
    assert fake_model.generate_calls[0]["max_new_tokens"] == 128
    assert "AuthError" in fake_tokenizer.last_messages[1]["content"]


def test_transformers_backend_enables_flash_attention_on_gpu_when_available(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            captured["model_kwargs"] = kwargs
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeTokenizer()

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: True),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_transformers_components",
        lambda: (FakeAutoModel, FakeAutoTokenizer),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_torch_module",
        lambda: fake_torch,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.gemma_attention_choice",
        lambda device_label, configured_value: "flash_attention_2",
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
    assert captured["model_kwargs"]["attn_implementation"] == "flash_attention_2"


def test_transformers_backend_falls_back_when_flash_attention_init_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    attempts: list[dict[str, Any]] = []

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            attempts.append(kwargs)
            if "attn_implementation" in kwargs:
                raise RuntimeError("flash attention unavailable")
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeTokenizer()

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: True),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_transformers_components",
        lambda: (FakeAutoModel, FakeAutoTokenizer),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_torch_module",
        lambda: fake_torch,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.gemma_attention_choice",
        lambda device_label, configured_value: "flash_attention_2",
    )
    backend = TransformersGemmaBackend(LocalModelConfig(model="google/gemma-4-E2B-it", device="cuda"))
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="AuthError: login failed",
        extracted_signal=ExtractedSignal(symbols=["AuthError"]),
        max_output_tokens=128,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert attempts[0]["attn_implementation"] == "flash_attention_2"
    assert "attn_implementation" not in attempts[1]


def test_transformers_backend_uses_bitsandbytes_quantization_without_model_move(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}
    fake_model = FakeModel()

    class FakeBitsAndBytesConfig:
        def __init__(self, **kwargs) -> None:
            self.kwargs = kwargs

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            captured["model_name"] = model_name
            captured["model_kwargs"] = kwargs
            fake_model.device = kwargs["device_map"]
            fake_model.hf_device_map = {"": kwargs["device_map"]}
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeTokenizer()

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: True),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_transformers_components",
        lambda: (FakeAutoModel, FakeAutoTokenizer),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_torch_module",
        lambda: fake_torch,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._load_bitsandbytes_config_class",
        lambda: FakeBitsAndBytesConfig,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._require_module",
        lambda module_name, message: None,
    )
    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cuda",
            dtype="bfloat16",
            quantization="bnb-4bit-nf4",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="AuthError: login failed",
        extracted_signal=ExtractedSignal(symbols=["AuthError"]),
        max_output_tokens=128,
    )

    result = asyncio.run(backend.compress(request))

    quantization_config = captured["model_kwargs"]["quantization_config"]
    assert result == "Model answer"
    assert backend.cache_model_id == "google/gemma-4-E2B-it[bnb-4bit-nf4]"
    assert captured["model_kwargs"]["device_map"] == "cuda:0"
    assert quantization_config.kwargs["load_in_4bit"] is True
    assert quantization_config.kwargs["bnb_4bit_quant_type"] == "nf4"
    assert quantization_config.kwargs["bnb_4bit_compute_dtype"] == "bfloat16"
    assert fake_model.to_device is None


def test_transformers_backend_uses_quanto_quantization_without_model_move(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}
    fake_model = FakeModel()

    class FakeQuantoConfig:
        def __init__(self, **kwargs) -> None:
            self.kwargs = kwargs

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            captured["model_kwargs"] = kwargs
            fake_model.device = kwargs["device_map"]
            fake_model.hf_device_map = {"": kwargs["device_map"]}
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeTokenizer()

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: False),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_transformers_components",
        lambda: (FakeAutoModel, FakeAutoTokenizer),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_torch_module",
        lambda: fake_torch,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._load_quanto_config_class",
        lambda: FakeQuantoConfig,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._module_available",
        lambda module_name: True,
    )
    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cpu",
            quantization="quanto-int8",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="AuthError: login failed",
        extracted_signal=ExtractedSignal(symbols=["AuthError"]),
        max_output_tokens=128,
    )

    result = asyncio.run(backend.compress(request))

    quantization_config = captured["model_kwargs"]["quantization_config"]
    assert result == "Model answer"
    assert captured["model_kwargs"]["device_map"] == "cpu"
    assert quantization_config.kwargs["weights"] == "int8"
    assert fake_model.to_device is None


def test_runtime_input_device_handles_integer_device_map_values() -> None:
    fake_model = FakeModel()
    fake_model.device = None
    fake_model.hf_device_map = {"": 0}

    assert _runtime_input_device(fake_model, "cpu") == "cuda:0"


def test_quanto_quantization_requires_accelerate(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._module_available",
        lambda module_name: module_name == "optimum.quanto",
    )

    with pytest.raises(BackendUnavailableError, match="accelerate"):
        build_transformers_load_options(
            config=LocalModelConfig(quantization="quanto-int4"),
            resolved_torch_device="cpu",
            torch_dtype="auto",
            attention_backend=None,
        )


def test_transformers_backend_fails_closed_when_quantization_dependency_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            raise AssertionError("full-precision fallback should not be attempted")

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeTokenizer()

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: False),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_transformers_components",
        lambda: (FakeAutoModel, FakeAutoTokenizer),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma._load_torch_module",
        lambda: fake_torch,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.gemma_attention_choice",
        lambda device_label, configured_value: "flash_attention_2",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._module_available",
        lambda module_name: False,
    )
    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cpu",
            quantization="bnb-8bit",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="AuthError: login failed",
        extracted_signal=ExtractedSignal(symbols=["AuthError"]),
        max_output_tokens=128,
    )

    with pytest.raises(BackendUnavailableError, match="bitsandbytes"):
        asyncio.run(backend.compress(request))


def test_normalize_generated_text_strips_short_edge_tags() -> None:
    assert _normalize_generated_text("<start_tag> concise summary <turn|>") == "concise summary"


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
