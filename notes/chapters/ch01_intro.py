#!/usr/bin/env python3
"""Chapter 01 — Introduction to Accounting (concepts → journal → ledger → trial balance)."""

import sys
from collections import defaultdict

sys.path.insert(0, "/workspace/notes")
from html_lib import *


# ---------------------------------------------------------------------------
# Continuous illustration — Meera Traders (Meera's Stationery), April 2025
# All later figures (journals, ledgers, trial balance) are built from TXNS
# so the arithmetic cannot drift.
# ---------------------------------------------------------------------------

TXNS = [
    {
        "date": "1 Apr 2025",
        "short": "1 Apr",
        "debit": "Cash A/c",
        "credit": "Capital A/c",
        "amt_n": 200000,
        "narration": "Being cash introduced by Meera as capital to start Meera Traders.",
        "why": "Cash (real/asset) comes into the business → Debit. The owner is the giver of that cash, so Capital (personal) → Credit.",
        "story": "Meera opens her stationery shop with her own savings of ₹2,00,000 in cash.",
    },
    {
        "date": "2 Apr 2025",
        "short": "2 Apr",
        "debit": "Bank A/c",
        "credit": "Cash A/c",
        "amt_n": 150000,
        "narration": "Being cash deposited into a newly opened bank account.",
        "why": "The bank (personal — the banker) receives money → Debit Bank. Cash (real) goes out of the till → Credit Cash.",
        "story": "She opens a current account and puts most of the cash in the bank, keeping some for the till.",
    },
    {
        "date": "3 Apr 2025",
        "short": "3 Apr",
        "debit": "Furniture A/c",
        "credit": "Cash A/c",
        "amt_n": 25000,
        "narration": "Being furniture purchased for cash for the shop.",
        "why": "Furniture (real/asset) comes in → Debit. Cash goes out → Credit.",
        "story": "Shelves, a counter and two chairs are bought and paid in cash.",
    },
    {
        "date": "4 Apr 2025",
        "short": "4 Apr",
        "debit": "Purchases A/c",
        "credit": "Cash A/c",
        "amt_n": 20000,
        "narration": "Being goods (stationery) purchased for cash.",
        "why": "Purchases is a nominal account (expense / cost of goods) → Debit all expenses. Cash goes out → Credit.",
        "story": "First stock of notebooks, pens and files is bought and paid in cash.",
    },
    {
        "date": "5 Apr 2025",
        "short": "5 Apr",
        "debit": "Purchases A/c",
        "credit": "Kabir A/c",
        "amt_n": 40000,
        "narration": "Being goods purchased on credit from Kabir.",
        "why": "Goods bought → Debit Purchases. Kabir (personal) is the giver of goods on credit → Credit Kabir (creditor / liability).",
        "story": "A bigger order is taken from wholesaler Kabir, to be paid later.",
    },
    {
        "date": "6 Apr 2025",
        "short": "6 Apr",
        "debit": "Cash A/c",
        "credit": "Sales A/c",
        "amt_n": 18000,
        "narration": "Being goods sold for cash.",
        "why": "Cash comes in → Debit Cash. Sales is a nominal income → Credit all incomes and gains.",
        "story": "Walk-in customers buy stationery and pay cash.",
    },
    {
        "date": "8 Apr 2025",
        "short": "8 Apr",
        "debit": "Sana A/c",
        "credit": "Sales A/c",
        "amt_n": 22000,
        "narration": "Being goods sold on credit to Sana.",
        "why": "Sana (personal) is the receiver of goods → Debit Sana (debtor / asset). Sales earned → Credit Sales. Cash has not moved, and that is fine under accrual.",
        "story": "A nearby tuition centre, Sana, takes a bulk order and will pay later.",
    },
    {
        "date": "10 Apr 2025",
        "short": "10 Apr",
        "debit": "Rent A/c",
        "credit": "Bank A/c",
        "amt_n": 8000,
        "narration": "Being shop rent for April paid by cheque.",
        "why": "Rent is a nominal expense → Debit. Bank is the giver → Credit Bank.",
        "story": "Monthly shop rent is paid from the bank account, not from the till.",
    },
    {
        "date": "12 Apr 2025",
        "short": "12 Apr",
        "debit": "Kabir A/c",
        "credit": "Bank A/c",
        "amt_n": 15000,
        "narration": "Being part payment made to Kabir by cheque.",
        "why": "Kabir (personal) is the receiver of money → Debit Kabir (liability falls). Bank is the giver → Credit Bank.",
        "story": "Meera pays Kabir part of what she owes, by cheque.",
    },
    {
        "date": "15 Apr 2025",
        "short": "15 Apr",
        "debit": "Cash A/c",
        "credit": "Sana A/c",
        "amt_n": 10000,
        "narration": "Being cash received from Sana against credit sales.",
        "why": "Cash comes in → Debit Cash. Sana is the giver of cash → Credit Sana (asset / debtor falls).",
        "story": "Sana pays ₹10,000 towards her bill. The rest is still receivable.",
    },
    {
        "date": "18 Apr 2025",
        "short": "18 Apr",
        "debit": "Wages A/c",
        "credit": "Cash A/c",
        "amt_n": 4000,
        "narration": "Being wages paid in cash to the shop helper.",
        "why": "Wages is a nominal expense → Debit. Cash goes out → Credit.",
        "story": "A helper is paid wages in cash from the till.",
    },
    {
        "date": "20 Apr 2025",
        "short": "20 Apr",
        "debit": "Drawings A/c",
        "credit": "Cash A/c",
        "amt_n": 5000,
        "narration": "Being cash withdrawn by the proprietor for personal use.",
        "why": "Meera (the owner) is the receiver of cash → Debit Drawings (personal). Cash goes out → Credit. This is NOT an expense of the shop.",
        "story": "Meera takes ₹5,000 from the till for household expenses.",
    },
    {
        "date": "22 Apr 2025",
        "short": "22 Apr",
        "debit": "Electricity A/c",
        "credit": "Outstanding Electricity A/c",
        "amt_n": 2000,
        "narration": "Being electricity charges for April remaining unpaid (outstanding).",
        "why": "Expense has been incurred this period → Debit Electricity (accrual + matching). The unpaid amount is a liability → Credit Outstanding Electricity (representative personal).",
        "story": "The electricity bill for April has arrived but will be paid in May. We still record it now.",
    },
    {
        "date": "25 Apr 2025",
        "short": "25 Apr",
        "debit": "Cash A/c",
        "credit": "Commission A/c",
        "amt_n": 3000,
        "narration": "Being commission received in cash.",
        "why": "Cash comes in → Debit Cash. Commission is a nominal income → Credit.",
        "story": "A publisher pays Meera a small display commission in cash.",
    },
    {
        "date": "28 Apr 2025",
        "short": "28 Apr",
        "debit": "Purchases A/c",
        "credit": "Kabir A/c",
        "amt_n": 10000,
        "narration": "Being additional goods purchased on credit from Kabir.",
        "why": "Same rule as 5 Apr: Debit Purchases, Credit Kabir. The creditor's balance rises again.",
        "story": "Fast-moving pens are reordered from Kabir on credit.",
    },
]


LEDGER_ORDER = [
    "Cash A/c",
    "Bank A/c",
    "Capital A/c",
    "Furniture A/c",
    "Purchases A/c",
    "Sales A/c",
    "Kabir A/c",
    "Sana A/c",
    "Rent A/c",
    "Wages A/c",
    "Drawings A/c",
    "Electricity A/c",
    "Outstanding Electricity A/c",
    "Commission A/c",
]


def inr(n: int) -> str:
    """Indian-grouped digits without the rupee sign (for journal / T-account cells)."""
    return rupee(n).replace("₹", "").replace("−", "-")


def short_name(acc: str) -> str:
    return acc.replace(" A/c", "")


def exam_ready(*paragraphs: str) -> str:
    body = "".join(f"<p>{para}</p>" for para in paragraphs)
    return box("exam", "12. Exam-ready answer (3–5 marks — write this)", body)


def exam_ready_list(intro: str, points: list, outro: str = "") -> str:
    body = f"<p>{intro}</p>" + ul(points)
    if outro:
        body += f"<p>{outro}</p>"
    return box("exam", "12. Exam-ready answer (3–5 marks — write this)", body)


def concept_block(
    title: str,
    definition_t: str,
    simple_t: str,
    why_t: str,
    life_t: str,
    ignored_t: str,
    exam_intro: str,
    exam_points: list,
    exam_outro: str = "",
    extra: str = "",
) -> str:
    parts = [
        h3(title),
        definition(definition_t),
        simple(simple_t),
        why(why_t),
        real_life(life_t),
        warn("<strong>What would go wrong if we ignored it.</strong> " + ignored_t),
        exam_ready_list(exam_intro, exam_points, exam_outro),
    ]
    if extra:
        parts.append(extra)
    return "".join(parts)


def build_books():
    """Post every journal to T-accounts and return ledgers + trial-balance rows."""
    books = {name: {"dr": [], "cr": []} for name in LEDGER_ORDER}
    for t in TXNS:
        d, c, a, n = t["debit"], t["credit"], t["short"], t["amt_n"]
        books[d]["dr"].append((f"{a}  To {short_name(c)}", inr(n), n))
        books[c]["cr"].append((f"{a}  By {short_name(d)}", inr(n), n))
    tb_dr = []
    tb_cr = []
    rendered = {}
    for name in LEDGER_ORDER:
        dr_e = books[name]["dr"]
        cr_e = books[name]["cr"]
        dr_tot = sum(x[2] for x in dr_e)
        cr_tot = sum(x[2] for x in cr_e)
        dr = [(x[0], x[1]) for x in dr_e]
        cr = [(x[0], x[1]) for x in cr_e]
        if dr_tot > cr_tot:
            bal = dr_tot - cr_tot
            cr.append(("30 Apr  By Balance c/d", inr(bal)))
            total = dr_tot
            nature, bal_amt = "Dr", bal
            tb_dr.append((short_name(name), bal))
        elif cr_tot > dr_tot:
            bal = cr_tot - dr_tot
            dr.append(("30 Apr  To Balance c/d", inr(bal)))
            total = cr_tot
            nature, bal_amt = "Cr", bal
            tb_cr.append((short_name(name), bal))
        else:
            total = dr_tot
            nature, bal_amt = "Nil", 0
        while len(dr) < len(cr):
            dr.append(("", ""))
        while len(cr) < len(dr):
            cr.append(("", ""))
        dr.append(("Total", inr(total)))
        cr.append(("Total", inr(total)))
        note = (
            f"Working: debit total {rupee(dr_tot)} − credit total {rupee(cr_tot)} "
            f"gives a <strong>{nature} balance {rupee(bal_amt)}</strong>. "
            f"Both sides of the account are totalled at {rupee(total)}. "
        )
        if nature == "Dr":
            note += f"On 1 May 2025 this comes down as <em>To Balance b/d {rupee(bal_amt)}</em> on the debit side."
        elif nature == "Cr":
            note += f"On 1 May 2025 this comes down as <em>By Balance b/d {rupee(bal_amt)}</em> on the credit side."
        rendered[name] = {
            "html": t_account(name, dr, cr) + raw_p(note),
            "nature": nature,
            "bal": bal_amt,
            "dr_tot": dr_tot,
            "cr_tot": cr_tot,
            "total": total,
        }
    return rendered, tb_dr, tb_cr


BOOKS, TB_DR, TB_CR = build_books()
TB_DR_TOTAL = sum(x[1] for x in TB_DR)
TB_CR_TOTAL = sum(x[1] for x in TB_CR)
assert TB_DR_TOTAL == TB_CR_TOTAL, (TB_DR_TOTAL, TB_CR_TOTAL)


def body() -> str:
    parts = []
    parts.append(
        chapter_open(
            "01",
            "Introduction to Accounting",
            "You will identify transactions, apply accounting concepts, write journals, "
            "post ledgers, balance accounts, and prepare a trial balance.",
            [
                "Accounting concepts and conventions",
                "Identifying business transactions",
                "Accounting rules",
                "Preparation of Journal",
                "Ledger",
                "Trial Balance",
            ],
        )
    )
    parts.append(_intro())
    parts.append(_section_a())
    parts.append(_section_b())
    parts.append(_section_c())
    parts.append(_section_d())
    parts.append(_section_e())
    parts.append(_section_f())
    parts.append(_section_g())
    parts.append(chapter_close())
    return "".join(parts)


# ===========================================================================
# Opening
# ===========================================================================

def _intro() -> str:
    parts = []
    parts.append(
        lead(
            "This chapter takes you from zero to a complete set of books for one shop. "
            "By the last page you will have written every journal, posted every ledger, "
            "balanced every account, and prepared a trial balance that actually ties. "
            "One business is used throughout, so the same rupees keep moving — you always "
            "know where you are."
        )
    )
    parts.append(h2("Meet Meera Traders — the shop we will keep for the whole chapter", "meera"))
    parts.append(
        p(
            b("Meera"),
            " starts a small stationery shop, ",
            b("Meera Traders"),
            " (also called Meera's Stationery), on ",
            b("1 April 2025"),
            " in Pune. April is the first month of the Indian financial year. "
            "For this chapter we treat ",
            b("April 2025"),
            " as one complete accounting period so that you can see a full cycle — "
            "transaction → journal → ledger → trial balance — without waiting till 31 March 2026. "
            "In real life her first year would run 1 April 2025 to 31 March 2026; the method is identical.",
        )
    )
    parts.append(
        keypoint(
            "We will <strong>not</strong> charge depreciation in this chapter (that is a later chapter) "
            "and we will <strong>not</strong> adjust closing stock. Purchases stay in the trial balance "
            "as an expense-type balance. A Trading Account needs closing stock; that comes when you "
            "prepare final accounts. For Chapter 1, a trial balance of ledger balances without a "
            "stock adjustment is correct and complete."
        )
    )
    parts.append(
        box(
            "life",
            "The story in one paragraph",
            "<p>Meera puts ₹2,00,000 cash into the shop, banks ₹1,50,000, buys furniture, "
            "purchases goods for cash and on credit from Kabir, sells for cash and on credit to Sana, "
            "pays rent by cheque, pays Kabir part of his bill, collects part of Sana's bill, "
            "pays wages, takes cash home (drawings), records unpaid electricity, earns a small "
            "commission, and reorders goods. Every rupee of this story will appear in the journal, "
            "then in the ledgers, then in the trial balance.</p>",
        )
    )
    parts.append(
        p(
            "Before we touch a journal, we need the ",
            b("rules of the game"),
            " — the concepts and conventions. They decide <em>what</em> we record, "
            "<em>when</em> we record it, and <em>at what amount</em>. Skip them and the "
            "journals will look like guesswork.",
        )
    )
    parts.append(
        connect(
            "Keep Meera in your head. Every concept below is illustrated with her shop, "
            "and the same fifteen transactions reappear in the Journal, Ledger and Trial Balance sections. "
            "Do not skip the concepts — examiners ask them as 3–5 mark theory, and they also "
            "decide how you treat outstanding electricity, drawings, and credit sales."
        )
    )
    return "".join(parts)


# ===========================================================================
# A. Concepts and conventions
# ===========================================================================

