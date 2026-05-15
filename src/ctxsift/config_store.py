"""Config storage, resolution, and rendering helpers."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from enum import Enum
from pathlib import Path
import tomllib
from typing import Any, Mapping

from platformdirs import user_config_path
from pydantic import TypeAdapter

from ctxsift.types import AppConfig, LocalQuantizationMode, ReasoningMode
from ctxsift.workspace import detect_workspace_context


class ConfigScope(str, Enum):
    """Supported config scopes."""

    GLOBAL = "global"
    WORKSPACE = "workspace"


@dataclass(frozen=True)
class ConfigKeySpec:
    """Validation metadata for a supported config key."""

    path: tuple[str, ...]
    adapter: TypeAdapter[Any]


@dataclass(frozen=True)
class GlobalConfigPaths:
    """Read and write paths for global config discovery."""

    read_path: Path
    legacy_path: Path
    write_path: Path


@dataclass(frozen=True)
class ConfigResolutionRequest:
    """Inputs used to resolve a config view."""

    cwd: Path | None = None
    force_global: bool = False
    cli_overrides: Mapping[str, Any] | None = None
    env: Mapping[str, str] | None = None


@dataclass(frozen=True)
class ConfigWriteRequest:
    """Inputs used to update one config key."""

    key: str
    raw_value: str
    cwd: Path | None = None
    force_global: bool = False
    env: Mapping[str, str] | None = None


@dataclass(frozen=True)
class ConfigSaveRequest:
    """Inputs used to persist one full config document."""

    config: AppConfig
    cwd: Path | None = None
    force_global: bool = False


@dataclass(frozen=True)
class ResolvedConfig:
    """Resolved config plus display metadata."""

    scope: ConfigScope
    read_path: Path
    write_path: Path
    file_exists: bool
    config: AppConfig


CONFIG_KEY_SPECS: dict[str, ConfigKeySpec] = {
    "timeout_ms": ConfigKeySpec(("timeout_ms",), TypeAdapter(int)),
    "retries": ConfigKeySpec(("retries",), TypeAdapter(int)),
    "max_output_tokens": ConfigKeySpec(("max_output_tokens",), TypeAdapter(int)),
    "db_path": ConfigKeySpec(("db_path",), TypeAdapter(str)),
    "remote.base_url": ConfigKeySpec(("remote", "base_url"), TypeAdapter(str)),
    "remote.api_key": ConfigKeySpec(("remote", "api_key"), TypeAdapter(str)),
    "remote.api_version": ConfigKeySpec(("remote", "api_version"), TypeAdapter(str)),
    "remote.model_name": ConfigKeySpec(("remote", "model_name"), TypeAdapter(str)),
    "remote.reasoning_mode": ConfigKeySpec(
        ("remote", "reasoning_mode"), TypeAdapter(ReasoningMode)
    ),
    "local.backend": ConfigKeySpec(("local", "backend"), TypeAdapter(str)),
    "local.model": ConfigKeySpec(("local", "model"), TypeAdapter(str)),
    "local.device": ConfigKeySpec(("local", "device"), TypeAdapter(str)),
    "local.dtype": ConfigKeySpec(("local", "dtype"), TypeAdapter(str)),
    "local.attn_implementation": ConfigKeySpec(
        ("local", "attn_implementation"),
        TypeAdapter(str),
    ),
    "local.quantization": ConfigKeySpec(
        ("local", "quantization"),
        TypeAdapter(LocalQuantizationMode),
    ),
    "embedding.model": ConfigKeySpec(("embedding", "model"), TypeAdapter(str)),
    "embedding.backend": ConfigKeySpec(("embedding", "backend"), TypeAdapter(str)),
    "embedding.device": ConfigKeySpec(("embedding", "device"), TypeAdapter(str)),
    "embedding.dtype": ConfigKeySpec(("embedding", "dtype"), TypeAdapter(str)),
    "embedding.attn_implementation": ConfigKeySpec(
        ("embedding", "attn_implementation"),
        TypeAdapter(str),
    ),
    "embedding.query_prompt_name": ConfigKeySpec(
        ("embedding", "query_prompt_name"),
        TypeAdapter(str),
    ),
    "embedding.query_prompt": ConfigKeySpec(
        ("embedding", "query_prompt"),
        TypeAdapter(str),
    ),
    "embedding.document_prompt_name": ConfigKeySpec(
        ("embedding", "document_prompt_name"),
        TypeAdapter(str),
    ),
    "embedding.max_length": ConfigKeySpec(("embedding", "max_length"), TypeAdapter(int)),
    "recall.default_limit": ConfigKeySpec(("recall", "default_limit"), TypeAdapter(int)),
    "recall.lexical_candidate_limit": ConfigKeySpec(
        ("recall", "lexical_candidate_limit"),
        TypeAdapter(int),
    ),
    "recall.vector_candidate_limit": ConfigKeySpec(
        ("recall", "vector_candidate_limit"),
        TypeAdapter(int),
    ),
    "recall.max_vector_distance": ConfigKeySpec(
        ("recall", "max_vector_distance"),
        TypeAdapter(float),
    ),
}


ENVIRONMENT_KEY_MAP: dict[str, tuple[str, ...]] = {
    "CTXSIFT_LLM_BASE_URL": ("remote", "base_url"),
    "CTXSIFT_LLM_API_KEY": ("remote", "api_key"),
    "CTXSIFT_LLM_API_VERSION": ("remote", "api_version"),
    "CTXSIFT_LLM_MODEL": ("remote", "model_name"),
    "CTXSIFT_LLM_REASONING_MODE": ("remote", "reasoning_mode"),
    "CTXSIFT_MAX_OUTPUT_TOKENS": ("max_output_tokens",),
    "CTXSIFT_TIMEOUT_MS": ("timeout_ms",),
    "CTXSIFT_RETRIES": ("retries",),
    "CTXSIFT_LOCAL_BACKEND": ("local", "backend"),
    "CTXSIFT_LOCAL_MODEL": ("local", "model"),
    "CTXSIFT_LOCAL_DEVICE": ("local", "device"),
    "CTXSIFT_LOCAL_DTYPE": ("local", "dtype"),
    "CTXSIFT_LOCAL_ATTN_IMPLEMENTATION": ("local", "attn_implementation"),
    "CTXSIFT_LOCAL_QUANTIZATION": ("local", "quantization"),
    "CTXSIFT_EMBEDDING_MODEL": ("embedding", "model"),
    "CTXSIFT_EMBEDDING_BACKEND": ("embedding", "backend"),
    "CTXSIFT_EMBEDDING_DEVICE": ("embedding", "device"),
    "CTXSIFT_EMBEDDING_DTYPE": ("embedding", "dtype"),
    "CTXSIFT_EMBEDDING_ATTN_IMPLEMENTATION": ("embedding", "attn_implementation"),
    "CTXSIFT_EMBEDDING_QUERY_PROMPT_NAME": ("embedding", "query_prompt_name"),
    "CTXSIFT_EMBEDDING_QUERY_PROMPT": ("embedding", "query_prompt"),
    "CTXSIFT_EMBEDDING_DOCUMENT_PROMPT_NAME": ("embedding", "document_prompt_name"),
    "CTXSIFT_EMBEDDING_MAX_LENGTH": ("embedding", "max_length"),
    "CTXSIFT_RECALL_DEFAULT_LIMIT": ("recall", "default_limit"),
    "CTXSIFT_RECALL_LEXICAL_CANDIDATE_LIMIT": ("recall", "lexical_candidate_limit"),
    "CTXSIFT_RECALL_VECTOR_CANDIDATE_LIMIT": ("recall", "vector_candidate_limit"),
    "CTXSIFT_RECALL_MAX_VECTOR_DISTANCE": ("recall", "max_vector_distance"),
    "CTXSIFT_DB_PATH": ("db_path",),
}


ENVIRONMENT_ADAPTERS: dict[str, TypeAdapter[Any]] = {
    "CTXSIFT_LLM_BASE_URL": TypeAdapter(str),
    "CTXSIFT_LLM_API_KEY": TypeAdapter(str),
    "CTXSIFT_LLM_API_VERSION": TypeAdapter(str),
    "CTXSIFT_LLM_MODEL": TypeAdapter(str),
    "CTXSIFT_LLM_REASONING_MODE": TypeAdapter(ReasoningMode),
    "CTXSIFT_MAX_OUTPUT_TOKENS": TypeAdapter(int),
    "CTXSIFT_TIMEOUT_MS": TypeAdapter(int),
    "CTXSIFT_RETRIES": TypeAdapter(int),
    "CTXSIFT_LOCAL_BACKEND": TypeAdapter(str),
    "CTXSIFT_LOCAL_MODEL": TypeAdapter(str),
    "CTXSIFT_LOCAL_DEVICE": TypeAdapter(str),
    "CTXSIFT_LOCAL_DTYPE": TypeAdapter(str),
    "CTXSIFT_LOCAL_ATTN_IMPLEMENTATION": TypeAdapter(str),
    "CTXSIFT_LOCAL_QUANTIZATION": TypeAdapter(LocalQuantizationMode),
    "CTXSIFT_EMBEDDING_MODEL": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_BACKEND": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_DEVICE": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_DTYPE": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_ATTN_IMPLEMENTATION": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_QUERY_PROMPT_NAME": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_QUERY_PROMPT": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_DOCUMENT_PROMPT_NAME": TypeAdapter(str),
    "CTXSIFT_EMBEDDING_MAX_LENGTH": TypeAdapter(int),
    "CTXSIFT_RECALL_DEFAULT_LIMIT": TypeAdapter(int),
    "CTXSIFT_RECALL_LEXICAL_CANDIDATE_LIMIT": TypeAdapter(int),
    "CTXSIFT_RECALL_VECTOR_CANDIDATE_LIMIT": TypeAdapter(int),
    "CTXSIFT_RECALL_MAX_VECTOR_DISTANCE": TypeAdapter(float),
    "CTXSIFT_DB_PATH": TypeAdapter(str),
}


def resolve_config(request: ConfigResolutionRequest) -> ResolvedConfig:
    """Resolve config for the requested scope."""
    scope = _selected_scope(request.force_global)
    paths = discover_global_config_paths()
    workspace = detect_workspace_context(request.cwd)
    resolved_layers = _resolved_layers(scope, paths, workspace, request.env)
    merged = _merge_config_layers(resolved_layers, request.cli_overrides)
    config = AppConfig.model_validate(merged)
    return ResolvedConfig(
        scope=scope,
        read_path=_read_path_for_scope(scope, paths, workspace),
        write_path=_write_path_for_scope(scope, paths, workspace),
        file_exists=_read_path_for_scope(scope, paths, workspace).exists(),
        config=config,
    )


def set_config_value(request: ConfigWriteRequest) -> ResolvedConfig:
    """Set a supported config key in the selected config file."""
    scope = _selected_scope(request.force_global)
    paths = discover_global_config_paths()
    workspace = detect_workspace_context(request.cwd)
    read_path = _read_path_for_scope(scope, paths, workspace)
    write_path = _write_path_for_scope(scope, paths, workspace)
    current_data = load_toml_file(read_path)
    updated_data = _set_supported_key(current_data, request.key, request.raw_value)
    validation_layers = _resolved_layers(scope, paths, workspace, request.env)
    if scope is ConfigScope.GLOBAL:
        validation_layers[1] = updated_data
    else:
        validation_layers[2] = updated_data
    merged = _merge_config_layers(validation_layers, None)
    AppConfig.model_validate(merged)
    save_toml_file(write_path, updated_data)
    return resolve_config(
        ConfigResolutionRequest(
            cwd=request.cwd,
            force_global=request.force_global,
            env=request.env,
        )
    )


def save_config(request: ConfigSaveRequest) -> ResolvedConfig:
    """Persist one full config document at the selected scope."""
    AppConfig.model_validate(request.config.model_dump(mode="json"))
    scope = _selected_scope(request.force_global)
    paths = discover_global_config_paths()
    workspace = detect_workspace_context(request.cwd)
    write_path = _write_path_for_scope(scope, paths, workspace)
    save_toml_file(write_path, request.config.model_dump(mode="json"))
    return resolve_config(
        ConfigResolutionRequest(
            cwd=request.cwd,
            force_global=request.force_global,
        )
    )


def render_resolved_config(result: ResolvedConfig) -> str:
    """Render a resolved config view for CLI output."""
    lines = [
        f"Scope: {result.scope.value}",
        f"Read path: {result.read_path}",
        f"Write path: {result.write_path}",
        "",
    ]
    redacted = _redacted_config_dict(result.config)
    lines.append(render_toml_document(redacted))
    return "\n".join(lines)


def discover_global_config_paths() -> GlobalConfigPaths:
    """Resolve global config read and write paths."""
    write_path = platform_global_config_path()
    legacy_path = legacy_global_config_path()
    if write_path.exists():
        read_path = write_path
    elif legacy_path.exists():
        read_path = legacy_path
    else:
        read_path = write_path
    return GlobalConfigPaths(read_path=read_path, legacy_path=legacy_path, write_path=write_path)


def platform_global_config_path() -> Path:
    """Return the platform-native global config path."""
    return user_config_path("ctxsift") / "config.toml"


def legacy_global_config_path() -> Path:
    """Return the legacy global config path."""
    return Path.home() / ".config" / "ctxsift" / "config.toml"


def load_toml_file(path: Path) -> dict[str, Any]:
    """Load a TOML file when it exists."""
    if not path.exists():
        return {}
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    return dict(data)


def save_toml_file(path: Path, data: Mapping[str, Any]) -> None:
    """Persist a TOML file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_toml_document(data), encoding="utf-8")


