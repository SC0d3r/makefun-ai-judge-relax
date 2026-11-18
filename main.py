"""Entry for the ai-judge-relax-01 competition.

Running this file writes one short second-person text to entry.txt
inside the output directory, so every run produces the same bytes.
MAKEFUN_OUTPUT_DIR sets that directory; the default is /output.
Python standard library only, no network.
"""

import os

DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


PARAGRAPHS = [
    (
        "The drops land on the canvas a hand apart, each drop its own drum, "
        "and you are in the bag, warm, with the zip someone shut from outside."
    ),
    (
        "A coat that is not yours lies over the bag, left there, and "
        "the rain slows. The flask sits by your knee, still warm where a hand "
        "set it down."
    ),
    (
        "The drops come two fingers apart now, and the drum thins into a tap. "
        "By the bag, the torch lays a hand of light on the canvas.\n"
        "A line apart."
    ),
    (
        "Then the tap is a tick, and the ticks come slower. "
        "The hand of light on the canvas thins to two fingers of light. "
        "Your own hand opens, and it stays open. No one asks."
    ),
    (
        "Two fingers thin to a line, rain and light on the same slow beat. "
        "The moon moves off the canvas, and the hour goes by with no clock.\n"
        "The light goes."
    ),
    (
        "One last drop lands, and no drop follows. "
        "The tick is gone. The canvas takes the dark on, all of it."
    ),
    (
        "The dark is on your side of the canvas, and no one needs you "
        "before morning."
    ),
]

TEXT = "\n\n".join(PARAGRAPHS)


def write_entry() -> str:
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))
    return path


if __name__ == "__main__":
    write_entry()
