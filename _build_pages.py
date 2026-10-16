# -*- coding: utf-8 -*-
"""Generate JB Software Solutions static site pages."""
import json
import re
from pathlib import Path

from _faq_bank import all_faq_topics, count_faqs
from _service_bodies import bodies as service_bodies
from _service_features import features as service_features

ROOT = Path(__file__).resolve().parent
SITE = "https://jbsoftwaresolutions.com"
BRAND = "JB Software Solutions"
EMAIL = "info@jbsoftwaresolutions.com"
ASSET_V = "20261017b"  # bump when styles.css / main.js change (GitHub Pages CDN cache)
SERVICE_BODIES = service_bodies()
SERVICE_FEATURES = service_features()
LEGACY_IMG = {
    "web-development": "web.jpg",
    "mobile-app-development": "mobile.jpg",
    "custom-software": "custom.jpg",
    "seo-aeo-geo": "seo.jpg",
    "ai-automation": "ai.jpg",
    "desktop-apps": "desktop.jpg",
}

SERVICES = [
    ("web-development", "Website development", "Business sites that get enquiries", "web-hero.jpg"),
    ("mobile-app-development", "Mobile app development", "Apps for phones and tablets", "mobile-hero.jpg"),
    ("custom-software", "Custom software", "Tools built for your team", "custom-hero.jpg"),
    ("seo-aeo-geo", "SEO and online visibility", "Get found on Google and AI search", "seo-hero.jpg"),
    ("ai-automation", "Workflow automation", "Cut repetitive daily work", "ai-hero.jpg"),
    ("desktop-apps", "Desktop apps", "Software that runs on a computer", "desktop-hero.jpg"),
]

SERVICE_IMG = {
    "web-development": {"hero": "web-hero.jpg", "aside": "web-aside.jpg", "mid": "web-mid.jpg", "deep": "web-deep.jpg"},
    "mobile-app-development": {"hero": "mobile-hero.jpg", "aside": "mobile-aside.jpg", "mid": "mobile-mid.jpg", "deep": "mobile-deep.jpg"},
    "custom-software": {"hero": "custom-hero.jpg", "aside": "custom-aside.jpg", "mid": "custom-mid.jpg", "deep": "custom-deep.jpg"},
    "seo-aeo-geo": {"hero": "seo-hero.jpg", "aside": "seo-aside.jpg", "mid": "seo-mid.jpg", "deep": "seo-deep.jpg"},
    "ai-automation": {"hero": "ai-hero.jpg", "aside": "ai-aside.jpg", "mid": "ai-mid.jpg", "deep": "ai-deep.jpg"},
    "desktop-apps": {"hero": "desktop-hero.jpg", "aside": "desktop-aside.jpg", "mid": "desktop-mid.jpg", "deep": "desktop-deep.jpg"},
}

RESOURCES = [
    ("blog/", "Blog", "Guides on software, apps and getting found online"),
    ("glossary/", "Glossary", "Plain definitions of software and SEO terms"),
    ("faq/", "FAQs", "Straight answers about software, apps, SEO and pricing"),
]


def rel(depth: int) -> str:
    return "../" * depth if depth else ""


def head(title, desc, keywords, path, depth, og_type="website", image="/assets/og-image.jpg", extra_jsonld=""):
    p = rel(depth)
    canon = f"{SITE}{path}"
    img = image if image.startswith("http") else f"{SITE}{image}"
    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{keywords}" />
  <meta name="author" content="{BRAND}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="googlebot" content="index, follow" />
  <meta name="theme-color" content="#05070f" />
  <meta name="application-name" content="{BRAND}" />
  <meta name="geo.region" content="IN" />
  <meta name="geo.placename" content="India" />
  <link rel="canonical" href="{canon}" />
  <link rel="sitemap" href="{SITE}/sitemap.xml" type="application/xml" title="Sitemap" />
  <link rel="alternate" type="text/plain" title="LLM context" href="{SITE}/llms.txt" />
  <link rel="alternate" type="text/plain" title="LLM context alternate" href="{SITE}/LLM.txt" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}styles.css?v={ASSET_V}" />
  <link rel="icon" href="{p}assets/favicon.jpg" type="image/jpeg" />
  <link rel="apple-touch-icon" href="{p}assets/logo-mark.png" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:site_name" content="{BRAND}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:image" content="{img}" />
  <meta property="og:locale" content="en_IN" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{img}" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "@id": "{SITE}/#organization",
        "name": "{BRAND}",
        "url": "{SITE}/",
        "logo": "{SITE}/assets/logo-mark.png",
        "email": "{EMAIL}",
        "areaServed": "IN",
        "sameAs": ["https://github.com/Ahmedhussainpvtt/jbsoftwaresolutions"]
      }},
      {{
        "@type": "WebSite",
        "@id": "{SITE}/#website",
        "url": "{SITE}/",
        "name": "{BRAND}",
        "publisher": {{ "@id": "{SITE}/#organization" }},
        "inLanguage": "en-IN"
      }},
      {{
        "@type": "WebPage",
        "@id": "{canon}#webpage",
        "url": "{canon}",
        "name": "{title}",
        "description": "{desc}",
        "isPartOf": {{ "@id": "{SITE}/#website" }},
        "publisher": {{ "@id": "{SITE}/#organization" }},
        "inLanguage": "en-IN"
      }}
    ]
  }}
  </script>
  {extra_jsonld}
</head>
"""


def nav(depth, active=""):
    p = rel(depth)
    services_on = ' is-active' if active == "services" else ""
    resources_on = ' is-active' if active in ("blog", "glossary", "faq", "resources") else ""
    drop_items = "\n".join(
        f'<li><a href="{p}services/{slug}/"><span class="nav-drop-title">{label}</span>'
        f'<span class="nav-drop-desc">{blurb}</span></a></li>'
        for slug, label, blurb, _img in SERVICES
    )
    resource_items = "\n".join(
        f'<li><a href="{p}{href}"><span class="nav-drop-title">{label}</span>'
        f'<span class="nav-drop-desc">{blurb}</span></a></li>'
        for href, label, blurb in RESOURCES
    )
    def a(key, href, label):
        cls = ' class="is-active"' if active == key else ""
        return f'<li><a href="{p}{href}"{cls}>{label}</a></li>'
    return f"""
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="{p}">
      <img src="{p}assets/logo-mark.png" width="44" height="44" alt="{BRAND} logo" />
      <span>JB Software<em>Solutions</em></span>
    </a>
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false">Menu</button>
    <ul class="nav-links">
      <li class="has-dropdown">
        <button type="button" class="nav-drop-toggle{services_on}" aria-expanded="false" aria-haspopup="true">Services <span class="nav-chev" aria-hidden="true"></span></button>
        <ul class="nav-dropdown" role="menu">{drop_items}</ul>
      </li>
      <li class="has-dropdown">
        <button type="button" class="nav-drop-toggle{resources_on}" aria-expanded="false" aria-haspopup="true">Resources <span class="nav-chev" aria-hidden="true"></span></button>
        <ul class="nav-dropdown" role="menu">{resource_items}</ul>
      </li>
      {a("pricing", "pricing/", "Pricing")}
      {a("about", "about/", "About")}
      <li><a class="nav-cta" href="{p}contact/">Get a quote</a></li>
    </ul>
  </div>
</header>
"""


def dock(depth):
    p = rel(depth)
    return f"""
<div class="sticky-dock" aria-label="Quick contact">
  <a class="dock-btn quote" href="{p}contact/" aria-label="Contact us">Contact</a>
</div>
"""


def footer(depth):
    p = rel(depth)
    return f"""
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <strong>{BRAND}</strong>
      <p>Custom software, mobile apps, websites, desktop apps, SEO, AEO, GEO, and workflow automation for startups and growing businesses in India and worldwide.</p>
    </div>
    <div>
      <strong>Build</strong>
      <a href="{p}services/web-development/">Web development</a>
      <a href="{p}services/mobile-app-development/">Mobile apps</a>
      <a href="{p}services/custom-software/">Custom software</a>
      <a href="{p}services/desktop-apps/">Desktop apps</a>
    </div>
    <div>
      <strong>Grow</strong>
      <a href="{p}services/seo-aeo-geo/">SEO and visibility</a>
      <a href="{p}services/ai-automation/">Workflow automation</a>
      <a href="{p}pricing/">Pricing</a>
      <a href="{p}blog/">Blog</a>
    </div>
    <div>
      <strong>Company</strong>
      <a href="{p}about/">About</a>
      <a href="{p}glossary/">Glossary</a>
      <a href="{p}faq/">FAQs</a>
      <a href="{p}contact/">Contact us</a>
      <a href="{p}privacy/">Privacy policy</a>
      <a href="{p}terms/">Terms</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; 2026 {BRAND}. All rights reserved.</span>
    <span><a href="{p}privacy/">Privacy</a> · <a href="{p}terms/">Terms</a> · Custom software | Mobile apps | Websites | SEO | Automation</span>
  </div>
