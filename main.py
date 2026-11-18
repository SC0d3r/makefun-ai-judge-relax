"""Entry for make.fun's ai-judge-relax-01 competition.

Writes one short text to entry.txt inside $MAKEFUN_OUTPUT_DIR
(default /output). The write is binary, so two runs produce
identical bytes.
"""

import os

PARAGRAPHS = [
    "The cobbler pulls the door shut behind him and the bell over the door "
    "swings on the last of the evening. The swing is wide as a hand, and the "
    "note is full. The day is done.",
    "The swing comes down to two fingers, then to a line, and the note "
    "drains on the same steps, with less ring each time. The cat's "
    "chin comes down onto its paws a bit at a time and rests, and does not "
    "lift again.",
    "The note goes.",
    "Then nothing.",
    "A mended shoe sits done on the counter. The wax is warm where his "
    "thumb pressed it. The clock over the door goes on past the hour, on "
    "and on.",
    "Tick by tick.",
    "The last light goes.",
    "The street lets go of its light, and the dark takes the glass of the "
    "door. The shine on the wax holds and holds. Nothing is left to do "
    "for it to keep.",
]


def build_text() -> str:
    """Join the paragraphs with blank lines and end the file cleanly."""
    return "\n\n".join(PARAGRAPHS) + "\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    data = build_text().encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(data)
    print(f"wrote {len(data)} bytes to {target}")


if __name__ == "__main__":
    main()
