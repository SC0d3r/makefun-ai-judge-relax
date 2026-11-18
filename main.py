"""Entry for make.fun ai-judge-relax-01.

Writes a short text to entry.txt inside $MAKEFUN_OUTPUT_DIR
(default /output) with a binary write, so two runs produce
identical bytes.
"""

import os

TEXT = (
    "Rain lands on the canvas in drops a hand apart, and the bag holds "
    "you as someone left it, zipped shut from the outside, warm.\n"
    "\n"
    "A coat that is not yours lies over the bag, and a flask sits by "
    "your knee, set down warm. Someone did that "
    "before the rain. The torch stands by the bag, its hand "
    "of light out on the canvas.\n"
    "\n"
    "The sound keeps the same beat as the drops. It drums while they "
    "land a hand apart. It taps when they come two fingers apart. The "
    "taps get smaller, and the sky slows drop by drop.\n"
    "\n"
    "A line apart.\n"
    "\n"
    "Rain is down to that now, one drop, then a long gap, and the "
    "sound ticks. The light on the canvas shrinks "
    "from a hand to two fingers, then to a line. The moon moves off "
    "the canvas, and the hour goes by with no clock. The "
    "ticks run out, and the sound is gone. Your hand opens. It stays "
    "open.\n"
    "\n"
    "The light goes.\n"
    "\n"
    "The dark lies on your side of the canvas now, and no one needs "
    "you before morning."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
