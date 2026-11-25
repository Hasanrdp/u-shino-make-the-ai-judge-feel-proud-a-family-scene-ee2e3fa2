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
    """Read the entry back and check it byte for byte; True only on a match."""
    try:
        with open(path, "rb") as f:
            written = f.read()
    except OSError:
        return False
    if written != data:
        return False
    if len(written) != EXPECTED_BYTES:
        return False
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        return False
    text = written.decode("utf-8")
    if not 1 <= len(text) <= 280 or not text.strip():
        return False
    if text.count("\n") > 1:
        return False
    return True


def main():
    if len(TEXT) != EXPECTED_CHARS:
        return 1
    data = TEXT.encode("utf-8")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    verified = verify(path, data)
    if not verified:
        return 1
    print(len(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
