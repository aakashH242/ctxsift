"""Tests for the local Transformers text backend and profile behavior."""

import asyncio
import inspect
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from ctxsift.models.base import (
    BackendUnavailableError,
    ModelCompressionInput,
    ModelOutputRejectedError,
)
from ctxsift.models.gemma_profile import (
    build_text_messages,
    generation_kwargs,
    matches_model_name,
    normalize_output,
)
from ctxsift.models.qwen25_profile import (
    build_text_messages as build_qwen25_messages,
    is_valid_output as is_valid_qwen25_output,
    matches_model_name as matches_qwen25_model_name,
    normalize_output as normalize_qwen25_output,
)
from ctxsift.models.qwen3_profile import (
    build_text_messages as build_qwen3_messages,
    is_valid_output as is_valid_qwen3_output,
    matches_model_name as matches_qwen3_model_name,
    normalize_output as normalize_qwen3_output,
)
from ctxsift.models.qwen35_profile import (
    build_text_messages as build_qwen35_messages,
    is_valid_output as is_valid_qwen35_output,
    matches_model_name as matches_qwen35_model_name,
    normalize_output as normalize_qwen35_output,
)
from ctxsift.models.granite_profile import (
    build_text_messages as build_granite_messages,
    is_valid_output as is_valid_granite_output,
    matches_model_name as matches_granite_model_name,
    normalize_output as normalize_granite_output,
)
from ctxsift.models.phi_profile import (
    build_text_messages as build_phi_messages,
    is_valid_output as is_valid_phi_output,
    matches_model_name as matches_phi_model_name,
    normalize_output as normalize_phi_output,
)
from ctxsift.models.smollm2_profile import (
    build_text_messages as build_smollm2_messages,
    is_valid_output as is_valid_smollm2_output,
    matches_model_name as matches_smollm2_model_name,
    normalize_output as normalize_smollm2_output,
)
from ctxsift.models.text_model_profiles import FALLBACK_PROFILE, resolve_text_model_profile
from ctxsift.models.text_profile_common import preserves_exact_anchors
from ctxsift.models.transformers_gemma import (
    TransformersGemmaBackend,
    TransformersTextBackend,
    _apply_text_chat_template,
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
        self.last_template_kwargs: dict[str, Any] | None = None
        self.pad_token_id = 0
        self.eos_token_id = 2

    def apply_chat_template(self, messages, tokenize, add_generation_prompt, enable_thinking=False):
        self.last_messages = messages
        self.last_template_kwargs = {
            "tokenize": tokenize,
            "add_generation_prompt": add_generation_prompt,
            "enable_thinking": enable_thinking,
        }
        return "templated prompt"

    def __call__(self, text: str, return_tensors: str) -> FakeInputs:
        return FakeInputs({"input_ids": [[1, 2, 3]], "text": text, "return_tensors": return_tensors})

    def decode(self, tokens, skip_special_tokens: bool) -> str:
        return "Model answer"


class FakeGraniteTokenizer:
    """Tokenizer stub with Granite-style thinking control."""

    def __init__(self) -> None:
        self.last_messages: list[dict[str, str]] | None = None
        self.last_template_kwargs: dict[str, Any] | None = None
        self.pad_token_id = 0
        self.eos_token_id = 2

    def apply_chat_template(self, messages, tokenize, add_generation_prompt, thinking=False):
        self.last_messages = messages
        self.last_template_kwargs = {
            "tokenize": tokenize,
            "add_generation_prompt": add_generation_prompt,
            "thinking": thinking,
        }
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


def test_gemma_profile_builds_anchor_prompt() -> None:
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

    messages = build_text_messages(request)
    user_text = messages[1]["content"]

    assert "Preserve exactly:" in user_text
    assert "src/auth.py" in user_text
    assert "src/auth.py:9 in login" in user_text
    assert "AuthError" in user_text
    assert "pytest" in user_text
    assert "Raw output:" in user_text


def test_gemma_profile_generation_kwargs_are_deterministic() -> None:
    tokenizer = FakeTokenizer()

    kwargs = generation_kwargs(tokenizer, 128)

    assert kwargs == {
        "do_sample": False,
        "max_new_tokens": 128,
        "pad_token_id": 0,
        "eos_token_id": 2,
    }


def test_gemma_profile_matches_gemma_model_names() -> None:
    assert matches_model_name("google/gemma-4-E2B-it") is True
    assert matches_model_name("gemma-4-e2b-it") is True
    assert matches_model_name("Qwen/Qwen2.5-0.5B-Instruct") is False


def test_qwen25_profile_matches_qwen25_model_names() -> None:
    assert matches_qwen25_model_name("Qwen/Qwen2.5-1.5B-Instruct") is True
    assert matches_qwen25_model_name("qwen2.5-0.5b-instruct") is True
    assert matches_qwen25_model_name("google/gemma-4-E2B-it") is False


def test_qwen25_profile_builds_standard_messages() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="src/config.py:88 ValidationError",
        extracted_signal=ExtractedSignal(
            referenced_files=["src/config.py"],
            command_terms=["python -m ctxsift compress"],
            error_lines=["ValidationError"],
        ),
        max_output_tokens=96,
    )

    messages = build_qwen25_messages(request)

    assert messages[0]["role"] == "system"
    assert "Preserve exactly:" in messages[1]["content"]
    assert "python -m ctxsift compress" in messages[1]["content"]


