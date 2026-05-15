"""CLI tests for workspace initialization."""

from dataclasses import dataclass
from pathlib import Path

import pytest
from typer.testing import CliRunner

import ctxsift.cli as cli
from ctxsift.cli import app


runner = CliRunner()


@dataclass(frozen=True)
class FakeDoctorReport:
    checks: list[object]


@pytest.fixture()
def fast_doctor_report(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_collect_doctor_report(cwd):
        return FakeDoctorReport(checks=[])

    monkeypatch.setattr(cli, "collect_doctor_report", fake_collect_doctor_report)
    monkeypatch.setattr(cli, "render_doctor_report", lambda report: "[required] sqlite_fts5: ok - FTS5 is available.")


def test_init_creates_workspace_database_in_git_repo(
    tmp_path: Path,
    monkeypatch,
    fast_doctor_report,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    monkeypatch.chdir(repo_path)

    result = runner.invoke(app, ["init"])

    assert result.exit_code == 0
    assert "Initialized workspace database" in result.stdout
    assert "[required] sqlite_fts5: ok" in result.stdout
    assert (repo_path / ".git" / "ctxsift" / "ctxsift.db").exists()


def test_init_write_ignore_skips_git_repo_ignore_edits(
    tmp_path: Path,
    monkeypatch,
    fast_doctor_report,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    monkeypatch.chdir(repo_path)

    result = runner.invoke(app, ["init", "--write-ignore"])

    assert result.exit_code == 0
    assert "No ignore update needed" in result.stdout
    assert not (repo_path / ".gitignore").exists()


def test_init_write_ignore_updates_non_git_workspace(
    tmp_path: Path,
    monkeypatch,
    fast_doctor_report,
) -> None:
    workspace_path = tmp_path / "workspace"
    workspace_path.mkdir(parents=True)
    monkeypatch.chdir(workspace_path)

    result = runner.invoke(app, ["init", "--write-ignore"])

    assert result.exit_code == 0
    assert "Updated" in result.stdout
    assert (workspace_path / ".ctxsift" / "ctxsift.db").exists()
    assert (workspace_path / ".gitignore").read_text(encoding="utf-8") == ".ctxsift/\n"


def test_init_write_ignore_is_idempotent_in_non_git_workspace(
    tmp_path: Path,
    monkeypatch,
    fast_doctor_report,
) -> None:
    workspace_path = tmp_path / "workspace"
    workspace_path.mkdir(parents=True)
    (workspace_path / ".gitignore").write_text(".ctxsift/\n", encoding="utf-8")
    monkeypatch.chdir(workspace_path)

    result = runner.invoke(app, ["init", "--write-ignore"])

    assert result.exit_code == 0
    assert "already contains .ctxsift/" in result.stdout
    assert (workspace_path / ".gitignore").read_text(encoding="utf-8") == ".ctxsift/\n"
