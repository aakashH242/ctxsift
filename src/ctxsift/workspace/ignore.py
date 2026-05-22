"""Workspace ignore-file helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ctxsift.types import WorkspaceContext

IGNORE_ENTRY = ".ctxsift/"


@dataclass(frozen=True)
class IgnoreWriteResult:
    """Result of a workspace ignore-file update attempt."""

    changed: bool
    detail: str


def ensure_workspace_ignore_entry(workspace: WorkspaceContext, db_path: Path) -> IgnoreWriteResult:
    """Ensure the workspace root .gitignore ignores .ctxsift/ when needed."""
    if _is_git_scoped_db(workspace, db_path):
        return IgnoreWriteResult(
            changed=False,
            detail="No ignore update needed; ctxsift data is stored under .git/.",
        )
    if not _is_workspace_scoped_db(workspace, db_path):
        return IgnoreWriteResult(
            changed=False,
            detail=f"No ignore update needed; ctxsift data uses custom path {db_path}.",
        )
    gitignore_path = Path(workspace.workspace_root) / ".gitignore"
    existing_text = gitignore_path.read_text(encoding="utf-8") if gitignore_path.exists() else ""
    lines = existing_text.splitlines()
    if any(line.strip() == IGNORE_ENTRY for line in lines):
        return IgnoreWriteResult(
            changed=False,
            detail=f".gitignore already contains {IGNORE_ENTRY}",
        )
    updated_text = _appended_ignore_text(existing_text)
    gitignore_path.write_text(updated_text, encoding="utf-8")
    return IgnoreWriteResult(
        changed=True,
        detail=f"Updated {gitignore_path} with {IGNORE_ENTRY}",
    )


def requires_workspace_ignore_entry(workspace: WorkspaceContext, db_path: Path) -> bool:
    """Return whether the configured DB path lives under the workspace .ctxsift directory."""
    return _is_workspace_scoped_db(workspace, db_path)


def _appended_ignore_text(existing_text: str) -> str:
    if not existing_text:
        return f"{IGNORE_ENTRY}\n"
    newline = "\r\n" if "\r\n" in existing_text else "\n"
    suffix = "" if existing_text.endswith(("\n", "\r")) else newline
    return f"{existing_text}{suffix}{IGNORE_ENTRY}{newline}"


def _is_git_scoped_db(workspace: WorkspaceContext, db_path: Path) -> bool:
    if not workspace.git_dir:
        return False
    git_scoped_root = Path(workspace.git_dir) / "ctxsift"
    return _is_within(db_path, git_scoped_root)


def _is_workspace_scoped_db(workspace: WorkspaceContext, db_path: Path) -> bool:
    workspace_scoped_root = Path(workspace.workspace_root) / ".ctxsift"
    return _is_within(db_path, workspace_scoped_root)


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError:
        return False
    return True
