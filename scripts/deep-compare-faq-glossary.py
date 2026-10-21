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
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


stg = json.loads(ROOT.joinpath("faqTopics.js").read_text(encoding="utf-8").split("export default ", 1)[1])
gloss = json.loads(ROOT.joinpath("glossaryTerms.js").read_text(encoding="utf-8").split("export default ", 1)[1])

print("=== glossary term sample keys ===")
print(list(gloss[0].keys()))
print(json.dumps(gloss[0], indent=2)[:900])

print("\n=== faq topic sample keys ===")
print(list(stg["topics"][0].keys()))
print(json.dumps(stg["topics"][0], indent=2)[:700])

# Compare glossary definitions against production pages
print("\n=== glossary vs production ===")
gloss_mism = []
for t in gloss:
    html = fetch(f"https://jbsoftwaresolutions.com/glossary/{t['slug']}/")
    h1 = re.search(r"<h1>([^<]+)</h1>", html)
    prod_h1 = h1.group(1).strip() if h1 else ""
    # definition section: look for heading Definition then next p
    dm = re.search(
        r"<h2[^>]*>\s*Definition\s*</h2>\s*<p[^>]*>(.*?)</p>",
        html,
        re.S | re.I,
    )
    prod_def = strip_html(dm.group(1)) if dm else ""
    stg_term = t.get("term") or t.get("title") or ""
    stg_def = t.get("definition") or t.get("body") or t.get("long") or ""
    stg_short = t.get("short") or t.get("blurb") or t.get("summary") or ""
    issues = []
    if prod_h1 and stg_term and prod_h1 != stg_term:
        issues.append(f"h1 prod={prod_h1!r} stg={stg_term!r}")
    if prod_def and stg_def and prod_def != stg_def:
        issues.append(f"def mismatch\n  prod: {prod_def[:120]}\n  stg:  {stg_def[:120]}")
    if not prod_def:
        issues.append("no prod definition found")
    if issues:
        gloss_mism.append((t["slug"], issues))

print(f"glossary checked {len(gloss)}, mismatches {len(gloss_mism)}")
for slug, issues in gloss_mism[:8]:
    print(slug, issues)

# Compare FAQ topic Q/A against production
print("\n=== faq topics vs production (sample + count) ===")
faq_mism = []
for topic in stg["topics"]:
    html = fetch(f"https://jbsoftwaresolutions.com/faq/{topic['slug']}/")
    prod_qs = re.findall(r"<summary[^>]*>(.*?)</summary>", html, re.S)
    prod_qs = [strip_html(q) for q in prod_qs]
    stg_qs = [q["q"] if isinstance(q, dict) else q[0] for q in topic["qs"]]
    if len(prod_qs) != len(stg_qs):
        faq_mism.append((topic["slug"], f"count {len(prod_qs)} vs {len(stg_qs)}"))
        continue
    for i, (a, b) in enumerate(zip(prod_qs, stg_qs)):
        if a != b:
            faq_mism.append((topic["slug"], f"Q{i}: prod={a[:80]!r} stg={b[:80]!r}"))
            break

print(f"faq topics checked {len(stg['topics'])}, mismatches {len(faq_mism)}")
for row in faq_mism[:15]:
    print(row)

# Hub card titles
prod_faq = fetch("https://jbsoftwaresolutions.com/faq/")
prod_gloss = fetch("https://jbsoftwaresolutions.com/glossary/")
prod_titles = [strip_html(x) for x in re.findall(r'class="faq-topic-card[^"]*"[^>]*>.*?<h[23][^>]*>(.*?)</h[23]>', prod_faq, re.S)]
if not prod_titles:
    prod_titles = [strip_html(x) for x in re.findall(r'class="faq-topic-card[\s\S]*?<h[23][^>]*>(.*?)</h[23]>', prod_faq)]
stg_titles = [t.get("title") or t.get("name") for t in stg["topics"]]
print("\nprod faq title count", len(prod_titles), "stg", len(stg_titles))
if prod_titles and stg_titles:
    for i, (a, b) in enumerate(zip(prod_titles, stg_titles)):
        if a != b:
            print("title mismatch", i, a, "vs", b)
            break
    else:
        print("faq hub titles order match" if len(prod_titles) == len(stg_titles) else "length differ")

prod_term_titles = [strip_html(x) for x in re.findall(r'class="term-card[\s\S]*?<h[23][^>]*>(.*?)</h[23]>', prod_gloss)]
stg_term_titles = [t.get("term") or t.get("title") for t in gloss]
print("prod gloss title count", len(prod_term_titles), "stg", len(stg_term_titles))
if prod_term_titles:
    for i, (a, b) in enumerate(zip(prod_term_titles, stg_term_titles)):
        if a != b:
            print("gloss title mismatch", i, a, "vs", b)
            break
    else:
        print("gloss hub titles order match" if len(prod_term_titles) == len(stg_term_titles) else "length differ")
