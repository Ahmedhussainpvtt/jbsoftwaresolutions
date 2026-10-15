# -*- coding: utf-8 -*-
"""Generate JB Software Solutions static site pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://ahmedhussainpvtt.github.io/jbsoftwaresolutions"
BRAND = "JB Software Solutions"
EMAIL = "info@jbsoftwaresolutions.com"
PHONE = "+91 93811 07468"
WA = "919381107468"


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
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}styles.css" />
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
        "telephone": "{PHONE}",
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
      {a("ai", "services/ai-automation/", "AI")}
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
  <a class="dock-btn wa" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">WA</a>
  <a class="dock-btn call" href="tel:{PHONE.replace(' ', '')}" aria-label="Call">Call</a>
  <a class="dock-btn quote" href="{p}contact/" aria-label="Get quote">Quote</a>
</div>
"""


def footer(depth):
    p = rel(depth)
    return f"""
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <strong>{BRAND}</strong>
      <p>Custom software, mobile apps, websites, desktop apps, SEO, AEO, GEO, and AI automation for startups and growing businesses in India and worldwide.</p>
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
      <a href="{p}services/ai-automation/">AI automation</a>
      <a href="{p}blog/">Blog</a>
    </div>
    <div>
      <strong>Company</strong>
      <a href="{p}about/">About</a>
      <a href="{p}contact/">Contact</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; 2026 {BRAND}. All rights reserved.</span>
    <span>Custom software | Mobile apps | Websites | SEO | AI</span>
  </div>
</footer>
{dock(depth)}
<script src="{p}main.js" defer></script>
</body>
</html>
"""


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


KW_HOME = (
    "custom software development company India, web development company, "
    "mobile app development, Flutter app development, React Native, "
    "SEO company India, AEO, GEO, generative engine optimization, "
    "AI automation agency, desktop app Electron, Next.js development, "
    "JB Software Solutions"
)

# ---------- HOME ----------
home_lines = [
    "> boot sequence: jb-agent v2.6",
    "> scanning market signals: SEO · AEO · GEO · apps · custom software",
    "> intent detected: **build products that rank and convert**",
    "> stacking: Next.js · Flutter · Node · AI agents · schema markup",
    "> proof mode: this page is not a brochure. it is a live system.",
    "> ready. tell us what you want shipped.",
]
home = head(
    f"{BRAND} | Custom Software, Mobile Apps, Websites, SEO and AI",
    "JB Software Solutions builds custom software, mobile apps, websites, desktop apps, and AI automation, then grows them with SEO, AEO and GEO so buyers find you on Google and inside ChatGPT.",
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
    "description": "Custom software, web, mobile, desktop, SEO/AEO/GEO and AI automation.",
    "priceRange": "$$",
    "areaServed": ["IN", "AE", "US", "GB"],
    "telephone": "{PHONE}",
    "email": "{EMAIL}"
  }}
  </script>
