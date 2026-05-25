"""Visible thought-leakage detection and cleanup helpers."""

from __future__ import annotations

from dataclasses import dataclass
import re

VISIBLE_THOUGHT_TAG_NAMES = (
    "think",
    "thinking",
    "thought",
    "analysis",
    "reasoning",
)
_VISIBLE_THOUGHT_TAG_RE = re.compile(
    r"</?\|?(?:" + "|".join(re.escape(name) for name in VISIBLE_THOUGHT_TAG_NAMES) + r")\|?>",
    re.IGNORECASE,
)
_VISIBLE_THOUGHT_LABEL_RE = re.compile(
    r"^(?:thinking|thought|analysis|reasoning|scratchpad)\s*:\s*",
    re.IGNORECASE,
)
_WHITESPACE_RE = re.compile(r"\s+")
_STRONG_META_PREFIXES = (
    "let me think",
    "lets think",
    "let's think",
    "let me",
    "i need to",
    "i should",
    "i will",
    "we need to",
    "we should",
    "the user wants",
    "the user asked",
    "the task is",
    "the task asks",
    "the instruction says",
    "to answer this",
    "to solve this",
)
_WEAK_META_PREFIXES = (
    "ok",
    "okay",
    "alright",
    "hmm",
    "wait",
    "here is",
    "here's",
)
_META_HINT_RE = re.compile(
    r"\b(?:"
    r"user|task|instruction|prompt|answer|output|return|requested|response|"
    r"json|yaml|table|command|format|payload|should|must|need|decide|"
    r"figure out|let's|lets"
    r")\b",
    re.IGNORECASE,
)
_CONDITIONAL_META_PREFIXES = (
    "first",
    "however",
    "but",
    "so",
    "next",
    "then",
)


@dataclass(frozen=True)
class VisibleThoughtLeakStats:
    """Counts and density for visible chain-of-thought leakage."""

    marker_count: int
    tag_marker_count: int
    prose_marker_count: int
    leaked_line_count: int
    leading_line_count: int
    leaked_char_count: int
    non_empty_line_count: int
    text_char_count: int

    @property
    def char_ratio(self) -> float:
        if self.text_char_count <= 0:
            return 0.0
        return self.leaked_char_count / self.text_char_count

    @property
    def line_ratio(self) -> float:
        if self.non_empty_line_count <= 0:
            return 0.0
        return self.leaked_line_count / self.non_empty_line_count

    @property
    def density(self) -> float:
        marker_ratio = min(1.0, self.marker_count / 5.0)
        weighted = (0.45 * self.char_ratio) + (0.35 * self.line_ratio) + (0.20 * marker_ratio)
        return max(self.char_ratio, min(1.0, weighted))

    @property
    def all_output_is_thought(self) -> bool:
        return self.marker_count > 0 and self.leading_line_count >= self.non_empty_line_count


def visible_thought_leak_stats(text: str) -> VisibleThoughtLeakStats:
    """Return visible thought leakage counts for one output string."""
    stripped = text.strip()
    if not stripped:
        return VisibleThoughtLeakStats(0, 0, 0, 0, 0, 0, 0, 0)

    lines = text.splitlines()
    thought_line_indexes: set[int] = set()
    prose_marker_count = 0
    tag_marker_count = len(_VISIBLE_THOUGHT_TAG_RE.findall(text))
    leading_line_count = 0
    seen_payload = False

    for index, raw_line in enumerate(lines):
        line = raw_line.strip()
        if not line:
            continue
        line_has_tag = _has_visible_thought_tag(line)
        line_is_meta = _looks_like_visible_thought_prose_line(line)
        if line_has_tag or line_is_meta:
            thought_line_indexes.add(index)
        if line_is_meta:
            prose_marker_count += 1
        if not seen_payload and (line_has_tag or line_is_meta):
            leading_line_count += 1
            continue
        if not line_has_tag and not line_is_meta:
            seen_payload = True

    leaked_char_count = sum(len(lines[index].strip()) for index in thought_line_indexes)
    non_empty_line_count = sum(1 for line in lines if line.strip())
    return VisibleThoughtLeakStats(
        marker_count=tag_marker_count + prose_marker_count,
        tag_marker_count=tag_marker_count,
        prose_marker_count=prose_marker_count,
        leaked_line_count=len(thought_line_indexes),
        leading_line_count=leading_line_count,
        leaked_char_count=leaked_char_count,
        non_empty_line_count=non_empty_line_count,
        text_char_count=len(stripped),
    )


def strip_leading_visible_thought_preamble(text: str) -> str:
    """Remove leading visible-thought prose when it is clearly extra scaffolding."""
    lines = text.splitlines()
    start_index = 0
    seen_marker = False
    while start_index < len(lines):
        line = lines[start_index].strip()
        if not line:
            start_index += 1
            continue
        if _has_visible_thought_tag(line) or _looks_like_visible_thought_prose_line(line):
            seen_marker = True
            start_index += 1
            continue
        break
    if not seen_marker:
        return text.strip()
    return "\n".join(lines[start_index:]).strip()


def _has_visible_thought_tag(line: str) -> bool:
    return _VISIBLE_THOUGHT_TAG_RE.search(_normalized_line(line)) is not None


def _looks_like_visible_thought_prose_line(line: str) -> bool:
    normalized = _normalized_line(line)
    if not normalized:
        return False
    if _VISIBLE_THOUGHT_LABEL_RE.match(normalized) is not None:
        return True
    if any(_starts_with_phrase(normalized, prefix) for prefix in _STRONG_META_PREFIXES):
        return True
    if "the user wants me to" in normalized:
        return True
    if any(_starts_with_phrase(normalized, prefix) for prefix in _WEAK_META_PREFIXES):
        return _contains_meta_hint(normalized)
    if any(_starts_with_phrase(normalized, prefix) for prefix in _CONDITIONAL_META_PREFIXES):
        return _contains_meta_hint(normalized)
    return False


def _starts_with_phrase(normalized: str, phrase: str) -> bool:
    if not normalized.startswith(phrase):
        return False
    if len(normalized) == len(phrase):
        return True
    return not normalized[len(phrase)].isalnum()


def _contains_meta_hint(normalized: str) -> bool:
    return _META_HINT_RE.search(normalized) is not None


def _normalized_line(line: str) -> str:
    return _WHITESPACE_RE.sub(" ", line.strip().casefold())
