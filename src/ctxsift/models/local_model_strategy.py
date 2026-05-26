"""Built-in and discovered local-model no-thinking strategy helpers."""

from __future__ import annotations

import json
import logging
from enum import Enum
from importlib import resources
from pathlib import Path
from typing import Any

from platformdirs import user_config_path
from pydantic import Field

from ctxsift.models.local_runtime import required_gguf_filename
from ctxsift.types import LocalModelConfig, StrictModel

LOGGER = logging.getLogger(__name__)
STORE_VERSION = 1


class ThinkingControlMode(str, Enum):
    """Supported prompt/template controls for hybrid thinking models."""

    NONE = "none"
    ENABLE_THINKING_FALSE = "enable_thinking_false"
    THINKING_FALSE = "thinking_false"


class PromptRenderMode(str, Enum):
    """How the backend should render the final prompt text."""

    BACKEND_DEFAULT = "backend_default"
    CHAT_TEMPLATE_TEXT = "chat_template_text"
    ALPACA_INSTRUCTION = "alpaca_instruction"


class DecodingMode(str, Enum):
    """Supported local decoding policies."""

    DETERMINISTIC = "deterministic"
    SAMPLED = "sampled"


class StrategySource(str, Enum):
    """Where one local-model strategy came from."""

    USER_OVERRIDE = "user_override"
    BUILT_IN = "built_in"
    DISCOVERED = "discovered"
    DEFAULT = "default"


class LocalModelStrategy(StrictModel):
    """One local-model prompt/render/decoding strategy."""

    backend: str
    model: str
    gguf_filename: str | None = None
    thinking_control: ThinkingControlMode = ThinkingControlMode.NONE
    prompt_renderer: PromptRenderMode = PromptRenderMode.BACKEND_DEFAULT
    decoding_mode: DecodingMode = DecodingMode.DETERMINISTIC
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None
    repetition_penalty: float | None = None
    source: StrategySource = StrategySource.BUILT_IN

    def matches(self, config: LocalModelConfig, *, backend: str) -> bool:
        """Return whether this strategy targets the given runtime config."""
        if self.backend != backend:
            return False
        if self.model != config.model.strip():
            return False
        expected_gguf = self.gguf_filename or ""
        actual_gguf = (config.gguf_filename or "").strip()
        return expected_gguf == actual_gguf

    def key(self) -> str:
        """Return one stable key for persistence and lookup."""
        return strategy_key(
            backend=self.backend,
            model=self.model,
            gguf_filename=self.gguf_filename,
        )


class LocalModelStrategyStore(StrictModel):
    """Persisted local-model strategy document."""

    version: int = STORE_VERSION
    strategies: list[LocalModelStrategy] = Field(default_factory=list)


def strategy_store_path() -> Path:
    """Return the internal global strategy store path."""
    return user_config_path("ctxsift") / "local_model_strategies.json"


def ensure_strategy_store() -> LocalModelStrategyStore:
    """Seed and refresh the global strategy store from built-ins."""
    built_in_store = _load_built_in_store()
    existing_store = _load_existing_store()
    merged_store = _merge_store_entries(built_in_store, existing_store)
    if _store_needs_save(merged_store, existing_store):
        _save_strategy_store(strategy_store_path(), merged_store)
    return merged_store


def resolve_local_model_strategy(
    config: LocalModelConfig,
    *,
    backend: str,
    tokenizer: Any | None = None,
) -> LocalModelStrategy:
    """Resolve one local-model strategy from built-ins, discovery, or fallback."""
    store = ensure_strategy_store()
    strategy = _stored_strategy_for_config(store, config, backend=backend)
    if strategy is not None:
        return strategy
    discovered_strategy = _discover_strategy_from_tokenizer(
        config, backend=backend, tokenizer=tokenizer
    )
    if discovered_strategy is not None:
        _persist_discovered_strategy(discovered_strategy)
        return discovered_strategy
    return default_local_model_strategy(config, backend=backend)


def default_local_model_strategy(config: LocalModelConfig, *, backend: str) -> LocalModelStrategy:
    """Return the conservative local fallback strategy."""
    gguf_filename = (config.gguf_filename or "").strip() or None
    return LocalModelStrategy(
        backend=backend,
        model=config.model.strip(),
        gguf_filename=gguf_filename,
        source=StrategySource.DEFAULT,
    )


def build_chat_template_kwargs(strategy: LocalModelStrategy) -> dict[str, Any]:
    """Build chat-template keyword arguments for one resolved strategy."""
    kwargs: dict[str, Any] = {"tokenize": False, "add_generation_prompt": True}
    if strategy.thinking_control is ThinkingControlMode.ENABLE_THINKING_FALSE:
        kwargs["enable_thinking"] = False
    elif strategy.thinking_control is ThinkingControlMode.THINKING_FALSE:
        kwargs["thinking"] = False
    return kwargs


