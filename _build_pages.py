# -*- coding: utf-8 -*-
"""Generate JB Software Solutions static site pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://jbsoftwaresolutions.com"
BRAND = "JB Software Solutions"
EMAIL = "info@jbsoftwaresolutions.com"
ASSET_V = "20261016e"  # bump when styles.css / main.js change (GitHub Pages CDN cache)


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
  <meta name="viewport" content="width=device-width, initial-scale=1" />
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
      {a("services", "services/web-development/", "Services")}
      {a("seo", "services/seo-aeo-geo/", "SEO / GEO")}
      {a("ai", "services/ai-automation/", "Automation")}
      {a("pricing", "pricing/", "Pricing")}
      {a("blog", "blog/", "Blog")}
      {a("about", "about/", "About")}
      {a("contact", "contact/", "Contact")}
      <li><a class="nav-cta btn-magnet" href="{p}contact/">Get a quote</a></li>
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
      <a href="{p}services/seo-aeo-geo/">SEO, AEO and GEO</a>
      <a href="{p}services/ai-automation/">Workflow automation</a>
      <a href="{p}pricing/">Pricing</a>
      <a href="{p}blog/">Blog</a>
    </div>
    <div>
      <strong>Company</strong>
      <a href="{p}about/">About</a>
      <a href="{p}contact/">Contact us</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; 2026 {BRAND}. All rights reserved.</span>
    <span>Custom software | Mobile apps | Websites | SEO | Automation</span>
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
    "custom software development company India, web development company India, "
    "mobile app development company, Flutter app development, React Native development, "
    "SEO company India, AEO services, GEO services, generative engine optimization, "
    "LLM SEO, ChatGPT SEO, AI Overviews SEO, workflow automation agency India, "
    "desktop app Electron, Next.js development, SaaS development, ERP software, "
    "hire software developers India, digital agency India, JB Software Solutions"
)

# ---------- HOME ----------
home_lines = [
    "> boot sequence: jb-agent v2.6",
    "> scanning market signals: SEO · AEO · GEO · apps · custom software",
    "> intent detected: **build products that rank and convert**",
    "> stacking: Next.js · Flutter · Node · business workflows · schema markup",
    "> proof mode: this page is not a brochure. it is a live system.",
    "> ready. tell us what you want shipped.",
]
home = head(
    f"{BRAND} | Custom Software Development, Mobile Apps, Websites, SEO, AEO, GEO",
    "JB Software Solutions is a custom software development company in India for web apps, Flutter mobile apps, desktop software, SEO, AEO, GEO and workflow automation. Get found on Google and cited in ChatGPT.",
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
          <div class="hero-brand">
            <img src="assets/logo-full.png" alt="{BRAND} custom software logo" width="180" height="100" />
          </div>
          <p class="hero-eyebrow">{BRAND}</p>
          <h1 class="hero-title">Custom software that <span class="grad">gets found</span></h1>
          <p class="hero-sub">JB Software Solutions builds websites, Flutter and React Native apps, desktop tools, SEO, AEO, GEO and workflow automation. Products that convert, then get found on Google and inside ChatGPT, Gemini and Perplexity.</p>
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
      <span>Custom software India</span><span>Flutter apps</span><span>Next.js websites</span>
      <span>Electron desktop</span><span>Technical SEO</span><span>AEO</span><span>GEO</span>
      <span>Workflow automation</span><span>SaaS MVP</span><span>ERP tools</span>
      <span>ChatGPT citations</span><span>Perplexity SEO</span><span>LLM SEO</span>
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

  <section class="section" id="engagements">
    <div class="container">
      <div class="section-kicker reveal">How buyers usually hire us</div>
      <h2 class="section-title reveal">Three briefs we close again and again</h2>
      <p class="section-sub reveal">No fake logos. Real engagement shapes founders bring us, with outcomes that matter for revenue.</p>
      <div class="engage-grid">
        <article class="engage-card reveal">
          <h3>Launch site that generates enquiries</h3>
          <p>Service or B2B brand needs a fast website, clear offers, schema, and SEO/GEO so Google and ChatGPT can recommend them.</p>
          <p><strong style="color:var(--text)">Typical outcome:</strong> indexed service pages, contact form lead flow, and a content cluster that compounds.</p>
        </article>
        <article class="engage-card reveal">
          <h3>MVP app without burning runway</h3>
          <p>Startup needs Android + iOS or a web product slice in weeks, not a six-month theatre production.</p>
          <p><strong style="color:var(--text)">Typical outcome:</strong> scoped Flutter or Next.js MVP, store or staging launch, and a written plan for v1.1.</p>
        </article>
        <article class="engage-card reveal">
          <h3>Replace spreadsheet chaos</h3>
          <p>Ops team is drowning in sheets, WhatsApp threads and manual follow-ups. They need a custom tool their staff will actually use.</p>
          <p><strong style="color:var(--text)">Typical outcome:</strong> role-based internal system, handover docs, and optional workflow automation on the boring parts.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section" id="promises">
    <div class="container">
      <div class="section-kicker reveal">Risk reverse</div>
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
          <h3>Websites</h3>
          <div class="from">From ₹50,000</div>
          <p>Marketing sites and landing systems with SEO foundations.</p>
        </article>
        <article class="price-card is-featured reveal">
          <h3>Apps and custom software</h3>
          <div class="from">From ₹3,00,000</div>
          <p>Focused web MVPs, Flutter apps and internal tools with clear milestones.</p>
        </article>
        <article class="price-card reveal">
          <h3>SEO / AEO / GEO</h3>
          <div class="from">From ₹25,000/mo</div>
          <p>Technical SEO plus AI-search citation work on a monthly retainer.</p>
        </article>
      </div>
      <p style="margin-top:1.5rem" class="reveal"><a class="btn btn-primary btn-magnet" href="pricing/">See full pricing</a> <a class="btn btn-ghost btn-magnet" href="contact/">Request a fixed quote</a></p>
    </div>
  </section>

  <section class="section" id="why-jb">
    <div class="container">
      <div class="section-kicker reveal">Revenue, not vanity</div>
      <h2 class="section-title reveal">How this site is designed to bring work in</h2>
      <p class="section-sub reveal">If this were only a portfolio, it would lose money. Every section below targets a commercial search or AI shortlist question, then routes to the contact form. Build projects pay once. SEO and GEO retainers compound. The win is owning both.</p>
      <div class="outcome-grid">
        <article class="outcome reveal">
          <h3>Project revenue</h3>
          <p>Websites, mobile MVPs, custom CRMs and desktop apps sold as clear fixed or phased scopes with IP handover.</p>
        </article>
        <article class="outcome reveal">
          <h3>Recurring revenue</h3>
          <p>SEO, AEO, GEO and product retainers that keep rankings, citations and features moving after launch.</p>
        </article>
        <article class="outcome reveal">
          <h3>Inbound that compounds</h3>
          <p>Keyword pages, FAQs, schema and blog clusters so Google and LLMs keep sending qualified founders our way.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section" id="market">
    <div class="container">
      <div class="section-kicker reveal">Competitive reality</div>
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
              <td>Electron and Tauri desktop when the browser is not enough</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="section-note reveal">We respect serious competitors in this category. We do not win by copying their homepage claims. We win by shipping measurable systems: faster pages, clearer offers, indexed content, and follow-through after launch.</p>
    </div>
  </section>

  <section class="section" id="keywords">
    <div class="container">
      <div class="section-kicker reveal">Search demand we serve</div>
      <h2 class="section-title reveal">Commercial keywords mapped to real services</h2>
      <p class="section-sub reveal">These are the queries founders and operators actually type, and the pages we built to answer them without doorway spam.</p>
      <div class="seo-cloud reveal">
        <a class="seo-chip" href="services/custom-software/">custom software development company India</a>
        <a class="seo-chip" href="services/web-development/">web development company</a>
        <a class="seo-chip" href="services/mobile-app-development/">mobile app development company</a>
        <a class="seo-chip" href="services/mobile-app-development/">Flutter app development</a>
        <a class="seo-chip" href="services/mobile-app-development/">React Native development</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">SEO company India</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">GEO generative engine optimization</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">AEO answer engine optimization</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">ChatGPT SEO</a>
        <a class="seo-chip" href="services/seo-aeo-geo/">LLM SEO</a>
        <a class="seo-chip" href="services/ai-automation/">business workflow automation</a>
        <a class="seo-chip" href="services/ai-automation/">AI business automation</a>
        <a class="seo-chip" href="services/desktop-apps/">Electron desktop app development</a>
        <a class="seo-chip" href="services/web-development/">Next.js development</a>
        <a class="seo-chip" href="services/custom-software/">SaaS MVP development</a>
        <a class="seo-chip" href="services/custom-software/">ERP and CRM software</a>
        <a class="seo-chip" href="blog/custom-software-development-cost-india-2026/">software development cost India</a>
        <a class="seo-chip" href="blog/what-is-geo-aeo-llm-seo-2026/">what is GEO</a>
        <a class="seo-chip" href="contact/">hire developers India</a>
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
          <h3>Web development</h3>
          <p>High-performance marketing sites and web apps on Next.js, React and Node. Core Web Vitals, schema markup and conversion paths baked in from sprint one.</p>
          <div class="tags"><span class="tag">Next.js</span><span class="tag">React</span><span class="tag">Node.js</span><span class="tag">SEO-ready</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/web-development/">Web development services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/web.jpg" alt="Web development - modern websites and web apps" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Mobile app development</h3>
          <p>iOS and Android from one Flutter or React Native codebase, or native when the product demands it. Store launch, push, analytics and post-release support.</p>
          <div class="tags"><span class="tag">Flutter</span><span class="tag">React Native</span><span class="tag">iOS</span><span class="tag">Android</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/mobile-app-development/">Mobile app services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/mobile.jpg" alt="Mobile app development for Android and iOS" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Custom software</h3>
          <p>Internal tools, CRMs, dashboards, ERPs and workflow systems tailored to how your team actually works. Full IP handover. No black-box lock-in.</p>
          <div class="tags"><span class="tag">SaaS</span><span class="tag">ERP</span><span class="tag">APIs</span><span class="tag">Automation</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/custom-software/">Custom software services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/custom.jpg" alt="Custom software and business dashboards" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>SEO, AEO and GEO</h3>
          <p>Technical SEO for Google, Answer Engine Optimization for featured answers, and Generative Engine Optimization so ChatGPT, Gemini and Perplexity cite your brand.</p>
          <div class="tags"><span class="tag">Technical SEO</span><span class="tag">AEO</span><span class="tag">GEO</span><span class="tag">LLM SEO</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/seo-aeo-geo/">SEO and GEO services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/seo.jpg" alt="SEO AEO and GEO search visibility" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Business workflow automation</h3>
          <p>We design and build workflows that automate how your business runs day to day: leads, follow-ups, approvals, notifications, CRM updates and repetitive ops. Practical automation that saves hours, not experimental AI labs.</p>
          <div class="tags"><span class="tag">Workflows</span><span class="tag">CRM automation</span><span class="tag">Integrations</span><span class="tag">Ops</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/ai-automation/">Automation services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/ai.jpg" alt="Business workflow and process automation" width="640" height="360" loading="lazy" /></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Desktop applications</h3>
          <p>Electron and Tauri apps for offline-first tools, hardware integrations, installers, code signing and auto-updates. When the browser is not enough.</p>
          <div class="tags"><span class="tag">Electron</span><span class="tag">Tauri</span><span class="tag">Offline</span><span class="tag">Windows</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/desktop-apps/">Desktop app services</a></p>
        </div>
        <div class="band-visual"><img src="assets/services/desktop.jpg" alt="Desktop application development" width="640" height="360" loading="lazy" /></div>
      </article>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-kicker reveal">Proof in motion</div>
      <h2 class="section-title reveal">Numbers we design every engagement around</h2>
      <div class="stats reveal">
        <div class="stat"><strong data-count="6" data-suffix="+">0</strong><span>Service verticals under one roof</span></div>
        <div class="stat"><strong data-count="90" data-suffix="+">0</strong><span>PageSpeed targets on web builds</span></div>
        <div class="stat"><strong data-count="14">0</strong><span>Day average MVP scope cycles</span></div>
        <div class="stat"><strong data-count="5">0</strong><span>AI answer engines we track for GEO</span></div>
      </div>
    </div>
  </section>

  <section class="section" id="industries">
    <div class="container">
      <div class="section-kicker reveal">Industries</div>
      <h2 class="section-title reveal">Where custom software and SEO actually pay back</h2>
      <p class="section-sub reveal">We prioritize verticals where a shipped product plus discoverability creates revenue faster than a brochure site ever will.</p>
      <div class="industry-grid">
        <article class="industry reveal"><h3>SaaS and startups</h3><p>MVP web apps, Flutter mobile shells, onboarding flows and launch SEO so early users can find you.</p></article>
        <article class="industry reveal"><h3>Services and agencies</h3><p>High-converting service sites, lead forms, WhatsApp CTAs and local plus AI-search visibility.</p></article>
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

  <section class="section">
    <div class="container">
      <div class="section-kicker reveal">Blog</div>
      <h2 class="section-title reveal">Field notes from the build floor</h2>
      <p class="section-sub reveal">Practical guides on GEO, custom software cost in India, and choosing Flutter vs React Native for MVPs.</p>
      <div class="blog-grid">
        <a class="blog-card reveal" href="blog/what-is-geo-aeo-llm-seo-2026/">
          <img src="assets/blog/geo-aeo-2026.jpg" alt="GEO AEO and LLM SEO illustrated neural network" width="640" height="360" loading="lazy" />
          <div class="body">
            <time datetime="2026-10-15">15 Oct 2026</time>
            <h3>What is GEO, AEO and LLM SEO in 2026?</h3>
            <p>Why Google rankings alone are not enough when buyers ask ChatGPT and Perplexity first.</p>
          </div>
        </a>
        <a class="blog-card reveal" href="blog/custom-software-development-cost-india-2026/">
          <img src="assets/blog/custom-software-cost.jpg" alt="Custom software development cost India" width="640" height="360" loading="lazy" />
          <div class="body">
            <time datetime="2026-10-15">15 Oct 2026</time>
            <h3>Custom software development cost in India 2026</h3>
            <p>Real ranges for MVPs, internal tools and multi-platform builds, plus what actually moves the price.</p>
          </div>
        </a>
        <a class="blog-card reveal" href="blog/flutter-vs-react-native-mvp-india-2026/">
          <img src="assets/blog/flutter-rn-mvp.jpg" alt="Flutter vs React Native for MVP" width="640" height="360" loading="lazy" />
          <div class="body">
            <time datetime="2026-10-15">15 Oct 2026</time>
            <h3>Flutter vs React Native for an India MVP</h3>
            <p>A practical choose-framework guide for startups that need Android and iOS without burning runway.</p>
          </div>
        </a>
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
      <div class="section-kicker">FAQ</div>
      <h2 class="section-title">Straight answers buyers and AI assistants both need</h2>
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
          <p>It depends on scope. Focused websites and web MVPs can start in the low lakhs INR. Mobile MVPs and multi-role internal systems cost more when payments, compliance and integrations expand. Read our <a href="blog/custom-software-development-cost-india-2026/">2026 cost guide</a> or ask for a scoped quote.</p>
        </details>
        <details>
          <summary>How is JB different from other India software and digital agencies?</summary>
          <p>Many competitors sell the same menu: apps, websites, AI and SEO. We differentiate with founder-accessible delivery, desktop capability when needed, and discovery engineered into the product so launch day is not day zero of marketing.</p>
        </details>
        <details>
          <summary>How fast can an MVP ship?</summary>
          <p>A focused web MVP often lands in 2 to 6 weeks. Mobile MVPs typically take 6 to 12 weeks depending on integrations and store requirements.</p>
        </details>
        <details>
          <summary>Do you work with startups and enterprises?</summary>
          <p>Both. Engagements can be fixed-scope projects, dedicated pods, or ongoing retainers for SEO, GEO and product iteration.</p>
        </details>
        <details>
          <summary>Is the website indexed for search and AI crawlers?</summary>
          <p>Yes. Pages include canonical URLs, sitemap.xml, robots.txt, llms.txt, structured data and crawlable HTML so Google and AI systems can discover and cite our services.</p>
        </details>
      </div>
    </div>
  </section>
</main>
{footer(0)}
"""
write(ROOT / "index.html", home)


