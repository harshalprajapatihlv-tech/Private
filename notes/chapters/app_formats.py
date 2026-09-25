import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "D",
        "Most Important Formats",
        "Draw these skeletons in the answer booklet first, then fill figures. Formats themselves carry marks.",
        ["Journal", "Ledger", "Trial Balance", "Store ledgers", "Depreciation schedule",
         "Schedule III P&L and BS", "Cash flow", "Ratio workings"],
    ))

    parts.append(h2("1. Journal"))
    parts.append(table(
        ["Date", "Particulars", "L.F.", "Debit (₹)", "Credit (₹)"],
        [
            ["yyyy-mm-dd", "Account to be debited …… Dr.", "", "xx", ""],
            ["", "&nbsp;&nbsp;&nbsp;&nbsp;To Account to be credited", "", "", "xx"],
            ["", "<em>(Being narration — why the entry is passed)</em>", "", "", ""],
        ],
        caption="Journal of … for the period …",
    ))
    parts.append(raw_p("Rule of writing: the debit account is written first, flush left, with ‘Dr.’ at the end of that line. The credit line is indented and begins with ‘To’."))

    parts.append(h2("2. Ledger"))
    parts.append(table(
        ["Date", "Particulars", "J.F.", "₹", "Date", "Particulars", "J.F.", "₹"],
        [
            ["", "To … (debit entries)", "", "xx", "", "By … (credit entries)", "", "xx"],
            ["", "To Balance c/d (if credit-heavy)", "", "xx", "", "By Balance c/d (if debit-heavy)", "", "xx"],
            ["", "Total", "", "xx", "", "Total", "", "xx"],
            ["Next period", "To Balance b/d", "", "xx", "Next period", "By Balance b/d", "", "xx"],
        ],
        caption="Dr &nbsp;&nbsp; Name of Account &nbsp;&nbsp; Cr",
    ))

    parts.append(h2("3. Trial Balance"))
    parts.append(table(
        ["Particulars", "L.F.", "Debit (₹)", "Credit (₹)"],
        [
            ["Cash, Bank, Debtors, Stock, Furniture, Expenses, Drawings, …", "", "xx", ""],
            ["Capital, Loans, Creditors, Sales, Commission, …", "", "", "xx"],
            ["<strong>Total</strong>", "", "<strong>xx</strong>", "<strong>xx</strong>"],
        ],
        caption="Trial Balance as at …",
        foot="The two totals must be identical. A trial balance is not a financial statement; it is a check.",
    ))

    parts.append(h2("4. Store ledger — FIFO"))
    parts.append(table(
        ["Date", "Receipts Qty", "Receipts Rate", "Receipts Amt", "Issues Qty", "Issues Rate", "Issues Amt", "Balance Qty", "Balance Rate / layers", "Balance Amt"],
        [
            ["", "", "", "", "", "oldest layer first", "", "", "show remaining layers", ""],
        ],
        foot="After every line, remaining quantity must equal previous balance + receipts − issues.",
    ))

    parts.append(h2("5. Store ledger — Weighted Average"))
    parts.append(table(
        ["Date", "Receipts Qty", "Rate", "Amt", "Issues Qty", "Rate (avg)", "Amt", "Bal. Qty", "Avg rate", "Amt"],
        [
            ["Purchase row", "q", "r", "q×r", "—", "—", "—", "new qty", "new total cost ÷ new qty", "new cost"],
            ["Issue row", "—", "—", "—", "q", "current avg", "q×avg", "left", "same avg", "left × avg"],
        ],
        foot="Never change the average on an issue row. Only purchases (and sometimes returns) change the average.",
    ))

    parts.append(h2("6. Depreciation schedule"))
    parts.append(table(
        ["Year / period", "Opening WDV or Cost", "Depreciation for the year", "Accumulated depreciation", "Closing WDV"],
        [
            ["Year 1", "Cost", "as per SLM or WDV, × months/12 if needed", "running total", "cost − accum."],
            ["Year 2", "…", "…", "…", "…"],
        ],
    ))

    parts.append(h2("7. Statement of Profit and Loss (Schedule III)"))
    parts.append(table(
        ["Particulars", "Note", "₹"],
        [
            ["I. Revenue from operations", "", "xx"],
            ["II. Other income", "", "xx"],
            ["III. Total income (I + II)", "", "xx"],
            ["IV. Expenses", "", ""],
            ["&nbsp;&nbsp;Cost of materials consumed / Purchases of stock-in-trade", "", "xx"],
            ["&nbsp;&nbsp;Changes in inventories of finished goods, WIP and stock-in-trade", "", "xx"],
            ["&nbsp;&nbsp;Employee benefits expense", "", "xx"],
            ["&nbsp;&nbsp;Finance costs", "", "xx"],
            ["&nbsp;&nbsp;Depreciation and amortisation expense", "", "xx"],
            ["&nbsp;&nbsp;Other expenses", "", "xx"],
            ["Total expenses", "", "xx"],
            ["V. Profit before exceptional items and tax (III − IV)", "", "xx"],
            ["VI. Exceptional items", "", "xx"],
            ["VII. Profit before tax", "", "xx"],
            ["VIII. Tax expense", "", "xx"],
            ["IX. Profit for the period", "", "xx"],
        ],
        caption="Statement of Profit and Loss for the year ended 31 March …",
    ))

    parts.append(h2("8. Balance Sheet (Schedule III)"))
    parts.append(table(
        ["Particulars", "Note", "₹"],
        [
            ["<strong>I. EQUITY AND LIABILITIES</strong>", "", ""],
            ["1. Shareholders’ funds", "", ""],
            ["&nbsp;&nbsp;(a) Share capital", "", "xx"],
            ["&nbsp;&nbsp;(b) Reserves and surplus", "", "xx"],
            ["2. Non-current liabilities", "", ""],
            ["&nbsp;&nbsp;(a) Long-term borrowings", "", "xx"],
            ["&nbsp;&nbsp;(b) Other long-term liabilities / provisions", "", "xx"],
            ["3. Current liabilities", "", ""],
            ["&nbsp;&nbsp;(a) Short-term borrowings", "", "xx"],
            ["&nbsp;&nbsp;(b) Trade payables", "", "xx"],
            ["&nbsp;&nbsp;(c) Other current liabilities", "", "xx"],
            ["&nbsp;&nbsp;(d) Short-term provisions", "", "xx"],
            ["<strong>Total</strong>", "", "<strong>xx</strong>"],
            ["<strong>II. ASSETS</strong>", "", ""],
            ["1. Non-current assets", "", ""],
            ["&nbsp;&nbsp;(a) Property, plant and equipment / Intangible assets", "", "xx"],
            ["&nbsp;&nbsp;(b) Non-current investments", "", "xx"],
            ["&nbsp;&nbsp;(c) Long-term loans and advances / other", "", "xx"],
            ["2. Current assets", "", ""],
            ["&nbsp;&nbsp;(a) Inventories", "", "xx"],
            ["&nbsp;&nbsp;(b) Trade receivables", "", "xx"],
            ["&nbsp;&nbsp;(c) Cash and cash equivalents", "", "xx"],
            ["&nbsp;&nbsp;(d) Short-term loans and advances / other current assets", "", "xx"],
            ["<strong>Total</strong>", "", "<strong>xx</strong>"],
        ],
        caption="Balance Sheet as at 31 March …",
        foot="The two totals must agree. Always show notes numbers. Always classify current vs non-current.",
    ))

    parts.append(h2("9. Cash Flow Statement — Indirect Method"))
    parts.append(table(
        ["Particulars", "₹", "₹"],
        [
            ["<strong>A. Cash flows from operating activities</strong>", "", ""],
            ["Net profit before tax", "", "xx"],
            ["Adjustments for: Depreciation", "xx", ""],
            ["Loss / (Profit) on sale of fixed assets", "xx", ""],
            ["Interest expense", "xx", ""],
            ["(Interest / dividend income)", "(xx)", ""],
            ["Operating profit before working capital changes", "", "xx"],
            ["(Increase) / Decrease in inventories", "xx", ""],
            ["(Increase) / Decrease in trade receivables", "xx", ""],
            ["Increase / (Decrease) in trade payables", "xx", ""],
            ["Cash generated from operations", "", "xx"],
            ["Income tax paid", "", "(xx)"],
            ["Net cash from operating activities (A)", "", "xx"],
            ["<strong>B. Cash flows from investing activities</strong>", "", ""],
            ["Purchase of PPE / investments", "", "(xx)"],
            ["Sale proceeds of PPE / investments", "", "xx"],
            ["Interest / dividend received", "", "xx"],
            ["Net cash from investing activities (B)", "", "xx"],
            ["<strong>C. Cash flows from financing activities</strong>", "", ""],
            ["Proceeds from issue of shares / loans", "", "xx"],
            ["Repayment of loans / redemption", "", "(xx)"],
            ["Interest paid", "", "(xx)"],
            ["Dividend paid", "", "(xx)"],
            ["Net cash from financing activities (C)", "", "xx"],
            ["Net increase / (decrease) in cash (A+B+C)", "", "xx"],
            ["Add: Opening cash and cash equivalents", "", "xx"],
            ["Closing cash and cash equivalents", "", "xx"],
        ],
    ))

    parts.append(h2("10. Ratio working table"))
    parts.append(table(
        ["Ratio", "Formula", "Substitution", "Answer (with unit)", "One-line comment"],
        [
            ["Current ratio", "CA / CL", "", "times", ""],
            ["GP ratio", "GP / Sales × 100", "", "%", ""],
            ["Inventory turnover", "COGS / Avg stock", "", "times", ""],
        ],
        foot="Always write the unit: times, %, or days. A bare number is incomplete.",
    ))
    parts.append(chapter_close())
    return "".join(parts)
