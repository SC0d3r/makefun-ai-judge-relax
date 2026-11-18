import os
from pathlib import Path

TEXT = (
    "The water is still warm at your knees, and the mirror clears at the edges.\n"
    "\n"
    "One last drop leaves the tap and lands with no sound.\n"
    "\n"
    "Someone sits on the edge of the bath, and the water moves at your side. The sleeves are rolled to the elbow, and one cuff is already wet.\n"
    "\n"
    "One hand washes the back of your neck, and the other stays at your back, flat and warm.\n"
    "\n"
    "The plug comes out, and the water turns and slips away, a small pull at your legs.\n"
    "\n"
    "A towel from the radiator is warm through, and it comes around you. You are lifted. Water runs off you onto the mat.\n"
    "\n"
    "The hall is dark, with a strip of light under your door. Behind you the water is going out of the bath, and the drain sound gets smaller, then quiet.\n"
    "\n"
    "The bed is turned down, and the cat is already asleep on the end of it, and she moves over without opening her eyes.\n"
    "\n"
    "She turns once. The warm place she leaves on the bed keeps its heat. Her breathing slows into the bed.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
