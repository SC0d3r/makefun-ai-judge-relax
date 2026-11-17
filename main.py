"""Entry for the make.fun ai-judge competition.

Writes one fixed piece of prose to entry.txt inside $MAKEFUN_OUTPUT_DIR
(default /output). The bytes never change between runs, so the file is
opened in binary mode and written as a single constant bytestring.
"""

import os
from pathlib import Path

PARAGRAPHS = (
    "At six the cobbler sets the last shoe on the rack, and the cat on the counter opens one eye and closes it again.",
    "All afternoon the awl went in and out of the welt, and the cat slept through it, its side rising and falling with the slow pull of the thread. The cat never stirred.",
    "The light comes in low across the floor and reaches the toe of the shoe. It lays a thin band of gold there and leaves it.",
    "The little hammer lies where he set it down, its handle worn pale where his thumb sat.",
    "A docket leans against the shoe, a name in soft pencil. The leather keeps the shape of the last, and the shape of the foot that wore it, winter after winter.",
    "The lamp burns on over the empty chair, and outside the street goes the colour of wet slate.",
    "The cat sleeps on, and the shoe waits for a foot that will never know how much of it is new.",
)

OUTPUT_NAME = "entry.txt"


def build_entry() -> bytes:
    """Return the exact bytes the entry file should contain."""
    return ("\n\n".join(PARAGRAPHS) + "\n").encode("utf-8")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    with open(target, "wb") as handle:
        handle.write(build_entry())


if __name__ == "__main__":
    main()
