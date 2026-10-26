import { Link, Navigate, useParams } from 'react-router-dom'
import { motion } from 'framer-motion'
import Reveal from '../components/Reveal'
import MagneticButton from '../components/MagneticButton'
import { getService } from '../data/services'
import { serviceImg } from '../data/site'
import PageHero from '../components/PageHero'
import { isFirstLoad } from '../firstLoad'
import { fadeUp, fadeLeft, fadeRight, scaleIn, stagger } from '../motion'

export function ServiceRoute() {
  const { slug } = useParams()
  const clean = (slug || '').replace(/\/$/, '')
  if (!getService(clean)) return <Navigate to="/" replace />
  return <ServicePage slug={clean} />
}

export default function ServicePage({ slug }) {
  const s = getService(slug)
  if (!s) {
    return (
      <PageHero>
        <div className="container">
          <Reveal as="h1">Service not found</Reveal>
          <MagneticButton to="/" className="btn btn-primary">
            Go home
          </MagneticButton>
        </div>
      </PageHero>
    )
  }

  const sec = s.section

  return (
    <>
      <PageHero className="service-hero">
        <div className="container service-hero-grid">
          <motion.div
            className="service-hero-copy"
            variants={stagger(0.12)}
            initial={isFirstLoad() ? false : 'hidden'}
            animate="show"
          >
            <motion.div className="section-kicker" variants={fadeUp}>
              Services
            </motion.div>
            <motion.h1 variants={fadeLeft}>{s.h1}</motion.h1>
            <motion.p variants={fadeUp}>{s.desc}</motion.p>
            <motion.div className="hero-cta" style={{ marginTop: '1.75rem' }} variants={fadeUp}>
              <MagneticButton to="/contact" className="btn btn-primary">
                Get a project quote
              </MagneticButton>
              <MagneticButton to="/pricing" className="btn btn-ghost">
                View pricing
              </MagneticButton>
            </motion.div>
          </motion.div>
          <motion.div
            className="service-hero-visual"
            initial={isFirstLoad() ? false : { opacity: 0, x: 48, scale: 0.94 }}
            animate={{ opacity: 1, x: 0, scale: 1 }}
            transition={{ duration: 0.85, ease: [0.16, 1, 0.3, 1], delay: 0.15 }}
            whileHover={{ scale: 1.02, y: -6 }}
          >
            <img
              {...serviceImg(s.imgs.hero)}
              sizes="(max-width: 900px) 92vw, 560px"
              alt={s.imageAlt}
              width="960"
              height="640"
              loading="eager"
              fetchPriority="high"
            />
          </motion.div>
        </div>
      </PageHero>

      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container">
          <Reveal className="section-kicker">{sec.offer_kicker}</Reveal>
          <Reveal className="section-title" as="h2">
            {sec.offer_h2}
          </Reveal>
          <Reveal className="section-sub" as="p">
            {sec.why}
          </Reveal>
          <motion.div
            className="service-offer-grid"
            variants={stagger(0.1)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.2 }}
          >
            <motion.div className="service-offer" variants={scaleIn} whileHover={{ y: -8, scale: 1.02 }}>
              <h3>{sec.include_h3}</h3>
              <ul>
                {s.bullets.map((b) => (
                  <li key={b}>{b}</li>
                ))}
              </ul>
            </motion.div>
            <motion.div className="service-offer" variants={scaleIn} whileHover={{ y: -8, scale: 1.02 }}>
              <h3>{sec.engage_h3}</h3>
              <ul>
                {s.engage.map((b) => (
                  <li key={b}>{b}</li>
                ))}
              </ul>
            </motion.div>
            <motion.div
              className="service-offer service-offer-cta"
              variants={scaleIn}
              whileHover={{ y: -8, scale: 1.02 }}
            >
              <h3>{sec.cta_h3}</h3>
              <p>Share goals, links and budget range. We reply with fit, timeline and a clear quote path.</p>
              <MagneticButton to="/contact" className="btn btn-primary">
                Start a brief
              </MagneticButton>
              <div className="service-chip-row" style={{ marginTop: '1rem' }}>
                {s.others.map((o) => (
                  <Link key={o.slug} className="service-chip" to={`/services/${o.slug}/`}>
                    {o.title}
                  </Link>
                ))}
              </div>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {s.features.map((feat, i) => (
        <section
          key={feat.title}
          className={`section service-feature${i % 2 === 1 ? ' is-reverse' : ''}`}
        >
          <div className="container service-feature-grid">
            <Reveal
              className="service-feature-media"
              variants={i % 2 === 1 ? fadeRight : fadeLeft}
            >
              <motion.img
                {...serviceImg(feat.image)}
                sizes="(max-width: 900px) 92vw, 540px"
                alt={feat.title}
                width="960"
                height="640"
                loading="lazy"
                whileHover={{ scale: 1.04 }}
                transition={{ type: 'spring', stiffness: 220, damping: 18 }}
              />
            </Reveal>
            <Reveal
              className="service-feature-copy"
              variants={i % 2 === 1 ? fadeLeft : fadeRight}
            >
              <div className="section-kicker">{feat.kicker}</div>
              <h2>{feat.title}</h2>
              <p>{feat.text}</p>
            </Reveal>
          </div>
        </section>
      ))}

      <section className="section service-closing" id="details">
        <div className="container">
          <Reveal className="service-closing-head">
            <div className="section-kicker">{sec.closing_kicker}</div>
            <h2 className="section-title">{sec.closing_h2}</h2>
          </Reveal>
          <div className="service-closing-body">
            <Reveal className="service-closing-lead" as="p">
              {s.closing.intro}
            </Reveal>
            <motion.div
              className="service-closing-grid"
              variants={stagger(0.1)}
              initial="hidden"
              whileInView="show"
              viewport={{ once: true }}
            >
              <motion.article className="service-closing-card" variants={scaleIn} whileHover={{ y: -8 }}>
                <h3>Cost and timeline</h3>
                <p>{s.closing.cost}</p>
              </motion.article>
              <motion.article className="service-closing-card" variants={scaleIn} whileHover={{ y: -8 }}>
                <h3>Who this is for</h3>
                <p>{s.closing.who}</p>
              </motion.article>
              <motion.article className="service-closing-card" variants={scaleIn} whileHover={{ y: -8 }}>
                <h3>Next step</h3>
                <p>
                  {s.closing.next}{' '}
                  <Link to="/contact">Contact us</Link>.
                </p>
              </motion.article>
            </motion.div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <motion.div
            className="cta-band"
            initial={{ opacity: 0, y: 40, scale: 0.97 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ once: true }}
            transition={{ type: 'spring', stiffness: 160, damping: 18 }}
            whileHover={{ scale: 1.01, y: -4 }}
          >
            <div>
              <h2>{sec.cta_h2}</h2>
              <p>Share goals and constraints. We come back with a clear plan on the contact form or email.</p>
            </div>
            <div className="cta-actions">
              <MagneticButton to="/contact" className="btn btn-primary">
                Contact JB Software Solutions
              </MagneticButton>
            </div>
          </motion.div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <Reveal className="section-kicker">FAQ</Reveal>
          <Reveal className="section-title" as="h2">
            {sec.faq_h2}
          </Reveal>
          <div className="faq">
            {s.faqs.map(([q, a], i) => (
              <Reveal key={q} as="details" delay={i * 0.05}>
                <summary>{q}</summary>
                <p>{a}</p>
              </Reveal>
            ))}
          </div>
        </div>
      </section>
    </>
  )
}
