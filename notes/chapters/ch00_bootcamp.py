#!/usr/bin/env python3
"""Chapter 00 — Accounting Basics Bootcamp. Teach from absolute zero."""

from __future__ import annotations

import sys

sys.path.insert(0, "/workspace/notes")
from html_lib import *

# ---------------------------------------------------------------------------
# Running equation — Rahul Stationery.
# Columns: cash, bank, furniture, stock, debtors, prepaid, creditors, loan, capital
# Arithmetic (comments = paper working):
# T1  start cash 1,00,000 / capital 1,00,000
#     C 1,00,000  B 0  F 0  S 0  Dr 0  Pre 0 | Cr 0  Ln 0  Cap 1,00,000
#     A 1,00,000 = L 0 + C 1,00,000
# T2  furniture 20,000 cash: C 80,000 F 20,000  A still 1,00,000
# T3  deposit 40,000: C 40,000 B 40,000  A still 1,00,000
# T4  stock 30,000 credit Aman: S 30,000 Cr 30,000  A 1,30,000 = 30,000 + 1,00,000
# T5  sell cost 10,000 for 15,000 cash:
#     C 40,000+15,000=55,000  S 30,000-10,000=20,000  Cap 1,00,000+5,000=1,05,000
#     A 55k+40k+20k+20k=1,35,000 = 30,000 + 1,05,000
# T6  rent 5,000 cheque: B 40,000-5,000=35,000  Cap 1,05,000-5,000=1,00,000
#     A 55+35+20+20=1,30,000 = 30,000 + 1,00,000
# T7  commission 2,000 cash: C 55,000+2,000=57,000  Cap 1,00,000+2,000=1,02,000
#     A 57+35+20+20=1,32,000 = 30,000 + 1,02,000
# T8  drawings 4,000 cash: C 57,000-4,000=53,000  Cap 1,02,000-4,000=98,000
#     A 53+35+20+20=1,28,000 = 30,000 + 98,000
# T9  pay Aman 12,000 cheque: B 35,000-12,000=23,000  Cr 30,000-12,000=18,000
#     A 53+23+20+20=1,16,000 = 18,000 + 98,000
# T10 loan 50,000 to bank: B 23,000+50,000=73,000  Ln 50,000
#     A 53+73+20+20=1,66,000 = 18,000+50,000 + 98,000 = 1,66,000
# ---------------------------------------------------------------------------

# (label, cash, bank, furn, stock, debtors, prepaid, cred, loan, cap)
EQ = [
    ("T1", 100000, 0, 0, 0, 0, 0, 0, 0, 100000),
    ("T2", 80000, 0, 20000, 0, 0, 0, 0, 0, 100000),
    ("T3", 40000, 40000, 20000, 0, 0, 0, 0, 0, 100000),
    ("T4", 40000, 40000, 20000, 30000, 0, 0, 30000, 0, 100000),
    ("T5", 55000, 40000, 20000, 20000, 0, 0, 30000, 0, 105000),
    ("T6", 55000, 35000, 20000, 20000, 0, 0, 30000, 0, 100000),
    ("T7", 57000, 35000, 20000, 20000, 0, 0, 30000, 0, 102000),
    ("T8", 53000, 35000, 20000, 20000, 0, 0, 30000, 0, 98000),
    ("T9", 53000, 23000, 20000, 20000, 0, 0, 18000, 0, 98000),
    ("T10", 53000, 73000, 20000, 20000, 0, 0, 18000, 50000, 98000),
]

HDR_EQ = [
    "After",
    "Cash",
    "Bank",
    "Furniture",
    "Stock",
    "Debtors",
    "Prepaid",
    "Creditors",
    "Loan",
    "Capital",
    "Assets",
    "L + C",
]


def _assert_equation() -> None:
    for t in EQ:
        label, cash, bank, furn, stock, debtors, prepaid, cred, loan, cap = t
        assets = cash + bank + furn + stock + debtors + prepaid
        lc = cred + loan + cap
        if assets != lc:
            raise AssertionError(f"{label}: assets {assets} != L+C {lc}")
    t10 = EQ[-1]
    assert t10[1] + t10[2] + t10[3] + t10[4] == 166000
    assert t10[7] + t10[8] == 68000
    assert t10[9] == 98000


_assert_equation()


def eq_rows(n: int) -> list:
    rows = []
    for t in EQ[:n]:
        label, cash, bank, furn, stock, debtors, prepaid, cred, loan, cap = t
        assets = cash + bank + furn + stock + debtors + prepaid
        lc = cred + loan + cap
        rows.append(
            [
                label,
                rupee(cash),
                rupee(bank),
                rupee(furn),
                rupee(stock),
                rupee(debtors),
                rupee(prepaid),
                rupee(cred),
                rupee(loan),
                rupee(cap),
                b(rupee(assets)),
                b(rupee(lc)),
            ]
        )
    return rows


def running_eq(n: int, caption: str) -> str:
    return table(
        HDR_EQ,
        eq_rows(n),
        caption=caption,
        foot="Check every row: Assets = Liabilities + Capital. If the last two columns differ, a posting is wrong.",
    )


def snapshot(n: int) -> str:
    t = EQ[n - 1]
    label, cash, bank, furn, stock, debtors, prepaid, cred, loan, cap = t
    assets = cash + bank + furn + stock + debtors + prepaid
    liab = cred + loan
    left = table(
        ["Assets", "₹"],
        [
            ["Cash", rupee(cash)],
            ["Bank", rupee(bank)],
            ["Furniture", rupee(furn)],
            ["Stock", rupee(stock)],
            ["Debtors", rupee(debtors)],
            ["Prepaid", rupee(prepaid)],
            [b("Total assets"), b(rupee(assets))],
        ],
        caption=f"Assets after {label}",
    )
    right = table(
        ["Liabilities and capital", "₹"],
        [
            ["Creditors (Aman)", rupee(cred)],
            ["Bank loan", rupee(loan)],
            [b("Total liabilities"), b(rupee(liab))],
            ["Capital", rupee(cap)],
            [b("Liabilities + capital"), b(rupee(liab + cap))],
        ],
        caption=f"L + C after {label}",
    )
    check = keypoint(
        f"After {label}: Assets {rupee(assets)} = Liabilities {rupee(liab)} + Capital {rupee(cap)} "
        f"= {rupee(liab + cap)}. The two sides match."
    )
    return two_col(left, right) + check


def teach_txn(
    code: str,
    title: str,
    what: str,
    account_rows: list,
    journal_entries: list,
    effect: str,
    snap_n: int,
    extra: str = "",
) -> str:
    parts = [
        h3(f"{code} — {title}"),
        raw_p(b("What happened? "), what),
        table(
            ["Account", "Nature", "₹ change", "Increase or decrease", "Debit or credit"],
            account_rows,
            caption=f"{code}: which accounts moved",
        ),
        journal(journal_entries, caption=f"{code} — Journal"),
        logic(effect),
        extra,
        snapshot(snap_n),
        running_eq(snap_n, f"Running equation after {code}"),
    ]
    return "".join(parts)


def body() -> str:
    parts: list[str] = []
    parts.append(
        chapter_open(
            "00",
            "Accounting Basics Bootcamp",
            "After this bootcamp you will be able to read any transaction, name the accounts it touches, say what increased or decreased, and write the debit and credit.",
            [
                "What is accounting",
                "Why accounting is needed",
                "Business transactions",
                "Assets, Liabilities, Capital",
                "Revenue, Expenses, Profit, Loss, Drawings",
                "Accounting equation",
                "Debit and Credit",
                "Basic accounting rules",
                "How transactions affect accounts",
            ],
        )
    )
    parts.append(_intro())
    parts.append(_what_is_accounting())
    parts.append(_why_accounts())
    parts.append(_bookkeeping_vs_accounting())
    parts.append(_entity())
    parts.append(_transaction())
    parts.append(_five_elements())
    parts.append(_assets())
    parts.append(_liabilities())
    parts.append(_capital())
    parts.append(_revenue())
    parts.append(_expenses())
    parts.append(_profit_loss())
    parts.append(_drawings())
    parts.append(_equation())
    parts.append(_debit_credit())
    parts.append(_modern_rules())
    parts.append(_golden_rules())
    parts.append(_txn_journals())
    parts.append(_drill())
    parts.append(_memory_mistakes())
    parts.append(_exam())
    parts.append(_bridge())
    parts.append(chapter_close())
    return "".join(parts)


def _intro() -> str:
    return (
        lead(
            "Meet "
            + b("Rahul")
            + ". He is 24. He has saved "
            + rupee(100000)
            + " and he is opening a small stationery shop — pens, notebooks, files, copier paper — on a rented lane in Pune. He will call it "
            + b("Rahul Stationery")
            + ". He has never kept books. This bootcamp starts at zero and walks with him, rupee by rupee, until you can read any transaction the way an accountant reads it."
        )
        + p(
            "You do not need any earlier chapter. You do not need commerce at school. If you can add and subtract, you can do this. Every number is shown. Nothing is skipped."
        )
        + p(
            "By the last page you will: (1) name the accounts a transaction touches, (2) say whether each account increased or decreased, (3) place the amount on the debit or the credit, (4) write the journal line, and (5) prove that the accounting equation still balances."
        )
        + keypoint(
            "One shop. One owner. Ten transactions. Every idea in this bootcamp is hung on Rahul. When you later open a factory, a hospital, or a listed company, the same ten ideas still hold. Only the names of the accounts get longer."
        )
    )


def _what_is_accounting() -> str:
    return (
        h2("1. What is accounting?", "what-is-accounting")
        + definition(
            "Accounting is the process of <strong>identifying</strong>, <strong>measuring</strong>, "
            "<strong>recording</strong>, <strong>classifying</strong>, <strong>summarising</strong>, "
            "<strong>analysing</strong> and <strong>communicating</strong> money information about a business "
            "so that the owner and outsiders can take decisions."
        )
        + simple(
            "Accounting is the memory and the language of a business. It notices every rupee that comes in or goes out, "
            "writes it down under a proper name, totals it, and then tells a story: did we make a profit? what do we own? what do we owe?"
        )
        + why(
            "Without accounting Rahul will forget, mix his personal spending with the shop, not know whether a notebook is sold at a profit, "
            "and have nothing to show a bank or the tax officer. Accounting turns a pile of bills into a picture of the shop."
        )
        + real_life(
            "Rahul sells a pack of pens for "
            + rupee(150)
            + " cash. Accounting does not stop at “money came in”. It identifies that this is a sale, measures it at "
            + rupee(150)
            + ", records it in the cash book and the sales account, classifies it as income, summarises it with all other sales at month-end, "
            "analyses whether pens are a good line, and communicates the profit in a statement Rahul can read."
        )
        + logic(
            "Business events happen in the real world. Accounting translates them into a common unit — the rupee — and into a common structure — accounts. "
            "That translation is why a bank in Mumbai can read the books of a shop in Pune without visiting the counter."
        )
        + p(b("The seven steps, in the order they actually happen:"))
        + table(
            ["Step", "Name", "What Rahul does", "Tiny example"],
            [
                [
                    "1",
                    b("Identifying"),
                    "Spot the events that change the shop’s money or value. Ignore the rest.",
                    "A customer pays " + rupee(150) + " — identify. A customer window-shops — ignore.",
                ],
                [
                    "2",
                    b("Measuring"),
                    "Put a rupee figure on the event. Accounting records only what can be measured in money.",
                    "The pens sold are measured at " + rupee(150) + ", not as “a happy customer”.",
                ],
                [
                    "3",
                    b("Recording"),
                    "Write the event in the books on the date it happened, with evidence (bill, voucher, cheque).",
                    "Cash book: cash in " + rupee(150) + ". Sales book: sale " + rupee(150) + ".",
                ],
                [
                    "4",
                    b("Classifying"),
                    "Put each amount under the right account name so similar things sit together.",
                    rupee(150) + " is Sales, not Capital, not a loan.",
                ],
                [
                    "5",
                    b("Summarising"),
                    "Total the accounts and present short statements — profit, and a list of what is owned and owed.",
                    "Month sales " + rupee(80000) + ", expenses " + rupee(55000) + ", profit " + rupee(25000) + ".",
                ],
                [
                    "6",
                    b("Analysing"),
                    "Ask what the numbers mean. Compare, find the cause, spot the leak.",
                    "Rent is 20% of sales — too high for this lane? Stock of diaries is not moving.",
                ],
                [
                    "7",
                    b("Communicating"),
                    "Give the picture to the people who need it: Rahul, the bank, the tax officer, a partner.",
                    "A one-page profit statement and a one-page list of assets and liabilities.",
                ],
            ],
            caption="Accounting is a process, not a single entry",
        )
        + formula(
            "Accounting = Identify → Measure → Record → Classify → Summarise → Analyse → Communicate",
            "Skip a step and the picture is either incomplete or useless to the reader.",
        )
        + steps(
            [
                "Read the event. Did money or value of the business change? If no, stop — it is not accounting yet.",
                "Measure it in ₹. Use the bill, the invoice, the cheque, or the agreed price. Do not guess.",
                "Name the accounts. At least two names, because every event has two sides (you will see why under the equation).",
                "Write the record. Date, accounts, amounts, a one-line narration of what happened.",
                "Later, add similar records together (classify and summarise) and read the totals (analyse and communicate).",
            ],
            title="7. How to process one event (exam procedure)",
        )
        + example(
            "0.1",
            "Easy",
            "Which of these is accounting, and which is just a thought?",
            p("Rahul thinks, “I might buy a photocopy machine next year.” A supplier delivers the machine today for "
              + rupee(40000)
              + " cash and leaves a tax invoice.")
            + p(b("Answer. ")
              + "The thought is not accounting — no money moved, no evidence, nothing to measure. "
              "The delivery is accounting: identify (machine bought), measure ("
              + rupee(40000)
              + "), record (Cash down, Furniture/Machinery up), classify (asset), and later summarise it on the list of things the shop owns."),
        )
        + identify(
            "If the question says “define accounting” or “accounting is the process of…”, write the seven verbs in order: "
            "identifying, measuring, recording, classifying, summarising, analysing, communicating. Then add “in terms of money, to help users take decisions.”"
        )
        + mistakes(
            [
                "Writing only “recording of transactions”. That is bookkeeping, which is one part of accounting, not the whole.",
                "Forgetting measuring. If you cannot put a rupee figure, accounting does not record it (a loyal customer is valuable — but not in the books).",
                "Stopping at recording. The exam wants the full process, including analysis and communication.",
            ]
        )
        + memory(
            "I-M-R-C-S-A-C: I Measure, Record, Classify, Summarise, Analyse, Communicate. "
            "Say it as “I mark rupees clearly so anyone can count.”"
        )
        + exam_answer(
            "Accounting is the process of identifying, measuring, recording, classifying, summarising, analysing and communicating "
            "financial information of a business. Identification picks the events that change the resources of the firm. "
            "Measurement expresses those events in money. Recording writes them in the books with evidence. "
            "Classification groups them under account heads. Summarising presents totals as statements. "
            "Analysis interprets the statements. Communication reports the picture to owners, lenders, the tax authority and other users "
            "so that decisions can be taken. Accounting is therefore both a record and a language."
        )
    )


