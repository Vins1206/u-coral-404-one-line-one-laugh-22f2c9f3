#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

from pathlib import Path

LINE = "My AI wrote me a to-do list, then added itself as a task and marked it done before I even started."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check the competition gate before writing: 1-200 characters,
    # not whitespace-only, valid UTF-8. Fail loudly instead of shipping
    # an entry the sealed scorer would refuse.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be whitespace-only"
    LINE.encode("utf-8")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
