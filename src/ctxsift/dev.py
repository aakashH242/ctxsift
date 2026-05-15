"""Development helper commands."""

from __future__ import annotations

import subprocess
import sys


FORMAT_COMMANDS: tuple[tuple[str, ...], ...] = ((sys.executable, "-m", "black", "src", "tests"),)

LINT_COMMANDS: tuple[tuple[str, ...], ...] = (
    (sys.executable, "-m", "black", "--check", "src", "tests"),
    (sys.executable, "-m", "ruff", "check", "src", "tests"),
    (sys.executable, "-m", "mypy", "src", "tests"),
)


def fmt() -> int:
    """Format the local source and test trees."""
    return _run_commands(FORMAT_COMMANDS)


def lint() -> int:
    """Run the local lint suite and stop on the first failure."""
    return _run_commands(LINT_COMMANDS)


def _run_commands(commands: tuple[tuple[str, ...], ...]) -> int:
    for command in commands:
        print(_render_command(command), flush=True)
        result = subprocess.run(command, check=False)
        if result.returncode != 0:
            return result.returncode
    return 0


def _render_command(command: tuple[str, ...]) -> str:
    return "$ " + " ".join(command)
