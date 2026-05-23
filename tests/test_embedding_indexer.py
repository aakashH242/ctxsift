"""Tests for recall embedding indexing."""

import asyncio
from pathlib import Path

import ctxsift.embedding_indexer as embedding_indexer
from ctxsift.storage import initialize_database
from ctxsift.types import EmbeddingConfig, StoredRecord
from ctxsift.storage.vector import search_record_embeddings


class FakeEmbeddingBackend:
    """Minimal backend for indexing tests."""

    model_name = "fake/embeddings"

    async def embedding_dimension(self) -> int:
        return 4

    async def embed_documents(self, request) -> list[list[float]]:
        return [[0.1, 0.2, 0.3, 0.4]]


def test_index_record_embedding_writes_to_sqlite_vec(
    tmp_path: Path,
    monkeypatch,
) -> None:
    db_path = tmp_path / ".ctxsift" / "ctxsift.db"
    asyncio.run(initialize_database(db_path))
    monkeypatch.setattr(
        embedding_indexer,
        "create_embedding_backend",
        lambda config: FakeEmbeddingBackend(),
    )

    asyncio.run(
        embedding_indexer.index_record_embedding(
            db_path=db_path,
            record_id=7,
            record=StoredRecord(
                instruction="summarize auth failures",
                normalized_instruction="summarize auth failures",
                compressed_output="AuthError in src/auth.py",
                raw_input_hash="hash",
                mode="pipe",
                workspace_root=str(tmp_path),
                cwd=str(tmp_path),
                command="pytest tests/test_auth.py -q",
            ),
            referenced_files=[],
            extracted_terms=[],
            config=EmbeddingConfig(model="fake/embeddings"),
        )
    )
    status, hits = asyncio.run(
        search_record_embeddings(
            db_path=db_path,
            query_vector=[0.1, 0.2, 0.3, 0.4],
            model_name="fake/embeddings",
            dimension=4,
            limit=3,
        )
    )

    assert status.available is True
    assert hits[0].record_id == 7
