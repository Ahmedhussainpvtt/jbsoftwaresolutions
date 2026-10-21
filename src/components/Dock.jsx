import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { AnimatePresence, motion } from 'framer-motion'

export default function Dock() {
  const [showTop, setShowTop] = useState(false)
  const [pad, setPad] = useState(0)

  useEffect(() => {
    const sync = () => {
      setShowTop(window.scrollY > 420)
      const vv = window.visualViewport
      if (!vv) {
        setPad(0)
        return
      }
      setPad(Math.max(0, Math.round(window.innerHeight - (vv.height + vv.offsetTop))))
    }
    sync()
    window.addEventListener('scroll', sync, { passive: true })
    window.addEventListener('resize', sync)
    window.visualViewport?.addEventListener('resize', sync)
    window.visualViewport?.addEventListener('scroll', sync)
    return () => {
      window.removeEventListener('scroll', sync)
      window.removeEventListener('resize', sync)
    }
  }, [])

  return (
    <motion.div
      className="sticky-dock"
      aria-label="Quick contact"
      style={{ '--dock-vv-pad': `${pad}px` }}
      initial={{ opacity: 0, y: 40, scale: 0.75, rotate: -4 }}
      animate={{ opacity: 1, y: 0, scale: 1, rotate: 0 }}
      transition={{ delay: 0.55, type: 'spring', stiffness: 260, damping: 14 }}
    >
      <AnimatePresence>
        {showTop && (
          <motion.button
            type="button"
            className="back-to-top is-visible"
            aria-label="Back to top"
            initial={{ opacity: 0, y: 12, scale: 0.85 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 10, scale: 0.9 }}
            whileHover={{ y: -3 }}
            whileTap={{ scale: 0.94 }}
            onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
            style={{ display: 'grid' }}
          >
            <span aria-hidden="true">↑</span>
            <span className="back-to-top-label">Top</span>
          </motion.button>
        )}
      </AnimatePresence>
      <motion.div whileHover={{ scale: 1.06 }} whileTap={{ scale: 0.94 }}>
        <Link className="dock-btn quote" to="/contact" aria-label="Contact us">
          Contact
        </Link>
      </motion.div>
    </motion.div>
  )
}