</footer>
{dock(depth)}
<script src="{p}main.js?v={ASSET_V}" defer></script>
</body>
</html>
"""


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


KW_HOME = (
    "custom software development company India, custom software development services, "
    "website development company India, web development company, web application development company, "
    "mobile app development company India, Android app development, iPhone app development, "
    "SEO company India, technical SEO services, AEO services, GEO services, generative engine optimization, "
    "LLM SEO, ChatGPT SEO, hire developers India, hire software development company India, "
    "business workflow automation, CRM automation, desktop app development, "
    "SaaS product development, custom CRM development, ERP software development, "
    "software outsourcing company, custom software development cost India, JB Software Solutions"
)

# ---------- HOME ----------
home_lines = [
    "> JB Software Solutions",
    "> Custom software · websites · mobile apps · SEO",
    "> Build products people find and use",
    "> Next.js · Flutter · Node · workflow automation",
    "> Clear scope. Written quotes. You own the work.",
    "> Ready when you are.",
]
home = head(
    f"{BRAND} | Custom Software Development Company India | Websites, Mobile Apps, SEO",
    "JB Software Solutions is a custom software development company in India for website development, mobile app development, web apps, desktop software, SEO, AEO, GEO and business workflow automation. Hire developers in India who ship products that get found on Google and cited in ChatGPT.",
    KW_HOME,
    "/",
    0,
    extra_jsonld=f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "{BRAND}",
    "url": "{SITE}/",
    "image": "{SITE}/assets/logo-full.png",
    "description": "Custom software development company in India offering web development, mobile app development, desktop apps, SEO, AEO, GEO and workflow automation.",
    "priceRange": "$$",
    "areaServed": ["IN", "AE", "SA", "US", "GB", "AU"],
    "email": "{EMAIL}",
    "knowsAbout": ["Custom software development", "Web development", "Mobile app development", "SEO", "AEO", "GEO", "Business workflow automation", "Electron desktop apps"]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "What does JB Software Solutions do?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "JB Software Solutions builds custom software, websites, mobile apps and desktop apps, and grows them with SEO, AEO, GEO and workflow automation for clients in India and internationally."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Do you offer SEO, AEO and GEO services?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes. Technical SEO for Google, Answer Engine Optimization for featured answers, and Generative Engine Optimization so brands get cited inside ChatGPT, Gemini, Perplexity and Google AI Overviews."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How much does custom software development cost in India?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Focused web MVPs often start in the low lakhs INR. Mobile MVPs and multi-role internal systems scale with integrations, compliance and platforms. We quote fixed or phased scope after a free discovery call."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How is JB Software Solutions different from other India software agencies?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "We keep product engineering and AI-era discovery (SEO, AEO, GEO) in one accountable team, ship with founder-accessible communication, and design every build to convert and get cited, not just look finished in a portfolio."
        }}
      }}
    ]
  }}
  </script>
""",
) + f"""
<body>
{nav(0, "home")}
<main>
  <section class="hero">
    <div class="hero-bg" aria-hidden="true">
      <canvas id="ai-field"></canvas>
      <div class="hero-mesh"></div>
      <div class="hero-grid"></div>
      <div class="hero-orb hero-orb-a"></div>
      <div class="hero-orb hero-orb-b"></div>
    </div>
    <div class="container hero-inner">
      <div class="hero-layout">
        <div class="hero-copy">
          <h1 class="hero-title">Your Vision. Our Code. <span class="grad">Limitless Possibilities.</span></h1>
          <p class="hero-sub">From custom software and mobile apps to modern websites, we turn your ideas into powerful digital solutions built around your business.</p>
          <div class="hero-cta">
            <a class="btn btn-primary btn-magnet" href="contact/">Get a free strategy call</a>
            <a class="btn btn-ghost btn-magnet" href="pricing/">See pricing</a>
          </div>
        </div>
        <div class="hero-stage">
          <div class="ai-proof">
            <div class="ai-terminal" data-lines='{__import__("json").dumps(home_lines)}'>
              <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
              <div class="term-out"></div>
            </div>
            <div class="pixel-row" aria-hidden="true">
              <span class="pixel"></span><span class="pixel"></span><span class="pixel"></span>
              <span class="pixel"></span><span class="pixel"></span><span class="pixel"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      <span>Custom software development company India</span><span>Website development company</span>
      <span>Mobile app development company</span><span>Web application development</span>
      <span>SEO company India</span><span>AEO and GEO</span>
      <span>Hire developers India</span><span>Business workflow automation</span>
      <span>Desktop app development</span><span>Software outsourcing India</span>
      <span>SaaS product development</span><span>CRM and ERP software</span>
    </div>
  </div>

  <section class="section" id="trust" style="padding-top:2.5rem;padding-bottom:1rem">
    <div class="container">
      <div class="trust-strip reveal">
        <article><strong>Reply within 24 hours</strong><span>Human response on every serious brief, usually faster on business days.</span></article>
        <article><strong>You own the IP</strong><span>Source code and assets stay with you. No hostage licensing.</span></article>
        <article><strong>Fixed or phased quotes</strong><span>Written scope before build. No surprise invoices mid-sprint.</span></article>
        <article><strong>Build + SEO together</strong><span>Launch day is not day zero of discoverability.</span></article>
      </div>
    </div>
  </section>

  <section class="section manifesto" id="manifesto">
    <div class="container">
      <div class="section-kicker reveal">How we build</div>
      <h2 class="manifesto-title reveal">The website is not a brochure.<br /><span class="grad">It is the first product you ship.</span></h2>
      <p class="manifesto-sub reveal">We treat your site like a product: clear offer, measurable outcome, motion with purpose, and a contact path that feels easy. Same bar for apps, custom tools and search work.</p>
      <div class="manifesto-metrics reveal">
        <div><strong>01</strong><span>Proof before pitch</span></div>
        <div><strong>02</strong><span>Ship weekly, not eventually</span></div>
        <div><strong>03</strong><span>SEO and product in one pod</span></div>
        <div><strong>04</strong><span>You keep the IP</span></div>
      </div>
    </div>
  </section>

  <section class="section" id="work">
    <div class="container work-head">
      <div>
        <div class="section-kicker reveal">Selected work</div>
        <h2 class="section-title reveal">Engagements shaped like revenue problems</h2>
      </div>
      <p class="section-sub reveal work-head-copy">No invented Fortune-500 logos. These are the engagement patterns founders actually hire us for: challenge, approach, result.</p>
    </div>
    <div class="work-filters reveal" role="tablist" aria-label="Filter work">
      <button type="button" class="work-filter is-active" data-filter="all" role="tab" aria-selected="true">All</button>
      <button type="button" class="work-filter" data-filter="web" role="tab" aria-selected="false">Web + SEO</button>
      <button type="button" class="work-filter" data-filter="mobile" role="tab" aria-selected="false">Mobile</button>
      <button type="button" class="work-filter" data-filter="ops" role="tab" aria-selected="false">Ops</button>
    </div>
    <div class="work-rail" id="work-rail">
      <article class="work-card" data-cat="web">
        <div class="work-meta"><span>01</span><span>Website development</span><div class="work-tag">Service business</div></div>
        <h3>A service brand that was invisible online starts getting enquiries</h3>
        <p class="work-challenge"><strong>Challenge:</strong> Nice-looking site, unclear offers, hard-to-find contact form, almost no search visibility.</p>
        <p class="work-approach"><strong>Approach:</strong> Rebuild the website with clear offers, faster pages, and content that answers what buyers actually search for.</p>
        <div class="work-results">
          <div><strong>3.1x</strong><span>qualified form leads in 90 days</span></div>
          <div><strong>42</strong><span>pages live for search</span></div>
          <div><strong>18 days</strong><span>to first launch</span></div>
        </div>
        <a class="work-link" href="contact/">Start a similar brief</a>
      </article>
      <article class="work-card" data-cat="mobile">
        <div class="work-meta"><span>02</span><span>Mobile app development</span><div class="work-tag">Startup product</div></div>
        <h3>A first mobile app in about 10 weeks, not six months of waiting</h3>
        <p class="work-challenge"><strong>Challenge:</strong> Founder needed one clear user journey live on phone stores before the next investor update.</p>
        <p class="work-approach"><strong>Approach:</strong> Keep the first version small, show progress every week, and launch to the app stores with support included.</p>
        <div class="work-results">
          <div><strong>10 wks</strong><span>typical first-app timeline</span></div>
          <div><strong>1</strong><span>main user journey, done well</span></div>
          <div><strong>Clear plan</strong><span>for what comes after launch</span></div>
        </div>
        <a class="work-link" href="contact/">Scope a mobile app</a>
      </article>
      <article class="work-card" data-cat="ops">
        <div class="work-meta"><span>03</span><span>Custom software</span><div class="work-tag">Internal tools</div></div>
        <h3>From WhatsApp and spreadsheets to a system staff actually use</h3>
        <p class="work-challenge"><strong>Challenge:</strong> Day-to-day work lived in sheets and chat. Follow-ups got lost.</p>
        <p class="work-approach"><strong>Approach:</strong> Build a simple internal tool with reminders, handoffs and the workflows the team already follows.</p>
        <div class="work-results">
          <div><strong>12h+</strong><span>saved per week for ops</span></div>
          <div><strong>Less chase</strong><span>for status in WhatsApp</span></div>
          <div><strong>You own it</strong><span>files and docs handed over</span></div>
        </div>
        <a class="work-link" href="contact/">Map your ops brief</a>
      </article>
      <article class="work-card work-card-cta" data-cat="all">
        <div class="work-meta"><span>04</span><span>Your brief next</span></div>
        <h3>Bring the constraint. We bring the plan.</h3>
        <p>Share goals, links and budget range. We reply with fit, timeline and a fixed or phased path. Same accountability pod for build and discovery.</p>
        <a class="btn btn-primary btn-magnet" href="contact/">Talk to JB</a>
      </article>
    </div>
  </section>

  <section class="section" id="promises">
    <div class="container">
      <div class="section-kicker reveal">What you can count on</div>
      <h2 class="section-title reveal">Promises that make booking us safer</h2>
      <ul class="promise-list reveal">
        <li><strong>Honest fit check</strong>If we are wrong for you, we say so before you pay.</li>
        <li><strong>Scope in writing</strong>Deliverables, timeline and price before the first sprint.</li>
        <li><strong>Weekly visible progress</strong>Working builds, not radio silence until the deadline.</li>
        <li><strong>Small-team attention</strong>You talk to people who ship, not a ticket queue that forgets your name.</li>
      </ul>
    </div>
  </section>

  <section class="section" id="pricing-teaser">
    <div class="container">
      <div class="section-kicker reveal">Transparent starting points</div>
      <h2 class="section-title reveal">Pricing ranges buyers can plan around</h2>
      <p class="section-sub reveal">Agencies that hide every number lose serious buyers to shops that show a floor. Here is ours. Exact quotes still depend on scope.</p>
      <div class="price-grid">
        <article class="price-card reveal">
          <h3>Website development</h3>
          <div class="from">From ₹50,000</div>
          <p>Business websites built to get enquiries and show up on Google.</p>
        </article>
        <article class="price-card is-featured reveal">
          <h3>Web apps and mobile apps</h3>
          <div class="from">From ₹3,00,000</div>
          <p>Web app development, mobile app development and internal business tools with clear milestones.</p>
        </article>
        <article class="price-card reveal">
          <h3>SEO and visibility</h3>
          <div class="from">From ₹25,000/mo</div>
          <p>Monthly work so people can find you on Google and AI search tools.</p>
        </article>
      </div>
      <p style="margin-top:1.5rem" class="reveal"><a class="btn btn-primary btn-magnet" href="pricing/">See full pricing</a> <a class="btn btn-ghost btn-magnet" href="contact/">Request a fixed quote</a></p>
    </div>
  </section>

  <section class="section" id="why-jb">
    <div class="container">
      <div class="section-kicker reveal">Built for results</div>
      <h2 class="section-title reveal">How we help you get found and get work</h2>
      <p class="section-sub reveal">Every section on this site answers a real buying question, then points to contact. Build projects ship once. SEO and visibility retainers keep compounding. We own both so product and discovery do not fight each other.</p>
      <div class="outcome-grid">
        <article class="outcome reveal">
          <h3>Project revenue</h3>
          <p>Websites, mobile apps, custom business tools and desktop apps sold as clear fixed or phased scopes. You own the work.</p>
        </article>
        <article class="outcome reveal">
          <h3>Recurring revenue</h3>
          <p>SEO, AEO, GEO and product retainers that keep rankings, citations and features moving after launch.</p>
        </article>
        <article class="outcome reveal">
          <h3>Inbound that compounds</h3>
          <p>Keyword pages, FAQs, schema and blog clusters so Google and answer surfaces keep sending qualified founders our way.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section" id="market">
    <div class="container">
      <div class="section-kicker reveal">How we compare</div>
      <h2 class="section-title reveal">The India market we compete in every week</h2>
      <p class="section-sub reveal">Buyers comparing full-stack India agencies for custom software, mobile apps, websites, digital marketing, SEO and AI search see a crowded field. Firms in Chennai, Hyderabad, Ahmedabad, Indore, Mohali and beyond now sell the same menu: React/Next web, Flutter apps, automation, SEO, AEO and GEO. JB Software Solutions is built to win that shortlist with sharper proof, faster founder access and discovery engineered into the build.</p>
      <div class="compare-wrap reveal">
        <table class="compare">
          <thead>
            <tr>
              <th>What buyers ask</th>
              <th>Typical India full-stack shop</th>
              <th>Marketing-first hybrid</th>
              <th>JB Software Solutions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Can you build and rank?</td>
              <td>Strong engineering, SEO often bolted on later</td>
              <td>Strong ads and SEO, product depth varies</td>
              <td>One pod owns product engineering plus SEO, AEO and GEO from day one</td>
            </tr>
            <tr>
              <td>Will AI assistants cite us?</td>
              <td>New GEO pages, uneven evidence</td>
              <td>GEO sold as a package, thin entity proof</td>
              <td>Service, tech and proof pages written for Google and ChatGPT citations</td>
            </tr>
            <tr>
              <td>Who do I talk to?</td>
              <td>Account layers and slow feedback</td>
              <td>Campaign managers front the relationship</td>
              <td>Direct path to the build team via the contact form and scoped quotes</td>
            </tr>
            <tr>
              <td>Desktop and offline tools?</td>
              <td>Rarely a first-class offer</td>
              <td>Usually out of scope</td>
              <td>Desktop apps when a website is not enough</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="section-note reveal">We respect serious competitors in this category. We do not win by copying their homepage claims. We win by shipping measurable systems: faster pages, clearer offers, indexed content, and follow-through after launch.</p>
    </div>
  </section>

  <section class="section" id="keywords">
    <div class="container">
      <div class="section-kicker reveal">Services people hire us for</div>
      <h2 class="section-title reveal">Commercial keywords mapped to real services</h2>
      <p class="section-sub reveal">These are the queries founders and operators actually type, and the pages we built to answer them clearly.</p>
      <div class="seo-cloud reveal">
        <a class="seo-chip" href="services/custom-software/">custom software development company India</a>
        <a class="seo-chip" href="services/custom-software/">custom software development services</a>
        <a class="seo-chip" href="services/custom-software/">bespoke software development</a>
        <a class="seo-chip" href="services/web-development/">website development company India</a>
        <a class="seo-chip" href="services/web-development/">web development company</a>
        <a class="seo-chip" href="services/web-development/">web application development company</a>
        <a class="seo-chip" href="services/web-development/">lead generation website</a>
        <a class="seo-chip" href="services/mobile-app-development/">mobile app development company India</a>
        <a class="seo-chip" href="services/mobile-app-development/">Android app development</a>
        <a class="seo-chip" href="services/mobile-app-development/">iPhone app development</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">SEO company India</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">technical SEO services</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">GEO generative engine optimization</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">AEO answer engine optimization</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">ChatGPT SEO</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">LLM SEO</a>
        <a class="seo-chip" href="services/ai-automation/">business workflow automation</a>
        <a class="seo-chip" href="services/ai-automation/">CRM automation</a>
        <a class="seo-chip" href="services/ai-automation/">AI business automation India</a>
        <a class="seo-chip" href="services/desktop-apps/">desktop app development</a>
        <a class="seo-chip" href="services/custom-software/">SaaS product development</a>
        <a class="seo-chip" href="services/custom-software/">custom CRM development</a>
        <a class="seo-chip" href="services/custom-software/">ERP software development</a>
        <a class="seo-chip" href="services/custom-software/">software outsourcing company</a>
        <a class="seo-chip" href="faq/custom-software-cost-india/">custom software development cost India</a>
        <a class="seo-chip" href="faq/website-development-cost-india/">website development cost India</a>
        <a class="seo-chip" href="faq/mobile-app-development-cost-india/">mobile app development cost India</a>
        <a class="seo-chip" href="faq/seo-aeo-geo-explained/">what is GEO and AEO</a>
        <a class="seo-chip" href="contact/">hire developers India</a>
        <a class="seo-chip" href="contact/">hire software development company India</a>
      </div>
    </div>
  </section>

  <section class="section" id="capabilities">
    <div class="container">
      <div class="section-kicker reveal">Capabilities</div>
      <h2 class="section-title reveal">Website, mobile app and custom software development services</h2>
      <p class="section-sub reveal">As a software development company in India, we ship website development, mobile app development, custom CRM and ERP tools, desktop apps, SEO and business workflow automation. Clear outcomes. Transparent starting prices.</p>
      <div class="bento" id="bento">
        <a class="bento-tile bento-lg reveal" href="services/web-development/">
          <span class="bento-num">01</span>
          <h3>Website development</h3>
          <p>Business websites that look good, load fast, and turn visitors into enquiries.</p>
          <span class="bento-go">Explore websites</span>
        </a>
        <a class="bento-tile reveal" href="services/mobile-app-development/">
          <span class="bento-num">02</span>
          <h3>Mobile app development</h3>
          <p>Phone apps for Android and iOS. First version often around 8 to 12 weeks.</p>
          <span class="bento-go">Explore apps</span>
        </a>
        <a class="bento-tile reveal" href="services/seo-aeo-geo/">
          <span class="bento-num">03</span>
          <h3>SEO and visibility</h3>
          <p>Get found on Google and mentioned in AI search tools.</p>
          <span class="bento-go">Explore SEO</span>
        </a>
        <a class="bento-tile reveal" href="services/custom-software/">
          <span class="bento-num">04</span>
          <h3>Custom software</h3>
          <p>Business tools built around how your team already works. You own everything.</p>
          <span class="bento-go">Explore software</span>
        </a>
        <a class="bento-tile bento-wide reveal" href="services/ai-automation/">
          <span class="bento-num">05</span>
          <h3>Workflow automation</h3>
          <p>Connect your tools so leads, follow-ups and approvals happen without copy-paste.</p>
          <span class="bento-go">Explore automation</span>
        </a>
        <a class="bento-tile reveal" href="services/desktop-apps/">
          <span class="bento-num">06</span>
          <h3>Desktop apps</h3>
          <p>Software that installs on a computer when a website is not enough.</p>
          <span class="bento-go">Explore desktop</span>
        </a>
      </div>
    </div>
  </section>

  <section class="section" id="services">
    <div class="container">
      <div class="section-kicker reveal">What we ship</div>
      <h2 class="section-title reveal">Software development and growth under one roof</h2>
      <p class="section-sub reveal">Most agencies hand you a site and disappear. We keep engineering and search together so the product you launch is the product that ranks, converts and gets cited.</p>

      <article class="service-band">
        <div>
          <h3>Website development</h3>
          <p>Business websites and web apps that load fast, explain your offer clearly, and help visitors contact you.</p>
          <div class="tags"><span class="tag">Business websites</span><span class="tag">Web apps</span><span class="tag">SEO-ready</span><span class="tag">Lead forms</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/web-development/">Website development services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/web-aside.jpg" alt="Website development - modern websites and web apps" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Mobile app development</h3>
          <p>Apps for Android and iPhone. We help you launch a focused first version, usually in about 8 to 12 weeks, then improve after feedback.</p>
          <div class="tags"><span class="tag">Android</span><span class="tag">iPhone</span><span class="tag">App store launch</span><span class="tag">Support after launch</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/mobile-app-development/">Mobile app services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/mobile-aside.jpg" alt="Mobile app development for phones and tablets" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Custom software</h3>
          <p>Internal tools, dashboards and business systems tailored to how your team actually works. You keep full ownership. No lock-in.</p>
          <div class="tags"><span class="tag">Internal tools</span><span class="tag">Dashboards</span><span class="tag">Team workflows</span><span class="tag">You own it</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/custom-software/">Custom software services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/custom-aside.jpg" alt="Custom software and business dashboards" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>SEO and online visibility</h3>
          <p>Help people find you on Google, and help AI tools like ChatGPT mention your brand when buyers ask questions.</p>
          <div class="tags"><span class="tag">Google SEO</span><span class="tag">Content</span><span class="tag">AI search</span><span class="tag">Monthly support</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/seo-aeo-geo/">SEO services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/seo-aside.jpg" alt="SEO and online visibility" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Workflow automation</h3>
          <p>Automate day-to-day work: leads, follow-ups, approvals, reminders and status updates. Practical automation that saves hours.</p>
          <div class="tags"><span class="tag">Leads</span><span class="tag">Follow-ups</span><span class="tag">Approvals</span><span class="tag">Ops</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/ai-automation/">Automation services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/ai-aside.jpg" alt="Business workflow and process automation" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Desktop apps</h3>
          <p>Software that installs on a computer for offline work, special devices, or offices where a website is not enough.</p>
          <div class="tags"><span class="tag">Windows</span><span class="tag">Offline use</span><span class="tag">Installers</span><span class="tag">Updates</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/desktop-apps/">Desktop app services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/desktop-aside.jpg" alt="Desktop application development" width="640" height="360" loading="lazy" /></div>
      </article>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-kicker reveal">Proof in motion</div>
      <h2 class="section-title reveal">Numbers we design every engagement around</h2>
      <div class="stats reveal">
        <div class="stat"><strong data-count="6" data-suffix="+">0</strong><span>Services under one roof</span></div>
        <div class="stat"><strong data-count="90" data-suffix="+">0</strong><span>Speed score target on websites</span></div>
        <div class="stat"><strong data-count="10">0</strong><span>Week average for a first mobile app</span></div>
        <div class="stat"><strong data-count="24">0</strong><span>Hour reply target on serious briefs</span></div>
      </div>
    </div>
  </section>

  <section class="section" id="industries">
    <div class="container">
      <div class="section-kicker reveal">Industries</div>
      <h2 class="section-title reveal">Where custom software and SEO actually pay back</h2>
      <p class="section-sub reveal">We prioritize verticals where a shipped product plus discoverability creates revenue faster than a brochure site ever will.</p>
      <div class="industry-grid">
        <article class="industry reveal"><h3>Startups and new products</h3><p>First websites, web apps and mobile apps, plus launch SEO so early users can find you.</p></article>
        <article class="industry reveal"><h3>Services and agencies</h3><p>High-converting service sites, lead forms, clear contact paths and local plus search visibility.</p></article>
        <article class="industry reveal"><h3>Retail and D2C</h3><p>Catalog experiences, internal ops tools and performance landing pages wired for paid and organic.</p></article>
        <article class="industry reveal"><h3>Logistics and field ops</h3><p>Tracking portals, vendor dashboards, offline-capable desktop helpers and mobile workforce apps.</p></article>
        <article class="industry reveal"><h3>Education and training</h3><p>Learning portals, admin panels and content structures that rank for course and admission intent.</p></article>
        <article class="industry reveal"><h3>Healthcare and clinics</h3><p>Appointment systems, patient-facing sites and careful data handling with clear consent paths.</p></article>
        <article class="industry reveal"><h3>Manufacturing and B2B</h3><p>Product catalogs, RFQ workflows, ERP-adjacent tools and entity-rich pages for AI citations.</p></article>
        <article class="industry reveal"><h3>GCC and export brands</h3><p>Bilingual sites, remote delivery from India, and SEO/GEO for India plus Middle East buyers.</p></article>
      </div>
    </div>
  </section>

  <section class="section" id="stack">
    <div class="container">
      <div class="section-kicker reveal">Technology</div>
      <h2 class="section-title reveal">Stacks buyers already search for</h2>
      <p class="section-sub reveal">We do not list every framework on earth. We list what we ship in production for software development projects in India and remote international work.</p>
      <div class="stack-grid reveal">
        <div><h3>Web</h3><p>Next.js, React, Node.js, TypeScript, WordPress when editorial speed matters, headless CMS when scale matters.</p></div>
        <div><h3>Mobile</h3><p>Flutter, React Native, native modules for camera, maps, payments and push.</p></div>
        <div><h3>Desktop</h3><p>Electron, Tauri, installers, code signing, auto-update and offline storage.</p></div>
        <div><h3>Automation</h3><p>Business workflows, CRM and ops automation, integrations between the tools you already use, dashboards.</p></div>
        <div><h3>Cloud</h3><p>AWS, GCP, Azure, CI/CD, monitoring and cost-aware architecture.</p></div>
        <div><h3>Search</h3><p>Technical SEO, schema, content clusters, AEO, GEO, LLM SEO and citation tracking.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-kicker reveal">How we work</div>
      <h2 class="section-title reveal">From brief to launched revenue system</h2>
      <div class="process-steps">
        <article class="reveal"><h3>Discover</h3><p>Goals, users, constraints, competitor landscape and the exact Google and ChatGPT questions your buyers already ask.</p></article>
        <article class="reveal"><h3>Design</h3><p>Architecture, UX and content structure for humans and crawlers. Prototypes before heavy code spend.</p></article>
        <article class="reveal"><h3>Build</h3><p>Agile sprints with demos every week. Web, mobile, desktop or workflow automation, same accountable pod.</p></article>
        <article class="reveal"><h3>Grow</h3><p>Launch, measure leads, SEO/AEO/GEO iterations and feature updates so the product keeps compounding.</p></article>
      </div>
    </div>
  </section>

  <section class="section" id="audience">
    <div class="container prose-wide">
      <div class="section-kicker reveal">Who hires us</div>
      <h2 class="section-title reveal">Built for founders who refuse a pretty dead site</h2>
      <div class="two-col reveal">
        <div>
          <p>Hire JB Software Solutions when you need a <strong>custom software development company in India</strong> that can also compete with modern digital agencies on SEO, AEO and GEO. Ideal briefs include SaaS MVPs, service-business websites that must generate enquiries, Flutter or React Native apps for Android and iOS, internal tools that replace spreadsheet chaos, and workflow automation that removes repetitive sales or support work.</p>
          <p>We also suit export-facing and GCC-facing brands that want India delivery costs with bilingual or multi-market sites, plus teams that already talked to large full-stack shops and felt the pitch was generic.</p>
        </div>
        <div>
          <p>If you only need a one-page brochure with no leads plan, we will say so. Revenue comes from products people use and pages people find. That is the filter we apply before we accept work.</p>
          <p>Start on the <a href="contact/">contact form</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>. Bring goals, links and a budget range. We return fit, timeline and a clear commercial path.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Ready to outrun the default agency shortlist?</h2>
          <p>Tell us what you are building. We reply with scope, timeline and a fixed or phased plan through the contact form.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-primary btn-magnet" href="contact/">Book a strategy call</a>
          <a class="btn btn-ghost btn-magnet" href="contact/">Contact us</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="faq">
    <div class="container">
      <div class="section-kicker">FAQs</div>
      <h2 class="section-title">Frequently asked questions</h2>
      <div class="faq">
        <details open>
          <summary>What does JB Software Solutions do?</summary>
          <p>We are a custom software development company in India offering web development, mobile app development, desktop apps, custom CRMs and ERPs, SEO, AEO, GEO and workflow automation for startups and growing businesses in India and internationally.</p>
        </details>
        <details>
          <summary>Do you offer SEO, AEO and GEO?</summary>
          <p>Yes. Technical SEO for Google, Answer Engine Optimization for featured answers, and Generative Engine Optimization so brands get cited inside ChatGPT, Gemini, Perplexity and Google AI Overviews. See our <a href="services/seo-aeo-geo/">SEO, AEO and GEO services</a>.</p>
        </details>
        <details>
          <summary>How much does custom software development cost in India?</summary>
          <p>It depends on scope. Business website development often starts from ₹50,000. Custom software and web apps often start from a few lakhs. Mobile app development often starts from ₹5,00,000. See our <a href="faq/custom-software-cost-india/">cost FAQs</a> or ask for a scoped quote.</p>
        </details>
        <details>
          <summary>How is JB different from other India software and digital agencies?</summary>
          <p>Many shops sell the same list: apps, websites and SEO. We stay easy to reach, write the scope before we build, and make sure launch day is not the first day you start thinking about being found online.</p>
        </details>
        <details>
          <summary>How fast can a first version ship?</summary>
          <p>A focused website or web app often lands in 2 to 6 weeks. A first mobile app typically takes about 8 to 12 weeks, depending on features and store requirements.</p>
        </details>
        <details>
          <summary>Can I hire developers in India through JB for a dedicated pod?</summary>
          <p>Yes. Fixed projects and dedicated pods are both available. Start with a written scope so capacity matches a real roadmap.</p>
        </details>
        <details>
          <summary>Do you offer website development and SEO together?</summary>
          <p>Yes. As a website development company and SEO company under one roof, we can ship the site and the discovery plan together so rankings are not an afterthought.</p>
        </details>
        <details>
          <summary>Do you work with startups and enterprises?</summary>
          <p>Both. Engagements can be fixed-scope projects, dedicated pods, or ongoing retainers for SEO, GEO and product iteration.</p>
        </details>
        <details>
          <summary>Is the website indexed for search and AI crawlers?</summary>
          <p>Yes. Pages include canonical URLs, sitemap.xml, robots.txt, structured data and crawlable HTML so search engines can discover our services. Browse the full <a href="faq/">FAQ hub</a> for 300+ indexed answers.</p>
        </details>
      </div>
    </div>
  </section>
</main>
{footer(0)}
"""
write(ROOT / "index.html", home)


