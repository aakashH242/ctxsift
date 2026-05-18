"""sqlite-vec storage helpers."""

from __future__ import annotations

from pathlib import Path

import aiosqlite

from ctxsift.types import VectorSearchHit, VectorStoreStatus


VECTOR_TABLE_NAME = "record_embeddings"
VECTOR_COLUMN_NAME = "embedding"
METADATA_MODEL_KEY = "vector_model_name"
METADATA_DIMENSION_KEY = "vector_dimension"


async def ensure_vector_store(
    db_path: Path,
    model_name: str,
    dimension: int,
) -> VectorStoreStatus:
    """Ensure sqlite-vec is available and the vector table matches the active model."""
    async with aiosqlite.connect(db_path) as connection:
        status = await _load_sqlite_vec(connection, model_name, dimension)
        if not status.available:
            return status
        metadata = await _vector_metadata(connection)
        mismatch_status = _metadata_mismatch_status(metadata, model_name, dimension, status)
        if mismatch_status is not None:
            return mismatch_status
        await _create_vector_table_if_needed(connection, dimension)
        await _store_vector_metadata(connection, model_name, dimension)
        await connection.commit()
        return status


async def upsert_record_embedding(
    db_path: Path,
    record_id: int,
    vector: list[float],
    model_name: str,
    dimension: int,
) -> VectorStoreStatus:
    """Insert or replace one record embedding."""
    status = await ensure_vector_store(db_path, model_name, dimension)
    if not status.available:
        return status
    payload = _serialized_vector(vector)
    async with aiosqlite.connect(db_path) as connection:
        load_status = await _load_sqlite_vec(connection, model_name, dimension)
        if not load_status.available:
            return load_status
        await connection.execute(
            f"DELETE FROM {VECTOR_TABLE_NAME} WHERE rowid = ?",
            (record_id,),
        )
        await connection.execute(
            f"""
            INSERT INTO {VECTOR_TABLE_NAME} (rowid, {VECTOR_COLUMN_NAME})
            VALUES (?, ?)
            """,
            (record_id, payload),
        )
        await connection.commit()
    return status


async def search_record_embeddings(
    db_path: Path,
    query_vector: list[float],
    model_name: str,
    dimension: int,
    limit: int,
) -> tuple[VectorStoreStatus, list[VectorSearchHit]]:
    """Search the sqlite-vec index for nearest records."""
    status = await ensure_vector_store(db_path, model_name, dimension)
    if not status.available:
        return status, []
    payload = _serialized_vector(query_vector)
    async with aiosqlite.connect(db_path) as connection:
        load_status = await _load_sqlite_vec(connection, model_name, dimension)
        if not load_status.available:
            return load_status, []
        cursor = await connection.execute(
            f"""
            SELECT rowid, distance
            FROM {VECTOR_TABLE_NAME}
            WHERE {VECTOR_COLUMN_NAME} MATCH ?
            ORDER BY distance ASC
            LIMIT ?
            """,
            (payload, limit),
        )
        rows = await cursor.fetchall()
    return status, [
        VectorSearchHit(record_id=int(row[0]), distance=float(row[1]))
        for row in rows
    ]


async def vector_store_status(
    db_path: Path,
    model_name: str,
    dimension: int,
) -> VectorStoreStatus:
    """Report vector-store availability without changing stored vectors."""
    return await ensure_vector_store(db_path, model_name, dimension)


async def probe_vector_store(db_path: Path) -> VectorStoreStatus:
    """Probe sqlite-vec availability and stored metadata without loading models."""
    async with aiosqlite.connect(db_path) as connection:
        status = await _load_sqlite_vec(connection, "", None)
        if not status.available:
            return status
        metadata = await _vector_metadata(connection)
    return VectorStoreStatus(
        available=True,
        model_name=metadata.get(METADATA_MODEL_KEY),
        dimension=_metadata_dimension(metadata),
        sqlite_vec_version=status.sqlite_vec_version,
    )


async def delete_record_embeddings(
    db_path: Path,
    record_ids: list[int],
) -> VectorStoreStatus:
    """Delete stored sqlite-vec rows for the given record ids when available."""
    if not record_ids:
        return VectorStoreStatus(available=True)
    async with aiosqlite.connect(db_path) as connection:
        status = await _load_sqlite_vec(connection, "", None)
        if not status.available:
            return status
        if not await _vector_table_exists(connection):
            return status
        await connection.executemany(
            f"DELETE FROM {VECTOR_TABLE_NAME} WHERE rowid = ?",
            [(record_id,) for record_id in record_ids],
        )
        await connection.commit()
        return status


