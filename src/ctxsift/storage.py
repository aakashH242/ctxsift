"""SQLite storage helpers for ctxsift."""

from __future__ import annotations

from pathlib import Path
import re

import aiosqlite

from ctxsift.recall_ranking import RankingRequest, rank_records
from ctxsift.types import (
    ExtractedTermRecord,
    CacheLookupResult,
    RecallStorageRecord,
    ReferencedFileRecord,
    StorageInitResult,
    StoredRecord,
)


SCHEMA_VERSION = "3"


SEARCH_TERM_RE = re.compile(r"[\w./:\\-]+")


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
    """
    CREATE TABLE IF NOT EXISTS vector_index_metadata (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
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
        db_path=str(db_path),
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


async def search_records(
    db_path: Path,
    query: str,
    file_filters: list[str] | None = None,
    limit: int = 10,
) -> list[RecallStorageRecord]:
    """Search stored records using FTS5 plus exact related-row matching."""
    normalized_query = query.casefold().strip()
    if not normalized_query:
        return []
    search_terms = _search_terms(query)
    file_filters = [item.casefold().replace("\\", "/") for item in (file_filters or [])]
    async with aiosqlite.connect(db_path) as connection:
        fts_ranks = await _fts_candidate_ranks(connection, search_terms)
        exact_ids = await _exact_candidate_ids(connection, normalized_query, search_terms)
        candidate_ids = set(fts_ranks) | exact_ids
        if not candidate_ids:
            return []
        record_rows = await _record_rows(connection, candidate_ids)
        file_rows = await _referenced_file_rows(connection, candidate_ids)
        term_rows = await _extracted_term_rows(connection, candidate_ids)
    candidates = _candidate_records(
        record_rows=record_rows,
        referenced_file_rows=file_rows,
        extracted_term_rows=term_rows,
    )
    ranked_candidates = rank_records(
        RankingRequest(
            records=candidates,
            fts_ranks=fts_ranks,
            normalized_query=normalized_query,
            search_terms=search_terms,
            file_filters=file_filters,
        )
    )
    return ranked_candidates[:limit]


async def read_recall_records_by_ids(
    db_path: Path,
    record_ids: list[int],
) -> list[RecallStorageRecord]:
    """Load stored recall records for explicit record ids."""
    if not record_ids:
        return []
    candidate_ids = set(record_ids)
    async with aiosqlite.connect(db_path) as connection:
        record_rows = await _record_rows(connection, candidate_ids)
        file_rows = await _referenced_file_rows(connection, candidate_ids)
        term_rows = await _extracted_term_rows(connection, candidate_ids)
    return _candidate_records(
        record_rows=record_rows,
        referenced_file_rows=file_rows,
        extracted_term_rows=term_rows,
    )


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
    record_id = cursor.lastrowid
    if record_id is None:
        raise RuntimeError("SQLite did not return a record id for the inserted row.")
    return int(record_id)


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


async def _fts_candidate_ranks(
    connection: aiosqlite.Connection,
    search_terms: list[str],
) -> dict[int, int]:
    if not search_terms:
        return {}
    cursor = await connection.execute(
        """
        SELECT rowid, bm25(records_fts) AS rank_score
        FROM records_fts
        WHERE records_fts MATCH ?
        ORDER BY rank_score ASC, rowid DESC
        """,
        (_fts_query(search_terms),),
    )
    rows = await cursor.fetchall()
    return {int(row[0]): index for index, row in enumerate(rows, start=1)}


async def _exact_candidate_ids(
    connection: aiosqlite.Connection,
    normalized_query: str,
    search_terms: list[str],
) -> set[int]:
    candidate_ids: set[int] = set()
    text_queries = [normalized_query, *search_terms]
    for text_query in text_queries:
        like_value = f"%{text_query}%"
        cursor = await connection.execute(
            """
            SELECT id
            FROM records
            WHERE lower(instruction) LIKE ?
               OR lower(compressed_output) LIKE ?
               OR lower(coalesce(command, '')) LIKE ?
            """,
            (like_value, like_value, like_value),
        )
        candidate_ids.update(int(row[0]) for row in await cursor.fetchall())
    for search_term in [normalized_query, *search_terms]:
        cursor = await connection.execute(
            """
            SELECT DISTINCT record_id
            FROM referenced_files
            WHERE lower(path) = ?
               OR lower(path) LIKE ?
               OR lower(coalesce(abs_path, '')) LIKE ?
            """,
            (
                search_term,
                f"%/{search_term}",
                f"%{search_term}%",
            ),
        )
        candidate_ids.update(int(row[0]) for row in await cursor.fetchall())
        cursor = await connection.execute(
            """
            SELECT DISTINCT record_id
            FROM extracted_terms
            WHERE lower(term) = ?
            """,
            (search_term,),
        )
        candidate_ids.update(int(row[0]) for row in await cursor.fetchall())
    return candidate_ids


async def _record_rows(connection: aiosqlite.Connection, record_ids: set[int]) -> dict[int, tuple]:
    placeholders = ", ".join("?" for _ in record_ids)
    cursor = await connection.execute(
        f"""
        SELECT id, created_at, workspace_root, instruction, compressed_output, command, command_exit_code
        FROM records
        WHERE id IN ({placeholders})
        """,
        tuple(sorted(record_ids)),
    )
    rows = await cursor.fetchall()
    return {int(row[0]): tuple(row) for row in rows}


async def _referenced_file_rows(
    connection: aiosqlite.Connection,
    record_ids: set[int],
) -> dict[int, list[ReferencedFileRecord]]:
    placeholders = ", ".join("?" for _ in record_ids)
    cursor = await connection.execute(
        f"""
        SELECT record_id, path, abs_path, sha256, exists_at_capture
        FROM referenced_files
        WHERE record_id IN ({placeholders})
        ORDER BY id ASC
        """,
        tuple(sorted(record_ids)),
    )
    rows = await cursor.fetchall()
    grouped: dict[int, list[ReferencedFileRecord]] = {record_id: [] for record_id in record_ids}
    for row in rows:
        grouped[int(row[0])].append(
            ReferencedFileRecord(
                path=str(row[1]),
                abs_path=str(row[2]) if row[2] is not None else None,
                sha256=str(row[3]) if row[3] is not None else None,
                exists_at_capture=bool(row[4]),
            )
        )
    return grouped


async def _extracted_term_rows(
    connection: aiosqlite.Connection,
    record_ids: set[int],
) -> dict[int, list[ExtractedTermRecord]]:
    placeholders = ", ".join("?" for _ in record_ids)
    cursor = await connection.execute(
        f"""
        SELECT record_id, term, kind
        FROM extracted_terms
        WHERE record_id IN ({placeholders})
        ORDER BY id ASC
        """,
        tuple(sorted(record_ids)),
    )
    rows = await cursor.fetchall()
    grouped: dict[int, list[ExtractedTermRecord]] = {record_id: [] for record_id in record_ids}
    for row in rows:
        grouped[int(row[0])].append(
            ExtractedTermRecord(
                term=str(row[1]),
                kind=str(row[2]) if row[2] is not None else None,
            )
        )
    return grouped


def _candidate_records(
    record_rows: dict[int, tuple],
    referenced_file_rows: dict[int, list[ReferencedFileRecord]],
    extracted_term_rows: dict[int, list[ExtractedTermRecord]],
) -> list[RecallStorageRecord]:
    results: list[RecallStorageRecord] = []
    for record_id, row in record_rows.items():
        referenced_files = referenced_file_rows.get(record_id, [])
        extracted_terms = extracted_term_rows.get(record_id, [])
        results.append(
            RecallStorageRecord(
                record_id=record_id,
                created_at=str(row[1]),
                workspace_root=str(row[2]) if row[2] is not None else None,
                instruction=str(row[3]),
                compressed_output=str(row[4]),
                command=str(row[5]) if row[5] is not None else None,
                command_exit_code=int(row[6]) if row[6] is not None else None,
                referenced_files=referenced_files,
                extracted_terms=extracted_terms,
            )
        )
    return results


def _search_terms(query: str) -> list[str]:
    terms = [match.group(0).casefold() for match in SEARCH_TERM_RE.finditer(query)]
    return _dedupe(terms)


def _fts_query(search_terms: list[str]) -> str:
    return " OR ".join(f'"{term.replace("\"", "\"\"")}"' for term in search_terms)


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result
