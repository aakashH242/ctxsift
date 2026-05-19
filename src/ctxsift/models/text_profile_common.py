"""Shared prompt, cleanup, and validation helpers for text-model profiles."""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Callable, Literal

from ctxsift.models.base import ModelCompressionInput


DEFAULT_SYSTEM_PROMPT = """You compress coding command output for later recall.

Follow the instruction carefully.
Do not invent causes or fixes.
Preserve exact filenames, symbols, error codes, test names, line numbers, and commands.
Do not add extra structure or explanation unless the instruction asks for it.
"""

CPU_PROTECTION_SYSTEM_PROMPT = """You compress coding command output on a small local CPU model.

Follow the instruction carefully.
Preserve exact filenames, symbols, error codes, test names, line numbers, and commands.
Do not invent causes or fixes.
"""

REPAIR_SYSTEM_PROMPT = """You are repairing an invalid compression summary.

Follow the instruction carefully.
Do not invent causes or fixes.
Preserve every required token exactly.
Do not add extra structure or explanation unless the instruction asks for it.
"""

CPU_PROTECTION_REPAIR_SYSTEM_PROMPT = """You are repairing an invalid CPU-mode compression result.

Follow the instruction carefully.
Preserve every required token exactly.
Do not invent causes or fixes.
"""

SCHEMA_LABELS = (
    "domains",
    "files",
    "traceback",
    "symbols",
    "commands",
    "errors",
    "packages",
    "tests",
    "warnings",
    "preserve exactly",
    "raw output",
    "task",
)

LEADING_HEADING_RE = re.compile(
    r"^(?:summary|result|failure summary|output summary)\s*:\s*",
    re.IGNORECASE,
)
STRUCTURED_LABEL_RE = re.compile(
    r"^(?:" + "|".join(re.escape(label) for label in SCHEMA_LABELS) + r")\s*:\s*$",
    re.IGNORECASE,
)
BULLET_LINE_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+")
SHORT_TAG_RE = re.compile(r"<[^>\n]{1,16}>")
WHITESPACE_RE = re.compile(r"[ \t]+")
MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
ROLE_TOKEN_LEAK_RE = re.compile(r"<\|(?:system|user|assistant)\|>", re.IGNORECASE)
CONTROL_TOKEN_LEAK_RE = re.compile(
    r"(<\|[^>\n]+\|>|</?(?:s|bos|eos|pad|unk|im_start|im_end|start_of_turn|end_of_turn|end_of_text|think|response)>|</?turn\|>|\[(?:/)?INST\])",
    re.IGNORECASE,
)
CONTROL_TOKEN_CLEAN_RE = re.compile(
    r"(<\|[^>\n]+\|>|</?(?:s|bos|eos|pad|unk|im_start|im_end|start_of_turn|end_of_turn|end_of_text|think|response)>|</?turn\|>|\[(?:/)?INST\])",
    re.IGNORECASE,
)
CPU_PROMPT_LABEL_RE = re.compile(
    r"^(?:instruction|output form|likely locus|preserve exactly|raw output|missing exact tokens that must appear verbatim)\s*:\s*",
    re.IGNORECASE,
)
CODE_BLOCK_RE = re.compile(r"^\s*```", re.MULTILINE)
HEADING_LINE_RE = re.compile(r"^\s{0,3}#{1,6}\s+\S", re.MULTILINE)
TABLE_LINE_RE = re.compile(r"^\s*\|.+\|\s*$", re.MULTILINE)
YAMLISH_LINE_RE = re.compile(r"^\s*[A-Za-z_][A-Za-z0-9_-]*:\s+\S", re.MULTILINE)
BENCHMARK_SCAFFOLD_RE = re.compile(
    r"^(?:here(?:'s| is)|below is)\b.*(?:instruction|output form|rewritten answer|requested output form|summary of the instruction)",
    re.IGNORECASE,
)

InstructionOutputMode = Literal["plain-text", "structured", "exact-lines", "exact-format"]
ValidationStatus = Literal["accepted", "soft_accepted", "rejected"]


@dataclass(frozen=True)
class TextValidationResult:
    """Structured validation result for one candidate model output."""

    status: ValidationStatus
    hard_fail_reasons: tuple[str, ...]
    quality_flags: tuple[str, ...]
    anchor_hits: int


@dataclass(frozen=True)
class RankedCandidate:
    """One normalized candidate output plus its validation result."""

    output: str
    validation: TextValidationResult


def build_standard_text_messages(
    request: ModelCompressionInput,
    *,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
) -> list[dict[str, str]]:
    """Build one conservative chat prompt for compression."""
    return [
        {"role": "system", "content": system_prompt.strip()},
        {"role": "user", "content": build_user_prompt(request)},
    ]


def build_user_prompt(request: ModelCompressionInput) -> str:
    """Build the shared user prompt with compact anchors and raw input."""
    sections = [
        f"Instruction:\n{request.instruction}",
        output_form_section(request),
        selection_discipline_section(request),
        build_anchor_section(request),
        f"Raw output:\n{request.raw_input}",
    ]
    return "\n\n".join(section for section in sections if section)


