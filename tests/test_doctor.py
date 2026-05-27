"""Tests for doctor checks."""

import asyncio
import sys
from dataclasses import dataclass
from pathlib import Path
import subprocess

import pytest

import ctxsift.diagnostics.doctor as doctor
import ctxsift.diagnostics.probes as probes
from ctxsift.config import store as config_store
from ctxsift.types import AppConfig, VectorStoreStatus


@dataclass(frozen=True)
class FakeResolvedConfig:
    config: AppConfig


@pytest.fixture(autouse=True)
def isolated_config_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Path:
    platform_path = tmp_path / "platform" / "config.toml"
    monkeypatch.setattr(config_store, "platform_global_config_path", lambda: platform_path)
    return platform_path


def test_doctor_reports_classified_warning_when_sqlite_vec_probe_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    async def failing_probe(db_path: Path) -> VectorStoreStatus:
        return VectorStoreStatus(
            available=False,
            warning="sqlite-vec is not installed; recall will use FTS5 only.",
        )

    monkeypatch.setattr(doctor, "probe_vector_store", failing_probe)

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[required] database: ok" in rendered
    assert "[required] sqlite_fts5: ok" in rendered
    assert "[warning] sqlite_vec: warning" in rendered
    assert "FTS5 only" in rendered


def test_doctor_reports_remote_config_warning_when_remote_is_incomplete(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    workspace_path = tmp_path / "workspace"
    workspace_path.mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate({"remote": {"base_url": "http://localhost:4000"}})
        ),
    )

    report = asyncio.run(doctor.collect_doctor_report(workspace_path))
    rendered = doctor.render_doctor_report(report)

    assert "[warning] remote_config: warning" in rendered
    assert "remote.model_name is missing" in rendered
    assert "[warning] git_workspace: warning" in rendered


def test_doctor_reports_optional_runtime_checks(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
        "resolve_config",
        lambda request: FakeResolvedConfig(config=AppConfig()),
    )

    monkeypatch.setattr(doctor, "cuda_probe", lambda: (False, "CUDA is unavailable."))
    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (False, f"{label} is not installed."),
    )
    monkeypatch.setattr(
        doctor,
        "resolve_local_runtime",
        lambda config: type("RuntimeSelection", (), {"uses_llama_cpp": False})(),
    )

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[optional] cuda: optional" in rendered
    assert "[optional] onnxruntime: optional" in rendered
    assert "[optional] flashattention: optional" in rendered


def test_doctor_skips_slow_cuda_probe_in_configure_mode(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
        "resolve_config",
        lambda request: FakeResolvedConfig(config=AppConfig()),
    )
    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (True, f"{label} is available."),
    )
    monkeypatch.setattr(
        doctor,
        "resolve_local_runtime",
        lambda config: type("RuntimeSelection", (), {"uses_llama_cpp": False})(),
    )

    def fail_if_called() -> tuple[bool, str]:
        raise AssertionError("cuda_probe should be skipped in configure mode")

    monkeypatch.setattr(doctor, "cuda_probe", fail_if_called)

    report = asyncio.run(
        doctor.collect_doctor_report(
            repo_path,
            options=doctor.DoctorOptions(include_slow_optional_runtime_checks=False),
        )
    )
    rendered = doctor.render_doctor_report(report)

    assert "[optional] cuda:" not in rendered
    assert "[optional] onnxruntime: ok" in rendered


def test_doctor_progress_reports_each_check(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
        "resolve_config",
        lambda request: FakeResolvedConfig(config=AppConfig()),
    )
    monkeypatch.setattr(doctor, "cuda_probe", lambda: (False, "CUDA is unavailable."))
    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (False, f"{label} is not installed."),
    )
    monkeypatch.setattr(
        doctor,
        "resolve_local_runtime",
        lambda config: type("RuntimeSelection", (), {"uses_llama_cpp": False})(),
    )

    messages: list[str] = []
    asyncio.run(
        doctor.collect_doctor_report(
            repo_path,
            options=doctor.DoctorOptions(progress=messages.append),
        )
    )

    assert "Health check: database..." in messages
    assert any(message.startswith("[required] database: ok") for message in messages)
    assert any(message.startswith("Health check: cuda...") for message in messages)


def test_doctor_warns_when_remote_is_enabled_without_litellm(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
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

    def fake_optional_package_probe(module_name: str, label: str) -> tuple[bool, str]:
        if module_name == "litellm":
            return False, f"{label} is not installed."
        return True, f"{label} is available."

    monkeypatch.setattr(doctor, "optional_package_probe", fake_optional_package_probe)

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[warning] litellm: warning" in rendered
    assert 'uv tool install "ctxsift[remote]"' in rendered
    assert "remote compression will not work" in rendered


def test_doctor_reports_model_mismatch_without_loading_embedding_backend(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    async def mismatched_probe(db_path: Path) -> VectorStoreStatus:
        return VectorStoreStatus(
            available=True,
            model_name="different-model",
            dimension=1024,
            sqlite_vec_version="v0.1.9",
        )

    monkeypatch.setattr(doctor, "probe_vector_store", mismatched_probe)

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[warning] sqlite_vec: warning" in rendered
    assert "model mismatch" in rendered


def test_doctor_reports_llama_cpp_checks_for_local_cpu_runtime(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate({"local": {"device": "cpu"}})
        ),
    )

    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (
            (False, f"{label} is not installed.")
            if module_name == "llama_cpp"
            else (True, f"{label} is available.")
        ),
    )
    monkeypatch.setattr(
        doctor,
        "resolve_local_runtime",
        lambda config: type("RuntimeSelection", (), {"uses_llama_cpp": True})(),
    )
    monkeypatch.setattr(
        doctor,
        "_gguf_resolution_check",
        lambda config: doctor.DoctorCheck(
            name="gguf_artifact",
            severity="warning",
            ok=True,
            detail="Configured GGUF artifact is not cached locally yet.",
        ),
    )

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[optional] llama_cpp: optional" in rendered
    assert "gguf_artifact: ok" in rendered


def test_cuda_probe_times_out_cleanly(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_run(*args, **kwargs):
        raise subprocess.TimeoutExpired(cmd="python -c ...", timeout=8.0)

    monkeypatch.setattr(probes.subprocess, "run", fake_run)

    ok, detail = probes.cuda_probe()

    assert ok is False
    assert "timed out" in detail


def test_gguf_resolution_check_reports_missing_hf_hub(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delitem(sys.modules, "huggingface_hub", raising=False)

    real_import = __import__

    def fake_import(name, *args, **kwargs):
        if name == "huggingface_hub":
            raise ImportError("No module named 'huggingface_hub'")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr("builtins.__import__", fake_import)

    check = doctor._gguf_resolution_check(AppConfig())

    assert check.ok is False
    assert "huggingface_hub is unavailable" in check.detail


def test_doctor_reports_gpu_quantization_package_warnings_when_bnb_is_selected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate(
                {"local": {"device": "cuda", "quantization": "bnb-4bit-nf4"}}
            )
        ),
    )
    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (False, f"{label} is not installed."),
    )
    monkeypatch.setattr(
        doctor,
        "resolve_local_runtime",
        lambda config: type("RuntimeSelection", (), {"uses_llama_cpp": False})(),
    )

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[warning] accelerate: warning" in rendered
    assert "[warning] bitsandbytes: warning" in rendered
