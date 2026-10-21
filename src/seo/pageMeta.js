import { BRAND, SITE, SERVICES } from '../data/site.js'
import faqData from '../data/faqTopics.js'
import glossaryTerms from '../data/glossaryTerms.js'
import { getService, SERVICE_SLUGS } from '../data/services.js'

const OG = `${SITE}/assets/og-image.jpg`

function abs(path) {
  const p = path.startsWith('/') ? path : `/${path}`
  return `${SITE}${p.endsWith('/') || p === '/' ? p : `${p}/`}`.replace(/([^:]\/)\/+/g, '$1')
}

export function orgGraph(pageUrl, title, desc) {
  return {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Organization',
        '@id': `${SITE}/#organization`,
        name: BRAND,
        url: `${SITE}/`,
        logo: `${SITE}/assets/logo-mark.png`,
        email: 'info@jbsoftwaresolutions.com',
        areaServed: 'IN',
        sameAs: ['https://github.com/Ahmedhussainpvtt/jbsoftwaresolutions'],
      },
      {
        '@type': 'WebSite',
        '@id': `${SITE}/#website`,
        url: `${SITE}/`,
        name: BRAND,
        publisher: { '@id': `${SITE}/#organization` },
        inLanguage: 'en-IN',
      },
      {
        '@type': 'WebPage',
        '@id': `${pageUrl}#webpage`,
        url: pageUrl,
        name: title,
        description: desc,
        isPartOf: { '@id': `${SITE}/#website` },
        publisher: { '@id': `${SITE}/#organization` },
        inLanguage: 'en-IN',
      },
    ],
  }
}

export function faqJsonLd(questions) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: questions.map(([q, a]) => ({
      '@type': 'Question',
      name: q,
      acceptedAnswer: { '@type': 'Answer', text: a },
    })),
  }
}

export function termJsonLd(term, url) {
  return {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'DefinedTerm',
        '@id': `${url}#term`,
        name: term.title,
        description: term.short,
        inDefinedTermSet: `${SITE}/glossary/`,
        url,
      },
      {
        '@type': 'WebPage',
        '@id': `${url}#webpage`,
        url,
        name: `${term.title} | Glossary | ${BRAND}`,
        description: term.short,
        isPartOf: { '@id': `${SITE}/#website` },
        about: { '@id': `${url}#term` },
      },
    ],
  }
}

