import os
from pathlib import Path

from PIL import Image

BRAND = Path(__file__).resolve().parent.parent / "brand"
out = Path(os.environ["TEMP"])

for name in ("jb-icon-transparent.png", "jb-logo-full-transparent.png"):
    im = Image.open(BRAND / name).convert("RGBA")
    for label, color in (("dark", (7, 11, 20, 255)), ("light", (248, 250, 252, 255))):
        bg = Image.new("RGBA", im.size, color)
        bg.alpha_composite(im)
        bg.convert("RGB").resize((512, 341)).save(out / f"prev-{label}-{name}.png")
    # Boost faint pixels so stray marks are obvious.
    alpha = im.getchannel("A").point(lambda v: 255 if 0 < v < 60 else 0)
    Image.merge("RGB", (alpha, alpha, alpha)).resize((512, 341)).save(out / f"prev-faint-{name}.png")
print("ok")
