import { Link, useNavigate } from 'react-router-dom'
import { useEffect } from 'react'
import { motion } from 'framer-motion'
import Reveal from '../components/Reveal'
import MagneticButton from '../components/MagneticButton'
import { EMAIL } from '../data/site'
import { stagger, scaleIn, fadeUp } from '../motion'
import privacyHtml from '../data/privacyHtml.js'
import termsHtml from '../data/termsHtml.js'

const PRICE_CARDS = [
  {
    title: 'Website development',
    from: 'From ₹50,000',
    items: [
      'Business website, about 5 to 12 pages',
      'Works well on phones',
      'Contact form and basic SEO setup',
    ],
  },
  {
    title: 'Web app development',
    from: 'From ₹3,00,000',
    featured: true,
    items: [
      'First version of your product in the browser',
      'Login, dashboard or simple workflows',
      'Clear milestones and handover docs',
    ],
  },
  {
    title: 'Mobile app development',
    from: 'From ₹5,00,000',
    items: [
      'First app for Android and/or iPhone',
      'Typical timeline around 8 to 12 weeks',
      'Help publishing to the app stores',
    ],
  },
  {
    title: 'Custom software',
    from: 'From ₹4,00,000',
    items: [
      'Internal tools for your team',
      'Connect to the apps you already use',
      'You own the finished work',
    ],
  },
  {
    title: 'SEO and visibility',
    from: 'From ₹25,000/mo',
    items: [
      'Help people find you on Google',
      'Useful content for buyer questions',
      'Checks for AI search mentions',
    ],
  },
  {
    title: 'Workflow automation',
    from: 'From ₹75,000',
    items: [
      'Lead and follow-up flows',
      'Connect forms, chat and CRM',
      'Approvals and reminders',
    ],
  },
]

function HtmlPage({ html }) {
  const navigate = useNavigate()

  useEffect(() => {
    const root = document.getElementById('legal-html-root')
    if (!root) return undefined
    const onClick = (e) => {
      const a = e.target.closest('[data-to]')
      if (!a) return
      e.preventDefault()
      navigate(a.getAttribute('data-to'))
    }
    root.addEventListener('click', onClick)
    return () => root.removeEventListener('click', onClick)
  }, [navigate, html])

  return <div id="legal-html-root" dangerouslySetInnerHTML={{ __html: html }} />
}

export function About() {
  return (
    <>
      <section className="page-hero">
        <div className="container">
          <Reveal className="section-kicker">About</Reveal>
          <Reveal as="h1">A small agency that fights for your outcome</Reveal>
          <Reveal as="p">
            We are not a factory floor of tickets. We are a tight team that works hard, stays close
            to the people who hire us, and actually loves seeing customers win.
          </Reveal>
          <div className="hero-cta" style={{ marginTop: '1.75rem' }}>
            <MagneticButton to="/contact" className="btn btn-primary">
              Work with us
            </MagneticButton>
            <MagneticButton to="/pricing" className="btn btn-ghost">
              See pricing
            </MagneticButton>
          </div>
        </div>
      </section>
      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container prose">
          <Reveal as="h2">We are small on purpose</Reveal>
          <Reveal as="p">
            JB Software Solutions is a small agency by choice. That means you are not lost behind
            layers of account managers. When you message us, the people building your product are in
            the loop. We sweat the details, we answer fast, and we stay supportive long after the
            launch party ends.
          </Reveal>
          <Reveal as="p">
            We really love our customers. Not as a slogan on a wall. As a working rule: clear
            communication, honest scope, patient hand-holding when something is new, and zero ego
            when feedback arrives. Your success is the only scoreboard that matters to us.
          </Reveal>
          <Reveal as="h2">Who we are</Reveal>
          <Reveal as="p">
            We help founders and operators ship digital products: websites, mobile apps, custom
            software, desktop tools, and the SEO / AEO / GEO layer that makes those products easier
            to find on Google and in answer-style results.
          </Reveal>
          <Reveal as="h2">How we work</Reveal>
          <ul>
            <li>Ship systems, not slide decks</li>
            <li>Measure outcomes: leads, retention, citations, not vanity screenshots</li>
            <li>Keep IP with the client</li>
            <li>Use AI for velocity. Keep humans on taste, care and accountability</li>
            <li>Treat every customer like the reason we get to do this work</li>
          </ul>
          <Reveal as="h2">Where we work</Reveal>
          <Reveal as="p">
            India-first delivery with remote collaboration for clients across India, the Middle
            East, the UK, the US and beyond.
          </Reveal>
          <p>
            <MagneticButton to="/contact" className="btn btn-primary">
              Work with us
            </MagneticButton>
          </p>
        </div>
      </section>
    </>
  )
}

