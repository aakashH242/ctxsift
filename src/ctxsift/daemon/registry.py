"""Filesystem-backed daemon registry and startup locks."""

from __future__ import annotations

import os
from pathlib import Path
import secrets
import socket
import time
from uuid import uuid4

from platformdirs import user_cache_path

from ctxsift.daemon.types import DaemonLaunchPayload, DaemonRegistryRecord, DaemonRole


class StartupLockError(RuntimeError):
    """Raised when a daemon startup lock cannot be acquired in time."""


def daemon_root_dir() -> Path:
    """Return the root directory used for daemon state."""
    return user_cache_path("ctxsift") / "daemon"


def records_dir() -> Path:
    path = daemon_root_dir() / "records"
    path.mkdir(parents=True, exist_ok=True)
    return path


def launches_dir() -> Path:
    path = daemon_root_dir() / "launches"
    path.mkdir(parents=True, exist_ok=True)
    return path


def locks_dir() -> Path:
    path = daemon_root_dir() / "locks"
    path.mkdir(parents=True, exist_ok=True)
    return path


def logs_dir() -> Path:
    path = daemon_root_dir() / "logs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def registry_path(role: DaemonRole, signature_hash: str) -> Path:
    return records_dir() / f"{role.value}-{signature_hash}.json"


def launch_path(role: DaemonRole, signature_hash: str) -> Path:
    return launches_dir() / f"{role.value}-{signature_hash}.json"


def log_path(role: DaemonRole, signature_hash: str) -> Path:
    return logs_dir() / f"{role.value}-{signature_hash}.log"


def write_launch_payload(path: Path, payload: DaemonLaunchPayload) -> None:
    _atomic_write_text(path, payload.model_dump_json(indent=2))


def read_launch_payload(path: Path) -> DaemonLaunchPayload:
    return DaemonLaunchPayload.model_validate_json(path.read_text(encoding="utf-8"))


def write_registry_record(path: Path, record: DaemonRegistryRecord) -> None:
    _atomic_write_text(path, record.model_dump_json(indent=2))


def read_registry_record(path: Path) -> DaemonRegistryRecord:
    return DaemonRegistryRecord.model_validate_json(path.read_text(encoding="utf-8"))


def list_registry_paths() -> list[Path]:
    return sorted(records_dir().glob("*.json"))


def delete_file_if_present(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        return


def reserve_startup_lock(role: DaemonRole, signature_hash: str, timeout_ms: int) -> Path | None:
    """Try to reserve one startup lock; return None if another starter should proceed."""
    lock_path = locks_dir() / f"{role.value}-{signature_hash}.lock"
    deadline = time.monotonic() + (timeout_ms / 1000)
    stale_after_seconds = max(timeout_ms / 1000, 10)
    while time.monotonic() < deadline:
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            if _lock_is_stale(lock_path, stale_after_seconds):
                delete_file_if_present(lock_path)
                continue
            time.sleep(0.05)
            continue
        else:
            os.close(fd)
            return lock_path
    return None


def release_startup_lock(path: Path | None) -> None:
    if path is None:
        return
    delete_file_if_present(path)


def random_auth_token() -> str:
    return secrets.token_hex(32)


def allocate_loopback_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def tail_log_text(path: Path, limit: int = 2000) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= limit:
        return text
    return text[-limit:]


def delete_registry_record_if_owned(path: Path, pid: int) -> None:
    """Delete one registry record only when it still belongs to the given pid."""
    record = _safe_read_registry_record(path)
    if record is None:
        delete_file_if_present(path)
        return
    if record.pid == pid:
        delete_file_if_present(path)


def _atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_name(f"{path.name}.{uuid4().hex}.tmp")
    temp_path.write_text(text, encoding="utf-8")
    os.replace(temp_path, path)


def _lock_is_stale(path: Path, stale_after_seconds: float) -> bool:
    try:
        modified_at = path.stat().st_mtime
    except FileNotFoundError:
        return False
    return (time.time() - modified_at) >= stale_after_seconds


def _safe_read_registry_record(path: Path) -> DaemonRegistryRecord | None:
    try:
        return read_registry_record(path)
    except Exception:
        return None