def _section_a() -> str:
    parts = []
    parts.append(h2("A. Accounting concepts and conventions", "concepts"))
    parts.append(
        definition(
            "Accounting <strong>concepts</strong> are the basic assumptions on which the "
            "whole recording system rests. Accounting <strong>conventions</strong> are the "
            "traditions and practical guidelines that accountants follow while applying those "
            "concepts. Together they make books of different businesses comparable, honest and useful."
        )
    )
    parts.append(
        simple(
            "Think of concepts as the constitution (the assumptions we agree to before we start) "
            "and conventions as the courtroom customs (how we behave when a judgement call appears). "
            "You cannot start Meera's books without the entity concept and dual aspect. "
            "You need conservatism when you are not sure whether to show a possible profit."
        )
    )
    parts.append(
        why(
            "Without a shared set of assumptions, Meera could value furniture at 'what she feels it is worth', "
            "mix her household spend with shop spend, and count a customer order as a sale before the "
            "goods leave the shop. A bank, a tax officer or an examiner reading those books would "
            "not be able to trust the profit figure."
        )
    )
    parts.append(h3("Concepts versus conventions — comparison (memorise this table)"))
    parts.append(
        table(
            ["Basis", "Accounting concepts", "Accounting conventions"],
            [
                [
                    "Meaning",
                    "Fundamental assumptions on which accounts are prepared",
                    "Customs, traditions and practical guidelines used while applying concepts",
                ],
                [
                    "Nature",
                    "Theoretical / structural — the 'constitution'",
                    "Practical / behavioural — the 'customs'",
                ],
                [
                    "Necessity",
                    "Books cannot even start without them",
                    "They guide judgement when more than one treatment is possible",
                ],
                [
                    "Flexibility",
                    "Rigid. You do not pick and choose.",
                    "Some discretion, within honesty and disclosure",
                ],
                [
                    "When they bite",
                    "Every single transaction (who, when, how much, two sides)",
                    "At year-end judgements (stock valuation, provisions, notes, change of method)",
                ],
                [
                    "Standard list (Indian MBA / CA textbooks)",
                    "Business entity, Money measurement, Going concern, Cost, Dual aspect, Accrual, Matching, Periodicity, Revenue recognition",
                    "Conservatism (prudence), Consistency, Materiality, Full disclosure",
                ],
            ],
            caption="Concepts are assumptions; conventions are traditions",
        )
    )
    parts.append(
        exam_tip(
            "If a 5-mark question says 'Distinguish between accounting concepts and conventions', "
            "draw a table with at least four bases (meaning, nature, necessity, examples) and "
            "end with one line: concepts tell us <em>what world we are recording</em>; "
            "conventions tell us <em>how to behave when we have a choice</em>."
        )
    )
    parts.append(
        memory(
            "C-oncepts = C-onstitution (assumptions). C-onventions = C-ustoms (traditions). "
            "Four conventions to chant: <strong>CCMD</strong> — Conservatism, Consistency, "
            "Materiality, Disclosure."
        )
    )

    # ---- each concept ----
    parts.append(h3("The concepts, one by one"))
    parts.append(
        p(
            "For every idea below you get the same six things an examiner wants: "
            "a definition, a plain-English restatement, why it exists, Meera's shop as a real-life "
            "picture, what blows up if you ignore it, and a 3–5 mark answer you can almost copy."
        )
    )

    parts.append(
        concept_block(
            "1. Business entity concept (separate entity)",
            "The business is treated as a person separate from its owner. Transactions are recorded "
            "<em>from the point of view of the business</em>, not from the point of view of Meera the human being. "
            "The owner's capital is a liability of the business to the owner. Personal assets, personal "
            "debts and household expenses of the owner do not enter the business books except as capital or drawings.",
            "Meera the person and Meera Traders the shop are two different 'people' in the ledger. "
            "When Meera puts money in, the shop <em>owes her</em> that money (Capital). "
            "When she takes money out for home, the shop records Drawings — not Rent, not Wages, not Purchases.",
            "If the shop and the owner are mixed, you can never know whether the shop made a profit. "
            "A lender, a tax officer and you yourself need a clean picture of <em>the business</em>. "
            "The entity concept is also why Capital sits on the liabilities side of the accounting equation: "
            "Assets = Liabilities + Capital. Capital is what the business owes the owner.",
            "On 1 April Meera brings in cash ₹2,00,000. The shop records Dr Cash, Cr Capital — "
            "not 'Meera got richer'. On 20 April she takes ₹5,000 from the till for household rice and milk. "
            "The shop records Dr Drawings ₹5,000, Cr Cash ₹5,000. If she had recorded it as Wages or "
            "Purchases, April's profit would have been understated by ₹5,000 and her capital would have looked too high.",
            "Personal spending would sit inside expenses, profit would be understated, capital would be wrong, "
            "and a bank looking at the Balance Sheet would think the shop is weaker (or stronger) than it is. "
            "In a company this mixing is also illegal: a company's money is not the director's pocket money.",
            "The business entity (or separate entity) concept states that the business and its owner are distinct. "
            "All recording is done from the viewpoint of the business.",
            [
                "The owner is treated as a <em>creditor</em> of the business to the extent of capital introduced.",
                "Cash or goods brought in by the owner → Credit Capital. Cash or goods taken out for personal use → Debit Drawings. Drawings is not an expense.",
                "Personal house, personal car, personal loan, school fees of children — none of these appear in the shop's books.",
                "Illustration (Meera Traders): capital introduced ₹2,00,000 is a liability of the shop to Meera; drawings ₹5,000 reduce that claim, they do not reduce profit as an expense.",
                "Importance: true profit, true financial position, clean tax computation, and the accounting equation Assets = Liabilities + Capital only makes sense under this concept.",
            ],
            "In short: the owner is a stranger to the books. Treat every transaction by asking 'what happened to the <em>shop</em>?'",
        )
    )
    parts.append(
        memory(
            "Entity trick: write <strong>'Owner = stranger'</strong> on the top of your rough sheet. "
            "If Meera pays her son's school fees from the till, it is Drawings, not a business expense."
        )
    )

    parts.append(
        concept_block(
            "2. Money measurement concept",
            "Only those transactions and events that can be measured in money (rupees) are recorded in the books. "
            "Qualitative facts — skill of the owner, loyalty of staff, a good location, a strike, the owner's health — "
            "are ignored by the ledger even when they matter a great deal to the real business.",
            "If you cannot put a reliable rupee figure on it, it does not go into Meera's journal. "
            "The shop can be in the best market in Pune and Meera can be a brilliant salesperson — "
            "the Cash book still will not have a line called 'Good location ₹___'.",
            "Money is a common measuring rod. Adding '3 shelves + 1 loyal helper + a prime corner shop' "
            "is impossible. Adding ₹25,000 furniture + ₹4,000 wages is possible. Comparability and "
            "objectivity come from using one unit — the rupee.",
            "Meera's helper is honest and customers love the shop. None of that is journalised. "
            "The helper's wages of ₹4,000 are journalised, because that is money. "
            "A customer order that has not yet been delivered has no rupee entry until the sale happens.",
            "Books would fill up with opinions ('goodwill of the locality ₹10,00,000 — I feel so'). "
            "Two accountants would write two different books. Profit would stop meaning anything. "
            "The opposite mistake is also ugly: leaving out a credit purchase of ₹40,000 because "
            "'we have not paid yet' — that <em>is</em> measurable in money, so it <em>must</em> be recorded.",
            "The money measurement concept states that only events measurable in monetary terms are recorded in the books of account.",
            [
                "The rupee is the measuring unit. Non-monetary facts are omitted even if they are important.",
                "Examples recorded: cash, bank, furniture at cost, purchases, sales, outstanding electricity ₹2,000.",
                "Examples not recorded: Meera's skill, staff loyalty, a pending order, a rise in the market value of furniture, a strike next door.",
                "Limitation (write this — examiners love it): the Balance Sheet does not show the full 'worth' of the business because human resources and other qualitative strengths are missing.",
                "Illustration: furniture is in the books at ₹25,000 (the bill), not at 'what a buyer might pay today'.",
            ],
            "So: if it has a rupee tag and it affects the business, record it. If it only has a feeling, leave it out.",
        )
    )
    parts.append(
        memory(
            "Money measurement: <strong>'No rupee, no record.'</strong> Skill, strikes, smiles and 'prime location' stay outside the journal."
        )
    )

    parts.append(
        concept_block(
            "3. Going concern concept",
            "The business is assumed to continue for the foreseeable future. There is no intention, "
            "and no necessity, to liquidate or to cut the scale of operations in a material way. "
            "Because of this we record fixed assets at historical cost and charge depreciation over "
            "their useful life, we classify liabilities as current and non-current, and we treat prepaid "
            "expenses as assets — none of which would make sense if the shop were closing tomorrow.",
            "We assume Meera's shop will still be open next year, and the year after. "
            "A chair bought for ₹2,000 is not written off the day it is purchased just because it "
            "would fetch only ₹200 in a fire sale. We keep it on the books as furniture and "
            "(in a later chapter) spread its cost over the years it will be used.",
            "If we assumed the opposite — that the business will die this month — every asset would "
            "have to be shown at forced-sale value, every long-term loan would become immediately "
            "payable, and the idea of 'this year's profit' would collapse. Going concern is what "
            "lets us cut the life of the business into accounting periods and still make sense.",
            "Meera buys furniture on 3 April for ₹25,000. Under going concern we show Furniture ₹25,000 "
            "as an asset at 30 April. We do <em>not</em> write it down to scrap value. "
            "We also prepaid nothing and we skip depreciation in this chapter — but the reason we "
            "<em>would</em> depreciate next chapter, rather than expense the whole ₹25,000 in April, "
            "is going concern: the shelves will serve many periods.",
            "Assets would be forced onto scrap values; a healthy shop would look like a closing-down sale; "
            "prepaid rent would not be an asset; depreciation over 10 years would be meaningless; "
            "and comparison with last year would be impossible. Lenders use going concern when they "
            "give a 5-year loan. If the assumption fails (the shop is actually shutting), accounts "
            "must be recast on a break-up basis and the auditor must flag it.",
            "The going concern concept assumes that the enterprise will continue to operate in the foreseeable future and will not be liquidated in the near term.",
            [
                "Fixed assets are recorded at cost and depreciated over useful life, not shown at scrap value.",
                "Liabilities are split into current and non-current; prepaid expenses are assets; deferred revenue is a liability.",
                "The concept justifies the accounting period: we can report year-by-year because the story continues.",
                "Illustration: Meera's furniture ₹25,000 stays an asset at 30 April. If she had decided to shut the shop on 30 April, we would have valued furniture at what it can fetch in a quick sale.",
                "If going concern is in doubt, the financial statements must say so, and a break-up basis may be used.",
            ],
            "Memory line: the business is not dying tomorrow, so we do not value it like a garage sale.",
        )
    )

    parts.append(
        concept_block(
            "4. Cost concept (historical cost)",
            "Assets are recorded at the price paid to acquire them (historical cost), including "
            "all costs necessary to bring the asset to its intended use. Subsequent rises or falls "
            "in market value are ignored in the books (except where a specific standard requires "
            "revaluation or a fall below cost for inventories). The cost is objective — it is on the bill.",
            "Whatever Meera paid, that is the number. Furniture cost her ₹25,000; even if a similar "
            "set now sells for ₹30,000, the ledger still says ₹25,000. We do not revalue every weekend.",
            "Historical cost is verifiable (the invoice exists). Market value is an opinion and changes "
            "every day. Using cost keeps books free of imaginary profits. "
            "It also pairs with going concern: we did not buy the shelves to resell them tomorrow, "
            "we bought them to use, so today's resale price is not the point.",
            "3 April: furniture purchased for cash ₹25,000. The cash memo is the voucher. "
            "Cost = ₹25,000. If a neighbour offers ₹28,000 for the same shelves on 30 April, "
            "Meera does <em>not</em> pass a journal 'Dr Furniture ₹3,000, Cr Profit'. That ₹3,000 "
            "is an unrealised gain. Conservatism also forbids it.",
            "Assets would swing with rumours of market price; profit would include gains that have "
            "not been converted into cash; two shops with identical furniture would show different "
            "figures because their owners 'feel' different values. Tax and audit would become a fight. "
            "The limitation to mention in exams: in inflation, historical cost understates the real "
            "value of old land and buildings — that is accepted, and disclosed if revaluation is done.",
            "The cost concept states that an asset is recorded at the price paid to acquire it (historical cost), not at its current market value.",
            [
                "Cost includes purchase price plus freight, installation and other costs to bring the asset to use.",
                "Unrealised market gains are not recorded. A fall in the value of inventory below cost is recognised (prudence), which is why 'cost or NRV, lower' exists — taught with final accounts / inventory.",
                "Illustration: furniture at ₹25,000 on 3 April remains ₹25,000 on 30 April in Chapter 1 (no depreciation yet, no revaluation).",
                "Advantage: objectivity and evidence. Limitation: ignores inflation and current worth.",
                "Equation link: the debit to Furniture equals the credit to Cash because both are at the same historical amount.",
            ],
        )
    )
    parts.append(
        memory(
            "Cost concept: <strong>'Record the bill, not the dream price.'</strong> "
            "The cash memo is the king, the property dealer is not."
        )
    )

    parts.append(
        concept_block(
            "5. Dual aspect concept (double entry)",
            "Every transaction has two aspects — a debit and a credit — of equal amount. "
            "This is the foundation of double-entry bookkeeping and of the accounting equation "
            "<strong>Assets = Liabilities + Capital</strong>. After every transaction the equation "
            "still holds, because we have touched two (or more) elements by the same rupees.",
            "There are always two sides. If the shop's cash goes up, something else also changed: "
            "either the owner put money in (Capital up), or a customer paid (a debtor down), or "
            "we made a sale (income up). You never record only one side. That is why the trial "
            "balance can add up.",
            "If we recorded only 'cash came in', we would not know <em>why</em>, and we would have "
            "no check. Dual aspect gives us (a) a complete story of each event and (b) an arithmetic "
            "check: total debits = total credits. The whole of Chapters 1's journal, ledger and "
            "trial balance is this one idea, repeated fifteen times.",
            "1 April: Assets (Cash) ↑ ₹2,00,000 and Capital ↑ ₹2,00,000. Equation holds. "
            "2 April: Cash ↓ ₹1,50,000 and Bank ↑ ₹1,50,000 — one asset swapped for another. "
            "5 April: Purchases (expense) ↑ ₹40,000 and Liability (Kabir) ↑ ₹40,000. "
            "20 April: Cash ↓ ₹5,000 and Drawings ↑ ₹5,000 (capital claim down). "
            "22 April: Expense (Electricity) ↑ ₹2,000 and Liability (Outstanding) ↑ ₹2,000 — "
            "no cash, still two sides.",
            "Single-entry, incomplete records, a trial balance that cannot be drawn, profit that "
            "cannot be checked, fraud that is harder to spot. If a student posts only the debit "
            "of a cash sale, the trial balance will not agree — that is dual aspect catching the error.",
            "The dual aspect concept states that every transaction has two equal and opposite effects, and is recorded by debiting one account and crediting another with the same amount.",
            [
                "Accounting equation: Assets = Liabilities + Capital. Incomes increase capital; expenses and drawings decrease it. A useful working form used at trial-balance stage is: Assets + Expenses + Drawings = Liabilities + Capital + Incomes.",
                "Illustration of Meera on 1 April: Cash (asset) ₹2,00,000 = Capital ₹2,00,000.",
                "After depositing ₹1,50,000 in the bank: Cash ₹50,000 + Bank ₹1,50,000 = Capital ₹2,00,000. Still equal.",
                "This concept is why the journal has two columns and why a trial balance is possible.",
                "A compound entry (two debits, one credit, or the reverse) still obeys dual aspect: <em>total</em> debit = <em>total</em> credit.",
            ],
            extra=formula(
                "Assets = Liabilities + Capital",
                "At trial-balance stage (before closing stock and profit calculation): "
                "Assets + Expenses + Drawings = Liabilities + Capital + Incomes. "
                "Both sides of Meera's trial balance equal ₹2,80,000 — that is dual aspect made visible.",
            ),
        )
    )
    parts.append(
        memory(
            "Dual aspect: <strong>'Two sides to every story, and the rupees on both sides are equal.'</strong> "
            "If you can name only one account, you have not finished thinking."
        )
    )

    parts.append(
        concept_block(
            "6. Accrual concept",
            "Revenues are recognised when they are <em>earned</em> and expenses when they are "
            "<em>incurred</em>, whether or not cash has been received or paid. This is the opposite "
            "of the cash basis, which records only cash movements. Indian GAAP / Companies Act "
            "accounts of companies are on accrual basis.",
            "Did the work happen this month? Then it belongs to this month — even if the money "
            "moves next month. Sana took goods on 8 April; that is April's sale, even though she "
            "pays later. Electricity was used in April; that is April's expense, even though Meera "
            "will pay the bill in May.",
            "Cash basis can be manipulated by delaying a payment or chasing a receipt. Accrual "
            "shows the true performance of the period. It is also why we have outstanding expenses, "
            "prepaid expenses, accrued income and income received in advance — four adjustments "
            "you will meet in final accounts, one of which (outstanding electricity) we already "
            "meet in this chapter.",
            "22 April: electricity used in April ₹2,000, unpaid. Journal: Dr Electricity ₹2,000, "
            "Cr Outstanding Electricity ₹2,000. If Meera ignored accrual and waited for the payment, "
            "April's profit would be overstated by ₹2,000 and May (when she pays) would be punished "
            "for April's light. 8 April credit sale to Sana ₹22,000 is also accrual: income is earned "
            "when goods are sold, not when cash arrives.",
            "Profit would jump around with the bank balance instead of with the work done. "
            "A shop that sold a lot on credit would look like a failure until the money came in. "
            "Unpaid bills would hide in a drawer and explode later. Comparison across months would die.",
            "The accrual concept states that incomes are recorded when earned and expenses when incurred, irrespective of the timing of cash.",
            [
                "Credit sales are income of the period of sale. Credit purchases are expenses/costs of the period of purchase.",
                "Outstanding expense: debit the expense, credit a liability (Meera: electricity ₹2,000).",
                "Prepaid expense, accrued income, income received in advance follow the same idea (later chapter).",
                "Accrual is the reason the cash book is not the same thing as the Profit and Loss Account. Profit ≠ cash.",
                "Companies in India must use accrual; a tiny shopkeeper using a cash diary is using a different (incomplete) basis.",
            ],
            extra=keypoint(
                "Outstanding electricity is the one accrual adjustment we <em>do</em> make in Chapter 1, "
                "because it is just another journal: expense ↑ and liability ↑. Prepaid, depreciation "
                "and closing stock are saved for later chapters. Do not invent them in Meera's books."
            ),
        )
    )
    parts.append(
        memory(
            "Accrual: <strong>'Earned, not received. Incurred, not paid.'</strong> "
            "Ask 'whose month is this income/expense?' not 'when did the cash move?'"
        )
    )

    parts.append(
        concept_block(
            "7. Matching concept",
            "The expenses of an accounting period are matched against the revenues of the "
            "<em>same</em> period to find the profit of that period. Revenues are recognised on "
            "accrual; then every cost that was incurred to earn those revenues is brought into "
            "the same Profit and Loss Account.",
            "Put April's costs next to April's sales — not next to March, not next to May. "
            "Rent of April, wages of April, electricity of April, and the cost of goods that "
            "were sold in April, all sit against April's sales and commission. That is how "
            "you get April's profit (once closing stock is also matched, in a later chapter).",
            "Without matching, you could take this year's sales and last year's rent and call "
            "the difference 'profit'. That number would not mean anything. Matching is why we "
            "adjust outstanding and prepaid items, why we carry closing stock to the next period, "
            "and why we depreciate assets over the years they help to earn revenue.",
            "Meera's April revenues (to be matched): Sales ₹40,000 + Commission ₹3,000. "
            "April costs already in the books: Purchases ₹70,000, Rent ₹8,000, Wages ₹4,000, "
            "Electricity ₹2,000. Purchases of ₹70,000 include goods still sitting on the shelf — "
            "those leftover goods are closing stock and will be matched to <em>next</em> period's "
            "sales. We do not make that stock entry in Chapter 1, so we also do not yet compute "
            "a Profit and Loss figure. Matching is why we wait.",
            "Profit would mix periods: pay two years' rent this year and this year looks like a "
            "disaster; skip the electricity bill and this year looks like a festival. "
            "Investors and examiners would be reading a mashed-up story.",
            "The matching concept requires that expenses incurred to earn the revenue of a period be recognised in the same period as that revenue.",
            [
                "It works together with accrual and with the accounting period.",
                "Practical tools of matching: outstanding / prepaid expenses, accrued / unearned income, depreciation, closing stock, cost of goods sold.",
                "Illustration: April electricity ₹2,000 is matched with April sales even though unpaid. Drawings ₹5,000 are <em>not</em> matched against sales — drawings are not an expense.",
                "Chapter 1 limit: we do not adjust closing stock, so we cannot yet state Meera's gross profit. That is honest matching — do not force a fake profit number.",
                "Exam line: 'Matching is the bridge from the trial balance to the Profit and Loss Account.'",
            ],
        )
    )
    parts.append(
        memory(
            "Matching: <strong>'Pair the cost with the sale it helped to earn.'</strong> "
            "Same period, same P&L. Drawings do not pair with sales — they are not a cost of earning."
        )
    )

    parts.append(
        concept_block(
            "8. Conservatism / prudence convention",
            "Anticipate no profit, but provide for all possible losses. Unrealised gains are ignored; "
            "known and expected losses are recognised. This is a convention (a tradition of caution) "
            "that colours judgement when two treatments are possible. It is why inventory is valued "
            "at cost or net realisable value, whichever is lower, and why a provision for doubtful "
            "debts is made.",
            "If you are not sure, be pessimistic in the books — not in life. Do not book a profit "
            "you have not locked in. Do provide for a loss that is knocking. "
            "The idea is to avoid showing a rosier picture than reality, so that nobody takes "
            "dividends (or decisions) out of paper profits.",
            "Users of accounts prefer a slightly understated profit to a profit that later evaporates. "
            "Prudence protects creditors and the owner from over-optimism. It is a brake, not a "
            "licence to hide profits: over-conservatism (secret reserves) is also wrong and is "
            "attacked by full disclosure and by accounting standards.",
            "A customer offers Meera ₹28,000 for furniture that cost ₹25,000. She does not record "
            "the ₹3,000 'gain' until she actually sells it. On the other side: if Sana looked likely "
            "to default, Meera would provide for a doubtful debt (later chapter) — she would not "
            "wait for the default to become certain. Stock, when we meet it, is never shown above cost.",
            "Unrealised gains would inflate capital; the owner might withdraw cash that is not really "
            "profit; a later year would take a shock. The opposite abuse — creating huge secret "
            "reserves by understating assets — would hide the true position from lenders and tax. "
            "Prudence is caution, not window-dressing in the other direction.",
            "The convention of conservatism (prudence) states that the accountant should not anticipate profits but should provide for all foreseeable losses.",
            [
                "Do not record unrealised gains (e.g. a rise in the market value of furniture).",
                "Do record expected losses (provision for doubtful debts, fall in stock value below cost).",
                "Stock valuation rule that follows: cost or NRV, whichever is lower.",
                "Illustration: Meera's furniture stays at ₹25,000; credit sales to Sana ₹22,000 are recorded (they are realised by the sale contract) but a mere enquiry from a customer is not a sale.",
                "Warning: excessive conservatism creates secret reserves and violates true and fair view. Standards now speak of 'prudence' as caution, not as a bias that overrides other concepts.",
            ],
        )
    )
    parts.append(
        memory(
            "Prudence: <strong>'Hope for the best, provide for the worst — in the books.'</strong> "
            "No profit until it is earned. Every probable loss gets a line."
        )
    )

    parts.append(
        concept_block(
            "9. Consistency convention",
            "Once an accounting method or policy is chosen, it is followed from one period to the "
            "next. A change is made only for a stronger reason (a better true-and-fair view, or a "
            "new standard), and the change and its rupee effect are disclosed. Consistency makes "
            "this year's figures comparable with last year's.",
            "Do not change the measuring scale every year. If Meera (in a later chapter) chooses "
            "Straight Line Method for depreciating furniture, she keeps SLM next year. "
            "She does not hop to Written Down Value in a year when she wants a lower profit, "
            "and hop back when she wants a higher one.",
            "Users compare April with May, this year with last year, Meera with another stationer. "
            "If the method keeps changing, they are comparing apples with oranges. Consistency "
            "does <em>not</em> mean 'never change'. It means 'do not change quietly, and do not "
            "change to dress up profit'.",
            "Suppose next year Meera wanted to switch the stock-flow method. She may, if FIFO "
            "or weighted average is genuinely better for her, but she must say so in the notes "
            "and show the effect. In Chapter 1 the live illustration is smaller: we use the same "
            "account titles, the same dual-aspect rules and the same (historical) cost for furniture "
            "all through April. We do not revalue furniture on 15 April and cost it again on 28 April.",
            "Profit can be manufactured by switching methods (SLM ↔ WDV, FIFO ↔ weighted average, "
            "changing the provision rate). Trends become fiction. Auditors and examiners treat an "
            "undisclosed change of method as a red flag — and as an error of principle.",
            "The convention of consistency requires that the same accounting methods and policies be followed from one period to another so that results are comparable.",
            [
                "It applies to depreciation method, stock valuation, provision rates, classification of items.",
                "Change is allowed if it improves true and fair view, or if a law / standard requires it — with disclosure of the nature of change and the rupee effect.",
                "Consistency is not a bar on correcting an error, and it is not a bar on a better policy.",
                "Illustration: furniture stays at historical cost throughout April; we do not mix 'cost today, market value tomorrow'.",
                "Exam pair: consistency (same method over time) × uniformity (same method across firms — which is <em>not</em> required). Do not confuse them.",
            ],
        )
    )
    parts.append(
        memory(
            "Consistency: <strong>'Don't change the scale.'</strong> "
            "Same method, year after year, unless you have a good reason and you disclose it."
        )
    )

    parts.append(
        concept_block(
            "10. Materiality convention",
            "An item is material if it can influence the decision of a user of the accounts. "
            "Material items must be recorded and shown properly. Immaterial items may be treated "
            "in a convenient way — for example, a stapler costing ₹80 can be debited to office "
            "expenses instead of being capitalised as an asset and depreciated over four years. "
            "Materiality is relative: ₹5,000 drawings are material for Meera; they would be "
            "rounding error for a steel plant.",
            "Don't sweat the stapler; don't hide the building. If a rupee amount is too small to "
            "change anyone's mind, we are allowed to be practical. If it is big enough to change "
            "a decision (a loan, a tax computation, a pass mark in an exam question), we treat it "
            "strictly by the concepts.",
            "Strict application of every concept to every pencil would make books expensive and "
            "unreadable. Materiality is the convention that lets accountants be efficient without "
            "being misleading. It is also the convention examiners use when they ask 'would you "
            "capitalise this?' — the answer depends on size relative to the business.",
            "Meera buys furniture ₹25,000 — clearly an asset (material). She also buys a box of "
            "drawing pins for the notice board, ₹60. In practice that ₹60 is Stationery expense "
            "(or Purchases), not 'Drawing-pin asset'. Outstanding electricity ₹2,000 is material "
            "for her tiny shop, so we do not skip it. In a company with ₹500 crore turnover the "
            "same ₹2,000 might be ignored — materiality is relative.",
            "If ignored on the 'too strict' side: every pen becomes a fixed asset, the Balance Sheet "
            "is cluttered, and time is wasted. If ignored on the 'too loose' side: a large outstanding "
            "expense or a large related-party payment is brushed under 'sundries', and users are misled. "
            "Window-dressing often pretends an item is immaterial when it is not.",
            "The convention of materiality states that only items that can influence the economic decisions of users need to be strictly applied and separately disclosed; trivial items may be treated conveniently.",
            [
                "Materiality is relative to the size and nature of the business and to the nature of the item (a small bribe is still material by nature).",
                "Practical effect: small tools expensed; large plant capitalised. Small rounding vs a large outstanding liability.",
                "Illustration: Meera's ₹2,000 outstanding electricity is material for her and is recorded. A ₹20 packet of rubber bands is expensed, not capitalised.",
                "Materiality cannot be used as an excuse to hide errors of principle or to offset assets against liabilities.",
                "In an exam, if the amount is given and the business is small, treat it strictly — the examiner put that number there for a reason.",
            ],
        )
    )
    parts.append(
        memory(
            "Materiality: <strong>'Don't sweat the stapler; never hide the building.'</strong> "
            "Relative to the size of the shop, and never an excuse for a wrong principle."
        )
    )

    parts.append(
        concept_block(
            "11. Full disclosure convention",
            "All material information that is necessary for a true and fair view — including "
            "accounting policies, contingent liabilities, outstanding and prepaid items, change "
            "of method, related-party dealings — must be disclosed in the financial statements "
            "or in the notes. Nothing important is kept in the accountant's head.",
            "Tell the whole truth that a reader needs. The face of the Balance Sheet cannot hold "
            "every story, so we add notes. If Meera had given a guarantee for a friend's loan, "
            "or if a case was pending, that would be disclosed even when no journal is passed "
            "(contingent liability). Disclosure does not always mean 'pass an entry'; it means "
            "'do not hide it'.",
            "Users who cannot see the methods and the risks will misread the profit. Law (Companies "
            "Act, Schedule III, accounting standards) has turned this convention into a detailed "
            "checklist for companies. For Meera's proprietorship the spirit is the same: the trial "
            "balance and, later, the statements plus notes should not mislead a lender.",
            "In this chapter we disclose, in words, that closing stock is not adjusted and that "
            "depreciation is not charged. That is already disclosure — a reader of Meera's trial "
            "balance must not think ₹70,000 purchases means ₹70,000 of goods have been sold. "
            "When outstanding electricity is recorded, it appears as a separate liability, not "
            "netted inside Capital. That is disclosure by classification.",
            "Window-dressing, secret reserves, netting a loan against a bank balance, hiding a "
            "change from SLM to WDV, not mentioning a court case — all of these survive if "
            "disclosure is ignored. The statements may still 'tally' and still be a lie.",
            "The convention of full disclosure requires that all material facts and accounting policies necessary for a true and fair view be disclosed in the financial statements and notes.",
            [
                "Disclosure is of material items, methods, changes, contingent liabilities, commitments and events after the balance sheet date (as applicable).",
                "It complements prudence (do not hide losses) and consistency (if you change, say so).",
                "Companies: Schedule III and accounting standards list what must be shown. Proprietorships follow the same spirit.",
                "Illustration: Meera's outstanding electricity is shown as a liability of ₹2,000, not silently mixed with creditors. Drawings are a separate debit balance, not a quiet reduction of Purchases.",
                "Tallying of the trial balance is not disclosure. A trial balance can agree and still conceal a wrong treatment — see Section F.",
            ],
        )
    )
    parts.append(
        memory(
            "Full disclosure: <strong>'Tell the whole truth that a user needs.'</strong> "
            "If it would change a lender's mind, it does not stay in your drawer."
        )
    )

    parts.append(
        concept_block(
            "12. Periodicity / accounting period concept",
            "The unlimited life of a going concern is cut into equal slices called accounting "
            "periods (usually a year; also a quarter or a month) so that profit, tax and "
            "performance can be reported at regular intervals. In India the financial year "
            "commonly runs 1 April to 31 March. Meera started on 1 April 2025; her first statutory "
            "year would end 31 March 2026. In this chapter we use the month of April 2025 as a "
            "mini-period so the full cycle can be seen.",
            "A movie is cut into episodes so you can follow the plot. The shop may live for thirty "
            "years; we still need to know how April went. Periodicity is the decision to stop, "
            "count, and report — even though the story continues on 1 May.",
            "Owners, banks and the tax department cannot wait until the shop closes forever to "
            "know the profit. Periodicity gives us a deadline: 30 April (in our mini-period) we "
            "balance the ledgers and draw a trial balance. Matching and accrual exist <em>because</em> "
            "we cut time into periods; otherwise we could wait for every cash movement.",
            "We close Meera's books for April on 30 April 2025 (April has 30 days, not 31). "
            "Outstanding electricity is brought in so that April, not May, carries April's power cost. "
            "On 1 May, asset, liability and capital balances are brought down (Balance b/d) and "
            "the next episode starts. Income and expense accounts of April will, in a later chapter, "
            "be closed to Profit and Loss; in Chapter 1 they simply show their balances on the trial balance.",
            "You would know the profit only at the funeral of the business — useless for tax, for "
            "a bank loan, for deciding whether to restock. Outstanding and prepaid adjustments "
            "would have no meaning because there would be no 'this period' versus 'next period'.",
            "The periodicity (accounting period) concept states that the life of the business is divided into regular intervals for which financial statements are prepared.",
            [
                "Usual period: one year (1 April to 31 March in India). Interim reporting: quarter / half-year / month.",
                "It works with going concern (the life continues) and with matching / accrual (cut the right incomes and expenses into this slice).",
                "At the end of each period we balance ledgers, draw a trial balance, and (later chapters) prepare Trading, Profit and Loss and Balance Sheet.",
                "Illustration: Meera's Chapter 1 period is 1 April 2025 to 30 April 2025. Outstanding electricity is an end-of-period accrual. Cash of ₹27,000 is a balance that goes into the next period.",
                "Do not write '31 April' — April has 30 days. Examiners notice.",
            ],
        )
    )
    parts.append(
        memory(
            "Periodicity: <strong>'Cut the movie into episodes.'</strong> "
            "Indian default episode = 1 April to 31 March. This chapter's episode = April 2025."
        )
    )

    parts.append(
        concept_block(
            "13. Revenue recognition (realisation) — brief",
            "Revenue is recognised when it is earned — that is, when goods have been sold or "
            "services rendered and a legally enforceable claim arises — not necessarily when cash "
            "is received. For a credit sale, the sale is recorded on the date of the invoice, "
            "not on the date the customer pays. For cash sales, earning and cash happen together. "
            "A mere order, or goods sent on sale-or-return that are not yet accepted, is not revenue.",
            "Meera earns a sale when the notebook leaves the shop and Sana accepts it, not when "
            "Sana's cash arrives a week later. Commission is earned when the display service is "
            "done (and here it is received in cash the same day). An enquiry, a quotation, a "
            "wish-list — none of these is a sale.",
            "If we recognised revenue at cash receipt, credit-selling businesses would show zero "
            "sales in a month of heavy credit and a mountain of sales in the month of collection. "
            "If we recognised it at the time of an order, we would book income before we have "
            "done the work. Realisation pins income to the earning event.",
            "8 April: goods sold to Sana ₹22,000 — Sales is credited now, Sana is debited now. "
            "15 April: cash from Sana ₹10,000 is <em>not</em> a second sale; it is a conversion "
            "of debtor into cash. 6 April cash sales ₹18,000 are both a sale and a cash receipt "
            "in one event. A school that asked Meera for a quotation of ₹50,000 has generated "
            "no journal at all.",
            "Booking orders as sales overstates income and debtors. Booking credit sales only "
            "when cash comes in understates income and hides debtors. Both destroy matching. "
            "A student who credits Sales again when Sana pays is committing a classic error — "
            "double counting revenue.",
            "The revenue recognition (realisation) concept states that revenue is recorded when it is earned — when goods are sold or services are rendered — and not necessarily when cash is received.",
            [
                "Credit sale: debit the customer, credit Sales, on the invoice date.",
                "Later collection: debit Cash/Bank, credit the customer. Do <em>not</em> credit Sales again.",
                "Not revenue: orders, quotations, goods on sale-or-return not yet accepted, unrealised rise in asset values.",
                "Illustration: Sana ₹22,000 is April revenue; the ₹10,000 received on 15 April is a balance-sheet swap (debtor ↓ cash ↑).",
                "It works with accrual and with prudence (do not realise a gain that is not yet earned).",
            ],
        )
    )
    parts.append(
        memory(
            "Revenue: <strong>'Sale is on the invoice, not on the cash.'</strong> "
            "When the customer later pays, you credit the customer, never Sales a second time."
        )
    )

    parts.append(h3("How the concepts sit on Meera's fifteen transactions"))
    parts.append(
        table(
            ["Date", "What happened", "Concept that decides the treatment"],
            [
                ["1 Apr", "Cash from owner ₹2,00,000", "Entity (owner ≠ shop) + Dual aspect (Cash and Capital) + Cost / Money measurement"],
                ["2 Apr", "Cash deposited in bank ₹1,50,000", "Dual aspect (asset swap) + Entity (it is the shop's bank account)"],
                ["3 Apr", "Furniture ₹25,000", "Cost (bill amount) + Going concern (keep it as an asset) + Money measurement"],
                ["4–5, 28 Apr", "Purchases cash and credit", "Dual aspect; credit purchase also Accrual (recorded though unpaid)"],
                ["6 & 8 Apr", "Cash and credit sales", "Revenue recognition (earned now) + Accrual (Sana has not paid)"],
                ["10, 18 Apr", "Rent, wages", "Matching (April's costs in April) + Entity (shop expenses)"],
                ["12 & 15 Apr", "Paid Kabir / received Sana", "Dual aspect only — these are settlements, not new purchases or sales"],
                ["20 Apr", "Cash taken home ₹5,000", "Entity (Drawings, not expense) + Dual aspect"],
                ["22 Apr", "Unpaid electricity ₹2,000", "Accrual + Matching + Periodicity + Dual aspect (expense and liability)"],
                ["25 Apr", "Commission ₹3,000", "Revenue recognition + Money measurement"],
                ["30 Apr", "We stop and add up", "Periodicity. No closing stock, no depreciation (disclosed — Full disclosure)"],
            ],
            caption="Every journal you will write is a concept in action",
        )
    )

    parts.append(
        identify(
            "If the question says <em>'explain any four accounting concepts'</em>, pick Entity, Dual aspect, "
            "Accrual, Going concern (the four that unlock the most marks) and for each write: definition, "
            "one Meera-style example, one line on 'what if ignored'. If it says <em>'conventions'</em>, "
            "you must use Conservatism, Consistency, Materiality, Full disclosure — not Entity. "
            "If it says <em>'why is capital a liability'</em>, the answer is Entity + Dual aspect. "
            "If it says <em>'why record outstanding electricity'</em>, the answer is Accrual + Matching + Periodicity."
        )
    )
    parts.append(
        mistakes(
            [
                "Calling conservatism a 'concept' and entity a 'convention' (know the standard split for the exam you are sitting; this chapter uses concepts = assumptions, conventions = CCMD).",
                "Treating drawings as an expense — that is an entity-concept failure, and it understates profit.",
                "Crediting Sales again when a debtor pays — that is a revenue-recognition failure, and it double-counts income.",
                "Skipping outstanding electricity 'because cash did not move' — that is an accrual failure.",
                "Revaluing furniture to market price 'to show a true picture' — cost + prudence forbid the unrealised gain.",
                "Writing a profit figure in Chapter 1 after looking at Sales − Purchases, without closing stock — that is a matching failure. Do not do it.",
                "Dating the trial balance 31 April 2025. April has 30 days.",
            ]
        )
    )
    parts.append(
        example(
            "A1",
            "Easy",
            "Which concept? — six one-liners",
            "<p>Name the concept / convention. Answers follow each line in italics.</p>"
            + ol(
                [
                    "Meera's skill as a salesperson is not in the books. <em>Money measurement.</em>",
                    "Furniture stays at ₹25,000 even though a dealer offered ₹28,000. <em>Cost, plus conservatism (no unrealised gain), plus going concern.</em>",
                    "Household milk from the till is Drawings. <em>Business entity.</em>",
                    "Electricity of April is recorded in April though paid in May. <em>Accrual (and matching, periodicity).</em>",
                    "The shop is assumed to be open next year, so furniture is an asset, not scrap. <em>Going concern.</em>",
                    "Sana's credit purchase is a sale of 8 April, not of 15 April. <em>Revenue recognition / realisation, plus accrual.</em>",
                ]
            ),
        )
    )
    parts.append(
        example(
            "A2",
            "Moderate",
            "Apply three concepts to one fact",
            "<p><strong>Fact.</strong> On 22 April Meera's electricity meter shows April consumption of "
            "₹2,000. The bill will be paid on 7 May.</p>"
            "<p><strong>Required.</strong> Which concepts force an entry on 22 (or 30) April, what is the "
            "entry, and what goes wrong if she waits till 7 May?</p>"
            "<p><strong>Solution.</strong></p>"
            "<p><em>Periodicity</em> says April is a separate episode that must be complete. "
            "<em>Accrual</em> says the expense was incurred in April. <em>Matching</em> says April's "
            "light must sit against April's sales. Dual aspect then gives the two accounts:</p>"
            + journal(
                [
                    {
                        "date": "22 Apr 2025",
                        "debit": "Electricity A/c",
                        "credit": "Outstanding Electricity A/c",
                        "amount": "2,000",
                        "narration": "Being electricity used in April remaining unpaid.",
                    }
                ],
                caption="Entry forced by accrual + matching + periodicity",
            )
            + "<p>If she waits till 7 May: April profit is overstated by ₹2,000, April's trial balance "
            "hides a liability of ₹2,000, and May is charged for April's light. A bank reading April "
            "figures would be misled. Entity also reminds us it is the <em>shop's</em> electricity, "
            "not Meera's house bill — if it had been her house, it would be Drawings, not Electricity.</p>",
        )
    )
    parts.append(
        example(
            "A3",
            "Exam-level",
            "5-mark theory — 'Explain the dual aspect concept. How does it lead to a trial balance?'",
            exam_ready(
                "Dual aspect means every transaction has two equal effects. If one account is debited, "
                "another is credited with the same rupees. This is the origin of the accounting equation "
                "Assets = Liabilities + Capital (incomes increase capital; expenses and drawings reduce it).",
                "Illustration from Meera Traders, 1 April 2025: cash introduced ₹2,00,000 increases an "
                "asset (Cash) and increases Capital. 5 April: credit purchase ₹40,000 increases an expense "
                "(Purchases) and increases a liability (Kabir). 22 April: outstanding electricity ₹2,000 "
                "increases an expense and increases a liability — cash does not move, but two aspects still exist.",
                "Because every debit has an equal credit, the total of all debit balances in the ledger "
                "must equal the total of all credit balances. A trial balance is simply that list. "
                "Meera's trial balance as at 30 April 2025 totals ₹2,80,000 on each side. If a student "
                "posts only one side of a journal, the trial balance refuses to agree — dual aspect has "
                "caught the arithmetic. (It will not catch an error of principle, as Section F shows.)",
            ),
        )
    )
    return "".join(parts)


