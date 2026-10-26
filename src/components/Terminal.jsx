import { useEffect, useState } from 'react'
import { motion, useReducedMotion } from 'framer-motion'
import { TERM_LINES } from '../data/site'
import { isFirstLoad } from '../firstLoad'

export default function Terminal() {
  const [count, setCount] = useState(0)
  const reduce = useReducedMotion()

  useEffect(() => {
    if (count >= TERM_LINES.length) return
    const t = setTimeout(() => setCount((c) => c + 1), count === 0 ? 320 : 420)
    return () => clearTimeout(t)
  }, [count])

  return (
    <motion.div
      className="ai-terminal"
      initial={isFirstLoad() ? false : { opacity: 0, y: 56, rotateX: 18, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, rotateX: 0, scale: 1 }}
      transition={{ delay: 0.28, duration: 0.95, ease: [0.16, 1, 0.3, 1] }}
      whileHover={
        reduce
          ? undefined
          : {
              y: -10,
              rotateX: -2,
              rotateY: 3,
              boxShadow: '0 28px 60px rgba(58, 208, 255, 0.28)',
              transition: { type: 'spring', stiffness: 260, damping: 16 },
            }
      }
      style={{ transformPerspective: 1100 }}
    >
      <div className="bar">
        {['#ff5f57', '#febc2e', '#28c840'].map((c, i) => (
          <span key={c} className="dot" style={{ background: c, '--dot-delay': `${i * 0.2}s` }} />
        ))}
      </div>
      <div className="term-out">
        {TERM_LINES.map((line, i) => (
          <motion.div
            key={line}
            initial={false}
            animate={
              i < count
                ? { opacity: 1, x: 0, filter: 'blur(0px)' }
                : { opacity: 0, x: -18, filter: 'blur(4px)' }
            }
            transition={{ duration: 0.4 }}
            style={{ marginBottom: 6 }}
            aria-hidden={i < count ? undefined : true}
          >
            {line}
          </motion.div>
        ))}
        <span className={`term-cursor${count < TERM_LINES.length ? '' : ' is-done'}`}>_</span>
      </div>
    </motion.div>
  )
}
