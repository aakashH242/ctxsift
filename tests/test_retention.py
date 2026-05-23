"""Tests for background record-retention cleanup."""

import asyncio
from pathlib import Path
import sqlite3

import pytest

from ctxsift.storage import retention
from ctxsift.storage import (
    initialize_database,
    insert_record_bundle,
    prune_expired_records,
    retention_cleanup_due,
)
from ctxsift.types import ExtractedTermRecord, ReferencedFileRecord, StoredRecord


def test_prune_expired_records_deletes_old_rows_and_related_rows(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"
    asyncio.run(initialize_database(db_path))
    old_record_id = asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="old auth failure",
                normalized_instruction="old auth failure",
                compressed_output="OldAuthError in src/old.py",
                raw_input_hash="hash-old",
                mode="pipe",
                workspace_root=str(tmp_path),
                cwd=str(tmp_path),
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/old.py",
                    abs_path=str(tmp_path / "src" / "old.py"),
                    sha256="sha-old",
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[ExtractedTermRecord(term="OldAuthError", kind="symbol")],
        )
    )
    fresh_record_id = asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="fresh auth failure",
                normalized_instruction="fresh auth failure",
                compressed_output="FreshAuthError in src/fresh.py",
                raw_input_hash="hash-fresh",
                mode="pipe",
                workspace_root=str(tmp_path),
                cwd=str(tmp_path),
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/fresh.py",
                    abs_path=str(tmp_path / "src" / "fresh.py"),
                    sha256="sha-fresh",
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[ExtractedTermRecord(term="FreshAuthError", kind="symbol")],
        )
    )
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            "UPDATE records SET created_at = '2000-01-01 00:00:00' WHERE id = ?",
            (old_record_id,),
        )
        connection.commit()
    deleted_embeddings: list[int] = []

    async def fake_delete_record_embeddings(db_path: Path, record_ids: list[int]):
        deleted_embeddings.extend(record_ids)
        return None

    monkeypatch.setattr(
        "ctxsift.storage.database.delete_record_embeddings", fake_delete_record_embeddings
    )

    result = asyncio.run(prune_expired_records(db_path, max_age_days=30))

    assert result.deleted_record_count == 1
    assert result.deleted_record_ids == [old_record_id]
    assert deleted_embeddings == [old_record_id]
    with sqlite3.connect(db_path) as connection:
        records = connection.execute("SELECT id FROM records ORDER BY id ASC").fetchall()
        referenced_files = connection.execute(
            "SELECT record_id, path FROM referenced_files ORDER BY record_id ASC"
        ).fetchall()
        extracted_terms = connection.execute(
            "SELECT record_id, term FROM extracted_terms ORDER BY record_id ASC"
        ).fetchall()
        fts_matches = connection.execute(
            "SELECT rowid FROM records_fts WHERE records_fts MATCH 'OldAuthError'"
        ).fetchall()
        last_run = connection.execute(
            "SELECT value FROM schema_info WHERE key = 'retention_last_run_at'"
        ).fetchone()

    assert records == [(fresh_record_id,)]
    assert referenced_files == [(fresh_record_id, "src/fresh.py")]
    assert extracted_terms == [(fresh_record_id, "FreshAuthError")]
    assert fts_matches == []
    assert last_run is not None


def test_retention_cleanup_due_is_false_after_recent_run(tmp_path: Path) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"
    asyncio.run(initialize_database(db_path))
    asyncio.run(prune_expired_records(db_path, max_age_days=30))

    due = asyncio.run(retention_cleanup_due(db_path, interval_seconds=3600))

    assert due is False


def test_schedule_retention_cleanup_skips_when_one_is_already_running(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"
    asyncio.run(initialize_database(db_path))
    retention._running_cleanup_threads.clear()

    async def always_due(db_path: Path, interval_seconds: int) -> bool:
        return True

    monkeypatch.setattr(retention, "retention_cleanup_due", always_due)
    monkeypatch.setattr(retention, "_reserve_lock", lambda path: True)
    monkeypatch.setattr(retention, "_release_lock", lambda path: None)

    class FakeThread:
        def __init__(self, *args, **kwargs) -> None:
            self.started = False

        def start(self) -> None:
            self.started = True

        def is_alive(self) -> bool:
            return self.started

    monkeypatch.setattr(retention.threading, "Thread", FakeThread)

    first = asyncio.run(retention.schedule_retention_cleanup(db_path, max_age_days=30))
    second = asyncio.run(retention.schedule_retention_cleanup(db_path, max_age_days=30))

    retention._running_cleanup_threads.clear()
    assert first is True
    assert second is False
