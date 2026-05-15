"""CLI tests for interactive configure."""

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


def test_configure_writes_workspace_scope_by_default(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    monkeypatch.chdir(repo_path)
    result = runner.invoke(app, ["configure"], input=_configure_input(remote_enabled=False))

    assert result.exit_code == 0
    workspace_config = repo_path / ".git" / "ctxsift" / "config.toml"
    assert workspace_config.exists()
    assert "Updated workspace config" in result.stdout
    text = workspace_config.read_text(encoding="utf-8")
    assert 'model = "google/gemma-4-E2B-it"' in text
    assert 'model = "microsoft/harrier-oss-v1-0.6b"' in text


def test_configure_global_writes_remote_values(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["configure", "--global"], input=_configure_input(remote_enabled=True))

    assert result.exit_code == 0
    assert isolated_config_paths.exists()
    text = isolated_config_paths.read_text(encoding="utf-8")
    assert 'base_url = "http://localhost:4000"' in text
    assert 'model_name = "gpt-4o-mini"' in text
    assert 'api_version = "2025-01-01"' in text


def test_configure_rejects_invalid_final_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(
        app,
        ["configure", "--global"],
        input=_configure_input(remote_enabled=False, recall_default_limit="0"),
    )

    assert result.exit_code != 0
    assert "greater than or equal to 1" in result.output


def _configure_input(
    remote_enabled: bool,
    recall_default_limit: str = "10",
) -> str:
    values = [
        "512",
        "90000",
        "1",
        "transformers",
        "google/gemma-4-E2B-it",
        "cpu",
        "auto",
        "y" if remote_enabled else "n",
    ]
    if remote_enabled:
        values.extend(
            [
                "http://localhost:4000",
                "gpt-4o-mini",
                "sk-test",
                "2025-01-01",
                "auto",
                "remote",
            ]
        )
    values.extend(
        [
            "microsoft/harrier-oss-v1-0.6b",
            "cpu",
            "auto",
            "",
            "",
            "",
            "32768",
            recall_default_limit,
            "50",
            "50",
            "",
        ]
    )
    return "\n".join(values) + "\n"