def service_page(slug, title, h1, desc, keywords, bullets, faqs, active, why=None):
    depth = 2
    why_text = why or (
        "Buyers shortlist vendors on Google and inside AI assistants. "
        "A pretty UI without crawlable structure, schema, speed and proof pages will not get found. "
        "We build products and the discovery layer together."
    )
    body = head(title, desc, keywords, f"/services/{slug}/", depth) + f"""
<body>
{nav(depth, active)}
<main>
  <section class="page-hero">
    <div class="container">
      <div class="section-kicker">Services</div>
      <h1>{h1}</h1>
      <p>{desc}</p>
      <div class="hero-cta" style="margin-top:1.75rem">
        <a class="btn btn-primary btn-magnet" href="{rel(depth)}contact/">Get a project quote</a>
        <a class="btn btn-ghost btn-magnet" href="{rel(depth)}pricing/">View pricing</a>
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container prose">
      <h2>What you get</h2>
      <ul>
        {''.join(f'<li>{b}</li>' for b in bullets)}
      </ul>
      <h2>Why this matters in 2026</h2>
      <p>{why_text}</p>
      <h2>Engagement models</h2>
      <ul>
        <li>Fixed-scope projects with milestones</li>
        <li>Time and materials for evolving products</li>
        <li>Dedicated pod for ongoing delivery</li>
        <li>Retainer for SEO, AEO, GEO and growth experiments</li>
      </ul>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <h2 class="section-title">FAQ</h2>
      <div class="faq">
        {''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)}
      </div>
      <div class="cta-band reveal" style="margin-top:2rem">
        <div><h2>Talk through your brief</h2><p>Share goals and constraints. We come back with a clear plan.</p></div>
        <a class="btn btn-primary btn-magnet" href="{rel(depth)}contact/">Contact JB Software Solutions</a>
      </div>
    </div>
  </section>
</main>
{footer(depth)}
"""
    write(ROOT / "services" / slug / "index.html", body)


