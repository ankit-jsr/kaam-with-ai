# KaamWithAI SEO + AEO Growth Playbook

**Created:** 15 November 2026  
**Status:** Working strategy; repository-level technical review partly verified. Google Search Console work is paused at the user's explicit instruction and must not resume without explicit reopening.  
**Site:** https://kaamwithai.pages.dev/  
**Audience:** Small-business owners and operators who want practical, trustworthy ways to get work done with AI.

## Executive decision

KaamWithAI should grow as a specialist editorial publication about **how small businesses actually get work done**: workflows, handoffs, automation decisions, AI-assisted operations, controls and measurable outcomes.

Do not become a generic AI news or “best AI tools” site. Do not publish to a word-count quota. Do not chase AEO hacks. Build a recognisable body of original operator reporting and practical implementation guidance, supported by a technically clean site and a deliberate distribution/link-earning programme.

SEO and AEO are not separate content factories. One useful, well-sourced page should serve:
- the reader who arrives from a search query;
- the person who asks an AI assistant a specific operational question;
- the journalist, consultant or operator who may cite or share it.

Google's current guidance says AI Overviews and AI Mode have no special technical or schema requirements beyond ordinary Search eligibility and foundational SEO. Google specifically cautions against unnecessary AI text files, artificial chunking and inauthentic mentions. A page must be indexed and eligible for a snippet before it can appear as a supporting link in those Google AI experiences.

## What is confirmed in the repository

As checked on 15 November 2026:
- Homepage has `index,follow`, a self-referencing canonical, WebSite JSON-LD and direct HTML links to five articles.
- `site/robots.txt` allows all crawlers and points to `https://kaamwithai.pages.dev/sitemap.xml`.
- `site/sitemap.xml` lists homepage, about, privacy and five articles.
- Three inspected article pages have `index,follow`, self-referencing canonicals and Article JSON-LD.
- The About page exists and describes editorial standards, but currently has minimal publisher/author detail.
- The inspected article byline is “KaamWithAI Editorial”; no named editor profile or contributor biography was found in the inspected pages.
- The static HTML means article text is present in the source rather than dependent on client-side rendering.

These checks confirm repository configuration, not the actual HTTP response Googlebot receives. The live URLs could not be independently fetched through the current web inspection route. Verify status codes, headers, CDN/bot behaviour and rendered output separately.

## Google Search Console: paused by user

The user has explicitly asked us to leave Google Search Console alone. Until the user explicitly reopens this work, do not access or investigate the property, inspect reports, run URL Inspection or Live Test, request screenshots, submit or resubmit a sitemap, request indexing, or change any property or account setting.

The previously reported “quota exceeded” message is a historical, unverified symptom—not a diagnosed cause. If the user reopens this work, first distinguish sitemap fetch/processing status from the separate URL Inspection request quota. Do not repeat indexing requests as a substitute for diagnosis.

External website checks that do not access or change Search Console may continue where useful, but they must not be represented as evidence from Search Console.

## Current strategic diagnosis

### 1. New-site discovery and trust are likely constraints, but not yet a proven cause
The site has five articles and launched only days ago. Google says discovery and indexing can take days to weeks and are not guaranteed. This does not excuse a persistent sitemap fetch error; technical evidence must be gathered first.

### 2. The current article set is editorially coherent in philosophy, but broad in search intent
Current themes span AI agents, customer enquiry management, an Anthropic shop experiment, ChatGPT Business Hub and a solo event agency's AI back office. The common thread is practical AI, but the target query and reader are not yet sharply defined.

### 3. Publisher identity and authorship can be stronger
The current generic “KaamWithAI Editorial” byline and short About page provide little evidence of who is accountable for reporting and what qualifies them to interpret workflows. Do not invent an author or credentials. Add a real editor/contributor profile only with accurate information, relevant experience and clear responsibility. Explain the reporting method and distinguish self-reported stories from reproduced tests.

### 4. Originality must be the moat
A Reddit anecdote rewritten as an article is not enough by itself. The value must come from source checking, workflow reconstruction, counterexamples, controls, useful templates/checklists, expert input or reproducible testing. Clearly label self-reported claims and never imply independent verification.

## Editorial positioning

**Promise:** Practical reporting and field guides on how small businesses can make everyday work better with AI and automation—what works, what breaks, what should stay human, and how to measure it.

**Core reader:** owner-operators, solo professionals and small teams without a dedicated automation/IT function.

**Editorial territory:**
1. Customer and revenue operations: enquiry capture, follow-up, quoting, scheduling, customer communication.
2. Back-office operations: invoices, bookkeeping handoffs, reconciliation, document handling, reporting.
3. Workflow automation decisions: AI vs rules vs OCR vs integrations vs spreadsheets vs human process.
4. Safe AI operations: permissions, source-of-truth, approvals, audit trails, failure handling.
5. Tool implementation only when tied to a real job and specific user.

