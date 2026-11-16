# The CPA Who Automates Bookkeeping Without Chasing AI

**Status:** Draft for editorial review — not published  
**Audience:** Small-business owners using QuickBooks Online, accountants and operators managing invoices, expenses and month-end work  
**Source:** One first-person Reddit account from a Canadian fractional CPA, plus official product documentation  
**Research brief:** `editorial/research/fractional-cpa-bookkeeping-stack-2026-11-16.md`

---

A Canadian fractional CPA was asked what AI tools they use.

Their answer was mostly about tools that have been doing bookkeeping work for years: document extraction, supplier rules, email filters, integrations and Google Sheets.

They describe working with several small businesses, from around CAD $100,000 to $9 million in annual revenue. For that client mix, the recurring work is familiar: collect invoices, code expenses, get payment data into the books, chase missing documents and close the month.

The CPA's view is that much of this work does not need a chatbot. It needs a process that can read a document, apply a rule, move a record to the right system and leave exceptions for someone to check.

This is one practitioner's account, not a survey or an independently audited case study. But the workflow is useful because it shows how an accountant decides what to automate and what to leave alone.

## Invoices go through extraction first

The CPA uses Dext to capture supplier invoices and extract the details. They say it handles most figures well, especially on standard invoices, and can cope with some poor-quality handwritten documents.

The next step is where the process becomes specific to each business. For suppliers with predictable invoices, the CPA sets up rules for general-ledger and tax coding. After those rules have been running for a few months, they enable auto-publishing for suppliers whose documents are consistent enough.

Dext supports supplier rules for fields such as category, tax rate, payment method, currency and description. Those rules can be applied to future documents from the supplier. The software also has auto-publish settings, but Dext's own guidance recommends starting with suppliers whose documents are predictable and checking that the coding is correct before allowing documents to publish automatically.

That last part matters. A rule that works for a monthly software invoice may be wrong when the supplier changes the tax treatment, adds a new service or issues a credit note. The CPA describes using auto-publish for selected suppliers after a period of checking; they are not saying every invoice should go straight into the ledger.

## Receipts and expenses follow a different route

The CPA uses Gmail filters to forward vendor invoices and receipts to Dext, then archive the original emails.

Employee expenses are handled through Float. In the workflow they describe, employees submit receipts, supplier rules help code transactions, managers approve expenses and the records are exported to QuickBooks Online.

There is still a month-end detail to watch. The CPA says a transaction can land in QuickBooks on the following day, which can affect the cut-off when the books are being closed.

Float's documentation describes its QuickBooks Online integration and also lists transactions that may need separate treatment during month-end reconciliation. A connected app does not remove the need to check that all the activity has reached the ledger and that clearing accounts reconcile.

Float is a Canada-focused option in this practitioner's stack. Businesses elsewhere should check which expense and accounting integrations are available in their country before choosing a tool.

## When the bank feed is unreliable, use a template

The CPA says bank feeds have been unreliable for some of their Canadian clients. When a direct connection does not work, they export bank transactions as a CSV, use a Google Sheets template to put the data into the expected format and import it into QuickBooks Online.

That is not a universal statement about Canadian bank feeds. It is what this practitioner says they do for some clients.

It is also a reminder that a spreadsheet can be a perfectly reasonable part of an automated process. The format is visible, the transformation can be checked, and the same template can be reused. The important checks are the date range, row count, opening and closing balances, totals and account mapping before the import is accepted.

## Payment platforms need the right connection

For ecommerce and payment data, the CPA uses different routes depending on the client's setup:

- Synder handles Stripe sales for clients where transaction-level detail is needed.
- The native QuickBooks Online and Shopify integration is enough for a straightforward Shopify setup.
- For one client, the Square connection did not provide the records they needed, so the CPA built a small Zapier flow to create transaction-level entries.

These are examples from particular client configurations, not a verdict on the products. A native connector may be the simplest choice when its data and reconciliation behaviour match the business. A third-party connector or a small Zapier workflow may help when the required level of detail is missing.

Before connecting anything, decide what the books need to show: daily summaries or individual transactions, fees, refunds, tax, payout timing and the link between a sale and its bank deposit. Then test a complete period and reconcile the totals. A connection that imports data is not automatically a correct accounting workflow.

## The month-end tracker is still a spreadsheet

The CPA also reuses a Google Sheets model to track missing information and follow up with clients during month-end close. They have not found another tool worth adopting for that job.