def supports_strategy_chat_template(tokenizer: Any, strategy: LocalModelStrategy) -> bool:
    """Return whether the tokenizer can honor the strategy's chat-template controls."""
    apply_chat_template = getattr(tokenizer, "apply_chat_template", None)
    if not callable(apply_chat_template):
        return False
    if strategy.thinking_control is ThinkingControlMode.NONE:
        return True
    signature = _safe_chat_template_signature(apply_chat_template)
    if signature is None:
        return False
    if strategy.thinking_control is ThinkingControlMode.ENABLE_THINKING_FALSE:
        return "enable_thinking" in signature.parameters
    if strategy.thinking_control is ThinkingControlMode.THINKING_FALSE:
        return "thinking" in signature.parameters
    return False


def render_prompt_with_strategy(
    tokenizer: Any,
    messages: list[dict[str, str]],
    strategy: LocalModelStrategy,
) -> str:
    """Render prompt text with one resolved strategy."""
    return tokenizer.apply_chat_template(messages, **build_chat_template_kwargs(strategy))


def render_nonchat_prompt_with_strategy(
    messages: list[dict[str, str]],
    strategy: LocalModelStrategy,
) -> str:
    """Render one non-chat prompt strategy into plain text."""
    if strategy.prompt_renderer is PromptRenderMode.ALPACA_INSTRUCTION:
        return _render_alpaca_instruction_prompt(messages)
    raise ValueError(f"Unsupported non-chat prompt renderer: {strategy.prompt_renderer.value}")


def apply_transformers_decoding_strategy(
    *,
    base_kwargs: dict[str, Any],
    tokenizer: object,
    max_output_tokens: int,
    strategy: LocalModelStrategy,
) -> dict[str, Any]:
    """Overlay one local strategy onto Transformers generation kwargs."""
    kwargs = dict(base_kwargs)
    kwargs["max_new_tokens"] = max_output_tokens
    if strategy.decoding_mode is DecodingMode.SAMPLED:
        kwargs["do_sample"] = True
        if strategy.temperature is not None:
            kwargs["temperature"] = strategy.temperature
        if strategy.top_p is not None:
            kwargs["top_p"] = strategy.top_p
        if strategy.top_k is not None:
            kwargs["top_k"] = strategy.top_k
        if strategy.repetition_penalty is not None:
            kwargs["repetition_penalty"] = strategy.repetition_penalty
    pad_token_id = getattr(tokenizer, "pad_token_id", None)
    eos_token_id = getattr(tokenizer, "eos_token_id", None)
    if pad_token_id is not None:
        kwargs["pad_token_id"] = int(pad_token_id)
    if eos_token_id is not None:
        kwargs["eos_token_id"] = int(eos_token_id)
    return kwargs


def llama_completion_options(
    *,
    max_output_tokens: int,
    strategy: LocalModelStrategy,
) -> dict[str, Any]:
    """Build llama.cpp completion options from one local strategy."""
    options: dict[str, Any] = {
        "max_tokens": max_output_tokens,
        "echo": False,
    }
    if strategy.decoding_mode is DecodingMode.SAMPLED:
        options["temperature"] = strategy.temperature if strategy.temperature is not None else 0.7
        if strategy.top_p is not None:
            options["top_p"] = strategy.top_p
        if strategy.top_k is not None:
            options["top_k"] = strategy.top_k
        if strategy.repetition_penalty is not None:
            options["repeat_penalty"] = strategy.repetition_penalty
    else:
        options["temperature"] = 0.0
    return options


def synchronize_strategy_store_for_config(config: LocalModelConfig) -> None:
    """Ensure the global internal store exists before later local-model use."""
    ensure_strategy_store()
    del config


def persist_runtime_strategy(
    config: LocalModelConfig,
    *,
    backend: str,
    strategy: LocalModelStrategy,
) -> LocalModelStrategy:
    """Persist one resolved runtime strategy as a discovered entry."""
    if strategy.source in {StrategySource.BUILT_IN, StrategySource.USER_OVERRIDE}:
        return strategy
    gguf_filename = (config.gguf_filename or "").strip() or None
    persisted_strategy = LocalModelStrategy(
        backend=backend,
        model=config.model.strip(),
        gguf_filename=gguf_filename,
        thinking_control=strategy.thinking_control,
        prompt_renderer=strategy.prompt_renderer,
        decoding_mode=strategy.decoding_mode,
        temperature=strategy.temperature,
        top_p=strategy.top_p,
        top_k=strategy.top_k,
        repetition_penalty=strategy.repetition_penalty,
        source=StrategySource.DISCOVERED,
    )
    _persist_discovered_strategy(persisted_strategy)
    return persisted_strategy


