"""CLI tests for deterministic compression."""

from pathlib import Path
import sqlite3

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
