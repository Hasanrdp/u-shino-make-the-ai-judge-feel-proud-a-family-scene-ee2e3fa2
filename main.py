#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene — make.fun entry.

Writes one short family scene to /output/entry.txt: the family photo
where the toddler sneezes at the flash, and Grandad calls it the only
honest photo they own. The text is fixed and deterministic — every run
writes the exact same bytes. Pure Python 3 standard library, no network,
no secrets, no input files.

Why this scene: it is a whole household in one breath — everyone smiling,
one small chaos, and a wry line from Grandad that turns the ruined photo
into the one worth keeping. Warm first, funny second, heartfelt in the
landing, and every word earns its place.
"""

import hashlib
import os

TEXT = (
    "At every family photo the toddler sneezes at the exact moment of the "
    "flash, so the one on the wall is all of us smiling and him mid-sneeze, "
    "and Grandad says it is the only honest photo we own."
)

# Pinned identity of the scene, verified 2026-11-26: 192 chars, 192 bytes.
# A typo or stray edit can never silently change the judged line — the
# program refuses to ship anything but exactly these bytes.
EXPECTED_SHA256 = "f5eeae44bbfc871716f1888d029a1aaaf2ad075ab8064e765cbb1cac79d27c09"
EXPECTED_CHARS = 192
EXPECTED_BYTES = 192


def verify(path, data):
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("entry.txt on disk does not match the scene")
    if len(written) != EXPECTED_BYTES:
        raise SystemExit("entry.txt is not 192 bytes")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.txt sha256 does not match its pinned value")
    text = written.decode("utf-8")
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit("entry text is outside the 1-280 character gate")
    if text.count("\n") > 1:
        raise SystemExit("entry text is more than two lines")
    return written


def main():
    if len(TEXT) != EXPECTED_CHARS:
        raise SystemExit("entry text is not 192 characters")
    data = TEXT.encode("utf-8")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    verified = verify(path, data)
    print(len(verified))
    return path


if __name__ == "__main__":
    print(main())
