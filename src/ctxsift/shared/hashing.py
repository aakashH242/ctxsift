"""Deterministic hashing helpers for text and files."""

from __future__ import annotations

import hashlib
from pathlib import Path

MAX_HASH_FILE_SIZE_BYTES = 2 * 1024 * 1024


def sha256_text(value: str) -> str:
    """Hash one text value deterministically."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_if_reasonable(path: Path | None) -> str | None:
    """Hash a file when it exists and is small enough for cheap verification."""
    if path is None or not path.exists() or not path.is_file():
        return None
    if path.stat().st_size > MAX_HASH_FILE_SIZE_BYTES:
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()
