#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.

The joke was chosen against the published judge brief: it must be a genuine
one-line joke about office life (not a caption or stray observation), funny
on first read, a single sentence, fresh and specific rather than generic,
and clear with no explanation needed.

Chosen line (101 characters, one sentence, one line):

    My manager's 'quick question' took 47 minutes, three whiteboards,
    and somehow became my Q3 objective.

Why this line: "quick question" is the office phrase everyone recognises;
the punchline escalates it in three concrete beats (47 minutes, three
whiteboards, Q3 objective) so the setup pays off with surprise instead of
restating a cliché. It never says "this meeting could have been an email",
yet it is exactly the line you send a colleague after a meeting that
should have been an email.
"""

import os
import sys

JOKE = (
    "My manager's 'quick question' took 47 minutes, three whiteboards, "
    "and somehow became my Q3 objective."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the sealed gate's rules before writing anything."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # One sentence: no sentence-ending punctuation before the final character.
    body = text.rstrip(".!?")
    if any(ch in body for ch in ".!?"):
        raise ValueError("entry must read as a single sentence")
    text.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> int:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)
    # Read back and confirm the file holds exactly the validated joke.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != JOKE:
        raise ValueError("written entry does not match the validated joke")
    print(f"wrote {len(JOKE)} chars to {OUTPUT_PATH}")
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
