"""CLI tests for `ctxsift run`."""

from pathlib import Path
import sqlite3
import sys

from typer.testing import CliRunner

from ctxsift import compression
from ctxsift.cli import app


runner = CliRunner()


def test_run_command_preserves_child_exit_code_and_stores_metadata(tmp_path: Path, monkeypatch) -> None:
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

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FakeBackend())
    result = runner.invoke(
        app,
        [
            "run",
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
    assert "Stdout:" in seen["raw_input"]
    assert "Stderr:" in seen["raw_input"]
    assert "Git repo:" in seen["raw_input"]
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


def test_run_command_requires_command_arguments() -> None:
    result = runner.invoke(app, ["run", "summarize failing command"])

    assert result.exit_code == 2
    assert "requires a command after `--`" in result.stderr


def test_run_command_returns_127_for_missing_executable(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    env = {"CTXSIFT_DB_PATH": str(tmp_path / "ctxsift.db")}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            assert "does-not-exist-ctxsift" in request.raw_input
            return "Launch failure summary"

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FakeBackend())
    result = runner.invoke(
        app,
        ["run", "summarize failing command", "--", "does-not-exist-ctxsift"],
        env=env,
    )

    assert result.exit_code == 127
    assert "Launch failure summary" in result.stdout
