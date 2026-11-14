# KaamWithAI — Operating Context

**Last updated:** 14 November 2026  
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

The ChatGPT Business Hub explainer was published on 14 November 2026 at https://kaamwithai.pages.dev/articles/chatgpt-business-hub-small-business.html. PR #4 is merged; GitHub Actions run #62 passed site validation and production deployment. The article is desk research, not hands-on testing.

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
- No further post is recommended on 13 November because post #2 was just published. A Reddit-sourced operator story about a staff accountant using ChatGPT to write VBA macros has now been drafted in the content library for a possible 16 November post; it is not yet approved or published.
- Research saved to `editorial/research/linkedin-company-page-growth-0-to-100-2026-11-13.md`.

### Reddit Operator Radar

- A recurring research programme has been started in `editorial/research/operator-radar-2026-11-13.md`.
- Best current leads: a staff accountant using ChatGPT to write VBA macros for reconciliations; a fractional CPA's mixed stack of OCR, rules, integrations and selective Claude use; and recurring operator pain points around invoice chasing, RFPs, customer inquiries and WhatsApp-to-CRM updates.
- Reddit claims are leads, not verified case studies. Preserve source type, caveats, comments, counterevidence and privacy. Do not publish self-reported time savings as verified results.

### Website/editorial status

- The `main` branch now contains four published articles: the first-agent guide, the customer-enquiry workflow guide, the Project Vend field report and the ChatGPT Business Hub explainer. The Business Hub article is at https://kaamwithai.pages.dev/articles/chatgpt-business-hub-small-business.html; homepage and sitemap updated. OpenAI's product page, Help Center and Business Agents Policy were rechecked on 14 November 2026. It is desk research, not hands-on testing. PR #4 merged and production deployment succeeded in GitHub Actions run #62.
- Google Search Console work is paused because the user explicitly said to leave Google alone. Do not resume the GSC investigation unless the user reopens it.
- Repository SEO basics: homepage and article canonicals are present; `robots.txt` allows crawling and references the sitemap; the sitemap now lists seven site URLs. The production deployment job succeeded, although a separate browser fetch of the Pages URL was not available in this run.

### Active automations and pending commitments

- **KaamWithAI Daily OS:** active, daily at 8:00 Asia/Kolkata.
- **Revisit YouTube:** active, one-time on 1 December 2026; prepare a lightweight setup recommendation only, no publishing without approval.
- **Publish Project Vend story:** completed and disabled.
- **Start workout:** disabled.
- Next priorities: (1) draft and fact-check the solo event-agency/Claude field report; (2) prepare the accountant/VBA Company Page post for 16 November; (3) keep the 300-client accounting-firm story on hold pending identity/vendor disclosure; (4) get the Company Page URL to add a Follow link and audit its Page settings; (5) collect post-level metrics when available.

## 11. Change log

- **13 Nov 2026:** Recorded LinkedIn posts #1 and #2 as published, created the durable content/performance library, added LinkedIn 0-to-100 research and started the Reddit Operator Radar. Refreshed the Business Hub article fact-check. GSC work paused per user instruction.


## 12. Website publishing update — 13 November 2026

**Historical snapshot:** the PR review state before merge; the final publication result is recorded in Section 14.

- User approved the ChatGPT Business Hub article for publication; approval is explicit and no further approval is required.
- Article page created on branch `publish/chatgpt-business-hub` at `site/articles/chatgpt-business-hub-small-business.html`. Homepage card and sitemap entry added. Editorial source marked approved, not yet live.
- Official OpenAI product page, Help Center and Business Agents Policy rechecked on 14 November 2026. Key caveats retained: claiming does not guarantee increased visibility or control independent recommendations; Business Agents are US-only for eligible ecommerce/online-service businesses; agents cannot complete purchases, bookings or order lookups; insights are aggregate and privacy-preserving.
- Article is desk research, not hands-on testing. Do not imply access to or testing of Business Hub.
- PR #4 is open. GitHub Actions run #51 completed: site validation passed; Cloudflare PR preview deployed successfully to `https://pr-4.kaamwithai.pages.dev` (deployment ID URL `https://631778a9.kaamwithai.pages.dev`). Production deployment is skipped until merge. The preview was deployed, but a separate browser fetch was not available in this run; source and automated validation were reviewed. Do not call the article live until merged and production URL is verified.