def _resolve_feature_img(slug, imgs, key):
    if key == "legacy":
        return LEGACY_IMG.get(slug, imgs.get("hero", "web-hero.jpg"))
    return imgs.get(key, imgs.get("hero", "web-hero.jpg"))


# Unique mid-page + closing headings per service (never reuse hero H1)
SERVICE_SECTION = {
    "web-development": {
        "offer_kicker": "Deliverables",
        "offer_h2": "What ships in a website project",
        "include_h3": "Pages and launch items",
        "engage_h3": "Ways to engage us",
        "cta_h3": "Start a website brief",
        "closing_kicker": "Pricing signal",
        "closing_h2": "Website cost, fit and next step",
        "faq_h2": "Website development FAQ",
        "cta_h2": "Ready for a site that brings enquiries?",
        "why": "A site that looks finished but cannot be found or contacted is a liability. We ship enquiry paths, mobile layout and crawlable structure with the build.",
    },
    "mobile-app-development": {
        "offer_kicker": "App scope",
        "offer_h2": "What a first mobile app includes",
        "include_h3": "First-version essentials",
        "engage_h3": "Delivery options",
        "cta_h3": "Start an app brief",
        "closing_kicker": "Budget signal",
        "closing_h2": "App cost, timeline and next step",
        "faq_h2": "Mobile app development FAQ",
        "cta_h2": "Ready to scope your first app?",
        "why": "The fastest path to learning is one user journey on the stores, not a bloated roadmap. We keep the first release honest and demo weekly.",
    },
    "custom-software": {
        "offer_kicker": "Build scope",
        "offer_h2": "What custom software engagements include",
        "include_h3": "System building blocks",
        "engage_h3": "How we contract the work",
        "cta_h3": "Map your ops brief",
        "closing_kicker": "Investment signal",
        "closing_h2": "Custom software cost and fit",
        "faq_h2": "Custom software FAQ",
        "cta_h2": "Ready to replace spreadsheet chaos?",
        "why": "If SaaS forces painful workarounds, custom software pays for itself. We map real roles first, then ship the workflow that removes re-entry and status chasing.",
    },
    "seo-aeo-geo": {
        "offer_kicker": "Visibility scope",
        "offer_h2": "What SEO, AEO and GEO cover",
        "include_h3": "Visibility workstream",
        "engage_h3": "Retainer shapes",
        "cta_h3": "Start a visibility plan",
        "closing_kicker": "Retainer signal",
        "closing_h2": "SEO pricing, fit and next step",
        "faq_h2": "SEO, AEO and GEO FAQ",
        "cta_h2": "Ready to get found and cited?",
        "why": "Rankings still matter. AI answers matter too. We fix technical basics and publish pages that buyers and assistants can both trust.",
    },
    "ai-automation": {
        "offer_kicker": "Automation scope",
        "offer_h2": "What workflow automation covers",
        "include_h3": "Flows we connect",
        "engage_h3": "How we phase flows",
        "cta_h3": "Start an automation map",
        "closing_kicker": "Effort signal",
        "closing_h2": "Automation cost, fit and next step",
        "faq_h2": "Workflow automation FAQ",
        "cta_h2": "Ready to stop the copy-paste?",
        "why": "Most businesses lose hours to copy-paste between forms, CRMs and chat. We automate that path so leads get followed up and ops stay visible.",
    },
    "desktop-apps": {
        "offer_kicker": "Desktop scope",
        "offer_h2": "What a desktop build includes",
        "include_h3": "Installable product pieces",
        "engage_h3": "How we package and ship",
        "cta_h3": "Start a desktop brief",
        "closing_kicker": "Scope signal",
        "closing_h2": "Desktop fit, cost path and next step",
        "faq_h2": "Desktop app FAQ",
        "cta_h2": "Ready when the browser is not enough?",
        "why": "Offline networks, printers, scanners and locked-down offices still need installable software. We build that when a website is the wrong tool.",
    },
}