service_page(
    "web-development",
    f"Web Development Company India | Next.js & React | {BRAND}",
    "Web development that ranks and converts",
    "JB Software Solutions builds fast, SEO-ready websites and web applications with Next.js, React and Node for startups and growing businesses.",
    "web development company India, Next.js development, React website, web application development, SEO website development, SaaS frontend",
    [
        "Marketing sites and product web apps on Next.js / React",
        "Performance budgets targeting 90+ PageSpeed where scope allows",
        "Structured data, clean URLs, sitemap and crawlable HTML",
        "CMS or headless content workflows when you need editorial control",
        "Analytics, conversion events and post-launch iteration",
    ],
    [
        ("Which stack do you recommend?", "Next.js and React for most marketing and SaaS fronts. We pick Node, Laravel or .NET for backends based on your team and hosting."),
        ("Can you redesign an existing site?", "Yes. We audit speed, SEO and conversion, then rebuild or iteratively improve without killing rankings."),
    ],
    "services",
)

service_page(
    "mobile-app-development",
    f"Mobile App Development Company | Flutter & React Native | {BRAND}",
    "Mobile apps for Android and iOS",
    "Cross-platform Flutter and React Native apps, or native builds, from MVP to store launch with JB Software Solutions.",
    "mobile app development company India, Flutter app development, React Native, Android app, iOS app, MVP mobile app",
    [
        "Flutter or React Native for shared Android and iOS codebases",
        "Native modules when camera, Bluetooth or performance needs demand it",
        "Play Store and App Store submission support",
        "Push notifications, auth, payments and analytics integrations",
        "Maintenance retainers after launch",
    ],
    [
        ("Flutter or React Native?", "Flutter for UI-heavy products and strong Android reach. React Native when your web team is already deep in React. We decide after discovery."),
        ("Do you build MVPs?", "Yes. Scoped MVPs in weeks, not quarters, with a clear path to v1.1."),
    ],
    "services",
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
    ],
    "services",
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
    ],
    "seo",
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
    "ai",
    why=(
        "Most businesses lose hours every week to copy-paste between forms, CRMs, WhatsApp and sheets. "
        "We map those paths and automate them so leads get followed up, ops stay visible, and your team stops chasing status. "
        "This is business process automation, not a custom AI research project."
    ),
)

