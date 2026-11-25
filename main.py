"""Write the tech support one-liner to the output file.

The entry is a single funny line from a hopeless tech support agent
to a desperate customer. The joke is the agent's cheerful uselessness:
the stock fix is the only trick he knows, and he has been saving it.
This program writes exactly that line and nothing else: no network
access, no randomness, and no dependence on the time or date, so every
run produces the same bytes.

The output directory is /output by default and can be overridden with
the OUTPUT_DIR environment variable (handy for local testing).
"""

import hashlib
import os
import sys

LINE = "Have you tried turning it off and on again? No? Wonderful \u2014 that's the only trick I know, and I was saving it."


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"Wrote {len(data)} bytes to {path} (sha256 {digest})")
    print(f"Line: {LINE!r} ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
