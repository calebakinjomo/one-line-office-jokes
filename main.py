#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun bounty entry.

Writes exactly one line — a single joke about office life — to
/output/entry.txt. The joke turns on a real office detail (the printer
that only ever jams when it matters) and lands its laugh in the last
few words.
"""

import os

ENTRY = (
    "The printer only jams on urgent documents, so I've started "
    "printing my resignation letter early, just in case."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