def service_page(slug, title, h1, desc, keywords, bullets, faqs, active, why=None, image="web-hero.jpg", image_alt="", extra_html=""):
    depth = 2
    p = rel(depth)
    sec = SERVICE_SECTION[slug]
    why_text = why or sec["why"]
    alt = image_alt or h1
    imgs = SERVICE_IMG.get(slug, {"hero": image, "aside": image, "mid": image, "deep": image})
    hero_img = imgs["hero"]
    long_body = (extra_html or SERVICE_BODIES.get(slug, "")).replace("{P}", p)
    long_body = long_body.replace("{IMG_MID}", "").replace("{IMG_DEEP}", "")
    long_body = re.sub(
        r'<figure class="service-figure">\s*<img[^>]*>\s*</figure>',
        "",
        long_body,
        flags=re.I,
    )

    feat_kickers = ("Outcome", "Process", "Strategy", "Coverage")
    feat_rows = []
    for i, feat in enumerate(SERVICE_FEATURES.get(slug, [])):
        img_file = _resolve_feature_img(slug, imgs, feat["img"])
        reverse = " is-reverse" if i % 2 == 1 else ""
        kicker = feat.get("kicker") or feat_kickers[i % len(feat_kickers)]
        feat_rows.append(f"""
  <section class="section service-feature{reverse}">
    <div class="container service-feature-grid">
      <div class="service-feature-media reveal">
        <img src="{p}assets/services/{img_file}" alt="{feat['title']}" width="960" height="640" loading="lazy" />
      </div>
      <div class="service-feature-copy reveal">
        <div class="section-kicker">{kicker}</div>
        <h2>{feat['title']}</h2>
        <p>{feat['text']}</p>
      </div>
    </div>
  </section>""")
    features_html = "".join(feat_rows)

    other = "".join(
        f'<a class="service-chip" href="{p}services/{s}/">{lab}</a>'
        for s, lab, _b, _i in SERVICES
        if s != slug
    )
    body = head(title, desc, keywords, f"/services/{slug}/", depth) + f"""
<body>
{nav(depth, active)}
<main>
  <section class="page-hero service-hero">
    <div class="container service-hero-grid">
      <div class="service-hero-copy">
        <div class="section-kicker">Services</div>
        <h1>{h1}</h1>
        <p>{desc}</p>
        <div class="hero-cta" style="margin-top:1.75rem">
          <a class="btn btn-primary btn-magnet" href="{p}contact/">Get a project quote</a>
          <a class="btn btn-ghost btn-magnet" href="{p}pricing/">View pricing</a>
        </div>
      </div>
      <div class="service-hero-visual reveal">
        <img src="{p}assets/services/{hero_img}" alt="{alt}" width="960" height="640" loading="eager" />
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="section-kicker reveal">{sec['offer_kicker']}</div>
      <h2 class="section-title reveal">{sec['offer_h2']}</h2>
      <p class="section-sub reveal">{why_text}</p>
      <div class="service-offer-grid">
        <div class="service-offer reveal">
          <h3>{sec['include_h3']}</h3>
          <ul>
            {''.join(f'<li>{b}</li>' for b in bullets)}
          </ul>
        </div>
        <div class="service-offer reveal">
          <h3>{sec['engage_h3']}</h3>
          <ul>
            <li>Fixed-scope projects with milestones</li>
            <li>Time and materials for evolving products</li>
            <li>Dedicated pod for ongoing delivery</li>
            <li>Retainer for SEO, AEO, GEO and growth experiments</li>
          </ul>
        </div>
        <div class="service-offer service-offer-cta reveal">
          <h3>{sec['cta_h3']}</h3>
          <p>Share goals, links and budget range. We reply with fit, timeline and a clear quote path.</p>
          <a class="btn btn-primary btn-magnet" href="{p}contact/">Start a brief</a>
          <div class="service-chip-row" style="margin-top:1rem">{other}</div>
        </div>
      </div>
    </div>
  </section>
{features_html}
  <section class="section service-closing" id="details">
    <div class="container">
      <div class="service-closing-head reveal">
        <div class="section-kicker">{sec['closing_kicker']}</div>
        <h2 class="section-title">{sec['closing_h2']}</h2>
      </div>
      <div class="service-closing-body reveal">
        {long_body}
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <div><h2>{sec['cta_h2']}</h2><p>Share goals and constraints. We come back with a clear plan on the contact form or email.</p></div>
        <div class="cta-actions">
          <a class="btn btn-primary btn-magnet" href="{p}contact/">Contact JB Software Solutions</a>
        </div>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-kicker">FAQ</div>
      <h2 class="section-title">{sec['faq_h2']}</h2>
      <div class="faq">
        {''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)}
      </div>
      <p class="section-note" style="margin-top:1.25rem">More indexed answers: <a href="{p}faq/">FAQ hub</a>.</p>
    </div>
  </section>
</main>
{footer(depth)}
"""
    write(ROOT / "services" / slug / "index.html", body)


service_page(
    "web-development",
    f"Website Development Company India | {BRAND}",
    "Website development that brings enquiries",
    "JB Software Solutions builds fast business websites and web apps for startups and growing businesses in India.",
    "website development company India, web development company, business website, web application development, SEO website development",
    [
        "Business websites and product web apps",
        "Pages that load fast on phone and desktop",
        "Clear offers, contact forms and basic SEO setup",
        "Easy ways for your team to update content when needed",
        "Support after launch so small fixes do not stall",
    ],
    [
        ("Can you redesign an existing site?", "Yes. We review speed, clarity and enquiry flow, then rebuild or improve step by step without losing what already works."),
        ("How long does a business website take?", "Many 5 to 12 page sites land in a few weeks once the offer and content are clear."),
        ("How much does website development cost in India?", "Business websites often start from ₹50,000. Page count, custom design and integrations change the quote."),
        ("Do you build SEO-friendly websites?", "Yes. Crawlable pages, sensible URLs, sitemap path and room for schema are part of the build."),
        ("Will I own the website?", "Yes. You keep domain, hosting accounts and the work we create for you."),
        ("Do you write website content?", "We guide structure and headlines. Final business claims stay with you unless content is scoped in."),
    ],
    "services",
    image="web-hero.jpg",
    image_alt="Website development - modern websites and web apps",
)

service_page(
    "mobile-app-development",
    f"Mobile App Development Company India | {BRAND}",
    "Mobile app development for Android and iPhone",
    "JB Software Solutions builds phone apps for Android and iPhone, from a focused first version through app store launch.",
    "mobile app development company India, Android app, iPhone app, mobile app development, app store launch",
    [
        "Apps for Android and iPhone",
        "A focused first version, often around 8 to 12 weeks",
        "Help publishing to Google Play and the App Store",
        "Login, payments, notifications and tracking when your brief needs them",
        "Support after launch so you can improve from real user feedback",
    ],
    [
        ("How long does a first app take?", "A focused first version often takes about 8 to 12 weeks. Bigger products take longer, and we say so up front."),
        ("Do I need both Android and iPhone at once?", "Many teams start with one store, then add the second. We plan that with you during discovery."),
        ("How much does mobile app development cost in India?", "Focused first apps often start from ₹5,00,000. Payments, maps, chat and multi-role features increase cost."),
        ("Do you publish to Google Play and the App Store?", "Yes. Store listing support can be included in the project scope."),
        ("Will I own the app code?", "Yes. Client projects include IP handover for the work we create for you."),
        ("Do you build apps for internal staff only?", "Yes. Internal mobile tools for field teams are a common brief."),
    ],
    "services",
    image="mobile-hero.jpg",
    image_alt="Mobile app development for phones and tablets",
)

service_page(
    "custom-software",
    f"Custom Software Development Company India | {BRAND}",
    "Custom software built around your process",
    "Bespoke CRMs, ERPs, dashboards and workflow systems with full IP ownership from JB Software Solutions.",
    "custom software development company India, bespoke software, CRM development, ERP software, internal tools, SaaS development",
    [
        "Discovery workshops that map real workflows before code",
        "Secure APIs, role-based access and audit-friendly data models",
        "Integrations with WhatsApp, UPI, payment gateways and third-party SaaS",
        "Source code handover and documentation",
        "Optional cloud, DevOps and monitoring setup",
    ],
    [
        ("Who owns the code?", "You do. Contracts include IP assignment for work we create for you."),
        ("Can you replace spreadsheets?", "That is a common brief. We turn spreadsheet chaos into a proper multi-user system."),
        ("How much does custom software cost in India?", "Focused internal tools often start from ₹4,00,000. Multi-department platforms are phased."),
        ("Custom software vs ready-made SaaS?", "Buy SaaS when it fits most of your process. Build custom when off-the-shelf tools force painful workarounds."),
        ("Do you build custom CRM and ERP modules?", "Yes. CRM pipelines, order flows, inventory and approval modules are common requests."),
        ("Can you integrate WhatsApp and payments?", "Yes, when those integrations are listed in the written scope."),
    ],
    "services",
    image="custom-hero.jpg",
    image_alt="Custom software and business dashboards",
)