def persist_prompt_renderer_fallback(
    config: LocalModelConfig,
    *,
    backend: str,
    strategy: LocalModelStrategy,
) -> None:
    """Persist one discovered prompt-render fallback for later local runs."""
    persist_runtime_strategy(
        config,
        backend=backend,
        strategy=strategy.model_copy(
            update={
                "prompt_renderer": PromptRenderMode.BACKEND_DEFAULT,
            }
        ),
    )


def probe_candidate_strategies(
    tokenizer: Any | None,
    current_strategy: LocalModelStrategy,
) -> list[LocalModelStrategy]:
    """Return safe prompt/thinking-control alternatives for one unknown local model."""
    apply_chat_template = getattr(tokenizer, "apply_chat_template", None)
    signature = (
        _safe_chat_template_signature(apply_chat_template)
        if callable(apply_chat_template)
        else None
    )
    candidates: list[LocalModelStrategy] = []
    seen: set[tuple[str, str]] = set()

    def add_candidate(
        prompt_renderer: PromptRenderMode,
        thinking_control: ThinkingControlMode,
    ) -> None:
        if prompt_renderer is PromptRenderMode.CHAT_TEMPLATE_TEXT and signature is None:
            return
        if thinking_control is ThinkingControlMode.ENABLE_THINKING_FALSE and (
            signature is None or "enable_thinking" not in signature.parameters
        ):
            return
        if thinking_control is ThinkingControlMode.THINKING_FALSE and (
            signature is None or "thinking" not in signature.parameters
        ):
            return
        key = (prompt_renderer.value, thinking_control.value)
        if key in seen:
            return
        seen.add(key)
        candidates.append(
            current_strategy.model_copy(
                update={
                    "prompt_renderer": prompt_renderer,
                    "thinking_control": thinking_control,
                    "source": StrategySource.DISCOVERED,
                }
            )
        )

    add_candidate(
        current_strategy.prompt_renderer,
        current_strategy.thinking_control,
    )
    add_candidate(
        PromptRenderMode.CHAT_TEMPLATE_TEXT,
        ThinkingControlMode.ENABLE_THINKING_FALSE,
    )
    add_candidate(
        PromptRenderMode.CHAT_TEMPLATE_TEXT,
        ThinkingControlMode.THINKING_FALSE,
    )
    add_candidate(
        PromptRenderMode.CHAT_TEMPLATE_TEXT,
        ThinkingControlMode.NONE,
    )
    add_candidate(
        PromptRenderMode.BACKEND_DEFAULT,
        ThinkingControlMode.NONE,
    )
    return candidates


def strategy_key(*, backend: str, model: str, gguf_filename: str | None) -> str:
    """Return the stable exact key for one local model/backend combination."""
    artifact = (gguf_filename or "").strip()
    return "::".join((backend, model.strip(), artifact))


def _merge_store_entries(
    built_in_store: LocalModelStrategyStore,
    existing_store: LocalModelStrategyStore,
) -> LocalModelStrategyStore:
    merged: dict[str, LocalModelStrategy] = {
        strategy.key(): strategy
        for strategy in existing_store.strategies
        if strategy.source in {StrategySource.DISCOVERED, StrategySource.USER_OVERRIDE}
    }
    for strategy in built_in_store.strategies:
        key = strategy.key()
        existing = merged.get(key)
        if existing is not None and existing.source is StrategySource.USER_OVERRIDE:
            continue
        merged[key] = strategy
    strategies = sorted(merged.values(), key=lambda entry: entry.key())
    return LocalModelStrategyStore(version=STORE_VERSION, strategies=strategies)


def _store_needs_save(
    merged_store: LocalModelStrategyStore,
    existing_store: LocalModelStrategyStore,
) -> bool:
    return merged_store.model_dump(mode="json") != existing_store.model_dump(mode="json")


def _load_built_in_store() -> LocalModelStrategyStore:
    raw_text = (
        resources.files("ctxsift")
        .joinpath("local_model_strategy_catalog.json")
        .read_text(encoding="utf-8")
    )
    return LocalModelStrategyStore.model_validate_json(raw_text)


def _load_existing_store() -> LocalModelStrategyStore:
    path = strategy_store_path()
    if not path.exists():
        return LocalModelStrategyStore()
    try:
        return LocalModelStrategyStore.model_validate_json(path.read_text(encoding="utf-8"))
    except Exception as error:
        LOGGER.warning("Ignoring invalid local strategy store at %s: %s", path, error)
        return LocalModelStrategyStore()


def _save_strategy_store(path: Path, store: LocalModelStrategyStore) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(store.model_dump(mode="json"), indent=2, sort_keys=True) + "\n"
    temp_path = path.with_suffix(".tmp")
    temp_path.write_text(payload, encoding="utf-8")
    temp_path.replace(path)


