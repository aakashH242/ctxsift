"""Embedding backend package."""

from __future__ import annotations

from typing import Any


def create_embedding_backend(*args: Any, **kwargs: Any):
    """Create one configured embedding backend."""
    from ctxsift.embeddings.factory import create_embedding_backend as _create_embedding_backend

    return _create_embedding_backend(*args, **kwargs)


def create_in_process_embedding_backend(*args: Any, **kwargs: Any):
    """Create one configured in-process embedding backend."""
    from ctxsift.embeddings.factory import (
        create_in_process_embedding_backend as _create_in_process_embedding_backend,
    )

    return _create_in_process_embedding_backend(*args, **kwargs)


__all__ = ["create_embedding_backend", "create_in_process_embedding_backend"]
