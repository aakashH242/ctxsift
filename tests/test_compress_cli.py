"""CLI tests for deterministic compression."""

import os
from pathlib import Path
import sqlite3
import sys
from typing import cast

import pytest
from typer.testing import CliRunner

import ctxsift.cli as cli
from ctxsift.cli import app
from ctxsift.compression import pipeline as compression

runner = CliRunner()


@pytest.fixture(autouse=True)
def configured_global_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "bootstrap_config_available", lambda cwd: True)


def test_compress_command_reads_stdin_and_uses_exact_cache(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    db_path = tmp_path / "ctxsift.db"
    _write_workspace_db_path_config(tmp_path, db_path)

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            return "Model output for AuthError"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())

    first_result = runner.invoke(
        app,
        [
            "compress",
            "--intent",
            "summary",
            "summarize auth failures",
            "--max-output-tokens",
            "128",
        ],
        input="AuthError: login failed\npytest exited with code 1\n",
    )
    second_result = runner.invoke(
        app,
        [
            "compress",
            "--intent",
            "summary",
            "summarize auth failures",
            "--max-output-tokens",
            "128",
        ],
        input="AuthError: login failed\npytest exited with code 1\n",
    )

    assert first_result.exit_code == 0
    assert second_result.exit_code == 0
    assert "Model output for AuthError" in first_result.stdout
    assert first_result.stdout == second_result.stdout
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 1


def test_compress_command_preserves_child_exit_code_and_stores_metadata(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.chdir(tmp_path)
    db_path = tmp_path / "ctxsift.db"
    _write_workspace_db_path_config(tmp_path, db_path)
    seen: dict[str, object] = {}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            seen["raw_input"] = request.raw_input
            return "Run summary"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())
    result = runner.invoke(
        app,
        [
            "compress",
            "--intent",
            "summary",
            "summarize failing command",
            "--",
            sys.executable,
            "-c",
            "import sys; print('hello'); print('oops', file=sys.stderr); raise SystemExit(3)",
        ],
    )

    assert result.exit_code == 3
    assert "Run summary" in result.stdout
    raw_input = cast(str, seen["raw_input"])
    assert raw_input == "hello\n\noops"
    with sqlite3.connect(db_path) as connection:
        row = connection.execute("""
            SELECT mode, command, command_exit_code, command_duration_ms, stdout_hash, stderr_hash
            FROM records
            """).fetchone()

    assert row is not None
    assert row[0] == "run"
    assert sys.executable in row[1]
    assert row[2] == 3
    assert row[3] >= 0
    assert row[4] is not None
    assert row[5] is not None


def test_compress_command_supports_explicit_shell_mode(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    _write_workspace_db_path_config(tmp_path, tmp_path / "ctxsift.db")
    seen: dict[str, object] = {}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            seen["raw_input"] = request.raw_input
            return "Shell summary"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())
    result = runner.invoke(
        app,
        [
            "compress",
            "--shell",
            "--intent",
            "summary",
            "summarize failing command",
            "--",
            _shell_test_command(),
        ],
    )

    assert result.exit_code == 0
    assert "Shell summary" in result.stdout
    raw_input = cast(str, seen["raw_input"])
    assert raw_input.strip() == "hello"


def test_compress_without_global_config_warns_and_returns_raw_input(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli, "bootstrap_config_available", lambda cwd: False)

    result = runner.invoke(
        app,
        ["compress", "--intent", "summary", "summarize auth failures"],
        input="AuthError: login failed\n",
    )

    assert result.exit_code == 0
    assert (
        "[ctxsift warning] No workspace config, global config, or ctxsift env config is set yet."
        in result.stderr
    )
    assert result.stdout == "AuthError: login failed\n"


def test_compress_accepts_env_only_config_and_initializes_workspace(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    env = {
        "CTXSIFT_LOCAL_MODEL": "HuggingFaceTB/SmolLM2-360M-Instruct",
    }

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            return "Env-config summary"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())

    result = runner.invoke(
        app,
        ["compress", "--intent", "summary", "summarize auth failures"],
        input="AuthError: login failed\n",
        env=env,
    )

    assert result.exit_code == 0
    assert "Env-config summary" in result.stdout
    assert (tmp_path / ".ctxsift" / "ctxsift.db").exists()


def test_compress_requires_intent_flag() -> None:
    result = runner.invoke(
        app,
        ["compress", "summarize auth failures"],
        input="AuthError: login failed\n",
    )

    assert result.exit_code != 0
    assert "Missing option '--intent'" in result.stderr


@pytest.mark.parametrize(
    "intent_name",
    [
        "summary",
        "recall",
        "exact-lines",
        "exact-format",
        "json",
        "yaml",
        "table",
        "bullet-list",
    ],
)
def test_compress_accepts_all_public_intents(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    intent_name: str,
) -> None:
    monkeypatch.chdir(tmp_path)
    _write_workspace_db_path_config(tmp_path, tmp_path / "ctxsift.db")
    seen: dict[str, object] = {}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            seen["intent"] = request.intent.value
            return "ok"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())
    result = runner.invoke(
        app,
        ["compress", "--intent", intent_name, "summarize auth failures"],
        input="AuthError: login failed\n",
    )

    assert result.exit_code == 0
    assert seen["intent"] == intent_name


def _write_workspace_db_path_config(tmp_path: Path, db_path: Path) -> None:
    config_path = tmp_path / ".ctxsift" / "config.toml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        f'db_path = "{db_path.as_posix()}"\n',
        encoding="utf-8",
    )


def _shell_test_command() -> str:
    if os.name == "nt":
        return "Write-Output hello | Out-String"
    return "printf 'hello\\n' | cat"
