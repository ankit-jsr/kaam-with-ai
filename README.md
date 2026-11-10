# KaamWithAI

Static publication hosted on https://kaamwithai.pages.dev/.

## Site structure
- `index.html`: homepage
- `articles/`: editorial articles
- `styles.css`: shared styles
- `sitemap.xml` and `robots.txt`: crawl discovery
- `scripts/validate_site.py`: local link, template and sitemap validation
- `.github/workflows/deploy.yml`: validation and Cloudflare deployment

## Publishing workflow
1. Create a branch for each content or site change.
2. Edit the HTML and related assets.
3. Run `python3 scripts/validate_site.py`.
4. Open a pull request; GitHub Actions validates it.
5. Review and merge to `main`.
6. GitHub Actions deploys `main` to the existing Cloudflare Pages project `kaamwithai`.

## Required GitHub Actions secrets
Add these under repository Settings → Secrets and variables → Actions:
- `CLOUDFLARE_API_TOKEN`: scoped to the Cloudflare account with Pages deployment permission.
- `CLOUDFLARE_ACCOUNT_ID`: Cloudflare account ID.

Never put secrets in source files, commits, issues or chat.

## Deployment architecture
The existing Cloudflare Pages project was created using Direct Upload, so it cannot be switched to Cloudflare's native Git integration in place. GitHub Actions can still deploy to that same Pages project using Wrangler, preserving the `kaamwithai.pages.dev` production URL.

## Editorial rules
- Do not invent first-hand testing, customers, statistics or results.
- Mark illustrative scenarios as illustrative.
- Prefer primary sources and original analysis.
- Don't publish shallow or near-duplicate pages merely to increase volume.
- Validate titles, canonical URLs, internal links, sitemap and mobile layout before merging.
