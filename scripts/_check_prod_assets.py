import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache", "Pragma": "no-cache"}


def fetch(url: str) -> tuple[str, dict]:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        headers = {k.lower(): v for k, v in r.headers.items()}
        return r.read().decode("utf-8", "ignore"), headers


html, h = fetch("https://jbsoftwaresolutions.com/?nocache=1")
print("html cache-control", h.get("cache-control"))
print("html age", h.get("age"))
css = re.search(r'styles\.css\?v=([^"&]+)', html)
js = re.search(r'main\.js\?v=([^"&]+)', html)
print("styles v=", css.group(1) if css else None)
print("main v=", js.group(1) if js else None)
print("has aurora in html?", "aurora" in html)  # injected by JS, expect False
print("ASSET expected 20261021a")

if css:
    body, ch = fetch(f"https://jbsoftwaresolutions.com/styles.css?v={css.group(1)}")
    print("css bytes", len(body), "has .aurora", ".aurora {" in body or ".aurora{" in body)
    print("css has morph-blob", "morph-blob" in body)
if js:
    body, ch = fetch(f"https://jbsoftwaresolutions.com/main.js?v={js.group(1)}")
    print("js bytes", len(body), "has initAurora", "initAurora" in body)
    print("js has initMorphBlob", "initMorphBlob" in body)
    print("js has initTextScramble", "initTextScramble" in body)

# local file check
from pathlib import Path
local = Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/JB Software Solutions")
print("local ASSET_V", re.search(r'ASSET_V = "([^"]+)"', (local / "_build_pages.py").read_text(encoding="utf-8")).group(1))
print("local main has initAurora", "initAurora" in (local / "main.js").read_text(encoding="utf-8"))
