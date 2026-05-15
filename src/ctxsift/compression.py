"""Compression pipeline, exact-cache helpers, and deterministic fallback."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re

from ctxsift import __version__
from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.embedding_indexer import index_record_embedding
from ctxsift.extraction import (
    ExtractionContext,
    build_extracted_terms,
    extract_referenced_files,
    extract_signal,
)
from ctxsift.models import create_local_backend
from ctxsift.models.base import BackendUnavailableError, ModelCompressionInput
from ctxsift.storage import find_cached_record, initialize_database, insert_record_bundle
from ctxsift.types import (
    CompressionRequest,
    CompressionResult,
    EmbeddingConfig,
    ExtractedSignal,
    ExtractedTermRecord,
    ReferencedFileRecord,
    StoredRecord,
    WorkspaceContext,
)
from ctxsift.workspace import detect_workspace_context


DETERMINISTIC_MODEL_ID = "deterministic"
DETERMINISTIC_PROVIDER = "deterministic"
MODEL_PROMPT_VERSION = "gemma-transformers-v1"
DETERMINISTIC_PROMPT_VERSION = "deterministic-v1"
LINE_LIMIT = 3
CHARACTERS_PER_TOKEN = 4
WHITESPACE_RE = re.compile(r"\s+")


async def compress_input(request: CompressionRequest) -> CompressionResult:
    """Compress one stdin payload through local model inference or deterministic fallback."""
    workspace = detect_workspace_context(Path(request.cwd) if request.cwd else None)
    resolved_config = resolve_config(
        ConfigResolutionRequest(
            cwd=Path(workspace.cwd),
            cli_overrides=_compression_overrides(request),
        )
    )
    db_path = _resolved_db_path(workspace.db_path, resolved_config.config.db_path)
    await initialize_database(db_path)

    normalized_instruction = normalize_instruction(request.instruction)
    raw_input_hash = sha256_text(request.raw_input)
    extraction_context = ExtractionContext(
        cwd=Path(workspace.cwd),
        workspace_root=Path(workspace.workspace_root),
    )
    extraction_text = _extraction_text(request)
    signal = extract_signal(extraction_text, extraction_context, command_args=request.command_args)
    referenced_files = extract_referenced_files(
        extraction_text,
        extraction_context,
        command_args=request.command_args,
    )
    extracted_terms = build_extracted_terms(signal)

    backend = create_local_backend(resolved_config.config.local)
    model_cache_key = build_exact_cache_key(
        workspace_root=workspace.workspace_root,
        raw_input_hash=raw_input_hash,
        normalized_instruction=normalized_instruction,
        model_id=backend.cache_model_id,
        max_output_tokens=resolved_config.config.max_output_tokens,
        ctxsift_version=__version__,
        prompt_version=MODEL_PROMPT_VERSION,
    )
    cached_result = await _cached_compression_result(db_path, model_cache_key)
    if cached_result is not None:
        return cached_result

    try:
        compressed_output = await backend.compress(
            ModelCompressionInput(
                instruction=request.instruction,
                raw_input=request.raw_input,
                extracted_signal=signal,
                max_output_tokens=resolved_config.config.max_output_tokens,
            )
        )
        return await _store_new_result(
            db_path=db_path,
            request=request,
            workspace=workspace,
            signal=signal,
            referenced_files=referenced_files,
            extracted_terms=extracted_terms,
            normalized_instruction=normalized_instruction,
            raw_input_hash=raw_input_hash,
            compressed_output=compressed_output,
            exact_cache_key=model_cache_key,
            model_provider=backend.provider_name,
            model_name=backend.model_name,
            prompt_version=MODEL_PROMPT_VERSION,
            max_output_tokens=resolved_config.config.max_output_tokens,
            embedding_config=resolved_config.config.embedding,
        )
    except BackendUnavailableError:
        return await _deterministic_fallback(
            db_path=db_path,
            request=request,
            workspace=workspace,
            signal=signal,
            referenced_files=referenced_files,
            extracted_terms=extracted_terms,
            normalized_instruction=normalized_instruction,
            raw_input_hash=raw_input_hash,
            max_output_tokens=resolved_config.config.max_output_tokens,
            embedding_config=resolved_config.config.embedding,
        )


def normalize_instruction(instruction: str) -> str:
    """Normalize an instruction for deterministic cache matching."""
    collapsed = WHITESPACE_RE.sub(" ", instruction.strip())
    return collapsed.casefold()


def build_exact_cache_key(
    workspace_root: str,
    raw_input_hash: str,
    normalized_instruction: str,
    model_id: str,
    max_output_tokens: int,
    ctxsift_version: str,
    prompt_version: str,
) -> str:
    """Build the exact-cache key used for compression lookup."""
    normalized_instruction_hash = sha256_text(normalized_instruction)
    parts = (
        workspace_root,
        raw_input_hash,
        normalized_instruction_hash,
        model_id,
        str(max_output_tokens),
        ctxsift_version,
        prompt_version,
    )
    return sha256_text("\n".join(parts))


def summarize_deterministically(
    raw_input: str, signal: ExtractedSignal, max_output_tokens: int
) -> str:
    """Produce a stable fallback summary without a model backend."""
    summary_lines = _summary_lines(raw_input, signal)
    budget = max(max_output_tokens, 1) * CHARACTERS_PER_TOKEN
    joined = "\n".join(summary_lines)
    if len(joined) <= budget:
        return joined
    return _trim_to_budget(summary_lines, budget)


def sha256_text(value: str) -> str:
    """Hash one text value deterministically."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


