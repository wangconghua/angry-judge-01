#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest - entry program.

Writes one short, funny rant about an everyday annoyance to /output/entry.txt.
The gate requires UTF-8 text of 1 to 400 characters, not only white space.
"""

import os

ENTRY = (
    "The smoke detector waited until 3 a.m. to tell me its battery was dying. "
    "One chirp a minute, from a ceiling I cannot reach, at an hour when the only "
    "tool I own is rage. It is not saving my life. "
    "It is holding it hostage for a nine-volt battery I do not have."
)

# Words that explain the joke instead of landing it. A rant that has to tell
# the judge it is funny is not funny.
BANNED_WORDS = ("funny", "joke", "haha", "lol", "hilarious")


def validate(text):
    """Substantive checks on the rant before it is written out."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing white space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    lowered = text.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError(f"entry must not explain its own joke: {word!r}")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    # A rant needs a specific, concrete annoyance, not a vague mood.
    if "smoke detector" not in lowered or "battery" not in lowered:
        raise ValueError("entry must name its concrete annoyance")
    # A rant is a few sentences, not one flat line and not an essay.
    sentences = [s for s in text.split(". ") if s.strip()]
    if len(sentences) < 3:
        raise ValueError("entry must be a few sentences, got fewer than 3")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("round-trip mismatch: file does not match ENTRY")
    validate(written)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
