"""CLI tests for workspace initialization."""

from pathlib import Path

from typer.testing import CliRunner

from ctxsift.cli import app


runner = CliRunner()


def test_init_creates_workspace_database_in_git_repo(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    monkeypatch.chdir(repo_path)

    result = runner.invoke(app, ["init"])

    assert result.exit_code == 0
    assert "Initialized workspace database" in result.stdout
    assert (repo_path / ".git" / "ctxsift" / "ctxsift.db").exists()


def test_init_acknowledges_write_ignore_without_editing_files(
    tmp_path: Path,
    monkeypatch,
) -> None:
    workspace_path = tmp_path / "workspace"
    workspace_path.mkdir(parents=True)
    monkeypatch.chdir(workspace_path)

    result = runner.invoke(app, ["init", "--write-ignore"])

    assert result.exit_code == 0
    assert "no ignore files were changed" in result.stdout
    assert (workspace_path / ".ctxsift" / "ctxsift.db").exists()