""",
) + f"""
<body>
{nav(0, "home")}
<main>
  <section class="hero">
    <canvas id="ai-field" aria-hidden="true"></canvas>
    <div class="container">
      <div class="hero-brand">
        <img src="assets/logo-full.png" alt="{BRAND}" width="220" height="120" />
      </div>
      <h1 class="hero-title">Software that <span class="grad">thinks in public</span></h1>
      <p class="hero-sub">We design, build and ship custom software, mobile apps, websites and desktop tools, then wire SEO, AEO and GEO so your brand shows up in Google and AI answers. If we say AI, the site has to prove it.</p>
      <div class="hero-cta">
        <a class="btn btn-primary btn-magnet" href="contact/">Start a project</a>
        <a class="btn btn-ghost btn-magnet" href="services/web-development/">Explore services</a>
      </div>
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
  </section>

  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      <span>Custom software</span><span>Flutter apps</span><span>Next.js websites</span>
      <span>Electron desktop</span><span>Technical SEO</span><span>AEO</span><span>GEO</span>
      <span>AI agents</span><span>UI/UX</span><span>Cloud and DevOps</span>
      <span>ChatGPT citations</span><span>Perplexity SEO</span><span>LLM SEO</span>
    </div>
  </div>

  <section class="section" id="services">
    <div class="container">
      <div class="section-kicker reveal">What we ship</div>
      <h2 class="section-title reveal">One team for build and discovery</h2>
      <p class="section-sub reveal">Most agencies hand you a site and disappear. We keep engineering and search under one roof so the product you launch is the product that ranks.</p>

      <article class="service-band">
        <div>
          <h3>Web development</h3>
          <p>High-performance marketing sites and web apps on Next.js, React and Node. Core Web Vitals, schema markup and conversion paths baked in from sprint one.</p>
          <div class="tags"><span class="tag">Next.js</span><span class="tag">React</span><span class="tag">Node.js</span><span class="tag">SEO-ready</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/web-development/">Web development services</a></p>
        </div>
        <div class="band-visual" style="--i:1"></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Mobile app development</h3>
          <p>iOS and Android from one Flutter or React Native codebase, or native when the product demands it. Store launch, push, analytics and post-release support.</p>
          <div class="tags"><span class="tag">Flutter</span><span class="tag">React Native</span><span class="tag">iOS</span><span class="tag">Android</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/mobile-app-development/">Mobile app services</a></p>
        </div>
        <div class="band-visual"></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Custom software</h3>
          <p>Internal tools, CRMs, dashboards, ERPs and workflow systems tailored to how your team actually works. Full IP handover. No black-box lock-in.</p>
          <div class="tags"><span class="tag">SaaS</span><span class="tag">ERP</span><span class="tag">APIs</span><span class="tag">Automation</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/custom-software/">Custom software services</a></p>
        </div>
        <div class="band-visual"></div>
      </article>

      <article class="service-band">
        <div>
          <h3>SEO, AEO and GEO</h3>
          <p>Technical SEO for Google, Answer Engine Optimization for featured answers, and Generative Engine Optimization so ChatGPT, Gemini and Perplexity cite your brand.</p>
          <div class="tags"><span class="tag">Technical SEO</span><span class="tag">AEO</span><span class="tag">GEO</span><span class="tag">LLM SEO</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/seo-aeo-geo/">SEO and GEO services</a></p>
        </div>
        <div class="band-visual"></div>
      </article>

      <article class="service-band">
        <div>
          <h3>AI automation and agents</h3>
          <p>Lead qualification bots, document AI, RAG over your data, and agent workflows that remove manual ops without turning your brand into a generic chatbot.</p>
          <div class="tags"><span class="tag">AI agents</span><span class="tag">RAG</span><span class="tag">LLM</span><span class="tag">Automation</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/ai-automation/">AI automation services</a></p>
        </div>
        <div class="band-visual"></div>
      </article>

      <article class="service-band">
        <div>
          <h3>Desktop applications</h3>
          <p>Electron and Tauri apps for offline-first tools, hardware integrations, installers, code signing and auto-updates. When the browser is not enough.</p>
          <div class="tags"><span class="tag">Electron</span><span class="tag">Tauri</span><span class="tag">Offline</span><span class="tag">Windows</span></div>
          <p style="margin-top:1rem"><a class="btn btn-ghost btn-magnet" href="services/desktop-apps/">Desktop app services</a></p>
        </div>
        <div class="band-visual"></div>
      </article>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-kicker reveal">Proof in motion</div>
      <h2 class="section-title reveal">Numbers we design for</h2>
      <div class="stats reveal">
        <div class="stat"><strong data-count="6" data-suffix="+">0</strong><span>Service verticals under one roof</span></div>
        <div class="stat"><strong data-count="90" data-suffix="+">0</strong><span>PageSpeed targets on web builds</span></div>
        <div class="stat"><strong data-count="14">0</strong><span>Day average MVP scope cycles</span></div>
        <div class="stat"><strong data-count="5">0</strong><span>AI answer engines we track for GEO</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-kicker reveal">How we work</div>
      <h2 class="section-title reveal">From brief to launched system</h2>
      <div class="process-steps">
        <article class="reveal"><h3>Discover</h3><p>Goals, users, constraints, competitors and the search queries your buyers already ask Google and ChatGPT.</p></article>
        <article class="reveal"><h3>Design</h3><p>Architecture, UX and content structure that serve both humans and crawlers. Prototypes before heavy code.</p></article>
        <article class="reveal"><h3>Build</h3><p>Agile sprints with demos every week. Web, mobile, desktop or AI agents, same accountable pod.</p></article>
        <article class="reveal"><h3>Grow</h3><p>Launch, measure, SEO/AEO/GEO iterations and feature updates so the product keeps compounding.</p></article>
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

  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Ready when you are</h2>
          <p>Tell us what you are building. We reply with scope, timeline and a fixed or phased plan. No lock-in theatre.</p>
        </div>
        <a class="btn btn-primary btn-magnet" href="contact/">Book a strategy call</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-kicker">FAQ</div>
      <h2 class="section-title">Straight answers</h2>
      <div class="faq">
        <details open>
          <summary>What does JB Software Solutions do?</summary>
          <p>We build custom software, websites, mobile apps and desktop apps, and we grow them with SEO, AEO, GEO and AI automation for clients in India and internationally.</p>
        </details>
        <details>
          <summary>Do you offer SEO and AI search optimization?</summary>
          <p>Yes. Technical SEO for Google, AEO for answer boxes, and GEO so brands get cited inside ChatGPT, Gemini, Perplexity and Google AI Overviews.</p>
        </details>
        <details>
          <summary>How fast can an MVP ship?</summary>
          <p>A focused web MVP often lands in 2 to 6 weeks. Mobile MVPs typically take 6 to 12 weeks depending on integrations and store requirements.</p>
        </details>
        <details>
          <summary>Do you work with startups and enterprises?</summary>
          <p>Both. Engagements can be fixed-scope projects, dedicated pods, or ongoing retainers for SEO and product iteration.</p>
        </details>
      </div>
    </div>
  </section>
