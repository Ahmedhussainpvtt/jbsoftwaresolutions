import re
import urllib.request
from pathlib import Path


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


faq = fetch("https://jbsoftwaresolutions.com/faq/")
gloss = fetch("https://jbsoftwaresolutions.com/glossary/")

Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/jbsoftwaresolutions-staging/scripts/_prod_faq.html").write_text(faq, encoding="utf-8")
Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/jbsoftwaresolutions-staging/scripts/_prod_gloss.html").write_text(gloss, encoding="utf-8")

# Find main content region
for name, html in [("faq", faq), ("gloss", gloss)]:
    print("====", name, "len", len(html))
    # title
    m = re.search(r"<title>([^<]+)</title>", html)
    print("title:", m.group(1) if m else None)
    # hero p
    hero = re.search(r'<section class="page-hero"[\s\S]*?<h1>([^<]+)</h1>\s*<p>(.*?)</p>', html)
    if hero:
        print("h1:", hero.group(1))
        print("hero p:", re.sub(r"<[^>]+>", "", hero.group(2))[:200])
    # card patterns
    for pat in [
        r'class="faq-topic-card"',
        r'class="term-card"',
        r'class="faq-card"',
        r'class="topic-card"',
        r"<details>",
        r'href="/faq/',
        r'href="/glossary/',
    ]:
        print(pat, html.count(pat))
    # sample a card block
    if name == "faq":
        m = re.search(r'(<a[^>]*href="/faq/[^"]+"[^>]*>[\s\S]{0,800}?</a>)', html)
        if m:
            print("SAMPLE CARD:\n", m.group(1)[:600])
        # also look for grid
        for cls in re.findall(r'class="([^"]*faq[^"]*)"', html):
            pass
        classes = sorted(set(re.findall(r'class="([^"]+)"', html)))
        print("classes with faq/topic/term:", [c for c in classes if any(x in c for x in ("faq", "topic", "term", "gloss"))])
    if name == "gloss":
        m = re.search(r'(<a[^>]*href="/glossary/[^"]+"[^>]*>[\s\S]{0,600}?</a>)', html)
        if m:
            print("SAMPLE CARD:\n", m.group(1)[:500])
        classes = sorted(set(re.findall(r'class="([^"]+)"', html)))
        print("classes with faq/topic/term:", [c for c in classes if any(x in c for x in ("faq", "topic", "term", "gloss"))])