service_page(
    "seo-aeo-geo",
    f"SEO, AEO and GEO Services India | ChatGPT & Google | {BRAND}",
    "SEO, AEO and GEO that put you in the answer",
    "Technical SEO plus Answer Engine and Generative Engine Optimization so JB Software Solutions clients rank on Google and get cited in ChatGPT, Gemini and Perplexity.",
    "SEO company India, AEO services, GEO services, generative engine optimization, LLM SEO, ChatGPT SEO, AI Overviews SEO",
    [
        "Technical SEO: speed, indexation, schema, Core Web Vitals",
        "Content clusters mapped to buyer questions, not keyword stuffing",
        "AEO for featured snippets and answer-style results",
        "GEO for citations across ChatGPT, Gemini, Perplexity and AI Overviews",
        "Monthly reporting on rankings and AI mention checks",
    ],
    [
        ("What is GEO?", "Generative Engine Optimization is the practice of structuring your brand's proof and content so AI assistants cite you when answering buyer questions."),
        ("Do you do local SEO?", "Yes. Google Business Profile, local pages and citation hygiene for city-level intent."),
        ("How much is an SEO retainer in India?", "Visibility retainers often start from ₹25,000 per month, depending on site size and competition."),
        ("What is AEO?", "Answer Engine Optimization helps your content show up as a short answer when search systems display direct answers."),
        ("Do you only write blogs for SEO?", "No. We prioritise technical fixes, service pages, FAQs and proof pages that match commercial intent."),
        ("Can SEO help if my website is weak?", "Often the site itself is the bottleneck. We may recommend a website rebuild alongside SEO."),
    ],
    "services",
    image="seo-hero.jpg",
    image_alt="SEO AEO and GEO search visibility",
)

service_page(
    "ai-automation",
    f"Business Workflow Automation | {BRAND}",
    "Automate how your business actually runs",
    "JB Software Solutions builds workflows and automations that connect your tools, cut repetitive work, and keep leads, follow-ups and ops moving without manual copy-paste.",
    "business workflow automation, AI business automation India, CRM automation, process automation, Zapier Make n8n workflows, lead automation, ops automation",
    [
        "End-to-end business workflows: lead capture to CRM to follow-up to notification",
        "Automation across the tools you already use (CRM, email, sheets, forms, chat, payment alerts)",
        "Approval flows, reminders, status updates and handoffs between teams",
        "Internal process automation that replaces spreadsheet and WhatsApp chaos",
        "Practical use of AI inside workflows where it helps (drafting, tagging, routing), not building custom RAG labs",
    ],
    [
        ("Do you build custom RAG or AI model products?", "No. We focus on workflow and business process automation. If a step benefits from AI assistance inside a workflow, we can wire that in. We do not sell custom RAG platforms or model training as a product."),
        ("Will this replace my team?", "No. Automation removes repetitive work so your team focuses on decisions, sales and customer care."),
        ("What tools can you connect?", "Common CRMs, forms, email, sheets, chat tools, payment notifications and custom webhooks. We map your stack in discovery and automate the boring path between systems."),
    ],
    "services",
    image="ai-hero.jpg",
    image_alt="Business workflow and process automation",
)

service_page(
    "desktop-apps",
    f"Desktop App Development | {BRAND}",
    "Desktop apps when a website is not enough",
    "JB Software Solutions builds software that installs on a computer for offline work, special devices, or locked-down office setups.",
    "desktop app development, Windows desktop software, offline app, computer software development India",
    [
        "Apps that install on Windows and Mac",
        "Works offline, then syncs when the internet is back",
        "Connect to printers, scanners or other office devices when needed",
        "Installers and update support",
        "Licensing options if you sell the software to customers",
    ],
    [
        ("When should I choose a desktop app?", "When people need to work offline, use special devices, handle large local files, or work in places where browsers are limited."),
        ("Can you turn our website product into a desktop app?", "Often yes. We package it as real installable software with menus, updates and a smoother desktop feel."),
    ],
    "services",
    image="desktop-hero.jpg",
    image_alt="Desktop application development",
)

# ---------- ABOUT ----------
about = head(
    f"About {BRAND} | Software, Apps and Search",
    "JB Software Solutions is a small, hardworking software agency that loves its customers. Custom products, SEO, AEO, GEO and workflow automation with real human support.",
    "about JB Software Solutions, small software agency India, customer first digital agency, software development studio",
    "/about/",
    1,
) + f"""
<body>
{nav(1, "about")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">About</div>
    <h1>A small agency that fights for your outcome</h1>
    <p>We are not a factory floor of tickets. We are a tight team that works hard, stays close to the people who hire us, and actually loves seeing customers win.</p>
    <div class="hero-cta" style="margin-top:1.75rem">
      <a class="btn btn-primary btn-magnet" href="{rel(1)}contact/">Work with us</a>
      <a class="btn btn-ghost btn-magnet" href="{rel(1)}pricing/">See pricing</a>
    </div>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container prose">
    <h2>We are small on purpose</h2>
    <p>{BRAND} is a small agency by choice. That means you are not lost behind layers of account managers. When you message us, the people building your product are in the loop. We sweat the details, we answer fast, and we stay supportive long after the launch party ends.</p>
    <p>We really love our customers. Not as a slogan on a wall. As a working rule: clear communication, honest scope, patient hand-holding when something is new, and zero ego when feedback arrives. Your success is the only scoreboard that matters to us.</p>
    <h2>Who we are</h2>
    <p>We help founders and operators ship digital products: websites, mobile apps, custom software, desktop tools, and the SEO / AEO / GEO layer that makes those products easier to find on Google and in answer-style results.</p>
    <h2>How we work</h2>
    <ul>
      <li>Ship systems, not slide decks</li>
      <li>Measure outcomes: leads, retention, citations, not vanity screenshots</li>
      <li>Keep IP with the client</li>
      <li>Use AI for velocity. Keep humans on taste, care and accountability</li>
      <li>Treat every customer like the reason we get to do this work</li>
    </ul>
    <h2>Where we work</h2>
    <p>India-first delivery with remote collaboration for clients across India, the Middle East, the UK, the US and beyond.</p>
    <p><a class="btn btn-primary btn-magnet" href="{rel(1)}contact/">Work with us</a></p>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "about" / "index.html", about)

# ---------- CONTACT ----------
contact = head(
    f"Contact {BRAND} | Get a Software or SEO Quote",
    "Contact JB Software Solutions for custom software, mobile apps, websites, SEO, GEO and workflow automation. Reply within 24 hours on business days.",
    "contact JB Software Solutions, software development quote, hire Flutter developer, SEO agency contact",
    "/contact/",
    1,
) + f"""
<body>
{nav(1, "contact")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Contact</div>
    <h1>Get a scoped quote</h1>
    <p>Send a short brief. We reply within 24 hours on business days with fit, rough timeline and next steps. No phone tag. No spam.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container contact-grid">
    <form class="form" action="https://formsubmit.co/{EMAIL}" method="POST">
      <input type="hidden" name="_next" value="{SITE}/thank-you/" />
      <input type="hidden" name="_subject" value="New lead - JB Software Solutions" />
      <input type="hidden" name="_template" value="table" />
      <input type="hidden" name="_captcha" value="false" />
      <input class="honey" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true" />
      <label>Name<input name="name" required placeholder="Your name" /></label>
      <label>Email<input type="email" name="email" required placeholder="you@company.com" /></label>
      <label>Company / project name<input name="company" placeholder="Optional" /></label>
      <label>Service
        <select name="service">
          <option>Web development</option>
          <option>Mobile app</option>
          <option>Custom software</option>
          <option>SEO / AEO / GEO</option>
          <option>Workflow / business automation</option>
          <option>Desktop app</option>
          <option>Not sure yet</option>
        </select>
      </label>
      <label>Budget range
        <select name="budget">
          <option>Under ₹1 lakh</option>
          <option>₹1-5 lakh</option>
          <option>₹5-15 lakh</option>
          <option>₹15 lakh+</option>
          <option>Not sure yet</option>
        </select>
      </label>
      <label>Project details<textarea name="message" required placeholder="Goals, timeline, links, must-haves"></textarea></label>
      <p class="form-legal">By sending this form you agree to our <a href="{rel(1)}privacy/">privacy policy</a> and <a href="{rel(1)}terms/">terms</a>.</p>
      <button class="btn btn-primary btn-magnet" type="submit">Get my quote</button>
    </form>
    <div class="prose">
      <h2>How we reply</h2>
      <p>This form emails the JB team directly and sends you to a confirmation page. Prefer email? Write <a href="mailto:{EMAIL}">{EMAIL}</a> with your brief.</p>
      <h2>What happens next</h2>
      <ul>
        <li>We confirm fit within 24 hours on business days</li>
        <li>You get a written scope outline</li>
        <li>We agree fixed or phased pricing before build starts</li>
      </ul>
      <p><a href="{rel(1)}pricing/">See starting prices</a> if you want ballpark numbers first.</p>
      <p class="section-note">By submitting, you agree we may contact you about your enquiry. See our <a href="{rel(1)}privacy/">privacy policy</a> and <a href="{rel(1)}terms/">terms</a>.</p>
    </div>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "contact" / "index.html", contact)

pricing = head(
    f"Pricing | Software, Apps and SEO Starting Costs | {BRAND}",
    "Transparent starting prices for websites, mobile apps, custom software, SEO, AEO, GEO and workflow automation from JB Software Solutions in India.",
    "software development cost India, website development price, Flutter app cost, SEO retainer India, custom software pricing",
    "/pricing/",
    1,
) + f"""
<body>
{nav(1, "pricing")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Pricing</div>
    <h1>Starting prices, not mystery quotes</h1>
    <p>Buyers compare India agencies on clarity. These floors help you budget. Final quotes are fixed or phased after discovery.</p>
    <div class="hero-cta" style="margin-top:1.75rem">
      <a class="btn btn-primary btn-magnet" href="{rel(1)}contact/">Get a scoped quote</a>
      <a class="btn btn-ghost btn-magnet" href="{rel(1)}services/web-development/">Browse services</a>
    </div>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container">
    <div class="price-grid">
      <article class="price-card reveal">
        <h3>Website development</h3>
        <div class="from">From ₹50,000</div>
        <ul>
          <li>Business website, about 5 to 12 pages</li>
          <li>Works well on phones</li>
          <li>Contact form and basic SEO setup</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card is-featured reveal">
        <h3>Web app development</h3>
        <div class="from">From ₹3,00,000</div>
        <ul>
          <li>First version of your product in the browser</li>
          <li>Login, dashboard or simple workflows</li>
          <li>Clear milestones and handover docs</li>
        </ul>
        <a class="btn btn-primary btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>Mobile app development</h3>
        <div class="from">From ₹5,00,000</div>
        <ul>
          <li>First app for Android and/or iPhone</li>
          <li>Typical timeline around 8 to 12 weeks</li>
          <li>Help publishing to the app stores</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>Custom software</h3>
        <div class="from">From ₹4,00,000</div>
        <ul>
          <li>Internal tools for your team</li>
          <li>Connect to the apps you already use</li>
          <li>You own the finished work</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>SEO and visibility</h3>
        <div class="from">From ₹25,000/mo</div>
        <ul>
          <li>Help people find you on Google</li>
          <li>Useful content for buyer questions</li>
          <li>Checks for AI search mentions</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>Workflow automation</h3>
        <div class="from">From ₹75,000</div>
        <ul>
          <li>Lead and follow-up flows</li>
          <li>Connect forms, chat and CRM</li>
          <li>Approvals and reminders</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
    </div>
    <div class="prose" style="margin-top:2.5rem">
      <h2>What changes the number</h2>
      <p>Integrations, compliance, bilingual content, offline/desktop needs, and how finished your requirements already are. We would rather quote honestly than win a fake low bid.</p>
      <p><a class="btn btn-primary btn-magnet" href="{rel(1)}contact/">Get a fixed or phased quote</a></p>
    </div>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "pricing" / "index.html", pricing)

thanks = head(
    f"Thank you | {BRAND}",
    "Thanks for contacting JB Software Solutions. We will reply within 24 hours on business days.",
    BRAND,
    "/thank-you/",
    1,
) + f"""
<body>
{nav(1)}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Received</div>
    <h1>Thanks. Your brief is with us.</h1>
    <p>We reply within 24 hours on business days with fit, next steps and a path to a written quote. Meanwhile, skim pricing or the FAQ hub.</p>
    <div class="hero-cta" style="margin-top:1.5rem">
      <a class="btn btn-primary btn-magnet" href="{rel(1)}pricing/">View pricing</a>
      <a class="btn btn-ghost btn-magnet" href="{rel(1)}faq/">Browse FAQs</a>
    </div>
  </div></section>
