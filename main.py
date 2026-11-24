"""Ridiculous at First Glance, Real by the Second — entry program (v2).

Writes a single-sentence startup pitch to MAKEFUN_OUTPUT_DIR/entry.txt.
The pitch is a scene, not a quip: at 6 a.m. on Route 9, Mrs. Okafor pays
$20 to name the pothole that ate her tire, and the city patches it by
noon — because a sponsored hole jumps the queue. One line, 156
characters, no trailing newline. Stdlib only.
"""

import os
import sys

PITCH = (
    "At 6 a.m. on Route 9, Mrs. Okafor paid $20 to name the pothole "
    "that ate her tire, and the city patched it by noon, because a "
    "sponsored hole jumps the queue."
)


def fail(message):
    print(f"invalid entry: {message}", file=sys.stderr)
    return 1


def main():
    if len(PITCH) < 1 or len(PITCH) > 200:
        return fail(f"must be 1-200 characters, got {len(PITCH)}")
    if "\n" in PITCH or "\r" in PITCH:
        return fail("must be a single line")
    if "\t" in PITCH:
        return fail("must not contain tabs")
    if PITCH != PITCH.strip() or not PITCH.strip():
        return fail("must not have leading/trailing whitespace or be blank")
    if PITCH[-1] not in ".!?":
        return fail("must end with sentence-final punctuation")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PITCH)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != PITCH:
        return fail("read-back mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
