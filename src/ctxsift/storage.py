"""SQLite storage helpers for ctxsift."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import aiosqlite

from ctxsift.types import ExtractedTermRecord, ReferencedFileRecord, StoredRecord


SCHEMA_VERSION = "2"


@dataclass(frozen=True)
class StorageInitResult:
    """Result of database initialization."""

    db_path: Path
    schema_version: str


@dataclass(frozen=True)
class CacheLookupResult:
    """Stored exact-cache hit details."""

    record_id: int
    compressed_output: str
    model_provider: str | None
    model_name: str | None


SCHEMA_STATEMENTS = (
    """
    CREATE TABLE IF NOT EXISTS schema_info (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        workspace_root TEXT,
        cwd TEXT,
        git_head TEXT,
        git_branch TEXT,
        git_dirty INTEGER,
        mode TEXT NOT NULL,
        command TEXT,
        command_exit_code INTEGER,
        command_duration_ms INTEGER,
        instruction TEXT NOT NULL,
        normalized_instruction TEXT NOT NULL,
        compressed_output TEXT NOT NULL,
        raw_input_hash TEXT NOT NULL,
        exact_cache_key TEXT,
        stdout_hash TEXT,
        stderr_hash TEXT,
        model_provider TEXT,
        model_name TEXT,
        max_output_tokens INTEGER,
        prompt_version TEXT,
        ctxsift_version TEXT
    )
    """,
    """
    CREATE VIRTUAL TABLE IF NOT EXISTS records_fts USING fts5(
        instruction,
        compressed_output,
        command,
        content='records',
        content_rowid='id'
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS referenced_files (
        id INTEGER PRIMARY KEY,
        record_id INTEGER NOT NULL,
        path TEXT NOT NULL,
        abs_path TEXT,
        sha256 TEXT,
        exists_at_capture INTEGER NOT NULL,
        FOREIGN KEY(record_id) REFERENCES records(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS extracted_terms (
        id INTEGER PRIMARY KEY,
        record_id INTEGER NOT NULL,
        term TEXT NOT NULL,
        kind TEXT,
        FOREIGN KEY(record_id) REFERENCES records(id)
    )
    """,
)


async def initialize_database(db_path: Path) -> StorageInitResult:
    """Create the workspace database and schema when needed."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    async with aiosqlite.connect(db_path) as connection:
        await _apply_schema(connection)
        await _store_schema_version(connection)
        await connection.commit()
    return StorageInitResult(
        db_path=db_path,
        schema_version=SCHEMA_VERSION,
    )


async def insert_record_bundle(
    db_path: Path,
    record: StoredRecord,
    referenced_files: list[ReferencedFileRecord] | None = None,
    extracted_terms: list[ExtractedTermRecord] | None = None,
) -> int:
    """Insert one record and all related search rows in one transaction."""
    async with aiosqlite.connect(db_path) as connection:
        record_id = await _insert_record(connection, record)
        await _insert_fts_row(connection, record_id, record)
        await _insert_referenced_files(connection, record_id, referenced_files or [])
        await _insert_extracted_terms(connection, record_id, extracted_terms or [])
        await connection.commit()
    return record_id


async def find_cached_record(
    db_path: Path,
    exact_cache_key: str,
) -> CacheLookupResult | None:
    """Find one previously stored exact-cache hit."""
    async with aiosqlite.connect(db_path) as connection:
        cursor = await connection.execute(
            """
            SELECT id, compressed_output, model_provider, model_name
            FROM records
            WHERE exact_cache_key = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (exact_cache_key,),
        )
        row = await cursor.fetchone()
    if row is None:
        return None
    return CacheLookupResult(
        record_id=int(row[0]),
        compressed_output=str(row[1]),
        model_provider=str(row[2]) if row[2] is not None else None,
        model_name=str(row[3]) if row[3] is not None else None,
    )


async def read_schema_version(db_path: Path) -> str | None:
    """Read the stored schema version."""
    async with aiosqlite.connect(db_path) as connection:
        cursor = await connection.execute(
            "SELECT value FROM schema_info WHERE key = 'schema_version'"
        )
        row = await cursor.fetchone()
    if row is None:
        return None
    return str(row[0])


async def _apply_schema(connection: aiosqlite.Connection) -> None:
    for statement in SCHEMA_STATEMENTS:
        await connection.execute(statement)
    await _ensure_record_columns(connection)
    await _ensure_indexes(connection)


async def _store_schema_version(connection: aiosqlite.Connection) -> None:
    await connection.execute(
        """
        INSERT INTO schema_info (key, value)
        VALUES ('schema_version', ?)
        ON CONFLICT(key) DO UPDATE SET value = excluded.value
        """,
        (SCHEMA_VERSION,),
    )


async def _insert_record(connection: aiosqlite.Connection, record: StoredRecord) -> int:
    cursor = await connection.execute(
        """
        INSERT INTO records (
            workspace_root,
            cwd,
            git_head,
            git_branch,
            git_dirty,
            mode,
            command,
            command_exit_code,
            command_duration_ms,
            instruction,
            normalized_instruction,
            compressed_output,
            raw_input_hash,
            exact_cache_key,
            stdout_hash,
            stderr_hash,
            model_provider,
            model_name,
            max_output_tokens,
            prompt_version,
            ctxsift_version
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            record.workspace_root,
            record.cwd,
            record.git_head,
            record.git_branch,
            _int_or_none(record.git_dirty),
            record.mode,
            record.command,
            record.command_exit_code,
            record.command_duration_ms,
            record.instruction,
            record.normalized_instruction,
            record.compressed_output,
            record.raw_input_hash,
            record.exact_cache_key,
            record.stdout_hash,
            record.stderr_hash,
            record.model_provider,
            record.model_name,
            record.max_output_tokens,
            record.prompt_version,
            record.ctxsift_version,
        ),
    )
    return int(cursor.lastrowid)


async def _insert_fts_row(
    connection: aiosqlite.Connection,
    record_id: int,
    record: StoredRecord,
) -> None:
    await connection.execute(
        """
        INSERT INTO records_fts (rowid, instruction, compressed_output, command)
        VALUES (?, ?, ?, ?)
        """,
        (
            record_id,
            record.instruction,
            record.compressed_output,
            record.command or "",
        ),
    )


async def _insert_referenced_files(
    connection: aiosqlite.Connection,
    record_id: int,
    referenced_files: list[ReferencedFileRecord],
) -> None:
    if not referenced_files:
        return
    await connection.executemany(
        """
        INSERT INTO referenced_files (
            record_id,
            path,
            abs_path,
            sha256,
            exists_at_capture
        ) VALUES (?, ?, ?, ?, ?)
        """,
        [
            (
                record_id,
                item.path,
                item.abs_path,
                item.sha256,
                int(item.exists_at_capture),
            )
            for item in referenced_files
        ],
    )


async def _insert_extracted_terms(
    connection: aiosqlite.Connection,
    record_id: int,
    extracted_terms: list[ExtractedTermRecord],
) -> None:
    if not extracted_terms:
        return
    await connection.executemany(
        """
        INSERT INTO extracted_terms (
            record_id,
            term,
            kind
        ) VALUES (?, ?, ?)
        """,
        [
            (
                record_id,
                item.term,
                item.kind,
            )
            for item in extracted_terms
        ],
    )


def _int_or_none(value: bool | None) -> int | None:
    if value is None:
        return None
    return int(value)


async def _ensure_record_columns(connection: aiosqlite.Connection) -> None:
    existing_columns = await _record_columns(connection)
    if "exact_cache_key" not in existing_columns:
        await connection.execute("ALTER TABLE records ADD COLUMN exact_cache_key TEXT")


async def _record_columns(connection: aiosqlite.Connection) -> set[str]:
    cursor = await connection.execute("PRAGMA table_info(records)")
    rows = await cursor.fetchall()
    return {str(row[1]) for row in rows}


async def _ensure_indexes(connection: aiosqlite.Connection) -> None:
    await connection.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_records_exact_cache_key
        ON records(exact_cache_key)
        """
    )
