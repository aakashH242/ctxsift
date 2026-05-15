"""Tests for workspace db path discovery and SQLite storage."""

import asyncio
from pathlib import Path
import sqlite3

from ctxsift.storage import initialize_database, insert_record_bundle, read_schema_version
from ctxsift.types import ExtractedTermRecord, ReferencedFileRecord, StoredRecord
from ctxsift.workspace import detect_workspace_context


def test_git_workspace_context_sets_default_db_path(tmp_path: Path) -> None:
    repo_path = tmp_path / "repo"
    (repo_path / ".git").mkdir(parents=True)

    workspace = detect_workspace_context(repo_path)

    assert workspace.db_path is not None
    assert workspace.db_path.endswith(".git\\ctxsift\\ctxsift.db")


def test_non_git_workspace_context_sets_default_db_path(tmp_path: Path) -> None:
    workspace = detect_workspace_context(tmp_path)

    assert workspace.db_path is not None
    assert workspace.db_path.endswith(".ctxsift\\ctxsift.db")


def test_initialize_database_creates_schema_and_version(tmp_path: Path) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"

    result = asyncio.run(initialize_database(db_path))

    assert result.db_path == db_path
    assert asyncio.run(read_schema_version(db_path)) == "2"
    with sqlite3.connect(db_path) as connection:
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type IN ('table', 'view')"
            ).fetchall()
        }
    assert "schema_info" in tables
    assert "records" in tables
    assert "records_fts" in tables
    assert "referenced_files" in tables
    assert "extracted_terms" in tables


def test_insert_record_bundle_persists_record_and_search_rows(tmp_path: Path) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"
    asyncio.run(initialize_database(db_path))
    record = StoredRecord(
        instruction="show auth failures",
        normalized_instruction="show auth failures",
        compressed_output="AuthError in tests/test_auth.py",
        raw_input_hash="abc123",
        mode="pipe",
        workspace_root=str(tmp_path),
        cwd=str(tmp_path),
        command="pytest -q",
        max_output_tokens=512,
    )
    referenced_files = [
        ReferencedFileRecord(
            path="tests/test_auth.py",
            abs_path=str(tmp_path / "tests" / "test_auth.py"),
            sha256="deadbeef",
            exists_at_capture=True,
        )
    ]
    extracted_terms = [
        ExtractedTermRecord(term="AuthError", kind="error_class"),
    ]

    record_id = asyncio.run(
        insert_record_bundle(
            db_path,
            record,
            referenced_files=referenced_files,
            extracted_terms=extracted_terms,
        )
    )

    with sqlite3.connect(db_path) as connection:
        stored_record = connection.execute(
            "SELECT instruction, compressed_output FROM records WHERE id = ?",
            (record_id,),
        ).fetchone()
        fts_matches = connection.execute(
            "SELECT rowid FROM records_fts WHERE records_fts MATCH 'AuthError'"
        ).fetchall()
        file_row = connection.execute(
            "SELECT path, exists_at_capture FROM referenced_files WHERE record_id = ?",
            (record_id,),
        ).fetchone()
        term_row = connection.execute(
            "SELECT term, kind FROM extracted_terms WHERE record_id = ?",
            (record_id,),
        ).fetchone()

    assert stored_record == ("show auth failures", "AuthError in tests/test_auth.py")
    assert fts_matches == [(record_id,)]
    assert file_row == ("tests/test_auth.py", 1)
    assert term_row == ("AuthError", "error_class")
