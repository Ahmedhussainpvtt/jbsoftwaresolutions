#!/usr/bin/env python3
"""Generate llms.txt + llms-full.txt (+ LLM.txt alias) for JB Software Solutions.

Same pattern as Kharch Log / Easy Peeze (llmstxt.org).
Reads sitemap.xml after seo-build.js.
"""
from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOMAIN = "https://jbsoftwaresolutions.com"
SITE_NAME = "JB Software Solutions"
TODAY = date.today().isoformat()
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
CONTACT = "info@jbsoftwaresolutions.com"

DESCS = {
    "/": "Custom software development company in India for web, mobile, desktop, SEO, AEO, GEO and AI automation.",
    "/about/": "About JB Software Solutions - product engineering plus AI-era discovery under one roof.",
    "/contact/": "Contact form for software, apps and SEO/GEO project quotes.",
    "/blog/": "Guides on GEO, AEO, custom software cost in India, and Flutter vs React Native.",
    "/services/web-development/": "Next.js and React web development with SEO foundations.",
    "/services/mobile-app-development/": "Flutter and React Native mobile app development for Android and iOS.",
    "/services/custom-software/": "Custom CRM, ERP, SaaS and internal tool development with IP handover.",
    "/services/seo-aeo-geo/": "Technical SEO, AEO and Generative Engine Optimization for Google and ChatGPT citations.",
    "/services/ai-automation/": "AI agents, RAG and workflow automation for sales, support and ops.",
    "/services/desktop-apps/": "Electron and Tauri desktop app development for offline and hardware-heavy tools.",
    "/blog/what-is-geo-aeo-llm-seo-2026/": "What GEO, AEO and LLM SEO mean in 2026 and how to get cited.",
    "/blog/custom-software-development-cost-india-2026/": "India 2026 custom software cost ranges and what moves the quote.",
    "/blog/flutter-vs-react-native-mvp-india-2026/": "Flutter vs React Native decision guide for India MVPs.",
}

FACTS = [
    "Brand: JB Software Solutions",
    "Services: custom software, web development, mobile apps, desktop apps, SEO, AEO, GEO, AI automation",
    "Contact: info@jbsoftwaresolutions.com (use the contact form on the site)",
    "Site: https://jbsoftwaresolutions.com/",
    "Competes with full-stack India agencies selling apps + SEO/GEO; differentiates with build + discovery in one team",
]


def slug_title(slug: str) -> str:
    return slug.replace("-", " ").strip().title()


def path_of(url: str) -> str:
    return url.replace(DOMAIN, "") or "/"


def load_sitemap_urls(sitemap: Path) -> list[str]:
    tree = ET.parse(sitemap)
    root = tree.getroot()
    urls = []
    for loc in root.findall(".//sm:loc", NS):
        u = (loc.text or "").strip()
        if u.startswith(DOMAIN):
            urls.append(u)
    return urls


def describe(path: str) -> str:
    if path in DESCS:
        return DESCS[path]
    parts = [p for p in path.strip("/").split("/") if p]
    if not parts:
        return "Home page."
    section, *rest = parts
    leaf = rest[-1] if rest else section
    title = slug_title(leaf)
    if section == "blog":
        return f"Blog: {title}."
    if section == "services":
        return f"Service: {title}."
    return f"{title}."


def sectionize(urls: list[str]) -> dict[str, list[tuple[str, str, str]]]:
    buckets: dict[str, list[tuple[str, str, str]]] = {
        "Company": [],
        "Services": [],
        "Blog": [],
        "Optional": [],
    }
    for url in urls:
        path = path_of(url)
        desc = describe(path)
        if path.startswith("/services/"):
            buckets["Services"].append((slug_title(path.strip("/").split("/")[-1]), url, desc))
        elif path.startswith("/blog/") and path != "/blog/":
            buckets["Blog"].append((slug_title(path.strip("/").split("/")[-1]), url, desc))
        elif path in ("/privacy/", "/terms/", "/404.html"):
            buckets["Optional"].append((slug_title(path.strip("/") or "page"), url, desc))
        else:
            title_map = {
                "/": "Home",
                "/about/": "About",
                "/contact/": "Contact",
                "/blog/": "Blog index",
            }
            buckets["Company"].append((title_map.get(path, slug_title(path.strip("/") or "page")), url, desc))
    return buckets


def render_llms(buckets: dict[str, list[tuple[str, str, str]]]) -> str:
    lines = [
        f"# {SITE_NAME}",
        "",
        "> JB Software Solutions is a custom software development company in India offering web development, "
        "mobile app development (Flutter and React Native), desktop apps (Electron and Tauri), custom CRM/ERP software, "
        "technical SEO, AEO, GEO / LLM SEO, and AI automation for startups and growing businesses.",
        "",
        f"Last updated: {TODAY}",
        f"Canonical site: {DOMAIN}/",
        f"Sitemap: {DOMAIN}/sitemap.xml",
        f"Full corpus: {DOMAIN}/llms-full.txt",
        f"Contact: {CONTACT}",
        "",
        "## Key facts",
        "",
    ]
    for f in FACTS:
        lines.append(f"- {f}")
    lines.append("")

    for heading in ("Company", "Services", "Blog", "Optional"):
        items = list(buckets.get(heading) or [])
        if heading == "Optional":
            items.append(("robots.txt", f"{DOMAIN}/robots.txt", "Crawl rules and sitemap pointer."))
            items.append(("llms-full.txt", f"{DOMAIN}/llms-full.txt", "Compact product corpus for AI agents."))
            items.append(("LLM.txt", f"{DOMAIN}/LLM.txt", "Alias of llms.txt for LLM crawlers."))
        if not items:
            continue
        lines.append(f"## {heading}")
        lines.append("")
        for title, url, desc in items:
            lines.append(f"- [{title}]({url}): {desc}")
        lines.append("")
    return "\n".join(lines)


def render_full(buckets: dict) -> str:
    lines = [
        f"# {SITE_NAME} - llms-full.txt",
        "",
        f"Generated: {TODAY}",
        f"Source: {DOMAIN}/",
        f"Index: {DOMAIN}/llms.txt",
        "",
        "Custom software, web, mobile, desktop, SEO/AEO/GEO and AI automation from India.",
        "",
        "## Facts",
        "",
    ]
    for f in FACTS:
        lines.append(f"- {f}")
    lines.append("")
    for heading, items in buckets.items():
        if not items or heading == "Optional":
            continue
        lines.append(f"## {heading}")
        lines.append("")
        for title, url, desc in items:
            lines.append(f"### {title}")
            lines.append(f"URL: {url}")
            lines.append(desc)
            lines.append("")
    return "\n".join(lines)


def main() -> None:
    sitemap = ROOT / "sitemap.xml"
    if not sitemap.exists():
        raise SystemExit("sitemap.xml missing - run npm run seo first")
    urls = load_sitemap_urls(sitemap)
    buckets = sectionize(urls)
    llms = render_llms(buckets)
    full = render_full(buckets)
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")
    (ROOT / "LLM.txt").write_text(llms, encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(full, encoding="utf-8")
    print(f"wrote llms.txt / LLM.txt ({len(urls)} urls)")
    print("wrote llms-full.txt")


if __name__ == "__main__":
    main()
