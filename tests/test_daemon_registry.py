"""Tests for daemon registry helpers."""

from __future__ import annotations

import os
import time
from pathlib import Path

import pytest

import ctxsift.daemon.registry as registry
from ctxsift.daemon.types import DaemonRegistryRecord, DaemonRole


@pytest.fixture()
def isolated_daemon_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    root = tmp_path / "daemon-root"
    monkeypatch.setattr(registry, "daemon_root_dir", lambda: root)
    return root


def test_reserve_startup_lock_reclaims_stale_lock(
    isolated_daemon_root: Path,
) -> None:
    lock_path = registry.locks_dir() / "compression-stale.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path.write_text("", encoding="utf-8")
    old_time = time.time() - 60
    os.utime(lock_path, (old_time, old_time))

    reserved = registry.reserve_startup_lock(
        role=DaemonRole.COMPRESSION,
        signature_hash="stale",
        timeout_ms=100,
    )

    assert reserved == lock_path
    registry.release_startup_lock(reserved)


def test_delete_registry_record_if_owned_preserves_newer_daemon_record(
    isolated_daemon_root: Path,
) -> None:
    path = registry.registry_path(DaemonRole.COMPRESSION, "shared")
    record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash="shared",
        model="fake/model",
        device="cpu",
        pid=200,
        port=5050,
        auth_token="token",
    )
    registry.write_registry_record(path, record)

    registry.delete_registry_record_if_owned(path, pid=100)

    assert path.exists()
    assert registry.read_registry_record(path).pid == 200


def test_delete_registry_record_if_owned_removes_matching_record(
    isolated_daemon_root: Path,
) -> None:
    path = registry.registry_path(DaemonRole.COMPRESSION, "shared")
    record = DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash="shared",
        model="fake/model",
        device="cpu",
        pid=200,
        port=5050,
        auth_token="token",
    )
    registry.write_registry_record(path, record)

    registry.delete_registry_record_if_owned(path, pid=200)

    assert path.exists() is False
