"""Entry for the make.fun ai-judge-relax-01 competition.

Writes the entry text to entry.txt inside $MAKEFUN_OUTPUT_DIR
(default /output) as one fixed byte payload, so two runs produce
identical bytes.
"""

import os
from pathlib import Path

OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"

TEXT = """Straw lies eight inches deep and holds the day in it. The sow is down on her side in the dark, her flank rising slow. Five piglets have folded into her curve; the sixth is still up. He noses her flank.

A fly rides the air over her ear and her ear flicks it away, twice. Her breath runs long and wide, lifting the five asleep against her belly.

Fourteen. Twelve. Nine. Six.

He works along her ribs, his snout reading the hide step by step. The five sleep pressed into her, their sides rising and falling with hers. Straw dust hangs over the bed and comes down without landing. He noses in.

In the passage a hand finds the lamp and turns it down a notch. The gold leaves the straw and the dark comes in close.

The ear lifts once to the fly and comes down without meeting it. He noses her flank one more time, presses in, and folds down against her.

The straw takes the rest of him."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = TEXT.encode("utf-8")
    with open(out_dir / OUTPUT_NAME, "wb") as stream:
        stream.write(payload)


if __name__ == "__main__":
    main()
