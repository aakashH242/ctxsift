"""Tests for doctor checks."""

import asyncio
from pathlib import Path

import pytest

import ctxsift.doctor as doctor
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError


def test_doctor_reports_warning_when_embedding_backend_unavailable(
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

    assert "sqlite_fts5: ok" in rendered
    assert "sqlite_vec: warning" in rendered
    assert "FTS5 only" in rendered
