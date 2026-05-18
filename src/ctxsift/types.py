"""Shared typed models for ctxsift."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, model_validator


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


class LocalQuantizationMode(str, Enum):
    """Supported Transformers quantization modes for local compression."""

    NONE = "none"
    BNB_8BIT = "bnb-8bit"
    BNB_4BIT_FP4 = "bnb-4bit-fp4"
    BNB_4BIT_NF4 = "bnb-4bit-nf4"


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


class StorageInitResult(StrictModel):
    """Result of database initialization."""

    db_path: Path
    schema_version: str


class CacheLookupResult(StrictModel):
    """Stored exact-cache hit details."""

    record_id: int
    compressed_output: str
    model_provider: str | None = None
    model_name: str | None = None


class CompressionRequest(StrictModel):
    """Compression input carried through the pipeline."""

    instruction: str
    raw_input: str = ""
    mode: str = "pipe"
    cwd: str | None = None
    max_output_tokens: int | None = None
    command: str | None = None
    command_args: list[str] = Field(default_factory=list)
    command_exit_code: int | None = None
    command_duration_ms: int | None = None
    stdout_hash: str | None = None
    stderr_hash: str | None = None
    git_head: str | None = None
    git_branch: str | None = None
    git_dirty: bool | None = None


class CompressionResult(StrictModel):
    """Compressed output produced for storage and display."""

    compressed_output: str
    referenced_files: list[str] = Field(default_factory=list)
    extracted_terms: list[str] = Field(default_factory=list)
    used_cache: bool = False
    model_provider: str | None = None
    model_name: str | None = None
    record_id: int | None = None


class RecallRecord(StrictModel):
    """Recall result displayed to the user."""

    record_id: int
    created_at: str
    freshness_status: FreshnessStatus
    instruction: str
    compressed_output: str
    command: str | None = None
    command_exit_code: int | None = None
    referenced_files: list[str] = Field(default_factory=list)
    matched_fields: list[str] = Field(default_factory=list)
    score: int = 0


class RecallStorageRecord(StrictModel):
    """Stored record plus related rows used by recall."""

    record_id: int
    created_at: str
    workspace_root: str | None = None
    instruction: str
    compressed_output: str
    command: str | None = None
    command_exit_code: int | None = None
    referenced_files: list["ReferencedFileRecord"] = Field(default_factory=list)
    extracted_terms: list["ExtractedTermRecord"] = Field(default_factory=list)
    matched_fields: list[str] = Field(default_factory=list)
    score: int = 0


class ExtractedSignal(StrictModel):
    """Deterministic signal extracted before model usage."""

    matched_domains: list[str] = Field(default_factory=list)
    referenced_files: list[str] = Field(default_factory=list)
    traceback_frames: list[str] = Field(default_factory=list)
    symbols: list[str] = Field(default_factory=list)
    tests: list[str] = Field(default_factory=list)
    packages: list[str] = Field(default_factory=list)
    command_terms: list[str] = Field(default_factory=list)
    eslint_rules: list[str] = Field(default_factory=list)
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
    exact_cache_key: str | None = None
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

    model: str = "ibm-granite/granite-4.0-350m-GGUF"
    gguf_filename: str | None = "smollm2-360m-instruct-q8_0.gguf"
    llama_context_window: int | None = None
    device: str = "auto"
    dtype: str = "auto"
    attn_implementation: str = "auto"
    quantization: LocalQuantizationMode = LocalQuantizationMode.NONE
    model_cache_path: str | None = None

    @model_validator(mode="after")
    def _validate_cpu_requirements(self) -> "LocalModelConfig":
        if not self.model.strip():
            raise ValueError("local.model cannot be empty.")
        normalized_device = self.device.strip().casefold()
        if normalized_device == "cpu" and not (self.gguf_filename or "").strip():
            raise ValueError("local.gguf_filename is required when local.device is cpu.")
        if normalized_device == "cpu" and self.quantization is not LocalQuantizationMode.NONE:
            raise ValueError(
                "local.quantization must be `none` when local.device is cpu; "
                "llama.cpp CPU runtime does not use Transformers quantization."
            )
        if self.llama_context_window is not None and self.llama_context_window <= 0:
            raise ValueError("local.llama_context_window must be greater than 0.")
        return self


class EmbeddingConfig(StrictModel):
    """Embedding model configuration."""

    model: str = "microsoft/harrier-oss-v1-0.6b"
    backend: str = "auto"
    device: str = "auto"
    dtype: str = "auto"
    attn_implementation: str = "auto"
    query_prompt_name: str = ""
    query_prompt: str = ""
    document_prompt_name: str = ""
    max_length: int = 32768


class VectorStoreStatus(StrictModel):
    """Availability status for sqlite-vec backed indexing."""

    available: bool
    warning: str | None = None
    dimension: int | None = None
    model_name: str | None = None
    sqlite_vec_version: str | None = None


class VectorSearchHit(StrictModel):
    """One vector-search hit from sqlite-vec."""

    record_id: int
    distance: float


class RecallConfig(StrictModel):
    """Recall retrieval configuration."""

    default_limit: int = Field(default=10, ge=1)
    lexical_candidate_limit: int = Field(default=50, ge=1)
    vector_candidate_limit: int = Field(default=50, ge=1)
    max_vector_distance: float = Field(default=0.75, ge=0.0)


class DaemonConfig(StrictModel):
    """Local daemon runtime configuration."""

    enabled: bool = True
    idle_timeout_seconds: int = Field(default=600, ge=1)
    startup_timeout_ms: int = Field(default=15000, ge=1000)
    embedding_batch_window_ms: int = Field(default=20, ge=0)
    embedding_max_batch_size: int = Field(default=16, ge=1)


class RetentionConfig(StrictModel):
    """Persistent record-retention configuration."""

    max_age_days: int = Field(default=30, ge=1)


class RetentionCleanupResult(StrictModel):
    """Result of one retention cleanup run."""

    deleted_record_count: int = 0
    deleted_record_ids: list[int] = Field(default_factory=list)


class AppConfig(StrictModel):
    """Top-level resolved ctxsift configuration."""

    timeout_ms: int = 90000
    retries: int = 1
    max_output_tokens: int = 512
    db_path: str | None = None
    remote: RemoteModelConfig = Field(default_factory=RemoteModelConfig)
    local: LocalModelConfig = Field(default_factory=LocalModelConfig)
    embedding: EmbeddingConfig = Field(default_factory=EmbeddingConfig)
    recall: RecallConfig = Field(default_factory=RecallConfig)
    daemon: DaemonConfig = Field(default_factory=DaemonConfig)
    retention: RetentionConfig = Field(default_factory=RetentionConfig)