# ===========================================================================
# B. Identifying transactions
# ===========================================================================

def _section_b() -> str:
    parts = []
    parts.append(h2("B. Identifying business transactions", "transactions"))
    parts.append(
        definition(
            "A <strong>business transaction</strong> is an economic event, measured in money, "
            "that changes the financial position of the <em>business</em>, that has already happened, "
            "and that is supported by evidence (a voucher / source document). Only transactions "
            "are journalised. Everything else may be important in life and still be invisible to the ledger."
        )
    )
    parts.append(
        simple(
            "Four gates. A fact must pass <em>all four</em> before it becomes a journal line: "
            "(1) it has a rupee figure, (2) it is the shop's event not Meera's private life, "
            "(3) it has happened (not a plan, not an order sitting in a WhatsApp chat), "
            "(4) there is a paper or electronic voucher you can file."
        )
    )
    parts.append(
        why(
            "Beginners lose marks by journalising things that are not transactions (hired a helper, "
            "received an enquiry, furniture's market value rose) and by skipping things that are "
            "(credit purchase, outstanding electricity, drawings). The four gates stop both mistakes. "
            "They are money measurement + entity + realisation + the audit trail, used as a checklist."
        )
    )
    parts.append(h3("The four gates (use this as an exam procedure)"))
    parts.append(
        steps(
            [
                "<strong>Monetary?</strong> Can I write a rupee amount that is not a guess? If no → not a transaction. (Money measurement.)",
                "<strong>Affects the business?</strong> Is it Meera Traders, or Meera's kitchen? Kitchen → ignore, or Drawings if shop money was used. (Entity.)",
                "<strong>Has it happened?</strong> Goods received / sold / paid / become payable / become receivable. A quotation, a budget, 'I will buy next week' → no. (Realisation / occurrence.)",
                "<strong>Evidence?</strong> Is there a cash memo, invoice, cheque, debit note, payslip, bill, or a signed voucher? Accountants do not write from memory. If a transaction happened, we <em>create</em> a voucher if the outsider did not give us one (e.g. a debit voucher for drawings).",
                "If all four are yes, name the two accounts and go to the Golden / Modern rules (Section C).",
            ],
            title="7. Step-by-step — is this a transaction?",
        )
    )
    parts.append(h3("Transactions versus non-transactions (Meera's April)"))
    parts.append(
        table(
            ["Event", "₹?", "Shop's?", "Happened?", "Voucher?", "Verdict", "If recorded, which journal?"],
            [
                ["Meera brings cash ₹2,00,000", "Yes", "Yes (capital)", "Yes", "Pay-in / capital voucher", b("Transaction"), "Dr Cash, Cr Capital"],
                ["Opens bank, deposits ₹1,50,000", "Yes", "Yes", "Yes", "Pay-in slip", b("Transaction"), "Dr Bank, Cr Cash"],
                ["Buys furniture ₹25,000 cash", "Yes", "Yes", "Yes", "Cash memo", b("Transaction"), "Dr Furniture, Cr Cash"],
                ["Buys goods from Kabir on credit ₹40,000", "Yes", "Yes", "Yes (goods received)", "Invoice / bill", b("Transaction"), "Dr Purchases, Cr Kabir"],
                ["Sells to Sana on credit ₹22,000", "Yes", "Yes", "Yes (goods delivered)", "Invoice", b("Transaction"), "Dr Sana, Cr Sales"],
                ["Electricity used ₹2,000 unpaid", "Yes", "Yes", "Yes (consumed)", "Bill (even if unpaid)", b("Transaction"), "Dr Electricity, Cr Outstanding Electricity"],
                ["Takes ₹5,000 home from the till", "Yes", "Affects shop cash", "Yes", "Debit voucher", b("Transaction"), "Dr Drawings, Cr Cash"],
                ["A school asks for a quotation of ₹50,000", "A number, but no deal", "Not yet", "No (only an enquiry)", "Quotation is not a voucher of a deal", "Not a transaction", "No entry"],
                ["Kabir promises a 5% discount next month", "Not yet earned", "Maybe later", "No", "None", "Not a transaction", "No entry"],
                ["Helper is 'hired' on 1 Apr, first wage on 18 Apr", "Wages yes, hiring no", "Yes", "Hiring is a contract, not a ₹ event", "Payslip on 18 Apr", "Hiring: no. Wages ₹4,000: yes", "Only the wage payment / accrual"],
                ["Market value of furniture becomes ₹28,000", "An opinion", "Shop's asset, but not a deal", "No sale", "No bill", "Not a transaction", "No entry (cost + prudence)"],
                ["Meera is a skilled seller / shop has a 'good name'", "No", "Qualitative", "Always true, never a ₹ event", "None", "Not a transaction", "No entry (money measurement)"],
                ["Meera pays son's fees ₹3,000 from her own purse", "Yes", b("No — not shop money"), "Yes, but personal", "School receipt (personal)", "Not a business transaction", "No entry in shop books"],
                ["Meera pays son's fees ₹3,000 from the till", "Yes", "Shop cash fell", "Yes", "Debit voucher", b("Transaction"), "Dr Drawings, Cr Cash"],
                ["Goods ordered from Kabir, not yet received", "Price known", "Intended", "No receipt yet", "Purchase order ≠ invoice", "Not yet", "Entry on receipt of goods / invoice"],
                ["Customer returns nothing — only praises the shop", "No", "Qualitative", "No ₹ event", "None", "Not a transaction", "No entry"],
            ],
            caption="Four gates applied to Meera's world",
            foot="A purchase order is not a purchase. A quotation is not a sale. A feeling is not a voucher.",
        )
    )
    parts.append(
        logic(
            "Notice the pattern. Credit events (Kabir, Sana, outstanding electricity) pass the gates "
            "even though cash is still. Cash is not one of the four gates. Beginners secretly add a "
            "fifth gate — 'did money move?' — and then skip half the journals. Delete that fifth gate."
        )
    )

    parts.append(h3("Source documents — the evidence behind every journal"))
    parts.append(
        simple(
            "A <strong>source document</strong> is the original paper (or electronic record) that "
            "proves the transaction. A <strong>voucher</strong> is the accounting file copy prepared "
            "from that document, numbered and authorised, on the strength of which the journal is written. "
            "In a small shop the cash memo itself is often used as the voucher. In an exam, 'no voucher, "
            "no entry' is the safe line."
        )
    )
    parts.append(
        table(
            ["Document", "What it is (one line)", "Typical Meera use", "Accounts it usually supports"],
            [
                [
                    b("Cash memo"),
                    "Bill issued / received when goods are sold or bought <em>for cash</em>.",
                    "6 Apr cash sales; 4 Apr cash purchases; 3 Apr furniture.",
                    "Cash with Sales / Purchases / Asset",
                ],
                [
                    b("Invoice (bill)"),
                    "Bill issued / received when goods are sold or bought <em>on credit</em>.",
                    "5 Apr and 28 Apr from Kabir; 8 Apr to Sana.",
                    "Purchases + Creditor, or Debtor + Sales",
                ],
                [
                    b("Debit note"),
                    "Note sent to a supplier when we return goods or claim an allowance — it is our advice that we have <em>debited</em> the supplier.",
                    "If Meera returned damaged pens to Kabir (not in April's list).",
                    "Debit Kabir, Credit Purchases / Returns",
                ],
                [
                    b("Credit note"),
                    "Note sent to a customer when the customer returns goods — it is our advice that we have <em>credited</em> the customer.",
                    "If Sana returned notebooks (not in April's list).",
                    "Debit Sales / Returns, Credit Sana",
                ],
                [
                    b("Cheque / pay-in slip / bank advice"),
                    "Instrument and bank paper for money in or out of the bank account; counterfoil or statement is the voucher.",
                    "2 Apr deposit; 10 Apr rent; 12 Apr payment to Kabir.",
                    "Bank with Cash / Rent / Kabir",
                ],
                [
                    b("Payslip / wage sheet"),
                    "Evidence of wages or salary earned and paid (or outstanding).",
                    "18 Apr wages ₹4,000.",
                    "Wages with Cash / Outstanding wages",
                ],
                [
                    b("Receipt"),
                    "Acknowledgement that we have received money (issued to Sana) or that someone has received money from us.",
                    "15 Apr cash from Sana; 25 Apr commission.",
                    "Cash with Sana / Commission",
                ],
                [
                    b("Debit voucher / credit voucher (internal)"),
                    "In-house paper when no outside bill exists — drawings, contra (cash deposited in bank), outstanding adjustments.",
                    "1 Apr capital; 20 Apr drawings; 22 Apr outstanding electricity.",
                    "Capital, Drawings, Outstanding expense",
                ],
            ],
            caption="Source documents you must be able to name in one line",
        )
    )
    parts.append(
        keypoint(
            "Debit note vs credit note, in one breath: <strong>we send a debit note when we debit someone "
            "(usually a supplier, for returns)</strong>. <strong>We send a credit note when we credit someone "
            "(usually a customer, for returns)</strong>. The name is from <em>our</em> books, not from theirs."
        )
    )
    parts.append(
        real_life(
            "On 5 April a carton of notebooks arrives with Kabir's invoice no. 214, ₹40,000, credit 30 days. "
            "That invoice is the source document. Meera (or her accountant) stamps it, numbers it as "
            "Purchase Voucher PV-003, and only then writes Dr Purchases, Cr Kabir. If the carton had "
            "arrived without an invoice, she would still record the purchase (goods happened) but she "
            "would chase the invoice — occurrence is the gate; the voucher is the evidence we must file."
        )
    )
    parts.append(
        exam_ready_list(
            "A business transaction is a monetary event that changes the financial position of the business, has already occurred, and is supported by a voucher.",
            [
                "Tests: (i) measurable in rupees, (ii) affects the business entity, (iii) has happened, (iv) evidenced.",
                "Credit purchases, credit sales, outstanding expenses and drawings all qualify even when cash does not move.",
                "Non-transactions: quotations, orders not yet fulfilled, market-value changes, skill of the owner, personal events from the owner's own purse.",
                "Source documents: cash memo (cash deals), invoice (credit deals), debit note (we debit a person), credit note (we credit a person), cheque / bank paper, payslip, receipt, internal voucher.",
                "Illustration: Meera's unpaid electricity ₹2,000 is a transaction (accrued, evidenced by the bill). A school's request for a ₹50,000 quotation is not.",
            ],
            "In an exam, if you are unsure, run the four gates in the rough sheet before you write a journal.",
        )
    )
    parts.append(
        example(
            "B1",
            "Easy",
            "Circle the transactions",
            "<p>Which of the following will enter Meera's journal? State the gate that fails for the others.</p>"
            + ul(
                [
                    "Bought goods for cash ₹8,000. <em>Yes — all four gates.</em>",
                    "Received an order from a college for ₹15,000 goods, delivery next month. <em>No — has not happened (no delivery, no invoice).</em>",
                    "Owner's private scooter sold for ₹20,000, money kept in her private purse. <em>No — does not affect the shop (entity).</em>",
                    "Paid wages ₹2,000 cash. <em>Yes.</em>",
                    "A competitor opened a bigger shop next door. <em>No — not monetary, no voucher, not our event in rupees.</em>",
                ]
            ),
        )
    )
    parts.append(
        example(
            "B2",
            "Exam-level",
            "4 marks — 'What is a voucher? Distinguish cash memo, invoice, debit note and credit note.'",
            exam_ready(
                "A voucher is the documentary evidence, numbered and authorised, on the basis of which "
                "a journal entry is passed. It is prepared from a source document (or is itself the source document).",
                "A <strong>cash memo</strong> supports a cash sale or cash purchase. An <strong>invoice</strong> "
                "supports a credit sale or credit purchase. A <strong>debit note</strong> is sent to a person "
                "when we debit that person (typically a supplier, for goods returned or a claim). A "
                "<strong>credit note</strong> is sent to a person when we credit that person (typically a "
                "customer, for goods returned). The name follows the effect in <em>our</em> books.",
                "Illustration: Kabir's invoice of 5 April is the voucher for Dr Purchases ₹40,000, Cr Kabir. "
                "If 10 notebooks are later returned to him, Meera issues a debit note and passes Dr Kabir, "
                "Cr Purchases / Purchase returns.",
            ),
        )
    )
    parts.append(
        identify(
            "If the question lists mixed events and says <em>'pass journal entries'</em>, first strike out "
            "the non-transactions (orders, quotations, personal events from a private purse, market-value "
            "changes, hiring without a wage). Then journalise the rest. Marks are lost on the extra entries "
            "as much as on the missing ones. If it says <em>'name the source document'</em>, give the one-line "
            "name from the table above — do not write an essay on printing presses."
        )
    )
    return "".join(parts)