def test_qwen25_profile_normalizes_headings_and_bullets() -> None:
    assert normalize_qwen25_output("Summary:\n- first\n\n\n- second") == "first\nsecond"


def test_qwen25_profile_rejects_schema_like_output() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="ValidationError",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )

    assert is_valid_qwen25_output(request, "Files:\nsrc/config.py") is False


def test_qwen3_profile_matches_qwen3_model_names() -> None:
    assert matches_qwen3_model_name("Qwen/Qwen3-1.7B") is True
    assert matches_qwen3_model_name("qwen3-0.6b") is True
    assert matches_qwen3_model_name("Qwen/Qwen2.5-1.5B-Instruct") is False


def test_qwen3_profile_builds_standard_messages() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="tests/test_cli.py::test_run failed",
        extracted_signal=ExtractedSignal(
            tests=["tests/test_cli.py::test_run"],
            command_terms=["pytest"],
        ),
        max_output_tokens=96,
    )

    messages = build_qwen3_messages(request)

    assert messages[0]["role"] == "system"
    assert "tests/test_cli.py::test_run" in messages[1]["content"]


def test_qwen3_profile_strips_reasoning_blocks() -> None:
    assert normalize_qwen3_output("<think>hidden chain</think>\nSummary:\n- final answer") == "final answer"


def test_qwen3_profile_rejects_schema_like_output() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="ValueError",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )

    assert is_valid_qwen3_output(request, "Commands:\npytest") is False


def test_qwen35_profile_matches_qwen35_model_names() -> None:
    assert matches_qwen35_model_name("Qwen/Qwen3.5-0.8B") is True
    assert matches_qwen35_model_name("qwen3.5-2b") is True
    assert matches_qwen35_model_name("Qwen/Qwen3-1.7B") is False


def test_qwen35_profile_builds_text_only_messages() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="docker build failed in infra/Dockerfile",
        extracted_signal=ExtractedSignal(
            referenced_files=["infra/Dockerfile"],
            command_terms=["docker build"],
        ),
        max_output_tokens=96,
    )

    messages = build_qwen35_messages(request)

    assert messages[0]["role"] == "system"
    assert "infra/Dockerfile" in messages[1]["content"]
    assert "docker build" in messages[1]["content"]


def test_qwen35_profile_uses_generic_cleanup() -> None:
    assert normalize_qwen35_output("Summary:\n- first\n\n\n- second") == "first\nsecond"


def test_smollm2_profile_matches_smollm2_model_names() -> None:
    assert matches_smollm2_model_name("HuggingFaceTB/SmolLM2-1.7B-Instruct") is True
    assert matches_smollm2_model_name("smollm2-360m") is True
    assert matches_smollm2_model_name("Qwen/Qwen2.5-1.5B-Instruct") is False


