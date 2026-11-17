"""Write the entry prose to entry.txt in the make.fun output directory."""

import os

TEXT = """\
The kettle has been off for a while. A brass fan on the sill turns through the last of its spin. Eight turns, then five, then two. The blades throw small shapes across the table.

A man sits at the table with his sleeves pushed up. His hands lie open on the wood. The room smells of toast and hot metal.

The fan slows to one turn. Its shadow crosses the cloth, then the man's wrist, then the cloth again.

The blades stop.

The man's hand closes a little, as if a fly had landed near it, and then opens.

The light has moved down the wall to the edge of the cupboard. A spoon lies on the cloth, its bowl full of orange.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
