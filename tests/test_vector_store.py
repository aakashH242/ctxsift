"""Tests for sqlite-vec storage helpers."""

import asyncio
from pathlib import Path

from ctxsift.storage import initialize_database
from ctxsift.vector_store import ensure_vector_store, search_record_embeddings, upsert_record_embedding


def test_vector_store_accepts_embeddings_and_searches(tmp_path: Path) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"
    asyncio.run(initialize_database(db_path))

    status = asyncio.run(ensure_vector_store(db_path, "model-a", 4))
    upsert_status = asyncio.run(
        upsert_record_embedding(db_path, 1, [0.1, 0.2, 0.3, 0.4], "model-a", 4)
    )
    search_status, hits = asyncio.run(
        search_record_embeddings(db_path, [0.1, 0.2, 0.3, 0.4], "model-a", 4, 3)
    )

    assert status.available is True
    assert upsert_status.available is True
    assert search_status.available is True
    assert hits[0].record_id == 1
    assert hits[0].distance == 0.0


def test_vector_store_dimension_mismatch_falls_back(tmp_path: Path) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"
    asyncio.run(initialize_database(db_path))
    asyncio.run(ensure_vector_store(db_path, "model-a", 4))

    mismatch = asyncio.run(ensure_vector_store(db_path, "model-b", 8))

    assert mismatch.available is False
    assert mismatch.warning is not None
    assert "dimension mismatch" in mismatch.warning
