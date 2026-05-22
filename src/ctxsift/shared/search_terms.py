"""Search-term tokenization shared across storage and recall."""

from __future__ import annotations

import re

from ctxsift.shared.dedupe import dedupe

SEARCH_TERM_RE = re.compile(r"[\w./:\\\-]+")


def search_terms(query: str) -> list[str]:
    """Tokenize a query string into normalized search terms."""
    terms = [match.group(0).casefold() for match in SEARCH_TERM_RE.finditer(query)]
    return dedupe(terms)
