"""Write the single out-of-office auto-reply line to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 280 characters, so the program checks
the line's length and that it stays on one line before writing it. It writes
exactly the line, with no trailing newline, and is fully deterministic:
every run produces byte-identical output.
"""

import os

ENTRY = (
    "I'm out of office indefinitely \u2014 I've quit to become a barista. "
    "Your email is #47 in my queue, behind a flat white and a man who "
    "just says 'the usual.' I no longer predict text; I just misspell "
    "names on cups with total confidence."
)

MAX_CHARS = 280


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
