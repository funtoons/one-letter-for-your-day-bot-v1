#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry.

Writes exactly one character, the letter Z, to /output/entry.txt.

The letter stands for the word behind the day: "zero sleep" -- a day
run on nothing, zombie mode, ZZZ. No word, no gloss, no punctuation
and no trailing newline is written: the file holds one byte, "Z".
"""

import os
from pathlib import Path

LETTER = "Z"


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    data = LETTER.encode("utf-8")
    assert len(data) == 1 and LETTER.isalpha() and LETTER.isupper()
    target.write_bytes(data)


if __name__ == "__main__":
    main()
