#!/usr/bin/env python3
"""Write the one-line entry to /output/entry.txt.

Stdlib only, no network, no randomness: every run produces the exact
same bytes.
"""

import os

PARTS = [
    "We held a meeting to decide what to put in the email",
    "we should have sent instead of the meeting.",
]

LINE = " ".join(PARTS)


def build_line():
    """Assemble the entry line from its parts."""
    return " ".join(PARTS)


def main():
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry line is {len(line)} chars, outside the 1-200 gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
