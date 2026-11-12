# KaamWithAI

Static publication hosted on https://kaamwithai.pages.dev/.

## Start here: durable project context

**Read [editorial/OPERATING_CONTEXT.md](editorial/OPERATING_CONTEXT.md) first when resuming work in a new ChatGPT conversation.** It records the audience, editorial standards, decisions, LinkedIn operating model, current status and handover instructions.

## Repository layout
- `site/`: files deployed to Cloudflare Pages
- `site/index.html`: homepage
- `site/articles/`: editorial articles
- `site/styles.css`: shared styles
- `site/sitemap.xml` and `site/robots.txt`: crawl discovery
- `editorial/research/`: research briefs and source notes
- `editorial/drafts/`: unpublished article drafts
- `editorial/distribution/`: social drafts, calendar and performance log
- `scripts/validate_site.py`: local link, template and sitemap validation
- `.github/workflows/deploy.yml`: pull-request validation, preview deploys and production deploys

## Publishing workflow
1. Create a branch for each content or site change.
2. Edit files under `site/`.
3. Run `python3 scripts/validate_site.py`.
4. Open a pull request to `main`. Automated validation and a Cloudflare preview deployment run.
5. Review the preview and merge the pull request.
6. A passing change merged to `main` deploys to the existing Cloudflare Pages project `kaamwithai`.

## One-time Cloudflare credentials
In Cloudflare, create a **Custom API Token** with:
- Account permission: **Cloudflare Pages — Edit**
- Scope it to the Cloudflare account that owns the Pages project.

Find the Account ID in the Cloudflare dashboard's account overview.

In this GitHub repository, open Settings → Secrets and variables → Actions and add:
- `CLOUDFLARE_API_TOKEN`: the new token value
- `CLOUDFLARE_ACCOUNT_ID`: the account ID

Do not put secrets in source files, commits, issues or chat. Do not paste the API token here.

## Deployment architecture
The existing Pages project was created using Direct Upload, so it cannot be switched to native Cloudflare Git integration in place. GitHub Actions deploys the `site/` folder to that same Pages project using Wrangler. This preserves the `kaamwithai.pages.dev` URL.

## Editorial rules
- Do not invent first-hand testing, customers, statistics or results.
- Mark illustrative scenarios as illustrative.
- Prefer primary sources and original analysis.
- Don't publish shallow or near-duplicate pages merely to increase volume.
- Validate titles, canonical URLs, internal links, sitemap and mobile layout before merging.
