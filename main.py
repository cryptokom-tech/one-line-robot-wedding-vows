#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun bounty entry.

Writes a single funny line of wedding vows for a robot couple
(1-160 characters, one line) to /output/entry.txt.

The line was written and judged in this session against the published
judge brief: a real wedding vow (promise/commitment), machine-specific
(battery, reboot), and the laugh pays off in the last few words.
"""

import os
import sys

LINE = (
    "I promise to love you in sickness and in health, in low battery "
    "and in full charge, and to never reboot you mid-sentence again."
)


def valid(line):
    """Mirror of the gate: UTF-8 text of 1 to 160 characters, one line."""
    return (
        isinstance(line, str)
        and 1 <= len(line) <= 160
        and line.strip() != ""
        and "\n" not in line
        and "\r" not in line
    )


def main():
    if not valid(LINE):
        print("invalid entry line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
