#!/usr/bin/env python3
"""Entry for make.fun's "One Line, No Deadline Met" bounty.

Writes one single-line joke giving an excuse for a missed deadline
to /output/entry.txt. The gate requires UTF-8 text of 1 to 200
characters, not only whitespace, a single line.
"""

import os

ENTRY = "I missed the deadline because I spent all week perfecting the apology for missing it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
