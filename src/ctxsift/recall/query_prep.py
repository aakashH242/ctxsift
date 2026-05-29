"""High-signal vector query preparation for recall."""

from __future__ import annotations

from pathlib import Path
import re
import shlex

from ctxsift.extraction.signal import ExtractionContext, extract_signal
from ctxsift.shared.search_terms import search_terms
from ctxsift.types import ExtractedSignal

COMMAND_TERMS = {
    "ansible",
    "bash",
    "bundle",
    "bun",
    "cargo",
    "cmake",
    "compose",
    "ctxsift",
    "docker",
    "docker-compose",
    "fd",
    "find",
    "git",
    "go",
    "gofmt",
    "grep",
    "helm",
    "jest",
    "kubeadm",
    "kubectl",
    "kustomize",
    "make",
    "mvn",
    "mypy",
    "node",
    "nox",
    "npm",
    "npx",
    "pdm",
    "pip",
    "pip3",
    "pnpm",
    "poetry",
    "powershell",
    "py",
    "pytest",
    "python",
    "pwsh",
    "rails",
    "rake",
    "rg",
    "ripgrep",
    "rspec",
    "ruby",
    "ruff",
    "rustc",
    "rustup",
    "sed",
    "sh",
    "terraform",
    "tox",
    "uv",
    "vitest",
    "yarn",
    "zsh",
}
COMMAND_WITH_SUBCOMMAND = {
    "ansible",
    "bundle",
    "bun",
    "cargo",
    "cmake",
    "docker",
    "fd",
    "find",
    "git",
    "go",
    "helm",
    "jest",
    "kubeadm",
    "kubectl",
    "kustomize",
    "make",
    "mvn",
    "node",
    "nox",
    "npm",
    "npx",
    "pdm",
    "pip",
    "pip3",
    "pnpm",
    "poetry",
    "py",
    "pytest",
    "python",
    "rails",
    "rake",
    "rg",
    "ripgrep",
    "rspec",
    "ruby",
    "ruff",
    "rustup",
    "sed",
    "terraform",
    "tox",
    "uv",
    "vitest",
    "yarn",
}
AMBIGUOUS_COMMAND_TERMS = {"find", "go", "make"}
SCRIPT_SUFFIXES = (".bat", ".cmd", ".exe", ".ps1", ".py", ".rb", ".sh")
SUBCOMMAND_STOPWORDS = {"and", "for", "from", "in", "is", "of", "on", "or", "the", "to", "with"}
PATH_SUFFIXES = (
    ".cfg",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".ps1",
    ".py",
    ".pyi",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
)
POLITE_PREFIXES = (
    "please ",
    "can you ",
    "could you ",
    "would you ",
    "i need ",
    "need to ",
    "help me ",
    "help me figure out ",
    "figure out ",
)
REWRITE_CLAUSE_RE = re.compile(r"[.!?]\s+|\n+")
TOKEN_RE = re.compile(r"[^\s,;()]+")
STOPWORDS = {
    "a",
    "after",
    "and",
    "are",
    "but",
    "for",
    "from",
    "help",
    "how",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "later",
    "me",
    "my",
    "of",
    "on",
    "or",
    "please",
    "should",
    "so",
    "that",
    "the",
    "then",
    "this",
    "to",
    "use",
    "we",
    "when",
    "why",
    "with",
}
STRONG_SIGNAL_FIELDS = (
    "symbols",
    "tests",
    "referenced_files",
    "traceback_frames",
    "packages",
)
COMMAND_SIGNAL_FIELDS = ("command_terms",)
FALLBACK_SIGNAL_FIELDS = ("exit_code_lines", "error_lines")
MAX_SUMMARY_CHARS = 160
MAX_ANCHOR_CHARS = 96
LONG_QUERY_TERM_THRESHOLD = 12
LONG_QUERY_CHAR_THRESHOLD = 140


def prepare_vector_recall_query(
    query: str,
    *,
    cwd: Path,
    workspace_root: Path,
    anchor_term_limit: int,
) -> str:
    """Return a compact anchor-biased vector query for long natural-language recall asks."""
    if anchor_term_limit <= 0:
        return query
    normalized_query = _normalized_query(query)
    if not normalized_query:
        return query
    signal = extract_signal(
        normalized_query,
        ExtractionContext(cwd=cwd, workspace_root=workspace_root),
    )
    anchor_candidates = _signal_anchor_candidates(
        signal,
        anchor_term_limit=anchor_term_limit,
        limit=max(anchor_term_limit * 3, 6),
    )
    if not _should_rewrite_query(query, normalized_query, anchor_candidates):
        return query
    summary = compact_instruction_summary(normalized_query)
    selected_anchors = _summary_distinct_anchors(summary, anchor_candidates, anchor_term_limit)
    if not selected_anchors:
        return summary or query
    if not summary:
        return " ".join(selected_anchors)
    return f"{summary}. {' '.join(selected_anchors)}"


