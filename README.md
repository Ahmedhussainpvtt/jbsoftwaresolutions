# JB Software Solutions

Static marketing site for [jbsoftwaresolutions.com](https://jbsoftwaresolutions.com/).

## SEO pipeline (same as Easy Peeze / Kharch Log)

Every push regenerates crawl artifacts before git:

1. `seo-build.js` + `seo.config.js` → page meta / canonical / OG / JSON-LD + `sitemap.xml` + `robots.txt` (+ `sitemaps.xml` / `robot.txt` aliases)
2. `generate-llms-txt.py` → `llms.txt` + `llms-full.txt` + `LLM.txt`

```bash
npm run seo          # meta + sitemap + robots
npm run llms         # llms.txt corpus from sitemap
npm run build        # pages + seo + llms
npm run push         # full gate then git push to main / Pages
```

Or:

```powershell
.\push-jb-website.ps1 -Message "Your message"
```

## Contact

- Email: info@jbsoftwaresolutions.com
- Public site routes visitors to the contact form (no phone listed)

## Local preview

```bash
npx --yes serve .
```