async def _load_sqlite_vec(
    connection: aiosqlite.Connection,
    model_name: str,
    dimension: int | None,
) -> VectorStoreStatus:
    try:
        import sqlite_vec
    except ImportError:
        return VectorStoreStatus(
            available=False,
            warning="sqlite-vec is not installed; recall will fall back to FTS5 only.",
            model_name=model_name,
            dimension=dimension,
        )
    try:
        await connection.enable_load_extension(True)
        await connection.load_extension(sqlite_vec.loadable_path())
        await connection.enable_load_extension(False)
        cursor = await connection.execute("SELECT vec_version()")
        row = await cursor.fetchone()
    except Exception as error:
        return VectorStoreStatus(
            available=False,
            warning=f"sqlite-vec could not be loaded; recall will fall back to FTS5 only. {error}",
            model_name=model_name,
            dimension=dimension,
        )
    return VectorStoreStatus(
        available=True,
        model_name=model_name,
        dimension=dimension,
        sqlite_vec_version=str(row[0]) if row is not None else None,
    )


async def _create_vector_table_if_needed(
    connection: aiosqlite.Connection,
    dimension: int,
) -> None:
    await connection.execute(
        f"""
        CREATE VIRTUAL TABLE IF NOT EXISTS {VECTOR_TABLE_NAME}
        USING vec0({VECTOR_COLUMN_NAME} float[{dimension}])
        """
    )


async def _vector_table_exists(connection: aiosqlite.Connection) -> bool:
    cursor = await connection.execute(
        """
        SELECT 1
        FROM sqlite_master
        WHERE type = 'table' AND name = ?
        """,
        (VECTOR_TABLE_NAME,),
    )
    row = await cursor.fetchone()
    return row is not None


async def _vector_metadata(connection: aiosqlite.Connection) -> dict[str, str]:
    cursor = await connection.execute(
        """
        SELECT key, value
        FROM vector_index_metadata
        WHERE key IN (?, ?)
        """,
        (METADATA_MODEL_KEY, METADATA_DIMENSION_KEY),
    )
    rows = await cursor.fetchall()
    return {str(row[0]): str(row[1]) for row in rows}


def _metadata_mismatch_status(
    metadata: dict[str, str],
    model_name: str,
    dimension: int,
    status: VectorStoreStatus,
) -> VectorStoreStatus | None:
    existing_model_name = metadata.get(METADATA_MODEL_KEY)
    if existing_model_name and existing_model_name != model_name:
        return VectorStoreStatus(
            available=False,
            warning=(
                "sqlite-vec index model mismatch; recall will fall back to FTS5 only. "
                f"DB model={existing_model_name}, configured model={model_name}."
            ),
            model_name=model_name,
            dimension=dimension,
            sqlite_vec_version=status.sqlite_vec_version,
        )
    existing_dimension = metadata.get(METADATA_DIMENSION_KEY)
    if existing_dimension is None:
        return None
    if int(existing_dimension) == dimension:
        return None
    return VectorStoreStatus(
        available=False,
        warning=(
            "sqlite-vec index dimension mismatch; recall will fall back to FTS5 only. "
            f"DB dimension={existing_dimension}, configured dimension={dimension}."
        ),
        model_name=model_name,
        dimension=dimension,
        sqlite_vec_version=status.sqlite_vec_version,
    )


def _metadata_dimension(metadata: dict[str, str]) -> int | None:
    raw_value = metadata.get(METADATA_DIMENSION_KEY)
    if raw_value is None:
        return None
    return int(raw_value)


async def _store_vector_metadata(
    connection: aiosqlite.Connection,
    model_name: str,
    dimension: int,
) -> None:
    await connection.executemany(
        """
        INSERT INTO vector_index_metadata (key, value)
        VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value = excluded.value
        """,
        [
            (METADATA_MODEL_KEY, model_name),
            (METADATA_DIMENSION_KEY, str(dimension)),
        ],
    )


def _serialized_vector(vector: list[float]) -> bytes:
    import sqlite_vec

    return sqlite_vec.serialize_float32(vector)
