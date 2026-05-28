"""Command execution helpers for safe argv mode and explicit shell mode."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
import os
from pathlib import Path
import shutil
import signal
import subprocess
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
CMD_EXE_METACHARACTERS = frozenset("^&|<>()%!")


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
    if request.timeout_ms is not None and request.timeout_ms < 1:
        raise CommandValidationError("Command timeout must be at least 1 ms when provided.")
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
        start_new_session=not _is_windows(),
        creationflags=_windows_creationflags(),
    )
    try:
        stdout_bytes, stderr_bytes = await _communicate_with_timeout(process, request.timeout_ms)
        exit_code = int(process.returncode or 0)
    except asyncio.TimeoutError:
        stdout_bytes, stderr_bytes = await _capture_timeout_result(process, request.timeout_ms)
        exit_code = 124
    duration_ms = int((time.perf_counter() - start_time) * 1000)
    return CommandExecutionResult(
        stdout=stdout_bytes.decode("utf-8", errors="replace"),
        stderr=stderr_bytes.decode("utf-8", errors="replace"),
        exit_code=exit_code,
        duration_ms=duration_ms,
        command_display=_command_display(request),
        argv=request.argv,
        shell=request.shell,
        cwd=str(request.cwd),
    )


def _launch_argv(request: CommandExecutionRequest) -> tuple[str, ...]:
    if request.shell:
        return _shell_launch_argv(request.argv[0])
    if _should_use_windows_shell_fallback(request.argv):
        return _windows_safe_argv_shell_launch(request.argv)
    return request.argv


def _command_display(request: CommandExecutionRequest) -> str:
    if request.shell:
        return request.argv[0]
    return " ".join(request.argv)


async def _communicate_with_timeout(
    process: asyncio.subprocess.Process,
    timeout_ms: int | None,
) -> tuple[bytes, bytes]:
    if timeout_ms is None:
        return await process.communicate()
    return await asyncio.wait_for(process.communicate(), timeout=max(timeout_ms, 1) / 1000)


async def _capture_timeout_result(
    process: asyncio.subprocess.Process,
    timeout_ms: int | None,
) -> tuple[bytes, bytes]:
    await _terminate_process(process)
    stdout_bytes, stderr_bytes = await _drain_terminated_process(process)
    stderr_text = stderr_bytes.decode("utf-8", errors="replace")
    timeout_text = _append_timeout_detail(stderr_text, _timeout_message(timeout_ms))
    return stdout_bytes, timeout_text.encode("utf-8")


async def _terminate_process(process: asyncio.subprocess.Process) -> None:
    if process.returncode is not None:
        return
    if _is_windows():
        await _terminate_windows_process_tree(process.pid)
        return
    killpg = getattr(os, "killpg", None)
    if killpg is None:
        process.kill()
        return
    sigkill = getattr(signal, "SIGKILL", signal.SIGTERM)
    try:
        killpg(process.pid, sigkill)
    except ProcessLookupError:
        return


async def _terminate_windows_process_tree(pid: int | None) -> None:
    if pid is None:
        return
    taskkill = shutil.which("taskkill")
    if taskkill is None:
        return
    killer = await asyncio.create_subprocess_exec(
        taskkill,
        "/T",
        "/F",
        "/PID",
        str(pid),
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    await killer.wait()


async def _drain_terminated_process(
    process: asyncio.subprocess.Process,
) -> tuple[bytes, bytes]:
    try:
        return await asyncio.wait_for(process.communicate(), timeout=5)
    except asyncio.TimeoutError:
        process.kill()
        return await process.communicate()


def _timeout_message(timeout_ms: int | None) -> str:
    if timeout_ms is None:
        return "ctxsift terminated the command after a timeout."
    return f"ctxsift terminated the command after exceeding the timeout of {timeout_ms} ms."


def _append_timeout_detail(stderr_text: str, timeout_detail: str) -> str:
    stripped = stderr_text.rstrip()
    if not stripped:
        return timeout_detail + "\n"
    return stripped + "\n" + timeout_detail + "\n"


def _shell_launch_argv(command: str) -> tuple[str, ...]:
    if _is_windows():
        executable = _windows_shell_executable()
        if executable.lower().endswith("cmd.exe"):
            return executable, "/C", command
        return executable, "-NoProfile", "-Command", command
    return "/bin/sh", "-c", command


def _should_use_windows_shell_fallback(argv: tuple[str, ...]) -> bool:
    if not _is_windows() or not argv:
        return False
    command = argv[0]
    command_path = Path(command)
    if command_path.is_absolute():
        return False
    if command_path.parent != Path():
        return False
    return shutil.which(command) is None


def _windows_safe_argv_shell_launch(argv: tuple[str, ...]) -> tuple[str, ...]:
    executable = _windows_shell_executable()
    if executable.lower().endswith("cmd.exe"):
        return executable, "/C", _cmd_exe_command_from_argv(argv)
    return executable, "-NoProfile", "-Command", _powershell_command_from_argv(argv)


def _cmd_exe_command_from_argv(argv: tuple[str, ...]) -> str:
    return " ".join(_cmd_exe_token(token) for token in argv)


def _cmd_exe_token(token: str) -> str:
    if token == "":
        return '""'
    parts: list[str] = []
    literal_chars: list[str] = []
    for char in token:
        if char in CMD_EXE_METACHARACTERS:
            _flush_cmd_literal(parts, literal_chars)
            parts.append("^" + char)
            continue
        literal_chars.append(char)
    _flush_cmd_literal(parts, literal_chars)
    return "".join(parts)


def _flush_cmd_literal(parts: list[str], literal_chars: list[str]) -> None:
    if not literal_chars:
        return
    parts.append(subprocess.list2cmdline(["".join(literal_chars)]))
    literal_chars.clear()


def _powershell_command_from_argv(argv: tuple[str, ...]) -> str:
    return "& " + " ".join(_powershell_literal(token) for token in argv)


def _powershell_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _windows_shell_executable() -> str:
    for candidate in ("pwsh.exe", "pwsh", "powershell.exe", "powershell"):
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    return "cmd.exe"


def _windows_creationflags() -> int:
    if not _is_windows():
        return 0
    return int(getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0))


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
