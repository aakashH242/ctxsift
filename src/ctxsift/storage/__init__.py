"""Data persistence: SQLite CRUD, vector store, and retention cleanup."""

from ctxsift.storage.database import (
    SCHEMA_VERSION,
    StorageInitResult,
    find_cached_record,
    initialize_database,
    insert_record_bundle,
    prune_expired_records,
    read_recall_records_by_ids,
    read_schema_version,
    retention_cleanup_due,
    search_records,
)
from ctxsift.storage.vector import (
    delete_record_embeddings,
    ensure_vector_store,
    probe_vector_store,
    search_record_embeddings,
    upsert_record_embedding,
)

__all__ = [
    "SCHEMA_VERSION",
    "StorageInitResult",
    "delete_record_embeddings",
    "ensure_vector_store",
    "find_cached_record",
    "initialize_database",
    "insert_record_bundle",
    "probe_vector_store",
    "prune_expired_records",
    "read_recall_records_by_ids",
    "read_schema_version",
    "retention_cleanup_due",
    "search_records",
    "search_record_embeddings",
    "upsert_record_embedding",
]
