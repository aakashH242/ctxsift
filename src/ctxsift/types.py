"""Shared typed models for ctxsift."""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class RunMode(str, Enum):
    """Supported top-level execution backends."""

    LOCAL = "local"
    REMOTE = "remote"


class ReasoningMode(str, Enum):
    """Supported remote reasoning controls."""

    AUTO = "auto"
    TRUE = "true"
    FALSE = "false"


class FreshnessStatus(str, Enum):
    """Freshness states for recalled records."""

    FRESH = "fresh"
    STALE_CHANGED = "stale_changed"
    STALE_DELETED = "stale_deleted"
    UNVERIFIABLE = "unverifiable"
    UNKNOWN = "unknown"


class StrictModel(BaseModel):
    """Base model with strict field handling."""

    model_config = ConfigDict(extra="forbid")


class WorkspaceContext(StrictModel):
    """Workspace metadata resolved from the current directory."""

    cwd: str
    workspace_root: str
    is_git_repo: bool
    git_dir: str | None = None
    workspace_config_path: str
    db_path: str | None = None


class CompressionRequest(StrictModel):
    """Compression input carried through the pipeline."""

    instruction: str
    raw_input: str | None = None
    mode: str = "pipe"
    cwd: str | None = None


class CompressionResult(StrictModel):
    """Compressed output produced for storage and display."""

    compressed_output: str
    referenced_files: list[str] = Field(default_factory=list)
    extracted_terms: list[str] = Field(default_factory=list)
    used_cache: bool = False
    model_provider: str | None = None
    model_name: str | None = None


class ExtractedSignal(StrictModel):
    """Deterministic signal extracted before model usage."""

    referenced_files: list[str] = Field(default_factory=list)
    symbols: list[str] = Field(default_factory=list)
    tests: list[str] = Field(default_factory=list)
    packages: list[str] = Field(default_factory=list)
    command_terms: list[str] = Field(default_factory=list)
    exit_code_lines: list[str] = Field(default_factory=list)
    warning_lines: list[str] = Field(default_factory=list)
    error_lines: list[str] = Field(default_factory=list)


class StoredRecord(StrictModel):
    """Stored record shape shared across later storage work."""

    instruction: str
    normalized_instruction: str
    compressed_output: str
    raw_input_hash: str
    mode: str
    id: int | None = None
    created_at: datetime | None = None
    workspace_root: str | None = None
    cwd: str | None = None
    git_head: str | None = None
    git_branch: str | None = None
    git_dirty: bool | None = None
    command: str | None = None
    command_exit_code: int | None = None
    command_duration_ms: int | None = None
    stdout_hash: str | None = None
    stderr_hash: str | None = None
    model_provider: str | None = None
    model_name: str | None = None
    max_output_tokens: int | None = None
    prompt_version: str | None = None
    ctxsift_version: str | None = None


class ReferencedFileRecord(StrictModel):
    """Referenced file metadata captured with one record."""

    path: str
    abs_path: str | None = None
    sha256: str | None = None
    exists_at_capture: bool


class ExtractedTermRecord(StrictModel):
    """One extracted search term captured with one record."""

    term: str
    kind: str | None = None


class RemoteModelConfig(StrictModel):
    """Remote provider configuration."""

    base_url: str = ""
    api_key: str = ""
    api_version: str = ""
    model_name: str = ""
    reasoning_mode: ReasoningMode = ReasoningMode.AUTO


class LocalModelConfig(StrictModel):
    """Local model configuration."""

    backend: str = "transformers"
    model: str = "google/gemma-4-E2B-it"
    device: str = "cpu"
    dtype: str = "auto"


class EmbeddingConfig(StrictModel):
    """Embedding model configuration."""

    model: str = "microsoft/harrier-oss-v1-0.6b"
    device: str = "cpu"
    dtype: str = "auto"
    query_prompt_name: str = "web_search_query"
    document_prompt_name: str = ""
    max_length: int = 32768


class AppConfig(StrictModel):
    """Top-level resolved ctxsift configuration."""

    run_mode: RunMode = RunMode.LOCAL
    timeout_ms: int = 90000
    retries: int = 1
    max_output_tokens: int = 512
    db_path: str | None = None
    remote: RemoteModelConfig = Field(default_factory=RemoteModelConfig)
    local: LocalModelConfig = Field(default_factory=LocalModelConfig)
    embedding: EmbeddingConfig = Field(default_factory=EmbeddingConfig)
