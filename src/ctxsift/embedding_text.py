"""Compact text builders for recall embeddings."""

from __future__ import annotations

from ctxsift.types import ExtractedTermRecord, ReferencedFileRecord, StoredRecord


def build_record_embedding_text(
    record: StoredRecord,
    referenced_files: list[ReferencedFileRecord],
    extracted_terms: list[ExtractedTermRecord],
) -> str:
    """Build compact, searchable text for vector recall indexing."""
    lines = [
        f"Instruction: {record.instruction}",
        f"Summary: {record.compressed_output}",
    ]
    if record.command:
        lines.append(f"Command: {record.command}")
    if referenced_files:
        file_list = ", ".join(item.path for item in referenced_files[:12])
        lines.append(f"Files: {file_list}")
    if extracted_terms:
        terms = ", ".join(item.term for item in extracted_terms[:24])
        lines.append(f"Terms: {terms}")
    return "\n".join(lines)
