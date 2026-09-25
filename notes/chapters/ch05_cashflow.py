"""Chapter 5 — Cash Flow Statements.

Beginner-to-exam teaching notes (indirect method, AS-3 / Ind AS-7).

=============================================================================
NUMERICAL PROOFS — A + B + C = change in cash and cash equivalents
-----------------------------------------------------------------------------
MEERA (teaching story):
  A = 75,000   B = -70,000   C = 50,000
  A+B+C = 55,000
  Closing cash 80,000 − Opening cash 25,000 = 55,000

EASY (Sneha Stores):
  A = 93,000   B = -40,000   C = 30,000
  A+B+C = 83,000
  Closing cash 98,000 − Opening cash 15,000 = 83,000

MODERATE (Ravi Traders Ltd.):
  A = 70,000   B = -95,000   C = 37,000
  A+B+C = 12,000
  Closing cash 42,000 − Opening cash 30,000 = 12,000
  BS both years: 3,93,000 (2025) and 4,80,000 (2026)

EXAM (Kaveri Appliances Ltd.):
  A = 2,12,600   B = -1,91,600   C = -10,000
  A+B+C = 11,000
  Closing cash 68,000 − Opening cash 57,000 = 11,000
  BS both years: 8,82,000 (2025) and 10,28,000 (2026)
  Plant: 6,00,000 + 2,00,000 − 80,000 = 7,20,000
  Accum. dep.: 1,20,000 + 60,000 − 30,000 = 1,50,000
  Tax: 40,000 + 55,000 − 45,000 = 50,000
  P&L: 1,40,000 + 1,10,000 − 40,000 = 2,10,000
  Interest received: 80,000 × 8/100 = 6,400 (opening investments; new bought at year-end)
  Interest paid: 2,00,000 × 10/100 = 20,000 (redeemed at year-end)

PRACTICE 1 (Hari Tools):
  A = 1,94,000   B = -81,000   C = 8,000
  A+B+C = 1,21,000
  Closing cash 1,43,000 − Opening cash 22,000 = 1,21,000

PRACTICE 2 (Arjun Textiles Ltd.):
  A = 1,45,000   B = -1,28,000   C = 7,000
  A+B+C = 24,000
  Closing cash 56,000 − Opening cash 32,000 = 24,000
  BS both years: 6,63,000 (2025) and 7,68,000 (2026)
  Plant: 3,50,000 + 1,50,000 − 50,000 = 4,50,000
  Accum. dep.: 70,000 + 45,000 − 20,000 = 95,000
  Tax: 25,000 + 37,000 − 32,000 = 30,000
  P&L: 90,000 + 80,000 − 15,000 (GR) − 25,000 (div) = 1,30,000
=============================================================================
"""

from __future__ import annotations

import sys

sys.path.insert(0, "/workspace/notes")
from html_lib import *


def _in(n) -> str:
    return rupee(n)


def _out(n) -> str:
    return f"({rupee(n)})"


