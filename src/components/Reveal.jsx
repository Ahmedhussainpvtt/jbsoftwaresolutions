import { motion, useReducedMotion } from 'framer-motion'
import { fadeUp } from '../motion'
import { isFirstLoad } from '../firstLoad'
import { useInHero } from './PageHero'

const TAGS = {
  div: motion.div,
  p: motion.p,
  h1: motion.h1,
  h2: motion.h2,
  h3: motion.h3,
  ul: motion.ul,
  li: motion.li,
  details: motion.details,
  article: motion.article,
  span: motion.span,
  section: motion.section,
  form: motion.form,
}

const STATIC = {
  div: 'div',
  p: 'p',
  h1: 'h1',
  h2: 'h2',
  h3: 'h3',
  ul: 'ul',
  li: 'li',
  details: 'details',
  article: 'article',
  span: 'span',
  section: 'section',
  form: 'form',
}

export default function Reveal({
  children,
  className = '',
  variants = fadeUp,
  delay = 0,
  as = 'div',
  once = true,
  amount = 0.22,
  whileHover,
  ...rest
}) {
  const reduce = useReducedMotion()
  const inHero = useInHero()
  const Tag = TAGS[as] || motion.div

  if (reduce) {
    const S = STATIC[as] || 'div'
    return (
      <S className={className} {...rest}>
        {children}
      </S>
    )
  }

  return (
    <Tag
      className={className}
      variants={variants}
      initial={inHero && isFirstLoad() ? false : 'hidden'}
      whileInView="show"
      viewport={{ once, amount, margin: '0px 0px -10% 0px' }}
      transition={{ delay }}
      whileHover={whileHover}
      {...rest}
    >
      {children}
    </Tag>
  )
}
