import { useEffect, useState } from 'react'

const KEY = 'jb-theme'

function systemTheme() {
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme)
}

export default function ThemeSwitch() {
  // Server HTML has no theme; the active button is styled from html[data-theme] until mount.
  const [theme, setTheme] = useState(null)

  useEffect(() => {
    setTheme(document.documentElement.getAttribute('data-theme') || systemTheme())
    const mq = window.matchMedia('(prefers-color-scheme: dark)')
    const onSystemChange = () => {
      let saved = null
      try {
        saved = localStorage.getItem(KEY)
      } catch {
        /* storage blocked */
      }
      if (saved) return
      const next = systemTheme()
      applyTheme(next)
      setTheme(next)
    }
    mq.addEventListener('change', onSystemChange)
    return () => mq.removeEventListener('change', onSystemChange)
  }, [])

  const choose = (next) => {
    applyTheme(next)
    setTheme(next)
    try {
      localStorage.setItem(KEY, next)
    } catch {
      /* storage blocked */
    }
  }

  return (
    <div className="theme-switch" role="group" aria-label="Color theme">
      <button
        type="button"
        className="theme-switch__btn theme-switch__btn--light"
        aria-label="Light theme"
        aria-pressed={theme === null ? undefined : theme === 'light'}
        onClick={() => choose('light')}
      >
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
          <circle cx="12" cy="12" r="4.2" fill="currentColor" />
          <g stroke="currentColor" strokeWidth="2" strokeLinecap="round">
            <path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6" />
          </g>
        </svg>
      </button>
      <button
        type="button"
        className="theme-switch__btn theme-switch__btn--dark"
        aria-label="Dark theme"
        aria-pressed={theme === null ? undefined : theme === 'dark'}
        onClick={() => choose('dark')}
      >
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
          <path
            fill="currentColor"
            d="M20.2 14.6A8.5 8.5 0 0 1 9.4 3.8a.6.6 0 0 0-.8-.7A9.6 9.6 0 1 0 20.9 15.4a.6.6 0 0 0-.7-.8Z"
          />
        </svg>
      </button>
    </div>
  )
}
