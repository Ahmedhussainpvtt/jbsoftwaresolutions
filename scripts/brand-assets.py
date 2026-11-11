"""Builds the site's logo, favicon and share images from the masters in brand/."""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "brand"
PUBLIC = ROOT / "public"
ASSETS = PUBLIC / "assets"
WHITE = (255, 255, 255, 255)


def load_clean(name):
    """Drop the near-invisible noise pixels around the artwork, then trim to the artwork."""
    im = Image.open(BRAND / name).convert("RGBA")
    alpha = im.getchannel("A").point(lambda v: 0 if v < 40 else v)
    im.putalpha(alpha)
    return im.crop(alpha.getbbox())


def square(im, pad_ratio):
    side = int(max(im.size) * (1 + pad_ratio * 2))
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.alpha_composite(im, ((side - im.width) // 2, (side - im.height) // 2))
    return canvas


def on_white(im):
    bg = Image.new("RGBA", im.size, WHITE)
    bg.alpha_composite(im)
    return bg.convert("RGB")


icon = square(load_clean("jb-icon-transparent.png"), 0.04)
full = load_clean("jb-logo-full-transparent.png")

icon.resize((96, 96), Image.LANCZOS).save(ASSETS / "logo-mark-96.webp", quality=92, method=6)
icon.resize((512, 512), Image.LANCZOS).save(ASSETS / "logo-mark.png", optimize=True)
full.save(ASSETS / "logo-full.png", optimize=True)

icon.resize((48, 48), Image.LANCZOS).save(PUBLIC / "favicon-48.png", optimize=True)
icon.resize((32, 32), Image.LANCZOS).save(PUBLIC / "favicon-32.png", optimize=True)
icon.save(PUBLIC / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

touch = square(load_clean("jb-icon-transparent.png"), 0.14)
on_white(touch.resize((180, 180), Image.LANCZOS)).save(PUBLIC / "apple-touch-icon.png", optimize=True)
on_white(touch.resize((512, 512), Image.LANCZOS)).save(PUBLIC / "favicon.jpg", quality=92)
on_white(touch.resize((512, 512), Image.LANCZOS)).save(ASSETS / "favicon.jpg", quality=92)

og = Image.new("RGBA", (1200, 630), WHITE)
target_h = 430
logo = full.resize((round(full.width * target_h / full.height), target_h), Image.LANCZOS)
og.alpha_composite(logo, ((1200 - logo.width) // 2, (630 - logo.height) // 2))
og.convert("RGB").save(ASSETS / "og-image.jpg", quality=90, optimize=True)

for f in ("logo-mark-96.webp", "logo-mark.png", "logo-full.png", "og-image.jpg", "favicon.jpg"):
    print(f"{f:20} {(ASSETS / f).stat().st_size:>8} bytes")
for f in ("favicon-48.png", "favicon-32.png", "favicon.ico", "apple-touch-icon.png"):
    print(f"{f:20} {(PUBLIC / f).stat().st_size:>8} bytes")
