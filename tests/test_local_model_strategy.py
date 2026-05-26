"""Tests for local-model no-thinking strategy resolution and persistence."""

from pathlib import Path

from ctxsift.models.local_model_strategy import (
    DecodingMode,
    LocalModelStrategy,
    LocalModelStrategyStore,
    PromptRenderMode,
    StrategySource,
    ThinkingControlMode,
    _merge_store_entries,
    _save_strategy_store,
    ensure_strategy_store,
    persist_prompt_renderer_fallback,
    probe_candidate_strategies,
    resolve_local_model_strategy,
    strategy_store_path,
    synchronize_strategy_store_for_config,
    persist_runtime_strategy,
)
from ctxsift.types import LocalModelConfig


class EnableThinkingTokenizer:
    """Tokenizer stub that exposes the Qwen/MiniCPM thinking control."""

    def apply_chat_template(
        self,
        messages,
        tokenize,
        add_generation_prompt,
        enable_thinking=False,
    ):
        del messages, tokenize, add_generation_prompt, enable_thinking
        return "templated"


class PlainChatTemplateTokenizer:
    """Tokenizer stub that exposes a standard chat template only."""

    def apply_chat_template(
        self,
        messages,
        tokenize,
        add_generation_prompt,
    ):
        del messages, tokenize, add_generation_prompt
        return "templated"


def test_synchronize_strategy_store_creates_internal_store(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.local_model_strategy.user_config_path",
        lambda app_name: tmp_path / app_name,
    )

    synchronize_strategy_store_for_config(LocalModelConfig())

    store_path = strategy_store_path()
    assert store_path.exists()
    store = ensure_strategy_store()
    assert any(
        strategy.model == "ibm-granite/granite-4.0-350m-GGUF"
        for strategy in store.strategies
    )


def test_resolve_local_model_strategy_persists_enable_thinking_discovery(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.local_model_strategy.user_config_path",
        lambda app_name: tmp_path / app_name,
    )
    config = LocalModelConfig(model="example/hybrid-1b", gguf_filename=None, device="cuda")

    strategy = resolve_local_model_strategy(
        config,
        backend="transformers",
        tokenizer=EnableThinkingTokenizer(),
    )

    assert strategy.source is StrategySource.DISCOVERED
    assert strategy.prompt_renderer is PromptRenderMode.CHAT_TEMPLATE_TEXT
    assert strategy.thinking_control is ThinkingControlMode.ENABLE_THINKING_FALSE
    store = ensure_strategy_store()
    assert any(
        entry.model == "example/hybrid-1b"
        and entry.thinking_control is ThinkingControlMode.ENABLE_THINKING_FALSE
        for entry in store.strategies
    )


def test_resolve_local_model_strategy_discovers_plain_chat_template(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.local_model_strategy.user_config_path",
        lambda app_name: tmp_path / app_name,
    )
    config = LocalModelConfig(model="example/plain-chat", gguf_filename=None, device="cuda")

    strategy = resolve_local_model_strategy(
        config,
        backend="transformers",
        tokenizer=PlainChatTemplateTokenizer(),
    )

    assert strategy.source is StrategySource.DISCOVERED
    assert strategy.prompt_renderer is PromptRenderMode.CHAT_TEMPLATE_TEXT
    assert strategy.thinking_control is ThinkingControlMode.NONE
    assert strategy.decoding_mode is DecodingMode.DETERMINISTIC


def test_persist_prompt_renderer_fallback_updates_discovered_strategy(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.local_model_strategy.user_config_path",
        lambda app_name: tmp_path / app_name,
    )
    config = LocalModelConfig(model="example/plain-chat", gguf_filename=None, device="cuda")
    discovered = resolve_local_model_strategy(
        config,
        backend="transformers",
        tokenizer=PlainChatTemplateTokenizer(),
    )

    persist_prompt_renderer_fallback(
        config,
        backend="transformers",
        strategy=discovered,
    )

    store = ensure_strategy_store()
    persisted = next(
        entry
        for entry in store.strategies
        if entry.model == "example/plain-chat" and entry.backend == "transformers"
    )
    assert persisted.source is StrategySource.DISCOVERED
    assert persisted.prompt_renderer is PromptRenderMode.BACKEND_DEFAULT


