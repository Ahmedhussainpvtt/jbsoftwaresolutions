import { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { EMAIL } from '../data/site'

// Easy Peeze API. JB-origin posts are emailed to info@jbsoftwaresolutions.com.
const CONTACT_API = 'https://easypeeze-tools-j6dbitzprq-el.a.run.app/contact'
// Shared Easy Peeze key (project ahmedhussianpvt). jbsoftwaresolutions.com must stay in its allowed domains.
const RECAPTCHA_SITE_KEY = '6Lf-LsEtAAAAAKGPRWhI5GDDjIYNOa_hWohbAJ9c'
const SOURCE = 'jbsoftwaresolutions.com/contact'

async function postJson(url, body) {
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(body),
    })
    const json = await res.json().catch(() => null)
    return { httpOk: res.ok, json }
  } catch {
    return { httpOk: false, json: null }
  }
}

function loadRecaptcha() {
  if (window.grecaptcha?.render) return Promise.resolve()
  if (window.__jbRecaptchaLoading) return window.__jbRecaptchaLoading
  window.__jbRecaptchaLoading = new Promise((resolve, reject) => {
    window.__jbRecaptchaReady = () => resolve()
    const s = document.createElement('script')
    s.src = 'https://www.google.com/recaptcha/api.js?onload=__jbRecaptchaReady&render=explicit'
    s.async = true
    s.defer = true
    s.onerror = reject
    document.head.appendChild(s)
  })
  return window.__jbRecaptchaLoading
}

export default function ContactForm() {
  const formRef = useRef(null)
  const captchaRef = useRef(null)
  const widgetId = useRef(null)
  const [captchaOk, setCaptchaOk] = useState(!RECAPTCHA_SITE_KEY)
  const [sending, setSending] = useState(false)
  const [status, setStatus] = useState(null)
  // Google's script is heavy; fetch it once the visitor starts using the form.
  const [wantCaptcha, setWantCaptcha] = useState(false)
  const engage = () => setWantCaptcha(true)

  useEffect(() => {
    if (!RECAPTCHA_SITE_KEY || !wantCaptcha) return undefined
    let cancelled = false
    loadRecaptcha()
      .then(() => {
        if (cancelled || !captchaRef.current || widgetId.current !== null) return
        widgetId.current = window.grecaptcha.render(captchaRef.current, {
          sitekey: RECAPTCHA_SITE_KEY,
          theme: 'dark',
          callback: () => setCaptchaOk(true),
          'expired-callback': () => setCaptchaOk(false),
          'error-callback': () => setCaptchaOk(false),
        })
      })
      .catch(() => setStatus({ error: true, text: `Could not load the spam check. Email ${EMAIL} instead.` }))
    return () => {
      cancelled = true
    }
  }, [wantCaptcha])

  // Read the token directly too; the button must not depend only on the widget callbacks.
  useEffect(() => {
    if (!RECAPTCHA_SITE_KEY) return undefined
    const id = setInterval(() => {
      if (widgetId.current === null || !window.grecaptcha?.getResponse) return
      const has = !!window.grecaptcha.getResponse(widgetId.current)
      setCaptchaOk((prev) => (prev === has ? prev : has))
    }, 400)
    return () => clearInterval(id)
  }, [])

  const resetCaptcha = () => {
    if (!RECAPTCHA_SITE_KEY) return
    setCaptchaOk(false)
    try {
      if (widgetId.current !== null) window.grecaptcha.reset(widgetId.current)
    } catch {
      /* widget gone */
    }
  }

  const onSubmit = async (e) => {
    e.preventDefault()
    if (sending) return
    const fd = new FormData(formRef.current)
    const name = String(fd.get('name') || '').trim()
    const email = String(fd.get('email') || '').trim()
    const message = String(fd.get('message') || '').trim()
    if (!name) return setStatus({ error: true, text: 'Please enter your name.' })
    if (!email.includes('@')) return setStatus({ error: true, text: 'Please enter a valid email.' })
    if (!message) return setStatus({ error: true, text: 'Please add some project details.' })

    let token = ''
    if (RECAPTCHA_SITE_KEY) {
      token = window.grecaptcha?.getResponse(widgetId.current) || ''
      if (!token || !captchaOk) {
        resetCaptcha()
        return setStatus({ error: true, text: 'Please complete the reCAPTCHA before sending.' })
      }
    }

    setSending(true)
    setStatus({ error: false, text: 'Sending...' })
    try {
      const api = await postJson(CONTACT_API, {
        name,
        email,
        company: String(fd.get('company') || '').trim(),
        service: fd.get('service'),
        budget: fd.get('budget'),
        project_details: message,
        source: SOURCE,
        'g-recaptcha-response': token,
      })
      if (!(api.httpOk && api.json?.ok === true && api.json?.emailQueued === true)) {
        throw new Error(api.json?.error || `Could not send. Email ${EMAIL} instead.`)
      }
      formRef.current.reset()
      setStatus({ error: false, text: 'Thanks - your brief was sent. We reply within 24 hours on business days.' })
    } catch (err) {
      setStatus({ error: true, text: err?.message || `Could not send. Email ${EMAIL} instead.` })
    } finally {
      setSending(false)
      resetCaptcha()
    }
  }

  return (
    <form
      className="form"
      ref={formRef}
      onSubmit={onSubmit}
      onFocus={engage}
      onPointerDown={engage}
      onKeyDown={engage}
      noValidate
    >
      <label>
        Name
        <input name="name" required maxLength={80} autoComplete="name" placeholder="Your name" />
      </label>
      <label>
        Email
        <input type="email" name="email" required maxLength={120} autoComplete="email" placeholder="you@company.com" />
      </label>
      <label>
        Company / project name
        <input name="company" maxLength={120} placeholder="Optional" />
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
        <textarea name="message" required maxLength={4000} placeholder="Goals, timeline, links, must-haves" />
      </label>
      {RECAPTCHA_SITE_KEY && <div ref={captchaRef} className="form-captcha" />}
      {RECAPTCHA_SITE_KEY && !captchaOk && !sending && (
        <p className="form-hint">Tick &quot;I&apos;m not a robot&quot; to enable the button.</p>
      )}
      <p className="form-legal">
        By sending this form you agree to our <Link to="/privacy">privacy policy</Link> and{' '}
        <Link to="/terms">terms</Link>.
      </p>
      {status && (
        <p className={`form-status${status.error ? ' is-error' : ' is-ok'}`} role="status" aria-live="polite">
          {status.text}
        </p>
      )}
      <button
        className="btn btn-primary"
        type="submit"
        disabled={sending || !captchaOk}
        aria-busy={sending}
      >
        {sending ? 'Sending...' : 'Get my quote'}
      </button>
    </form>
  )
}
