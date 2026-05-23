"""Tests for shell-syntax detection and execution validation."""

import asyncio
from pathlib import Path
import sys

import pytest

from ctxsift.execution import (
    CommandExecutionRequest,
    CommandValidationError,
    detect_shell_syntax,
    execute_command,
)


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        (("uv", "run", "pytest"), []),
        (("pytest", "-q"), []),
        (("uv", "run", "pytest", "2>&1"), ["2>&1", ">", "&"]),
        ((("python", "-c", "print('hello'); print('bye')")), []),
        (("pytest", "-q", "|", "tee", "out.log"), ["|"]),
        (("npm", "test", "&&", "npm", "run", "lint"), ["&&", "&"]),
        (("echo", "hello; echo bye"), [";"]),
        (("grep", "foo", "file.txt"), []),
    ],
)
def test_detect_shell_syntax(argv: tuple[str, ...], expected: list[str]) -> None:
    assert detect_shell_syntax(argv) == expected


def test_shell_mode_requires_one_command_string(tmp_path) -> None:
    request = CommandExecutionRequest(
        argv=("echo", "hello"),
        shell=True,
        cwd=tmp_path,
    )

    with pytest.raises(CommandValidationError, match="one command string"):
        asyncio.run(execute_command(request))


def test_execute_command_enforces_timeout(tmp_path: Path) -> None:
    result = asyncio.run(
        execute_command(
            CommandExecutionRequest(
                argv=(sys.executable, "-c", "import time; time.sleep(5)"),
                shell=False,
                cwd=tmp_path,
                timeout_ms=100,
            )
        )
    )

    assert result.exit_code == 124
    assert "exceeding the timeout of 100 ms" in result.stderr
    assert result.duration_ms < 5000


def test_execute_command_rejects_non_positive_timeout(tmp_path: Path) -> None:
    request = CommandExecutionRequest(
        argv=(sys.executable, "-c", "print('ok')"),
        shell=False,
        cwd=tmp_path,
        timeout_ms=0,
    )

    with pytest.raises(CommandValidationError, match="at least 1 ms"):
        asyncio.run(execute_command(request))
