import { useState } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { BRAND, EMAIL, SERVICES, BOOKING_URL, SOCIALS, LOCATION, TAGLINE, asset } from '../data/site'
import Reveal from './Reveal'
import { stagger, fadeUp } from '../motion'

const GROUPS = [
  {
    title: 'Services',
    links: SERVICES.map((s) => ({ label: s.title, to: `/services/${s.slug}` })),
  },
  {
    title: 'Resources',
    links: [
      { label: 'Blog', to: '/blog' },
      { label: 'Glossary', to: '/glossary' },
      { label: 'FAQs', to: '/faq' },
    ],
  },
  {
    title: 'Company',
    links: [
      { label: 'About', to: '/about' },
      { label: 'Pricing', to: '/pricing' },
      { label: 'Contact us', to: '/contact' },
      { label: 'Book a call', href: BOOKING_URL },
    ],
  },
]

const LEGAL = [
  { label: 'Privacy policy', to: '/privacy' },
  { label: 'Terms', to: '/terms' },
]

function SocialIcon({ id }) {
  if (id === 'linkedin') {
    return (
      <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
        <path
          fill="currentColor"
          d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.75h4v11H3v-11Zm6.5 0h3.83v1.5h.05c.53-1 1.84-2.05 3.79-2.05 4.05 0 4.8 2.66 4.8 6.13v5.42h-4v-4.8c0-1.15-.02-2.62-1.6-2.62-1.6 0-1.84 1.25-1.84 2.54v4.88h-4v-11Z"
        />
      </svg>
    )
  }
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
      <rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" strokeWidth="2" />
      <circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" strokeWidth="2" />
      <circle cx="17.3" cy="6.7" r="1.3" fill="currentColor" />
    </svg>
  )
}

function FooterGroup({ group }) {
  const [open, setOpen] = useState(false)
  return (
    <motion.div className={`footer-group${open ? ' is-open' : ''}`} variants={fadeUp}>
      <button
        type="button"
        className="footer-group__toggle"
        aria-expanded={open}
        onClick={() => setOpen((v) => !v)}
      >
        {group.title}
        <span className="footer-group__chev" aria-hidden="true" />
      </button>
      <ul className="footer-group__links">
        {group.links.map((l) => (
          <li key={l.label}>
            {l.href ? (
              <a href={l.href} target="_blank" rel="noopener noreferrer">
                {l.label}
              </a>
            ) : (
              <Link to={l.to}>{l.label}</Link>
            )}
          </li>
        ))}
      </ul>
    </motion.div>
  )
}

export default function Footer() {
  return (
    <footer className="footer">
      <Reveal className="container footer-grid" variants={stagger(0.06)} as="div">
        <motion.div className="footer-brand" variants={fadeUp}>
          <Link className="footer-logo" to="/" aria-label={`${BRAND} home`}>
            <img src={asset('logo-mark-96.webp')} width="44" height="44" alt="" />
            <span>
              JB Software<em>Solutions</em>
            </span>
          </Link>
          <p className="footer-tagline">{TAGLINE}</p>
          <p className="footer-about">
            Custom software, mobile apps, websites, desktop apps, SEO, AEO, GEO, and workflow
            automation for startups and growing businesses in India and worldwide.
          </p>
        </motion.div>
        <div className="footer-groups">
          {GROUPS.map((g) => (
            <FooterGroup key={g.title} group={g} />
          ))}
          <motion.div className="footer-reach" variants={fadeUp}>
            <p className="footer-reach__title">Get in touch</p>
            <ul className="footer-contact">
              <li>
                <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true">
                  <path
                    fill="currentColor"
                    d="M12 2.5a7 7 0 0 0-7 7c0 5.1 6.13 11.47 6.39 11.74a.85.85 0 0 0 1.22 0C12.87 20.97 19 14.6 19 9.5a7 7 0 0 0-7-7Zm0 9.75a2.75 2.75 0 1 1 0-5.5 2.75 2.75 0 0 1 0 5.5Z"
                  />
                </svg>
                <span>{LOCATION}</span>
              </li>
              <li>
                <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true">
                  <path
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinejoin="round"
                    d="M3.5 6.5h17v11h-17zM3.5 7l8.5 6.5L20.5 7"
                  />
                </svg>
                <a href={`mailto:${EMAIL}`}>{EMAIL}</a>
              </li>
            </ul>
            <div className="footer-social">
              {SOCIALS.map((s) => (
                <a
                  key={s.id}
                  href={s.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={`${BRAND} on ${s.label}`}
                >
                  <SocialIcon id={s.id} />
                </a>
              ))}
            </div>
          </motion.div>
        </div>
      </Reveal>
      <div className="container footer-bottom">
        <span>&copy; 2026 {BRAND}. All rights reserved.</span>
        <nav className="footer-legal" aria-label="Legal">
          {LEGAL.map((l) => (
            <Link key={l.to} to={l.to}>
              {l.label}
            </Link>
          ))}
          <span>Made in {LOCATION.split(',')[0]}</span>
        </nav>
      </div>
    </footer>
  )
}
