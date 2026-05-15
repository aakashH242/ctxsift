"""Recall search orchestration and CLI rendering."""

from __future__ import annotations

from pathlib import Path

from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.recall_freshness import assess_record_freshness
from ctxsift.storage import initialize_database, search_records
from ctxsift.types import RecallRecord
from ctxsift.workspace import detect_workspace_context


async def recall_records(
    query: str,
    cwd: Path,
    file_filters: list[str] | None = None,
    limit: int = 10,
) -> list[RecallRecord]:
    """Recall stored records and annotate them with freshness labels."""
    workspace = detect_workspace_context(cwd)
    resolved_config = resolve_config(ConfigResolutionRequest(cwd=Path(workspace.cwd)))
    db_path = _resolved_db_path(workspace.db_path, resolved_config.config.db_path)
    await initialize_database(db_path)
    rows = await search_records(db_path, query, file_filters=file_filters, limit=limit)
    results: list[RecallRecord] = []
    for row in rows:
        freshness_status = await assess_record_freshness(row)
        results.append(
            RecallRecord(
                record_id=row.record_id,
                created_at=row.created_at,
                freshness_status=freshness_status,
                instruction=row.instruction,
                compressed_output=row.compressed_output,
                command=row.command,
                command_exit_code=row.command_exit_code,
                referenced_files=[item.path for item in row.referenced_files],
                matched_fields=row.matched_fields,
                score=row.score,
            )
        )
    return results


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
