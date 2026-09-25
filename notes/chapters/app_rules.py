import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "B",
        "Accounting Rules Cheat Sheet",
        "A one-sitting recap of debit, credit, and the journal patterns you will actually write in the paper.",
        ["Golden rules", "Modern rules", "Normal balances", "Adjustment treatments",
         "Company vs sole proprietor", "Fifteen common journals"],
    ))

    parts.append(h2("Golden rules (traditional)"))
    parts.append(table(
        ["Type of account", "Rule", "Typical examples"],
        [
            ["Personal (people, firms, banks)", "Debit the receiver, Credit the giver", "Debtors, Creditors, Bank, Capital, Drawings"],
            ["Real (things you can own)", "Debit what comes in, Credit what goes out", "Cash, Furniture, Machinery, Stock, Building"],
            ["Nominal (incomes and expenses)", "Debit all expenses and losses, Credit all incomes and gains", "Rent, Salary, Sales, Commission, Depreciation"],
        ],
    ))
    parts.append(memory("Personal = people. Real = things. Nominal = names of incomes/expenses (they exist only in the books)."))

    parts.append(h2("Modern rules (recommended in the hall)"))
    parts.append(table(
        ["Element", "Increase", "Decrease", "Normal balance"],
        [
            ["Asset", "Debit", "Credit", "Debit"],
            ["Expense / Loss", "Debit", "Credit", "Debit"],
            ["Drawings", "Debit", "Credit", "Debit"],
            ["Liability", "Credit", "Debit", "Credit"],
            ["Capital", "Credit", "Debit", "Credit"],
            ["Income / Gain", "Credit", "Debit", "Credit"],
        ],
    ))
    parts.append(formula("Debit-nature items: Assets, Expenses, Drawings. Credit-nature items: Liabilities, Capital, Incomes."))

    parts.append(h2("How to build any journal in 40 seconds"))
    parts.append(steps([
        "Read the sentence. Underline the two (or more) things that changed.",
        "Name the accounts in textbook language (not ‘the guy we buy from’ — Creditor / Kabir A/c).",
        "Classify each: asset, liability, capital, income, expense.",
        "Ask: did it increase or decrease?",
        "Apply the modern table. One account is debited, one is credited (compound if more).",
        "Amounts on both sides must be equal.",
        "Write a narration in brackets: (Being …).",
    ]))

    parts.append(h2("Adjustment treatments (exam night)"))
    parts.append(table(
        ["Adjustment", "Journal", "P&L impact", "Balance Sheet impact"],
        [
            ["Outstanding expense (e.g. rent unpaid)", "Expense Dr. To Outstanding expense", "Expense ↑", "Current liability"],
            ["Prepaid expense (insurance paid in advance)", "Prepaid expense Dr. To Expense", "Expense ↓", "Current asset"],
            ["Accrued income (commission earned, not received)", "Accrued income Dr. To Income", "Income ↑", "Current asset"],
            ["Income received in advance", "Income Dr. To Income received in advance", "Income ↓", "Current liability"],
            ["Depreciation", "Depreciation Dr. To Accumulated depreciation (or Asset)", "Expense ↑", "Asset shown net (or cost less accum.)"],
            ["Closing stock (if not in TB)", "Closing stock Dr. To Trading / Purchases / Changes in inventory", "COGS ↓ / profit ↑", "Current asset"],
            ["Further bad debts", "Bad debts Dr. To Debtors", "Loss ↑", "Debtors ↓"],
            ["New provision for doubtful debts", "Profit & Loss Dr. To Provision", "Expense (or net with old provision)", "Deducted from debtors"],
            ["Interest on loan outstanding", "Interest Dr. To Outstanding interest", "Finance cost ↑", "Added to loan or shown current liability"],
            ["Provision for tax", "Tax expense Dr. To Provision for tax", "Profit ↓", "Current liability"],
            ["Drawings (sole proprietor)", "Drawings Dr. To Cash/Bank/Purchases", "Not an expense", "Deducted from capital"],
            ["Goods taken by owner", "Drawings Dr. To Purchases", "Purchases ↓", "Capital ↓"],
            ["Goods used as samples", "Advertisement / Sales promotion Dr. To Purchases", "Expense ↑", "Stock not inflated"],
        ],
    ))

    parts.append(h2("Company vs sole proprietor — do not mix"))
    parts.append(table(
        ["Item", "Sole proprietor", "Company"],
        [
            ["Owner’s money", "Capital", "Share capital + Reserves"],
            ["Owner taking money", "Drawings", "Dividend (not drawings)"],
            ["Format", "Trading, P&L, Balance Sheet (horizontal or vertical)", "Schedule III Statement of P&L and Balance Sheet"],
            ["Tax", "Often after P&L (owner’s tax)", "Tax expense of the company"],
            ["Loan from owner", "Often treated as capital or loan — follow question", "If director, usually a liability"],
        ],
    ))

    parts.append(h2("Fifteen journals you will write"))
    parts.append(journal([
        {"date": "—", "debit": "Cash / Bank A/c", "credit": "Capital A/c", "amount": "xx", "narration": "Being capital introduced"},
        {"date": "—", "debit": "Purchases A/c", "credit": "Cash / Creditor A/c", "amount": "xx", "narration": "Being goods purchased"},
        {"date": "—", "debit": "Cash / Debtor A/c", "credit": "Sales A/c", "amount": "xx", "narration": "Being goods sold"},
        {"date": "—", "debit": "Furniture A/c", "credit": "Cash A/c", "amount": "xx", "narration": "Being furniture purchased (asset, not purchases)"},
        {"date": "—", "debit": "Rent A/c", "credit": "Cash / Outstanding rent A/c", "amount": "xx", "narration": "Being rent of the period"},
        {"date": "—", "debit": "Creditor A/c", "credit": "Bank A/c", "amount": "xx", "narration": "Being payment to creditor"},
        {"date": "—", "debit": "Bank A/c", "credit": "Debtor A/c", "amount": "xx", "narration": "Being receipt from debtor"},
        {"date": "—", "debit": "Drawings A/c", "credit": "Cash A/c", "amount": "xx", "narration": "Being cash withdrawn by owner"},
        {"date": "—", "debit": "Depreciation A/c", "credit": "Accumulated depreciation A/c", "amount": "xx", "narration": "Being depreciation provided"},
        {"date": "—", "debit": "Profit & Loss A/c", "credit": "Depreciation A/c", "amount": "xx", "narration": "Being depreciation transferred (closing)"},
    ], "Core pattern journals (amounts as per question)"))

    parts.append(mistakes([
        "Debiting cash when cash comes in is correct; students often reverse cash because they think ‘credit means money in’ from banking language. Bank language ≠ accounting language.",
        "Buying furniture is not Purchases. Purchases = goods in which the firm trades.",
        "Drawings are not an expense. They never appear in the P&L as a cost.",
        "A company has no drawings account in the owner sense.",
        "Outstanding expense is a liability, not an asset. Prepaid is an asset, not an expense of this year.",
    ]))
    parts.append(chapter_close())
    return "".join(parts)