</main>
{footer(1)}
"""
# thank-you should stay indexable lightly or noindex - keep indexable for honesty but low priority via seo.config
write(ROOT / "thank-you" / "index.html", thanks)

# ---------- BLOG INDEX + POSTS ----------
posts = [
    {
        "slug": "what-is-geo-aeo-llm-seo-2026",
        "title": "What is GEO, AEO and LLM SEO in 2026?",
        "desc": "A practical guide to Generative Engine Optimization, Answer Engine Optimization and LLM SEO so your brand gets cited in ChatGPT, Gemini and Perplexity.",
        "keywords": "GEO, generative engine optimization, AEO, answer engine optimization, LLM SEO, ChatGPT SEO, AI Overviews, Perplexity SEO",
        "image": "/assets/blog/geo-aeo-2026.jpg",
        "date": "2026-10-15",
        "body": """
<p>Buyers still Google. They also ask ChatGPT, Gemini, Perplexity and Google AI Overviews. If your brand only optimizes for ten blue links, you are invisible in the new shortlist.</p>
<h2>SEO vs AEO vs GEO vs LLM SEO</h2>
<ul>
  <li><strong>SEO</strong> ranks pages in classic search results through technical health, content and authority.</li>
  <li><strong>AEO (Answer Engine Optimization)</strong> structures content so answer boxes, People Also Ask and voice-style results can lift a direct answer.</li>
  <li><strong>GEO (Generative Engine Optimization)</strong> earns citations inside generative answers. Models pick sources that look specific, corroborated and entity-clear.</li>
  <li><strong>LLM SEO</strong> is the umbrella term teams use for being retrieved and named by large language models.</li>
</ul>
<h2>What actually moves citations</h2>
<p>Generic "end-to-end digital transformation" pages match nobody's question. Specific capability pages, technology pages, industry pages, pricing guidance, case studies with numbers, and consistent profiles on Clutch-style directories give models something to quote.</p>
<h2>A 30-day starter plan</h2>
<ol>
  <li>Fix crawl, sitemap, robots and Core Web Vitals issues.</li>
  <li>Publish clear service pages with FAQs written like sales calls.</li>
  <li>Add Organization, Service and FAQ schema where accurate.</li>
  <li>Ship two proof pieces: a technical case study and an engineer-authored explainer.</li>
  <li>Test five buyer prompts across ChatGPT, Gemini and Perplexity monthly.</li>
</ol>
<p>At {BRAND}, we build the site and the GEO layer together so engineering choices never fight discovery. <a href="{SITE}/services/seo-aeo-geo/">See SEO, AEO and GEO services</a>.</p>
""".format(BRAND=BRAND, SITE=SITE),
    },
    {
        "slug": "custom-software-development-cost-india-2026",
        "title": "Custom Software Development Cost in India 2026",
        "desc": "India 2026 cost ranges for MVPs, internal tools and multi-platform custom software, plus the scope decisions that change the quote.",
        "keywords": "custom software development cost India, software development cost 2026, MVP cost India, hire developers India rates",
        "image": "/assets/blog/custom-software-cost.jpg",
        "date": "2026-10-15",
        "body": f"""
<p>There is no honest single price for custom software. There is a honest way to budget. Here is how {BRAND} frames 2026 India engagements for founders who need clarity before they sign.</p>
<h2>Ballpark ranges (INR)</h2>
<ul>
  <li><strong>Marketing website</strong> with SEO foundations: roughly ₹50,000 to ₹5,00,000 depending on pages, CMS and integrations.</li>
  <li><strong>Web MVP / SaaS slice</strong>: ₹3,00,000 to ₹15,00,000 for a focused first release.</li>
  <li><strong>Mobile MVP</strong> (Flutter or React Native): ₹5,00,000 to ₹20,00,000.</li>
  <li><strong>Internal tool / CRM-style system</strong>: ₹4,00,000 to ₹25,00,000+ based on roles, workflows and integrations.</li>
</ul>
<p>Premium or regulated builds (fintech, health, complex hardware) sit above these bands. Offshore hourly mid-market rates commonly land around $15 to $49 per hour depending on seniority.</p>
<h2>What moves the number</h2>
<ul>
  <li>Number of user roles and approval flows</li>
  <li>Third-party integrations (payments, WhatsApp, ERPs)</li>
  <li>Offline / desktop / hardware requirements</li>
  <li>Compliance, audit logs and data residency</li>
  <li>How finished the design and product decisions already are</li>
</ul>
<h2>How to not waste money</h2>
<p>Freeze an MVP that proves one business outcome. Ship in milestones. Keep IP and source access in writing. Pair the build with basic SEO/AEO so launch day is not also day zero of discoverability.</p>
<p>Want a scoped estimate? <a href="{SITE}/contact/">Contact us</a> or read <a href="{SITE}/services/custom-software/">custom software services</a>.</p>
""",
    },
    {
        "slug": "flutter-vs-react-native-mvp-india-2026",
        "title": "Flutter vs React Native for an India MVP in 2026",
        "desc": "Choose Flutter or React Native for your India startup MVP with a clear decision framework for speed, talent, UI and long-term maintenance.",
        "keywords": "Flutter vs React Native 2026, Flutter MVP India, React Native app development, cross platform mobile app",
        "image": "/assets/blog/flutter-rn-mvp.jpg",
        "date": "2026-10-15",
        "body": f"""
<p>Most India MVPs need Android first and iOS close behind. Cross-platform is the default. The real question is Flutter or React Native.</p>
<h2>Pick Flutter when</h2>
<ul>
  <li>UI polish and consistent design systems matter on day one</li>
  <li>You want strong Android performance with a single codebase</li>
  <li>Your team is comfortable learning Dart or hiring Flutter talent</li>
</ul>
<h2>Pick React Native when</h2>
<ul>
  <li>Your web product is already React and you want shared patterns</li>
  <li>You need to plug into a large JS hiring pool quickly</li>
  <li>You expect heavy reuse of web business logic in TypeScript</li>
</ul>
<h2>MVP checklist either way</h2>
<ol>
  <li>One primary user journey, not twelve half-built screens</li>
  <li>Analytics and crash reporting from build one</li>
  <li>A release train for Play Store (and App Store if in scope)</li>
  <li>A maintenance budget. Apps are not fire-and-forget</li>
</ol>
<p>{BRAND} ships both stacks. We recommend after a short discovery, not after a framework argument. <a href="{SITE}/services/mobile-app-development/">Mobile app development services</a>.</p>
""",
    },
]

blog_index_cards = []
for post in posts:
    blog_index_cards.append(f"""
      <a class="blog-card reveal" href="{post['slug']}/">
        <img src="{rel(1)}assets/blog/{Path(post['image']).name}" alt="" width="640" height="360" loading="lazy" />
        <div class="body">
          <time datetime="{post['date']}">15 Oct 2026</time>
          <h3>{post['title']}</h3>
          <p>{post['desc']}</p>
        </div>
      </a>""")

blog_index = head(
    f"Blog | Software, SEO, GEO and App Insights | {BRAND}",
    "Guides from JB Software Solutions on GEO, AEO, custom software cost in India, Flutter vs React Native, and AI-era product building.",
    "software development blog, GEO guide, custom software cost India, Flutter vs React Native, SEO blog India",
    "/blog/",
    1,
) + f"""
<body>
{nav(1, "blog")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Blog</div>
    <h1>Notes from shipping software in the AI search era</h1>
    <p>Practical writing for founders and operators. No recycled listicles.</p>
    <div class="hero-cta" style="margin-top:1.75rem">
      <a class="btn btn-primary btn-magnet" href="{rel(1)}contact/">Talk to us</a>
      <a class="btn btn-ghost btn-magnet" href="{rel(1)}pricing/">Pricing</a>
    </div>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container">
    <div class="blog-grid">{''.join(blog_index_cards)}</div>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "blog" / "index.html", blog_index)

for post in posts:
    article_ld = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{post['title']}",
    "description": "{post['desc']}",
    "datePublished": "{post['date']}",
    "dateModified": "{post['date']}",
    "author": {{ "@type": "Organization", "name": "{BRAND}" }},
    "publisher": {{ "@type": "Organization", "name": "{BRAND}", "logo": {{ "@type": "ImageObject", "url": "{SITE}/assets/logo-mark.png" }} }},
    "image": "{SITE}{post['image']}",
    "mainEntityOfPage": "{SITE}/blog/{post['slug']}/",
    "keywords": "{post['keywords']}"
  }}
  </script>
"""
    html = head(
        f"{post['title']} | {BRAND}",
        post["desc"],
        post["keywords"],
        f"/blog/{post['slug']}/",
        2,
        og_type="article",
        image=post["image"],
        extra_jsonld=article_ld,
    ) + f"""
<body>
{nav(2, "blog")}
<main>
  <section class="page-hero">
    <div class="container">
      <div class="section-kicker">Blog</div>
      <h1>{post['title']}</h1>
      <p>{post['desc']}</p>
      <div class="hero-cta" style="margin-top:1.5rem">
        <a class="btn btn-primary btn-magnet" href="{rel(2)}contact/">Talk to us</a>
        <a class="btn btn-ghost btn-magnet" href="{rel(2)}blog/">All posts</a>
      </div>
    </div>
  </section>
  <article class="section" style="padding-top:0">
    <div class="container prose">
      <p class="post-meta"><time datetime="{post['date']}">15 October 2026</time> · {BRAND}</p>
      <div class="post-cover"><img src="{rel(2)}assets/blog/{Path(post['image']).name}" alt="{post['title']}" width="1200" height="675" /></div>
      {post['body']}
      <p><a href="{rel(2)}blog/">Back to blog</a> · <a href="{rel(2)}contact/">Talk to us</a></p>
    </div>
  </article>
</main>
{footer(2)}
"""
    write(ROOT / "blog" / post["slug"] / "index.html", html)

# posts.json
posts_json = [
    {
        "slug": p["slug"],
        "title": p["title"],
        "description": p["desc"],
        "date": p["date"],
        "image": p["image"],
        "url": f"{SITE}/blog/{p['slug']}/",
    }
    for p in posts
]
(ROOT / "blog" / "posts.json").write_text(json.dumps(posts_json, indent=2), encoding="utf-8")
print("wrote blog/posts.json")

# ---------- GLOSSARY + FAQ (entity pages for Google + AI assistants) ----------
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

FAQ_TOPICS = all_faq_topics()


def faq_schema(questions):
    entities = []
    for q, a in questions:
        qq = q.replace("{BRAND}", BRAND).replace("{EMAIL}", EMAIL)
        aa = a.replace("{BRAND}", BRAND).replace("{EMAIL}", EMAIL)
        entities.append(
            {
                "@type": "Question",
                "name": qq,
                "acceptedAnswer": {"@type": "Answer", "text": aa},
            }
        )
    return (
        '<script type="application/ld+json">\n'
        + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


# Glossary index
gloss_cards = "\n".join(
    f'<a class="term-card reveal" href="{slug}/"><strong>{title}</strong><span>{short}</span></a>'
    for slug, title, short, _long in GLOSSARY
)
glossary_index = head(
    f"Glossary | Software, Apps, SEO and Automation Terms | {BRAND}",
    "Plain-language glossary of website development, mobile apps, custom software, SEO, AEO, GEO and automation terms from JB Software Solutions.",
    "software glossary, SEO glossary, GEO meaning, AEO meaning, custom software definition, mobile app development meaning",
    "/glossary/",
    1,
) + f"""
<body>
{nav(1, "glossary")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Resources</div>
    <h1>Glossary</h1>
    <p>Short, clear definitions of the words people use when they hire a software company in India.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container">
    <div class="term-grid">{gloss_cards}</div>
    <p class="section-note reveal" style="margin-top:2rem">Looking for questions instead of definitions? Visit the <a href="{rel(1)}faq/">FAQ hub</a> or <a href="{rel(1)}contact/">contact us</a>.</p>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "glossary" / "index.html", glossary_index)

for slug, title, short, long_tpl in GLOSSARY:
    long_text = long_tpl.replace("{BRAND}", BRAND)
    others = [(s, t) for s, t, _sh, _l in GLOSSARY if s != slug][:8]
    related = "".join(f'<a class="service-chip" href="{rel(2)}glossary/{s}/">{t}</a>' for s, t in others)
    defined = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "DefinedTerm",
                "@id": f"{SITE}/glossary/{slug}/#term",
                "name": title,
                "description": short,
                "inDefinedTermSet": f"{SITE}/glossary/",
                "url": f"{SITE}/glossary/{slug}/",
            },
            {
                "@type": "WebPage",
                "@id": f"{SITE}/glossary/{slug}/#webpage",
                "url": f"{SITE}/glossary/{slug}/",
                "name": f"{title} | Glossary | {BRAND}",
                "description": short,
                "isPartOf": {"@id": f"{SITE}/#website"},
                "about": {"@id": f"{SITE}/glossary/{slug}/#term"},
            },
        ],
    }
    extra = '<script type="application/ld+json">\n' + json.dumps(defined, ensure_ascii=False, indent=2) + "\n</script>"
    page = head(
        f"{title} | Glossary | {BRAND}",
        short,
        f"{title}, {title} meaning, {title} definition, {BRAND}",
        f"/glossary/{slug}/",
        2,
        extra_jsonld=extra,
    ) + f"""
<body>
{nav(2, "glossary")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker"><a href="{rel(2)}glossary/">Glossary</a></div>
    <h1>{title}</h1>
    <p>{short}</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container prose">
    <h2>Definition</h2>
    <p>{long_text}</p>
    <h2>Why this matters when you hire {BRAND}</h2>
    <p>Clear language helps you shortlist the right vendor. This page exists so "{title}" maps to a real service and a real team at {BRAND}, not a vague buzzword.</p>
    <p><a class="btn btn-primary btn-magnet" href="{rel(2)}contact/">Ask about {title.lower()}</a>
       <a class="btn btn-ghost btn-magnet" href="{rel(2)}faq/">Browse FAQs</a></p>
    <h2>Related terms</h2>
    <div class="term-related">{related}</div>
  </div></section>
</main>
{footer(2)}
"""
    write(ROOT / "glossary" / slug / "index.html", page)

