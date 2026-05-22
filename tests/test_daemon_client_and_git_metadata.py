"""Tests for daemon HTTP helpers and git metadata capture."""

from __future__ import annotations

import asyncio
from email.message import Message
import io
from pathlib import Path
from typing import cast
from urllib import error as urllib_error

import pytest

import ctxsift.daemon.client as daemon_client
import ctxsift.git_metadata as git_metadata
from ctxsift.compression.intent import CompressionIntent
from ctxsift.daemon.types import (
    CompressRequestPayload,
    DaemonRegistryRecord,
    DaemonRole,
    EmbedDocumentsRequestPayload,
    EmbedQueryRequestPayload,
)
from ctxsift.embeddings.base import DocumentEmbeddingRequest, QueryEmbeddingRequest
from ctxsift.types import ExtractedSignal, WorkspaceContext


@pytest.fixture
def registry_record() -> DaemonRegistryRecord:
    return DaemonRegistryRecord(
        role=DaemonRole.COMPRESSION,
        signature_hash="sig",
        model="demo/model",
        device="cpu",
        pid=123,
        port=4040,
        auth_token="secret",
    )


class FakeHttpResponse:
    """Small context-manager response stub."""

    def __init__(self, body: str) -> None:
        self._body = body

    def __enter__(self) -> "FakeHttpResponse":
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        del exc_type, exc, traceback
        return None

    def read(self) -> bytes:
        return self._body.encode("utf-8")


class FakeAsyncProcess:
    """Async subprocess stub."""

    def __init__(self, returncode: int, stdout: bytes = b"") -> None:
        self.returncode = returncode
        self._stdout = stdout

    async def communicate(self) -> tuple[bytes, bytes]:
        return self._stdout, b""