## 13. Daily operating update — 14 November 2026

### Website and publishing
- PR #4 — [Publish ChatGPT Business Hub field guide](https://github.com/ankit-jsr/kaam-with-ai/pull/4) — remains open and mergeable.
- GitHub Actions run #51 succeeded. The `Validate site` job passed. The Cloudflare `Deploy pull-request preview` job succeeded and produced `https://pr-4.kaamwithai.pages.dev`; production deployment was skipped as expected for a PR.
- OpenAI's product page, Help Center (updated two days before this check) and Business Agents Policy (updated 10 November) were rechecked on 14 November. Eligibility and capability caveats remain in the article.
- PR is approved by the user at the editorial level; production publication still requires merge and deployment verification.

### LinkedIn
- No post recommended on 14 November. Post #2 was published 13 November; the next distinct story is reserved for Monday 16 November.
- KWAI-LI-003 is now drafted and ready for user review. It covers a staff accountant using ChatGPT to write VBA macros for reconciliation tasks. The source is first-hand but self-reported, from an employee at a private company, and has no quantified savings. IT/security restrictions are explicitly noted.
- Do not mark KWAI-LI-003 posted until the user confirms.

### Research
- Re-opened the original Reddit thread and checked comments for the VBA story. Updated the Operator Radar with evidence limits and IT-control counterpoints.
- Fresh small-business subreddit searches surfaced mostly weak, promotional or generic prompts; no stronger case-study candidate replaced the current queue.
- Fractional CPA story remains the leading candidate for the next website article, but needs deeper source extraction and tool-role verification.

### Google Search Console
- Remains paused at the user's instruction. No GSC access, screenshots or changes were requested or made.


- **Research correction (14 Nov):** The Operator Radar previously conflated two separate Reddit accounts. The fractional CPA describes an OCR/rules/integrations-heavy stack; a different account, who says they run a 300-client firm, describes Claude, QBO/MCP and Loopfour. The research brief and content library now separate them. The 300-client firm story is the strongest next website candidate; the staff accountant VBA story remains the next LinkedIn candidate for 16 Nov.


## 14. Post-merge and research update — 14 November 2026

### Website
- PR #4 merged on 14 November 2026 at 02:40 UTC (merge commit `3013440a1379e291a8159a48198911cbd3996075`).
- GitHub Actions run #62 completed successfully. The `Validate site` job passed and `Deploy production to Cloudflare Pages` succeeded.
- Published article: https://kaamwithai.pages.dev/articles/chatgpt-business-hub-small-business.html
- Homepage card and sitemap entry are in `main`. The sitemap now lists seven URLs. A separate browser fetch of the production Pages URL was unavailable in this run; deployment success is confirmed by the production workflow.

### Distribution
- No LinkedIn post recommended on 14 November. Post #2 went live 13 November; KWAI-LI-003 is ready for user review for Monday 16 November. The user still manually reviews and posts; nothing has been scheduled or published by the assistant.
- KWAI-LI-006 (300-client accounting firm using Claude) is on hold because the Reddit account may be commercially connected to NumbersGame/Loopfour. Do not frame as an independent customer case without confirming identity and disclosing ownership.
- KWAI-LI-007 (solo event-staffing operator using Claude) is a researched future derivative; write the website article first.

### Editorial research
- Strongest next website candidate: the solo event-staffing operator whose Claude back office made confident errors that nearly cost deals. Full research brief: `editorial/research/solo-event-agency-claude-back-office-2026-11-14.md`.
- The 300-client accounting-firm brief now includes Anthropic's current commercial data/training/retention controls and Enterprise pricing, plus the possible vendor conflict. It is held pending identity confirmation.
- The fractional CPA's OCR/rules/integrations account remains a separate, non-AI-heavy contrast story. Do not conflate it with the Claude/Loopfour account.

### Automations and constraints
- KaamWithAI Daily OS remains active daily at 08:00 Asia/Kolkata.
- Revisit YouTube remains active for 1 December 2026; faceless production, ElevenLabs narration and minimal hands-on work remain the recorded preference. No publishing without approval.
- Google Search Console remains paused at the user's instruction. No GSC access or changes were made.
