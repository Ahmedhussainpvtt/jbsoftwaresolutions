import { lazy, Suspense, useEffect, useState } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import Header from './components/Header'
import Footer from './components/Footer'
import Dock from './components/Dock'
import ScrollProgress from './components/ScrollProgress'
import ScrollToTop from './components/ScrollToTop'
import { isFirstLoad, markLoaded } from './firstLoad'
import Home from './pages/Home'
import { modules, moduleForPath, Page } from './routes'
import { pageVariants } from './motion'
import './styles.css'
import './motion-extras.css'

const Decor = lazy(() => import('./components/Decor'))
const Seo = lazy(() => import('./seo/Seo'))

const { simple, faq, glossary, service } = modules

function useIdle() {
  const [ready, setReady] = useState(false)
  useEffect(() => {
    const go = () => setReady(true)
    if ('requestIdleCallback' in window) {
      const id = window.requestIdleCallback(go, { timeout: 3000 })
      return () => window.cancelIdleCallback(id)
    }
    const t = setTimeout(go, 1500)
    return () => clearTimeout(t)
  }, [])
  return ready
}

function prefetchFromLink(e) {
  const a = e.target instanceof Element ? e.target.closest('a[href^="/"]') : null
  if (a) moduleForPath(new URL(a.href).pathname)?.load()
}

export default function App() {
  const location = useLocation()
  const idle = useIdle()
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    markLoaded()
    setMounted(true)
    const opts = { passive: true }
    document.addEventListener('pointerover', prefetchFromLink, opts)
    document.addEventListener('touchstart', prefetchFromLink, opts)
    document.addEventListener('focusin', prefetchFromLink)
    return () => {
      document.removeEventListener('pointerover', prefetchFromLink, opts)
      document.removeEventListener('touchstart', prefetchFromLink, opts)
      document.removeEventListener('focusin', prefetchFromLink)
    }
  }, [])

  const [landing] = useState(location.pathname)
  useEffect(() => {
    if (location.pathname !== landing) document.documentElement.classList.remove('first-load')
  }, [location.pathname, landing])

  useEffect(() => {
    document.querySelectorAll('[data-seo-static]').forEach((el) => el.remove())
  }, [location.pathname])

  return (
    <>
      {mounted && (
        <Suspense fallback={null}>
          <Seo />
        </Suspense>
      )}
      <ScrollToTop />
      <ScrollProgress />
      {idle && (
        <Suspense fallback={null}>
          <Decor />
        </Suspense>
      )}
      <Header />
      <motion.main
        key={location.pathname}
        variants={pageVariants}
        initial={isFirstLoad() ? false : 'initial'}
        animate="animate"
      >
        <Suspense fallback={null}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="about" element={<Page mod={simple} name="About" />} />
            <Route path="pricing" element={<Page mod={simple} name="Pricing" />} />
            <Route path="contact" element={<Page mod={simple} name="Contact" />} />
            <Route path="blog" element={<Page mod={simple} name="BlogHub" />} />
            <Route path="privacy" element={<Page mod={simple} name="Privacy" />} />
            <Route path="terms" element={<Page mod={simple} name="Terms" />} />
            <Route path="faq" element={<Page mod={faq} name="FaqHub" />} />
            <Route path="faq/:slug" element={<Page mod={faq} name="FaqTopic" />} />
            <Route path="glossary" element={<Page mod={glossary} name="GlossaryHub" />} />
            <Route path="glossary/:slug" element={<Page mod={glossary} name="GlossaryTerm" />} />
            <Route path="services/:slug" element={<Page mod={service} name="ServiceRoute" />} />
            <Route path="*" element={<Page mod={simple} name="NotFound" />} />
          </Routes>
        </Suspense>
      </motion.main>
      <Footer />
      <Dock />
    </>
  )
}