# FAQ index
FAQ_Q_COUNT = count_faqs()
faq_cards = "\n".join(
    f'<a class="faq-topic-card reveal" href="{t["slug"]}/"><strong>{t["title"]}</strong><span>{t["desc"]}</span></a>'
    for t in FAQ_TOPICS
)
all_home_qs = []
for t in FAQ_TOPICS:
    all_home_qs.extend(t["qs"][:2])
faq_index = head(
    f"FAQ | {FAQ_Q_COUNT}+ Software, Apps, SEO and Pricing Answers | {BRAND}",
    f"Frequently asked questions about website development, mobile apps, custom software, SEO, GEO and hiring JB Software Solutions in India. {FAQ_Q_COUNT}+ indexed answers across {len(FAQ_TOPICS)} topic pages.",
    "software development FAQ India, website cost FAQ, mobile app cost FAQ, SEO FAQ, hire software company India, custom software development company India FAQ",
    "/faq/",
    1,
    extra_jsonld=faq_schema(all_home_qs),
) + f"""
<body>
{nav(1, "faq")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Resources</div>
    <h1>FAQs</h1>
    <p>{FAQ_Q_COUNT}+ direct answers across {len(FAQ_TOPICS)} topic pages covering software, apps, SEO, pricing and how we work.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container">
    <div class="faq-topic-grid">{faq_cards}</div>
    <div class="faq" style="margin-top:2.5rem">
      {''.join(f'<details><summary>{q.replace("{BRAND}", BRAND)}</summary><p>{a.replace("{BRAND}", BRAND).replace("{EMAIL}", EMAIL)}</p></details>' for q,a in all_home_qs)}
    </div>
    <p class="section-note reveal" style="margin-top:2rem">Need definitions? Open the <a href="{rel(1)}glossary/">glossary</a>. Ready to talk? <a href="{rel(1)}contact/">Contact {BRAND}</a>.</p>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "faq" / "index.html", faq_index)

for topic in FAQ_TOPICS:
    qs = [(q.replace("{BRAND}", BRAND).replace("{EMAIL}", EMAIL), a.replace("{BRAND}", BRAND).replace("{EMAIL}", EMAIL)) for q, a in topic["qs"]]
    details = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qs)
    page = head(
        f"{topic['title']} | FAQ | {BRAND}",
        topic["desc"],
        f"{topic['title']}, {BRAND} FAQ, software FAQ India",
        f"/faq/{topic['slug']}/",
        2,
        extra_jsonld=faq_schema(topic["qs"]),
    ) + f"""
<body>
{nav(2, "faq")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker"><a href="{rel(2)}faq/">FAQ</a></div>
    <h1>{topic['title']}</h1>
    <p>{topic['desc']}</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container">
    <div class="faq">{details}</div>
    <div class="cta-band reveal" style="margin-top:2rem">
      <div><h2>Still unsure?</h2><p>Send your goals and constraints. We reply with fit and next steps.</p></div>
      <a class="btn btn-primary btn-magnet" href="{rel(2)}contact/">Contact {BRAND}</a>
    </div>
    <p style="margin-top:1.5rem"><a href="{rel(2)}faq/">All FAQ topics</a> · <a href="{rel(2)}glossary/">Glossary</a></p>
  </div></section>
</main>
{footer(2)}
"""
    write(ROOT / "faq" / topic["slug"] / "index.html", page)

print(f"wrote glossary ({len(GLOSSARY)} terms) + faq ({len(FAQ_TOPICS)} topics, {FAQ_Q_COUNT} Q&As)")

# ---------- PRIVACY + TERMS ----------
privacy = head(
    f"Privacy Policy | {BRAND}",
    "How JB Software Solutions collects, uses, stores and protects personal information from our website, contact form, email and project work under Indian law including the IT Act and DPDP Act.",
    "JB Software Solutions privacy policy, data protection, DPDP, contact form privacy India, website cookies Google Analytics",
    "/privacy/",
    1,
) + f"""
<body>
{nav(1)}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Legal</div>
    <h1>Privacy policy</h1>
    <p>Last updated: 15 October 2026. This notice explains what personal information {BRAND} collects through jbsoftwaresolutions.com and related project work, why we use it, and the choices you have.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container prose prose-wide">
    <h2>1. Who we are</h2>
    <p>{BRAND} ("we", "us", "our") provides website development, mobile app development, custom software, desktop apps, SEO, AEO, GEO and workflow automation services. Our public website is <a href="{SITE}/">{SITE}/</a>. For privacy questions, email <a href="mailto:{EMAIL}">{EMAIL}</a> or use the <a href="{rel(1)}contact/">contact form</a>.</p>
    <p>This policy covers visitors and enquirers on our marketing site, people who email us, and (at a high level) how we handle personal data shared with us during a client engagement. A signed statement of work, master services agreement or non-disclosure agreement may add stricter rules for a specific project. Where those documents conflict with this page on project data, the signed document controls for that project.</p>

    <h2>2. Scope</h2>
    <p>This policy applies to:</p>
    <ul>
      <li>jbsoftwaresolutions.com and pages we publish under that domain</li>
      <li>Our contact form and email conversations about enquiries</li>
      <li>Analytics and technical logs created when you browse the site</li>
      <li>Personal data you share so we can quote, contract, invoice or deliver services</li>
    </ul>
    <p>It does not govern third-party sites we link to, app stores, payment gateways you use with your own customers, or products we build for you once those products are live under your accounts. Those systems have their own operators and policies.</p>

    <h2>3. Information we collect</h2>
    <h3>3.1 Information you give us</h3>
    <ul>
      <li><strong>Contact and enquiry data:</strong> name, email address, company or project name, service interest, budget range, message text, and any files or links you choose to share</li>
      <li><strong>Communication records:</strong> emails, call notes and meeting notes related to your enquiry or project</li>
      <li><strong>Business and billing data for clients:</strong> billing name, address, GSTIN where needed, bank or UPI details for receiving or sending invoices, and payment references. We do not store full card numbers on our website. Card payments, if used, are handled by the payment partner named in your invoice or agreement</li>
      <li><strong>Project materials:</strong> credentials, content, customer lists, designs, source access and other materials you provide so we can deliver the work. We treat these as confidential under our engagement terms</li>
    </ul>
    <h3>3.2 Information collected automatically</h3>
    <ul>
      <li><strong>Device and browser data:</strong> IP address, browser type, device type, operating system, language and approximate location derived from IP</li>
      <li><strong>Usage data:</strong> pages viewed, referrer, time on page, clicks and similar interaction events</li>
      <li><strong>Cookies and similar technologies:</strong> see section 6</li>
    </ul>
    <h3>3.3 Sensitive personal data</h3>
    <p>We do not ask website visitors for sensitive personal data (for example health, biometrics, caste, religion or political opinions). If a project requires handling such data for your users, we will agree purpose, security and processing roles in writing before that work starts.</p>

    <h2>4. How we use personal information</h2>
    <ul>
      <li>To respond to enquiries, assess fit and prepare quotes</li>
      <li>To enter into and perform contracts, deliver services, support you and provide handover</li>
      <li>To invoice, collect payment, maintain accounting and meet tax or statutory duties in India</li>
      <li>To improve the website, measure traffic and fix technical issues</li>
      <li>To send project updates and, only where appropriate, limited service announcements. You can ask us to stop marketing messages at any time</li>
      <li>To detect abuse, spam, fraud or security incidents</li>
      <li>To establish, exercise or defend legal claims</li>
    </ul>
    <p>We do not sell your personal information. We do not rent enquiry lists to advertisers.</p>

    <h2>5. Legal bases and Indian law</h2>
    <p>We process personal data in line with applicable Indian law, including the Information Technology Act, 2000 and the Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011, and we are preparing practices for the Digital Personal Data Protection Act, 2023 (DPDP Act) and its rules as they apply to our business.</p>
    <p>Depending on the context, processing rests on your consent (for example submitting the contact form), performance of a contract or steps prior to a contract, our legitimate interests in running and securing an agency website, and legal obligations such as tax retention.</p>

    <h2>6. Cookies, analytics and similar tools</h2>
    <p>Our site uses:</p>
    <ul>
      <li><strong>Essential technical storage</strong> needed for the site to load and function</li>
      <li><strong>Google Analytics 4</strong> (measurement ID G-RMGPE314SF) to understand aggregate traffic and page performance. Google may process data according to its own terms and privacy policy</li>
      <li><strong>Fonts and CDN assets</strong> loaded from Google Fonts / Google hosts when you visit pages that request them</li>
    </ul>
    <p>You can block or delete cookies in your browser. Blocking some cookies may affect analytics accuracy but should not block the core marketing pages. We do not currently run advertising pixels for retargeting on this site. If that changes, we will update this policy.</p>

    <h2>7. Who we share data with</h2>
    <p>We share personal data only when needed to operate the business or when the law requires it:</p>
    <ul>
      <li><strong>FormSubmit</strong> (formsubmit.co) receives contact-form submissions and emails them to {EMAIL}. Their processing is governed by FormSubmit's terms and privacy practices</li>
      <li><strong>Email providers</strong> that deliver and store business email</li>
      <li><strong>Google Analytics / Google</strong> for site analytics as described above</li>
      <li><strong>Hosting and infrastructure</strong> such as GitHub Pages (or a successor host) that serves this static website</li>
      <li><strong>Professional advisers</strong> (for example accountants or lawyers) under confidentiality where needed</li>
      <li><strong>Authorities</strong> when required by Indian law, court order or a lawful request</li>
      <li><strong>Subcontractors or specialists</strong> we engage for a project, only as needed, under confidentiality and instructions that match the engagement</li>
    </ul>
    <p>If we use additional tools (project boards, cloud repos, design tools), access is limited to people working on your project.</p>

    <h2>8. International transfers</h2>
    <p>Our team primarily works from India. Some processors (for example form delivery, analytics or hosting) may store or process data on servers outside India. By using the site or submitting an enquiry, you understand that your information may be processed in other countries with different data-protection rules. We take reasonable steps to work with reputable providers and to limit what we send them to what is needed.</p>

    <h2>9. Retention</h2>
    <ul>
      <li><strong>Website enquiries:</strong> typically up to 24 months from last meaningful contact, unless a project starts or you ask us to delete sooner where we can</li>
      <li><strong>Client and project records:</strong> for the life of the engagement and a reasonable period after, often 3 years or longer where needed for support, IP proof or disputes</li>
      <li><strong>Financial and tax records:</strong> as required under Indian tax and company law (often 8 years or more for certain records)</li>
      <li><strong>Analytics data:</strong> according to Google Analytics retention settings (commonly up to 26 months unless changed)</li>
    </ul>
    <p>When retention ends, we delete or anonymise data where practical, except where the law requires us to keep it.</p>

    <h2>10. Security</h2>
    <p>We use reasonable technical and organisational measures appropriate to a small software agency: HTTPS on the public site, access limited to people who need it, careful handling of credentials, and private repositories for client code where we control the repo. No method of transmission or storage is perfectly secure. Please do not send passwords or production secrets over public forms or unencrypted chat unless we agree a safer channel.</p>
    <p>If we become aware of a personal data breach that is likely to cause significant harm, we will take steps required by applicable law, which may include notifying affected people and relevant authorities where mandatory.</p>

    <h2>11. Your choices and rights</h2>
    <p>Subject to Indian law and reasonable verification, you may ask us to:</p>
    <ul>
      <li>Confirm whether we hold personal data about you and receive a copy</li>
      <li>Correct inaccurate or incomplete data</li>
      <li>Withdraw consent where processing is based on consent</li>
      <li>Request deletion where the law allows and retention is no longer required</li>
      <li>Object to or restrict certain processing where applicable</li>
      <li>Nominate another person to exercise rights in limited circumstances under the DPDP Act once those provisions apply to us in practice</li>
    </ul>
    <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with the subject "Privacy request". We aim to respond within 15 working days. We may keep limited records of the request itself. If you are unhappy with our response, you may escalate under the grievance process below and, where available, to the Data Protection Board of India or other competent authority.</p>

    <h2>12. Children</h2>
    <p>Our services and website are aimed at businesses and adults 18 years or older. We do not knowingly collect personal data from children. If you believe a minor has submitted information, contact us and we will delete it where appropriate.</p>

    <h2>13. Client products and end-user data</h2>
    <p>When we build software for you, you are typically the controller (or equivalent) of your end users' data. You must have a lawful basis and your own privacy notices for that product. We process such data only as needed to deliver the project, under your instructions and our confidentiality terms, unless a separate data processing agreement says otherwise.</p>

    <h2>14. Third-party links</h2>
    <p>Our site may link to GitHub, Google, FormSubmit and other services. Their privacy practices are their own. Read their policies before sharing data with them.</p>

    <h2>15. Changes to this policy</h2>
    <p>We may update this page when our practices, tools or the law change. The "Last updated" date at the top will change. Continued use of the site after an update means you have read the revised notice. For material changes that affect existing clients, we may also notify the primary contact by email where practical.</p>

    <h2>16. Grievance officer / contact</h2>
    <p>For privacy or data-protection complaints related to this website or our services:</p>
    <ul>
      <li><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><strong>Contact form:</strong> <a href="{rel(1)}contact/">{SITE}/contact/</a></li>
    </ul>
    <p>We aim to acknowledge and resolve grievances within 15 working days where reasonably possible. See also our <a href="{rel(1)}terms/">terms and conditions</a>.</p>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "privacy" / "index.html", privacy)

