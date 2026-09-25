#!/usr/bin/env python3
"""Chapter 4 — Company Accounts. Beginner-to-exam teaching notes."""

from __future__ import annotations

import sys

sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(
        chapter_open(
            "04",
            "Company Accounts",
            "You will present a company's Statement of Profit and Loss and Balance Sheet as per Schedule III, support them with notes, and process exam adjustments.",
            [
                "Schedule III of Companies Act, 2013",
                "Format and presentation of company financial statements",
                "Profit & Loss Account",
                "Balance Sheet",
                "Notes to Accounts",
                "Adjustments",
            ],
        )
    )
    parts.append(_why_companies())
    parts.append(_schedule_iii())
    parts.append(_current_noncurrent())
    parts.append(_pnl_format())
    parts.append(_northwind())
    parts.append(_balance_sheet())
    parts.append(_share_capital())
    parts.append(_reserves())
    parts.append(_notes_to_accounts())
    parts.append(_adjustments())
    parts.append(_horizon())
    parts.append(_exam_skills())
    parts.append(_practice())
    parts.append(chapter_close())
    return "".join(parts)


# ---------------------------------------------------------------------------
# 1. Why companies prepare financial statements
# ---------------------------------------------------------------------------


def _why_companies() -> str:
    s = []
    s.append(h2("Why a company prepares financial statements", "why-company-fs"))
    s.append(
        lead(
            "A company is not a person sitting with a cash box. It is a <strong>separate legal entity</strong> "
            "created under the Companies Act, 2013. The company owns the assets, the company owes the loans, "
            "and the company earns the profit. Shareholders own <em>shares</em>, not the furniture."
        )
    )
    s.append(
        definition(
            "Company financial statements are the Statement of Profit and Loss, the Balance Sheet, and the "
            "Notes to Accounts (plus a Cash Flow Statement, taught in a later chapter) prepared in the "
            "<strong>prescribed form</strong> so that owners, lenders, tax authorities and regulators get a "
            "<strong>true and fair view</strong> of the company's profit and financial position."
        )
    )
    s.append(
        simple(
            "Think of the company as a cricket club that is a legal 'person'. The club's bank account is not "
            "the captain's bank account. At year-end the club must publish: how much it earned and spent "
            "(Profit and Loss), and what it owns and owes (Balance Sheet). The law even tells you "
            "<em>which headings to use and in which order</em>. That law-table is Schedule III."
        )
    )
    s.append(
        why(
            "Shareholders put in money but do not run the shop every day — directors do. Lenders decide "
            "whether to give a loan. The tax department computes tax on profit. SEBI and the Registrar of "
            "Companies check that listed / registered companies are not hiding losses. Without a common "
            "format, every company would invent its own sheet and nobody could compare two companies. "
            "The Companies Act therefore <strong>mandates</strong> these statements. They are not optional homework."
        )
    )
    s.append(
        real_life(
            "You hold 100 shares of Horizon Ltd. You cannot walk into the factory and count the machines. "
            "You wait for the annual report. The Statement of Profit and Loss tells you whether the company "
            "made a profit this year. The Balance Sheet tells you whether that profit is sitting in cash, "
            "in unsold stock, or is already owed to the bank. Notes tell you the story behind the big numbers "
            "— how many shares exist, how old the plant is, how much dividend is proposed."
        )
    )
    s.append(
        logic(
            "Accounting equation still holds: <strong>Assets = Equity + Liabilities</strong>. "
            "For a sole trader, 'Equity' is Capital + Profits − Drawings. For a company, 'Equity' is "
            "<strong>Share capital + Reserves and surplus</strong>. There are <em>no drawings</em>. "
            "Owners take money out only as <strong>dividend</strong> (and only if the company declares it). "
            "Profit of the year flows into Reserves and surplus, not into a capital account with a person's name."
        )
    )
    s.append(
        connect(
            "Chapters on journal, ledger, trial balance and adjustments still apply. You still debit expenses "
            "and assets, credit incomes and liabilities. What changes is the <strong>wrapping paper</strong>: "
            "the face of the statements must follow Schedule III headings, and some items (tax, dividend, "
            "share capital) exist only because the owner is a company, not a person."
        )
    )
    s.append(h3("Company vs sole trader — what actually changes in the exam"))
    s.append(
        table(
            ["Point", "Sole trader / partnership", "Company (this chapter)"],
            [
                [
                    "Owner's identity",
                    "The person and the business are mixed",
                    "Company is a separate legal person",
                ],
                [
                    "Owner's account",
                    "Capital, drawings",
                    "Share capital + reserves. No drawings",
                ],
                [
                    "Format of statements",
                    "You may use any clear T-shape or vertical",
                    "Must follow Schedule III headings and order",
                ],
                [
                    "Profit and Loss heading",
                    "Trading and P&L Account",
                    "Statement of Profit and Loss",
                ],
                [
                    "Tax on profit",
                    "Owner pays tax personally; often ignored in the books",
                    "Company pays tax. Provision for tax is an expense and a liability",
                ],
                [
                    "Distribution of profit",
                    "Drawings, or transfer to capital",
                    "Dividend. Proposed dividend is a note, not a liability, until declared",
                ],
                [
                    "Comparatives",
                    "Usually current year only",
                    "Schedule III wants previous-year figures too (exams often give only current year)",
                ],
            ],
            caption="What you must switch in your brain when the question says 'Ltd'",
        )
    )
    s.append(
        keypoint(
            "If the name ends with Ltd or Limited (or Pvt Ltd), you are in company accounts. "
            "Do not open a Drawings account. Do not use a sole-trader Trading Account heading on the face. "
            "Use Statement of Profit and Loss and Balance Sheet as per Schedule III of the Companies Act, 2013."
        )
    )
    s.append(
        exam_answer(
            "A company is a separate legal entity. Its financial statements give a true and fair view of "
            "profit and financial position to shareholders, lenders, tax authorities and regulators. "
            "Preparation is mandatory under the Companies Act, 2013, in the form prescribed by Schedule III."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 2. Schedule III
# ---------------------------------------------------------------------------


def _schedule_iii() -> str:
    s = []
    s.append(h2("Schedule III of the Companies Act, 2013 — what it is", "schedule-iii"))
    s.append(
        definition(
            "Schedule III is the <strong>prescribed format</strong> for the Balance Sheet and the Statement of "
            "Profit and Loss of Indian companies. It is a schedule attached to the Companies Act, 2013. "
            "When an exam says 'as per Schedule III' or 'as per Companies Act 2013', it means: use these "
            "headings, this order, these groupings, figures in ₹, and (in real life) previous-year comparatives."
        )
    )
    s.append(
        simple(
            "Schedule III is the seating chart of the annual report. It does not tell you how to <em>calculate</em> "
            "depreciation or closing stock — those rules come from accounting standards and from this chapter's "
            "adjustments. It only tells you <em>where each calculated figure sits</em> on the page. "
            "Share capital on this line, trade payables on that line, finance costs on that line. No mixing."
        )
    )
    s.append(
        why(
            "Without a common chart, one company would put bank overdraft under 'sundry creditors' and another "
            "under 'loans'. Analysts, bankers and examiners would waste time hunting. Schedule III is the "
            "agreed map of India for company statements. MBA exams mark you down for putting a figure under "
            "the wrong head even when the rupee amount is correct."
        )
    )
    s.append(
        real_life(
            "Open any annual report of an Indian listed company. You will see 'Balance Sheet as at 31 March …' "
            "with Equity and Liabilities first and Assets below, using exactly the heads in this chapter: "
            "Shareholders' funds, Non-current liabilities, Current liabilities, Non-current assets, Current assets. "
            "That is Schedule III at work, not a designer's choice."
        )
    )
    s.append(
        logic(
            "Schedule III has two divisions. <strong>Division I</strong> is for companies that follow Accounting "
            "Standards (AS) — this is the format MBA / university papers almost always want. "
            "<strong>Division II</strong> is for Ind AS companies (mostly listed and large companies). "
            "The line items look similar. We teach Division I vertical format. "
            "The old Companies Act, 1956 horizontal (T-shape) company Balance Sheet is gone. Do not draw it."
        )
    )
    s.append(
        format_box(
            "What 'as per Schedule III' means in an answer sheet",
            ul(
                [
                    "<strong>Vertical format</strong> — one column of figures (plus a previous-year column in real life).",
                    "<strong>Prescribed headings and order</strong> — do not rename 'Trade payables' as 'Sundry creditors' on the face.",
                    "<strong>Figures in rupees</strong> — and round off as per size in real filings (exams usually want the given rupees).",
                    "<strong>Previous-year comparatives</strong> — mention them; if the question gives only one year, present one year.",
                    "<strong>Notes to Accounts</strong> — face of the statement is a summary; detail lives in notes, with note numbers on the face.",
                    "<strong>Current vs non-current split</strong> — 12-month / operating-cycle rule, taught next.",
                    "<strong>True and fair</strong> — the format is compulsory, but the numbers must still be honest and complete.",
                ]
            ),
        )
    )
    s.append(
        steps(
            [
                "Read the question. If it says Schedule III / Companies Act 2013 / 'in the prescribed form', lock this format.",
                "Extract the trial balance. Split every item into: P&L (income/expense) or Balance Sheet (asset/liability/equity).",
                "Process adjustments (closing stock, outstanding, prepaid, depreciation, provisions, tax, commission).",
                "Prepare Notes first (share capital, reserves, PPE, receivables, expenses). Totals from notes go to the face.",
                "Write Statement of Profit and Loss with Roman numbering I to IX as in the format.",
                "Write Balance Sheet with Equity and Liabilities first, then Assets. Both sides must <strong>tie</strong>.",
                "Show working notes for COGS, depreciation, employee benefits, other expenses, net receivables.",
            ]
        )
    )
    s.append(
        warn(
            "Rounding in real Schedule III: companies with turnover below ₹100 crore may round to hundreds, "
            "thousands, lakhs or millions; larger companies to lakhs, millions or crores. "
            "In your exam, unless told to round, write the full rupee amounts with Indian commas (₹1,00,000)."
        )
    )
    s.append(
        exam_answer(
            "Schedule III of the Companies Act, 2013 prescribes the form of Balance Sheet and Statement of "
            "Profit and Loss of a company. It requires vertical presentation, a current / non-current "
            "classification, specified major heads in a fixed order, corresponding previous-year figures, "
            "and supporting Notes to Accounts, so that the statements give a true and fair view and are comparable."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 3. Current vs non-current
# ---------------------------------------------------------------------------


def _current_noncurrent() -> str:
    s = []
    s.append(h3("Current vs non-current — the 12-month operating-cycle rule"))
    s.append(
        definition(
            "Every asset and every liability on a company Balance Sheet is classified as "
            "<strong>current</strong> or <strong>non-current</strong>. "
            "Current means 'turning into cash, or falling due, in the normal operating cycle or within 12 months'. "
            "Non-current means 'held for the longer haul'."
        )
    )
    s.append(
        simple(
            "Operating cycle is the time from buying raw material (or goods) to collecting cash from the customer. "
            "A bakery's cycle may be a few days. A shipbuilder's cycle may be three years. "
            "If you cannot identify the cycle, the law says: treat it as <strong>12 months</strong>. "
            "Exam default is 12 months unless the question gives a longer cycle."
        )
    )
    s.append(
        logic(
            "<strong>An asset is current</strong> if any one of these is true: (a) it will be realised or sold in the "
            "operating cycle; (b) it is held mainly for trading; (c) it will be realised within 12 months after "
            "the Balance Sheet date; (d) it is cash or a cash equivalent. Otherwise it is non-current. "
            "<br/><br/>"
            "<strong>A liability is current</strong> if: (a) it will be settled in the operating cycle; (b) it is held "
            "for trading; (c) it is due within 12 months; or (d) the company has no unconditional right to defer "
            "settlement beyond 12 months. Otherwise it is non-current."
        )
    )
    s.append(
        table(
            ["Item", "Classification", "Why"],
            [
                ["Land and building used as factory", "Non-current asset (PPE)", "Held to use for years, not to sell this year"],
                ["Stock of goods", "Current asset (Inventories)", "Expected to be sold in the cycle"],
                ["Trade receivables", "Current asset", "Customers usually pay within the cycle / 12 months"],
                ["12% Debentures repayable after 5 years", "Non-current liability", "Not due within 12 months"],
                ["Instalment of that loan due next year", "Current liability (other current liabilities)", "Due within 12 months — 'current maturity'"],
                ["Bank overdraft", "Current liability (short-term borrowings)", "Repayable on demand"],
                ["Trade payables", "Current liability", "Suppliers of goods, settled in the cycle"],
                ["Outstanding salary", "Current liability (other current liabilities)", "Wages already earned, unpaid, due now"],
                ["Provision for tax", "Current liability (short-term provisions)", "Tax for this year, payable soon"],
                ["Prepaid insurance for next 8 months", "Current asset (other current assets)", "Benefit within 12 months"],
                ["Long-term investment in another company's shares", "Non-current asset", "Held for more than 12 months"],
                ["Income received in advance", "Current liability (other current liabilities)", "You still owe the service"],
            ],
            caption="Quick classification — learn these; they are 2-mark gifts",
        )
    )
    s.append(
        example(
            "4.1",
            "Easy",
            "Classify ten items as current or non-current",
            p("Horizon Ltd's trial balance includes the items below. Classify each for a Schedule III Balance Sheet.")
            + table(
                ["Item", "Your classification"],
                [
                    ["Plant purchased for the factory", "Non-current asset — PPE"],
                    ["Goods unsold on 31 March", "Current asset — Inventories"],
                    ["Amount due from customers", "Current asset — Trade receivables"],
                    ["Cash at bank", "Current asset — Cash and cash equivalents"],
                    ["Equity share capital", "Shareholders' funds (neither current nor non-current liability)"],
                    ["General reserve", "Shareholders' funds — Reserves and surplus"],
                    ["10-year debentures", "Non-current liability — Long-term borrowings"],
                    ["Creditors for goods", "Current liability — Trade payables"],
                    ["Bank overdraft", "Current liability — Short-term borrowings"],
                    ["Outstanding interest on debentures", "Current liability — Other current liabilities"],
                ],
            )
            + p(
                "Share capital and reserves are ",
                b("equity"),
                ", not liabilities. They sit at the top of Equity and Liabilities because they represent owners, not outsiders.",
            ),
        )
    )
    s.append(
        mistakes(
            [
                "Putting bank overdraft under Trade payables — overdraft is a borrowing, not a supplier balance.",
                "Leaving next year's instalment of a 5-year loan inside Long-term borrowings — split the current maturity out.",
                "Calling outstanding rent a Trade payable — rent is not a purchase of stock-in-trade; it is Other current liabilities.",
                "Treating share capital as a non-current liability — it is equity.",
            ]
        )
    )
    s.append(
        memory(
            "Current = cash within a year (or the cycle). Non-current = the long stay. "
            "Liabilities tell you who funded the assets. Notes are the footnotes of the story."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 4. Statement of Profit and Loss — format and every line
# ---------------------------------------------------------------------------


def _pnl_format() -> str:
    s = []
    s.append(h2("Statement of Profit and Loss — full exam format", "pnl"))
    s.append(
        definition(
            "The Statement of Profit and Loss is the company's income statement for a period (usually the year "
            "ended 31 March). It starts with revenue, deducts expenses in a prescribed order, and ends with "
            "<strong>Profit for the period</strong> after tax. Under Schedule III it is a vertical statement "
            "with Roman numbered lines I to IX."
        )
    )
    s.append(
        simple(
            "Sole traders often split 'Trading Account' (gross profit) and 'P&L Account' (net profit). "
            "A company still computes the same ideas, but on the <em>face</em> you show one Statement of Profit "
            "and Loss. Gross profit is not a mandatory face heading. Cost of goods sold appears as "
            "purchases, materials, and changes in inventories — three separate lines."
        )
    )
    s.append(
        why(
            "Investors want to see, in a standard order: how much the operations earned, how much other income "
            "arrived, how costs broke into materials, people, interest, depreciation and the rest, and how much "
            "tax ate. Mixing interest into 'other expenses' would hide how heavily the company is borrowed. "
            "That is why Finance costs is its own line."
        )
    )
    s.append(
        format_box(
            "Statement of Profit and Loss (Schedule III, Division I)",
            table(
                ["", "Particulars", "Note", "₹"],
                [
                    ["I", "Revenue from operations", "1", ""],
                    ["II", "Other income", "2", ""],
                    ["III", "Total income (I + II)", "", ""],
                    ["IV", "Expenses", "", ""],
                    ["", "&nbsp;&nbsp;Cost of materials consumed", "", ""],
                    ["", "&nbsp;&nbsp;Purchases of stock-in-trade", "", ""],
                    ["", "&nbsp;&nbsp;Changes in inventories of finished goods, work-in-progress and stock-in-trade", "", ""],
                    ["", "&nbsp;&nbsp;Employee benefits expense", "3", ""],
                    ["", "&nbsp;&nbsp;Finance costs", "4", ""],
                    ["", "&nbsp;&nbsp;Depreciation and amortisation expense", "5", ""],
                    ["", "&nbsp;&nbsp;Other expenses", "6", ""],
                    ["", "Total expenses", "", ""],
                    ["V", "Profit before exceptional items and tax (III − IV)", "", ""],
                    ["VI", "Exceptional items", "", ""],
                    ["VII", "Profit before tax (V − VI)", "", ""],
                    ["VIII", "Tax expense", "", ""],
                    ["", "&nbsp;&nbsp;Current tax", "", ""],
                    ["", "&nbsp;&nbsp;Deferred tax", "", ""],
                    ["IX", "Profit (loss) for the period (VII − VIII)", "", ""],
                ],
                caption="Face of the Statement of Profit and Loss — learn the Roman numbers",
                foot="Note numbers on the face point to Notes to Accounts. Previous-year column omitted when the question gives one year only.",
            ),
        )
    )
    s.append(h3("Line-by-line: what goes where"))

    s.append(h4("I  Revenue from operations"))
    s.append(
        p(
            "This is money from the company's ",
            b("main business"),
            " — selling goods or rendering the services it exists to sell. For a trading company: sales of goods. "
            "For a manufacturer: sales of finished goods. For a software firm: fee income. "
            "Also included: other operating revenue such as export incentives linked to sales.",
        )
    )
    s.append(
        p(
            "Sales are shown ",
            b("net of returns"),
            ". GST collected is not your income (it is a liability to government) — exam TBs usually give sales already exclusive of tax. "
            "If the TB shows 'Sales 9,50,000' that is line I, unless the question says it includes something non-operating.",
        )
    )

    s.append(h4("II  Other income"))
    s.append(
        p(
            "Income that is ",
            b("not the main operations"),
            ". Typical exam items:",
        )
    )
    s.append(
        ul(
            [
                "<strong>Interest</strong> received on deposits or on investments.",
                "<strong>Dividend</strong> received on shares held as investments.",
                "<strong>Profit on sale of a fixed asset</strong> (PPE) or of an investment.",
                "<strong>Rent received</strong> if renting out is not the company's business (a trading company sub-letting one floor).",
                "Miscellaneous income, commission received (when commission is not the business).",
            ]
        )
    )
    s.append(
        keypoint(
            "Same rupee, different shelf. Interest <em>earned</em> on a bank deposit is Other income. "
            "Interest <em>paid</em> on a loan is Finance costs. Dividend received is Other income. "
            "Dividend paid is not an expense of the P&L at all — it is an appropriation of reserves."
        )
    )

    s.append(h4("III  Total income (I + II)"))
    s.append(
        p(
            "Just add. Show the working. If Revenue is ₹9,50,000 and Other income is ₹39,000, Total income = ₹9,89,000."
        )
    )

    s.append(h4("IV  Expenses — each prescribed line"))
    s.append(
        table(
            ["Line", "What it means", "Exam examples", "What it is NOT"],
            [
                [
                    "Cost of materials consumed",
                    "Raw materials used by a manufacturer: Opening RM + Purchases − Closing RM",
                    "Steel used to make machines",
                    "Not used by a pure trading company (they have no 'materials')",
                ],
                [
                    "Purchases of stock-in-trade",
                    "Goods bought for resale, as they are",
                    "A trader buying fans to sell fans",
                    "Not raw material. Not a fixed asset purchase",
                ],
                [
                    "Changes in inventories of FG, WIP, stock-in-trade",
                    "Opening minus closing of those stocks. Increase in stock is a negative expense (credit). Decrease is a positive expense",
                    "Opening stock ₹80,000, closing ₹1,10,000 → change = (₹30,000)",
                    "Raw material change sits inside 'materials consumed', not here",
                ],
                [
                    "Employee benefits expense",
                    "Cost of people: salaries, wages, bonus, contribution to PF, staff welfare, manager's commission on profit",
                    "Salaries ₹1,10,000 + outstanding ₹10,000 = ₹1,20,000",
                    "Not contractor bills for repairs (those are Other expenses). Not drawings",
                ],
                [
                    "Finance costs",
                    "Cost of borrowed money: interest on loans, debentures, overdraft; other borrowing costs",
                    "12% of ₹2,00,000 debentures = ₹24,000 for the year",
                    "Not repayment of the loan principal. Not dividend on shares",
                ],
                [
                    "Depreciation and amortisation",
                    "Wear-and-tear of PPE (depreciation) and writing off intangibles such as patents (amortisation)",
                    "Building 5%, plant 10%, furniture 10%",
                    "Not the purchase of a new machine (that is an asset)",
                ],
                [
                    "Other expenses",
                    "Everything left: rent, insurance, electricity, advertisement, bad debts, provision for doubtful debts, samples, repairs, audit fee",
                    "Rent, prepaid-adjusted insurance, electricity, ads, bad debts, extra PFDD",
                    "Not materials, not salaries, not interest, not depreciation — those have their own lines",
                ],
            ],
            caption="The seven expense lines — put each voucher on the correct one",
        )
    )
    s.append(
        formula(
            "Change in inventories (FG / WIP / stock-in-trade) = Opening inventory − Closing inventory",
            "If closing is bigger than opening, the change is negative and it reduces total expenses. "
            "That is the Schedule III way of showing that you produced or bought more than you sold. "
            "Cost of goods sold for a trader = Opening stock + Purchases − Closing stock, which equals "
            "Purchases of stock-in-trade + Changes in inventories.",
        )
    )
    s.append(
        p(
            "Worked micro-example of the identity. Opening inventory ₹80,000. Purchases ₹6,20,000. Closing inventory ₹1,10,000."
        )
    )
    s.append(
        ul(
            [
                "Goods available = ₹80,000 + ₹6,20,000 = ₹7,00,000.",
                "COGS = ₹7,00,000 − ₹1,10,000 = ₹5,90,000.",
                "Schedule III lines: Purchases of stock-in-trade ₹6,20,000; Changes in inventories = ₹80,000 − ₹1,10,000 = (₹30,000).",
                "₹6,20,000 + (₹30,000) = ₹5,90,000. Same COGS. Always check this identity before you proceed.",
            ]
        )
    )

    s.append(h4("V  Profit before exceptional items and tax (III − IV)"))
    s.append(p("Total income minus total expenses. This is the ordinary operating-and-other result."))

    s.append(h4("VI  Exceptional items"))
    s.append(
        p(
            "Material items that are unusual or arise from a non-recurring event — for example profit on sale of a whole division, "
            "or a large one-time legal settlement. Rare in exam trial balances. If none, write ",
            b("Nil"),
            " or skip the amount. Do not dump ordinary 'other expenses' here.",
        )
    )

    s.append(h4("VII  Profit before tax"))
    s.append(p("Line V minus exceptional items. If exceptional is Nil, V = VII."))

    s.append(h4("VIII  Tax expense"))
    s.append(
        p(
            b("Current tax"),
            " is the income-tax payable on this year's taxable profit — in exams this is the given 'Provision for tax'. ",
            b("Deferred tax"),
            " arises when accounting profit and taxable profit differ because of timing differences "
            "(for example depreciation in books ≠ depreciation in the Income-tax Act). "
            "Deferred tax liability (DTL) sits under non-current liabilities; deferred tax asset (DTA) under non-current assets. "
            "Most MBA problems only give current tax. Charge it as tax expense; credit Provision for tax (short-term provision).",
        )
    )

    s.append(h4("IX  Profit for the period"))
    s.append(
        p(
            "This is the bottom line. It is ",
            b("not"),
            " drawn by the owners. It is transferred to ",
            b("Surplus in Reserves and surplus"),
            " on the Balance Sheet. That is how a profitable year makes shareholders' funds grow.",
        )
    )
    s.append(
        identify(
            "If the question says 'prepare the Statement of Profit and Loss as per Schedule III / Companies Act 2013', "
            "use the Roman numbered format above. If it only says 'prepare a Profit and Loss Account of the company', "
            "still use this format — examiners expect Schedule III once the entity is a company."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 5. Northwind — full worked P&L (moderate)
# ---------------------------------------------------------------------------


def _northwind() -> str:
    s = []
    s.append(h3("Worked Statement of Profit and Loss — Northwind Trading Ltd"))
    s.append(
        example(
            "4.2",
            "Moderate",
            "Northwind Trading Ltd — from trial balance to Schedule III P&L (and a compact Balance Sheet)",
            _northwind_body(),
        )
    )
    return "".join(s)


def _northwind_body() -> str:
    s = []
    s.append(
        p(
            "Northwind Trading Ltd is a small trading company (it buys goods and resells them — no factory). "
            "Year ended 31 March 2026. We first prove the trial balance, then process four adjustments, "
            "then write the Statement of Profit and Loss with note numbers, then a compact Balance Sheet so you see both faces before the exam-length illustration."
        )
    )
    s.append(h4("Trial balance as at 31 March 2026"))
    s.append(
        table(
            ["Particulars", "Dr (₹)", "Cr (₹)"],
            [
                ["Equity share capital (shares of ₹10)", "", "2,00,000"],
                ["10% Bank loan (repayable in 2029)", "", "1,00,000"],
                ["General reserve", "", "20,000"],
                ["Surplus (opening credit balance)", "", "30,000"],
                ["Sales", "", "5,40,000"],
                ["Trade payables", "", "40,000"],
                ["Plant", "2,00,000", ""],
                ["Furniture", "40,000", ""],
                ["Purchases", "3,60,000", ""],
                ["Opening inventory", "50,000", ""],
                ["Salaries", "70,000", ""],
                ["Rent", "36,000", ""],
                ["Insurance", "8,000", ""],
                ["Advertisement", "15,000", ""],
                ["Interest on bank loan", "10,000", ""],
                ["Bad debts", "6,000", ""],
                ["Trade receivables", "80,000", ""],
                ["Cash at bank", "55,000", ""],
                ["<strong>Total</strong>", "<strong>9,30,000</strong>", "<strong>9,30,000</strong>"],
            ],
            caption="Northwind Trading Ltd — trial balance (already tied)",
            foot="Check: 2,00,000 + 40,000 + 3,60,000 + 50,000 + 70,000 + 36,000 + 8,000 + 15,000 + 10,000 + 6,000 + 80,000 + 55,000 = 9,30,000 Dr. "
            "2,00,000 + 1,00,000 + 20,000 + 30,000 + 5,40,000 + 40,000 = 9,30,000 Cr.",
        )
    )
    s.append(p(b("Adjustments")))
    s.append(
        ol(
            [
                "Closing inventory ₹70,000.",
                "Depreciate plant 10% and furniture 10% (straight line on the given cost; residual is Nil in this problem).",
                "Outstanding rent ₹4,000.",
                "Provision for tax ₹7,000.",
            ]
        )
    )
    s.append(h4("Workings — every multiplication shown"))
    s.append(
        table(
            ["Working", "Computation", "₹"],
            [
                ["Revenue from operations", "Sales as per TB", "5,40,000"],
                ["Other income", "None in TB", "Nil"],
                ["Purchases of stock-in-trade", "Purchases as per TB", "3,60,000"],
                ["Changes in inventories", "Opening ₹50,000 − Closing ₹70,000", "(20,000)"],
                ["COGS check", "₹50,000 + ₹3,60,000 − ₹70,000", "3,40,000"],
                ["Employee benefits", "Salaries ₹70,000 (no outstanding on salaries)", "70,000"],
                [
                    "Finance costs",
                    "10% × ₹1,00,000 = 10/100 × 1,00,000. TB already has ₹10,000, so the year is fully charged. Nothing outstanding.",
                    "10,000",
                ],
                ["Depreciation — plant", "10/100 × ₹2,00,000 = ₹20,000", "20,000"],
                ["Depreciation — furniture", "10/100 × ₹40,000 = ₹4,000", "4,000"],
                ["Depreciation — total", "₹20,000 + ₹4,000", "24,000"],
                ["Rent (other expenses)", "₹36,000 + outstanding ₹4,000", "40,000"],
                ["Insurance", "As per TB (no prepaid given)", "8,000"],
                ["Advertisement", "As per TB", "15,000"],
                ["Bad debts", "As per TB", "6,000"],
                ["Other expenses — total", "₹40,000 + ₹8,000 + ₹15,000 + ₹6,000", "69,000"],
                [
                    "Total expenses",
                    "₹3,60,000 + (₹20,000) + ₹70,000 + ₹10,000 + ₹24,000 + ₹69,000 = ₹3,40,000 + ₹70,000 = ₹4,10,000; + ₹10,000 = ₹4,20,000; + ₹24,000 = ₹4,44,000; + ₹69,000",
                    "5,13,000",
                ],
                ["Profit before tax", "₹5,40,000 − ₹5,13,000", "27,000"],
                ["Tax expense", "Provision for tax (given)", "7,000"],
                ["Profit for the period", "₹27,000 − ₹7,000", "20,000"],
            ],
            caption="Northwind — workings that feed the face and the notes",
        )
    )
    s.append(h4("Statement of Profit and Loss for the year ended 31 March 2026"))
    s.append(
        table(
            ["", "Particulars", "Note", "₹"],
            [
                ["I", "Revenue from operations", "1", "5,40,000"],
                ["II", "Other income", "", "—"],
                ["III", "Total income (I + II)", "", "<strong>5,40,000</strong>"],
                ["IV", "Expenses", "", ""],
                ["", "&nbsp;&nbsp;Purchases of stock-in-trade", "", "3,60,000"],
                ["", "&nbsp;&nbsp;Changes in inventories of stock-in-trade", "2", "(20,000)"],
                ["", "&nbsp;&nbsp;Employee benefits expense", "3", "70,000"],
                ["", "&nbsp;&nbsp;Finance costs", "4", "10,000"],
                ["", "&nbsp;&nbsp;Depreciation and amortisation expense", "5", "24,000"],
                ["", "&nbsp;&nbsp;Other expenses", "6", "69,000"],
                ["", "Total expenses", "", "<strong>5,13,000</strong>"],
                ["V", "Profit before exceptional items and tax (III − IV)", "", "27,000"],
                ["VI", "Exceptional items", "", "—"],
                ["VII", "Profit before tax", "", "27,000"],
                ["VIII", "Tax expense — current tax", "7", "7,000"],
                ["IX", "Profit for the period", "", "<strong>20,000</strong>"],
            ],
            caption="Northwind Trading Ltd — Statement of Profit and Loss (Schedule III)",
        )
    )
    s.append(h4("Notes referred to above (extract)"))
    s.append(
        table(
            ["Note", "Content", "₹"],
            [
                ["1 Revenue from operations", "Sale of products (traded goods)", "5,40,000"],
                [
                    "2 Changes in inventories",
                    "Stock-in-trade: opening ₹50,000 less closing ₹70,000. Increase in stock is shown as a credit (negative expense).",
                    "(20,000)",
                ],
                ["3 Employee benefits", "Salaries", "70,000"],
                ["4 Finance costs", "Interest on 10% bank loan (10/100 × ₹1,00,000)", "10,000"],
                [
                    "5 Depreciation",
                    "Plant ₹20,000 (10/100 × ₹2,00,000) + Furniture ₹4,000 (10/100 × ₹40,000)",
                    "24,000",
                ],
                [
                    "6 Other expenses",
                    "Rent ₹40,000 + Insurance ₹8,000 + Advertisement ₹15,000 + Bad debts ₹6,000",
                    "69,000",
                ],
                ["7 Tax expense", "Current tax (provision)", "7,000"],
            ],
        )
    )
    s.append(
        p(
            "Profit ₹20,000 is ",
            b("not"),
            " cash in a drawer. It is the residue of income over expenses. It will sit inside Reserves and surplus. "
            "Follow it onto the Balance Sheet.",
        )
    )
    s.append(h4("Compact Balance Sheet as at 31 March 2026 (so the P&L is not left hanging)"))
    s.append(
        p(
            "PPE = Plant (₹2,00,000 − ₹20,000) + Furniture (₹40,000 − ₹4,000) = ₹1,80,000 + ₹36,000 = ₹2,16,000. "
            "Current assets = Inventory ₹70,000 + Trade receivables ₹80,000 + Cash ₹55,000 = ₹2,05,000. "
            "Total assets = ₹2,16,000 + ₹2,05,000 = ₹4,21,000."
        )
    )
    s.append(
        p(
            "Share capital ₹2,00,000. Reserves = General reserve ₹20,000 + Surplus (₹30,000 opening + ₹20,000 profit) = ₹70,000. "
            "Shareholders' funds = ₹2,70,000. Non-current liability (bank loan) ₹1,00,000. "
            "Current liabilities = Trade payables ₹40,000 + Outstanding rent ₹4,000 + Provision for tax ₹7,000 = ₹51,000. "
            "Total equity and liabilities = ₹2,70,000 + ₹1,00,000 + ₹51,000 = ₹4,21,000. ",
            b("Tied."),
        )
    )
    s.append(
        table(
            ["Particulars", "Note", "₹"],
            [
                ["<strong>I  EQUITY AND LIABILITIES</strong>", "", ""],
                ["1. Shareholders' funds", "", ""],
                ["&nbsp;&nbsp;(a) Share capital", "", "2,00,000"],
                ["&nbsp;&nbsp;(b) Reserves and surplus", "8", "70,000"],
                ["2. Non-current liabilities", "", ""],
                ["&nbsp;&nbsp;(a) Long-term borrowings (10% bank loan)", "", "1,00,000"],
                ["3. Current liabilities", "", ""],
                ["&nbsp;&nbsp;(a) Trade payables", "", "40,000"],
                ["&nbsp;&nbsp;(b) Other current liabilities (outstanding rent)", "", "4,000"],
                ["&nbsp;&nbsp;(c) Short-term provisions (provision for tax)", "", "7,000"],
                ["<strong>Total</strong>", "", "<strong>4,21,000</strong>"],
                ["<strong>II  ASSETS</strong>", "", ""],
                ["1. Non-current assets", "", ""],
                ["&nbsp;&nbsp;(a) Property, plant and equipment", "5", "2,16,000"],
                ["2. Current assets", "", ""],
                ["&nbsp;&nbsp;(a) Inventories", "", "70,000"],
                ["&nbsp;&nbsp;(b) Trade receivables", "", "80,000"],
                ["&nbsp;&nbsp;(c) Cash and cash equivalents", "", "55,000"],
                ["<strong>Total</strong>", "", "<strong>4,21,000</strong>"],
            ],
            caption="Northwind Trading Ltd — Balance Sheet (compact, Schedule III)",
            foot="Note 8 Reserves: General reserve ₹20,000 + Surplus ₹50,000 (opening ₹30,000 + profit ₹20,000) = ₹70,000.",
        )
    )
    s.append(
        exam_tip(
            "Always prove two things: (1) the trial balance totals before you touch adjustments; "
            "(2) the Balance Sheet totals after adjustments. If they do not tie, a working is wrong — "
            "usually closing stock omitted on the asset side, or outstanding interest omitted as both expense and liability."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 6. Balance Sheet
# ---------------------------------------------------------------------------


def _balance_sheet() -> str:
    s = []
    s.append(h2("Balance Sheet — full Schedule III format", "balance-sheet"))
    s.append(
        definition(
            "The company Balance Sheet is a statement of assets, equity and liabilities as at a date, "
            "presented vertically as per Schedule III: first <strong>Equity and Liabilities</strong> "
            "(who funded the company), then <strong>Assets</strong> (what the company owns). "
            "Both totals must be equal."
        )
    )
    s.append(
        simple(
            "If the Statement of Profit and Loss is the year's movie, the Balance Sheet is the photograph on 31 March. "
            "It does not tell you what happened during the year except through the profit sitting in reserves. "
            "Every rupee of asset was funded either by owners (share capital + reserves) or by outsiders (liabilities)."
        )
    )
    s.append(
        why(
            "A bank reading only the P&L might see a profit and still miss that the company has no cash "
            "(profit locked in receivables) or that a huge loan is due next month. The Balance Sheet, split "
            "current / non-current, answers: can this company pay its bills in the next 12 months, and is the "
            "owners' cushion (equity) thick enough?"
        )
    )
    s.append(
        real_life(
            "Horizon Ltd owns a building, plant, furniture, stock, debtors and cash. That is the Assets side. "
            "Those things were paid for by shareholders (capital + accumulated profits) and by holders of 12% debentures "
            "and by suppliers who have not yet been paid. That is Equity and Liabilities. "
            "If the two sides do not equal, a posting is missing — the photograph is torn."
        )
    )
    s.append(
        logic(
            "Accounting equation: Assets = Shareholders' funds + Non-current liabilities + Current liabilities. "
            "Profit for the year increases shareholders' funds (via surplus). Losses decrease them. "
            "Buying a machine with cash swaps one asset for another; the total does not change. "
            "Buying a machine on long-term loan increases assets and non-current liabilities together."
        )
    )
    s.append(
        format_box(
            "Balance Sheet (Schedule III, Division I) — the full skeleton",
            table(
                ["", "Particulars", "Note", "₹"],
                [
                    ["", "<strong>I  EQUITY AND LIABILITIES</strong>", "", ""],
                    ["1", "Shareholders' funds", "", ""],
                    ["", "&nbsp;&nbsp;(a) Share capital", "", ""],
                    ["", "&nbsp;&nbsp;(b) Reserves and surplus", "", ""],
                    ["", "&nbsp;&nbsp;(c) Money received against share warrants", "", ""],
                    ["2", "Share application money pending allotment", "", ""],
                    ["3", "Non-current liabilities", "", ""],
                    ["", "&nbsp;&nbsp;(a) Long-term borrowings", "", ""],
                    ["", "&nbsp;&nbsp;(b) Deferred tax liabilities (net)", "", ""],
                    ["", "&nbsp;&nbsp;(c) Other long-term liabilities", "", ""],
                    ["", "&nbsp;&nbsp;(d) Long-term provisions", "", ""],
                    ["4", "Current liabilities", "", ""],
                    ["", "&nbsp;&nbsp;(a) Short-term borrowings", "", ""],
                    ["", "&nbsp;&nbsp;(b) Trade payables", "", ""],
                    ["", "&nbsp;&nbsp;(c) Other current liabilities", "", ""],
                    ["", "&nbsp;&nbsp;(d) Short-term provisions", "", ""],
                    ["", "<strong>Total</strong>", "", ""],
                    ["", "<strong>II  ASSETS</strong>", "", ""],
                    ["1", "Non-current assets", "", ""],
                    ["", "&nbsp;&nbsp;(a) Property, plant and equipment / Fixed assets (tangible + intangible)", "", ""],
                    ["", "&nbsp;&nbsp;(b) Non-current investments", "", ""],
                    ["", "&nbsp;&nbsp;(c) Deferred tax assets (net)", "", ""],
                    ["", "&nbsp;&nbsp;(d) Long-term loans and advances", "", ""],
                    ["", "&nbsp;&nbsp;(e) Other non-current assets", "", ""],
                    ["2", "Current assets", "", ""],
                    ["", "&nbsp;&nbsp;(a) Current investments", "", ""],
                    ["", "&nbsp;&nbsp;(b) Inventories", "", ""],
                    ["", "&nbsp;&nbsp;(c) Trade receivables", "", ""],
                    ["", "&nbsp;&nbsp;(d) Cash and cash equivalents", "", ""],
                    ["", "&nbsp;&nbsp;(e) Short-term loans and advances", "", ""],
                    ["", "&nbsp;&nbsp;(f) Other current assets", "", ""],
                    ["", "<strong>Total</strong>", "", ""],
                ],
                caption="Memorise this order. Examiners award format marks for the heads even when a note is thin.",
            ),
        )
    )

    s.append(h3("Every major head, in simple words, with examples"))

    s.append(h4("1  Shareholders' funds"))
    s.append(
        p(
            b("(a) Share capital"),
            " — money the company has called from shareholders as the face value of shares. "
            "Not the market price. Not reserves. Taught in full in the next section.",
        )
    )
    s.append(
        p(
            b("(b) Reserves and surplus"),
            " — profits kept in the company: surplus in P&L, general reserve, securities premium, capital reserve. "
            "Current-year profit (line IX) is added to surplus here.",
        )
    )
    s.append(
        p(
            b("(c) Money received against share warrants"),
            " — a share warrant is a ticket that lets the holder buy shares later at a stated price. "
            "Money already collected against that ticket is not share capital yet (shares are not issued). "
            "Show it as a separate line under shareholders' funds. Exams mention it more often than they give a figure.",
        )
    )

    s.append(h4("2  Share application money pending allotment"))
    s.append(
        p(
            "People applied for shares and sent money; the company has ",
            b("not yet allotted"),
            " the shares. Until allotment, this is not share capital. "
            "If allotment is expected, it sits on this line. If the issue is failing and money is refundable, "
            "it is a current liability. Mention the head in theory answers even when the TB has no such item.",
        )
    )

    s.append(h4("3  Non-current liabilities"))
    s.append(
        table(
            ["Head", "Meaning", "Examples"],
            [
                [
                    "(a) Long-term borrowings",
                    "Loans and debentures not due within 12 months",
                    "12% Debentures repayable in 2029; 10% term loan from SBI for 7 years (exclude the instalment due next year)",
                ],
                [
                    "(b) Deferred tax liabilities (net)",
                    "Tax that is economically owed later because books and tax law time things differently",
                    "Depreciation in books slower than tax depreciation, creating a DTL. Brief in MBA papers; often Nil",
                ],
                [
                    "(c) Other long-term liabilities",
                    "Long-term dues that are not borrowings",
                    "Trade payables on an unusually long cycle; security deposits received that are not refundable within 12 months",
                ],
                [
                    "(d) Long-term provisions",
                    "Provisions payable after 12 months",
                    "Provision for employee gratuity (the long-term portion); warranty provision covering years 2–5",
                ],
            ],
        )
    )

    s.append(h4("4  Current liabilities — the exam trap cluster"))
    s.append(
        p(
            "Four boxes. Mixing them is the most common way to lose marks when the arithmetic is otherwise perfect."
        )
    )
    s.append(
        table(
            ["Head", "Who lives here", "Examples", "Do not put here"],
            [
                [
                    "(a) Short-term borrowings",
                    "Interest-bearing money you borrowed that is payable on demand or within 12 months",
                    "Bank overdraft, cash credit, short-term bank loan, loans repayable on demand",
                    "Suppliers of goods (those are trade payables). Outstanding interest (that is other current liabilities)",
                ],
                [
                    "(b) Trade payables",
                    "Amounts due for goods and services bought in the ordinary course of business",
                    "Creditors for purchases, bills payable arising from credit purchases",
                    "Loan from a bank. Outstanding salary. GST payable. Proposed dividend",
                ],
                [
                    "(c) Other current liabilities",
                    "Current dues that are neither borrowings nor trade payables",
                    "Outstanding expenses, income received in advance, current maturities of long-term debt, interest accrued on borrowings, unpaid dividend (once declared), statutory dues (GST, TDS)",
                    "The loan principal that is still long-term. Provision for tax (that is a provision)",
                ],
                [
                    "(d) Short-term provisions",
                    "Provisions expected to be settled within 12 months",
                    "Provision for tax, provision for a known legal claim due soon. (Provision for doubtful debts is NOT here — it is deducted from receivables)",
                    "Outstanding rent (that is a known unpaid bill, so other current liability, not a provision)",
                ],
            ],
            caption="Trade payable vs borrowing vs other current liability vs provision — learn the four-way split",
        )
    )
    s.append(
        keypoint(
            "MSME split (one line, because the statute asks for it): Trade payables must be broken, in the notes, into "
            "(i) total outstanding dues of micro and small enterprises, and (ii) dues of other creditors. "
            "On the face you still show one Trade payables total. If the question is silent on MSME, write the total "
            "and, in a theory line, mention that the split is required."
        )
    )
    s.append(
        p(
            b("Current maturities of long-term debt."),
            " Horizon has 12% Debentures ₹2,00,000 due in several years — all non-current. "
            "If ₹40,000 of a term loan must be repaid in the next 12 months, that ₹40,000 leaves Long-term borrowings "
            "and sits under Other current liabilities (Division I). Forget this split and your current ratio in the next chapter will also be wrong.",
        )
    )

    s.append(h4("Assets — non-current"))
    s.append(
        table(
            ["Head", "Meaning", "Examples"],
            [
                [
                    "(a) PPE / Fixed assets (tangible + intangible)",
                    "Assets used to run the business, not to resell",
                    "Land, building, plant, furniture, vehicles (tangible). Patents, trademarks, computer software, goodwill (intangible). Shown at cost less accumulated depreciation / amortisation",
                ],
                [
                    "(b) Non-current investments",
                    "Investments held for more than 12 months",
                    "Shares of a subsidiary, long-term bonds, investment in land held for capital appreciation",
                ],
                [
                    "(c) Deferred tax assets (net)",
                    "Tax already economically 'prepaid' because of timing differences the other way",
                    "Often Nil in exam TBs",
                ],
                [
                    "(d) Long-term loans and advances",
                    "Money the company has given that will come back after 12 months",
                    "Security deposit with the landlord for a 5-year lease; long-term loan to a subsidiary",
                ],
                [
                    "(e) Other non-current assets",
                    "Long-term assets that do not fit above",
                    "Unamortised share-issue expenses in older papers; long-term prepaid (e.g. 3-year insurance unexpired beyond 12 months)",
                ],
            ],
        )
    )

    s.append(h4("Assets — current"))
    s.append(
        table(
            ["Head", "Meaning", "Examples"],
            [
                [
                    "(a) Current investments",
                    "Investments held to be sold / matured within 12 months",
                    "3-month treasury bill, surplus cash parked in a liquid mutual fund",
                ],
                [
                    "(b) Inventories",
                    "Goods held for sale or in process, plus stores",
                    "Closing stock of traded goods; RM, WIP, FG of a manufacturer; stores and spares. Valued at cost or NRV, whichever is lower (that valuation rule is AS-2; exam usually gives the figure)",
                ],
                [
                    "(c) Trade receivables",
                    "Money customers owe for goods / services sold in the ordinary course",
                    "Sundry debtors, bills receivable from customers. Shown net of provision for doubtful debts. Ageing (overdue vs others) goes in the notes",
                ],
                [
                    "(d) Cash and cash equivalents",
                    "Cash on hand, balances with banks, short deposits with original maturity of 3 months or less",
                    "Cash in hand, current account, 30-day fixed deposit. A 2-year FD is not a cash equivalent — it is an investment or other bank balance disclosed separately",
                ],
                [
                    "(e) Short-term loans and advances",
                    "Recoverable within 12 months, not trade receivables",
                    "Advance to a supplier, staff advance, GST input recoverable. Some papers put prepaid expenses here; Division I also allows Other current assets",
                ],
                [
                    "(f) Other current assets",
                    "Current assets that are not investments, stock, receivables, cash or advances",
                    "Prepaid insurance, accrued interest, prepaid rent, unbilled revenue",
                ],
            ],
        )
    )
    s.append(
        identify(
            "If the question says 'prepare Balance Sheet as per Schedule III / Companies Act 2013', draw this vertical "
            "skeleton first (heads only), then drop numbers from notes into it. Do not draw a T-shape with 'Liabilities' "
            "on the left in the 1956 style."
        )
    )
    s.append(
        mistakes(
            [
                "Writing 'Sundry creditors' on the face instead of Trade payables.",
                "Putting outstanding expenses under Trade payables or under Short-term provisions.",
                "Showing provision for doubtful debts on the liabilities side — it is a deduction from Trade receivables.",
                "Showing drawings — companies do not have drawings.",
                "Forgetting to add current-year profit to Reserves and surplus.",
                "Grossing PPE without deducting depreciation for the year.",
            ]
        )
    )
    s.append(
        memory(
            "Read the Balance Sheet as a sentence: 'Owners and lenders funded these assets.' "
            "Equity and Liabilities = the sources. Assets = the uses. Notes are the footnotes of the story."
        )
    )
    s.append(
        exam_answer(
            "The company Balance Sheet as per Schedule III of the Companies Act, 2013 is presented vertically. "
            "Equity and Liabilities comprise: (1) Shareholders' funds — share capital, reserves and surplus, money received against share warrants; "
            "(2) Share application money pending allotment; (3) Non-current liabilities — long-term borrowings, deferred tax liabilities (net), "
            "other long-term liabilities, long-term provisions; (4) Current liabilities — short-term borrowings, trade payables, "
            "other current liabilities, short-term provisions. Assets comprise: (1) Non-current assets — PPE / fixed assets, non-current investments, "
            "deferred tax assets (net), long-term loans and advances, other non-current assets; (2) Current assets — current investments, inventories, "
            "trade receivables, cash and cash equivalents, short-term loans and advances, other current assets."
        )
    )
    return "".join(s)

# ---------------------------------------------------------------------------
# 7. Share capital
# ---------------------------------------------------------------------------


def _share_capital() -> str:
    s = []
    s.append(h2("Share capital — authorised, issued, subscribed, called-up, paid-up", "share-capital"))
    s.append(
        definition(
            "Share capital is the owners' capital of a company, divided into shares of a fixed face value "
            "(for example ₹10 each). On the face of the Balance Sheet you report the <strong>paid-up</strong> "
            "amount. The note to share capital then unrolls authorised, issued, subscribed, called-up, "
            "calls in arrears, and the number of shares."
        )
    )
    s.append(
        simple(
            "A sole trader says 'I put in ₹5,00,000'. A company cannot say that, because there are many owners. "
            "It cuts the ₹5,00,000 into 50,000 slices of ₹10. Each slice is a share. The Memorandum of Association "
            "also states a ceiling — the company must not issue more than that ceiling without following the law. "
            "That ceiling is authorised capital."
        )
    )
    s.append(
        why(
            "Lenders and shareholders need to know: how much capital is legally allowed, how much has actually "
            "been issued, whether some applicants still owe a call, and whether the company has headroom to issue "
            "more shares. A single figure 'Share capital ₹5,00,000' on the face is not enough — the note is the "
            "legal disclosure."
        )
    )
    s.append(
        real_life(
            "Horizon Ltd's Memorandum authorises 1,00,000 equity shares of ₹10 each (authorised ₹10,00,000). "
            "It has so far issued and allotted 50,000 shares, fully called and fully paid. Face of the Balance Sheet: "
            "Share capital ₹5,00,000. The remaining authorised ₹5,00,000 is simply unused capacity — it is not a liability "
            "and not an asset."
        )
    )
    s.append(
        logic(
            "Authorised ≥ Issued ≥ Subscribed ≥ Called-up ≥ Paid-up. "
            "Paid-up = Called-up − Calls in arrears. "
            "Forfeited shares (if any) sit as a separate line in the share-capital note until they are reissued; "
            "after reissue the profit on forfeiture goes to Capital reserve, which is a reserve, not share capital."
        )
    )
    s.append(
        table(
            ["Layer", "Meaning", "Horizon-style numbers"],
            [
                [
                    "Authorised (nominal) capital",
                    "Maximum the company may issue, as per its Memorandum",
                    "1,00,000 equity shares of ₹10 = ₹10,00,000",
                ],
                [
                    "Issued capital",
                    "Shares actually offered to the public / allottees",
                    "50,000 shares of ₹10 = ₹5,00,000",
                ],
                [
                    "Subscribed capital",
                    "Shares the public has agreed to take",
                    "50,000 shares = ₹5,00,000 (here issued = subscribed)",
                ],
                [
                    "Called-up capital",
                    "The slice of face value the company has demanded so far",
                    "₹10 called on 50,000 shares = ₹5,00,000",
                ],
                [
                    "Calls in arrears",
                    "Called-up money that some shareholders have not yet paid",
                    "Nil in Horizon. See the separate example below.",
                ],
                [
                    "Paid-up capital (this is the face figure)",
                    "Called-up minus calls in arrears",
                    "₹5,00,000",
                ],
            ],
            caption="Five layers of share capital — only paid-up goes to the face total",
        )
    )
    s.append(
        example(
            "4.3",
            "Easy",
            "Calls in arrears — how paid-up capital is computed",
            p(
                "Aarav Textiles Ltd has authorised capital of 1,00,000 equity shares of ₹10. "
                "It issued 80,000 shares. Public subscribed 75,000 shares. ₹8 per share has been called. "
                "Calls in arrears ₹10,000. Compute the figure that appears as Share capital on the Balance Sheet."
            )
            + p(b("Step 1 — called-up capital."))
            + p("75,000 shares × ₹8 = ₹6,00,000. (Use subscribed shares, not issued, because 5,000 issued shares were not taken.)")
            + p(b("Step 2 — paid-up capital."))
            + p("₹6,00,000 − calls in arrears ₹10,000 = ₹5,90,000.")
            + p(
                b("On the face:"),
                " Share capital ₹5,90,000. In the note you may write: Subscribed and called-up ₹6,00,000, less calls in arrears ₹10,000, paid-up ₹5,90,000."
            )
            + p(
                "Authorised ₹10,00,000 is disclosed in the note only. Issued 80,000 is disclosed in the note only. "
                "Neither of those numbers is added into the Balance Sheet total."
            ),
        )
    )
    s.append(
        keypoint(
            "Equity shares vs preference shares: equity shares take the residual profit and residual assets; "
            "preference shares usually take a fixed dividend first. On the Balance Sheet both are share capital; "
            "the note splits them. MBA problems in this chapter are almost always equity only."
        )
    )
    s.append(
        mistakes(
            [
                "Adding authorised capital into the Balance Sheet total — authorised is a ceiling, not money received.",
                "Using the stock-market price of the share instead of face value.",
                "Treating calls in arrears as a current asset (old habit). Under Schedule III, calls in arrears are deducted from called-up capital in the share-capital note.",
                "Confusing securities premium with share capital. Premium is a reserve (Reserves and surplus), not share capital.",
            ]
        )
    )
    s.append(
        memory(
            "Authorised is the size of the parking lot. Issued is how many cars were invited. "
            "Subscribed is how many actually drove in. Called-up is the ticket price demanded. "
            "Paid-up is the money that actually reached the till."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 8. Reserves and surplus
# ---------------------------------------------------------------------------


def _reserves() -> str:
    s = []
    s.append(h2("Reserves and surplus — where this year's profit goes", "reserves"))
    s.append(
        definition(
            "Reserves and surplus are owners' funds other than share capital: profits kept back, and capital "
            "receipts such as securities premium. Under Schedule III the note typically shows: capital reserve, "
            "capital redemption reserve, securities premium, general reserve, and surplus (balance in Statement of Profit and Loss)."
        )
    )
    s.append(
        simple(
            "Profit of the year is not put in a director's pocket. It is poured into a bucket called Surplus. "
            "The company may then ladle some of that bucket into General reserve (a rainy-day bowl) or pay dividend "
            "(which takes money out of the bucket and, once declared, out of the bank). "
            "Securities premium is a different bucket: it is the extra money investors paid above face value when shares were issued. You must not use it as if it were trading profit."
        )
    )
    s.append(
        why(
            "Share capital is sticky — you cannot casually give it back. Reserves show how much extra cushion the "
            "owners have built. A company with share capital ₹5,00,000 and reserves ₹1,58,000 is sturdier than one "
            "with the same capital and a negative surplus."
        )
    )
    s.append(
        logic(
            "Movement of surplus for the year: Opening surplus + Profit for the period − Appropriations "
            "(transfer to general reserve, dividend declared) = Closing surplus. "
            "Under modern Companies Act treatment, a dividend that is only <em>proposed</em> by the board is "
            "<strong>not</strong> deducted here and is <strong>not</strong> a liability. It is disclosed in notes. "
            "A dividend that is <em>declared</em> (shareholders have approved it, or an interim dividend that has been paid/become payable) is deducted from surplus."
        )
    )
    s.append(
        table(
            ["Reserve", "Where it comes from", "Where it sits", "Typical exam use"],
            [
                [
                    "Surplus (P&L balance)",
                    "Accumulated profits not earmarked",
                    "Reserves and surplus",
                    "Opening credit + current profit",
                ],
                [
                    "General reserve",
                    "Transfer from surplus, by board decision",
                    "Reserves and surplus",
                    "Often given as an opening figure; transfer only if the question says so",
                ],
                [
                    "Securities premium",
                    "Issue of shares above face value",
                    "Reserves and surplus (a capital reserve in nature)",
                    "Cannot be used to pay dividend. Specified uses in Section 52 (issue expenses, premium on redemption, bonus shares, etc.)",
                ],
                [
                    "Capital reserve",
                    "Capital profits (reissue of forfeited shares, profit on sale of a capital asset sometimes)",
                    "Reserves and surplus",
                    "Not available for dividend",
                ],
            ],
        )
    )
    s.append(
        example(
            "4.4",
            "Easy",
            "How current-year profit flows into reserves",
            p(
                "Opening surplus ₹55,000. General reserve (opening) ₹40,000. Profit for the year ₹63,000. "
                "No transfer to general reserve, no dividend declared. Write the reserves note."
            )
            + table(
                ["Particulars", "₹"],
                [
                    ["General reserve (as per last Balance Sheet; no transfer this year)", "40,000"],
                    ["Surplus: balance as per last Balance Sheet", "55,000"],
                    ["Add: Profit for the year", "63,000"],
                    ["Surplus at the end of the year", "1,18,000"],
                    ["<strong>Total reserves and surplus</strong>", "<strong>1,58,000</strong>"],
                ],
                caption="This is Horizon Ltd's actual reserves note — we will meet it again",
            )
            + p("If the board had transferred ₹10,000 to general reserve, general reserve would become ₹50,000 and surplus would become ₹1,08,000. The total ₹1,58,000 would not change — you only moved a ladle from one bowl to the other."),
        )
    )
    s.append(
        warn(
            "Do not debit 'Drawings' and do not show a 'Net profit transferred to capital' line as you would for a sole trader. "
            "The capital figure (share capital) stays at paid-up capital unless new shares are issued. Profit lives in reserves."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 9. Notes to Accounts
# ---------------------------------------------------------------------------


def _notes_to_accounts() -> str:
    s = []
    s.append(h2("Notes to Accounts — why they exist and how they look", "notes"))
    s.append(
        definition(
            "Notes to Accounts are the legally required explanations and breakdowns that support the face of the "
            "Balance Sheet and the Statement of Profit and Loss. Schedule III says the face shall show the major "
            "heads; the detail (share-capital reconciliation, PPE movement, composition of other expenses, etc.) "
            "lives in numbered notes. The face carries the note number in a column."
        )
    )
    s.append(
        simple(
            "The face of the statements is a summary so a reader can see the whole photograph in one glance. "
            "If you printed every sub-item on the face, the page would be a jungle. Notes are the footnotes of the story. "
            "You cannot skip them in an exam that says 'with notes' — and even when it does not, showing three or four notes earns format marks."
        )
    )
    s.append(
        why(
            "Two companies can both show Other expenses ₹1,06,000. One spent it on research, the other on a failed advertisement blitz. "
            "The note tells you which. Share capital ₹5,00,000 could be 50,000 fully paid shares or 1,00,000 shares of ₹10 with ₹5 called — "
            "only the note reveals that. The law therefore makes notes part of the financial statements, not an annexure you may omit."
        )
    )
    s.append(
        real_life(
            "In an annual report the Balance Sheet line 'Trade receivables' has a note number. Open that note and you see "
            "the split of outstanding for more than six months vs others, provision for doubtful debts, and dues from related parties. "
            "That is the same discipline we use, in miniature, in exam answers."
        )
    )
    s.append(
        logic(
            "A note does not change the total. It unpacks it. If Other expenses on the face is ₹1,06,000, the note must add to ₹1,06,000. "
            "If it does not, you have either missed an item or double-counted. Always cross-foot notes to the face."
        )
    )
    s.append(h3("Three sample notes (the ones examiners almost always want)"))
    s.append(h4("Sample note A — Share capital"))
    s.append(
        table(
            ["Particulars", "31 Mar 2026 ₹"],
            [
                ["<strong>Authorised</strong>", ""],
                ["1,00,000 equity shares of ₹10 each", "10,00,000"],
                ["<strong>Issued, subscribed and fully paid</strong>", ""],
                ["50,000 equity shares of ₹10 each fully paid", "5,00,000"],
                ["Reconciliation of number of shares: opening 50,000; issued during the year Nil; closing 50,000", ""],
            ],
            caption="Note — Share capital (Horizon Ltd style)",
            foot="Also state: rights, preferences, restrictions (equity shares carry one vote each); shares held by promoters (if asked). Face figure = ₹5,00,000.",
        )
    )
    s.append(h4("Sample note B — Reserves and surplus"))
    s.append(
        table(
            ["Particulars", "₹"],
            [
                ["General reserve", "40,000"],
                ["Surplus in Statement of Profit and Loss", ""],
                ["&nbsp;&nbsp;Opening balance", "55,000"],
                ["&nbsp;&nbsp;Add: Profit for the year", "63,000"],
                ["&nbsp;&nbsp;Closing surplus", "1,18,000"],
                ["<strong>Total</strong>", "<strong>1,58,000</strong>"],
            ],
            caption="Note — Reserves and surplus",
        )
    )
    s.append(h4("Sample note C — Other expenses"))
    s.append(
        table(
            ["Particulars", "₹"],
            [
                ["Rent", "48,000"],
                ["Insurance (₹12,000 − prepaid ₹3,000)", "9,000"],
                ["Electricity", "18,000"],
                ["Advertisement", "22,000"],
                ["Bad debts", "8,000"],
                ["Provision for doubtful debts (increase)", "1,000"],
                ["<strong>Total (agrees to P&L face)</strong>", "<strong>1,06,000</strong>"],
            ],
            caption="Note — Other expenses (Horizon Ltd — we rebuild this in the full illustration)",
        )
    )
    s.append(
        p(
            "Other typical notes: Long-term borrowings (nature of loan, interest rate, security), PPE (gross block, depreciation, net block for each class), "
            "Inventories (RM / WIP / FG / stock-in-trade), Revenue from operations (sale of products vs services), Trade receivables (gross, provision, net)."
        )
    )
    s.append(
        exam_tip(
            "Write the note number on the face even if your notes are short. A face that says 'Other expenses  …  Note 6  …  ₹1,06,000' "
            "looks like a company statement. A face with no note column looks like a sole-trader account."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 10. Adjustments — the exam core
# ---------------------------------------------------------------------------


def _adjustments() -> str:
    s = []
    s.append(h2("Adjustments — the exam core", "adjustments"))
    s.append(
        lead(
            "The trial balance is a photograph of the ledger <em>before</em> year-end housekeeping. "
            "Adjustments are that housekeeping. For every adjustment you must be able to say four things: "
            "what it means in English, the journal, which statement is hit, and a mini numerical effect."
        )
    )
    s.append(
        definition(
            "Year-end adjustments are entries that bring unrecorded assets, liabilities, incomes and expenses "
            "into the books so that the Statement of Profit and Loss shows the year's true profit and the Balance Sheet "
            "shows the true position on 31 March. Matching concept: this year's income against this year's expenses."
        )
    )
    s.append(
        simple(
            "The ledger clerk recorded what was paid and what was received. You, the accountant, record what was "
            "<em>incurred</em> and what was <em>earned</em>. Rent unpaid is still an expense of this year. Insurance paid for next year is not this year's expense. "
            "Closing stock is an asset that is no longer 'purchases sitting in the P&L'."
        )
    )
    s.append(
        why(
            "Without adjustments, profit is whatever cash happened to move, and the Balance Sheet misses unpaid bills and unused prepayments. "
            "That is neither true nor fair, and it is not what the examiner wants."
        )
    )
    s.append(
        steps(
            [
                "Read each adjustment. Translate it into: extra expense, less expense, extra income, less income, extra asset, extra liability.",
                "Pass the journal (even if the question does not ask for journals — it stops you from one-sided posting).",
                "Post the P&L effect to the correct Schedule III line (employee benefits vs finance costs vs other expenses vs tax).",
                "Post the Balance Sheet effect to the correct head (other current liability vs short-term provision vs deduction from an asset).",
                "After all adjustments, total the P&L, transfer profit to surplus, and check that the Balance Sheet ties.",
            ],
            title="7. One method that works for every adjustment",
        )
    )

    s.append(h3("Adjustment 1 — Closing stock (if not already in the trial balance)"))
    s.append(
        p(
            "Closing stock is the goods still unsold (or unused) on 31 March. If the TB has opening inventory and purchases but no closing figure, "
            "the question will give closing inventory as an adjustment. It is an asset, and it reduces the cost charged this year."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Inventories (Closing stock)",
                    "credit": "Changes in inventories / Trading A/c",
                    "amount": "1,10,000",
                    "narration": "Stock-in-trade on hand taken into accounts.",
                }
            ],
            caption="Closing inventory ₹1,10,000",
        )
    )
    s.append(
        table(
            ["Statement", "Where it hits", "Mini numbers"],
            [
                [
                    "P&L",
                    "Changes in inventories = Opening − Closing. If closing ₹1,10,000 and opening ₹80,000, change = (₹30,000)",
                    "COGS falls by ₹1,10,000 compared with charging all purchases",
                ],
                [
                    "Balance Sheet",
                    "Current assets — Inventories",
                    "₹1,10,000 on the assets side",
                ],
            ],
        )
    )
    s.append(
        warn(
            "If closing stock is already inside the trial balance (rare in company papers, common in some old TBs as a memorandum), do not add it again. "
            "Look: is it listed among the debit balances? Then it is already an asset and the P&L has already been credited."
        )
    )

    s.append(h3("Adjustment 2 — Outstanding expenses (wages, rent, interest, salary)"))
    s.append(
        p(
            "The service was used this year; the cash has not gone out by 31 March. Still an expense of this year, and a liability on 31 March."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Salaries / Rent / Wages (expense)",
                    "credit": "Outstanding salaries / rent / wages",
                    "amount": "10,000",
                    "narration": "Salaries accrued but not paid.",
                }
            ],
            caption="Outstanding salaries ₹10,000",
        )
    )
    s.append(
        p(
            "P&L: add ₹10,000 to Employee benefits (if salary/wages) or to Other expenses (if rent) or to Finance costs (if interest). "
            "Balance Sheet: Other current liabilities ₹10,000 — not Trade payables, not Short-term borrowings, not a provision."
        )
    )
    s.append(
        example(
            "4.5",
            "Easy",
            "Outstanding rent",
            p("Rent in the TB ₹48,000. Outstanding rent ₹4,000.")
            + p("Expense for the year = ₹48,000 + ₹4,000 = ₹52,000 (Other expenses).")
            + p("Liability = ₹4,000 (Other current liabilities).")
            + p("The cash of ₹48,000 already reduced Cash in the TB. You do not touch cash again."),
        )
    )

    s.append(h3("Adjustment 3 — Prepaid expenses"))
    s.append(
        p(
            "Cash went out this year for a benefit that belongs to next year (insurance paid in March for April–June). "
            "That slice is an asset, not this year's expense."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Prepaid insurance",
                    "credit": "Insurance (expense)",
                    "amount": "3,000",
                    "narration": "Insurance unexpired carried forward.",
                }
            ],
            caption="Prepaid insurance ₹3,000",
        )
    )
    s.append(
        p(
            "P&L: Insurance in TB ₹12,000 − prepaid ₹3,000 = ₹9,000 inside Other expenses. "
            "Balance Sheet: Other current assets ₹3,000 (some papers park it under Short-term loans and advances — Other current assets is cleaner for a prepayment)."
        )
    )

    s.append(h3("Adjustment 4 — Accrued income"))
    s.append(
        p(
            "You have earned it; the customer / bank has not yet paid. Example: interest on a deposit for January–March, credited by the bank only in April."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Accrued interest (asset)",
                    "credit": "Interest income (other income)",
                    "amount": "5,000",
                    "narration": "Interest earned but not yet received.",
                }
            ],
            caption="Accrued interest ₹5,000",
        )
    )
    s.append(
        p(
            "P&L: add ₹5,000 to Other income. Balance Sheet: Other current assets ₹5,000. "
            "Do not add it to Trade receivables — the debtor is not a customer for goods."
        )
    )

    s.append(h3("Adjustment 5 — Income received in advance (unearned)"))
    s.append(
        p(
            "Cash arrived this year for a service you will give next year. Example: tenant paid April rent in March. Not this year's income; you owe the service."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Rent received (income)",
                    "credit": "Income received in advance",
                    "amount": "8,000",
                    "narration": "Rent received relating to the next year.",
                }
            ],
            caption="Unearned rent ₹8,000",
        )
    )
    s.append(
        p(
            "P&L: reduce Other income by ₹8,000. Balance Sheet: Other current liabilities ₹8,000. "
            "If Rent received in the TB is ₹20,000 and ₹8,000 is unearned, Other income from rent = ₹12,000."
        )
    )

    s.append(h3("Adjustment 6 — Depreciation on PPE"))
    s.append(
        p(
            "Machines wear out. The cost is spread over the years that use the machine. Depreciation is an expense; it is also a reduction in the book value of PPE. "
            "No cash moves."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "lines": [
                        {"side": "dr", "account": "Depreciation (P&L)", "amount": "51,000"},
                        {"side": "cr", "account": "Land and building", "amount": "20,000"},
                        {"side": "cr", "account": "Plant", "amount": "25,000"},
                        {"side": "cr", "account": "Furniture", "amount": "6,000"},
                    ],
                    "narration": "Depreciation written off for the year. (Alternatively credit Accumulated depreciation; net PPE is the same.)",
                }
            ],
            caption="Horizon-style depreciation for the year",
        )
    )
    s.append(
        p("Multiplications: Building 5/100 × ₹4,00,000 = ₹20,000. Plant 10/100 × ₹2,50,000 = ₹25,000. Furniture 10/100 × ₹60,000 = ₹6,000. Total ₹51,000.")
    )
    s.append(
        p(
            "P&L: Depreciation and amortisation expense ₹51,000 — its own line, not Other expenses. "
            "Balance Sheet: PPE shown net, ₹4,00,000 + ₹2,50,000 + ₹60,000 − ₹51,000 = ₹6,59,000. "
            "The note shows each class at cost, depreciation, net."
        )
    )
    s.append(
        formula(
            "Straight line (SLM): Depreciation for the year = (Cost − Residual value) / Useful life. Rate on original cost = (1 / life) × 100.",
            "Written down value (WDV): Depreciation = Book value × rate. Residual is not deducted each year; the rate is designed to approach it. "
            "In most Schedule III problems the question gives a % on the TB cost (SLM with residual Nil). Use that % and show the multiplication.",
        )
    )

    s.append(h3("Adjustment 7 — Interest on loan / debentures outstanding"))
    s.append(
        p(
            "Interest is the rent of borrowed money. Even if you have not paid the second half-year, the year has used the money for 12 months, so 12 months of interest is an expense. "
            "The unpaid slice is a liability."
        )
    )
    s.append(
        p(
            b("Horizon numbers."),
            " 12% Debentures ₹2,00,000. Interest for the year = 12/100 × ₹2,00,000 = ₹24,000. "
            "TB already shows Interest on debentures ₹12,000 (the first half paid). Outstanding = ₹24,000 − ₹12,000 = ₹12,000."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Finance costs (interest on debentures)",
                    "credit": "Interest accrued and due / Outstanding debenture interest",
                    "amount": "12,000",
                    "narration": "Second half-year interest on 12% debentures not yet paid.",
                }
            ],
            caption="Outstanding debenture interest ₹12,000",
        )
    )
    s.append(
        p(
            "P&L: Finance costs = ₹12,000 (TB) + ₹12,000 (outstanding) = ₹24,000. "
            "Balance Sheet: Other current liabilities ₹12,000 (interest accrued). "
            "The debentures themselves stay under Long-term borrowings ₹2,00,000. Do not add outstanding interest to the debenture principal."
        )
    )
    s.append(
        keypoint(
            "Two hits, always: extra finance cost AND extra current liability. Students often remember the expense and forget the liability (Balance Sheet will not tie) "
            "or remember the liability and leave finance cost at the TB figure (profit overstated)."
        )
    )

    s.append(h3("Adjustment 8 — Provision for tax"))
    s.append(
        p(
            "A company is a taxable person. Estimated income-tax on this year's profit is an expense of this year, even though the return will be filed later. "
            "We create a provision."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Tax expense (current tax)",
                    "credit": "Provision for tax",
                    "amount": "35,000",
                    "narration": "Provision for current tax for the year.",
                }
            ],
            caption="Provision for tax ₹35,000",
        )
    )
    s.append(
        p(
            "P&L: line VIII Tax expense ₹35,000 — after Profit before tax, never mixed into Other expenses. "
            "Balance Sheet: Short-term provisions ₹35,000. "
            "It is a provision (estimate) rather than a fully billed outstanding, which is why it is not Other current liabilities."
        )
    )

    s.append(h3("Adjustment 9 — Proposed dividend / dividend (read this twice)"))
    s.append(
        definition(
            "A dividend is a distribution of profit to shareholders. It is <strong>not</strong> an expense of earning the profit. "
            "It is an appropriation of profit that has already been computed. Under the Companies Act, 2013 as it stands, "
            "a dividend becomes a liability only when it is <strong>declared</strong> (or, for interim dividend, when the board declares it and it becomes payable)."
        )
    )
    s.append(
        simple(
            "The board may <em>propose</em> ₹1 per share at its meeting in April, after the 31 March books are closed. "
            "Shareholders vote on that proposal at the AGM in August. Until they vote yes, the company does not legally owe the dividend. "
            "So on 31 March there is no liability. The proposal is a footnote. "
            "Once the AGM declares it, next year's books show Dividend payable as a current liability until it is paid."
        )
    )
    s.append(
        why(
            "AS-4 (and the 2016 Companies (Accounting Standards) Amendment) stopped companies from booking proposed dividend as a liability of the year just ended. "
            "Schedule III follows that: proposed dividend is disclosed in notes, not recognised. "
            "University MBA papers are mixed — some still want the old appropriation. You must know both, and you must state which one you are using."
        )
    )

    s.append(h4("Modern Schedule III treatment (use this unless the question forces the old way)"))
    s.append(
        p(
            "No journal on 31 March for a dividend that is only proposed. Profit for the period is transferred in full to Surplus. "
            "In the notes you write: 'The Board has proposed a dividend of ₹… per equity share, aggregating ₹…. "
            "The proposed dividend is subject to approval at the ensuing AGM and is not recognised as a liability.'"
        )
    )
    s.append(
        p(
            "When the dividend is later declared: debit Surplus (reserves), credit Dividend payable (Other current liabilities). "
            "When paid: debit Dividend payable, credit Bank. Cash leaves. Equity falls. P&L of the year of payment is not charged."
        )
    )

    s.append(h4("Old university / P&L appropriation treatment (still seen in some papers)"))
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Surplus / P&L Appropriation",
                    "credit": "Proposed dividend",
                    "amount": "50,000",
                    "narration": "OLD TREATMENT: proposed dividend appropriated. Not the current Schedule III recognition.",
                }
            ],
            caption="Old exam treatment — proposed dividend ₹50,000 (50,000 shares × ₹1)",
        )
    )
    s.append(
        p(
            "Under that old treatment, Surplus falls by ₹50,000 and Short-term provisions (or a separate 'Proposed dividend') rises by ₹50,000. "
            "Profit for the period on the face of the P&L is still computed ",
            b("before"),
            " this appropriation — you do not put proposed dividend inside expenses. You appropriate after arriving at profit.",
        )
    )
    s.append(
        keypoint(
            "Current Schedule III: proposed dividend is NOT a liability until declared; shown in notes. "
            "Provision for dividend once declared is a current liability (Other current liabilities — unpaid dividend). "
            "Never show proposed dividend as an expense in the Statement of Profit and Loss. It is not Employee benefits, not Other expenses, not Finance costs."
        )
    )
    s.append(
        exam_tip(
            "If the question is silent, apply the modern treatment, write one sentence in a working note, and do not create a liability. "
            "If the question says 'take proposed dividend as a liability' or shows an appropriation account, follow the old treatment. "
            "Either way, do not debit it inside line IV expenses."
        )
    )

    s.append(h3("Adjustment 10 — Provision for doubtful debts (and the increase)"))
    s.append(
        p(
            "Some customers may not pay. We do not wait for them to officially fail. We estimate a provision. "
            "The provision is a contra-asset: it is deducted from Trade receivables, not shown as a liability."
        )
    )
    s.append(
        formula(
            "Required provision = given % × Trade receivables (usually sundry debtors; bills receivable are normally left out unless the question says otherwise).",
            "Charge to P&L this year = Required provision − Existing provision already in the TB. "
            "If the result is positive, extra Other expenses. If negative, write back (other income / reduction in other expenses).",
        )
    )
    s.append(
        p(
            b("Horizon numbers."),
            " Trade receivables ₹1,40,000. Required = 5/100 × ₹1,40,000 = ₹7,000. Existing provision in TB ₹6,000. "
            "Increase charged to P&L = ₹7,000 − ₹6,000 = ₹1,000."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Other expenses (provision for doubtful debts)",
                    "credit": "Provision for doubtful debts",
                    "amount": "1,000",
                    "narration": "Provision raised from ₹6,000 to ₹7,000 (5% of ₹1,40,000).",
                }
            ],
            caption="Increase in provision ₹1,000",
        )
    )
    s.append(
        p(
            "P&L: ₹1,000 inside Other expenses (together with bad debts actually written off). "
            "Balance Sheet: Trade receivables shown net — gross ₹1,40,000 (plus bills receivable if you group them) less provision ₹7,000. "
            "Bad debts already written off in the TB (₹8,000) are an Other expense of their own; do not also deduct them from debtors — the TB debtors are already after that write-off."
        )
    )
    s.append(
        example(
            "4.6",
            "Moderate",
            "Debtors, bad debts already in TB, and a new provision rate",
            p("TB: Trade receivables ₹1,40,000; Bad debts ₹8,000; Provision for doubtful debts ₹6,000. Adjustment: provision to be 5% of debtors.")
            + ol(
                [
                    "Debtors on the TB are already after writing off ₹8,000. Do not reduce them again for those bad debts.",
                    "Required provision = 5/100 × ₹1,40,000 = ₹7,000.",
                    "Existing provision ₹6,000, so P&L charge = ₹1,000.",
                    "Other expenses includes Bad debts ₹8,000 + Increase in provision ₹1,000 = ₹9,000 from this cluster.",
                    "Balance Sheet: Trade receivables ₹1,40,000 − ₹7,000 = ₹1,33,000 (before grouping bills receivable).",
                ]
            ),
        )
    )

    s.append(h3("Adjustment 11 — Goods distributed as samples / used in the business"))
    s.append(
        p(
            "Goods that left the shop were not sold. If they were given as free samples, that is advertisement. "
            "If the company used its own goods to build an office table, that is a fixed asset (or an expense if the amount is tiny). "
            "In both cases Purchases (or Inventory) must be reduced, because those goods are not available for sale."
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Advertisement / Sales promotion",
                    "credit": "Purchases",
                    "amount": "8,000",
                    "narration": "Goods distributed as free samples.",
                }
            ],
            caption="Samples ₹8,000",
        )
    )
    s.append(
        journal(
            [
                {
                    "date": "31 Mar",
                    "debit": "Furniture (PPE)",
                    "credit": "Purchases",
                    "amount": "10,000",
                    "narration": "Goods of the company used to make office furniture.",
                }
            ],
            caption="Goods used in the business ₹10,000",
        )
    )
    s.append(
        table(
            ["Case", "P&L", "Balance Sheet"],
            [
                [
                    "Samples ₹8,000",
                    "Purchases of stock-in-trade fall by ₹8,000; Other expenses (advertisement) rise by ₹8,000. Profit is unchanged if you forget both, but the lines are wrong — and if you reduce purchases only, profit is overstated",
                    "No extra asset. Inventory is already lower because those goods are gone",
                ],
                [
                    "Goods used to make furniture ₹10,000",
                    "Purchases fall by ₹10,000 (COGS down, profit up by ₹10,000 — correct, because the goods became an asset, not a cost of sales). Then depreciate the furniture if the adjustment says so",
                    "PPE (furniture) rises by ₹10,000",
                ],
            ],
        )
    )

    s.append(h3("Adjustment 12 — Manager's commission on profit"))
    s.append(
        p(
            "A manager may be promised a percentage of profit. Two wordings exist, and they are not the same number. "
            "Commission is an Employee benefits expense (some papers park it in Other expenses — Employee benefits is the better Schedule III home). "
            "Outstanding commission is Other current liabilities."
        )
    )
    s.append(
        formula(
            "On profit BEFORE charging commission: Commission = Rate × Profit before commission.",
            "On profit AFTER charging commission: Commission = Profit before commission × Rate / (100 + Rate). "
            "Always read the words 'before charging' or 'after charging'. If the question is silent, examiners often mean before charging — but write your assumption.",
        )
    )
    s.append(
        example(
            "4.7",
            "Moderate",
            "Same profit, two commissions — why the formula changes",
            p("Profit before commission and before tax ₹1,10,000. Rate 10%. Tax ignored in this mini example so the formula is visible.")
            + p(b("Case A — 10% on profit before charging such commission."))
            + p("Commission = 10/100 × ₹1,10,000 = ₹11,000.")
            + p("Profit after commission = ₹1,10,000 − ₹11,000 = ₹99,000. Check: 10% of ₹1,10,000 is ₹11,000, as promised.")
            + p(b("Case B — 10% on profit after charging such commission."))
            + p("Let commission be C. Profit after commission = ₹1,10,000 − C. We need C = 10/100 × (₹1,10,000 − C).")
            + p("C = ₹11,000 − 0.10 C.  C + 0.10 C = ₹11,000.  1.10 C = ₹11,000.  C = ₹11,000 × 100/110 = ₹10,000.")
            + p("Shortcut: C = ₹1,10,000 × 10/110 = ₹10,000.")
            + p("Check: Profit after commission = ₹1,00,000. 10% of ₹1,00,000 = ₹10,000. The manager got 10% of the profit that remains after paying him. That is the point of 'after charging'.")
            + journal(
                [
                    {
                        "date": "31 Mar",
                        "debit": "Employee benefits (manager's commission)",
                        "credit": "Outstanding commission",
                        "amount": "10,000",
                        "narration": "Case B: commission 10% after charging such commission.",
                    }
                ]
            ),
        )
    )
    s.append(
        p(
            "If commission is on profit ",
            b("after tax"),
            ", compute tax first on the specified base (the question will say whether tax is before or after commission). "
            "Most MBA problems keep it simple: commission on profit before tax, either before or after charging commission. Do not invent a tax round unless asked."
        )
    )
    s.append(
        exam_tip(
            "When both tax and commission appear: read the order in the question. A common exam sequence is: "
            "profit before commission and tax → charge commission → profit before tax → charge tax. "
            "If commission is 'after charging such commission' but 'before tax', apply the Rate/(100+Rate) formula on the pre-tax, pre-commission profit."
        )
    )

    s.append(h3("Map: every adjustment onto Schedule III"))
    s.append(
        table(
            ["Adjustment", "P&L line", "Balance Sheet line"],
            [
                ["Closing stock", "Changes in inventories (and it shapes COGS)", "Current assets — Inventories"],
                ["Outstanding salary / wages", "Employee benefits expense", "Other current liabilities"],
                ["Outstanding rent / electricity", "Other expenses", "Other current liabilities"],
                ["Outstanding interest", "Finance costs", "Other current liabilities"],
                ["Prepaid insurance / rent", "Reduces Other expenses", "Other current assets"],
                ["Accrued income", "Other income", "Other current assets"],
                ["Income received in advance", "Reduces Other income / Revenue", "Other current liabilities"],
                ["Depreciation", "Depreciation and amortisation", "Deducted from PPE"],
                ["Provision for tax", "Tax expense (current tax)", "Short-term provisions"],
                ["Proposed dividend (modern)", "No P&L charge", "No liability; disclose in notes"],
                ["Dividend declared / unpaid", "Not an expense; debit Surplus", "Other current liabilities"],
                ["Increase in PFDD", "Other expenses", "Deducted from Trade receivables"],
                ["Bad debts (already in TB or extra)", "Other expenses", "Debtors already reduced if written off"],
                ["Goods as samples", "Other expenses up; Purchases down", "No extra line"],
                ["Goods used as asset", "Purchases down", "PPE up"],
                ["Manager's commission", "Employee benefits", "Other current liabilities"],
            ],
            caption="Pin this table above your desk before the exam",
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 11. Horizon Ltd — complete exam illustration
# ---------------------------------------------------------------------------


def _horizon() -> str:
    s = []
    s.append(h2("Complete exam illustration — Horizon Ltd", "horizon"))
    s.append(
        example(
            "4.8",
            "Exam-level",
            "Horizon Ltd — trial balance, seven adjustments, full Statement of Profit and Loss and Balance Sheet with notes",
            _horizon_body(),
        )
    )
    return "".join(s)


def _horizon_body() -> str:
    s = []
    s.append(
        p(
            "This is the 16-mark shape you will meet: a trial balance of a company, a list of adjustments, and the instruction "
            "'Prepare the Statement of Profit and Loss and the Balance Sheet as per Schedule III of the Companies Act, 2013.'"
        )
    )
    s.append(
        p(
            b("Horizon Ltd"),
            " is a trading company. Equity shares have a face value of ₹10. Year ended 31 March 2026. "
            "The trial balance below was built so that both sides equal ₹18,80,000 ",
            b("before"),
            " adjustments. Dividend received and rent received were added as other income so the books tie; they are not balancing junk — they teach line II."
        )
    )
    s.append(h4("Trial balance as at 31 March 2026"))
    s.append(
        table(
            ["Particulars", "Dr (₹)", "Cr (₹)"],
            [
                ["Land and building", "4,00,000", ""],
                ["Plant", "2,50,000", ""],
                ["Furniture", "60,000", ""],
                ["Purchases", "6,20,000", ""],
                ["Opening inventory", "80,000", ""],
                ["Trade receivables", "1,40,000", ""],
                ["Bills receivable", "30,000", ""],
                ["Cash and bank", "70,000", ""],
                ["Salaries", "1,10,000", ""],
                ["Rent", "48,000", ""],
                ["Insurance", "12,000", ""],
                ["Interest on debentures", "12,000", ""],
                ["Electricity", "18,000", ""],
                ["Advertisement", "22,000", ""],
                ["Bad debts", "8,000", ""],
                ["Equity share capital (50,000 shares of ₹10)", "", "5,00,000"],
                ["12% Debentures (long-term)", "", "2,00,000"],
                ["Sales", "", "9,50,000"],
                ["Trade payables", "", "90,000"],
                ["General reserve", "", "40,000"],
                ["Surplus (opening credit)", "", "55,000"],
                ["Provision for doubtful debts", "", "6,000"],
                ["Dividend received", "", "19,000"],
                ["Rent received", "", "20,000"],
                ["<strong>Total</strong>", "<strong>18,80,000</strong>", "<strong>18,80,000</strong>"],
            ],
            caption="Horizon Ltd — trial balance (tied before adjustments)",
            foot="Dr check: 4,00,000 + 2,50,000 + 60,000 = 7,10,000 PPE; + 6,20,000 + 80,000 = 14,10,000; + 1,40,000 + 30,000 + 70,000 = 16,50,000; "
            "expenses 1,10,000 + 48,000 + 12,000 + 12,000 + 18,000 + 22,000 + 8,000 = 2,30,000; grand 18,80,000. "
            "Cr check: 5,00,000 + 2,00,000 + 9,50,000 = 16,50,000; + 90,000 + 40,000 + 55,000 + 6,000 + 19,000 + 20,000 = 18,80,000.",
        )
    )
    s.append(p(b("Adjustments")))
    s.append(
        ol(
            [
                "Closing inventory ₹1,10,000.",
                "Depreciate building 5%, plant 10%, furniture 10% (on the TB costs; residual Nil).",
                "Outstanding salaries ₹10,000.",
                "Prepaid insurance ₹3,000.",
                "Provision for doubtful debts to be 5% of trade receivables (sundry debtors ₹1,40,000; bills receivable are considered good).",
                "Provision for tax ₹35,000.",
                "Provide the outstanding interest on 12% debentures for the year (half-year interest is already in the TB).",
            ]
        )
    )
    s.append(
        p(
            b("Modern dividend note (no figure given, so none is booked):"),
            " no proposed dividend is recognised as a liability. If the board later proposes one, it will be a disclosure, not a 31 March liability."
        )
    )

    s.append(h4("Step 1 — working notes (every multiplication)"))

    s.append(p(b("WN 1  Revenue from operations")))
    s.append(p("Sales as per TB = ₹9,50,000. No returns given."))

    s.append(p(b("WN 2  Other income")))
    s.append(p("Dividend received ₹19,000 + Rent received ₹20,000 = ₹39,000. Neither is the trading activity, so they are not revenue from operations."))

    s.append(p(b("WN 3  Purchases of stock-in-trade and changes in inventories")))
    s.append(
        table(
            ["", "₹"],
            [
                ["Opening inventory", "80,000"],
                ["Add: Purchases", "6,20,000"],
                ["Goods available for sale", "7,00,000"],
                ["Less: Closing inventory", "1,10,000"],
                ["Cost of goods sold", "5,90,000"],
                ["Schedule III split: Purchases of stock-in-trade", "6,20,000"],
                ["Changes in inventories (80,000 − 1,10,000)", "(30,000)"],
                ["Check: 6,20,000 + (30,000)", "5,90,000"],
            ],
        )
    )

    s.append(p(b("WN 4  Employee benefits expense")))
    s.append(p("Salaries ₹1,10,000 + outstanding salaries ₹10,000 = ₹1,20,000."))

    s.append(p(b("WN 5  Finance costs")))
    s.append(
        p(
            "Coupon for the year = 12/100 × ₹2,00,000 = ₹24,000. "
            "Already debited in TB = ₹12,000. Outstanding = ₹24,000 − ₹12,000 = ₹12,000. "
            "Finance costs on the face = ₹24,000."
        )
    )

    s.append(p(b("WN 6  Depreciation and amortisation")))
    s.append(
        table(
            ["Asset", "Computation", "₹"],
            [
                ["Building", "5/100 × ₹4,00,000", "20,000"],
                ["Plant", "10/100 × ₹2,50,000", "25,000"],
                ["Furniture", "10/100 × ₹60,000", "6,000"],
                ["Total", "₹20,000 + ₹25,000 + ₹6,000", "51,000"],
            ],
        )
    )

    s.append(p(b("WN 7  Other expenses")))
    s.append(
        table(
            ["Item", "Computation", "₹"],
            [
                ["Rent", "As per TB (no outstanding on rent)", "48,000"],
                ["Insurance", "₹12,000 − prepaid ₹3,000", "9,000"],
                ["Electricity", "As per TB", "18,000"],
                ["Advertisement", "As per TB", "22,000"],
                ["Bad debts", "As per TB (already written off)", "8,000"],
                ["Increase in provision for doubtful debts", "Required 5/100 × ₹1,40,000 = ₹7,000; existing ₹6,000; charge ₹1,000", "1,000"],
                ["Total", "48,000 + 9,000 = 57,000; + 18,000 = 75,000; + 22,000 = 97,000; + 8,000 = 1,05,000; + 1,000", "1,06,000"],
            ],
        )
    )

    s.append(p(b("WN 8  Tax expense")))
    s.append(p("Current tax = provision given = ₹35,000. Deferred tax Nil."))

    s.append(p(b("WN 9  Profit")))
    s.append(
        table(
            ["", "₹"],
            [
                ["Total income (₹9,50,000 + ₹39,000)", "9,89,000"],
                [
                    "Total expenses: purchases 6,20,000 + change (30,000) + employee 1,20,000 + finance 24,000 + depreciation 51,000 + other 1,06,000",
                    "",
                ],
                ["6,20,000 − 30,000 = 5,90,000", ""],
                ["5,90,000 + 1,20,000 = 7,10,000", ""],
                ["7,10,000 + 24,000 = 7,34,000", ""],
                ["7,34,000 + 51,000 = 7,85,000", ""],
                ["7,85,000 + 1,06,000 = 8,91,000", "8,91,000"],
                ["Profit before tax 9,89,000 − 8,91,000", "98,000"],
                ["Less: Tax 35,000", "35,000"],
                ["Profit for the period", "63,000"],
            ],
        )
    )

    s.append(p(b("WN 10  Reserves and surplus")))
    s.append(
        p(
            "General reserve ₹40,000 (no transfer asked). Surplus = opening ₹55,000 + profit ₹63,000 = ₹1,18,000. "
            "Total reserves = ₹40,000 + ₹1,18,000 = ₹1,58,000."
        )
    )

    s.append(p(b("WN 11  Property, plant and equipment")))
    s.append(
        table(
            ["Class", "Cost ₹", "Depreciation for the year ₹", "Net ₹"],
            [
                ["Land and building", "4,00,000", "20,000", "3,80,000"],
                ["Plant", "2,50,000", "25,000", "2,25,000"],
                ["Furniture", "60,000", "6,000", "54,000"],
                ["Total", "7,10,000", "51,000", "6,59,000"],
            ],
            foot="No opening accumulated depreciation is given, so the year's charge is the entire accumulated figure at year-end.",
        )
    )

    s.append(p(b("WN 12  Trade receivables")))
    s.append(
        p(
            "Sundry debtors ₹1,40,000 + bills receivable (from customers) ₹30,000 = ₹1,70,000 gross. "
            "Less provision ₹7,000. Net ₹1,63,000. "
            "Provision was computed on sundry debtors only (5% × ₹1,40,000), which is the usual exam reading of '5% of trade receivables' when bills are listed separately and said to be good."
        )
    )

    s.append(p(b("WN 13  Other current liabilities")))
    s.append(p("Outstanding salaries ₹10,000 + Outstanding debenture interest ₹12,000 = ₹22,000."))

    s.append(p(b("WN 14  Other current assets")))
    s.append(p("Prepaid insurance ₹3,000."))

    s.append(h4("Step 2 — Statement of Profit and Loss for the year ended 31 March 2026"))
    s.append(
        table(
            ["", "Particulars", "Note", "₹"],
            [
                ["I", "Revenue from operations", "1", "9,50,000"],
                ["II", "Other income", "2", "39,000"],
                ["III", "Total income (I + II)", "", "<strong>9,89,000</strong>"],
                ["IV", "Expenses", "", ""],
                ["", "&nbsp;&nbsp;Purchases of stock-in-trade", "", "6,20,000"],
                ["", "&nbsp;&nbsp;Changes in inventories of stock-in-trade", "3", "(30,000)"],
                ["", "&nbsp;&nbsp;Employee benefits expense", "4", "1,20,000"],
                ["", "&nbsp;&nbsp;Finance costs", "5", "24,000"],
                ["", "&nbsp;&nbsp;Depreciation and amortisation expense", "6", "51,000"],
                ["", "&nbsp;&nbsp;Other expenses", "7", "1,06,000"],
                ["", "Total expenses", "", "<strong>8,91,000</strong>"],
                ["V", "Profit before exceptional items and tax (III − IV)", "", "98,000"],
                ["VI", "Exceptional items", "", "—"],
                ["VII", "Profit before tax", "", "98,000"],
                ["VIII", "Tax expense — current tax", "8", "35,000"],
                ["IX", "Profit for the period", "", "<strong>63,000</strong>"],
            ],
            caption="Horizon Ltd — Statement of Profit and Loss (Schedule III)",
        )
    )

    s.append(h4("Step 3 — Balance Sheet as at 31 March 2026"))
    s.append(
        table(
            ["Particulars", "Note", "₹"],
            [
                ["<strong>I  EQUITY AND LIABILITIES</strong>", "", ""],
                ["1. Shareholders' funds", "", ""],
                ["&nbsp;&nbsp;(a) Share capital", "9", "5,00,000"],
                ["&nbsp;&nbsp;(b) Reserves and surplus", "10", "1,58,000"],
                ["2. Share application money pending allotment", "", "—"],
                ["3. Non-current liabilities", "", ""],
                ["&nbsp;&nbsp;(a) Long-term borrowings — 12% Debentures", "11", "2,00,000"],
                ["4. Current liabilities", "", ""],
                ["&nbsp;&nbsp;(a) Short-term borrowings", "", "—"],
                ["&nbsp;&nbsp;(b) Trade payables", "12", "90,000"],
                ["&nbsp;&nbsp;(c) Other current liabilities", "13", "22,000"],
                ["&nbsp;&nbsp;(d) Short-term provisions", "14", "35,000"],
                ["<strong>Total</strong>", "", "<strong>10,05,000</strong>"],
                ["<strong>II  ASSETS</strong>", "", ""],
                ["1. Non-current assets", "", ""],
                ["&nbsp;&nbsp;(a) Property, plant and equipment", "6", "6,59,000"],
                ["2. Current assets", "", ""],
                ["&nbsp;&nbsp;(a) Inventories", "3", "1,10,000"],
                ["&nbsp;&nbsp;(b) Trade receivables", "15", "1,63,000"],
                ["&nbsp;&nbsp;(c) Cash and cash equivalents", "", "70,000"],
                ["&nbsp;&nbsp;(d) Other current assets", "16", "3,000"],
                ["<strong>Total</strong>", "", "<strong>10,05,000</strong>"],
            ],
            caption="Horizon Ltd — Balance Sheet (Schedule III)",
            foot="Equity and liabilities: 5,00,000 + 1,58,000 = 6,58,000; + 2,00,000 = 8,58,000; + 90,000 + 22,000 + 35,000 = 10,05,000. "
            "Assets: 6,59,000 + 1,10,000 = 7,69,000; + 1,63,000 = 9,32,000; + 70,000 = 10,02,000; + 3,000 = 10,05,000. Tied.",
        )
    )

    s.append(h4("Step 4 — Notes to Accounts"))
    s.append(
        table(
            ["Note", "Particulars", "₹"],
            [
                ["1", "Revenue from operations — sale of products", "9,50,000"],
                ["2", "Other income — dividend received ₹19,000 + rent received ₹20,000", "39,000"],
                ["3", "Inventories — stock-in-trade (closing). Change during the year: opening ₹80,000 − closing ₹1,10,000 = (₹30,000)", "1,10,000"],
                ["4", "Employee benefits — salaries ₹1,10,000 + outstanding ₹10,000", "1,20,000"],
                ["5", "Finance costs — interest on 12% debentures (12/100 × ₹2,00,000)", "24,000"],
                ["6", "PPE / Depreciation — see WN 11. Depreciation charged ₹51,000; net block ₹6,59,000", "6,59,000"],
                ["7", "Other expenses — rent ₹48,000 + insurance ₹9,000 + electricity ₹18,000 + advertisement ₹22,000 + bad debts ₹8,000 + increase in PFDD ₹1,000", "1,06,000"],
                ["8", "Tax expense — current tax", "35,000"],
                [
                    "9",
                    "Share capital. Authorised: 1,00,000 equity shares of ₹10 = ₹10,00,000. Issued, subscribed and fully paid: 50,000 equity shares of ₹10 = ₹5,00,000. No calls in arrears. No movement in the number of shares during the year.",
                    "5,00,000",
                ],
                ["10", "Reserves and surplus — general reserve ₹40,000 + surplus ₹1,18,000 (opening ₹55,000 + profit ₹63,000). No proposed dividend recognised as a liability.", "1,58,000"],
                ["11", "Long-term borrowings — 12% Debentures, unsecured, not due within 12 months. Interest outstanding is not added here; it is in Note 13.", "2,00,000"],
                [
                    "12",
                    "Trade payables ₹90,000. Of which: dues of micro and small enterprises — not ascertained from the given data; dues of other creditors ₹90,000 (disclosure principle stated).",
                    "90,000",
                ],
                ["13", "Other current liabilities — outstanding salaries ₹10,000 + outstanding debenture interest ₹12,000", "22,000"],
                ["14", "Short-term provisions — provision for tax", "35,000"],
                ["15", "Trade receivables — sundry debtors ₹1,40,000 + bills receivable ₹30,000 = ₹1,70,000, less provision for doubtful debts ₹7,000", "1,63,000"],
                ["16", "Other current assets — prepaid insurance", "3,000"],
            ],
            caption="Horizon Ltd — Notes to Accounts",
        )
    )

    s.append(
        p(
            b("Why the Balance Sheet must be ₹10,05,000, in one paragraph."),
            " Start from PPE at cost ₹7,10,000 minus this year's depreciation ₹51,000 = ₹6,59,000. "
            "Add closing inventory ₹1,10,000, net receivables ₹1,63,000, cash ₹70,000, prepaid ₹3,000. "
            "That is every asset that still exists on 31 March. On the other side, owners have share capital ₹5,00,000 plus reserves ₹1,58,000; "
            "debenture-holders have ₹2,00,000; suppliers ₹90,000; unpaid salary and interest ₹22,000; tax provision ₹35,000. "
            "Sources ₹10,05,000 equal uses ₹10,05,000."
        )
    )
    s.append(
        exam_tip(
            "In the answer book, write workings first (they carry marks even if a face total slips), then P&L, then Balance Sheet, then notes. "
            "Box the two grand totals. If they differ, the usual missing piece is outstanding interest (expense remembered, liability forgotten) "
            "or closing stock (P&L credited, asset forgotten)."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 12. Exam skills: identify, mistakes, memory, 5-mark
# ---------------------------------------------------------------------------


def _exam_skills() -> str:
    s = []
    s.append(h2("How to identify the question, traps, and a 5-mark theory answer", "exam-skills"))
    s.append(
        identify(
            "The question is this chapter when it says any of: "
            "'prepare the Statement of Profit and Loss and Balance Sheet as per Schedule III'; "
            "'as per Companies Act, 2013'; "
            "'in the prescribed form'; "
            "the entity is 'Ltd' / 'Limited' / 'Pvt Ltd' and you are given a trial balance plus adjustments. "
            "If it asks only for a cash flow, that is the next chapter. If it asks ratios, that is the ratios chapter — "
            "but those ratios are computed from the Schedule III statements you have just learned to build."
        )
    )
    s.append(
        mistakes(
            [
                "Putting drawings in a company problem. Companies do not have drawings; they have dividends.",
                "Mixing Trade payables with borrowings (bank overdraft) and with Other current liabilities (outstanding expenses, current maturities, accrued interest).",
                "Forgetting the current vs non-current split — dumping a 5-year loan and next year's instalment in one line.",
                "Showing proposed dividend as an expense in the Statement of Profit and Loss. It is not an expense. Modern treatment: note only, no liability until declared.",
                "Not netting provision for doubtful debts against Trade receivables, and instead parking it under liabilities.",
                "Forgetting outstanding interest on both sides: it is Finance costs AND Other current liabilities.",
                "Charging depreciation inside Other expenses instead of the prescribed Depreciation line.",
                "Putting interest received inside Revenue from operations, or interest paid inside Other expenses.",
                "Adding authorised capital into the Balance Sheet total.",
                "Leaving current-year profit out of Reserves and surplus — then the Balance Sheet will not tie.",
                "Using a 1956 horizontal T-shape instead of the vertical Schedule III order.",
                "Ignoring 'increase in provision': if the TB already has a provision, only the extra amount is this year's expense.",
            ]
        )
    )
    s.append(
        memory(
            "Liabilities tell you who funded the assets. Notes are the footnotes of the story. "
            "P&L is the movie of the year; Balance Sheet is the photograph on 31 March. "
            "Current = within a year (or the cycle). Interest paid is finance cost; interest earned is other income. "
            "No drawings. Dividend is not an expense. Proposed dividend, today, is a note."
        )
    )
    s.append(
        qna(
            "What is Schedule III of the Companies Act, 2013? State the major heads of the Balance Sheet.",
            "<p>Schedule III is the schedule to the Companies Act, 2013 that prescribes the format of the Balance Sheet "
            "and the Statement of Profit and Loss of a company. It requires vertical presentation, classification of items "
            "into current and non-current, corresponding figures of the previous year, and Notes to Accounts, so that the "
            "statements give a true and fair view and can be compared across companies.</p>"
            "<p>Major heads of the Balance Sheet:</p>"
            "<p><strong>Equity and Liabilities —</strong> (1) Shareholders' funds: share capital; reserves and surplus; "
            "money received against share warrants. (2) Share application money pending allotment. "
            "(3) Non-current liabilities: long-term borrowings; deferred tax liabilities (net); other long-term liabilities; "
            "long-term provisions. (4) Current liabilities: short-term borrowings; trade payables; other current liabilities; "
            "short-term provisions.</p>"
            "<p><strong>Assets —</strong> (1) Non-current assets: property, plant and equipment / fixed assets (tangible and intangible); "
            "non-current investments; deferred tax assets (net); long-term loans and advances; other non-current assets. "
            "(2) Current assets: current investments; inventories; trade receivables; cash and cash equivalents; "
            "short-term loans and advances; other current assets.</p>",
            marks="5 marks",
        )
    )
    s.append(
        exam_answer(
            "Schedule III of the Companies Act, 2013 prescribes the vertical form of the Balance Sheet and Statement of Profit and Loss. "
            "The Balance Sheet major heads are: Shareholders' funds; Share application money pending allotment; Non-current liabilities; "
            "Current liabilities; Non-current assets; Current assets — each with the sub-heads listed in the 5-mark answer above. "
            "Items are classified current or non-current using the operating cycle / 12-month rule, and the face is supported by Notes to Accounts."
        )
    )
    s.append(
        steps(
            [
                "Underline 'Schedule III' / 'Companies Act 2013' / 'Ltd'. Draw the empty P&L and BS skeletons with heads.",
                "Tick every TB item into a skeleton line (or into a working that feeds a line). Do not leave an item un-ticked.",
                "Process adjustments in order: stock, outstanding, prepaid, accrued, unearned, depreciation, interest, provision, PFDD, samples, commission, tax, dividend.",
                "Compute P&L down to Profit for the period. Transfer that profit to surplus.",
                "Build notes. Cross-foot each note to the face.",
                "Total Equity and Liabilities. Total Assets. If they differ, hunt outstanding interest, closing stock, and the profit transfer first.",
            ],
            title="7. 16-mark procedure you can write in the margin",
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# 13. Practice
# ---------------------------------------------------------------------------


def _practice() -> str:
    s = []
    s.append(h2("Practice — then check the solution", "practice"))
    s.append(
        practice(
            "4.1",
            "Easy",
            "Where does each item sit?",
            p("State the Schedule III line (P&L or Balance Sheet) for: (i) Bank overdraft (ii) Outstanding audit fee (iii) Securities premium "
              "(iv) Interest on debentures (v) Dividend received (vi) Provision for tax (vii) Prepaid rent (viii) Calls in arrears."),
            a=ul(
                [
                    "(i) Balance Sheet — Current liabilities — Short-term borrowings.",
                    "(ii) Balance Sheet — Other current liabilities; and P&L — Other expenses (if not already in TB).",
                    "(iii) Balance Sheet — Shareholders' funds — Reserves and surplus.",
                    "(iv) P&L — Finance costs. Unpaid slice: Other current liabilities.",
                    "(v) P&L — Other income.",
                    "(vi) P&L — Tax expense; Balance Sheet — Short-term provisions.",
                    "(vii) Balance Sheet — Other current assets; and it reduces Other expenses.",
                    "(viii) Deducted from called-up capital in the Share capital note; face shows paid-up.",
                ]
            ),
        )
    )
    s.append(
        practice(
            "4.2",
            "Moderate",
            "Commission after charging, plus outstanding interest",
            p(
                "Profit before commission, interest outstanding and tax is ₹2,30,000. This figure has not yet been charged with: "
                "(a) outstanding interest on 10% loan of ₹1,00,000 for the full year (nothing paid yet); "
                "(b) manager's commission 10% on profit after charging such commission but before tax; "
                "(c) provision for tax ₹30,000. Compute finance cost, commission, profit before tax, and profit for the period."
            ),
            a=p(b("Step 1 — finance cost."))
            + p("Interest outstanding = 10/100 × ₹1,00,000 = ₹10,000. This is Finance costs. It is also Other current liabilities ₹10,000.")
            + p(b("Step 2 — profit before commission and tax."))
            + p("₹2,30,000 − ₹10,000 = ₹2,20,000.")
            + p(b("Step 3 — commission after charging such commission."))
            + p("Commission = ₹2,20,000 × 10 / 110.")
            + p("₹2,20,000 × 10 = ₹22,00,000.  ₹22,00,000 / 110 = ₹20,000.")
            + p("Check: profit after commission = ₹2,20,000 − ₹20,000 = ₹2,00,000.  10% of ₹2,00,000 = ₹20,000. Holds.")
            + p(b("Step 4 — profit before tax."))
            + p("₹2,20,000 − ₹20,000 = ₹2,00,000.")
            + p(b("Step 5 — profit for the period."))
            + p("Tax ₹30,000. Profit for the period = ₹2,00,000 − ₹30,000 = ₹1,70,000.")
            + p("Employee benefits include outstanding commission ₹20,000. Finance costs ₹10,000. Tax expense ₹30,000. Short-term provisions (tax) ₹30,000. Other current liabilities: interest ₹10,000 + commission ₹20,000 = ₹30,000."),
        )
    )
    s.append(
        practice(
            "4.3",
            "Exam-level",
            "Rebuild three Horizon figures from memory",
            p(
                "Without looking back: (i) write the identity that makes 'Purchases + Changes in inventories' equal COGS for Horizon; "
                "(ii) compute the increase in PFDD; (iii) name the two items inside Other current liabilities and their total. "
                "Then state why proposed dividend, had the board proposed ₹1 per share, would not appear in those liabilities under current Schedule III."
            ),
            a=ul(
                [
                    "(i) Opening ₹80,000 + Purchases ₹6,20,000 − Closing ₹1,10,000 = COGS ₹5,90,000. Purchases ₹6,20,000 + Change (₹30,000) = ₹5,90,000.",
                    "(ii) 5/100 × ₹1,40,000 = ₹7,000 required; existing ₹6,000; increase ₹1,000.",
                    "(iii) Outstanding salaries ₹10,000 + Outstanding debenture interest ₹12,000 = ₹22,000.",
                    "Proposed dividend of 50,000 × ₹1 = ₹50,000 would be disclosed in notes. It is not a liability until declared, so it does not sit in Other current liabilities or Short-term provisions on 31 March 2026.",
                ]
            ),
        )
    )
    s.append(
        connect(
            "You can now wrap any adjusted trial balance of a company in Schedule III clothing. "
            "The next chapter typically takes this Profit before tax / Profit for the period and the Balance Sheet "
            "and asks you to explain cash (cash flow statement) or to compute ratios. Garbage in, garbage out: "
            "if outstanding interest never reached Finance costs, every profitability and coverage ratio later will be wrong."
        )
    )
    return "".join(s)


# ---------------------------------------------------------------------------
# Arithmetic audit (not rendered — for the writer and for anyone debugging)
# ---------------------------------------------------------------------------
# HORIZON LTD as at 31 March 2026
# TB Dr:
#   Land & building 4,00,000
#   Plant 2,50,000
#   Furniture 60,000
#   Purchases 6,20,000
#   Opening inventory 80,000
#   Trade receivables 1,40,000
#   Bills receivable 30,000
#   Cash and bank 70,000
#   Salaries 1,10,000
#   Rent 48,000
#   Insurance 12,000
#   Interest on debentures 12,000
#   Electricity 18,000
#   Advertisement 22,000
#   Bad debts 8,000
#   TB Dr total 18,80,000
# TB Cr:
#   Equity share capital 5,00,000
#   12% Debentures 2,00,000
#   Sales 9,50,000
#   Trade payables 90,000
#   General reserve 40,000
#   Surplus 55,000
#   Provision for doubtful debts 6,000
#   Dividend received 19,000
#   Rent received 20,000
#   TB Cr total 18,80,000
#   TB TIES at 18,80,000.
#
# Adjustments:
#   Closing inventory 1,10,000
#   Dep building 5/100*4,00,000 = 20,000
#   Dep plant 10/100*2,50,000 = 25,000
#   Dep furniture 10/100*60,000 = 6,000
#   Dep total 51,000
#   Outstanding salaries 10,000
#   Prepaid insurance 3,000
#   PFDD required 5/100*1,40,000 = 7,000; existing 6,000; increase 1,000
#   Provision for tax 35,000
#   Debenture interest for year 12/100*2,00,000 = 24,000; TB 12,000; outstanding 12,000
#
# P&L:
#   I  Revenue 9,50,000
#   II Other income 19,000+20,000 = 39,000
#   III Total income 9,89,000
#   Purchases 6,20,000
#   Changes in inventories 80,000-1,10,000 = (30,000)
#   Employee 1,10,000+10,000 = 1,20,000
#   Finance 24,000
#   Depreciation 51,000
#   Other expenses 48,000+9,000+18,000+22,000+8,000+1,000 = 1,06,000
#   IV Total expenses 6,20,000-30,000+1,20,000+24,000+51,000+1,06,000 = 8,91,000
#   V/VII PBT 9,89,000-8,91,000 = 98,000
#   VIII Tax 35,000
#   IX PAT 63,000
#
# Reserves: GR 40,000 + Surplus 55,000+63,000=1,18,000 → 1,58,000
# Shareholders' funds 5,00,000+1,58,000 = 6,58,000
# NCL 2,00,000
# CL: TP 90,000 + OCL 10,000+12,000=22,000 + STP 35,000 = 1,47,000
# Equity & Liabilities 6,58,000+2,00,000+1,47,000 = 10,05,000
#
# PPE net 3,80,000+2,25,000+54,000 = 6,59,000
# Inventories 1,10,000
# Trade receivables 1,40,000+30,000-7,000 = 1,63,000
# Cash 70,000
# Other current assets 3,000
# Assets 6,59,000+1,10,000+1,63,000+70,000+3,000 = 10,05,000
# BS TIES at 10,05,000.
#
# NORTHWIND TRADING LTD
# TB both sides 9,30,000
# Dep 10/100*2,00,000=20,000; 10/100*40,000=4,000; total 24,000
# Outstanding rent 4,000; tax 7,000; closing stock 70,000
# P&L: revenue 5,40,000; purchases 3,60,000; change (20,000); employee 70,000;
#   finance 10,000; dep 24,000; other 40,000+8,000+15,000+6,000=69,000
#   expenses 5,13,000; PBT 27,000; tax 7,000; PAT 20,000
# BS: SC 2,00,000 + GR 20,000 + surplus 30,000+20,000=50,000 → equity 2,70,000
#   NCL 1,00,000; CL 40,000+4,000+7,000=51,000; L total 4,21,000
#   PPE 1,80,000+36,000=2,16,000; CA 70,000+80,000+55,000=2,05,000; A total 4,21,000
#   TIES at 4,21,000.
#
# MANAGER COMMISSION CHECK (example 4.7):
#   Before charging: 10/100*1,10,000 = 11,000; leftover 99,000
#   After charging: 1,10,000*10/110 = 10,000; leftover 1,00,000; 10% of 1,00,000 = 10,000.
#
# PRACTICE 4.2:
#   Start 2,30,000 − interest 10,000 = 2,20,000
#   Commission 2,20,000*10/110 = 20,000
#   PBT 2,00,000; tax 30,000; PAT 1,70,000.
