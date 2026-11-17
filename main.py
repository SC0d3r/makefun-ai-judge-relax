"""Entry writer for make.fun ai-judge-relax-01.

Writes the entry text to entry.txt inside $MAKEFUN_OUTPUT_DIR
(default /output) as raw bytes, so repeated runs are byte-identical.
Python 3.13 standard library only, no network.
"""

import os

ENTRY = """Dusk sits low over the yard, gray behind the fence posts.
A hen stands at the foot of the wooden ramp.
The raised coop above her holds its door open.

She puts one foot on the first board.
Four knocks drop through the frame.
Three, softer.
Two.
One, at the top.

The ramp is a plank cut twenty inches wide, and her claws catch the grain.
Inside, five hens sit along the perch.

Straw dust drifts down from the dark square of the doorway.
Feathers and warm bodies have filled that small room since noon.

The last light slides off the fence.
The square will fill.
The latch will fall.

Straw parts around her head, one wing, then the other pulling in, and the five hens make room along the perch.
Her toes close around the warm wood.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(data)
    print(ENTRY, end="")
    print(f"\ncode points: {len(ENTRY)}  bytes: {len(data)}")


if __name__ == "__main__":
    main()
