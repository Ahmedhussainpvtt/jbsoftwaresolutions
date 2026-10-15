# JB Software Solutions

Static marketing site for [JB Software Solutions](https://ahmedhussainpvtt.github.io/jbsoftwaresolutions/).

## Deploy (GitHub Pages)

1. Repo Settings â†’ Pages â†’ Source: **Deploy from a branch**
2. Branch: `main` / folder: `/ (root)`
3. Site URL: `https://ahmedhussainpvtt.github.io/jbsoftwaresolutions/`

## Update contact

Edit phone, WhatsApp and email in `_build_pages.py`, then run:

```bash
py -3 _build_pages.py
```

Or search-replace across HTML for `info@jbsoftwaresolutions.com` and `+91 93811 07468`.

## Local preview

```bash
npx --yes serve .
```

Open the printed localhost URL (use the `/jbsoftwaresolutions` path only after Pages deploy; locally serve from this folder root).
