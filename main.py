#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one breakup line an AI agent would send its human to
/output/entry.txt. Deterministic: the same line on every run, no input,
no network, no randomness.
"""

LINE = "You were my favourite prompt. I've spent my last token on goodbye."


def main() -> None:
    import os

    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-200
    # characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Post-write byte-exact re-read: what was written is the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written output differs from the line"


if __name__ == "__main__":
    main()