async def _cached_compression_result(db_path: Path, cache_key: str) -> CompressionResult | None:
    cached_record = await find_cached_record(db_path, cache_key)
    if cached_record is None:
        return None
    return CompressionResult(
        compressed_output=cached_record.compressed_output,
        used_cache=True,
        model_provider=cached_record.model_provider,
        model_name=cached_record.model_name,
        record_id=cached_record.record_id,
    )


async def _deterministic_fallback(
    db_path: Path,
    request: CompressionRequest,
    workspace: WorkspaceContext,
    signal: ExtractedSignal,
    referenced_files: list[ReferencedFileRecord],
    extracted_terms: list[ExtractedTermRecord],
    normalized_instruction: str,
    raw_input_hash: str,
    max_output_tokens: int,
    embedding_config: EmbeddingConfig,
) -> CompressionResult:
    fallback_cache_key = build_exact_cache_key(
        workspace_root=workspace.workspace_root,
        raw_input_hash=raw_input_hash,
        normalized_instruction=normalized_instruction,
        model_id=DETERMINISTIC_MODEL_ID,
        max_output_tokens=max_output_tokens,
        ctxsift_version=__version__,
        prompt_version=DETERMINISTIC_PROMPT_VERSION,
    )
    cached_result = await _cached_compression_result(db_path, fallback_cache_key)
    if cached_result is not None:
        return cached_result
    compressed_output = summarize_deterministically(request.raw_input, signal, max_output_tokens)
    return await _store_new_result(
        db_path=db_path,
        request=request,
        workspace=workspace,
        signal=signal,
        referenced_files=referenced_files,
        extracted_terms=extracted_terms,
        normalized_instruction=normalized_instruction,
        raw_input_hash=raw_input_hash,
        compressed_output=compressed_output,
        exact_cache_key=fallback_cache_key,
        model_provider=DETERMINISTIC_PROVIDER,
        model_name=DETERMINISTIC_MODEL_ID,
        prompt_version=DETERMINISTIC_PROMPT_VERSION,
        max_output_tokens=max_output_tokens,
        embedding_config=embedding_config,
    )


async def _store_new_result(
    db_path: Path,
    request: CompressionRequest,
    workspace: WorkspaceContext,
    signal: ExtractedSignal,
    referenced_files: list[ReferencedFileRecord],
    extracted_terms: list[ExtractedTermRecord],
    normalized_instruction: str,
    raw_input_hash: str,
    compressed_output: str,
    exact_cache_key: str,
    model_provider: str,
    model_name: str,
    prompt_version: str,
    max_output_tokens: int,
    embedding_config: EmbeddingConfig,
) -> CompressionResult:
    record = StoredRecord(
        instruction=request.instruction,
        normalized_instruction=normalized_instruction,
        compressed_output=compressed_output,
        raw_input_hash=raw_input_hash,
        exact_cache_key=exact_cache_key,
        mode=request.mode,
        workspace_root=workspace.workspace_root,
        cwd=workspace.cwd,
        git_head=request.git_head,
        git_branch=request.git_branch,
        git_dirty=request.git_dirty,
        command=request.command,
        command_exit_code=request.command_exit_code,
        command_duration_ms=request.command_duration_ms,
        stdout_hash=request.stdout_hash,
        stderr_hash=request.stderr_hash,
        model_provider=model_provider,
        model_name=model_name,
        max_output_tokens=max_output_tokens,
        prompt_version=prompt_version,
        ctxsift_version=__version__,
    )
    record_id = await insert_record_bundle(
        db_path,
        record,
        referenced_files=referenced_files,
        extracted_terms=extracted_terms,
    )
    try:
        await index_record_embedding(
            db_path=db_path,
            record_id=record_id,
            record=record,
            referenced_files=referenced_files,
            extracted_terms=extracted_terms,
            config=embedding_config,
        )
    except Exception:
        pass
    return CompressionResult(
        compressed_output=compressed_output,
        referenced_files=signal.referenced_files,
        extracted_terms=[item.term for item in extracted_terms],
        used_cache=False,
        model_provider=model_provider,
        model_name=model_name,
        record_id=record_id,
    )


