"""Tests for doctor checks."""

import asyncio
from dataclasses import dataclass
from pathlib import Path

import pytest

import ctxsift.doctor as doctor
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError
from ctxsift.types import AppConfig


@dataclass(frozen=True)
class FakeResolvedConfig:
    config: AppConfig


def test_doctor_reports_classified_warning_when_embedding_backend_unavailable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    def fail_backend(config):
        raise EmbeddingBackendUnavailableError("local embedding model is not cached")

    monkeypatch.setattr(doctor, "create_embedding_backend", fail_backend)

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
            config=AppConfig.model_validate({"run_mode": "remote"})
        ),
    )

    def fail_backend(config):
        raise EmbeddingBackendUnavailableError("local embedding model is not cached")

    monkeypatch.setattr(doctor, "create_embedding_backend", fail_backend)

    report = asyncio.run(doctor.collect_doctor_report(workspace_path))
    rendered = doctor.render_doctor_report(report)

    assert "[warning] remote_config: warning" in rendered
    assert "remote.base_url is missing" in rendered
    assert "[warning] git_workspace: warning" in rendered


def test_doctor_reports_optional_runtime_checks(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(doctor, "cuda_probe", lambda: (False, "CUDA is unavailable."))
    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (False, f"{label} is not installed."),
    )

    def fail_backend(config):
        raise EmbeddingBackendUnavailableError("local embedding model is not cached")

    monkeypatch.setattr(doctor, "create_embedding_backend", fail_backend)

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[optional] cuda: optional" in rendered
    assert "[optional] onnxruntime: optional" in rendered
    assert "[optional] flashattention: optional" in rendered
