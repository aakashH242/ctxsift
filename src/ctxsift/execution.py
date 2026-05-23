"""Command execution helpers for safe argv mode and explicit shell mode."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
import os
from pathlib import Path
import shutil
import time

SHELL_SYNTAX_LABELS = (
    ("||", "||"),
    ("&&", "&&"),
    ("2>&1", "2>&1"),
    (">>", ">>"),
    ("|", "|"),
    (">", ">"),
    ("&", "&"),
    (";", ";"),
    ("<", "<"),
    ("$(", "$(...)"),
    ("${", "${VAR}"),
    ("`", "`...`"),
)

CODE_LITERAL_FLAGS = {"-c", "-command"}


@dataclass(frozen=True)
class CommandExecutionRequest:
    """One command execution request."""

    argv: tuple[str, ...]
    shell: bool
    cwd: Path
    timeout_ms: int | None = None


@dataclass(frozen=True)
class CommandExecutionResult:
    """One command execution result."""

    stdout: str
    stderr: str
    exit_code: int
    duration_ms: int
    command_display: str
    argv: tuple[str, ...]
    shell: bool
    cwd: str


class CommandValidationError(ValueError):
    """Raised when command execution input is invalid."""


async def execute_command(request: CommandExecutionRequest) -> CommandExecutionResult:
    """Execute one command in argv mode or explicit shell mode."""
    _validate_request(request)
    return await _execute_subprocess(request)


def detect_shell_syntax(argv: tuple[str, ...]) -> list[str]:
    """Return obvious shell-syntax markers found in argv-mode input."""
    matches: list[str] = []
    for index, token in enumerate(argv):
        if _is_literal_code_argument(argv, index):
            continue
        for needle, label in SHELL_SYNTAX_LABELS:
            if needle in token:
                _append_unique(matches, label)
        if _contains_env_reference(token):
            _append_unique(matches, "$VAR")
    return matches


def build_shell_syntax_error(argv: tuple[str, ...]) -> CommandValidationError:
    """Build a usage error for shell syntax found in argv mode."""
    syntax_tokens = detect_shell_syntax(argv)
    token_list = ", ".join(syntax_tokens)
    command_text = " ".join(argv)
    message = (
        f"This command appears to contain shell syntax: {token_list}\n\n"
        "ctxsift compress uses safe argv mode by default.\n\n"
        "Use explicit shell mode:\n\n"
        f'ctxsift compress --intent summary --shell "show failures" -- "{command_text}"'
    )
    return CommandValidationError(message)


def capture_launch_failure(
    request: CommandExecutionRequest,
    error: FileNotFoundError,
) -> CommandExecutionResult:
    """Build a synthetic execution result when launch fails before execution."""
    return CommandExecutionResult(
        stdout="",
        stderr=str(error),
        exit_code=127,
        duration_ms=0,
        command_display=_command_display(request),
        argv=request.argv,
        shell=request.shell,
        cwd=str(request.cwd),
    )


def _validate_request(request: CommandExecutionRequest) -> None:
    if not request.argv:
        raise CommandValidationError("`ctxsift compress` requires a command after `--`.")
    if request.shell:
        _validate_shell_command(request.argv)
        return
    syntax_tokens = detect_shell_syntax(request.argv)
    if syntax_tokens:
        raise build_shell_syntax_error(request.argv)


def _validate_shell_command(argv: tuple[str, ...]) -> None:
    if len(argv) != 1:
        raise CommandValidationError("Shell mode expects one command string after `--`.")
    if not argv[0].strip():
        raise CommandValidationError("Shell mode expects one non-empty command string after `--`.")


async def _execute_subprocess(request: CommandExecutionRequest) -> CommandExecutionResult:
    launch_argv = _launch_argv(request)
    start_time = time.perf_counter()
    process = await asyncio.create_subprocess_exec(
        *launch_argv,
        cwd=str(request.cwd),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout_bytes, stderr_bytes = await process.communicate()
    duration_ms = int((time.perf_counter() - start_time) * 1000)
    return CommandExecutionResult(
        stdout=stdout_bytes.decode("utf-8", errors="replace"),
        stderr=stderr_bytes.decode("utf-8", errors="replace"),
        exit_code=int(process.returncode or 0),
        duration_ms=duration_ms,
        command_display=_command_display(request),
        argv=request.argv,
        shell=request.shell,
        cwd=str(request.cwd),
    )


def _launch_argv(request: CommandExecutionRequest) -> tuple[str, ...]:
    if request.shell:
        return _shell_launch_argv(request.argv[0])
    return request.argv


def _command_display(request: CommandExecutionRequest) -> str:
    if request.shell:
        return request.argv[0]
    return " ".join(request.argv)


def _shell_launch_argv(command: str) -> tuple[str, ...]:
    if _is_windows():
        executable = _windows_shell_executable()
        if executable.lower().endswith("cmd.exe"):
            return executable, "/C", command
        return executable, "-NoProfile", "-Command", command
    return "/bin/sh", "-c", command


def _windows_shell_executable() -> str:
    for candidate in ("pwsh.exe", "pwsh", "powershell.exe", "powershell"):
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    return "cmd.exe"


def _contains_env_reference(token: str) -> bool:
    for index, char in enumerate(token):
        if char != "$":
            continue
        if index + 1 >= len(token):
            continue
        next_char = token[index + 1]
        if next_char in "{(" or next_char.isalpha() or next_char == "_":
            return True
    return False


def _is_literal_code_argument(argv: tuple[str, ...], index: int) -> bool:
    if index == 0:
        return False
    return argv[index - 1].casefold() in CODE_LITERAL_FLAGS


def _append_unique(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def _is_windows() -> bool:
    return os.name == "nt"
