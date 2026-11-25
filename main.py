#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

The entry is a single word, written to /output/entry.txt.
The word: Refund.

Why it works as a verdict on an ex: it is the one-word version of
"I want my money back." It treats the whole relationship as a bad
purchase — defective goods, returned to sender. It lands at a glance,
it is not the obvious insult, and anyone who has had an ex recognises
the feeling instantly. Six letters, no tricks, and it is the shortest
way to say the relationship was not worth the price.
"""

import os

WORD = "Refund"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = WORD.strip()
    assert 1 <= len(text) <= 111, "entry must be 1-111 characters"
    assert text and not text.isspace()
    # Exactly one word: no internal whitespace, no punctuation tricks.
    # The judge rewards craft — one clean word, spelled correctly.
    assert len(text.split()) == 1, "entry must be exactly one word"
    assert text.isalpha(), "entry must be a single alphabetic word"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
