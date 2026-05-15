"""Shared pytest fixtures."""

import pytest

import ctxsift.compression as compression
import ctxsift.recall as recall


@pytest.fixture(autouse=True)
def disable_embedding_index_side_effects(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep unrelated tests from attempting real embedding indexing work."""

    async def no_op_index_record_embedding(**kwargs) -> None:
        return None

    monkeypatch.setattr(compression, "index_record_embedding", no_op_index_record_embedding)

    async def no_op_vector_hits(*args, **kwargs):
        return []

    monkeypatch.setattr(recall, "_vector_hits", no_op_vector_hits)