def _why_accounts() -> str:
    return (
        h2("2. Why do businesses keep accounts?", "why-accounts")
        + definition(
            "Businesses keep accounts so that they have a reliable memory of every rupee, can compute profit or loss, "
            "can pay the correct tax, can borrow from a bank, can control theft and waste, and can decide what to do next."
        )
        + simple(
            "Rahul cannot keep 400 bills in his head. Accounts are a notebook that never gets tired, never takes sides, and can be shown to other people."
        )
        + why(
            "The shop is not a hobby. Money is coming from Rahul’s savings, later from a bank, and the government wants its tax. "
            "Accounts are how Rahul proves what happened — to himself first, then to everyone else."
        )
        + real_life(
            "A bank manager asks Rahul, “What did you earn last year, and what do you own today?” If Rahul shrugs, there is no loan. "
            "If Rahul opens a set of books that add up, the manager has something to read."
        )
        + logic(
            "Every reason below is a different reader of the same books. The books do not change for each reader. "
            "The statements pulled from the books do."
        )
        + table(
            ["Need", "Question the books answer", "What goes wrong without books"],
            [
                [
                    b("Memory"),
                    "What happened on 12 June? Who still owes us? Whom do we still owe?",
                    "Rahul forgets that Aman is still to be paid " + rupee(18000) + ".",
                ],
                [
                    b("Profit"),
                    "Did the shop earn more than it spent? How much?",
                    "Busy counter, empty pocket — he sold below cost and never noticed.",
                ],
                [
                    b("Tax"),
                    "What is taxable income? What GST was collected and paid?",
                    "He pays too much, or too little and faces a notice.",
                ],
                [
                    b("Bank loan"),
                    "Is the shop able to repay? What security does it have?",
                    "The manager has no numbers. The file is closed.",
                ],
                [
                    b("Control"),
                    "Is cash matching the till? Is stock walking out the door?",
                    "An employee can pocket cash and there is no trail.",
                ],
                [
                    b("Decision"),
                    "Should we drop diaries and add art supplies? Is rent too high?",
                    "Decisions are made on a feeling, which is how shops quietly die.",
                ],
            ],
            caption="Six reasons — memory, profit, tax, bank loan, control, decision",
        )
        + example(
            "0.2",
            "Easy",
            "Name the reason",
            p("Rahul wants to know whether notebooks or greeting cards give him more leftover money after cost. Which reason is this?")
            + p(b("Answer. ") + "Decision (and profit). Accounts will show sales and cost of each line so he can keep the better one."),
        )
        + identify(
            "If the question is “why is accounting needed / objectives of accounting”, list these six: memory (record), profit (result), tax (statutory), "
            "bank loan (creditworthiness), control (stewardship), decision (management). One line of explanation under each."
        )
        + mistakes(
            [
                "Writing only “to know profit”. That is one reason, not the full answer.",
                "Mixing “control” with “tax”. Control is internal (cash, stock, people). Tax is a duty to the government.",
            ]
        )
        + memory(
            "MP-TB-CD: Memory, Profit, Tax, Bank-loan, Control, Decision. “My Profit To Bank Comes Daily.”"
        )
    )


def _bookkeeping_vs_accounting() -> str:
    return (
        h2("3. Bookkeeping versus accounting", "bookkeeping-vs-accounting")
        + definition(
            "<strong>Bookkeeping</strong> is the recording of transactions in the books, in a systematic way. "
            "<strong>Accounting</strong> is bookkeeping plus classifying, summarising, analysing and communicating — that is, recording plus interpreting."
        )
        + simple(
            "Bookkeeping is writing it down correctly. Accounting is writing it down and then reading what it means. "
            "Every accountant book-keeps. Not every bookkeeper accounts."
        )
        + why(
            "Exam papers love this pair. If you treat them as the same word you lose marks. "
            "In a small shop Rahul may do both. In a company a clerk book-keeps and a manager accounts."
        )
        + real_life(
            "Rahul’s cousin Neha writes every cash receipt and payment in a register. That is bookkeeping. "
            "At month-end Rahul takes Neha’s totals, computes profit, compares this month with last month, and decides to cut the greeting-card order. That is accounting."
        )
        + logic(
            "Recording is the foundation. Interpretation is the roof. You cannot interpret what was never recorded. "
            "You also cannot call a pile of recordings “accounts” until someone has totalled and read them."
        )
        + two_col(
            box(
                "simple",
                "Bookkeeping",
                ul(
                    [
                        "Identifying and recording transactions.",
                        "Journal, cash book, ledger postings.",
                        "Clerical, rule-based, day to day.",
                        "Output: a complete record.",
                        "Does not, by itself, explain profit or position.",
                    ]
                ),
            ),
            box(
                "simple",
                "Accounting",
                ul(
                    [
                        "Recording + classifying + summarising + analysing + communicating.",
                        "Trial balance, profit statement, balance sheet, ratios.",
                        "Includes bookkeeping, then goes further.",
                        "Output: statements plus meaning.",
                        "Answers “so what?” for owner, bank, tax.",
                    ]
                ),
            ),
        )
        + formula(
            "Accounting = Bookkeeping + Interpreting (summarising, analysing, communicating)",
            "Bookkeeping is necessary. It is not sufficient.",
        )
        + example(
            "0.3",
            "Moderate",
            "Is Neha an accountant?",
            p("Neha posts every bill to the correct page and her totals always match. She never prepares a profit figure and never comments on the numbers. Is she doing accounting?")
            + p(b("Answer. ")
              + "She is doing bookkeeping. Accounting begins when those records are summarised into profit and position and then analysed. "
              "If Rahul takes her ledger and prepares a profit statement, that extra work is accounting."),
        )
        + identify(
            "If the question says “distinguish between bookkeeping and accounting”, draw a two-column table: meaning, scope, level of work, output, who does it. "
            "End with the line: bookkeeping is a part of accounting."
        )
        + mistakes(
            [
                "Saying accounting is “only interpretation” — it includes recording.",
                "Saying bookkeeping is useless. Without it, accounting has nothing to interpret.",
            ]
        )
        + memory(
            "Bookkeeping = the book. Accounting = the book + the story of the book."
        )
    )


def _entity() -> str:
    return (
        h2("4. The business is not the owner", "business-entity")
        + definition(
            "The <strong>business entity concept</strong> says that the business is treated as a person separate from its owner. "
            "The books of Rahul Stationery record the shop, not Rahul’s private life."
        )
        + simple(
            "Imagine the shop is a box. Rahul can put money into the box and take money out of the box, but the box has its own list of belongings and debts. "
            "We never mix the box with Rahul’s rent for his flat, his dinner, or his bike."
        )
        + why(
            "If we mix them, profit becomes a lie. Paying for a movie ticket from the till would look like a shop expense and would hide the true profit of selling pens."
        )
        + real_life(
            "Rahul takes a notebook from the shelf for his sister’s homework. In his head “it is my shop, my notebook”. In the books it is "
            + b("drawings")
            + " — the owner took goods — not an expense of selling stationery to customers."
        )
        + logic(
            "Capital is the amount the owner has put into the box. Drawings are the amount the owner has taken out of the box. "
            "Both exist only because the box and the owner are recorded as two parties talking to each other."
        )
        + keypoint(
            "Business ≠ owner. The shop can owe the owner (capital). The owner can owe the shop (if he takes goods without recording drawings — which we will not allow). "
            "Every personal withdrawal is drawings. Every personal bill paid from the till is drawings, not rent, not salary, not “miscellaneous”."
        )
        + example(
            "0.4",
            "Easy",
            "Whose electricity?",
            p("Rahul pays " + rupee(800) + " for the shop’s electricity and " + rupee(1200) + " for his home electricity, both from the shop’s cash box.")
            + p(b("Answer. ")
              + rupee(800)
              + " is an expense of the business (electricity). "
              + rupee(1200)
              + " is drawings — the owner took cash for a personal bill. Recording the "
              + rupee(1200)
              + " as electricity would understate profit by "
              + rupee(1200)
              + "."),
        )
        + identify(
            "If the question says “business entity / accounting entity / separate entity”, write: the business is assumed to be distinct from the owner; "
            "only business transactions enter the books; owner’s private expenses are drawings, not business expenses."
        )
        + mistakes(
            [
                "Treating a sole proprietor’s shop as legally a company. Entity is an accounting idea. A sole shop is not a separate legal person, but we still keep separate books.",
                "Calling drawings an expense. Drawings reduce capital. They do not go to the profit calculation as rent or purchases would.",
            ]
        )
        + memory(
            "Two names, two pockets: “Rahul” and “Rahul Stationery”. If it is not for the shop, it is not a shop expense."
        )
        + exam_answer(
            "Under the business entity concept the enterprise is treated as a unit separate from its owner. Transactions are recorded from the point of view of the business, not the owner. "
            "Money introduced by the owner is capital of the business (a claim on the business). Money or goods taken by the owner for personal use are drawings, which reduce capital, "
            "and are not expenses of the business. This separation is what makes profit of the shop measurable."
        )
    )


def _transaction() -> str:
    return (
        h2("5. What is a business transaction?", "transaction")
        + definition(
            "A <strong>business transaction</strong> is an event that changes the money or the value of the business, can be measured in rupees, "
            "and is supported by evidence (bill, invoice, cheque, receipt, voucher, contract)."
        )
        + simple(
            "If the shop’s pocket got heavier or lighter, or what the shop owns or owes changed, and you can prove it with a paper (or a bank SMS), it is a transaction. "
            "If nothing moved except a thought or a handshake, it is not."
        )
        + why(
            "Accounting records transactions, not hopes. If we recorded every idea, the books would be fiction. Evidence is what lets a bank, an auditor, or an examiner trust the figure."
        )
        + real_life(
            "A customer says, “I will definitely buy 20 diaries next week.” That is not a transaction. Next week she pays "
            + rupee(2000)
            + " and takes the diaries — now it is a transaction: cash in, stock out, evidence = bill."
        )
        + logic(
            "Three tests, all must pass: (1) change in money or value of this business, (2) measurable in ₹, (3) evidence. Fail any one, leave it out of the books."
        )
        + table(
            ["Event", "Transaction?", "Why"],
            [
                ["Rahul thinks of buying a glass display for " + rupee(8000) + ".", b("No"), "Only a thought. Nothing moved. No evidence."],
                ["Rahul shakes hands with a carpenter “to discuss a counter”.", b("No"), "Handshake without money or a signed order. No value change yet."],
                ["Rahul starts the shop with cash " + rupee(100000) + ".", b("Yes"), "Cash of the shop rose. Capital rose. Bank deposit slip / cash in hand is evidence."],
                ["Buys furniture for " + rupee(20000) + " cash, takes a bill.", b("Yes"), "Cash down, furniture up. Bill in hand."],
                ["Orders 100 notebooks by a WhatsApp message. Nothing delivered, nothing paid.", b("No"), "A mere order. Stock has not come. Cash has not gone. (When goods or invoice arrive, then yes.)"],
                ["A friend praises the shop.", b("No"), "Goodwill in conversation is not measured in ₹ in these books."],
                ["Rahul’s sister studies at the counter.", b("No"), "No money, no value change of the shop."],
                ["Pays rent " + rupee(5000) + " by cheque.", b("Yes"), "Bank down, expense up. Cheque and rent receipt."],
                ["Aman supplies stock of " + rupee(30000) + " on credit, invoice received.", b("Yes"), "Stock up, a creditor (Aman) up. Invoice is evidence. Cash need not move."],
                ["Rahul takes " + rupee(4000) + " from the till for a personal trip.", b("Yes"), "Cash of the shop down, drawings up. Even though it is personal, the shop’s cash changed — so the shop must record it."],
            ],
            caption="What is a transaction, and what is not",
        )
        + warn(
            "Credit purchases and credit sales are transactions. “On credit” does not mean “not yet a transaction”. Value changed: you have the goods, you owe Aman. Record it the day the invoice/goods arrive, not the day you pay."
        )
        + example(
            "0.5",
            "Easy",
            "Tick the transactions",
            p("From this list, which two enter the books today? (a) Rahul plans to take a loan next month. (b) A customer pays "
              + rupee(500)
              + " cash for pens. (c) Rahul dreams of a second shop. (d) Furniture of "
              + rupee(20000)
              + " is delivered and paid for.")
            + p(b("Answer. ") + "(b) and (d). (a) is a plan. (c) is a dream. Both fail the three tests."),
        )
        + identify(
            "If the question says “which of the following is not a transaction”, look for: thoughts, plans, orders not executed, personal events that do not touch the shop, or things that cannot be measured in money."
        )
        + mistakes(
            [
                "Waiting for cash before recording. Credit purchases and credit sales are transactions on the invoice date.",
                "Recording a signed “we will do business sometime” handshake. No goods, no money, no invoice — no transaction.",
                "Leaving drawings out because “it is personal”. Personal for Rahul, but the shop’s cash moved — the shop must record it.",
            ]
        )
        + memory(
            "C-M-E: Change, Money-measure, Evidence. All three, or it stays out."
        )
    )


def _five_elements() -> str:
    return (
        h2("6. The five elements — a map", "five-elements")
        + p(
            "Every amount in Rahul’s books belongs to one of five families. Learn the families first. Names of accounts come after."
        )
        + table(
            ["Family", "In one line", "Rahul example", "Where it lives in the equation"],
            [
                [b("Assets"), "What the shop owns or is owed.", "Cash, bank, stock, furniture, debtors.", "Left side — resources."],
                [b("Liabilities"), "What the shop owes to outsiders.", "Aman the creditor, a bank loan, unpaid rent.", "Right side — outsiders’ claims."],
                [b("Capital"), "What the shop owes to the owner.", "Rahul’s " + rupee(100000) + " put in.", "Right side — owner’s claim."],
                [b("Revenue (income)"), "Value earned by the shop from its work.", "Sales, commission received, interest received.", "Increases capital (profit)."],
                [b("Expenses"), "Cost of earning that revenue.", "Rent, salary, electricity, cost of goods sold.", "Decreases capital (and may create a loss)."],
            ],
            caption="Five families. Every account is a child of one family.",
        )
        + keypoint(
            "Revenue and expenses are not a sixth and seventh side of the equation. They explain why capital changed. "
            "Profit (revenue − expenses) is added to capital. A loss is subtracted. Drawings are also subtracted from capital, but drawings are not an expense."
        )
        + formula(
            "Assets = Liabilities + Capital, &nbsp; and Capital grows with profit and shrinks with loss and drawings",
            "Master this map. Debit and credit are only a way of writing the map.",
        )
    )


