import os

PARAGRAPHS = (
    "The last of the sun comes through the west window and lies on the "
    "kitchen table in a long gold panel.",
    "It has been sliding across the wood all afternoon. Now it moves by "
    "inches, and its near edge thins.",
    "A man sits at the table with his sleeves rolled and a cup between his "
    "hands. The tea has gone lukewarm. Flour dries in a pale stripe on his "
    "forearm.",
    "The light reaches the pear in the blue bowl. It rests on the pear's "
    "skin, then slips off onto the wood.",
    "His foot slides forward out of its shoe without his deciding to. The "
    "shoe stays where it was, heel down, on the rug.",
    "The light climbs the wall and stops under the sill. The radiator ticks "
    "and warms. The pear rests in the bowl, the cup on the table, and the "
    "chair takes his weight.",
)

TEXT = "\n\n".join(PARAGRAPHS) + "\n"
DATA = TEXT.encode("utf-8")
assert len(TEXT) < 900, len(TEXT)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")
with open(OUT_PATH, "wb") as handle:
    handle.write(DATA)

print(TEXT, end="")
print("CHARACTERS:", len(TEXT))
