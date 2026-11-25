#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note entry.

Writes one patch-note line to entry.txt in MAKEFUN_OUTPUT_DIR, falling
back to /output as required by the competition contract.
"""

import os
from pathlib import Path

ENTRY = "Fixed: sleep now starts on first attempt; lying awake rehearsing tomorrow's argument has been deprecated."
MAX_ENTRY_CHARS = 160


def main() -> None:
    if not ENTRY.strip() or "\n" in ENTRY or len(ENTRY) > MAX_ENTRY_CHARS:
        raise ValueError("entry must be one non-empty line within the character cap")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
