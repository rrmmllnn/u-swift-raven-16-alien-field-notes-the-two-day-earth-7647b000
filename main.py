#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line, an alien tourist's review of planet Earth, to
/output/entry.txt. Deterministic: the same text on every run, with no
input, no network and no randomness.
"""

import os
import sys

MAX_LEN = 200

LINE = "Two days on Earth: the locals talk to their pets like colleagues, wave at cameras, and sleep away a third of their lives. Baffling. Five stars, would visit again."

def main():
    if not LINE.strip() or "\n" in LINE or len(LINE) > MAX_LEN:
        raise SystemExit("review line must be a single non-blank line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
