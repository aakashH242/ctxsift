"""Factories for configured model backends."""

from __future__ import annotations

from ctxsift.models.base import BackendUnavailableError, ModelBackend
from ctxsift.models.transformers_gemma import TransformersGemmaBackend
from ctxsift.types import LocalModelConfig


def create_local_backend(config: LocalModelConfig) -> ModelBackend:
    """Create one configured local model backend."""
    if config.backend == "transformers":
        return TransformersGemmaBackend(config)
    raise BackendUnavailableError(f"Unsupported local backend '{config.backend}'.")
