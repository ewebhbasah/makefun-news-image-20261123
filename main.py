"""THE MORNING POST — entrypoint NI23 G4 Final 5 (@kangair110).

Halaman depan koran satu gambar untuk Senin 23 November 2026: lead
Alcaraz menjuarai ATP Finals, 13 kartu bernomor, 27 brief ALSO ON,
peta dunia titik-titik berpin, strip angka, dan kotak DATE CHECK.
Program ini hanya menyalin entry.png yang sudah jadi ke direktori
keluaran Make Fun — tidak ada pemrosesan gambar di sini (stdlib only,
copy-only), dengan penjaga ukuran + sha256 berkas sumber.
"""
import hashlib
import os
import shutil
import sys

EXPECTED_BYTES = 214280
EXPECTED_SHA256 = "dac8e34c48b5479d0a2e545b336aa1c76b6c70cea8f0ec9c4d639512d147a887"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    payload = open(source, "rb").read()
    if len(payload) != EXPECTED_BYTES:
        print("ukuran entry.png menyimpang: %d" % len(payload), file=sys.stderr)
        return 1
    if hashlib.sha256(payload).hexdigest() != EXPECTED_SHA256:
        print("sha256 entry.png menyimpang", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    copied = open(target, "rb").read()
    if hashlib.sha256(copied).hexdigest() != EXPECTED_SHA256:
        print("salinan keluaran tidak utuh", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