def build_cpu_protection_messages(request: ModelCompressionInput) -> list[dict[str, str]]:
    """Build one compact CPU-mode prompt that minimizes structural drift."""
    return [{"role": "user", "content": build_cpu_protection_user_prompt(request)}]


def build_cpu_protection_user_prompt(request: ModelCompressionInput) -> str:
    """Build a CPU-specific user prompt with explicit output-form rules."""
    sections = [
        f"Instruction:\n{request.instruction}",
        cpu_prompt_output_form_section(request),
        selection_discipline_section(request),
        build_cpu_signal_section(request),
        f"Raw output:\n{request.raw_input}",
    ]
    return "\n\n".join(section for section in sections if section)


def apply_soft_length_hint(
    messages: list[dict[str, str]],
    request: ModelCompressionInput,
) -> list[dict[str, str]]:
    """Append one soft length hint to the final user message."""
    if not messages:
        return messages
    updated_messages = [dict(message) for message in messages]
    hint = soft_length_hint_section(request)
    if not hint:
        return updated_messages
    for message in reversed(updated_messages):
        if message.get("role", "").strip().casefold() == "user":
            content = message.get("content", "").strip()
            message["content"] = f"{content}\n\n{hint}" if content else hint
            return updated_messages
    updated_messages[-1]["content"] = (
        f"{updated_messages[-1].get('content', '').strip()}\n\n{hint}".strip()
    )
    return updated_messages


def build_repair_messages(
    request: ModelCompressionInput,
    invalid_output: str,
) -> list[dict[str, str]]:
    """Build one shared repair prompt for invalid first-pass model output."""
    missing_anchors = [anchor for anchor in anchors_from_request(request) if anchor not in invalid_output]
    sections = [
        "Your previous answer was invalid for recall-oriented compression.",
        "Previous answer:",
        invalid_output.strip() or "(empty)",
    ]
    if missing_anchors:
        sections.extend(
            [
                "Missing exact tokens that must appear verbatim:",
                "\n".join(f"- {anchor}" for anchor in missing_anchors),
            ]
        )
    sections.extend(
        [
            output_form_section(request),
            selection_discipline_section(request),
            build_anchor_section(request),
            f"Raw output:\n{request.raw_input}",
            "Rewrite the answer so it follows the instruction carefully and preserves the required tokens.",
        ]
    )
    return [
        {"role": "system", "content": REPAIR_SYSTEM_PROMPT.strip()},
        {"role": "user", "content": "\n\n".join(section for section in sections if section)},
    ]


def build_cpu_protection_repair_messages(
    request: ModelCompressionInput,
    invalid_output: str,
) -> list[dict[str, str]]:
    """Build a CPU-mode repair prompt that preserves requested output structure."""
    missing_anchors = [anchor for anchor in cpu_anchors_from_request(request) if anchor not in invalid_output]
    sections = [
        "Your previous answer was invalid for CPU protection mode.",
        "Previous answer:",
        invalid_output.strip() or "(empty)",
        cpu_prompt_output_form_section(request),
    ]
    if missing_anchors:
        sections.extend(
            [
                "Missing exact tokens that must appear verbatim:",
                "\n".join(f"- {anchor}" for anchor in missing_anchors),
            ]
        )
    sections.extend(
        [
            build_cpu_signal_section(request),
            selection_discipline_section(request),
            f"Raw output:\n{request.raw_input}",
            "Rewrite the answer so it follows the instruction exactly and preserves the required tokens.",
        ]
    )
    return [
        {"role": "user", "content": "\n\n".join(section for section in sections if section)},
    ]


def build_anchor_section(request: ModelCompressionInput) -> str:
    """Build a compact exact-preservation section from extracted signal."""
    anchors = anchors_from_request(request)
    if not anchors:
        return ""
    bullet_lines = "\n".join(f"- {anchor}" for anchor in anchors)
    return f"Preserve exactly:\n{bullet_lines}"


def build_cpu_signal_section(request: ModelCompressionInput) -> str:
    """Build one compact CPU-specific hint block from extracted signal."""
    sections: list[str] = []
    likely_locus = likely_failing_locus_from_request(request)
    if likely_locus:
        sections.append(f"Likely locus:\n{likely_locus}")
    anchors = cpu_anchors_from_request(request)
    if anchors:
        bullet_lines = "\n".join(f"- {anchor}" for anchor in anchors)
        sections.append(f"Preserve exactly:\n{bullet_lines}")
    return "\n\n".join(sections)


