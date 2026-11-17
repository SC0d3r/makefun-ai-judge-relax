import os

PARAGRAPHS = [
    "The last of the sun is in the west window. The light lies low across the "
    "floorboards in one long amber panel.",
    "A potter's wheel turns in the middle of the room. The clay under her hands "
    "is a low, wet hill. The wheel is slowing. Each turn takes longer than the "
    "one before.",
    "She sits with her knees apart and her elbows on her thighs. Water runs "
    "down her wrist and stops at the crease.",
    "The wheel comes around again. Her thumb lifts on its own and presses a "
    "shallow line into the rim. The clay leans into her hand and keeps the shape.",
    "The wheel turns once more and stops. Her hands stay on the clay. The "
    "flywheel ticks twice and settles.",
    "Her feet are flat on the floor and her shoulders are low. The light has "
    "climbed to the shelf behind her, where six cups stand in a row and hold the "
    "last of the sun. The walls keep the heat of the day.",
]

TEXT = "\n\n".join(PARAGRAPHS) + "\n"
DATA = TEXT.encode("utf-8")

assert len(TEXT) < 900, len(TEXT)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as handle:
        handle.write(DATA)
    print(TEXT, end="")
    print(f"CHARACTERS: {len(TEXT)}")


if __name__ == "__main__":
    main()
