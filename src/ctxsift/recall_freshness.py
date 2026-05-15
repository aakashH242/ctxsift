"""Freshness validation helpers for recall records."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime
from datetime import timezone
from pathlib import Path

from ctxsift.file_fingerprint import sha256_if_reasonable
from ctxsift.git_file_status import read_git_file_status
from ctxsift.types import FreshnessStatus, RecallStorageRecord, ReferencedFileRecord


MTIME_STALE_TOLERANCE_SECONDS = 1.0


@dataclass(frozen=True)
class FileFreshnessEvidence:
    """Freshness evidence for one referenced file."""

    status: FreshnessStatus


async def assess_record_freshness(record: RecallStorageRecord) -> FreshnessStatus:
    """Assess freshness for one recalled record using git, hash, and mtime cues."""
    if not record.referenced_files:
        return FreshnessStatus.UNVERIFIABLE
    workspace_root = Path(record.workspace_root) if record.workspace_root else None
    captured_at = _parse_created_at(record.created_at)
    saw_unknown = False
    for referenced_file in record.referenced_files:
        evidence = await _assess_referenced_file(
            record=record,
            referenced_file=referenced_file,
            workspace_root=workspace_root,
            captured_at=captured_at,
        )
        if evidence.status is FreshnessStatus.STALE_DELETED:
            return FreshnessStatus.STALE_DELETED
        if evidence.status is FreshnessStatus.STALE_CHANGED:
            return FreshnessStatus.STALE_CHANGED
        if evidence.status is FreshnessStatus.UNKNOWN:
            saw_unknown = True
    if saw_unknown:
        return FreshnessStatus.UNKNOWN
    return FreshnessStatus.FRESH


def resolve_referenced_file(
    referenced_file: ReferencedFileRecord,
    workspace_root: Path | None,
) -> Path | None:
    """Resolve a referenced file against the stored workspace root."""
    if referenced_file.abs_path:
        return Path(referenced_file.abs_path)
    candidate = Path(referenced_file.path)
    if candidate.is_absolute():
        return candidate
    if workspace_root is None:
        return None
    return workspace_root / candidate


async def _assess_referenced_file(
    record: RecallStorageRecord,
    referenced_file: ReferencedFileRecord,
    workspace_root: Path | None,
    captured_at: datetime,
) -> FileFreshnessEvidence:
    resolved_path = resolve_referenced_file(referenced_file, workspace_root)
    if resolved_path is None:
        return FileFreshnessEvidence(FreshnessStatus.UNKNOWN)
    if referenced_file.exists_at_capture and not resolved_path.exists():
        return FileFreshnessEvidence(FreshnessStatus.STALE_DELETED)
    if not referenced_file.exists_at_capture:
        if resolved_path.exists():
            return FileFreshnessEvidence(FreshnessStatus.STALE_CHANGED)
        return FileFreshnessEvidence(FreshnessStatus.UNKNOWN)
    git_status = await _read_relative_git_status(record, referenced_file, workspace_root)
    if git_status is not None:
        if git_status.is_deleted:
            return FileFreshnessEvidence(FreshnessStatus.STALE_DELETED)
        if git_status.is_changed:
            return FileFreshnessEvidence(FreshnessStatus.STALE_CHANGED)
    if referenced_file.sha256:
        current_sha = await asyncio.to_thread(sha256_if_reasonable, resolved_path)
        if current_sha and current_sha != referenced_file.sha256:
            return FileFreshnessEvidence(FreshnessStatus.STALE_CHANGED)
        if current_sha:
            return FileFreshnessEvidence(FreshnessStatus.FRESH)
    if _mtime_is_newer_than_capture(resolved_path, captured_at):
        return FileFreshnessEvidence(FreshnessStatus.STALE_CHANGED)
    if resolved_path.exists():
        return FileFreshnessEvidence(FreshnessStatus.FRESH)
    return FileFreshnessEvidence(FreshnessStatus.UNKNOWN)


async def _read_relative_git_status(
    record: RecallStorageRecord,
    referenced_file: ReferencedFileRecord,
    workspace_root: Path | None,
):
    if workspace_root is None:
        return None
    relative_path = _relative_path_for_git(referenced_file, workspace_root)
    if relative_path is None:
        return None
    return await read_git_file_status(workspace_root, relative_path)


def _relative_path_for_git(
    referenced_file: ReferencedFileRecord,
    workspace_root: Path,
) -> str | None:
    candidate = Path(referenced_file.path)
    if not candidate.is_absolute():
        return candidate.as_posix()
    try:
        return candidate.relative_to(workspace_root).as_posix()
    except ValueError:
        return None


def _mtime_is_newer_than_capture(path: Path, captured_at: datetime) -> bool:
    if not path.exists():
        return False
    modified_at = path.stat().st_mtime
    return modified_at > (captured_at.timestamp() + MTIME_STALE_TOLERANCE_SECONDS)


def _parse_created_at(created_at: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(created_at)
    except ValueError:
        parsed = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)
