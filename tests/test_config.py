"""Tests for config resolution and path discovery."""

from pathlib import Path

import pytest

from ctxsift import config_store
from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.types import AppConfig, LocalQuantizationMode, ReasoningMode
from ctxsift.workspace import detect_workspace_context


def test_app_config_defaults_are_stable() -> None:
    config = AppConfig()

    assert config.max_output_tokens == 512
    assert config.timeout_ms == 90000
    assert config.retries == 1
    assert config.remote.reasoning_mode is ReasoningMode.AUTO
    assert config.local.attn_implementation == "auto"
    assert config.local.quantization is LocalQuantizationMode.NONE
    assert config.embedding.backend == "auto"
    assert config.embedding.attn_implementation == "auto"
    assert config.embedding.query_prompt_name == ""
    assert config.embedding.query_prompt == ""
    assert config.recall.default_limit == 10
    assert config.recall.lexical_candidate_limit == 50
    assert config.recall.vector_candidate_limit == 50
    assert config.recall.max_vector_distance == 0.75


def test_reasoning_mode_rejects_invalid_values() -> None:
    with pytest.raises(ValueError):
        AppConfig.model_validate(
            {
                "remote": {
                    "reasoning_mode": "invalid",
                }
            }
        )


def test_global_config_prefers_platform_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    platform_path = tmp_path / "platform" / "config.toml"
    legacy_path = tmp_path / "legacy" / "config.toml"
    platform_path.parent.mkdir(parents=True)
    legacy_path.parent.mkdir(parents=True)
    platform_path.write_text("max_output_tokens = 640\n", encoding="utf-8")
    legacy_path.write_text("max_output_tokens = 320\n", encoding="utf-8")
    monkeypatch.setattr(config_store, "platform_global_config_path", lambda: platform_path)
    monkeypatch.setattr(config_store, "legacy_global_config_path", lambda: legacy_path)

    paths = config_store.discover_global_config_paths()

    assert paths.read_path == platform_path
    assert paths.write_path == platform_path


def test_global_config_falls_back_to_legacy_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    platform_path = tmp_path / "platform" / "config.toml"
    legacy_path = tmp_path / "legacy" / "config.toml"
    legacy_path.parent.mkdir(parents=True)
    legacy_path.write_text("max_output_tokens = 320\n", encoding="utf-8")
    monkeypatch.setattr(config_store, "platform_global_config_path", lambda: platform_path)
    monkeypatch.setattr(config_store, "legacy_global_config_path", lambda: legacy_path)

    paths = config_store.discover_global_config_paths()

    assert paths.read_path == legacy_path
    assert paths.write_path == platform_path


def test_git_workspace_path_uses_dot_git_ctxsift(tmp_path: Path) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    workspace = detect_workspace_context(repo_path)

    assert workspace.is_git_repo is True
    assert workspace.workspace_config_path.endswith(".git\\ctxsift\\config.toml")


def test_non_git_workspace_path_uses_ctxsift_directory(tmp_path: Path) -> None:
    workspace = detect_workspace_context(tmp_path)

    assert workspace.is_git_repo is False
    assert workspace.workspace_config_path.endswith(".ctxsift\\config.toml")


def test_config_resolution_uses_expected_precedence(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    workspace_path = tmp_path / "repo"
    git_dir = workspace_path / ".git"
    git_dir.mkdir(parents=True)
    workspace_config = git_dir / "ctxsift" / "config.toml"
    workspace_config.parent.mkdir(parents=True)
    workspace_config.write_text("max_output_tokens = 256\n", encoding="utf-8")
    platform_path = tmp_path / "platform" / "config.toml"
    platform_path.parent.mkdir(parents=True)
    platform_path.write_text("max_output_tokens = 128\n", encoding="utf-8")
    monkeypatch.setattr(config_store, "platform_global_config_path", lambda: platform_path)
    monkeypatch.setattr(
        config_store,
        "legacy_global_config_path",
        lambda: tmp_path / "legacy" / "config.toml",
    )

    result = resolve_config(
        ConfigResolutionRequest(
            cwd=workspace_path,
            env={"CTXSIFT_MAX_OUTPUT_TOKENS": "384"},
            cli_overrides={"max_output_tokens": 512},
        )
    )

    assert result.config.max_output_tokens == 512


def test_environment_layer_maps_supported_env_vars() -> None:
    layer = config_store.environment_layer(
        {
            "CTXSIFT_LLM_MODEL": "gpt-5-mini",
            "CTXSIFT_TIMEOUT_MS": "1234",
            "CTXSIFT_EMBEDDING_MODEL": "mini",
            "CTXSIFT_LOCAL_MODEL": "google/gemma-4-E2B-it",
            "CTXSIFT_LOCAL_ATTN_IMPLEMENTATION": "flash_attention_2",
            "CTXSIFT_LOCAL_QUANTIZATION": "quanto-int8",
            "CTXSIFT_EMBEDDING_QUERY_PROMPT_NAME": "web_search_query",
            "CTXSIFT_EMBEDDING_QUERY_PROMPT": "Instruct: custom\nQuery: ",
            "CTXSIFT_EMBEDDING_BACKEND": "onnx",
            "CTXSIFT_EMBEDDING_ATTN_IMPLEMENTATION": "sdpa",
            "CTXSIFT_RECALL_DEFAULT_LIMIT": "12",
            "CTXSIFT_RECALL_LEXICAL_CANDIDATE_LIMIT": "44",
            "CTXSIFT_RECALL_VECTOR_CANDIDATE_LIMIT": "33",
            "CTXSIFT_RECALL_MAX_VECTOR_DISTANCE": "0.61",
        }
    )

    assert layer["remote"]["model_name"] == "gpt-5-mini"
    assert layer["timeout_ms"] == 1234
    assert layer["local"]["model"] == "google/gemma-4-E2B-it"
    assert layer["local"]["attn_implementation"] == "flash_attention_2"
    assert layer["local"]["quantization"] is LocalQuantizationMode.QUANTO_INT8
    assert layer["embedding"]["model"] == "mini"
    assert layer["embedding"]["backend"] == "onnx"
    assert layer["embedding"]["attn_implementation"] == "sdpa"
    assert layer["embedding"]["query_prompt_name"] == "web_search_query"
    assert layer["embedding"]["query_prompt"] == "Instruct: custom\nQuery: "
    assert layer["recall"]["default_limit"] == 12
    assert layer["recall"]["lexical_candidate_limit"] == 44
    assert layer["recall"]["vector_candidate_limit"] == 33
    assert layer["recall"]["max_vector_distance"] == 0.61
