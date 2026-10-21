import { motion, useReducedMotion } from 'framer-motion'
import { wordReveal, stagger } from '../motion'

function Words({ text, className = '', delay = 0 }) {
  const parts = text.split(' ')
  return (
    <motion.span
      className={className}
      variants={stagger(0.08)}
      initial="hidden"
      animate="show"
      transition={{ delayChildren: delay }}
      style={{ display: 'inline' }}
    >
      {parts.map((w, i) => (
        <span
          key={`${w}-${i}`}
          className="hero-word"
          style={{
            display: 'inline-block',
            overflow: 'hidden',
            verticalAlign: 'top',
            marginRight: '0.28em',
            perspective: 900,
          }}
        >
          <motion.span
            style={{ display: 'inline-block', transformOrigin: '50% 100%' }}
            variants={wordReveal}
          >
            {w}
          </motion.span>
        </span>
      ))}
    </motion.span>
  )
}

export default function HeroTitle() {
  const reduce = useReducedMotion()
  if (reduce) {
    return (
      <h1 className="hero-title">
        Your Vision. Our Code. <span className="grad">Limitless Possibilities.</span>
      </h1>
    )
  }
  return (
    <h1 className="hero-title" style={{ perspective: 1000 }}>
      <Words text="Your Vision. Our Code." />
      <span className="grad">
        <Words text="Limitless Possibilities." delay={0.35} />
      </span>
    </h1>
  )
}