def _assets() -> str:
    return (
        h2("7. Assets", "assets")
        + definition(
            "An <strong>asset</strong> is a resource of the business that has money value and will give a benefit in the future — something the shop owns, or something someone owes the shop."
        )
        + simple(
            "If Rahul can point to it and say “this belongs to the shop and it is worth rupees”, it is an asset. Cash in the drawer. Money in the bank. Pens on the shelf. The wooden counter. A customer who has not yet paid."
        )
        + why(
            "We list assets so that we know what the shop has to work with, and so that the bank and Rahul can see the resources that stand behind the liabilities and capital."
        )
        + real_life(
            "Rahul’s wooden display is an asset because it will be used for years to hold goods. A chocolate he eats at lunch is not an asset of the shop — it is gone, and it was personal."
        )
        + logic(
            "An asset is a future benefit stored in rupees. Cash is a benefit now. Stock is a benefit when sold. Furniture is a benefit while it is used. "
            "A debtor is a benefit when the customer pays. Prepaid rent is a benefit because next month’s occupancy is already paid."
        )
        + table(
            ["Asset", "What it is", "Current or non-current", "Why it is an asset"],
            [
                [b("Cash"), "Notes and coins in the till / cash box.", "Current", "Can be spent immediately."],
                [b("Bank"), "Money in the shop’s bank account.", "Current", "Can be drawn by cheque or UPI."],
                [b("Inventory / Stock"), "Goods held for sale — pens, notebooks, files.", "Current", "Will turn into cash when customers buy."],
                [b("Debtors / Receivables"), "Customers who bought on credit and still owe the shop.", "Current", "They are expected to pay in a short time."],
                [b("Furniture"), "Counter, shelves, chairs, display.", "Non-current", "Used for years, not sold to customers."],
                [b("Machinery"), "Photocopy machine, billing printer.", "Non-current", "Used to run the shop, not held for sale."],
                [b("Building"), "The shop premises if Rahul owns it.", "Non-current", "Used for years."],
                [b("Prepaid (e.g. prepaid insurance, prepaid rent)"), "An expense paid in advance, benefit still to come.", "Current", "The unused portion is a resource — we have already paid for a future benefit."],
            ],
            caption="Assets Rahul will meet — and whether they are current",
        )
        + h3("Current versus non-current, in simple words")
        + two_col(
            box(
                "simple",
                "Current assets",
                "<p>Things that are cash, or will become cash, or will be used up, <strong>within about a year</strong> (one operating cycle).</p>"
                + ul(
                    [
                        "Cash, bank",
                        "Stock",
                        "Debtors",
                        "Prepaid expenses",
                        "Short-term deposits",
                    ]
                ),
            ),
            box(
                "simple",
                "Non-current assets",
                "<p>Things the shop will <strong>use for more than a year</strong>, not sell in the ordinary course of business.</p>"
                + ul(
                    [
                        "Furniture, fixtures",
                        "Machinery, computers",
                        "Building, land",
                        "Goodwill, patents (intangible)",
                    ]
                ),
            ),
        )
        + p(
            b("Simple test. ")
            + "Will this turn into cash, or get used up, inside a year? Current. Will we still be using it next year and the year after? Non-current. "
            "Stock of pens is current even if a few diaries stay on the shelf for 14 months — we hold them to sell, not to use."
        )
        + warn(
            "Buying a photocopy machine is not “purchases”. Purchases means goods bought to sell. A machine is an asset (machinery). Mixing these two is one of the most common exam mistakes and we will hit it again."
        )
        + example(
            "0.6",
            "Easy",
            "Sort these into current and non-current",
            p("Cash " + rupee(53000) + ", furniture " + rupee(20000) + ", stock of pens " + rupee(20000) + ", prepaid insurance " + rupee(3000) + ", building " + rupee(500000) + ", debtors " + rupee(8000) + ".")
            + p(b("Answer. ")
              + "Current: cash, stock, prepaid insurance, debtors. Non-current: furniture, building."),
        )
        + example(
            "0.7",
            "Moderate",
            "Is a debtor an asset even if the customer is a friend?",
            p("Rahul sells " + rupee(2000) + " of files to his college friend on credit.")
            + p(b("Answer. ")
              + "Yes. The shop is owed " + rupee(2000) + ". That claim is a debtor, a current asset. Friendship is not recorded. If the friend never pays, the asset will later be written off as a loss — but on the day of sale it is an asset."),
        )
        + identify(
            "If the question says “what are assets / classify assets / current vs fixed (non-current)”, define, then split current (cash, bank, stock, debtors, prepaid) and non-current (furniture, machinery, building, goodwill). Give one line on the “within a year” test."
        )
        + mistakes(
            [
                "Calling the owner’s personal bike a shop asset. Entity concept — only if the shop owns it.",
                "Listing capital as an asset. Capital is the owner’s claim, on the other side.",
                "Calling stock a non-current asset “because we always keep stock”. Stock is held for sale, so it is current.",
            ]
        )
        + memory(
            "Asset = a future benefit the shop controls. Current = cash-ish within a year. Non-current = used for years (furniture, machines, building)."
        )
    )


def _liabilities() -> str:
    return (
        h2("8. Liabilities", "liabilities")
        + definition(
            "A <strong>liability</strong> is an amount the business owes to an outsider — a present duty to pay money or to give goods/services, arising from a past event."
        )
        + simple(
            "If someone who is not Rahul can knock on the shop door and say “pay me”, that amount is a liability. Aman who supplied stock on credit. The bank that gave a loan. The landlord if this month’s rent is still unpaid."
        )
        + why(
            "Liabilities are claims on the assets. We list them so that we never confuse “what we have” with “what is ours”. A shop can be full of stock and still be in trouble if most of it is owed to suppliers."
        )
        + real_life(
            "Aman delivers notebooks worth "
            + rupee(30000)
            + " and says “pay me in 30 days”. Rahul has the notebooks (asset) and he has a creditor called Aman (liability). Both must be recorded the same day. Recording only the stock would pretend the notebooks are free."
        )
        + logic(
            "A liability is the other side of an asset that arrived before cash left, or of cash that arrived with a promise to return it (a loan). Dual aspect: something came in, a claim was created."
        )
        + table(
            ["Liability", "What it is", "Current or non-current", "Rahul example"],
            [
                [
                    b("Creditors / Payables"),
                    "Suppliers from whom we bought on credit.",
                    "Current",
                    "Aman " + rupee(30000) + " for stock.",
                ],
                [
                    b("Bank loan (due after 12 months)"),
                    "Money borrowed from a bank, repayable later.",
                    "Non-current (the long-term part)",
                    "A 3-year loan of " + rupee(50000) + ".",
                ],
                [
                    b("Bank overdraft / loan due within 12 months"),
                    "Short borrowing, or the instalment due this year.",
                    "Current",
                    "Overdraft to pay a supplier this week.",
                ],
                [
                    b("Outstanding expenses"),
                    "Expenses incurred but not yet paid (rent unpaid, salary unpaid).",
                    "Current",
                    "Outstanding rent " + rupee(5000) + " if Rahul has used the shop but not paid.",
                ],
            ],
            caption="Liabilities — outsiders’ claims",
        )
        + h3("Current versus non-current liabilities")
        + two_col(
            box(
                "simple",
                "Current liabilities",
                "<p>Duties we expect to settle <strong>within a year</strong>.</p>"
                + ul(
                    [
                        "Creditors (Aman)",
                        "Outstanding rent, outstanding salary",
                        "Bank overdraft",
                        "Short-term loan / this year’s instalment",
                        "GST payable, tax deducted but not deposited",
                    ]
                ),
            ),
            box(
                "simple",
                "Non-current liabilities",
                "<p>Duties that stretch <strong>beyond a year</strong>.</p>"
                + ul(
                    [
                        "Term loan from a bank (the part due after 12 months)",
                        "Long-term deposit from a customer or tenant",
                        "Debentures (in a company)",
                    ]
                ),
            ),
        )
        + keypoint(
            "Capital is not a liability to an outsider. It is a claim of the owner. In the equation it sits with liabilities because both are claims on assets, but we never call capital “a liability” in a classification question — we call it capital / equity / owner’s equity."
        )
        + example(
            "0.8",
            "Easy",
            "Is a bank loan a liability or capital?",
            p("Rahul’s bank credits " + rupee(50000) + " as a loan. His aunt also gifts him " + rupee(10000) + " which he puts into the shop.")
            + p(b("Answer. ")
              + "The "
              + rupee(50000)
              + " is a liability (bank loan) — it must be repaid. The "
              + rupee(10000)
              + " is capital — the owner (via his aunt’s gift, now his money) put it in; it is not repayable on demand as a loan is."),
        )
        + identify(
            "If the question says “what are liabilities / classify liabilities”, define as amounts owed to outsiders, then split current (creditors, outstanding expenses, overdraft) and non-current (term loan). Stress: capital is not a liability."
        )
        + mistakes(
            [
                "Calling capital a liability. Capital is the owner’s claim, shown with liabilities in the equation, but classified separately.",
                "Forgetting outstanding expenses. If the shop has used electricity this month and not paid, a liability already exists.",
                "Treating a loan as income. A loan increases cash/bank and increases a liability. It is not sales. It is not profit.",
            ]
        )
        + memory(
            "Liability = we owe an outsider. Current = due within a year (Aman, unpaid rent). Non-current = due after a year (term loan). Capital is the owner, not an outsider."
        )
    )


def _capital() -> str:
    return (
        h2("9. Capital", "capital")
        + definition(
            "<strong>Capital</strong> is the amount the owner has invested in the business — the owner’s claim on the assets after outsiders have been provided for. In equation form, Capital = Assets − Liabilities."
        )
        + simple(
            "Capital is Rahul’s money in the shop. When he puts " + rupee(100000) + " into the cash box on day one, the shop now owes that claim to Rahul. It is not a gift the shop can forget. It is not a loan with interest. It is the owner’s stake."
        )
        + why(
            "Without capital we cannot say whose leftover the assets are. After Aman and the bank have been provided for, what remains is Rahul’s. That remainder is capital."
        )
        + real_life(
            "Rahul puts " + rupee(100000) + " cash in. Later the shop makes a profit of " + rupee(2000) + " and Rahul takes " + rupee(4000) + " home. Closing capital is "
            + rupee(100000)
            + " + "
            + rupee(2000)
            + " − "
            + rupee(4000)
            + " = "
            + rupee(98000)
            + ". You will watch this happen, transaction by transaction, in the equation section."
        )
        + logic(
            "Capital is a claim, so it lives on the same side as liabilities. It grows when the owner introduces money or when the shop makes a profit. It shrinks when the shop makes a loss or when the owner takes drawings."
        )
        + formula(
            "Closing capital = Opening capital + Additional capital + Profit − Loss − Drawings",
            "Profit itself is Revenue − Expenses. If expenses exceed revenue, there is a loss and capital falls.",
        )
        + format_box(
            "How capital moves",
            table(
                ["Event", "Effect on capital"],
                [
                    ["Owner puts cash/goods in", "Capital increases"],
                    ["Shop earns revenue (sales, commission, interest received)", "Capital increases (via profit)"],
                    ["Shop incurs expenses (rent, salary, cost of goods sold)", "Capital decreases (via profit/loss)"],
                    ["Owner takes cash or goods for personal use (drawings)", "Capital decreases"],
                    ["Loss for the period", "Capital decreases"],
                ],
            ),
        )
        + example(
            "0.9",
            "Moderate",
            "Compute closing capital",
            p("Opening capital " + rupee(100000) + ". Profit " + rupee(2000) + ". Drawings " + rupee(4000) + ". No extra capital introduced.")
            + p(b("Working. ") + rupee(100000) + " + " + rupee(2000) + " − " + rupee(4000) + " = " + rupee(98000) + ".")
            + p(b("Answer. ") + "Closing capital " + rupee(98000) + "."),
        )
        + identify(
            "If the question says “what is capital / compute closing capital”, write the definition, then the formula Opening + additional capital + profit − loss − drawings. Never subtract drawings from profit as if drawings were an expense — subtract them from capital."
        )
        + mistakes(
            [
                "Treating capital as cash. Cash is an asset. Capital is a claim. On day one they may be equal; after a few transactions they are not (see T2: cash is " + rupee(80000) + ", capital is still " + rupee(100000) + ").",
                "Adding a bank loan to capital. A loan is a liability.",
            ]
        )
        + memory(
            "Capital is the owner’s stake, not the cash in the till. Formula: start + profit − drawings (and − loss if any)."
        )
    )


def _revenue() -> str:
    return (
        h2("10. Revenue / Income", "revenue")
        + definition(
            "<strong>Revenue</strong> (income) is the value earned by the business from its ordinary activities and from other permitted gains — sales of goods, commission received, interest received, rent received."
        )
        + simple(
            "Revenue is the shop earning. Not a loan. Not capital introduced. Earning. When a customer buys a notebook, that selling price is sales (revenue). When a neighbour pays Rahul a small commission for collecting a courier, that is commission received (revenue)."
        )
        + why(
            "Revenue is one half of profit. Without naming it we cannot say whether the shop earned more than it spent."
        )
        + real_life(
            "Rahul sells a box of files for " + rupee(15000) + " cash. The " + rupee(15000) + " is sales, a revenue. It is not “cash capital”. It is not a loan. Cash rose because a customer paid for goods."
        )
        + logic(
            "Revenue increases capital. That is why, under the modern rule, an increase in income is credited — the same side as an increase in capital."
        )
        + table(
            ["Income", "What it is", "Not to be confused with"],
            [
                [b("Sales"), "Selling price of goods sold to customers.", "Capital introduced; a bank loan; cash withdrawn."],
                [b("Commission received"), "Earning for a service or a referral.", "Commission paid (that is an expense)."],
                [b("Interest received"), "Earning on money the shop has lent or deposited.", "Interest paid on a loan (expense)."],
                [b("Rent received"), "If Rahul sub-lets a corner of the shop.", "Rent paid for the shop (expense)."],
            ],
            caption="Incomes you must name correctly",
        )
        + warn(
            "“Received” in the name (interest received, commission received, rent received) signals income. “Paid” (interest paid, rent paid) signals expense. The exam uses these two words as a trap. Read them."
        )
        + example(
            "0.10",
            "Easy",
            "Is a loan income?",
            p("The bank credits " + rupee(50000) + " into Rahul’s account as a loan. Is this revenue?")
            + p(b("Answer. ")
              + "No. The shop must repay it. Bank (asset) increases and Bank loan (liability) increases. Revenue would increase capital without creating a repayable duty. A loan is not earning."),
        )
        + identify(
            "If the question says “what is revenue / give examples of income”, write: value earned by the business. Examples: sales, commission received, interest received, rent received. Explicitly exclude capital introduced and loans."
        )
        + mistakes(
            [
                "Crediting cash because “money came in”. Money coming in is a debit to Cash/Bank. The credit is to Sales, Commission, Loan, or Capital — depending on why the money came in.",
                "Treating sales and capital as the same because both “bring money”. Why the money came in is the whole point.",
            ]
        )
        + memory(
            "Income = earned. Sales, commission received, interest received, rent received. If we have to give it back (loan) or if the owner put it in (capital), it is not income."
        )
    )


