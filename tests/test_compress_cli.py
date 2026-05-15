"""CLI tests for deterministic compression."""

import os
from pathlib import Path
import sqlite3
import sys
from typing import cast

from typer.testing import CliRunner

from ctxsift.cli import app
from ctxsift import compression


runner = CliRunner()


def test_compress_command_reads_stdin_and_uses_exact_cache(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    env = {"CTXSIFT_DB_PATH": str(tmp_path / "ctxsift.db")}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            return "Model output for AuthError"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())

    first_result = runner.invoke(
        app,
        ["compress", "summarize auth failures", "--max-output-tokens", "128"],
        input="AuthError: login failed\npytest exited with code 1\n",
        env=env,
    )
    second_result = runner.invoke(
        app,
        ["compress", "summarize auth failures", "--max-output-tokens", "128"],
        input="AuthError: login failed\npytest exited with code 1\n",
        env=env,
    )

    assert first_result.exit_code == 0
    assert second_result.exit_code == 0
    assert "Model output for AuthError" in first_result.stdout
    assert first_result.stdout == second_result.stdout
    with sqlite3.connect(Path(env["CTXSIFT_DB_PATH"])) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 1


def test_compress_command_preserves_child_exit_code_and_stores_metadata(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.chdir(tmp_path)
    env = {"CTXSIFT_DB_PATH": str(tmp_path / "ctxsift.db")}
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
            "summarize failing command",
            "--",
            sys.executable,
            "-c",
            "import sys; print('hello'); print('oops', file=sys.stderr); raise SystemExit(3)",
        ],
        env=env,
    )

    assert result.exit_code == 3
    assert "Run summary" in result.stdout
    raw_input = cast(str, seen["raw_input"])
    assert raw_input == "hello\n\noops"
    with sqlite3.connect(Path(env["CTXSIFT_DB_PATH"])) as connection:
        row = connection.execute(
            """
            SELECT mode, command, command_exit_code, command_duration_ms, stdout_hash, stderr_hash
            FROM records
            """
        ).fetchone()

    assert row is not None
    assert row[0] == "run"
    assert sys.executable in row[1]
    assert row[2] == 3
    assert row[3] >= 0
    assert row[4] is not None
    assert row[5] is not None


def test_compress_command_supports_explicit_shell_mode(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    env = {"CTXSIFT_DB_PATH": str(tmp_path / "ctxsift.db")}
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
            "summarize failing command",
            "--",
            _shell_test_command(),
        ],
        env=env,
    )

    assert result.exit_code == 0
    assert "Shell summary" in result.stdout
    raw_input = cast(str, seen["raw_input"])
    assert raw_input.strip() == "hello"


def _shell_test_command() -> str:
    if os.name == "nt":
        return "Write-Output hello | Out-String"
    return "printf 'hello\\n' | cat"
