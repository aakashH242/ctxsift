"""Tests for command execution and run-payload rendering."""

import asyncio
from pathlib import Path
import sys

from ctxsift.execution import CommandExecutionRequest, execute_command
from ctxsift.git_metadata import GitMetadata
from ctxsift.run_capture import render_run_payload
from ctxsift.types import WorkspaceContext


def test_run_command_captures_stdout_stderr_exit_code_and_duration(tmp_path: Path) -> None:
    capture = asyncio.run(
        execute_command(
            CommandExecutionRequest(
                argv=(
                    sys.executable,
                    "-c",
                    "import sys; print('hello'); print('oops', file=sys.stderr); raise SystemExit(3)",
                ),
                shell=False,
                cwd=tmp_path,
            )
        )
    )

    assert capture.exit_code == 3
    assert capture.stdout.replace("\r\n", "\n") == "hello\n"
    assert capture.stderr.replace("\r\n", "\n") == "oops\n"
    assert capture.duration_ms >= 0
    assert capture.command_display.startswith(sys.executable)


def test_render_run_payload_includes_workspace_git_and_output_sections(tmp_path: Path) -> None:
    workspace = WorkspaceContext(
        cwd=str(tmp_path),
        workspace_root=str(tmp_path),
        is_git_repo=True,
        git_dir=str(tmp_path / ".git"),
        workspace_config_path=str(tmp_path / ".git" / "ctxsift" / "config.toml"),
        db_path=str(tmp_path / ".git" / "ctxsift" / "ctxsift.db"),
    )
    payload = render_run_payload(
        execution=asyncio.run(
            execute_command(
                CommandExecutionRequest(
                    argv=(sys.executable, "-c", "print('hello')"),
                    shell=False,
                    cwd=tmp_path,
                )
            )
        ),
        workspace=workspace,
        git_metadata=GitMetadata(
            git_head="abc123",
            git_branch="main",
            git_dirty=True,
        ),
    )

    assert "Workspace root:" in payload
    assert "Git head: abc123" in payload
    assert "Git branch: main" in payload
    assert "Git dirty: True" in payload
    assert "Shell mode: False" in payload
    assert "Stdout:" in payload
    assert "hello" in payload