/** Normalize pathname → meta payload */
export function metaForPath(pathname) {
  const path = (pathname || '/').replace(/\/+$/, '') || '/'

  if (path === '/') {
    const title = `${BRAND} | Custom Software Development, Mobile Apps, Websites, SEO, AEO, GEO`
    const desc = `${BRAND} builds custom software, mobile apps, websites, SEO, AEO and GEO for startups and growing businesses in India and worldwide.`
    const keywords =
      'custom software development company India, website development company India, mobile app development company India, SEO company India, AEO, GEO, hire developers India, workflow automation'
    const preview = faqData.preview || []
    return {
      path: '/',
      title,
      desc,
      keywords,
      canonical: abs('/'),
      jsonld: [orgGraph(abs('/'), title, desc), faqJsonLd(preview.slice(0, 8))],
      crawlHtml: crawlHome(),
    }
  }

  const staticPages = {
    '/about': {
      title: `About | ${BRAND}`,
      desc: `About ${BRAND}: a small India software agency for websites, apps, custom software, SEO, AEO and GEO.`,
      keywords: 'about JB Software Solutions, software company India, custom software agency India',
      crawl: `<h1>About ${BRAND}</h1><p>A small agency that fights for your outcome. We build websites, mobile apps, custom software, desktop tools, and SEO / AEO / GEO.</p>`,
    },
    '/pricing': {
      title: `Pricing | ${BRAND}`,
      desc: `Transparent starting prices for website development, web apps, mobile apps, custom software, SEO and automation from ${BRAND}.`,
      keywords: 'software development cost India, website development cost India, mobile app cost India, SEO retainer India',
      crawl: `<h1>Pricing</h1><p>Transparent starting points for websites, apps, custom software, SEO and automation.</p>`,
    },
    '/contact': {
      title: `Contact | ${BRAND}`,
      desc: `Contact ${BRAND} for a scoped quote on software, apps, websites, SEO or automation.`,
      keywords: 'contact JB Software Solutions, hire software company India, request quote',
      crawl: `<h1>Contact</h1><p>Send your goals and constraints. Email info@jbsoftwaresolutions.com.</p>`,
    },
    '/blog': {
      title: `Blog | ${BRAND}`,
      desc: `Guides on software, apps, SEO, AEO, GEO and hiring a development company in India.`,
      keywords: 'software blog India, GEO AEO SEO guides, custom software cost India',
      crawl: `<h1>Blog</h1><p>Guides on software, apps and getting found online.</p>`,
    },
    '/privacy': {
      title: `Privacy policy | ${BRAND}`,
      desc: `Privacy policy for ${BRAND}.`,
      keywords: 'privacy policy',
      crawl: `<h1>Privacy policy</h1>`,
    },
    '/terms': {
      title: `Terms | ${BRAND}`,
      desc: `Terms of use for ${BRAND}.`,
      keywords: 'terms of use',
      crawl: `<h1>Terms</h1>`,
    },
    '/faq': {
      title: `FAQ | ${faqData.count}+ Software, Apps, SEO and Pricing Answers | ${BRAND}`,
      desc: `Frequently asked questions about website development, mobile apps, custom software, SEO, GEO and hiring ${BRAND} in India. ${faqData.count}+ indexed answers across ${faqData.topicCount} topic pages.`,
      keywords:
        'software development FAQ India, website cost FAQ, mobile app cost FAQ, SEO FAQ, hire software company India, custom software development company India FAQ',
      crawl: crawlFaqHub(),
    },
    '/glossary': {
      title: `Glossary | Software, Apps, SEO and Automation Terms | ${BRAND}`,
      desc: `Plain-language glossary of website development, mobile apps, custom software, SEO, AEO, GEO and automation terms from ${BRAND}.`,
      keywords:
        'software glossary, SEO glossary, GEO meaning, AEO meaning, custom software definition, mobile app development meaning',
      crawl: crawlGlossaryHub(),
    },
  }

  if (staticPages[path]) {
    const s = staticPages[path]
    const extra =
      path === '/faq'
        ? [faqJsonLd((faqData.preview || []).slice(0, 20))]
        : []
    return {
      path,
      title: s.title,
      desc: s.desc,
      keywords: s.keywords,
      canonical: abs(path),
      jsonld: [orgGraph(abs(path), s.title, s.desc), ...extra],
      crawlHtml: s.crawl,
    }
  }

  const faqMatch = path.match(/^\/faq\/([^/]+)$/)
  if (faqMatch) {
    const topic = faqData.topics.find((t) => t.slug === faqMatch[1])
    if (topic) {
      const title = `${topic.title} | FAQ | ${BRAND}`
      return {
        path,
        title,
        desc: topic.desc,
        keywords: `${topic.title}, ${BRAND} FAQ, software FAQ India`,
        canonical: abs(path),
        jsonld: [orgGraph(abs(path), title, topic.desc), faqJsonLd(topic.qs)],
        crawlHtml: crawlFaqTopic(topic),
      }
    }
  }

  const glossMatch = path.match(/^\/glossary\/([^/]+)$/)
  if (glossMatch) {
    const term = glossaryTerms.find((t) => t.slug === glossMatch[1])
    if (term) {
      const title = `${term.title} | Glossary | ${BRAND}`
      return {
        path,
        title,
        desc: term.short,
        keywords: `${term.title}, ${term.title} meaning, ${term.title} definition, ${BRAND}`,
        canonical: abs(path),
        jsonld: [termJsonLd(term, abs(path))],
        crawlHtml: crawlTerm(term),
      }
    }
  }

  const svcMatch = path.match(/^\/services\/([^/]+)$/)
  if (svcMatch) {
    const s = getService(svcMatch[1])
    if (s) {
      const title = `${s.h1} | ${BRAND}`
      const keywords = `${s.navTitle}, ${s.navTitle} India, ${BRAND}, ${s.bullets.slice(0, 3).join(', ')}`
      return {
        path,
        title,
        desc: s.desc,
        keywords,
        canonical: abs(path),
        jsonld: [orgGraph(abs(path), title, s.desc), faqJsonLd(s.faqs || [])],
        crawlHtml: crawlService(s),
      }
    }
  }

  const title = `${BRAND} | Custom Software, Mobile Apps, Websites, SEO`
  const desc = `${BRAND} - custom software, mobile apps, websites, SEO, AEO and GEO.`
  return {
    path,
    title,
    desc,
    keywords: 'JB Software Solutions, custom software India',
    canonical: abs(path === '/' ? '/' : path),
    jsonld: [orgGraph(abs(path), title, desc)],
    crawlHtml: `<h1>${BRAND}</h1>`,
  }
}

