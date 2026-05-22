"""Loopback HTTP client helpers for ctxsift daemons."""

from __future__ import annotations

import json
from urllib import error as urllib_error
from urllib import request as urllib_request

from ctxsift.daemon.types import (
    CompressRequestPayload,
    CompressResponsePayload,
    DaemonRegistryRecord,
    EmbedDocumentsRequestPayload,
    EmbedDocumentsResponsePayload,
    EmbedQueryRequestPayload,
    EmbedQueryResponsePayload,
    HealthResponse,
    JsonErrorPayload,
)

AUTH_HEADER = "X-Ctxsift-Token"


class DaemonClientError(RuntimeError):
    """Raised when a daemon request cannot be completed."""


def read_health(record: DaemonRegistryRecord, timeout_ms: int = 1500) -> HealthResponse:
    """Read one daemon health payload."""
    payload = _request_json(
        record=record,
        path="/health",
        timeout_ms=timeout_ms,
    )
    return HealthResponse.model_validate(payload)


def request_compress(
    record: DaemonRegistryRecord,
    request: CompressRequestPayload,
    timeout_ms: int,
) -> CompressResponsePayload:
    """Request one compressed output from a compression daemon."""
    payload = _request_json(
        record=record,
        path="/compress",
        method="POST",
        body=request.model_dump(mode="json"),
        timeout_ms=timeout_ms,
    )
    return CompressResponsePayload.model_validate(payload)


def request_embed_query(
    record: DaemonRegistryRecord,
    request: EmbedQueryRequestPayload,
    timeout_ms: int,
) -> EmbedQueryResponsePayload:
    """Request one query embedding from an embedding daemon."""
    payload = _request_json(
        record=record,
        path="/embed_query",
        method="POST",
        body=request.model_dump(mode="json"),
        timeout_ms=timeout_ms,
    )
    return EmbedQueryResponsePayload.model_validate(payload)


def request_embed_documents(
    record: DaemonRegistryRecord,
    request: EmbedDocumentsRequestPayload,
    timeout_ms: int,
) -> EmbedDocumentsResponsePayload:
    """Request one document embedding batch from an embedding daemon."""
    payload = _request_json(
        record=record,
        path="/embed_documents",
        method="POST",
        body=request.model_dump(mode="json"),
        timeout_ms=timeout_ms,
    )
    return EmbedDocumentsResponsePayload.model_validate(payload)


def request_stop(record: DaemonRegistryRecord, timeout_ms: int = 2000) -> None:
    """Request one graceful daemon shutdown."""
    _request_json(
        record=record,
        path="/stop",
        method="POST",
        body={},
        timeout_ms=timeout_ms,
    )


def _request_json(
    record: DaemonRegistryRecord,
    path: str,
    timeout_ms: int,
    method: str = "GET",
    body: dict | None = None,
) -> dict:
    timeout_seconds = max(timeout_ms, 1) / 1000
    data = None
    headers = {
        AUTH_HEADER: record.auth_token,
        "Accept": "application/json",
    }
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib_request.Request(
        url=f"http://127.0.0.1:{record.port}{path}",
        data=data,
        headers=headers,
        method=method,
    )
    try:
        with urllib_request.urlopen(request, timeout=timeout_seconds) as response:
            raw_body = response.read().decode("utf-8")
    except urllib_error.HTTPError as error:
        detail = _http_error_detail(error)
        raise DaemonClientError(detail) from error
    except urllib_error.URLError as error:
        raise DaemonClientError(str(error.reason)) from error
    except TimeoutError as error:
        raise DaemonClientError("timed out") from error
    try:
        payload = json.loads(raw_body) if raw_body else {}
    except json.JSONDecodeError as error:
        raise DaemonClientError("Daemon returned invalid JSON.") from error
    if not isinstance(payload, dict):
        raise DaemonClientError("Daemon returned a non-object JSON payload.")
    return payload


def _http_error_detail(error: urllib_error.HTTPError) -> str:
    try:
        body = error.read().decode("utf-8")
    except Exception:
        body = ""
    if body:
        try:
            payload = JsonErrorPayload.model_validate_json(body)
        except Exception:
            return f"HTTP {error.code}: {body}"
        return f"HTTP {error.code}: {payload.error} {payload.detail}".strip()
    return f"HTTP {error.code}: {error.reason}"
