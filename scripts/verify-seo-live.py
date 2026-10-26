import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


checks = [
    ("https://jbsoftwaresolutions.com/", "home"),
    ("https://jbsoftwaresolutions.com/faq/website-development-cost-india/", "faq"),
    ("https://jbsoftwaresolutions.com/glossary/seo/", "gloss"),
    ("https://jbsoftwaresolutions.com/services/web-development/", "svc"),
]
for url, name in checks:
    html = fetch(url)
    title = re.search(r"<title>([^<]+)</title>", html)
    kw = re.search(r'name="keywords" content="([^"]*)"', html)
    canon = re.search(r'rel="canonical" href="([^"]*)"', html)
    print(
        name,
        "| title=",
        (title.group(1)[:60] if title else None),
        "| kw=",
        bool(kw and kw.group(1)),
        "| canon=",
        (canon.group(1) if canon else None),
        "| FAQPage=",
        "FAQPage" in html,
        "| seo-static=",
        "seo-static" in html,
        "| ld=",
        html.count("application/ld+json"),
    )

sm = fetch("https://jbsoftwaresolutions.com/sitemap.xml")
print("sitemap locs", sm.count("<loc>"))
