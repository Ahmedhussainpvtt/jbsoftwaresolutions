export const BRAND = 'JB Software Solutions'
export const EMAIL = 'info@jbsoftwaresolutions.com'
export const SITE = 'https://jbsoftwaresolutions.com'

export const SERVICES = [
  { slug: 'web-development', title: 'Website development', desc: 'Business sites that get enquiries', img: 'web-hero.jpg' },
  { slug: 'mobile-app-development', title: 'Mobile app development', desc: 'Apps for phones and tablets', img: 'mobile-hero.jpg' },
  { slug: 'custom-software', title: 'Custom software', desc: 'Tools built for your team', img: 'custom-hero.jpg' },
  { slug: 'seo-aeo-geo', title: 'SEO and online visibility', desc: 'Get found on Google and AI search', img: 'seo-hero.jpg' },
  { slug: 'ai-automation', title: 'Workflow automation', desc: 'Cut repetitive daily work', img: 'ai-hero.jpg' },
  { slug: 'desktop-apps', title: 'Desktop apps', desc: 'Software that runs on a computer', img: 'desktop-hero.jpg' },
]

export const RESOURCES = [
  { to: '/blog', title: 'Blog', desc: 'Guides on software, apps and getting found online' },
  { to: '/glossary', title: 'Glossary', desc: 'Plain definitions of software and SEO terms' },
  { to: '/faq', title: 'FAQs', desc: 'Straight answers about software, apps, SEO and pricing' },
]

export const MARQUEE = [
  'Custom software development company India',
  'Website development company',
  'Mobile app development company',
  'Web application development',
  'SEO company India',
  'AEO and GEO',
  'Hire developers India',
  'Business workflow automation',
  'Desktop app development',
  'Software outsourcing India',
  'SaaS product development',
  'CRM and ERP software',
]

export const TRUST = [
  { title: 'Reply within 24 hours', text: 'Human response on every serious brief, usually faster on business days.' },
  { title: 'You own the IP', text: 'Source code and assets stay with you. No hostage licensing.' },
  { title: 'Fixed or phased quotes', text: 'Written scope before build. No surprise invoices mid-sprint.' },
  { title: 'Build + SEO together', text: 'Launch day is not day zero of discoverability.' },
]

export const WORK = [
  {
    cat: 'web',
    meta: '01',
    label: 'Website development',
    tag: 'Service business',
    title: 'A service brand that was invisible online starts getting enquiries',
    challenge: 'Nice-looking site, unclear offers, hard-to-find contact form, almost no search visibility.',
    approach: 'Rebuild the website with clear offers, faster pages, and content that answers what buyers actually search for.',
    results: [
      { k: '3.1x', v: 'qualified form leads in 90 days' },
      { k: '42', v: 'pages live for search' },
      { k: '18 days', v: 'to first launch' },
    ],
  },
  {
    cat: 'mobile',
    meta: '02',
    label: 'Mobile app development',
    tag: 'Startup product',
    title: 'A first mobile app in about 10 weeks, not six months of waiting',
    challenge: 'Founder needed one clear user journey live on phone stores before the next investor update.',
    approach: 'Keep the first version small, show progress every week, and launch to the app stores with support included.',
    results: [
      { k: '10 wks', v: 'typical first-app timeline' },
      { k: '1', v: 'main user journey, done well' },
      { k: 'Clear plan', v: 'for what comes after launch' },
    ],
  },
  {
    cat: 'ops',
    meta: '03',
    label: 'Custom software',
    tag: 'Internal tools',
    title: 'From WhatsApp and spreadsheets to a system staff actually use',
    challenge: 'Day-to-day work lived in sheets and chat. Follow-ups got lost.',
    approach: 'Build a simple internal tool with reminders, handoffs and the workflows the team already follows.',
    results: [
      { k: '12h+', v: 'saved per week for ops' },
      { k: 'Less chase', v: 'for status in WhatsApp' },
      { k: 'You own it', v: 'files and docs handed over' },
    ],
  },
]

export const PRICES = [
  { title: 'Website development', from: 'From ₹50,000', text: 'Business websites built to get enquiries and show up on Google.' },
  { title: 'Web apps and mobile apps', from: 'From ₹3,00,000', text: 'Web app development, mobile app development and internal business tools with clear milestones.', featured: true },
  { title: 'SEO and visibility', from: 'From ₹25,000/mo', text: 'Monthly work so people can find you on Google and AI search tools.' },
]

export const HOME_FAQS = [
  { q: 'What does JB Software Solutions do?', a: 'We build custom software, websites, mobile apps and desktop apps, and grow them with SEO, AEO, GEO and workflow automation.' },
  { q: 'How much does a project cost?', a: 'Business websites often start from ₹50,000. Custom software and web apps from a few lakhs. Mobile apps often from ₹5,00,000. Ask for a scoped quote.' },
  { q: 'Do you offer SEO and visibility?', a: 'Yes. Technical SEO for Google plus AEO and GEO so your brand shows up in answer-style results.' },
  { q: 'Who owns the code?', a: 'You do. Source and assets are handed over after payment for that scope.' },
]

export const TERM_LINES = [
  '> JB Software Solutions',
  '> Custom software · websites · mobile apps · SEO',
  '> Build products people find and use',
  '> Next.js · Flutter · Node · workflow automation',
  '> Clear scope. Written quotes. You own the work.',
  '> Ready when you are.',
]

export function asset(path) {
  const base = import.meta.env.BASE_URL || '/'
  return `${base}assets/${path}`.replace(/\/{2,}/g, '/').replace(':/', '://')
}

const SERVICE_IMG_WIDTHS = [480, 768, 1152]

export function serviceImg(file) {
  const name = file.replace(/\.(jpe?g|png)$/i, '')
  return {
    src: asset(`services/${name}-768.webp`),
    srcSet: SERVICE_IMG_WIDTHS.map((w) => `${asset(`services/${name}-${w}.webp`)} ${w}w`).join(', '),
  }
}
