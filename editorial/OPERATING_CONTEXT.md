# KaamWithAI — Operating Context

**Last updated:** 13 November 2026  
**Purpose:** Durable handover and source of truth for work across ChatGPT conversations. Read this before making project decisions or asking the user to repeat context.

## 1. Project

KaamWithAI is a content-led publication/business helping small-business owners use AI in practical everyday work.

- Website: https://kaamwithai.pages.dev/
- GitHub repository: https://github.com/ankit-jsr/kaam-with-ai
- Audience: non-technical small-business owners and operators.
- Editorial promise: useful, grounded explanations and practical workflows; no AI hype, generic copy or unsupported claims.
- Primary publishing destination for social distribution: **KaamWithAI LinkedIn Company Page only**. Do not publish to the user's personal LinkedIn profile.
- The user is currently publishing LinkedIn posts manually. Do not schedule or publish on their behalf.

## 2. How to work with the user

- The user expects autonomous execution and continuity, not repeated questions or generic progress updates.
- Preserve decisions and project state here and in the relevant project files so a new conversation can resume without asking for context again.
- Before asking a question, inspect this file, README, relevant editorial files and recent repository state.
- Be candid about what is verified, drafted, committed, deployed, published or merely proposed.
- Do not claim a change is on GitHub unless the file/commit is confirmed.
- Do not claim a social post is live unless the user confirms it or provides its URL.
- When a task is clear and authorised, execute it. Ask only for genuinely blocking decisions or approvals.

## 3. Editorial standards

- Write for a small-business owner, not an AI enthusiast or technical audience.
- Lead with a recognisable business problem, useful tension or surprising fact.
- Be specific. Explain what a tool can and cannot do, who can access it, limitations and practical implications.
- Prefer primary sources and original analysis. Verify time-sensitive product claims immediately before publication.
- Never invent first-hand testing, customer stories, business outcomes, statistics or quotes.
- Label illustrative examples as illustrative.
- Avoid generic AI-sounding openings, breathless claims, filler and shallow listicles.
- For narrative articles, build the story. Do not reveal the entire payoff in the first fold or headline/deck.
- Do not publish near-duplicate pieces simply to increase volume.
- Every article/post should have a clear reader benefit and a reason to exist.

## 4. LinkedIn operating system

### Destination and workflow

- Destination: KaamWithAI Company Page only.
- Manual workflow: assistant researches, plans, drafts and maintains the library; user reviews, copies and posts.
- No LinkedIn automation or auto-publishing until the manual experiment demonstrates value and the user explicitly decides to automate.
- Never post to the user's personal profile.

### Cadence

- Initial target: approximately **3 posts per week**, not a rigid quota.
- Quality and relevance take priority. Some days should have no post.
- Each morning, decide whether a post is warranted that day based on the editorial queue, timely developments, audience usefulness and recent coverage.
- Avoid posting multiple versions of the same idea or repeating an angle too soon.

### Daily delivery

On a recommended posting day, give the user:
1. The complete, ready-to-copy post.
2. The strategic angle and intended audience response.
3. Suggested format (text, image, carousel, link, etc.) and asset needs.
4. Why this topic is timely or useful.
5. Any factual/source caveat that needs attention.

On a non-posting day, explicitly say no post is recommended and briefly explain why. Do not manufacture filler.

### Library and status tracking

Maintain LinkedIn distribution records under `editorial/distribution/`. For each item, track:
- unique ID or date;
- topic and angle;
- status: idea / researched / drafted / ready / posted / retired;
- final copy and source links;
- recommended format;
- posting date and Company Page URL once supplied by user;
- performance metrics if supplied (impressions, reactions, comments, reposts, clicks, follows, visits);
- learning and follow-up action.

When the user says a post is live, update the library. Ask for its URL only if useful and not already provided. Never infer that a post went live from a draft being sent.

### Measurement

Run an initial 30-day manual experiment. Evaluate:
- reach/impressions;
- meaningful engagement (comments, shares, saves if available);
- Company Page visits and follower growth;
- website clicks/referrals where measurable;
- quality of audience and conversations, not vanity metrics alone.

Use results to adjust topics, hooks, format and cadence. Do not overreact to one post.

## 5. Current LinkedIn content state (13 Nov 2026)

A set of three draft posts about OpenAI Business Hub / Business Agents exists:
- `editorial/distribution/2026-11-linkedin-drafts.md`
- Status: editorial drafts only; **not scheduled or published**.
- Topics: (1) profile vs product feed vs Business Agent distinction, (2) practical business information audit, (3) current boundaries of Business Agents.
- These claims were based on a research brief and must be rechecked against current official documentation before posting because product availability and policy can change.

The broader article draft is:
- `editorial/drafts/chatgpt-business-hub-small-business.md`
- Status: draft, not approved/published.

Other recent LinkedIn activity:
- A Make vs n8n vs manual publishing discussion took place.
- Decision: start manually. Revisit automation only after learning from the content experiment.
- Metricool was checked; only YouTube was connected, not LinkedIn. Do not use Metricool for LinkedIn unless the correct Company Page is connected.
- No Make or n8n workflow has been created.

## 6. Current website and repository structure

