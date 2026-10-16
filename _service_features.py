# -*- coding: utf-8 -*-
"""Alternating image/content feature rows for JB service pages."""

BRAND = "JB Software Solutions"


def features():
    """slug -> list of {title, text, img} where img is a SERVICE_IMG key or filename."""
    return {
        "web-development": [
            {
                "title": "Clear offers that turn visits into enquiries",
                "text": f"{BRAND} structures every business website around what you sell, who it is for, and the next step a buyer should take. No vague hero copy. No buried contact forms. Pages are written so Google and people both understand the offer.",
                "img": "aside",
            },
            {
                "title": "How we work on website projects",
                "text": "Discover the brief, map the sitemap, design mobile-first pages, then launch with basic SEO and a handover. You see progress weekly. You keep the domain, hosting accounts and the work we create for you.",
                "img": "mid",
            },
            {
                "title": "Built to get found, not only look finished",
                "text": "Crawlable URLs, sensible titles, FAQ room and speed checks ship with the build. Pair with our SEO, AEO and GEO retainer when you want ongoing rankings and AI citations after launch.",
                "img": "deep",
            },
            {
                "title": "What this service covers",
                "text": "Business websites, lead-generation sites, product marketing pages and redesigns of outdated WordPress or builder sites. We scope page count, content readiness and integrations before the quote is fixed.",
                "img": "legacy",
            },
        ],
        "mobile-app-development": [
            {
                "title": "One journey done well before the feature pile-on",
                "text": f"{BRAND} starts mobile apps with a single primary user path. Payments, maps, chat and extra roles are listed as features so the first version stays shippable in about 8 to 12 weeks.",
                "img": "aside",
            },
            {
                "title": "How we work on mobile apps",
                "text": "Discovery and journey map, clickable flow, weekly working builds, store listing support, then a post-launch fixes window. You own the developer accounts. We do not disappear on launch day.",
                "img": "mid",
            },
            {
                "title": "Android, iPhone, or phased stores",
                "text": "Many India launches start on Android. We can plan both stores from day one or phase iPhone after proof. Cross-platform builds are common when both stores matter and the product is not hardware-heavy.",
                "img": "deep",
            },
            {
                "title": "What this service covers",
                "text": "Consumer apps, field and staff tools, store submission support, and first versions with login, notifications and tracking when those are in scope. Always compare inclusions, not only the headline price.",
                "img": "legacy",
            },
        ],
        "custom-software": [
            {
                "title": "Software that matches how your team already works",
                "text": f"{BRAND} builds internal tools, CRM-style pipelines, portals and dashboards around real roles, not generic SaaS screenshots. Spreadsheets and WhatsApp chaos become a system staff will actually open.",
                "img": "aside",
            },
            {
                "title": "How we work on custom software",
                "text": "Discovery workshops, written scope with milestones, weekly demos, QA against acceptance criteria, then IP handover and training. You talk to people who ship, not a ticket queue that forgets your name.",
                "img": "mid",
            },
            {
                "title": "Build vs buy, decided honestly",
                "text": "Buy SaaS when it fits most of your process. Build custom when off-the-shelf tools force painful workarounds. We say so even when that means a smaller project for us.",
                "img": "deep",
            },
            {
                "title": "What this service covers",
                "text": "Custom CRM workflows, focused ERP-style modules, client portals, admin panels, SaaS first slices and API integrations. Ownership and access are agreed in writing before build starts.",
                "img": "legacy",
            },
        ],
        "seo-aeo-geo": [
            {
                "title": "Visibility for Google and AI assistants",
                "text": f"{BRAND} treats SEO, AEO and GEO as one practice. Technical fixes, service pages and FAQ clusters help people find you on Google and make your brand easier to cite in ChatGPT, Gemini and Perplexity.",
                "img": "aside",
            },
            {
                "title": "How we work on visibility retainers",
                "text": "Audit, prioritise commercial pages, ship fixes and content in steady batches, then report rankings, enquiries and AI mention checks in language you can read. No vanity dashboards.",
                "img": "mid",
            },
            {
                "title": "Content that answers buyer questions",
                "text": "We publish service pages, FAQs and glossary-style proof, not only blog fluff. That is how answer engines and generative tools pick up accurate facts about what you offer.",
                "img": "deep",
            },
            {
                "title": "What this service covers",
                "text": "Technical SEO, on-page structure, content clusters, AEO, GEO, schema where useful and local SEO when location matters. Pair with a website rebuild when the site itself is the bottleneck.",
                "img": "legacy",
            },
        ],
        "ai-automation": [
            {
                "title": "Automate the boring path between your tools",
                "text": f"{BRAND} maps lead capture, CRM updates, follow-ups and approvals so your team stops copy-pasting. The product is your workflow, not an experimental AI lab.",
                "img": "aside",
            },
            {
                "title": "How we work on automation projects",
                "text": "Map the painful path, pick the highest-ROI flow first, implement and test failure cases, document owners, then train the team and monitor the first weeks.",
                "img": "mid",
            },
            {
                "title": "Practical AI inside the process",
                "text": "If a step benefits from light AI assist for drafting, tagging or routing, we can wire that in. We do not sell custom RAG platforms or model-training theatre.",
                "img": "deep",
            },
            {
                "title": "What this service covers",
                "text": "Lead-to-CRM flows, approval routing, stall alerts, weekly digests, handoffs between sales and delivery, and connections across forms, email, sheets, chat and payment alerts.",
                "img": "legacy",
            },
        ],
        "desktop-apps": [
            {
                "title": "When a browser is not enough",
                "text": f"{BRAND} builds installable desktop software for offline work, device access and locked-down offices. If web or mobile is a better fit, we say so before you spend.",
                "img": "aside",
            },
            {
                "title": "How we work on desktop projects",
                "text": "Same JB standard: discovery, written scope, weekly demos, QA and IP handover. Installers and update paths are part of the plan, not an afterthought.",
                "img": "mid",
            },
            {
                "title": "Offline-first and device-aware",
                "text": "Local data with sync when connectivity returns, plus hooks for printers, scanners or serial devices when your brief needs them. Windows-first, Mac when scoped.",
                "img": "deep",
            },
            {
                "title": "What this service covers",
                "text": "Shop-floor tools, back-office utilities, field catalogues, licensed products for customer PCs, and packaging an existing web product into a desktop shell when appropriate.",
                "img": "legacy",
            },
        ],
    }
