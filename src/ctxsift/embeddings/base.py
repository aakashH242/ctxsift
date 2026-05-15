"""Embedding backend contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


DEFAULT_RECALL_QUERY_PROMPT = (
    "Instruct: Given a coding issue, command output, or debugging question, "
    "retrieve prior command outputs, errors, files, and fixes that are most useful "
    "for resolving the current problem.\n"
    "Query: "
)


class EmbeddingBackendUnavailableError(RuntimeError):
    """Raised when a configured embedding backend cannot be used."""


@dataclass(frozen=True)
class QueryEmbeddingRequest:
    """One query embedding request."""

    text: str
    max_length: int


@dataclass(frozen=True)
class DocumentEmbeddingRequest:
    """One document embedding request."""

    texts: list[str]
    max_length: int


class EmbeddingBackend(ABC):
    """Async embedding backend interface."""

    provider_name: str
    model_name: str

    @abstractmethod
    async def embedding_dimension(self) -> int:
        """Return the sentence-embedding dimension for the active model."""

    @abstractmethod
    async def embed_query(self, request: QueryEmbeddingRequest) -> list[float]:
        """Encode one retrieval query."""

    @abstractmethod
    async def embed_documents(self, request: DocumentEmbeddingRequest) -> list[list[float]]:
        """Encode one or more retrieval documents."""
