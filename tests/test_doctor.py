"""Tests for doctor checks."""

import asyncio
from dataclasses import dataclass
from pathlib import Path

import pytest

import ctxsift.doctor as doctor
from ctxsift.types import AppConfig, VectorStoreStatus


@dataclass(frozen=True)
class FakeResolvedConfig:
    config: AppConfig


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

    monkeypatch.setattr(doctor, "cuda_probe", lambda: (False, "CUDA is unavailable."))
    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (False, f"{label} is not installed."),
    )

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[optional] cuda: optional" in rendered
    assert "[optional] onnxruntime: optional" in rendered
    assert "[optional] flashattention: optional" in rendered


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


def test_doctor_reports_quantization_package_warnings_when_quanto_is_selected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    monkeypatch.setattr(
        doctor,
        "resolve_config",
        lambda request: FakeResolvedConfig(
            config=AppConfig.model_validate({"local": {"quantization": "quanto-int4"}})
        ),
    )
    monkeypatch.setattr(
        doctor,
        "optional_package_probe",
        lambda module_name, label: (False, f"{label} is not installed."),
    )
    monkeypatch.setattr(
        doctor,
        "optional_package_probe_any",
        lambda module_names, label: (False, f"{label} is not installed."),
    )

    report = asyncio.run(doctor.collect_doctor_report(repo_path))
    rendered = doctor.render_doctor_report(report)

    assert "[warning] accelerate: warning" in rendered
    assert "[warning] optimum_quanto: warning" in rendered
