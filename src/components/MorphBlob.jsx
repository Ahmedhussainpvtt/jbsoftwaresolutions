import { motion } from 'framer-motion'
import useMotionTier from '../hooks/useMotionTier'

export default function MorphBlob() {
  const tier = useMotionTier()
  if (tier !== 'full') return null

  return (
    <motion.svg
      className="morph-blob"
      viewBox="0 0 600 600"
      aria-hidden="true"
      animate={{ rotate: [0, 20, -12, 0] }}
      transition={{ duration: 28, repeat: Infinity, ease: 'easeInOut' }}
    >
      <defs>
        <linearGradient id="blobGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#3dff7a" stopOpacity="0.45" />
          <stop offset="50%" stopColor="#3ad0ff" stopOpacity="0.35" />
          <stop offset="100%" stopColor="#ff9a1f" stopOpacity="0.3" />
        </linearGradient>
      </defs>
      <motion.path
        fill="url(#blobGrad)"
        animate={{
          d: [
            'M320,80 C430,90 520,180 530,290 C540,410 450,520 320,540 C190,560 80,460 70,320 C60,190 180,70 320,80 Z',
            'M300,60 C450,70 560,200 540,330 C520,470 390,560 260,540 C130,520 50,390 70,250 C90,110 180,50 300,60 Z',
            'M340,90 C460,120 510,240 500,360 C490,480 370,550 240,520 C110,490 70,350 100,220 C130,90 230,60 340,90 Z',
            'M320,80 C430,90 520,180 530,290 C540,410 450,520 320,540 C190,560 80,460 70,320 C60,190 180,70 320,80 Z',
          ],
        }}
        transition={{ duration: 14, repeat: Infinity, ease: 'easeInOut' }}
      />
    </motion.svg>
  )
}
