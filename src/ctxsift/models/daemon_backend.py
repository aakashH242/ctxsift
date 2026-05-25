"""Daemon-backed local compression backend."""

from __future__ import annotations

import asyncio

from ctxsift.daemon.client import DaemonClientError, request_compress
from ctxsift.daemon.manager import compression_daemon_spec, ensure_daemon, forget_daemon
from ctxsift.daemon.types import CompressRequestPayload
from ctxsift.daemon.registry import tail_log_text
from ctxsift.models.base import BackendUnavailableError, ModelBackend, ModelCompressionInput
from ctxsift.models.local_runtime import local_cache_model_id, local_provider_name
from ctxsift.types import AppConfig


class DaemonCompressionBackend(ModelBackend):
    """Local compression backend that delegates to a background daemon."""

    def __init__(self, config: AppConfig) -> None:
        self._config = config
        self.provider_name = local_provider_name(config.local)
        self.model_name = config.local.model

    @property
    def cache_model_id(self) -> str:
        return local_cache_model_id(self._config.local)

    async def compress(self, request: ModelCompressionInput) -> str:
        payload = CompressRequestPayload(
            intent=request.intent,
            instruction=request.instruction,
            raw_input=request.raw_input,
            extracted_signal=request.extracted_signal,
            max_output_tokens=request.max_output_tokens,
            recovery_enabled=request.recovery_enabled,
        )
        return await self._call_with_restart(payload)

    async def preload(self) -> None:
        await asyncio.to_thread(ensure_daemon, self._current_spec())

    async def shutdown(self) -> None:
        return None

    async def _call_with_restart(self, payload: CompressRequestPayload) -> str:
        spec = self._current_spec()
        try:
            return await self._call_once(spec, payload)
        except (DaemonClientError, RuntimeError):
            forget_daemon(spec)
            try:
                return await self._call_once(spec, payload)
            except (DaemonClientError, RuntimeError) as error:
                log_tail = tail_log_text(self._log_path(spec))
                detail = str(error)
                if log_tail:
                    detail = f"{detail}. Log tail: {log_tail.strip()}"
                raise BackendUnavailableError(detail) from error

    async def _call_once(self, spec, payload: CompressRequestPayload) -> str:
        record = await asyncio.to_thread(ensure_daemon, spec)
        response = await asyncio.to_thread(
            request_compress,
            record,
            payload,
            self._config.timeout_ms,
        )
        return response.compressed_output

    def _current_spec(self):
        return compression_daemon_spec(self._config.local, self._config.daemon)

    def _log_path(self, spec):
        from ctxsift.daemon.registry import log_path

        return log_path(spec.role, spec.signature_hash)
