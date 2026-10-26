import { Link, useParams, Navigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import Reveal from '../components/Reveal'
import PageHero from '../components/PageHero'
import MagneticButton from '../components/MagneticButton'
import glossaryTerms from '../data/glossaryTerms.js'
import { BRAND } from '../data/site'
import { scaleIn, stagger } from '../motion'

export function GlossaryHub() {
  return (
    <>
      <PageHero>
        <div className="container">
          <Reveal className="section-kicker">Resources</Reveal>
          <Reveal as="h1">Glossary</Reveal>
          <Reveal as="p">
            Short, clear definitions of the words people use when they hire a software company in
            India.
          </Reveal>
        </div>
      </PageHero>
      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container">
          <motion.div
            className="term-grid"
            variants={stagger(0.03)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.05 }}
          >
            {glossaryTerms.map((t) => (
              <motion.div key={t.slug} variants={scaleIn} whileHover={{ y: -6, scale: 1.02 }}>
                <Link className="term-card" to={`/glossary/${t.slug}`}>
                  <strong>{t.title}</strong>
                  <span>{t.short}</span>
                </Link>
              </motion.div>
            ))}
          </motion.div>
          <p className="section-note" style={{ marginTop: '2rem' }}>
            Looking for questions instead of definitions? Visit the <Link to="/faq">FAQ hub</Link>{' '}
            or <Link to="/contact">contact us</Link>.
          </p>
        </div>
      </section>
    </>
  )
}

export function GlossaryTerm() {
  const { slug } = useParams()
  const term = glossaryTerms.find((t) => t.slug === slug)
  const related = glossaryTerms.filter((t) => t.slug !== slug).slice(0, 8)
  if (!term) return <Navigate to="/glossary" replace />

  return (
    <>
      <PageHero>
        <div className="container">
          <Reveal className="section-kicker">
            <Link to="/glossary">Glossary</Link>
          </Reveal>
          <Reveal as="h1">{term.title}</Reveal>
          <Reveal as="p">{term.short}</Reveal>
        </div>
      </PageHero>
      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container prose">
          <h2>Definition</h2>
          <p>{term.long}</p>
          <h2>Why this matters when you hire {BRAND}</h2>
          <p>
            Clear language helps you shortlist the right vendor. This page exists so &quot;{term.title}&quot;
            maps to a real service and a real team at {BRAND}, not a vague buzzword.
          </p>
          <p>
            <MagneticButton to="/contact" className="btn btn-primary">
              Ask about {term.title.toLowerCase()}
            </MagneticButton>{' '}
            <MagneticButton to="/faq" className="btn btn-ghost">
              Browse FAQs
            </MagneticButton>
          </p>
          <h2>Related terms</h2>
          <div className="term-related">
            {related.map((r) => (
              <Link key={r.slug} className="service-chip" to={`/glossary/${r.slug}`}>
                {r.title}
              </Link>
            ))}
          </div>
        </div>
      </section>
    </>
  )
}
