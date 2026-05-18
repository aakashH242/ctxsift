"""Interactive configure flow helpers."""

from __future__ import annotations

from pathlib import Path

from pydantic import TypeAdapter
import typer

from ctxsift.config_store import ConfigScope
from ctxsift.types import (
    AppConfig,
    ReasoningMode,
    RemoteModelConfig,
)

CPU_RECOMMENDED_LOCAL_MODEL = "HuggingFaceTB/SmolLM2-360M-Instruct"
CPU_RECOMMENDED_LOCAL_GGUF_REPO = "ibm-granite/granite-4.0-350m-GGUF"
CPU_RECOMMENDED_LOCAL_GGUF_FILENAME = "smollm2-360m-instruct-q8_0.gguf"
GPU_RECOMMENDED_LOCAL_MODEL = "Qwen/Qwen3.5-0.8B"
LEGACY_LOCAL_MODEL_DEFAULT = "google/gemma-4-E2B-it"
AUTO_LOCAL_MODEL_DEFAULTS = {
    LEGACY_LOCAL_MODEL_DEFAULT,
    CPU_RECOMMENDED_LOCAL_MODEL,
    CPU_RECOMMENDED_LOCAL_GGUF_REPO,
    GPU_RECOMMENDED_LOCAL_MODEL,
}


def prompt_for_config(current: AppConfig) -> AppConfig:
    """Collect one full config interactively using current values as defaults."""
    compression_mode = _prompt_choice(
        "Compression mode",
        _current_compression_mode(current),
        ["local", "remote"],
    )
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
    local = _local_config_for_mode(current, compression_mode)
    remote = _remote_config_for_mode(current, compression_mode)
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
            "local": local.model_dump(mode="json"),
            "embedding": {
                "model": embedding_model,
                "backend": current.embedding.backend,
                "device": embedding_device,
                "dtype": embedding_dtype,
                "attn_implementation": current.embedding.attn_implementation,
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


def _local_config_for_mode(current: AppConfig, compression_mode: str):
    if compression_mode == "remote":
        return current.local
    cuda_available = _cuda_available()
    local_device = _prompt_choice(
        _local_device_prompt(cuda_available),
        _default_local_device(current.local.device, current.local.model, cuda_available),
        _local_device_choices(cuda_available),
    )
    if _uses_cpu_llama_runtime(local_device):
        typer.echo(
            "CPU local compression uses embedded llama.cpp. "
            "Use a Hugging Face GGUF repo id for the model, then choose one GGUF filename "
            "from that repo's Files tab. CtxSift will download the artifact for you."
        )
    local_model = typer.prompt(
        _local_model_prompt(local_device),
        default=_default_local_model(current.local.model, local_device),
    )
    local_gguf_filename = _default_local_gguf_filename(
        current.local.gguf_filename,
        current.local.model,
        local_model,
        local_device,
    )
    if _uses_cpu_llama_runtime(local_device):
        local_gguf_filename = typer.prompt(
            "Local GGUF filename (from that repo's Files tab)",
            default=local_gguf_filename,
        )
    else:
        local_gguf_filename = None
    local_model_cache_path = typer.prompt(
        "Local model cache path override (leave blank for default cache)",
        default=current.local.model_cache_path or "",
        show_default=bool(current.local.model_cache_path),
    )
    local_dtype = typer.prompt(
        "Local dtype",
        default=current.local.dtype,
    )
    return current.local.model_validate(
        {
            **current.local.model_dump(mode="json"),
            "model": local_model,
            "gguf_filename": local_gguf_filename,
            "device": local_device,
            "model_cache_path": local_model_cache_path or None,
            "dtype": local_dtype,
        }
    )


def _remote_config_for_mode(current: AppConfig, compression_mode: str) -> RemoteModelConfig:
    if compression_mode == "local":
        return RemoteModelConfig()
    return _prompt_remote_config(current.remote, remote_enabled=True)


def prompt_for_save_scope(workspace_path: Path, global_path: Path) -> ConfigScope:
    """Ask where the collected config should be written."""
    typer.echo("")
    typer.echo("Save config to:")
    typer.echo(f"  workspace: {workspace_path}")
    typer.echo(f"  global:    {global_path}")
    while True:
        raw_value = typer.prompt(
            "Save target (workspace/global, default global)",
            default="global",
        ).strip().casefold()
        if raw_value in {"global", "g"}:
            return ConfigScope.GLOBAL
        if raw_value in {"workspace", "w"}:
            return ConfigScope.WORKSPACE
        typer.echo("Invalid value. Choose `workspace` or `global`.", err=True)


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


def _prompt_choice(prompt: str, current: str, choices: list[str]) -> str:
    default_value = _default_choice(current, choices)
    canonical_choices = {choice.casefold(): choice for choice in choices}
    choice_list = ", ".join(choices)
    while True:
        raw_value = typer.prompt(f"{prompt} ({choice_list})", default=default_value)
        selected = canonical_choices.get(raw_value.strip().casefold())
        if selected is not None:
            return selected
        typer.echo(f"Invalid value. Choose one of: {choice_list}", err=True)


def _default_choice(current: str, choices: list[str]) -> str:
    normalized_choices = {choice.casefold(): choice for choice in choices}
    return normalized_choices.get(current.strip().casefold(), choices[0])


def _current_compression_mode(current: AppConfig) -> str:
    if current.remote.base_url.strip():
        return "remote"
    return "local"


def _local_device_prompt(cuda_available: bool) -> str:
    if cuda_available:
        return "Local device (GPU detected)"
    return "Local device (CPU only detected)"


def _local_device_choices(cuda_available: bool) -> list[str]:
    if cuda_available:
        return ["cuda", "cpu"]
    return ["cpu"]


def _default_local_device(current_device: str, current_model: str, cuda_available: bool) -> str:
    normalized = current_device.strip().casefold()
    if normalized.startswith("cuda") and cuda_available:
        return "cuda"
    if (
        normalized == "cpu"
        and cuda_available
        and current_model in AUTO_LOCAL_MODEL_DEFAULTS
    ):
        return "cuda"
    if normalized == "cpu":
        return "cpu"
    if cuda_available:
        return "cuda"
    return "cpu"


def _local_model_prompt(local_device: str) -> str:
    recommendation = _recommended_local_model(local_device)
    if _uses_cpu_llama_runtime(local_device):
        return f"Local model repo (GGUF repo id, recommended: {recommendation})"
    return f"Local model (recommended: {recommendation})"


def _default_local_model(current_model: str, local_device: str) -> str:
    if not current_model or current_model in AUTO_LOCAL_MODEL_DEFAULTS:
        return _recommended_local_model(local_device)
    return current_model


def _recommended_local_model(local_device: str) -> str:
    if local_device.strip().casefold().startswith("cuda"):
        return GPU_RECOMMENDED_LOCAL_MODEL
    return CPU_RECOMMENDED_LOCAL_GGUF_REPO


def _default_local_gguf_filename(
    current_filename: str | None,
    current_model: str,
    selected_model: str,
    local_device: str,
) -> str:
    if not _uses_cpu_llama_runtime(local_device):
        return ""
    if current_filename and selected_model == current_model:
        return current_filename
    if selected_model == CPU_RECOMMENDED_LOCAL_GGUF_REPO:
        return CPU_RECOMMENDED_LOCAL_GGUF_FILENAME
    return current_filename or ""


def _uses_cpu_llama_runtime(local_device: str) -> bool:
    return not local_device.strip().casefold().startswith("cuda")


def _cuda_available() -> bool:
    try:
        import torch
    except ImportError:
        return False
    return bool(torch.cuda.is_available())
