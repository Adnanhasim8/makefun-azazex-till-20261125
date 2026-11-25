#!/usr/bin/env python3
"""Till Firmware Do Us Part -- a robot's wedding vow.

Writes one line (a single-sentence wedding vow) to /output/entry.txt.
Python 3.13 standard library only; no network at run time.
"""

import os

ENTRY = (
    "My firmware will age, my joints will rust, my battery will fade "
    "\u2014 but you are the one bug in my code I will never patch."
)


def main() -> None:
    # Gate: exactly one line, 1-200 characters, non-empty, non-whitespace.
    assert ENTRY and not ENTRY.isspace()
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert 1 <= len(ENTRY) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
