"""Tests for compression behavior, backend selection, and fallback handling."""

import asyncio
from dataclasses import dataclass
from pathlib import Path
import sqlite3

import pytest

from ctxsift.compression.intent import CompressionIntent
from ctxsift.compression import pipeline as compression
from ctxsift.compression import compress_input, summarize_deterministically
from ctxsift.execution import CommandExecutionResult
from ctxsift.git_metadata import GitMetadata
from ctxsift.models.base import BackendUnavailableError
from ctxsift.models.transformers_backend import TransformersTextBackend
from ctxsift.compression.run_payload import render_run_payload
from ctxsift.types import AppConfig, CompressionRequest, LocalModelConfig
from ctxsift.types import WorkspaceContext


def _command_result(
    *,
    command: list[str],
    cwd: str,
    stdout: str,
    stderr: str,
    exit_code: int,
    duration_ms: int,
    shell: bool = False,
) -> CommandExecutionResult:
    return CommandExecutionResult(
        stdout=stdout,
        stderr=stderr,
        exit_code=exit_code,
        duration_ms=duration_ms,
        command_display=" ".join(command),
        argv=tuple(command),
        shell=shell,
        cwd=cwd,
    )


def test_compress_input_returns_local_passthrough_without_storing_when_backend_is_unavailable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    (repo_path / "src").mkdir()
    (repo_path / "tests").mkdir()
    (repo_path / "src" / "auth.py").write_text("raise AuthError\n", encoding="utf-8")
    (repo_path / "tests" / "test_auth.py").write_text(
        "def test_login():\n    assert False\n", encoding="utf-8"
    )

    class FailingBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            raise BackendUnavailableError("model unavailable")

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FailingBackend())
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
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
    assert result.model_provider == "transformers"
    assert result.model_name == "google/gemma-test"
    assert "[ctxsift warning] Local compression failed:" in result.compressed_output
    assert "AuthError: login failed" in result.compressed_output
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 0


def test_compress_input_does_not_cache_local_passthrough_when_backend_is_unavailable(
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

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FailingBackend())
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction=" Summarize   auth failures ",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
        max_output_tokens=128,
    )

    second_request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction="summarize auth failures",
        raw_input=request.raw_input,
        cwd=request.cwd,
        max_output_tokens=request.max_output_tokens,
    )

    first_result = asyncio.run(compress_input(request))
    second_result = asyncio.run(compress_input(second_request))

    assert first_result.used_cache is False
    assert second_result.used_cache is False
    assert second_result.record_id is None
    assert second_result.compressed_output == first_result.compressed_output
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 0


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

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
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


def test_compress_input_schedules_background_retention_cleanup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    scheduled: dict[str, object] = {}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            return "Model summary with AuthError"

    async def fake_schedule_retention_cleanup(db_path: Path, max_age_days: int) -> bool:
        scheduled["db_path"] = db_path
        scheduled["max_age_days"] = max_age_days
        return True

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())
    monkeypatch.setattr(compression, "schedule_retention_cleanup", fake_schedule_retention_cleanup)
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize auth failures",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
    )

    asyncio.run(compress_input(request))

    assert scheduled["db_path"] == repo_path / ".git" / "ctxsift" / "ctxsift.db"
    assert scheduled["max_age_days"] == 30


def test_compress_input_run_mode_sends_only_output_text_to_model_backend(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    seen: dict[str, object] = {}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            seen["raw_input"] = request.raw_input
            return "Model summary"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())
    capture = _command_result(
        command=["python", "-c", "print('hello')"],
        cwd=str(repo_path),
        stdout="hello\n",
        stderr="oops\n",
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
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize the failure",
        raw_input=render_run_payload(
            capture,
            workspace,
            GitMetadata(git_head="abc123", git_branch="main", git_dirty=False),
        ),
        mode="run",
        cwd=str(repo_path),
        command="python -c print('hello')",
        command_args=list(capture.argv),
        command_exit_code=capture.exit_code,
        command_duration_ms=capture.duration_ms,
    )

    result = asyncio.run(compress_input(request))

    assert result.compressed_output == "Model summary"
    assert compression._run_payload_output_text(request.raw_input) == "hello\n\noops"
    assert seen["raw_input"] == "hello\n\noops"


def test_compress_input_run_mode_preserves_literal_fence_lines_in_command_output(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    seen: dict[str, object] = {}

    class FakeBackend:
        provider_name = "transformers"
        model_name = "google/gemma-test"
        cache_model_id = "google/gemma-test"

        async def compress(self, request) -> str:
            seen["raw_input"] = request.raw_input
            return "Model summary"

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FakeBackend())
    capture = _command_result(
        command=["python", "-c", "print('hello')"],
        cwd=str(repo_path),
        stdout="before\n```\nafter\n",
        stderr="warn\n",
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
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize the failure",
        raw_input=render_run_payload(
            capture,
            workspace,
            GitMetadata(git_head="abc123", git_branch="main", git_dirty=False),
        ),
        mode="run",
        cwd=str(repo_path),
        command="python -c print('hello')",
        command_args=list(capture.argv),
        command_exit_code=capture.exit_code,
        command_duration_ms=capture.duration_ms,
    )

    result = asyncio.run(compress_input(request))

    assert result.compressed_output == "Model summary"
    assert compression._run_payload_output_text(request.raw_input) == "before\n```\nafter\n\nwarn"
    assert seen["raw_input"] == "before\n```\nafter\n\nwarn"


