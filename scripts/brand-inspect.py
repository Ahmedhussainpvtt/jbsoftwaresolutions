from pathlib import Path

from PIL import Image

BRAND = Path(__file__).resolve().parent.parent / "brand"

for f in sorted(p for p in BRAND.iterdir() if p.suffix.lower() in (".png", ".jpg")):
    im = Image.open(f)
    line = f"{f.name:32} {im.size} mode={im.mode}"
    if "A" in im.mode:
        alpha = im.getchannel("A")
        box = alpha.point(lambda v: 255 if v > 8 else 0).getbbox()
        line += f" alpha={alpha.getextrema()} corner={alpha.getpixel((0, 0))} content={box}"
    else:
        rgb = im.convert("RGB")
        line += f" corner={rgb.getpixel((0, 0))}"
    print(line)
