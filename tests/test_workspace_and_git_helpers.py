"""Tests for workspace discovery, git file status, and timestamp helpers."""

from __future__ import annotations

import asyncio
from datetime import timezone
from pathlib import Path

import pytest

from ctxsift.git_file_status import _parse_git_file_status, read_git_file_status
from ctxsift.shared.timestamps import parse_created_at
from ctxsift.workspace.discovery import (
    _find_git_root,
    _read_gitdir_pointer,
    _resolve_git_directory,
    detect_workspace_context,
)


class FakeAsyncProcess:
    """Async subprocess stub."""

    def __init__(self, returncode: int, stdout: bytes = b"") -> None:
        self.returncode = returncode
        self._stdout = stdout

    async def communicate(self) -> tuple[bytes, bytes]:
        return self._stdout, b""


def test_detect_workspace_context_uses_ctxsift_directory_for_non_git_workspace(
    tmp_path: Path,
) -> None:
    context = detect_workspace_context(tmp_path)

    assert context.is_git_repo is False
    assert Path(context.workspace_config_path) == tmp_path / ".ctxsift" / "config.toml"
    assert context.db_path is not None
    assert Path(context.db_path) == tmp_path / ".ctxsift" / "ctxsift.db"


def test_detect_workspace_context_uses_git_directory_for_repo_workspace(tmp_path: Path) -> None:
    git_dir = tmp_path / ".git"
    git_dir.mkdir()

    context = detect_workspace_context(tmp_path)

    assert context.is_git_repo is True
    assert context.git_dir == str(git_dir.resolve())
    assert Path(context.workspace_config_path) == git_dir.resolve() / "ctxsift" / "config.toml"


def test_find_git_root_walks_up_parent_directories(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    nested = repo_root / "src" / "pkg"
    nested.mkdir(parents=True)
    (repo_root / ".git").mkdir()

    git_root = _find_git_root(nested)

    assert git_root == repo_root


def test_resolve_git_directory_supports_pointer_file(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    actual_git_dir = tmp_path / "actual.git"
    actual_git_dir.mkdir()
    (repo_root / ".git").write_text(f"gitdir: {actual_git_dir}\n", encoding="utf-8")

    resolved = _resolve_git_directory(repo_root)

    assert resolved == actual_git_dir.resolve()


def test_resolve_git_directory_raises_for_missing_git_entry(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="Could not resolve"):
        _resolve_git_directory(tmp_path)


def test_read_gitdir_pointer_supports_relative_target(tmp_path: Path) -> None:
    git_file = tmp_path / ".git"
    target = tmp_path / ".git-data"
    target.mkdir()
    git_file.write_text("gitdir: .git-data\n", encoding="utf-8")

    resolved = _read_gitdir_pointer(git_file)

    assert resolved == target.resolve()


def test_read_gitdir_pointer_rejects_unknown_format(tmp_path: Path) -> None:
    git_file = tmp_path / ".git"
    git_file.write_text("not-a-pointer\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported .git file format"):
        _read_gitdir_pointer(git_file)


def test_parse_git_file_status_reports_clean_file() -> None:
    status = _parse_git_file_status("src/app.py", "")

    assert status.is_changed is False
    assert status.is_deleted is False
    assert status.raw_status is None


def test_parse_git_file_status_reports_deleted_file() -> None:
    status = _parse_git_file_status("src/app.py", " D src/app.py\n")

    assert status.is_changed is True
    assert status.is_deleted is True
    assert status.raw_status == " D"


def test_read_git_file_status_returns_none_without_git_repo(tmp_path: Path) -> None:
    status = asyncio.run(read_git_file_status(tmp_path, "src/app.py"))

    assert status is None


def test_read_git_file_status_returns_none_when_git_is_missing(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    (tmp_path / ".git").mkdir()

    async def fake_create_subprocess_exec(*args, **kwargs):
        del args, kwargs
        raise FileNotFoundError

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_create_subprocess_exec)

    status = asyncio.run(read_git_file_status(tmp_path, "src/app.py"))

    assert status is None


def test_read_git_file_status_returns_none_on_non_zero_exit(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    (tmp_path / ".git").mkdir()

    async def fake_create_subprocess_exec(*args, **kwargs):
        del args, kwargs
        return FakeAsyncProcess(returncode=1, stdout=b" M src/app.py")

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_create_subprocess_exec)

    status = asyncio.run(read_git_file_status(tmp_path, "src/app.py"))

    assert status is None


def test_read_git_file_status_parses_success_output(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    (tmp_path / ".git").mkdir()

    async def fake_create_subprocess_exec(*args, **kwargs):
        del args, kwargs
        return FakeAsyncProcess(returncode=0, stdout=b" M src/app.py\n")

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_create_subprocess_exec)

    status = asyncio.run(read_git_file_status(tmp_path, "src/app.py"))

    assert status is not None and status.is_changed is True and status.raw_status == " M"


def test_parse_created_at_accepts_isoformat_timestamp() -> None:
    parsed = parse_created_at("2026-05-23T12:34:56+02:00")

    assert parsed.tzinfo == timezone.utc
    assert parsed.hour == 10


def test_parse_created_at_accepts_legacy_timestamp_without_timezone() -> None:
    parsed = parse_created_at("2026-05-23 12:34:56")

    assert parsed.tzinfo == timezone.utc
    assert parsed.hour == 12