# ===========================================================================
# C. Accounting rules
# ===========================================================================

def _section_c() -> str:
    parts = []
    parts.append(h2("C. Accounting rules — Golden rules and Modern (equation) rules", "rules"))
    parts.append(
        definition(
            "Accounting rules decide, for each account touched by a transaction, whether it is "
            "<strong>debited</strong> or <strong>credited</strong>. Two equally correct systems are "
            "taught in India: the traditional <strong>Golden rules</strong> (based on Personal, Real "
            "and Nominal accounts) and the <strong>Modern rules</strong> (based on the accounting "
            "equation: assets, liabilities, capital, expenses, incomes). Use either in an exam; "
            "never mix the vocabulary inside one working."
        )
    )
    parts.append(
        simple(
            "You already know that every transaction has two sides (dual aspect). The rules answer "
            "the next question: <em>which</em> side is the debit? Golden rules ask 'what kind of "
            "account is this — a person, a thing, or an income/expense?' Modern rules ask 'which "
            "piece of the equation moved, and did it go up or down?' Both give the same journal."
        )
    )
    parts.append(
        why(
            "Without a rule you would guess. Guessing is how Cash is credited when it comes in, "
            "and how a student debits Sales. The rules are short, and they cover every transaction "
            "Meera will ever have — including outstanding electricity and drawings."
        )
    )
    parts.append(h3("Step 0 — classify the account, then apply a rule"))
    parts.append(
        p(
            "Both systems start with a classification. Get the classification wrong and the rule "
            "will be applied to the wrong object. This is the most common 1-mark leak in a 10-mark journal question."
        )
    )
    parts.append(
        table(
            ["Family (Golden)", "What lives here", "Modern name", "Normal balance", "Meera examples"],
            [
                [
                    b("Personal"),
                    "Persons, firms, banks, the owner, and 'representative' persons (outstanding, prepaid, accrued).",
                    "Capital; Liabilities (creditors, outstanding); Assets of a personal kind (debtors, bank)",
                    "Giver → Cr, Receiver → Dr. So capital / creditors / outstanding = Cr; debtors / bank = Dr.",
                    "Capital, Kabir, Sana, Bank, Drawings, Outstanding Electricity",
                ],
                [
                    b("Real"),
                    "Things the business owns — tangible (cash, furniture, stock, machinery) and intangible (patents, goodwill when purchased).",
                    "Assets",
                    "Debit what comes in, Credit what goes out. Asset balances are Debit.",
                    "Cash, Furniture. (Stock, when it appears later.)",
                ],
                [
                    b("Nominal"),
                    "Expenses, losses, incomes, gains. These are closed to P&L at year end; they belong to a period.",
                    "Expenses / Incomes",
                    "Debit all expenses and losses; Credit all incomes and gains.",
                    "Purchases, Sales, Rent, Wages, Electricity, Commission",
                ],
            ],
            caption="Three Golden families, mapped to the Modern equation",
            foot="Bank is Personal (the banker is a person) and also an Asset. Purchases is Nominal, not Real — we do not keep a 'Goods A/c' in this system.",
        )
    )
    parts.append(
        warn(
            "<strong>Purchases is not a Real account.</strong> Goods coming in feel like 'a thing', "
            "so students debit a Goods A/c or treat Purchases as Real. In the books you will write "
            "in this course, inward goods go to <em>Purchases A/c</em> (nominal) and outward goods "
            "go to <em>Sales A/c</em> (nominal). A Stock (real) account appears only when we value "
            "closing stock in final accounts. Treat this as a permanent exam trap."
        )
    )

    parts.append(h3("The three Golden rules (write these word-perfect)"))
    parts.append(
        table(
            ["Kind of account", "Debit", "Credit", "Memory"],
            [
                [b("Personal"), "the receiver", "the giver", "Who received the benefit? Debit them. Who gave it? Credit them."],
                [b("Real"), "what comes in", "what goes out", "Things: in = Dr, out = Cr. Cash in hand went out to the bank → Credit Cash, Debit Bank."],
                [b("Nominal"), "all expenses and losses", "all incomes and gains", "Bad news (cost) on the left. Good news (income) on the right."],
            ],
            caption="Golden rules of debit and credit",
        )
    )
    parts.append(
        format_box(
            "Golden rules — three lines to memorise",
            "<p><strong>Personal:</strong> Debit the receiver, Credit the giver.</p>"
            "<p><strong>Real:</strong> Debit what comes in, Credit what goes out.</p>"
            "<p><strong>Nominal:</strong> Debit all expenses and losses, Credit all incomes and gains.</p>",
        )
    )

    parts.append(h3("The Modern (equation) rules"))
    parts.append(
        p(
            "Start from Assets = Liabilities + Capital. Expenses and Drawings reduce capital; "
            "Incomes increase it. Five + one boxes, each with an increase side and a decrease side:"
        )
    )
    parts.append(
        table(
            ["Box", "Increase", "Decrease", "Normal balance", "Meera"],
            [
                [b("Assets"), "Debit", "Credit", "Debit", "Cash, Bank, Furniture, Sana (debtor)"],
                [b("Liabilities"), "Credit", "Debit", "Credit", "Kabir (creditor), Outstanding Electricity"],
                [b("Capital"), "Credit", "Debit", "Credit", "Capital A/c"],
                [b("Drawings"), "Debit", "Credit", "Debit", "Drawings A/c (contra-capital)"],
                [b("Expenses / Losses"), "Debit", "Credit", "Debit", "Purchases, Rent, Wages, Electricity"],
                [b("Incomes / Gains"), "Credit", "Debit", "Credit", "Sales, Commission"],
            ],
            caption="Modern debit-credit rules — DEAD CLIC lives here",
        )
    )
    parts.append(
        memory(
            "<strong>DEAD CLIC.</strong> Debit: Expenses, Assets, Drawings. "
            "Credit: Liabilities, Incomes, Capital. "
            "When the item <em>increases</em>, use its normal side. When it <em>decreases</em>, use the opposite side. "
            "Kabir is paid ₹15,000: a liability decreases → Debit Kabir (opposite of its normal credit)."
        )
    )
    parts.append(
        formula(
            "Assets + Expenses + Drawings  =  Liabilities + Capital + Incomes",
            "This is the trial-balance form of the equation. Left side = all normal-debit boxes. "
            "Right side = all normal-credit boxes. Meera's both sides = ₹2,80,000 on 30 April 2025.",
        )
    )

    parts.append(h3("Big classification table — decide the family before you debit"))
    parts.append(
        table(
            ["Account", "Golden family", "Modern box", "Increase is…", "Typical balance"],
            [
                ["Cash", "Real", "Asset", "Debit", "Dr"],
                ["Bank", "Personal (the banker) / treated as Real in some books", "Asset", "Debit", "Dr"],
                ["Furniture / Machinery / Building / Vehicle", "Real", "Asset", "Debit", "Dr"],
                ["Stock / Closing stock", "Real", "Asset", "Debit", "Dr"],
                ["Sana (debtor) / Bills receivable", "Personal", "Asset", "Debit", "Dr"],
                ["Prepaid rent / Accrued commission", "Representative personal", "Asset", "Debit", "Dr"],
                ["Purchases / Wages / Rent / Electricity / Carriage / Advertisement", "Nominal", "Expense", "Debit", "Dr"],
                ["Sales returns / Purchase of an expense nature", "Nominal", "Expense (or contra-income)", "Debit", "Dr"],
                ["Drawings", "Personal (the owner)", "Drawings / contra-capital", "Debit", "Dr"],
                ["Capital", "Personal (the owner)", "Capital", "Credit", "Cr"],
                ["Kabir (creditor) / Bills payable / Bank loan", "Personal", "Liability", "Credit", "Cr"],
                ["Outstanding electricity / Outstanding wages", "Representative personal", "Liability", "Credit", "Cr"],
                ["Sales / Commission / Interest received / Discount received", "Nominal", "Income", "Credit", "Cr"],
                ["Purchase returns", "Nominal", "Contra-expense / income-like", "Credit", "Cr"],
            ],
            caption="Classification table you can take into any journal question",
            foot="Bank: Personal under Golden rules (Debit the receiver = the banker when we deposit). Asset under Modern rules. Same entry either way: Dr Bank.",
        )
    )

    parts.append(h3("How to choose the two accounts — exam method"))
    parts.append(
        steps(
            [
                "Read the transaction twice. Ignore colour commentary ('happily', 'after a long bargain', 'a loyal customer').",
                "Ask: what two (or more) things changed in the shop? Cash? A person? An expense? An income? An asset?",
                "Give them their <em>book names</em>: goods bought → Purchases (not 'Goods'); goods sold → Sales (not 'Goods'); cash taken by owner → Drawings (not 'Meera' and not 'Expense'); unpaid electricity → Electricity and Outstanding Electricity (not 'Bill').",
                "Classify each name: Personal / Real / Nominal, or Asset / Liability / Capital / Expense / Income / Drawings.",
                "Apply the Golden rule or the Modern rule to each name. Write 'Dr …' and 'Cr …' in the rough sheet with amounts.",
                "Check dual aspect: total debit rupees = total credit rupees. If not, a third account is hiding (compound entry) or an amount is wrong.",
                "Only now write the formal journal: debit account first with 'Dr', credit account next indented with 'To', narration in brackets, L.F. blank.",
            ],
            title="7. Step-by-step — from a sentence to two accounts",
        )
    )
    parts.append(h3("A cheat-sheet that still needs a brain"))
    parts.append(
        table(
            ["If the sentence says…", "Usually debit", "Usually credit"],
            [
                ["Started business with cash / introduced capital in cash", "Cash", "Capital"],
                ["Opened bank and deposited cash / cash paid into bank", "Bank", "Cash"],
                ["Withdrew cash from bank for office", "Cash", "Bank"],
                ["Bought furniture / machine / vehicle for cash", "The asset", "Cash (or Bank if cheque)"],
                ["Bought goods for cash", "Purchases", "Cash"],
                ["Bought goods from X (credit)", "Purchases", "X (creditor)"],
                ["Sold goods for cash", "Cash", "Sales"],
                ["Sold goods to Y (credit)", "Y (debtor)", "Sales"],
                ["Paid rent / wages / electricity by cash or cheque", "The expense", "Cash or Bank"],
                ["Expense incurred but not paid (outstanding)", "The expense", "Outstanding … (liability)"],
                ["Received commission / interest / rent", "Cash or Bank", "The income"],
                ["Paid X (a creditor)", "X", "Cash or Bank"],
                ["Received from Y (a debtor)", "Cash or Bank", "Y"],
                ["Owner took cash / goods for personal use", "Drawings", "Cash (or Purchases if goods)"],
                ["Owner brought extra cash later", "Cash", "Capital"],
            ],
            caption="Sentence → two accounts (always still classify — this is a map, not a substitute for rules)",
        )
    )
    parts.append(
        logic(
            "Settlements are not new sales or new purchases. 'Received from Sana ₹10,000' does not "
            "touch Sales. 'Paid Kabir ₹15,000' does not touch Purchases. The original sale / purchase "
            "was recorded on 8 Apr / 5 Apr. Today we only swap a debtor for cash, or cut a creditor "
            "against bank. If you recast Sales every time a customer pays, you will double income "
            "and the trial balance may still agree — an error of principle that Section F cannot catch."
        )
    )

    parts.append(
        example(
            "C1",
            "Easy",
            "Same entry, two rule-languages — cash sales ₹18,000",
            "<p><strong>Golden.</strong> Cash is Real — cash comes in → Debit Cash. "
            "Sales is Nominal — income → Credit Sales.</p>"
            "<p><strong>Modern.</strong> Asset (Cash) increases → Debit. Income (Sales) increases → Credit.</p>"
            + journal(
                [
                    {
                        "date": "6 Apr 2025",
                        "debit": "Cash A/c",
                        "credit": "Sales A/c",
                        "amount": "18,000",
                        "narration": "Being goods sold for cash.",
                    }
                ],
                caption="Identical journal from either language",
            ),
        )
    )
    parts.append(
        example(
            "C2",
            "Moderate",
            "Personal + Nominal together — paid Kabir by cheque ₹15,000",
            "<p>Two accounts: Kabir (Personal / Liability) and Bank (Personal-asset / Asset).</p>"
            "<p><strong>Golden.</strong> Kabir is the receiver of money → Debit Kabir. "
            "Bank (the banker) is the giver → Credit Bank.</p>"
            "<p><strong>Modern.</strong> Liability to Kabir decreases → Debit Kabir. "
            "Asset Bank decreases → Credit Bank.</p>"
            "<p>Purchases is not in this entry. The goods were already debited on 5 April.</p>"
            + journal(
                [
                    {
                        "date": "12 Apr 2025",
                        "debit": "Kabir A/c",
                        "credit": "Bank A/c",
                        "amount": "15,000",
                        "narration": "Being part payment made to Kabir by cheque.",
                    }
                ]
            ),
        )
    )
    parts.append(
        example(
            "C3",
            "Exam-level",
            "Outstanding electricity — representative personal account",
            "<p>22 April, electricity ₹2,000 unpaid. Two accounts: Electricity (Nominal / Expense) "
            "and Outstanding Electricity (Representative Personal / Liability).</p>"
            "<p><strong>Golden.</strong> Debit all expenses → Debit Electricity. "
            "Outstanding Electricity is a personal account standing in place of the electricity "
            "company; that company is the giver of the service on credit → Credit Outstanding Electricity.</p>"
            "<p><strong>Modern.</strong> Expense increases → Debit Electricity. "
            "Liability increases → Credit Outstanding Electricity.</p>"
            "<p>Cash is not here. Accrual does not wait for cash. This single entry is where "
            "Entity (shop's bill), Accrual, Matching, Periodicity and Dual aspect all meet the rules.</p>",
        )
    )
    parts.append(
        exam_ready_list(
            "State the Golden rules of accounting and the modern rules of debit and credit.",
            [
                "Golden rules: Personal — Debit the receiver, Credit the giver. Real — Debit what comes in, Credit what goes out. Nominal — Debit all expenses and losses, Credit all incomes and gains.",
                "Modern rules (from Assets = Liabilities + Capital): increase in assets / expenses / drawings is Debit; increase in liabilities / capital / incomes is Credit. Decreases reverse the side.",
                "Classification must precede the rule. Purchases is nominal (expense), not real. Bank is personal (and an asset). Outstanding expense is a representative personal account (a liability).",
                "Illustration: goods sold to Sana ₹22,000 → Debit Sana (receiver / asset↑), Credit Sales (income↑). Later cash from Sana → Debit Cash, Credit Sana — Sales is not touched again.",
                "Both languages must produce the same journal. In an exam pick one language and stay with it.",
            ],
        )
    )
    parts.append(
        identify(
            "If the question says <em>'state the rules of debit and credit'</em>, write Golden and Modern "
            "as two short labelled blocks — do not ramble. If it gives transactions and says "
            "<em>'give the two accounts and the rule applied'</em>, make a four-column working: "
            "Transaction | Accounts | Type | Dr/Cr with rule in six words. If it says "
            "<em>'classify the following accounts'</em>, they want Personal / Real / Nominal "
            "(and you can add Asset / Liability / etc. in a second column for extra finish)."
        )
    )
    parts.append(
        mistakes(
            [
                "Debiting 'Goods A/c' instead of Purchases, or crediting 'Goods A/c' instead of Sales.",
                "Treating Bank as Real under Golden rules and then 'crediting Bank because cash came out of the bank' — the giver is the banker, so Credit Bank is correct, but the reason is Personal, not Real. (Modern: asset down → Credit Bank. Same entry.)",
                "Debiting Capital when the owner introduces cash (you must Credit Capital — the owner is the giver).",
                "Crediting Drawings when the owner takes cash (Drawings is the receiver → Debit Drawings).",
                "Using Sales when a debtor pays, or Purchases when a creditor is paid.",
                "Mixing Golden language ('receiver') with Modern language ('asset increases') in the same sentence of a 4-mark answer — pick a horse.",
            ]
        )
    )
    return "".join(parts)


