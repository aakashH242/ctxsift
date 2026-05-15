"""Tests for shell-syntax detection and execution validation."""

import asyncio

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