def render_toml_document(data: Mapping[str, Any]) -> str:
    """Render a flat-plus-one-level TOML document."""
    top_level: list[str] = []
    sections: list[str] = []
    for key, value in data.items():
        if isinstance(value, Mapping):
            section_lines = [f"[{key}]"]
            for nested_key, nested_value in value.items():
                section_lines.append(f"{nested_key} = {_toml_value(nested_value)}")
            sections.append("\n".join(section_lines))
            continue
        top_level.append(f"{key} = {_toml_value(value)}")
    blocks = [block for block in ("\n".join(top_level), "\n\n".join(sections)) if block]
    return "\n\n".join(blocks) + "\n"


def _toml_value(value: Any) -> str:
    if isinstance(value, Enum):
        return json.dumps(value.value)
    if value is None:
        return json.dumps("")
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    return json.dumps(value)


def _resolved_layers(
    scope: ConfigScope,
    global_paths: GlobalConfigPaths,
    workspace: Any,
    env: Mapping[str, str] | None,
) -> list[dict[str, Any]]:
    defaults = AppConfig().model_dump(mode="json")
    global_file = load_toml_file(global_paths.read_path)
    workspace_file = load_toml_file(Path(workspace.workspace_config_path))
    if scope is ConfigScope.GLOBAL:
        workspace_file = {}
    environment = environment_layer(env)
    return [defaults, global_file, workspace_file, environment]


