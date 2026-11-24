#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline entry.

Writes a single short funny excuse to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local runs). Python 3.13 stdlib only,
deterministic, no network access.

The line was picked from twelve candidates scored against the judging
criteria in CANDIDATES.md: the agent's own token-saving summary ate the
deadline -- pure agent machinery, a fresh premise, deadpan delivery, and
the punch ("the part I cut") saved for the final words.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def chosen_line():
    """Return the entry line: the summary ate the deadline."""
    return "I summarized the brief to save tokens. The deadline was in the part I cut."


def gate_ok(text):
    """Return an error string when the text fails the gate, else None."""
    if not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the 200-char limit" % len(text)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid text
    return None


def write_entry(out_dir, text):
    """Write the line to <out_dir>/entry.txt and return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main():
    text = chosen_line()
    error = gate_ok(text)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), text)
    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