The spreadsheet is not a temporary embarrassment in an otherwise automated system. It gives the accountant a shared list of what is missing, who needs to provide it and what is still open. If the process is clear and the team uses it consistently, replacing it may add work rather than remove it.

## Where this accountant chooses not to use AI

The CPA says they do not use AI to draft routine client emails or marketing copy. Their concern is practical: reviewing a generated email may mean reading the whole thread anyway, and their inbox already functions as their task list.

They have also tried QuickBooks Online's AI financial-analysis feature. In one example, a query about the five largest vendor expenses returned poor results because journal entries affected the vendor attribution. That is one person's experience with one query; it does not establish that the feature is generally unreliable.

The broader point is that the tool should fit the task. If a rule can code a recurring invoice accurately, a language model may add another step. If a spreadsheet can reshape a predictable bank export, there may be little to gain from asking AI to interpret it.

## A simple way to choose what to automate

The CPA's workflow suggests a useful order for reviewing bookkeeping tasks:

| If the task is… | Start by evaluating… | Check before relying on it |
|---|---|---|
| Reading invoices and receipts | OCR or document extraction | Supplier, date, amount, tax and original document |
| Coding a recurring supplier | Supplier rules | Exceptions, tax changes and unusual invoices |
| Moving data between systems | Native integration or connector | Missing records, duplicates, fees, timing and mapping |
| Reformatting a predictable bank export | A saved spreadsheet template | Date range, row count, totals and account mapping |
| Explaining unusual transactions | AI with access to the supporting records | Source documents, calculations and review by the accountant |
| Making accounting judgments or approving entries | A qualified person | Evidence, treatment and approval trail |

This is an editorial framework drawn from one reported workflow and the vendors' documentation. It is not accounting advice or a tested implementation recipe.

For a small business, a useful first step is to write down how one month of transactions actually moves: where documents arrive, who checks them, how they are coded, which system receives them and what gets reconciled at month-end. Mark the repeated steps, the exceptions and the decisions that require judgment. Then choose the simplest tool that handles each part.

You may find that the first improvement is a supplier rule, a better import template or a clearer approval step. An AI assistant can still help with tasks such as explaining an unfamiliar transaction or drafting a note from verified records. It does not need to be the centre of the workflow.

## What we could and couldn't verify

The practitioner describes their own stack in a public Reddit discussion. We have not interviewed them, inspected their accounting systems or measured the time saved. The revenue range and workflow details are self-reported.

We checked official documentation for Dext, Float, Synder, QuickBooks Online, Shopify and Zapier to confirm the capabilities described. Those documents confirm that the products support the relevant types of rules, integrations or exports; they do not verify how this CPA configured them or whether the setup works as described for every client.

The CPA's comments about bank feeds, the Square integration and QuickBooks AI are their own experience. The workflow serves Canadian clients, so details such as Float availability and bank connectivity may not apply elsewhere.

---

## Sources and verification

- [Reddit: Best AI tools for accountants in 2026? Looking to automate workflows](https://www.reddit.com/r/Accounting/comments/1ri7g98/best_ai_tools_for_accountants_in_2026_looking_to/) — first-person account from a user identifying as a Canadian fractional CPA.
- [Dext: Supplier and customer rules](https://help.dext.com/en/articles/216125-how-to-use-supplier-and-customer-rules-in-dext)
- [Dext: Rules and automation](https://help.dext.com/en/articles/416713-rules-and-automation-in-dext)
- [Dext: Getting started for accountants and bookkeepers](https://help.dext.com/en/articles/416727-getting-started-with-dext-for-accountants-and-bookkeepers)
- [Float: QuickBooks Online integration](https://floatfinancial.com/integrations)
- [Float: QBO export guide](https://help.floatfinancial.com/hc/en-us/articles/4415413399444-How-do-QBO-Exports-Work)
- [Float: Month-end reconciliation guide](https://help.floatfinancial.com/hc/en-us/articles/44398462225428-Best-Practices-Guide-for-Month-End-Reconciliation-using-QuickBooks-Online-QBO)
- [Intuit App Marketplace: Synder](https://quickbooks.intuit.com/app/apps/appdetails/synder/)
- [Intuit: Connect Shopify to QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/manage-integrations/connect-shopify-quickbooks-online/L1Xv7ZCFB_US_en_US)
- [Zapier: QuickBooks Online and Square](https://zapier.com/apps/quickbooks/integrations/square)

**Editorial note:** This is a reported workflow based on one self-reported practitioner account, not a verified customer case study. There is no independent interview, system inspection, measured accuracy or quantified time saving. The named products are examples from that practitioner's setup, not endorsements.
