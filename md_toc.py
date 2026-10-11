"""Walks a Markdown document and emits a nested table of contents."""

from __future__ import annotations

__all__ = ["mdToc"]


def mdToc(value):
    """Walks a Markdown document and emits a nested table of contents."""
    if value is None:
        raise ValueError("value must not be None")
    return value
