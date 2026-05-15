"""CLI tests for the config command group."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from ctxsift import config_store
from ctxsift.cli import app


runner = CliRunner()


@pytest.fixture()
def isolated_config_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Path:
    platform_path = tmp_path / "platform" / "config.toml"
    legacy_path = tmp_path / "legacy" / "config.toml"
    monkeypatch.setattr(config_store, "platform_global_config_path", lambda: platform_path)
    monkeypatch.setattr(config_store, "legacy_global_config_path", lambda: legacy_path)
    return platform_path


def test_config_show_reports_workspace_scope(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    monkeypatch.chdir(repo_path)

    result = runner.invoke(app, ["config", "show"])

    assert result.exit_code == 0
    assert "Scope: workspace" in result.stdout
    assert ".git" in result.stdout


def test_config_set_writes_global_file_and_show_reads_it(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    set_result = runner.invoke(app, ["config", "set", "max_output_tokens", "768", "--global"])
    show_result = runner.invoke(app, ["config", "show", "--global"])

    assert set_result.exit_code == 0
    assert show_result.exit_code == 0
    assert "max_output_tokens = 768" in show_result.stdout
    assert isolated_config_paths.exists()


def test_config_show_redacts_secret_values(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    runner.invoke(app, ["config", "set", "remote.api_key", "sk-secret-token", "--global"])

    result = runner.invoke(app, ["config", "show", "--global"])

    assert result.exit_code == 0
    assert "sk-secret-token" not in result.stdout
    assert "sk-...oken" in result.stdout


def test_config_set_rejects_unknown_keys(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["config", "set", "unknown.key", "value", "--global"])

    assert result.exit_code != 0
    assert "Unknown config key" in result.output


def test_config_set_rejects_invalid_values(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["config", "set", "remote.reasoning_mode", "maybe", "--global"])

    assert result.exit_code != 0
    assert "Input should be" in result.output


def test_config_set_rejects_non_positive_recall_limit(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["config", "set", "recall.default_limit", "0", "--global"])

    assert result.exit_code != 0
    assert "greater than or equal to 1" in result.output


def test_config_show_global_override_skips_workspace_scope(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    monkeypatch.chdir(repo_path)

    result = runner.invoke(app, ["config", "show", "--global"])

    assert result.exit_code == 0
    assert "Scope: global" in result.stdout


def test_config_set_supports_recall_limit_keys(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    set_result = runner.invoke(app, ["config", "set", "recall.default_limit", "15", "--global"])
    show_result = runner.invoke(app, ["config", "show", "--global"])

    assert set_result.exit_code == 0
    assert "default_limit = 15" in show_result.stdout