def _expenses() -> str:
    return (
        h2("11. Expenses", "expenses")
        + definition(
            "An <strong>expense</strong> is a cost incurred to earn the revenue of the period — rent, salary, electricity, insurance expired, interest paid, and the cost of goods that were sold."
        )
        + simple(
            "Expenses are the shop spending in order to run and to sell. Paying the landlord. Paying a helper. Paying the electricity board. The cost of the notebooks that actually left the shelf."
        )
        + why(
            "Profit is a leftover. You cannot know the leftover until you have named every cost of earning this period’s revenue."
        )
        + real_life(
            "Rahul pays " + rupee(5000) + " rent by cheque. That " + rupee(5000) + " is an expense. It does not buy him a lasting asset. It buys him one month of occupying the lane. The benefit dies with the month — that is the mark of an expense."
        )
        + logic(
            "Expenses decrease capital. That is why an increase in expense is debited — the same side as a decrease in capital (and the same side as drawings)."
        )
        + h3("Purchases of goods versus buying a machine")
        + p(
            b("Purchases")
            + " means goods bought for resale — the stock of a stationery shop: pens, notebooks, files, erasers. In the journal we debit "
            + b("Purchases A/c")
            + " (a nominal account, treated as an expense of buying goods). Those goods sit as "
            + b("stock")
            + " (an asset) until they are sold. Unsold goods remain an asset. Sold goods become an expense (cost of goods sold)."
        )
        + p(
            "Buying a "
            + b("machine, furniture, or a building")
            + " is not purchases. Those are assets the shop will use, not sell. Debit Furniture or Machinery, not Purchases. This single mix-up costs marks in almost every exam."
        )
        + table(
            ["Spending", "Account to debit", "Family", "Why"],
            [
                ["Pens and notebooks to sell, " + rupee(30000), "Purchases (and they become Stock)", "Expense / Asset (stock)", "Goods for resale."],
                ["Wooden counter, " + rupee(20000), "Furniture", "Asset (non-current)", "Will be used, not sold to customers."],
                ["Photocopy machine, " + rupee(40000), "Machinery", "Asset (non-current)", "A tool of the shop, not merchandise."],
                ["Shop rent, " + rupee(5000), "Rent", "Expense", "Benefit of one month, then gone."],
                ["Helper’s salary, " + rupee(8000), "Salary", "Expense", "Cost of labour this month."],
                ["Electricity bill, " + rupee(800), "Electricity", "Expense", "Used up in the month."],
                ["Interest on loan, " + rupee(500), "Interest paid", "Expense", "Cost of borrowing, not a repayment of the loan itself."],
            ],
            caption="Purchases of goods are not the same as buying a machine",
        )
        + two_col(
            box(
                "key",
                "Goods (purchases / stock)",
                ul(
                    [
                        "Bought to be sold.",
                        "Account: Purchases (journal), Stock (equation / balance sheet).",
                        "Unsold = asset. Sold = expense (cost).",
                    ]
                ),
            ),
            box(
                "key",
                "Use-assets (furniture / machinery)",
                ul(
                    [
                        "Bought to be used for years.",
                        "Account: Furniture, Machinery, Building.",
                        "Never “Purchases”. Never an expense on day one.",
                    ]
                ),
            ),
        )
        + example(
            "0.11",
            "Moderate",
            "Three payments, three families",
            p("Rahul pays by cheque: (i) " + rupee(12000) + " to Aman for stock bought earlier, (ii) " + rupee(5000) + " rent, (iii) " + rupee(20000) + " for a new display cabinet.")
            + p(b("Answer. ")
              + "(i) is not an expense today — it reduces a liability (Aman) and reduces Bank. The expense/stock was recorded when the goods arrived. "
              + "(ii) is an expense (Rent). "
              + "(iii) is an asset (Furniture), not purchases and not an expense."),
        )
        + identify(
            "If the question says “purchases”, think goods for resale. If it says furniture / machinery / building / vehicle, think asset. If it says rent, salary, electricity, interest paid, think expense."
        )
        + mistakes(
            [
                "Debiting Purchases when a machine is bought. Debit Machinery.",
                "Debiting Rent when last month’s outstanding rent is paid. That payment reduces a liability (Outstanding rent); the expense was recorded last month.",
                "Treating repayment of a loan as an expense. Repayment reduces the liability and reduces Bank. Interest on the loan is the expense.",
            ]
        )
        + memory(
            "Expense = used up to earn this period’s income. Purchases = goods to sell. Furniture/machinery = goods to use. Paying a creditor is not a new expense."
        )
    )


def _profit_loss() -> str:
    return (
        h2("12. Profit and loss", "profit-loss")
        + definition(
            "<strong>Profit</strong> is the excess of revenue over expenses for a period. <strong>Loss</strong> is the excess of expenses over revenue. Profit increases capital. Loss decreases capital."
        )
        + simple(
            "Profit is leftover earning. If the shop earned " + rupee(17000) + " and spent " + rupee(15000) + " to earn it, leftover is " + rupee(2000) + " — profit. If it had spent " + rupee(20000) + ", leftover would be negative — a loss of " + rupee(3000) + "."
        )
        + why(
            "Profit is the score of the shop. Rahul did not open a stationery shop to move cash from one pocket to another. He opened it to have more capital at the end than at the start, after drawings."
        )
        + real_life(
            "In our ten transactions Rahul will: sell stock that cost " + rupee(10000) + " for " + rupee(15000) + " (sales "
            + rupee(15000)
            + ", cost "
            + rupee(10000)
            + "), pay rent "
            + rupee(5000)
            + ", receive commission "
            + rupee(2000)
            + ". Revenue = "
            + rupee(15000)
            + " + "
            + rupee(2000)
            + " = "
            + rupee(17000)
            + ". Expenses = "
            + rupee(10000)
            + " + "
            + rupee(5000)
            + " = "
            + rupee(15000)
            + ". Profit = "
            + rupee(17000)
            + " − "
            + rupee(15000)
            + " = "
            + rupee(2000)
            + "."
        )
        + logic(
            "Profit is not cash. Rahul can be in profit and still be short of cash (money stuck in stock or debtors). Profit is a change in capital, not a change in the till. We will prove this with the running equation."
        )
        + formula(
            "Profit (or Loss) = Revenue − Expenses",
            "If the result is negative, it is a loss. Add profit to capital. Subtract a loss from capital. Do not touch drawings here — drawings are not an expense.",
        )
        + table(
            ["Item", "₹", "Family"],
            [
                ["Sales", rupee(15000), "Revenue"],
                ["Commission received", rupee(2000), "Revenue"],
                [b("Total revenue"), b(rupee(17000)), ""],
                ["Cost of stock sold", rupee(10000), "Expense"],
                ["Rent", rupee(5000), "Expense"],
                [b("Total expenses"), b(rupee(15000)), ""],
                [b("Profit"), b(rupee(2000)), "Added to capital"],
            ],
            caption="Rahul’s profit from T1–T10 (full working)",
        )
        + example(
            "0.12",
            "Exam-level",
            "Profit is not cash",
            p("Suppose Rahul had sold the same goods on credit instead of cash. Sales still " + rupee(15000) + ", cost still " + rupee(10000) + ", rent still paid " + rupee(5000) + ", commission still " + rupee(2000) + " cash. Is profit still " + rupee(2000) + "? Is cash the same?")
            + p(b("Answer. ")
              + "Profit is still "
              + rupee(2000)
              + " — revenue and expenses did not change. Cash is lower by "
              + rupee(15000)
              + ", and Debtors are higher by "
              + rupee(15000)
              + ". Profit ≠ cash. This is why later chapters separate the profit statement from the cash flow statement."),
        )
        + identify(
            "If the question says “calculate profit” or “does the firm make a profit or a loss”, list all revenues, list all expenses, subtract. Do not include capital introduced, loans, drawings, or purchase of furniture in this arithmetic."
        )
        + mistakes(
            [
                "Subtracting drawings from revenue as if drawings were an expense. Drawings reduce capital, not profit.",
                "Including purchase of furniture in expenses. Furniture is an asset.",
                "Including a loan received as revenue. A loan is a liability.",
                "Equating profit with the increase in cash. Cash also moves when we buy furniture, pay creditors, take loans, and make drawings.",
            ]
        )
        + memory(
            "Profit = Revenue − Expenses. Negative = loss. Profit goes to capital. Drawings do not enter this formula."
        )
    )


def _drawings() -> str:
    return (
        h2("13. Drawings", "drawings")
        + definition(
            "<strong>Drawings</strong> are money or goods the owner takes from the business for personal use. Drawings reduce capital. Drawings are not an expense of the business."
        )
        + simple(
            "When Rahul takes " + rupee(4000) + " from the till to pay for a personal trip, the shop did not incur a trip expense. The owner took his own money out of the box. We reduce cash and we reduce capital, through an account called Drawings."
        )
        + why(
            "If we called drawings an expense, profit of the shop would depend on how much pizza Rahul ate, which is nonsense. The shop’s profit should measure the shop, not the owner’s kitchen."
        )
        + real_life(
            "Two cases, same idea: (1) Rahul takes cash " + rupee(4000) + " — Drawings Dr., Cash Cr. (2) Rahul takes a box of pens costing " + rupee(500) + " for his cousins — Drawings Dr., Purchases/Stock Cr. Both reduce capital. Neither is rent, sales, or salary."
        )
        + logic(
            "The shop and the owner are separate (entity). When the owner takes from the shop, the shop’s claim owed to the owner (capital) shrinks. That is a capital movement, not a cost of earning sales."
        )
        + two_col(
            box(
                "miss",
                "Drawings — not an expense",
                ul(
                    [
                        "Owner taking cash for home.",
                        "Owner taking goods for family.",
                        "Owner’s personal electricity paid from the till.",
                        "Owner’s medical bill paid by the shop.",
                        "Effect: capital ↓. Profit is not charged.",
                    ]
                ),
            ),
            box(
                "key",
                "These ARE expenses",
                ul(
                    [
                        "Shop rent.",
                        "Shop salary.",
                        "Shop electricity.",
                        "Cost of goods sold to customers.",
                        "Effect: profit ↓, and therefore capital ↓.",
                    ]
                ),
            ),
        )
        + formula(
            "Closing capital = Opening capital + Profit − Drawings",
            "Drawings sit in this capital formula, not inside Profit = Revenue − Expenses.",
        )
        + example(
            "0.13",
            "Easy",
            "Where does " + rupee(4000) + " go?",
            p("Rahul withdraws " + rupee(4000) + " cash for personal use. A student writes: Debit Rent " + rupee(4000) + ", Credit Cash " + rupee(4000) + ".")
            + p(b("Answer. ")
              + "Wrong. Rent is a shop expense. This is drawings. Debit Drawings "
              + rupee(4000)
              + ", Credit Cash "
              + rupee(4000)
              + ". Profit is unaffected. Capital falls by "
              + rupee(4000)
              + "."),
        )
        + identify(
            "If the question says “withdrew / took for personal use / household / private”, the account is Drawings. Never Rent, never Miscellaneous expense, never Salary of the owner in a sole-proprietor set of books (the owner is rewarded by profit, not by a salary, unless the question specifically creates a salary)."
        )
        + mistakes(
            [
                "Debiting Salary when the owner takes cash. The owner is not an employee of himself in a sole shop (unless the question says so).",
                "Debiting Purchases when the owner takes goods — that would leave purchases too high and profit too low. Credit Purchases or Stock, debit Drawings.",
                "Showing drawings on the profit statement as an expense. Show them in the capital working only.",
            ]
        )
        + memory(
            "Drawings = owner taking. Reduces capital. Not an expense. Mantra: “Personal take = Drawings. Shop spend = Expense.”"
        )
        + exam_answer(
            "Drawings are cash or goods withdrawn by the proprietor for personal use. They are not a business expense because they are not incurred to earn revenue of the firm. Drawings are deducted from capital. "
            "If cash is withdrawn: Drawings A/c Dr. To Cash A/c. If goods are withdrawn: Drawings A/c Dr. To Purchases (or Stock) A/c. Treating drawings as rent, salary or purchases understates profit and violates the business entity concept."
        )
    )


def _equation() -> str:
    return (
        h2("14. The accounting equation", "equation")
        + definition(
            "The <strong>accounting equation</strong> is Assets = Liabilities + Capital. It is always true, after every transaction, because every event has two sides (dual aspect)."
        )
        + simple(
            "Think of a weighing scale. On the left, everything the shop has (assets). On the right, who provided those things: outsiders (liabilities) and Rahul (capital). The two pans must weigh the same. Always."
        )
        + why(
            "If the scale does not balance, a transaction was recorded on only one side, or an amount was mistyped. The equation is the first error-check in accounting. The trial balance in Chapter 1 is this idea in list form."
        )
        + real_life(
            "Rahul puts " + rupee(100000) + " cash into the shop. The shop now has cash of " + rupee(100000) + " (asset). Who provided it? Rahul. So capital is " + rupee(100000) + ". Left " + rupee(100000) + ", right " + rupee(100000) + "."
        )
        + logic(
            "Assets are resources. Claims on those resources are either outsiders’ (liabilities) or the owner’s (capital). There is nothing left to be a third pan. So A = L + C, always. When the shop earns a profit, assets rise (or a liability falls) and capital rises by the same profit. When the owner draws, assets fall and capital falls."
        )
        + formula(
            "Assets = Liabilities + Capital",
            "This is the compact form. It never takes a holiday.",
        )
        + formula(
            "Assets = Liabilities + Opening capital + Profit − Drawings",
            "And Profit = Revenue − Expenses. Substituting: Assets = Liabilities + Opening capital + Revenue − Expenses − Drawings.",
        )
        + formula(
            "Assets + Expenses + Drawings = Liabilities + Opening capital + Revenue",
            "This rearranged form is why, in Chapter 1, a trial balance still totals. Expenses and drawings sit on the debit side with assets; revenue and capital sit on the credit side with liabilities.",
        )
        + format_box(
            "How to use the equation on any transaction",
            ol(
                [
                    "Name what changed (at least two things — dual aspect).",
                    "Classify each as Asset, Liability, or Capital (revenue/expense/drawings are capital-changes).",
                    "Write the + or − rupee amount against each.",
                    "Add the new totals. Check Assets = Liabilities + Capital.",
                    "If they do not match, you missed a side. Go back.",
                ]
            ),
        )
        + p(
            "We now walk "
            + b("ten transactions")
            + " of Rahul Stationery. After every one you will see: (1) a snapshot of each account, (2) the proof A = L + C, (3) a running table that keeps Cash, Bank, Furniture, Stock, Debtors, Prepaid, Creditors, Loan and Capital. Debtors and Prepaid stay "
            + rupee(0)
            + " — the columns are there so you can see the empty slots. All arithmetic is shown. Indian commas throughout."
        )
        + p(
            b("Opening position. ")
            + "Before T1 the shop does not exist. Every account is "
            + rupee(0)
            + ". Assets "
            + rupee(0)
            + " = Liabilities "
            + rupee(0)
            + " + Capital "
            + rupee(0)
            + "."
        )
        + _t1_to_t10()
        + h3("After T10 — full equation and a mini balance sheet")
        + p(
            "Let us add the last row by hand, slowly, so the exam working is visible."
        )
        + table(
            ["Account", "Amount", "Side"],
            [
                ["Cash", rupee(53000), "Asset"],
                ["Bank", rupee(73000), "Asset"],
                ["Furniture", rupee(20000), "Asset"],
                ["Stock", rupee(20000), "Asset"],
                ["Debtors", rupee(0), "Asset"],
                ["Prepaid", rupee(0), "Asset"],
                [b("Total assets"), b(rupee(166000)), "53,000 + 73,000 + 20,000 + 20,000 + 0 + 0 = 1,66,000"],
                ["Creditors (Aman)", rupee(18000), "Liability"],
                ["Bank loan", rupee(50000), "Liability"],
                [b("Total liabilities"), b(rupee(68000)), "18,000 + 50,000 = 68,000"],
                ["Opening capital", rupee(100000), "Capital"],
                ["Add: profit (working below)", rupee(2000), "Capital ↑"],
                ["Less: drawings", rupee(4000), "Capital ↓"],
                [b("Closing capital"), b(rupee(98000)), "1,00,000 + 2,000 − 4,000 = 98,000"],
                [b("Liabilities + capital"), b(rupee(166000)), "68,000 + 98,000 = 1,66,000"],
            ],
            caption="Paper working after T10 — every addition shown",
            foot="Assets 1,66,000 = Liabilities 68,000 + Capital 98,000. The equation balances.",
        )
        + h4("Profit working (so the 2,000 is not a magic number)")
        + table(
            ["", "₹", "₹"],
            [
                ["Sales (T5)", "", rupee(15000)],
                ["Add: Commission received (T7)", "", rupee(2000)],
                [b("Revenue"), "", b(rupee(17000))],
                ["Cost of stock sold (T5: stock out at cost)", rupee(10000), ""],
                ["Rent (T6)", rupee(5000), ""],
                [b("Expenses"), "", b(rupee(15000))],
                [b("Profit"), "", b(rupee(2000))],
            ],
            caption="Profit = Revenue − Expenses = 17,000 − 15,000 = 2,000",
        )
        + formula(
            "A = L + Opening capital + Profit − Drawings  →  1,66,000 = 68,000 + 1,00,000 + 2,000 − 4,000",
            "68,000 + 1,00,000 = 1,68,000; plus 2,000 = 1,70,000; minus 4,000 = 1,66,000. Matches assets.",
        )
        + h4("Mini balance sheet of Rahul Stationery (after T10)")
        + p(
            "A balance sheet is the equation written as a statement on a given date. Same numbers, presentation form. "
            "Indian MBA exams use a vertical statement. A simple two-sided form is shown first because it is the equation on a page."
        )
        + two_col(
            table(
                ["Assets", "₹"],
                [
                    [b("Current assets"), ""],
                    ["Cash", rupee(53000)],
                    ["Bank", rupee(73000)],
                    ["Stock", rupee(20000)],
                    ["Debtors", rupee(0)],
                    ["Prepaid", rupee(0)],
                    [b("Non-current assets"), ""],
                    ["Furniture", rupee(20000)],
                    [b("Total assets"), b(rupee(166000))],
                ],
                caption="Assets",
            ),
            table(
                ["Liabilities and capital", "₹"],
                [
                    [b("Capital"), ""],
                    ["Opening capital", rupee(100000)],
                    ["Add: profit", rupee(2000)],
                    ["Less: drawings", rupee(4000)],
                    ["Closing capital", rupee(98000)],
                    [b("Non-current liabilities"), ""],
                    ["Bank loan", rupee(50000)],
                    [b("Current liabilities"), ""],
                    ["Creditors — Aman", rupee(18000)],
                    [b("Total liabilities and capital"), b(rupee(166000))],
                ],
                caption="Claims on the assets",
            ),
        )
        + keypoint(
            "The mini balance sheet totals "
            + rupee(166000)
            + " on both sides. That is not a coincidence and not a rounding. It is the accounting equation, after ten transactions, still standing. If you ever finish a sum and the sides differ, the error is in the postings, not in the equation."
        )
        + running_eq(10, "Full running equation — T1 to T10 (all rows together)")
        + table(
            ["Txn", "What happened to the equation, in one line"],
            [
                ["T1", "A +1,00,000 (cash) and C +1,00,000. Both sides up equally."],
                ["T2", "One asset swapped for another (cash → furniture). Totals unchanged."],
                ["T3", "One asset swapped for another (cash → bank). Totals unchanged."],
                ["T4", "A +30,000 (stock) and L +30,000 (Aman). Both sides up equally."],
                ["T5", "Cash +15,000, stock −10,000, so assets net +5,000; capital +5,000 profit."],
                ["T6", "Bank −5,000 and capital −5,000 (rent expense). Both sides down equally."],
                ["T7", "Cash +2,000 and capital +2,000 (commission). Both sides up equally."],
                ["T8", "Cash −4,000 and capital −4,000 (drawings). Both sides down equally."],
                ["T9", "Bank −12,000 and creditors −12,000. Both sides down equally."],
                ["T10", "Bank +50,000 and loan +50,000. Both sides up equally."],
            ],
            caption="Every transaction hits the equation at least twice",
        )
        + example(
            "0.14",
            "Exam-level",
            "Prove the expanded equation after T10",
            p("Using A = L + Opening capital + Rev − Exp − Drawings, plug in every figure.")
            + p("Assets = " + rupee(166000) + ".")
            + p("Liabilities = " + rupee(18000) + " + " + rupee(50000) + " = " + rupee(68000) + ".")
            + p("Opening capital = " + rupee(100000) + ".")
            + p("Revenue = " + rupee(15000) + " + " + rupee(2000) + " = " + rupee(17000) + ".")
            + p("Expenses = " + rupee(10000) + " + " + rupee(5000) + " = " + rupee(15000) + ".")
            + p("Drawings = " + rupee(4000) + ".")
            + p("Right-hand side = 68,000 + 1,00,000 + 17,000 − 15,000 − 4,000.")
            + p("1,68,000 + 17,000 = 1,85,000; 1,85,000 − 15,000 = 1,70,000; 1,70,000 − 4,000 = 1,66,000.")
            + p(b("Left-hand side = right-hand side = ") + rupee(166000) + ". Proved."),
        )
        + identify(
            "If the question says “explain the accounting equation with an example”, write A = L + C, one sentence on dual aspect, then a 3-to-5 line numerical example (opening capital, one purchase of an asset, one expense) and a mini statement that totals. A 5-mark ready answer is at the end of this bootcamp."
        )
        + mistakes(
            [
                "Writing Assets = Liabilities − Capital. The sign is plus. Capital is added, because it is a claim.",
                "Forgetting that profit lives inside capital. If you add profit as a fourth item without reducing the way you show capital, you will double-count.",
                "Changing only one side. If cash goes up, something else moved — capital, loan, sales, or another asset.",
            ]
        )
        + memory(
            "A = L + C. Left = what we have. Right = who provided it. After every transaction, re-total both sides. If they differ, you missed a side."
        )
    )


