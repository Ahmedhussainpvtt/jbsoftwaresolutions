import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


pages = [
    "/",
    "/faq/",
    "/glossary/",
    "/pricing/",
    "/about/",
    "/contact/",
    "/services/web-development/",
    "/faq/website-development-cost-india/",
    "/glossary/seo/",
]

print("=== production SEO audit ===")
for path in pages:
    html = fetch("https://jbsoftwaresolutions.com" + path)
    title = re.search(r"<title>([^<]+)</title>", html)
    desc = re.search(r'name="description" content="([^"]*)"', html)
    robots = re.search(r'name="robots" content="([^"]*)"', html)
    canon = re.search(r'rel="canonical" href="([^"]*)"', html)
    og = "og:title" in html
    tw = "twitter:card" in html
    ld = html.count("application/ld+json")
    print(
        path,
        "| title=",
        bool(title),
        "| desc=",
        bool(desc and desc.group(1)),
        "| robots=",
        (robots.group(1)[:20] if robots else None),
        "| canon=",
        (canon.group(1) if canon else None),
        "| og=",
        og,
        "| tw=",
        tw,
        "| jsonld=",
        ld,
    )

sm = fetch("https://jbsoftwaresolutions.com/sitemap.xml")
print("sitemap locs", sm.count("<loc>"))
print("robots.txt snippet:")
print(fetch("https://jbsoftwaresolutions.com/robots.txt")[:300])
try:
    ll = fetch("https://jbsoftwaresolutions.com/llms.txt")
    print("llms.txt bytes", len(ll))
except Exception as e:
    print("llms.txt FAIL", e)
