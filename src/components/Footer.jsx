import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { BRAND, EMAIL, SERVICES } from '../data/site'
import Reveal from './Reveal'
import { stagger, fadeUp } from '../motion'

export default function Footer() {
  return (
    <footer className="footer">
      <Reveal className="container footer-grid" variants={stagger(0.06)} as="div">
        <motion.div variants={fadeUp}>
          <strong>{BRAND}</strong>
          <p>
            Custom software, mobile apps, websites, desktop apps, SEO, AEO, GEO, and workflow
            automation for startups and growing businesses in India and worldwide.
          </p>
        </motion.div>
        <motion.div variants={fadeUp}>
          <strong>Build</strong>
          {SERVICES.slice(0, 4).map((s) => (
            <Link key={s.slug} to={`/services/${s.slug}`}>
              {s.title}
            </Link>
          ))}
        </motion.div>
        <motion.div variants={fadeUp}>
          <strong>Grow</strong>
          <Link to="/services/seo-aeo-geo">SEO and visibility</Link>
          <Link to="/services/ai-automation">Workflow automation</Link>
          <Link to="/pricing">Pricing</Link>
          <Link to="/blog">Blog</Link>
        </motion.div>
        <motion.div variants={fadeUp}>
          <strong>Company</strong>
          <Link to="/about">About</Link>
          <Link to="/glossary">Glossary</Link>
          <Link to="/faq">FAQs</Link>
          <Link to="/contact">Contact us</Link>
          <Link to="/privacy">Privacy policy</Link>
          <Link to="/terms">Terms</Link>
          <a href={`mailto:${EMAIL}`}>{EMAIL}</a>
        </motion.div>
      </Reveal>
      <div className="container footer-bottom">
        <span>&copy; 2026 {BRAND}. All rights reserved.</span>
        <span>
          <Link to="/privacy">Privacy</Link> · <Link to="/terms">Terms</Link> · Custom software |
          Mobile apps | Websites | SEO | Automation
        </span>
      </div>
    </footer>
  )
}