def _t1_to_t10() -> str:
    bits = []

    bits.append(
        teach_txn(
            "T1",
            "Rahul starts with cash ₹1,00,000",
            "Rahul puts his savings of "
            + rupee(100000)
            + " into the shop’s cash box. The shop is born. The shop now has cash. The shop now owes that claim to Rahul (capital).",
            [
                ["Cash", "Asset", "+" + rupee(100000), "Increase", "Debit"],
                ["Capital", "Capital", "+" + rupee(100000), "Increase", "Credit"],
            ],
            [
                {
                    "date": "T1",
                    "debit": "Cash A/c",
                    "credit": "Capital A/c",
                    "amount": rupee(100000),
                    "narration": "Being cash introduced by Rahul as capital to start Rahul Stationery",
                }
            ],
            "One asset up, capital up, same amount. 1,00,000 = 0 + 1,00,000. "
            "Nothing is “profit”. He moved money from his personal pocket into the shop’s pocket.",
            1,
        )
    )

    bits.append(
        teach_txn(
            "T2",
            "Buys furniture ₹20,000 cash",
            "Rahul buys a wooden counter and shelves for "
            + rupee(20000)
            + " and pays cash. He takes a bill. Cash leaves. Furniture arrives. Totals of the equation do not change — one asset replaces another.",
            [
                ["Furniture", "Asset (non-current)", "+" + rupee(20000), "Increase", "Debit"],
                ["Cash", "Asset (current)", "−" + rupee(20000), "Decrease", "Credit"],
            ],
            [
                {
                    "date": "T2",
                    "debit": "Furniture A/c",
                    "credit": "Cash A/c",
                    "amount": rupee(20000),
                    "narration": "Being furniture purchased for cash for the shop",
                }
            ],
            "Cash 1,00,000 − 20,000 = 80,000. Furniture 0 + 20,000 = 20,000. "
            "Assets still 80,000 + 20,000 = 1,00,000. Capital unchanged at 1,00,000. "
            "This is not Purchases — furniture will be used, not sold to customers.",
            2,
        )
    )

    bits.append(
        teach_txn(
            "T3",
            "Deposits ₹40,000 into bank",
            "Rahul does not want "
            + rupee(80000)
            + " sitting in the till. He deposits "
            + rupee(40000)
            + " in the shop’s bank account. Cash falls. Bank rises. Still only a swap of assets.",
            [
                ["Bank", "Asset (current)", "+" + rupee(40000), "Increase", "Debit"],
                ["Cash", "Asset (current)", "−" + rupee(40000), "Decrease", "Credit"],
            ],
            [
                {
                    "date": "T3",
                    "debit": "Bank A/c",
                    "credit": "Cash A/c",
                    "amount": rupee(40000),
                    "narration": "Being cash deposited into the shop’s bank account",
                }
            ],
            "Cash 80,000 − 40,000 = 40,000. Bank 0 + 40,000 = 40,000. "
            "Assets 40,000 + 40,000 + 20,000 furniture = 1,00,000. Capital still 1,00,000. "
            "Depositing your own cash into your own bank is not income.",
            3,
        )
    )

    bits.append(
        teach_txn(
            "T4",
            "Buys stock ₹30,000 on credit from Aman",
            "Aman, a wholesaler, delivers pens and notebooks worth "
            + rupee(30000)
            + ". He will be paid later. Invoice received. Stock of the shop rises. A creditor called Aman rises. Cash does not move — and it is still a transaction.",
            [
                ["Stock (Purchases)", "Asset / goods for resale", "+" + rupee(30000), "Increase", "Debit"],
                ["Aman (Creditors)", "Liability (current)", "+" + rupee(30000), "Increase", "Credit"],
            ],
            [
                {
                    "date": "T4",
                    "debit": "Purchases A/c",
                    "credit": "Aman (Creditor) A/c",
                    "amount": rupee(30000),
                    "narration": "Being goods purchased on credit from Aman for resale",
                }
            ],
            "In the journal we debit Purchases (the name Chapter 1 will use for goods bought). "
            "In the equation we show those goods as Stock, an asset, because they are sitting on the shelf. "
            "Stock 0 + 30,000 = 30,000. Creditors 0 + 30,000 = 30,000. "
            "Assets 40,000 cash + 40,000 bank + 20,000 furniture + 30,000 stock = 1,30,000. "
            "L + C = 30,000 + 1,00,000 = 1,30,000. Both sides rose together.",
            4,
            extra=warn(
                "Two names, one pile of pens: Purchases is the journal name (nominal, goods bought). Stock is the equation / balance-sheet name (asset, goods still in hand). Unsold purchases = stock. Do not debit Furniture. Do not debit Aman. Aman is credited because he is the giver of credit — the shop received goods from him."
            ),
        )
    )

    bits.append(
        teach_txn(
            "T5",
            "Sells stock that cost ₹10,000 for ₹15,000 cash",
            "A customer buys a chunk of the stock. The stock had cost Rahul "
            + rupee(10000)
            + ". The customer pays "
            + rupee(15000)
            + " cash. Two things happen at once: (1) an asset swap — cash in, stock out; (2) a profit of "
            + rupee(5000)
            + " which increases capital. You must show both. Showing only the "
            + rupee(15000)
            + " would pretend the goods were free.",
            [
                ["Cash", "Asset", "+" + rupee(15000), "Increase", "Debit"],
                ["Stock", "Asset", "−" + rupee(10000), "Decrease", "Credit"],
                ["Sales / Profit (inside capital)", "Income → Capital", "+" + rupee(5000), "Increase", "Credit"],
            ],
            [
                {
                    "date": "T5",
                    "lines": [
                        {"side": "dr", "account": "Cash A/c", "amount": rupee(15000)},
                        {"side": "cr", "account": "Sales A/c", "amount": rupee(15000)},
                    ],
                    "narration": "Being goods sold for cash (selling price)",
                },
                {
                    "date": "T5",
                    "lines": [
                        {"side": "dr", "account": "Cost of goods sold / Trading A/c", "amount": rupee(10000)},
                        {"side": "cr", "account": "Stock A/c", "amount": rupee(10000)},
                    ],
                    "narration": "Being cost of stock taken out of the shelf (so the equation stays honest)",
                },
            ],
            "Cash 40,000 + 15,000 = 55,000. Stock 30,000 − 10,000 = 20,000. "
            "Net assets rise by 15,000 − 10,000 = 5,000. That 5,000 is profit, so capital 1,00,000 + 5,000 = 1,05,000. "
            "Assets 55,000 + 40,000 bank + 20,000 furniture + 20,000 stock = 1,35,000. "
            "L + C = 30,000 + 1,05,000 = 1,35,000. "
            "In Chapter 1 you will often write only Cash Dr. To Sales, and match cost later through opening/closing stock. "
            "For this bootcamp we take stock down now, at cost, so every row of the equation is true on the day.",
            5,
            extra=keypoint(
                "Selling price "
                + rupee(15000)
                + " minus cost "
                + rupee(10000)
                + " = profit "
                + rupee(5000)
                + ". Never reduce stock by the selling price. Stock leaves at cost. Cash enters at selling price. The gap is profit."
            ),
        )
    )

    bits.append(
        teach_txn(
            "T6",
            "Pays rent ₹5,000 by cheque",
            "The landlord is paid "
            + rupee(5000)
            + " by cheque for this month’s occupation of the lane. Bank falls. Rent is an expense, so capital falls. The shop did not buy an asset. It bought one month of sitting in the shop, and that month will end.",
            [
                ["Rent (Expense)", "Expense → Capital ↓", "+" + rupee(5000) + " expense", "Expense increase", "Debit"],
                ["Bank", "Asset", "−" + rupee(5000), "Decrease", "Credit"],
            ],
            [
                {
                    "date": "T6",
                    "debit": "Rent A/c",
                    "credit": "Bank A/c",
                    "amount": rupee(5000),
                    "narration": "Being shop rent paid by cheque",
                }
            ],
            "Bank 40,000 − 5,000 = 35,000. Capital 1,05,000 − 5,000 = 1,00,000. "
            "Assets 55,000 + 35,000 + 20,000 + 20,000 = 1,30,000. "
            "L + C = 30,000 + 1,00,000 = 1,30,000. "
            "Cheque means Bank, not Cash. If the question says cash, credit Cash.",
            6,
        )
    )

    bits.append(
        teach_txn(
            "T7",
            "Receives commission ₹2,000 cash",
            "A neighbouring shop pays Rahul "
            + rupee(2000)
            + " cash as commission for handling a bulk order. This is income, not capital introduced, not a loan. Cash rises. Capital rises.",
            [
                ["Cash", "Asset", "+" + rupee(2000), "Increase", "Debit"],
                ["Commission received", "Income → Capital ↑", "+" + rupee(2000), "Income increase", "Credit"],
            ],
            [
                {
                    "date": "T7",
                    "debit": "Cash A/c",
                    "credit": "Commission received A/c",
                    "amount": rupee(2000),
                    "narration": "Being commission received in cash",
                }
            ],
            "Cash 55,000 + 2,000 = 57,000. Capital 1,00,000 + 2,000 = 1,02,000. "
            "Assets 57,000 + 35,000 + 20,000 + 20,000 = 1,32,000. "
            "L + C = 30,000 + 1,02,000 = 1,32,000. "
            "The word received saved you: commission received is income. Commission paid would have been an expense.",
            7,
        )
    )

    bits.append(
        teach_txn(
            "T8",
            "Rahul withdraws ₹4,000 cash for personal use",
            "Rahul takes "
            + rupee(4000)
            + " from the till for a personal trip. The shop’s cash falls. This is drawings, not rent, not salary, not a shop expense. Capital falls.",
            [
                ["Drawings", "Contra-capital", "+" + rupee(4000) + " drawings", "Drawings increase (capital ↓)", "Debit"],
                ["Cash", "Asset", "−" + rupee(4000), "Decrease", "Credit"],
            ],
            [
                {
                    "date": "T8",
                    "debit": "Drawings A/c",
                    "credit": "Cash A/c",
                    "amount": rupee(4000),
                    "narration": "Being cash withdrawn by the owner for personal use",
                }
            ],
            "Cash 57,000 − 4,000 = 53,000. Capital 1,02,000 − 4,000 = 98,000. "
            "Assets 53,000 + 35,000 + 20,000 + 20,000 = 1,28,000. "
            "L + C = 30,000 + 98,000 = 1,28,000. "
            "Profit is not charged. The profit figure we computed earlier does not contain this 4,000. Only capital does.",
            8,
            extra=warn(
                "If you debit Rent or Salary here, you understate profit by "
                + rupee(4000)
                + " and you violate the entity concept. The trip is Rahul’s, not the shop’s."
            ),
        )
    )

    bits.append(
        teach_txn(
            "T9",
            "Pays Aman ₹12,000 by cheque",
            "Rahul pays Aman part of what is owed: "
            + rupee(12000)
            + " by cheque. Bank falls. The creditor Aman falls. This is not a new purchase and not an expense. The expense/stock was recorded on T4. Today we only settle part of a debt.",
            [
                ["Aman (Creditors)", "Liability", "−" + rupee(12000), "Decrease", "Debit"],
                ["Bank", "Asset", "−" + rupee(12000), "Decrease", "Credit"],
            ],
            [
                {
                    "date": "T9",
                    "debit": "Aman (Creditor) A/c",
                    "credit": "Bank A/c",
                    "amount": rupee(12000),
                    "narration": "Being part payment to Aman by cheque",
                }
            ],
            "Bank 35,000 − 12,000 = 23,000. Creditors 30,000 − 12,000 = 18,000. "
            "Assets 53,000 + 23,000 + 20,000 + 20,000 = 1,16,000. "
            "L + C = 18,000 + 98,000 = 1,16,000. "
            "To decrease a liability we debit it (modern rule). Golden rule: Aman is a personal account — he is receiving money, so debit the receiver.",
            9,
        )
    )

    bits.append(
        teach_txn(
            "T10",
            "Takes a bank loan ₹50,000 credited to bank",
            "The bank sanctions a loan of "
            + rupee(50000)
            + " and credits the shop’s bank account. Bank rises. A liability called Bank loan rises. This is not income. This is not capital. It must be repaid.",
            [
                ["Bank", "Asset", "+" + rupee(50000), "Increase", "Debit"],
                ["Bank loan", "Liability", "+" + rupee(50000), "Increase", "Credit"],
            ],
            [
                {
                    "date": "T10",
                    "debit": "Bank A/c",
                    "credit": "Bank loan A/c",
                    "amount": rupee(50000),
                    "narration": "Being loan taken from the bank, credited to the shop’s account",
                }
            ],
            "Bank 23,000 + 50,000 = 73,000. Loan 0 + 50,000 = 50,000. "
            "Assets 53,000 + 73,000 + 20,000 + 20,000 = 1,66,000. "
            "Liabilities 18,000 + 50,000 = 68,000. Capital 98,000. "
            "L + C = 68,000 + 98,000 = 1,66,000. The scale balances.",
            10,
        )
    )
    return "".join(bits)