# ===========================================================================
# D. Journal
# ===========================================================================

def _section_d() -> str:
    parts = []
    parts.append(h2("D. Journal — the chronological book of original entry", "journal"))
    parts.append(
        definition(
            "The <strong>journal</strong> is the book of original entry in which transactions are "
            "recorded, day by day, in chronological order, as they occur, each with a debit, a "
            "credit and a narration. It is the first formal writing of the dual aspect. From the "
            "journal, the same rupees are later copied (posted) into the ledger, account-wise."
        )
    )
    parts.append(
        simple(
            "A diary of the shop, written in a strict two-column language. Monday's events are "
            "above Tuesday's. Each event says: this account is debited, that account is credited, "
            "this is why. The journal does not tell you 'how much cash is left' — that is the "
            "ledger's job. The journal tells you 'what happened, in the order it happened'."
        )
    )
    parts.append(
        why(
            "Memory is a bad accountant. The journal (a) captures the story while it is fresh, "
            "(b) forces you to decide debit and credit <em>before</em> the figures are scattered "
            "across many ledger pages, (c) provides a narration that the ledger will not repeat, "
            "and (d) is the audit trail from voucher to ledger. That is why it is called the "
            "book of <em>original</em> entry — the ledger is a rearrangement, not the first writing."
        )
    )
    parts.append(
        real_life(
            "On 5 April Kabir's invoice lands at 4 p.m. Meera (or her accountant) writes one journal "
            "line that evening: Dr Purchases ₹40,000, To Kabir ₹40,000, narration, voucher number. "
            "She does not yet open Kabir's ledger page — that can wait for the posting session. "
            "If she posted to the ledger first, with no journal, a missing narration and a missing "
            "date-order would make errors very hard to find."
        )
    )
    parts.append(
        logic(
            "Journal = time order. Ledger = account order. Trial balance = a list of leftover "
            "balances. Financial statements = a regrouping of those balances into performance and "
            "position. You cannot skip the journal and still claim a clean audit trail. (Some small "
            "shops use 'journal proper' only for adjustments and put cash in a cash book — that is "
            "a later refinement. In this chapter every April event, cash or not, goes through the journal.)"
        )
    )

    parts.append(h3("Format of the journal"))
    parts.append(
        format_box(
            "Journal",
            "<p>Heading: Journal of (name of the business) for (period).</p>"
            "<table><thead><tr>"
            "<th>Date</th><th>Particulars</th><th>L.F.</th>"
            "<th>Debit (₹)</th><th>Credit (₹)</th>"
            "</tr></thead><tbody>"
            "<tr><td>1 Apr 2025</td><td>Cash A/c &nbsp;&nbsp;&nbsp; Dr.</td><td></td>"
            "<td class='num'>2,00,000</td><td></td></tr>"
            "<tr><td></td><td class='indent'>To Capital A/c</td><td></td>"
            "<td></td><td class='num'>2,00,000</td></tr>"
            "<tr><td></td><td colspan='4'><em>(Being cash introduced by Meera as capital…)</em></td></tr>"
            "</tbody></table>"
            "<p>Five columns. Debit account is written first, flush left, with <strong>Dr.</strong> at the end of the name. "
            "Credit account is written next, indented, beginning with <strong>To</strong>. "
            "Narration sits under the entry, in brackets, not posted to the ledger. "
            "L.F. (Ledger Folio) is the page number of the ledger account — filled only at the time of posting, left blank till then.</p>",
        )
    )
    parts.append(
        table(
            ["Column", "What you write", "What you never write"],
            [
                ["Date", "Date of the <em>transaction</em> (the invoice date, the cash-memo date).", "Date on which you sat down to write the books, if that is later."],
                ["Particulars", "Account titles as they will appear in the ledger, plus narration below.", "Long stories, customer addresses, 'goods' as an account name."],
                ["L.F.", "Ledger page number, at the moment of posting.", "A guess. Leave it blank in an exam unless folios are given."],
                ["Debit (₹)", "Amount of the debit account(s).", "A different figure from the credit 'because cash discount' you have not been told about."],
                ["Credit (₹)", "Amount of the credit account(s). Total of this column for the entry = total of Debit.", "A blank credit on a complete entry."],
            ],
            caption="The five columns, used correctly",
        )
    )

    parts.append(h3("Narration rules"))
    parts.append(
        ul(
            [
                "A narration is a one-line explanation of <em>why</em> the entry was passed. It starts traditionally with 'Being …'.",
                "It is written immediately under the debit and credit lines, in brackets or in italics, on the Particulars column.",
                "It is <strong>not posted</strong> to the ledger. The ledger has no narration column.",
                "It should mention the other party or the voucher identity when that helps ('from Kabir', 'by cheque').",
                "It should not repeat the account names mechanically ('Being cash and capital') without the business reason.",
                "Compound entries get one narration covering the whole event, not a narration per line.",
                "If the examiner says 'narrations are not required', skip them and save time. Otherwise always write them — they are cheap marks and they catch your own silly errors.",
            ]
        )
    )

    parts.append(h3("Compound entries"))
    parts.append(
        definition(
            "A <strong>compound (or combined) journal entry</strong> is one entry in which there "
            "are two or more debits, or two or more credits, or both, for a single event (or for "
            "several events of the same date that you are allowed to combine). Dual aspect still "
            "holds: <em>total</em> debit = <em>total</em> credit."
        )
    )
    parts.append(
        simple(
            "Sometimes one event touches three accounts. Meera might start the shop with cash "
            "AND furniture. One story, three accounts, one compound entry — not two simple entries "
            "(unless you prefer two; both are acceptable if the story is really two events)."
        )
    )
    parts.append(
        example(
            "D1",
            "Easy",
            "Compound entry that is NOT in Meera's books (teaching only)",
            "<p>Suppose, instead of bringing only cash, Meera had introduced cash ₹1,50,000 and "
            "furniture ₹50,000 on 1 April. One event, three accounts:</p>"
            + journal(
                [
                    {
                        "date": "1 Apr 2025",
                        "lines": [
                            {"account": "Cash A/c", "side": "dr", "amount": "1,50,000"},
                            {"account": "Furniture A/c", "side": "dr", "amount": "50,000"},
                            {"account": "Capital A/c", "side": "cr", "amount": "2,00,000"},
                        ],
                        "narration": "Being cash and furniture introduced by Meera as capital.",
                    }
                ],
                caption="Compound entry — two debits, one credit",
            )
            + "<p>Check: ₹1,50,000 + ₹50,000 = ₹2,00,000. Dual aspect holds. "
            "In the actual Meera books of this chapter she brought only cash, so we do <em>not</em> "
            "use this entry in the continuous example. Another common compound: rent ₹8,000 and "
            "wages ₹4,000 paid by one cheque on the same day → Dr Rent, Dr Wages, To Bank ₹12,000.</p>",
        )
    )
    parts.append(
        keypoint(
            "In a compound entry, debit lines are listed first (each with Dr. and its own amount), "
            "then credit lines (each with To). Do not write 'To Sundries' in an exam unless the "
            "question is old-style and many small credits would clutter the page; naming the actual "
            "accounts is always safer and is what MBA examiners expect."
        )
    )

    parts.append(h3("STEP-BY-STEP exam method to write a journal entry"))
    parts.append(
        steps(
            [
                "Read the transaction. Strike out any non-transaction (Section B four gates).",
                "Name the two (or more) accounts with their book titles (Purchases, not Goods; Drawings, not 'Meera took money').",
                "Classify each: Personal / Real / Nominal, or Asset / Liability / Capital / Expense / Income / Drawings.",
                "Apply Golden or Modern rules. In the rough sheet write: Dr (name) ₹x, Cr (name) ₹x.",
                "For a compound event, list every debit and every credit; add them; confirm equality.",
                "Copy into the journal format: Date | Debit name …… Dr. | | amount | (blank). Next row: (blank) | To Credit name | | (blank) | amount.",
                "Write the narration in brackets under the entry. Leave L.F. blank.",
                "Draw a line under the entry (in paper exams) so the next date does not merge into this one.",
                "Move to the next transaction. Do not post to the ledger until the whole journal of the period is written (in this chapter's method).",
            ],
            title="7. Step-by-step — writing one journal entry in the exam hall",
        )
    )

    parts.append(h3("Worked walk-through — every Meera journal, with the 'why'"))
    parts.append(
        p(
            "Below, each of the fifteen April events is journalised on its own, with classification "
            "and the one-line reason for the debit and the credit. After that you will see the",
            b("complete Journal of Meera Traders"),
            "as it would appear in the book. Amounts are round rupees, Indian commas. "
            "No depreciation. No closing stock. Outstanding electricity is included."
        )
    )

    for t in TXNS:
        parts.append(h4(f"{t['date']} — {t['story']}"))
        parts.append(
            journal(
                [
                    {
                        "date": t["date"],
                        "debit": t["debit"],
                        "credit": t["credit"],
                        "amount": inr(t["amt_n"]),
                        "narration": t["narration"],
                    }
                ],
                caption=f"Journal — {t['short']}",
            )
        )
        parts.append(raw_p(b("Why this debit / credit. "), e(t["why"])))

    parts.append(h3("Complete Journal of Meera Traders for April 2025"))
    parts.append(
        p(
            "This is the same fifteen entries in one book, which is what you present in an exam "
            "when the question says 'Journalise the following'."
        )
    )
    parts.append(
        journal(
            [
                {
                    "date": t["date"],
                    "debit": t["debit"],
                    "credit": t["credit"],
                    "amount": inr(t["amt_n"]),
                    "narration": t["narration"],
                }
                for t in TXNS
            ],
            caption="Journal of Meera Traders for April 2025",
        )
    )

    # Prove journal totals
    j_total = sum(t["amt_n"] for t in TXNS)
    parts.append(
        raw_p(
            b("Arithmetic check of the journal. "),
            f"There are 15 simple entries. The sum of the Debit column is "
            f"{rupee(j_total)} and the sum of the Credit column is {rupee(j_total)}. "
            f"Working: 2,00,000 + 1,50,000 + 25,000 + 20,000 + 40,000 + 18,000 + 22,000 + 8,000 "
            f"+ 15,000 + 10,000 + 4,000 + 5,000 + 2,000 + 3,000 + 10,000. "
            f"Step by step: 2,00,000 + 1,50,000 = 3,50,000; + 25,000 = 3,75,000; + 20,000 = 3,95,000; "
            f"+ 40,000 = 4,35,000; + 18,000 = 4,53,000; + 22,000 = 4,75,000; + 8,000 = 4,83,000; "
            f"+ 15,000 = 4,98,000; + 10,000 = 5,08,000; + 4,000 = 5,12,000; + 5,000 = 5,17,000; "
            f"+ 2,000 = 5,19,000; + 3,000 = 5,22,000; + 10,000 = {rupee(j_total)}. "
            "This is <em>not</em> the trial-balance total. The journal total double-counts the story "
            "(every rupee appears once as debit and once as credit, and many rupees move twice in "
            "the month — e.g. cash introduced and then banked). The trial balance total is the sum "
            "of leftover <em>balances</em>, which we will see is ₹2,80,000."
        )
    )
    parts.append(
        table(
            ["#", "Date", "Debit", "Credit", "₹", "Why this debit / credit (one line)"],
            [
                [
                    str(i + 1),
                    t["short"],
                    t["debit"],
                    t["credit"],
                    inr(t["amt_n"]),
                    t["why"],
                ]
                for i, t in enumerate(TXNS)
            ],
            caption="One-line debit/credit reason for every Meera journal — revision sheet",
        )
    )

    parts.append(
        example(
            "D2",
            "Moderate",
            "A mini-journal that is not Meera — 6 transactions of Arun Traders",
            "<p>Arun starts on 1 May 2025. Journalise. (This is practice of the method, not part of Meera's books.)</p>"
            + ul(
                [
                    "1 May — started with cash ₹1,00,000.",
                    "2 May — opened bank and deposited ₹70,000.",
                    "3 May — bought goods from Neha ₹25,000 on credit.",
                    "4 May — sold goods for cash ₹12,000.",
                    "5 May — rent outstanding ₹3,000 (not yet paid).",
                    "6 May — withdrew cash for personal use ₹2,000.",
                ]
            )
            + journal(
                [
                    {"date": "1 May 2025", "debit": "Cash A/c", "credit": "Capital A/c", "amount": "1,00,000",
                     "narration": "Being cash introduced by Arun as capital."},
                    {"date": "2 May 2025", "debit": "Bank A/c", "credit": "Cash A/c", "amount": "70,000",
                     "narration": "Being cash deposited into bank."},
                    {"date": "3 May 2025", "debit": "Purchases A/c", "credit": "Neha A/c", "amount": "25,000",
                     "narration": "Being goods purchased on credit from Neha."},
                    {"date": "4 May 2025", "debit": "Cash A/c", "credit": "Sales A/c", "amount": "12,000",
                     "narration": "Being goods sold for cash."},
                    {"date": "5 May 2025", "debit": "Rent A/c", "credit": "Outstanding Rent A/c", "amount": "3,000",
                     "narration": "Being rent for May remaining unpaid."},
                    {"date": "6 May 2025", "debit": "Drawings A/c", "credit": "Cash A/c", "amount": "2,000",
                     "narration": "Being cash withdrawn for personal use."},
                ],
                caption="Journal of Arun Traders (teaching example, not Meera)",
            )
            + "<p>Check the traps: 5 May does not credit Bank or Cash. 6 May does not debit Rent or Wages. "
            "3 May does not debit 'Neha' on the goods side — Neha is credited because she is the giver.</p>",
        )
    )

    parts.append(
        identify(
            "If the question gives a list of sentences and says <em>'Journalise'</em> / <em>'write journal entries'</em> / "
            "<em>'book of original entry'</em>, you stop at the journal — do not draw T-accounts unless asked. "
            "If it says <em>'journalise and post'</em>, journal first (all dates), then ledger. "
            "If it includes a quotation, a market-value change, or a personal event from a private purse, "
            "write 'No entry' with a six-word reason — that is a mark, not a skip. "
            "If two expenses are paid by one cheque, offer a compound entry."
        )
    )
    parts.append(
        mistakes(
            [
                "Writing the credit account first. Format is always Debit (Dr.) then To Credit.",
                "Forgetting 'To' before the credit account, or writing 'By' in the journal ('By' is a ledger word).",
                "Posting the narration to the ledger, or skipping the narration when the question did not waive it.",
                "Using 31 April as a date.",
                "Passing two entries for a deposit into bank (Dr Bank Cr Capital, then Dr Cash…) — it is Dr Bank, Cr Cash. Capital was already credited on day one.",
                "Crediting Sales when cash is received from a debtor.",
                "Leaving debit and credit amounts unequal in a compound entry.",
            ]
        )
    )
    parts.append(
        exam_ready_list(
            "What is a journal? Give its format and the rules for recording entries.",
            [
                "Meaning: the journal is the book of original entry in which transactions are recorded chronologically, each with equal debit and credit and a narration.",
                "Format: Date | Particulars | L.F. | Debit (₹) | Credit (₹). Debit account is written first with 'Dr.'; credit account next, indented, with 'To'. Narration in brackets below. L.F. is the ledger page, filled at posting.",
                "Rules: only business transactions; dual aspect; Golden or Modern rules to choose sides; compound entries when one event has more than two accounts; total Dr = total Cr.",
                "Utility: chronological record, audit trail from voucher, narration preserved, basis for posting to the ledger, errors easier to locate than in a ledger-only system.",
                "Illustration: Meera Traders, 1–30 April 2025, fifteen journals totalling ₹5,32,000 on each column, from which fourteen ledger accounts are posted (Section E) and a trial balance of ₹2,80,000 is drawn (Section F).",
            ],
        )
    )
    return "".join(parts)


