"""Prompt building for compression backends."""

from __future__ import annotations

from ctxsift.models.base import ModelBackend, ModelCompressionInput

SYSTEM_PROMPT = """You compress coding command output for later recall.

Preserve exact filenames, symbols, error codes, test names, line numbers, and commands.
Do not invent facts or fixes.
Return concise plain text only.
"""


def build_messages(request: ModelCompressionInput) -> list[dict[str, object]]:
    """Build one chat message list for the local Gemma backend."""
    prompt = "\n".join(_prompt_sections(request))
    return [
        {
            "role": "system",
            "content": [ModelBackend.text_content(SYSTEM_PROMPT.strip())],
        },
        {
            "role": "user",
            "content": [ModelBackend.text_content(prompt)],
        },
    ]


def build_text_messages(request: ModelCompressionInput) -> list[dict[str, str]]:
    """Build a plain-text chat history for text-only local generation."""
    prompt = "\n".join(_prompt_sections(request))
    return [
        {"role": "system", "content": SYSTEM_PROMPT.strip()},
        {"role": "user", "content": prompt},
    ]


def _prompt_sections(request: ModelCompressionInput) -> list[str]:
    sections = [
        f"Instruction:\n{request.instruction}",
        _structured_signal_section(request),
        f"Raw input:\n```text\n{request.raw_input}\n```",
        (
            "Write a compact summary that keeps exact filenames, symbols, error codes, "
            "test names, line numbers, and commands unchanged."
        ),
    ]
    return sections


def _structured_signal_section(request: ModelCompressionInput) -> str:
    signal = request.extracted_signal
    lines: list[str] = ["Extracted signal:"]
    _append_signal(lines, "Domains", signal.matched_domains)
    _append_signal(lines, "Files", signal.referenced_files)
    _append_signal(lines, "Traceback frames", signal.traceback_frames)
    _append_signal(lines, "Tests", signal.tests)
    _append_signal(lines, "Packages", signal.packages)
    _append_signal(lines, "Symbols", signal.symbols)
    _append_signal(lines, "Commands", signal.command_terms)
    _append_signal(lines, "Exit code lines", signal.exit_code_lines)
    _append_signal(lines, "Warnings", signal.warning_lines)
    _append_signal(lines, "Errors", signal.error_lines)
    return "\n".join(lines)


def _append_signal(lines: list[str], label: str, values: list[str]) -> None:
    if not values:
        return
    lines.append(f"- {label}:")
    lines.extend(f"  - {value}" for value in values)
