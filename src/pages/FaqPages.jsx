import { Link, useParams, Navigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import Reveal from '../components/Reveal'
import MagneticButton from '../components/MagneticButton'
import faqData from '../data/faqTopics.js'
import { BRAND } from '../data/site'
import { scaleIn, stagger } from '../motion'

export function FaqHub() {
  const { count, topicCount, topics, preview } = faqData

  return (
    <>
      <section className="page-hero">
        <div className="container">
          <Reveal className="section-kicker">Resources</Reveal>
          <Reveal as="h1">FAQs</Reveal>
          <Reveal as="p">
            {count}+ direct answers across {topicCount} topic pages covering software, apps, SEO,
            pricing and how we work.
          </Reveal>
        </div>
      </section>
      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container">
          <motion.div
            className="faq-topic-grid"
            variants={stagger(0.03)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.05 }}
          >
            {topics.map((t) => (
              <motion.div key={t.slug} variants={scaleIn} whileHover={{ y: -6, scale: 1.02 }}>
                <Link className="faq-topic-card" to={`/faq/${t.slug}`}>
                  <strong>{t.title}</strong>
                  <span>{t.desc}</span>
                </Link>
              </motion.div>
            ))}
          </motion.div>
          <div className="faq" style={{ marginTop: '2.5rem' }}>
            {preview.map(([q, a]) => (
              <details key={q}>
                <summary>{q}</summary>
                <p>{a}</p>
              </details>
            ))}
          </div>
          <p className="section-note" style={{ marginTop: '2rem' }}>
            Need definitions? Open the <Link to="/glossary">glossary</Link>. Ready to talk?{' '}
            <Link to="/contact">Contact {BRAND}</Link>.
          </p>
        </div>
      </section>
    </>
  )
}

export function FaqTopic() {
  const { slug } = useParams()
  const topic = faqData.topics.find((t) => t.slug === slug)
  if (!topic) return <Navigate to="/faq" replace />

  return (
    <>
      <section className="page-hero">
        <div className="container">
          <Reveal className="section-kicker">
            <Link to="/faq">FAQ</Link>
          </Reveal>
          <Reveal as="h1">{topic.title}</Reveal>
          <Reveal as="p">{topic.desc}</Reveal>
        </div>
      </section>
      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container">
          <div className="faq">
            {topic.qs.map(([q, a]) => (
              <details key={q}>
                <summary>{q}</summary>
                <p>{a}</p>
              </details>
            ))}
          </div>
          <motion.div
            className="cta-band"
            style={{ marginTop: '2rem' }}
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <div>
              <h2>Still unsure?</h2>
              <p>Send your goals and constraints. We reply with fit and next steps.</p>
            </div>
            <MagneticButton to="/contact" className="btn btn-primary">
              Contact {BRAND}
            </MagneticButton>
          </motion.div>
          <p style={{ marginTop: '1.5rem' }}>
            <Link to="/faq">All FAQ topics</Link> · <Link to="/glossary">Glossary</Link>
          </p>
        </div>
      </section>
    </>
  )
}