export function allSeoRoutes() {
  const routes = [
    '/',
    '/about',
    '/pricing',
    '/contact',
    '/blog',
    '/privacy',
    '/terms',
    '/faq',
    '/glossary',
    ...SERVICES.map((s) => `/services/${s.slug}`),
    ...SERVICE_SLUGS.map((s) => `/services/${s}`),
    ...faqData.topics.map((t) => `/faq/${t.slug}`),
    ...glossaryTerms.map((t) => `/glossary/${t.slug}`),
  ]
  return [...new Set(routes)]
}

function esc(s) {
  return String(s || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

function crawlHome() {
  return `<h1>${esc(BRAND)}</h1>
<p>Custom software, mobile apps, websites, desktop apps, SEO, AEO, GEO, and workflow automation for startups and growing businesses in India and worldwide.</p>
<ul>${SERVICES.map((s) => `<li><a href="/services/${s.slug}/">${esc(s.title)}</a> - ${esc(s.desc)}</li>`).join('')}</ul>
<section><h2>FAQs</h2>${(faqData.preview || [])
    .slice(0, 12)
    .map(([q, a]) => `<details><summary>${esc(q)}</summary><p>${esc(a)}</p></details>`)
    .join('')}</section>`
}

function crawlFaqHub() {
  return `<h1>FAQs</h1><p>${faqData.count}+ direct answers across ${faqData.topicCount} topic pages.</p>
<nav>${faqData.topics.map((t) => `<a href="/faq/${t.slug}/"><strong>${esc(t.title)}</strong> - ${esc(t.desc)}</a>`).join('<br/>')}</nav>
<section>${(faqData.preview || [])
    .map(([q, a]) => `<details><summary>${esc(q)}</summary><p>${esc(a)}</p></details>`)
    .join('')}</section>`
}

function crawlFaqTopic(topic) {
  return `<h1>${esc(topic.title)}</h1><p>${esc(topic.desc)}</p>
${topic.qs.map(([q, a]) => `<details><summary>${esc(q)}</summary><p>${esc(a)}</p></details>`).join('')}`
}

function crawlGlossaryHub() {
  return `<h1>Glossary</h1><p>Short, clear definitions of the words people use when they hire a software company in India.</p>
${glossaryTerms.map((t) => `<a href="/glossary/${t.slug}/"><strong>${esc(t.title)}</strong> - ${esc(t.short)}</a>`).join('<br/>')}`
}

function crawlTerm(term) {
  return `<h1>${esc(term.title)}</h1><p>${esc(term.short)}</p><h2>Definition</h2><p>${esc(term.long)}</p>`
}

function crawlService(s) {
  return `<h1>${esc(s.h1)}</h1><p>${esc(s.desc)}</p>
<ul>${(s.bullets || []).map((b) => `<li>${esc(b)}</li>`).join('')}</ul>
${(s.features || []).map((f) => `<h2>${esc(f.title)}</h2><p>${esc(f.text)}</p>`).join('')}
<section><h2>${esc(s.section?.faq_h2 || 'FAQ')}</h2>${(s.faqs || [])
    .map(([q, a]) => `<details><summary>${esc(q)}</summary><p>${esc(a)}</p></details>`)
    .join('')}</section>`
}
