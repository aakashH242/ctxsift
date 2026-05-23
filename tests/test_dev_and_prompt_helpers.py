"""Tests for dev helpers and compression prompt builders."""

from __future__ import annotations

from types import SimpleNamespace
from typing import cast

import pytest

import ctxsift.dev as dev_helpers
from ctxsift.compression.intent import CompressionIntent
from ctxsift.compression.prompt import (
    _append_signal,
    _structured_signal_section,
    build_messages,
    build_text_messages,
)
from ctxsift.models.base import ModelCompressionInput
from ctxsift.types import ExtractedSignal


@pytest.fixture
def compression_request() -> ModelCompressionInput:
    return ModelCompressionInput(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize the failing command output.",
        raw_input="src/app.py:19\nValueError: boom",
        extracted_signal=ExtractedSignal(
            matched_domains=["python"],
            referenced_files=["src/app.py"],
            traceback_frames=["src/app.py:19 in main"],
            tests=["tests/test_app.py::test_main"],
            packages=["pytest"],
            symbols=["ValueError"],
            command_terms=["uv run pytest"],
            exit_code_lines=["exit code 1"],
            warning_lines=["warning: skipped cache"],
            error_lines=["ValueError: boom"],
        ),
        max_output_tokens=96,
    )


def test_fmt_delegates_to_run_commands(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, tuple[tuple[str, ...], ...]] = {}

    def fake_run_commands(commands: tuple[tuple[str, ...], ...]) -> int:
        captured["commands"] = commands
        return 0

    monkeypatch.setattr(dev_helpers, "_run_commands", fake_run_commands)

    result = dev_helpers.fmt()

    assert result == 0
    assert captured["commands"] == dev_helpers.FORMAT_COMMANDS


def test_lint_delegates_to_run_commands(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, tuple[tuple[str, ...], ...]] = {}

    def fake_run_commands(commands: tuple[tuple[str, ...], ...]) -> int:
        captured["commands"] = commands
        return 0

    monkeypatch.setattr(dev_helpers, "_run_commands", fake_run_commands)

    result = dev_helpers.lint()

    assert result == 0
    assert captured["commands"] == dev_helpers.LINT_COMMANDS


def test_run_commands_returns_zero_when_all_commands_succeed(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    calls: list[tuple[str, ...]] = []

    def fake_run(command: tuple[str, ...], check: bool) -> SimpleNamespace:
        calls.append(command)
        assert check is False
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(dev_helpers.subprocess, "run", fake_run)

    result = dev_helpers._run_commands((("python", "-m", "black"), ("python", "-m", "ruff")))

    assert result == 0
    assert calls == [("python", "-m", "black"), ("python", "-m", "ruff")]
    assert "$ python -m black" in capsys.readouterr().out


def test_run_commands_stops_on_first_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, ...]] = []

    def fake_run(command: tuple[str, ...], check: bool) -> SimpleNamespace:
        del check
        calls.append(command)
        return SimpleNamespace(returncode=7 if command[-1] == "ruff" else 0)

    monkeypatch.setattr(dev_helpers.subprocess, "run", fake_run)

    result = dev_helpers._run_commands(
        (("python", "-m", "black"), ("python", "-m", "ruff"), ("python", "-m", "mypy"))
    )

    assert result == 7
    assert calls == [("python", "-m", "black"), ("python", "-m", "ruff")]


def test_render_command_joins_tokens() -> None:
    assert dev_helpers._render_command(("uv", "run", "pytest")) == "$ uv run pytest"


def test_build_messages_wraps_system_and_user_content(
    compression_request: ModelCompressionInput,
) -> None:
    messages = build_messages(compression_request)
    system_content = cast(list[dict[str, str]], messages[0]["content"])
    user_content = cast(list[dict[str, str]], messages[1]["content"])

    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert system_content[0]["text"].startswith("You compress coding command output")
    assert "Instruction:" in user_content[0]["text"]
    assert "Raw input:" in user_content[0]["text"]


def test_build_text_messages_returns_plain_text_payloads(
    compression_request: ModelCompressionInput,
) -> None:
    messages = build_text_messages(compression_request)
    structured_messages = build_messages(compression_request)
    expected_system_content = cast(list[dict[str, str]], structured_messages[0]["content"])
    expected_user_content = cast(list[dict[str, str]], structured_messages[1]["content"])

    assert messages == [
        {"role": "system", "content": expected_system_content[0]["text"]},
        {"role": "user", "content": expected_user_content[0]["text"]},
    ]


def test_structured_signal_section_lists_all_non_empty_signal_groups(
    compression_request: ModelCompressionInput,
) -> None:
    section = _structured_signal_section(compression_request)

    assert "- Domains:" in section
    assert "- Files:" in section
    assert "- Traceback frames:" in section
    assert "- Tests:" in section
    assert "- Packages:" in section
    assert "- Symbols:" in section
    assert "- Commands:" in section
    assert "- Exit code lines:" in section
    assert "- Warnings:" in section
    assert "- Errors:" in section


def test_append_signal_skips_empty_values() -> None:
    lines = ["Extracted signal:"]

    _append_signal(lines, "Files", [])

    assert lines == ["Extracted signal:"]


def test_append_signal_appends_bullets_for_present_values() -> None:
    lines = ["Extracted signal:"]

    _append_signal(lines, "Files", ["src/app.py", "tests/test_app.py"])

    assert lines == [
        "Extracted signal:",
        "- Files:",
        "  - src/app.py",
        "  - tests/test_app.py",
    ]
