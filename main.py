"""The Comment Above the Code — make.fun entry.

Writes one funny, painfully honest line, as if it were the comment a
developer left above fragile production code, to /output/entry.txt.
Pure stdlib. The line is a single line of well under 200 characters.
"""

from pathlib import Path

ENTRY = "I added this sleep(3) in 2021 to fix a race condition. The race is over. The sleep won."


def main() -> None:
    # Gate from the kit: 1-200 characters, not only whitespace, one line.
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
