"""Deterministic extraction helpers."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re

from ctxsift.extraction_domains import DomainExtractionResult, run_domain_parsers
from ctxsift.types import ExtractedSignal, ExtractedTermRecord, ReferencedFileRecord


MAX_HASH_FILE_SIZE_BYTES = 2 * 1024 * 1024

TRACEBACK_FILE_RE = re.compile(r'File ["\'](?P<path>[^"\']+)["\'], line \d+')
GENERIC_FILE_RE = re.compile(
    r"(?P<path>(?:[A-Za-z]:[\\/]|\.{0,2}[\\/]|)(?:[\w.\- ]+[\\/])*[\w.\- ]+\.(?:py|pyi|ts|tsx|js|jsx|json|ya?ml|toml|ini|cfg|md|txt|sql|sh|ps1|dockerfile))(?::\d+(?::\d+)?)?(?:::[:\w.\-]+)?",
    re.IGNORECASE,
)
PYTEST_TEST_RE = re.compile(r"(?P<test>[\w./\\-]+::[\w\[\].-]+)")
SYMBOL_RE = re.compile(r"\b(?:[A-Z][A-Za-z0-9_]*Error|[A-Za-z_][A-Za-z0-9_]*Exception|[A-Za-z_][A-Za-z0-9_]*Warning)\b")
MODULE_RE = re.compile(
    r"(?:No module named|Cannot find module|ModuleNotFoundError: No module named)\s+['\"](?P<package>[^'\"]+)['\"]"
)
EXIT_CODE_RE = re.compile(r"\b(?:exit(?:ed)? with code|exit code)\s+\d+\b", re.IGNORECASE)
WARNING_RE = re.compile(r"\bwarning\b", re.IGNORECASE)
ERROR_RE = re.compile(r"\b(error|failed|failure|traceback|exception)\b", re.IGNORECASE)
COMMAND_RE = re.compile(r"\b(?:pytest|ruff|mypy|docker|docker-compose|compose|kubectl|npm|pnpm|yarn|git|python|uv)\b")


@dataclass(frozen=True)
class ExtractionContext:
    """Filesystem context used for deterministic extraction."""

    cwd: Path
    workspace_root: Path


def extract_signal(text: str, context: ExtractionContext) -> ExtractedSignal:
    """Extract deterministic signal from command output."""
    referenced_files = extract_referenced_files(text, context)
    domain_results = run_domain_parsers(text)
    generic_signal = _generic_signal(text)
    merged_signal = _merge_domain_results(domain_results, generic_signal)
    return ExtractedSignal(
        matched_domains=merged_signal.matched_domains,
        referenced_files=[item.path for item in referenced_files],
        traceback_frames=merged_signal.traceback_frames,
        symbols=merged_signal.symbols,
        tests=merged_signal.tests,
        packages=merged_signal.packages,
        command_terms=merged_signal.command_terms,
        eslint_rules=merged_signal.eslint_rules,
        exit_code_lines=merged_signal.exit_code_lines,
        warning_lines=merged_signal.warning_lines,
        error_lines=merged_signal.error_lines,
    )


def extract_referenced_files(text: str, context: ExtractionContext) -> list[ReferencedFileRecord]:
    """Extract normalized file references and capture lightweight file metadata."""
    candidates = _extract_file_candidates(text)
    records: list[ReferencedFileRecord] = []
    seen_paths: set[str] = set()
    for candidate in candidates:
        normalized = _normalize_candidate_path(candidate)
        resolved = _resolve_candidate_path(normalized, context)
        display_path = _display_path(normalized, resolved, context)
        if display_path in seen_paths:
            continue
        seen_paths.add(display_path)
        records.append(
            ReferencedFileRecord(
                path=display_path,
                abs_path=str(resolved) if resolved is not None else None,
                sha256=_sha256_if_reasonable(resolved),
                exists_at_capture=resolved is not None and resolved.exists(),
            )
        )
    return records


def build_extracted_terms(signal: ExtractedSignal) -> list[ExtractedTermRecord]:
    """Convert extracted signal into searchable term rows."""
    terms: list[ExtractedTermRecord] = []
    terms.extend(_term_rows(signal.referenced_files, "file"))
    terms.extend(_term_rows(signal.traceback_frames, "traceback_frame"))
    terms.extend(_term_rows(signal.symbols, "symbol"))
    terms.extend(_term_rows(signal.tests, "test"))
    terms.extend(_term_rows(signal.packages, "package"))
    terms.extend(_term_rows(signal.command_terms, "command"))
    terms.extend(_term_rows(signal.eslint_rules, "eslint_rule"))
    return terms


def _generic_signal(text: str) -> ExtractedSignal:
    lines = text.splitlines()
    return ExtractedSignal(
        matched_domains=["generic"],
        traceback_frames=[],
        symbols=_dedupe(_extract_symbols(text)),
        tests=_dedupe(_extract_tests(text)),
        packages=_dedupe(_extract_packages(text)),
        command_terms=_dedupe(_extract_command_terms(text)),
        eslint_rules=[],
        exit_code_lines=_matching_lines(lines, EXIT_CODE_RE),
        warning_lines=_matching_lines(lines, WARNING_RE),
        error_lines=_matching_lines(lines, ERROR_RE),
    )


def _merge_domain_results(
    domain_results: list[DomainExtractionResult],
    generic_signal: ExtractedSignal,
) -> ExtractedSignal:
    matched_domains = [result.domain for result in domain_results if result.matched]
    if not matched_domains:
        return generic_signal
    traceback_frames: list[str] = []
    symbols: list[str] = []
    tests: list[str] = []
    packages: list[str] = []
    command_terms: list[str] = []
    eslint_rules: list[str] = []
    warning_lines: list[str] = []
    error_lines: list[str] = []
    exit_code_lines: list[str] = []
    for result in domain_results:
        if not result.matched:
            continue
        traceback_frames.extend(result.traceback_frames)
        symbols.extend(result.symbols)
        tests.extend(result.tests)
        packages.extend(result.packages)
        command_terms.extend(result.command_terms)
        eslint_rules.extend(result.eslint_rules)
        warning_lines.extend(result.warning_lines)
        error_lines.extend(result.error_lines)
        exit_code_lines.extend(result.exit_code_lines)
    traceback_frames.extend(generic_signal.traceback_frames)
    symbols.extend(generic_signal.symbols)
    tests.extend(generic_signal.tests)
    packages.extend(generic_signal.packages)
    command_terms.extend(generic_signal.command_terms)
    eslint_rules.extend(generic_signal.eslint_rules)
    warning_lines.extend(generic_signal.warning_lines)
    error_lines.extend(generic_signal.error_lines)
    exit_code_lines.extend(generic_signal.exit_code_lines)
    return ExtractedSignal(
        matched_domains=_dedupe(matched_domains),
        referenced_files=[],
        traceback_frames=_dedupe(traceback_frames),
        symbols=_dedupe(symbols),
        tests=_dedupe(tests),
        packages=_dedupe(packages),
        command_terms=_dedupe(command_terms),
        eslint_rules=_dedupe(eslint_rules),
        exit_code_lines=_dedupe(exit_code_lines),
        warning_lines=_dedupe(warning_lines),
        error_lines=_dedupe(error_lines),
    )


def _extract_file_candidates(text: str) -> list[str]:
    candidates: list[str] = []
    for match in TRACEBACK_FILE_RE.finditer(text):
        candidates.append(match.group("path"))
    for match in GENERIC_FILE_RE.finditer(text):
        candidates.append(_strip_position_suffix(match.group("path")))
    return candidates


def _strip_position_suffix(candidate: str) -> str:
    without_test = candidate.split("::", 1)[0]
    path_part, separator, tail = without_test.rpartition(":")
    if not separator:
        return without_test
    if tail.isdigit() and path_part:
        prior, inner_separator, inner_tail = path_part.rpartition(":")
        if inner_separator and inner_tail.isdigit():
            return prior
        return path_part
    return without_test


def _normalize_candidate_path(candidate: str) -> Path:
    return Path(candidate.replace("\\", "/"))


def _resolve_candidate_path(candidate: Path, context: ExtractionContext) -> Path | None:
    if candidate.is_absolute():
        resolved = candidate.resolve()
        return resolved if resolved.exists() else None
    cwd_path = (context.cwd / candidate).resolve()
    if cwd_path.exists():
        return cwd_path
    workspace_path = (context.workspace_root / candidate).resolve()
    if workspace_path.exists():
        return workspace_path
    return None


def _display_path(candidate: Path, resolved: Path | None, context: ExtractionContext) -> str:
    if resolved is None:
        return candidate.as_posix()
    try:
        return resolved.relative_to(context.workspace_root).as_posix()
    except ValueError:
        return str(resolved)


def _sha256_if_reasonable(path: Path | None) -> str | None:
    if path is None or not path.exists() or not path.is_file():
        return None
    if path.stat().st_size > MAX_HASH_FILE_SIZE_BYTES:
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _extract_tests(text: str) -> list[str]:
    return [match.group("test") for match in PYTEST_TEST_RE.finditer(text)]


def _extract_packages(text: str) -> list[str]:
    return [match.group("package") for match in MODULE_RE.finditer(text)]


def _extract_symbols(text: str) -> list[str]:
    return [match.group(0) for match in SYMBOL_RE.finditer(text)]


def _extract_command_terms(text: str) -> list[str]:
    return [match.group(0) for match in COMMAND_RE.finditer(text)]


def _matching_lines(lines: list[str], pattern: re.Pattern[str]) -> list[str]:
    return _dedupe([line.strip() for line in lines if pattern.search(line)])


def _term_rows(values: list[str], kind: str) -> list[ExtractedTermRecord]:
    return [ExtractedTermRecord(term=value, kind=kind) for value in _dedupe(values)]


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result
