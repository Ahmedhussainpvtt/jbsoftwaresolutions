import { useMemo, useState, useRef } from 'react'
import { Link } from 'react-router-dom'
import {
  motion,
  AnimatePresence,
  useScroll,
  useTransform,
  useMotionValue,
  useSpring,
  useReducedMotion,
} from 'framer-motion'
import Reveal from '../components/Reveal'
import MagneticButton from '../components/MagneticButton'
import Terminal from '../components/Terminal'
import HeroTitle from '../components/HeroTitle'
import FloatingBits from '../components/FloatingBits'
import MorphBlob from '../components/MorphBlob'
import ScrollMarquee from '../components/ScrollMarquee'
import TiltCard from '../components/TiltCard'
import CountUp from '../components/CountUp'
import TextScramble from '../components/TextScramble'
import {
  TRUST,
  MARQUEE,
  WORK,
  PRICES,
  SERVICES,
  HOME_FAQS,
} from '../data/site'
import {
  fadeUp,
  fadeLeft,
  fadeRight,
  scaleIn,
  stagger,
  cardHover,
} from '../motion'

const chips = [
  ['custom software development company India', '/services/custom-software'],
  ['website development company India', '/services/web-development'],
  ['mobile app development company India', '/services/mobile-app-development'],
  ['SEO company India', '/services/seo-aeo-geo'],
  ['GEO generative engine optimization', '/services/seo-aeo-geo'],
  ['business workflow automation', '/services/ai-automation'],
  ['desktop app development', '/services/desktop-apps'],
  ['hire developers India', '/contact'],
]

