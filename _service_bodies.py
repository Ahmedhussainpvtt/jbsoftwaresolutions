# -*- coding: utf-8 -*-
"""Short closing blocks for JB service pages (not SEO essay dumps)."""

BRAND = "JB Software Solutions"


def bodies():
    """Return compact HTML for the closing details band after feature rows."""
    return {
        "web-development": _closing(
            intro=f"{BRAND} builds business websites that explain the offer, load fast on phones, and turn visitors into enquiries.",
            cost="Business websites often start from <strong>₹50,000</strong>. Page count, custom design, bilingual content and integrations change the quote. Many 5 to 12 page sites launch in <strong>2 to 6 weeks</strong> when content is ready.",
            who="Service businesses, founders replacing outdated sites, and teams that want India delivery with written scope and basic SEO built in.",
            next_step='Share your current site, must-have pages and budget on the <a href="../../contact/">contact form</a>. Related: <a href="../../faq/website-development-cost-india/">cost FAQ</a> and <a href="../../pricing/">pricing</a>.',
        ),
        "mobile-app-development": _closing(
            intro=f"{BRAND} builds focused Android and iPhone apps with weekly demos and store launch support, not twelve-month science projects.",
            cost="Focused first apps often start from <strong>₹5,00,000</strong>. A clear first version often takes about <strong>8 to 12 weeks</strong>. Payments, maps, chat and multi-role features raise the quote.",
            who="Startups that need one journey live on the stores, and teams that need field or staff apps with honest scope.",
            next_step='Send the main user journey and store goals via <a href="../../contact/">contact</a>. Related: <a href="../../faq/mobile-app-development-cost-india/">mobile cost FAQ</a>.',
        ),
        "custom-software": _closing(
            intro=f"{BRAND} builds internal tools, CRM-style workflows, portals and dashboards around how your team already works. You own the work.",
            cost="Focused internal tools often start from <strong>₹4,00,000</strong>. Multi-department platforms are phased. Price follows roles, workflows, integrations and reporting.",
            who="Ops, sales and support teams outgrowing sheets and WhatsApp, plus founders who need a SaaS first slice with clear IP handover.",
            next_step='Describe the painful workflow on the <a href="../../contact/">contact form</a>. Related: <a href="../../faq/custom-software-cost-india/">custom software cost FAQ</a>.',
        ),
        "seo-aeo-geo": _closing(
            intro=f"{BRAND} runs SEO, AEO and GEO together so you rank on Google and stay easier to cite in ChatGPT, Gemini and Perplexity.",
            cost="Visibility retainers often start from <strong>₹25,000 per month</strong>. Scope depends on site size and competition. Pair with a website rebuild when the site itself is the bottleneck.",
            who="Service businesses that need inbound, product teams that need crawlable docs, and brands tired of ads-only growth.",
            next_step='Send your domain and target services via <a href="../../contact/">contact</a>. Related: <a href="../../faq/seo-aeo-geo-explained/">SEO / AEO / GEO FAQ</a>.',
        ),
        "ai-automation": _closing(
            intro=f"{BRAND} automates the boring path between forms, CRM, email and chat. Fewer lost leads. Less status chasing. Not a custom RAG lab.",
            cost="Automation projects often start from <strong>₹75,000</strong>. Simple flows ship fast. Multi-system setups are phased.",
            who="Sales and ops teams drowning in copy-paste, and founders who want visibility without hiring more coordinators.",
            next_step='Describe the repetitive path that wastes the most hours on <a href="../../contact/">contact</a>. Related: <a href="../../faq/workflow-automation-india/">automation FAQ</a>.',
        ),
        "desktop-apps": _closing(
            intro=f"{BRAND} builds installable desktop software when offline work, devices or locked-down offices make a website the wrong tool.",
            cost="Desktop work is scoped after discovery. Windows-first is common. Mac is available when listed in the quote.",
            who="Factories, field teams and offices that need installers, offline data or hardware connections.",
            next_step='Tell us the offline or device constraint on <a href="../../contact/">contact</a>. Related: <a href="../../faq/desktop-app-development-india/">desktop FAQ</a>.',
        ),
    }


def _closing(intro, cost, who, next_step):
    return f"""
<p class="service-closing-lead">{intro}</p>
<div class="service-closing-grid">
  <article class="service-closing-card">
    <h3>Cost and timeline</h3>
    <p>{cost}</p>
  </article>
  <article class="service-closing-card">
    <h3>Who this is for</h3>
    <p>{who}</p>
  </article>
  <article class="service-closing-card">
    <h3>Next step</h3>
    <p>{next_step}</p>
  </article>
</div>
"""
