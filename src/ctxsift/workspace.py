"""Workspace discovery helpers."""

from __future__ import annotations

from pathlib import Path

from ctxsift.types import WorkspaceContext


def detect_workspace_context(cwd: Path | None = None) -> WorkspaceContext:
    """Resolve workspace metadata for the current working directory."""
    current_directory = (cwd or Path.cwd()).resolve()
    git_root = _find_git_root(current_directory)
    if git_root is None:
        workspace_root = current_directory
        config_path = workspace_root / ".ctxsift" / "config.toml"
        return WorkspaceContext(
            cwd=str(current_directory),
            workspace_root=str(workspace_root),
            is_git_repo=False,
            workspace_config_path=str(config_path),
        )

    git_directory = _resolve_git_directory(git_root)
    config_path = git_directory / "ctxsift" / "config.toml"
    return WorkspaceContext(
        cwd=str(current_directory),
        workspace_root=str(git_root),
        is_git_repo=True,
        git_dir=str(git_directory),
        workspace_config_path=str(config_path),
    )


def _find_git_root(start_path: Path) -> Path | None:
    for candidate in (start_path, *start_path.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def _resolve_git_directory(git_root: Path) -> Path:
    git_entry = git_root / ".git"
    if git_entry.is_dir():
        return git_entry.resolve()
    if git_entry.is_file():
        return _read_gitdir_pointer(git_entry)
    raise FileNotFoundError(f"Could not resolve .git directory from {git_root}")


def _read_gitdir_pointer(git_file: Path) -> Path:
    content = git_file.read_text(encoding="utf-8").strip()
    prefix = "gitdir:"
    if not content.lower().startswith(prefix):
        raise ValueError(f"Unsupported .git file format in {git_file}")
    raw_path = content[len(prefix) :].strip()
    candidate = Path(raw_path)
    if candidate.is_absolute():
        return candidate.resolve()
    return (git_file.parent / candidate).resolve()
