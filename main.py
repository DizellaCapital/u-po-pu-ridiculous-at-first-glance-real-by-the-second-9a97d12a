"""Ridiculous at First Glance, Real by the Second — entry program.

Writes a single-sentence startup pitch to MAKEFUN_OUTPUT_DIR/entry.txt:
pothole naming rights, sold to sponsors for $20 a month, with the city
fixing the sponsored potholes first — because even asphalt answers to
advertising. One line, 136 characters, no trailing newline. Stdlib only.
"""

import os
import sys

LINE = "We sell pothole naming rights for $20 a month, and the city fixes the sponsored ones first, because even asphalt answers to advertising."


def main():
    length = len(LINE)
    if length < 1 or length > 200:
        print(f"entry must be 1-200 characters, got {length}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if "\t" in LINE:
        print("entry must not contain tabs", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