export function Pricing() {
  return (
    <>
      <section className="page-hero">
        <div className="container">
          <Reveal className="section-kicker">Pricing</Reveal>
          <Reveal as="h1">Starting prices, not mystery quotes</Reveal>
          <Reveal as="p">
            Buyers compare India agencies on clarity. These floors help you budget. Final quotes are
            fixed or phased after discovery.
          </Reveal>
          <div className="hero-cta" style={{ marginTop: '1.75rem' }}>
            <MagneticButton to="/contact" className="btn btn-primary">
              Get a scoped quote
            </MagneticButton>
            <MagneticButton to="/services/web-development" className="btn btn-ghost">
              Browse services
            </MagneticButton>
          </div>
        </div>
      </section>
      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container">
          <motion.div
            className="price-grid"
            variants={stagger(0.08)}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
          >
            {PRICE_CARDS.map((p) => (
              <motion.article
                key={p.title}
                className={`price-card${p.featured ? ' is-featured' : ''}`}
                variants={scaleIn}
                whileHover={{ y: -10, scale: 1.02 }}
              >
                <h3>{p.title}</h3>
                <div className="from">{p.from}</div>
                <ul>
                  {p.items.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
                <MagneticButton
                  to="/contact"
                  className={`btn ${p.featured ? 'btn-primary' : 'btn-ghost'}`}
                >
                  Request quote
                </MagneticButton>
              </motion.article>
            ))}
          </motion.div>
          <div className="prose" style={{ marginTop: '2.5rem' }}>
            <Reveal as="h2">What changes the number</Reveal>
            <Reveal as="p">
              Integrations, compliance, bilingual content, offline/desktop needs, and how finished
              your requirements already are. We would rather quote honestly than win a fake low bid.
            </Reveal>
            <p>
              <MagneticButton to="/contact" className="btn btn-primary">
                Get a fixed or phased quote
              </MagneticButton>
            </p>
          </div>
        </div>
      </section>
    </>
  )
}

export function Contact() {
  return (
    <>
      <section className="page-hero">
        <div className="container">
          <Reveal className="section-kicker">Contact</Reveal>
          <Reveal as="h1">Get a scoped quote</Reveal>
          <Reveal as="p">
            Send a short brief. We reply within 24 hours on business days with fit, rough timeline
            and next steps. No phone tag. No spam.
          </Reveal>
        </div>
      </section>
      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container contact-grid">
          <Reveal variants={fadeUp}>
            <form className="form" action={`https://formsubmit.co/${EMAIL}`} method="POST">
              <input type="hidden" name="_next" value="https://jbsoftwaresolutions.com/thank-you/" />
              <input type="hidden" name="_subject" value="New lead - JB Software Solutions" />
              <input type="hidden" name="_template" value="table" />
              <input type="hidden" name="_captcha" value="false" />
              <input
                className="honey"
                type="text"
                name="_honey"
                tabIndex={-1}
                autoComplete="off"
                aria-hidden="true"
              />
              <label>
                Name
                <input name="name" required placeholder="Your name" />
              </label>
              <label>
                Email
                <input type="email" name="email" required placeholder="you@company.com" />
              </label>
              <label>
                Company / project name
                <input name="company" placeholder="Optional" />
              </label>
              <label>
                Service
                <select name="service">
                  <option>Web development</option>
                  <option>Mobile app</option>
                  <option>Custom software</option>
                  <option>SEO / AEO / GEO</option>
                  <option>Workflow / business automation</option>
                  <option>Desktop app</option>
                  <option>Not sure yet</option>
                </select>
              </label>
              <label>
                Budget range
                <select name="budget">
                  <option>Under ₹1 lakh</option>
                  <option>₹1-5 lakh</option>
                  <option>₹5-15 lakh</option>
                  <option>₹15 lakh+</option>
                  <option>Not sure yet</option>
                </select>
              </label>
              <label>
                Project details
                <textarea name="message" required placeholder="Goals, timeline, links, must-haves" />
              </label>
              <p className="form-legal">
                By sending this form you agree to our <Link to="/privacy">privacy policy</Link> and{' '}
                <Link to="/terms">terms</Link>.
              </p>
              <button className="btn btn-primary" type="submit">
                Get my quote
              </button>
            </form>
          </Reveal>
          <div className="prose">
            <Reveal as="h2">How we reply</Reveal>
            <Reveal as="p">
              This form emails the JB team directly and sends you to a confirmation page. Prefer
              email? Write <a href={`mailto:${EMAIL}`}>{EMAIL}</a> with your brief.
            </Reveal>
            <Reveal as="h2">What happens next</Reveal>
            <ul>
              <li>We confirm fit within 24 hours on business days</li>
              <li>You get a written scope outline</li>
              <li>We agree fixed or phased pricing before build starts</li>
            </ul>
            <p>
              <Link to="/pricing">See starting prices</Link> if you want ballpark numbers first.
            </p>
            <p className="section-note">
              By submitting, you agree we may contact you about your enquiry. See our{' '}
              <Link to="/privacy">privacy policy</Link> and <Link to="/terms">terms</Link>.
            </p>
          </div>
        </div>
      </section>
    </>
  )
}

export function BlogHub() {
  return (
    <section className="page-hero">
      <div className="container">
        <Reveal className="section-kicker">Resources</Reveal>
        <Reveal as="h1">Blog</Reveal>
        <Reveal as="p">Guides on software, apps and getting found online.</Reveal>
        <MagneticButton to="/" className="btn btn-primary" style={{ marginTop: '1rem' }}>
          Back home
        </MagneticButton>
      </div>
    </section>
  )
}

export function Privacy() {
  return <HtmlPage html={privacyHtml} />
}

export function Terms() {
  return <HtmlPage html={termsHtml} />
}

export function NotFound() {
  return (
    <section className="page-hero">
      <div className="container">
        <Reveal className="section-kicker">Error</Reveal>
        <Reveal as="h1">Page not found</Reveal>
        <MagneticButton to="/" className="btn btn-primary">
          Go home
        </MagneticButton>
      </div>
    </section>
  )
}
