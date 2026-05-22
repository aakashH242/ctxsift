"""Daemon startup, discovery, and lifecycle management."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

from ctxsift.daemon.client import DaemonClientError, read_health, request_stop
from ctxsift.daemon.registry import (
    allocate_loopback_port,
    delete_file_if_present,
    launch_path,
    list_registry_paths,
    log_path,
    random_auth_token,
    read_registry_record,
    registry_path,
    release_startup_lock,
    reserve_startup_lock,
    tail_log_text,
    write_launch_payload,
)
from ctxsift.daemon.signatures import (
    build_compression_signature,
    build_embedding_signature,
    signature_hash,
)
from ctxsift.daemon.types import (
    DaemonLaunchPayload,
    DaemonRegistryRecord,
    DaemonRole,
    DaemonStatus,
    RuntimeSignature,
)
from ctxsift.models.local_runtime import resolve_local_runtime
from ctxsift.types import AppConfig, DaemonConfig, EmbeddingConfig, LocalModelConfig

START_POLL_INTERVAL_SECONDS = 0.1
STOP_POLL_INTERVAL_SECONDS = 0.1
HEALTH_TIMEOUT_MS = 1500


@dataclass(frozen=True)
class DaemonSpec:
    """One desired daemon instance."""

    role: DaemonRole
    signature: RuntimeSignature
    signature_hash: str
    model: str
    device: str
    daemon_config: DaemonConfig
    local_config: LocalModelConfig | None = None
    embedding_config: EmbeddingConfig | None = None


def required_daemon_specs(config: AppConfig) -> list[DaemonSpec]:
    """Return the daemon specs implied by one resolved config."""
    if not config.daemon.enabled:
        return []
    specs = [embedding_daemon_spec(config.embedding, config.daemon)]
    if not config.remote.base_url.strip():
        specs.append(compression_daemon_spec(config.local, config.daemon))
    return specs


def compression_daemon_spec(config: LocalModelConfig, daemon: DaemonConfig) -> DaemonSpec:
    """Build one compression daemon spec."""
    signature = build_compression_signature(config)
    runtime = resolve_local_runtime(config)
    digest = signature_hash(signature)
    return DaemonSpec(
        role=DaemonRole.COMPRESSION,
        signature=signature,
        signature_hash=digest,
        model=config.model,
        device=runtime.resolved_device.label,
        daemon_config=daemon,
        local_config=config,
    )


def embedding_daemon_spec(config: EmbeddingConfig, daemon: DaemonConfig) -> DaemonSpec:
    """Build one embedding daemon spec."""
    signature = build_embedding_signature(config)
    digest = signature_hash(signature)
    return DaemonSpec(
        role=DaemonRole.EMBEDDING,
        signature=signature,
        signature_hash=digest,
        model=config.model,
        device=config.device,
        daemon_config=daemon,
        embedding_config=config,
    )


def ensure_daemon(spec: DaemonSpec) -> DaemonRegistryRecord:
    """Ensure one daemon is running and healthy."""
    existing = _healthy_registry_record(spec)
    if existing is not None:
        return existing
    lock_path = reserve_startup_lock(
        role=spec.role,
        signature_hash=spec.signature_hash,
        timeout_ms=spec.daemon_config.startup_timeout_ms,
    )
    if lock_path is None:
        record = _wait_for_daemon(spec, spec.daemon_config.startup_timeout_ms)
        if record is not None:
            return record
        raise RuntimeError(
            f"Timed out waiting for {spec.role.value} daemon startup lock for {spec.model}."
        )
    try:
        existing = _healthy_registry_record(spec)
        if existing is not None:
            return existing
        payload = _launch_payload(spec)
        launch_file = launch_path(spec.role, spec.signature_hash)
        delete_file_if_present(launch_file)
        write_launch_payload(launch_file, payload)
        process = _start_worker_process(payload, launch_file)
        record = _wait_for_daemon(spec, spec.daemon_config.startup_timeout_ms, process)
        if record is None:
            detail = tail_log_text(log_path(spec.role, spec.signature_hash)).strip()
            raise RuntimeError(
                f"Failed to start {spec.role.value} daemon for {spec.model}."
                + (f" Log tail: {detail}" if detail else "")
            )
        delete_file_if_present(launch_file)
        return record
    finally:
        release_startup_lock(lock_path)


def stop_daemon(spec: DaemonSpec) -> DaemonStatus:
    """Stop one daemon implied by the current config."""
    path = registry_path(spec.role, spec.signature_hash)
    if not path.exists():
        return DaemonStatus(
            role=spec.role,
            signature_hash=spec.signature_hash,
            model=spec.model,
            device=spec.device,
            healthy=False,
            detail="not running",
        )
    record = _read_valid_record(path)
    if record is None:
        delete_file_if_present(path)
        return DaemonStatus(
            role=spec.role,
            signature_hash=spec.signature_hash,
            model=spec.model,
            device=spec.device,
            healthy=False,
            detail="removed stale registry entry",
        )
    return _stop_record(record, path)


def stop_all_daemons() -> list[DaemonStatus]:
    """Stop all registered daemons."""
    results: list[DaemonStatus] = []
    for path in list_registry_paths():
        record = _read_valid_record(path)
        if record is None:
            delete_file_if_present(path)
            continue
        results.append(_stop_record(record, path))
    return results


def daemon_statuses(config: AppConfig, include_all: bool = False) -> list[DaemonStatus]:
    """Return daemon status rows for the current config or all registered daemons."""
    if include_all:
        return _all_daemon_statuses()
    return [_status_for_spec(spec) for spec in required_daemon_specs(config)]


def startup_statuses(config: AppConfig) -> list[DaemonStatus]:
    """Start the daemons implied by the current config and return status rows."""
    statuses: list[DaemonStatus] = []
    for spec in required_daemon_specs(config):
        superseded_records = _superseded_registry_records(spec)
        already_running = _healthy_registry_record(spec) is not None
        record = ensure_daemon(spec)
        statuses.append(
            DaemonStatus(
                role=record.role,
                signature_hash=record.signature_hash,
                model=record.model,
                device=record.device,
                pid=record.pid,
                port=record.port,
                healthy=True,
                detail="already running" if already_running else "started",
            )
        )
        statuses.extend(_supersede_record(record, spec) for record in superseded_records)
    return statuses


def _all_daemon_statuses() -> list[DaemonStatus]:
    statuses: list[DaemonStatus] = []
    for path in list_registry_paths():
        record = _read_valid_record(path)
        if record is None:
            delete_file_if_present(path)
            continue
        if _record_is_healthy(record):
            statuses.append(
                DaemonStatus(
                    role=record.role,
                    signature_hash=record.signature_hash,
                    model=record.model,
                    device=record.device,
                    pid=record.pid,
                    port=record.port,
                    healthy=True,
                    detail="running",
                )
            )
            continue
        delete_file_if_present(path)
        statuses.append(
            DaemonStatus(
                role=record.role,
                signature_hash=record.signature_hash,
                model=record.model,
                device=record.device,
                pid=record.pid,
                port=record.port,
                healthy=False,
                detail="stale registry entry",
            )
        )
    return statuses


def _status_for_spec(spec: DaemonSpec) -> DaemonStatus:
    record = _healthy_registry_record(spec)
    if record is not None:
        return DaemonStatus(
            role=record.role,
            signature_hash=record.signature_hash,
            model=record.model,
            device=record.device,
            pid=record.pid,
            port=record.port,
            healthy=True,
            detail="running",
        )
    return DaemonStatus(
        role=spec.role,
        signature_hash=spec.signature_hash,
        model=spec.model,
        device=spec.device,
        healthy=False,
        detail="not running",
    )


def _superseded_registry_records(spec: DaemonSpec) -> list[DaemonRegistryRecord]:
    records: list[DaemonRegistryRecord] = []
    for path in list_registry_paths():
        record = _read_valid_record(path)
        if record is None:
            delete_file_if_present(path)
            continue
        if record.role is not spec.role:
            continue
        if record.signature_hash == spec.signature_hash:
            continue
        if not _record_is_healthy(record):
            delete_file_if_present(path)
            continue
        records.append(record)
    return records


def forget_daemon(spec: DaemonSpec) -> None:
    """Remove one daemon registry entry so the next request restarts it."""
    delete_file_if_present(registry_path(spec.role, spec.signature_hash))


def _healthy_registry_record(spec: DaemonSpec) -> DaemonRegistryRecord | None:
    path = registry_path(spec.role, spec.signature_hash)
    record = _read_valid_record(path)
    if record is None:
        delete_file_if_present(path)
        return None
    if _record_is_healthy(record):
        return record
    delete_file_if_present(path)
    return None


def _read_valid_record(path: Path) -> DaemonRegistryRecord | None:
    try:
        return read_registry_record(path)
    except FileNotFoundError:
        return None
    except Exception:
        return None


def _record_is_healthy(record: DaemonRegistryRecord) -> bool:
    try:
        read_health(record, timeout_ms=HEALTH_TIMEOUT_MS)
    except DaemonClientError:
        return False
    return True


def _wait_for_daemon(
    spec: DaemonSpec,
    timeout_ms: int,
    process: subprocess.Popen[str] | None = None,
) -> DaemonRegistryRecord | None:
    deadline = time.monotonic() + max(timeout_ms, 1) / 1000
    while time.monotonic() < deadline:
        record = _healthy_registry_record(spec)
        if record is not None:
            return record
        if process is not None and process.poll() is not None:
            return None
        time.sleep(START_POLL_INTERVAL_SECONDS)
    return None


def _wait_for_registry_removal(path: Path, timeout_ms: int) -> None:
    deadline = time.monotonic() + max(timeout_ms, 1) / 1000
    while path.exists() and time.monotonic() < deadline:
        time.sleep(STOP_POLL_INTERVAL_SECONDS)
    delete_file_if_present(path)


def _start_worker_process(payload: DaemonLaunchPayload, launch_file: Path) -> subprocess.Popen[Any]:
    log_file = Path(payload.log_path)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        create_new_process_group = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
        create_new_console = getattr(subprocess, "CREATE_NEW_CONSOLE", 0x00000010)
        python_executable = subprocess.list2cmdline([sys.executable])
        launch_file_arg = subprocess.list2cmdline([str(launch_file)])
        daemon_command = (
            f"{python_executable} -m ctxsift.daemon_worker --launch-file {launch_file_arg}"
        )
        return subprocess.Popen(
            args=["cmd.exe", "/k", daemon_command],
            stdin=subprocess.DEVNULL,
            cwd=str(Path.cwd()),
            close_fds=True,
            creationflags=create_new_process_group | create_new_console,
        )
    output_handle = log_file.open("a", encoding="utf-8")
    try:  # pragma: no cover - Windows is primary env, but keep POSIX-safe.
        return subprocess.Popen(
            args=[
                sys.executable,
                "-m",
                "ctxsift.daemon_worker",
                "--launch-file",
                str(launch_file),
            ],
            stdin=subprocess.DEVNULL,
            cwd=str(Path.cwd()),
            close_fds=True,
            stdout=output_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    finally:
        output_handle.close()


def _launch_payload(spec: DaemonSpec) -> DaemonLaunchPayload:
    return DaemonLaunchPayload(
        role=spec.role,
        signature_hash=spec.signature_hash,
        port=allocate_loopback_port(),
        auth_token=random_auth_token(),
        registry_path=str(registry_path(spec.role, spec.signature_hash)),
        log_path=str(log_path(spec.role, spec.signature_hash)),
        daemon=spec.daemon_config,
        local=spec.local_config,
        embedding=spec.embedding_config,
    )


def _stop_record(record: DaemonRegistryRecord, path: Path) -> DaemonStatus:
    if not _record_is_healthy(record):
        delete_file_if_present(path)
        return DaemonStatus(
            role=record.role,
            signature_hash=record.signature_hash,
            model=record.model,
            device=record.device,
            pid=record.pid,
            port=record.port,
            healthy=False,
            detail="removed stale registry entry",
        )
    try:
        request_stop(record, timeout_ms=2000)
    except DaemonClientError as error:
        delete_file_if_present(path)
        return DaemonStatus(
            role=record.role,
            signature_hash=record.signature_hash,
            model=record.model,
            device=record.device,
            pid=record.pid,
            port=record.port,
            healthy=False,
            detail=f"stop request failed; removed registry entry ({error})",
        )
    _wait_for_registry_removal(path, 5000)
    return DaemonStatus(
        role=record.role,
        signature_hash=record.signature_hash,
        model=record.model,
        device=record.device,
        pid=record.pid,
        port=record.port,
        healthy=False,
        detail="stopped",
    )


def _supersede_record(record: DaemonRegistryRecord, spec: DaemonSpec) -> DaemonStatus:
    stopped_status = _stop_record(record, registry_path(record.role, record.signature_hash))
    supersede_detail = (
        f"superseded by current config ({spec.model} {spec.device})"
        if stopped_status.detail == "stopped"
        else f"{stopped_status.detail}; superseded by current config ({spec.model} {spec.device})"
    )
    return DaemonStatus(
        role=stopped_status.role,
        signature_hash=stopped_status.signature_hash,
        model=stopped_status.model,
        device=stopped_status.device,
        pid=stopped_status.pid,
        port=stopped_status.port,
        healthy=stopped_status.healthy,
        detail=supersede_detail,
    )