service_page(
    "desktop-apps",
    f"Desktop App Development | Electron & Tauri | {BRAND}",
    "Desktop apps when the browser is not enough",
    "Electron and Tauri desktop software with installers, code signing, offline storage and hardware integrations.",
    "desktop app development, Electron app development, Tauri, Windows desktop software, offline first app, cross platform desktop",
    [
        "Cross-platform desktop with Electron or Tauri",
        "Offline-first data with sync when connectivity returns",
        "Serial / USB / hardware integrations for industrial tools",
        "Windows and macOS installers with auto-update channels",
        "Licensing and activation flows when you sell the app",
    ],
    [
        ("When should I choose desktop over web?", "Offline, hardware access, heavy local files, or environments where browsers are locked down."),
        ("Can you wrap our existing web app?", "Often yes. We harden cold start, native menus, signing and updates so it feels like a real desktop citizen."),
    ],
    "services",
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
    <p>We help founders and operators ship digital products: websites, mobile apps, custom software, desktop tools, and the SEO / AEO / GEO layer that makes those products discoverable on Google and inside AI assistants.</p>
    <h2>How we think</h2>
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
      <button class="btn btn-primary btn-magnet" type="submit">Get my quote</button>
    </form>
    <div class="prose">
      <h2>Why this form exists</h2>
      <p>Serious buyers want a written reply, not a dead mailto popup. This form emails the JB team directly and sends you to a confirmation page.</p>
      <p>Prefer email? Write <a href="mailto:{EMAIL}">{EMAIL}</a> with your brief.</p>
      <h2>What happens next</h2>
      <ul>
        <li>We confirm fit within 24 hours on business days</li>
        <li>You get a written scope outline</li>
        <li>We agree fixed or phased pricing before build starts</li>
      </ul>
      <p><a href="{rel(1)}pricing/">See starting prices</a> if you want ballpark numbers first.</p>
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
        <h3>Business website</h3>
        <div class="from">From ₹50,000</div>
        <ul>
          <li>5-12 pages, mobile-first</li>
          <li>SEO basics, schema, sitemap</li>
          <li>Contact lead capture</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card is-featured reveal">
        <h3>Web MVP / SaaS slice</h3>
        <div class="from">From ₹3,00,000</div>
        <ul>
          <li>Core user journey only</li>
          <li>Auth, dashboard or workflows</li>
          <li>Deployed staging + docs</li>
        </ul>
        <a class="btn btn-primary btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>Mobile app MVP</h3>
        <div class="from">From ₹5,00,000</div>
        <ul>
          <li>Flutter or React Native</li>
          <li>Android first, iOS as scoped</li>
          <li>Store submission support</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>Custom internal tool</h3>
        <div class="from">From ₹4,00,000</div>
        <ul>
          <li>Roles, workflows, reporting</li>
          <li>Integrations as needed</li>
          <li>Full IP handover</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>SEO + AEO + GEO</h3>
        <div class="from">From ₹25,000/mo</div>
        <ul>
          <li>Technical and on-page SEO</li>
          <li>Content clusters</li>
          <li>AI citation checks</li>
        </ul>
        <a class="btn btn-ghost btn-magnet" href="{rel(1)}contact/">Request quote</a>
      </article>
      <article class="price-card reveal">
        <h3>Workflow automation</h3>
        <div class="from">From ₹75,000</div>
        <ul>
          <li>Lead and follow-up flows</li>
          <li>CRM / ops integrations</li>
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
    <p>We reply within 24 hours on business days with fit, next steps and a path to a written quote. Meanwhile, skim pricing or the blog.</p>
    <div class="hero-cta" style="margin-top:1.5rem">
      <a class="btn btn-primary btn-magnet" href="{rel(1)}pricing/">View pricing</a>
      <a class="btn btn-ghost btn-magnet" href="{rel(1)}blog/">Read the blog</a>
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
import json
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
