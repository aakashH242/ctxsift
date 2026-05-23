"""Factories for configured model backends."""

from __future__ import annotations

from ctxsift.models.base import BackendUnavailableError, ModelBackend, RemoteBackendOptions
from ctxsift.models.daemon_backend import DaemonCompressionBackend
from ctxsift.models.llama_cpp_backend import LlamaCppBackend
from ctxsift.models.litellm_remote import LiteLLMRemoteBackend
from ctxsift.models.local_runtime import resolve_local_runtime
from ctxsift.models.transformers_gemma import TransformersTextBackend
from ctxsift.types import AppConfig, LocalModelConfig


def create_local_backend(config: LocalModelConfig) -> ModelBackend:
    """Create one configured local model backend."""
    runtime = resolve_local_runtime(config)
    if runtime.uses_llama_cpp:
        return LlamaCppBackend(config)
    if runtime.uses_transformers:
        return TransformersTextBackend(config)
    raise BackendUnavailableError("Could not resolve a supported local runtime.")


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
    if config.daemon.enabled:
        return DaemonCompressionBackend(config)
    return create_local_backend(config.local)