# ===========================================================================
# E. Ledger
# ===========================================================================

def _section_e() -> str:
    parts = []
    parts.append(h2("E. Ledger — the account-wise book of final entry", "ledger"))
    parts.append(
        definition(
            "The <strong>ledger</strong> is the principal book of account in which every account "
            "named in the journal is given its own page (or T-account), and all debits and credits "
            "of that account are collected. It is a rearrangement of the journal: the journal is "
            "date-wise, the ledger is account-wise. Balancing the ledger tells us, for each account, "
            "what is left at the end of the period."
        )
    )
    parts.append(
        simple(
            "The journal is a movie (events in order). The ledger is a set of character files "
            "(everything that happened to Cash in one place, everything that happened to Kabir "
            "in another). If someone asks 'how much does Meera still owe Kabir?' you do not re-read "
            "fifteen journals — you open Kabir's page and read the balance."
        )
    )
    parts.append(
        why(
            "A journal cannot answer account-wise questions. 'What is cash in hand?' needs every "
            "cash debit and every cash credit added, which is exactly the Cash ledger. "
            "The ledger is also the only place we <em>balance</em> an account. Without balances "
            "there is no trial balance and no Balance Sheet. That is why the ledger is called the "
            "book of <em>final</em> entry (the journal was original entry)."
        )
    )
    parts.append(
        real_life(
            "On 30 April a supplier calls: 'Meera, what is outstanding on my account?' She opens "
            "Kabir A/c: credit purchases ₹40,000 + ₹10,000, minus a cheque of ₹15,000, balance "
            "₹35,000 credit. One page, ten seconds. The journal would have taken her a hunt across "
            "three dates (5, 12, 28 April)."
        )
    )
    parts.append(
        logic(
            "Journal first, ledger second — always. If you open the Cash T-account and invent "
            "figures without a journal, you have no narration, no voucher link, and no proof that "
            "the other side was posted. Double entry is 'every journal line has a home in a ledger "
            "page', not 'write T-accounts from memory'."
        )
    )

    parts.append(h3("Format of a ledger account (T-form)"))
    parts.append(
        format_box(
            "Ledger account (T-form)",
            "<p>The page is split down the middle. Left = Debit. Right = Credit. The name of the "
            "account sits on the top, with 'Dr' on the left and 'Cr' on the right.</p>"
            "<p>Full textbook columns on <em>each</em> side: Date | Particulars | J.F. | Amount. "
            "J.F. is the journal folio (page of the journal from which this line was posted) — "
            "the mirror of L.F. in the journal.</p>"
            "<p>In this chapter the T-accounts are drawn in a compact teaching form "
            "(Particulars | ₹ on each side) so that you can see the arithmetic. In a paper exam, "
            "add the Date and J.F. columns if the question shows that ruling.</p>"
            "<p><strong>Particulars convention:</strong> on the debit side you write "
            "<em>To (name of the other account)</em>. On the credit side you write "
            "<em>By (name of the other account)</em>. 'To' and 'By' are ledger words. "
            "The journal used 'Dr' and 'To'; the ledger uses 'To' (debit side) and 'By' (credit side).</p>",
        )
    )
    parts.append(
        table(
            ["Side", "You write", "It means"],
            [
                ["Debit (left)", "To Capital / To Sales / To Sana / To Balance c/d", "This account was debited; the name after 'To' is the other account in the journal (or a balancing figure)."],
                ["Credit (right)", "By Cash / By Purchases / By Balance c/d", "This account was credited; the name after 'By' is the other account in the journal (or a balancing figure)."],
            ],
            caption="'To' lives on the left; 'By' lives on the right",
        )
    )

    parts.append(h3("Posting rules"))
    parts.append(
        steps(
            [
                "Open a ledger account for every name that appears in the Particulars column of the journal (not for the narration).",
                "Take the first journal entry. The account that was debited in the journal gets a line on its <em>debit</em> side: Date, 'To (credit account's name)', amount. The amount is the same rupee figure.",
                "The account that was credited in the journal gets a line on its <em>credit</em> side: Date, 'By (debit account's name)', amount. Same rupees.",
                "Fill L.F. in the journal with the ledger page, and J.F. in the ledger with the journal page. (In exams these are often left blank.)",
                "Repeat for every journal entry, including compound entries (each debit line and each credit line is posted separately).",
                "Narrations are not posted. Totals of the journal are not posted. Only the account lines move.",
                "After the last posting of the period, balance every account (next sub-section).",
            ],
            title="7. Step-by-step posting method",
        )
    )
    parts.append(
        keypoint(
            "Posting in one sentence: <strong>debit in the journal → debit side of that account; "
            "credit in the journal → credit side of that account.</strong> The 'other account' "
            "is what you write after To / By. Never write 'To Cash' on the Cash account's own debit "
            "side for a cash introduction — Cash's debit side says <em>To Capital</em>, because "
            "Capital is the other name in that journal."
        )
    )

    parts.append(h3("Balancing an account"))
    parts.append(
        definition(
            "<strong>Balancing</strong> means finding the difference between the two sides of an "
            "account and writing that difference on the <em>smaller</em> side as "
            "<em>Balance c/d</em> (carried down), so that both sides total the same. The same "
            "figure is brought down on the <em>opposite</em> side as <em>Balance b/d</em> "
            "(brought down) at the start of the next period. A debit balance sits on the credit "
            "side as c/d (to make the sides equal) and comes back on the debit side as b/d."
        )
    )
    parts.append(
        steps(
            [
                "Add the debit side. Add the credit side. Show the additions in the rough sheet — never skip the arithmetic.",
                "The bigger total is the total you will write on <em>both</em> sides.",
                "Difference = bigger total − smaller total. This difference is the balance.",
                "Write 'Balance c/d' on the <em>smaller</em> side, with the difference as the amount, dated the last day of the period (30 Apr 2025).",
                "Write 'Total' on both sides — they are now equal.",
                "On the first day of the next period (1 May 2025), write 'Balance b/d' on the <em>bigger</em> side (the side that originally won). A debit-balance account opens with To Balance b/d; a credit-balance account opens with By Balance b/d.",
                "If both sides are already equal and non-zero, the account is closed (nil balance) — rare in this chapter. If an account has only one line, you still balance it so that the c/d is visible for the trial balance.",
            ],
            title="7. Step-by-step balancing method",
        )
    )
    parts.append(
        table(
            ["If…", "Balance c/d is written on…", "Nature of balance", "Goes to trial balance on…", "Examples in Meera"],
            [
                ["Debit total > Credit total", "Credit side", "Debit balance", "Debit column", "Cash, Bank, Furniture, Purchases, Sana, Rent, Wages, Drawings, Electricity"],
                ["Credit total > Debit total", "Debit side", "Credit balance", "Credit column", "Capital, Sales, Kabir, Outstanding Electricity, Commission"],
            ],
            caption="Reading a balance from a T-account",
        )
    )
    parts.append(
        memory(
            "The balance c/d sits on the <strong>poor</strong> (smaller) side, like a guest who "
            "makes the two teams equal. The balance b/d returns to the <strong>rich</strong> side "
            "the next morning. Debit-balance accounts are assets / expenses / drawings. "
            "Credit-balance accounts are liabilities / capital / incomes."
        )
    )

    parts.append(h3("Posting Meera's fifteen journals — every ledger, balanced"))
    parts.append(
        p(
            "Each T-account below is posted from the journal in Section D. Particulars use the "
            "'To / By (other account)' convention, with the date. Balance c/d is on 30 April 2025. "
            "Totals on both sides are equal. The arithmetic is shown under every account. "
            "Fourteen accounts are opened — one for every name that appeared in the journal."
        )
    )

    # Every ledger that appeared in the journal, posted and balanced.
    for name in LEDGER_ORDER:
        parts.append(h4(name))
        parts.append(_ledger_intro(name))
        parts.append(BOOKS[name]["html"])

    parts.append(h3("Posting cross-check of the ledgers"))
    parts.append(
        p(
            "Before we move to the trial balance, confirm that every journal rupee landed somewhere. "
            "For each journal, the debit amount must appear on the debit side of the debit account, "
            "and the credit amount on the credit side of the credit account. A quick account-wise "
            "recap of the <em>pre-balancing</em> totals:"
        )
    )
    recap_rows = []
    for name in LEDGER_ORDER:
        rec = BOOKS[name]
        recap_rows.append(
            [
                name,
                inr(rec["dr_tot"]),
                inr(rec["cr_tot"]),
                rec["nature"] + " " + inr(rec["bal"]),
            ]
        )
    parts.append(
        table(
            ["Account", "Debit postings (₹)", "Credit postings (₹)", "Balance c/d"],
            recap_rows,
            caption="Ledger recap of Meera Traders, 30 April 2025 — before drawing the trial balance",
            foot="Debit-posting column total and credit-posting column total both equal the journal column total ₹5,32,000, because posting copies both sides. Balances are the differences, and those differences are what the trial balance lists.",
        )
    )
    post_dr = sum(BOOKS[n]["dr_tot"] for n in LEDGER_ORDER)
    post_cr = sum(BOOKS[n]["cr_tot"] for n in LEDGER_ORDER)
    parts.append(
        raw_p(
            b("Posting proof. "),
            f"Sum of all debit postings across all ledgers = {rupee(post_dr)}. "
            f"Sum of all credit postings = {rupee(post_cr)}. "
            "These equal the journal column total. If they did not, a line was posted to the wrong "
            "side or skipped. This proof is not the trial balance — the trial balance uses "
            f"balances, not these raw postings. The balances themselves add to {rupee(TB_DR_TOTAL)} "
            "on each side, which is the next section."
        )
    )

    parts.append(
        example(
            "E1",
            "Easy",
            "Post one journal into two T-accounts",
            "<p>Journal of 3 April: Dr Furniture ₹25,000, To Cash ₹25,000.</p>"
            "<p>Furniture is debited in the journal → debit side of Furniture A/c: <em>3 Apr To Cash 25,000</em>.</p>"
            "<p>Cash is credited in the journal → credit side of Cash A/c: <em>3 Apr By Furniture 25,000</em>.</p>"
            "<p>Furniture has no other line this month, so it is balanced: By Balance c/d ₹25,000 "
            "on the credit side, total ₹25,000 both sides, To Balance b/d ₹25,000 on 1 May.</p>",
        )
    )
    parts.append(
        example(
            "E2",
            "Exam-level",
            "Balance the Cash account from scratch (show every addition)",
            "<p>Debit side of Cash (money in):</p>"
            + ul(
                [
                    "1 Apr To Capital = ₹2,00,000",
                    "6 Apr To Sales = ₹18,000",
                    "15 Apr To Sana = ₹10,000",
                    "25 Apr To Commission = ₹3,000",
                    "Debit total = 2,00,000 + 18,000 = 2,18,000; + 10,000 = 2,28,000; + 3,000 = <strong>₹2,31,000</strong>",
                ]
            )
            + "<p>Credit side of Cash (money out):</p>"
            + ul(
                [
                    "2 Apr By Bank = ₹1,50,000",
                    "3 Apr By Furniture = ₹25,000",
                    "4 Apr By Purchases = ₹20,000",
                    "18 Apr By Wages = ₹4,000",
                    "20 Apr By Drawings = ₹5,000",
                    "Credit total = 1,50,000 + 25,000 = 1,75,000; + 20,000 = 1,95,000; + 4,000 = 1,99,000; + 5,000 = <strong>₹2,04,000</strong>",
                ]
            )
            + f"<p>Bigger side is Debit ₹2,31,000. Difference = 2,31,000 − 2,04,000 = <strong>{rupee(27000)}</strong>. "
            "Write By Balance c/d ₹27,000 on the credit side. Both sides now total ₹2,31,000. "
            "Nature: Debit balance ₹27,000 = cash in hand on 30 April 2025. "
            "On 1 May: To Balance b/d ₹27,000 on the debit side of Cash.</p>"
            + BOOKS["Cash A/c"]["html"],
        )
    )

    parts.append(
        identify(
            "If the question says <em>'post to ledger'</em> / <em>'prepare ledger accounts'</em> / "
            "<em>'show T-accounts'</em>, they want every account opened, posted, and balanced, with "
            "totals. If it says <em>'prepare the Cash Book'</em>, that is a specialised ledger (later "
            "refinement) — in this chapter Cash is an ordinary T-account. If it says "
            "<em>'balance the following account'</em>, show both sides, c/d on the smaller, totals, "
            "and state the nature of the balance in a line underneath. If journal is not asked, you "
            "may still sketch it in rough — posting from thin air costs marks."
        )
    )
    parts.append(
        mistakes(
            [
                "Writing 'To Cash' on the debit of Cash (the other account must be named: To Capital, To Sales, To Sana, To Commission).",
                "Using 'By' on the debit side or 'To' on the credit side.",
                "Putting Balance c/d on the bigger side. c/d always pads the smaller side.",
                "Forgetting to bring down Balance b/d, or bringing it down on the same side as c/d.",
                "Posting the narration. Posting the journal totals as if they were an account.",
                "Skipping an account that appeared only once (Commission, Furniture, Drawings) — it still needs a page and a balance.",
                "Balancing Capital onto the debit column of the trial balance (Capital is a credit balance).",
            ]
        )
    )
    parts.append(
        exam_ready_list(
            "What is a ledger? Distinguish it from a journal and explain balancing of an account.",
            [
                "A ledger is the principal book in which a separate account is opened for every account named in the journal, and all debits and credits of that account are posted. It is account-wise; the journal is date-wise.",
                "Journal is the book of original entry (first recording, with narration). Ledger is the book of final entry (classified recording, source of balances). L.F. in the journal points to the ledger page; J.F. in the ledger points back to the journal page.",
                "Posting rule: a debit in the journal is written on the debit side of that account as 'To (other account)'; a credit in the journal is written on the credit side as 'By (other account)'.",
                "Balancing: total both sides; write Balance c/d on the smaller side so that sides agree; bring the same figure down on the opposite side as Balance b/d next period. Debit balance = assets / expenses / drawings. Credit balance = liabilities / capital / incomes.",
                "Illustration: Meera's Cash A/c debit postings ₹2,31,000, credit postings ₹2,04,000, Balance c/d ₹27,000 (debit). Kabir A/c credit postings ₹50,000, debit postings ₹15,000, Balance c/d ₹35,000 (credit).",
            ],
        )
    )
    parts.append(
        connect(
            "Fourteen balances are now sitting in the ledgers. The next — and last — book of this "
            "chapter is a list of those balances, debit column versus credit column. If dual aspect "
            "and posting were both honest, the two columns will be equal. That list is the trial balance."
        )
    )
    return "".join(parts)


