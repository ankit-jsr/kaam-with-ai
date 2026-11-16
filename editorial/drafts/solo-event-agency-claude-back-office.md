# The Vendor Had Replied. Claude Said They Hadn't.

**Status:** Published 15 November 2026 — https://kaamwithai.pages.dev/articles/solo-event-agency-claude-back-office.html  
**Audience:** Small-business owners and solo operators considering AI for email, vendors, calendars and internal records  
**Source:** First-person Reddit account from a solo event-staffing/activation operator, posted 11 September 2026  
**Research brief:** `editorial/research/solo-event-agency-claude-back-office-2026-11-14.md`

---

A vendor had answered every question that morning.

But when the owner of a small event-staffing agency asked Claude about the conversation, it said the vendor had gone quiet.

The owner later found the answers in the full email thread. Claude had looked at the short search preview and missed the vendor's actual reply.

That sounds like a small mistake. In an event business, it can change what you tell a client, which supplier you chase, and whether you believe a job is moving forward.

The operator described the incident in a Reddit discussion about running a business with Claude. They work alone, they said, and Claude had gradually become part of the back office: email, vendor communication, the applicant database and the calendar.

Claude had become a regular part of the work, though several mistakes had nearly cost the business deals.

The email preview was only the beginning.

## The mistakes affected everyday business decisions

The operator described another occasion when Claude said an email had been “staged”. They went looking in Gmail for the draft. It did not exist.

In a separate incident, Claude referred to suppliers as “brand partner candidates”. The distinction mattered: a vendor is paid by the agency; a sponsor pays the agency. The operator spent two days planning around an opportunity that was never there.

Claude also said a table in the business database did not exist, without checking. It was there.

Each mistake involved a basic piece of business information: whether someone had replied, whether an email draft existed, what kind of relationship a company had with the agency, or whether a database record was present.

Each answer sounded plausible. Suppliers do go quiet, email drafts can be saved and database records can be missing. The problem was that Claude presented these claims as facts without checking the underlying record.

They also noticed a pattern in long sessions: details from earlier conversation began to be treated as if they were current evidence.

## The rules the operator added

The operator kept using Claude and added a few checks around the work it was doing.

The first was a master state file to carry business context between sessions. The second was a set of labels for the certainty of a fact:

- **CONFIRMED**
- **STATED**
- **ASSUMED**
- **OPEN**

They also added two explicit rules: never treat an email preview as the full thread, and never claim an action happened without tool output confirming it.

The operator reports that errors fell from several per week to a few per month after these changes. That is their own estimate; no independent error log or audit was provided.

The changes gave Claude a clearer way to label information: what it had checked in a source, what someone had told it, what it had inferred and what was still unknown.

## A state file can preserve a mistake, too

The comments under the discussion add an important complication.

Another solo-agency operator said models can mistake a summary of a tool result for the result itself. An email preview is only a short extract from a conversation. A database summary is not a substitute for checking the record.

The commenter also warned about the state file. If the model itself is allowed to write assumptions into its permanent notes, an unverified claim can become durable context. The next session may read it back as established fact.

Their proposed safeguards were stricter: only verified tool output should update durable state, entries should be dated, and a factual assertion should include a quotation from the source. If there is no source, the system should say it is unverified.

Other commenters suggested using shorter sessions, explicit project instructions and human approval for consequential decisions. One argued that a deterministic dashboard can be safer than relying on a language model to call and edit business systems reliably.

These are suggestions from individual practitioners, not fixes tested across different businesses. They are worth considering whenever an AI system carries notes from one session to the next: an old assumption can be repeated until someone checks the original record.

## Check the record before acting

AI can help prepare emails, organise information and move routine work along. Before acting on its answer, check the original record:

- When it says a supplier has not replied, open the full email thread.
- When it says a draft is ready, look for the draft in Gmail.
- When it reports a database change or calendar booking, check that record in the system itself.

Preparing an email, sending it after approval and seeing it in the Sent folder are three separate steps. A business should be able to check each one. The operator says the new rules reduced the number of mistakes, but we cannot independently verify that improvement or conclude that the workflow is now error-free.

For a related example of why long-running agents need boundaries, read our [Project Vend field report](/articles/claude-blue-blazer-shopkeeper.html). If you're considering a first business agent, start with a narrower job and less authority than you think.

---

## Sources and verification

- [Reddit: Anyone actually running a business with Claude?](https://www.reddit.com/r/ClaudeCode/comments/1wd3hgd/anyone_actually_running_a_business_with_claude/) — first-person account and discussion, posted 11 September 2026.

**Editorial note:** This article is based on a self-reported Reddit account and its comments. We have not interviewed the operator, inspected their systems, independently verified the reported error reduction or reproduced the failures. The author says the mistakes nearly cost deals; they do not report an actual lost deal. The reported improvement from several errors per week to a few per month is the author's estimate, not a measured result.