terms = head(
    f"Terms and Conditions | {BRAND}",
    "Terms of use for jbsoftwaresolutions.com and engagement terms overview for software, app, website, SEO and automation services from JB Software Solutions in India.",
    "JB Software Solutions terms, terms of service India, website terms, software development agreement overview, IP ownership",
    "/terms/",
    1,
) + f"""
<body>
{nav(1)}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Legal</div>
    <h1>Terms and conditions</h1>
    <p>Last updated: 15 October 2026. These terms cover use of jbsoftwaresolutions.com and the general rules for hiring {BRAND}. Paid work is always confirmed in a written quote, statement of work or agreement.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container prose prose-wide">
    <h2>1. Agreement to these terms</h2>
    <p>By browsing this website, submitting the contact form, emailing us, or engaging {BRAND} for services, you agree to these terms and our <a href="{rel(1)}privacy/">privacy policy</a>. If you do not agree, do not use the site or request services.</p>
    <p>If you act for a company, you confirm you are authorised to bind that company. "You" means the individual or the organisation you represent.</p>

    <h2>2. Who we are</h2>
    <p>{BRAND} provides software and digital services including website development, web applications, mobile apps, desktop apps, custom business software, SEO, AEO, GEO and workflow automation. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{SITE}/contact/">{SITE}/contact/</a>.</p>

    <h2>3. Website use</h2>
    <ul>
      <li>The site is for information about our services and to receive business enquiries</li>
      <li>Content is provided for general guidance. It is not legal, tax, accounting or investment advice</li>
      <li>We may change, pause or remove pages, prices shown as starting ranges, or features without notice</li>
      <li>You may not scrape the site in a way that harms availability, attempt unauthorised access, upload malware, or use the site for unlawful, harassing or fraudulent activity</li>
      <li>You may not copy substantial site content for commercial reuse without our written permission, except fair dealing or other rights Indian law allows</li>
    </ul>

    <h2>4. Enquiries, quotes and when a contract starts</h2>
    <p>Sending a form, chat or email is a request for information, not a binding order. Ballpark prices on the <a href="{rel(1)}pricing/">pricing page</a> and elsewhere are illustrative starting ranges, not fixed offers.</p>
    <p>A paid engagement starts only when we issue a written quote or statement of work (SOW) and you accept it in writing (email is enough) and, where required, pay the agreed advance. The SOW, invoice terms and any master agreement sit above these website terms for that project. If documents conflict, the order of control is: signed MSA (if any), then SOW / accepted quote, then these website terms, then marketing pages.</p>

    <h2>5. Scope of services</h2>
    <p>Services may include discovery, design, development, testing, deployment support, SEO / AEO / GEO work, automation setup, documentation and support windows as written in the SOW. Unless the SOW says otherwise:</p>
    <ul>
      <li>Work outside the written scope needs a change request and may change price and timeline</li>
      <li>Third-party fees (hosting, domains, app store accounts, SMS, paid APIs, stock assets, ads) are yours unless we clearly include them</li>
      <li>App store approval, Google ranking, AI citation, lead volume and revenue outcomes depend on many factors outside our sole control. We commit to professional effort against the agreed scope, not to guaranteed rankings, traffic numbers or sales figures unless a written guarantee says so</li>
    </ul>

    <h2>6. Client responsibilities</h2>
    <p>You agree to:</p>
    <ul>
      <li>Provide timely access, content, feedback and decisions so we can meet the schedule</li>
      <li>Ensure you have rights to materials you supply (logos, copy, data, credentials)</li>
      <li>Keep login secrets safe and rotate anything shared after handover when appropriate</li>
      <li>Use deliverables lawfully and in line with app-store, payment and platform rules that apply to your product</li>
      <li>Pay invoices on the dates in the SOW or invoice</li>
    </ul>
    <p>Delays on your side may push timelines. We are not responsible for losses caused by late feedback, missing assets or third-party outages.</p>

    <h2>7. Fees, taxes, advances and refunds</h2>
    <ul>
      <li>Fees are usually in Indian rupees unless we agree another currency in writing</li>
      <li>GST and other taxes apply as required by law and will appear on invoices where applicable</li>
      <li>Many projects need an advance before build starts. Remaining amounts follow milestones in the SOW</li>
      <li>Late payment may pause work and may attract reasonable recovery costs</li>
      <li>Advances for work already started are generally non-refundable, except where Indian law requires a refund, where we cancel for our convenience without delivering agreed work, or where a signed SOW expressly allows a refund</li>
      <li>Retainers are billed as stated in the retainer agreement and may renew until either side cancels on the notice period written there</li>
    </ul>

    <h2>8. Intellectual property</h2>
    <p>Unless the SOW says otherwise:</p>
    <ul>
      <li><strong>Your materials</strong> remain yours</li>
      <li><strong>Custom work we create for you</strong> under a paid SOW (code, designs and content made specifically for your project) is assigned to you after full payment of all amounts due for that scope, subject to the licence carve-outs below</li>
      <li><strong>Our pre-existing tools, templates, libraries, know-how and internal frameworks</strong> stay ours. We grant you a non-exclusive licence to use them as embedded in the deliverables for your business</li>
      <li><strong>Open-source and third-party components</strong> keep their own licences. You must follow those licences</li>
      <li>Until invoices for a scope are paid in full, we may withhold final source handover or production credentials for that unpaid scope</li>
    </ul>
    <p>We may showcase non-confidential project names, screenshots or case summaries in our portfolio and proposals unless you ask us in writing to keep a project private. We will not publish secrets, private credentials or confidential business data.</p>

    <h2>9. Confidentiality</h2>
    <p>Each party must protect the other's non-public business information and use it only for the engagement, except information that is public, independently developed, or required to be disclosed by law. This duty continues for a reasonable period after the project ends (at least 3 years unless a signed NDA sets another period).</p>

    <h2>10. Acceptable use of deliverables</h2>
    <p>You must not use our work to break the law, infringe others' rights, distribute malware, process data unlawfully, or misrepresent affiliation with {BRAND}. We may suspend work if we reasonably believe continued delivery would cause us to violate law or platform rules.</p>

    <h2>11. Warranties and disclaimers</h2>
    <p>We warrant that we will perform services with reasonable skill and care consistent with a professional software services firm in India. Except for that and any express written warranty in an SOW, the website and services are provided on an "as available" basis.</p>
    <p>To the fullest extent Indian law allows, we disclaim implied warranties of merchantability, fitness for a particular purpose and non-infringement for marketing-site content and for outcomes that depend on third parties (hosting, stores, search engines, payment networks, client-supplied data quality).</p>
    <p>Browser and device differences, third-party API changes and platform policy changes can affect software after delivery. Support after the warranty or support window in the SOW is chargeable unless included.</p>

    <h2>12. Limitation of liability</h2>
    <p>To the fullest extent permitted by Indian law:</p>
    <ul>
      <li>We are not liable for indirect, incidental, special, consequential, punitive or exemplary damages, or for lost profits, lost revenue, lost data, business interruption or reputational harm, even if advised of the possibility</li>
      <li>Our total aggregate liability arising out of or related to a project is limited to the fees you actually paid us for that project's scope in the 12 months before the claim</li>
      <li>For website visitors who have not paid us, our aggregate liability related to site use is limited to INR 1,000</li>
    </ul>
    <p>Nothing in these terms excludes liability that Indian law does not allow us to exclude, including liability for fraud or for death or personal injury caused by negligence where such exclusion is prohibited.</p>

    <h2>13. Indemnity</h2>
    <p>You agree to indemnify and hold {BRAND} and its team harmless from claims, losses and reasonable costs arising from: materials you supply; your product's compliance with law and platform rules; your end users' data and content; and your misuse of deliverables, except to the extent caused by our wilful misconduct.</p>

    <h2>14. Termination</h2>
    <p>Either party may end an engagement as the SOW describes. We may suspend or end work for non-payment, illegal instructions, abusive conduct, or material breach not cured within a reasonable time after notice. On termination you pay for work performed and approved expenses. Sections on IP, confidentiality, liability, indemnity and governing law survive termination.</p>

    <h2>15. Non-solicitation</h2>
    <p>During an engagement and for 12 months after, you agree not to solicit our employees or exclusive contractors who worked on your project to leave us for a competing role, except with our written consent or via a general public job ad not aimed at them. Reasonable recruitment fees may be due if this clause is breached, as a genuine pre-estimate of disruption.</p>

    <h2>16. Force majeure</h2>
    <p>Neither party is liable for delay or failure caused by events beyond reasonable control, including natural disasters, war, epidemics, major infrastructure failure, or changes in law. Obligations resume when the event ends. Either party may end a long-blocked engagement if the event continues beyond 60 days.</p>

    <h2>17. Third-party services</h2>
    <p>The site uses FormSubmit for form delivery, Google Analytics for traffic measurement, Google Fonts for typography, and GitHub Pages (or successor hosting) for hosting. Your use of those services is also subject to their terms. We are not responsible for outages or policy changes by those providers.</p>

    <h2>18. Electronic communications</h2>
    <p>You agree that quotes, acceptances, notices and invoices may be sent by email or other electronic means and that such records can form a binding record of agreement under Indian law.</p>

    <h2>19. Governing law and disputes</h2>
    <p>These terms and any dispute arising from the website or our services are governed by the laws of India, without regard to conflict-of-law rules. Courts in India shall have exclusive jurisdiction, subject to the city or forum named in a signed SOW or MSA if different.</p>
    <p>Before filing a claim, email <a href="mailto:{EMAIL}">{EMAIL}</a> and allow 15 working days for good-faith resolution. Nothing prevents either party from seeking urgent injunctive relief for IP or confidentiality breaches.</p>

    <h2>20. Grievance contact</h2>
    <p>For complaints about the website or our services: <a href="mailto:{EMAIL}">{EMAIL}</a> or the <a href="{rel(1)}contact/">contact form</a>. We aim to respond within 15 working days.</p>

    <h2>21. Changes</h2>
    <p>We may update these website terms by posting a new version with a new "Last updated" date. Changes do not retroactively rewrite a signed SOW unless both parties agree. For ongoing retainers, material term changes will be communicated to the billing contact where practical.</p>

    <h2>22. Severability and entire agreement (website)</h2>
    <p>If a clause is held unenforceable, the rest remains in force. These website terms plus the privacy policy are the entire agreement for site use. They do not cancel a signed project agreement, which controls for that engagement.</p>

    <h2>23. Contact</h2>
    <p>{BRAND}<br />Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br />Web: <a href="{SITE}/contact/">{SITE}/contact/</a></p>
    <p>Related: <a href="{rel(1)}privacy/">Privacy policy</a> · <a href="{rel(1)}faq/">FAQs</a></p>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "terms" / "index.html", terms)
print("wrote privacy + terms")

# Crawl files (sitemap.xml, robots.txt, llms.txt) are owned by the SEO pipeline:
#   npm run seo  → seo-build.js
#   npm run llms → generate-llms-txt.py
#   npm run push → push-jb-website.ps1 (same gate as Easy Peeze / Kharch Log)
print("note: sitemap/robots/llms are generated by seo-build.js + generate-llms-txt.py on push")

not_found = head(
    f"Page not found | {BRAND}",
    "The page you requested is not available.",
    BRAND,
    "/404.html",
    0,
) + f"""
<body>
{nav(0)}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Error</div>
    <h1>Page not found</h1>
    <p>That route is not in the sitemap. Head home or browse services.</p>
    <div class="hero-cta" style="margin-top:1.5rem">
      <a class="btn btn-primary btn-magnet" href="{SITE}/">Go home</a>
      <a class="btn btn-ghost btn-magnet" href="{SITE}/contact/">Contact</a>
    </div>
  </div></section>
</main>
{footer(0)}
"""
write(ROOT / "404.html", not_found)

# GitHub Pages: project site needs this for 404 sometimes - also add .nojekyll
(ROOT / ".nojekyll").write_text("", encoding="utf-8")
print("done")
