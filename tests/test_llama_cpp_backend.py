"""Tests for llama.cpp local strategy handling."""

from pathlib import Path
from typing import Any

from ctxsift.models.llama_cpp_backend import (
    LlamaCppBackend,
    LlamaRuntime,
    _generate_with_runtime_strategy,
)
from ctxsift.models.local_model_strategy import (
    DecodingMode,
    LocalModelStrategy,
    PromptRenderMode,
    StrategySource,
    ThinkingControlMode,
)
from ctxsift.types import LocalModelConfig


class FakeTokenizer:
    """Tokenizer stub that renders a text prompt with thinking control."""

    def __init__(self) -> None:
        self.last_kwargs: dict[str, Any] | None = None

    def apply_chat_template(
        self,
        messages,
        tokenize,
        add_generation_prompt,
        enable_thinking=False,
    ):
        self.last_kwargs = {
            "messages": messages,
            "tokenize": tokenize,
            "add_generation_prompt": add_generation_prompt,
            "enable_thinking": enable_thinking,
        }
        return "templated prompt"


class FakeLlamaModel:
    """llama.cpp model stub for text and chat completion."""

    def __init__(self) -> None:
        self.completion_calls: list[dict[str, Any]] = []
        self.chat_calls: list[dict[str, Any]] = []

    def create_completion(self, **kwargs):
        self.completion_calls.append(kwargs)
        return {"choices": [{"text": "Model answer"}]}

    def create_chat_completion(self, **kwargs):
        self.chat_calls.append(kwargs)
        return {"choices": [{"message": {"content": "Chat answer"}}]}


def test_generate_with_runtime_strategy_uses_qwen_sampled_text_completion() -> None:
    tokenizer = FakeTokenizer()
    model = FakeLlamaModel()
    runtime = LlamaRuntime(
        model=model,
        model_path=Path("dummy.gguf"),
        tokenizer=tokenizer,
        strategy=LocalModelStrategy(
            backend="llama_cpp",
            model="unsloth/Qwen3-0.6B-GGUF",
            gguf_filename="Qwen3-0.6B-Q8_0.gguf",
            thinking_control=ThinkingControlMode.ENABLE_THINKING_FALSE,
            prompt_renderer=PromptRenderMode.CHAT_TEMPLATE_TEXT,
            decoding_mode=DecodingMode.SAMPLED,
            temperature=0.7,
            top_p=0.8,
            top_k=20,
        ),
    )
    messages = [{"role": "user", "content": "Summarize failures"}]

    output, effective_strategy = _generate_with_runtime_strategy(
        runtime=runtime,
        messages=messages,
        max_output_tokens=64,
    )

    assert output == "Model answer"
    assert effective_strategy.prompt_renderer is PromptRenderMode.CHAT_TEMPLATE_TEXT
    assert tokenizer.last_kwargs is not None
    assert tokenizer.last_kwargs["enable_thinking"] is False
    assert model.completion_calls[0]["prompt"] == "templated prompt"
    assert model.completion_calls[0]["temperature"] == 0.7
    assert model.completion_calls[0]["top_p"] == 0.8
    assert model.completion_calls[0]["top_k"] == 20
    assert model.chat_calls == []


def test_generate_with_runtime_strategy_falls_back_to_generic_prompt_without_tokenizer() -> None:
    model = FakeLlamaModel()
    runtime = LlamaRuntime(
        model=model,
        model_path=Path("dummy.gguf"),
        tokenizer=None,
        strategy=LocalModelStrategy(
            backend="llama_cpp",
            model="unsloth/Qwen3-0.6B-GGUF",
            gguf_filename="Qwen3-0.6B-Q8_0.gguf",
            prompt_renderer=PromptRenderMode.CHAT_TEMPLATE_TEXT,
            decoding_mode=DecodingMode.SAMPLED,
            temperature=0.7,
        ),
    )
    messages = [{"role": "user", "content": "Summarize failures"}]

    output, effective_strategy = _generate_with_runtime_strategy(
        runtime=runtime,
        messages=messages,
        max_output_tokens=32,
    )

    assert output == "Model answer"
    assert effective_strategy.prompt_renderer is PromptRenderMode.BACKEND_DEFAULT
    assert "<|user|>" in model.completion_calls[0]["prompt"]
    assert model.completion_calls[0]["temperature"] == 0.7
    assert model.chat_calls == []


def test_generate_with_runtime_strategy_uses_alpaca_instruction_prompt() -> None:
    model = FakeLlamaModel()
    runtime = LlamaRuntime(
        model=model,
        model_path=Path("dummy.gguf"),
        tokenizer=None,
        strategy=LocalModelStrategy(
            backend="llama_cpp",
            model="SupraLabs/Supra-50M-Instruct",
            prompt_renderer=PromptRenderMode.ALPACA_INSTRUCTION,
            decoding_mode=DecodingMode.SAMPLED,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
            repetition_penalty=1.15,
        ),
    )
    messages = [
        {"role": "system", "content": "You compress raw tool output into compact recall notes."},
        {"role": "user", "content": "Summarize pytest failed in tests/test_auth.py::test_login"},
    ]

    output, effective_strategy = _generate_with_runtime_strategy(
        runtime=runtime,
        messages=messages,
        max_output_tokens=32,
    )

    prompt_text = model.completion_calls[0]["prompt"]
    assert output == "Model answer"
    assert effective_strategy.prompt_renderer is PromptRenderMode.ALPACA_INSTRUCTION
    assert "Below is an instruction that describes a task" in prompt_text
    assert (
        "### Instruction:\nSummarize pytest failed in tests/test_auth.py::test_login" in prompt_text
    )
    assert "### Input:" in prompt_text
    assert "You compress raw tool output into compact recall notes." in prompt_text
    assert model.completion_calls[0]["temperature"] == 0.7
    assert model.completion_calls[0]["top_p"] == 0.9
    assert model.completion_calls[0]["top_k"] == 50
    assert model.completion_calls[0]["repeat_penalty"] == 1.15
    assert model.chat_calls == []


def test_llama_backend_reuses_discovered_strategy_without_reprobe() -> None:
    backend = LlamaCppBackend(
        LocalModelConfig(
            model="unsloth/Qwen3-0.6B-GGUF",
            gguf_filename="Qwen3-0.6B-Q8_0.gguf",
            device="cpu",
        )
    )
    strategy = LocalModelStrategy(
        backend="llama_cpp",
        model="unsloth/Qwen3-0.6B-GGUF",
        gguf_filename="Qwen3-0.6B-Q8_0.gguf",
        prompt_renderer=PromptRenderMode.BACKEND_DEFAULT,
        source=StrategySource.DISCOVERED,
    )
    runtime = LlamaRuntime(
        model=FakeLlamaModel(),
        model_path=Path("dummy.gguf"),
        tokenizer=FakeTokenizer(),
        strategy=strategy,
    )

    candidates = backend._candidate_strategies(runtime)

    assert candidates == [strategy]