</main>
{footer(0)}
"""
write(ROOT / "index.html", home)


def service_page(slug, title, h1, desc, keywords, bullets, faqs, active):
    depth = 2
    body = head(title, desc, keywords, f"/services/{slug}/", depth) + f"""
<body>
{nav(depth, active)}
<main>
  <section class="page-hero">
    <div class="container">
      <div class="section-kicker">Services</div>
      <h1>{h1}</h1>
      <p>{desc}</p>
      <div class="hero-cta" style="margin-top:1.5rem">
        <a class="btn btn-primary btn-magnet" href="{rel(depth)}contact/">Get a project quote</a>
        <a class="btn btn-ghost btn-magnet" href="{rel(depth)}blog/">Read the blog</a>
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
      <p>Buyers shortlist vendors on Google and inside AI assistants. A pretty UI without crawlable structure, schema, speed and proof pages will not get found. We build products and the discovery layer together.</p>
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
    f"AI Automation and AI Agents Company | {BRAND}",
    "AI automation that does real work",
    "Custom AI agents, RAG systems and workflow automation that plug into your CRM, support and ops stack.",
    "AI automation agency India, AI agents development, RAG chatbot, LLM workflow, custom AI software, business process automation",
    [
        "AI agents for lead qualification, support triage and internal ops",
        "RAG over your documents with permission-aware retrieval",
        "Human-in-the-loop controls so taste and brand stay intact",
        "Integrations with WhatsApp, email, Slack and CRMs",
        "Evaluation harnesses so quality does not silently drift",
    ],
    [
        ("Will this replace my team?", "No. We remove repetitive work so your team focuses on decisions and relationships."),
        ("Is my data safe?", "We design with least privilege, NDAs and deployment options that keep sensitive data in your cloud when required."),
    ],
    "ai",
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
    f"About {BRAND} | Software, Apps and AI Search",
    "JB Software Solutions is a software and digital growth studio building custom products and growing them with SEO, AEO, GEO and AI automation.",
    "about JB Software Solutions, software development studio India, digital agency software SEO AI",
    "/about/",
    1,
) + f"""
<body>
{nav(1, "about")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">About</div>
    <h1>Built to prove the pitch</h1>
    <p>If we sell software craft and AI-era discovery, our own site has to move, load and earn trust. That is the bar we hold for client work too.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container prose">
    <h2>Who we are</h2>
    <p>{BRAND} helps founders and operators ship digital products: websites, mobile apps, custom software, desktop tools, and the SEO / AEO / GEO layer that makes those products discoverable on Google and inside AI assistants.</p>
    <h2>How we think</h2>
    <ul>
      <li>Ship systems, not slide decks</li>
      <li>Measure outcomes: leads, retention, citations, not vanity screenshots</li>
      <li>Keep IP with the client</li>
      <li>Use AI for velocity. Keep humans on taste and accountability</li>
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
    "Contact JB Software Solutions for custom software, mobile apps, websites, SEO, GEO and AI automation. Free strategy discussion.",
    "contact JB Software Solutions, software development quote, hire Flutter developer, SEO agency contact",
    "/contact/",
    1,
) + f"""
<body>
{nav(1, "contact")}
<main>
  <section class="page-hero"><div class="container">
    <div class="section-kicker">Contact</div>
    <h1>Tell us what you want shipped</h1>
    <p>Share a short brief. We reply with fit, rough timeline and next steps. Prefer WhatsApp or a call? Use the sticky buttons.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container contact-grid">
    <form class="form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <label>Name<input name="name" required placeholder="Your name" /></label>
      <label>Email<input type="email" name="email" required placeholder="you@company.com" /></label>
      <label>Service
        <select name="service">
          <option>Web development</option>
          <option>Mobile app</option>
          <option>Custom software</option>
          <option>SEO / AEO / GEO</option>
          <option>AI automation</option>
          <option>Desktop app</option>
          <option>Not sure yet</option>
        </select>
      </label>
      <label>Project details<textarea name="message" required placeholder="Goals, timeline, links, budget range"></textarea></label>
      <button class="btn btn-primary btn-magnet" type="submit">Send message</button>
    </form>
    <div class="prose">
      <h2>Direct lines</h2>
      <p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>Phone: <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a></p>
      <p>WhatsApp: <a href="https://wa.me/{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
      <h2>What happens next</h2>
      <ul>
        <li>We confirm we are the right fit (or say who would be better)</li>
        <li>You get a written scope outline</li>
        <li>We agree fixed or phased pricing before build starts</li>
      </ul>
    </div>
  </div></section>
