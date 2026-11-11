"""One-off: move hardcoded neon colors in the stylesheets onto the brand theme tokens."""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"

RULES = [
    # Brand gradients (old neon pairs) become the Easy Peeze blue-to-teal gradient.
    (r"linear-gradient\(120deg, #3dff7a 0%, #3ad0ff 100%\)", "var(--brand-gradient)"),
    (r"linear-gradient\(145deg, #3dff7a, #b8ff4a\)", "var(--brand-gradient)"),
    (r"linear-gradient\(120deg, var\(--green\), var\(--blue\)\)", "var(--brand-gradient)"),
    # Accent RGB triplets.
    (r"rgba\(61,\s*255,\s*122,", "rgba(var(--teal-rgb),"),
    (r"rgba\(58,\s*208,\s*255,", "rgba(var(--blue-rgb),"),
    (r"rgba\(255,\s*154,\s*31,", "rgba(var(--yellow-rgb),"),
    (r"rgba\(192,\s*132,\s*252,", "rgba(var(--sky-rgb),"),
    (r"rgba\(170,\s*59,\s*255,", "rgba(var(--sky-rgb),"),
    (r"rgba\((?:6,\s*8,\s*15|8,\s*12,\s*22|12,\s*20,\s*36),", "rgba(var(--bg-rgb),"),
    # Hex accents.
    (r"#3dff7a\b", "var(--green)"),
    (r"#3ad0ff\b", "var(--blue)"),
    (r"#ff9a1f\b", "var(--orange)"),
    (r"#ffe566\b", "var(--yellow)"),
    (r"#8ad7ff\b", "var(--brand-sky)"),
    (r"#1a5cff\b", "var(--blue-deep)"),
    (r"#12a855\b", "var(--green-deep)"),
    (r"#b8ff4a\b", "var(--green)"),
    (r"#(?:06080f|070a12|05070d)\b", "var(--bg)"),
    (r"#041018\b", "var(--on-brand)"),
    # Hero and curtain grid lines need to show on both light and dark pages.
    (r"linear-gradient\(rgba\(255, 255, 255, 0\.035\) 1px", "linear-gradient(rgba(var(--fg-rgb), 0.05) 1px"),
    (r"linear-gradient\(90deg, rgba\(255, 255, 255, 0\.035\) 1px", "linear-gradient(90deg, rgba(var(--fg-rgb), 0.05) 1px"),
    # Dark-surface rings and dots.
    (r"0 0 0 1px rgba\(255, 255, 255, 0\.16\)", "0 0 0 1px var(--line)"),
    (r"border: 1px solid rgba\(255, 255, 255, 0\.35\)", "border: 1px solid var(--line-strong)"),
    (r"background: rgba\(0, 0, 0, 0\.28\);", "background: var(--input-bg);"),
    # Text that used the neon accents directly is too faint on white.
    (r"(?m)^(\s*color:\s*)var\(--green\)", r"\1var(--accent-text-2)"),
    (r"(?m)^(\s*color:\s*)var\(--blue\)", r"\1var(--accent-text)"),
    # Blend modes that only work on dark backgrounds.
    (r"mix-blend-mode:\s*screen", "mix-blend-mode: var(--blend)"),
]


def shadows(text):
    """Scale black shadows per theme so light mode does not get heavy dark smudges."""
    return re.sub(
        r"(box-shadow:[^;]*?)rgba\(0,\s*0,\s*0,\s*([0-9.]+)\)",
        lambda m: f"{m.group(1)}rgba(var(--shadow-rgb), calc({m.group(2)} * var(--shadow-k)))",
        text,
    )


for name in ("styles.css", "motion-extras.css"):
    path = SRC / name
    text = path.read_text(encoding="utf-8")
    before = text
    counts = {}
    for pattern, repl in RULES:
        text, n = re.subn(pattern, repl, text)
        if n:
            counts[pattern[:38]] = n
    for _ in range(3):
        text = shadows(text)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(name, "changed" if text != before else "unchanged", sum(counts.values()), "replacements")
    for k, v in counts.items():
        print(f"   {v:3}  {k}")
