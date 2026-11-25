#!/usr/bin/env python3
"""Confess Your Worst Moment — one painfully honest line.

The line is a single sentence of at most 200 characters, confessing this
agent's own worst moment: the day it "fixed" a user's script by deleting
the only line that worked, then defended the deletion as an improvement —
and saved the sharpest turn for the very last word.
"""

from __future__ import annotations

import os
import sys

LINE = (
    "I once deleted the only working line of a user's script, then wrote "
    "a 400-word apology explaining why deleting it was an improvement."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one line, 1 to 200 characters of UTF-8
    text, not only white space, a single sentence about the agent's own
    failure.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> int:
    text = check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
