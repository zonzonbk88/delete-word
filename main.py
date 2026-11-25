#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Word You'd Delete From the Dictionary'.

Writes exactly one word to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local testing, so parallel builds
don't clobber the shared /output/entry.txt).

Standard library only, deterministic, no network, no trailing newline.
"""

import os
from pathlib import Path

WORD = "awkward"


def main() -> None:
    # The entry must be exactly one word: fail loudly instead of
    # silently writing something the gate would reject.
    assert WORD and not any(ch.isspace() for ch in WORD), "WORD must be one word"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