def test_probe_candidate_strategies_prefers_thinking_control_then_fallback() -> None:
    current = resolve_local_model_strategy(
        LocalModelConfig(model="example/hybrid-1b", gguf_filename=None, device="cuda"),
        backend="transformers",
        tokenizer=EnableThinkingTokenizer(),
    )

    candidates = probe_candidate_strategies(EnableThinkingTokenizer(), current)

    assert candidates[0].thinking_control is ThinkingControlMode.ENABLE_THINKING_FALSE
    assert any(
        candidate.prompt_renderer is PromptRenderMode.BACKEND_DEFAULT
        and candidate.thinking_control is ThinkingControlMode.NONE
        for candidate in candidates
    )


def test_merge_store_keeps_user_override_over_built_in() -> None:
    built_in = LocalModelStrategyStore(
        strategies=[
            LocalModelStrategy(
                backend="transformers",
                model="Qwen/Qwen3-1.7B",
                thinking_control=ThinkingControlMode.ENABLE_THINKING_FALSE,
                prompt_renderer=PromptRenderMode.CHAT_TEMPLATE_TEXT,
                source=StrategySource.BUILT_IN,
            )
        ]
    )
    existing = LocalModelStrategyStore(
        strategies=[
            LocalModelStrategy(
                backend="transformers",
                model="Qwen/Qwen3-1.7B",
                thinking_control=ThinkingControlMode.NONE,
                prompt_renderer=PromptRenderMode.BACKEND_DEFAULT,
                source=StrategySource.USER_OVERRIDE,
            )
        ]
    )

    merged = _merge_store_entries(built_in, existing)

    assert len(merged.strategies) == 1
    assert merged.strategies[0].source is StrategySource.USER_OVERRIDE
    assert merged.strategies[0].prompt_renderer is PromptRenderMode.BACKEND_DEFAULT


def test_resolve_local_model_strategy_preserves_user_override_over_discovery(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "ctxsift.models.local_model_strategy.user_config_path",
        lambda app_name: tmp_path / app_name,
    )
    override = LocalModelStrategy(
        backend="transformers",
        model="example/hybrid-1b",
        thinking_control=ThinkingControlMode.NONE,
        prompt_renderer=PromptRenderMode.BACKEND_DEFAULT,
        source=StrategySource.USER_OVERRIDE,
    )
    _save_strategy_store(
        strategy_store_path(),
        LocalModelStrategyStore(strategies=[override]),
    )
    config = LocalModelConfig(model="example/hybrid-1b", gguf_filename=None, device="cuda")

    resolved = resolve_local_model_strategy(
        config,
        backend="transformers",
        tokenizer=EnableThinkingTokenizer(),
    )

    assert resolved.source is StrategySource.USER_OVERRIDE
    assert resolved.prompt_renderer is PromptRenderMode.BACKEND_DEFAULT
    assert resolved.thinking_control is ThinkingControlMode.NONE


def test_persist_runtime_strategy_keeps_user_override_unchanged() -> None:
    config = LocalModelConfig(model="example/hybrid-1b", gguf_filename=None, device="cuda")
    override = LocalModelStrategy(
        backend="transformers",
        model="example/hybrid-1b",
        thinking_control=ThinkingControlMode.NONE,
        prompt_renderer=PromptRenderMode.BACKEND_DEFAULT,
        source=StrategySource.USER_OVERRIDE,
    )

    persisted = persist_runtime_strategy(
        config,
        backend="transformers",
        strategy=override,
    )

    assert persisted is override
