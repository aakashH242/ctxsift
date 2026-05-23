"""Structured rendering for command execution results."""

from __future__ import annotations

from ctxsift.execution import CommandExecutionResult
from ctxsift.git_metadata import GitMetadata
from ctxsift.types import WorkspaceContext


def render_run_payload(
    execution: CommandExecutionResult,
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


def _capture_sections(execution: CommandExecutionResult) -> list[str]:
    return [
        f"Command: {execution.command_display}",
        f"Shell mode: {execution.shell}",
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