def test_smollm2_profile_builds_standard_messages() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="pnpm lint failed in src/app.ts",
        extracted_signal=ExtractedSignal(
            referenced_files=["src/app.ts"],
            command_terms=["pnpm lint"],
        ),
        max_output_tokens=96,
    )

    messages = build_smollm2_messages(request)

    assert messages[0]["role"] == "system"
    assert "src/app.ts" in messages[1]["content"]
    assert "pnpm lint" in messages[1]["content"]


def test_smollm2_profile_uses_generic_cleanup() -> None:
    assert normalize_smollm2_output("Summary:\n- first\n\n\n- second") == "first\nsecond"


def test_smollm2_profile_rejects_schema_like_output() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="lint failed",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )

    assert is_valid_smollm2_output(request, "Commands:\npnpm lint") is False


def test_granite_profile_matches_granite_model_names() -> None:
    assert matches_granite_model_name("ibm-granite/granite-3.3-2b-instruct") is True
    assert matches_granite_model_name("granite-3.3-2b-instruct") is True
    assert matches_granite_model_name("google/gemma-4-E2B-it") is False


def test_granite_profile_builds_standard_messages() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="terraform apply failed in infra/main.tf",
        extracted_signal=ExtractedSignal(
            referenced_files=["infra/main.tf"],
            command_terms=["terraform apply"],
        ),
        max_output_tokens=96,
    )

    messages = build_granite_messages(request)

    assert messages[0]["role"] == "system"
    assert "infra/main.tf" in messages[1]["content"]
    assert "terraform apply" in messages[1]["content"]


def test_granite_profile_strips_reasoning_blocks() -> None:
    assert normalize_granite_output("<think>chain</think><response>final answer</response>") == "final answer"


def test_granite_profile_rejects_schema_like_output() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="apply failed",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )

    assert is_valid_granite_output(request, "Files:\ninfra/main.tf") is False


def test_phi_profile_matches_phi_model_names() -> None:
    assert matches_phi_model_name("microsoft/Phi-3.5-mini-instruct") is True
    assert matches_phi_model_name("phi-3.5-mini-instruct") is True
    assert matches_phi_model_name("Qwen/Qwen3-1.7B") is False


def test_phi_profile_builds_strict_chat_messages() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="uv run failed in src/cli.py",
        extracted_signal=ExtractedSignal(
            referenced_files=["src/cli.py"],
            command_terms=["uv run"],
        ),
        max_output_tokens=96,
    )

    messages = build_phi_messages(request)

    assert messages[0]["role"] == "system"
    assert "src/cli.py" in messages[1]["content"]
    assert "uv run" in messages[1]["content"]


def test_phi_profile_uses_generic_cleanup() -> None:
    assert normalize_phi_output("Summary:\n- first\n\n\n- second") == "first\nsecond"


def test_phi_profile_rejects_role_token_leakage() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="run failed",
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )

    assert is_valid_phi_output(request, "<|assistant|> final answer") is False


def test_profile_registry_resolves_known_families_and_fallback() -> None:
    assert resolve_text_model_profile("google/gemma-4-E2B-it").family_name == "gemma"
    assert resolve_text_model_profile("Qwen/Qwen2.5-0.5B-Instruct").family_name == "qwen2.5"
    assert resolve_text_model_profile("Qwen/Qwen3-1.7B").family_name == "qwen3"
    assert resolve_text_model_profile("Qwen/Qwen3.5-0.8B").family_name == "qwen3.5"
    assert resolve_text_model_profile("HuggingFaceTB/SmolLM2-1.7B-Instruct").family_name == "smollm2"
    assert resolve_text_model_profile("ibm-granite/granite-3.3-2b-instruct").family_name == "granite"
    assert resolve_text_model_profile("microsoft/Phi-3.5-mini-instruct").family_name == "phi"
    assert resolve_text_model_profile("unknown/model").family_name == FALLBACK_PROFILE.family_name


