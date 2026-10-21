import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { copyFileSync, existsSync } from 'node:fs'
import { resolve, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = dirname(fileURLToPath(import.meta.url))

// Production: https://jbsoftwaresolutions.com/ (custom domain, Pages from gh-pages)
export default defineConfig({
  plugins: [
    react(),
    {
      name: 'spa-github-pages-404',
      closeBundle() {
        const index = resolve(root, 'dist/index.html')
        const fallback = resolve(root, 'dist/404.html')
        if (existsSync(index)) copyFileSync(index, fallback)
        for (const name of ['CNAME', '.nojekyll']) {
          const src = resolve(root, 'public', name)
          if (existsSync(src)) copyFileSync(src, resolve(root, 'dist', name))
        }
      },
    },
  ],
  base: '/',
})
