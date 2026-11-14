# Field brief: A solo event agency put Claude in the back office

**Research date:** 14 November 2026  
**Source date:** 11 September 2026  
**Status:** Strong next website-story candidate; self-reported, not independently verified  
**Audience:** Small-business owners and solo operators who are considering AI for email, vendors, calendars and internal records

## The setup

A solo operator says they run a small event-staffing and activation agency. Claude has become part of the business back office: email, vendor communication, applicant database and calendar.

The author says the setup is useful enough to help them operate at their current size. But they also describe several confident errors that nearly cost deals.

**Primary source:** [Reddit — Anyone actually running a business with Claude?](https://www.reddit.com/r/ClaudeCode/comments/1wd3hgd/anyone_actually_running_a_business_with_claude/)

## The failures

The operator gives four concrete examples:

1. **An email preview became the whole story.** Claude said a vendor had gone silent, even though the vendor had answered every question that morning. Claude had relied on an email search preview rather than retrieving the full thread.
2. **A draft was said to exist when it did not.** Claude described an email as “staged”; the operator searched Gmail for a draft that had never actually been created.
3. **A vendor became a sponsor.** Claude referred to suppliers as “brand partner candidates”. The distinction mattered: a vendor is paid by the agency; a sponsor pays the agency. The operator spent two days planning around an opportunity that did not exist.
4. **A database table was declared missing without being checked.** Claude said a table did not exist, although it was there.

The author sees a common pattern: Claude reports something as fact without verifying the underlying source. They say the problem gets worse in long sessions when earlier context is treated as current truth.

## The guardrails the operator added

The author says they introduced:
- A master state file to preserve business context between sessions.
- Explicit fact labels: **CONFIRMED / STATED / ASSUMED / OPEN**.
- A rule never to treat an email preview as the full thread.
- A rule never to claim an action happened without tool output confirming it.

They report that errors fell from several per week to a few per month. This is the author's own estimate, not an independently measured result.

## What the comments add

The thread contains useful counterpoints:
- Another solo-agency operator says a state file can make the problem worse if the model itself writes assumptions into it. Their suggestion: only tool output should update durable state, date every entry, and let old records expire.
- The same commenter suggests requiring a source quotation before a factual assertion; without evidence, label it unverified.
- Other commenters recommend shorter/fresh sessions and explicit rules in project instructions.
- One commenter argues that a deterministic dashboard may be safer than relying on an LLM to call and edit systems reliably.
- Another says the model can do the heavy lifting, but a person should decide consequential actions before a deterministic workflow executes them.

These are individual suggestions, not proven universal fixes. The article should distinguish the original operator's own guardrails from ideas offered by commenters.

## The useful KaamWithAI thesis

The interesting story is not “Claude runs a business”. It is that a solo operator found out how quickly an AI back office can turn an incomplete observation into a confident business fact.

The failure pattern is operational:
- A preview is not the source record.
- A proposed action is not a completed action.
- A summary is not proof that the event happened.
- A supplier and a sponsor are not interchangeable.
- A state file is not reliable merely because it is persistent.

The guardrail is to make the system show its evidence: retrieve the full source, quote the relevant line, label uncertainty, and require a real tool receipt before saying a draft was created, a message was sent, or a record was changed.

## Proposed article direction

**Working headline:** The AI Back Office That Nearly Cost a Solo Agency Its Deals

**Alternative:** A Solo Event Agency Put Claude in the Back Office. Then It Started Making Mistakes.

**Opening idea:** The operator was told a vendor had gone quiet. The vendor had answered that morning. The AI had read a preview, not the conversation. Build the rest of the story from there rather than listing every failure in the opening.

**Narrative outline:**
1. Introduce the solo event-staffing operator and why email, vendors, applicants and calendars make a useful AI back office.
2. Reconstruct the first failure: a search preview mistaken for a full email thread.
3. Reveal the other mistakes: nonexistent draft, vendor/sponsor confusion, unverified database claim.
4. Identify the shared failure mode: treating summaries and model-generated state as source evidence.
5. Explain the operator's guardrails and the reported reduction in errors, with clear attribution.
6. Add the commenters' strongest warning: a state file can preserve an assumption just as easily as a fact.
7. Give small-business owners a practical checklist before they let AI handle business operations.

## Practical checklist for readers

- **Retrieve the source, not the preview.** For email, open the complete thread and check the latest message.
- **Separate intent from completion.** “I will draft it” is not “draft created”; “ready to send” is not “sent”.
- **Require action receipts.** Store a message ID, draft ID, calendar event ID, database result or transaction reference.
- **Label the certainty of facts.** Confirmed, stated, assumed and open are different states.
- **Date durable notes.** Facts and assumptions can expire; old context should not silently become current.
- **Do not let the model be the only writer of its own source of truth.** Prefer records generated from verified tool output.
- **Use deterministic systems for consequential execution.** Let AI interpret and prepare; let rules and approvals control what is actually sent, booked or changed.
- **Keep human approval for commitments, money, contracts and unusual exceptions.**

## Claims we must not make

- Do not claim the agency's revenue, staff size beyond the author's solo-operator description, or number of clients; none is supplied.
- Do not say the errors actually caused lost deals. The author says they nearly cost deals.
- Do not present the reported reduction from several errors a week to a few a month as independently verified.
- Do not imply these guardrails eliminate hallucinations or guarantee reliability.
- Do not imply Claude is integrated with every named business system; the post does not specify the full technical setup.
- Do not identify or expose the Reddit account holder beyond the public details necessary to understand the business type.

## Editorial next step

This is the strongest current candidate for the next KaamWithAI website field report after the Business Hub article. It is a concrete, first-person small-business account with a meaningful failure mode, practical controls and counterarguments. It has low visible engagement and no independent verification; do not treat Reddit votes as evidence of representativeness. No direct interview, independent reproduction or access to the operator's systems has been obtained.
