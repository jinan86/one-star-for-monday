#!/usr/bin/env python3
"""One Star for Monday — make.fun entry.

Writes a single one-star review of Monday, written as though Monday
were a restaurant, to /output/entry.txt. Deterministic: the same text
every run.
"""

import os

ENTRY = "The bill charged me full price for Saturday and Sunday, then Monday at half. I only ate Monday."

# Gate self-check: 1-180 chars, at most 25 words, one line, no hashtag.
assert 1 <= len(ENTRY) <= 180, "entry length out of gate"
assert len(ENTRY.split()) <= 25, "entry over 25 words"
assert "\n" not in ENTRY and "#" not in ENTRY, "entry must be one plain line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