def output_form_section(request: ModelCompressionInput) -> str:
    """Describe the allowed output form in an instruction-aware way."""
    instruction = request.instruction.casefold()
    if _requests_exact_lines(instruction):
        return (
            "Output form:\n"
            "- return the exact requested lines or quoted excerpts only\n"
            "- copy quoted or extracted lines exactly from the raw output\n"
            "- do not summarize unless the instruction also asks for it"
        )
    if _requests_exact_format(instruction):
        return (
            "Output form:\n"
            "- return only the requested value, command, identifier, or lines\n"
            "- no prose, labels, bullets, headings, code fences, or surrounding context\n"
            "- if the instruction implies one exact span, output only that span and nothing else"
        )
    if _requests_structured_output(instruction):
        return (
            "Output form:\n"
            "- follow the requested structure exactly\n"
            "- return only the requested json, yaml, table, or bullet structure\n"
            "- do not add prose before or after the structured output"
        )
    return (
        "Output form:\n"
        "- return a concise plain-text recall summary\n"
        "- avoid headings, bullets, markdown, or extra sections unless the instruction asks for them"
    )


def soft_length_hint_section(request: ModelCompressionInput) -> str:
    """Return one soft response-length hint tied to the configured max tokens."""
    return (
        "Length guidance:\n"
        "- keep the response concise\n"
        "- if the instruction requires exact quoted material or a longer structured answer, prioritize correctness instead"
    )


def selection_discipline_section(request: ModelCompressionInput) -> str:
    """Add one compact reminder when the instruction has strict include/exclude rules."""
    instruction = request.instruction.casefold()
    if not _requests_strict_selection(instruction):
        return ""
    return (
        "Selection discipline:\n"
        "- include only items that satisfy the instruction\n"
        "- omit related but out-of-scope items even if they look useful\n"
        "- if one short reason is requested, give only that reason"
    )


def cpu_output_form_section(request: ModelCompressionInput) -> str:
    """Backward-compatible CPU alias for shared output-form guidance."""
    return output_form_section(request)


def instruction_output_mode(instruction: str) -> InstructionOutputMode:
    """Classify which output contract an instruction is asking for."""
    normalized = instruction.casefold()
    if _requests_exact_lines(normalized):
        return "exact-lines"
    if _requests_exact_format(normalized):
        return "exact-format"
    if _requests_structured_output(normalized):
        return "structured"
    return "plain-text"


def cpu_prompt_output_form_section(request: ModelCompressionInput) -> str:
    """Return CPU output-form guidance only when the instruction explicitly needs it."""
    instruction = request.instruction.casefold()
    if (
        _requests_exact_lines(instruction)
        or _requests_exact_format(instruction)
        or _requests_structured_output(instruction)
    ):
        return output_form_section(request)
    return ""


def anchors_from_request(request: ModelCompressionInput) -> list[str]:
    """Return a compact ordered anchor list from deterministic extracted signal."""
    explicit_anchors = _explicit_anchors_from_request(request, limit=8)
    if explicit_anchors:
        return explicit_anchors
    signal = request.extracted_signal
    ordered_values = (
        signal.referenced_files,
        signal.traceback_frames,
        signal.tests,
        signal.symbols,
        signal.packages,
        signal.command_terms,
        signal.exit_code_lines,
        signal.error_lines,
    )
    anchors: list[str] = []
    seen: set[str] = set()
    for values in ordered_values:
        for value in values:
            candidate = value.strip()
            if not candidate or candidate in seen:
                continue
            seen.add(candidate)
            anchors.append(candidate)
            if len(anchors) == 8:
                return anchors
    return anchors


def cpu_anchors_from_request(request: ModelCompressionInput) -> list[str]:
    """Return a shorter anchor list for small CPU models."""
    explicit_anchors = _explicit_anchors_from_request(request, limit=4)
    if explicit_anchors:
        return explicit_anchors
    signal = request.extracted_signal
    ordered_values = (
        signal.referenced_files,
        signal.tests,
        signal.symbols,
        signal.error_lines,
        signal.traceback_frames,
        signal.command_terms,
        signal.exit_code_lines,
        signal.packages,
    )
    anchors: list[str] = []
    seen: set[str] = set()
    for values in ordered_values:
        for value in values:
            candidate = value.strip()
            if not candidate or candidate in seen:
                continue
            seen.add(candidate)
            anchors.append(candidate)
            if len(anchors) == 4:
                return anchors
    return anchors


def _explicit_anchors_from_request(request: ModelCompressionInput, *, limit: int) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()
    for value in request.required_anchors:
        candidate = value.strip()
        if not candidate or candidate in seen:
            continue
        seen.add(candidate)
        anchors.append(candidate)
        if len(anchors) == limit:
            break
    return anchors


def likely_failing_locus_from_request(request: ModelCompressionInput) -> str:
    """Return one compact likely-locus hint from deterministic extracted signal."""
    signal = request.extracted_signal
    locus_parts: list[str] = []

    primary_file = _first_non_empty(signal.referenced_files, signal.traceback_frames)
    if primary_file:
        locus_parts.append(primary_file)

    primary_test = _first_non_empty(signal.tests)
    if primary_test and primary_test not in locus_parts:
        locus_parts.append(primary_test)

    primary_symbol = _first_non_empty(signal.symbols)
    if primary_symbol and primary_symbol not in locus_parts:
        locus_parts.append(primary_symbol)

    primary_command = _first_non_empty(signal.command_terms)
    if primary_command:
        if locus_parts:
            return f"{' | '.join(locus_parts)} during {primary_command}"
        return f"during {primary_command}"

    return " | ".join(locus_parts)


