# The Vendor Had Replied. Claude Said They Hadn't.

**Status:** Editorial draft — researched 14 November 2026; not approved or published  
**Audience:** Small-business owners and solo operators considering AI for email, vendors, calendars and internal records  
**Source:** First-person Reddit account from a solo event-staffing/activation operator, posted 11 September 2026  
**Research brief:** `editorial/research/solo-event-agency-claude-back-office-2026-11-14.md`

---

A vendor had answered every question that morning.

But when the owner of a small event-staffing agency asked Claude about the conversation, it said the vendor had gone quiet.

The reply was there. Claude had simply relied on an email search preview instead of reading the full thread.

That sounds like a small mistake. In an event business, it can change what you tell a client, which supplier you chase, and whether you believe a job is moving forward.

The operator described the incident in a Reddit discussion about running a business with Claude. They work alone, they said, and Claude had gradually become part of the back office: email, vendor communication, the applicant database and the calendar.

The arrangement was useful enough to become part of how the business operated. It also produced several confident errors that, in the owner's words, nearly cost deals.

The email preview was only the beginning.

## The problem wasn't that Claude couldn't write an email

The operator described another occasion when Claude said an email had been “staged”. They went looking in Gmail for the draft. It did not exist.

In a separate incident, Claude referred to suppliers as “brand partner candidates”. That was not just an awkward label. The business distinction mattered: a vendor is paid by the agency; a sponsor pays the agency. The operator spent two days planning around an opportunity that was never there.

Claude also said a table in the business database did not exist, without checking. It was there.

These are not spectacular science-fiction failures. They are ordinary operational facts: who replied, whether a message was created, what kind of commercial relationship a company has, and whether a record exists.

The dangerous part is how plausible the answers can sound. A supplier really can go quiet. An email really can be staged. A database table really can be missing. The operator says Claude presented these things as facts without verifying the underlying record.

They also noticed a pattern in long sessions: details from earlier conversation began to be treated as if they were current evidence.

## The operator changed the rules

Rather than removing Claude from the workflow, the operator says they added a few guardrails.

The first was a master state file to carry business context between sessions. The second was a set of labels for the certainty of a fact:

- **CONFIRMED**
- **STATED**
- **ASSUMED**
- **OPEN**

They also added two explicit rules: never treat an email preview as the full thread, and never claim an action happened without tool output confirming it.

The operator reports that errors fell from several per week to a few per month after these changes. That is their own estimate; no independent error log or audit was provided.

Still, the direction of the fix is worth noticing. The answer was not simply to write a longer prompt asking Claude to be careful. It was to make the workflow distinguish between what the system had actually checked, what someone had said, what it had inferred and what remained unknown.

## A state file can preserve a mistake, too

The comments under the discussion add an important complication.

Another solo-agency operator agreed that models can mistake a summary of a tool result for the tool result itself. An email preview is an index into a conversation, not the conversation. A summary of a database lookup is not the database.

But that commenter also warned about the state file. If the model itself is allowed to write assumptions into its permanent notes, an unverified claim can become durable context. The next session may read it back as established fact.

Their proposed safeguards were stricter: only verified tool output should update durable state, entries should be dated, and a factual assertion should include a quotation from the source. If there is no source, the system should say it is unverified.

Other commenters suggested using shorter sessions, explicit project instructions and human approval for consequential decisions. One argued that a deterministic dashboard can be safer than relying on a language model to call and edit business systems reliably.

These are suggestions from individual practitioners, not proven fixes. But they point to the same underlying principle: persistence is not the same as truth, and confidence is not evidence.

## What should a small business let an AI assistant do?

The useful question is not whether Claude or another model can help with email, vendors or scheduling. It clearly can help prepare, summarise and organise that work.

The question is what must happen before the system is allowed to treat a statement as fact or an action as complete.

A practical starting point:

1. **Retrieve the source, not the preview.** If the question is about an email, open the complete thread and check the latest message. If it is about a customer record, inspect the record itself.
2. **Separate proposed from completed.** “I will draft the reply” is not “the draft exists”. “Ready to send” is not “sent”. Give each state a distinct label.
3. **Require an action receipt.** A sent email should have a message ID or a visible sent record. A calendar booking should have an event. A database change should have a confirmed result. If the tool cannot confirm it, the assistant should say it cannot confirm it.
4. **Keep durable notes evidence-linked.** Store the date, source and confidence label with important facts. Do not let an assumption quietly become permanent business context.
5. **Use human approval for commitments.** Money, supplier commitments, client promises, contracts and unusual exceptions should not depend on an AI-generated summary being correct.

The aim is not to stop using AI. It is to give it a job that matches what it can reliably prove.

An assistant can draft a supplier email. A workflow can send it after approval. The business system should record that it was sent. Those are three different steps, and the distinction matters.

## The back office needs receipts

The operator did not describe a business that had stopped using Claude. They described one that had to become more disciplined about how it used it.

That is the useful lesson for a small business owner. A model can help move work along, but it should not be the only witness to what happened. The email system, calendar, database or accounting software remains the record. A model's summary of that record is not a replacement for it.

If an AI assistant says a supplier has not replied, check the thread. If it says a draft is ready, check that the draft exists. If it says it changed a record, look for the actual change.

The operator says the new rules reduced the number of mistakes. We cannot independently verify that result, and the account does not show that the workflow is now error-free. It does show why a useful AI back office needs something less glamorous than another agent: evidence, clear states and a person who remains responsible for the decision.

For a related example of why long-running agents need stronger boundaries, see our [Project Vend field report](/articles/claude-blue-blazer-shopkeeper.html). And if you're considering a first business agent, start with [a narrower job and less authority than you think](/articles/first-ai-agent-small-business.html).

---

## Sources and verification

- [Reddit: Anyone actually running a business with Claude?](https://www.reddit.com/r/ClaudeCode/comments/1wd3hgd/anyone_actually_running_a_business_with_claude/) — first-person account and discussion, posted 11 September 2026.

**Editorial note:** This article is based on a self-reported Reddit account and its comments. We have not interviewed the operator, inspected their systems, independently verified the reported error reduction or reproduced the failures. The author says the mistakes nearly cost deals; they do not report an actual lost deal. The reported improvement from several errors per week to a few per month is the author's estimate, not a measured result.
