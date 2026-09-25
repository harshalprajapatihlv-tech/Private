import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "H",
        "Last 30 Minutes Before the Exam",
        "A calm, ordered glance — not a reread of the book. Then a one-sitting recap of each chapter.",
        ["Last 30 minutes", "Panic protocol", "Chapter-by-chapter recap", "Memory tricks"],
    ))

    parts.append(h2("A. Last 30 minutes — what to actually look at"))
    parts.append(ol([
        "<strong>Equation:</strong> Assets = Liabilities + Capital. Dual aspect: two effects every time.",
        "<strong>Debit increases</strong> assets, expenses, drawings. <strong>Credit increases</strong> liabilities, capital, incomes.",
        "<strong>Journal skeleton</strong> in your head: Dr. … To … (Being …).",
        "<strong>FIFO:</strong> old stock leaves first; newest remains. <strong>WAM:</strong> mix the pool after every purchase; issue at the mix.",
        "<strong>SLM:</strong> (Cost − Scrap) / Life, equal each year. <strong>WDV:</strong> Book value × rate, falling each year.",
        "<strong>Part-year:</strong> months of use / 12. Indian year-end often 31 March.",
        "<strong>Schedule III P&L heads:</strong> Revenue from operations, Other income, Expenses (purchases, change in inventory, employee, finance, depreciation, other), Tax, Profit.",
        "<strong>Schedule III BS heads:</strong> Shareholders’ funds, Non-current liabilities, Current liabilities; Non-current assets, Current assets.",
        "<strong>CFS add-backs:</strong> depreciation, losses on sale, interest expense (then show interest paid in financing). <strong>Deduct:</strong> profit on sale, income moved to investing.",
        "<strong>WC rule:</strong> increase in current assets = cash went out. Increase in current liabilities = cash was held back.",
        "<strong>Twelve ratios:</strong> Current, Quick, Debt–equity, Proprietary, GP%, NP%, Operating ratio, Inventory turnover, Debtors days, ROCE, ROE, Interest coverage.",
        "<strong>Identification:</strong> last sentence of the question = the requirement.",
    ]))

    parts.append(h2("Panic protocol (when a numerical looks ugly)"))
    parts.append(ol([
        "Write the format / skeleton immediately. Formats score.",
        "Fill every figure you are sure of. Leave a blank with a working-note number for the rest.",
        "Open a working note: ‘WN-1 Depreciation’, ‘WN-2 Closing stock’. Examiners read workings.",
        "Check one identity: units (inventory), totals (TB, BS), or cash movement (CFS).",
        "If two methods are possible, pick one, label it, finish it. An incomplete perfect method scores less than a complete labelled one.",
        "Never leave a theory question blank. Dump the definition, three reasons, one example.",
    ]))

    parts.append(h2("B. Final quick revision — chapter recap"))

    parts.append(h3("Bootcamp"))
    parts.append(raw_p(
        "Accounting records and explains business money-events so owners can see profit, position, and cash. "
        "A transaction changes value and has evidence. Assets are what the business owns; liabilities are what it owes; "
        "capital is the owner’s residual claim. Revenue increases that claim; expenses decrease it; drawings are the owner taking value out. "
        "Debit is left; credit is right. Cash coming in is a debit to Cash."
    ))

    parts.append(h3("Chapter 1"))
    parts.append(raw_p(
        "Concepts (entity, money measurement, going concern, cost, dual aspect, accrual, matching, prudence, consistency, materiality, disclosure, periodicity) "
        "tell you <em>how</em> to record. Journal is date-wise; ledger is account-wise; trial balance tests arithmetic equality of debits and credits. "
        "Flow: voucher → journal → ledger → trial balance → financial statements."
    ))

    parts.append(h3("Chapter 2"))
    parts.append(raw_p(
        "Closing stock is a current asset and it changes COGS, so it changes profit. FIFO assumes oldest goods are sold first. "
        "WAM uses a weighted mix. Always reconcile units. AS-2: inventory at cost or NRV, whichever is lower. LIFO is not used in India."
    ))

    parts.append(h3("Chapter 3"))
    parts.append(raw_p(
        "Depreciation allocates cost over useful life. It is not cash leaving. SLM = equal yearly amount. WDV = reducing amount. "
        "Add installation to cost. Charge till the date of sale. Profit/loss on sale = proceeds versus NBV."
    ))

    parts.append(h3("Chapter 4"))
    parts.append(raw_p(
        "Companies present Statement of P&L and Balance Sheet as per Schedule III. Notes complete the story. "
        "Adjustments implement accrual: outstanding, prepaid, depreciation, provisions. The Balance Sheet must tie. "
        "A company has share capital and reserves, not ‘capital + drawings’."
    ))

    parts.append(h3("Chapter 5"))
    parts.append(raw_p(
        "Profit is an accrual story; cash flow is a wallet story. Operating = running the shop (indirect: profit, add non-cash, squeeze WC, pay tax). "
        "Investing = buying/selling long tools and investments. Financing = owners and lenders. A+B+C must explain the change in cash."
    ))

    parts.append(h3("Chapter 6"))
    parts.append(raw_p(
        "The annual report is the year’s public file: narrative (MD&A, Directors’ Report), governance, auditor’s opinion, and the financial statements with notes. "
        "Read the auditor first, then statements, then notes, then the story. Users: owners, lenders, analysts, employees, government."
    ))

    parts.append(h3("Chapter 7"))
    parts.append(raw_p(
        "Ratios turn statements into questions: can we pay bills (liquidity), can we survive debt (solvency), do we earn (profitability), do we use assets (turnover)? "
        "Balance sheet ratios use only BS; revenue ratios only P&L; combined ratios mix both. Write formula, substitute, unit, one-line meaning."
    ))

    parts.append(h2("Memory tricks — last look"))
    parts.append(ul([
        "DEAD CLIC: Debit Expenses, Assets, Drawings; Credit Liabilities, Income, Capital.",
        "FIFO: first in, first out — the new stock is still on the shelf.",
        "WAM: stir the soup, then ladle. Do not stir when you ladle (issue).",
        "SLM: same load every year. WDV: the new phone loses more value in year one.",
        "Outstanding = still owed = liability. Prepaid = paid too early = asset.",
        "Depreciation: add back in cash flow, because you never paid it in cash this year.",
        "Increase in debtors: you made sales but the cash is still in the customer’s pocket.",
        "ROCE uses EBIT and all long-term funds. ROE uses PAT and owners’ funds only.",
        "Schedule III Balance Sheet: who funded it (equity + liabilities) = what we hold (assets).",
    ]))
    parts.append(exam_tip(
        "When time is almost up, stop hunting for a perfect last figure. Box the answer you have, "
        "write ‘WN’ for anything unfinished, and move to a theory question. Theory in complete sentences still scores."
    ))
    parts.append(chapter_close())
    return "".join(parts)
