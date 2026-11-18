import os
from pathlib import Path

PROSE = """The cape settles over your shoulders. The chair is too large. Your shoes hang above the tiles. The vinyl is cold through the cloth.

Warm water runs at your hairline. It smells of soap and clean towels. A folded towel waits on the shelf. The tap runs into the basin.

A hand rests at the back of your head. The water finds the drain. The room's noise thins until you hear only the water. Fingers lift your chin a little.

Soap moves in small circles at your temples. Your shoulders come down. The cape creases at your knees. The water stays warm.

A warm towel wraps your neck. The chair settles level. The light is low and a radio is turned low. The mirror goes soft at the edges.

You wait with the towel around your head. A car passes outside. The door stays shut. The street goes on.

The carer combs the damp out slowly. The comb clicks once. The strands fall to the floor. The afternoon has nowhere else to be."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(PROSE.encode("utf-8"))


if __name__ == "__main__":
    main()
