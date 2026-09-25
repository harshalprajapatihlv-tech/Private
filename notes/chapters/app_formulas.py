import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "A",
        "Master Formula Sheet",
        "Every formula you need in the examination, in one place. Know what each symbol means before you memorise.",
        ["Accounting equation", "Inventory (FIFO, WAM, COGS)", "Depreciation SLM & WDV",
         "Company accounts workings", "Cash flow derivations", "All ratios"],
    ))
    parts.append(lead(
        "Copy this sheet once into your rough notes. In the hall, write the formula first, then substitute, then compute. Marks are often given for the formula even if arithmetic slips."
    ))

    parts.append(h2("1. Accounting equation"))
    parts.append(formula("Assets = Liabilities + Capital"))
    parts.append(formula(
        "Assets = Liabilities + Opening capital + Profit − Loss − Drawings + Additional capital",
        "Profit = Revenue − Expenses. Drawings reduce capital, they are not a business expense.",
    ))
    parts.append(formula("Closing capital = Opening capital + Additional capital + Profit − Drawings"))

    parts.append(h2("2. Inventory and trading"))
    parts.append(formula("Cost of goods sold (COGS) = Opening stock + Purchases + Direct expenses − Closing stock"))
    parts.append(formula("Gross profit = Sales − COGS &nbsp; (or Sales + Closing stock − Opening stock − Purchases − Direct expenses)"))
    parts.append(formula("Net profit = Gross profit + Other income − Indirect expenses"))
    parts.append(h3("FIFO"))
    parts.append(raw_p(
        "<strong>Rule.</strong> Issues are taken from the <em>oldest</em> layer still in stock. "
        "Closing stock is the <em>latest</em> layers that remain."
    ))
    parts.append(formula(
        "Closing stock (FIFO) = remaining quantity in each leftover layer × that layer’s purchase cost",
    ))
    parts.append(formula("COGS (FIFO) = cost of layers issued  &nbsp;|&nbsp;  Check: Opening cost + Purchases cost = COGS + Closing stock"))
    parts.append(h3("Weighted average (WAM)"))
    parts.append(formula("Weighted average cost = Total cost of units on hand ÷ Total units on hand"))
    parts.append(raw_p(
        "<strong>Perpetual / moving average (usual exam method):</strong> recompute the average "
        "<em>after every purchase</em>. Issues go out at the average then ruling. Do not recompute on an issue."
    ))
    parts.append(raw_p(
        "<strong>Periodic average:</strong> one average for the whole period using opening + all purchases, "
        "then closing quantity × that average."
    ))
    parts.append(formula("Unit check: Opening qty + Purchases qty − Issues qty = Closing qty"))

    parts.append(h2("3. Depreciation"))
    parts.append(formula("Depreciable amount = Cost − Residual (scrap) value"))
    parts.append(raw_p("Cost includes purchase price, non-refundable taxes, freight inward, and installation needed to bring the asset to use."))
    parts.append(h3("Straight Line Method (SLM) / Original cost / Fixed instalment"))
    parts.append(formula("Annual depreciation = (Cost − Residual) ÷ Useful life in years"))
    parts.append(formula("SLM rate on original cost = (Annual depreciation ÷ Cost) × 100"))
    parts.append(formula("Part-year depreciation = Annual depreciation × (Months of use ÷ 12)"))
    parts.append(h3("Written Down Value (WDV) / Diminishing / Reducing balance"))
    parts.append(formula("Depreciation for the year = Book value at the start of the period × Rate"))
    parts.append(formula("Part-year WDV = Cost (or WDV) × Rate × (Months of use ÷ 12)"))
    parts.append(formula(
        "Optional WDV rate if life and scrap are given: R = 1 − (Scrap ÷ Cost)<sup>1/n</sup>",
        "MBA papers almost always give the rate. Do not invent a rate.",
    ))
    parts.append(h3("Sale of asset"))
    parts.append(formula("Net book value (NBV) on sale date = Cost − Accumulated depreciation till date of sale"))
    parts.append(formula("Profit on sale = Sale proceeds − NBV &nbsp;&nbsp;|&nbsp;&nbsp; Loss on sale = NBV − Sale proceeds"))

    parts.append(h2("4. Company accounts workings"))
    parts.append(formula("Revenue from operations + Other income = Total income"))
    parts.append(formula("Profit before tax = Total income − Total expenses ± Exceptional items"))
    parts.append(formula("Profit after tax = Profit before tax − Tax expense"))
    parts.append(formula("Changes in inventories = Opening inventory − Closing inventory  (a positive figure is an expense)"))
    parts.append(formula(
        "Manager’s commission on profit after commission = Profit before commission × Rate ÷ (100 + Rate)",
        "If the question says ‘on profit before commission’, just multiply profit × rate.",
    ))
    parts.append(formula("Trade receivables (net) = Gross receivables − Provision for doubtful debts"))
    parts.append(formula("PPE (net) = Gross cost − Accumulated depreciation"))
    parts.append(formula("Shareholders’ funds = Share capital + Reserves and surplus − Fictitious assets if any"))
    parts.append(formula(
        "New provision for doubtful debts = Required % × Debtors (after writing off further bad debts)",
    ))
    parts.append(formula(
        "If an old provision already exists: P&L charge (or credit) = New provision − Old provision + Fresh bad debts",
    ))

    parts.append(h2("5. Cash flow (indirect method) — derivations"))
    parts.append(formula("Net increase in cash = Operating (A) + Investing (B) + Financing (C)"))
    parts.append(formula("Closing cash & cash equivalents = Opening + Net increase  (must equal the Balance Sheet)"))
    parts.append(formula("Tax paid = Opening tax provision + Current tax charged − Closing tax provision  (adjust for prepaid tax if given)"))
    parts.append(formula("Dividend paid = Opening proposed/unpaid dividend + Dividend declared − Closing unpaid dividend"))
    parts.append(formula(
        "Purchase of PPE (if missing) : Opening cost + Purchases − Cost of asset sold = Closing cost",
    ))
    parts.append(formula(
        "Depreciation for the year (if missing): Opening accum. dep. + Dep. charged − Accum. dep. on asset sold = Closing accum. dep.",
    ))
    parts.append(formula("Sale proceeds of PPE = NBV of asset sold ± Profit/Loss on sale"))

    parts.append(h2("6. Ratio analysis"))
    parts.append(h3("Balance Sheet ratios (both figures from the Balance Sheet)"))
    parts.append(formula("Current ratio = Current assets ÷ Current liabilities"))
    parts.append(formula("Quick (acid-test) ratio = (Current assets − Inventory − Prepaid expenses) ÷ Current liabilities"))
    parts.append(formula("Absolute liquid / cash ratio = (Cash + Cash equivalents + Marketable securities) ÷ Current liabilities"))
    parts.append(formula("Debt–equity ratio = Long-term debt ÷ Shareholders’ funds"))
    parts.append(formula("Proprietary ratio = Shareholders’ funds ÷ Total assets"))
    parts.append(formula("Capital gearing ratio = (Preference capital + Long-term debt) ÷ Equity shareholders’ funds"))
    parts.append(formula("Fixed assets to long-term funds = Net fixed assets ÷ (Shareholders’ funds + Long-term debt)"))
    parts.append(formula("Current assets to proprietary funds = Current assets ÷ Shareholders’ funds"))
    parts.append(h3("Revenue ratios (both figures from the P&L)"))
    parts.append(formula("Gross profit ratio = (Gross profit ÷ Revenue from operations) × 100"))
    parts.append(formula("Net profit ratio = (Profit after tax ÷ Revenue from operations) × 100"))
    parts.append(formula("Operating profit ratio = (Operating profit (EBIT) ÷ Revenue from operations) × 100"))
    parts.append(formula("Operating ratio = (COGS + Operating expenses) ÷ Revenue from operations × 100"))
    parts.append(formula("Expense ratio = (Particular expense ÷ Revenue from operations) × 100"))
    parts.append(h3("Combined ratios (P&L figure with a Balance Sheet figure)"))
    parts.append(formula("Inventory turnover = COGS ÷ Average inventory"))
    parts.append(formula("Average inventory = (Opening inventory + Closing inventory) ÷ 2"))
    parts.append(formula("Inventory holding period (days) = 365 ÷ Inventory turnover"))
    parts.append(formula("Debtors turnover = Credit sales ÷ Average trade receivables"))
    parts.append(formula("Average collection period = 365 ÷ Debtors turnover"))
    parts.append(formula("Creditors turnover = Credit purchases ÷ Average trade payables"))
    parts.append(formula("Average payment period = 365 ÷ Creditors turnover"))
    parts.append(formula("Working capital turnover = Revenue from operations ÷ Working capital"))
    parts.append(formula("Working capital = Current assets − Current liabilities"))
    parts.append(formula("Fixed asset turnover = Revenue from operations ÷ Net fixed assets"))
    parts.append(formula("Capital turnover = Revenue from operations ÷ Capital employed"))
    parts.append(formula("Capital employed = Shareholders’ funds + Long-term debt  (or Net fixed assets + Working capital)"))
    parts.append(formula("ROCE = (EBIT ÷ Capital employed) × 100"))
    parts.append(formula("ROE = (Profit after tax ÷ Equity shareholders’ funds) × 100"))
    parts.append(formula("Return on assets = (PAT ÷ Total assets) × 100"))
    parts.append(formula("EPS = Profit after tax (less preference dividend) ÷ Number of equity shares"))
    parts.append(formula("Interest coverage = EBIT ÷ Interest"))
    parts.append(exam_tip(
        "If opening figures are not given, use closing balances for turnover ratios and write the assumption. "
        "Never mix a % ratio with a ‘times’ ratio without stating the unit."
    ))
    parts.append(chapter_close())
    return "".join(parts)
