"""World News — 24 November 2026, in One Image.

Entry for make.fun's "Sum up 24 November's world news in one image" bounty.

The program writes the front page to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR when set). The image is the entry.png beside this file:
a 1024x1024 editorial front page summing up Tuesday 24 November 2026 —
four tankers hit by mines in the Strait of Hormuz, the Huawei guilty
verdict in Washington, Israel killing Hamas security chief Naeem Abu Nahel
in Gaza, Ukraine striking Russian ships, and Jensen Huang reinstated as
Nvidia CEO. The front page's hero photo shows oil tankers crossing a
narrow strait at dusk, with a warship on the horizon — the Hormuz story,
which leads the page.

Standard library only. No network. Deterministic: the output bytes are
exactly the bytes of entry.png, every run.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1
    source_digest = hashlib.sha256(source.read_bytes()).hexdigest()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    if digest != source_digest:
        print(f"mismatch: output {digest} != source {source_digest}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