def preserves_exact_anchors(request: ModelCompressionInput, text: str) -> bool:
    """Return whether the output preserves every extracted anchor verbatim."""
    anchors = anchors_from_request(request)
    if not anchors:
        return True
    return all(anchor in text for anchor in anchors)


def anchor_hit_count(request: ModelCompressionInput, text: str) -> int:
    """Return how many generic extracted anchors survived verbatim."""
    return sum(1 for anchor in anchors_from_request(request) if anchor in text)


def normalize_instruction_aware_output(request: ModelCompressionInput, text: str) -> str:
    """Normalize output without destroying instruction-required structure."""
    mode = instruction_output_mode(request.instruction)
    cleaned = text.strip()
    if not cleaned:
        return ""
    cleaned = strip_known_control_tokens(request, cleaned)
    if not cleaned:
        return ""
    if mode in {"exact-lines", "exact-format"}:
        return collapse_outer_blank_lines(cleaned)
    cleaned = strip_reasoning_blocks(cleaned, "think", "response")
    cleaned = strip_edge_tags(cleaned)
    cleaned = cleaned.strip()
    if not cleaned:
        return ""
    if mode == "structured":
        cleaned = strip_heading(cleaned)
        return collapse_outer_blank_lines(cleaned)
    return normalize_plain_output(cleaned)


def normalize_cpu_protection_output(request: ModelCompressionInput, text: str) -> str:
    """Normalize CPU output with extra cleanup for echoed prompt scaffolding."""
    normalized = normalize_instruction_aware_output(request, text)
    if not normalized:
        return ""
    instruction = request.instruction.casefold()
    if _requests_exact_lines(instruction) or _requests_structured_output(instruction):
        return normalized
    return strip_cpu_prompt_labels(normalized)


def normalize_profile_output(
    request_or_text: ModelCompressionInput | str,
    text: str | None = None,
) -> str:
    """Normalize profile output with optional backward-compatible request context."""
    if text is None:
        return normalize_plain_output(str(request_or_text))
    return normalize_instruction_aware_output(request_or_text, text)


def validate_instruction_aware_output(request: ModelCompressionInput, text: str) -> TextValidationResult:
    """Validate one normalized output against the shared instruction-first contract."""
    cleaned = text.strip()
    if not cleaned:
        return TextValidationResult(
            status="rejected",
            hard_fail_reasons=("empty_output",),
            quality_flags=(),
            anchor_hits=0,
        )

    hard_fail_reasons: list[str] = []
    if has_role_token_leakage(cleaned):
        hard_fail_reasons.append("role_token_leakage")
    if _has_unrepaired_control_token_leak(request, cleaned):
        hard_fail_reasons.append("control_token_leakage")
    if _has_unrepaired_schema_echo(request, cleaned):
        hard_fail_reasons.append("schema_echo")
    if _has_unrepaired_cpu_prompt_echo(request, cleaned):
        hard_fail_reasons.append("prompt_scaffold_echo")
    if _has_generic_prompt_guidance_echo(request, cleaned):
        hard_fail_reasons.append("prompt_scaffold_echo")

    hits = anchor_hit_count(request, cleaned)
    if hard_fail_reasons:
        return TextValidationResult(
            status="rejected",
            hard_fail_reasons=tuple(dict.fromkeys(hard_fail_reasons)),
            quality_flags=(),
            anchor_hits=hits,
        )

    quality_flags: list[str] = []
    anchors = anchors_from_request(request)
    if anchors and hits < len(anchors):
        quality_flags.append("missing_exact_anchors")

    mode = instruction_output_mode(request.instruction)
    if mode == "plain-text":
        if not is_plain_text_contract(cleaned):
            quality_flags.append("plain_text_style_mismatch")
    elif mode == "exact-format":
        if not _looks_like_exact_format_output(cleaned):
            quality_flags.append("exact_format_style_mismatch")
    elif mode == "structured":
        if not has_requested_structure(cleaned):
            quality_flags.append("structured_output_mismatch")
    else:
        if not looks_like_verbatim_excerpt(request, cleaned):
            quality_flags.append("verbatim_alignment_weak")

    status: ValidationStatus = "accepted" if not quality_flags else "soft_accepted"
    return TextValidationResult(
        status=status,
        hard_fail_reasons=(),
        quality_flags=tuple(dict.fromkeys(quality_flags)),
        anchor_hits=hits,
    )


