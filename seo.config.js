/**
 * JB Software Solutions - SEO source of truth.
 * Run: npm run seo
 * Wired into: push-jb-website.ps1 (same pattern as Easy Peeze / Kharch Log)
 */
module.exports = {
  site: {
    name: 'JB Software Solutions',
    origin: 'https://jbsoftwaresolutions.com',
    locale: 'en_IN',
    language: 'en-IN',
    themeColor: '#05070f',
    defaultTitle: 'JB Software Solutions | Custom Software, Mobile Apps, Websites, SEO and AI',
    titleTemplate: '%s | JB Software Solutions',
    defaultDescription:
      'JB Software Solutions builds custom software, mobile apps, websites, desktop apps, SEO, AEO, GEO and AI automation for businesses in India and worldwide.',
    defaultOgImage: 'https://jbsoftwaresolutions.com/assets/og-image.jpg',
    favicon: 'https://jbsoftwaresolutions.com/assets/favicon.jpg',
    twitterCard: 'summary_large_image',
    author: 'JB Software Solutions',
    gtagId: 'G-RMGPE314SF',
  },

  organization: {
    '@type': 'Organization',
    '@id': 'https://jbsoftwaresolutions.com/#organization',
    name: 'JB Software Solutions',
    url: 'https://jbsoftwaresolutions.com/',
    logo: 'https://jbsoftwaresolutions.com/assets/logo-mark.png',
    email: 'info@jbsoftwaresolutions.com',
    sameAs: ['https://github.com/Ahmedhussainpvtt/jbsoftwaresolutions'],
  },

  robots: {
    extra: [
      'User-agent: *',
      'Allow: /',
      '',
      'User-agent: GPTBot',
      'Allow: /',
      '',
      'User-agent: ChatGPT-User',
      'Allow: /',
      '',
      'User-agent: Google-Extended',
      'Allow: /',
      '',
      'User-agent: PerplexityBot',
      'Allow: /',
      '',
      'User-agent: ClaudeBot',
      'Allow: /',
      '',
      'User-agent: anthropic-ai',
      'Allow: /',
      '',
      'Sitemap: https://jbsoftwaresolutions.com/sitemap.xml',
      '',
    ].join('\n'),
  },

  excludeFromSitemap: ['/404.html', '/thank-you/'],

  skipPaths: [],

  defaults: {
    changefreq: 'monthly',
    priority: 0.6,
    robots: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1',
  },

  pages: {
    '/': {
      title: 'JB Software Solutions | Custom Software Development, Mobile Apps, Websites, SEO, AEO, GEO and AI',
      description:
        'JB Software Solutions is a custom software development company in India for web apps, Flutter mobile apps, desktop software, SEO, AEO, GEO and AI automation. Get found on Google and cited in ChatGPT.',
      changefreq: 'weekly',
      priority: 1.0,
      schemaType: 'WebSite',
    },
    '/about/': {
      title: 'About JB Software Solutions',
      description:
        'JB Software Solutions is a software and digital growth studio building custom products and growing them with SEO, AEO, GEO and AI automation.',
      priority: 0.7,
    },
    '/contact/': {
      title: 'Contact JB Software Solutions | Get a Software or SEO Quote',
      description:
        'Contact JB Software Solutions for custom software, mobile apps, websites, SEO, GEO and AI automation. Send a brief through the contact form.',
      priority: 0.8,
      changefreq: 'yearly',
    },
    '/blog/': {
      title: 'Blog | Software, SEO, GEO and App Insights | JB Software Solutions',
      description:
        'Guides from JB Software Solutions on GEO, AEO, custom software cost in India, Flutter vs React Native, and AI-era product building.',
      priority: 0.8,
      changefreq: 'weekly',
    },
    '/pricing/': {
      title: 'Pricing | Software, Apps and SEO Starting Costs | JB Software Solutions',
      description:
        'Transparent starting prices for websites, mobile apps, custom software, SEO, AEO, GEO and AI automation from JB Software Solutions in India.',
      priority: 0.9,
      changefreq: 'weekly',
    },
    '/thank-you/': {
      title: 'Thank you | JB Software Solutions',
      description: 'Thanks for contacting JB Software Solutions. We will reply within 24 hours on business days.',
      priority: 0.1,
      changefreq: 'yearly',
      sitemap: false,
      noindex: true,
    },
    '/services/web-development/': {
      title: 'Web Development Company India | Next.js and React | JB Software Solutions',
      description:
        'JB Software Solutions builds fast, SEO-ready websites and web applications with Next.js, React and Node for startups and growing businesses.',
      priority: 0.9,
      changefreq: 'weekly',
    },
    '/services/mobile-app-development/': {
      title: 'Mobile App Development Company | Flutter and React Native | JB Software Solutions',
      description:
        'Cross-platform Flutter and React Native apps, or native builds, from MVP to store launch with JB Software Solutions.',
      priority: 0.9,
      changefreq: 'weekly',
    },
    '/services/custom-software/': {
      title: 'Custom Software Development Company India | JB Software Solutions',
      description:
        'Bespoke CRMs, ERPs, dashboards and workflow systems with full IP ownership from JB Software Solutions.',
      priority: 0.9,
      changefreq: 'weekly',
    },
    '/services/seo-aeo-geo/': {
      title: 'SEO, AEO and GEO Services India | ChatGPT and Google | JB Software Solutions',
      description:
        'Technical SEO plus Answer Engine and Generative Engine Optimization so JB Software Solutions clients rank on Google and get cited in ChatGPT, Gemini and Perplexity.',
      priority: 0.9,
      changefreq: 'weekly',
    },
    '/services/ai-automation/': {
      title: 'Business Workflow and AI Automation | JB Software Solutions',
      description:
        'JB Software Solutions builds business workflows and automations that connect your tools, cut repetitive work, and keep leads, follow-ups and ops moving.',
      priority: 0.85,
      changefreq: 'weekly',
    },
    '/services/desktop-apps/': {
      title: 'Desktop App Development | Electron and Tauri | JB Software Solutions',
      description:
        'Electron and Tauri desktop software with installers, code signing, offline storage and hardware integrations.',
      priority: 0.85,
      changefreq: 'weekly',
    },
    '/blog/what-is-geo-aeo-llm-seo-2026/': {
      title: 'What is GEO, AEO and LLM SEO in 2026? | JB Software Solutions',
      description:
        'A practical guide to Generative Engine Optimization, Answer Engine Optimization and LLM SEO so your brand gets cited in ChatGPT, Gemini and Perplexity.',
      priority: 0.75,
      changefreq: 'monthly',
      ogType: 'article',
    },
    '/blog/custom-software-development-cost-india-2026/': {
      title: 'Custom Software Development Cost in India 2026 | JB Software Solutions',
      description:
        'India 2026 cost ranges for MVPs, internal tools and multi-platform custom software, plus the scope decisions that change the quote.',
      priority: 0.75,
      changefreq: 'monthly',
      ogType: 'article',
    },
    '/blog/flutter-vs-react-native-mvp-india-2026/': {
      title: 'Flutter vs React Native for an India MVP in 2026 | JB Software Solutions',
      description:
        'Choose Flutter or React Native for your India startup MVP with a clear decision framework for speed, talent, UI and long-term maintenance.',
      priority: 0.75,
      changefreq: 'monthly',
      ogType: 'article',
    },
  },
};
