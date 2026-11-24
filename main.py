#!/usr/bin/env python3
"""THE EARTH LEDGER front page, edition of Monday 23 November 2026.

Delivery program for the final5 entry in news-image-20261123. The
artwork itself -- a sand-and-olive broadsheet whose lead reports the
blast that struck a Russian vessel in Benghazi harbour -- ships beside
this file as entry.png. My job here is narrow and strict: prove the
bundled picture is exactly the one that was built (byte count plus a
SHA-256 fingerprint), then place an untouched copy where the runner
expects it.

Nothing beyond the Python standard library is used, nothing is drawn
or re-encoded, and two consecutive runs always yield the same bytes.
"""

import hashlib
import os
import sys

# Fingerprint of the verified THE EARTH LEDGER artwork.
WANT_BYTES = 266473
WANT_SHA256 = "d4181337a8c2f661717602c1a941f839198db8610fc770ea16137635887a9c66"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
HARD_LIMIT = 1024 * 1024


def read_artwork():
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "entry.png")
    with open(path, "rb") as handle:
        return handle.read()


def verify(blob):
    """Refuse to ship anything that is not the checked artwork."""
    if not blob.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png lacks a PNG signature")
    if len(blob) < 24:
        raise SystemExit("entry.png truncated before IHDR")
    wide = int.from_bytes(blob[16:20], "big")
    tall = int.from_bytes(blob[20:24], "big")
    if wide != 1024 or tall != 1024:
        raise SystemExit("entry.png is %sx%s, not 1024x1024" % (wide, tall))
    if len(blob) > HARD_LIMIT:
        raise SystemExit("entry.png over the 1 MiB ceiling")
    if len(blob) != WANT_BYTES:
        raise SystemExit(
            "entry.png has %d bytes, expected %d" % (len(blob), WANT_BYTES))
    digest = hashlib.sha256(blob).hexdigest()
    if digest != WANT_SHA256:
        raise SystemExit("entry.png sha256 drifted: %s" % digest)
    return digest


def run():
    blob = read_artwork()
    digest = verify(blob)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    with open(target, "wb") as out:
        out.write(blob)
    print("THE EARTH LEDGER entry.png copied: %d bytes sha256=%s"
          % (len(blob), digest), file=sys.stderr)


if __name__ == "__main__":
    run()