def _debit_credit() -> str:
    return (
        h2("15. Debit and credit — left and right, not good and bad", "debit-credit")
        + definition(
            "<strong>Debit</strong> means the left side of an account. <strong>Credit</strong> means the right side of an account. "
            "They are directions, like east and west. They are not praise and blame. They are not “good” and “bad”."
        )
        + simple(
            "Picture a big T. The name of the account sits on the top bar. The left arm is Debit (Dr). The right arm is Credit (Cr). "
            "Every amount goes on one arm or the other. “Debit Cash” means “write the amount on the left of the Cash account”."
        )
        + why(
            "We need a convention so that two people, or a person and a computer, put the same amount in the same place. "
            "Left and right is that convention. The modern rules in the next section tell you which side to use for which family."
        )
        + real_life(
            "When Rahul’s bank sends an SMS “INR 50,000 credited”, the bank is speaking from the bank’s books. In the bank’s books Rahul is a liability, so an increase is a credit. "
            "In Rahul’s books the bank account is an asset, so the same money is a debit to Bank. Same rupees, two books, opposite sides — because the two entities are facing each other. This confuses every beginner. Hold it: we always record from the shop’s point of view."
        )
        + logic(
            "Because A = L + C, the two sides of the equation must keep equal. Debits record increases in the left family (assets, and also expenses and drawings). "
            "Credits record increases in the right family (liabilities, capital, income). That is why total debits always equal total credits. It is the equation wearing a T-shirt."
        )
        + format_box(
            "The T-account",
            "<p>Every account is written as a T:</p>"
            + t_account(
                "Name of the account",
                [("Left side = DEBIT (Dr)", "…"), ("All debit amounts sit here", "…")],
                [("Right side = CREDIT (Cr)", "…"), ("All credit amounts sit here", "…")],
            )
            + "<p>The difference between the two sides is the <strong>balance</strong>. If debits are bigger, it is a debit balance. If credits are bigger, it is a credit balance. Assets normally have debit balances. Liabilities and capital normally have credit balances.</p>"
        )
        + p("Watch Cash take shape across T1, T2, T3. After three transactions the T already looks like a real account:")
        + t_account(
            "Cash",
            [("To Capital (T1)", rupee(100000))],
            [("By Furniture (T2)", rupee(20000)), ("By Bank (T3)", rupee(40000))],
            cr_bal=rupee(40000),
        )
        + p(
            "Debits 1,00,000. Credits 20,000 + 40,000 = 60,000. Balance (debits bigger) = 1,00,000 − 60,000 = "
            + rupee(40000)
            + " debit, which is cash in hand after T3. The words "
            + b("To")
            + " (on the debit) and "
            + b("By")
            + " (on the credit) are traditional labels for the other account involved."
        )
        + example(
            "0.15",
            "Easy",
            "Is “credit” a compliment?",
            p("A student says: “Credit Cash because cash coming in is a good thing.”")
            + p(b("Answer. ")
              + "No. Cash coming in is an increase in an asset, so it is a "
              + b("debit")
              + " to Cash. “Credit” here is the right-hand column, not a compliment. This single superstition — cash in = credit — produces the most common journal error in first-year scripts."),
        )
        + identify(
            "If the question says “what do you mean by debit and credit”, write: debit = left, credit = right; they are not good/bad; every account has both sides; the rules in the next section decide which side an increase goes to."
        )
        + mistakes(
            [
                "Thinking debit is bad and credit is good (or the reverse).",
                "Crediting Cash whenever cash is received. Cash received is Debit Cash.",
                "Using the bank SMS language (“amount credited”) as if it were the shop’s books.",
            ]
        )
        + memory(
            "Dr is the door on the left. Cr is the corridor on the right. Good and bad have left the building."
        )
    )


def _modern_rules() -> str:
    return (
        h2("16. Modern rules of debit and credit (best for MBA)", "modern-rules")
        + definition(
            "The modern (equation) rules follow the five families. Increase an asset or an expense: debit. Increase a liability, capital or income: credit. Reverse the side for a decrease."
        )
        + simple(
            "Look at the equation A = L + C. Left family grows on the left (debit). Right family grows on the right (credit). Expenses and drawings behave like negative capital, so they grow on the debit. Income behaves like positive capital, so it grows on the credit."
        )
        + why(
            "MBA papers and every computerised system (Tally, Zoho, SAP) use this. If you remember five lines you can journal any transaction without first asking “is this personal, real or nominal?”. Learn these first. Keep the golden rules as a second language."
        )
        + real_life(
            "T6: rent paid by cheque. Rent is an expense → increase in expense → debit Rent. Bank is an asset → decrease in asset → credit Bank. You did not need to classify Rent as “nominal” to get this right. You only needed “expense up = debit”."
        )
        + logic(
            "These rules are the equation, itemised. They cannot contradict A = L + C. If a posting made from these rules fails to balance, the classification of the account was wrong, not the rule."
        )
        + table(
            ["Family", "Increase", "Decrease", "Normal balance"],
            [
                [b("Asset"), b("Debit"), "Credit", "Debit"],
                [b("Liability"), b("Credit"), "Debit", "Credit"],
                [b("Capital"), b("Credit"), "Debit", "Credit"],
                [b("Expense"), b("Debit"), "Credit", "Debit"],
                [b("Income / Revenue"), b("Credit"), "Debit", "Credit"],
                ["Drawings (contra-capital)", "Debit (drawings up = capital down)", "Credit", "Debit"],
            ],
            caption="Modern rules — five families plus drawings",
        )
        + format_box(
            "The five lines to memorise",
            ul(
                [
                    b("Increase in Asset = Debit") + "; Decrease in Asset = Credit.",
                    b("Increase in Liability = Credit") + "; Decrease in Liability = Debit.",
                    b("Increase in Capital = Credit") + "; Decrease in Capital (drawings, loss) = Debit.",
                    b("Increase in Expense = Debit") + "; Decrease in Expense = Credit.",
                    b("Increase in Income = Credit") + "; Decrease in Income = Debit.",
                ]
            ),
        )
        + memory(
            b("DEAD CLIC")
            + " — Debit: Expenses, Assets, Drawings. Credit: Liabilities, Income, Capital. "
            "To increase the account, use its DEAD-or-CLIC side. To decrease it, use the other side."
        )
        + steps(
            [
                "Read the transaction in plain English (ignore debit/credit for ten seconds).",
                "Name two (or more) accounts.",
                "Put each account in a family: Asset, Liability, Capital, Expense, Income (or Drawings).",
                "Say increase or decrease for each.",
                "Apply the table: asset/expense/drawings up → debit; liability/capital/income up → credit.",
                "Check: at least one debit and one credit, and the rupees match.",
            ],
            title="7. How to journal any transaction with modern rules",
        )
        + example(
            "0.16",
            "Easy",
            "Apply DEAD CLIC",
            p("Paid salary " + rupee(8000) + " cash.")
            + p("Salary = expense, increase → Debit Salary. Cash = asset, decrease → Credit Cash.")
            + journal(
                [
                    {
                        "date": "—",
                        "debit": "Salary A/c",
                        "credit": "Cash A/c",
                        "amount": rupee(8000),
                        "narration": "Being salary paid in cash",
                    }
                ],
                caption="Salary paid",
            ),
        )
        + example(
            "0.17",
            "Moderate",
            "A decrease in a liability",
            p("Paid Aman " + rupee(12000) + " by cheque (our T9).")
            + p(
                "Aman = liability, decrease → Debit Aman. Bank = asset, decrease → Credit Bank. Two decreases, still one debit and one credit, still in balance, both sides of the equation fall by "
                + rupee(12000)
                + "."
            ),
        )
        + example(
            "0.18",
            "Exam-level",
            "Four accounts in one story",
            p(
                "Rahul sells goods costing "
                + rupee(4000)
                + " to a customer for "
                + rupee(6000)
                + " on credit, and the customer pays "
                + rupee(2500)
                + " immediately in cash, balance later."
            )
            + p(
                b("Accounts. ")
                + "Cash (asset ↑ "
                + rupee(2500)
                + ") Debit. Debtors (asset ↑ "
                + rupee(3500)
                + ") Debit. Stock (asset ↓ "
                + rupee(4000)
                + ") Credit. Sales/profit (income ↑ "
                + rupee(2000)
                + ") Credit."
            )
            + p(
                "Debits 2,500 + 3,500 = 6,000. Credits: stock 4,000 + profit 2,000 = 6,000. Or, in Chapter-1 style: Debit Cash 2,500, Debit Debtors 3,500, Credit Sales 6,000; and take stock down by cost 4,000."
            )
            + p("Equation: assets net +2,500 +3,500 −4,000 = +2,000; capital +2,000. Holds."),
        )
        + identify(
            "If the question says “rules of debit and credit” in an MBA / management accounting paper, write the five modern lines first, with DEAD CLIC. Add a one-line example for each family. Give golden rules only if marks remain or the question says “traditional”."
        )
        + mistakes(
            [
                "Debiting a liability when it increases (taking a loan and debiting Bank loan). Loan increase = credit.",
                "Crediting an expense when it increases (crediting Rent because “we paid, so credit”). Expense increase = debit.",
                "Using DEAD CLIC on the decrease side without flipping. DEAD CLIC is the increase side.",
            ]
        )
    )


def _golden_rules() -> str:
    return (
        h2("17. Traditional golden rules (personal, real, nominal)", "golden-rules")
        + definition(
            "The traditional Indian rules first classify every account as <strong>personal</strong>, <strong>real</strong> or <strong>nominal</strong>, and then apply one sentence per class. They give the same debit and credit as the modern rules. They are still asked in many B.Com and MBA theory papers."
        )
        + simple(
            "Three families of names. Personal = people and institutions (including the owner, the bank, Aman, outstanding rent). Real = things (cash, stock, furniture, goodwill). Nominal = incomes and expenses (sales, rent, salary). One sentence each, and you can journal."
        )
        + why(
            "Older examiners and many Indian textbooks still open with these. If a 5-mark question says “golden rules of accounting”, this is the answer they have in the scheme. Learn them. Use modern rules to think; use golden rules to write the theory."
        )
        + real_life(
            "T9, paying Aman. Aman is a person → personal account. He is receiving money → “debit the receiver” → Debit Aman. Bank is also personal (the bank as an artificial person) and is giving money → “credit the giver” → Credit Bank. Same entry as the modern rule produced."
        )
        + logic(
            "Personal accounts track who. Real accounts track what thing. Nominal accounts track why capital changed this year (incomes and expenses). The three sentences are just DEAD CLIC in older clothes."
        )
        + table(
            ["Class of account", "Golden rule", "Matches modern rule"],
            [
                [
                    b("Personal"),
                    b("Debit the receiver, Credit the giver"),
                    "People we owe more to → credit (liability ↑). People who owe us more → debit (asset ↑).",
                ],
                [
                    b("Real"),
                    b("Debit what comes in, Credit what goes out"),
                    "Thing comes in = asset ↑ = debit. Thing goes out = asset ↓ = credit.",
                ],
                [
                    b("Nominal"),
                    b("Debit all expenses and losses, Credit all incomes and gains"),
                    "Expense ↑ = debit. Income ↑ = credit.",
                ],
            ],
            caption="Three golden rules — textbook wording, use this in the exam",
        )
        + h3("How to classify an account — with many examples")
        + h4("1. Personal accounts — people, firms, institutions")
        + table(
            ["Kind", "Meaning", "Examples"],
            [
                [
                    b("Natural personal"),
                    "A living person.",
                    "Aman (creditor), Ramesh (debtor), Rahul’s Capital, Drawings, any customer’s name, any supplier’s name.",
                ],
                [
                    b("Artificial personal"),
                    "A body that the law treats as a person.",
                    "Bank A/c, State Bank of India, XYZ Pvt Ltd, a municipal corporation, a club, the Government, GST payable.",
                ],
                [
                    b("Representative personal"),
                    "An account that stands in for a person (usually unpaid or prepaid).",
                    "Outstanding rent (stands for the landlord), Prepaid insurance (stands for the insurer), Accrued commission, Unearned rent, Outstanding salary.",
                ],
            ],
            caption="Personal accounts — three sub-kinds, this is an exam favourite",
        )
        + h4("2. Real accounts — things owned")
        + table(
            ["Kind", "Meaning", "Examples"],
            [
                [
                    b("Tangible real"),
                    "Things you can touch.",
                    "Cash, Stock, Furniture, Machinery, Building, Vehicle, Land, Computer, Fixtures.",
                ],
                [
                    b("Intangible real"),
                    "Things you cannot touch but the shop owns.",
                    "Goodwill, Patents, Trade marks, Copyrights, Computer software (in many papers).",
                ],
            ],
            caption="Real accounts — debit what comes in, credit what goes out",
        )
        + h4("3. Nominal accounts — incomes, expenses, gains, losses")
        + table(
            ["Kind", "Examples (debit these — expenses/losses)", "Examples (credit these — incomes/gains)"],
            [
                [
                    "Trading items",
                    "Purchases, Wages, Carriage inwards, Freight, Import duty.",
                    "Sales, Closing stock (when credited in trading a/c).",
                ],
                [
                    "Operating expenses / incomes",
                    "Rent, Salary, Electricity, Telephone, Advertising, Insurance expired, Depreciation, Discount allowed, Bad debts, Interest paid, Commission paid.",
                    "Commission received, Interest received, Rent received, Discount received.",
                ],
                [
                    "Gains and losses",
                    "Loss on sale of furniture, Loss by fire, Loss by theft.",
                    "Profit on sale of furniture, Bad debts recovered.",
                ],
            ],
            caption="Nominal accounts — the profit-and-loss family",
        )
        + warn(
            "Bank A/c is personal (artificial person), not real. Cash A/c is real. Students mix these. Cash in hand = real. Cash at bank = personal. Both are assets. Both increase with a debit. The class differs; the modern rule does not."
        )
        + two_col(
            box(
                "format",
                "T4 through golden rules",
                "<p>Purchases of stock from Aman "
                + rupee(30000)
                + ".</p>"
                + ul(
                    [
                        "Purchases = nominal (expense of goods) → debit all expenses → <strong>Debit Purchases</strong>.",
                        "Aman = personal → he is the giver of goods → credit the giver → <strong>Credit Aman</strong>.",
                    ]
                ),
            ),
            box(
                "format",
                "T2 through golden rules",
                "<p>Furniture bought for cash "
                + rupee(20000)
                + ".</p>"
                + ul(
                    [
                        "Furniture = real → what comes in → <strong>Debit Furniture</strong>.",
                        "Cash = real → what goes out → <strong>Credit Cash</strong>.",
                    ]
                ),
            ),
        )
        + example(
            "0.19",
            "Moderate",
            "Classify, then journal",
            p("Outstanding rent " + rupee(5000) + " at year end (rent of the shop not yet paid).")
            + p(
                b("Classify. ")
                + "Rent = nominal (expense) → debit Rent. Outstanding rent = representative personal (stands for the landlord) → the landlord is a giver of the service we have used → credit Outstanding rent."
            )
            + journal(
                [
                    {
                        "date": "Year end",
                        "debit": "Rent A/c",
                        "credit": "Outstanding rent A/c",
                        "amount": rupee(5000),
                        "narration": "Being rent of the period still unpaid",
                    }
                ],
                caption="Outstanding rent",
            )
            + p("Modern view of the same: expense up = debit; liability up = credit. Same entry."),
        )
        + example(
            "0.20",
            "Exam-level",
            "Prepaid insurance",
            p(
                "Rahul pays "
                + rupee(12000)
                + " insurance for 12 months on 1 October. Year end is 31 March. Six months are unused."
            )
            + p(
                "Unused 6/12 × 12,000 = 6,000. Prepaid insurance is a representative personal account (the insurer still owes six months of cover) and also a current asset."
            )
            + p(
                "At year end: Debit Prepaid insurance "
                + rupee(6000)
                + ", Credit Insurance "
                + rupee(6000)
                + " (reducing the expense to the six months that belong to this year). Golden rule: prepaid = personal → debit the receiver (the prepaid account stands for the insurer who has taken money and still must provide cover). Insurance = nominal → credit it because we are reducing an expense."
            )
            + p("Modern: asset up = debit Prepaid; expense down = credit Insurance."),
        )
        + identify(
            "If the question says “golden rules / traditional rules / personal real nominal”, write the three sentences exactly: Debit the receiver, Credit the giver. Debit what comes in, Credit what goes out. Debit all expenses and losses, Credit all incomes and gains. Then classify 4–6 accounts as a working. Mention the three kinds of personal account if marks are 5 or more."
        )
        + mistakes(
            [
                "Calling Bank a real account. Bank is personal (artificial).",
                "Calling Capital a nominal account. Capital is personal (the owner).",
                "Calling Drawings a nominal (expense) account. Drawings is personal (the owner receiving).",
                "Calling Outstanding rent a nominal account. It is representative personal — a liability.",
                "Calling Goodwill a nominal account. Goodwill is real (intangible asset).",
                "Calling Purchases a real account. Purchases is nominal. Stock/Inventory is real.",
            ]
        )
        + memory(
            "PNG: Personal — people. Real — things. Nominal — names of incomes and expenses (nominal = “in name”, the profit names). "
            "Personal: receiver Dr, giver Cr. Real: in Dr, out Cr. Nominal: expenses Dr, incomes Cr."
        )
        + exam_answer(
            "The traditional golden rules of accounting depend on the class of the account. "
            "(1) Personal accounts (natural, artificial, representative): Debit the receiver, Credit the giver. "
            "(2) Real accounts (tangible and intangible): Debit what comes in, Credit what goes out. "
            "(3) Nominal accounts (expenses, losses, incomes, gains): Debit all expenses and losses, Credit all incomes and gains. "
            "Illustration: goods purchased on credit from Aman — Purchases is nominal so it is debited (expense); Aman is personal and is the giver so he is credited. "
            "These rules produce the same journals as the modern equation rules."
        )
    )


