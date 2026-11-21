#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a calm text built around a
single vast, concrete image — starlight that left its star before anyone
alive was born, and is still arriving tonight.
"""

from pathlib import Path

ENTRY = (
    "High above you tonight, a star is still sending out the light it made "
    "before anyone alive was born. It has been crossing the dark for a "
    "thousand years, asking nothing, and a little of it reaches your eyes "
    "now — the same light, still arriving."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
