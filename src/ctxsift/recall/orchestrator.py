"""Recall search orchestration and CLI rendering."""

from __future__ import annotations

import asyncio
from pathlib import Path

from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.embeddings import create_embedding_backend
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError, QueryEmbeddingRequest
from ctxsift.recall.freshness import assess_record_freshness
from ctxsift.recall.hybrid import HybridRecallRequest, build_hybrid_records
from ctxsift.recall.temporal import render_capture_time
from ctxsift.storage.retention import schedule_retention_cleanup
from ctxsift.shared.db_path import resolved_db_path
from ctxsift.shared.search_terms import search_terms as _search_terms
from ctxsift.storage import initialize_database, read_recall_records_by_ids, search_records
from ctxsift.types import RecallRecord
from ctxsift.storage.vector import search_record_embeddings
from ctxsift.workspace import detect_workspace_context


async def recall_records(
    query: str,
    cwd: Path,
    file_filters: list[str] | None = None,
    limit: int | None = None,
    warnings_sink: list[str] | None = None,
) -> list[RecallRecord]:
    """Recall stored records and annotate them with freshness labels."""
    workspace = detect_workspace_context(cwd)
    resolved_config = resolve_config(ConfigResolutionRequest(cwd=Path(workspace.cwd)))
    recall_config = resolved_config.config.recall
    db_path = resolved_db_path(workspace.db_path, resolved_config.config.db_path)
    await initialize_database(db_path)
    try:
        await schedule_retention_cleanup(
            db_path,
            resolved_config.config.retention.max_age_days,
        )
    except Exception:
        pass
    resolved_limit = limit or recall_config.default_limit
    normalized_query = query.casefold().strip()
    search_terms_list = _search_terms(query)
    lexical_records = await search_records(
        db_path,
        query,
        file_filters=None,
        limit=recall_config.lexical_candidate_limit,
    )
    vector_hits = await _vector_hits(
        db_path,
        query,
        resolved_config.config.embedding,
        resolved_config.config.daemon,
        resolved_config.config.timeout_ms,
        recall_config.vector_candidate_limit,
        warnings_sink=warnings_sink,
    )
    candidate_records = await _candidate_records(db_path, lexical_records, vector_hits)
    freshness_pairs = await asyncio.gather(
        *(assess_record_freshness(record) for record in candidate_records),
    )
    freshness_by_record_id = {
        record.record_id: freshness
        for record, freshness in zip(candidate_records, freshness_pairs, strict=True)
    }
    return build_hybrid_records(
        HybridRecallRequest(
            lexical_records=lexical_records,
            all_records=candidate_records,
            vector_hits=vector_hits,
            freshness_by_record_id=freshness_by_record_id,
            file_filters=_normalized_file_filters(file_filters),
            limit=resolved_limit,
            normalized_query=normalized_query,
            search_terms=search_terms_list,
            max_vector_distance=recall_config.max_vector_distance,
            min_score=recall_config.min_score,
            weak_fallback_min_score=recall_config.weak_fallback_min_score,
            weak_fallback_limit=recall_config.weak_fallback_limit,
        )
    )


def render_recall_records(results: list[RecallRecord]) -> str:
    """Render recall results for the CLI."""
    if not results:
        return "No recall results."
    blocks = [render_recall_record(result) for result in results]
    return "\n\n".join(blocks)


def render_recall_record(result: RecallRecord) -> str:
    """Render one recall result block."""
    lines = [
        f"[{result.record_id}] {result.freshness_status.value} score={result.score}",
        render_capture_time(result.created_at),
        f"Instruction: {result.instruction}",
    ]
    if result.command:
        lines.append(f"Command: {result.command}")
    if result.command_exit_code is not None:
        lines.append(f"Exit code: {result.command_exit_code}")
    if result.referenced_files:
        lines.append(f"Files: {', '.join(result.referenced_files)}")
    if result.matched_fields:
        lines.append(f"Matched: {', '.join(result.matched_fields)}")
    lines.append("Summary:")
    lines.append(result.compressed_output)
    return "\n".join(lines)


async def _vector_hits(
    db_path: Path,
    query: str,
    config,
    daemon_config,
    timeout_ms: int,
    limit: int,
    warnings_sink: list[str] | None = None,
):
    try:
        backend = _embedding_backend(config, daemon_config, timeout_ms)
        dimension = await backend.embedding_dimension()
        query_vector = await backend.embed_query(
            QueryEmbeddingRequest(
                text=query,
                max_length=config.max_length,
            )
        )
    except EmbeddingBackendUnavailableError as error:
        if warnings_sink is not None:
            warnings_sink.append(
                f"[ctxsift warning] Embedding recall backend unavailable: {error}. "
                "Continuing with lexical-only recall."
            )
        return []
    _, hits = await search_record_embeddings(
        db_path=db_path,
        query_vector=query_vector,
        model_name=backend.model_name,
        dimension=dimension,
        limit=limit,
    )
    return hits


async def _candidate_records(db_path: Path, lexical_records, vector_hits):
    record_map = {record.record_id: record for record in lexical_records}
    vector_only_ids = [hit.record_id for hit in vector_hits if hit.record_id not in record_map]
    if vector_only_ids:
        vector_only_records = await read_recall_records_by_ids(db_path, vector_only_ids)
        for record in vector_only_records:
            record_map[record.record_id] = record
    return list(record_map.values())


def _normalized_file_filters(file_filters: list[str] | None) -> list[str]:
    return [item.casefold().replace("\\", "/") for item in (file_filters or [])]


def _embedding_backend(config, daemon_config, timeout_ms: int):
    if daemon_config is None or not daemon_config.enabled:
        return create_embedding_backend(config)
    return create_embedding_backend(config, daemon=daemon_config, timeout_ms=timeout_ms)