Avoid broad AI news, generic model roundups, thin “top 20 tools” pages, and unrelated trending topics.

## Search strategy for a young publication

### Keyword selection
For each candidate query, record:
- exact query and close variants;
- intent (informational, commercial investigation, transactional, navigational);
- target reader and job-to-be-done;
- current SERP format and dominant competitors;
- likely difficulty relative to a new domain;
- whether the query can lead to a real business outcome;
- unique evidence/experience we can add;
- target URL and supporting cluster.

Prioritise specific, low-competition, high-intent questions rather than high-volume generic terms. Use Search Console query data once available, Google autocomplete/related searches/PAA, Reddit/community language, competitor SERPs and keyword tools. Do not fabricate search volume or difficulty.

### Page architecture
Use one primary intent/keyword cluster per page. Do not create multiple near-duplicate pages for keyword variants. Create:
- a useful pillar page for a coherent workflow/topic;
- focused supporting pages for specific subproblems;
- contextual links both ways;
- a small “related guides” block on each relevant article.

### On-page checklist
- One descriptive H1 that serves the reader, not keyword stuffing.
- Title tag and meta description accurately describe the page and its search intent.
- Short, stable, human-readable URL.
- Intro quickly establishes the problem and audience without spoiling a narrative.
- Clear H2/H3 hierarchy based on real subquestions.
- Direct answer to the main question where appropriate, without flattening story-led reporting.
- Concrete examples, limitations, steps, decision criteria and failure modes.
- Primary sources linked close to claims; dates for time-sensitive product facts.
- Visible byline and accurate author/editor profile.
- Clear disclosure of self-reported, desk-researched, independently verified or reproduced status.
- Descriptive internal-link anchor text; link to related guides where genuinely useful.
- Image alt text that describes meaningful images; no decorative keyword stuffing.
- Article schema matching visible content, author, dates and canonical URL.
- No fabricated FAQ, review, HowTo or Person schema. Only add schema when the page visibly and accurately supports it.
- Check title/description, canonical, robots and rendered HTML before publishing.

## AEO / answer-engine readiness

Do not create a separate set of pages just for “AEO”. Make the useful content easy to understand, retrieve and cite.

For suitable how-to and explainer pages:
- State the answer clearly near the relevant question.
- Use descriptive question-style subheadings where they reflect real queries.
- Define terms in plain language.
- Give a concise answer, then the nuance, steps and evidence.
- Use tables for comparisons and decision rules where they genuinely help.
- Attribute claims and link to primary evidence.
- Include dates and version/availability context for changing products.
- Make author, publisher and methodology clear.
- Keep visible page text accessible in HTML.
- Use structured data that reflects visible page content.

For narrative field reports:
- Preserve the story and suspense.
- Add a clearly labelled “What this means for an operator” or practical takeaway section.
- Separate what the source reported from what we infer.
- Include counterevidence and limits.

Do not:
- add `llms.txt` expecting it to improve Google AI visibility;
- manufacture FAQ blocks solely for schema;
- mechanically chunk every paragraph into snippets;
- add fake author credentials or fake expert quotes;
- buy fake AI citations/mentions;
- use AI-generated content at scale without original work and fact-checking.

## First recommended topic cluster

Start with **customer enquiry and follow-up operations for small service businesses**. It is closer to a concrete business pain and commercial outcome than generic AI-agent content, and connects to the existing enquiry article.

Potential structure (validate queries and SERPs before drafting):
- Pillar: A practical enquiry-to-booking system for a small service business.
- Supporting: How to stop losing enquiries across WhatsApp, email and website forms.
- Supporting: A simple lead follow-up process when you have no CRM.
- Supporting: When a small business needs a CRM—and when a spreadsheet is enough.
- Supporting: How to draft follow-up messages with AI without sending incorrect promises.
- Supporting: How to measure enquiry response time, follow-up completion and lead conversion.

Second cluster candidate: **small-business finance admin and reconciliation workflows**, using the accountant examples as leads only. Do not present Reddit claims as verified case studies. Distinguish conventional automation from AI.

## Distribution and authority programme

Publishing is not distribution. Every substantial article should have a distribution plan:
1. LinkedIn Company Page post with a distinct angle, not just an article link.
2. Relevant community participation only where rules allow and the contribution is genuinely useful; no link dropping.
3. Outreach to named practitioners/associations/newsletters who may find the research useful. Ask for critique or expert input, not a backlink favour.
4. Original assets worth referencing: workflow diagrams, checklists, small datasets, decision trees, implementation templates.
5. Encourage sources/interviewees to review factual attribution where appropriate, without allowing them to control editorial conclusions.
6. Track referral visits and links earned.

