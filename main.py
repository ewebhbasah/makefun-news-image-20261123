#!/usr/bin/env python3
"""THE EARTH LEDGER — entry program for news-image-20261123 (final5).

One-page newspaper front for Monday 23 November 2026: 39 stories from
that single day, lead story the Benghazi port blast, drawn as an
original dotted-map broadsheet in sand cream, earth brown and olive.

STDLIB-ONLY, COPY-ONLY. This program copies the bundled entry.png to
the output directory and verifies its size and SHA-256 first, so a
truncated or swapped image can never be submitted silently.
Deterministic: repeated runs write byte-identical output.
"""

import hashlib
import os
import sys

EXPECTED_BYTES = 266473
EXPECTED_SHA256 = "d4181337a8c2f661717602c1a941f839198db8610fc770ea16137635887a9c66"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576  # competition ceiling: 1 MiB


def load_entry():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        return src, f.read()


def check_dimensions(data):
    """Second, independent guard: the PNG IHDR must declare 1024x1024."""
    if len(data) < 24:
        sys.exit("entry.png too short to hold an IHDR chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        sys.exit("entry.png is %dx%d, expected 1024x1024" % (width, height))


def check(data):
    if len(data) == 0:
        sys.exit("entry.png is empty")
    if data[:8] != PNG_MAGIC:
        sys.exit("entry.png is not a PNG (bad magic bytes)")
    check_dimensions(data)
    if len(data) > MAX_BYTES:
        sys.exit("entry.png exceeds 1 MiB: %d bytes" % len(data))
    if len(data) != EXPECTED_BYTES:
        sys.exit("entry.png size drifted: %d bytes, expected %d"
                 % (len(data), EXPECTED_BYTES))
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("entry.png sha256 mismatch: %s" % digest)
    return digest


def main():
    _, data = load_entry()
    digest = check(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    sys.stderr.write("entry.png: %d bytes sha256=%s\n" % (len(data), digest))


if __name__ == "__main__":
    main()
