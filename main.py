import os
from pathlib import Path

TEXT = (
    "The water is still warm at your knees, and the mirror clears at the edges, slow, like a window in winter.\n"
    "\n"
    "One last drop leaves the tap and lands with no sound. The tap is dry and cool.\n"
    "\n"
    "A hand rests on the edge and the water moves at your side. The sleeves are rolled to the elbow, and one cuff is wet.\n"
    "\n"
    "One hand washes the back of your neck, and the other stays at your back, flat and warm.\n"
    "\n"
    "The plug comes out, and the water turns and slips away, a small pull at your legs.\n"
    "\n"
    "A towel from the radiator is soft in both hands. You are lifted. Water spills off you onto the mat, quick and light. The mat is wet.\n"
    "\n"
    "The hall is dark, with a strip of light under your door.\n"
    "\n"
    "The bed is turned down, and the cat is asleep on the end of it, edging over, her eyes closed.\n"
    "\n"
    "Back in the bath, the water sinks away. The drain sound is small, then faint, then only hush. You are warm. The house is asleep around you, and morning is far off.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
