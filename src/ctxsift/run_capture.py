"""Async direct subprocess capture for `ctxsift run`."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
import time

from ctxsift.git_metadata import GitMetadata
from ctxsift.types import WorkspaceContext


@dataclass(frozen=True)
class CommandCapture:
    """Captured subprocess output and timing."""

    command: list[str]
    cwd: str
    stdout: str
    stderr: str
    exit_code: int
    duration_ms: int


async def run_command(command: list[str], cwd: Path) -> CommandCapture:
    """Run one command directly without an implicit shell."""
    start_time = time.perf_counter()
    process = await asyncio.create_subprocess_exec(
        *command,
        cwd=str(cwd),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout_bytes, stderr_bytes = await process.communicate()
    duration_ms = int((time.perf_counter() - start_time) * 1000)
    return CommandCapture(
        command=command,
        cwd=str(cwd),
        stdout=stdout_bytes.decode("utf-8", errors="replace"),
        stderr=stderr_bytes.decode("utf-8", errors="replace"),
        exit_code=int(process.returncode or 0),
        duration_ms=duration_ms,
    )


def render_command_capture(capture: CommandCapture) -> str:
    """Render captured command output into the structured compression input."""
    return "\n".join(_capture_sections(capture)).strip()


def render_run_payload(
    capture: CommandCapture,
    workspace: WorkspaceContext,
    git_metadata: GitMetadata,
) -> str:
    """Render the structured run payload sent through compression."""
    sections = [
        f"Workspace root: {workspace.workspace_root}",
        f"Git repo: {workspace.is_git_repo}",
    ]
    if git_metadata.git_head:
        sections.append(f"Git head: {git_metadata.git_head}")
    if git_metadata.git_branch:
        sections.append(f"Git branch: {git_metadata.git_branch}")
    if git_metadata.git_dirty is not None:
        sections.append(f"Git dirty: {git_metadata.git_dirty}")
    sections.append("")
    sections.extend(_capture_sections(capture))
    return "\n".join(sections).strip()


def capture_launch_failure(
    command: list[str], cwd: Path, error: FileNotFoundError
) -> CommandCapture:
    """Build a synthetic capture when process launch fails before execution."""
    return CommandCapture(
        command=command,
        cwd=str(cwd),
        stdout="",
        stderr=str(error),
        exit_code=127,
        duration_ms=0,
    )


def _capture_sections(capture: CommandCapture) -> list[str]:
    sections = [
        f"Command: {render_command(capture.command)}",
        f"Cwd: {capture.cwd}",
        f"Exit code: {capture.exit_code}",
        f"Duration ms: {capture.duration_ms}",
        "",
        "Stdout:",
        "```text",
        capture.stdout,
        "```",
        "",
        "Stderr:",
        "```text",
        capture.stderr,
        "```",
    ]
    return sections


def render_command(command: list[str]) -> str:
    """Render one command list for storage and display."""
    return " ".join(command)
