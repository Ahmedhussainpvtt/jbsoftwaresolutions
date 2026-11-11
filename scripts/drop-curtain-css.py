"""One-off: remove the route-wipe curtain styles from motion-extras.css."""
import re
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "src" / "motion-extras.css"
css = path.read_text(encoding="utf-8")
before = css

css = re.sub(r"/\* Route wipe curtain \*/\n.*?(?=/\* Morphing hero blob \*/)", "", css, flags=re.S)
css = re.sub(r"\n\.page-curtain\.is-lite \{[^}]*\}\n", "\n", css)
css = re.sub(r"\n\s*\.page-curtain-label \{\s*font-size: 2\.2rem;\s*\}\n", "\n", css)
css = css.replace("  .page-curtain-shine,\n", "").replace("  .page-curtain,\n", "")

path.write_text(css, encoding="utf-8", newline="\n")
print("removed", len(before) - len(css), "chars; curtain left:", css.count("curtain"))
