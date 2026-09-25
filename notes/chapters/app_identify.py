import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "C",
        "Numerical Question Identification Guide",
        "The fastest marks in accounting come from recognising the question type in the first 20 seconds.",
        ["Journal / ledger / TB", "Inventory", "Depreciation", "Company accounts", "Cash flow", "Ratios"],
    ))
    parts.append(lead(
        "Read the last sentence of the question first — that is usually the requirement. Then scan for trigger words in the table below."
    ))
    parts.append(table(
        ["If the question gives / asks", "Topic", "Method / formulas to use"],
        [
            ["Transactions with dates; ‘journalise’ / ‘pass journal entries’", "Journal", "Two accounts, modern or golden rules, narration, equal debit and credit"],
            ["‘Post to ledger’ / ‘prepare ledger accounts’ / ‘T-accounts’", "Ledger", "Debit journal line → debit of that account; balance c/d on smaller side"],
            ["‘Prepare trial balance’ / list of balances", "Trial Balance", "Debit: assets, expenses, drawings. Credit: liabilities, capital, incomes. Totals must agree"],
            ["TB disagrees / ‘suspense’ / ‘errors’", "Errors & TB", "TB catches unequal posting, not omission, principle error, or compensating error"],
            ["FIFO / ‘first in first out’ / ‘latest lots remain’", "Inventory FIFO", "Issue oldest layers first; closing = latest layers × their costs; reconcile units and rupees"],
            ["Weighted average / WAM / moving average / average cost", "Inventory WAM", "Average = total cost ÷ total units after each purchase; issues at ruling average"],
            ["Store ledger / receipts and issues with dates and rates", "Inventory (FIFO or WAM as named)", "Columns: receipts, issues, balance — qty, rate, amount"],
            ["Closing stock value when prices are rising, compare methods", "FIFO vs WAM", "Rising prices: FIFO closing stock higher, profit higher than WAM"],
            ["COGS / gross profit from stock records", "Trading", "COGS = op stock + purchases − cl stock; GP = sales − COGS"],
            ["Straight line / original cost / equal instalment / fixed instalment", "Depreciation SLM", "(Cost − Scrap) ÷ Life; part-year × months/12"],
            ["WDV / diminishing / reducing balance / ‘on written down value’", "Depreciation WDV", "Opening WDV × rate; do not deduct scrap each year"],
            ["Purchased on 1 Oct / 1 July / ‘put to use’ mid-year", "Part-year depreciation", "Count months from date of use to year-end (Indian FY often 31 March)"],
            ["Installation / freight / erection on a machine", "Cost of asset", "Add to cost before computing depreciation"],
            ["Sold on … / ‘profit or loss on sale of asset’", "Asset disposal", "Charge dep till sale date; NBV vs sale proceeds"],
            ["Rate % p.a. on original cost", "Usually SLM", "Apply % to cost, then months if needed"],
            ["Rate % p.a. on WDV / on book value", "WDV", "Apply % to book value"],
            ["Schedule III / Companies Act 2013 / Statement of Profit and Loss", "Company P&L", "Revenue, other income, expense heads, tax, notes"],
            ["Prepare Balance Sheet of a company / major heads", "Company BS", "Equity & liabilities vs Assets; current vs non-current"],
            ["Notes to accounts", "Notes", "Share capital, reserves, PPE, inventory, revenue, other expenses"],
            ["Outstanding / unpaid / due but not paid", "Accrual", "Expense Dr. To Outstanding (liability)"],
            ["Prepaid / unexpired / paid in advance", "Prepaid", "Asset; reduce this year’s expense"],
            ["Accrued income / earned but not received", "Accrued income", "Income ↑ and current asset"],
            ["Received in advance / unearned", "Unearned income", "Income ↓ and current liability"],
            ["Provision for doubtful debts … % of debtors", "PDD", "Required provision on debtors after further bad debts; P&L gets the change"],
            ["Provision for tax", "Tax", "Tax expense and current liability"],
            ["Manager’s commission … % of profit after commission", "Commission", "Profit × r/(100+r)"],
            ["Closing inventory given as an adjustment", "Closing stock", "Current asset; reduces COGS / shown in changes in inventory"],
            ["‘Profit is not cash’ / prepare Cash Flow Statement / AS-3 / Ind AS-7 / indirect method", "CFS", "Start with profit before tax; add dep; WC changes; investing; financing"],
            ["Two years’ Balance Sheets plus additional information", "CFS (exam favourite)", "Derive purchases of FA, dep, tax paid, dividend paid with workings"],
            ["Depreciation in a cash flow question", "CFS operating", "ADD back (non-cash). Never show as investing outflow"],
            ["Profit on sale of machine in CFS", "CFS operating + investing", "Deduct profit from operating; show full sale proceeds under investing"],
            ["Issue of bonus shares / conversion of debentures", "CFS non-cash", "Do not show as cash inflow/outflow; ignore or disclose"],
            ["Current ratio / working capital ratio", "BS ratio", "CA ÷ CL"],
            ["Acid test / liquid / quick ratio", "BS ratio", "(CA − stock − prepaid) ÷ CL"],
            ["Cash ratio / absolute liquid", "BS ratio", "(Cash + marketable securities) ÷ CL"],
            ["Debt–equity / leverage / gearing", "BS ratio", "Long-term debt ÷ shareholders’ funds (state formula used)"],
            ["Gross profit ratio / GP %", "Revenue ratio", "GP ÷ Sales × 100"],
            ["Net profit ratio / NP %", "Revenue ratio", "PAT ÷ Sales × 100"],
            ["Operating ratio / operating profit ratio", "Revenue ratio", "Op. cost ÷ Sales; EBIT ÷ Sales"],
            ["Stock turnover / inventory turnover / how fast stock sells", "Combined", "COGS ÷ average stock; days = 365/turnover"],
            ["Debtors turnover / collection period", "Combined", "Credit sales ÷ average debtors"],
            ["Creditors turnover / payment period", "Combined", "Credit purchases ÷ average creditors"],
            ["ROCE / return on capital employed / overall profitability", "Combined", "EBIT ÷ capital employed × 100"],
            ["ROE / return on equity / return on shareholders’ funds", "Combined", "PAT ÷ equity funds × 100"],
            ["EPS / earnings per share", "Combined", "PAT (less pref. div.) ÷ number of equity shares"],
            ["Interest coverage / times interest earned", "Combined", "EBIT ÷ interest"],
            ["Current ratio 2.5, working capital ₹…, find CA and CL", "Reconstruct", "CA − CL = WC and CA = 2.5 CL → solve two equations"],
            ["GP ratio and stock turnover given, find sales / COGS / stock", "Reconstruct", "Link GP% to sales and COGS, turnover to COGS and average stock"],
            ["Ideal current ratio / comment on liquidity", "Interpretation", "Write the number AND what it means; compare with 2:1 or industry"],
        ],
        caption="Trigger words → method",
    ))
    parts.append(exam_tip(
        "If two methods are possible (FIFO vs WAM, SLM vs WDV) and the question is silent, write one line: "
        "‘Assuming FIFO / SLM as commonly used’ — then proceed. Do not freeze."
    ))
    parts.append(chapter_close())
    return "".join(parts)