def _ledger_intro(name: str) -> str:
    notes = {
        "Cash A/c": "Real / Asset. Debit what comes in, credit what goes out. Four inflows, five outflows.",
        "Bank A/c": "Personal (banker) and an Asset. One deposit, two payments by cheque.",
        "Capital A/c": "Personal / Capital. Credited once, on 1 April. Credit balance = owner's claim.",
        "Furniture A/c": "Real / Asset. One purchase, at historical cost. No depreciation in this chapter.",
        "Purchases A/c": "Nominal / Expense. Three inward lots of goods (cash + two credit). Not a Real 'Goods' account.",
        "Sales A/c": "Nominal / Income. Cash sales + credit sales. Not credited again when Sana pays.",
        "Kabir A/c": "Personal / Liability (creditor). Two credit purchases, one part-payment.",
        "Sana A/c": "Personal / Asset (debtor). One credit sale, one part-collection.",
        "Rent A/c": "Nominal / Expense. Paid by cheque — Bank is credited, not Cash.",
        "Wages A/c": "Nominal / Expense. Paid in cash.",
        "Drawings A/c": "Personal (owner) / contra-capital. Debit balance. Not an expense, not in P&L as a cost.",
        "Electricity A/c": "Nominal / Expense. Debited although unpaid — accrual.",
        "Outstanding Electricity A/c": "Representative personal / Liability. Will be paid in May; until then it is a creditor-like balance.",
        "Commission A/c": "Nominal / Income. Cash received. Credit balance.",
    }
    return p(notes[name])


# ===========================================================================
# F. Trial Balance
# ===========================================================================

def _section_f() -> str:
    parts = []
    parts.append(h2("F. Trial Balance", "trial-balance"))
    parts.append(
        definition(
            "A <strong>trial balance</strong> is a statement (not a book, not an account) that lists "
            "every ledger balance on a given date, with debit balances in one column and credit "
            "balances in the other. If double entry and posting have been arithmetically honest, "
            "the two columns are equal. It is a test of arithmetical accuracy, a summary of the "
            "ledger, and the raw material of the financial statements that come in later chapters."
        )
    )
    parts.append(
        simple(
            "Take the last line of every T-account — the Balance c/d, flipped back to its true "
            "side — and copy it onto a two-column list. Assets, expenses and drawings on the left. "
            "Liabilities, capital and incomes on the right. Add. If the additions match, the books "
            "are arithmetically in balance. They are not necessarily <em>correct</em> (Section F "
            "will show you errors a trial balance cannot see)."
        )
    )
    parts.append(
        why(
            "Without a trial balance you would walk into the Trading Account with unbalanced books "
            "and a profit figure you cannot trust. With it, you (a) catch unequal postings, "
            "(b) get a one-page photograph of every account, and (c) have a starting sheet for "
            "final accounts. It is the bouncer at the door between the ledger and the financial statements."
        )
    )
    parts.append(
        real_life(
            "On 30 April Meera's accountant balances fourteen T-accounts, copies the fourteen "
            "balances onto a sheet headed 'Trial Balance of Meera Traders as at 30 April 2025', "
            "and adds. Both columns are ₹2,80,000. She can now, in a later chapter, build a "
            "Trading and Profit and Loss Account and a Balance Sheet from this sheet, after "
            "adjustments (closing stock, depreciation) that we are deliberately not making yet."
        )
    )
    parts.append(
        logic(
            "Why must the columns agree? Because of dual aspect: every debit had an equal credit "
            "in the journal, and posting copied both sides. The leftover differences (balances) "
            "are just a regrouping of those equal pairs, so they too must be equal. "
            "Formally: Assets + Expenses + Drawings = Liabilities + Capital + Incomes."
        )
    )

    parts.append(h3("Which balances go where"))
    parts.append(
        table(
            ["Debit column of the trial balance", "Credit column of the trial balance"],
            [
                [
                    "Assets (Cash, Bank, Furniture, Debtors, Stock when given, Prepaid expenses)",
                    "Liabilities (Creditors, Outstanding expenses, Loans, Bank overdraft)",
                ],
                [
                    "Expenses and losses (Purchases, Rent, Wages, Electricity, Carriage, Sales returns)",
                    "Incomes and gains (Sales, Commission, Interest received, Purchase returns)",
                ],
                [
                    "Drawings (and any other contra-capital debit)",
                    "Capital (and any reserve, in a company)",
                ],
            ],
            caption="DEAD on the debit; CLIC on the credit",
        )
    )
    parts.append(
        memory(
            "Trial balance columns = <strong>DEAD | CLIC</strong>. "
            "Debit: Expenses, Assets, Drawings. Credit: Liabilities, Incomes, Capital. "
            "If you have parked Purchases on the credit, you have classified it as an income — stop."
        )
    )

    parts.append(h3("Format"))
    parts.append(
        format_box(
            "Trial Balance (balances method)",
            "<p><strong>Trial Balance of (name) as at (date)</strong></p>"
            "<p>Columns: S. No. | Name of account | L.F. | Debit (₹) | Credit (₹)</p>"
            "<p>One line per account that has a leftover balance. Accounts with a nil balance may "
            "be omitted. Totals of the two amount columns are written on the last row and must agree.</p>"
            "<p>Three methods exist. <strong>Balances method</strong> (used here, and in almost every "
            "exam) lists balances. <strong>Totals method</strong> lists the raw debit total and credit "
            "total of each ledger (before balancing) — both grand totals still agree, but the sheet "
            "is bulkier and is not used to prepare final accounts. <strong>Totals-cum-balances</strong> "
            "shows both. Always use the balances method unless the question forces another.</p>",
        )
    )

    parts.append(h3("Meera's Trial Balance as at 30 April 2025"))
    parts.append(
        p(
            "Copied from the Balance c/d of every ledger in Section E. April has 30 days, so the "
            "date is 30 April 2025, not 31 April. Closing stock is not on this trial balance because "
            "we did not pass a closing-stock entry. Depreciation is not on it because we did not "
            "charge any. Purchases of ₹70,000 include goods still in the shop — do not read this "
            "sheet as a Profit and Loss Account."
        )
    )

    tb_rows = []
    n = 1
    # Present in a conventional order: assets, drawings, expenses, then capital, liabilities, incomes
    debit_order = [
        "Cash",
        "Bank",
        "Furniture",
        "Sana",
        "Drawings",
        "Purchases",
        "Rent",
        "Wages",
        "Electricity",
    ]
    credit_order = [
        "Capital",
        "Kabir",
        "Outstanding Electricity",
        "Sales",
        "Commission",
    ]
    dr_map = {n: a for n, a in TB_DR}
    cr_map = {n: a for n, a in TB_CR}

    for name in debit_order:
        tb_rows.append([str(n), name, "", inr(dr_map[name]), ""])
        n += 1
    for name in credit_order:
        tb_rows.append([str(n), name, "", "", inr(cr_map[name])])
        n += 1
    tb_rows.append(
        [
            "",
            b("Total"),
            "",
            b(inr(TB_DR_TOTAL)),
            b(inr(TB_CR_TOTAL)),
        ]
    )
    parts.append(
        table(
            ["S. No.", "Name of account", "L.F.", "Debit (₹)", "Credit (₹)"],
            tb_rows,
            caption="Trial Balance of Meera Traders as at 30 April 2025",
            foot="Totals equal. Dual aspect and posting both survive the test. This is the balances method.",
        )
    )

    parts.append(h4("Addition of the debit column — do not skip"))
    parts.append(
        ol(
            [
                f"Cash {rupee(27000)} + Bank {rupee(127000)} = {rupee(154000)}",
                f"{rupee(154000)} + Furniture {rupee(25000)} = {rupee(179000)}",
                f"{rupee(179000)} + Sana {rupee(12000)} = {rupee(191000)}",
                f"{rupee(191000)} + Drawings {rupee(5000)} = {rupee(196000)}",
                f"{rupee(196000)} + Purchases {rupee(70000)} = {rupee(266000)}",
                f"{rupee(266000)} + Rent {rupee(8000)} = {rupee(274000)}",
                f"{rupee(274000)} + Wages {rupee(4000)} = {rupee(278000)}",
                f"{rupee(278000)} + Electricity {rupee(2000)} = {rupee(TB_DR_TOTAL)}",
            ]
        )
    )
    parts.append(h4("Addition of the credit column — do not skip"))
    parts.append(
        ol(
            [
                f"Capital {rupee(200000)} + Kabir {rupee(35000)} = {rupee(235000)}",
                f"{rupee(235000)} + Outstanding Electricity {rupee(2000)} = {rupee(237000)}",
                f"{rupee(237000)} + Sales {rupee(40000)} = {rupee(277000)}",
                f"{rupee(277000)} + Commission {rupee(3000)} = {rupee(TB_CR_TOTAL)}",
            ]
        )
    )
    parts.append(
        keypoint(
            f"Debit total {rupee(TB_DR_TOTAL)} = Credit total {rupee(TB_CR_TOTAL)}. "
            "The trial balance ties. If your working copy does not, you have a posting or a "
            "balancing error — go back to the T-accounts; do not 'adjust' a balancing figure "
            "on the trial balance itself (that is the job of a suspense account, a later topic, "
            "and even then only after you have hunted)."
        )
    )

    parts.append(h4("The same numbers as the trial-balance equation"))
    parts.append(
        table(
            ["Left (normal-debit boxes)", "₹", "Right (normal-credit boxes)", "₹"],
            [
                ["Assets — Cash", inr(27000), "Capital", inr(200000)],
                ["Assets — Bank", inr(127000), "Liabilities — Kabir", inr(35000)],
                ["Assets — Furniture", inr(25000), "Liabilities — Outstanding Electricity", inr(2000)],
                ["Assets — Sana (debtor)", inr(12000), "Incomes — Sales", inr(40000)],
                ["Drawings", inr(5000), "Incomes — Commission", inr(3000)],
                ["Expenses — Purchases", inr(70000), "", ""],
                ["Expenses — Rent", inr(8000), "", ""],
                ["Expenses — Wages", inr(4000), "", ""],
                ["Expenses — Electricity", inr(2000), "", ""],
                [b("Total"), b(inr(TB_DR_TOTAL)), b("Total"), b(inr(TB_CR_TOTAL))],
            ],
            caption="Assets + Expenses + Drawings = Liabilities + Capital + Incomes",
        )
    )
    parts.append(
        warn(
            "<strong>Do not compute a fake profit from this sheet.</strong> "
            "Sales ₹40,000 + Commission ₹3,000 − Purchases ₹70,000 − Rent ₹8,000 − Wages ₹4,000 "
            "− Electricity ₹2,000 = a 'loss' of ₹41,000, but Purchases include unsold goods. "
            "Matching forbids this subtraction until closing stock is brought in. Chapter 1 stops "
            "at the trial balance. The shop is not loss-making just because the stock is still on "
            "the shelf. Write this sentence in the exam if you are asked 'comment on the performance' "
            "from a trial balance that has purchases and no closing stock: "
            "<em>Performance cannot be judged until the Trading Account is prepared with closing stock.</em>"
        )
    )

    parts.append(h3("What the trial balance DOES catch"))
    parts.append(
        table(
            ["Error", "Why the TB refuses to agree", "Meera-style picture"],
            [
                [
                    "Posted to one side only (partial omission of posting)",
                    "One account got the rupees, the other did not",
                    "Dr Purchases ₹40,000 posted, Cr Kabir forgotten → debit column ₹40,000 too big",
                ],
                [
                    "Unequal posting / different amounts on the two sides",
                    "Dr ≠ Cr for that pair",
                    "Rent ₹8,000 posted as Dr Rent ₹8,000, Cr Bank ₹800",
                ],
                [
                    "Posted twice on the same side",
                    "That column grows by the extra amount",
                    "Cash sale posted twice to Cash, once to Sales",
                ],
                [
                    "Balance of an account listed on the wrong side of the TB",
                    "A debit balance sitting in the credit column (or reverse) shifts the difference by twice the amount",
                    "Putting Drawings ₹5,000 in the credit column",
                ],
                [
                    "Wrong totalling of a ledger side or of the TB itself",
                    "Pure arithmetic",
                    "Cash debit side added as ₹2,21,000 instead of ₹2,31,000",
                ],
                [
                    "Balance omitted from the TB",
                    "That column is short",
                    "Forgetting to list Commission ₹3,000",
                ],
                [
                    "Transposition / slide on one side only (₹1,250 written as ₹1,520, or ₹8,000 as ₹800)",
                    "One side off by a difference that is often divisible by 9 (a hunting clue)",
                    "Wages ₹4,000 posted as ₹4,000 debit and ₹400 credit",
                ],
            ],
            caption="Errors that make the trial balance disagree",
        )
    )

    parts.append(h3("What the trial balance does NOT catch"))
    parts.append(
        table(
            ["Error", "Why the TB still agrees", "Meera-style picture"],
            [
                [
                    b("Error of omission") + " (complete)",
                    "Both debit and credit never entered, so both columns miss the same rupees",
                    "The 25 Apr commission of ₹3,000 is wholly left out of the journal",
                ],
                [
                    b("Error of omission of posting") + " (both sides skipped after journalising)",
                    "Journal has it; neither ledger is posted; balances miss both sides",
                    "Furniture journal written, Furniture A/c and Cash A/c never opened for it",
                ],
                [
                    b("Error of principle"),
                    "Wrong <em>class</em> of account, but Dr still equals Cr",
                    "Furniture ₹25,000 debited to Purchases instead of Furniture — TB agrees, assets understated, expenses overstated",
                ],
                [
                    b("Error of commission") + " (wrong account of the same class)",
                    "A personal account of one person instead of another; sides still equal",
                    "Credit sales to Sana posted to 'Sana' wrongly as 'Kabir' debit — still a personal debit",
                ],
                [
                    b("Compensating errors"),
                    "Two (or more) errors of equal amount cancel",
                    "Cash undercast by ₹1,000 and Sales undercast by ₹1,000",
                ],
                [
                    b("Wrong amount on both sides") + " (error of original entry)",
                    "Journal itself has the wrong rupees, posted faithfully both ways",
                    "Kabir's invoice ₹40,000 journalised as ₹4,000 Dr Purchases, Cr Kabir",
                ],
                [
                    b("Complete reversal"),
                    "Debit and credit swapped; amounts still equal",
                    "Dr Capital, Cr Cash for the 1 Apr introduction — TB agrees, Cash is a credit (absurd), Capital is a debit",
                ],
            ],
            caption="A trial balance that ties is not a certificate of truth",
        )
    )
    parts.append(
        keypoint(
            "A trial balance is a test of <em>arithmetic</em>, not of <em>principle</em>. "
            "It catches unequal posting and one-side misses. It does not catch omitted transactions, "
            "double omissions of posting, errors of principle, compensating errors, the same wrong "
            "amount on both sides, or a complete reversal. Examiners ask this list by heart."
        )
    )

    parts.append(h3("Objectives and limitations — exam-ready"))
    parts.append(
        exam_ready_list(
            "State the objectives (functions) of a trial balance.",
            [
                "To test the arithmetical accuracy of posting and balancing (dual aspect made visible).",
                "To summarise all ledger balances on one date, on one page.",
                "To help locate errors when the columns disagree (unequal posting, one side missed, wrong-side listing, totalling errors).",
                "To provide the opening sheet for preparing Trading A/c, Profit and Loss A/c and Balance Sheet (after adjustments in later chapters).",
                "To give a quick reading of assets, liabilities, incomes and expenses before the statements are drawn.",
            ],
            "Illustration: Meera's trial balance as at 30 April 2025 totals ₹2,80,000 both sides and is the photograph of her fourteen ledger balances.",
        )
    )
    parts.append(
        exam_ready_list(
            "State the limitations of a trial balance.",
            [
                "Agreement is not conclusive proof of accuracy — only of arithmetic equality of debits and credits.",
                "It does not detect: complete omission, omission of posting on both sides, error of principle, error of commission (wrong account of same class), compensating errors, wrong original amount on both sides, complete reversal.",
                "It does not prove that the profit is true (matching items such as closing stock, depreciation, outstanding/prepaid may still be missing — as they are, deliberately, in Chapter 1).",
                "It is not a financial statement and not a substitute for a Balance Sheet. A trial balance has expenses and incomes on it; a Balance Sheet does not.",
                "It cannot, by itself, say which account is wrong when it disagrees — it only raises the alarm. Location of the error needs a hunt (difference, divisibility by 9, comparison with journal).",
            ],
            "One-line close: a trial balance that agrees can still be wrong; a trial balance that disagrees is definitely arithmetically wrong.",
        )
    )

    parts.append(
        example(
            "F1",
            "Easy",
            "Place the balance — debit or credit column?",
            ol(
                [
                    "Cash ₹27,000 — <em>Debit (asset).</em>",
                    "Capital ₹2,00,000 — <em>Credit.</em>",
                    "Purchases ₹70,000 — <em>Debit (expense).</em>",
                    "Sales ₹40,000 — <em>Credit (income).</em>",
                    "Drawings ₹5,000 — <em>Debit (not an expense, but still a debit balance).</em>",
                    "Outstanding electricity ₹2,000 — <em>Credit (liability).</em>",
                    "Sana ₹12,000 — <em>Debit (debtor / asset).</em>",
                    "Kabir ₹35,000 — <em>Credit (creditor / liability).</em>",
                    "Commission ₹3,000 — <em>Credit (income).</em>",
                    "Furniture ₹25,000 — <em>Debit (asset).</em>",
                ]
            ),
        )
    )
    parts.append(
        example(
            "F2",
            "Moderate",
            "Will the trial balance agree? Six independent errors",
            "<p>Start from Meera's tying TB of ₹2,80,000. Take each error one at a time (not together) and say agree / disagree, and by how much if it disagrees.</p>"
            + ol(
                [
                    "The 25 Apr commission of ₹3,000 is completely omitted. <em>Agrees. Both sides miss ₹3,000. New totals ₹2,77,000. Error of omission.</em>",
                    "Furniture ₹25,000 is debited to Purchases instead of Furniture. <em>Agrees. Error of principle. Purchases becomes ₹95,000, Furniture disappears. Totals still ₹2,80,000. The Balance Sheet (later) will miss an asset.</em>",
                    "Rent posted Dr Rent ₹8,000, Cr Bank ₹800. <em>Disagrees. Credit column short by ₹7,200.</em>",
                    "Cash from Sana ₹10,000 credited to Sales instead of Sana. <em>Agrees. Error of principle / commission. Sales overstated, Sana's balance not reduced. Still equal.</em>",
                    "Wages ₹4,000 posted only to the debit of Wages, credit to Cash forgotten. <em>Disagrees. Debit column ₹4,000 too big.</em>",
                    "1 Apr capital entry reversed: Dr Capital, Cr Cash ₹2,00,000. <em>Agrees. Complete reversal. Cash would show a credit balance (nonsensical) but the columns would still match.</em>",
                ]
            ),
        )
    )
    parts.append(
        example(
            "F3",
            "Exam-level",
            "8 marks — prepare a trial balance from balances, then answer limitations",
            "<p><strong>Part A.</strong> You have already prepared Meera's TB above — that is the 8-mark numerical. "
            "Always: heading with name and date, L.F. column, DEAD on debit, CLIC on credit, totals equal, "
            "no closing stock invented.</p>"
            "<p><strong>Part B (5 marks theory, often attached).</strong> 'The agreement of a trial balance "
            "is not a conclusive proof of the accuracy of the books. Explain.'</p>"
            + exam_ready(
                "A trial balance agrees when the total of debit balances equals the total of credit balances. "
                "That equality follows from dual aspect and from posting both sides. It proves arithmetic "
                "equality, not the absence of every error.",
                "Errors that leave the equality intact include: complete omission of a transaction, omission "
                "of posting on both sides, error of principle (capital item treated as revenue or the reverse), "
                "error of commission (posted to the wrong account of the same class), compensating errors, "
                "recording the wrong amount on both sides, and complete reversal of an entry.",
                "Illustration: if Meera's furniture of ₹25,000 is debited to Purchases, the trial balance "
                "still totals ₹2,80,000, but the asset Furniture is missing and expenses are overstated. "
                "A true and fair view is lost even though the bouncer at the door smiled. Hence agreement "
                "is necessary but not sufficient.",
            ),
        )
    )

    parts.append(h3("Identify the question — journal, ledger, TB, or 'find the error'"))
    parts.append(
        identify(
            "<strong>If the question gives transactions and asks 'journalise'</strong> → stop at the journal "
            "(Section D method). Do not draw T-accounts unless asked. "
            "<strong>If it asks 'post to the ledger' / 'prepare accounts'</strong> → journal in rough if needed, "
            "then T-accounts, balance every account, show totals. "
            "<strong>If it asks 'prepare a trial balance'</strong> → you need balances. If transactions are given, "
            "you must journalise and post first (even if those workings are 'rough'), then list DEAD | CLIC, "
            "then add. Never invent closing stock. "
            "<strong>If it says 'the trial balance does not agree, find the error'</strong> → compute the difference; "
            "if divisible by 2, look for a balance on the wrong side; if divisible by 9, look for a transposition; "
            "look for an amount equal to the difference that was posted one side only. "
            "<strong>If it says 'TB agrees, yet the books are wrong — explain'</strong> → they want the limitations list "
            "(omission, principle, commission, compensating, original-entry, reversal), each with a one-line illustration. "
            "<strong>If it mixes theory</strong> ('is TB a conclusive proof?') with a numerical, split your answer: "
            "numerical first (marks are in the totals), theory second (the list)."
        )
    )
    parts.append(
        mistakes(
            [
                "Dating the TB 31 April, or 'for the year ended 30 April' (it is a statement <em>as at</em> a date, not an account 'for' a period — though incomes and expenses of the period appear on it).",
                "Putting Sales in the debit column and Purchases in the credit column.",
                "Putting Drawings in the credit column 'because it relates to the owner'. Drawings is a debit balance.",
                "Putting Outstanding electricity in the debit column 'because electricity is an expense'. The outstanding account is a liability.",
                "Adding closing stock on the debit of a Chapter-1 TB when no adjustment entry was passed. (When closing stock is given as an adjustment, it appears in the TB as a debit after the adjustment — that is a later chapter.)",
                "Calling a tying TB 'proof that the profit is correct'.",
                "Forcing the TB to agree by parking the difference in Capital. Hunt, or (later) use Suspense — do not silently corrupt Capital.",
            ]
        )
    )
    return "".join(parts)


