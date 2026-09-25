import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "G",
        "Common Mistakes Checklist",
        "Read this the night before. Most lost marks in Accounting for Managers are these traps, not ‘hard maths’.",
        ["Bootcamp", "Journal–ledger–TB", "Inventory", "Depreciation",
         "Company accounts", "Cash flow", "Annual reports", "Ratios"],
    ))

    parts.append(h2("Bootcamp and debit–credit"))
    parts.append(ul([
        "Treating debit as ‘bad’ and credit as ‘good’. They are only left and right.",
        "Using bank-language: ‘my account was credited’ means the bank’s liability to you increased — that is the bank’s books, not yours.",
        "Calling furniture ‘purchases’. Purchases = goods for resale.",
        "Treating drawings as an expense in the P&L.",
        "Forgetting that every transaction has two sides (dual aspect).",
        "Writing only one account in a journal.",
        "Increasing cash with a credit. Cash is an asset: increase = debit.",
    ]))

    parts.append(h2("Chapter 1 — Journal, ledger, trial balance"))
    parts.append(ul([
        "Posting a journal debit to the credit of the ledger (the most common posting error).",
        "Balancing an account by putting the balance on the larger side. Balance c/d sits on the smaller side so that totals match.",
        "Forgetting the narration, or writing a narration that restates the account names without the event.",
        "Including closing stock in the trial balance when it is given as an adjustment (it is not yet a ledger balance unless already recorded).",
        "Assuming a trial balance that agrees means the books are correct. It only means debits equal credits.",
        "Listing sales on the debit side of the trial balance because ‘sales is goods going out’.",
        "Omitting compound entries (one debit, two credits) when cash and discount both arise.",
    ]))

    parts.append(h2("Chapter 2 — Inventory"))
    parts.append(ul([
        "Issuing newest stock first when the question said FIFO.",
        "Recomputing weighted average on an issue. Average changes on purchase, not on issue.",
        "Valuing stock at selling price. Stock is at cost (or NRV if lower) — not at sales value.",
        "Forgetting opening stock in both units and rupees.",
        "Units not reconciling: opening + receipts − issues must equal closing units. If they don’t, the rupee answer is wrong.",
        "Adding freight to every unit in the warehouse. Freight of a lot joins that lot’s cost (FIFO) or the pool (WAM).",
        "Mixing FIFO layers after an issue (keeping a layer that was fully issued).",
        "Using LIFO in an Indian paper without being asked. AS-2 does not allow LIFO.",
    ]))

    parts.append(h2("Chapter 3 — Depreciation"))
    parts.append(ul([
        "Applying an SLM rate to WDV, or a WDV rate to original cost in later years.",
        "Deducting scrap value every year under WDV. Scrap is not subtracted annually under WDV.",
        "Charging a full year when the asset was purchased on 1 October (usually 6/12).",
        "Forgetting to add installation, freight, and non-refundable duties to cost.",
        "Stopping depreciation on 1 April when the asset was sold on 30 September — charge up to the date of sale unless the question says otherwise.",
        "Treating depreciation as a cash outflow in later cash-flow questions.",
        "Showing the asset at cost on the Balance Sheet without deducting accumulated depreciation.",
        "Computing profit on sale against original cost instead of net book value.",
    ]))

    parts.append(h2("Chapter 4 — Company accounts"))
    parts.append(ul([
        "Using a sole-proprietor Trading Account format when the question says Schedule III.",
        "Putting drawings in a company Balance Sheet.",
        "Showing proposed dividend as a liability when it is only proposed (current law: disclose in notes until declared). If the university paper still treats it as appropriation, follow the paper’s hint — but know the modern treatment.",
        "Classifying trade payables as borrowings, or a bank term loan as a trade payable.",
        "Putting outstanding expenses under provisions always — usually ‘other current liabilities’.",
        "Forgetting to move the current portion of long-term debt to current liabilities when asked.",
        "Not netting the provision for doubtful debts against trade receivables.",
        "Leaving the Balance Sheet totals unequal and not checking workings.",
        "Treating interest on debentures as a distribution (it is a finance cost).",
        "Ignoring ‘changes in inventories’ and writing a manufacturing account inside Schedule III.",
    ]))

    parts.append(h2("Chapter 5 — Cash flow"))
    parts.append(ul([
        "Starting from PAT without adding back tax, then also deducting tax paid — be consistent with ‘profit before tax’ format.",
        "Not adding back depreciation.",
        "Not deducting profit on sale of asset from operating profit (otherwise the profit is counted twice when sale proceeds go to investing).",
        "Showing purchase of machinery as an operating outflow.",
        "Treating bonus issue or conversion of debentures as a cash inflow.",
        "Using the tax figure from the P&L as ‘tax paid’ instead of deriving tax paid from provisions.",
        "Including cash and bank already inside working capital changes (they are the result, not an adjustment).",
        "Forgetting that an increase in debtors is a use of cash (subtract).",
        "Failing to tick that A+B+C equals the movement in cash on the Balance Sheet.",
    ]))

    parts.append(h2("Chapter 6 — Annual reports"))
    parts.append(ul([
        "Saying the annual report is ‘just the Balance Sheet’.",
        "Ignoring the auditor’s opinion and quoting MD&A claims as facts.",
        "Confusing the Directors’ Report with MD&A.",
        "Not using the notes when a face figure looks too round or too neat.",
    ]))

    parts.append(h2("Chapter 7 — Ratios"))
    parts.append(ul([
        "Using sales instead of COGS in inventory turnover (state the formula you chose; COGS is preferred).",
        "Including inventory or prepaid expenses in the quick ratio.",
        "Using PAT in the numerator of ROCE (use EBIT / operating profit).",
        "Using only share capital in ROE instead of shareholders’ funds (capital + reserves).",
        "Dropping the unit: 2 is incomplete; 2 times or 2:1 is complete.",
        "Not averaging opening and closing when both are given.",
        "Interpreting ‘higher is always better’. A current ratio of 8 may mean idle cash or slow stock.",
        "Mixing days and times in the same sentence without conversion.",
        "Taking total sales when the question says credit sales for debtors turnover.",
    ]))
    parts.append(chapter_close())
    return "".join(parts)
