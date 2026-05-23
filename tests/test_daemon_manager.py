"""Tests for daemon manager lifecycle helpers."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

import ctxsift.daemon.manager as manager
from ctxsift.daemon.client import DaemonClientError
from ctxsift.daemon.types import DaemonLaunchPayload, DaemonRegistryRecord, DaemonRole
from ctxsift.types import AppConfig, DaemonConfig, EmbeddingConfig, LocalModelConfig


def test_ensure_daemon_reuses_healthy_existing_record(monkeypatch: pytest.MonkeyPatch) -> None:
    spec = manager.compression_daemon_spec(AppConfig().local, AppConfig().daemon)
    record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash=spec.signature_hash,
        model=spec.model,
        device=spec.device,
        pid=123,
        port=4040,
        auth_token="token",
    )
    monkeypatch.setattr(manager, "_healthy_registry_record", lambda current_spec: record)

    result = manager.ensure_daemon(spec)

    assert result == record


def test_daemon_statuses_all_marks_stale_registry_entries(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stale_path = tmp_path / "compression-stale.json"
    stale_path.write_text("stale", encoding="utf-8")
    record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash="stale",
        model="fake/model",
        device="cpu",
        pid=456,
        port=5050,
        auth_token="token",
    )
    monkeypatch.setattr(manager, "list_registry_paths", lambda: [stale_path])
    monkeypatch.setattr(manager, "_read_valid_record", lambda path: record)
    monkeypatch.setattr(
        manager,
        "read_health",
        lambda record_arg, timeout_ms=1500: (_ for _ in ()).throw(DaemonClientError("down")),
    )

    statuses = manager.daemon_statuses(AppConfig(), include_all=True)

    assert len(statuses) == 1
    assert statuses[0].healthy is False
    assert statuses[0].detail == "stale registry entry"
    assert stale_path.exists() is False


def test_required_daemon_specs_in_remote_mode_only_need_embeddings() -> None:
    config = AppConfig.model_validate(
        {"remote": {"base_url": "http://localhost:4000", "model_name": "gpt-5-mini"}}
    )

    specs = manager.required_daemon_specs(config)

    assert [spec.role for spec in specs] == [DaemonRole.EMBEDDING]


def test_required_daemon_specs_respect_disabled_daemon_kill_switch() -> None:
    config = AppConfig.model_validate({"daemon": {"enabled": False}})

    assert manager.required_daemon_specs(config) == []


def test_startup_statuses_reports_superseded_same_role_daemon(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = AppConfig.model_validate({"local": {"device": "cpu"}})
    spec = manager.compression_daemon_spec(config.local, config.daemon)
    old_record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash="old-signature",
        model="old/model",
        device="cpu",
        pid=456,
        port=5050,
        auth_token="token",
    )
    current_record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash=spec.signature_hash,
        model=spec.model,
        device=spec.device,
        pid=123,
        port=4040,
        auth_token="token",
    )
    stale_path = tmp_path / "compression-old.json"
    stale_path.write_text("{}", encoding="utf-8")

    monkeypatch.setattr(manager, "required_daemon_specs", lambda current_config: [spec])
    monkeypatch.setattr(manager, "_healthy_registry_record", lambda current_spec: None)
    monkeypatch.setattr(manager, "ensure_daemon", lambda current_spec: current_record)
    monkeypatch.setattr(manager, "list_registry_paths", lambda: [stale_path])
    monkeypatch.setattr(manager, "_read_valid_record", lambda path: old_record)
    monkeypatch.setattr(manager, "_record_is_healthy", lambda record: True)
    monkeypatch.setattr(
        manager,
        "_stop_record",
        lambda record, path: manager.DaemonStatus(
            role=record.role,
            signature_hash=record.signature_hash,
            model=record.model,
            device=record.device,
            pid=record.pid,
            port=record.port,
            healthy=False,
            detail="stopped",
        ),
    )

    statuses = manager.startup_statuses(config)

    assert len(statuses) == 2
    assert statuses[0].detail == "started"
    assert statuses[1].model == "old/model"
    assert "superseded by current config" in statuses[1].detail


def test_start_worker_process_uses_new_console_on_windows(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    payload = DaemonLaunchPayload(
        role=DaemonRole.COMPRESSION,
        signature_hash="sig",
        port=4012,
        auth_token="token",
        registry_path=str(tmp_path / "registry.json"),
        log_path=str(tmp_path / "daemon.log"),
        daemon=DaemonConfig(),
        local=LocalModelConfig(model="ibm-granite/granite-4.0-350m-GGUF", device="cpu"),
        embedding=EmbeddingConfig(),
    )
    captured: dict[str, Any] = {}

    monkeypatch.setattr(manager.os, "name", "nt")
    monkeypatch.setattr(manager.subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200, raising=False)
    monkeypatch.setattr(manager.subprocess, "CREATE_NEW_CONSOLE", 0x00000010, raising=False)
    monkeypatch.setattr(manager.sys, "executable", r"C:\Python312\python.exe")

    def fake_popen(**kwargs):
        captured.update(kwargs)
        return SimpleNamespace()

    monkeypatch.setattr(manager.subprocess, "Popen", fake_popen)

    manager._start_worker_process(payload, tmp_path / "launch.json")

    assert captured["creationflags"] == 0x00000210
    assert captured["args"][0:2] == ["cmd.exe", "/c"]
    assert "ctxsift.daemon_worker" in captured["args"][2]
    assert "--launch-file" in captured["args"][2]
    assert r"C:\Python312\python.exe" in captured["args"][2]
    assert "stdout" not in captured
    assert "stderr" not in captured
    assert "start_new_session" not in captured
