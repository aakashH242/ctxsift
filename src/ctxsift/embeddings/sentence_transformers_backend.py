"""Sentence Transformers embedding backend."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any

import numpy as np
import torch

from ctxsift.embeddings.base import (
    DEFAULT_RECALL_QUERY_PROMPT,
    DocumentEmbeddingRequest,
    EmbeddingBackend,
    EmbeddingBackendUnavailableError,
    QueryEmbeddingRequest,
)
from ctxsift.types import EmbeddingConfig


class SentenceTransformersBackend(EmbeddingBackend):
    """Lazy Sentence Transformers backend with Harrier-aware query prompting."""

    provider_name = "sentence_transformers"

    def __init__(self, config: EmbeddingConfig) -> None:
        self.config = config
        self.model_name = config.model
        self._model = None
        self._lock = asyncio.Lock()
        self._dimension: int | None = None

    async def embedding_dimension(self) -> int:
        model = await self._load_model()
        dimension = _model_embedding_dimension(model)
        if dimension is None:
            if self._dimension is None:
                probe = await self.embed_documents(
                    DocumentEmbeddingRequest(
                        texts=["ctxsift dimension probe"],
                        max_length=self.config.max_length,
                    )
                )
                self._dimension = len(probe[0])
            return self._dimension
        self._dimension = int(dimension)
        return self._dimension

    async def embed_query(self, request: QueryEmbeddingRequest) -> list[float]:
        model = await self._load_model()
        return await asyncio.to_thread(self._encode_query_sync, model, request)

    async def embed_documents(self, request: DocumentEmbeddingRequest) -> list[list[float]]:
        model = await self._load_model()
        return await asyncio.to_thread(self._encode_documents_sync, model, request)

    async def _load_model(self):
        if self._model is not None:
            return self._model
        async with self._lock:
            if self._model is not None:
                return self._model
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError as error:
                raise EmbeddingBackendUnavailableError(
                    "sentence-transformers is not installed."
                ) from error
            try:
                model = await asyncio.to_thread(
                    SentenceTransformer,
                    self.model_name,
                    device=self._resolved_device(),
                    local_files_only=True,
                    model_kwargs=self._model_kwargs(),
                )
            except Exception as error:  # pragma: no cover - backend-specific failures
                raise EmbeddingBackendUnavailableError(
                    f"Could not load embedding model '{self.model_name}': {error}"
                ) from error
            model.max_seq_length = self.config.max_length
            self._model = model
            return self._model

    def _encode_query_sync(self, model, request: QueryEmbeddingRequest) -> list[float]:
        kwargs = self._common_encode_kwargs()
        kwargs.update(self._query_prompt_kwargs(model))
        encoder = self._query_encoder(model, kwargs)
        embedding = encoder(request.text, **kwargs)
        return _embedding_to_list(embedding)

    def _encode_documents_sync(self, model, request: DocumentEmbeddingRequest) -> list[list[float]]:
        kwargs = self._common_encode_kwargs()
        kwargs.update(self._document_prompt_kwargs(model))
        encoder = self._document_encoder(model, kwargs)
        embeddings = encoder(request.texts, **kwargs)
        return _embeddings_to_lists(embeddings)

    def _query_encoder(self, model, kwargs: dict[str, Any]) -> Callable[..., Any]:
        if hasattr(model, "encode_query"):
            return model.encode_query
        kwargs.pop("prompt_name", None)
        kwargs.pop("prompt", None)
        return model.encode

    def _document_encoder(self, model, kwargs: dict[str, Any]) -> Callable[..., Any]:
        if hasattr(model, "encode_document"):
            return model.encode_document
        kwargs.pop("prompt_name", None)
        kwargs.pop("prompt", None)
        return model.encode

    def _common_encode_kwargs(self) -> dict[str, Any]:
        return {
            "batch_size": 1,
            "convert_to_numpy": True,
            "device": self._resolved_device(),
            "normalize_embeddings": True,
            "show_progress_bar": False,
            "truncate_dim": None,
        }

    def _query_prompt_kwargs(self, model) -> dict[str, Any]:
        if self.config.query_prompt_name:
            return {"prompt_name": self.config.query_prompt_name}
        if self.config.query_prompt:
            return {"prompt": self.config.query_prompt}
        if self._is_harrier_model() and hasattr(model, "encode_query"):
            return {"prompt": DEFAULT_RECALL_QUERY_PROMPT}
        return {}

    def _document_prompt_kwargs(self, model) -> dict[str, Any]:
        if self.config.document_prompt_name and hasattr(model, "encode_document"):
            return {"prompt_name": self.config.document_prompt_name}
        return {}

    def _is_harrier_model(self) -> bool:
        return self.model_name.casefold().startswith("microsoft/harrier-oss")

    def _model_kwargs(self) -> dict[str, Any]:
        dtype = self.config.dtype
        supported = {"auto", "float32", "float16", "bfloat16"}
        if dtype not in supported:
            raise EmbeddingBackendUnavailableError(f"Unsupported embedding dtype '{dtype}'.")
        return {"dtype": dtype}

    def _resolved_device(self) -> str:
        configured = self.config.device.casefold()
        if configured == "cpu":
            return "cpu"
        if configured.startswith("cuda") and torch.cuda.is_available():
            return self.config.device
        if configured == "auto" and torch.cuda.is_available():
            return "cuda"
        return "cpu"


def _embedding_to_list(embedding: Any) -> list[float]:
    if isinstance(embedding, np.ndarray):
        return embedding.astype(np.float32).tolist()
    return np.asarray(embedding, dtype=np.float32).tolist()


def _embeddings_to_lists(embeddings: Any) -> list[list[float]]:
    if isinstance(embeddings, np.ndarray):
        array = embeddings.astype(np.float32)
    else:
        array = np.asarray(embeddings, dtype=np.float32)
    if array.ndim == 1:
        return [array.tolist()]
    return array.tolist()


def _model_embedding_dimension(model) -> int | None:
    if hasattr(model, "get_embedding_dimension"):
        return model.get_embedding_dimension()
    return model.get_sentence_embedding_dimension()