def recover_scaffold_prefixed_output(
    request: ModelCompressionInput,
    text: str,
    *,
    normalize_output: Callable[[ModelCompressionInput, str], str] | None = None,
) -> str:
    """Best-effort scaffold-echo recovery before validation."""
    cleaned = text.strip()
    if not cleaned:
        return cleaned
    if not _should_attempt_scaffold_recovery(request, cleaned):
        return cleaned
    normalizer = normalize_output or normalize_instruction_aware_output
    if request.evaluation_context == "benchmark":
        candidates = _benchmark_recovery_candidates(
            request,
            cleaned,
            normalize_output=normalizer,
        )
    else:
        candidates = _prod_recovery_candidates(
            request,
            cleaned,
            normalize_output=normalizer,
        )
    best = min(candidates, key=lambda candidate: _scaffold_recovery_rank(request, candidate))
    original_rank = _scaffold_recovery_rank(request, cleaned)
    if _scaffold_recovery_rank(request, best) < original_rank:
        return best
    return cleaned


def choose_preferred_candidate(
    request: ModelCompressionInput,
    candidates: list[str],
) -> RankedCandidate | None:
    """Return the highest-ranked non-rejected candidate, if any."""
    ranked_candidates = [
        RankedCandidate(output=candidate, validation=validate_instruction_aware_output(request, candidate))
        for candidate in candidates
        if candidate.strip()
    ]
    usable = [candidate for candidate in ranked_candidates if candidate.validation.status != "rejected"]
    if not usable:
        return None
    return min(
        usable,
        key=lambda candidate: _candidate_rank(request, candidate),
    )


def should_attempt_repair(validation: TextValidationResult) -> bool:
    """Return whether one candidate should get a repair retry."""
    return validation.status != "accepted"


def is_valid_instruction_aware_output(
    request: ModelCompressionInput,
    text: str,
    *,
    require_exact_anchors: bool = False,
) -> bool:
    """Backward-compatible boolean view of the shared validator."""
    validation = validate_instruction_aware_output(request, text)
    if validation.status == "rejected":
        return False
    if require_exact_anchors:
        return preserves_exact_anchors(request, text)
    return True


def is_valid_cpu_protection_output(request: ModelCompressionInput, text: str) -> bool:
    """Backward-compatible CPU alias for the shared instruction-aware validator."""
    return validate_instruction_aware_output(request, text).status != "rejected"


def deterministic_generation_kwargs(tokenizer: object, max_output_tokens: int) -> dict[str, int | bool]:
    """Return one conservative deterministic generation config."""
    kwargs: dict[str, int | bool] = {
        "do_sample": False,
        "max_new_tokens": max_output_tokens,
    }
    pad_token_id = getattr(tokenizer, "pad_token_id", None)
    eos_token_id = getattr(tokenizer, "eos_token_id", None)
    if pad_token_id is not None:
        kwargs["pad_token_id"] = int(pad_token_id)
    if eos_token_id is not None:
        kwargs["eos_token_id"] = int(eos_token_id)
    return kwargs


def normalize_plain_output(text: str) -> str:
    """Apply shared edge cleanup for compression output."""
    cleaned = text.strip()
    cleaned = strip_edge_tags(cleaned)
    cleaned = strip_heading(cleaned)
    cleaned = strip_bullets(cleaned)
    return collapse_blank_lines(cleaned)


def strip_reasoning_blocks(text: str, *tag_names: str) -> str:
    """Strip simple XML-like reasoning blocks that some chat models leak."""
    cleaned = text
    for tag_name in tag_names:
        pattern = re.compile(
            rf"<{re.escape(tag_name)}>\s*.*?\s*</{re.escape(tag_name)}>",
            re.IGNORECASE | re.DOTALL,
        )
        cleaned = pattern.sub("", cleaned)
    return cleaned.strip()


def strip_edge_tags(text: str) -> str:
    """Strip short model-leaked tags from the outer edges of the output."""
    cleaned = text
    while True:
        updated = re.sub(
            r"^\s*<(?!\|(?:system|user|assistant)\|)(?!/?(?:image|video|audio)\b)[^>\n]{1,16}>\s*",
            "",
            cleaned,
            count=1,
        )
        updated = re.sub(
            r"\s*<(?!\|(?:system|user|assistant)\|)(?!/?(?:image|video|audio)\b)[^>\n]{1,16}>\s*$",
            "",
            updated,
            count=1,
        )
        updated = updated.strip()
        if updated == cleaned:
            return cleaned
        cleaned = updated


def strip_known_control_tokens(request: ModelCompressionInput, text: str) -> str:
    """Strip known model control tokens unless they are part of the raw input itself."""
    raw_input = request.raw_input

    def _replace(match: re.Match[str]) -> str:
        token = match.group(0)
        if token in raw_input:
            return token
        return " "

    cleaned = CONTROL_TOKEN_CLEAN_RE.sub(_replace, text)
    cleaned = WHITESPACE_RE.sub(" ", cleaned)
    cleaned = re.sub(r"\n[ \t]+", "\n", cleaned)
    return cleaned.strip()


def strip_heading(text: str) -> str:
    """Strip one leading summary-style heading."""
    return LEADING_HEADING_RE.sub("", text, count=1).strip()