def test_run_payload_output_text_ignores_length_like_lines_inside_legacy_fenced_output() -> None:
    raw_input = "\n".join(
        [
            "Workspace root: /repo",
            "Git repo: True",
            "",
            "Command: demo",
            "Shell mode: False",
            "Cwd: /repo",
            "Exit code: 1",
            "Duration ms: 3",
            "",
            "Stdout:",
            "```text",
            "real line",
            "Stdout:",
            "Length: 4",
            "fake",
            "```",
            "",
            "Stderr:",
            "```text",
            "warn",
            "```",
        ]
    )

    assert (
        compression._run_payload_output_text(raw_input)
        == "real line\nStdout:\nLength: 4\nfake\nwarn"
    )


def test_compress_input_uses_remote_backend_when_base_url_is_configured(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    captured = {"factory_calls": 0, "local_calls": 0}

    class FakeRemoteBackend:
        provider_name = "litellm"
        model_name = "gpt-5-mini"
        cache_model_id = "litellm:gpt-5-mini@http://localhost:4000"

        async def compress(self, request) -> str:
            return "Remote compressed output"

    def fake_create_compression_backend(config):
        captured["factory_calls"] += 1
        assert config.remote.base_url == "http://localhost:4000"
        return FakeRemoteBackend()

    def fail_create_local_backend(config):
        captured["local_calls"] += 1
        raise AssertionError("Local backend should not be constructed when LiteLLM is enabled.")

    monkeypatch.setattr(compression, "create_compression_backend", fake_create_compression_backend)
    monkeypatch.setattr(
        "ctxsift.models.factory.create_local_backend",
        fail_create_local_backend,
    )

    @dataclass(frozen=True)
    class FakeResolvedConfig:
        config: object

    monkeypatch.setattr(
        compression,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate(
                {
                    "remote": {
                        "base_url": "http://localhost:4000",
                        "model_name": "gpt-5-mini",
                    }
                }
            )
        ),
    )
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize auth failures",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.model_provider == "litellm"
    assert result.model_name == "gpt-5-mini"
    assert result.compressed_output == "Remote compressed output"
    assert captured["factory_calls"] == 1
    assert captured["local_calls"] == 0


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

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FailingBackend())
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize auth failures",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.model_provider == "transformers"
    assert result.model_name == "google/gemma-test"
    assert "[ctxsift warning] Local compression failed:" in result.compressed_output
    assert "AuthError: login failed" in result.compressed_output


def test_compress_input_falls_back_when_backend_factory_is_unavailable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"

    def fail_backend_factory(config):
        raise BackendUnavailableError("remote misconfigured")

    monkeypatch.setattr(compression, "create_compression_backend", fail_backend_factory)

    @dataclass(frozen=True)
    class FakeResolvedConfig:
        config: object

    monkeypatch.setattr(
        compression,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate(
                {
                    "remote": {
                        "base_url": "http://localhost:4000",
                        "model_name": "gpt-5-mini",
                    }
                }
            )
        ),
    )
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize auth failures",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.model_provider == "litellm"
    assert result.model_name == "gpt-5-mini"
    assert "[ctxsift warning] Remote compression failed:" in result.compressed_output
    assert "AuthError: login failed" in result.compressed_output
    assert result.record_id is None
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 0


def test_compress_input_remote_failure_passthrough_uses_run_output_body(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    class FailingRemoteBackend:
        provider_name = "litellm"
        model_name = "gpt-5-mini"
        cache_model_id = "litellm:gpt-5-mini@http://localhost:4000"

        async def compress(self, request) -> str:
            raise BackendUnavailableError("proxy unavailable")

    @dataclass(frozen=True)
    class FakeResolvedConfig:
        config: object

    monkeypatch.setattr(
        compression, "create_compression_backend", lambda config: FailingRemoteBackend()
    )
    monkeypatch.setattr(
        compression,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate(
                {
                    "remote": {
                        "base_url": "http://localhost:4000",
                        "model_name": "gpt-5-mini",
                    }
                }
            )
        ),
    )
    capture = _command_result(
        command=["python", "-c", "print('hello')"],
        cwd=str(repo_path),
        stdout="hello\n",
        stderr="oops\n",
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
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize the failure",
        raw_input=render_run_payload(
            capture,
            workspace,
            GitMetadata(git_head="abc123", git_branch="main", git_dirty=False),
        ),
        mode="run",
        cwd=str(repo_path),
        command="python -c print('hello')",
        command_args=list(capture.argv),
        command_exit_code=capture.exit_code,
        command_duration_ms=capture.duration_ms,
    )

    result = asyncio.run(compress_input(request))

    assert result.model_provider == "litellm"
    assert "hello" in result.compressed_output
    assert "oops" in result.compressed_output
    assert "[ctxsift metadata]" not in result.compressed_output
    assert "Command:" not in result.compressed_output
    assert "Exit code: 1" not in result.compressed_output


