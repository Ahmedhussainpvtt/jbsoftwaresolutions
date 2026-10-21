import { motion } from 'framer-motion'
import useMotionTier from '../hooks/useMotionTier'

export default function ScrollMarquee({ items }) {
  const tier = useMotionTier()
  const doubled = [...items, ...items]
  if (tier === 'off') {
    return (
      <div className="marquee" aria-hidden="true">
        <div className="marquee-track" style={{ display: 'flex', gap: '2.5rem' }}>
          {items.map((t) => (
            <span key={t}>{t}</span>
          ))}
        </div>
      </div>
    )
  }

  return (
    <div className="scroll-marquees" aria-hidden="true">
      <div className="marquee marquee-scroll">
        <motion.div
          className="marquee-track"
          style={{ display: 'flex', width: 'max-content', gap: '2.5rem' }}
          animate={{ x: ['0%', '-50%'] }}
          transition={{ duration: tier === 'lite' ? 40 : 28, repeat: Infinity, ease: 'linear' }}
        >
          {doubled.map((t, i) => (
            <span key={`a-${t}-${i}`}>{t}</span>
          ))}
        </motion.div>
      </div>
      {tier === 'full' && (
        <div className="marquee marquee-scroll marquee-reverse">
          <motion.div
            className="marquee-track"
            style={{ display: 'flex', width: 'max-content', gap: '2.5rem' }}
            animate={{ x: ['-50%', '0%'] }}
            transition={{ duration: 38, repeat: Infinity, ease: 'linear' }}
          >
            {doubled.map((t, i) => (
              <span key={`b-${t}-${i}`}>{t}</span>
            ))}
          </motion.div>
        </div>
      )}
    </div>
  )
}