- `site/`: deployed static website.
- `site/index.html`: homepage.
- `site/articles/`: published articles.
- `editorial/research/`: research briefs and source notes.
- `editorial/drafts/`: unpublished article drafts.
- `editorial/distribution/`: social drafts, calendar and performance log.
- `scripts/validate_site.py`: site validation.
- `.github/workflows/deploy.yml`: validation and Cloudflare Pages deployment.

Website URL: https://kaamwithai.pages.dev/

Publishing website changes follows README instructions: branch, edit, validate, PR, preview, review and merge. Do not conflate website publication with LinkedIn publication.

## 7. Current automation

The existing **KaamWithAI Daily OS** automation has been updated to include LinkedIn planning and manual distribution responsibilities. It should:
- review repository/project state and outstanding commitments;
- maintain the LinkedIn library;
- choose whether today is a posting day;
- prepare a ready-to-copy post on posting days, or recommend no post when appropriate;
- never publish or schedule posts;
- provide a concise morning brief with priorities, completed work and true blockers.

The automation prompt is an execution instruction, not a substitute for this repository record. Update both when durable operating decisions change.

## 8. How to resume in a new conversation

Start by reading:
1. `editorial/OPERATING_CONTEXT.md` (this file);
2. `README.md`;
3. the latest files in `editorial/distribution/`;
4. relevant current research/drafts and recent commits.

Then state only genuinely important changes since the last handover. Continue the work; do not ask the user to restate the project, audience, channel, cadence or manual-posting decision.

## 9. Change log

- **13 Nov 2026:** Established manual LinkedIn operating model for KaamWithAI Company Page only; initial target around three posts/week; assistant owns editorial selection and library; user manually reviews and publishes; 30-day learning experiment before considering automation.
- **13 Nov 2026:** Recorded existing Business Hub LinkedIn drafts and current publishing/tool status.


## 10. Latest operating update — 13 November 2026

### LinkedIn publication and distribution

- **Post #1** was published on 10 November 2026. Its angle was the administrative burden of running a small business and the practical value of a first AI agent. The article link `https://kaamwithai.pages.dev/articles/first-ai-agent-small-business` was placed in the first comment after LinkedIn flagged the URL in the post body. Exact final copy and post URL were not preserved; no performance metrics supplied.
- **Post #2** was confirmed live by the user on 13 November 2026. It covered OpenAI Businesses in ChatGPT and the need to make business information accurate before building an agent. The user's screenshot showed 0 followers shortly after publication; this is not a post-performance metric. Post URL and analytics not supplied.
- The durable log is now `editorial/distribution/2026-11-linkedin-content-library.md`. It tracks both published posts, old drafts, the rolling queue and performance data.
- The earlier Business Hub information-audit draft overlaps with post #2 and should not be repeated. The separate Business Agent-boundaries draft is on hold pending a future need and fresh fact-check.
- The user reports that the Company Page is not appearing in LinkedIn search. The direct public Page URL is not yet recorded; obtain it before attempting a precise Page audit or adding the LinkedIn Follow link to the website.
- No further post is recommended on 13 November because post #2 was just published. The next candidate is a Reddit-sourced operator story about a staff accountant using ChatGPT to write VBA macros, targeted for 16 November if the final copy is sound.
- Research saved to `editorial/research/linkedin-company-page-growth-0-to-100-2026-11-13.md`.

### Reddit Operator Radar

- A recurring research programme has been started in `editorial/research/operator-radar-2026-11-13.md`.
- Best current leads: a staff accountant using ChatGPT to write VBA macros for reconciliations; a fractional CPA's mixed stack of OCR, rules, integrations and selective Claude use; and recurring operator pain points around invoice chasing, RFPs, customer inquiries and WhatsApp-to-CRM updates.
- Reddit claims are leads, not verified case studies. Preserve source type, caveats, comments, counterevidence and privacy. Do not publish self-reported time savings as verified results.

### Website/editorial status

- The website repository currently contains three published articles: the first-agent guide, the customer-enquiry workflow guide and the Project Vend field report. The homepage links to these three articles.
- The ChatGPT Business Hub explainer remains an unpublished draft. It was rechecked against current OpenAI product, Help Center and policy pages on 13 November 2026. The draft now explicitly states that claiming a profile does not change its visibility in ChatGPT. It is awaiting editorial approval; do not publish without the user's approval.
- Google Search Console work is paused because the user explicitly said to leave Google alone. Do not resume the GSC investigation unless the user reopens it.
- Repository SEO basics observed: homepage canonical is present; `robots.txt` allows crawling and references the sitemap; sitemap lists six site URLs. A live production fetch could not be independently verified in this run.

### Active automations and pending commitments

- **KaamWithAI Daily OS:** active, daily at 8:00 Asia/Kolkata.
- **Revisit YouTube:** active, one-time on 1 December 2026; prepare a lightweight setup recommendation only, no publishing without approval.
- **Publish Project Vend story:** completed and disabled.
- **Start workout:** disabled.
- Next priorities: (1) get the Company Page URL and diagnose LinkedIn Page settings/search insights; (2) add a Follow link to the website once the URL is known; (3) get the Business Hub article approved before publishing; (4) draft the next operator-story post; (5) collect post-level LinkedIn metrics.

## 11. Change log

- **13 Nov 2026:** Recorded LinkedIn posts #1 and #2 as published, created the durable content/performance library, added LinkedIn 0-to-100 research and started the Reddit Operator Radar. Refreshed the Business Hub article fact-check. GSC work paused per user instruction.
