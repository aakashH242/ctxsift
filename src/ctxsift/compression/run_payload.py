"""Structured rendering for command execution results."""

from __future__ import annotations

from dataclasses import dataclass

from ctxsift.execution import CommandExecutionResult
from ctxsift.git_metadata import GitMetadata
from ctxsift.types import WorkspaceContext


@dataclass(frozen=True)
class CommandCapture:
    """Backwards-compatible synthetic capture used by tests and fixtures."""

    command: list[str]
    cwd: str
    stdout: str
    stderr: str
    exit_code: int
    duration_ms: int
    shell: bool = False


def render_run_payload(
    execution: CommandExecutionResult | CommandCapture,
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
    sections.extend(_capture_sections(execution))
    return "\n".join(sections)


def _capture_sections(execution: CommandExecutionResult | CommandCapture) -> list[str]:
    return [
        f"Command: {_command_display(execution)}",
        f"Shell mode: {_shell_mode(execution)}",
        f"Cwd: {execution.cwd}",
        f"Exit code: {execution.exit_code}",
        f"Duration ms: {execution.duration_ms}",
        "",
        _output_section("Stdout", execution.stdout),
        "",
        _output_section("Stderr", execution.stderr),
    ]


def _output_section(label: str, content: str) -> str:
    return f"{label}:\nLength: {len(content)}\n{content}"


def _command_display(execution: CommandExecutionResult | CommandCapture) -> str:
    if isinstance(execution, CommandExecutionResult):
        return execution.command_display
    return " ".join(execution.command)


def _shell_mode(execution: CommandExecutionResult | CommandCapture) -> bool:
    if isinstance(execution, CommandExecutionResult):
        return execution.shell
    return execution.shell
