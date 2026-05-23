"""Shared pytest fixtures."""

from pathlib import Path

import pytest

from ctxsift.config import store as config_store
import ctxsift.compression.pipeline as compression
import ctxsift.recall.orchestrator as recall_orchestrator


@pytest.fixture(autouse=True)
def disable_embedding_index_side_effects(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep unrelated tests from attempting real embedding indexing work."""

    async def no_op_index_record_embedding(**kwargs) -> None:
        return None

    monkeypatch.setattr(compression, "index_record_embedding", no_op_index_record_embedding)

    async def no_op_vector_hits(*args, **kwargs):
        return []

    monkeypatch.setattr(recall_orchestrator, "_vector_hits", no_op_vector_hits)


@pytest.fixture(autouse=True)
def isolate_ctxsift_config(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Keep tests independent from developer-machine config and env overrides."""

    platform_path = tmp_path / "platform-config" / "config.toml"
    monkeypatch.setattr(config_store, "platform_global_config_path", lambda: platform_path)

    for env_name in config_store.ENVIRONMENT_KEY_MAP:
        monkeypatch.delenv(env_name, raising=False)