def strip_bullets(text: str) -> str:
    """Strip simple list bullets from each line."""
    lines = []
    for line in text.splitlines():
        lines.append(BULLET_LINE_RE.sub("", line, count=1))
    return "\n".join(lines).strip()


def collapse_blank_lines(text: str) -> str:
    """Normalize whitespace while keeping sentence structure intact."""
    lines = [WHITESPACE_RE.sub(" ", line).strip() for line in text.splitlines()]
    normalized = "\n".join(line for line in lines if line)
    normalized = MULTI_NEWLINE_RE.sub("\n\n", normalized)
    return normalized.strip()


def collapse_outer_blank_lines(text: str) -> str:
    """Trim outer blank lines while preserving internal formatting."""
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines).strip()


def is_plain_text_contract(text: str) -> bool:
    """Return whether the output still satisfies the shared formatting contract."""
    if not text.strip():
        return False
    if SHORT_TAG_RE.search(text):
        return False
    if LEADING_HEADING_RE.match(text):
        return False
    if STRUCTURED_LABEL_RE.search(text):
        return False
    if any(BULLET_LINE_RE.match(line) for line in text.splitlines() if line.strip()):
        return False
    return True


def has_structured_schema_leakage(text: str) -> bool:
    """Return whether output still looks like echoed schema labels."""
    return any(STRUCTURED_LABEL_RE.match(line) for line in text.splitlines() if line.strip())


def has_role_token_leakage(text: str) -> bool:
    """Return whether output still contains chat role control tokens."""
    return ROLE_TOKEN_LEAK_RE.search(text) is not None


def strip_cpu_prompt_labels(text: str) -> str:
    """Strip echoed CPU prompt labels from the start of lines."""
    lines = []
    for line in text.splitlines():
        lines.append(CPU_PROMPT_LABEL_RE.sub("", line, count=1))
    cleaned = "\n".join(lines).strip()
    return collapse_blank_lines(cleaned)


def has_cpu_prompt_scaffold_leakage(text: str) -> bool:
    """Return whether CPU output still obviously echoes prompt scaffolding."""
    return any(CPU_PROMPT_LABEL_RE.match(line) for line in text.splitlines() if line.strip())


def has_requested_structure(text: str) -> bool:
    """Return whether the output contains one requested structured form."""
    stripped = text.strip()
    if not stripped:
        return False
    if stripped.startswith("```") and stripped.endswith("```"):
        return True
    if (stripped.startswith("{") and stripped.endswith("}")) or (
        stripped.startswith("[") and stripped.endswith("]")
    ):
        return True
    lines = [line for line in text.splitlines() if line.strip()]
    if any(BULLET_LINE_RE.match(line) for line in lines):
        return True
    if any(HEADING_LINE_RE.match(line) for line in lines):
        return True
    if any(TABLE_LINE_RE.match(line) for line in lines):
        return True
    yaml_line_count = sum(1 for line in lines if YAMLISH_LINE_RE.match(line))
    return yaml_line_count >= 2


def looks_like_verbatim_excerpt(request: ModelCompressionInput, text: str) -> bool:
    """Return whether the output plausibly preserves requested verbatim lines."""
    return _verbatim_excerpt_ratio(request, text) >= _required_verbatim_excerpt_ratio(request, text)


def _verbatim_excerpt_ratio(request: ModelCompressionInput, text: str) -> float:
    """Return how much of the output lines match raw-input lines verbatim."""
    output_lines = [
        normalized
        for line in text.splitlines()
        if (normalized := _normalize_verbatim_line(line))
    ]
    if not output_lines:
        return 0.0
    raw_lines = {
        normalized
        for line in request.raw_input.splitlines()
        if (normalized := _normalize_verbatim_line(line))
    }
    if not raw_lines:
        return 0.0
    matched_lines = sum(1 for line in output_lines if line in raw_lines)
    return matched_lines / len(output_lines)


def _required_verbatim_excerpt_ratio(request: ModelCompressionInput, text: str) -> float:
    del request
    return 1.0 if text.strip() else 0.0


def validation_flags(validation: TextValidationResult) -> tuple[str, ...]:
    """Return the user-facing flags for one validation result."""
    if validation.status == "rejected":
        return validation.hard_fail_reasons
    return validation.quality_flags


def _requests_exact_lines(instruction: str) -> bool:
    return any(
        token in instruction
        for token in (
            "quote exactly",
            "quote the",
            "verbatim",
            "exact lines",
            "exact line",
            "first 8 lines",
            "first 5 lines",
            "next 5 lines",
            "copy the lines",
            "extract the lines",
        )
    )


def _requests_exact_format(instruction: str) -> bool:
    return any(
        token in instruction
        for token in (
            "output exactly the requested value or lines",
            "exact match or regex-constrained output required",
            "no prose, bullets, backticks, or extra whitespace",
            "return only the requested value",
            "return only the requested command",
        )
    )


