"""Factories for configured model backends."""

from __future__ import annotations

from ctxsift.models.base import BackendUnavailableError, ModelBackend, RemoteBackendOptions
from ctxsift.models.litellm_remote import LiteLLMRemoteBackend
from ctxsift.models.transformers_gemma import TransformersGemmaBackend
from ctxsift.types import AppConfig, LocalModelConfig


def create_local_backend(config: LocalModelConfig) -> ModelBackend:
    """Create one configured local model backend."""
    if config.backend == "transformers":
        return TransformersGemmaBackend(config)
    raise BackendUnavailableError(f"Unsupported local backend '{config.backend}'.")


def create_compression_backend(config: AppConfig) -> ModelBackend:
    """Create the active compression backend for the resolved app config."""
    if config.remote.base_url.strip():
        if not config.remote.model_name.strip():
            raise BackendUnavailableError(
                "Remote LiteLLM backend is enabled by base_url but remote.model_name is empty."
            )
        return LiteLLMRemoteBackend(
            RemoteBackendOptions(
                base_url=config.remote.base_url,
                api_key=config.remote.api_key,
                api_version=config.remote.api_version,
                model_name=config.remote.model_name,
                reasoning_mode=config.remote.reasoning_mode.value,
                timeout_ms=config.timeout_ms,
                retries=config.retries,
            )
        )
    return create_local_backend(config.local)
