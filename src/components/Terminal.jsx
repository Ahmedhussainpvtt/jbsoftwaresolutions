import { useEffect, useState } from 'react'
import { motion, AnimatePresence, useReducedMotion } from 'framer-motion'
import { TERM_LINES } from '../data/site'

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
      initial={{ opacity: 0, y: 56, rotateX: 18, scale: 0.9 }}
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
          <motion.span
            key={c}
            className="dot"
            style={{ background: c }}
            animate={reduce ? undefined : { scale: [1, 1.25, 1] }}
            transition={{ duration: 1.6, delay: i * 0.2, repeat: Infinity }}
          />
        ))}
      </div>
      <div className="term-out">
        <AnimatePresence>
          {TERM_LINES.slice(0, count).map((line, i) => (
            <motion.div
              key={line}
              initial={{ opacity: 0, x: -18, filter: 'blur(4px)' }}
              animate={{ opacity: 1, x: 0, filter: 'blur(0px)' }}
              transition={{ duration: 0.4, delay: 0.02 * i }}
              style={{ marginBottom: 6 }}
            >
              {line}
            </motion.div>
          ))}
        </AnimatePresence>
        {count < TERM_LINES.length && (
          <motion.span
            animate={{ opacity: [1, 0.12, 1] }}
            transition={{ duration: 0.75, repeat: Infinity }}
          >
            _
          </motion.span>
        )}
      </div>
    </motion.div>
  )
}