def _stored_strategy_for_config(
    store: LocalModelStrategyStore,
    config: LocalModelConfig,
    *,
    backend: str,
) -> LocalModelStrategy | None:
    key = strategy_key_for_config(config, backend=backend)
    for strategy in store.strategies:
        if strategy.key() == key:
            return strategy
    return None


def _discover_strategy_from_tokenizer(
    config: LocalModelConfig,
    *,
    backend: str,
    tokenizer: Any | None,
) -> LocalModelStrategy | None:
    if tokenizer is None:
        return None
    apply_chat_template = getattr(tokenizer, "apply_chat_template", None)
    if not callable(apply_chat_template):
        return None
    signature = _safe_chat_template_signature(apply_chat_template)
    if signature is None:
        return None
    gguf_filename = (config.gguf_filename or "").strip() or None
    return LocalModelStrategy(
        backend=backend,
        model=config.model.strip(),
        gguf_filename=gguf_filename,
        thinking_control=_discovered_thinking_control(signature) or ThinkingControlMode.NONE,
        prompt_renderer=PromptRenderMode.CHAT_TEMPLATE_TEXT,
        decoding_mode=DecodingMode.DETERMINISTIC,
        source=StrategySource.DISCOVERED,
    )


def _safe_chat_template_signature(apply_chat_template: Any) -> Any | None:
    try:
        import inspect

        return inspect.signature(apply_chat_template)
    except (TypeError, ValueError):
        return None


def _discovered_thinking_control(signature: Any) -> ThinkingControlMode | None:
    if "enable_thinking" in signature.parameters:
        return ThinkingControlMode.ENABLE_THINKING_FALSE
    if "thinking" in signature.parameters:
        return ThinkingControlMode.THINKING_FALSE
    return None


def _persist_discovered_strategy(strategy: LocalModelStrategy) -> None:
    store = ensure_strategy_store()
    merged: dict[str, LocalModelStrategy] = {entry.key(): entry for entry in store.strategies}
    existing = merged.get(strategy.key())
    if existing is not None and existing.source is StrategySource.USER_OVERRIDE:
        return
    if merged.get(strategy.key()) == strategy:
        return
    merged[strategy.key()] = strategy
    updated_store = LocalModelStrategyStore(
        version=STORE_VERSION,
        strategies=sorted(merged.values(), key=lambda entry: entry.key()),
    )
    _save_strategy_store(strategy_store_path(), updated_store)


def _render_alpaca_instruction_prompt(messages: list[dict[str, str]]) -> str:
    user_parts: list[str] = []
    context_parts: list[str] = []
    for message in messages:
        role = message.get("role", "user").strip().casefold()
        content = message.get("content", "").strip()
        if not content:
            continue
        if role == "user":
            user_parts.append(content)
            continue
        if role == "system":
            context_parts.append(content)
            continue
        context_parts.append(f"{role.title()}:\n{content}")

    if user_parts:
        primary_instruction, primary_input = _split_alpaca_user_instruction(user_parts[0])
        instruction_text = primary_instruction
        input_chunks: list[str] = []
        if primary_input:
            input_chunks.append(primary_input)
        input_chunks.extend(user_parts[1:])
        input_chunks.extend(context_parts)
        input_text = "\n\n".join(chunk for chunk in input_chunks if chunk.strip()).strip()
    else:
        instruction_text = "\n\n".join(context_parts).strip()
        input_text = ""
    if input_text:
        return (
            "Below is an instruction that describes a task, paired with an input "
            "that provides further context. Write a response that appropriately "
            "completes the request.\n\n"
            f"### Instruction:\n{instruction_text}\n\n"
            f"### Input:\n{input_text}\n\n"
            "### Response:\n"
        )
    return (
        "Below is an instruction that describes a task. Write a response that "
        "appropriately completes the request.\n\n"
        f"### Instruction:\n{instruction_text}\n\n"
        "### Response:\n"
    )


def _split_alpaca_user_instruction(user_text: str) -> tuple[str, str]:
    normalized = user_text.strip()
    if not normalized.startswith("Instruction:"):
        return normalized, ""
    remainder = normalized[len("Instruction:") :].lstrip()
    if not remainder:
        return normalized, ""
    head, separator, tail = remainder.partition("\n\n")
    instruction_text = head.strip() or normalized
    input_text = tail.strip() if separator else ""
    return instruction_text, input_text


def strategy_key_for_config(config: LocalModelConfig, *, backend: str) -> str:
    """Return the exact lookup key for one runtime config."""
    gguf_filename: str | None = None
    if backend == "llama_cpp":
        gguf_filename = required_gguf_filename(config)
    return strategy_key(
        backend=backend,
        model=config.model.strip(),
        gguf_filename=gguf_filename,
    )
