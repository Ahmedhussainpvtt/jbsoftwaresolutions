import { motion } from 'framer-motion'
import useMotionTier from '../hooks/useMotionTier'

export default function Aurora() {
  const tier = useMotionTier()
  if (tier !== 'full') return null

  return (
    <div className="aurora" aria-hidden="true">
      <motion.span
        className="aurora-beam aurora-a"
        animate={{ x: ['-20%', '30%', '-10%'], rotate: [0, 12, -6, 0], opacity: [0.35, 0.55, 0.3] }}
        transition={{ duration: 18, repeat: Infinity, ease: 'easeInOut' }}
      />
      <motion.span
        className="aurora-beam aurora-b"
        animate={{ x: ['10%', '-25%', '15%'], rotate: [0, -10, 8, 0], opacity: [0.25, 0.45, 0.28] }}
        transition={{ duration: 22, repeat: Infinity, ease: 'easeInOut' }}
      />
      <motion.span
        className="aurora-beam aurora-c"
        animate={{ y: ['0%', '18%', '-8%', '0%'], opacity: [0.15, 0.35, 0.18] }}
        transition={{ duration: 16, repeat: Infinity, ease: 'easeInOut' }}
      />
      <div className="noise-grain" />
    </div>
  )
}