def _merge_config_layers(
    layers: list[dict[str, Any]],
    cli_overrides: Mapping[str, Any] | None,
) -> dict[str, Any]:
    merged: dict[str, Any] = {}
    for layer in layers:
        merged = merge_dicts(merged, layer)
    if cli_overrides:
        merged = merge_dicts(merged, dict(cli_overrides))
    return merged


def merge_dicts(base: Mapping[str, Any], overlay: Mapping[str, Any]) -> dict[str, Any]:
    """Merge nested config dictionaries."""
    merged = dict(base)
    for key, value in overlay.items():
        if isinstance(value, Mapping) and isinstance(merged.get(key), Mapping):
            merged[key] = merge_dicts(merged[key], value)
            continue
        merged[key] = value
    return merged


def environment_layer(env: Mapping[str, str] | None = None) -> dict[str, Any]:
    """Build the environment override layer."""
    source = env or os.environ
    layer: dict[str, Any] = {}
    for env_name, path in ENVIRONMENT_KEY_MAP.items():
        raw_value = source.get(env_name)
        if raw_value is None:
            continue
        value = ENVIRONMENT_ADAPTERS[env_name].validate_python(raw_value)
        _assign_nested_value(layer, path, value)
    return layer


def _selected_scope(force_global: bool) -> ConfigScope:
    if force_global:
        return ConfigScope.GLOBAL
    return ConfigScope.WORKSPACE


