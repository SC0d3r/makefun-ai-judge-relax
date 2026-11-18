import os
from pathlib import Path

TEXT = (
    "The cape comes up to your chin, and the chair is too big. The water is warm at your hairline. The shop smells of soap and clean towels.\n"
    "\n"
    "Her hand is at the back of your head. The water runs through, clear and slow, and finds the drain. The sound of it gets smaller until it is only the room.\n"
    "\n"
    "She works the soap in small circles at your temples. Your shoulders come down.\n"
    "\n"
    "The towel is warm against your neck. The chair comes level. The lights are low, the radio turned down to a murmur.\n"
    "\n"
    "You sit with the towel around your head. A car passes outside. The door does not open. The street goes on without you.\n"
    "\n"
    "She combs the damp out, slow, from the crown to the ends. The comb clicks once against the chair.\n"
    "\n"
    "The last of the water runs out of the basin. The shop settles around you. The afternoon has nowhere else to be.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
