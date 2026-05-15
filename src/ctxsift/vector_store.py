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
        mismatch_status = _dimension_mismatch_status(metadata, model_name, dimension, status)
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


async def _load_sqlite_vec(
    connection: aiosqlite.Connection,
    model_name: str,
    dimension: int,
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


def _dimension_mismatch_status(
    metadata: dict[str, str],
    model_name: str,
    dimension: int,
    status: VectorStoreStatus,
) -> VectorStoreStatus | None:
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