# ===========================================================================
# G. Exam toolkit
# ===========================================================================

def _section_g() -> str:
    parts = []
    parts.append(h2("G. Common mistakes, memory tricks, exam tips — and the flow of the books", "exam-toolkit"))

    parts.append(h3("The accounting flow (memorise, then draw in 30 seconds)"))
    parts.append(
        format_box(
            "From a rupee event to the financial statements",
            "<p style='text-align:center; line-height:1.9'>"
            "<strong>TRANSACTION</strong> (a rupee event that passes the four gates)<br/>↓<br/>"
            "<strong>VOUCHER / SOURCE DOCUMENT</strong> (cash memo, invoice, cheque, payslip, debit/credit note, internal voucher)<br/>↓<br/>"
            "<strong>JOURNAL</strong> (book of original entry — chronological, with narration)<br/>↓<br/>"
            "<strong>LEDGER</strong> (book of final entry — account-wise T-accounts, posted, balanced)<br/>↓<br/>"
            "<strong>TRIAL BALANCE</strong> (statement of balances — arithmetical check)<br/>↓<br/>"
            "<strong>ADJUSTMENTS</strong> (closing stock, depreciation, outstanding/prepaid, more — later chapters)<br/>↓<br/>"
            "<strong>FINANCIAL STATEMENTS</strong> (Trading A/c → Profit and Loss A/c → Balance Sheet) "
            "— preview of later chapters; not prepared in Chapter 1"
            "</p>"
            "<p>Meera's Chapter 1 stops at the trial balance. The arrows after that are so you never "
            "think the TB is the last word. Profit lives in the Profit and Loss Account, not in the TB.</p>",
        )
    )
    parts.append(
        table(
            ["Stage", "Question it answers", "Order", "Meera in April"],
            [
                ["Transaction + voucher", "Did something real happen, in rupees, to the shop, with evidence?", "Event order", "15 events, each with a memo / invoice / cheque / internal voucher"],
                ["Journal", "What happened, on which date, Dr which, Cr which, why?", "Date order", "15 journals, column totals ₹5,32,000"],
                ["Ledger", "What is the story of this one account, and what is left?", "Account order", "14 T-accounts, each balanced on 30 Apr"],
                ["Trial balance", "Do all leftover balances still obey dual aspect?", "List of balances", f"As at 30 Apr 2025, totals {rupee(TB_DR_TOTAL)} both sides"],
                ["Statements (later)", "Did we make a profit, and what do we own/owe?", "Performance then position", "Not in this chapter (needs stock & depreciation)"],
            ],
            caption="Five stages, five questions",
        )
    )

    parts.append(h3("Memory sheet (one page, before you walk into the hall)"))
    parts.append(
        table(
            ["Idea", "Hook"],
            [
                ["Entity", "Owner = stranger. Household milk from the till = Drawings."],
                ["Money measurement", "No rupee, no record."],
                ["Going concern", "Not a garage sale tomorrow."],
                ["Cost", "Record the bill, not the dream price."],
                ["Dual aspect", "Two sides to every story; rupees equal."],
                ["Accrual", "Earned not received; incurred not paid."],
                ["Matching", "Pair the cost with the sale of the same period."],
                ["Prudence", "Hope for the best, provide for the worst (in the books)."],
                ["Consistency", "Don't change the scale."],
                ["Materiality", "Don't sweat the stapler; never hide the building."],
                ["Full disclosure", "Tell the whole truth a user needs."],
                ["Periodicity", "Cut the movie into episodes. Indian year: 1 Apr–31 Mar."],
                ["Revenue", "Sale is on the invoice, not on the cash."],
                ["Golden rules", "Personal: receiver Dr, giver Cr. Real: in Dr, out Cr. Nominal: expenses Dr, incomes Cr."],
                ["Modern / TB columns", "DEAD CLIC — Dr: Expenses Assets Drawings. Cr: Liabilities Incomes Capital."],
                ["Purchases vs Sales", "Inward goods → Purchases (never Goods A/c). Outward goods → Sales. Settlements do not retouch them."],
                ["Journal vs Ledger", "Journal = diary (date). Ledger = files (account). 'To' on Dr side of ledger, 'By' on Cr side."],
                ["Balancing", "c/d on the poor (smaller) side; b/d returns to the rich side next morning."],
                ["TB catches", "One side missed, unequal posting, wrong-side listing, totalling errors."],
                ["TB misses", "Omission, principle, commission, compensating, wrong amount both sides, reversal."],
                ["April", "Has 30 days. Date the TB 30 April 2025."],
            ],
            caption="Chant these on the bus to the exam centre",
        )
    )

    parts.append(h3("Common mistakes (the full charge-sheet)"))
    parts.append(
        mistakes(
            [
                "Mixing Meera the person with Meera Traders — personal fees from the till recorded as an expense instead of Drawings.",
                "Waiting for cash before recording credit purchases, credit sales, or outstanding electricity.",
                "Crediting Sales a second time when a debtor pays; debiting Purchases a second time when a creditor is paid.",
                "Debiting Goods A/c / Stock A/c for purchases in Chapter 1.",
                "Treating Bank deposit as Dr Bank, Cr Capital (Capital was already credited on day one).",
                "Writing 'By' in the journal, or writing the credit account first.",
                "Putting Balance c/d on the bigger side of a T-account.",
                "Listing Capital, Sales or Creditors in the debit column of the TB; listing Drawings or Purchases in the credit column.",
                "Inventing closing stock or depreciation to 'complete' Chapter 1. Do not.",
                "Computing Sales − Purchases from the TB and calling it profit.",
                "Dating anything 31 April.",
                "Calling a tying trial balance conclusive proof of accuracy.",
                "Skipping the four gates and journalising a quotation or a market-value change.",
                "Using 'To Sundries' to hide the fact that you cannot name the other account.",
            ]
        )
    )

    parts.append(h3("Exam tips"))
    parts.append(
        exam_tip(
            "Numerical questions are won in the rough sheet. Always: (1) four gates, (2) name the "
            "two accounts, (3) classify, (4) apply one language of rules, (5) check Dr = Cr, "
            "(6) only then copy into the ruling. A student who writes straight into the journal "
            "ruling reverses at least one entry every sitting."
        )
    )
    parts.append(
        exam_tip(
            "Theory questions are won with a definition, two points of explanation, one illustration, "
            "and one line of importance. Meera Traders is a legal illustration — use her rupees "
            "(₹2,00,000 capital, ₹2,000 outstanding electricity, ₹5,000 drawings, ₹22,000 credit "
            "sale to Sana). Examiners prefer a concrete rupee to a vague 'for example a firm'."
        )
    )
    parts.append(
        exam_tip(
            "Presentation: journal with narrations unless waived; ledger with To/By and totals; "
            "trial balance with a heading, a date 'as at 30 April 2025', and a total line that "
            "you have actually added (show the addition in rough). Neat rulings score; sprawling "
            "arrows do not. If a TB disagrees and you have two minutes left, write the difference "
            "and the most likely class of error — do not silently 'adjust' Capital."
        )
    )
    parts.append(
        exam_tip(
            "Time budget for a 15-mark 'journal, ledger, TB' question: 4 minutes journals, "
            "7 minutes ledgers (open all accounts before you post the first line, so you do not "
            "forget Commission), 3 minutes TB, 1 minute to re-add. Leave depreciation and stock "
            "alone unless the question asked for them."
        )
    )

    parts.append(h3("Practice"))
    parts.append(
        practice(
            "G1",
            "Easy",
            "Four gates and a concept",
            "<p>Meera is offered ₹32,000 for her furniture (cost ₹25,000) by a neighbouring café, "
            "for delivery next week. She is considering it. Is there a journal today? Which concepts "
            "decide the answer? If she accepts and delivers next week, what (in outline) will the "
            "entry be then?</p>",
            "<p><strong>Today:</strong> no journal. The offer is not a transaction (has not happened; "
            "no invoice). Cost concept and prudence also forbid writing the furniture up to ₹32,000. "
            "Money measurement does not let us record 'a good offer'.</p>"
            "<p><strong>On delivery next week:</strong> Dr Cash / Bank / Debtor ₹32,000; Cr Furniture "
            "₹25,000; Cr Profit on sale of furniture ₹7,000 (a nominal gain — realisation has now "
            "happened). That is a later-period entry, not April's. Going concern of April is not "
            "broken just because she is considering a sale.</p>",
        )
    )
    parts.append(
        practice(
            "G2",
            "Moderate",
            "Journal + one ledger + a question on TB",
            "<p>From Meera's books, without looking back: (a) journalise 12 Apr, 15 Apr and 22 Apr; "
            "(b) show Kabir's ledger after all April postings, balanced; (c) state two errors that "
            "would leave the trial balance still agreeing, using these three dates as illustrations.</p>",
            journal(
                [
                    {"date": "12 Apr 2025", "debit": "Kabir A/c", "credit": "Bank A/c", "amount": "15,000",
                     "narration": "Being part payment made to Kabir by cheque."},
                    {"date": "15 Apr 2025", "debit": "Cash A/c", "credit": "Sana A/c", "amount": "10,000",
                     "narration": "Being cash received from Sana against credit sales."},
                    {"date": "22 Apr 2025", "debit": "Electricity A/c", "credit": "Outstanding Electricity A/c",
                     "amount": "2,000",
                     "narration": "Being electricity charges for April remaining unpaid."},
                ],
                caption="(a) Three journals",
            )
            + "<p><strong>(b)</strong> Kabir A/c — Dr: 12 Apr To Bank 15,000; 30 Apr To Balance c/d 35,000. "
            "Cr: 5 Apr By Purchases 40,000; 28 Apr By Purchases 10,000. Totals 50,000 both sides. "
            "Credit balance ₹35,000.</p>"
            "<p><strong>(c)</strong> Complete omission of the 22 Apr outstanding entry: TB still agrees, "
            "expense and liability both missing (accrual failure too). Complete reversal of 15 Apr "
            "(Dr Sana, Cr Cash ₹10,000): TB still agrees, but Cash and Sana are both wrong. "
            "Error of principle on 12 Apr (Dr Purchases instead of Dr Kabir): TB still agrees, "
            "Purchases overstated, Kabir still showing ₹50,000.</p>",
        )
    )
    parts.append(
        practice(
            "G3",
            "Exam-level",
            "15 marks — the full cycle on a short set (not Meera, so you cannot copy)",
            "<p>Ruchi Traders, a book shop, started on 1 June 2025. Prepare Journal, Ledger (all "
            "accounts, balanced) and a Trial Balance as at 30 June 2025. Do not adjust closing stock. "
            "Do not charge depreciation.</p>"
            + ul(
                [
                    "1 Jun — Ruchi introduced cash ₹1,20,000.",
                    "2 Jun — Deposited ₹80,000 into bank.",
                    "4 Jun — Bought furniture by cheque ₹15,000.",
                    "5 Jun — Bought goods for cash ₹10,000 and from Omar on credit ₹30,000.",
                    "8 Jun — Cash sales ₹9,000; credit sales to Tara ₹16,000.",
                    "12 Jun — Paid Omar by cheque ₹12,000.",
                    "18 Jun — Received from Tara by cash ₹6,000.",
                    "20 Jun — Wages paid in cash ₹3,000; rent unpaid ₹4,000.",
                    "25 Jun — Ruchi took cash ₹2,000 for home.",
                    "28 Jun — Commission received in cash ₹1,000.",
                ]
            )
            + "<p>Hint: 5 Jun can be two simple entries or one compound (Dr Purchases ₹40,000; "
            "To Cash ₹10,000, To Omar ₹30,000). 20 Jun is two events: Dr Wages Cr Cash, and "
            "Dr Rent Cr Outstanding Rent. 8 Jun is two sales. Count the accounts before you open "
            "the ledgers: Cash, Bank, Capital, Furniture, Purchases, Omar, Sales, Tara, Wages, "
            "Rent, Outstanding Rent, Drawings, Commission.</p>"
            "<p><strong>Key balances you should land on (check after you finish):</strong> "
            "Cash — in: 1,20,000 + 9,000 + 6,000 + 1,000 = 1,36,000; out: 80,000 + 10,000 + 3,000 + 2,000 = 95,000; "
            "bal Dr ₹41,000. Bank — in 80,000; out 15,000 + 12,000 = 27,000; bal Dr ₹53,000. "
            "Purchases Dr ₹40,000. Sales Cr ₹25,000. Omar Cr ₹18,000. Tara Dr ₹10,000. "
            "Furniture Dr ₹15,000. Capital Cr ₹1,20,000. Drawings Dr ₹2,000. Wages Dr ₹3,000. "
            "Rent Dr ₹4,000. Outstanding Rent Cr ₹4,000. Commission Cr ₹1,000.</p>"
            "<p><strong>Trial Balance total:</strong> Dr: 41,000 + 53,000 + 15,000 + 40,000 + 10,000 + 2,000 + 3,000 + 4,000 = ₹1,68,000. "
            "Cr: 1,20,000 + 18,000 + 25,000 + 4,000 + 1,000 = ₹1,68,000. It must tie. "
            "If it does not, hunt — do not touch Capital.</p>",
        )
    )

    parts.append(h3("A last look at Meera — where every rupee sits on 30 April 2025"))
    parts.append(
        p(
            "If you can explain this table in one minute, the chapter has done its job."
        )
    )
    parts.append(
        table(
            ["Account", "Why it exists (one breath)", "Balance", "Side"],
            [
                ["Cash", "What is in the till after all inflows and outflows", rupee(27000), "Dr — asset"],
                ["Bank", "What is in the current account after the deposit and two cheques", rupee(127000), "Dr — asset"],
                ["Furniture", "Shelves and counter at historical cost, still going concern", rupee(25000), "Dr — asset"],
                ["Sana", "Credit customer who has not yet paid the remaining bill", rupee(12000), "Dr — asset (debtor)"],
                ["Drawings", "Shop cash Meera took home — owner is a stranger", rupee(5000), "Dr — contra-capital"],
                ["Purchases", "All goods bought in April, sold or unsold — no stock adjustment yet", rupee(70000), "Dr — expense"],
                ["Rent", "April's shop rent, matched to April, paid by cheque", rupee(8000), "Dr — expense"],
                ["Wages", "Helper's April wages, paid in cash", rupee(4000), "Dr — expense"],
                ["Electricity", "April's light, accrued, matched, not paid", rupee(2000), "Dr — expense"],
                ["Capital", "What the shop owes Meera for her 1 April introduction", rupee(200000), "Cr — capital"],
                ["Kabir", "Wholesaler still to be paid after one cheque", rupee(35000), "Cr — liability"],
                ["Outstanding Electricity", "The electricity company as a representative creditor", rupee(2000), "Cr — liability"],
                ["Sales", "Goods sold for cash and on credit — earned, not necessarily collected", rupee(40000), "Cr — income"],
                ["Commission", "Display commission earned and received", rupee(3000), "Cr — income"],
                [b("Trial balance"), b("Dual aspect, still standing"), b(rupee(TB_DR_TOTAL)), b("both sides")],
            ],
            caption="Meera Traders — the whole of Chapter 1 in fourteen balances",
        )
    )
    parts.append(
        connect(
            "Next chapters will take this same trial balance and (a) adjust closing stock so that "
            "Purchases can become Cost of goods sold, (b) charge depreciation on Furniture so that "
            "cost is matched over years, (c) prepare the Trading and Profit and Loss Account, and "
            "(d) prepare the Balance Sheet. None of that changes a single journal you wrote in April. "
            "Adjustments are additional journals. The fifteen entries of this chapter stay as they are."
        )
    )
    parts.append(
        qna(
            "Is a trial balance a conclusive proof of accuracy of the books? (5 marks)",
            exam_ready(
                "No. A trial balance is a test of arithmetical accuracy of double entry and posting. "
                "When it agrees, total debit balances equal total credit balances. That equality can "
                "survive serious errors.",
                "It will not reveal: complete omission of a transaction, omission of posting on both "
                "sides, error of principle (Meera's furniture debited to Purchases), error of commission, "
                "compensating errors, a wrong amount entered on both sides, or a complete reversal.",
                "It also says nothing about whether matching is complete (Meera's TB has no closing stock "
                "and no depreciation, by design). Therefore agreement is necessary before preparing "
                "final accounts, but it is not sufficient proof that the books are true and fair.",
            ),
            marks="5",
        )
    )
    parts.append(
        qna(
            "Distinguish between journal and ledger. (5 marks)",
            exam_ready(
                "The journal is the book of original entry. Transactions are recorded in it chronologically, "
                "each with a debit, a credit and a narration. The ledger is the book of final entry. "
                "Each account named in the journal is given a page, and the journal lines are posted "
                "to those pages, account-wise.",
                "Journal answers 'what happened today?'. Ledger answers 'what is the position of this "
                "account?'. Journal has an L.F. column pointing forward; ledger has a J.F. column "
                "pointing back. Narration lives only in the journal. Balancing is done only in the ledger.",
                "Illustration: Meera's 5 April credit purchase is one journal line (Dr Purchases, Cr Kabir). "
                "In the ledger it becomes one debit line on Purchases (To Kabir) and one credit line on "
                "Kabir (By Purchases). Kabir's page, after the 12 April payment and the 28 April reorder, "
                "shows a credit balance of ₹35,000 — a fact you cannot read off the journal at a glance.",
            ),
            marks="5",
        )
    )
    return "".join(parts)
