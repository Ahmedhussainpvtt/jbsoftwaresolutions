export const easeOut = [0.16, 1, 0.3, 1]
export const easeExpo = [0.19, 1, 0.22, 1]
export const springSoft = { type: 'spring', stiffness: 140, damping: 16, mass: 0.7 }
export const springSnappy = { type: 'spring', stiffness: 320, damping: 20, mass: 0.55 }
export const springBouncy = { type: 'spring', stiffness: 420, damping: 14, mass: 0.5 }

export const pageVariants = {
  initial: { opacity: 0, y: 48, scale: 0.985, filter: 'blur(12px)' },
  animate: {
    opacity: 1,
    y: 0,
    scale: 1,
    filter: 'blur(0px)',
    transition: { duration: 0.65, ease: easeExpo },
  },
  exit: {
    opacity: 0,
    y: -28,
    scale: 0.99,
    filter: 'blur(10px)',
    transition: { duration: 0.32, ease: 'easeIn' },
  },
}

export const fadeUp = {
  hidden: { opacity: 0, y: 56, scale: 0.96, filter: 'blur(6px)' },
  show: {
    opacity: 1,
    y: 0,
    scale: 1,
    filter: 'blur(0px)',
    transition: { duration: 0.8, ease: easeOut },
  },
}

export const fadeLeft = {
  hidden: { opacity: 0, x: -64, rotate: -1.5, filter: 'blur(4px)' },
  show: {
    opacity: 1,
    x: 0,
    rotate: 0,
    filter: 'blur(0px)',
    transition: { duration: 0.85, ease: easeOut },
  },
}

export const fadeRight = {
  hidden: { opacity: 0, x: 64, rotate: 1.5, filter: 'blur(4px)' },
  show: {
    opacity: 1,
    x: 0,
    rotate: 0,
    filter: 'blur(0px)',
    transition: { duration: 0.85, ease: easeOut },
  },
}

export const scaleIn = {
  hidden: { opacity: 0, scale: 0.78, rotate: -4, y: 24 },
  show: {
    opacity: 1,
    scale: 1,
    rotate: 0,
    y: 0,
    transition: springSoft,
  },
}

export const popIn = {
  hidden: { opacity: 0, scale: 0.5, y: 20 },
  show: {
    opacity: 1,
    scale: 1,
    y: 0,
    transition: springBouncy,
  },
}

export const stagger = (delay = 0.07) => ({
  hidden: {},
  show: {
    transition: { staggerChildren: delay, delayChildren: 0.08 },
  },
})

export const wordReveal = {
  hidden: { y: '120%', opacity: 0, rotateX: 55, scale: 0.92 },
  show: {
    y: '0%',
    opacity: 1,
    rotateX: 0,
    scale: 1,
    transition: { duration: 0.72, ease: easeExpo },
  },
}

export const charReveal = {
  hidden: { y: '110%', opacity: 0, rotateY: 40 },
  show: {
    y: '0%',
    opacity: 1,
    rotateY: 0,
    transition: { duration: 0.55, ease: easeOut },
  },
}

export const cardHover = {
  rest: { y: 0, scale: 1, rotateX: 0, rotateY: 0 },
  hover: {
    y: -14,
    scale: 1.035,
    transition: springSnappy,
  },
}

export const glowPulse = {
  animate: {
    boxShadow: [
      '0 14px 40px rgba(61, 255, 122, 0.28)',
      '0 22px 70px rgba(58, 208, 255, 0.55)',
      '0 18px 50px rgba(255, 154, 31, 0.35)',
      '0 14px 40px rgba(61, 255, 122, 0.28)',
    ],
    transition: { duration: 3.2, repeat: Infinity, ease: 'easeInOut' },
  },
}

export const floatY = (amp = 14, dur = 5) => ({
  animate: {
    y: [0, -amp, 0, amp * 0.6, 0],
    transition: { duration: dur, repeat: Infinity, ease: 'easeInOut' },
  },
})
