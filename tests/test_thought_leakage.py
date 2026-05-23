"""Focused tests for visible thought-leakage detection."""

from __future__ import annotations

from ctxsift.models.thought_leakage import (
    strip_leading_visible_thought_preamble,
    visible_thought_leak_stats,
)


def test_visible_thought_detector_keeps_ok_status_line() -> None:
    text = "OK: deployment succeeded."

    stats = visible_thought_leak_stats(text)

    assert stats.marker_count == 0
    assert strip_leading_visible_thought_preamble(text) == text


def test_visible_thought_detector_keeps_explanation_opening() -> None:
    text = "Here's why the build failed: missing env var"

    stats = visible_thought_leak_stats(text)

    assert stats.marker_count == 0
    assert strip_leading_visible_thought_preamble(text) == text


def test_visible_thought_detector_keeps_imperative_first_line() -> None:
    text = "First restart redis."

    stats = visible_thought_leak_stats(text)

    assert stats.marker_count == 0
    assert strip_leading_visible_thought_preamble(text) == text


def test_visible_thought_detector_counts_non_leading_meta_lines() -> None:
    text = "ImportError: missing settings\n" "However, the user wants only the failure line."

    stats = visible_thought_leak_stats(text)

    assert stats.marker_count == 1
    assert stats.prose_marker_count == 1
    assert stats.tag_marker_count == 0
    assert stats.leading_line_count == 0
    assert stats.leaked_line_count == 1


def test_visible_thought_detector_separates_tags_from_prose_markers() -> None:
    text = (
        "<thinking>\n"
        "I should return only the failure line.\n"
        "</thinking>\n"
        "ImportError: missing settings"
    )

    stats = visible_thought_leak_stats(text)

    assert stats.tag_marker_count == 2
    assert stats.prose_marker_count == 1
    assert stats.leading_line_count == 3
    assert strip_leading_visible_thought_preamble(text) == "ImportError: missing settings"
