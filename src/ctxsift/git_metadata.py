"""Async git metadata capture for run-mode records."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path

from ctxsift.types import WorkspaceContext


@dataclass(frozen=True)
class GitMetadata:
    """Captured git state for one run."""

    git_head: str | None = None
    git_branch: str | None = None
    git_dirty: bool | None = None


async def capture_git_metadata(workspace: WorkspaceContext) -> GitMetadata:
    """Capture git metadata when the workspace is a git repo."""
    if not workspace.is_git_repo:
        return GitMetadata()
    repo_path = Path(workspace.workspace_root)
    head_task = _git_output(repo_path, "rev-parse", "HEAD")
    branch_task = _git_output(repo_path, "branch", "--show-current")
    dirty_task = _git_output(repo_path, "status", "--porcelain")
    head, branch, dirty_output = await asyncio.gather(head_task, branch_task, dirty_task)
    return GitMetadata(
        git_head=head or None,
        git_branch=branch or None,
        git_dirty=bool(dirty_output) if dirty_output is not None else None,
    )


async def _git_output(repo_path: Path, *args: str) -> str | None:
    try:
        process = await asyncio.create_subprocess_exec(
            "git",
            "-C",
            str(repo_path),
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
    except FileNotFoundError:
        return None
    stdout, _ = await process.communicate()
    if process.returncode != 0:
        return None
    return stdout.decode("utf-8", errors="replace").strip()
