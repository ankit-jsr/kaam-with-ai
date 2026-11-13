# KaamWithAI Operator Radar — Reddit research

**Started:** 13 November 2026  
**Purpose:** Find real examples of people using AI in everyday work, then investigate the workflow rather than repeating a tool list.  
**Editorial status:** Research leads only. No story in this brief is independently verified.

## Editorial thesis

The most useful AI stories are often not about a fully autonomous agent. They are about an operator removing one irritating, repeated job: preparing a reconciliation, writing a macro, extracting invoice data, following up on a lead, converting a quote, or moving information between systems.

KaamWithAI should report what people actually did, what the workflow looks like, what remains human, what broke, and whether the effort was worth it.

## How to use Reddit responsibly

Reddit is a source of qualitative leads, not a database of verified case studies.

For each candidate:
1. Open the original thread and read the post and relevant comments, not just the search snippet.
2. Classify the source: owner/operator, employee, accountant/adviser, automation builder, vendor, or anonymous/unclear.
3. Separate first-hand claims from second-hand claims and speculation.
4. Capture the exact workflow, systems involved, frequency, baseline, claimed outcome, human checks and failure cases.
5. Look for promotional incentives, affiliate codes, vendor links, engagement farming or obvious AI-generated copy.
6. Seek corroboration where the claim is important: official product documentation, a second independent account, public workflow documentation, or a reproducible test.
7. Label outcomes as self-reported unless independently verified.
8. Do not expose usernames or personal details unnecessarily. Link to the original thread and paraphrase; do not present a Reddit user's claim as a verified KaamWithAI case study.
9. Do not claim we tested a workflow unless we actually reproduce it.
10. Check each subreddit's rules before participating. Do not use communities as a disguised market-research survey or spam channel.

## Candidate stories found

### 1. A staff accountant used ChatGPT to write VBA macros for monthly reconciliations

**Source:** https://www.reddit.com/r/Accounting/comments/1v12xrz/how_i_use_ai_as_a_staff_accountant/  
**Thread date:** 19 July 2026  
**Signal:** 266 points at time of search  
**Source type:** First-hand employee/operator account; works for a private company. Not established as a small-business owner.  
**Evidence status:** Detailed self-report; not independently verified.

The accountant says they use ChatGPT primarily to write VBA scripts/macros, rather than upload a workbook and ask a model to perform accounting work. They describe macros that:
- Open the latest downloaded workbook based on a filename prefix.
- Find relevant data by header names rather than fixed column letters.
- Append data to a reconciliation workbook.
- Refresh pivot-table ranges.
- Roll reconciliation dates forward based on the file name.
- Include error handling so the macro can stop and explain what is wrong.
- Help automate repeated spreadsheet work.

The author says they did not know how to code before using ChatGPT. They also describe using Codex/Python for more general computer workflows and one-off research databases.

**Useful counterpoints in the comments:**
- The author confirms the company is private.
- Other accountants raise IT controls and review requirements.
- One commenter says processes should be understood manually before automating them.
- The author agrees they typically perform a new task manually for a month or two before automating it.
- Commenters stress verifying that a macro ran correctly, not just that it completed without an error.

**Why it is interesting:** The AI did not replace accounting judgment. It helped a non-programmer turn a known, repetitive process into deterministic code. The story gives us concrete steps and a useful distinction between AI-generated code and AI making financial decisions.

**Potential angle:** “An accountant didn't ask AI to do the accounting. He asked it to write the macro.”

**What we still need:** Clarify the actual time saved, the review process, the security approval, and whether the macros are still in use. No quantified saving is stated in the original post.

**Editorial priority:** High as an operator story, with a clear caveat that the author is an employee at a private company rather than a confirmed small-business owner.

### 2. A fractional CPA uses AI selectively and relies on ordinary automation for the rest

**Source:** https://www.reddit.com/r/Accounting/comments/1ri7g98/best_ai_tools_for_accountants_in_2026_looking_to/  
**Thread started:** March 2026; the detailed CPA comment was posted later in the thread.  
**Source type:** First-hand fractional CPA in Canada, reporting work for multiple small businesses from roughly $100,000 to $9 million in annual revenue.  
**Evidence status:** Detailed self-report; not independently verified.

The CPA describes a deliberately mixed stack:
- Dext for invoice extraction, supplier rules and publishing into QuickBooks Online.
- Gmail filters to forward vendor invoices/receipts into Dext.
- Float for employee expenses and reimbursements.
- Synder for sales/Stripe reconciliation.
- A simple Zapier flow for Square transactions where the native integration was inadequate.
- Google Sheets templates for bank data and recurring client models.
- Claude for commentary/report preparation, anomaly flags and some transaction work, with additional integration to the accounting system.
- Asana SOPs written in plain steps; processes are performed manually for a month or two before being turned into workflows.
- Human approvers are assigned for automated actions.

The CPA is skeptical of AI-native accounting startups and says reliable OCR, rules and integrations often solve more than adding an AI layer. They also describe limitations in built-in AI financial analysis.

**Why it is interesting:** It is an unusually practical account of where AI is useful, where ordinary rules-based automation is better, and why a human approval step matters.

**Potential angle:** “A fractional CPA's AI stack is mostly not AI.”

**What we still need:** Verify the CPA's current stack and exact tool roles, understand the MCP integration, and avoid endorsing products based on a single Reddit comment. The thread contains vendor-like comments and tool recommendations; keep those separate from the CPA's own account.