export default function Home() {
  const [filter, setFilter] = useState('all')
  const reduce = useReducedMotion()
  const heroRef = useRef(null)
  const cards = useMemo(
    () => (filter === 'all' ? WORK : WORK.filter((w) => w.cat === filter)),
    [filter],
  )
  const { scrollYProgress } = useScroll({
    target: heroRef,
    offset: ['start start', 'end start'],
  })
  const meshY = useTransform(scrollYProgress, [0, 1], [0, 160])
  const copyY = useTransform(scrollYProgress, [0, 1], [0, 80])
  const stageY = useTransform(scrollYProgress, [0, 1], [0, -40])
  const heroOpacity = useTransform(scrollYProgress, [0, 0.85], [1, 0.35])

  const mx = useMotionValue(0)
  const my = useMotionValue(0)
  const smx = useSpring(mx, { stiffness: 80, damping: 20 })
  const smy = useSpring(my, { stiffness: 80, damping: 20 })
  const orbAx = useTransform(smx, (v) => v * 1.4)
  const orbAy = useTransform(smy, (v) => v * 1.2)

  const onHeroMove = (e) => {
    if (reduce || !heroRef.current) return
    const r = heroRef.current.getBoundingClientRect()
    const px = (e.clientX - r.left) / r.width - 0.5
    const py = (e.clientY - r.top) / r.height - 0.5
    mx.set(px * 28)
    my.set(py * 18)
  }

  return (
    <>
      <section
        className="hero"
        ref={heroRef}
        onPointerMove={onHeroMove}
        onPointerLeave={() => {
          mx.set(0)
          my.set(0)
        }}
      >
        <motion.div className="hero-bg" aria-hidden="true" style={{ y: meshY, opacity: heroOpacity }}>
          <motion.div className="hero-mesh" style={{ x: smx, y: smy }} />
          <div className="hero-grid" />
          <motion.div className="hero-orb hero-orb-a" style={{ x: orbAx, y: orbAy }} />
          <div className="hero-orb hero-orb-b" />
          <div className="hero-orb hero-orb-c" />
          <FloatingBits />
          <MorphBlob />
        </motion.div>
        <div className="container hero-inner">
          <div className="hero-layout">
            <motion.div className="hero-copy" style={{ y: copyY }}>
              <HeroTitle />
              <p className="hero-sub hero-in" style={{ '--d': '120ms' }}>
                From custom software and mobile apps to modern websites, we turn your ideas into
                powerful digital solutions built around your business.
              </p>
              <div className="hero-cta hero-in" style={{ '--d': '220ms' }}>
                <MagneticButton to="/contact" className="btn btn-primary">
                  Get a free strategy call
                </MagneticButton>
                <MagneticButton to="/pricing" className="btn btn-ghost">
                  See pricing
                </MagneticButton>
              </div>
            </motion.div>
            <motion.div className="hero-stage" style={{ y: stageY }}>
              <div className="ai-proof">
                <Terminal />
                <div className="pixel-row" aria-hidden="true">
                  {Array.from({ length: 6 }).map((_, i) => (
                    <span
                      key={i}
                      className="pixel pixel-pulse"
                      style={{ '--pd': `${1.8 + i * 0.18}s`, '--pdl': `${i * 0.12}s` }}
                    />
                  ))}
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      <ScrollMarquee items={MARQUEE} />

      <section className="section" id="trust" style={{ paddingTop: '2.5rem', paddingBottom: '1rem' }}>
        <div className="container">
          <motion.div
            className="trust-strip"
            variants={stagger(0.1)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.3 }}
          >
            {TRUST.map((t) => (
              <motion.article
                key={t.title}
                variants={fadeUp}
                whileHover={reduce ? undefined : { y: -8, scale: 1.03, rotate: -0.4 }}
                transition={{ type: 'spring', stiffness: 280, damping: 18 }}
              >
                <strong>{t.title}</strong>
                <span>{t.text}</span>
              </motion.article>
            ))}
          </motion.div>
        </div>
      </section>

      <section className="section manifesto section-wipe" id="manifesto">
        <div className="container">
          <Reveal className="section-kicker">
            <TextScramble text="How we build" as="span" />
          </Reveal>
          <Reveal className="manifesto-title" as="h2" variants={fadeLeft}>
            The website is not a brochure.
            <br />
            <span className="grad">It is the first product you ship.</span>
          </Reveal>
          <Reveal className="manifesto-sub" as="p" variants={fadeRight}>
            We treat your site like a product: clear offer, measurable outcome, motion with purpose,
            and a contact path that feels easy. Same bar for apps, custom tools and search work.
          </Reveal>
          <motion.div
            className="manifesto-metrics"
            variants={stagger(0.1)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
          >
            {[
              [1, 'Proof before pitch'],
              [2, 'Ship weekly, not eventually'],
              [3, 'SEO and product in one pod'],
              [4, 'You keep the IP'],
            ].map(([n, label], i) => (
              <TiltCard
                key={label}
                className="manifesto-metric"
                max={8}
                variants={scaleIn}
                whileHover={reduce ? undefined : { scale: 1.06, y: -6 }}
              >
                <strong>
                  0
                  <CountUp to={n} />
                </strong>
                <span>{label}</span>
              </TiltCard>
            ))}
          </motion.div>
        </div>
      </section>

      <section className="section" id="work">
        <div className="container work-head">
          <div>
            <Reveal className="section-kicker">Selected work</Reveal>
            <Reveal className="section-title" as="h2">
              Engagements shaped like revenue problems
            </Reveal>
          </div>
          <Reveal className="section-sub work-head-copy" as="p">
            No invented Fortune-500 logos. These are the engagement patterns founders actually hire
            us for: challenge, approach, result.
          </Reveal>
        </div>
        <div className="work-filters" role="tablist" aria-label="Filter work">
          {[
            ['all', 'All'],
            ['web', 'Web + SEO'],
            ['mobile', 'Mobile'],
            ['ops', 'Ops'],
          ].map(([id, label]) => (
            <motion.button
              key={id}
              type="button"
              className={`work-filter${filter === id ? ' is-active' : ''}`}
              role="tab"
              aria-selected={filter === id}
              onClick={() => setFilter(id)}
              whileHover={{ scale: 1.08 }}
              whileTap={{ scale: 0.94 }}
              layout
            >
              {filter === id && (
                <motion.span
                  className="work-filter-glow"
                  layoutId="workFilterGlow"
                  transition={{ type: 'spring', stiffness: 380, damping: 28 }}
                />
              )}
              <span style={{ position: 'relative', zIndex: 1 }}>{label}</span>
            </motion.button>
          ))}
        </div>
        <motion.div className="work-rail" layout>
          <AnimatePresence mode="popLayout">
            {cards.map((w) => (
              <TiltCard
                key={w.title}
                as={motion.article}
                className="work-card shine-sweep"
                max={9}
                layout
                initial={{ opacity: 0, y: 40, scale: 0.92, filter: 'blur(8px)' }}
                animate={{ opacity: 1, y: 0, scale: 1, filter: 'blur(0px)' }}
                exit={{ opacity: 0, scale: 0.88, y: -24, filter: 'blur(6px)', rotate: -2 }}
                transition={{ type: 'spring', stiffness: 220, damping: 22 }}
                whileHover="hover"
                variants={cardHover}
              >
                <div className="work-meta">
                  <span>{w.meta}</span>
                  <span>{w.label}</span>
                  <div className="work-tag">{w.tag}</div>
                </div>
                <h3>{w.title}</h3>
                <p className="work-challenge">
                  <strong>Challenge:</strong> {w.challenge}
                </p>
                <p className="work-approach">
                  <strong>Approach:</strong> {w.approach}
                </p>
                <div className="work-results">
                  {w.results.map((r, ri) => (
                    <motion.div
                      key={r.k}
                      initial={{ opacity: 0, y: 12 }}
                      whileInView={{ opacity: 1, y: 0 }}
                      viewport={{ once: true }}
                      transition={{ delay: ri * 0.08 }}
                    >
                      <strong>{r.k}</strong>
                      <span>{r.v}</span>
                    </motion.div>
                  ))}
                </div>
                <Link className="work-link" to="/contact">
                  Start a similar brief
                </Link>
              </TiltCard>
            ))}
          </AnimatePresence>
          <TiltCard
            as={motion.article}
            className="work-card work-card-cta shine-sweep"
            max={7}
            layout
            whileHover={{ scale: 1.03, y: -6 }}
          >
            <div className="work-meta">
              <span>04</span>
              <span>Your brief next</span>
            </div>
            <h3>Bring the constraint. We bring the plan.</h3>
            <p>
              Share goals, links and budget range. We reply with fit, timeline and a fixed or phased
              path.
            </p>
            <MagneticButton to="/contact" className="btn btn-primary">
              Talk to JB
            </MagneticButton>
          </TiltCard>
        </motion.div>
      </section>

      <section className="section" id="promises">
        <div className="container">
          <Reveal className="section-kicker">What you can count on</Reveal>
          <Reveal className="section-title" as="h2">
            Promises that make booking us safer
          </Reveal>
          <motion.ul
            className="promise-list"
            variants={stagger(0.12)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
          >
            {[
              ['Honest fit check', 'If we are wrong for you, we say so before you pay.'],
              ['Scope in writing', 'Deliverables, timeline and price before the first sprint.'],
              ['Weekly visible progress', 'Working builds, not radio silence until the deadline.'],
              ['Small-team attention', 'You talk to people who ship, not a ticket queue.'],
            ].map(([t, b]) => (
              <motion.li
                key={t}
                variants={fadeLeft}
                whileHover={reduce ? undefined : { x: 14, scale: 1.01 }}
              >
                <strong>{t}</strong>
                {b}
              </motion.li>
            ))}
          </motion.ul>
        </div>
      </section>

      <section className="section" id="pricing-teaser">
        <div className="container">
          <Reveal className="section-kicker">Transparent starting points</Reveal>
          <Reveal className="section-title" as="h2">
            Pricing ranges buyers can plan around
          </Reveal>
          <Reveal className="section-sub" as="p">
            Agencies that hide every number lose serious buyers to shops that show a floor. Here is
            ours. Exact quotes still depend on scope.
          </Reveal>
          <motion.div
            className="price-grid"
            variants={stagger(0.12)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
          >
            {PRICES.map((p) => (
              <TiltCard
                key={p.title}
                as={motion.article}
                className={`price-card shine-sweep${p.featured ? ' is-featured' : ''}`}
                max={8}
                variants={scaleIn}
                whileHover={reduce ? undefined : { y: -14, scale: 1.04 }}
              >
                <h3>{p.title}</h3>
                <div className="from">{p.from}</div>
                <p>{p.text}</p>
              </TiltCard>
            ))}
          </motion.div>
          <p style={{ marginTop: '1.5rem' }}>
            <MagneticButton to="/pricing" className="btn btn-primary">
              See full pricing
            </MagneticButton>{' '}
            <MagneticButton to="/contact" className="btn btn-ghost">
              Request a fixed quote
            </MagneticButton>
          </p>
        </div>
      </section>

      <section className="section" id="capabilities">
        <div className="container">
          <Reveal className="section-kicker">Capabilities</Reveal>
          <Reveal className="section-title" as="h2">
            Website, mobile app and custom software development services
          </Reveal>
          <motion.div
            className="bento"
            id="bento"
            variants={stagger(0.07)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.15 }}
          >
            {SERVICES.map((s, i) => (
              <TiltCard
                key={s.slug}
                className={`bento-tile shine-sweep${i === 0 ? ' bento-lg' : ''}${i === 4 ? ' bento-wide' : ''}`}
                max={11}
                variants={scaleIn}
              >
                <Link to={`/services/${s.slug}/`} className="bento-tile-link">
                  <span className="bento-num">0{i + 1}</span>
                  <h3>{s.title}</h3>
                  <p>{s.desc}</p>
                  <span className="bento-go">Explore</span>
                </Link>
              </TiltCard>
            ))}
          </motion.div>
        </div>
      </section>

      <section className="section" id="keywords">
        <div className="container">
          <Reveal className="section-kicker">Services people hire us for</Reveal>
          <Reveal className="section-title" as="h2">
            Commercial keywords mapped to real services
          </Reveal>
          <motion.div
            className="seo-cloud"
            variants={stagger(0.035)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
          >
            {chips.map(([label, to]) => (
              <motion.div
                key={label}
                className="seo-chip-wrap"
                variants={fadeUp}
                whileHover={reduce ? undefined : { scale: 1.08, y: -3 }}
              >
                <Link className="seo-chip" to={to}>
                  {label}
                </Link>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <Reveal className="section-kicker">
            <TextScramble text="FAQs" as="span" />
          </Reveal>
          <Reveal className="section-title" as="h2">
            Frequently asked questions
          </Reveal>
          <div className="faq">
            {HOME_FAQS.map((f, i) => (
              <motion.details
                key={f.q}
                initial={{ opacity: 0, x: -24 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.06 }}
              >
                <summary>{f.q}</summary>
                <p>{f.a}</p>
              </motion.details>
            ))}
          </div>
          <p className="section-note" style={{ marginTop: '1.25rem' }}>
            More answers: <Link to="/faq">FAQ hub</Link>.
          </p>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <motion.div
            className="cta-band"
            initial={{ opacity: 0, y: 50, scale: 0.96 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ once: true }}
            transition={{ type: 'spring', stiffness: 160, damping: 18 }}
            whileHover={reduce ? undefined : { scale: 1.015, y: -4 }}
          >
            <div>
              <h2>Ready to build something people can find?</h2>
              <p>Send a short brief. We reply with fit, timeline and a clear commercial path.</p>
            </div>
            <div className="cta-actions">
              <MagneticButton to="/contact" className="btn btn-primary">
                Contact JB Software Solutions
              </MagneticButton>
            </div>
          </motion.div>
        </div>
      </section>
    </>
  )
}