Prioritise editorially earned links from relevant professional communities, associations, consultants, educators and small-business resources. Avoid paid link schemes, mass guest-post swaps, irrelevant directories and spam comments.

## Measurement system

Weekly:
- indexed URLs and sitemap status;
- crawl status / last crawl for key URLs;
- impressions, clicks, CTR, average position by query and page;
- pages with impressions but poor CTR;
- query clusters where the site appears;
- referring domains and quality/relevance of links;
- referral traffic and meaningful engagement;
- LinkedIn reach, page visits and link clicks if available.

Monthly:
- which topic clusters are earning impressions and citations;
- which pages need stronger evidence, better intent match or consolidation;
- whether distribution is producing relevant mentions and links;
- which content types produce useful business conversations or leads.

Do not use raw publishing volume, DR/DA, word count, or number of schema types as success metrics.

## 30-day execution plan

### Days 1–3: establish the non-GSC technical baseline
- Test live HTTP status, redirects, content type, robots.txt, sitemap XML and Cloudflare bot handling without accessing Search Console.
- Confirm host, canonical and sitemap URL consistency from the public site.
- If available, review server/CDN logs for crawler access; do not infer Googlebot identity from a user-agent string alone.
- Use Bing Webmaster Tools as a separate discovery channel only if already available and appropriate.
- Search Console diagnostics remain paused; do not request screenshots or indexing.

### Days 4–7: improve trust and structure
- Strengthen About/editorial methodology and accurate authorship.
- Add contextual internal links among the five existing articles where useful.
- Add a “related guides” component and breadcrumb navigation if it improves user navigation.
- Review sitemap freshness and only include canonical, indexable, useful URLs.
- Select the first query cluster using actual SERP review.

### Week 2: publish a strong pillar and first support page
- Build a useful, evidence-rich enquiry operations pillar connected to the existing article.
- Add a real downloadable checklist/template only if it provides utility.
- Conduct at least one practitioner interview or obtain a reproducible workflow example.

### Weeks 3–4: supporting depth and distribution
- Publish 2–3 tightly related supporting pages only if each addresses a distinct intent.
- Produce one original visual/checklist/data asset.
- Distribute through the Company Page and targeted practitioner outreach.
- Review non-GSC crawl, referral and distribution evidence. Revisit Search Console only if the user explicitly reopens it.

## Decisions and constraints
- Do not access or investigate Search Console, request screenshots, submit URLs or sitemaps, request indexing, or change settings until the user explicitly reopens the work.
- Do not buy a domain or migrate until the user selects/approves the domain. A custom domain is recommended for brand ownership and long-term continuity, not as a guaranteed ranking fix.
- Do not publish LinkedIn posts automatically. User manually posts to the Company Page.
- Website publishing can proceed through the established PR/validation/deployment workflow.
- Keep the editorial promise natural and reader-first. SEO should improve discovery of genuinely useful work, not dictate what the publication becomes.

## Core references reviewed (15 November 2026)

### Google
- Search crawling and indexing FAQ: https://developers.google.com/search/help/crawling-index-faq
- URL Inspection: https://support.google.com/webmasters/answer/9012289
- Ask Google to recrawl: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- AI features and website guidance: https://developers.google.com/search/docs/appearance/ai-features
- AI optimization guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide

### SEO practitioner / platform references
- Ahrefs, Topical Authority (1 June 2026): https://ahrefs.com/blog/topical-authority/
- Ahrefs, Keyword Strategy (updated 13 March 2026): https://ahrefs.com/blog/keyword-strategy/
- Ahrefs, Internal Links for SEO (updated 10 March 2026): https://ahrefs.com/blog/internal-links-for-seo/
- Semrush, Topic Clusters: https://www.semrush.com/blog/topic-clusters/
- Semrush, SEO Content: https://www.semrush.com/blog/seo-content/
- Yoast, Content Optimization: https://yoast.com/help/optimize-your-content-with-yoast-seo-sidebar/
- Yoast, Schema SEO: https://yoast.com/help/implementing-schema-with-yoast-seo/
- WordPress.com, SEO: https://wordpress.com/support/seo/
- Yotpo, Reviews and Organic Traffic: https://www.yotpo.com/blog/reviews-increase-organic-traffic/

Note: Vendor blogs contain product marketing and practitioner recommendations. Treat them as hypotheses and operating ideas, not Google's confirmed ranking factors. Validate tactics against Google documentation and our own performance data.
