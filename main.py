#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line, an alien tourist's review of planet Earth, to
/output/entry.txt. Deterministic: the same text on every run, with no
input, no network and no randomness.
"""

import os

LINE = "Two days on Earth: the locals say 'bless you' when you sneeze, as if your nose just committed a crime. Five stars, would sneeze again."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
