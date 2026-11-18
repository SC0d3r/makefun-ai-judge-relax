"""Entry for the make.fun ai-judge-relax-01 competition.

A cobbler's shop just after closing. The text below is written to
entry.txt inside $MAKEFUN_OUTPUT_DIR (default /output) as one fixed
byte string, so two runs produce identical bytes.
"""

import os

PARAGRAPHS = [
    "At six the cobbler pulls the shop door shut behind him, and the "
    "bell over the door swings on, and on, and on.",

    "The swing narrows to the width of a hand, and its note is full. "
    "The swing narrows to two fingers, and the note has less in it. "
    "The swing narrows to a line, and the note has no ring in it.",

    "The note goes.",

    "To nothing.",

    "A cat sleeps on the counter. Its chin lowers onto its paws a "
    "little at a time. It rests there, and does not lift again.",

    "The shoe sits finished, and the wax is warm where his thumb "
    "pressed it. The clock over the door goes on past the hour, "
    "tick by tick.",

    "The last light.",

    "The street lets go of its light, and the dark takes "
    "the glass. The shine on it holds, and holds. "
    "Nothing needs to be done for it to keep.",
]

TEXT = "\n\n".join(PARAGRAPHS) + "\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
