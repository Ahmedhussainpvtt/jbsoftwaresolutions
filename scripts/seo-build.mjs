/**
 * After Vite build: emit crawlable HTML for every route + sitemap/robots/llms.
 * Each page gets full meta/keywords/OG/JSON-LD and a #seo-static content block
 * that React removes on hydrate (crawlers still see the HTML).
 */
import { readFileSync, writeFileSync, mkdirSync, copyFileSync, existsSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const dist = join(root, 'dist')

const { allSeoRoutes, metaForPath } = await import(pathToFileURL(join(root, 'src/seo/pageMeta.js')).href)
const ssrEntry = join(root, 'dist-ssr', 'entry-server.js')
const { render, preloadAll } = existsSync(ssrEntry) ? await import(pathToFileURL(ssrEntry).href) : { render: null }
if (preloadAll) await preloadAll()

const SITE = 'https://jbsoftwaresolutions.com'
const template = optimizeShell(readFileSync(join(dist, 'index.html'), 'utf8'))

// Inline the stylesheet (one fewer render-blocking request) and start the app
// bundle after `load`, so the prerendered HTML paints without competing for bandwidth.
function optimizeShell(html) {
  let out = html.replace(/<link rel="stylesheet"[^>]*href="([^"]+\.css)"[^>]*>/g, (_, href) => {
    const css = readFileSync(join(dist, href.replace(/^\//, '')), 'utf8')
    return `<style>${css.replace(/<\/style/gi, '<\\/style')}</style>`
  })
  const preloads = []
  out = out.replace(/<link rel="modulepreload"[^>]*href="([^"]+)"[^>]*>\s*/g, (_, href) => {
    preloads.push(href)
    return ''
  })
  out = out.replace(/<script type="module" crossorigin src="([^"]+)"><\/script>/, (_, src) => {
    const deps = JSON.stringify(preloads)
    const loader = `(function(){var started=0;function go(){if(started++)return;${deps}.forEach(function(h){var l=document.createElement('link');l.rel='modulepreload';l.href=h;document.head.appendChild(l)});var s=document.createElement('script');s.type='module';s.crossOrigin='';s.src='${src}';document.head.appendChild(s)}function afterPaint(){try{new PerformanceObserver(function(l){if(l.getEntriesByName('first-contentful-paint').length)setTimeout(go,0)}).observe({type:'paint',buffered:true})}catch(e){go()}setTimeout(go,3000)}if(document.readyState==='complete')afterPaint();else addEventListener('load',afterPaint)})()`
    return `<script>${loader}</script>`
  })
  return out
}

function inject(html, meta, appHtml = '') {
  let out = html

  // Replace core head tags
  out = out.replace(/<title>[^<]*<\/title>/, `<title>${esc(meta.title)}</title>`)
  out = out.replace(
    /<meta name="description" content="[^"]*"\s*\/?>/,
    `<meta name="description" content="${escAttr(meta.desc)}" />`,
  )
  if (/name="keywords"/.test(out)) {
    out = out.replace(
      /<meta name="keywords" content="[^"]*"\s*\/?>/,
      `<meta name="keywords" content="${escAttr(meta.keywords)}" />`,
    )
  } else {
    out = out.replace(
      '</title>',
      `</title>\n    <meta name="keywords" content="${escAttr(meta.keywords)}" />`,
    )
  }
  if (/rel="canonical"/.test(out)) {
    out = out.replace(/<link rel="canonical" href="[^"]*"\s*\/?>/, `<link rel="canonical" href="${meta.canonical}" />`)
  } else {
    out = out.replace('</title>', `</title>\n    <link rel="canonical" href="${meta.canonical}" />`)
  }
  out = out.replace(/property="og:title" content="[^"]*"/, `property="og:title" content="${escAttr(meta.title)}"`)
  out = out.replace(/property="og:description" content="[^"]*"/, `property="og:description" content="${escAttr(meta.desc)}"`)
  out = out.replace(/property="og:url" content="[^"]*"/, `property="og:url" content="${meta.canonical}"`)
  out = out.replace(/name="twitter:title" content="[^"]*"/, `name="twitter:title" content="${escAttr(meta.title)}"`)
  out = out.replace(
    /name="twitter:description" content="[^"]*"/,
    `name="twitter:description" content="${escAttr(meta.desc)}"`,
  )

  // Strip old json-ld then append fresh
  out = out.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/g, '')
  const ld = (meta.jsonld || [])
    .map((b) => `<script type="application/ld+json">\n${JSON.stringify(b, null, 2)}\n</script>`)
    .join('\n')
  out = out.replace('</head>', `  ${ld}\n  </head>`)

  const crawl = `<section id="seo-static" data-seo-static="1">${meta.crawlHtml || ''}</section>`
  if (out.includes('id="root"')) {
    out = out.replace(/<div id="root"><\/div>/, () => `<div id="root">${appHtml}</div>\n    ${crawl}`)
  } else {
    out = out.replace('</body>', `    ${crawl}\n  </body>`)
  }
  return out
}

function esc(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}
function escAttr(s) {
  return esc(s).replace(/"/g, '&quot;')
}

function outPathFor(route) {
  if (route === '/') return join(dist, 'index.html')
  const clean = route.replace(/^\//, '').replace(/\/$/, '')
  const dir = join(dist, clean)
  mkdirSync(dir, { recursive: true })
  return join(dir, 'index.html')
}

const routes = allSeoRoutes()
let written = 0
for (const route of routes) {
  const meta = metaForPath(route)
  const appHtml = render ? render(route === '/' ? '/' : `${route.replace(/\/$/, '')}/`) : ''
  const html = inject(template, meta, appHtml)
  writeFileSync(outPathFor(route), html, 'utf8')
  written += 1
}

// SPA fallback: no prerendered markup, the client renders whatever route it lands on
writeFileSync(join(dist, '404.html'), inject(template, metaForPath('/')), 'utf8')

// Sitemap
const today = new Date().toISOString().slice(0, 10)
const urls = routes.map((r) => {
  const loc = r === '/' ? `${SITE}/` : `${SITE}${r}/`
  const priority = r === '/' ? '1.0' : r.split('/').length <= 2 ? '0.8' : '0.6'
  return `  <url>\n    <loc>${loc}</loc>\n    <lastmod>${today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>${priority}</priority>\n  </url>`
})
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.join('\n')}\n</urlset>\n`
writeFileSync(join(dist, 'sitemap.xml'), sitemap, 'utf8')
writeFileSync(join(dist, 'sitemaps.xml'), sitemap, 'utf8')

const robots = `User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

Sitemap: ${SITE}/sitemap.xml
`
writeFileSync(join(dist, 'robots.txt'), robots, 'utf8')
writeFileSync(join(dist, 'robot.txt'), robots, 'utf8')

const llms = [
  `# ${SITE.replace('https://', '')}`,
  '',
  `> JB Software Solutions - custom software, websites, mobile apps, SEO, AEO, GEO.`,
  '',
  '## Pages',
  ...routes.map((r) => `- ${r === '/' ? SITE + '/' : SITE + r + '/'}`),
  '',
].join('\n')
writeFileSync(join(dist, 'llms.txt'), llms, 'utf8')
writeFileSync(join(dist, 'LLM.txt'), llms, 'utf8')
writeFileSync(join(dist, 'llms-full.txt'), llms, 'utf8')

for (const name of ['CNAME', '.nojekyll']) {
  const src = join(root, 'public', name)
  if (existsSync(src)) copyFileSync(src, join(dist, name))
}

console.log(`SEO build: wrote ${written} HTML pages + sitemap (${routes.length} urls)`)
