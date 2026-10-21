import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/jbsoftwaresolutions-staging/src/data")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def strip_html(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


stg = json.loads(ROOT.joinpath("faqTopics.js").read_text(encoding="utf-8").split("export default ", 1)[1])
gloss = json.loads(ROOT.joinpath("glossaryTerms.js").read_text(encoding="utf-8").split("export default ", 1)[1])

# Sample 5 FAQ topics: compare full Q+A pairs
samples = [0, 10, 27, 40, 54]
faq_fail = []
for i in samples:
    t = stg["topics"][i]
    html = fetch(f"https://jbsoftwaresolutions.com/faq/{t['slug']}/")
    pairs = re.findall(r"<details>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>", html, re.S)
    pairs = [(strip_html(q), strip_html(a)) for q, a in pairs]
    stg_pairs = [(q, a) for q, a in t["qs"]]
    if pairs != stg_pairs:
        faq_fail.append((t["slug"], len(pairs), len(stg_pairs), pairs[0] if pairs else None, stg_pairs[0] if stg_pairs else None))

print("faq sample fails", len(faq_fail))
for row in faq_fail:
    print(row)

# All glossary long defs
gloss_fail = []
for t in gloss:
    html = fetch(f"https://jbsoftwaresolutions.com/glossary/{t['slug']}/")
    m = re.search(r"<h2[^>]*>\s*Definition\s*</h2>\s*<p>(.*?)</p>", html, re.S | re.I)
    prod = strip_html(m.group(1)) if m else ""
    if prod != t["long"]:
        gloss_fail.append((t["slug"], prod[:100], t["long"][:100]))

print("gloss fails", len(gloss_fail))
for row in gloss_fail[:5]:
    print(row)

print("DONE topics", stg["topicCount"], "qs", stg["count"], "gloss", len(gloss))
