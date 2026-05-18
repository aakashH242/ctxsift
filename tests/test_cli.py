"""Smoke tests for the ctxsift CLI scaffold."""

from typer.testing import CliRunner

from ctxsift.cli import app


runner = CliRunner()


def test_cli_help_renders() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Local-first command output compression and recall." in result.stdout


def test_cli_help_lists_v1_commands() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    for command_name in ("configure", "compress", "recall", "config", "doctor", "daemon"):
        assert command_name in result.stdout