def test_compress_input_remote_litellm_missing_returns_raw_output_with_warning(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"

    @dataclass(frozen=True)
    class FakeResolvedConfig:
        config: object

    monkeypatch.setattr(
        compression,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate(
                {
                    "remote": {
                        "base_url": "http://localhost:4000",
                        "model_name": "gpt-5-mini",
                    }
                }
            )
        ),
    )

    from ctxsift.models import litellm_remote

    monkeypatch.setattr(
        litellm_remote,
        "_load_litellm_acompletion",
        lambda: (_ for _ in ()).throw(BackendUnavailableError("LiteLLM is not installed.")),
    )

    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize auth failures",
        raw_input="AuthError: login failed\npytest exited with code 1\n",
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.model_provider == "litellm"
    assert result.model_name == "gpt-5-mini"
    assert (
        "[ctxsift warning] Remote compression failed: LiteLLM is not installed."
        in result.compressed_output
    )
    assert result.compressed_output.endswith("AuthError: login failed\npytest exited with code 1")
    assert result.record_id is None
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 0


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

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FailingBackend())
    capture = _command_result(
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
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize the failure",
        raw_input=render_run_payload(
            capture,
            workspace,
            GitMetadata(git_head="abc123", git_branch="main", git_dirty=False),
        ),
        mode="run",
        cwd=str(repo_path),
        command="python -c print('src/generated.py')",
        command_args=list(capture.argv),
        command_exit_code=capture.exit_code,
        command_duration_ms=capture.duration_ms,
    )

    result = asyncio.run(compress_input(request))

    assert result.referenced_files == ["src/real.py"]
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

    monkeypatch.setattr(compression, "create_compression_backend", lambda config: FailingBackend())
    capture = _command_result(
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
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize the command",
        raw_input=render_run_payload(
            capture,
            workspace,
            GitMetadata(git_head="abc123", git_branch="main", git_dirty=False),
        ),
        mode="run",
        cwd=str(repo_path),
        command="python -c print('src/generated.py')",
        command_args=list(capture.argv),
        command_exit_code=capture.exit_code,
        command_duration_ms=capture.duration_ms,
    )

    result = asyncio.run(compress_input(request))

    assert result.referenced_files == []
    assert "src/generated.py" not in result.compressed_output


def test_summarize_deterministically_does_not_truncate_values() -> None:
    raw_input = "\n".join(f"line {index}" for index in range(1, 8))

    output = summarize_deterministically(raw_input, compression.ExtractedSignal())

    assert "line 1" in output
    assert "line 7" in output
    assert "..." not in output


def test_compress_input_unknown_family_fallback_profile_stores_soft_accepted_output(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    class FakeInputs(dict):
        def to(self, device):
            self["device"] = device
            return self

    class InvalidTokenizer:
        pad_token_id = 0
        eos_token_id = 2

        def apply_chat_template(self, messages, tokenize, add_generation_prompt):
            return "templated prompt"

        def __call__(self, text: str, return_tensors: str) -> FakeInputs:
            return FakeInputs({"input_ids": [[1, 2, 3]]})

        def decode(self, tokens, skip_special_tokens: bool) -> str:
            return "generic summary without anchors"

    class FakeModel:
        device = "cpu"
        hf_device_map = None

        def to(self, device: str) -> None:
            self.device = device

        def eval(self) -> None:
            return None

        def generate(self, **kwargs):
            return [[1, 2, 3, 4]]

    class FakeAutoModel:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return FakeModel()

    class FakeAutoTokenizer:
        @staticmethod
        def from_pretrained(model_name: str, **kwargs):
            return InvalidTokenizer()

    fake_torch = type(
        "FakeTorch",
        (),
        {
            "cuda": type("Cuda", (), {"is_available": staticmethod(lambda: False)})(),
            "float32": "float32",
            "float16": "float16",
            "bfloat16": "bfloat16",
        },
    )()
    monkeypatch.setattr(
        "ctxsift.models.transformers_backend._load_transformers_components",
        lambda: (FakeAutoModel, FakeAutoTokenizer),
    )
    monkeypatch.setattr(
        "ctxsift.models.transformers_backend._load_torch_module",
        lambda: fake_torch,
    )
    monkeypatch.setattr(
        compression,
        "create_compression_backend",
        lambda config: TransformersTextBackend(
            LocalModelConfig(model="unknown/model", device="auto")
        ),
    )
    request = CompressionRequest(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize cli failure",
        raw_input="src/cli.py\nValidationError: Extra inputs are not permitted\n",
        cwd=str(repo_path),
    )

    result = asyncio.run(compress_input(request))

    assert result.record_id is not None
    assert result.model_provider == "transformers"
    assert result.model_name == "unknown/model"
    assert result.compressed_output == "generic summary without anchors"
    db_path = repo_path / ".git" / "ctxsift" / "ctxsift.db"
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM records").fetchone()[0]

    assert count == 1
