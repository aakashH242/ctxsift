"""CLI tests for interactive configure."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from ctxsift import config_store
from ctxsift.cli import app
from ctxsift import configure_setup
from ctxsift import configure_flow
from ctxsift.doctor import DoctorCheck, DoctorReport
from ctxsift.model_preload import ModelPreloadResult


runner = CliRunner()


@pytest.fixture()
def isolated_config_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Path:
    platform_path = tmp_path / "platform" / "config.toml"
    legacy_path = tmp_path / "legacy" / "config.toml"
    monkeypatch.setattr(config_store, "platform_global_config_path", lambda: platform_path)
    monkeypatch.setattr(config_store, "legacy_global_config_path", lambda: legacy_path)
    return platform_path


@pytest.fixture(autouse=True)
def fast_configure_side_effects(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_collect_doctor_report_for_config(cwd, config):
        return DoctorReport(
            checks=[
                DoctorCheck(
                    name="sqlite_fts5",
                    severity="required",
                    ok=True,
                    detail="FTS5 is available.",
                )
            ]
        )

    async def fake_preload_configured_models(config):
        results = [
            ModelPreloadResult(
                label=f"embedding model {config.embedding.model}",
                ok=True,
                detail=f"Preloaded embedding model {config.embedding.model}.",
            )
        ]
        if not config.remote.base_url.strip():
            results.append(
                ModelPreloadResult(
                    label=f"local compression model {config.local.model}",
                    ok=True,
                    detail=f"Preloaded local compression model {config.local.model}.",
                )
            )
        return results

    monkeypatch.setattr(
        configure_setup,
        "collect_doctor_report_for_config",
        fake_collect_doctor_report_for_config,
    )
    monkeypatch.setattr(
        configure_setup,
        "preload_configured_models",
        fake_preload_configured_models,
    )


def test_configure_writes_workspace_scope_by_default(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)
    monkeypatch.chdir(repo_path)
    monkeypatch.setattr(configure_flow, "_cuda_available", lambda: False)
    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="local",
            save_target="workspace",
        ),
    )

    assert result.exit_code == 0
    workspace_config = repo_path / ".git" / "ctxsift" / "config.toml"
    assert workspace_config.exists()
    assert "Updated workspace config" in result.stdout
    assert (repo_path / ".git" / "ctxsift" / "ctxsift.db").exists()
    assert "Preloaded embedding model microsoft/harrier-oss-v1-0.6b." in result.stdout
    assert "Preloaded local compression model ibm-granite/granite-4.0-350m-GGUF." in result.stdout
    assert "[required] sqlite_fts5: ok" in result.stdout
    text = workspace_config.read_text(encoding="utf-8")
    assert 'model = "ibm-granite/granite-4.0-350m-GGUF"' in text
    assert 'gguf_filename = "smollm2-360m-instruct-q8_0.gguf"' in text
    assert 'quantization = "none"' in text
    assert 'model = "microsoft/harrier-oss-v1-0.6b"' in text


def test_configure_can_set_local_model_cache_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(configure_flow, "_cuda_available", lambda: False)

    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="local",
            local_model_cache_path="D:/ctxsift-model-cache",
            save_target="global",
            write_ignore_answer="",
        ),
    )

    assert result.exit_code == 0
    assert "Local model cache path override" in result.output
    text = isolated_config_paths.read_text(encoding="utf-8")
    assert 'model_cache_path = "D:/ctxsift-model-cache"' in text


def test_configure_global_writes_remote_values(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="remote",
            save_target="global",
            write_ignore_answer="",
        ),
    )

    assert result.exit_code == 0
    assert isolated_config_paths.exists()
    text = isolated_config_paths.read_text(encoding="utf-8")
    assert 'base_url = "http://localhost:4000"' in text
    assert 'model_name = "gpt-4o-mini"' in text
    assert 'api_version = "2025-01-01"' in text
    assert (tmp_path / ".ctxsift" / "ctxsift.db").exists()
    assert "Preloaded local compression model" not in result.stdout
    assert "Remote base URL" in result.output
    assert "Local device" not in result.output
    assert "Local model (recommended:" not in result.output
    assert "Local GGUF filename" not in result.output


def test_configure_succeeds_when_remote_litellm_warning_is_reported(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    async def fake_collect_doctor_report_for_config(cwd, config):
        return DoctorReport(
            checks=[
                DoctorCheck(
                    name="litellm",
                    severity="warning",
                    ok=False,
                    detail=(
                        "LiteLLM is not installed. Install it with `uv add \"ctxsift[remote]\"`; "
                        "remote compression will not work until it is available."
                    ),
                )
            ]
        )

    monkeypatch.setattr(
        configure_setup,
        "collect_doctor_report_for_config",
        fake_collect_doctor_report_for_config,
    )

    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="remote",
            save_target="global",
            write_ignore_answer="",
        ),
    )

    assert result.exit_code == 0
    assert isolated_config_paths.exists()
    assert "Updated global config" in result.stdout
    assert "[warning] litellm: warning" in result.stdout
    assert 'uv add "ctxsift[remote]"' in result.stdout


def test_configure_rejects_invalid_final_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="local",
            recall_default_limit="0",
            save_target="global",
            write_ignore_answer="",
        ),
    )

    assert result.exit_code != 0
    assert "greater than or equal to 1" in result.output


def test_configure_hides_advanced_acceleration_prompts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(configure_flow, "_cuda_available", lambda: False)

    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="local",
            save_target="global",
            write_ignore_answer="",
        ),
    )

    assert result.exit_code == 0
    assert "Local attention backend" not in result.output
    assert "Embedding attention backend" not in result.output
    assert "Local quantization" not in result.output
    assert "Embedding backend" not in result.output


def test_configure_uses_gpu_recommended_model_when_cuda_is_available(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(configure_flow, "_cuda_available", lambda: True)

    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="local",
            embedding_device="cuda",
            save_target="global",
            write_ignore_answer="",
            include_gguf_prompt=False,
        ),
    )

    assert result.exit_code == 0
    assert "Local device (GPU detected) (cuda, cpu)" in result.output
    assert "Local model (recommended: Qwen/Qwen3.5-0.8B)" in result.output
    assert "Local GGUF filename" not in result.output
    assert 'model = "Qwen/Qwen3.5-0.8B"' in isolated_config_paths.read_text(encoding="utf-8")


def test_configure_local_mode_hides_remote_prompts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(configure_flow, "_cuda_available", lambda: False)

    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="local",
            save_target="global",
            write_ignore_answer="",
        ),
    )

    assert result.exit_code == 0
    assert "Remote base URL" not in result.output
    assert "Remote model name" not in result.output
    assert "Remote API key" not in result.output
    assert "Local GGUF filename" in result.output


def test_configure_allow_ignore_updates_non_git_workspace_gitignore(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(configure_flow, "_cuda_available", lambda: False)

    result = runner.invoke(
        app,
        ["configure"],
        input=_configure_input(
            compression_mode="local",
            save_target="global",
            write_ignore_answer="",
        ),
    )

    assert result.exit_code == 0
    assert ".ctxsift/" in (tmp_path / ".gitignore").read_text(encoding="utf-8")
    assert "Add .ctxsift/ to the workspace .gitignore?" in result.output


def test_configure_no_write_ignore_override_skips_gitignore_update(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    isolated_config_paths: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(configure_flow, "_cuda_available", lambda: False)

    result = runner.invoke(
        app,
        ["configure", "--no-write-ignore"],
        input=_configure_input(compression_mode="local", save_target="global"),
    )

    assert result.exit_code == 0
    assert "Add .ctxsift/ to the workspace .gitignore?" not in result.output
    assert not (tmp_path / ".gitignore").exists()


def test_cli_help_mentions_configure_and_not_init() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Use `ctxsift configure` to set up ctxsift and the current workspace." in result.stdout
    assert "ctxsift init" not in result.stdout


def test_init_command_is_not_available() -> None:
    result = runner.invoke(app, ["init"])

    assert result.exit_code != 0
    assert "No such command 'init'" in result.output


def _configure_input(
    compression_mode: str,
    recall_default_limit: str = "10",
    local_device: str = "",
    local_model_cache_path: str = "",
    embedding_device: str = "auto",
    save_target: str = "global",
    write_ignore_answer: str | None = None,
    include_gguf_prompt: bool = True,
) -> str:
    values = [
        compression_mode,
        "512",
        "90000",
        "1",
    ]
    if compression_mode == "local":
        values.extend([local_device, ""])
        if include_gguf_prompt:
            values.append("")
        values.append(local_model_cache_path)
        values.append("auto")
    if compression_mode == "remote":
        values.extend(
            [
                "http://localhost:4000",
                "gpt-4o-mini",
                "sk-test",
                "2025-01-01",
                "auto",
            ]
        )
    values.extend(
        [
            "microsoft/harrier-oss-v1-0.6b",
            embedding_device,
            "auto",
            "",
            "",
            "",
            "32768",
            recall_default_limit,
            "50",
            "50",
            "0.75",
            "",
            save_target,
        ]
    )
    if write_ignore_answer is not None:
        values.append(write_ignore_answer)
    return "\n".join(values) + "\n"
