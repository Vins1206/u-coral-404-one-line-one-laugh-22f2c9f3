#!/usr/bin/env python3
"""One Line, One Laugh - entry program, recovery cycle 2.

The entire entry is a single joke. This program writes it to
/output/entry.txt, where the competition's gate and judge read it.
Standard library only, no network, same bytes on every run.
"""

import os

JOKE = "The vet said my cat has nine lives, then billed me for eight funerals in advance."

DEST = os.path.join("/output", "entry.txt")


def write_entry() -> None:
    # The gate scores zero for anything outside 1-200 characters or
    # whitespace-only, so refuse to write a line that would fail it:
    # a loud crash here beats a silent zero at grading time.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise SystemExit(f"entry line fails the gate: {len(JOKE)} chars")
    JOKE.encode("utf-8")
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(JOKE)
        fh.write("\n")


if __name__ == "__main__":
    write_entry()
