"""Entry for the make.fun ai-judge-relax-01 competition.

A cobbler's shop just after closing. The text below is written to
entry.txt inside $MAKEFUN_OUTPUT_DIR (default /output) as one fixed
byte string, so two runs produce identical bytes.
"""

import os

PARAGRAPHS = [
    "At ten past six the cobbler pulls the shop door shut behind him, "
    "and the bell over the latch keeps swinging.",

    "The swing narrows to the width of a hand, and its ring is full. "
    "To the width of two fingers, and the ring has less in it. "
    "To a line, and the sound has no ring left in it. "
    "To nothing, and it does not move.",

    "A cat sleeps on the counter. Its chin lowers onto its paws a "
    "little at a time, and rests there, and does not lift again.",

    "A broom leans under the bench where he left it, and the dust "
    "around it keeps its shape.",

    "The mended shoe sits on the rack, wax warm where his thumb "
    "pressed it, holding a low shine.",

    "The clock over the door goes on past the hour, tick by tick. "
    "The colour of wet slate leaves the street, and the dark takes "
    "the glass.",

    "The shine on the wax will keep until morning, and nothing needs "
    "to be done for it to keep.",
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
