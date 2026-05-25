"""Interactive configure flow helpers."""

from __future__ import annotations

from pathlib import Path

from pydantic import TypeAdapter
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
import typer

from ctxsift.config.store import ConfigScope
from ctxsift.models.hf_hub_cache import default_hf_cache_dir
from ctxsift.models.quantized_model_cache import default_quantized_cache_root
from ctxsift.types import (
    AppConfig,
    ReasoningMode,
    RemoteModelConfig,
)

CPU_RECOMMENDED_LOCAL_MODEL = "ibm-granite/granite-4.0-350m-GGUF"
CPU_RECOMMENDED_LOCAL_GGUF_REPO = "ibm-granite/granite-4.0-350m-GGUF"
CPU_RECOMMENDED_LOCAL_GGUF_FILENAME = "granite-4.0-350m-Q8_0.gguf"
GPU_RECOMMENDED_LOCAL_MODEL = "LiquidAI/LFM2.5-1.2B-Instruct"
LEGACY_LOCAL_MODEL_DEFAULT = "google/gemma-4-E2B-it"
AUTO_LOCAL_MODEL_DEFAULTS = {
    LEGACY_LOCAL_MODEL_DEFAULT,
    CPU_RECOMMENDED_LOCAL_MODEL,
    CPU_RECOMMENDED_LOCAL_GGUF_REPO,
    GPU_RECOMMENDED_LOCAL_MODEL,
}
console = Console()


def prompt_for_config(current: AppConfig) -> AppConfig:
    """Collect one full config interactively using current values as defaults."""
    _render_configure_header()
    _render_section("Compression")
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
    _render_note(
        "Unsure? Keep recovery enabled and run a benchmark with your desired model to find whether it helps or not.",
        title="Response recovery",
    )
    recovery_enabled = typer.confirm(
        "Keep deterministic response recovery enabled?",
        default=current.recovery_enabled,
    )
    local = _local_config_for_mode(current, compression_mode)
    remote = _remote_config_for_mode(current, compression_mode)
    _render_section("Embeddings")
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
    _render_section("Recall")
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
    recall_min_score = typer.prompt(
        "Recall minimum score",
        default=current.recall.min_score,
        type=int,
    )
    weak_fallback_min_score = typer.prompt(
        "Recall weak fallback minimum score",
        default=current.recall.weak_fallback_min_score,
        type=int,
    )
    weak_fallback_limit = typer.prompt(
        "Recall weak fallback limit",
        default=current.recall.weak_fallback_limit,
        type=int,
    )
    return AppConfig.model_validate(
        {
            "timeout_ms": timeout_ms,
            "retries": retries,
            "max_output_tokens": max_output_tokens,
            "recovery_enabled": recovery_enabled,
            "db_path": None,
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
                "min_score": recall_min_score,
                "weak_fallback_min_score": weak_fallback_min_score,
                "weak_fallback_limit": weak_fallback_limit,
            },
        }
    )


def _local_config_for_mode(current: AppConfig, compression_mode: str):
    if compression_mode == "remote":
        return current.local
    _render_section("Local Compression")
    cuda_available = _cuda_available()
    local_device = _prompt_choice(
        _local_device_prompt(cuda_available),
        _default_local_device(current.local.device, current.local.model, cuda_available),
        _local_device_choices(cuda_available),
    )
    if _uses_cpu_llama_runtime(local_device):
        _render_note(
            "CPU local compression uses embedded llama.cpp.\n"
            "Use a Hugging Face GGUF repo id for the model, then choose one GGUF filename "
            "from that repo's Files tab. CtxSift will download the artifact for you.",
            title="CPU local compression",
        )
    local_model = typer.prompt(
        _local_model_prompt(local_device),
        default=_default_local_model(current.local.model, local_device),
    )
    local_gguf_filename: str | None = _default_local_gguf_filename(
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
    _render_model_cache_note(current.local.model_cache_path)
    local_model_cache_path = typer.prompt(
        "Local model cache path override",
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
    _render_section("Remote Compression")
    return _prompt_remote_config(current.remote, remote_enabled=True)


def prompt_for_save_scope(workspace_path: Path, global_path: Path) -> ConfigScope:
    """Ask where the collected config should be written."""
    _render_section("Save Target")
    table = Table(show_header=True, header_style="bold", box=None, padding=(0, 1))
    table.add_column("Scope", style="bold")
    table.add_column("Path")
    table.add_row("workspace", str(workspace_path))
    table.add_row("global", str(global_path))
    console.print(table)
    while True:
        raw_value = (
            typer.prompt(
                "Save target (workspace/global, default global)",
                default="global",
            )
            .strip()
            .casefold()
        )
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
    if normalized == "cpu" and cuda_available and current_model in AUTO_LOCAL_MODEL_DEFAULTS:
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


def _render_model_cache_note(configured_path: str | None) -> None:
    configured = (configured_path or "").strip()
    if configured:
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("Label", style="bold")
        table.add_column("Value")
        table.add_row("Current local model cache root", configured)
        table.add_row(
            "Behavior",
            "Leave blank only if you want to clear the override and go back to the defaults.",
        )
        console.print(Panel(table, title="Model Cache", border_style="cyan"))
        return
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column("Label", style="bold")
    table.add_column("Value")
    table.add_row(
        "Purpose",
        "Local model cache root controls where downloaded local model artifacts are cached.",
    )
    table.add_row("Default Hugging Face cache", str(default_hf_cache_dir()))
    table.add_row("Default quantized model cache", str(default_quantized_cache_root()))
    table.add_row(
        "Behavior",
        "Leave blank to keep using those defaults, or enter one directory to override them.",
    )
    console.print(Panel(table, title="Model Cache", border_style="cyan"))


def _render_configure_header() -> None:
    console.print(
        Panel(
            "Set compression, recall, embedding, and storage defaults for this machine or workspace.",
            title="CtxSift Configure",
            border_style="cyan",
        )
    )


def _render_section(title: str) -> None:
    console.print(Rule(title, style="cyan"))


def _render_note(message: str, title: str) -> None:
    console.print(Panel(message, title=title, border_style="yellow"))
