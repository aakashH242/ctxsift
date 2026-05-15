"""Git file-status helpers for recall freshness checks."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GitFileStatus:
    """Git status for one file path."""

    path: str
    is_changed: bool = False
    is_deleted: bool = False
    raw_status: str | None = None


async def read_git_file_status(
    workspace_root: Path | None,
    relative_path: str,
) -> GitFileStatus | None:
    """Read git status for one file path when a repo is available."""
    if workspace_root is None or not (workspace_root / ".git").exists():
        return None
    try:
        process = await asyncio.create_subprocess_exec(
            "git",
            "-C",
            str(workspace_root),
            "status",
            "--porcelain",
            "--",
            relative_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
    except FileNotFoundError:
        return None
    stdout, _ = await process.communicate()
    if process.returncode != 0:
        return None
    return _parse_git_file_status(relative_path, stdout.decode("utf-8", errors="replace"))


def _parse_git_file_status(relative_path: str, output: str) -> GitFileStatus:
    lines = [line for line in output.splitlines() if line.strip()]
    if not lines:
        return GitFileStatus(path=relative_path)
    status_code = lines[0][:2]
    return GitFileStatus(
        path=relative_path,
        is_changed=bool(status_code.strip()),
        is_deleted="D" in status_code,
        raw_status=status_code,
    )