def test_read_health_validates_health_payload(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    monkeypatch.setattr(
        daemon_client,
        "_request_json",
        lambda **kwargs: {
            "role": "compression",
            "signature_hash": kwargs["record"].signature_hash,
            "pid": 123,
            "model": kwargs["record"].model,
            "device": kwargs["record"].device,
            "queue_depth": 2,
        },
    )

    response = daemon_client.read_health(registry_record)

    assert response.queue_depth == 2


def test_request_compress_validates_response_payload(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    request = CompressRequestPayload(
        intent=CompressionIntent.SUMMARY,
        instruction="Summarize",
        raw_input="boom",
        extracted_signal=ExtractedSignal(error_lines=["boom"]),
        max_output_tokens=64,
    )
    monkeypatch.setattr(
        daemon_client,
        "_request_json",
        lambda **kwargs: {"compressed_output": f"ok:{kwargs['body']['instruction']}"},
    )

    response = daemon_client.request_compress(registry_record, request, timeout_ms=900)

    assert response.compressed_output == "ok:Summarize"


def test_request_embed_query_validates_response_payload(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    request = EmbedQueryRequestPayload(
        request=QueryEmbeddingRequest(text="find auth", max_length=128)
    )
    monkeypatch.setattr(
        daemon_client,
        "_request_json",
        lambda **kwargs: {"vector": [0.1, 0.2], "model_name": "embed", "dimension": 2},
    )

    response = daemon_client.request_embed_query(registry_record, request, timeout_ms=900)

    assert response.vector == [0.1, 0.2]


def test_request_embed_documents_validates_response_payload(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    request = EmbedDocumentsRequestPayload(
        request=DocumentEmbeddingRequest(texts=["a", "b"], max_length=128)
    )
    monkeypatch.setattr(
        daemon_client,
        "_request_json",
        lambda **kwargs: {"vectors": [[0.1], [0.2]], "model_name": "embed", "dimension": 1},
    )

    response = daemon_client.request_embed_documents(registry_record, request, timeout_ms=900)

    assert response.vectors == [[0.1], [0.2]]


def test_request_stop_posts_empty_body(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    captured: dict[str, object] = {}

    def fake_request_json(**kwargs):
        captured.update(kwargs)
        return {}

    monkeypatch.setattr(daemon_client, "_request_json", fake_request_json)

    daemon_client.request_stop(registry_record, timeout_ms=2000)

    assert captured["body"] == {}


def test_request_json_sends_headers_and_decodes_response(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    captured: dict[str, object] = {}

    def fake_urlopen(request, timeout: float):
        captured["url"] = request.full_url
        captured["method"] = request.get_method()
        captured["data"] = request.data
        captured["headers"] = dict(request.header_items())
        captured["timeout"] = timeout
        return FakeHttpResponse('{"ok": true}')

    monkeypatch.setattr(daemon_client.urllib_request, "urlopen", fake_urlopen)

    payload = daemon_client._request_json(
        record=registry_record,
        path="/health",
        timeout_ms=1500,
        method="POST",
        body={"hello": "world"},
    )

    assert payload == {"ok": True}
    assert captured["url"] == "http://127.0.0.1:4040/health"
    assert captured["method"] == "POST"
    assert captured["timeout"] == 1.5
    data = cast(bytes, captured["data"])
    headers = cast(dict[str, str], captured["headers"])

    assert b'"hello": "world"' in data
    assert headers["X-ctxsift-token"] == "secret"


def test_request_json_raises_daemon_client_error_for_http_error(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    http_error = urllib_error.HTTPError(
        url="http://127.0.0.1:4040/health",
        code=500,
        msg="boom",
        hdrs=Message(),
        fp=io.BytesIO(b'{"error": "internal", "detail": "trace"}'),
    )
    monkeypatch.setattr(
        daemon_client.urllib_request,
        "urlopen",
        lambda request, timeout: (_ for _ in ()).throw(http_error),
    )

    with pytest.raises(daemon_client.DaemonClientError, match="HTTP 500: internal trace"):
        daemon_client._request_json(registry_record, "/health", timeout_ms=10)


def test_request_json_raises_daemon_client_error_for_url_error(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    url_error = urllib_error.URLError("refused")
    monkeypatch.setattr(
        daemon_client.urllib_request,
        "urlopen",
        lambda request, timeout: (_ for _ in ()).throw(url_error),
    )

    with pytest.raises(daemon_client.DaemonClientError, match="refused"):
        daemon_client._request_json(registry_record, "/health", timeout_ms=10)


def test_request_json_raises_daemon_client_error_for_timeout(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    monkeypatch.setattr(
        daemon_client.urllib_request,
        "urlopen",
        lambda request, timeout: (_ for _ in ()).throw(TimeoutError()),
    )

    with pytest.raises(daemon_client.DaemonClientError, match="timed out"):
        daemon_client._request_json(registry_record, "/health", timeout_ms=10)


def test_request_json_rejects_invalid_json(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    monkeypatch.setattr(
        daemon_client.urllib_request,
        "urlopen",
        lambda request, timeout: FakeHttpResponse("not-json"),
    )

    with pytest.raises(daemon_client.DaemonClientError, match="invalid JSON"):
        daemon_client._request_json(registry_record, "/health", timeout_ms=10)


def test_request_json_rejects_non_object_payload(
    monkeypatch: pytest.MonkeyPatch,
    registry_record: DaemonRegistryRecord,
) -> None:
    monkeypatch.setattr(
        daemon_client.urllib_request,
        "urlopen",
        lambda request, timeout: FakeHttpResponse("[1, 2, 3]"),
    )

    with pytest.raises(daemon_client.DaemonClientError, match="non-object JSON payload"):
        daemon_client._request_json(registry_record, "/health", timeout_ms=10)


def test_http_error_detail_falls_back_to_plain_body() -> None:
    error = urllib_error.HTTPError(
        url="http://127.0.0.1:4040/health",
        code=502,
        msg="bad gateway",
        hdrs=Message(),
        fp=io.BytesIO(b"plain failure"),
    )

    detail = daemon_client._http_error_detail(error)

    assert detail == "HTTP 502: plain failure"


def test_http_error_detail_falls_back_to_reason_when_body_is_empty() -> None:
    error = urllib_error.HTTPError(
        url="http://127.0.0.1:4040/health",
        code=404,
        msg="missing",
        hdrs=Message(),
        fp=io.BytesIO(b""),
    )

    detail = daemon_client._http_error_detail(error)

    assert detail == "HTTP 404: missing"


def test_capture_git_metadata_returns_empty_for_non_git_workspace() -> None:
    workspace = WorkspaceContext(
        cwd="D:/repo",
        workspace_root="D:/repo",
        is_git_repo=False,
        workspace_config_path="D:/repo/.ctxsift/config.toml",
        db_path="D:/repo/.ctxsift/ctxsift.db",
    )

    metadata = asyncio.run(git_metadata.capture_git_metadata(workspace))

    assert metadata == git_metadata.GitMetadata()


def test_capture_git_metadata_collects_head_branch_and_dirty(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    workspace = WorkspaceContext(
        cwd="D:/repo",
        workspace_root="D:/repo",
        is_git_repo=True,
        git_dir="D:/repo/.git",
        workspace_config_path="D:/repo/.git/ctxsift/config.toml",
        db_path="D:/repo/.git/ctxsift/ctxsift.db",
    )

    async def fake_git_output(repo_path: Path, *args: str) -> str | None:
        del repo_path
        outputs: dict[tuple[str, ...], str] = {
            ("rev-parse", "HEAD"): "abc123",
            ("branch", "--show-current"): "main",
            ("status", "--porcelain"): " M src/app.py",
        }
        return outputs[args]

    monkeypatch.setattr(git_metadata, "_git_output", fake_git_output)

    metadata = asyncio.run(git_metadata.capture_git_metadata(workspace))

    assert metadata == git_metadata.GitMetadata(
        git_head="abc123",
        git_branch="main",
        git_dirty=True,
    )


def test_git_output_returns_none_when_git_is_missing(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    async def fake_create_subprocess_exec(*args, **kwargs):
        del args, kwargs
        raise FileNotFoundError

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_create_subprocess_exec)

    result = asyncio.run(git_metadata._git_output(tmp_path, "status", "--porcelain"))

    assert result is None


def test_git_output_returns_none_on_non_zero_exit(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    async def fake_create_subprocess_exec(*args, **kwargs):
        del args, kwargs
        return FakeAsyncProcess(returncode=1, stdout=b"ignored")

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_create_subprocess_exec)

    result = asyncio.run(git_metadata._git_output(tmp_path, "status", "--porcelain"))

    assert result is None


def test_git_output_returns_trimmed_stdout(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    async def fake_create_subprocess_exec(*args, **kwargs):
        del args, kwargs
        return FakeAsyncProcess(returncode=0, stdout=b"main\n")

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_create_subprocess_exec)

    result = asyncio.run(git_metadata._git_output(tmp_path, "branch", "--show-current"))

    assert result == "main"