def _txn_journals() -> str:
    return (
        h2("18. T1–T10 recap: journals, T-accounts, equation effect", "txn-recap")
        + p(
            "You have already seen each of T1–T10 as a full teaching block (what happened, accounts, increase or decrease, debit, credit, journal, equation). "
            "This section is the exam desk-view: one summary table, then the ledger T-accounts that Chapter 1 will call posting, then a proof that the T-accounts produce the same closing figures as the equation."
        )
        + table(
            ["Txn", "What happened", "Accounts", "↑ / ↓", "Debit", "Credit", "Effect on equation"],
            [
                ["T1", "Started with cash " + rupee(100000), "Cash ; Capital", "A ↑ C ↑", "Cash", "Capital", "Both sides +1,00,000"],
                ["T2", "Furniture " + rupee(20000) + " cash", "Furniture ; Cash", "A ↑ A ↓", "Furniture", "Cash", "Totals unchanged"],
                ["T3", "Deposit " + rupee(40000), "Bank ; Cash", "A ↑ A ↓", "Bank", "Cash", "Totals unchanged"],
                ["T4", "Stock " + rupee(30000) + " on credit", "Purchases/Stock ; Aman", "A ↑ L ↑", "Purchases", "Aman", "Both sides +30,000"],
                ["T5", "Sold cost 10,000 for 15,000 cash", "Cash ; Stock ; Sales", "A ↑ A ↓ C ↑", "Cash 15,000 and COGS 10,000", "Sales 15,000 and Stock 10,000", "Both sides +5,000 profit"],
                ["T6", "Rent " + rupee(5000) + " cheque", "Rent ; Bank", "E ↑ A ↓ (C ↓)", "Rent", "Bank", "Both sides −5,000"],
                ["T7", "Commission " + rupee(2000) + " cash", "Cash ; Commission", "A ↑ I ↑ (C ↑)", "Cash", "Commission", "Both sides +2,000"],
                ["T8", "Drawings " + rupee(4000) + " cash", "Drawings ; Cash", "D ↑ A ↓ (C ↓)", "Drawings", "Cash", "Both sides −4,000"],
                ["T9", "Paid Aman " + rupee(12000) + " cheque", "Aman ; Bank", "L ↓ A ↓", "Aman", "Bank", "Both sides −12,000"],
                ["T10", "Loan " + rupee(50000) + " to bank", "Bank ; Bank loan", "A ↑ L ↑", "Bank", "Bank loan", "Both sides +50,000"],
            ],
            caption="One-page recap of all ten transactions",
        )
        + h3("Ledger T-accounts after T10")
        + p(
            "Posting means taking each journal line to the T of that account. Debit journal line → left of the T. Credit journal line → right of the T. "
            "Balance c/d is written on the <strong>smaller</strong> side so the two sides of the T equal: an asset (debit balance) shows Balance c/d on the credit; a liability or capital (credit balance) shows Balance c/d on the debit. We now post every line of T1–T10. Arithmetic of each balance is shown."
        )
        + two_col(
            t_account(
                "Cash",
                [
                    ("To Capital (T1)", rupee(100000)),
                    ("To Sales (T5)", rupee(15000)),
                    ("To Commission (T7)", rupee(2000)),
                ],
                [
                    ("By Furniture (T2)", rupee(20000)),
                    ("By Bank (T3)", rupee(40000)),
                    ("By Drawings (T8)", rupee(4000)),
                ],
                cr_bal=rupee(53000),
            ),
            t_account(
                "Bank",
                [
                    ("To Cash (T3)", rupee(40000)),
                    ("To Bank loan (T10)", rupee(50000)),
                ],
                [
                    ("By Rent (T6)", rupee(5000)),
                    ("By Aman (T9)", rupee(12000)),
                ],
                cr_bal=rupee(73000),
            ),
        )
        + p(
            b("Cash working. ")
            + "Debits: 1,00,000 + 15,000 + 2,000 = 1,17,000. Credits: 20,000 + 40,000 + 4,000 = 64,000. "
            "Balance 1,17,000 − 64,000 = "
            + rupee(53000)
            + " debit."
        )
        + p(
            b("Bank working. ")
            + "Debits: 40,000 + 50,000 = 90,000. Credits: 5,000 + 12,000 = 17,000. "
            "Balance 90,000 − 17,000 = "
            + rupee(73000)
            + " debit."
        )
        + two_col(
            t_account(
                "Furniture",
                [("To Cash (T2)", rupee(20000))],
                [],
                cr_bal=rupee(20000),
            ),
            t_account(
                "Stock",
                [("To Purchases / Aman (T4)", rupee(30000))],
                [("By Cost of sales (T5)", rupee(10000))],
                cr_bal=rupee(20000),
            ),
        )
        + two_col(
            t_account(
                "Aman (Creditor)",
                [("To Bank (T9)", rupee(12000))],
                [("By Purchases (T4)", rupee(30000))],
                dr_bal=rupee(18000),
            ),
            t_account(
                "Bank loan",
                [],
                [("By Bank (T10)", rupee(50000))],
                dr_bal=rupee(50000),
            ),
        )
        + p(
            b("Aman working. ")
            + "Credit 30,000 − Debit 12,000 = "
            + rupee(18000)
            + " credit balance (we still owe him). "
            + b("Bank loan working. ")
            + "Credit "
            + rupee(50000)
            + ", no debit yet, credit balance "
            + rupee(50000)
            + "."
        )
        + two_col(
            t_account(
                "Capital (introduced)",
                [],
                [("By Cash (T1)", rupee(100000))],
                dr_bal=rupee(100000),
            ),
            t_account(
                "Drawings",
                [("To Cash (T8)", rupee(4000))],
                [],
                cr_bal=rupee(4000),
            ),
        )
        + two_col(
            t_account(
                "Sales",
                [],
                [("By Cash (T5)", rupee(15000))],
                dr_bal=rupee(15000),
            ),
            t_account(
                "Commission received",
                [],
                [("By Cash (T7)", rupee(2000))],
                dr_bal=rupee(2000),
            ),
        )
        + two_col(
            t_account(
                "Rent",
                [("To Bank (T6)", rupee(5000))],
                [],
                cr_bal=rupee(5000),
            ),
            t_account(
                "Cost of goods sold",
                [("To Stock (T5)", rupee(10000))],
                [],
                cr_bal=rupee(10000),
            ),
        )
        + h3("Closing the nominal accounts into capital")
        + p(
            "Sales "
            + rupee(15000)
            + " + Commission "
            + rupee(2000)
            + " − Cost of goods sold "
            + rupee(10000)
            + " − Rent "
            + rupee(5000)
            + " = profit "
            + rupee(2000)
            + ". Profit is credited to Capital. Drawings "
            + rupee(4000)
            + " is debited to Capital. Capital then shows:"
        )
        + t_account(
            "Capital (after closing profit and drawings)",
            [("To Drawings", rupee(4000))],
            [("By Cash (introduced)", rupee(100000)), ("By Profit (Rev − Exp)", rupee(2000))],
            dr_bal=rupee(98000),
        )
        + p(
            b("Capital working. ")
            + "Credits 1,00,000 + 2,000 = 1,02,000. Debit 4,000. Balance 1,02,000 − 4,000 = "
            + rupee(98000)
            + " credit. Matches the equation table after T10."
        )
        + table(
            ["Account", "Debit balance", "Credit balance"],
            [
                ["Cash", rupee(53000), ""],
                ["Bank", rupee(73000), ""],
                ["Furniture", rupee(20000), ""],
                ["Stock", rupee(20000), ""],
                ["Debtors", rupee(0), ""],
                ["Prepaid", rupee(0), ""],
                ["Aman (Creditors)", "", rupee(18000)],
                ["Bank loan", "", rupee(50000)],
                ["Capital", "", rupee(98000)],
                [b("Totals"), b(rupee(166000)), b(rupee(166000))],
            ],
            caption="A mini trial balance after closing — this is Chapter 1’s destination",
            foot="Debit total 53,000 + 73,000 + 20,000 + 20,000 = 1,66,000. Credit total 18,000 + 50,000 + 98,000 = 1,66,000.",
        )
        + keypoint(
            "Journal → T-accounts (ledger) → list of balances (trial balance) → the list is the equation. Chapter 1 is this pipeline, taught as a craft. This bootcamp is why the pipeline cannot fail if you post both sides."
        )
    )


def _drill() -> str:
    return (
        h2("19. Classification drill — 20 accounts", "drill")
        + p(
            "Cover the last two columns with your hand. Name the type (personal / real / nominal — and the sub-kind if you can), the nature (asset / liability / capital / income / expense / drawings), and which side increases the account. Then check."
        )
        + table(
            ["#", "Account", "Type (golden)", "Nature (modern)", "To increase: Debit or Credit"],
            [
                ["1", "Cash", "Real (tangible)", "Asset (current)", b("Debit")],
                ["2", "Bank", "Personal (artificial)", "Asset (current)", b("Debit")],
                ["3", "Capital", "Personal (natural — the owner)", "Capital", b("Credit")],
                ["4", "Drawings", "Personal (natural — the owner receiving)", "Contra-capital (drawings)", b("Debit")],
                ["5", "Purchases", "Nominal (expense of goods)", "Expense (goods for resale; unsold = stock)", b("Debit")],
                ["6", "Sales", "Nominal (income)", "Income / Revenue", b("Credit")],
                ["7", "Rent", "Nominal (expense)", "Expense", b("Debit")],
                ["8", "Salary", "Nominal (expense)", "Expense", b("Debit")],
                ["9", "Furniture", "Real (tangible)", "Asset (non-current)", b("Debit")],
                ["10", "Machinery", "Real (tangible)", "Asset (non-current)", b("Debit")],
                ["11", "Creditors", "Personal (natural / artificial)", "Liability (current)", b("Credit")],
                ["12", "Debtors", "Personal (natural / artificial)", "Asset (current)", b("Debit")],
                ["13", "Loan", "Personal (the lender)", "Liability (non-current if long-term)", b("Credit")],
                ["14", "Interest received", "Nominal (income)", "Income", b("Credit")],
                ["15", "Interest paid", "Nominal (expense)", "Expense", b("Debit")],
                ["16", "Stock", "Real (tangible)", "Asset (current)", b("Debit")],
                ["17", "Commission (received)", "Nominal (income)", "Income", b("Credit")],
                ["18", "Outstanding rent", "Personal (representative)", "Liability (current)", b("Credit")],
                ["19", "Prepaid insurance", "Personal (representative)", "Asset (current)", b("Debit")],
                ["20", "Goodwill", "Real (intangible)", "Asset (non-current)", b("Debit")],
            ],
            caption="Twenty accounts — type, nature, and the side that increases them",
            foot="Commission with no adjective is treated here as commission received (income), because that is how T7 used it. Commission paid would be nominal / expense / debit to increase.",
        )
        + p(b("Patterns you should now see without thinking:"))
        + ul(
            [
                "Every asset in this list increases with a debit. Every liability and capital increases with a credit.",
                "Every expense (Purchases, Rent, Salary, Interest paid) increases with a debit. Every income (Sales, Interest received, Commission) increases with a credit.",
                "Drawings increases with a debit — it is the owner receiving, and it reduces capital.",
                "Bank is personal; Cash is real; both are assets; both debit to increase. The golden class differs, the modern side does not.",
                "Outstanding … is usually a representative personal liability (credit to increase). Prepaid … is usually a representative personal asset (debit to increase).",
                "Goodwill looks “nominal” because it is a word, but it is a real intangible asset. Debit to increase.",
            ]
        )
        + example(
            "0.21",
            "Easy",
            "Fill three blanks",
            p("Debtors: type? nature? side to increase? Outstanding rent: type? nature? side to increase? Sales: type? nature? side to increase?")
            + p(b("Answer. ")
              + "Debtors — personal, asset, Debit. Outstanding rent — representative personal, liability, Credit. Sales — nominal, income, Credit."),
        )
        + identify(
            "If the question is a classification table (very common for 5–8 marks), use exactly these three columns: Personal/Real/Nominal, Asset/Liability/Capital/Income/Expense, Dr or Cr to increase. Do not leave a cell blank. Bank and Outstanding/Prepaid are the traps."
        )
    )