def _requests_structured_output(instruction: str) -> bool:
    return any(
        token in instruction
        for token in (
            "bullet",
            "bullets",
            "list",
            "markdown",
            "code block",
            "table",
            "json",
            "yaml",
            "return only the requested structured output",
            "heading",
            "headings",
        )
    )


def _requests_strict_selection(instruction: str) -> bool:
    return any(
        token in instruction
        for token in (
            "return only",
            "include only",
            "output only",
            "exclude ",
            "omit ",
            "do not include",
            "security-sensitive changed files",
        )
    )


def _looks_like_exact_format_output(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if "```" in stripped:
        return False
    if LEADING_HEADING_RE.match(stripped):
        return False
    if any(BULLET_LINE_RE.match(line) for line in stripped.splitlines() if line.strip()):
        return False
    if stripped.count("\n") > 4:
        return False
    return True


def _first_non_empty(*value_groups: list[str]) -> str:
    for values in value_groups:
        for value in values:
            candidate = value.strip()
            if candidate:
                return candidate
    return ""


def _candidate_rank(request: ModelCompressionInput, candidate: RankedCandidate) -> tuple[int, int, int, int]:
    status_rank = 0 if candidate.validation.status == "accepted" else 1
    concise_rank = len(candidate.output) if instruction_output_mode(request.instruction) == "plain-text" else 0
    return (
        status_rank,
        -candidate.validation.anchor_hits,
        len(candidate.validation.quality_flags),
        concise_rank,
    )


def _benchmark_recovery_candidates(
    request: ModelCompressionInput,
    text: str,
    *,
    normalize_output: Callable[[ModelCompressionInput, str], str],
) -> list[str]:
    candidates: list[str] = []
    for candidate in (
        text,
        _strip_prompt_wrapper_lines(request, text),
        _trim_to_first_anchor(text, anchors_from_request(request)),
        _trim_to_first_raw_line(request, text),
        _trim_to_first_anchor(_strip_prompt_wrapper_lines(request, text), anchors_from_request(request)),
        _trim_to_first_raw_line(request, _strip_prompt_wrapper_lines(request, text)),
    ):
        normalized = normalize_output(request, candidate)
        if not normalized or normalized in candidates:
            continue
        candidates.append(normalized)
    return candidates or [text]


def _prod_recovery_candidates(
    request: ModelCompressionInput,
    text: str,
    *,
    normalize_output: Callable[[ModelCompressionInput, str], str],
) -> list[str]:
    candidates: list[str] = []
    for candidate in (
        text,
        _strip_prompt_wrapper_lines(request, text),
    ):
        normalized = normalize_output(request, candidate)
        if not normalized or normalized in candidates:
            continue
        candidates.append(normalized)
    return candidates or [text]


def _scaffold_recovery_rank(request: ModelCompressionInput, text: str) -> tuple[int, int, int, int, int]:
    scaffold_penalty = int(_has_unrepaired_schema_echo(request, text)) + int(
        _has_unrepaired_cpu_prompt_echo(request, text)
    ) + int(_has_generic_prompt_guidance_echo(request, text))
    leading_penalty = int(_looks_like_scaffold_lead(text))
    mode = instruction_output_mode(request.instruction)
    mode_bonus = 0
    if mode == "exact-lines":
        mode_bonus = -int(_verbatim_excerpt_ratio(request, text) * 1000)
    elif mode == "structured":
        mode_bonus = -int(has_requested_structure(text))
    else:
        mode_bonus = -int(is_plain_text_contract(text))
    return (
        scaffold_penalty,
        leading_penalty,
        -anchor_hit_count(request, text),
        mode_bonus,
        len(text),
    )


def _should_attempt_scaffold_recovery(request: ModelCompressionInput, text: str) -> bool:
    return any(
        (
            _has_unrepaired_schema_echo(request, text),
            _has_unrepaired_cpu_prompt_echo(request, text),
            _has_generic_prompt_guidance_echo(request, text),
            _looks_like_scaffold_lead(text),
        )
    )


def _normalize_verbatim_line(line: str) -> str:
    cleaned = line.strip()
    if cleaned.startswith(">"):
        cleaned = cleaned[1:].strip()
    if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {'"', "'", "`"}:
        cleaned = cleaned[1:-1].strip()
    return cleaned


def _strip_prompt_wrapper_lines(request: ModelCompressionInput, text: str) -> str:
    mode = instruction_output_mode(request.instruction)
    raw_lines = {line.strip().casefold() for line in request.raw_input.splitlines() if line.strip()}
    normalized_raw_lines = {_normalized_guidance_line(line) for line in request.raw_input.splitlines() if line.strip()}
    cleaned_lines: list[str] = []
    inside_wrapper_block = False
    for line in text.splitlines():
        stripped = line.strip()
        lowered = _normalized_guidance_line(stripped)
        if not stripped:
            inside_wrapper_block = False
            continue
        if lowered == "raw output:":
            inside_wrapper_block = False
            continue
        if lowered in raw_lines:
            inside_wrapper_block = False
            cleaned_lines.append(stripped)
            continue
        if lowered in normalized_raw_lines:
            inside_wrapper_block = False
            cleaned_lines.append(stripped)
            continue
        if inside_wrapper_block:
            continue
        if _is_prompt_wrapper_label(request, stripped, mode=mode) or CPU_PROMPT_LABEL_RE.match(stripped):
            inside_wrapper_block = True
            continue
        if (lowered in _guidance_lines() or _is_soft_length_guidance_line(lowered)) and lowered not in normalized_raw_lines:
            inside_wrapper_block = True
            continue
        if BENCHMARK_SCAFFOLD_RE.match(stripped):
            continue
        cleaned_lines.append(stripped)
    return "\n".join(cleaned_lines).strip()


def _trim_to_first_anchor(text: str, anchors: list[str]) -> str:
    matches = [text.find(anchor) for anchor in anchors if anchor and text.find(anchor) >= 0]
    if not matches:
        return text
    return text[min(matches):].strip()


def _trim_to_first_raw_line(request: ModelCompressionInput, text: str) -> str:
    candidates = [line.strip() for line in request.raw_input.splitlines() if line.strip()]
    indexed = [(text.find(line), line) for line in candidates if len(line) >= 8 and text.find(line) >= 0]
    if not indexed:
        return text
    position, line = min(indexed, key=lambda item: item[0])
    return text[position:].strip() if position >= 0 else line


def _has_unrepaired_schema_echo(request: ModelCompressionInput, text: str) -> bool:
    mode = instruction_output_mode(request.instruction)
    suspect_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and _is_prompt_wrapper_label(request, line.strip(), mode=mode)
    ]
    if not suspect_lines:
        return False
    raw_lines = {line.strip() for line in request.raw_input.splitlines() if line.strip()}
    return any(line not in raw_lines for line in suspect_lines)