def compact_instruction_summary(query: str) -> str:
    """Trim a verbose recall request down to its first high-signal clause."""
    normalized = _normalized_query(query)
    if not normalized:
        return ""
    lowered = normalized.casefold()
    for prefix in POLITE_PREFIXES:
        if lowered.startswith(prefix):
            normalized = normalized[len(prefix) :].strip()
            break
    clauses = [
        segment.strip(" ,;:-") for segment in REWRITE_CLAUSE_RE.split(normalized) if segment.strip()
    ]
    summary = clauses[0] if clauses else normalized
    if len(summary) <= MAX_SUMMARY_CHARS:
        return summary
    truncated = summary[:MAX_SUMMARY_CHARS].rsplit(" ", 1)[0].strip()
    return truncated or summary[:MAX_SUMMARY_CHARS].strip()


def _normalized_query(query: str) -> str:
    return " ".join(query.strip().split())


def _should_rewrite_query(query: str, normalized_query: str, anchors: list[str]) -> bool:
    if not anchors:
        return False
    if "\n" in query:
        return True
    if len(normalized_query) > LONG_QUERY_CHAR_THRESHOLD:
        return True
    query_terms = search_terms(normalized_query)
    if len(query_terms) > LONG_QUERY_TERM_THRESHOLD:
        return True
    clauses = [segment for segment in REWRITE_CLAUSE_RE.split(normalized_query) if segment.strip()]
    return len(clauses) > 1 and len(query_terms) > 8


def _signal_anchor_candidates(
    signal: ExtractedSignal,
    *,
    anchor_term_limit: int,
    limit: int,
) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()
    command_confidence = _has_command_confidence(signal.command_terms)
    _extend_anchor_candidates(
        anchors,
        seen,
        signal=signal,
        fields=STRONG_SIGNAL_FIELDS,
        value_extractor=_strong_anchor_terms_from_value,
        limit=limit,
    )
    if len(anchors) < anchor_term_limit:
        _extend_anchor_candidates(
            anchors,
            seen,
            signal=signal,
            fields=COMMAND_SIGNAL_FIELDS,
            value_extractor=_command_anchor_terms_from_value,
            limit=limit,
        )
    if len(anchors) < anchor_term_limit:
        _extend_anchor_candidates(
            anchors,
            seen,
            signal=signal,
            fields=FALLBACK_SIGNAL_FIELDS,
            value_extractor=lambda value: _anchor_terms_from_value(
                value,
                include_commands=command_confidence,
            ),
            limit=limit,
        )
    return anchors


def _extend_anchor_candidates(
    anchors: list[str],
    seen: set[str],
    *,
    signal: ExtractedSignal,
    fields: tuple[str, ...],
    value_extractor,
    limit: int,
) -> None:
    for field_name in fields:
        for value in getattr(signal, field_name):
            for candidate in value_extractor(value):
                normalized_candidate = candidate.casefold()
                if not candidate or normalized_candidate in seen:
                    continue
                seen.add(normalized_candidate)
                anchors.append(candidate)
                if len(anchors) >= limit:
                    return


def _strong_anchor_terms_from_value(value: str) -> list[str]:
    candidate = value.strip()
    if not candidate:
        return []
    structured_candidates = _structured_anchor_substrings(candidate, include_commands=False)
    if structured_candidates:
        return structured_candidates
    if _looks_like_path(candidate) or _looks_like_symbol(candidate):
        return [candidate]
    return [term for term in search_terms(candidate) if _looks_like_strong_anchor_term(term)]


def _command_anchor_terms_from_value(value: str) -> list[str]:
    command_phrases = _command_phrase_candidates(value)
    if command_phrases:
        return command_phrases
    return [term for term in search_terms(value) if _is_confident_command_token(term)]


def _anchor_terms_from_value(value: str, *, include_commands: bool = True) -> list[str]:
    candidate = value.strip()
    if not candidate:
        return []
    command_phrases = _command_phrase_candidates(candidate) if include_commands else []
    structured_candidates = _structured_anchor_substrings(candidate, include_commands=False)
    if structured_candidates:
        if command_phrases:
            return [*structured_candidates, *command_phrases]
        return structured_candidates
    if _looks_like_anchor_span(candidate, include_commands=include_commands):
        if command_phrases:
            return command_phrases
        return [candidate]
    if command_phrases:
        return command_phrases
    return [
        term
        for term in search_terms(candidate)
        if _looks_like_anchor_term(term, include_commands=include_commands)
    ]


def _structured_anchor_substrings(value: str, *, include_commands: bool = True) -> list[str]:
    grouped_anchors: dict[str, list[str]] = {
        "symbol": [],
        "path": [],
        "command": [],
    }
    seen: set[str] = set()
    for match in TOKEN_RE.finditer(value):
        token = match.group(0).strip("\"'[]{}<>")
        if not token:
            continue
        normalized_token = token.casefold()
        if normalized_token in seen:
            continue
        seen.add(normalized_token)
        if _looks_like_symbol(token):
            grouped_anchors["symbol"].append(token)
            continue
        if _looks_like_path(token):
            grouped_anchors["path"].append(token)
            continue
        if include_commands and _looks_like_command(token):
            grouped_anchors["command"].append(token)
    return [
        *grouped_anchors["symbol"],
        *grouped_anchors["path"],
        *grouped_anchors["command"],
    ]


