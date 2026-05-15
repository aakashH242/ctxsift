"""Interactive configure flow helpers."""

from __future__ import annotations

from pydantic import TypeAdapter
import typer

from ctxsift.types import (
    AppConfig,
    LocalQuantizationMode,
    ReasoningMode,
    RemoteModelConfig,
)


def prompt_for_config(current: AppConfig) -> AppConfig:
    """Collect one full config interactively using current values as defaults."""
    max_output_tokens = typer.prompt(
        "Max output tokens",
        default=current.max_output_tokens,
        type=int,
    )
    timeout_ms = typer.prompt(
        "Timeout (ms)",
        default=current.timeout_ms,
        type=int,
    )
    retries = typer.prompt(
        "Retries",
        default=current.retries,
        type=int,
    )
    local_backend = typer.prompt(
        "Local backend",
        default=current.local.backend,
    )
    local_model = typer.prompt(
        "Local model",
        default=current.local.model,
    )
    local_device = typer.prompt(
        "Local device",
        default=current.local.device,
    )
    local_dtype = typer.prompt(
        "Local dtype",
        default=current.local.dtype,
    )
    local_attention = typer.prompt(
        "Local attention backend",
        default=current.local.attn_implementation,
    )
    local_quantization = _prompt_enum(
        "Local quantization",
        current.local.quantization,
        TypeAdapter(LocalQuantizationMode),
    )
    remote_enabled = typer.confirm(
        "Enable remote LiteLLM backend?",
        default=bool(current.remote.base_url.strip()),
    )
    remote = _prompt_remote_config(current.remote, remote_enabled)
    embedding_model = typer.prompt(
        "Embedding model",
        default=current.embedding.model,
    )
    embedding_device = typer.prompt(
        "Embedding device",
        default=current.embedding.device,
    )
    embedding_dtype = typer.prompt(
        "Embedding dtype",
        default=current.embedding.dtype,
    )
    embedding_backend = typer.prompt(
        "Embedding backend",
        default=current.embedding.backend,
    )
    embedding_attention = typer.prompt(
        "Embedding attention backend",
        default=current.embedding.attn_implementation,
    )
    query_prompt_name = typer.prompt(
        "Embedding query prompt name",
        default=current.embedding.query_prompt_name,
        show_default=bool(current.embedding.query_prompt_name),
    )
    query_prompt = typer.prompt(
        "Embedding query prompt",
        default=current.embedding.query_prompt,
        show_default=bool(current.embedding.query_prompt),
    )
    document_prompt_name = typer.prompt(
        "Embedding document prompt name",
        default=current.embedding.document_prompt_name,
        show_default=bool(current.embedding.document_prompt_name),
    )
    embedding_max_length = typer.prompt(
        "Embedding max length",
        default=current.embedding.max_length,
        type=int,
    )
    recall_default_limit = typer.prompt(
        "Recall default limit",
        default=current.recall.default_limit,
        type=int,
    )
    lexical_candidate_limit = typer.prompt(
        "Recall lexical candidate limit",
        default=current.recall.lexical_candidate_limit,
        type=int,
    )
    vector_candidate_limit = typer.prompt(
        "Recall vector candidate limit",
        default=current.recall.vector_candidate_limit,
        type=int,
    )
    max_vector_distance = typer.prompt(
        "Recall max vector distance",
        default=current.recall.max_vector_distance,
        type=float,
    )
    db_path = typer.prompt(
        "Database path override",
        default=current.db_path or "",
        show_default=bool(current.db_path),
    )
    return AppConfig.model_validate(
        {
            "timeout_ms": timeout_ms,
            "retries": retries,
            "max_output_tokens": max_output_tokens,
            "db_path": db_path or None,
            "remote": remote.model_dump(mode="json"),
            "local": {
                "backend": local_backend,
                "model": local_model,
                "device": local_device,
                "dtype": local_dtype,
                "attn_implementation": local_attention,
                "quantization": local_quantization,
            },
            "embedding": {
                "model": embedding_model,
                "backend": embedding_backend,
                "device": embedding_device,
                "dtype": embedding_dtype,
                "attn_implementation": embedding_attention,
                "query_prompt_name": query_prompt_name,
                "query_prompt": query_prompt,
                "document_prompt_name": document_prompt_name,
                "max_length": embedding_max_length,
            },
            "recall": {
                "default_limit": recall_default_limit,
                "lexical_candidate_limit": lexical_candidate_limit,
                "vector_candidate_limit": vector_candidate_limit,
                "max_vector_distance": max_vector_distance,
            },
        }
    )


def _prompt_remote_config(current: RemoteModelConfig, remote_enabled: bool) -> RemoteModelConfig:
    if not remote_enabled:
        return RemoteModelConfig()
    base_url = typer.prompt(
        "Remote base URL",
        default=current.base_url,
    )
    model_name = typer.prompt(
        "Remote model name",
        default=current.model_name,
    )
    api_key = typer.prompt(
        "Remote API key (leave blank to keep current value)",
        default="",
        hide_input=True,
        show_default=False,
    )
    api_version = typer.prompt(
        "Remote API version",
        default=current.api_version,
        show_default=bool(current.api_version),
    )
    reasoning_mode = _prompt_enum(
        "Remote reasoning mode",
        current.reasoning_mode,
        TypeAdapter(ReasoningMode),
    )
    return RemoteModelConfig.model_validate(
        {
            "base_url": base_url,
            "api_key": api_key or current.api_key,
            "api_version": api_version,
            "model_name": model_name,
            "reasoning_mode": reasoning_mode,
        }
    )
def _prompt_enum(prompt: str, current, adapter: TypeAdapter) -> str:
    default_value = current.value
    while True:
        raw_value = typer.prompt(prompt, default=default_value)
        try:
            return adapter.validate_python(raw_value).value
        except Exception as error:
            typer.echo(f"Invalid value: {error}", err=True)
