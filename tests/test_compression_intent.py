"""Tests for explicit compression intent behavior."""

from __future__ import annotations

import pytest

from ctxsift.compression.intent import CompressionIntent
from ctxsift.compression.pipeline import build_exact_cache_key
from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.text_profile_common import (
    build_standard_text_messages,
    normalize_instruction_aware_output,
    validate_instruction_aware_output,
)
from ctxsift.types import ExtractedSignal


def _request(
    intent: CompressionIntent,
    *,
    instruction: str,
    raw_input: str = "alpha\nbeta\ngamma",
) -> ModelCompressionInput:
    return ModelCompressionInput(
        intent=intent,
        instruction=instruction,
        raw_input=raw_input,
        extracted_signal=ExtractedSignal(),
        max_output_tokens=64,
    )


def test_build_exact_cache_key_differs_by_intent() -> None:
    summary_key = build_exact_cache_key(
        workspace_root="/tmp/repo",
        raw_input_hash="raw-hash",
        normalized_instruction="summarize failures",
        intent=CompressionIntent.SUMMARY,
        model_id="model-id",
        max_output_tokens=128,
        ctxsift_version="0.1.0",
        prompt_version="prompt-v1",
    )
    recall_key = build_exact_cache_key(
        workspace_root="/tmp/repo",
        raw_input_hash="raw-hash",
        normalized_instruction="summarize failures",
        intent=CompressionIntent.RECALL,
        model_id="model-id",
        max_output_tokens=128,
        ctxsift_version="0.1.0",
        prompt_version="prompt-v1",
    )

    assert summary_key != recall_key


def test_recall_intent_uses_recall_oriented_prompt_wording() -> None:
    summary_messages = build_standard_text_messages(
        _request(
            CompressionIntent.SUMMARY,
            instruction="Summarize the failure.",
        )
    )
    recall_messages = build_standard_text_messages(
        _request(
            CompressionIntent.RECALL,
            instruction="Summarize the failure for later recall.",
        )
    )

    assert "optimized for later retrieval" not in summary_messages[1]["content"]
    assert "optimized for later retrieval" in recall_messages[1]["content"]


def test_exact_lines_rejects_reasoning_prose() -> None:
    validation = validate_instruction_aware_output(
        _request(
            CompressionIntent.EXACT_LINES,
            instruction="Return only the exact lines.",
            raw_input="FAILED test_api.py::test_login\nFAILED test_jobs.py::test_retry",
        ),
        "Okay, let's tackle this. FAILED test_api.py::test_login",
    )

    assert validation.status == "rejected"
    assert "exact_lines_contract_breakage" in validation.hard_fail_reasons


def test_exact_format_rejects_prose_wrapper() -> None:
    validation = validate_instruction_aware_output(
        _request(
            CompressionIntent.EXACT_FORMAT,
            instruction="Return only the requested command. No prose.",
            raw_input="kubectl delete pod bad-pod -n prod",
        ),
        "Here is the command: kubectl delete pod bad-pod -n prod",
    )

    assert validation.status == "rejected"
    assert "exact_format_contract_breakage" in validation.hard_fail_reasons


@pytest.mark.parametrize("wrapper_tag", ["think", "thinking", "thought"])
def test_normalization_strips_leaked_reasoning_wrappers(wrapper_tag: str) -> None:
    request = _request(
        CompressionIntent.SUMMARY,
        instruction="Summarize the failure for later recall.",
        raw_input="AuthError: login failed",
    )

    normalized = normalize_instruction_aware_output(
        request,
        f"<{wrapper_tag}>Okay, let's see.</{wrapper_tag}>AuthError: login failed",
    )

    assert normalized == "AuthError: login failed"
    assert validate_instruction_aware_output(request, normalized).status == "accepted"


@pytest.mark.parametrize(
    "raw_output",
    [
        "<think>Okay, let's see.",
        "<|thinking|>Okay, let's see.",
        "<|thought>Okay, let's see.",
    ],
)
def test_unterminated_reasoning_blocks_are_rejected(raw_output: str) -> None:
    request = _request(
        CompressionIntent.EXACT_FORMAT,
        instruction="Return only the requested command. No prose.",
        raw_input="kubectl delete pod bad-pod -n prod",
    )

    normalized = normalize_instruction_aware_output(request, raw_output)
    validation = validate_instruction_aware_output(request, normalized)

    assert normalized == raw_output
    assert validation.status == "rejected"
    assert "unterminated_reasoning_block" in validation.hard_fail_reasons


@pytest.mark.parametrize(
    ("intent", "instruction", "valid_output", "invalid_output"),
    [
        (
            CompressionIntent.JSON,
            "Return valid JSON only with keys file and line.",
            '{"file":"app.py","line":12}',
            "file=app.py line=12",
        ),
        (
            CompressionIntent.YAML,
            "Return YAML only with keys errors and file.",
            "errors:\n- file: app.py",
            "Here is the YAML:\nerrors:\n- file: app.py",
        ),
        (
            CompressionIntent.TABLE,
            "Return only the requested table.",
            "| file |\n| --- |\n| app.py |",
            "file\napp.py",
        ),
        (
            CompressionIntent.BULLET_LIST,
            "Return only the requested bullet list.",
            "- app.py\n- worker.py",
            "app.py\nworker.py",
        ),
    ],
)
def test_structured_intents_reject_wrong_shape(
    intent: CompressionIntent,
    instruction: str,
    valid_output: str,
    invalid_output: str,
) -> None:
    request = _request(intent, instruction=instruction)

    assert validate_instruction_aware_output(request, valid_output).status != "rejected"
    assert validate_instruction_aware_output(request, invalid_output).status == "rejected"
