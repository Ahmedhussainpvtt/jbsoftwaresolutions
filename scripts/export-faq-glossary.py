# -*- coding: utf-8 -*-
"""Export production FAQ + glossary data into staging React modules."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(r"c:\Users\Alex\OneDrive\Desktop\ExpenseTracker")
JB = ROOT / "JB Software Solutions"
OUT = ROOT / "jbsoftwaresolutions-staging" / "src" / "data"

sys.path.insert(0, str(JB))
from _faq_bank import all_faq_topics, count_faqs  # noqa: E402

BRAND = "JB Software Solutions"
EMAIL = "info@jbsoftwaresolutions.com"

# Keep in sync with JB Software Solutions/_build_pages.py GLOSSARY
GLOSSARY = [
    ("custom-software-development", "Custom software development", "Building software made for one business instead of buying a ready-made product.", "Custom software development means designing and building tools around your real workflows. {BRAND} builds custom software for Indian startups and growing companies, with clear scope and full ownership handed to the client."),
    ("website-development", "Website development", "Creating a business website that explains your offer and captures enquiries.", "Website development is the work of planning, designing and building a site people can use on phone and desktop. At {BRAND}, website development includes clear offers, contact forms and basic search setup."),
    ("web-app-development", "Web app development", "Building a product that runs in the browser with login and workflows.", "Web app development is for tools people use daily in a browser: dashboards, portals and online products. {BRAND} ships focused first versions with milestones and handover docs."),
    ("mobile-app-development", "Mobile app development", "Building apps for Android and iPhone phones and tablets.", "Mobile app development creates apps people install from Google Play or the App Store. {BRAND} helps founders launch a focused first app, often in about 8 to 12 weeks."),
    ("desktop-app-development", "Desktop app development", "Software that installs on a computer when a website is not enough.", "Desktop app development is for tools that need offline use, special devices, or office setups where browsers are limited. {BRAND} builds installable desktop apps with update support."),
    ("seo", "SEO", "Search engine optimization: helping people find you on Google.", "SEO means improving your website so the right people can find you on Google. {BRAND} pairs SEO with the product build so launch day is not day zero of discoverability."),
    ("aeo", "AEO", "Answer engine optimization: showing up in short answer results.", "AEO (answer engine optimization) is writing and structuring content so search systems can use it as a direct answer. {BRAND} builds FAQ-style proof pages that help AEO."),
    ("geo-generative-engine-optimization", "GEO", "Generative engine optimization: helping AI tools mention your brand.", "GEO (generative engine optimization) is the practice of making your brand easy for AI assistants to cite. {BRAND} creates clear service and proof pages so ChatGPT, Gemini and Perplexity can mention you."),
    ("workflow-automation", "Workflow automation", "Connecting tools so repetitive work happens without copy-paste.", "Workflow automation links forms, chat, CRM and reminders so leads and tasks move without manual chasing. {BRAND} builds practical automation for sales and ops teams."),
    ("crm-software", "CRM software", "A system to track leads, customers and follow-ups in one place.", "CRM software stores customer conversations and next steps so nothing is lost in WhatsApp or spreadsheets. {BRAND} builds custom CRM-style tools when off-the-shelf tools do not fit."),
    ("erp-software", "ERP software", "Software that connects core business processes like stock, orders and finance.", "ERP software ties major business processes together. {BRAND} builds focused ERP-style modules when a full mega-suite is too heavy."),
    ("saas", "SaaS", "Software as a service: a product customers use online on a subscription.", "SaaS is an online product customers log into and pay for over time. {BRAND} helps founders ship the first usable slice of a SaaS product."),
    ("mvp", "MVP", "Minimum viable product: the smallest first version that proves value.", "An MVP is a first version with only the features needed to learn from real users. {BRAND} scopes first versions tightly so founders can launch without waiting months."),
    ("fixed-scope-project", "Fixed-scope project", "A project with written deliverables, timeline and price before build starts.", "A fixed-scope project agrees what will be delivered and for how much before coding begins. {BRAND} prefers written scope so buyers are not surprised mid-build."),
    ("software-ip-ownership", "Software IP ownership", "Who owns the code and design after the project is done.", "Software IP ownership should sit with the client for work built for them. {BRAND} includes source and asset handover so you are not locked in."),
    ("lead-generation-website", "Lead generation website", "A site built to turn visitors into enquiries, not just look pretty.", "A lead generation website focuses on clear offers, trust and easy contact. {BRAND} builds enquiry-first websites for service businesses in India."),
    ("app-store-launch", "App store launch", "Publishing an app on Google Play or the Apple App Store.", "App store launch covers accounts, store listings, screenshots and review. {BRAND} supports publishing as part of mobile app projects."),
    ("internal-tools", "Internal tools", "Software your own team uses to run the business day to day.", "Internal tools replace messy sheets and chat with one system staff actually open. {BRAND} builds internal tools around real roles and handoffs."),
    ("page-speed", "Page speed", "How fast a website loads on phones and computers.", "Page speed affects user trust and search visibility. {BRAND} sets speed targets on website and web app builds."),
    ("conversion-rate", "Conversion rate", "The share of visitors who take a useful action, like sending a form.", "Conversion rate measures whether the site turns attention into enquiries or sales. {BRAND} designs pages and forms to improve that path."),
    ("schema-markup", "Schema markup", "Extra labels on a page that help search and AI systems understand it.", "Schema markup is structured information that explains what a page is about. {BRAND} adds schema on service and FAQ pages so Google and AI tools can read them cleanly."),
    ("llms-txt", "llms.txt", "A text file that helps AI systems understand a website.", "llms.txt is a plain-text map of important pages for AI crawlers. {BRAND} publishes llms.txt so assistants can find accurate service and pricing facts."),
    ("india-software-development-company", "India software development company", "A team in India that builds software for local and global clients.", "An India software development company designs and builds digital products at India-friendly rates with remote delivery. {BRAND} is a small India software agency focused on websites, apps, SEO and automation."),
    ("hire-developers-india", "Hire developers in India", "Engaging an India team to build or improve your product.", "Hiring developers in India can mean a dedicated pod or a fixed project. {BRAND} offers scoped quotes with founder-accessible communication."),
    ("whatsapp-business-automation", "WhatsApp business automation", "Using rules and tools so WhatsApp messages trigger follow-ups automatically.", "WhatsApp business automation reduces lost leads by sending reminders and logging chats into a system. {BRAND} can connect WhatsApp-related workflows into wider ops automation."),
    ("google-business-profile", "Google Business Profile", "Your free business listing on Google Maps and local search.", "Google Business Profile helps local buyers find and trust you. {BRAND} can align site content and local SEO with your profile."),
    ("core-web-vitals", "Core Web Vitals", "Google's main measures of how fast and stable a page feels.", "Core Web Vitals track loading, interactivity and layout stability. {BRAND} designs websites with these measures in mind without drowning buyers in jargon."),
    ("offline-first-app", "Offline-first app", "An app that still works when the internet is weak or missing.", "An offline-first app stores work locally and syncs later. {BRAND} builds offline-capable desktop and field tools when connectivity is unreliable."),
    ("product-discovery", "Product discovery", "The short planning phase before build, to agree goals and scope.", "Product discovery clarifies users, outcomes and constraints before coding. {BRAND} starts serious projects with discovery so quotes stay honest."),
    ("retainer", "Retainer", "A monthly engagement for ongoing work like SEO or product updates.", "A retainer keeps improvements moving after launch. {BRAND} offers retainers for SEO, visibility and product iteration."),
]


def fill(text: str) -> str:
    return text.replace("{BRAND}", BRAND).replace("{EMAIL}", EMAIL)


def write_js(name: str, value) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_text("export default " + json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name, "items", len(value) if isinstance(value, list) else "obj")


def main() -> None:
    topics = []
    for t in all_faq_topics():
        topics.append(
            {
                "slug": t["slug"],
                "title": fill(t["title"]),
                "desc": fill(t["desc"]),
                "qs": [[fill(q), fill(a)] for q, a in t["qs"]],
            }
        )

    gloss = []
    for slug, title, short, long_tpl in GLOSSARY:
        gloss.append(
            {
                "slug": slug,
                "title": title,
                "short": short,
                "long": fill(long_tpl),
            }
        )

    preview = []
    for t in topics:
        preview.extend(t["qs"][:2])

    write_js(
        "faqTopics.js",
        {
            "count": count_faqs(),
            "topicCount": len(topics),
            "topics": topics,
            "preview": preview,
        },
    )
    write_js("glossaryTerms.js", gloss)


if __name__ == "__main__":
    main()