</main>
{footer(1)}
"""
write(ROOT / "contact" / "index.html", contact)

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
  <article class="section">
    <div class="container prose">
      <p class="post-meta"><time datetime="{post['date']}">15 October 2026</time> · {BRAND}</p>
      <h1>{post['title']}</h1>
      <p>{post['desc']}</p>
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

# robots, sitemap, llms, 404, CNAME none
urls = [
    "/",
    "/about/",
    "/contact/",
    "/blog/",
    "/services/web-development/",
    "/services/mobile-app-development/",
    "/services/custom-software/",
    "/services/seo-aeo-geo/",
    "/services/ai-automation/",
    "/services/desktop-apps/",
] + [f"/blog/{p['slug']}/" for p in posts]

(ROOT / "robots.txt").write_text(
    f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
""",
    encoding="utf-8",
)

sitemap_items = "\n".join(
    f"""  <url>
    <loc>{SITE}{u}</loc>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if u == "/" else "0.8"}</priority>
    <lastmod>2026-10-15</lastmod>
  </url>"""
    for u in urls
)
(ROOT / "sitemap.xml").write_text(
    f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_items}
</urlset>
""",
    encoding="utf-8",
)

(ROOT / "llms.txt").write_text(
    f"""# {BRAND}

> Custom software, mobile apps, websites, desktop apps, SEO, AEO, GEO and AI automation.

- Home: {SITE}/
- Web development: {SITE}/services/web-development/
- Mobile apps: {SITE}/services/mobile-app-development/
- Custom software: {SITE}/services/custom-software/
- SEO AEO GEO: {SITE}/services/seo-aeo-geo/
- AI automation: {SITE}/services/ai-automation/
- Desktop apps: {SITE}/services/desktop-apps/
- Blog: {SITE}/blog/
- Contact: {SITE}/contact/
- Email: {EMAIL}
""",
    encoding="utf-8",
)

not_found = head(
    f"Page not found | {BRAND}",
    "The page you requested is not available.",
    BRAND,
    "/404.html",
    0,
) + f"""
<body>
{nav(0)}
<main class="page-hero"><div class="container">
  <h1>404</h1>
  <p>That route is not in the sitemap. Head home or browse services.</p>
  <p><a class="btn btn-primary" href="{SITE}/">Go home</a></p>
</div></main>
{footer(0)}
"""
write(ROOT / "404.html", not_found)

# GitHub Pages: project site needs this for 404 sometimes - also add .nojekyll
(ROOT / ".nojekyll").write_text("", encoding="utf-8")
print("done")
