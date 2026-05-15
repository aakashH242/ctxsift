"""Tests for deterministic compression and exact-cache behavior."""

import asyncio
from pathlib import Path
import sqlite3

import pytest

from ctxsift import compression
from ctxsift.compression import compress_input
from ctxsift.git_metadata import GitMetadata
from ctxsift.models.base import BackendUnavailableError
from ctxsift.run_capture import CommandCapture, render_run_payload
from ctxsift.types import CompressionRequest
from ctxsift.types import WorkspaceContext


def test_compress_input_persists_deterministic_summary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    (repo_path / "src").mkdir()
    (repo_path / "tests").mkdir()
    (repo_path / "src" / "auth.py").write_text("raise AuthError\n", encoding="utf-8")
    (repo_path / "tests" / "test_auth.py").write_text("def test_login():\n    assert False\n", encoding="utf-8")

    class FailingBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            raise BackendUnavailableError("model unavailable")

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FailingBackend())
    request = CompressionRequest(
        instruction="Summarize auth failures for me",
        raw_input="\n".join(
            [
                'File "src/auth.py", line 9, in login',
                "tests/test_auth.py::test_login FAILED",
                "AuthError: login failed",
                "pytest exited with code 1",
            ]
        ),
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.used_cache is False
    assert result.model_provider == "deterministic"
    assert result.model_name == "deterministic"
    assert "Domains: python, pytest" in result.compressed_output
    assert "Files: src/auth.py, tests/test_auth.py" in result.compressed_output
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"
    with sqlite3.connect(db_path) as connection:
        row = connection.execute(
            """
            SELECT exact_cache_key, model_provider, model_name, prompt_version, ctxsift_version
            FROM records
            """
        ).fetchone()

    assert row is not None
    assert row[0]
    assert row[1:] == ("deterministic", "deterministic", "deterministic-v1", "0.1.0")


def test_compress_input_uses_exact_cache_without_duplicate_record(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    class FailingBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            raise BackendUnavailableError("model unavailable")

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FailingBackend())
    request = CompressionRequest(
        instruction=" Summarize   auth failures ",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
        max_output_tokens=128,
    )

    second_request = CompressionRequest(
        instruction="summarize auth failures",
        raw_input=request.raw_input,
        cwd=request.cwd,
        max_output_tokens=request.max_output_tokens,
    )

    first_result = asyncio.run(compress_input(request))
    second_result = asyncio.run(compress_input(second_request))

    assert first_result.used_cache is False
    assert second_result.used_cache is True
    assert second_result.record_id == first_result.record_id
    assert second_result.compressed_output == first_result.compressed_output
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 1


def test_compress_input_uses_model_backend_when_available(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            assert "AuthError" in request.raw_input
            assert "AuthError" in request.extracted_signal.symbols
            return "Model summary with AuthError"

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FakeBackend())
    request = CompressionRequest(
        instruction="Summarize auth failures",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.used_cache is False
    assert result.model_provider == "transformers"
    assert result.model_name == "google/gemma-test"
    assert result.compressed_output == "Model summary with AuthError"
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"
    with sqlite3.connect(db_path) as connection:
        stored = connection.execute(
            "SELECT model_provider, model_name, prompt_version FROM records"
        ).fetchone()

    assert stored == ("transformers", "google/gemma-test", "gemma-transformers-v1")


def test_compress_input_falls_back_when_model_backend_is_unavailable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    class FailingBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            raise BackendUnavailableError("model unavailable")

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FailingBackend())
    request = CompressionRequest(
        instruction="Summarize auth failures",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.model_provider == "deterministic"
    assert result.model_name == "deterministic"
    assert "Errors:" in result.compressed_output


def test_compress_input_run_mode_ignores_inline_command_code_when_extracting_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    actual_file = repo_path / "src" / "real.py"
    actual_file.parent.mkdir(parents=True)
    actual_file.write_text("print('hello')\n", encoding="utf-8")

    class FailingBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            raise BackendUnavailableError("model unavailable")

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FailingBackend())
    capture = CommandCapture(
        command=["python", "-c", "print('src/generated.py')"],
        cwd=str(repo_path),
        stdout="src/real.py:12:3\n",
        stderr="",
        exit_code=1,
        duration_ms=7,
    )
    workspace = WorkspaceContext(
        cwd=str(repo_path),
        workspace_root=str(repo_path),
        is_git_repo=True,
        git_dir=str(repo_path / ".git"),
        workspace_config_path=str(repo_path / ".git" / "ctxsift" / "config.toml"),
        db_path=str(repo_path / ".git" / "ctxsift" / "ctxsift.db"),
    )
    request = CompressionRequest(
        instruction="Summarize the failure",
        raw_input=render_run_payload(
            capture,
            workspace,
            GitMetadata(git_head="abc123", git_branch="main", git_dirty=False),
        ),
        mode="run",
        cwd=str(repo_path),
        command="python -c print('src/generated.py')",
        command_args=capture.command,
        command_exit_code=capture.exit_code,
        command_duration_ms=capture.duration_ms,
    )

    result = asyncio.run(compress_input(request))

    assert result.referenced_files == ["src/real.py"]
    assert "Files: src/real.py" in result.compressed_output
    assert "src/generated.py" not in result.compressed_output


def test_compress_input_run_mode_with_empty_output_does_not_promote_inline_command_code(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    class FailingBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            raise BackendUnavailableError("model unavailable")

    monkeypatch.setattr(compression, "create_local_backend", lambda config: FailingBackend())
    capture = CommandCapture(
        command=["python", "-c", "print('src/generated.py')"],
        cwd=str(repo_path),
        stdout="",
        stderr="",
        exit_code=0,
        duration_ms=3,
    )
    workspace = WorkspaceContext(
        cwd=str(repo_path),
        workspace_root=str(repo_path),
        is_git_repo=True,
        git_dir=str(repo_path / ".git"),
        workspace_config_path=str(repo_path / ".git" / "ctxsift" / "config.toml"),
        db_path=str(repo_path / ".git" / "ctxsift" / "ctxsift.db"),
    )
    request = CompressionRequest(
        instruction="Summarize the command",
        raw_input=render_run_payload(
            capture,
            workspace,
            GitMetadata(git_head="abc123", git_branch="main", git_dirty=False),
        ),
        mode="run",
        cwd=str(repo_path),
        command="python -c print('src/generated.py')",
        command_args=capture.command,
        command_exit_code=capture.exit_code,
        command_duration_ms=capture.duration_ms,
    )

    result = asyncio.run(compress_input(request))

    assert result.referenced_files == []
    assert "src/generated.py" not in result.compressed_output
