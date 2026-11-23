#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first that comes to mind, to
/output/entry.txt. No topic, no explanation, no second draft.

The word: psithurism — the sound of wind in the trees. Surprising,
vivid, and its own whispering sound rewards a second look.
"""

from pathlib import Path

WORD = "psithurism"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
