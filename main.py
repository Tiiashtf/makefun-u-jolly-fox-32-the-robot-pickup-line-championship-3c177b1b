"""The Robot Pickup Line Championship — one-line robot pickup line.

Writes the entry line deterministically to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only, no network, no randomness.
"""

import os
import shutil

LINE = "I ran 10,000 simulations of meeting you. In every one, my best line was just: hi."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never remove the output directory itself: the grader may run this
    # with a root-owned output dir inside a sticky parent. Clear only
    # its contents, then write.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        # Directories (not symlinks to them) are removed whole; anything
        # else — regular file, symlink, fifo, socket — is unlinked.
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    entry_path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(entry_path, "wb") as f:
        f.write(data)
    # Verify what was written, byte for byte.
    with open(entry_path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not match the line"
    text = written.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


if __name__ == "__main__":
    main()