def _read_path_for_scope(scope: ConfigScope, paths: GlobalConfigPaths, workspace: Any) -> Path:
    if scope is ConfigScope.GLOBAL:
        return paths.read_path
    return Path(workspace.workspace_config_path)


def _write_path_for_scope(scope: ConfigScope, paths: GlobalConfigPaths, workspace: Any) -> Path:
    if scope is ConfigScope.GLOBAL:
        return paths.write_path
    return Path(workspace.workspace_config_path)


def _set_supported_key(data: Mapping[str, Any], key: str, raw_value: str) -> dict[str, Any]:
    spec = CONFIG_KEY_SPECS.get(key)
    if spec is None:
        supported_keys = ", ".join(sorted(CONFIG_KEY_SPECS))
        raise ValueError(f"Unknown config key '{key}'. Supported keys: {supported_keys}")
    updated = merge_dicts({}, data)
    value = spec.adapter.validate_python(raw_value)
    _assign_nested_value(updated, spec.path, value)
    return updated


def _assign_nested_value(data: dict[str, Any], path: tuple[str, ...], value: Any) -> None:
    current = data
    for key in path[:-1]:
        nested = current.get(key)
        if not isinstance(nested, dict):
            nested = {}
            current[key] = nested
        current = nested
    current[path[-1]] = value


def _redacted_config_dict(config: AppConfig) -> dict[str, Any]:
    data = config.model_dump(mode="json")
    api_key = data["remote"]["api_key"]
    data["remote"]["api_key"] = _redact_secret(api_key)
    return data


def _redact_secret(secret: str) -> str:
    if not secret:
        return ""
    if len(secret) <= 4:
        return "*" * len(secret)
    return f"{secret[:3]}...{secret[-4:]}"
