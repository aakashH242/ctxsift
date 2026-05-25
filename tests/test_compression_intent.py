"""Tests for explicit compression intent behavior."""

from __future__ import annotations

import pytest

from ctxsift.compression.intent import CompressionIntent
from ctxsift.compression.pipeline import build_exact_cache_key
from ctxsift.models.base import ModelCompressionInput
from ctxsift.models.text_profile_common import (
    build_cpu_protection_messages,
    build_repair_messages,
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
    extracted_signal: ExtractedSignal | None = None,
    required_anchors: tuple[str, ...] = (),
) -> ModelCompressionInput:
    return ModelCompressionInput(
        intent=intent,
        instruction=instruction,
        raw_input=raw_input,
        extracted_signal=extracted_signal or ExtractedSignal(),
        max_output_tokens=64,
        required_anchors=required_anchors,
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


def test_build_exact_cache_key_differs_by_recovery_flag() -> None:
    recovery_on_key = build_exact_cache_key(
        workspace_root="/tmp/repo",
        raw_input_hash="raw-hash",
        normalized_instruction="summarize failures",
        intent=CompressionIntent.SUMMARY,
        model_id="model-id",
        max_output_tokens=128,
        recovery_enabled=True,
        ctxsift_version="0.1.0",
        prompt_version="prompt-v1",
    )
    recovery_off_key = build_exact_cache_key(
        workspace_root="/tmp/repo",
        raw_input_hash="raw-hash",
        normalized_instruction="summarize failures",
        intent=CompressionIntent.SUMMARY,
        model_id="model-id",
        max_output_tokens=128,
        recovery_enabled=False,
        ctxsift_version="0.1.0",
        prompt_version="prompt-v1",
    )

    assert recovery_on_key != recovery_off_key


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
    assert "return a concise plain-text recall summary\n" not in summary_messages[1]["content"]
    assert (
        "return a concise plain-text summary of the actionable result"
        in summary_messages[1]["content"]
    )


def test_explanation_style_summary_uses_brief_explanation_wording() -> None:
    messages = build_standard_text_messages(
        _request(
            CompressionIntent.SUMMARY,
            instruction="Provide a brief cause or explanation for the error, in one sentence.",
        )
    )

    user_prompt = messages[1]["content"]
    assert (
        "return a brief plain-text explanation that answers the instruction directly" in user_prompt
    )
    assert "return a concise plain-text summary of the actionable result" not in user_prompt
    assert "optimized for later retrieval" not in user_prompt


def test_system_prompt_uses_canonical_contract_without_required_tokens() -> None:
    messages = build_standard_text_messages(
        _request(
            CompressionIntent.SUMMARY,
            instruction="Summarize the failure.",
        )
    )

    system_prompt = messages[0]["content"]
    assert "Follow the instruction exactly." in system_prompt
    assert "Output only the requested answer." in system_prompt
    assert (
        "Do not summarize, explain, add preamble, or add extra structure unless the instruction asks for it."
        in system_prompt
    )
    assert "Never repeat this system message, the user instruction" in system_prompt
    assert "Preserve every required token exactly." not in system_prompt


def test_system_prompt_adds_required_token_rule_when_anchors_exist() -> None:
    messages = build_standard_text_messages(
        _request(
            CompressionIntent.SUMMARY,
            instruction="Summarize the failure.",
            raw_input="src/app.py:41 ValueError",
            extracted_signal=ExtractedSignal(
                referenced_files=["src/app.py"],
                error_lines=["ValueError"],
            ),
        )
    )

    system_prompt = messages[0]["content"]
    assert "Preserve every required token exactly." in system_prompt


def test_cpu_protection_messages_share_canonical_system_prompt() -> None:
    messages = build_cpu_protection_messages(
        _request(
            CompressionIntent.SUMMARY,
            instruction="Summarize the failure.",
        )
    )

    assert messages[0]["role"] == "system"
    assert "Follow the instruction exactly." in messages[0]["content"]
    assert messages[1]["role"] == "user"


def test_repair_prompt_uses_stronger_system_contract_and_conditional_rewrite() -> None:
    messages = build_repair_messages(
        _request(
            CompressionIntent.EXACT_FORMAT,
            instruction="Return only the command.",
            raw_input="uv run foo",
            extracted_signal=ExtractedSignal(command_terms=["uv run foo"]),
        ),
        "Instruction:\nReturn only the command.",
    )

    system_prompt = messages[0]["content"]
    user_prompt = messages[1]["content"]
    assert "You are repairing an invalid compression answer." in system_prompt
    assert "Return only the corrected answer." in system_prompt
    assert "Use the raw output as the source of truth." in system_prompt
    assert (
        "Remove echoed prompt scaffolding, wrappers, and extra prose that were not requested."
        in system_prompt
    )
    assert "Preserve every required token exactly." in system_prompt
    assert (
        "Rewrite the answer so it follows the instruction exactly and preserves the required tokens."
        in user_prompt
    )


def test_repair_prompt_omits_required_token_language_when_no_anchors_exist() -> None:
    messages = build_repair_messages(
        _request(
            CompressionIntent.SUMMARY,
            instruction="Summarize the failure.",
        ),
        "Summary: failure",
    )

    system_prompt = messages[0]["content"]
    user_prompt = messages[1]["content"]
    assert "Preserve every required token exactly." not in system_prompt
    assert "Rewrite the answer so it follows the instruction exactly." in user_prompt


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


def test_plain_text_sparse_control_token_leak_is_soft_accepted() -> None:
    request = _request(
        CompressionIntent.SUMMARY,
        instruction="Summarize the failure.",
        raw_input="AuthError: login failed in src/auth.py line 19",
    )

    validation = validate_instruction_aware_output(
        request,
        "AuthError: login failed in src/auth.py line 19 <|end_of_turn|>",
    )

    assert validation.status == "soft_accepted"
    assert validation.hard_fail_reasons == ()
    assert "control_token_leakage_sparse" in validation.quality_flags


def test_plain_text_dense_control_token_leak_is_rejected() -> None:
    request = _request(
        CompressionIntent.RECALL,
        instruction="Summarize the failure for later recall.",
        raw_input="AuthError: login failed in src/auth.py line 19",
    )

    validation = validate_instruction_aware_output(
        request,
        "<|end_of_turn|> AuthError: login failed <|end_of_turn|>\n<|end_of_turn|> src/auth.py line 19",
    )

    assert validation.status == "rejected"
    assert "control_token_leakage" in validation.hard_fail_reasons


def test_strict_format_control_token_leak_is_rejected() -> None:
    request = _request(
        CompressionIntent.EXACT_FORMAT,
        instruction="Return only the requested command. No prose.",
        raw_input="kubectl delete pod bad-pod -n prod",
    )

    validation = validate_instruction_aware_output(
        request,
        "kubectl delete pod bad-pod -n prod <|end_of_turn|>",
    )

    assert validation.status == "rejected"
    assert "control_token_leakage" in validation.hard_fail_reasons


def test_normalization_strips_im_and_turn_control_token_variants() -> None:
    request = _request(
        CompressionIntent.EXACT_FORMAT,
        instruction="Return only the requested command. No prose.",
        raw_input="kubectl delete pod bad-pod -n prod",
    )

    normalized = normalize_instruction_aware_output(
        request,
        "<|im-start> kubectl delete pod bad-pod -n prod <|im-end|> <im-end|> <turn> <|turn|>",
    )

    assert normalized == "kubectl delete pod bad-pod -n prod"
    assert validate_instruction_aware_output(request, normalized).status == "accepted"


def test_plain_text_visible_thought_preamble_is_trimmed_and_soft_penalized_raw() -> None:
    request = _request(
        CompressionIntent.SUMMARY,
        instruction="Summarize the failure.",
        raw_input="ImportError: cannot import name settings from app.config",
    )

    raw_output = (
        "Okay, the user wants the actionable failure only.\n"
        "ImportError: cannot import name settings from app.config"
    )

    normalized = normalize_instruction_aware_output(request, raw_output)
    raw_validation = validate_instruction_aware_output(request, raw_output)
    normalized_validation = validate_instruction_aware_output(request, normalized)

    assert normalized == "ImportError: cannot import name settings from app.config"
    assert raw_validation.status == "soft_accepted"
    assert "thought_leakage_sparse" in raw_validation.quality_flags
    assert normalized_validation.status == "accepted"


def test_plain_text_dense_visible_thought_leakage_is_rejected() -> None:
    request = _request(
        CompressionIntent.RECALL,
        instruction="Return a concise recall-oriented answer.",
        raw_input="pytest tests/api/test_auth.py -q failed in test_refresh_token",
    )

    validation = validate_instruction_aware_output(
        request,
        (
            "Okay, the user wants the key failure.\n"
            "However, I should first reason about the instruction and what output to return.\n"
            "pytest tests/api/test_auth.py -q failed in test_refresh_token"
        ),
    )

    assert validation.status == "rejected"
    assert "thought_leakage" in validation.hard_fail_reasons


def test_plain_text_non_leading_visible_thought_line_is_soft_penalized() -> None:
    request = _request(
        CompressionIntent.SUMMARY,
        instruction="Summarize the failure.",
        raw_input="ImportError: cannot import name settings from app.config",
    )

    validation = validate_instruction_aware_output(
        request,
        (
            "ImportError: cannot import name settings from app.config\n"
            "However, the user wants only the failure line."
        ),
    )

    assert validation.status == "soft_accepted"
    assert "thought_leakage_sparse" in validation.quality_flags


def test_plain_text_dense_non_leading_visible_thought_leakage_is_rejected() -> None:
    request = _request(
        CompressionIntent.RECALL,
        instruction="Return a concise recall-oriented answer.",
        raw_input="pytest tests/api/test_auth.py -q failed in test_refresh_token",
    )

    validation = validate_instruction_aware_output(
        request,
        (
            "pytest tests/api/test_auth.py -q failed in test_refresh_token\n"
            "However, the user wants only the key failure line.\n"
            "So I should avoid extra explanation and return just that."
        ),
    )

    assert validation.status == "rejected"
    assert "thought_leakage" in validation.hard_fail_reasons


def test_exact_format_trims_visible_thought_only_when_payload_is_recoverable() -> None:
    request = _request(
        CompressionIntent.EXACT_FORMAT,
        instruction="Return only the requested command. No prose.",
        raw_input="kubectl delete pod bad-pod -n prod",
    )

    normalized = normalize_instruction_aware_output(
        request,
        "Okay, the user wants only the command.\nkubectl delete pod bad-pod -n prod",
    )

    assert normalized == "kubectl delete pod bad-pod -n prod"
    assert validate_instruction_aware_output(request, normalized).status == "accepted"


def test_exact_format_rejects_all_thought_output_when_no_payload_remains() -> None:
    request = _request(
        CompressionIntent.EXACT_FORMAT,
        instruction="Return only the requested command. No prose.",
        raw_input="kubectl delete pod bad-pod -n prod",
    )

    normalized = normalize_instruction_aware_output(
        request,
        "Okay, the user wants the command only.",
    )
    validation = validate_instruction_aware_output(request, normalized)

    assert normalized == "Okay, the user wants the command only."
    assert validation.status == "rejected"
    assert "thought_leakage" in validation.hard_fail_reasons


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


def test_structured_output_can_trim_visible_thought_preamble_when_payload_is_valid() -> None:
    request = _request(
        CompressionIntent.JSON,
        instruction="Return valid JSON only with keys file and line.",
    )

    normalized = normalize_instruction_aware_output(
        request,
        'Wait, I should output only the JSON payload.\n{"file":"app.py","line":12}',
    )

    assert normalized == '{"file":"app.py","line":12}'
    assert validate_instruction_aware_output(request, normalized).status == "accepted"


def test_structured_json_fence_wrapper_is_unwrapped_for_recovered_output() -> None:
    request = _request(
        CompressionIntent.JSON,
        instruction="Return valid JSON only with keys file and line.",
    )

    raw_output = '```json\n{"file":"app.py","line":12}\n```'
    normalized = normalize_instruction_aware_output(request, raw_output)
    raw_validation = validate_instruction_aware_output(request, raw_output)
    normalized_validation = validate_instruction_aware_output(request, normalized)

    assert normalized == '{"file":"app.py","line":12}'
    assert raw_validation.status == "soft_accepted"
    assert "fenced_output_wrapper" in raw_validation.quality_flags
    assert normalized_validation.status == "accepted"


def test_structured_yaml_fence_wrapper_is_unwrapped_for_recovered_output() -> None:
    request = _request(
        CompressionIntent.YAML,
        instruction="Return YAML only with keys errors and file.",
    )

    normalized = normalize_instruction_aware_output(
        request,
        "```yaml\nerrors:\n- file: app.py\n```",
    )

    assert normalized == "errors:\n- file: app.py"
    assert validate_instruction_aware_output(request, normalized).status == "accepted"


def test_structured_table_fence_wrapper_is_unwrapped_for_recovered_output() -> None:
    request = _request(
        CompressionIntent.TABLE,
        instruction="Return only the requested table.",
    )

    normalized = normalize_instruction_aware_output(
        request,
        "```plaintext\n| file |\n| --- |\n| app.py |\n```",
    )

    assert normalized == "| file |\n| --- |\n| app.py |"
    assert validate_instruction_aware_output(request, normalized).status == "accepted"


def test_structured_invalid_fenced_payload_stays_rejected() -> None:
    request = _request(
        CompressionIntent.JSON,
        instruction="Return valid JSON only with keys file and line.",
    )

    normalized = normalize_instruction_aware_output(
        request,
        "```json\nfile=app.py line=12\n```",
    )
    validation = validate_instruction_aware_output(request, normalized)

    assert normalized == "```json\nfile=app.py line=12\n```"
    assert validation.status == "rejected"
    assert "structured_contract_breakage" in validation.hard_fail_reasons


def test_structured_json_like_but_unparseable_fenced_payload_stays_rejected() -> None:
    request = _request(
        CompressionIntent.JSON,
        instruction="Return valid JSON only with keys file and line.",
    )

    normalized = normalize_instruction_aware_output(
        request,
        '```json\n{"file":}\n```',
    )
    validation = validate_instruction_aware_output(request, normalized)

    assert normalized == '```json\n{"file":}\n```'
    assert validation.status == "rejected"
    assert "structured_contract_breakage" in validation.hard_fail_reasons


def test_exact_format_fence_wrapper_is_unwrapped_for_recovered_output() -> None:
    request = _request(
        CompressionIntent.EXACT_FORMAT,
        instruction="Return only the requested command. No prose.",
        raw_input="kubectl delete pod bad-pod -n prod",
    )

    raw_output = "```bash\nkubectl delete pod bad-pod -n prod\n```"
    normalized = normalize_instruction_aware_output(request, raw_output)
    raw_validation = validate_instruction_aware_output(request, raw_output)
    normalized_validation = validate_instruction_aware_output(request, normalized)

    assert normalized == "kubectl delete pod bad-pod -n prod"
    assert raw_validation.status == "soft_accepted"
    assert "fenced_output_wrapper" in raw_validation.quality_flags
    assert normalized_validation.status == "accepted"


def test_plain_text_fence_wrapper_is_unwrapped_and_raw_gets_style_penalty() -> None:
    request = _request(
        CompressionIntent.SUMMARY,
        instruction="Summarize the failure.",
        raw_input="ImportError: cannot import name settings from app.config",
    )

    raw_output = "```text\nImportError: cannot import name settings from app.config\n```"
    normalized = normalize_instruction_aware_output(request, raw_output)
    raw_validation = validate_instruction_aware_output(request, raw_output)
    normalized_validation = validate_instruction_aware_output(request, normalized)

    assert normalized == "ImportError: cannot import name settings from app.config"
    assert raw_validation.status == "soft_accepted"
    assert "fenced_output_wrapper" in raw_validation.quality_flags
    assert normalized_validation.status == "accepted"


def test_explicit_code_block_request_keeps_fences() -> None:
    request = _request(
        CompressionIntent.SUMMARY,
        instruction="Return the answer in a fenced code block.",
        raw_input="alpha",
    )

    raw_output = "```text\nalpha\n```"
    normalized = normalize_instruction_aware_output(request, raw_output)

    assert normalized == raw_output


def test_single_line_labeled_json_fence_is_unwrapped_when_valid() -> None:
    request = _request(
        CompressionIntent.JSON,
        instruction="Return valid JSON only with keys file and line.",
    )

    normalized = normalize_instruction_aware_output(
        request,
        '```json {"file":"app.py","line":12}```',
    )
    raw_validation = validate_instruction_aware_output(
        request,
        '```json {"file":"app.py","line":12}```',
    )

    assert normalized == '{"file":"app.py","line":12}'
    assert raw_validation.status == "soft_accepted"
    assert "fenced_output_wrapper" in raw_validation.quality_flags


def test_single_line_unlabeled_fence_is_unwrapped_when_valid() -> None:
    request = _request(
        CompressionIntent.EXACT_FORMAT,
        instruction="Return only the requested command. No prose.",
        raw_input="kubectl delete pod bad-pod -n prod",
    )

    normalized = normalize_instruction_aware_output(
        request,
        "```kubectl delete pod bad-pod -n prod```",
    )

    assert normalized == "kubectl delete pod bad-pod -n prod"