**Editorial priority:** High. Strong fit for small-business operators, especially as a counterweight to AI-everywhere hype.

### 3. Small-business automation builders are repeatedly asked to solve boring workflow problems

**Source:** https://www.reddit.com/r/AiAutomations/comments/1wpzmnj/ive_been_automating_work_for_small_businesses/  
**Thread date:** September 2026  
**Source type:** Automation builder/vendor AMA, with comments from people describing their work.  
**Evidence status:** Useful demand discovery, not a verified success story.

The thread includes people describing work such as:
- Chasing overdue invoices while checking whether someone has already followed up.
- Finding and qualifying government RFPs and re-entering repeated company information.
- Editing e-commerce product photos, writing listings and researching comparables.
- Collecting rental-listing data from a website.
- Drafting replies to customer inquiries with human review.
- Copying staff updates from WhatsApp into Zoho Desk, checking whether emails were answered and escalating delays. One commenter says this combined work takes 2–2.5 hours per day.
- Handling PDF invoices that require employee-name extraction and cost-centre/location matching.

**Why it is interesting:** The recurring demand is for removing tedious coordination and data movement, not necessarily for an autonomous AI employee.

**Caution:** The original poster is a service provider promoting their automation work. Treat the thread as a source of pain-point examples, not independent proof that the suggested automations work or that customers will pay.

**Editorial priority:** Medium for workflow discovery; do not write a success story from this thread.

### 4. Invoice follow-up automation — and the warning not to reinvent existing software

**Source:** https://www.reddit.com/r/smallbusiness/comments/1qq7raa/invoice_followup_automated/  
**Thread date:** 29 January 2026  
**Source type:** Automation builder describing a client workflow; not the business owner.  
**Evidence status:** Specific workflow description with a useful counterpoint in comments.

The builder describes:
1. An invoice email arriving in a dedicated mailbox.
2. Extracting the invoice reference from the email.
3. Retrieving the invoice from Lexware/Lexoffice.
4. Scheduling a follow-up sequence if no response arrives.

A commenter immediately points out that QuickBooks and other billing systems already provide accounts-receivable reminders. This is a useful editorial warning: before building a custom AI workflow, check whether the existing software already solves the problem.

**Potential angle:** “Before you build an AI invoice chaser, check what your accounting software already does.”

**Editorial priority:** Medium as a counterexample, not as a standalone success story.

### 5. An older small-business job-tracking system built with AI

**Source:** https://www.reddit.com/r/smallbusiness/comments/1k87bzg/how_are_small_businesses_actually_using_ai_in/  
**Thread date:** 2024/2025-era thread; older than the other leads.  
**Source type:** First-hand account from a business owner's spouse.  
**Evidence status:** Detailed self-report; old and not independently verified.

The commenter says their business produced 30–50 jobs per day and lacked visibility into production progress. After a long delay with a roughly $1,000/month industry software contract, the owner's husband built a job-tracking system over a weekend using AI-assisted coding. Employees created job tickets, each ticket had a QR code, workers scanned it as they completed steps, customers received an email, pickup triggered an accounting handoff, and the data synced to Airtable.

A reply raised cybersecurity and maintenance concerns; the owner acknowledged the password-only protection was not a long-term solution.

**Why it is interesting:** AI-assisted coding can help a domain expert build a workflow that fits the business better than a generic package. But the security and maintenance caveats are central, not footnotes.

**Editorial priority:** Archive / lower priority due to age.

## Early patterns worth investigating

1. **AI writes the code; ordinary software runs the process.** VBA, Python, Apps Script and spreadsheet formulas can be more reliable and cheaper than an agent making every decision.
2. **The handoffs are often the pain.** Email-to-accounting, WhatsApp-to-ticketing, PDF-to-spreadsheet, enquiry-to-CRM and quote-to-invoice are recurring examples.
3. **Human review is not an afterthought.** Good workflows define what can be prepared automatically and which exceptions require a person.
4. **A process needs to be understood before it is automated.** The accountant and CPA accounts both stress documenting and manually understanding the workflow first.
5. **Sometimes the right answer is not AI.** Built-in accounting rules, OCR, native reminders, Zapier and simple spreadsheet templates may be sufficient.

## First editorial candidate

**Recommended first story:** the fractional CPA's deliberately mixed stack.

Why: it is the closest fit to KaamWithAI's small-business audience, has a first-hand account from a practitioner serving multiple small businesses, and offers a non-hype thesis: reliable data capture and rules first, AI where judgment or language work adds value, human approval for exceptions.

**Alternative:** the staff accountant's VBA story is more vivid and technically detailed. It may work better as a practical LinkedIn post first, with an article later if we can get more detail on actual time saved and controls.

## Recurring research workflow

- Search operator communities for first-person accounts, not just tool announcements.
- Save candidate URLs and classify the source type.
- Read full threads and comments.
- Score each candidate on specificity, first-hand detail, workflow clarity, measurable outcome, counterevidence and reproducibility.
- Reject or hold promotional, vague, unverifiable or duplicated stories.
- Choose one strong story at a time for deeper reporting.
- Turn one validated story into: a website article, a LinkedIn Company Page post, and a practical workflow/checklist when appropriate.

**Do not turn every Reddit anecdote into content. The value is in the investigation, not the volume of links collected.**