def _memory_mistakes() -> str:
    return (
        h2("20. Memory tricks and common mistakes", "memory-mistakes")
        + h3("Memory tricks (keep these on a one-page card)")
        + memory(
            b("DEAD CLIC. ")
            + "Debit Expenses, Assets, Drawings. Credit Liabilities, Income, Capital. This is the increase-side. Flip it to decrease."
        )
        + memory(
            b("A = L + C. ")
            + "What we have = who provided it. After every transaction, re-total both sides."
        )
        + memory(
            b("PNG golden. ")
            + "Personal: Debit the receiver, Credit the giver. Real: Debit what comes in, Credit what goes out. Nominal: Debit expenses and losses, Credit incomes and gains."
        )
        + memory(
            b("C-M-E for a transaction. ")
            + "Change in money/value, Measurable in ₹, Evidence. All three, or it stays out."
        )
        + memory(
            b("Two pockets. ")
            + "Rahul ≠ Rahul Stationery. Personal take = Drawings. Shop spend = Expense."
        )
        + memory(
            b("Goods to sell vs goods to use. ")
            + "Pens to sell = Purchases / Stock. A counter to use = Furniture. A photocopier to use = Machinery. Never debit Purchases for a machine."
        )
        + memory(
            b("Received vs paid. ")
            + "Interest received / commission received / rent received = income (credit). Interest paid / commission paid / rent paid = expense (debit)."
        )
        + memory(
            b("Cash coming in is a debit to Cash. ")
            + "Say it out loud. The bank SMS that says “credited” is the bank’s books, not yours."
        )
        + h3("Common mistakes — and the repair")
        + mistakes(
            [
                "<strong>Drawings treated as an expense.</strong> Repair: Drawings reduce capital, not profit. Debit Drawings, not Rent, not Salary, not Miscellaneous. Profit = Revenue − Expenses. Drawings do not sit in that formula.",
                "<strong>Cash received credited to Cash.</strong> Repair: Cash is an asset. Asset up = debit. Credit the reason the cash came (Sales, Capital, Loan, Commission, Debtors). “Credit” is the right column, not a compliment.",
                "<strong>Purchases of goods mixed with furniture / machinery.</strong> Repair: Purchases = goods for resale. Furniture/Machinery = assets to use. T2 is Furniture Dr, Cash Cr. T4 is Purchases Dr, Aman Cr.",
                "<strong>A loan treated as income or as capital.</strong> Repair: A loan is a liability. Bank Dr, Bank loan Cr. It must be repaid. It is not sales and not capital.",
                "<strong>Paying a creditor treated as a new expense.</strong> Repair: The expense/stock was recorded when the goods arrived (T4). T9 only reduces Aman and reduces Bank.",
                "<strong>Stock reduced by selling price.</strong> Repair: Stock leaves at cost. Cash/Debtors enter at selling price. The gap is profit. T5: stock −10,000, cash +15,000, capital +5,000.",
                "<strong>Bank classified as a real account.</strong> Repair: Bank is personal (artificial person). Cash is real. Both debit to increase.",
                "<strong>Outstanding rent classified as nominal.</strong> Repair: Outstanding rent is representative personal, a current liability, credit to increase. The nominal account is Rent (the expense).",
                "<strong>Goodwill classified as nominal.</strong> Repair: Goodwill is a real intangible asset. Debit to increase.",
                "<strong>Capital treated as cash.</strong> Repair: Cash is an asset. Capital is a claim. After T2 they are no longer equal: cash 80,000, capital 1,00,000.",
                "<strong>Waiting for cash before recording a credit purchase or credit sale.</strong> Repair: The invoice date is the transaction date. T4 is a transaction on the day Aman delivers, not on the day we pay.",
                "<strong>Owner’s personal bill recorded as a shop expense.</strong> Repair: Entity concept. Personal electricity, personal trip, personal medical bill = Drawings.",
                "<strong>One-sided posting.</strong> Repair: Dual aspect. If you debit, you must credit. If the equation’s last two columns differ, you missed a side.",
                "<strong>Profit treated as cash.</strong> Repair: Profit is a change in capital. Cash also moves for loans, drawings, furniture, and paying creditors. After T10 profit is 2,000; cash is 53,000. They are different numbers.",
            ]
        )
        + table(
            ["Wrong journal", "Why it is wrong", "Right journal"],
            [
                [
                    "Rent Dr 4,000 / Cash Cr 4,000 when owner takes cash home",
                    "Personal take is not rent",
                    "Drawings Dr 4,000 / Cash Cr 4,000",
                ],
                [
                    "Cash Cr 2,000 / Commission Dr 2,000 when commission is received",
                    "Cash in is Debit Cash; income is Credit",
                    "Cash Dr 2,000 / Commission received Cr 2,000",
                ],
                [
                    "Purchases Dr 20,000 / Cash Cr 20,000 for a wooden counter",
                    "A counter is furniture, not goods for sale",
                    "Furniture Dr 20,000 / Cash Cr 20,000",
                ],
                [
                    "Cash Dr 50,000 / Commission Cr 50,000 for a bank loan",
                    "A loan is not earning",
                    "Bank Dr 50,000 / Bank loan Cr 50,000",
                ],
                [
                    "Purchases Dr 12,000 / Bank Cr 12,000 when paying Aman",
                    "Paying a creditor is not a new purchase",
                    "Aman Dr 12,000 / Bank Cr 12,000",
                ],
            ],
            caption="Five broken journals you will now refuse to write",
        )
        + example(
            "0.22",
            "Exam-level",
            "Find four errors",
            p(
                "A student journals: (i) Started business Cash Cr 1,00,000, Capital Dr 1,00,000. "
                "(ii) Bought furniture Purchases Dr 20,000, Cash Cr 20,000. "
                "(iii) Commission received Commission Dr 2,000, Cash Cr 2,000. "
                "(iv) Drawings Salary Dr 4,000, Cash Cr 4,000."
            )
            + p(b("Repair. "))
            + ol(
                [
                    "Cash is an asset increasing → Debit Cash, Credit Capital.",
                    "Furniture is an asset, not purchases → Debit Furniture, Credit Cash.",
                    "Cash in = Debit Cash. Commission is income → Credit Commission received.",
                    "Owner taking cash is Drawings, not Salary → Debit Drawings, Credit Cash.",
                ]
            ),
        )
    )


def _exam() -> str:
    ans = (
        "<p><strong>Meaning.</strong> The accounting equation is <strong>Assets = Liabilities + Capital</strong>. "
        "It is the dual-aspect idea written as algebra. Every transaction has two sides, so the two sides of the equation remain equal after every event.</p>"
        "<p><strong>Assets</strong> are resources of the business (cash, bank, stock, debtors, furniture, prepaid expenses). "
        "<strong>Liabilities</strong> are amounts owed to outsiders (creditors, bank loan, outstanding expenses). "
        "<strong>Capital</strong> is the owner’s claim on the business. Capital itself moves: "
        "Closing capital = Opening capital + Profit − Drawings, and Profit = Revenue − Expenses. "
        "The expanded form is therefore Assets = Liabilities + Opening capital + Revenue − Expenses − Drawings.</p>"
        "<p><strong>Why it always holds.</strong> Assets are what the firm has. Liabilities and capital are who provided those assets. "
        "There is no third claim, so the two totals cannot differ if both sides of every event have been recorded.</p>"
        "<p><strong>Example — Rahul Stationery (extract).</strong></p>"
        "<p>T1: Rahul starts with cash ₹1,00,000. Assets (cash) ₹1,00,000 = Liabilities ₹0 + Capital ₹1,00,000.</p>"
        "<p>T2: Buys furniture ₹20,000 cash. Cash falls by ₹20,000, furniture rises by ₹20,000. Totals still ₹1,00,000 = ₹0 + ₹1,00,000. One asset replaces another.</p>"
        "<p>T4: Buys stock ₹30,000 on credit from Aman. Stock +₹30,000, Creditors +₹30,000. Assets ₹1,30,000 = Liabilities ₹30,000 + Capital ₹1,00,000.</p>"
        "<p>T5: Sells stock that cost ₹10,000 for ₹15,000 cash. Cash +₹15,000, Stock −₹10,000 (assets net +₹5,000); profit ₹5,000 increases capital. Assets ₹1,35,000 = Liabilities ₹30,000 + Capital ₹1,05,000.</p>"
        "<p>After ten such transactions the books of Rahul Stationery show: Cash ₹53,000 + Bank ₹73,000 + Furniture ₹20,000 + Stock ₹20,000 = <strong>Assets ₹1,66,000</strong>. "
        "Creditors ₹18,000 + Bank loan ₹50,000 = Liabilities ₹68,000. Opening capital ₹1,00,000 + profit ₹2,000 − drawings ₹4,000 = Capital ₹98,000. "
        "Liabilities + Capital = ₹68,000 + ₹98,000 = <strong>₹1,66,000</strong>. The equation balances, and that equality is the proof asked for in the examination.</p>"
        "<p><strong>Conclusion.</strong> The accounting equation is both a definition of financial position and a check on recording. "
        "A balance sheet is this equation presented as a statement on a given date. If the two sides ever differ, a transaction has been posted on only one side or an amount has been misstated.</p>"
    )
    return (
        h2("21. Exam-ready 5-mark answer", "exam-5mark")
        + qna(
            "Explain the accounting equation with an example.",
            ans,
            marks="5 marks",
        )
        + exam_answer(
            "Write four blocks: (1) statement of A = L + C and dual aspect, (2) one sentence each on assets, liabilities, capital, and the expanded form with profit and drawings, "
            "(3) a short numerical example with at least three transactions and a total that matches, (4) a one-line conclusion that a balance sheet is the equation on a date. "
            "Do not skip the arithmetic. Examiners award method marks on the numbers."
        )
        + exam_tip(
            "If the paper gives you a list of transactions and says “show the accounting equation”, draw a running table with a column per account plus Total Assets and L+C, one row per transaction, and tick every row. That is exactly the T1–T10 table in this bootcamp. You will not lose a mark for layout if every row adds up."
        )
        + h3("Other 2–5 mark questions this bootcamp has already written for you")
        + table(
            ["Question", "Where the answer lives", "Marks it usually carries"],
            [
                ["Define accounting. Is it a process?", "Section 1 — seven verbs, exam-ready paragraph", "3–5"],
                ["Why do firms keep books?", "Section 2 — MP-TB-CD six reasons", "5"],
                ["Bookkeeping vs accounting", "Section 3 — two-column distinguish", "4–5"],
                ["Business entity concept", "Section 4 — exam-ready paragraph", "3–5"],
                ["What is a transaction? Give examples of what is not.", "Section 5 — three tests + table", "4–5"],
                ["Assets, with current vs non-current", "Section 7", "5"],
                ["Liabilities, with current vs non-current", "Section 8", "4–5"],
                ["What are drawings? Are they an expense?", "Section 13 — exam-ready paragraph", "3–5"],
                ["Modern rules of debit and credit", "Section 16 — five lines + DEAD CLIC", "5"],
                ["Golden rules of accounting", "Section 17 — exam-ready paragraph", "5"],
                ["Classify: Bank, Outstanding rent, Goodwill, Drawings, Purchases", "Section 19 drill", "5"],
            ],
            caption="Theory map — do not hunt through a textbook the night before",
        )
    )


def _bridge() -> str:
    return (
        h2("22. How this bootcamp connects to Chapter 1", "bridge-ch1")
        + connect(
            "Chapter 1 is Journal → Ledger → Trial Balance. This bootcamp is why those three tools exist and what they are for. "
            "You already did all three, quietly, on Rahul’s ten transactions. Chapter 1 teaches the craft: dates, narration, folio numbers, balancing accounts, and the trial-balance listing."
        )
        + table(
            ["Bootcamp idea you now own", "Chapter 1 name for the same idea", "What will be new in Chapter 1"],
            [
                [
                    "Write the two sides of a transaction with Dr and Cr",
                    b("Journal"),
                    "Date column, L.F. column, narration in brackets, compound entries, GST, and the rule “debit is written first”.",
                ],
                [
                    "The T-shape with left and right",
                    b("Ledger (posting)"),
                    "A separate page (or folio) per account, “To” and “By”, balancing c/d and b/d, and the ledger as a book of accounts.",
                ],
                [
                    "The list of debit and credit balances that totals "
                    + rupee(166000)
                    + " on both sides",
                    b("Trial balance"),
                    "A formal two-column list of every account, used as a check before preparing statements. If it does not tally, an error is hiding.",
                ],
                [
                    "A = L + C, and the mini balance sheet",
                    "The destination of the trial balance",
                    "Chapter 1 stops at the trial balance. Later chapters open it into a Trading A/c, Profit and Loss A/c, and a Schedule-III balance sheet.",
                ],
                [
                    "Purchases vs Furniture, Drawings vs Expense, Loan vs Income",
                    "Account-name discipline in the journal",
                    "More names: carriage, discount allowed/received, bad debts, depreciation. Same five families.",
                ],
            ],
            caption="Nothing in Chapter 1 is a new universe — it is this bootcamp, written as a procedure",
        )
        + steps(
            [
                "A transaction happens (bootcamp: three tests).",
                "You journal it (bootcamp: modern or golden rules; Chapter 1: the journal paper format).",
                "You post each line to a T-account / ledger folio (bootcamp section 18; Chapter 1: posting rules).",
                "You list every balance — debits in one column, credits in the other — and they must match (bootcamp mini trial balance; Chapter 1: trial balance).",
                "If they match, the equation is intact and you may go on to profit and the balance sheet. If they do not, you hunt the missing side before you go on.",
            ],
            title="7. The one pipeline you will live in for the rest of the subject",
        )
        + keypoint(
            "Before you open Chapter 1, you should be able to take any one-line transaction — “paid electricity ₹900 by UPI”, “sold goods costing ₹3,000 for ₹4,200 on credit”, “owner took goods ₹700” — and say: accounts, increase or decrease, debit, credit, effect on A = L + C. If you can, the journal paper in Chapter 1 is only stationery. If you cannot, go back to T1–T10 and walk them once more, out loud."
        )
        + identify(
            "If a Chapter 1 question gives you a list of transactions and says “journalise, post, and prepare a trial balance”, you are being asked to run the pipeline above. Name the accounts with bootcamp discipline first, then worry about the ruling of the journal paper. Most errors in Chapter 1 are classification errors from this bootcamp, not ruling errors."
        )
        + p(
            "Rahul’s shop is still open. The furniture is in the lane, Aman is still owed "
            + rupee(18000)
            + ", the bank loan sits in the account, and capital is "
            + rupee(98000)
            + ". Chapter 1 will put the same ten facts on journal paper, ledger paper, and a trial balance. You already know what the numbers must be. That is the point of a bootcamp."
        )
    )


if __name__ == "__main__":
    html = body()
    assert "1,66,000" in html
    assert "1,00,000" in html
    assert EQ[-1][1] + EQ[-1][2] + EQ[-1][3] + EQ[-1][4] == 166000
    print("ch00_bootcamp: ok, html length", len(html))
