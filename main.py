#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- a single-line safety warning label for every human
being, at most 160 characters -- to /output/entry.txt.

The joke: humans read warning labels, nod solemnly, and then do exactly
what the label warns against. The label warns about the very behaviour
of ignoring warning labels, so the laugh lands in the last few words.
"""

import os

ENTRY = (
    "WARNING: Contains one human who will read this label carefully, "
    "nod solemnly, and immediately do the exact thing it warns against."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
