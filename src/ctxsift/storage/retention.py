"""Background retention scheduling for persisted workspace records."""

from __future__ import annotations

import asyncio
import hashlib
import os
from pathlib import Path
import threading
import time

from platformdirs import user_cache_path

from ctxsift.storage.database import prune_expired_records, retention_cleanup_due

RETENTION_CLEANUP_INTERVAL_SECONDS = 3600
RETENTION_LOCK_STALE_AFTER_SECONDS = 300

_running_cleanup_threads: dict[str, threading.Thread] = {}
_running_cleanup_lock = threading.Lock()


async def schedule_retention_cleanup(db_path: Path, max_age_days: int) -> bool:
    """Start one best-effort background cleanup when due and not already running."""
    normalized_db_path = str(db_path.expanduser().resolve())
    if not await retention_cleanup_due(
        Path(normalized_db_path),
        RETENTION_CLEANUP_INTERVAL_SECONDS,
    ):
        return False
    with _running_cleanup_lock:
        _prune_finished_threads()
        if normalized_db_path in _running_cleanup_threads:
            return False
        lock_path = _lock_path_for_database(Path(normalized_db_path))
        if not _reserve_lock(lock_path):
            return False
        cleanup_thread = threading.Thread(
            target=_run_cleanup_thread,
            args=(Path(normalized_db_path), max_age_days, normalized_db_path, lock_path),
            name=f"ctxsift-retention-{hashlib.sha256(normalized_db_path.encode('utf-8')).hexdigest()[:8]}",
            daemon=True,
        )
        _running_cleanup_threads[normalized_db_path] = cleanup_thread
        try:
            cleanup_thread.start()
        except Exception:
            _running_cleanup_threads.pop(normalized_db_path, None)
            _release_lock(lock_path)
            raise
        return True


def _run_cleanup_thread(
    db_path: Path,
    max_age_days: int,
    normalized_db_path: str,
    lock_path: Path,
) -> None:
    try:
        asyncio.run(prune_expired_records(db_path, max_age_days))
    except Exception:
        return
    finally:
        _release_lock(lock_path)
        with _running_cleanup_lock:
            current_thread = _running_cleanup_threads.get(normalized_db_path)
            if current_thread is threading.current_thread():
                _running_cleanup_threads.pop(normalized_db_path, None)


def _lock_path_for_database(db_path: Path) -> Path:
    lock_name = hashlib.sha256(str(db_path).encode("utf-8")).hexdigest()
    lock_dir = user_cache_path("ctxsift") / "retention" / "locks"
    lock_dir.mkdir(parents=True, exist_ok=True)
    return lock_dir / f"{lock_name}.lock"


def _reserve_lock(lock_path: Path) -> bool:
    if _lock_is_stale(lock_path):
        _release_lock(lock_path)
    try:
        fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.close(fd)
    return True


def _release_lock(lock_path: Path) -> None:
    try:
        lock_path.unlink()
    except FileNotFoundError:
        return


def _lock_is_stale(lock_path: Path) -> bool:
    try:
        modified_at = lock_path.stat().st_mtime
    except FileNotFoundError:
        return False
    return (time.time() - modified_at) >= RETENTION_LOCK_STALE_AFTER_SECONDS


def _prune_finished_threads() -> None:
    finished_paths = [
        db_path
        for db_path, cleanup_thread in _running_cleanup_threads.items()
        if not cleanup_thread.is_alive()
    ]
    for db_path in finished_paths:
        _running_cleanup_threads.pop(db_path, None)