def body() -> str:
    parts: list[str] = []
    parts.append(
        chapter_open(
            "5",
            "Cash Flow Statements",
            "You will be able to explain why profit is not cash, classify every "
            "item into operating / investing / financing activities (AS-3), and "
            "prepare a complete Cash Flow Statement by the indirect method — "
            "including working notes for plant, depreciation, tax, dividend and "
            "interest — so that net cash (A+B+C) equals the change in cash on "
            "the Balance Sheet.",
            [
                "Need and importance of Cash Flow Statement",
                "Preparation of Cash Flow Statement",
                "Indirect Method",
            ],
        )
    )

    # ------------------------------------------------------------------
    # 0. THE HOOK — Profit ≠ Cash (Meera)
    # ------------------------------------------------------------------
    parts.append(h2("Profit is not cash — start here, or the whole chapter will feel like magic", "profit-not-cash"))
    parts.append(
        lead(
            "This is the heart of the chapter. If you only remember one sentence, "
            "remember this: <strong>a business can make a handsome profit and still "
            "run out of cash — and it can make a loss and still have cash coming in.</strong> "
            "The Profit and Loss Account does not tell you what happened to the bank "
            "balance. The Cash Flow Statement does."
        )
    )
    parts.append(
        p(
            "Meet Meera. She runs a small garment shop in Pune. At the year-end her "
            "accountant smiles and says, “Madam, you made a profit of "
            f"{rupee(100000)} this year.” Meera opens her bank app. She expected the "
            "balance to have grown by about the same amount. It has not. She is "
            "confused, and a little angry. This chapter exists because of Meera."
        )
    )
    parts.append(
        p(
            "Here is everything that happened in Meera’s year. We will walk through "
            "<em>each</em> item and ask two questions: <strong>Did this change profit? "
            "Did this change cash?</strong> Those two answers are often different. "
            "That difference is the whole subject."
        )
    )

    parts.append(h3("Meera’s year, item by item"))
    parts.append(
        table(
            ["What happened", "In the Profit & Loss Account?", "In the bank account?"],
            [
                [
                    f"Credit sales still receivable {rupee(40000)} "
                    "(customers have the clothes; Meera does not have the money yet)",
                    f"Yes — sales (and therefore profit) include this {rupee(40000)}",
                    "No cash received. Debtors went up. The bank did not.",
                ],
                [
                    f"Bought a stitching machine for {rupee(70000)} cash",
                    "No — this is an asset, not an expense. Profit is untouched "
                    "(except later, a little, through depreciation).",
                    f"Yes — {rupee(70000)} left the bank today.",
                ],
                [
                    f"Depreciation on shop fittings {rupee(15000)}",
                    f"Yes — it is an expense. It reduced profit by {rupee(15000)}.",
                    "No cash moved. Depreciation is a book entry, not a cheque.",
                ],
                [
                    f"Took a bank loan of {rupee(50000)}",
                    "No — a loan is not income. Profit does not include it.",
                    f"Yes — {rupee(50000)} came into the bank.",
                ],
            ],
            caption="Meera’s four items — profit and cash disagree on every one of them",
        )
    )

    parts.append(
        p(
            "Now let us put full numbers on the same story, so you can <em>see</em> "
            "the gap. Assume the rest of her trading is ordinary cash business, and "
            "she started the year with cash of "
            f"{rupee(25000)}."
        )
    )

    parts.append(h3("Step 1 — How the accountant got profit of ₹1,00,000"))
    parts.append(
        p(
            "Meera’s sales for the year were "
            f"{rupee(500000)}. Out of this, "
            f"{rupee(40000)} is still to be collected from customers, so cash actually "
            f"collected from customers is {rupee(500000)} − {rupee(40000)} = {rupee(460000)}."
        )
    )
    parts.append(
        p(
            "Cash operating expenses (purchases of cloth, wages, rent, electricity, "
            f"all paid in cash) were {rupee(385000)}. Depreciation was {rupee(15000)}. "
            "There were no other expenses."
        )
    )
    parts.append(
        table(
            ["Particulars", "₹"],
            [
                ["Sales", _in(500000)],
                ["Less: Cash operating expenses", _out(385000)],
                [f"Profit before depreciation ({rupee(500000)} − {rupee(385000)})", _in(115000)],
                ["Less: Depreciation (expense, but not cash)", _out(15000)],
                [f"<strong>Net profit</strong> ({rupee(115000)} − {rupee(15000)})", f"<strong>{_in(100000)}</strong>"],
            ],
            caption="Meera’s Profit and Loss Account (condensed)",
        )
    )
    parts.append(
        p(
            "The accountant is not wrong. Profit really is "
            f"{rupee(100000)}. The P&L Account is doing its job. It is just "
            "answering a <em>different question</em> from the one Meera asked her bank app."
        )
    )

    parts.append(h3("Step 2 — What actually happened to the bank balance"))
    parts.append(
        p("Write every cash movement. Do not skip a line. This is how cash works.")
    )
    parts.append(
        table(
            ["Movement", "Work", "₹"],
            [
                ["Opening cash / bank", "given", _in(25000)],
                [
                    "Add: Cash collected from customers",
                    f"{rupee(500000)} − {rupee(40000)} = {rupee(460000)}",
                    _in(460000),
                ],
                ["Less: Cash operating expenses", "given", _out(385000)],
                [
                    "Sub-total after running the shop",
                    f"{rupee(25000)} + {rupee(460000)} − {rupee(385000)} = {rupee(100000)}",
                    _in(100000),
                ],
                ["Less: Machine purchased (cash)", "given", _out(70000)],
                [
                    "Sub-total after buying the machine",
                    f"{rupee(100000)} − {rupee(70000)} = {rupee(30000)}",
                    _in(30000),
                ],
                ["Add: Loan taken", "given", _in(50000)],
                [
                    "<strong>Closing cash / bank</strong>",
                    f"{rupee(30000)} + {rupee(50000)} = {rupee(80000)}",
                    f"<strong>{_in(80000)}</strong>",
                ],
            ],
            caption="Meera’s actual cash movement for the year",
        )
    )
    parts.append(
        keypoint(
            f"Profit = {rupee(100000)}. Increase in cash = "
            f"{rupee(80000)} − {rupee(25000)} = {rupee(55000)}. "
            f"They are not equal. {rupee(100000)} ≠ {rupee(55000)}. "
            "Anyone who treats “profit” as “cash generated” is reading the wrong statement."
        )
    )

    parts.append(h3("Step 3 — The same story, rewritten as a Cash Flow Statement"))
    parts.append(
        p(
            "The indirect method (the method this chapter teaches, and the method "
            "your exam will ask) <em>starts from profit</em> and then <strong>undoes "
            "every item that is not cash, and every item that is not operating</strong>. "
            "Watch how Meera’s four items become four adjustments."
        )
    )
    parts.append(
        table(
            ["Particulars", "₹"],
            [
                ["<strong>Cash flows from operating activities</strong>", ""],
                ["Net profit", _in(100000)],
                [
                    "Add: Depreciation (expense deducted in P&L, but no cash left)",
                    _in(15000),
                ],
                [
                    "Less: Increase in debtors (profit counted a sale that brought no cash)",
                    _out(40000),
                ],
                [
                    f"<strong>Net cash from operating activities (A)</strong> "
                    f"({rupee(100000)} + {rupee(15000)} − {rupee(40000)})",
                    f"<strong>{_in(75000)}</strong>",
                ],
                ["<strong>Cash flows from investing activities</strong>", ""],
                ["Purchase of machinery (cash)", _out(70000)],
                [f"<strong>Net cash from investing activities (B)</strong>", f"<strong>{_out(70000)}</strong>"],
                ["<strong>Cash flows from financing activities</strong>", ""],
                ["Loan taken", _in(50000)],
                [f"<strong>Net cash from financing activities (C)</strong>", f"<strong>{_in(50000)}</strong>"],
                [
                    f"<strong>Net increase in cash (A + B + C)</strong> "
                    f"({rupee(75000)} − {rupee(70000)} + {rupee(50000)})",
                    f"<strong>{_in(55000)}</strong>",
                ],
                ["Add: Opening cash and cash equivalents", _in(25000)],
                [
                    f"<strong>Closing cash and cash equivalents</strong> "
                    f"({rupee(55000)} + {rupee(25000)})",
                    f"<strong>{_in(80000)}</strong>",
                ],
            ],
            caption="Meera — first Cash Flow Statement (indirect method)",
            foot="Proof: A + B + C = 75,000 − 70,000 + 50,000 = 55,000, which equals closing cash 80,000 − opening cash 25,000. The statement is internally true.",
        )
    )
    parts.append(
        logic(
            "Profit measures <em>performance</em> using accrual accounting: you count a "
            "sale when you earn it, and an expense when you consume it — even if cash "
            "moves on a different day, or never moves (depreciation). Cash flow measures "
            "<em>liquidity</em>: what actually went into and out of the bank. Both are "
            "true. They answer different questions. The Cash Flow Statement is the bridge: "
            "it starts from the profit figure you already trust, and walks you, line by "
            "line, to the cash figure you can see in the bank."
        )
    )
    parts.append(
        memory(
            "Three moves, always, in this order: "
            "<strong>(1) Add back non-cash expenses</strong> (depreciation, written-off "
            "items). <strong>(2) Undo non-operating items</strong> that sat inside profit "
            "(profit/loss on sale, interest, dividend income) so they can be placed in "
            "investing or financing. <strong>(3) Squeeze working capital</strong> — "
            "stock, debtors, prepaid, creditors, outstanding — because extra current "
            "assets lock cash and extra current liabilities keep cash in the business. "
            "Then tax paid. That is operating cash. Then buy/sell the tools (investing). "
            "Then talk to owners and lenders (financing)."
        )
    )
    parts.append(
        connect(
            "Chapter on the Profit and Loss Account told you <em>whether</em> the "
            "business earned. Chapter on the Balance Sheet told you <em>what it owns "
            "and owes on a date</em>. This chapter tells you <em>where the cash came "
            "from and where it went during the period</em>. The three statements are a "
            "set. A Cash Flow Statement that does not reconcile to the change in cash "
            "on the two Balance Sheets is simply wrong — the examiner will see it in "
            "ten seconds."
        )
    )

    # ------------------------------------------------------------------
    # 1. Meaning
    # ------------------------------------------------------------------
    parts.append(h2("What is a Cash Flow Statement?", "meaning"))
    parts.append(
        definition(
            "A <strong>Cash Flow Statement (CFS)</strong> is a statement that shows "
            "the inflows (receipts) and outflows (payments) of <em>cash and cash "
            "equivalents</em> during an accounting period, classified into "
            "<strong>operating, investing and financing</strong> activities. It explains "
            "the movement from the opening cash balance to the closing cash balance. "
            "In India it is prepared as per <strong>AS-3 (Cash Flow Statements)</strong> "
            "or, for companies following Ind AS, <strong>Ind AS-7 (Statement of Cash Flows)</strong>."
        )
    )
    parts.append(
        simple(
            "Imagine a video of your bank account for the whole year, sorted into three "
            "folders: (A) money from running the shop, (B) money spent on or received "
            "from long-term assets, (C) money from owners and lenders. That video, "
            "printed as a statement, is the Cash Flow Statement. It does not replace "
            "the P&L. It sits beside it."
        )
    )
    parts.append(
        why(
            "Profit can hide a cash crisis. A fast-growing firm that sells on credit, "
            "fills its godown, and buys a new machine can show a profit and still bounce "
            "a cheque. Lenders, owners and managers cannot wait until the cash actually "
            "runs out. They need a statement whose last line is the same number as the "
            "cash on the Balance Sheet — with every rupee of movement labelled."
        )
    )
    parts.append(
        real_life(
            "A Mumbai trader earns "
            f"{rupee(800000)} profit in a year of boom. Almost all of it is sitting in "
            "debtors (retail chains pay in 90 days) and in extra Diwali stock. He has "
            "also paid "
            f"{rupee(500000)} for a delivery van. His bank account is tight. The P&L "
            "says “well done”. The CFS says “operating cash is weak; investing ate the "
            "rest; you need a working-capital loan or slower growth.” Both statements "
            "are useful. Only one of them would have stopped him bouncing the VAT payment."
        )
    )
    parts.append(
        logic(
            "Accrual accounting records <em>when the right to cash arises</em>, not when "
            "cash arrives. To convert accrual profit into cash, we reverse every accrual "
            "and every non-cash charge, and we park non-operating cash in the activity "
            "that actually produced it. That conversion is the indirect method."
        )
    )

    parts.append(
        table(
            ["Statement", "Question it answers", "What it will not tell you"],
            [
                [
                    "Profit & Loss Account",
                    "Did we earn a profit this year?",
                    "Whether that profit is sitting in the bank, in debtors, or was never cash (depreciation).",
                ],
                [
                    "Balance Sheet",
                    "What do we own and owe <em>on one date</em>?",
                    "How we moved from last year’s cash to this year’s cash.",
                ],
                [
                    "Cash Flow Statement",
                    "Where did cash come from, and where did it go, during the year?",
                    "Whether the business is “profitable”. A firm can have positive cash and a loss, or the reverse.",
                ],
            ],
            caption="The three statements are a set — each answers one question",
        )
    )

    # ------------------------------------------------------------------
    # 2. Need and importance
    # ------------------------------------------------------------------
    parts.append(h2("Need and importance of a Cash Flow Statement", "need"))
    parts.append(
        definition(
            "The <strong>need</strong> for a Cash Flow Statement arises because profit "
            "is an accrual figure. Users who care about <em>liquidity, solvency and "
            "the quality of earnings</em> cannot read those things from the P&L "
            "alone. The CFS is the statement that reports the generation and use of "
            "cash, classified by activity, so that users can judge whether the firm "
            "can pay its bills, repay loans, pay dividends and fund growth from its "
            "own operations."
        )
    )
    parts.append(
        simple(
            "You need a CFS for the same reason you look at your bank SMS thread and "
            "not only at your salary slip. The salary slip is the P&L. The SMS "
            "thread is the cash flow. Both matter. They are not the same document."
        )
    )
    parts.append(
        why(
            "Without a CFS: (i) a lender cannot see whether instalments will be paid "
            "from operations or from fresh borrowing; (ii) management cannot see that "
            "stock and debtors are swallowing cash; (iii) investors cannot see whether "
            "dividends are being paid from genuine operating cash or from selling the "
            "family silver (fixed assets) or from new loans; (iv) the P&L and "
            "Balance Sheet remain two unconnected photographs instead of a film of "
            "the year."
        )
    )
    parts.append(h3("Who uses it, and for what"))
    parts.append(
        table(
            ["User", "What they look for", "Why it matters"],
            [
                [
                    "Management",
                    "Operating cash vs profit; working-capital squeeze; free cash after investing",
                    "Deciding credit policy, stock levels, capex, and whether a loan is needed.",
                ],
                [
                    "Lenders and bankers",
                    "Cash from operations compared with interest and principal due",
                    "A firm that borrows to pay interest is not the same as a firm that generates cash and then borrows to grow.",
                ],
                [
                    "Investors and analysts",
                    "Quality of earnings: is profit turning into cash?",
                    "Profit built on rising debtors is weaker than the same profit collected in cash.",
                ],
                [
                    "Suppliers and employees",
                    "Ability to pay on time",
                    "Outstanding wages and creditors are paid in cash, not in profit.",
                ],
                [
                    "Regulators / tax authorities",
                    "A complete set of financial statements",
                    "Listed and prescribed companies must present a CFS with the annual accounts.",
                ],
            ],
            caption="Users of the Cash Flow Statement",
        )
    )
    parts.append(h3("Legal and accounting status in India (exam points)"))
    parts.append(
        ul(
            [
                "<strong>AS-3 Cash Flow Statements</strong> is the Accounting Standard "
                "for companies that are not on Ind AS. It requires a CFS classifying "
                "cash flows into operating, investing and financing, and permits both "
                "direct and indirect methods for operating cash (Indian MBA exams almost "
                "always want the <em>indirect</em> method).",
                "<strong>Ind AS-7 Statement of Cash Flows</strong> is the Ind-AS version "
                "(aligned with IAS-7). The three-activity structure is the same. The "
                "main exam-relevant difference is that Ind AS-7 <em>allows options</em> "
                "for classifying interest and dividend; AS-3 is stricter. For MBA we "
                "teach the <strong>AS-3 classic classification</strong> unless the "
                "question names Ind AS-7 and asks for the option.",
                "<strong>Companies Act, 2013:</strong> a Cash Flow Statement is part of "
                "the financial statements. It is <strong>mandatory for companies other "
                "than One Person Companies, small companies and dormant companies</strong> "
                "(they are exempt unless they choose to prepare it). "
                "<strong>Listed companies</strong> must prepare it (SEBI LODR + accounting "
                "standards). “Prescribed companies” in older exam language means companies "
                "that the Act / rules require to include a CFS.",
                "The CFS <strong>complements</strong> the P&L and the Balance Sheet. "
                "It does not replace either. Schedule III presentation still starts with "
                "the Balance Sheet and Statement of Profit and Loss; the CFS is the third "
                "primary statement.",
            ]
        )
    )
    parts.append(
        exam_answer(
            "A Cash Flow Statement is needed because the Profit and Loss Account is "
            "prepared on the accrual basis and therefore profit is not equal to cash. "
            "The CFS reports inflows and outflows of cash and cash equivalents, classified "
            "into operating, investing and financing activities, as required by AS-3 "
            "(or Ind AS-7). It is useful to management for liquidity planning, to lenders "
            "for assessing debt-servicing capacity, and to investors for judging the "
            "quality of earnings. Under the Companies Act, 2013 it is mandatory for "
            "companies other than OPC, small companies and dormant companies; listed "
            "companies must prepare it. It complements the P&L and the Balance Sheet "
            "by reconciling the opening and closing cash balances."
        )
    )
    parts.append(
        identify(
            "If the question says <em>“Explain the need / importance / advantages of a "
            "Cash Flow Statement”</em> or <em>“Why is a CFS prepared?”</em> — write the "
            "theory answer above: profit ≠ cash, three activities, users (management, "
            "lenders, investors), AS-3 / Ind AS-7, mandatory for listed and prescribed "
            "companies, complements P&L and BS. This is a 5–8 mark theory question. "
            "If it says <em>“Prepare a Cash Flow Statement”</em> / <em>“indirect method”</em> "
            "/ <em>“AS-3”</em>, it is a practical question — go to the format and the "
            "workings, not the theory."
        )
    )

    # ------------------------------------------------------------------
    # 3. Cash and cash equivalents
    # ------------------------------------------------------------------
    parts.append(h2("Meaning of cash and cash equivalents", "cash-equivalents"))
    parts.append(
        definition(
            "<strong>Cash</strong> comprises cash on hand and demand deposits with banks "
            "(cash at bank). <strong>Cash equivalents</strong> are short-term, highly "
            "liquid investments that are readily convertible into known amounts of cash "
            "and that are subject to an insignificant risk of changes in value. AS-3 "
            "says an investment normally qualifies only when it has a <strong>short "
            "maturity of, say, three months or less from the date of acquisition</strong>."
        )
    )
    parts.append(
        simple(
            "Cash equivalents are not “investments” in the ordinary sense. They are "
            "parking places for spare money that you can turn back into cash almost "
            "at once, without worrying that the price moved. A 60-day Treasury bill "
            "bought two months ago is a cash equivalent. Shares of Infosys, even if "
            "you plan to sell them tomorrow, are <em>not</em> — equity shares have "
            "price risk, so they are investing items, not cash."
        )
    )
    parts.append(
        why(
            "The CFS tracks the movement of the firm’s most liquid resources. If we "
            "counted only the notes in the till, a firm could “improve” its cash by "
            "shifting money into a 30-day deposit and the statement would show a fake "
            "outflow. Treating cash and cash equivalents as one pool stops that game. "
            "The last line of the CFS must equal cash + cash equivalents on the Balance Sheet."
        )
    )
    parts.append(
        real_life(
            "On 31 March a company holds: currency "
            f"{rupee(20000)}, current-account balance {rupee(180000)}, a 91-day T-bill "
            f"bought on 1 March (maturity 30 May) {rupee(50000)}, and 1,000 equity shares "
            f"bought as a temporary parking {rupee(300000)}. Cash and cash equivalents = "
            f"{rupee(20000)} + {rupee(180000)} + {rupee(50000)} = {rupee(250000)}. The "
            "equity shares are <em>investments</em>, not cash equivalents, even though "
            "the treasurer thinks of them as spare money."
        )
    )
    parts.append(
        logic(
            "“Known amount of cash” + “insignificant risk of value change” + “short "
            "maturity (≤ 3 months from acquisition)” is a three-part test. Fail any "
            "one part and the item is an investment (investing activity), not cash. "
            "Equity shares fail the risk test. A two-year bond bought yesterday fails "
            "the maturity test. A six-month FD bought four months ago also fails "
            "(remaining life is short, but AS-3 looks at maturity <em>from the date "
            "of acquisition</em>, not remaining life)."
        )
    )
    parts.append(
        table(
            ["Item", "Cash / cash equivalent?", "Why"],
            [
                ["Cash in hand", "Yes — cash", "Notes and coins."],
                ["Bank current account (favourable balance)", "Yes — cash", "Demand deposit."],
                ["Bank savings account", "Yes — cash", "Withdraw on demand."],
                [
                    "Short-term deposits / T-bills / commercial paper maturing ≤ 3 months from acquisition",
                    "Yes — cash equivalent",
                    "Highly liquid, known amount, insignificant value risk.",
                ],
                [
                    "Equity shares (even listed, even held for 2 days)",
                    "No — investing item",
                    "Price risk is not “insignificant”. AS-3 specifically excludes equity investments.",
                ],
                [
                    "Investments with original maturity of 6 months or 1 year",
                    "No — investing item",
                    "Maturity from acquisition exceeds about three months.",
                ],
                [
                    "Advance to a supplier / deposit with a landlord",
                    "No",
                    "Not cash; not a short-term liquid investment. Working capital / other asset.",
                ],
                [
                    "Bank overdraft repayable on demand",
                    "Exam: follow the question",
                    "AS-3: may be included as a cash equivalent (negative cash) if it is an integral part of cash management. Many MBA papers treat overdraft as a <strong>financing</strong> inflow/outflow. See the box below.",
                ],
            ],
            caption="What is (and is not) cash and cash equivalents",
        )
    )
    parts.append(
        warn(
            "<strong>Bank overdraft — the exam trap.</strong> AS-3 permits a bank "
            "overdraft repayable on demand to be treated as a <em>component of cash "
            "and cash equivalents</em> (so you net it against cash; the change in "
            "overdraft is not shown as financing). In practice, a large number of MBA "
            "and professional papers treat an increase in overdraft as a "
            "<strong>financing inflow</strong> and a decrease as a "
            "<strong>financing outflow</strong>, and they keep “cash” as the favourable "
            "bank balance only. <strong>Rule for the exam: follow the question.</strong> "
            "If the question shows overdraft separately from cash and does not say "
            "“cash and cash equivalents include overdraft”, treat the movement in "
            "overdraft as financing. If it says “cash and cash equivalents” and the "
            "overdraft is listed under that head, net it. Never invent a treatment "
            "that contradicts the question’s own figures."
        )
    )
    parts.append(
        exam_answer(
            "Cash comprises cash on hand and demand deposits with banks. Cash equivalents "
            "are short-term, highly liquid investments that are readily convertible into "
            "known amounts of cash and that are subject to an insignificant risk of changes "
            "in value. An investment normally qualifies as a cash equivalent only when it "
            "has a short maturity of three months or less from the date of acquisition. "
            "Equity shares are not cash equivalents. Bank overdraft repayable on demand "
            "may be treated as a cash equivalent under AS-3 if it is an integral part of "
            "cash management; however, many examination problems treat overdraft as a "
            "financing activity, and that treatment should be followed when the question "
            "presents it that way."
        )
    )

    # ------------------------------------------------------------------
    # 4. Three activities
    # ------------------------------------------------------------------
    parts.append(h2("The three activities — the skeleton of every Cash Flow Statement", "three-activities"))
    parts.append(
        definition(
            "AS-3 requires every cash flow to be classified into one of three activities. "
            "<strong>Operating activities</strong> are the principal revenue-producing "
            "activities of the enterprise and other activities that are not investing or "
            "financing. <strong>Investing activities</strong> are the acquisition and "
            "disposal of long-term assets and other investments not included in cash "
            "equivalents. <strong>Financing activities</strong> are activities that result "
            "in changes in the size and composition of the owners’ capital and borrowings "
            "of the enterprise."
        )
    )
    parts.append(
        simple(
            "<strong>Operations = running the shop. Investing = buying and selling the "
            "shop’s tools (and spare long-term money). Financing = talking to owners and "
            "lenders.</strong> Every line you write on a CFS must sit in one of these "
            "three rooms. If you cannot decide which room, you have not yet understood "
            "the item."
        )
    )
    parts.append(
        why(
            "Classification is the whole point. A firm that generates "
            f"{rupee(10000000)} from operations and spends it on a new plant is a "
            "different animal from a firm that generates "
            f"{rupee(10000000)} by issuing shares and using the money to cover an "
            "operating cash drain. The total change in cash can be identical. The "
            "story is not. Examiners award marks for putting the rupee in the correct "
            "activity, not merely for the final cash figure."
        )
    )
    parts.append(
        memory(
            "Shop / Tools / Owners-and-lenders. If cash moved because a customer, a "
            "supplier, an employee or the tax department was involved in day-to-day "
            "business → operating. If cash moved because a long-term asset or an "
            "investment was bought or sold, or because interest/dividend was "
            "<em>received</em> → investing (AS-3). If cash moved because shares, "
            "debentures or loans were issued or repaid, or because interest/dividend "
            "was <em>paid</em> → financing (AS-3)."
        )
    )

    parts.append(h3("Operating activities"))
    parts.append(
        definition(
            "Operating cash flows are the cash effects of transactions that determine "
            "net profit or loss, other than those that are classified as investing or "
            "financing. In the <strong>indirect method</strong>, we do not list cash "
            "from customers and cash to suppliers. We <em>start from profit</em> and "
            "adjust it until only operating cash remains."
        )
    )
    parts.append(
        simple(
            "If you closed the shutters, stopped buying machines, and neither borrowed "
            "nor repaid anyone — the cash that would still move is operating cash. "
            "Customers pay you. You pay suppliers, staff, rent, power, and income tax. "
            "That is the shop running."
        )
    )
    parts.append(
        real_life(
            "A restaurant’s operating inflows: cash from diners, collections from "
            "credit-card companies. Operating outflows: vegetables, salaries, rent, "
            "gas, GST/income tax paid. Buying a new oven is <em>not</em> operating "
            "(investing). Taking a loan to buy the oven is <em>not</em> operating "
            "(financing). Paying the baker is operating."
        )
    )
    parts.append(
        table(
            ["Typical operating item", "Inflow or outflow", "Indirect-method treatment"],
            [
                ["Cash collected from customers", "Inflow", "Hidden inside profit; increase in debtors is deducted, decrease is added."],
                ["Cash paid to suppliers of goods / services", "Outflow", "Hidden inside profit; increase in stock/prepaid deducted; increase in creditors/outstanding added."],
                ["Wages, salaries, rent, power paid", "Outflow", "Already in profit; outstanding wages movement is a working-capital adjustment."],
                ["Income tax paid", "Outflow", "Shown separately after “cash generated from operations”, not left inside profit."],
                ["Depreciation, amortisation, written-off expenses", "No cash", "Added back to profit (non-cash)."],
                ["Interest paid / dividend paid", "Not operating under AS-3", "Added back if they reduced profit, then shown as <em>financing</em> outflows."],
                ["Interest received / dividend received", "Not operating under AS-3", "Deducted if they increased profit, then shown as <em>investing</em> inflows."],
            ],
            caption="Operating activities — what belongs, and how the indirect method handles it",
        )
    )

    parts.append(h3("Investing activities"))
    parts.append(
        definition(
            "Investing activities are the acquisition and disposal of long-term assets "
            "and of other investments not included in cash equivalents. They show how "
            "much cash was used to obtain resources that will generate future income "
            "and cash flows — and how much cash came back when those resources were sold."
        )
    )
    parts.append(
        simple(
            "Buying or selling the things the business <em>keeps</em> (plant, buildings, "
            "patents, shares of other companies, long-term deposits) is investing. "
            "The cash that changes hands is the <strong>actual sale proceeds or the "
            "actual purchase price</strong>, not the book value, not the profit or loss "
            "on sale. Profit or loss on sale is only a P&L figure; we remove it "
            "from operating and put the real cash in investing."
        )
    )
    parts.append(
        real_life(
            f"A factory sells an old lathe. Cost {rupee(80000)}, accumulated depreciation "
            f"{rupee(50000)}, book value {rupee(30000)}, sold for {rupee(35000)} cash. "
            f"Investing inflow is {rupee(35000)} — the proceeds — not {rupee(30000)} and "
            f"not the profit of {rupee(5000)}. The {rupee(5000)} profit is deducted from "
            "operating profit so it is not counted twice."
        )
    )
    parts.append(
        table(
            ["Typical investing item (AS-3)", "Inflow or outflow", "Notes"],
            [
                ["Purchase of property, plant, equipment, intangibles", "Outflow", "Cash portion only. If bought by issuing shares, that portion is non-cash — exclude."],
                ["Sale proceeds of PPE / intangibles", "Inflow", "Gross proceeds, not book value."],
                ["Purchase of investments (other than cash equivalents)", "Outflow", "Shares, bonds, mutual funds, long-term deposits."],
                ["Sale proceeds of such investments", "Inflow", "Gross proceeds."],
                ["Loans and advances given to third parties", "Outflow", "AS-3: investing. Repayment received = investing inflow."],
                ["Interest received", "Inflow", "AS-3 classic: investing. Deduct from operating if it was inside profit."],
                ["Dividend received", "Inflow", "AS-3 classic: investing. Deduct from operating if it was inside profit."],
                ["Capital work-in-progress paid", "Outflow", "Same family as purchase of PPE."],
            ],
            caption="Investing activities — AS-3 list you must memorise",
        )
    )

    parts.append(h3("Financing activities"))
    parts.append(
        definition(
            "Financing activities are those that result in changes in the size and "
            "composition of the owners’ capital (equity, including preference share "
            "capital) and borrowings of the enterprise. They answer: how did the firm "
            "raise cash from owners and lenders, and how did it return cash to them?"
        )
    )
    parts.append(
        simple(
            "If the other party to the cash movement is an <em>owner</em> (shareholder) "
            "or a <em>lender</em> (bank, debenture-holder), it is financing — with the "
            "AS-3 twist that <strong>interest paid and dividend paid</strong> are also "
            "financing, even though interest was an expense in the P&L."
        )
    )
    parts.append(
        real_life(
            f"A company issues 10,000 equity shares of {rupee(10)} at a premium of "
            f"{rupee(5)}. Cash received = 10,000 × {rupee(15)} = {rupee(150000)}. The "
            "whole "
            f"{rupee(150000)} is a financing inflow (share capital "
            f"{rupee(100000)} + securities premium {rupee(50000)}). The split between "
            "capital and premium matters for the Balance Sheet; for the CFS it is one "
            "cash inflow: proceeds from issue of shares."
        )
    )
    parts.append(
        table(
            ["Typical financing item (AS-3)", "Inflow or outflow", "Notes"],
            [
                ["Proceeds from issue of equity / preference shares (for cash)", "Inflow", "Include securities premium received in cash."],
                ["Proceeds from issue of debentures / bonds", "Inflow", "Cash actually received (after discount, if issued at discount for cash)."],
                ["Long-term or short-term loans taken", "Inflow", "Bank term loan, deposits accepted, etc."],
                ["Repayment of loans / redemption of debentures / preference shares", "Outflow", "Cash actually paid. Premium on redemption is part of the outflow."],
                ["Buy-back of shares", "Outflow", "Financing."],
                ["Interest paid", "Outflow", "AS-3: financing. Add back in operating if it reduced profit."],
                ["Dividend paid (equity or preference)", "Outflow", "AS-3: financing. Dividend is appropriation, not operating."],
                ["Bonus issue / conversion of debentures into shares / asset bought by issuing shares", "Neither — non-cash", "Disclose in a note. Do not put a figure in A, B or C."],
            ],
            caption="Financing activities — AS-3 list you must memorise",
        )
    )

    parts.append(h3("AS-3 classic classification of interest and dividend (memorise this)"))
    parts.append(
        formula(
            "AS-3: Interest received = Investing inflow &nbsp;|&nbsp; "
            "Dividend received = Investing inflow &nbsp;|&nbsp; "
            "Interest paid = Financing outflow &nbsp;|&nbsp; "
            "Dividend paid = Financing outflow",
            "This is the default for MBA exams unless the question names Ind AS-7 and asks you to use an option.",
        )
    )
    parts.append(
        p(
            "<strong>Ind AS-7 options</strong> (know that they exist; do not use them "
            "unless asked): interest paid and interest/dividend received may be "
            "classified as <em>operating or</em> as financing/investing respectively; "
            "dividend paid may be classified as <em>operating or financing</em>. "
            "Once chosen, the policy must be consistent. For this chapter and for "
            "almost every MBA problem, <strong>use the AS-3 classic four-line rule "
            "above</strong>."
        )
    )
    parts.append(
        exam_tip(
            "The examiner’s favourite trick is to leave interest paid inside profit "
            "and then also forget it in financing — or the reverse, to show it in "
            "financing without adding it back in operating. Both errors understate "
            "or overstate total cash by the interest figure. The pair is compulsory: "
            "<strong>add back interest expense in operating, then show interest paid "
            "as a financing outflow.</strong> Same pairing for interest/dividend "
            "<em>income</em>: deduct in operating, show as investing inflow."
        )
    )
    parts.append(
        identify(
            "If the question says <em>“classify the following into operating, investing "
            "and financing”</em>, write three headings and drop each item in the "
            "correct bucket using the AS-3 lists above. If it says "
            "<em>“interest received”</em> without naming Ind AS-7, it is investing. "
            "If it says <em>“dividend paid”</em>, it is financing. If it says "
            "<em>“purchase of machinery by issue of shares”</em>, write "
            "<strong>non-cash investing and financing transaction — disclosed in a "
            "note, not in the CFS body</strong>."
        )
    )

    # ------------------------------------------------------------------
    # 5. Indirect method format
    # ------------------------------------------------------------------
    parts.append(h2("Indirect method — the format you must memorise", "indirect-format"))
    parts.append(
        definition(
            "Under the <strong>indirect method</strong>, net cash from operating "
            "activities is obtained by <em>adjusting net profit before tax</em> for "
            "non-cash items, unpaid/unearned items, non-operating items that belong "
            "in investing or financing, and changes in working capital, and then "
            "deducting income tax paid. Investing and financing sections then list "
            "the actual cash receipts and payments of those activities. Direct method "
            "(cash from customers, cash to suppliers) exists in AS-3 but is "
            "<strong>not</strong> the method this syllabus asks you to prepare."
        )
    )
    parts.append(
        simple(
            "Indirect means: do not start from the cash book. Start from the profit "
            "you already computed. Then repair that profit until it becomes operating "
            "cash. It is called “indirect” because cash from customers is never shown "
            "as a line; it is buried inside “profit ± adjustments”."
        )
    )
    parts.append(
        why(
            "Indian companies almost always publish the indirect method. MBA exams "
            "give you a P&L (or two Balance Sheets from which you reconstruct "
            "profit) plus additional information. That data set is designed for the "
            "indirect format. Learn one format, in this order, and never shuffle the "
            "blocks."
        )
    )
    parts.append(
        format_box(
            "Cash Flow Statement (Indirect Method) as per AS-3",
            table(
                ["Particulars", "₹"],
                [
                    ["<strong>A. Cash flows from operating activities</strong>", ""],
                    ["Net profit before tax", "×××"],
                    ["Adjustments for:", ""],
                    ["&nbsp;&nbsp;Add: Depreciation / amortisation", "×××"],
                    ["&nbsp;&nbsp;Add: Loss on sale of fixed asset / investments", "×××"],
                    ["&nbsp;&nbsp;Less: Profit on sale of fixed asset / investments", "(×××)"],
                    ["&nbsp;&nbsp;Add: Interest expense (to move it to financing)", "×××"],
                    ["&nbsp;&nbsp;Less: Interest income (to move it to investing)", "(×××)"],
                    ["&nbsp;&nbsp;Less: Dividend income (to move it to investing)", "(×××)"],
                    ["&nbsp;&nbsp;Add: Other non-cash expenses (goodwill written off, preliminary expenses written off, etc.)", "×××"],
                    ["<em>Operating profit before working capital changes</em>", "×××"],
                    ["Adjustments for working capital:", ""],
                    ["&nbsp;&nbsp;Add: Decrease in current assets (except cash and cash equivalents)", "×××"],
                    ["&nbsp;&nbsp;Less: Increase in current assets (except cash and cash equivalents)", "(×××)"],
                    ["&nbsp;&nbsp;Add: Increase in current liabilities (except bank overdraft if treated as financing)", "×××"],
                    ["&nbsp;&nbsp;Less: Decrease in current liabilities", "(×××)"],
                    ["<em>Cash generated from operations</em>", "×××"],
                    ["Less: Income tax paid", "(×××)"],
                    ["<strong>Net cash from (used in) operating activities (A)</strong>", "<strong>×××</strong>"],
                    ["<strong>B. Cash flows from investing activities</strong>", ""],
                    ["Purchase of PPE / investments", "(×××)"],
                    ["Sale proceeds of PPE / investments", "×××"],
                    ["Interest received", "×××"],
                    ["Dividend received", "×××"],
                    ["<strong>Net cash from (used in) investing activities (B)</strong>", "<strong>×××</strong>"],
                    ["<strong>C. Cash flows from financing activities</strong>", ""],
                    ["Proceeds from issue of shares / debentures / loans", "×××"],
                    ["Repayment of loans / redemption of debentures", "(×××)"],
                    ["Interest paid", "(×××)"],
                    ["Dividend paid", "(×××)"],
                    ["<strong>Net cash from (used in) financing activities (C)</strong>", "<strong>×××</strong>"],
                    ["<strong>Net increase / (decrease) in cash and cash equivalents (A + B + C)</strong>", "<strong>×××</strong>"],
                    ["Add: Opening cash and cash equivalents", "×××"],
                    ["<strong>Closing cash and cash equivalents</strong> (must equal the Balance Sheet)", "<strong>×××</strong>"],
                ],
                caption="Memorise this skeleton. Every practical question is this skeleton with numbers.",
            ),
        )
    )
    parts.append(
        steps(
            [
                "Read the question and mark three things: the two cash figures (opening and closing), the profit figure (or the two P&L surplus balances from which you will reconstruct profit), and the additional information (depreciation, sales of assets, tax, dividend, interest).",
                "Reconstruct <strong>Net profit before tax</strong> if it is not given: Closing P&L surplus − Opening P&L surplus + dividend paid (and/or current proposed dividend if appropriated) + transfer to reserves + bonus issue from P&L = Profit after tax. Then PAT + current tax charge = PBT. (Full working is later in this chapter.)",
                "Start the operating section with that PBT. Add back every non-cash expense (depreciation, amortisation, written-off items, loss on sale). Deduct every non-cash / non-operating income (profit on sale, interest income, dividend income). Add back interest expense.",
                "You now have operating profit before working capital changes. For every current asset except cash: increase → deduct, decrease → add. For every current liability except items you are treating as financing (often bank overdraft) and except provision for tax / proposed dividend (those have their own workings): increase → add, decrease → deduct.",
                "This gives cash generated from operations. Deduct income tax <em>paid</em> (not the P&L tax charge). Result is <strong>(A)</strong>.",
                "Build investing (B): actual cash paid for PPE and investments, actual sale proceeds, interest received, dividend received. Derive missing purchase / sale figures from Plant A/c and Accumulated Depreciation A/c.",
                "Build financing (C): cash proceeds of issues and loans, cash repayments, interest paid, dividend paid. Ignore bonus issues and conversions.",
                "Compute A + B + C. Add opening cash and cash equivalents. The total <strong>must</strong> equal closing cash and cash equivalents on the Balance Sheet. If it does not, a working is wrong — find it before you move on. This equality is the only full-statement check the examiner has, and it is the only full-statement check you have.",
            ]
        )
    )
    parts.append(
        keypoint(
            "The last three lines are not decoration. "
            "<strong>A + B + C + Opening cash = Closing cash.</strong> "
            "If you cannot make this identity true, you have not finished the question. "
            "Do not “plug” the difference into some random line. Go back to plant, tax, "
            "dividend and working capital — that is where almost every missing rupee hides."
        )
    )

    # ------------------------------------------------------------------
    # 6. Item-by-item table
    # ------------------------------------------------------------------
    parts.append(h2("Every common item — added, deducted, included or excluded", "item-table"))
    parts.append(
        p(
            "Treat this table as a drill sheet. For each item, four questions: "
            "Do I touch operating profit? Do I put a cash line in investing or "
            "financing? Is it a working-capital movement? Or is it non-cash and "
            "therefore excluded from the body of the CFS? Learn the <em>why</em> "
            "column; the rest follows."
        )
    )
    parts.append(
        table(
            ["Item", "Added / Deducted / Included / Excluded", "Which activity", "Why"],
            [
                [
                    "Depreciation",
                    "Added back to profit",
                    "Operating (adjustment only — no cash line)",
                    "It reduced profit but no cash left the bank. Adding it back undoes the deduction.",
                ],
                [
                    "Amortisation of intangibles / patents / computer software",
                    "Added back to profit",
                    "Operating (adjustment)",
                    "Same logic as depreciation: non-cash expense.",
                ],
                [
                    "Profit on sale of fixed asset",
                    "Deducted from profit; sale proceeds included in investing",
                    "Operating (deduct) + Investing (inflow = proceeds)",
                    "The profit is inside PBT but the cash is the full sale proceeds, which is an investing inflow. If you do not deduct the profit, you count it twice (once in operating, once inside proceeds).",
                ],
                [
                    "Loss on sale of fixed asset",
                    "Added back to profit; sale proceeds included in investing",
                    "Operating (add) + Investing (inflow = proceeds)",
                    "The loss reduced profit without being a cash outflow. Adding it back, then showing actual proceeds in investing, puts the true cash in the right place.",
                ],
                [
                    "Goodwill written off",
                    "Added back to profit",
                    "Operating (adjustment)",
                    "Non-cash expense (or appropriation treated as non-cash). No cash moved.",
                ],
                [
                    "Preliminary expenses written off",
                    "Added back to profit",
                    "Operating (adjustment)",
                    "Non-cash write-off of a deferred expense. Cash was spent in an earlier year.",
                ],
                [
                    "Discount on issue of debentures written off",
                    "Added back to profit",
                    "Operating (adjustment)",
                    "Non-cash. The related cash (issue proceeds, redemption) sits in financing.",
                ],
                [
                    "Interest paid (interest expense)",
                    "Added back to profit; then shown as a cash outflow",
                    "Operating (add back) + Financing (outflow) under AS-3",
                    "It reduced PBT but it is not an operating cash flow under AS-3. Pair the two entries or you drop the cash once.",
                ],
                [
                    "Interest received (interest income)",
                    "Deducted from profit; then shown as a cash inflow",
                    "Operating (deduct) + Investing (inflow) under AS-3",
                    "It increased PBT but AS-3 classifies the cash as investing. Pair the two entries.",
                ],
                [
                    "Dividend paid",
                    "Not an expense (appropriation). Do not add/deduct in operating. Show the cash paid.",
                    "Financing outflow under AS-3",
                    "Dividend never sits inside PBT. Find the cash paid from proposed-dividend workings or from additional information.",
                ],
                [
                    "Dividend received",
                    "Deducted from profit if included in PBT; then shown as a cash inflow",
                    "Operating (deduct) + Investing (inflow) under AS-3",
                    "Same pairing as interest received.",
                ],
                [
                    "Issue of shares for cash (including premium received in cash)",
                    "Included as a cash inflow (the actual proceeds)",
                    "Financing inflow",
                    "Owners put cash in. Bonus issue is a different item — see below.",
                ],
                [
                    "Bonus issue",
                    "<strong>Excluded — non-cash</strong>",
                    "None in the CFS body. Disclose in a note if asked.",
                    "Reserves (or P&L) are converted into share capital. No cash moves. If bonus was charged to P&L surplus, add it back when reconstructing PAT, then ignore it in A, B and C.",
                ],
                [
                    "Conversion of debentures into shares",
                    "<strong>Excluded — non-cash</strong>",
                    "None in the CFS body. Disclose in a note.",
                    "Liability becomes equity. No cash. When reconciling debentures and share capital, strip this amount out of “cash proceeds” and “cash redemption”.",
                ],
                [
                    "Purchase of asset by issuing shares (or debentures)",
                    "<strong>Excluded — non-cash</strong> (cash portion, if any, is investing)",
                    "Note. Cash paid, if mixed consideration, is investing outflow.",
                    "AS-3: non-cash investing and financing transactions are disclosed in a note, not in the statement.",
                ],
                [
                    "Increase in debtors (trade receivables)",
                    "Deducted in working capital",
                    "Operating",
                    "Sales were counted in profit but the cash has not arrived. Cash is locked in debtors.",
                ],
                [
                    "Decrease in debtors",
                    "Added in working capital",
                    "Operating",
                    "Old credit sales have been collected. Extra cash came in, over and above this year’s sales.",
                ],
                [
                    "Increase in stock (inventory)",
                    "Deducted in working capital",
                    "Operating",
                    "Cash (or credit that will become cash) was used to buy goods that are still unsold. Cash is locked in the godown.",
                ],
                [
                    "Decrease in stock",
                    "Added in working capital",
                    "Operating",
                    "Stock sold (its cost is in P&L as COGS) was bought in an earlier period. You get the cash effect of running down the godown.",
                ],
                [
                    "Decrease in creditors (trade payables)",
                    "Deducted in working capital",
                    "Operating",
                    "You paid old dues. Extra cash left, over and above this year’s purchases.",
                ],
                [
                    "Increase in creditors",
                    "Added in working capital",
                    "Operating",
                    "Purchases were counted in profit/COGS but not fully paid. Cash was retained.",
                ],
                [
                    "Prepaid expenses (increase)",
                    "Deducted (increase in current asset)",
                    "Operating",
                    "You paid this year for an expense that belongs to next year. Extra cash left.",
                ],
                [
                    "Prepaid expenses (decrease)",
                    "Added (decrease in current asset)",
                    "Operating",
                    "This year’s P&L expense includes a prepayment made last year. Cash did not leave this year for that portion.",
                ],
                [
                    "Outstanding expenses (increase)",
                    "Added (increase in current liability)",
                    "Operating",
                    "Expense is in the P&L but unpaid. Cash still in the bank.",
                ],
                [
                    "Outstanding expenses (decrease)",
                    "Deducted (decrease in current liability)",
                    "Operating",
                    "You paid last year’s outstanding plus this year’s. Extra cash left.",
                ],
                [
                    "Provision for tax (the P&L charge)",
                    "Do not treat as a working-capital item. Start from PBT so the charge is not inside the starting profit. Then deduct <em>tax paid</em>.",
                    "Operating — the cash line is “Income tax paid”",
                    "Tax paid = Opening provision + Current tax charge − Closing provision. Using the closing provision as if it were tax paid is a classic error.",
                ],
                [
                    "Proposed dividend",
                    "Not a working-capital item in the operating section. The cash line is dividend paid, in financing.",
                    "Financing outflow = dividend paid",
                    "Dividend paid = Opening proposed + Interim dividend + Current proposed − Closing proposed (when proposed is shown as a liability on both Balance Sheets). If the question simply gives “dividend paid”, use that figure.",
                ],
                [
                    "Provision for doubtful debts",
                    "Use <strong>net debtors as per the Balance Sheet</strong>. Do not add the provision back as a separate non-cash item, and do not treat the provision as a separate liability.",
                    "Operating, via the movement in net debtors",
                    "If net debtors fall because the provision rose, that decrease is added in WC and it automatically corrects the non-cash charge that reduced profit. One consistent method: always take current assets as they appear on the BS (net).",
                ],
                [
                    "Purchase of fixed assets",
                    "Included as an investing outflow (cash paid)",
                    "Investing",
                    "Derive: Opening FA at cost + Purchases − Cost of assets sold = Closing FA at cost. Purchases = Closing cost − Opening cost + Cost sold. Only the cash portion is an outflow.",
                ],
                [
                    "Sale of fixed assets",
                    "Included as an investing inflow (sale proceeds)",
                    "Investing",
                    "Proceeds = Book value + Profit − Loss. Book value = Cost of asset sold − Accumulated depreciation on it. Never use book value as the cash figure.",
                ],
            ],
            caption="Master treatment table — pin this beside every practical question",
            foot="Working-capital rule in one line: increase in current assets (except cash) → deduct; decrease in current assets → add; increase in current liabilities (except tax provision, proposed dividend, and overdraft-if-financing) → add; decrease in current liabilities → deduct.",
        )
    )
    parts.append(
        formula(
            "Working capital squeeze: CA ↑ = cash locked (deduct). CA ↓ = cash released (add). "
            "CL ↑ = cash retained (add). CL ↓ = cash paid out (deduct).",
            "Current assets here exclude cash and cash equivalents. Current liabilities here exclude items given their own cash line (tax paid, dividend paid) and exclude overdraft when you are treating overdraft as financing.",
        )
    )

    # ------------------------------------------------------------------
    # 7. Working notes — reconstructing missing figures
    # ------------------------------------------------------------------
    parts.append(h2("Working notes the examiner expects — how to find the missing figures", "workings"))
    parts.append(
        p(
            "A typical exam question does <em>not</em> give you profit before tax, tax "
            "paid, purchases of plant, sale proceeds and depreciation in a neat list. "
            "It gives two Balance Sheets and four or five lines of additional "
            "information. You have to <strong>build T-accounts</strong> (or equations) "
            "to find the missing numbers. These workings carry marks of their own. "
            "Show them. Do not hide them inside the CFS."
        )
    )

    parts.append(h3("Working 1 — Reconstruct profit before tax from P&L surplus"))
    parts.append(
        format_box(
            "Profit before tax from two Balance Sheets",
            "<p>Closing balance of Profit & Loss surplus (from BS)</p>"
            "<p>Less: Opening balance of Profit & Loss surplus</p>"
            "<p>= Increase in surplus during the year</p>"
            "<p>Add: Dividend paid / proposed (if it was appropriated out of this year’s profit)</p>"
            "<p>Add: Transfer to general reserve / other reserves</p>"
            "<p>Add: Bonus issue capitalised from P&L</p>"
            "<p>= <strong>Profit after tax (PAT)</strong></p>"
            "<p>Add: Current year’s tax charge (provision made this year)</p>"
            "<p>= <strong>Profit before tax (PBT)</strong> — this is the first line of the CFS</p>",
        )
    )
    parts.append(
        p(
            "If the question already gives “Net profit before tax”, skip this working "
            "and start the CFS with that figure. If it gives “Net profit” after tax, "
            "add the current tax charge to reach PBT. Always be sure whether the "
            "starting figure is before or after tax, and before or after interest. "
            "The standard format starts from <strong>profit before tax, after interest</strong> "
            "— which is why we then add interest back."
        )
    )

    parts.append(h3("Working 2 — Plant (fixed asset) at cost, and purchases"))
    parts.append(
        formula(
            "Opening plant at cost + Purchases − Cost of plant sold = Closing plant at cost",
            "Therefore Purchases = Closing cost − Opening cost + Cost of plant sold. "
            "If no sale is mentioned, Purchases = Closing − Opening (when the BS shows cost, not WDV).",
        )
    )
    parts.append(
        p(
            "Some Balance Sheets show plant at written-down value (after depreciation) "
            "with no separate accumulated-depreciation line. Then the equation is:"
        )
    )
    parts.append(
        formula(
            "Opening WDV + Purchases − WDV of asset sold − Depreciation for the year = Closing WDV",
            "WDV of asset sold = Cost sold − Accumulated depreciation on sold, which equals Sale proceeds − Profit + Loss.",
        )
    )

    parts.append(h3("Working 3 — Accumulated depreciation, and depreciation for the year"))
    parts.append(
        formula(
            "Opening accumulated depreciation + Depreciation charged this year − Accumulated depreciation on asset sold = Closing accumulated depreciation",
            "Therefore Depreciation for the year = Closing accum. dep. − Opening accum. dep. + Accum. dep. on asset sold.",
        )
    )

    parts.append(h3("Working 4 — Sale proceeds of a fixed asset"))
    parts.append(
        formula(
            "Book value (WDV) of asset sold = Cost of asset sold − Accumulated depreciation on it<br/>"
            "Sale proceeds = Book value + Profit on sale − Loss on sale",
            "If the question gives proceeds, you can run the same equation backwards to find profit or loss, and then use that profit/loss in the operating adjustments.",
        )
    )
    parts.append(
        logic(
            "Why we never put book value in the CFS: book value is not cash. The buyer "
            "pays the agreed price. That price is the investing inflow. The difference "
            "between price and book value is a non-cash gain or loss which we park as "
            "an operating adjustment so that it does not contaminate operating cash "
            "and is not double-counted."
        )
    )

    parts.append(h3("Working 5 — Tax paid"))
    parts.append(
        formula(
            "Opening provision for tax + Current year’s tax charge − Closing provision for tax = Tax paid",
            "“Current year’s tax charge” is the amount debited to P&L (the provision made this year). "
            "It is not the same as tax paid, and it is not the same as the closing provision.",
        )
    )
    parts.append(
        p(
            "If the question states “tax paid ₹…”, use that figure directly as the "
            "operating outflow and use the T-account only to find the current-year "
            "charge (which you need to reconstruct PBT). If there is advance tax or "
            "TDS, it is part of tax paid — do not show it twice."
        )
    )

    parts.append(h3("Working 6 — Dividend paid"))
    parts.append(
        formula(
            "When proposed dividend is a Balance-Sheet liability in both years:<br/>"
            "Dividend paid = Opening proposed dividend + Interim dividend (if any) + Current proposed − Closing proposed",
            "Often there is no interim and current proposed is unpaid, so Dividend paid = Opening proposed dividend. "
            "If the question simply says “dividend paid ₹…”, use that. Do not deduct proposed dividend inside operating profit.",
        )
    )
    parts.append(
        warn(
            "Modern Company Law / revised AS-4 / Ind AS: proposed dividend is <em>not</em> "
            "a liability until it is declared. Many current Balance Sheets therefore do "
            "not show proposed dividend. In that case the question will give “dividend "
            "paid” in additional information, and P&L surplus is before that "
            "appropriation or the appropriation is already reflected — follow the "
            "numbers you are given. Older MBA textbooks still show proposed dividend as "
            "a current liability. Both presentations appear in papers. Read the BS."
        )
    )

    parts.append(h3("Working 7 — Interest paid / received"))
    parts.append(
        p(
            "Interest on 10% debentures of "
            f"{rupee(200000)} for a full year = {rupee(200000)} × 10/100 = {rupee(20000)}. "
            "Always write the multiplication. If debentures were issued or redeemed "
            "<em>during</em> the year, the question will usually tell you the interest "
            "figure, or tell you the date so you can compute time-proportion. If it is "
            "silent, a reasonable exam assumption is: issued/redeemed at year-end, so "
            "interest is on the <em>opening</em> balance (for redemption) or on the "
            "<em>opening</em> balance only (for issue at year-end, new money carries "
            "no interest this year). State your assumption in a working note."
        )
    )
    parts.append(
        exam_tip(
            "Outstanding interest is a current liability. If interest <em>expense</em> "
            "is "
            f"{rupee(20000)} and outstanding interest rose by "
            f"{rupee(2000)}, then interest <em>paid</em> = {rupee(20000)} − {rupee(2000)} = "
            f"{rupee(18000)}. Put {rupee(20000)} as the add-back (the P&L figure) and "
            f"{rupee(18000)} as the financing outflow (the cash). Do not also count the "
            "outstanding-interest movement inside the general “outstanding expenses” "
            "line or you will double-count. Cleanest method: keep interest outstanding "
            "out of WC, and compute interest paid from the interest T-account."
        )
    )

    parts.append(h3("Provision for doubtful debts — one consistent method"))
    parts.append(
        p(
            "Two methods exist in textbooks. Mixing them is how students lose marks. "
            "We use <strong>one method only</strong> in this chapter:"
        )
    )
    parts.append(
        keypoint(
            "Take debtors <em>net of provision</em>, exactly as a typical Balance Sheet "
            "presents “Trade receivables”. Do not add back the provision charge as a "
            "separate non-cash item. Do not treat the provision as a separate current "
            "liability. The movement in net debtors already does the right job: a "
            "pure increase in the provision (gross debtors unchanged) reduces net "
            "debtors, which you add in working capital, which cancels the non-cash "
            "charge that reduced profit."
        )
    )

    # ------------------------------------------------------------------
    # 8. Easy example
    # ------------------------------------------------------------------
    parts.append(h2("Solved examples — Easy, then Moderate, then Exam-level", "examples"))
    parts.append(
        p(
            "Three fully worked statements follow. Every arithmetic step is shown. "
            "After each, A + B + C is compared with the change in cash. That comparison "
            "is the proof that the statement is internally true. You should do the same "
            "on every exam script."
        )
    )

    easy_body = (
        p(
            "<strong>Sneha Stores</strong> provides the following information for the "
            "year ended 31 March 2026. Prepare a Cash Flow Statement by the indirect "
            "method."
        )
        + ul(
            [
                f"Net profit before tax: {rupee(100000)}",
                f"Depreciation: {rupee(20000)}",
                f"Tax paid during the year: {rupee(25000)}",
                f"Increase in stock: {rupee(10000)}",
                f"Increase in creditors: {rupee(8000)}",
                f"Purchase of furniture (cash): {rupee(40000)}",
                f"Loan taken: {rupee(30000)}",
                f"Opening cash and cash equivalents: {rupee(15000)}",
            ]
        )
        + p("Closing cash is not given. You must find it. That is normal.")
        + h4("Step 1 — Operating activities (A)")
        + p(
            "Start with profit before tax. Add back depreciation (non-cash). Then "
            "working capital: stock went up — cash locked — deduct. Creditors went "
            "up — cash retained — add. Then deduct tax paid."
        )
        + p(
            f"Operating profit before working capital changes = {rupee(100000)} + "
            f"{rupee(20000)} = {rupee(120000)}."
        )
        + p(
            f"After working capital = {rupee(120000)} − {rupee(10000)} + {rupee(8000)} = "
            f"{rupee(118000)} (this is cash generated from operations)."
        )
        + p(
            f"Net cash from operating activities (A) = {rupee(118000)} − {rupee(25000)} = "
            f"{rupee(93000)}."
        )
        + h4("Step 2 — Investing activities (B)")
        + p(
            f"Only one item: furniture purchased for cash {rupee(40000)}. "
            f"Net cash from investing activities (B) = ({rupee(40000)})."
        )
        + h4("Step 3 — Financing activities (C)")
        + p(
            f"Only one item: loan taken {rupee(30000)}. "
            f"Net cash from financing activities (C) = {rupee(30000)}."
        )
        + h4("Step 4 — Net change and closing cash")
        + p(
            f"A + B + C = {rupee(93000)} − {rupee(40000)} + {rupee(30000)}."
        )
        + p(
            f"{rupee(93000)} − {rupee(40000)} = {rupee(53000)}."
        )
        + p(
            f"{rupee(53000)} + {rupee(30000)} = {rupee(83000)} net increase in cash."
        )
        + p(
            f"Closing cash = {rupee(15000)} + {rupee(83000)} = {rupee(98000)}."
        )
        + table(
            ["Particulars", "₹"],
            [
                ["<strong>Cash flows from operating activities</strong>", ""],
                ["Net profit before tax", _in(100000)],
                ["Adjustments for:", ""],
                ["&nbsp;&nbsp;Depreciation", _in(20000)],
                ["Operating profit before working capital changes", _in(120000)],
                ["&nbsp;&nbsp;Increase in stock", _out(10000)],
                ["&nbsp;&nbsp;Increase in creditors", _in(8000)],
                ["Cash generated from operations", _in(118000)],
                ["Income tax paid", _out(25000)],
                ["<strong>Net cash from operating activities (A)</strong>", f"<strong>{_in(93000)}</strong>"],
                ["<strong>Cash flows from investing activities</strong>", ""],
                ["Purchase of furniture", _out(40000)],
                ["<strong>Net cash from investing activities (B)</strong>", f"<strong>{_out(40000)}</strong>"],
                ["<strong>Cash flows from financing activities</strong>", ""],
                ["Loan taken", _in(30000)],
                ["<strong>Net cash from financing activities (C)</strong>", f"<strong>{_in(30000)}</strong>"],
                ["<strong>Net increase in cash and cash equivalents (A + B + C)</strong>", f"<strong>{_in(83000)}</strong>"],
                ["Opening cash and cash equivalents", _in(15000)],
                ["<strong>Closing cash and cash equivalents</strong>", f"<strong>{_in(98000)}</strong>"],
            ],
            caption="Sneha Stores — Cash Flow Statement for the year ended 31 March 2026 (indirect method)",
            foot="Proof: 93,000 − 40,000 + 30,000 = 83,000 = 98,000 − 15,000.",
        )
    )
    parts.append(
        example("5.1", "Easy", "Sneha Stores — first full CFS from a short list of facts", easy_body)
    )

    # ------------------------------------------------------------------
    # 9. Moderate example
    # ------------------------------------------------------------------
    moderate_q = (
        p(
            "<strong>Ravi Traders Ltd.</strong> gives its summarised Balance Sheets and "
            "additional information. Prepare a Cash Flow Statement (indirect method) "
            "for the year ended 31 March 2026, with working notes."
        )
        + table(
            ["Particulars", "31 March 2025 ₹", "31 March 2026 ₹"],
            [
                ["<strong>Equity and liabilities</strong>", "", ""],
                ["Equity share capital", _in(200000), _in(240000)],
                ["10% Debentures", _in(80000), _in(100000)],
                ["Profit & Loss A/c (surplus)", _in(60000), _in(95000)],
                ["Trade creditors", _in(35000), _in(28000)],
                ["Outstanding expenses", _in(4000), _in(6000)],
                ["Provision for tax", _in(14000), _in(11000)],
                ["<strong>Total</strong>", f"<strong>{_in(393000)}</strong>", f"<strong>{_in(480000)}</strong>"],
                ["<strong>Assets</strong>", "", ""],
                ["Plant at cost", _in(250000), _in(320000)],
                ["Less: Accumulated depreciation", _out(50000), _out(70000)],
                ["Plant (net)", _in(200000), _in(250000)],
                ["Investments", _in(50000), _in(70000)],
                ["Inventory", _in(60000), _in(75000)],
                ["Trade debtors", _in(45000), _in(38000)],
                ["Prepaid expenses", _in(8000), _in(5000)],
                ["Cash and cash equivalents", _in(30000), _in(42000)],
                ["<strong>Total</strong>", f"<strong>{_in(393000)}</strong>", f"<strong>{_in(480000)}</strong>"],
            ],
            caption="Ravi Traders Ltd. — summarised Balance Sheets",
        )
        + p("<strong>Additional information</strong>")
        + ol(
            [
                f"Plant costing {rupee(20000)} (accumulated depreciation on it {rupee(8000)}) was sold for {rupee(15000)}.",
                "The rest of the movement in plant at cost is a cash purchase of plant.",
                f"Debentures of {rupee(20000)} were issued at par for cash at the end of the year.",
                f"Interest on debentures paid during the year {rupee(8000)} "
                f"(computed as {rupee(80000)} × 10/100 = {rupee(8000)}; new debentures carry no interest this year).",
                f"Tax paid during the year {rupee(23000)}.",
                f"Dividend paid during the year {rupee(15000)}.",
                "Equity shares were issued at par for cash. No bonus issue.",
            ]
        )
    )

    moderate_a = (
        h4("Working note 1 — Plant at cost (purchases)")
        + p(
            f"Opening plant at cost {rupee(250000)} + Purchases − Cost of plant sold "
            f"{rupee(20000)} = Closing plant at cost {rupee(320000)}."
        )
        + p(
            f"Purchases = {rupee(320000)} − {rupee(250000)} + {rupee(20000)} = "
            f"{rupee(70000)} + {rupee(20000)} = {rupee(90000)}."
        )
        + t_account(
            "Plant A/c (at cost)",
            [
                ("To Balance b/d", rupee(250000)),
                ("To Bank (purchases)", rupee(90000)),
            ],
            [
                ("By Asset sold (cost)", rupee(20000)),
            ],
            cr_bal=rupee(320000),
        )
        + h4("Working note 2 — Accumulated depreciation (depreciation for the year)")
        + p(
            f"Opening accum. dep. {rupee(50000)} + Depreciation for the year − Accum. dep. "
            f"on asset sold {rupee(8000)} = Closing accum. dep. {rupee(70000)}."
        )
        + p(
            f"Depreciation for the year = {rupee(70000)} − {rupee(50000)} + {rupee(8000)} = "
            f"{rupee(20000)} + {rupee(8000)} = {rupee(28000)}."
        )
        + t_account(
            "Accumulated Depreciation A/c",
            [
                ("To Asset sold", rupee(8000)),
            ],
            [
                ("By Balance b/d", rupee(50000)),
                ("By Profit & Loss (dep.)", rupee(28000)),
            ],
            dr_bal=rupee(70000),
        )
        + h4("Working note 3 — Profit / loss on sale of plant, and sale proceeds")
        + p(
            f"Book value of plant sold = Cost {rupee(20000)} − Accum. dep. {rupee(8000)} = {rupee(12000)}."
        )
        + p(
            f"Sold for {rupee(15000)}. Profit on sale = {rupee(15000)} − {rupee(12000)} = {rupee(3000)}."
        )
        + p(
            f"Investing inflow = sale proceeds {rupee(15000)} (not the book value, not the profit)."
        )
        + h4("Working note 4 — Provision for tax (current tax charge)")
        + p(
            f"Opening provision {rupee(14000)} + Current tax charge − Tax paid {rupee(23000)} = "
            f"Closing provision {rupee(11000)}."
        )
        + p(
            f"Current tax charge = {rupee(11000)} − {rupee(14000)} + {rupee(23000)} = "
            f"{rupee(20000)}."
        )
        + p(
            f"Check: {rupee(14000)} + {rupee(20000)} − {rupee(23000)} = {rupee(11000)}. Yes."
        )
        + t_account(
            "Provision for Tax A/c",
            [
                ("To Bank (tax paid)", rupee(23000)),
            ],
            [
                ("By Balance b/d", rupee(14000)),
                ("By Profit & Loss (current tax)", rupee(20000)),
            ],
            dr_bal=rupee(11000),
        )
        + h4("Working note 5 — Profit before tax")
        + p(
            f"Increase in P&L surplus = {rupee(95000)} − {rupee(60000)} = {rupee(35000)}."
        )
        + p(
            f"This increase is after dividend of {rupee(15000)} was paid (appropriated). "
            f"So PAT = {rupee(35000)} + {rupee(15000)} = {rupee(50000)}."
        )
        + p(
            f"PBT = PAT + current tax charge = {rupee(50000)} + {rupee(20000)} = {rupee(70000)}."
        )
        + p(
            f"This {rupee(70000)} is after charging depreciation {rupee(28000)}, after "
            f"including profit on sale {rupee(3000)}, and after charging interest "
            f"{rupee(8000)}. Those three will be adjusted in operating."
        )
        + h4("Working note 6 — Other movements (read off the two Balance Sheets)")
        + ul(
            [
                f"Equity share capital issued for cash = {rupee(240000)} − {rupee(200000)} = {rupee(40000)}.",
                f"Debentures issued for cash = {rupee(100000)} − {rupee(80000)} = {rupee(20000)} (matches additional info).",
                f"Investments purchased = {rupee(70000)} − {rupee(50000)} = {rupee(20000)} (cash; investing outflow).",
                f"Inventory increased = {rupee(75000)} − {rupee(60000)} = {rupee(15000)} (deduct).",
                f"Debtors decreased = {rupee(45000)} − {rupee(38000)} = {rupee(7000)} (add).",
                f"Prepaid expenses decreased = {rupee(8000)} − {rupee(5000)} = {rupee(3000)} (add).",
                f"Creditors decreased = {rupee(35000)} − {rupee(28000)} = {rupee(7000)} (deduct).",
                f"Outstanding expenses increased = {rupee(6000)} − {rupee(4000)} = {rupee(2000)} (add).",
            ]
        )
        + h4("Cash Flow Statement")
        + p(
            f"Operating profit before WC = PBT {rupee(70000)} + Dep {rupee(28000)} − Profit on sale "
            f"{rupee(3000)} + Interest expense {rupee(8000)}."
        )
        + p(
            f"{rupee(70000)} + {rupee(28000)} = {rupee(98000)}."
        )
        + p(
            f"{rupee(98000)} − {rupee(3000)} = {rupee(95000)}."
        )
        + p(
            f"{rupee(95000)} + {rupee(8000)} = {rupee(103000)}."
        )
        + p(
            "Working capital adjustments:"
        )
        + p(
            f"{rupee(103000)} − inventory {rupee(15000)} = {rupee(88000)}."
        )
        + p(
            f"{rupee(88000)} + debtors {rupee(7000)} = {rupee(95000)}."
        )
        + p(
            f"{rupee(95000)} + prepaid {rupee(3000)} = {rupee(98000)}."
        )
        + p(
            f"{rupee(98000)} − creditors {rupee(7000)} = {rupee(91000)}."
        )
        + p(
            f"{rupee(91000)} + outstanding {rupee(2000)} = {rupee(93000)} cash generated from operations."
        )
        + p(
            f"Tax paid {rupee(23000)}. Net operating (A) = {rupee(93000)} − {rupee(23000)} = {rupee(70000)}."
        )
        + p(
            f"Investing (B) = − plant purchased {rupee(90000)} + sale proceeds {rupee(15000)} − investments "
            f"{rupee(20000)} = −{rupee(90000)} + {rupee(15000)} = −{rupee(75000)}; −{rupee(75000)} − "
            f"{rupee(20000)} = −{rupee(95000)}."
        )
        + p(
            f"Financing (C) = share issue {rupee(40000)} + debenture issue {rupee(20000)} − interest paid "
            f"{rupee(8000)} − dividend paid {rupee(15000)}."
        )
        + p(
            f"{rupee(40000)} + {rupee(20000)} = {rupee(60000)}."
        )
        + p(
            f"{rupee(60000)} − {rupee(8000)} = {rupee(52000)}."
        )
        + p(
            f"{rupee(52000)} − {rupee(15000)} = {rupee(37000)}."
        )
        + p(
            f"A + B + C = {rupee(70000)} − {rupee(95000)} + {rupee(37000)}."
        )
        + p(
            f"{rupee(70000)} − {rupee(95000)} = −{rupee(25000)}; −{rupee(25000)} + {rupee(37000)} = {rupee(12000)}."
        )
        + p(
            f"Opening cash {rupee(30000)} + {rupee(12000)} = {rupee(42000)} closing cash, which matches the Balance Sheet."
        )
        + table(
            ["Particulars", "₹"],
            [
                ["<strong>Cash flows from operating activities</strong>", ""],
                ["Net profit before tax", _in(70000)],
                ["Adjustments for:", ""],
                ["&nbsp;&nbsp;Depreciation", _in(28000)],
                ["&nbsp;&nbsp;Profit on sale of plant", _out(3000)],
                ["&nbsp;&nbsp;Interest expense", _in(8000)],
                ["Operating profit before working capital changes", _in(103000)],
                ["&nbsp;&nbsp;Increase in inventory", _out(15000)],
                ["&nbsp;&nbsp;Decrease in debtors", _in(7000)],
                ["&nbsp;&nbsp;Decrease in prepaid expenses", _in(3000)],
                ["&nbsp;&nbsp;Decrease in creditors", _out(7000)],
                ["&nbsp;&nbsp;Increase in outstanding expenses", _in(2000)],
                ["Cash generated from operations", _in(93000)],
                ["Income tax paid", _out(23000)],
                ["<strong>Net cash from operating activities (A)</strong>", f"<strong>{_in(70000)}</strong>"],
                ["<strong>Cash flows from investing activities</strong>", ""],
                ["Purchase of plant", _out(90000)],
                ["Sale proceeds of plant", _in(15000)],
                ["Purchase of investments", _out(20000)],
                ["<strong>Net cash from investing activities (B)</strong>", f"<strong>{_out(95000)}</strong>"],
                ["<strong>Cash flows from financing activities</strong>", ""],
                ["Proceeds from issue of equity shares", _in(40000)],
                ["Proceeds from issue of 10% debentures", _in(20000)],
                ["Interest paid", _out(8000)],
                ["Dividend paid", _out(15000)],
                ["<strong>Net cash from financing activities (C)</strong>", f"<strong>{_in(37000)}</strong>"],
                ["<strong>Net increase in cash and cash equivalents (A + B + C)</strong>", f"<strong>{_in(12000)}</strong>"],
                ["Opening cash and cash equivalents", _in(30000)],
                ["<strong>Closing cash and cash equivalents</strong>", f"<strong>{_in(42000)}</strong>"],
            ],
            caption="Ravi Traders Ltd. — Cash Flow Statement for the year ended 31 March 2026 (indirect method, AS-3)",
            foot="Proof: A + B + C = 70,000 − 95,000 + 37,000 = 12,000 = closing cash 42,000 − opening cash 30,000.",
        )
    )
    parts.append(
        example(
            "5.2",
            "Moderate",
            "Ravi Traders Ltd. — two-year Balance Sheets, sale of plant, tax, dividend, interest",
            moderate_q + moderate_a,
        )
    )

    # ------------------------------------------------------------------
    # 10. Exam-level example
    # ------------------------------------------------------------------
    exam_q = (
        p(
            "<strong>Kaveri Appliances Ltd.</strong> You are given summarised Balance "
            "Sheets and additional information. Prepare a complete Cash Flow Statement "
            "by the indirect method as per AS-3, with working notes for plant, "
            "accumulated depreciation, tax, dividend and interest."
        )
        + table(
            ["Particulars", "31 March 2025 ₹", "31 March 2026 ₹"],
            [
                ["<strong>Equity and liabilities</strong>", "", ""],
                ["Equity share capital", _in(400000), _in(500000)],
                ["10% Debentures", _in(200000), _in(150000)],
                ["Profit & Loss surplus", _in(140000), _in(210000)],
                ["Trade creditors", _in(90000), _in(110000)],
                ["Outstanding expenses", _in(12000), _in(8000)],
                ["Provision for tax", _in(40000), _in(50000)],
                ["<strong>Total</strong>", f"<strong>{_in(882000)}</strong>", f"<strong>{_in(1028000)}</strong>"],
                ["<strong>Assets</strong>", "", ""],
                ["Plant at cost", _in(600000), _in(720000)],
                ["Less: Accumulated depreciation", _out(120000), _out(150000)],
                ["Plant (net)", _in(480000), _in(570000)],
                ["Investments (includes 8% government securities)", _in(80000), _in(120000)],
                ["Inventory", _in(150000), _in(135000)],
                ["Trade debtors", _in(100000), _in(125000)],
                ["Prepaid expenses", _in(15000), _in(10000)],
                ["Cash and cash equivalents", _in(57000), _in(68000)],
                ["<strong>Total</strong>", f"<strong>{_in(882000)}</strong>", f"<strong>{_in(1028000)}</strong>"],
            ],
            caption="Kaveri Appliances Ltd. — summarised Balance Sheets",
        )
        + p("<strong>Additional information</strong>")
        + ol(
            [
                f"Plant costing {rupee(80000)}, on which accumulated depreciation was {rupee(30000)}, was sold for {rupee(42000)} cash.",
                "The remaining increase in plant at cost is a cash purchase.",
                f"Debentures of {rupee(50000)} were redeemed at par at the <em>end</em> of the year.",
                f"Equity shares of {rupee(100000)} were issued at par for cash. There was no bonus issue and no conversion.",
                f"Tax paid during the year {rupee(45000)}.",
                f"Dividend paid during the year {rupee(40000)}.",
                f"Interest on 10% debentures paid {rupee(20000)} "
                f"(= {rupee(200000)} × 10/100 = {rupee(20000)}; redemption at year-end, so interest is on opening debentures).",
                f"Interest received on 8% government securities {rupee(6400)} "
                f"(= {rupee(80000)} × 8/100 = {rupee(6400)}; the additional investments were purchased at the end of the year, so they earned nothing this year). This interest is included in profit.",
            ]
        )
    )

    exam_a = (
        h4("Working note 1 — Plant A/c (purchases)")
        + p(
            f"Opening cost {rupee(600000)} + Purchases − Cost sold {rupee(80000)} = Closing cost {rupee(720000)}."
        )
        + p(
            f"Purchases = {rupee(720000)} − {rupee(600000)} + {rupee(80000)} = {rupee(120000)} + {rupee(80000)} = {rupee(200000)}."
        )
        + t_account(
            "Plant A/c (at cost)",
            [
                ("To Balance b/d", rupee(600000)),
                ("To Bank (purchases)", rupee(200000)),
            ],
            [
                ("By Asset sold (cost)", rupee(80000)),
            ],
            cr_bal=rupee(720000),
        )
        + h4("Working note 2 — Accumulated Depreciation A/c")
        + p(
            f"Opening {rupee(120000)} + Depreciation for the year − On asset sold {rupee(30000)} = Closing {rupee(150000)}."
        )
        + p(
            f"Depreciation for the year = {rupee(150000)} − {rupee(120000)} + {rupee(30000)} = {rupee(30000)} + {rupee(30000)} = {rupee(60000)}."
        )
        + t_account(
            "Accumulated Depreciation A/c",
            [
                ("To Asset sold", rupee(30000)),
            ],
            [
                ("By Balance b/d", rupee(120000)),
                ("By Profit & Loss (dep.)", rupee(60000)),
            ],
            dr_bal=rupee(150000),
        )
        + h4("Working note 3 — Sale of plant (loss and proceeds)")
        + p(
            f"Book value of plant sold = {rupee(80000)} − {rupee(30000)} = {rupee(50000)}."
        )
        + p(
            f"Sale proceeds given = {rupee(42000)}."
        )
        + p(
            f"Loss on sale = {rupee(50000)} − {rupee(42000)} = {rupee(8000)}."
        )
        + t_account(
            "Asset Disposal / Sale of Plant A/c",
            [
                ("To Plant (cost)", rupee(80000)),
            ],
            [
                ("By Accumulated depreciation", rupee(30000)),
                ("By Bank (sale proceeds)", rupee(42000)),
                ("By Profit & Loss (loss)", rupee(8000)),
            ],
        )
        + p(
            f"Check the credits: {rupee(30000)} + {rupee(42000)} + {rupee(8000)} = {rupee(80000)}, which equals the debit. The account balances. Loss is {rupee(8000)}; investing inflow is {rupee(42000)}."
        )
        + h4("Working note 4 — Provision for Tax A/c")
        + p(
            f"Opening {rupee(40000)} + Current tax charge − Tax paid {rupee(45000)} = Closing {rupee(50000)}."
        )
        + p(
            f"Current tax charge = {rupee(50000)} − {rupee(40000)} + {rupee(45000)} = {rupee(10000)} + {rupee(45000)} = {rupee(55000)}."
        )
        + p(
            f"Check: {rupee(40000)} + {rupee(55000)} − {rupee(45000)} = {rupee(50000)}. Yes."
        )
        + t_account(
            "Provision for Tax A/c",
            [
                ("To Bank (tax paid)", rupee(45000)),
            ],
            [
                ("By Balance b/d", rupee(40000)),
                ("By Profit & Loss (current tax)", rupee(55000)),
            ],
            dr_bal=rupee(50000),
        )
        + h4("Working note 5 — Dividend and profit before tax")
        + p(
            f"Increase in P&L surplus = {rupee(210000)} − {rupee(140000)} = {rupee(70000)}."
        )
        + p(
            f"Dividend paid (given) {rupee(40000)} was appropriated out of profit, so "
            f"PAT = {rupee(70000)} + {rupee(40000)} = {rupee(110000)}."
        )
        + p(
            f"PBT = PAT + current tax = {rupee(110000)} + {rupee(55000)} = {rupee(165000)}."
        )
        + p(
            f"This PBT already includes: depreciation {rupee(60000)} (charged), loss on sale "
            f"{rupee(8000)} (charged), interest expense {rupee(20000)} (charged), interest "
            f"income {rupee(6400)} (credited). All four will be adjusted."
        )
        + h4("Working note 6 — Interest")
        + p(
            f"Interest paid (financing outflow) = {rupee(200000)} × 10/100 = {rupee(20000)}. "
            "Add the same {rupee(20000)} back in operating."
        )
        + p(
            f"Interest received (investing inflow) = {rupee(80000)} × 8/100 = {rupee(6400)}. "
            f"Deduct {rupee(6400)} in operating."
        )
        + h4("Working note 7 — Share capital, debentures, investments, working capital")
        + ul(
            [
                f"Shares issued for cash = {rupee(500000)} − {rupee(400000)} = {rupee(100000)}.",
                f"Debentures redeemed for cash = {rupee(200000)} − {rupee(150000)} = {rupee(50000)}.",
                f"Investments purchased for cash = {rupee(120000)} − {rupee(80000)} = {rupee(40000)}.",
                f"Inventory decreased = {rupee(150000)} − {rupee(135000)} = {rupee(15000)} (add).",
                f"Debtors increased = {rupee(125000)} − {rupee(100000)} = {rupee(25000)} (deduct).",
                f"Prepaid decreased = {rupee(15000)} − {rupee(10000)} = {rupee(5000)} (add).",
                f"Creditors increased = {rupee(110000)} − {rupee(90000)} = {rupee(20000)} (add).",
                f"Outstanding expenses decreased = {rupee(12000)} − {rupee(8000)} = {rupee(4000)} (deduct).",
            ]
        )
        + h4("Build operating profit before working capital changes")
        + p(f"PBT {rupee(165000)}")
        + p(f"+ Depreciation {rupee(60000)} → {rupee(165000)} + {rupee(60000)} = {rupee(225000)}")
        + p(f"+ Loss on sale {rupee(8000)} → {rupee(225000)} + {rupee(8000)} = {rupee(233000)}")
        + p(f"+ Interest expense {rupee(20000)} → {rupee(233000)} + {rupee(20000)} = {rupee(253000)}")
        + p(f"− Interest income {rupee(6400)} → {rupee(253000)} − {rupee(6400)} = {rupee(246600)}")
        + h4("Working capital, cash generated, tax, (A)")
        + p(f"{rupee(246600)} + decrease in inventory {rupee(15000)} = {rupee(261600)}")
        + p(f"{rupee(261600)} − increase in debtors {rupee(25000)} = {rupee(236600)}")
        + p(f"{rupee(236600)} + decrease in prepaid {rupee(5000)} = {rupee(241600)}")
        + p(f"{rupee(241600)} + increase in creditors {rupee(20000)} = {rupee(261600)}")
        + p(f"{rupee(261600)} − decrease in outstanding {rupee(4000)} = {rupee(257600)} cash generated from operations")
        + p(f"− Tax paid {rupee(45000)} → Net cash from operating activities (A) = {rupee(257600)} − {rupee(45000)} = {rupee(212600)}")
        + h4("Investing (B)")
        + p(f"Purchase of plant {rupee(200000)} (outflow)")
        + p(f"Sale proceeds of plant {rupee(42000)} (inflow)")
        + p(f"Purchase of investments {rupee(40000)} (outflow)")
        + p(f"Interest received {rupee(6400)} (inflow)")
        + p(
            f"B = −{rupee(200000)} + {rupee(42000)} − {rupee(40000)} + {rupee(6400)}"
        )
        + p(f"−{rupee(200000)} + {rupee(42000)} = −{rupee(158000)}")
        + p(f"−{rupee(158000)} − {rupee(40000)} = −{rupee(198000)}")
        + p(f"−{rupee(198000)} + {rupee(6400)} = −{rupee(191600)}")
        + h4("Financing (C)")
        + p(f"Issue of shares {rupee(100000)} (inflow)")
        + p(f"Redemption of debentures {rupee(50000)} (outflow)")
        + p(f"Interest paid {rupee(20000)} (outflow)")
        + p(f"Dividend paid {rupee(40000)} (outflow)")
        + p(
            f"C = {rupee(100000)} − {rupee(50000)} − {rupee(20000)} − {rupee(40000)}"
        )
        + p(f"{rupee(100000)} − {rupee(50000)} = {rupee(50000)}")
        + p(f"{rupee(50000)} − {rupee(20000)} = {rupee(30000)}")
        + p(f"{rupee(30000)} − {rupee(40000)} = −{rupee(10000)}")
        + h4("Net change")
        + p(
            f"A + B + C = {rupee(212600)} + ({rupee(191600)}) + ({rupee(10000)})"
        )
        + p(f"{rupee(212600)} − {rupee(191600)} = {rupee(21000)}")
        + p(f"{rupee(21000)} − {rupee(10000)} = {rupee(11000)} net increase in cash")
        + p(
            f"Opening cash {rupee(57000)} + {rupee(11000)} = {rupee(68000)} closing cash — matches the Balance Sheet. The statement is complete and internally true."
        )
        + table(
            ["Particulars", "₹"],
            [
                ["<strong>Cash flows from operating activities</strong>", ""],
                ["Net profit before tax", _in(165000)],
                ["Adjustments for:", ""],
                ["&nbsp;&nbsp;Depreciation", _in(60000)],
                ["&nbsp;&nbsp;Loss on sale of plant", _in(8000)],
                ["&nbsp;&nbsp;Interest expense", _in(20000)],
                ["&nbsp;&nbsp;Interest income", _out(6400)],
                ["Operating profit before working capital changes", _in(246600)],
                ["&nbsp;&nbsp;Decrease in inventory", _in(15000)],
                ["&nbsp;&nbsp;Increase in debtors", _out(25000)],
                ["&nbsp;&nbsp;Decrease in prepaid expenses", _in(5000)],
                ["&nbsp;&nbsp;Increase in creditors", _in(20000)],
                ["&nbsp;&nbsp;Decrease in outstanding expenses", _out(4000)],
                ["Cash generated from operations", _in(257600)],
                ["Income tax paid", _out(45000)],
                ["<strong>Net cash from operating activities (A)</strong>", f"<strong>{_in(212600)}</strong>"],
                ["<strong>Cash flows from investing activities</strong>", ""],
                ["Purchase of plant", _out(200000)],
                ["Sale proceeds of plant", _in(42000)],
                ["Purchase of investments", _out(40000)],
                ["Interest received", _in(6400)],
                ["<strong>Net cash from investing activities (B)</strong>", f"<strong>{_out(191600)}</strong>"],
                ["<strong>Cash flows from financing activities</strong>", ""],
                ["Proceeds from issue of equity shares", _in(100000)],
                ["Redemption of 10% debentures", _out(50000)],
                ["Interest paid", _out(20000)],
                ["Dividend paid", _out(40000)],
                ["<strong>Net cash from financing activities (C)</strong>", f"<strong>{_out(10000)}</strong>"],
                ["<strong>Net increase in cash and cash equivalents (A + B + C)</strong>", f"<strong>{_in(11000)}</strong>"],
                ["Opening cash and cash equivalents", _in(57000)],
                ["<strong>Closing cash and cash equivalents</strong>", f"<strong>{_in(68000)}</strong>"],
            ],
            caption="Kaveri Appliances Ltd. — Cash Flow Statement for the year ended 31 March 2026 (indirect method, AS-3)",
            foot="Proof: 2,12,600 − 1,91,600 − 10,000 = 11,000 = 68,000 − 57,000. Plant, accum. dep., tax and P&L T-accounts all balance. Interest received 80,000 × 8/100 = 6,400; interest paid 2,00,000 × 10/100 = 20,000.",
        )
    )
    parts.append(
        example(
            "5.3",
            "Exam-level",
            "Kaveri Appliances Ltd. — full two-year BS, sale of plant at a loss, redemption, interest received and paid",
            exam_q + exam_a,
        )
    )

    # ------------------------------------------------------------------
    # 11. Identify / mistakes / memory
    # ------------------------------------------------------------------
    parts.append(h2("How to identify the question, the mistakes that cost marks, and what to remember", "exam-craft"))
    parts.append(
        identify(
            "You are in this chapter when the question says any of: "
            "<em>“Prepare a Cash Flow Statement”</em>, "
            "<em>“Cash Flow Statement as per AS-3”</em>, "
            "<em>“indirect method”</em>, "
            "<em>“from the following Balance Sheets prepare a CFS”</em>, "
            "<em>“classify the following into operating, investing and financing”</em>, "
            "<em>“need / importance of Cash Flow Statement”</em>. "
            "Two-year Balance Sheets plus additional information about depreciation, "
            "sale of an asset, tax and dividend is the standard 15-mark practical. "
            "A short list of adjustments is the 8–10 mark practical. Theory on need, "
            "cash equivalents, or classification is 4–8 marks."
        )
    )
    parts.append(
        mistakes(
            [
                "<strong>Treating depreciation as a cash outflow.</strong> Depreciation never leaves the bank. It is added back. Writing it as an investing or operating payment is a full-mark loss on that line.",
                "<strong>Not deducting profit on sale (or not adding loss on sale) in operating.</strong> Then showing the full sale proceeds in investing double-counts the gain (or understates cash by the loss). Always pair: adjust the P&L result of the sale in operating, put <em>proceeds</em> in investing.",
                "<strong>Putting purchase of a fixed asset in operating</strong> because “we paid cash to run the business”. Buying the shop’s tools is investing, not operating.",
                "<strong>Treating a bonus issue as a financing inflow.</strong> Bonus is non-cash. Same error: conversion of debentures into shares, or an asset bought by issuing shares. Exclude from A, B and C; disclose in a note.",
                "<strong>Using the closing provision for tax as “tax paid”.</strong> Tax paid = opening provision + current charge − closing provision. The closing provision is what is still unpaid.",
                "<strong>Forgetting the interest pair.</strong> Add back interest expense in operating, then show interest paid in financing. Doing only one of the two drops (or double-counts) cash by that amount. Same pairing for interest/dividend income with investing.",
                "<strong>Calling “cash” only the notes in the till and forgetting cash at bank / cash equivalents.</strong> The last line must equal the BS figure for cash and cash equivalents.",
                "<strong>Squeezing provision for tax or proposed dividend through working capital</strong> as if they were creditors. They have their own cash lines (tax paid, dividend paid). Putting them in both places is a double count.",
                "<strong>Using book value as the sale proceeds.</strong> Proceeds = WDV + profit − loss. Investing inflow is proceeds.",
                "<strong>Taking the movement in plant at cost as the purchase, ignoring a sale.</strong> Purchases = closing cost − opening cost + cost of assets sold. Ignoring the sale understates purchases and therefore understates the investing outflow.",
                "<strong>Mixing gross debtors with a separate provision, and also adding the provision charge back.</strong> Pick net debtors as per BS and stop. Do not also add back the provision.",
                "<strong>Plugging the difference</strong> so that closing cash magically appears. If A+B+C does not equal the change in cash, a working is wrong. Find it.",
            ]
        )
    )
    parts.append(
        memory(
            "Operations = running the shop; Investing = buying and selling the shop’s "
            "tools; Financing = talking to owners and lenders. "
            "Then the three repairs of the indirect method: "
            "<strong>add back non-cash, undo non-operating, squeeze working capital.</strong> "
            "CA up → cash down. CL up → cash up. "
            "Last line is a lock: A + B + C + opening cash = closing cash. "
            "AS-3 interest/dividend rhyme: <em>received → investing; paid → financing.</em>"
        )
    )

    # ------------------------------------------------------------------
    # 12. Practice
    # ------------------------------------------------------------------
    parts.append(h2("Practice — two full questions, with solutions", "practice"))
    parts.append(
        p(
            "Attempt each question on paper first. Prepare working notes. Do not look "
            "at the solution until A + B + C equals the change in cash — or until you "
            "are stuck. The solutions show every multiplication."
        )
    )

    p1_q = (
        p(
            "<strong>Hari Tools</strong> extracted the following from its accounts for "
            "the year ended 31 March 2026. Prepare a Cash Flow Statement by the "
            "indirect method as per AS-3. Find the closing cash."
        )
        + ul(
            [
                f"Net profit before tax {rupee(200000)} (this figure is after interest expense, after interest income, after depreciation, and after profit on sale of furniture).",
                f"Depreciation {rupee(35000)}.",
                f"Profit on sale of furniture {rupee(5000)}.",
                f"Interest expense (included in P&L) {rupee(12000)}.",
                f"Interest income (included in P&L) {rupee(4000)}.",
                f"Increase in debtors {rupee(18000)}.",
                f"Decrease in stock {rupee(10000)}.",
                f"Increase in creditors {rupee(7000)}.",
                f"Decrease in outstanding expenses {rupee(3000)}.",
                f"Tax paid {rupee(40000)}.",
                f"Purchase of machinery {rupee(90000)}.",
                f"Sale of furniture (proceeds) {rupee(25000)}.",
                f"Purchase of investments {rupee(20000)}.",
                f"Dividend paid {rupee(30000)}.",
                f"Loan raised {rupee(50000)}.",
                f"Opening cash and cash equivalents {rupee(22000)}.",
            ]
        )
    )
    p1_a = (
        p(
            f"Operating profit before WC = {rupee(200000)} + dep {rupee(35000)} − profit on sale "
            f"{rupee(5000)} + interest expense {rupee(12000)} − interest income {rupee(4000)}."
        )
        + p(f"{rupee(200000)} + {rupee(35000)} = {rupee(235000)}")
        + p(f"{rupee(235000)} − {rupee(5000)} = {rupee(230000)}")
        + p(f"{rupee(230000)} + {rupee(12000)} = {rupee(242000)}")
        + p(f"{rupee(242000)} − {rupee(4000)} = {rupee(238000)}")
        + p(
            f"Working capital: − increase in debtors {rupee(18000)} + decrease in stock {rupee(10000)} "
            f"+ increase in creditors {rupee(7000)} − decrease in outstanding {rupee(3000)}."
        )
        + p(f"WC net = −{rupee(18000)} + {rupee(10000)} = −{rupee(8000)}; −{rupee(8000)} + {rupee(7000)} = −{rupee(1000)}; −{rupee(1000)} − {rupee(3000)} = −{rupee(4000)}.")
        + p(f"Cash generated = {rupee(238000)} − {rupee(4000)} = {rupee(234000)}.")
        + p(f"Net operating (A) = {rupee(234000)} − tax {rupee(40000)} = {rupee(194000)}.")
        + p(
            f"Investing (B) = − machinery {rupee(90000)} + furniture proceeds {rupee(25000)} − investments "
            f"{rupee(20000)} + interest received {rupee(4000)}."
        )
        + p(f"−{rupee(90000)} + {rupee(25000)} = −{rupee(65000)}; −{rupee(65000)} − {rupee(20000)} = −{rupee(85000)}; −{rupee(85000)} + {rupee(4000)} = −{rupee(81000)}.")
        + p(
            f"Financing (C) = loan {rupee(50000)} − interest paid {rupee(12000)} − dividend {rupee(30000)}."
        )
        + p(f"{rupee(50000)} − {rupee(12000)} = {rupee(38000)}; {rupee(38000)} − {rupee(30000)} = {rupee(8000)}.")
        + p(
            f"A + B + C = {rupee(194000)} − {rupee(81000)} + {rupee(8000)} = {rupee(113000)} + {rupee(8000)} = {rupee(121000)}."
        )
        + p(
            f"Closing cash = {rupee(22000)} + {rupee(121000)} = {rupee(143000)}."
        )
        + table(
            ["Particulars", "₹"],
            [
                ["Net profit before tax", _in(200000)],
                ["+ Depreciation", _in(35000)],
                ["− Profit on sale of furniture", _out(5000)],
                ["+ Interest expense", _in(12000)],
                ["− Interest income", _out(4000)],
                ["Operating profit before working capital changes", _in(238000)],
                ["− Increase in debtors", _out(18000)],
                ["+ Decrease in stock", _in(10000)],
                ["+ Increase in creditors", _in(7000)],
                ["− Decrease in outstanding expenses", _out(3000)],
                ["Cash generated from operations", _in(234000)],
                ["− Income tax paid", _out(40000)],
                ["<strong>Net cash from operating activities (A)</strong>", f"<strong>{_in(194000)}</strong>"],
                ["Purchase of machinery", _out(90000)],
                ["Sale proceeds of furniture", _in(25000)],
                ["Purchase of investments", _out(20000)],
                ["Interest received", _in(4000)],
                ["<strong>Net cash from investing activities (B)</strong>", f"<strong>{_out(81000)}</strong>"],
                ["Loan raised", _in(50000)],
                ["Interest paid", _out(12000)],
                ["Dividend paid", _out(30000)],
                ["<strong>Net cash from financing activities (C)</strong>", f"<strong>{_in(8000)}</strong>"],
                ["<strong>Net increase in cash (A + B + C)</strong>", f"<strong>{_in(121000)}</strong>"],
                ["Opening cash and cash equivalents", _in(22000)],
                ["<strong>Closing cash and cash equivalents</strong>", f"<strong>{_in(143000)}</strong>"],
            ],
            caption="Hari Tools — Cash Flow Statement (indirect method, AS-3)",
            foot="Proof: 1,94,000 − 81,000 + 8,000 = 1,21,000 = 1,43,000 − 22,000.",
        )
    )
    parts.append(
        practice(
            "5.1",
            "Easy–Moderate",
            "Hari Tools — full CFS from a list, including the interest pair",
            p1_q,
            p1_a,
        )
    )

    p2_q = (
        p(
            "<strong>Arjun Textiles Ltd.</strong> From the following summarised Balance "
            "Sheets and additional information, prepare a Cash Flow Statement (indirect "
            "method, AS-3) for the year ended 31 March 2026, with working notes."
        )
        + table(
            ["Particulars", "31 March 2025 ₹", "31 March 2026 ₹"],
            [
                ["<strong>Equity and liabilities</strong>", "", ""],
                ["Equity share capital", _in(300000), _in(400000)],
                ["12% Debentures", _in(150000), _in(100000)],
                ["Profit & Loss surplus", _in(90000), _in(130000)],
                ["General reserve", _in(40000), _in(55000)],
                ["Trade creditors", _in(50000), _in(42000)],
                ["Outstanding expenses", _in(8000), _in(11000)],
                ["Provision for tax", _in(25000), _in(30000)],
                ["<strong>Total</strong>", f"<strong>{_in(663000)}</strong>", f"<strong>{_in(768000)}</strong>"],
                ["<strong>Assets</strong>", "", ""],
                ["Land and building (not depreciated; no movement)", _in(200000), _in(200000)],
                ["Plant at cost", _in(350000), _in(450000)],
                ["Less: Accumulated depreciation on plant", _out(70000), _out(95000)],
                ["Plant (net)", _in(280000), _in(355000)],
                ["Inventory", _in(85000), _in(100000)],
                ["Trade debtors", _in(60000), _in(48000)],
                ["Prepaid expenses", _in(6000), _in(9000)],
                ["Cash and cash equivalents", _in(32000), _in(56000)],
                ["<strong>Total</strong>", f"<strong>{_in(663000)}</strong>", f"<strong>{_in(768000)}</strong>"],
            ],
            caption="Arjun Textiles Ltd. — summarised Balance Sheets",
        )
        + p("<strong>Additional information</strong>")
        + ol(
            [
                f"Plant costing {rupee(50000)} (accumulated depreciation {rupee(20000)}) was sold for {rupee(22000)}.",
                "The rest of the increase in plant at cost is a cash purchase.",
                f"Debentures of {rupee(50000)} were redeemed at par at the end of the year.",
                f"Equity shares of {rupee(100000)} were issued at par for cash. No bonus, no conversion.",
                f"Transfer to general reserve {rupee(15000)}.",
                f"Tax paid {rupee(32000)}.",
                f"Dividend paid {rupee(25000)}.",
                f"Interest on 12% debentures paid {rupee(18000)} "
                f"(= {rupee(150000)} × 12/100 = {rupee(18000)}).",
            ]
        )
    )
    p2_a = (
        h4("Workings")
        + p(
            f"<strong>Plant purchases:</strong> {rupee(450000)} − {rupee(350000)} + cost sold {rupee(50000)} = "
            f"{rupee(100000)} + {rupee(50000)} = {rupee(150000)}."
        )
        + p(
            f"<strong>Depreciation for the year:</strong> closing accum. {rupee(95000)} − opening {rupee(70000)} + on sold {rupee(20000)} = "
            f"{rupee(25000)} + {rupee(20000)} = {rupee(45000)}."
        )
        + p(
            f"<strong>Book value of plant sold:</strong> {rupee(50000)} − {rupee(20000)} = {rupee(30000)}. "
            f"Sold for {rupee(22000)}. <strong>Loss on sale</strong> = {rupee(30000)} − {rupee(22000)} = {rupee(8000)}."
        )
        + p(
            f"<strong>Current tax charge:</strong> closing provision {rupee(30000)} − opening {rupee(25000)} + tax paid {rupee(32000)} = "
            f"{rupee(5000)} + {rupee(32000)} = {rupee(37000)}. "
            f"Check: {rupee(25000)} + {rupee(37000)} − {rupee(32000)} = {rupee(30000)}."
        )
        + p(
            f"<strong>PAT:</strong> increase in P&L {rupee(130000)} − {rupee(90000)} = {rupee(40000)}, "
            f"plus transfer to general reserve {rupee(15000)}, plus dividend {rupee(25000)} → "
            f"PAT = {rupee(40000)} + {rupee(15000)} + {rupee(25000)} = {rupee(80000)}."
        )
        + p(
            f"<strong>PBT</strong> = PAT {rupee(80000)} + current tax {rupee(37000)} = {rupee(117000)}."
        )
        + p(
            f"Check on general reserve: {rupee(40000)} + {rupee(15000)} = {rupee(55000)}, matches the BS. "
            "Transfer to reserve is an appropriation — it is used only to reconstruct PAT. It is not an operating adjustment and not a cash flow."
        )
        + p(
            f"<strong>Interest paid</strong> = {rupee(150000)} × 12/100 = {rupee(18000)} (add back the same amount in operating)."
        )
        + h4("Operating")
        + p(
            f"PBT {rupee(117000)} + dep {rupee(45000)} + loss on sale {rupee(8000)} + interest {rupee(18000)} = "
            f"operating profit before WC."
        )
        + p(f"{rupee(117000)} + {rupee(45000)} = {rupee(162000)}")
        + p(f"{rupee(162000)} + {rupee(8000)} = {rupee(170000)}")
        + p(f"{rupee(170000)} + {rupee(18000)} = {rupee(188000)}")
        + p(
            f"WC: inventory increase {rupee(100000)} − {rupee(85000)} = {rupee(15000)} (deduct); "
            f"debtors decrease {rupee(60000)} − {rupee(48000)} = {rupee(12000)} (add); "
            f"prepaid increase {rupee(9000)} − {rupee(6000)} = {rupee(3000)} (deduct); "
            f"creditors decrease {rupee(50000)} − {rupee(42000)} = {rupee(8000)} (deduct); "
            f"outstanding increase {rupee(11000)} − {rupee(8000)} = {rupee(3000)} (add)."
        )
        + p(
            f"WC net = −{rupee(15000)} + {rupee(12000)} − {rupee(3000)} − {rupee(8000)} + {rupee(3000)} = −{rupee(11000)}."
        )
        + p(f"Cash generated = {rupee(188000)} − {rupee(11000)} = {rupee(177000)}.")
        + p(f"Net operating (A) = {rupee(177000)} − tax {rupee(32000)} = {rupee(145000)}.")
        + h4("Investing and financing")
        + p(
            f"Investing (B) = − plant purchased {rupee(150000)} + sale proceeds {rupee(22000)} = −{rupee(128000)}. "
            "(Land and building did not move; no investing item there.)"
        )
        + p(
            f"Financing (C) = share issue {rupee(100000)} − redemption {rupee(50000)} − interest {rupee(18000)} − dividend {rupee(25000)}."
        )
        + p(f"{rupee(100000)} − {rupee(50000)} = {rupee(50000)}; {rupee(50000)} − {rupee(18000)} = {rupee(32000)}; {rupee(32000)} − {rupee(25000)} = {rupee(7000)}.")
        + p(
            f"A + B + C = {rupee(145000)} − {rupee(128000)} + {rupee(7000)} = {rupee(17000)} + {rupee(7000)} = {rupee(24000)}."
        )
        + p(
            f"Opening cash {rupee(32000)} + {rupee(24000)} = {rupee(56000)} closing cash, matching the Balance Sheet."
        )
        + table(
            ["Particulars", "₹"],
            [
                ["Net profit before tax", _in(117000)],
                ["+ Depreciation", _in(45000)],
                ["+ Loss on sale of plant", _in(8000)],
                ["+ Interest expense", _in(18000)],
                ["Operating profit before working capital changes", _in(188000)],
                ["− Increase in inventory", _out(15000)],
                ["+ Decrease in debtors", _in(12000)],
                ["− Increase in prepaid expenses", _out(3000)],
                ["− Decrease in creditors", _out(8000)],
                ["+ Increase in outstanding expenses", _in(3000)],
                ["Cash generated from operations", _in(177000)],
                ["− Income tax paid", _out(32000)],
                ["<strong>Net cash from operating activities (A)</strong>", f"<strong>{_in(145000)}</strong>"],
                ["Purchase of plant", _out(150000)],
                ["Sale proceeds of plant", _in(22000)],
                ["<strong>Net cash from investing activities (B)</strong>", f"<strong>{_out(128000)}</strong>"],
                ["Proceeds from issue of equity shares", _in(100000)],
                ["Redemption of 12% debentures", _out(50000)],
                ["Interest paid", _out(18000)],
                ["Dividend paid", _out(25000)],
                ["<strong>Net cash from financing activities (C)</strong>", f"<strong>{_in(7000)}</strong>"],
                ["<strong>Net increase in cash (A + B + C)</strong>", f"<strong>{_in(24000)}</strong>"],
                ["Opening cash and cash equivalents", _in(32000)],
                ["<strong>Closing cash and cash equivalents</strong>", f"<strong>{_in(56000)}</strong>"],
            ],
            caption="Arjun Textiles Ltd. — Cash Flow Statement for the year ended 31 March 2026 (indirect method, AS-3)",
            foot="Proof: 1,45,000 − 1,28,000 + 7,000 = 24,000 = 56,000 − 32,000. Transfer to general reserve is not a cash flow.",
        )
        + t_account(
            "Plant A/c (at cost)",
            [
                ("To Balance b/d", rupee(350000)),
                ("To Bank (purchases)", rupee(150000)),
            ],
            [
                ("By Asset sold (cost)", rupee(50000)),
            ],
            cr_bal=rupee(450000),
        )
        + t_account(
            "Accumulated Depreciation A/c",
            [
                ("To Asset sold", rupee(20000)),
            ],
            [
                ("By Balance b/d", rupee(70000)),
                ("By Profit & Loss (dep.)", rupee(45000)),
            ],
            dr_bal=rupee(95000),
        )
        + t_account(
            "Provision for Tax A/c",
            [
                ("To Bank (tax paid)", rupee(32000)),
            ],
            [
                ("By Balance b/d", rupee(25000)),
                ("By Profit & Loss (current tax)", rupee(37000)),
            ],
            dr_bal=rupee(30000),
        )
    )
    parts.append(
        practice(
            "5.2",
            "Exam-level",
            "Arjun Textiles Ltd. — two-year BS with general reserve, sale of plant at a loss, redemption",
            p2_q,
            p2_a,
        )
    )

    # ------------------------------------------------------------------
    # 13. Theory Q&A (exam-ready, not a "summary")
    # ------------------------------------------------------------------
    parts.append(h2("Theory questions the examiner actually sets", "theory-qna"))
    parts.append(
        p(
            "Practical questions are the bulk of the marks. These theory questions "
            "still appear, usually for 4–8 marks. Answer in the shape the examiner "
            "rewards: definition, then three or four sharp points, then the standard "
            "tag (AS-3 / Companies Act) if it is relevant."
        )
    )
    parts.append(
        qna(
            "Why is profit not equal to cash? Illustrate.",
            "<p>Profit is computed on the accrual basis. Revenue is recognised when "
            "earned and expenses when incurred, whether or not cash has moved. Cash "
            "is recognised only when it is received or paid. Therefore:</p>"
            "<ul>"
            "<li>Credit sales increase profit but not cash until collected.</li>"
            "<li>Depreciation decreases profit but not cash.</li>"
            "<li>Purchase of a machine decreases cash but not profit (except later, through depreciation).</li>"
            "<li>A loan increases cash but not profit.</li>"
            "</ul>"
            f"<p>Illustration: Meera’s profit {rupee(100000)} against a cash increase of "
            f"only {rupee(55000)} in the opening example of this chapter — the gap is "
            "exactly these four kinds of item.</p>",
            "6 marks",
        )
    )
    parts.append(
        qna(
            "State the importance of a Cash Flow Statement.",
            "<p>A CFS reports inflows and outflows of cash and cash equivalents, classified "
            "into operating, investing and financing activities (AS-3 / Ind AS-7). It is "
            "important because:</p>"
            "<ul>"
            "<li>It reveals liquidity — the ability to pay creditors, lenders, employees and tax — which profit conceals.</li>"
            "<li>Management uses it to plan working capital, capex and dividends.</li>"
            "<li>Lenders use it to judge whether debt can be serviced from operations.</li>"
            "<li>Investors use it to test the quality of earnings (is profit turning into cash?).</li>"
            "<li>It complements the P&L and the Balance Sheet by reconciling opening and closing cash.</li>"
            "<li>It is mandatory for listed companies and for companies other than OPC, small companies and dormant companies.</li>"
            "</ul>",
            "8 marks",
        )
    )
    parts.append(
        qna(
            "What are cash and cash equivalents? Is a bank overdraft a cash equivalent?",
            "<p>Cash = cash on hand + demand deposits with banks. Cash equivalents = "
            "short-term, highly liquid investments readily convertible into known amounts "
            "of cash and subject to an insignificant risk of changes in value, normally "
            "with a maturity of three months or less from the date of acquisition. Equity "
            "shares are not cash equivalents.</p>"
            "<p>Bank overdraft repayable on demand may be treated as a component of cash "
            "and cash equivalents under AS-3 if it is an integral part of cash management. "
            "Many examination problems instead treat the movement in overdraft as a "
            "financing inflow or outflow. Follow the question.</p>",
            "5 marks",
        )
    )
    parts.append(
        qna(
            "Distinguish operating, investing and financing activities, with two examples of each. How are interest and dividend classified under AS-3?",
            "<p><strong>Operating</strong> — principal revenue-producing activities: cash from customers, cash to suppliers, wages, income tax paid.</p>"
            "<p><strong>Investing</strong> — acquisition and disposal of long-term assets and of investments other than cash equivalents: purchase/sale of plant, purchase/sale of investments.</p>"
            "<p><strong>Financing</strong> — changes in owners’ capital and borrowings: issue of shares, loans taken, redemption of debentures, repayment of loans.</p>"
            "<p><strong>AS-3 classification of interest and dividend:</strong> interest received and dividend received = investing inflows; interest paid and dividend paid = financing outflows. (Ind AS-7 permits options; unless named, use AS-3.)</p>",
            "8 marks",
        )
    )
    parts.append(
        qna(
            "Give the pro-forma of a Cash Flow Statement under the indirect method.",
            "<p>Write the boxed format taught in this chapter, in this order: net profit "
            "before tax; adjustments for depreciation, profit/loss on sale, interest, "
            "non-cash items; operating profit before working capital changes; changes in "
            "current assets and current liabilities; cash generated from operations; tax "
            "paid; net operating (A); investing receipts and payments (B); financing "
            "receipts and payments (C); A+B+C; opening cash; closing cash. Closing cash "
            "must equal the Balance Sheet.</p>",
            "8 marks",
        )
    )
    parts.append(
        qna(
            "How will you treat the following in a Cash Flow Statement (indirect method, AS-3): depreciation; profit on sale of machine; bonus issue; increase in debtors; proposed dividend; purchase of machinery by issue of shares?",
            "<ul>"
            "<li><strong>Depreciation</strong> — add back to profit (operating adjustment; non-cash).</li>"
            "<li><strong>Profit on sale of machine</strong> — deduct from profit; show sale proceeds as investing inflow.</li>"
            "<li><strong>Bonus issue</strong> — non-cash; exclude from the CFS body; disclose in a note. If capitalised from P&L, add back when reconstructing PAT.</li>"
            "<li><strong>Increase in debtors</strong> — deduct in working-capital adjustments (operating).</li>"
            "<li><strong>Proposed dividend</strong> — not an operating item. Dividend <em>paid</em> is a financing outflow (usually equal to opening proposed dividend if that is the unpaid liability brought forward).</li>"
            "<li><strong>Purchase of machinery by issue of shares</strong> — non-cash investing and financing transaction; disclose in a note; no figure in A, B or C.</li>"
            "</ul>",
            "6 marks",
        )
    )

    parts.append(chapter_close())
    return "".join(parts)
