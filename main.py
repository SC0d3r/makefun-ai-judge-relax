import os

PARAGRAPHS = [
    "Late light comes in low through the west window. It lies across the floor "
    "in a long yellow band.",
    "The band touches the leg of a wooden chair and climbs it slowly. The grain "
    "of the wood shows in the light, warm and close.",
    "A woman sits in the chair with her hands loose in her lap. Her shoes are "
    "off, set side by side on the rug, one heel against the other.",
    "The light moves up the arm of the chair and onto the blanket folded there. "
    "The wool is pale and soft. It holds the color and goes quiet.",
    "The band narrows as the sun drops behind the rooftops. It draws back "
    "toward the window, thinner and dimmer, and comes to rest on the sill.",
    "She stays where she is, her head back against the chair. The walls keep "
    "their one warm shade. The room holds its warmth around her.",
]

TEXT = "\n\n".join(PARAGRAPHS) + "\n"
data = TEXT.encode("utf-8")
assert len(TEXT) < 1000, len(TEXT)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "wb") as f:
    f.write(data)

print("WROTE:", out_path)
print("CHARACTERS:", len(TEXT))
print()
print(TEXT, end="")
