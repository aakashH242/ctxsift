"""Signal extraction: deterministic file and term extraction from command output."""

from ctxsift.extraction.signal import (
    ExtractionContext,
    build_extracted_terms,
    extract_referenced_files,
    extract_signal,
)
from ctxsift.extraction.domains import DomainExtractionResult, run_domain_parsers

__all__ = [
    "DomainExtractionResult",
    "ExtractionContext",
    "build_extracted_terms",
    "extract_referenced_files",
    "extract_signal",
    "run_domain_parsers",
]
