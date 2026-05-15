"""Recall search orchestration and CLI rendering."""

from __future__ import annotations

import asyncio
from pathlib import Path
import re

from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.embeddings import create_embedding_backend
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError, QueryEmbeddingRequest
from ctxsift.recall_freshness import assess_record_freshness
from ctxsift.recall_hybrid import HybridRecallRequest, build_hybrid_records
from ctxsift.storage import initialize_database, read_recall_records_by_ids, search_records
from ctxsift.types import RecallRecord
from ctxsift.vector_store import search_record_embeddings
from ctxsift.workspace import detect_workspace_context

SEARCH_TERM_RE = re.compile(r"[\w./:\\-]+")


async def recall_records(
    query: str,
    cwd: Path,
    file_filters: list[str] | None = None,
    limit: int | None = None,
) -> list[RecallRecord]:
    """Recall stored records and annotate them with freshness labels."""
    workspace = detect_workspace_context(cwd)
    resolved_config = resolve_config(ConfigResolutionRequest(cwd=Path(workspace.cwd)))
    recall_config = resolved_config.config.recall
    db_path = _resolved_db_path(workspace.db_path, resolved_config.config.db_path)
    await initialize_database(db_path)
    resolved_limit = limit or recall_config.default_limit
    normalized_query = query.casefold().strip()
    search_terms = _search_terms(query)
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
        recall_config.vector_candidate_limit,
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
            search_terms=search_terms,
            max_vector_distance=recall_config.max_vector_distance,
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
        f"[{result.record_id}] {result.freshness_status.value} score={result.score} created_at={result.created_at}",
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


def _resolved_db_path(workspace_db_path: str | None, config_db_path: str | None) -> Path:
    selected = config_db_path or workspace_db_path
    if not selected:
        raise ValueError("Could not resolve a ctxsift database path.")
    return Path(selected).expanduser()


async def _vector_hits(db_path: Path, query: str, config, limit: int):
    try:
        backend = create_embedding_backend(config)
        dimension = await backend.embedding_dimension()
        query_vector = await backend.embed_query(
            QueryEmbeddingRequest(
                text=query,
                max_length=config.max_length,
            )
        )
    except EmbeddingBackendUnavailableError:
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


def _search_terms(query: str) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for match in SEARCH_TERM_RE.finditer(query):
        value = match.group(0).casefold()
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result