def test_fallback_profile_requires_exact_anchor_preservation() -> None:
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="src/cli.py ValidationError",
        extracted_signal=ExtractedSignal(
            referenced_files=["src/cli.py"],
            error_lines=["ValidationError"],
        ),
        max_output_tokens=64,
    )

    assert preserves_exact_anchors(request, "src/cli.py ValidationError") is True
    assert preserves_exact_anchors(request, "cli.py validation failed") is False
    assert FALLBACK_PROFILE.is_valid_output(request, "src/cli.py ValidationError") is True
    assert FALLBACK_PROFILE.is_valid_output(request, "cli.py validation failed") is True


def test_gemma_profile_normalizes_headings_and_bullets() -> None:
    assert normalize_output("Summary: \n- first line\n- second line") == "first line\nsecond line"
    assert normalize_output("<turn|> concise summary <turn|>") == "concise summary"


def test_resolve_device_fails_when_explicit_cuda_is_unavailable() -> None:
    torch_module = SimpleNamespace(cuda=SimpleNamespace(is_available=lambda: False))

    with pytest.raises(BackendUnavailableError, match="CUDA is not available"):
        _resolve_device("cuda", torch_module)


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
    assert fake_model.to_device == "cuda:0"
    assert fake_model.eval_called is True
    assert fake_model.generate_calls[0]["max_new_tokens"] == 128
    assert fake_model.generate_calls[0]["do_sample"] is False
    assert fake_model.generate_calls[0]["pad_token_id"] == 0
    assert fake_model.generate_calls[0]["eos_token_id"] == 2
    assert "AuthError" in fake_tokenizer.last_messages[1]["content"]


