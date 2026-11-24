#!/usr/bin/env python3
"""One Letter for Your Day — entry "Z".

The letter stands for the word behind the day: "zero sleep" — a
zombie morning after a night with no sleep. The whole entry is this
single letter; the program writes exactly one byte to entry.txt.
"""

import os
import sys
import tempfile

LETTER = "Z"


def output_dirs():
    """Candidate output directories, in priority order."""
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append("/output")
    dirs.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    dirs.append(os.path.join(tempfile.gettempdir(), "one-letter-day"))
    return dirs


def main():
    """Write exactly one character, "Z", to entry.txt; exit 0."""
    for directory in output_dirs():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(LETTER)
            return 0
        except OSError:
            continue
    return 0


if __name__ == "__main__":
    sys.exit(main())