def _command_phrase_candidates(value: str) -> list[str]:
    tokens = _shell_tokens(value)
    if not tokens:
        return []
    for index, token in enumerate(tokens):
        executable = _normalized_executable(token)
        if not executable:
            continue
        if executable in AMBIGUOUS_COMMAND_TERMS and not _has_subcommand_hint(tokens, index):
            continue
        if not (_looks_like_script_token(token) or executable in COMMAND_TERMS):
            continue
        phrase = _command_phrase(tokens, index, executable)
        if phrase:
            return [phrase]
    return []


def _shell_tokens(value: str) -> list[str]:
    text = value.strip()
    if not text:
        return []
    for posix in (True, False):
        try:
            tokens = shlex.split(text, posix=posix)
        except ValueError:
            continue
        if tokens:
            return tokens
    return [token for token in re.split(r"\s+", text) if token]


def _normalized_executable(token: str) -> str:
    candidate = token.strip().strip("\"'")
    if not candidate:
        return ""
    candidate = candidate.replace("\\", "/").rsplit("/", 1)[-1]
    lowered = candidate.casefold()
    if lowered in {"python3", "python3.exe"}:
        return "python"
    if lowered.endswith(".exe"):
        lowered = lowered[:-4]
    return lowered


def _looks_like_script_token(token: str) -> bool:
    lowered = token.strip().strip("\"'").casefold()
    return lowered.endswith(SCRIPT_SUFFIXES) or lowered.startswith(("./", ".\\"))


def _has_subcommand_hint(tokens: list[str], index: int) -> bool:
    if index + 1 >= len(tokens):
        return False
    next_token = tokens[index + 1].strip().strip("\"'").casefold()
    if not next_token or next_token in SUBCOMMAND_STOPWORDS:
        return False
    return next_token.startswith("-") or next_token in COMMAND_WITH_SUBCOMMAND


def _command_phrase(tokens: list[str], index: int, executable: str) -> str:
    if executable in {"python", "py"} and index + 2 < len(tokens):
        second = tokens[index + 1].strip().casefold()
        third = tokens[index + 2].strip().strip("\"'")
        if second == "-m" and third:
            return f"{executable} -m {third}"
    if index + 1 < len(tokens):
        subcommand = tokens[index + 1].strip().strip("\"'").casefold()
        if subcommand and not subcommand.startswith("-") and subcommand not in SUBCOMMAND_STOPWORDS:
            return f"{executable} {subcommand}"
    return executable


def _summary_distinct_anchors(summary: str, anchors: list[str], limit: int) -> list[str]:
    selected: list[str] = []
    seen: set[str] = set()
    summary_casefold = summary.casefold()
    for anchor in anchors:
        normalized_anchor = anchor.casefold()
        if normalized_anchor in seen or normalized_anchor in summary_casefold:
            continue
        seen.add(normalized_anchor)
        selected.append(anchor)
        if len(selected) >= limit:
            return selected
    return selected


def _looks_like_anchor_span(value: str, *, include_commands: bool = True) -> bool:
    if len(value) > MAX_ANCHOR_CHARS:
        return False
    if _looks_like_path(value):
        return True
    if _looks_like_symbol(value):
        return True
    return include_commands and _looks_like_command(value)


def _looks_like_anchor_term(term: str, *, include_commands: bool = True) -> bool:
    if len(term) < 3 or term.isdigit() or term in STOPWORDS:
        return False
    if not include_commands and term.casefold() in COMMAND_TERMS:
        return False
    if _looks_like_path(term):
        return True
    if include_commands and _is_confident_command_token(term):
        return True
    if term.endswith(("error", "exception", "warning")):
        return True
    if any(character.isdigit() for character in term) and any(
        character.isalpha() for character in term
    ):
        return True
    if any(marker in term for marker in ("_", "-", ".", ":")):
        return True
    return len(term) >= 5


def _looks_like_path(value: str) -> bool:
    lowered = value.casefold()
    return "/" in value or "\\" in value or "::" in value or lowered.endswith(PATH_SUFFIXES)


def _looks_like_symbol(value: str) -> bool:
    if " " in value:
        return False
    return value.endswith(("Error", "Exception", "Warning")) or (
        any(character.isupper() for character in value[1:])
        and any(character.islower() for character in value)
    )


def _looks_like_command(value: str) -> bool:
    return bool(_command_phrase_candidates(value))


def _has_command_confidence(command_terms: list[str]) -> bool:
    for value in command_terms:
        if _command_phrase_candidates(value):
            return True
        if any(_is_confident_command_token(token) for token in search_terms(value)):
            return True
    return False


def _is_confident_command_token(token: str) -> bool:
    normalized = token.casefold()
    if normalized not in COMMAND_TERMS:
        return False
    return normalized not in AMBIGUOUS_COMMAND_TERMS


def _looks_like_strong_anchor_term(term: str) -> bool:
    if _looks_like_path(term):
        return True
    if _looks_like_symbol(term):
        return True
    lowered = term.casefold()
    return lowered.endswith(("error", "exception", "warning")) or "::" in term