def test_transformers_backend_supports_qwen25_profile(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_model = FakeModel()
    fake_tokenizer = FakeTokenizer()

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_tokenizer

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
    backend = TransformersTextBackend(
        LocalModelConfig(
            model="Qwen/Qwen2.5-0.5B-Instruct",
            device="cpu",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="ValidationError: Extra inputs are not permitted",
        extracted_signal=ExtractedSignal(
            referenced_files=["src/config.py"],
            command_terms=["python -m ctxsift compress"],
            error_lines=["ValidationError: Extra inputs are not permitted"],
        ),
        max_output_tokens=96,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert "python -m ctxsift compress" in fake_tokenizer.last_messages[1]["content"]
    assert backend._profile.family_name == "qwen2.5"


def test_transformers_backend_supports_qwen3_profile_and_disables_thinking(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_model = FakeModel()
    fake_tokenizer = FakeTokenizer()

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_tokenizer

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
    backend = TransformersTextBackend(
        LocalModelConfig(
            model="Qwen/Qwen3-1.7B",
            device="cpu",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="tests/test_cli.py::test_run failed",
        extracted_signal=ExtractedSignal(
            tests=["tests/test_cli.py::test_run"],
            command_terms=["pytest"],
        ),
        max_output_tokens=96,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert backend._profile.family_name == "qwen3"
    assert fake_tokenizer.last_messages is not None
    assert fake_tokenizer.last_template_kwargs == {
        "tokenize": False,
        "add_generation_prompt": True,
        "enable_thinking": False,
    }


def test_transformers_backend_supports_qwen35_profile(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_model = FakeModel()
    fake_tokenizer = FakeTokenizer()

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_tokenizer

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
    backend = TransformersTextBackend(
        LocalModelConfig(
            model="Qwen/Qwen3.5-0.8B",
            device="cpu",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="docker build failed in infra/Dockerfile",
        extracted_signal=ExtractedSignal(
            referenced_files=["infra/Dockerfile"],
            command_terms=["docker build"],
        ),
        max_output_tokens=96,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert backend._profile.family_name == "qwen3.5"
    assert fake_tokenizer.last_messages is not None


def test_transformers_backend_supports_smollm2_profile(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_model = FakeModel()
    fake_tokenizer = FakeTokenizer()

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_tokenizer

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
    backend = TransformersTextBackend(
        LocalModelConfig(
            model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
            device="cpu",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="pnpm lint failed in src/app.ts",
        extracted_signal=ExtractedSignal(
            referenced_files=["src/app.ts"],
            command_terms=["pnpm lint"],
        ),
        max_output_tokens=96,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert backend._profile.family_name == "smollm2"
    assert fake_tokenizer.last_messages is not None


def test_transformers_backend_supports_granite_profile_and_disables_thinking(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_model = FakeModel()
    fake_tokenizer = FakeGraniteTokenizer()

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_model

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return fake_tokenizer

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
    backend = TransformersTextBackend(
        LocalModelConfig(
            model="ibm-granite/granite-3.3-2b-instruct",
            device="cpu",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="terraform apply failed in infra/main.tf",
        extracted_signal=ExtractedSignal(
            referenced_files=["infra/main.tf"],
            command_terms=["terraform apply"],
        ),
        max_output_tokens=96,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert backend._profile.family_name == "granite"
    assert fake_tokenizer.last_template_kwargs == {
        "tokenize": False,
        "add_generation_prompt": True,
        "thinking": False,
    }


def test_transformers_backend_supports_phi_profile_with_trust_remote_code(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_model = FakeModel()
    fake_tokenizer = FakeTokenizer()
    captured: dict[str, Any] = {}

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
    backend = TransformersTextBackend(
        LocalModelConfig(
            model="microsoft/Phi-3.5-mini-instruct",
            device="cpu",
        )
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="uv run failed in src/cli.py",
        extracted_signal=ExtractedSignal(
            referenced_files=["src/cli.py"],
            command_terms=["uv run"],
        ),
        max_output_tokens=96,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "Model answer"
    assert backend._profile.family_name == "phi"
    assert captured["model_kwargs"]["trust_remote_code"] is True
    assert captured["tokenizer_kwargs"]["trust_remote_code"] is True


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
        "ctxsift.models.transformers_gemma.text_attention_choice",
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
        "ctxsift.models.transformers_gemma.text_attention_choice",
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


def test_transformers_backend_uses_bnb8_quantization_without_model_move(
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
    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cuda",
            gguf_filename=None,
            quantization="bnb-8bit",
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
    assert captured["model_kwargs"]["device_map"] == "cuda:0"
    assert quantization_config.kwargs["load_in_8bit"] is True
    assert fake_model.to_device is None


def test_transformers_backend_reuses_persisted_quantized_checkpoint(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    calls: list[tuple[str, dict[str, Any]]] = []
    tokenizer_calls: list[tuple[str, dict[str, Any]]] = []

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            calls.append((model_name, kwargs))
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            tokenizer_calls.append((model_name, kwargs))
            return FakeTokenizer()

    fake_torch = SimpleNamespace(
        cuda=SimpleNamespace(is_available=lambda: True),
        float32="float32",
        float16="float16",
        bfloat16="bfloat16",
    )
    cache_dir = tmp_path / "quant-cache"
    cache_dir.mkdir(parents=True)
    (cache_dir / "config.json").write_text("{}", encoding="utf-8")
    (cache_dir / "ctxsift-quantized-model.json").write_text("{}", encoding="utf-8")
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
        lambda: type("FakeBitsAndBytesConfig", (), {"__init__": lambda self, **kwargs: None}),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.resolve_quantized_model_cache",
        lambda config, model_name: SimpleNamespace(model_dir=cache_dir),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.has_persisted_quantized_model",
        lambda cache: True,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.cached_model_source",
        lambda cache: str(cache.model_dir),
    )

    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cuda",
            gguf_filename=None,
            quantization="bnb-8bit",
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
    assert calls[0][0] == str(cache_dir)
    assert "quantization_config" not in calls[0][1]
    assert tokenizer_calls[0][0] == str(cache_dir)


def test_transformers_backend_persists_quantized_checkpoint_after_initial_load(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    fake_model = FakeModel()
    persisted: dict[str, Any] = {}

    class FakeBitsAndBytesConfig:
        def __init__(self, **kwargs) -> None:
            self.kwargs = kwargs

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            persisted["loaded_from"] = model_name
            persisted["model_kwargs"] = kwargs
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
    cache_dir = tmp_path / "quant-cache"
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
        "ctxsift.models.transformers_gemma.resolve_quantized_model_cache",
        lambda config, model_name: SimpleNamespace(model_dir=cache_dir),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.has_persisted_quantized_model",
        lambda cache: False,
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_gemma.persist_quantized_model_cache",
        lambda cache, model, tokenizer, model_name, config: persisted.update(
            {
                "persisted_cache_dir": cache.model_dir,
                "persisted_model_name": model_name,
                "persisted_quantization": config.quantization.value,
                "persisted_tokenizer": tokenizer,
            }
        ),
    )

    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cuda",
            gguf_filename=None,
            quantization="bnb-8bit",
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
    assert persisted["loaded_from"] == "google/gemma-4-E2B-it"
    assert persisted["persisted_cache_dir"] == cache_dir
    assert persisted["persisted_model_name"] == "google/gemma-4-E2B-it"
    assert persisted["persisted_quantization"] == "bnb-8bit"
    assert isinstance(persisted["persisted_tokenizer"], FakeTokenizer)


def test_runtime_input_device_handles_integer_device_map_values() -> None:
    fake_model = FakeModel()
    fake_model.device = None
    fake_model.hf_device_map = {"": 0}

    assert _runtime_input_device(fake_model, "cpu") == "cuda:0"


def test_bitsandbytes_quantization_requires_accelerate(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._module_available",
        lambda module_name: module_name == "bitsandbytes",
    )

    with pytest.raises(BackendUnavailableError, match="accelerate"):
        build_transformers_load_options(
            config=LocalModelConfig(device="cuda", gguf_filename=None, quantization="bnb-4bit-nf4"),
            resolved_torch_device="cuda:0",
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
        "ctxsift.models.transformers_gemma.text_attention_choice",
        lambda device_label, configured_value: "flash_attention_2",
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_quantization._module_available",
        lambda module_name: False,
    )
    backend = TransformersGemmaBackend(
        LocalModelConfig(
            model="google/gemma-4-E2B-it",
            device="cuda",
            gguf_filename=None,
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


def test_transformers_backend_rejects_invalid_gemma_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class InvalidTokenizer(FakeTokenizer):
        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "<|assistant|> final answer"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

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
    backend = TransformersGemmaBackend(LocalModelConfig(model="google/gemma-4-E2B-it", device="cpu"))
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="AuthError: login failed",
        extracted_signal=ExtractedSignal(symbols=["AuthError"]),
        max_output_tokens=64,
    )

    with pytest.raises(ModelOutputRejectedError, match="gemma output validation failed"):
        asyncio.run(backend.compress(request))


def test_transformers_backend_rejects_invalid_qwen25_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class InvalidTokenizer(FakeTokenizer):
        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "Files:\nsrc/config.py"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

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
    backend = TransformersTextBackend(
        LocalModelConfig(model="Qwen/Qwen2.5-0.5B-Instruct", device="cpu")
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="ValidationError",
        extracted_signal=ExtractedSignal(referenced_files=["src/config.py"]),
        max_output_tokens=64,
    )

    with pytest.raises(ModelOutputRejectedError, match="qwen2.5 output validation failed"):
        asyncio.run(backend.compress(request))


def test_transformers_backend_rejects_invalid_qwen3_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class InvalidTokenizer(FakeTokenizer):
        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "Commands:\npytest"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

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
    backend = TransformersTextBackend(
        LocalModelConfig(model="Qwen/Qwen3-1.7B", device="cpu")
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="pytest failed",
        extracted_signal=ExtractedSignal(command_terms=["pytest"]),
        max_output_tokens=64,
    )

    with pytest.raises(ModelOutputRejectedError, match="qwen3 output validation failed"):
        asyncio.run(backend.compress(request))


def test_transformers_backend_rejects_invalid_qwen35_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class InvalidTokenizer(FakeTokenizer):
        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "<|assistant|> leaked role token"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

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
    backend = TransformersTextBackend(
        LocalModelConfig(model="Qwen/Qwen3.5-0.8B", device="cpu")
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="docker build failed",
        extracted_signal=ExtractedSignal(command_terms=["docker build"]),
        max_output_tokens=64,
    )

    with pytest.raises(ModelOutputRejectedError, match="qwen3.5 output validation failed"):
        asyncio.run(backend.compress(request))


def test_transformers_backend_rejects_invalid_smollm2_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class InvalidTokenizer(FakeTokenizer):
        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "Files:\nsrc/app.ts"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

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
    backend = TransformersTextBackend(
        LocalModelConfig(model="HuggingFaceTB/SmolLM2-1.7B-Instruct", device="cpu")
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="pnpm lint failed",
        extracted_signal=ExtractedSignal(command_terms=["pnpm lint"]),
        max_output_tokens=64,
    )

    with pytest.raises(ModelOutputRejectedError, match="smollm2 output validation failed") as error:
        asyncio.run(backend.compress(request))

    message = str(error.value)
    assert "first_pass='Files: src/app.ts'" in message
    assert "repair_pass='Files: src/app.ts'" in message


def test_transformers_backend_rejects_invalid_granite_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class InvalidTokenizer(FakeGraniteTokenizer):
        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "Files:\ninfra/main.tf"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

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
    backend = TransformersTextBackend(
        LocalModelConfig(model="ibm-granite/granite-3.3-2b-instruct", device="cpu")
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="terraform apply failed",
        extracted_signal=ExtractedSignal(command_terms=["terraform apply"]),
        max_output_tokens=64,
    )

    with pytest.raises(ModelOutputRejectedError, match="granite output validation failed"):
        asyncio.run(backend.compress(request))


def test_transformers_backend_rejects_invalid_phi_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class InvalidTokenizer(FakeTokenizer):
        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "final <|assistant|> answer"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

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
    backend = TransformersTextBackend(
        LocalModelConfig(model="microsoft/Phi-3.5-mini-instruct", device="cpu")
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="uv run failed",
        extracted_signal=ExtractedSignal(command_terms=["uv run"]),
        max_output_tokens=64,
    )

    with pytest.raises(ModelOutputRejectedError, match="phi output validation failed"):
        asyncio.run(backend.compress(request))


def test_transformers_backend_repairs_invalid_first_pass_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class RepairingTokenizer(FakeTokenizer):
        def __init__(self) -> None:
            super().__init__()
            self.decode_calls = 0

        def decode(self, tokens, skip_special_tokens: bool) -> str:
            self.decode_calls += 1
            if self.decode_calls == 1:
                return "Commands:\npytest"
            return "tests/test_cli.py::test_run failed under pytest"

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return RepairingTokenizer()

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
    backend = TransformersTextBackend(
        LocalModelConfig(model="Qwen/Qwen3-1.7B", device="cpu")
    )
    request = ModelCompressionInput(
        instruction="Summarize failures",
        raw_input="tests/test_cli.py::test_run failed",
        extracted_signal=ExtractedSignal(
            tests=["tests/test_cli.py::test_run"],
            command_terms=["pytest"],
        ),
        max_output_tokens=64,
    )

    result = asyncio.run(backend.compress(request))

    assert result == "tests/test_cli.py::test_run failed under pytest"


def test_apply_text_chat_template_handles_uninspectable_signature() -> None:
    class BuiltinLikeTokenizer:
        def apply_chat_template(self, *args, **kwargs):
            return "templated"

    original_signature = inspect.signature

    def raising_signature(callable_object):
        if callable_object.__name__ == "apply_chat_template":
            raise ValueError("signature unavailable")
        return original_signature(callable_object)

    tokenizer = BuiltinLikeTokenizer()
    messages = [{"role": "system", "content": "x"}]

    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr("ctxsift.models.transformers_gemma.inspect.signature", raising_signature)
        result = _apply_text_chat_template(tokenizer, messages)

    assert result == "templated"


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