def _has_unrepaired_cpu_prompt_echo(request: ModelCompressionInput, text: str) -> bool:
    suspect_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and CPU_PROMPT_LABEL_RE.match(line)
    ]
    if not suspect_lines:
        return False
    raw_lines = {line.strip() for line in request.raw_input.splitlines() if line.strip()}
    return any(line not in raw_lines for line in suspect_lines)


def _has_unrepaired_control_token_leak(request: ModelCompressionInput, text: str) -> bool:
    raw_input = request.raw_input
    for match in CONTROL_TOKEN_LEAK_RE.finditer(text):
        token = match.group(0)
        if token not in raw_input:
            return True
    return False


def _has_generic_prompt_guidance_echo(request: ModelCompressionInput, text: str) -> bool:
    raw_lines = {_normalized_guidance_line(line) for line in request.raw_input.splitlines() if line.strip()}
    guidance_lines = _guidance_lines()
    for line in text.splitlines():
        candidate = _normalized_guidance_line(line)
        if not candidate:
            continue
        if (candidate in guidance_lines or _is_soft_length_guidance_line(candidate)) and candidate not in raw_lines:
            return True
    return False


def _is_prompt_wrapper_label(
    request: ModelCompressionInput,
    line: str,
    *,
    mode: InstructionOutputMode | None = None,
) -> bool:
    normalized_mode = mode or instruction_output_mode(request.instruction)
    stripped = line.strip()
    if not STRUCTURED_LABEL_RE.match(stripped):
        return False
    lowered = stripped.casefold()
    if normalized_mode != "structured":
        return True
    return lowered in {
        "domains:",
        "traceback:",
        "symbols:",
        "commands:",
        "packages:",
        "preserve exactly:",
        "raw output:",
        "task:",
    }


def _guidance_lines() -> set[str]:
    return {
        "length guidance:",
        "follow the instruction carefully.",
        "do not invent causes or fixes.",
        "return a concise plain-text recall summary",
        "avoid headings, bullets, markdown, or extra sections unless the instruction asks for them",
        "return the exact requested lines or quoted excerpts only",
        "copy quoted or extracted lines exactly from the raw output",
        "do not summarize unless the instruction also asks for it",
        "follow the requested structure exactly",
        "do not add extra sections that were not requested",
        "if the instruction requires exact quoted material or a longer structured answer, prioritize correctness instead",
    }


def _looks_like_scaffold_lead(text: str) -> bool:
    first_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if not first_line:
        return False
    lowered = first_line.casefold()
    return bool(
        BENCHMARK_SCAFFOLD_RE.match(first_line)
        or lowered.startswith("instruction:")
        or lowered.startswith("output form:")
        or lowered.startswith("preserve exactly:")
        or lowered.startswith("raw output:")
        or lowered.startswith("length guidance:")
    )


def _normalized_guidance_line(line: str) -> str:
    normalized = BULLET_LINE_RE.sub("", line.strip(), count=1)
    return WHITESPACE_RE.sub(" ", normalized).strip().casefold()


def _is_soft_length_guidance_line(line: str) -> bool:
    return line == "keep the response concise"
