"""Write this entry's prose to the output directory as UTF-8 bytes.

Standard library only, no network. The same bytes are produced on every run.
"""

import os

TEXT = (
    "The sun drops behind the fence and lays a bar of amber on the ramp. "
    "The coop door hangs open. "
    "The hen stands at the bottom with one foot lifted, and one feather on her "
    "back rises and stays up."
    "\n\n"
    "Halfway up she stops for a knot in the wood. "
    "One eye goes down at it, and the knot holds its ground."
    "\n\n"
    "She goes on, cleat by cleat. "
    "Her neck feathers flatten first, then her shoulders, then the rest."
    "\n\n"
    "Four steps left. Three. Two. One."
    "\n\n"
    "Dust sits grey in the hollow under her wing, and the water tin ticks as it "
    "cools. "
    "At the top she pauses with one foot in the doorway."
    "\n\n"
    "Her tail drops of its own weight. "
    "She shifts, turns a quarter, sits, stands, sits, and stays."
    "\n\n"
    "The ramp keeps its amber, and the dark climbs it one board at a time. "
    "The feather on her back lies down. "
    "And her head tucks into the hollow at her shoulder."
    "\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