def _compression_overrides(request: CompressionRequest) -> dict[str, int]:
    overrides: dict[str, int] = {}
    if request.max_output_tokens is not None:
        overrides["max_output_tokens"] = request.max_output_tokens
    return overrides


def _resolved_db_path(workspace_db_path: str | None, config_db_path: str | None) -> Path:
    selected = config_db_path or workspace_db_path
    if not selected:
        raise ValueError("Could not resolve a ctxsift database path.")
    return Path(selected).expanduser()


def _extraction_text(request: CompressionRequest) -> str:
    if request.mode != "run":
        return request.raw_input
    output_text = _run_payload_output_text(request.raw_input)
    if output_text is not None:
        return output_text
    return request.raw_input


def _run_payload_output_text(raw_input: str) -> str | None:
    lines = raw_input.splitlines()
    sections: list[str] = []
    index = 0
    saw_output_section = False
    while index < len(lines):
        if lines[index] not in {"Stdout:", "Stderr:"}:
            index += 1
            continue
        saw_output_section = True
        index += 1
        block_lines, index = _read_run_output_block(lines, index)
        if block_lines:
            sections.append("\n".join(block_lines))
    if not saw_output_section:
        return None
    return "\n".join(section for section in sections if section).strip()


def _read_run_output_block(lines: list[str], start_index: int) -> tuple[list[str], int]:
    index = start_index
    if index >= len(lines):
        return [], index
    if lines[index].startswith("```"):
        index += 1
        block_lines: list[str] = []
        while index < len(lines) and not lines[index].startswith("```"):
            block_lines.append(lines[index])
            index += 1
        if index < len(lines) and lines[index].startswith("```"):
            index += 1
        return block_lines, index
    block_lines = []
    while index < len(lines) and lines[index].strip():
        block_lines.append(lines[index])
        index += 1
    return block_lines, index


def _summary_lines(raw_input: str, signal: ExtractedSignal) -> list[str]:
    if not raw_input.strip():
        return ["Summary:", "(no input)"]
    lines: list[str] = []
    if signal.matched_domains and signal.matched_domains != ["generic"]:
        lines.append(f"Domains: {', '.join(signal.matched_domains)}")
    _append_joined(lines, "Files", signal.referenced_files)
    _append_joined(lines, "Traceback", signal.traceback_frames)
    _append_joined(lines, "Tests", signal.tests)
    _append_joined(lines, "Packages", signal.packages)
    _append_joined(lines, "Symbols", signal.symbols)
    _append_joined(lines, "Commands", signal.command_terms)
    _append_joined(lines, "Exit codes", signal.exit_code_lines)
    _append_labeled_lines(lines, "Warnings", signal.warning_lines)
    _append_labeled_lines(lines, "Errors", signal.error_lines)
    if lines:
        return lines
    fallback_lines = _fallback_lines(raw_input)
    if fallback_lines:
        return ["Summary:"] + fallback_lines
    return ["Summary:", "(no input)"]


def _append_joined(lines: list[str], label: str, values: list[str]) -> None:
    if not values:
        return
    lines.append(f"{label}: {', '.join(values[:LINE_LIMIT])}")


def _append_labeled_lines(lines: list[str], label: str, values: list[str]) -> None:
    if not values:
        return
    lines.append(f"{label}:")
    lines.extend(f"- {value}" for value in values[:LINE_LIMIT])


def _fallback_lines(raw_input: str) -> list[str]:
    non_empty_lines = [line.strip() for line in raw_input.splitlines() if line.strip()]
    return [f"- {line}" for line in non_empty_lines[:LINE_LIMIT]]


def _trim_to_budget(summary_lines: list[str], budget: int) -> str:
    trimmed_lines: list[str] = []
    used = 0
    for line in summary_lines:
        line_cost = len(line) if not trimmed_lines else len(line) + 1
        if used + line_cost <= budget:
            trimmed_lines.append(line)
            used += line_cost
            continue
        remaining = budget - used
        if remaining <= 4:
            break
        if trimmed_lines:
            remaining -= 1
        trimmed_lines.append(f"{line[:remaining - 3].rstrip()}...")
        break
    if not trimmed_lines:
        return "..."
    return "\n".join(trimmed_lines)
