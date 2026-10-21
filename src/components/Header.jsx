import { useEffect, useState } from 'react'
import { Link, NavLink, useLocation } from 'react-router-dom'
import { AnimatePresence, motion } from 'framer-motion'
import { SERVICES, RESOURCES, asset } from '../data/site'

export default function Header() {
  const [scrolled, setScrolled] = useState(false)
  const [open, setOpen] = useState(false)
  const [servicesOpen, setServicesOpen] = useState(false)
  const [resourcesOpen, setResourcesOpen] = useState(false)
  const loc = useLocation()
  const homeHref = import.meta.env.BASE_URL || '/'

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  useEffect(() => {
    setOpen(false)
    setServicesOpen(false)
    setResourcesOpen(false)
  }, [loc.pathname])

  return (
    <motion.header
      className={`site-header${scrolled ? ' is-scrolled' : ''}`}
      initial={{ y: -80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
    >
      <div className="container nav">
        <a className="logo" href={homeHref}>
          <motion.img
            src={asset('logo-mark.png')}
            width="44"
            height="44"
            alt="JB Software Solutions logo"
            whileHover={{ rotate: 8, scale: 1.08 }}
            transition={{ type: 'spring', stiffness: 300, damping: 16 }}
          />
          <span>
            JB Software<em>Solutions</em>
          </span>
        </a>
        <button
          className="nav-toggle"
          type="button"
          aria-label="Open menu"
          aria-expanded={open}
          onClick={() => setOpen((v) => !v)}
        >
          Menu
        </button>
        <ul className={`nav-links${open ? ' is-open' : ''}`}>
          <li className={`has-dropdown${servicesOpen ? ' is-open' : ''}`}>
            <button
              type="button"
              className="nav-drop-toggle"
              aria-expanded={servicesOpen}
              onClick={() => {
                setServicesOpen((v) => !v)
                setResourcesOpen(false)
              }}
            >
              Services <span className="nav-chev" aria-hidden="true" />
            </button>
            <AnimatePresence>
              {servicesOpen && (
                <motion.ul
                  className="nav-dropdown"
                  role="menu"
                  initial={{ opacity: 0, y: 12, scale: 0.96, filter: 'blur(6px)' }}
                  animate={{ opacity: 1, y: 0, scale: 1, filter: 'blur(0px)' }}
                  exit={{ opacity: 0, y: 8, scale: 0.97, filter: 'blur(4px)' }}
                  transition={{ duration: 0.28, ease: [0.22, 1, 0.36, 1] }}
                  style={{ display: 'grid' }}
                >
                  {SERVICES.map((s, i) => (
                    <motion.li
                      key={s.slug}
                      initial={{ opacity: 0, x: -10 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 0.04 * i }}
                    >
                      <Link to={`/services/${s.slug}`}>
                        <span className="nav-drop-title">{s.title}</span>
                        <span className="nav-drop-desc">{s.desc}</span>
                      </Link>
                    </motion.li>
                  ))}
                </motion.ul>
              )}
            </AnimatePresence>
          </li>
          <li className={`has-dropdown${resourcesOpen ? ' is-open' : ''}`}>
            <button
              type="button"
              className="nav-drop-toggle"
              aria-expanded={resourcesOpen}
              onClick={() => {
                setResourcesOpen((v) => !v)
                setServicesOpen(false)
              }}
            >
              Resources <span className="nav-chev" aria-hidden="true" />
            </button>
            <AnimatePresence>
              {resourcesOpen && (
                <motion.ul
                  className="nav-dropdown"
                  role="menu"
                  initial={{ opacity: 0, y: 12, scale: 0.96, filter: 'blur(6px)' }}
                  animate={{ opacity: 1, y: 0, scale: 1, filter: 'blur(0px)' }}
                  exit={{ opacity: 0, y: 8, scale: 0.97, filter: 'blur(4px)' }}
                  transition={{ duration: 0.28, ease: [0.22, 1, 0.36, 1] }}
                  style={{ display: 'grid' }}
                >
                  {RESOURCES.map((r, i) => (
                    <motion.li
                      key={r.to}
                      initial={{ opacity: 0, x: -10 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 0.04 * i }}
                    >
                      <Link to={r.to.replace(/\/$/, '') || '/'}>
                        <span className="nav-drop-title">{r.title}</span>
                        <span className="nav-drop-desc">{r.desc}</span>
                      </Link>
                    </motion.li>
                  ))}
                </motion.ul>
              )}
            </AnimatePresence>
          </li>
          <li>
            <NavLink to="/pricing">Pricing</NavLink>
          </li>
          <li>
            <NavLink to="/about">About</NavLink>
          </li>
          <li>
            <NavLink className="nav-cta" to="/contact">
              Get a quote
            </NavLink>
          </li>
        </ul>
      </div>
    </motion.header>
  )
}
