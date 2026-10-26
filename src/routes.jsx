// Inner pages ship as separate chunks. The current page's chunk is loaded
// before hydration (client) or before rendering (prerender), so the first
// render never suspends and matches the static HTML.
function lazyModule(load) {
  let mod = null
  let pending = null
  return {
    load() {
      if (!pending) pending = load().then((m) => (mod = m))
      return pending
    },
    get: () => mod,
  }
}

export const modules = {
  simple: lazyModule(() => import('./pages/SimplePage')),
  faq: lazyModule(() => import('./pages/FaqPages')),
  glossary: lazyModule(() => import('./pages/GlossaryPages')),
  service: lazyModule(() => import('./pages/ServicePage')),
}

export function moduleForPath(pathname = '/') {
  const p = pathname.replace(/^\/+/, '')
  if (p === '') return null
  if (p.startsWith('faq')) return modules.faq
  if (p.startsWith('glossary')) return modules.glossary
  if (p.startsWith('services/')) return modules.service
  return modules.simple
}

export const preloadAll = () => Promise.all(Object.values(modules).map((m) => m.load()))

export function Page({ mod, name = 'default', ...props }) {
  const m = mod.get()
  if (!m) throw mod.load()
  const C = m[name]
  return <C {...props} />
}
