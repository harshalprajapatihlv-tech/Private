#!/usr/bin/env python3
"""Chapter 07 — Ratio Analysis. Beginner-to-exam teaching notes."""

from __future__ import annotations

import sys

sys.path.insert(0, "/workspace/notes")
from html_lib import *

# ---------------------------------------------------------------------------
# One company for the whole chapter: Kaveri Traders Ltd
# Year ended 31 March 2026. Every ratio is computed from these figures.
# Arithmetic is asserted below — if a number in the notes is wrong, this
# module will refuse to import.
# ---------------------------------------------------------------------------

SALES = 1_000_000
CASH_SALES = 200_000
CREDIT_SALES = 800_000
OP_STOCK = 80_000
CL_STOCK = 120_000
PURCHASES = 790_000
COGS = 750_000
GP = 250_000
EMP = 60_000
OTHER_OPEX = 40_000
OPEX = 100_000
OP_COST = 850_000
EBIT = 150_000
INTEREST = 30_000
PBT = 120_000
TAX = 30_000
PAT = 90_000
ESC = 400_000
RES = 200_000
SF = 600_000
LTD = 200_000
CL_ = 150_000  # current liabilities = trade payables
FA = 650_000
INV = 120_000
TR = 100_000
CASH = 80_000
CA = 300_000
TA = 950_000
OP_TR = 60_000
OP_CL = 110_000
SHARES = 40_000
FV = 10
AVG_INV = 100_000
AVG_TR = 80_000
AVG_CL = 130_000
WC = 150_000
CE = 800_000
QA = 180_000  # CA − inventory; no prepaid
TD = 350_000  # total debt = LTD + CL


def _assert_kaveri() -> None:
    assert CASH_SALES + CREDIT_SALES == SALES
    assert CREDIT_SALES == 4 * CASH_SALES
    assert OP_STOCK + PURCHASES - CL_STOCK == COGS
    assert SALES - COGS == GP
    assert EMP + OTHER_OPEX == OPEX
    assert GP - OPEX == EBIT
    assert COGS + OPEX == OP_COST
    assert EBIT - INTEREST == PBT
    assert PBT - TAX == PAT
    assert ESC + RES == SF
    assert INV + TR + CASH == CA
    assert FA + CA == TA
    assert SF + LTD + CL_ == TA
    assert CA - CL_ == WC
    assert SF + LTD == CE
    assert FA + WC == CE
    assert ESC // FV == SHARES
    assert (OP_STOCK + CL_STOCK) // 2 == AVG_INV
    assert (OP_TR + TR) // 2 == AVG_TR
    assert (OP_CL + CL_) // 2 == AVG_CL
    assert CA - INV == QA
    assert LTD + CL_ == TD
    assert CA / CL_ == 2
    assert QA / CL_ == 1.2
    assert abs(CASH / CL_ - 8 / 15) < 1e-12
    assert LTD / SF == 1 / 3
    assert TD / SF == TD / SF
    assert abs(SF / TA - 12 / 19) < 1e-12
    assert FA / CE == 13 / 16
    assert CA / SF == 0.5
    assert GP / SALES == 0.25
    assert PAT / SALES == 0.09
    assert EBIT / SALES == 0.15
    assert OP_COST / SALES == 0.85
    assert abs(OP_COST / SALES + EBIT / SALES - 1) < 1e-12
    assert COGS / AVG_INV == 7.5
    assert CREDIT_SALES / AVG_TR == 10
    assert abs(PURCHASES / AVG_CL - 79 / 13) < 1e-12
    assert SALES / WC == 20 / 3
    assert abs(SALES / FA - 20 / 13) < 1e-12
    assert SALES / CE == 1.25
    assert EBIT / CE == 0.1875
    assert PAT / SF == 0.15
    assert PAT / SHARES == 2.25
    assert EBIT / INTEREST == 5
    npm = PAT / SALES
    at = SALES / TA
    em = TA / SF
    assert abs(npm * at * em - PAT / SF) < 1e-12
    # reconstruction set B
    assert 2.5 * 100_000 - 100_000 == 150_000
    assert 1.5 * 100_000 == 150_000
    assert 250_000 - 150_000 == 100_000
    # reconstruction set C
    assert 5 * 40_000 == 200_000
    assert 200_000 / 0.80 == 250_000
    assert 250_000 - 200_000 == 50_000


_assert_kaveri()


def _pct(n: int, d: int, dp: int = 2) -> str:
    v = 100.0 * n / d
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v))}%"
    s = f"{v:.{dp}f}"
    return s + "%"


def _times(n: int | float, d: int | float, dp: int = 2) -> str:
    v = n / d
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v))} times"
    return f"{v:.{dp}f} times"


def _days(turns: float, dp: int = 2) -> str:
    return f"{(365.0 / turns):.{dp}f} days"


def _ratio_pair(n: int | float, d: int | float, dp: int = 2) -> str:
    v = n / d
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v))} : 1"
    return f"{v:.{dp}f} : 1"


def work_table(formula_s: str, pick_s: str, arith_s: str, answer_s: str) -> str:
    return table(
        ["Line of working", "What you write in the answer booklet"],
        [
            ["1. Formula", formula_s],
            ["2. Figures picked", pick_s],
            ["3. Arithmetic (nothing skipped)", arith_s],
            ["4. Answer with unit", b(answer_s)],
        ],
        caption="Four-line working — the examiner awards marks on each line",
        foot="If you jump from the formula to a final number, you lose method marks when the arithmetic slips.",
    )


def ratio_section(
    heading: str,
    bucket: str,
    ideal: str,
    meaning: str,
    simple_txt: str,
    purpose: str,
    formula_expr: str,
    formula_note: str,
    components: list,
    pick: str,
    steps_list: list,
    high: str,
    low: str,
    too_high: str,
    ex_num: str,
    work_formula: str,
    work_pick: str,
    work_arith: str,
    work_answer: str,
    kaveri_read: str,
    mistakes_list: list,
    mem: str,
    extra: str = "",
) -> str:
    return (
        h3(heading)
        + p(b("Syllabus bucket. ") + bucket)
        + (p(b("Ideal / usual comment. ") + ideal) if ideal else "")
        + definition(meaning)
        + simple(simple_txt)
        + why(purpose)
        + formula(formula_expr, formula_note)
        + table(
            ["Component", "What it means", "How to pick it from the statements"],
            components,
            caption=f"{heading} — every piece of the formula",
        )
        + format_box("How to pick the figure (any paper, and Kaveri)", f"<p>{pick}</p>")
        + steps(steps_list)
        + table(
            ["Signal", "Interpretation"],
            [
                ["High (or rising)", high],
                ["Low (or falling)", low],
                ["Too high can also be bad", too_high],
            ],
            caption="A ratio is a sentence, not a trophy",
        )
        + example(
            ex_num,
            "Easy",
            f"{heading} from Kaveri Traders Ltd (31 March 2026)",
            work_table(work_formula, work_pick, work_arith, work_answer)
            + p(b("Reading for Kaveri. ") + kaveri_read),
        )
        + mistakes(mistakes_list)
        + memory(mem)
        + extra
    )


def body() -> str:
    parts: list[str] = []
    parts.append(
        chapter_open(
            "07",
            "Ratio Analysis",
            "After this chapter you will classify every ratio as Balance Sheet, Revenue or Combined; pick the correct figures from a Profit and Loss Account and a Balance Sheet; compute the ratio with its unit; and interpret whether the result is healthy — including when a ‘high’ number is actually a warning.",
            [
                "Need and importance of ratios",
                "Ratio formulas",
                "Balance Sheet ratios",
                "Revenue ratios",
                "Combined ratios",
                "Numerical problems",
            ],
        )
    )
    parts.append(_intro())
    parts.append(_need())
    parts.append(_limitations())
    parts.append(_classify())
    parts.append(_kaveri())
    parts.append(_exam_method())
    parts.append(_bs_intro())
    parts.append(_bs_current())
    parts.append(_bs_quick())
    parts.append(_bs_cash())
    parts.append(_bs_de())
    parts.append(_bs_prop())
    parts.append(_bs_gear())
    parts.append(_bs_falt())
    parts.append(_bs_caprop())
    parts.append(_rev_intro())
    parts.append(_rev_gp())
    parts.append(_rev_np())
    parts.append(_rev_opr())
    parts.append(_rev_or())
    parts.append(_rev_exp())
    parts.append(_comb_intro())
    parts.append(_comb_ito())
    parts.append(_comb_ihp())
    parts.append(_comb_dto())
    parts.append(_comb_acp())
    parts.append(_comb_cto())
    parts.append(_comb_app())
    parts.append(_comb_wct())
    parts.append(_comb_fat())
    parts.append(_comb_capt())
    parts.append(_comb_roce())
    parts.append(_comb_roe())
    parts.append(_comb_roa())
    parts.append(_comb_eps())
    parts.append(_comb_icr())
    parts.append(_dupont())
    parts.append(_kaveri_health())
    parts.append(_rebuild())
    parts.append(_identify())
    parts.append(_mistakes_all())
    parts.append(_memory_all())
    parts.append(_formula_table())
    parts.append(_practice())
    parts.append(_theory())
    parts.append(chapter_close())
    return "".join(parts)


# ---------------------------------------------------------------------------
# 1. Opening
# ---------------------------------------------------------------------------


def _intro() -> str:
    return (
        lead(
            "A bank manager in Mysore is looking at two trading companies. Both sold goods worth "
            + rupee(SALES)
            + " last year. Both show a profit. One of them will get the loan. The other will not. "
            "The difference is not the sales figure. The difference is the "
            + b("relationships")
            + " between the figures — how much of that sale is leftover as profit, how quickly stock turns into cash, "
            "whether the firm can pay its bills next month, and whether the owners or the lenders have a bigger claim. "
            "Those relationships are "
            + b("ratios")
            + "."
        )
        + p(
            "This chapter uses "
            + b("one")
            + " company, "
            + b("Kaveri Traders Ltd")
            + ", for every single ratio. You will first read a short Profit and Loss Account and a short Balance Sheet. "
            "Then you will compute every ratio the syllabus names from those two statements. When the exam gives you a different company, "
            "the method does not change — only the numbers do."
        )
        + connect(
            "Chapter 4 taught you to "
            + b("prepare")
            + " a company Balance Sheet and Statement of Profit and Loss (Schedule III). "
            "Chapter 6 taught you to "
            + b("read")
            + " an annual report. This chapter teaches you to "
            + b("analyse")
            + " those statements with arithmetic. A ratio is not a new statement. It is a smarter way of reading the two you already have."
        )
        + keypoint(
            "A ratio is a fraction. One figure divided by another. The art is (1) choosing the right pair, "
            "(2) picking both figures from the correct statement and the correct year, "
            "(3) writing the unit (times, %, days, or a : ratio), and (4) saying what the number means. "
            "A naked 2.1 with no unit and no sentence scores half marks at best."
        )
    )


def _need() -> str:
    return (
        h2("1. Need and importance of ratio analysis", "need")
        + definition(
            "A <strong>ratio</strong> is the arithmetical relationship between two figures drawn from the financial statements, "
            "expressed as a pure number (times), a percentage, a number of days, or a proportion (a : b). "
            "<strong>Ratio analysis</strong> is the method of computing these relationships, comparing them with a standard, "
            "a previous year or another firm, and interpreting what they say about liquidity, solvency, profitability and efficiency."
        )
        + simple(
            "A ratio is a comparison written as a short number. "
            + rupee(300000)
            + " of current assets and "
            + rupee(150000)
            + " of current liabilities is a current ratio of 2. "
            "The 2 is easier to carry in your head, easier to compare with last year, and easier to compare with a rival, than the two raw rupee totals."
        )
        + why(
            "Financial statements are long. A Balance Sheet of a real company has dozens of lines. "
            "The human brain cannot hold “sales ten lakh, stock one lakh twenty thousand, debtors one lakh…” and see the story. "
            "Ratios shrink the story to a handful of numbers, each of which answers one managerial question: "
            "Can we pay bills? Are we too borrowed? How much of each sale is profit? How fast does stock move?"
        )
        + real_life(
            "Kaveri’s owner, Meera, wants a bank working-capital limit. The manager will not read every ledger. "
            "He will compute (or ask her to compute) current ratio, quick ratio, debt-equity, interest coverage and stock turnover. "
            "If those five numbers sit in a healthy range, the file moves. If current ratio is 0.8, the file stops — "
            "no matter how colourful the sales graph is."
        )
        + logic(
            "A single rupee figure has no meaning until it is placed next to another rupee figure. "
            "Profit of "
            + rupee(90000)
            + " sounds pleasant. Profit of "
            + rupee(90000)
            + " on sales of "
            + rupee(SALES)
            + " is a 9% net margin. "
            "Profit of "
            + rupee(90000)
            + " on owners’ funds of "
            + rupee(SF)
            + " is a 15% return on equity. "
            "Same profit, two different questions, two different ratios. That is the whole subject."
        )
        + p(b("What ratio analysis is used for — five jobs."))
        + table(
            ["Job", "Question it answers", "Typical tool"],
            [
                [
                    b("Compare"),
                    "Is this year better than last year? (trend / intra-firm)",
                    "Same ratio, two years, side by side",
                ],
                [
                    b("Benchmark"),
                    "Are we better or worse than other traders? (inter-firm)",
                    "Our ratio vs industry average",
                ],
                [
                    b("Diagnose liquidity"),
                    "Can we pay what is due in the next 12 months?",
                    "Current, quick, cash, working-capital turnover",
                ],
                [
                    b("Diagnose solvency"),
                    "Can we survive in the long run? Is the loan load safe?",
                    "Debt-equity, proprietary, gearing, interest coverage",
                ],
                [
                    b("Diagnose profitability & efficiency"),
                    "Are we earning, and are we using assets hard enough?",
                    "GP, NP, operating, ROCE, ROE, turnovers, EPS",
                ],
            ],
            caption="Five jobs of ratio analysis",
        )
        + h3("Why ratios, not raw figures?")
        + ul(
            [
                b("Scale. ")
                + "A firm with sales of "
                + rupee(10000000)
                + " and a firm with sales of "
                + rupee(1000000)
                + " cannot be compared on raw profit. They can be compared on net profit ratio.",
                b("Trend. ")
                + "Current assets of "
                + rupee(300000)
                + " this year and "
                + rupee(280000)
                + " last year look like an improvement — until you notice current liabilities jumped from "
                + rupee(100000)
                + " to "
                + rupee(150000)
                + ". The current ratio fell from 2.8 to 2.0. The ratio caught what the raw total hid.",
                b("Diagnosis. ")
                + "A falling net profit ratio with a stable gross profit ratio means the leak is below the gross-profit line (operating expenses, interest or tax) — you know where to look.",
                b("Communication. ")
                + "A board, a bank and an examiner all understand “current ratio 2 : 1”. They do not all want to re-read the whole Balance Sheet.",
                b("Control. ")
                + "Management sets a target (stock turnover at least 8 times; collection period under 40 days) and watches the ratio the way a driver watches the speedometer.",
            ]
        )
        + format_box(
            "Four-way classification of what a ratio talks about (use this in theory answers)",
            table(
                ["Family", "About", "Examples in this chapter"],
                [
                    [
                        b("Liquidity"),
                        "Short-term ability to pay",
                        "Current, quick, absolute liquid",
                    ],
                    [
                        b("Solvency / leverage"),
                        "Long-term survival and mix of debt vs equity",
                        "Debt-equity, proprietary, capital gearing, interest coverage",
                    ],
                    [
                        b("Profitability"),
                        "How much leftover from sales and from funds",
                        "GP, NP, operating profit, ROCE, ROE, ROA, EPS",
                    ],
                    [
                        b("Efficiency / activity / turnover"),
                        "How hard assets and working capital are worked",
                        "Stock, debtors, creditors, FA, capital, WC turnovers",
                    ],
                ],
            )
            + p(
                "The "
                + b("syllabus classification")
                + " in the next section is different: it is by "
                + b("where the two figures come from")
                + " (Balance Sheet, P&L, or one of each). "
                "Both classifications are examinable. Do not mix up the names."
            ),
        )
        + steps(
            [
                "Read the question. Is it theory (need, importance, limitations, classification) or a numerical?",
                "If theory: write a definition, then 5–8 numbered points with one line of explanation each. End with a limitation if marks are 8 or more.",
                "If numerical: extract the two statements (or the given ratios), label each figure BS or P&L, then choose the family (liquidity / solvency / profitability / efficiency) and the syllabus bucket (BS / Revenue / Combined).",
                "Write the formula. Substitute. Divide. Write the unit. Write one sentence of meaning if the question says “comment” or “interpret”.",
            ]
        )
        + example(
            "7.0",
            "Easy",
            "Why a ratio beats a raw figure",
            p(
                "Firm A earns PAT of "
                + rupee(90000)
                + " with owners’ funds of "
                + rupee(600000)
                + ". "
                "Firm B earns PAT of "
                + rupee(120000)
                + " with owners’ funds of "
                + rupee(1200000)
                + ". Who is using owners’ money better?"
            )
            + p(b("Working."))
            + p("Firm A ROE = " + rupee(90000) + " ÷ " + rupee(600000) + " × 100 = 15%.")
            + p("Firm B ROE = " + rupee(120000) + " ÷ " + rupee(1200000) + " × 100 = 10%.")
            + p(
                b("Answer. ")
                + "Firm A. B’s profit is bigger in rupees, but A returns 15 paise per owners’ rupee against B’s 10 paise. "
                "Without the ratio, the bigger profit would have fooled you."
            ),
        )
        + identify(
            "If the question says “need / importance / advantages / utility of ratio analysis”, write: "
            "comparison (intra-firm trend and inter-firm), diagnosis of liquidity, solvency, profitability and efficiency, "
            "simplification of statements, help to management / creditors / investors, and use in forecasting. "
            "If it says “limitations / disadvantages / drawbacks”, use the next section — do not recycle the importance points with a ‘not’ stuck in front."
        )
        + mistakes(
            [
                "Treating a ratio as a conclusion. “Current ratio is 2, so the company is good” is incomplete. Good compared with what? Last year? The industry? The 2 : 1 rule of thumb?",
                "Using ratios as the only evidence. Window dressing, different accounting policies and non-money facts (a strike, a new patent) do not appear in the ratio.",
                "Writing ‘ratios help in decision making’ as a full answer. The examiner wants which decision and which ratio.",
            ]
        )
        + memory(
            "C-T-D-C — Compare, Trend, Diagnose, Communicate. That is why ratios exist. "
            "Four health checks: Liquidity (today’s bills), Solvency (tomorrow’s survival), Profitability (leftover), Efficiency (speed)."
        )
        + exam_answer(
            "Ratio analysis is the process of computing, comparing and interpreting arithmetical relationships between figures in the financial statements. "
            "It is needed because raw rupee totals of two firms, or of two years, are not comparable when the firms differ in size. "
            "Ratios reduce the statements to a small set of indicators of liquidity (current, quick), solvency (debt-equity, proprietary), "
            "profitability (gross profit, net profit, ROCE, ROE) and efficiency (stock, debtors, capital turnover). "
            "They help management to control operations, help lenders to judge creditworthiness, help investors to judge return, "
            "and help the analyst to locate the area in which the business is weak. A ratio has meaning only against a benchmark — "
            "a previous period, an industry average, or a conventional ideal — and must be read with the limitations of historical data and window dressing in mind."
        )
    )


def _limitations() -> str:
    return (
        h3("Limitations of ratio analysis (always asked)")
        + definition(
            "A limitation of ratio analysis is a reason why a computed ratio may mislead, or may not be enough, "
            "for a decision. Ratios are a tool. They are not the business itself."
        )
        + simple(
            "A ratio is a photograph of the past, taken with the company’s own camera, possibly after the furniture was rearranged for the photo. "
            "You still look at the photo — you just do not buy the house from the photo alone."
        )
        + table(
            ["Limitation", "What it means", "What you do about it"],
            [
                [
                    b("Historical"),
                    "Figures are last year’s. The factory may already have burned, or a new contract may already have been signed.",
                    "Read notes, directors’ report, and subsequent events. Do not treat the ratio as tomorrow’s cash.",
                ],
                [
                    b("Window dressing"),
                    "Management can postpone a purchase, push a sale, or repay a creditor on 30 March and re-borrow on 2 April, so that 31 March looks liquid.",
                    "Look at average figures, cash flow, and more than one year. One beautiful year-end is a warning, not a comfort.",
                ],
                [
                    b("Different policies"),
                    "One firm uses FIFO, another weighted average; one uses SLM, another WDV. Stock and profit, and therefore every ratio that uses them, are not comparable.",
                    "Read the accounting-policy note. Adjust, or at least say “not strictly comparable”.",
                ],
                [
                    b("No standalone meaning"),
                    "Current ratio 2 : 1 is not ‘good’ by itself. In a supermarket 1.2 may be healthy; in a shipyard 2 may be tight.",
                    "Always pair with an industry benchmark and with other ratios of the same firm.",
                ],
                [
                    b("Need for a benchmark"),
                    "Without last year, a rival, or a rule of thumb, a ratio is a number in a vacuum.",
                    "Write the comparison in the answer. “1.2, above the 1 : 1 ideal” scores; “1.2” does not.",
                ],
                [
                    b("Ignores qualitative facts"),
                    "Skill of the owner, quality of the product, pending court case, labour unrest — none of these is a ratio.",
                    "Read the notes and the auditors’ report. Mention qualitative factors in a comment question.",
                ],
                [
                    b("Price-level / inflation"),
                    "Fixed assets at 2014 cost sit next to sales at 2026 prices. FA turnover looks better than the real use of capacity.",
                    "Be careful with any ratio that mixes an old Balance-Sheet cost with a current P&L figure.",
                ],
                [
                    b("Year-end snapshot"),
                    "A seasonal trader may look weak on 31 March and strong on 31 December. One day is not the year.",
                    "Prefer averages of opening and closing; mention seasonality in the comment.",
                ],
                [
                    b("Arithmetic without cause"),
                    "A ratio tells you that stock is slow. It does not tell you whether the cause is a bad product, a weak salesman, or a flood.",
                    "Use ratios to locate the room. Then walk into the room (ageing, product mix, visit).",
                ],
            ],
            caption="Nine limitations — write any six in an 8-mark answer, each with one line of explanation",
        )
        + exam_answer(
            "Ratio analysis has important limitations. The data are historical and may not continue. "
            "Management may window-dress year-end figures. Different accounting policies (stock valuation, depreciation) destroy comparability. "
            "A ratio has no meaning in isolation — it needs an industry or trend benchmark. "
            "Qualitative factors and subsequent events are ignored. Inflation mixes old costs with current revenues. "
            "Year-end figures may be seasonal. And a ratio identifies a symptom, not a cause. "
            "Therefore ratios must be read together, over several years, along with notes to accounts and cash-flow information."
        )
        + warn(
            "In a 5-mark “limitations” question, three one-word bullets (“historical, window dressing, not comparable”) "
            "are not enough. Give one sentence of meaning under each heading. The marks are in the sentence."
        )
    )


def _classify() -> str:
    return (
        h2("2. Classification of ratios as per this syllabus", "classify")
        + definition(
            "This syllabus classifies ratios by the <strong>source of the two figures</strong>. "
            "(1) <strong>Balance Sheet ratios</strong> — numerator and denominator both from the Balance Sheet. "
            "(2) <strong>Revenue ratios</strong> (also called Profit and Loss, income-statement, or P&L ratios) — both from the Statement of Profit and Loss. "
            "(3) <strong>Combined ratios</strong> — one figure from the P&L and one from the Balance Sheet."
        )
        + simple(
            "Look at the two numbers you are about to divide. If both live on the Balance Sheet (a photograph of one day), it is a Balance Sheet ratio. "
            "If both live on the P&L (a movie of one year), it is a Revenue ratio. If one lives on each statement (a movie divided by a photograph), it is Combined."
        )
        + why(
            "Examiners in this paper ask “classify the following ratios” and they mean "
            + b("this")
            + " three-bucket split, not the liquidity/solvency/profitability split. "
            "If you write ‘current ratio is a liquidity ratio’ when they asked for the syllabus classification, you have answered a different question."
        )
        + real_life(
            "Meera’s current assets and current liabilities are both on Kaveri’s Balance Sheet — current ratio is a Balance Sheet ratio. "
            "Gross profit and sales are both on the P&L — GP ratio is a Revenue ratio. "
            "Cost of goods sold is on the P&L, average stock is on the Balance Sheet — stock turnover is Combined."
        )
        + logic(
            "A Balance Sheet ratio compares two stocks (positions on one date). A Revenue ratio compares two flows (over a period). "
            "A Combined ratio compares a flow with a stock, which is why we so often use an "
            + b("average")
            + " of opening and closing Balance-Sheet figures — to give the stock a chance to represent the whole year."
        )
        + format_box(
            "The three buckets (memorise the test, not a random list)",
            table(
                ["Bucket", "Test (say this in the exam)", "What it usually measures", "Ratios in this chapter"],
                [
                    [
                        b("Balance Sheet ratios"),
                        "Both numerator and denominator are Balance-Sheet positions.",
                        "Liquidity and solvency / capital structure",
                        "Current; quick / acid test; absolute liquid; debt-equity; proprietary; capital gearing; fixed assets to long-term funds; current assets to proprietary funds",
                    ],
                    [
                        b("Revenue ratios"),
                        "Both figures are P&L flows for the year.",
                        "Profitability margins and cost structure",
                        "Gross profit ratio; net profit ratio; operating profit ratio; operating ratio; expense ratios",
                    ],
                    [
                        b("Combined ratios"),
                        "One figure from P&L, one from Balance Sheet (use averages when opening is given).",
                        "Turnovers / efficiency, and returns on funds, plus EPS and interest coverage",
                        "Inventory turnover and holding period; debtors turnover and collection period; creditors turnover and payment period; WC / FA / capital turnover; ROCE; ROE; ROA; EPS; interest coverage",
                    ],
                ],
                caption="Syllabus classification — this is the one you must not skip",
            ),
        )
        + two_col(
            table(
                ["Ratio", "Bucket"],
                [
                    ["Current ratio", "Balance Sheet"],
                    ["Quick ratio", "Balance Sheet"],
                    ["Debt-equity", "Balance Sheet"],
                    ["Gross profit ratio", "Revenue"],
                    ["Operating ratio", "Revenue"],
                    ["Stock turnover", "Combined"],
                    ["ROCE", "Combined"],
                    ["EPS", "Combined"],
                ],
                caption="Spot check — cover the right column and say the bucket",
            ),
            box(
                "key",
                "Why ROCE is Combined, not Revenue",
                "<p>EBIT lives on the P&L. Capital employed lives on the Balance Sheet "
                "(equity + long-term debt, or fixed assets + working capital). "
                "One from each statement → Combined. Students often dump ROCE into “profitability” "
                "and then, when asked for the syllabus bucket, wrongly say Revenue. Profitability is the "
                "<em>purpose</em>. Combined is the <em>source</em>.</p>",
            ),
        )
        + identify(
            "If the question says “classify as Balance Sheet / Revenue / Combined (or income-statement / mixed)”, "
            "apply the source test. Ignore the words liquidity and profitability for that question. "
            "If the question says “liquidity / solvency / profitability / activity”, use the four-family table in section 1. "
            "Read the question’s own headings before you start listing."
        )
        + mistakes(
            [
                "Putting stock turnover under Balance Sheet because stock is a Balance-Sheet item. The other half (COGS) is P&L — it is Combined.",
                "Putting current ratio under Combined because ‘current assets come from operations’. Both CA and CL are BS positions. It is a Balance Sheet ratio.",
                "Calling every profitability ratio a Revenue ratio. ROCE, ROE, ROA and EPS are profitability by purpose but Combined by source.",
                "Forgetting that interest coverage (EBIT / Interest) is Combined — EBIT is P&L, but some papers treat both as P&L (interest is a P&L expense too!). In this syllabus we place it under Combined because it is read with solvency; if both figures are from P&L you may also defend it as Revenue. State your reason. In these notes it sits with Combined, next to ROCE, because the exam uses it as a solvency companion of debt-equity.",
            ]
        )
        + keypoint(
            "Interest coverage: both EBIT and interest appear in the P&L, so a strict source-test would call it a Revenue ratio. "
            "Many MBA papers still group it with leverage / Combined because you interpret it together with debt-equity. "
            "In the formula table at the end of this chapter it is listed as Combined (solvency companion). "
            "If the question is a pure source-test and offers ‘P&L ratio’ as a choice, you may tick that and write ‘both figures from P&L’."
        )
        + memory(
            "BS–BS = Balance Sheet ratio (structure). P&L–P&L = Revenue ratio (margin). P&L–BS = Combined (speed or return). "
            "Three buckets. Every ratio in the paper falls into one of them."
        )
        + exam_answer(
            "Ratios are classified, for this syllabus, by the statement from which the two figures are taken. "
            "Balance Sheet ratios use two position figures from the Balance Sheet (current ratio, quick ratio, debt-equity, proprietary ratio, capital gearing, "
            "fixed assets to long-term funds, current assets to proprietary funds). "
            "Revenue ratios use two flow figures from the Statement of Profit and Loss (gross profit ratio, net profit ratio, operating profit ratio, operating ratio, expense ratios). "
            "Combined ratios use one flow and one position (inventory, debtors and creditors turnovers and their holding/collection/payment periods, "
            "working-capital, fixed-asset and capital turnovers, ROCE, ROE, ROA, EPS, and interest coverage as a solvency companion). "
            "This source classification is separate from the purpose classification into liquidity, solvency, profitability and efficiency."
        )
    )


def _kaveri() -> str:
    pl = table(
        ["Particulars", "₹"],
        [
            ["Revenue from operations (Sales)", rupee(SALES)],
            ["&nbsp;&nbsp;of which: cash sales", rupee(CASH_SALES)],
            ["&nbsp;&nbsp;of which: credit sales", rupee(CREDIT_SALES)],
            ["Less: Cost of goods sold (working below)", rupee(COGS)],
            [b("Gross profit"), b(rupee(GP))],
            ["Less: Employee benefits expense", rupee(EMP)],
            ["Less: Other operating expenses (includes depreciation)", rupee(OTHER_OPEX)],
            [b("Operating profit (EBIT / PBIT)"), b(rupee(EBIT))],
            ["Less: Finance costs (interest on long-term debt)", rupee(INTEREST)],
            [b("Profit before tax"), b(rupee(PBT))],
            ["Less: Tax expense", rupee(TAX)],
            [b("Profit after tax (PAT) for the year"), b(rupee(PAT))],
        ],
        caption="Kaveri Traders Ltd — Statement of Profit and Loss for the year ended 31 March 2026 (teaching / GP format)",
        foot="Schedule III would list purchases and the change in inventory as separate expense lines; the net of those two lines is COGS. For ratios, COGS is the figure you need.",
    )
    cogs_w = table(
        ["Working: Cost of goods sold", "₹"],
        [
            ["Opening inventory (1 April 2025)", rupee(OP_STOCK)],
            ["Add: Purchases (all on credit)", rupee(PURCHASES)],
            ["Goods available for sale", rupee(OP_STOCK + PURCHASES)],
            ["Less: Closing inventory (31 March 2026)", rupee(CL_STOCK)],
            [b("Cost of goods sold"), b(rupee(COGS))],
        ],
        caption="COGS working — this is also how you rebuild COGS in any paper",
    )
    bs_eq = table(
        ["Particulars", "₹"],
        [
            [b("I. EQUITY AND LIABILITIES"), ""],
            ["1. Shareholders’ funds", ""],
            ["&nbsp;&nbsp;(a) Equity share capital (40,000 shares of ₹10 each)", rupee(ESC)],
            ["&nbsp;&nbsp;(b) Reserves and surplus", rupee(RES)],
            ["&nbsp;&nbsp;" + b("Shareholders’ funds"), b(rupee(SF))],
            ["2. Non-current liabilities", ""],
            ["&nbsp;&nbsp;Long-term borrowings", rupee(LTD)],
            ["3. Current liabilities", ""],
            ["&nbsp;&nbsp;Trade payables (creditors) — all for goods", rupee(CL_)],
            [b("Total equity and liabilities"), b(rupee(TA))],
        ],
        caption="Kaveri Traders Ltd — Equity and liabilities as at 31 March 2026",
    )
    bs_as = table(
        ["Particulars", "₹"],
        [
            [b("II. ASSETS"), ""],
            ["1. Non-current assets", ""],
            ["&nbsp;&nbsp;Property, plant and equipment (net)", rupee(FA)],
            ["2. Current assets", ""],
            ["&nbsp;&nbsp;(a) Inventories", rupee(INV)],
            ["&nbsp;&nbsp;(b) Trade receivables (debtors)", rupee(TR)],
            ["&nbsp;&nbsp;(c) Cash and cash equivalents", rupee(CASH)],
            ["&nbsp;&nbsp;" + b("Current assets"), b(rupee(CA))],
            [b("Total assets"), b(rupee(TA))],
        ],
        caption="Kaveri Traders Ltd — Assets as at 31 March 2026",
    )
    notes = table(
        ["Extra fact (given in the question, or in notes)", "₹ / rule"],
        [
            ["Opening trade receivables (1 April 2025)", rupee(OP_TR)],
            ["Opening trade payables (1 April 2025)", rupee(OP_CL)],
            ["Opening inventory (already in COGS working)", rupee(OP_STOCK)],
            ["Credit sales", "80% of sales = " + rupee(CREDIT_SALES)],
            ["Cash sales", "20% of sales = " + rupee(CASH_SALES)],
            ["Purchases", "100% on credit = " + rupee(PURCHASES)],
            ["Preference share capital", "Nil"],
            ["Marketable securities / current investments", "Nil"],
            ["Prepaid expenses", "Nil"],
            ["Fictitious assets / miscellaneous expenditure", "Nil"],
            ["Proposed dividend / outstanding expenses in CL", "Nil — CL is only trade payables"],
            ["Face value of an equity share", rupee(FV)],
            ["Number of equity shares", f"{SHARES:,}".replace(",", ",") + " shares"],
        ],
        caption="Facts that are not a separate line on the face of the statements — read the notes",
        foot="When a question is silent on opening debtors or opening creditors, use the closing figure and write the assumption. Kaveri gives openings, so we use averages.",
    )
    extract = table(
        ["Ready-to-use figure", "Amount", "How it was built"],
        [
            ["Gross profit", rupee(GP), rupee(SALES) + " − " + rupee(COGS)],
            ["Operating expenses", rupee(OPEX), rupee(EMP) + " + " + rupee(OTHER_OPEX)],
            ["Operating cost", rupee(OP_COST), rupee(COGS) + " + " + rupee(OPEX)],
            ["EBIT (operating profit)", rupee(EBIT), rupee(GP) + " − " + rupee(OPEX) + "  (also PBT + interest)"],
            ["Shareholders’ funds", rupee(SF), rupee(ESC) + " + " + rupee(RES)],
            ["Capital employed", rupee(CE), rupee(SF) + " + " + rupee(LTD) + "  (also FA + WC)"],
            ["Working capital", rupee(WC), rupee(CA) + " − " + rupee(CL_)],
            ["Quick assets", rupee(QA), rupee(CA) + " − " + rupee(INV) + "  (no prepaid)"],
            ["Average inventory", rupee(AVG_INV), "(" + rupee(OP_STOCK) + " + " + rupee(CL_STOCK) + ") ÷ 2"],
            ["Average trade receivables", rupee(AVG_TR), "(" + rupee(OP_TR) + " + " + rupee(TR) + ") ÷ 2"],
            ["Average trade payables", rupee(AVG_CL), "(" + rupee(OP_CL) + " + " + rupee(CL_) + ") ÷ 2"],
            ["Total assets / total of BS", rupee(TA), rupee(FA) + " + " + rupee(CA)],
            ["Total debt", rupee(TD), rupee(LTD) + " + " + rupee(CL_)],
        ],
        caption="Extract — copy this into the margin of your answer booklet before you compute any ratio",
    )
    return (
        h2("3. The running company — Kaveri Traders Ltd", "kaveri")
        + lead(
            "Every worked ratio in this chapter uses Kaveri Traders Ltd, a wholesale trader, year ended 31 March 2026. "
            "The numbers were chosen so that most divisions come out clean. Live with these two statements. "
            "By the end of the chapter you should be able to recompute any ratio with the statements closed."
        )
        + p(
            b("Business. ")
            + "Kaveri buys goods on credit, sells 80% on credit and 20% for cash, owns its godown and office (fixed assets), "
            "and has one term loan. There are no preference shares, no prepaid expenses, no marketable securities, and no fictitious assets. "
            "That keeps the picking rules visible: when a component is nil, we still "
            + b("name")
            + " it, then drop it."
        )
        + h3("Statement of Profit and Loss (condensed teaching format)")
        + pl
        + cogs_w
        + h3("Balance Sheet (Schedule III condensed — vertical)")
        + p(
            "Indian MBA papers use the Companies Act 2013 vertical form: Equity and Liabilities first, Assets second, one total. "
            "Kaveri’s condensed statement follows that order. There is no “horizontal T” in the exam answer."
        )
        + two_col(bs_eq, bs_as)
        + keypoint(
            "Check the Balance Sheet before you touch a ratio: Equity and liabilities "
            + rupee(TA)
            + " = Assets "
            + rupee(TA)
            + ". "
            "Capital employed two ways: shareholders’ funds "
            + rupee(SF)
            + " + long-term debt "
            + rupee(LTD)
            + " = "
            + rupee(CE)
            + "; "
            "also net fixed assets "
            + rupee(FA)
            + " + working capital "
            + rupee(WC)
            + " = "
            + rupee(CE)
            + ". "
            "If these two capital-employed workings disagree, you have mis-picked a figure — stop and find it."
        )
        + h3("Notes and ready extract")
        + notes
        + extract
        + warn(
            "Credit sales are "
            + rupee(CREDIT_SALES)
            + " — not "
            + rupee(SALES)
            + ". "
            "If a question is silent on the cash/credit split, the usual exam assumption is that "
            + b("all sales are credit sales")
            + ", and you write that assumption on the face of the answer. "
            "Kaveri is not silent: 80% credit is given, so debtors turnover must use "
            + rupee(CREDIT_SALES)
            + "."
        )
        + example(
            "7.1",
            "Easy",
            "Prove the two statements lock together",
            p(b("Balance Sheet total."))
            + p(
                "Equity "
                + rupee(ESC)
                + " + Reserves "
                + rupee(RES)
                + " + Long-term debt "
                + rupee(LTD)
                + " + Trade payables "
                + rupee(CL_)
                + " = "
                + rupee(ESC + RES)
                + " + "
                + rupee(LTD)
                + " + "
                + rupee(CL_)
                + " = "
                + rupee(SF + LTD)
                + " + "
                + rupee(CL_)
                + " = "
                + rupee(TA)
                + "."
            )
            + p(
                "Fixed assets "
                + rupee(FA)
                + " + Inventory "
                + rupee(INV)
                + " + Receivables "
                + rupee(TR)
                + " + Cash "
                + rupee(CASH)
                + " = "
                + rupee(FA)
                + " + "
                + rupee(CA)
                + " = "
                + rupee(TA)
                + "."
            )
            + p(b("Capital employed, method 1 (liability side)."))
            + p(rupee(SF) + " + " + rupee(LTD) + " = " + rupee(CE) + ".")
            + p(b("Capital employed, method 2 (asset side)."))
            + p(
                "Working capital = "
                + rupee(CA)
                + " − "
                + rupee(CL_)
                + " = "
                + rupee(WC)
                + ". "
                "FA + WC = "
                + rupee(FA)
                + " + "
                + rupee(WC)
                + " = "
                + rupee(CE)
                + "."
            )
            + p(b("Gross profit check."))
            + p(
                "GP ratio is given as 25% of sales, so GP = 25% × "
                + rupee(SALES)
                + " = "
                + rupee(GP)
                + ". "
                "COGS = sales − GP = "
                + rupee(SALES)
                + " − "
                + rupee(GP)
                + " = "
                + rupee(COGS)
                + ". "
                "Purchases = COGS + closing stock − opening stock = "
                + rupee(COGS)
                + " + "
                + rupee(CL_STOCK)
                + " − "
                + rupee(OP_STOCK)
                + " = "
                + rupee(COGS + CL_STOCK)
                + " − "
                + rupee(OP_STOCK)
                + " = "
                + rupee(PURCHASES)
                + "."
            )
            + p(
                b("Answer. ")
                + "The statements lock. You may now compute every ratio from this extract without going back to the ledgers."
            ),
        )
    )


def _exam_method() -> str:
    return (
        h2("4. Exam method that never changes", "method")
        + steps(
            [
                "Draw a two-column extract: P&L figures on the left, Balance Sheet figures on the right. Include openings if given.",
                "Build the derived figures: GP, COGS, operating cost, EBIT, shareholders’ funds, capital employed, working capital, quick assets, averages.",
                "Read the requirement. Circle the ratio names. Next to each, write BS / Rev / Combined — this chooses the formula family.",
                "Write the formula in words, then in figures, then the arithmetic, then the answer with unit (times, %, days, ₹, or a : b).",
                "If the question says “comment / interpret / evaluate”, add two sentences: (a) against the ideal or last year, (b) one risk if the ratio went further in the same direction.",
                "If an opening figure is missing, use the closing figure and write “opening not given, closing figure used as a proxy for average”.",
            ]
        )
        + exam_tip(
            "Units: turnover ratios are in "
            + b("times")
            + "; margin and return ratios are in "
            + b("%")
            + "; collection / payment / holding periods are in "
            + b("days")
            + " (or months/weeks if asked); current and quick are written as "
            + b("x : 1")
            + "; EPS is in "
            + b("₹ per share")
            + ". A correct 7.5 without “times” is a half-done answer."
        )
        + keypoint(
            "365 days in a year is the default in these notes. Some question papers use 360 days to make the division neat, "
            "or 12 months, or 52 weeks. If the paper states a convention, obey it. If it is silent, 365 is acceptable; write “taking 365 days in a year”."
        )
    )


# ---------------------------------------------------------------------------
# 5. Balance Sheet ratios
# ---------------------------------------------------------------------------


def _bs_intro() -> str:
    return (
        h2("5. Balance Sheet ratios", "bs")
        + lead(
            "Both figures come from the Balance Sheet. These ratios talk about "
            + b("structure")
            + ": can Kaveri pay what is due this year (liquidity), and who has financed the firm — owners or lenders (solvency)."
        )
        + p(
            "There is no P&L number in this section. If you catch yourself reaching for sales or PAT, you have slipped into a Combined or Revenue ratio."
        )
    )


def _bs_current() -> str:
    return ratio_section(
        heading="5.1 Current ratio (working capital ratio)",
        bucket="Balance Sheet ratio — both figures from the Balance Sheet. Purpose family: liquidity.",
        ideal="Textbook ideal ≈ 2 : 1. A conventional rule of thumb, not a law. Trading firms can live a little lower; manufacturers with slow stock need it higher.",
        meaning="The current ratio is current assets divided by current liabilities. It asks: for every rupee payable within a year, how many rupees of assets are expected to turn into cash within a year?",
        simple_txt="It is the short-term cushion. Current assets are the things that will become cash soon (stock, debtors, cash, prepaid). Current liabilities are the bills due soon (creditors, outstanding expenses, short-term borrowings, overdraft). Divide the first by the second.",
        purpose="Lenders and the owner want to know whether next year’s bills can be paid from next year’s convertibles, without selling the godown. A bank sanction note almost always quotes this ratio.",
        formula_expr="Current ratio = Current assets ÷ Current liabilities &nbsp;&nbsp;(written as CA : CL, e.g. 2 : 1)",
        formula_note="Working capital = CA − CL is the rupee cousin, not the ratio. Current ratio 2 does not mean working capital is ₹2. Current ratio 2 means CA = 2 × CL.",
        components=[
            [
                "Current assets",
                "Assets expected to be realised within 12 months: inventory, trade receivables, cash and bank, short-term investments, prepaid expenses, bills receivable.",
                "Balance Sheet → Current assets. For Kaveri: inventory "
                + rupee(INV)
                + " + receivables "
                + rupee(TR)
                + " + cash "
                + rupee(CASH)
                + " = "
                + rupee(CA)
                + ".",
            ],
            [
                "Current liabilities",
                "Obligations due within 12 months: trade payables, outstanding expenses, short-term borrowings, bank overdraft, current maturities of long-term debt, tax payable.",
                "Balance Sheet → Current liabilities. For Kaveri: only trade payables "
                + rupee(CL_)
                + ".",
            ],
        ],
        pick="Add every current asset on the face of the BS (do not skip prepaid or cash). Add every current liability (do not skip outstanding expenses or overdraft if given). Do not include long-term borrowings. Do not include fixed assets.",
        steps_list=[
            "From the Balance Sheet, total current assets. From the Balance Sheet, total current liabilities.",
            "Write Current ratio = CA ÷ CL.",
            "Divide. Write the answer as a number of times, or as x : 1.",
            "Compare with 2 : 1 and with last year / industry if given. One sentence of comment if asked.",
        ],
        high="Comfortable cushion. Suppliers and banks are happier. The firm can take small shocks (a slow customer, a late sale) without defaulting.",
        low="Bills may not be paid on time. A ratio under 1 means current assets do not even cover current liabilities — technically insolvent in the short run.",
        too_high="Idle cash sitting in the bank earning little, or stock piling up, or debtors not being collected. Owners’ money is sleeping. A current ratio of 5 is not a prize; it is a question: why is capital stuck in working capital instead of earning in the business or being returned to owners?",
        ex_num="K1",
        work_formula="Current ratio = Current assets ÷ Current liabilities",
        work_pick="CA = "
        + rupee(CA)
        + " (inventory "
        + rupee(INV)
        + " + receivables "
        + rupee(TR)
        + " + cash "
        + rupee(CASH)
        + "). CL = "
        + rupee(CL_)
        + " (trade payables).",
        work_arith=rupee(CA)
        + " ÷ "
        + rupee(CL_)
        + " = "
        + str(CA // CL_)
        + ". Written as "
        + _ratio_pair(CA, CL_)
        + ".",
        work_answer=_ratio_pair(CA, CL_) + " &nbsp;(or " + _times(CA, CL_) + ")",
        kaveri_read="Exactly the textbook ideal of 2 : 1. Short-term bills of "
        + rupee(1)
        + " are covered by "
        + rupee(2)
        + " of current assets. Not tight, not bloated. We still need the quick ratio, because part of that cushion is stock, which is the slowest current asset.",
        mistakes_list=[
            "Reading “current ratio 2” as CA − CL = 2. No: CA = 2 × CL. If WC is "
            + rupee(150000)
            + " and CR is 2, CL is "
            + rupee(150000)
            + ", not "
            + rupee(2)
            + ".",
            "Leaving prepaid expenses out of CA. Prepaid is a current asset. (It is excluded only when we compute the quick ratio.)",
            "Putting long-term debt into CL. A term loan due after 12 months is non-current.",
            "Using working capital as the denominator. The denominator is CL, not WC.",
        ],
        mem="Current = everything soon-to-be-cash over everything soon-to-be-paid. Ideal 2 : 1 — “two on top, one below”.",
        extra=warn(
            "Bank overdraft: treat it as a current liability (denominator). Do not net it off cash unless the question says “cash net of overdraft”. "
            "Proposed dividend, if given as a current liability in the paper’s own BS, stays in CL."
        ),
    )


def _bs_quick() -> str:
    return ratio_section(
        heading="5.2 Quick ratio (acid-test / liquid ratio)",
        bucket="Balance Sheet ratio. Purpose family: liquidity (stricter than current).",
        ideal="Textbook ideal ≈ 1 : 1. Quick assets should at least equal current liabilities.",
        meaning="The quick ratio is quick (liquid) assets divided by current liabilities. Quick assets are current assets minus inventory and minus prepaid expenses. It asks: if we cannot sell a single extra unit of stock, can we still pay the bills from cash, near-cash and debtors?",
        simple_txt="The current ratio trusts stock. The acid test does not. Stock may be slow, damaged, or overvalued. Prepaid expenses will not pay a creditor — the landlord already has that rent. So we drop both, and test again.",
        purpose="To measure immediate liquidity. A firm with a pretty current ratio of 2.5 that is almost all unsold monsoon stock will fail the acid test. Banks look at this after they look at current ratio.",
        formula_expr="Quick ratio = (Current assets − Inventory − Prepaid expenses) ÷ Current liabilities",
        formula_note="Quick assets = Cash + Bank + Marketable securities + Trade receivables + Bills receivable. Equivalent formula: Quick assets ÷ CL. Ideal ≈ 1 : 1.",
        components=[
            [
                "Quick assets",
                "Current assets that can be converted into cash in a short time without a special sale of stock.",
                "Kaveri: CA "
                + rupee(CA)
                + " − inventory "
                + rupee(INV)
                + " − prepaid "
                + rupee(0)
                + " = "
                + rupee(QA)
                + ". Check: receivables "
                + rupee(TR)
                + " + cash "
                + rupee(CASH)
                + " = "
                + rupee(QA)
                + ".",
            ],
            [
                "Inventory (stock)",
                "Goods held for sale. Slowest current asset; may not realise book value.",
                "BS → Inventories. Kaveri closing stock "
                + rupee(INV)
                + ". Deduct it.",
            ],
            [
                "Prepaid expenses",
                "Already paid; will not come back as cash. Cannot be used to pay a creditor.",
                "Kaveri has none. If a paper gives prepaid "
                + rupee(20000)
                + ", deduct that too.",
            ],
            [
                "Current liabilities",
                "Same CL as in the current ratio.",
                "Kaveri: "
                + rupee(CL_)
                + ".",
            ],
        ],
        pick="Start with total CA. Subtract closing inventory. Subtract prepaid expenses (and any deferred or non-cash current assets the question flags). Do not subtract debtors — debtors are quick. Do not subtract cash. Divide by the same CL you used for the current ratio.",
        steps_list=[
            "Compute current assets and current liabilities as for the current ratio.",
            "Identify inventory and prepaid (and loose tools / stock of stationery if the paper treats them as non-quick).",
            "Quick assets = CA − inventory − prepaid.",
            "Quick ratio = Quick assets ÷ CL. Write as x : 1.",
        ],
        high="The firm can pay short-term dues even if stock freezes. Creditors are well covered by cash and debtors.",
        low="Below 1 : 1, the firm depends on selling stock (or taking a new loan) to pay today’s bills. That is a liquidity risk.",
        too_high="Cash and debtors piled up. Cash earning little; debtors perhaps too generous (check collection period). Capital is idle.",
        ex_num="K2",
        work_formula="Quick ratio = (CA − Inventory − Prepaid) ÷ CL",
        work_pick="CA "
        + rupee(CA)
        + ", Inventory "
        + rupee(INV)
        + ", Prepaid nil, CL "
        + rupee(CL_)
        + ". Quick assets = "
        + rupee(CA)
        + " − "
        + rupee(INV)
        + " = "
        + rupee(QA)
        + ".",
        work_arith=rupee(QA)
        + " ÷ "
        + rupee(CL_)
        + " = "
        + f"{QA / CL_:.1f}"
        + ". Written as "
        + _ratio_pair(QA, CL_)
        + ".",
        work_answer=_ratio_pair(QA, CL_),
        kaveri_read="1.2 : 1 is above the 1 : 1 ideal. Even with stock ignored, Kaveri covers its bills. The gap between current 2.0 and quick 1.2 is stock of "
        + rupee(INV)
        + " — we will later see whether that stock is moving (spoiler: stock turnover 7.5 times, so it is moving).",
        mistakes_list=[
            "Forgetting to deduct prepaid expenses. Prepaid is in CA, but it is not a quick asset.",
            "Deducting debtors “because they might not pay”. Doubtful debts, if a provision is given, are already netted. Do not drop the whole receivables line.",
            "Using opening stock instead of closing stock. The Balance Sheet is a closing photograph. Quick ratio uses closing inventory.",
            "Changing the CL between current and quick. Same denominator.",
        ],
        mem="Acid test = drop the slow and the already-spent: drop stock, drop prepaid. Ideal 1 : 1 — “one on top, one below”.",
        extra=exam_tip(
            "If the paper gives “liquid assets” as a ready total, believe it. If it gives a list, you must deduct stock and prepaid yourself. "
            "Loose tools and prepaid rent are the two items students most often leave inside quick assets."
        ),
    )


def _bs_cash() -> str:
    return ratio_section(
        heading="5.3 Absolute liquid ratio (cash ratio)",
        bucket="Balance Sheet ratio. Purpose family: liquidity (strictest).",
        ideal="Conventional ideal ≈ 0.5 : 1 (cash and near-cash equal half of current liabilities). Not always required; many traders run lower because cash earns little.",
        meaning="The absolute liquid ratio is cash plus marketable securities (current investments), divided by current liabilities. It asks: without collecting a single debtor and without selling a single unit of stock, can we pay any part of the bills today?",
        simple_txt="Only money that is already money (or can be sold on the stock exchange this afternoon). Cash at bank, cash in hand, and Treasury bills / listed securities held as current investments. Nothing else.",
        purpose="To test emergency liquidity. A firm that looks fine on the current and quick ratios can still bounce a cheque if debtors are slow and the bank will not extend the overdraft. This ratio is that cheque-book test.",
        formula_expr="Absolute liquid ratio = (Cash and bank + Marketable securities) ÷ Current liabilities",
        formula_note="Also called cash ratio or super-quick ratio. Marketable securities = current investments that can be sold at once. Do not include long-term investments.",
        components=[
            [
                "Cash and cash equivalents",
                "Cash in hand, cash at bank, short-term deposits that are as good as cash.",
                "BS → Cash and cash equivalents. Kaveri: "
                + rupee(CASH)
                + ".",
            ],
            [
                "Marketable securities",
                "Current investments: listed shares, T-bills, mutual-fund units held to be sold any day.",
                "Kaveri: nil. If a paper gives “current investments "
                + rupee(40000)
                + "”, add them to cash.",
            ],
            [
                "Current liabilities",
                "Same CL as current and quick.",
                "Kaveri: "
                + rupee(CL_)
                + ".",
            ],
        ],
        pick="Take the cash-and-cash-equivalents line. Add current investments / marketable securities if given. Do not add debtors. Do not add stock. Divide by CL.",
        steps_list=[
            "Pick cash and bank. Add marketable securities / current investments.",
            "Pick current liabilities (same as current ratio).",
            "Divide. Write as x : 1.",
            "Comment against 0.5 : 1 if the question asks for a comment.",
        ],
        high="The firm can pay a large slice of bills today. Useful in a credit freeze.",
        low="The firm depends on collecting debtors or selling stock or drawing an overdraft. Normal for a well-run trader, dangerous if debtors are already slow.",
        too_high="Cash hoard. Opportunity cost: that cash could repay a loan, earn in the business, or be paid as dividend. A cash ratio of 2 is usually poor treasury management, not strength.",
        ex_num="K3",
        work_formula="Absolute liquid ratio = (Cash + Marketable securities) ÷ CL",
        work_pick="Cash "
        + rupee(CASH)
        + ", marketable securities nil, CL "
        + rupee(CL_)
        + ".",
        work_arith=rupee(CASH)
        + " ÷ "
        + rupee(CL_)
        + " = 80,000 ÷ 1,50,000 = 8/15 = 0.5333…",
        work_answer="0.53 : 1 &nbsp;(exactly 8 : 15)",
        kaveri_read="Just above the 0.5 : 1 rule of thumb. Kaveri can pay a little more than half its current bills from cash already in the bank, without waiting for a debtor. Comfortable, not idle.",
        mistakes_list=[
            "Adding debtors. Debtors are quick, not absolute liquid.",
            "Adding long-term investments. A 5-year bond is not cash.",
            "Netting off overdraft against cash without being asked, then also keeping overdraft in CL — you would double-count the benefit.",
        ],
        mem="Absolute = already money. Cash + marketable securities only. Ideal about half a rupee of cash per rupee of CL (0.5 : 1).",
    )


def _bs_de() -> str:
    return ratio_section(
        heading="5.4 Debt-equity ratio",
        bucket="Balance Sheet ratio. Purpose family: solvency / leverage / capital structure.",
        ideal="No single ideal. Many Indian textbooks quote 2 : 1 as an outer ceiling for long-term debt : equity (debt not more than twice equity), and 1 : 1 as comfortable. Trading firms often sit well below 1 : 1. Banks have their own covenants.",
        meaning="The debt-equity ratio compares long-term outside funds with owners’ funds. It asks: for every rupee the owners have committed, how many rupees have long-term lenders committed?",
        simple_txt="It is the see-saw between borrowed money and own money. High debt-equity means the see-saw is heavy on the lenders’ side — cheaper (interest is tax-deductible) but riskier (interest must be paid even in a bad year).",
        purpose="To judge long-term solvency and financial risk. A lender looks at this before sanctioning a term loan. An owner looks at this before taking more debt to “gear up” return on equity.",
        formula_expr="Debt-equity ratio = Long-term debt ÷ Shareholders’ funds &nbsp;&nbsp;(MBA exam standard)",
        formula_note="Two versions exist. (A) Long-term debt ÷ Shareholders’ funds — the common Indian MBA version, used in this chapter. (B) Total debt (long-term + current) ÷ Shareholders’ funds — used when the question says “total debt” or “debt” without “long-term”. Write which version you are using.",
        components=[
            [
                "Long-term debt (version A)",
                "Debentures, term loans, bonds, and sometimes preference share capital (fixed-dividend outsider). Exclude trade payables.",
                "Kaveri: long-term borrowings "
                + rupee(LTD)
                + ". No preference capital.",
            ],
            [
                "Total debt (version B)",
                "Long-term debt + current liabilities.",
                "Kaveri: "
                + rupee(LTD)
                + " + "
                + rupee(CL_)
                + " = "
                + rupee(TD)
                + ".",
            ],
            [
                "Shareholders’ funds (equity)",
                "Equity share capital + reserves and surplus − fictitious assets (preliminary expenses, P&L debit balance).",
                "Kaveri: "
                + rupee(ESC)
                + " + "
                + rupee(RES)
                + " = "
                + rupee(SF)
                + ". No fictitious assets.",
            ],
        ],
        pick="Do not use equity share capital alone — reserves belong to owners too. Do not put trade payables into long-term debt for version A. If preference capital is given, check the question: some papers treat it as debt (fixed dividend), some as equity. The common MBA treatment of capital gearing puts preference with debt; for debt-equity, follow the question’s wording. Kaveri has no preference, so the issue does not arise.",
        steps_list=[
            "Decide version A (long-term) or B (total) from the wording.",
            "Shareholders’ funds = equity share capital + reserves − fictitious assets.",
            "Divide debt by shareholders’ funds. Write as x : 1 (or as a pure number).",
            "Comment: higher = more risk for owners and lenders; lower = more cushion, but maybe unused cheap debt.",
        ],
        high="Lenders have a large claim. Interest burden is heavy. A bad year can wipe owners out (and then hurt lenders). High financial risk. Some owners like it because a successful year magnifies ROE — that is gearing.",
        low="Owners have financed most of the firm. Safe for lenders. Conservative. ROE will not get a debt-boost.",
        too_high="A debt-equity of 4 : 1 on long-term funds is usually dangerous outside specialised project finance. One missed season and the firm cannot service interest. Banks will not lend more. Too low (say 0 : 1 with no debt at all) can also be ‘bad’ in a value sense: the firm may be refusing cheap, tax-deductible funds.",
        ex_num="K4",
        work_formula="Debt-equity (long-term) = Long-term debt ÷ Shareholders’ funds",
        work_pick="Long-term debt "
        + rupee(LTD)
        + "; Shareholders’ funds "
        + rupee(ESC)
        + " + "
        + rupee(RES)
        + " = "
        + rupee(SF)
        + ".",
        work_arith=rupee(LTD)
        + " ÷ "
        + rupee(SF)
        + " = 2,00,000 ÷ 6,00,000 = 1/3 = 0.333…",
        work_answer="0.33 : 1 &nbsp;(or 1 : 3)",
        kaveri_read="Conservative. For every "
        + rupee(3)
        + " of owners’ money there is "
        + rupee(1)
        + " of long-term debt. Lenders are well covered. Version B (total debt) = "
        + rupee(TD)
        + " ÷ "
        + rupee(SF)
        + " = "
        + _ratio_pair(TD, SF)
        + " — still modest, because current liabilities are only trade credit, not a bank overdraft.",
        mistakes_list=[
            "Using only share capital "
            + rupee(ESC)
            + " as equity and ignoring reserves "
            + rupee(RES)
            + ". That would wrongly give 2,00,000/4,00,000 = 0.5 instead of 0.33.",
            "Putting current liabilities into long-term debt when the question said “long-term debt-equity”.",
            "Inverting the ratio (equity/debt) without saying so. Some papers want Equity-debt; read the name.",
            "Treating a bank overdraft as long-term debt. It is current.",
        ],
        mem="Debt over Equity = outsiders over owners. “DE” — Debt first, Equity under it. Low is safe; high is geared.",
        extra=example(
            "K4b",
            "Easy",
            "Both versions, side by side, from Kaveri",
            work_table(
                "Version A: LTD ÷ SF &nbsp;&nbsp; Version B: (LTD + CL) ÷ SF",
                "LTD "
                + rupee(LTD)
                + ", CL "
                + rupee(CL_)
                + ", SF "
                + rupee(SF),
                "A: "
                + rupee(LTD)
                + " ÷ "
                + rupee(SF)
                + " = 0.33 : 1. &nbsp; B: "
                + rupee(TD)
                + " ÷ "
                + rupee(SF)
                + " = 3,50,000 ÷ 6,00,000 = 35/60 = 7/12 = 0.58 : 1.",
                "A = 0.33 : 1 (use unless the question says total debt); B = 0.58 : 1",
            )
            + p(
                "In the rest of this chapter, “debt-equity” means version A (long-term), which is the common MBA exam version."
            ),
        ),
    )


def _bs_prop() -> str:
    return ratio_section(
        heading="5.5 Proprietary ratio",
        bucket="Balance Sheet ratio. Purpose family: solvency / capital structure.",
        ideal="Higher is safer. A common comfort zone is 0.60 to 0.75 (60%–75% of assets financed by owners). There is no single statutory ideal.",
        meaning="The proprietary ratio is shareholders’ funds divided by total assets (or total of the Balance Sheet). It is the owners’ slice of the whole pie. It asks: what fraction of every rupee of assets is financed by the owners, not by outsiders?",
        simple_txt="If the proprietary ratio is 0.63, then 63 paise of every asset-rupee is owners’ money, and 37 paise is owed to lenders and creditors. It is the complement of the outsider’s-funds ratio.",
        purpose="To judge the cushion available to creditors. A high proprietary ratio means outsiders have a thick layer of owners’ money standing in front of them if the firm is wound up.",
        formula_expr="Proprietary ratio = Shareholders’ funds ÷ Total assets &nbsp;&nbsp;(or × 100 for a percentage)",
        formula_note="Total assets = total of the Balance Sheet = Equity + all liabilities. Outsiders’ funds ratio = 1 − proprietary ratio (when both are in the same units).",
        components=[
            [
                "Shareholders’ funds",
                "Equity share capital + reserves − fictitious assets. Same equity you used in debt-equity.",
                "Kaveri: "
                + rupee(SF)
                + ".",
            ],
            [
                "Total assets",
                "Non-current assets + current assets. Equals the Balance Sheet total.",
                "Kaveri: "
                + rupee(FA)
                + " + "
                + rupee(CA)
                + " = "
                + rupee(TA)
                + ".",
            ],
        ],
        pick="Numerator is not share capital alone. Denominator is the BS total, not just fixed assets. If fictitious assets exist, deduct them from shareholders’ funds and also from total assets (they are not real assets).",
        steps_list=[
            "Compute shareholders’ funds.",
            "Take the Balance Sheet total as total assets.",
            "Divide. Express as a ratio (0.63 : 1) or as 63%.",
            "Optionally compute outsiders’ funds ratio = 1 − this, as a check.",
        ],
        high="Strong owner-cushion. Easy to borrow more if needed. Conservative structure.",
        low="Assets are mostly outsider-financed. Creditors are less protected. A sequence of losses will wipe equity fast.",
        too_high="Almost no debt. Safe, but the firm may be under-levered: it is not using tax-deductible interest, and ROE may be lower than it could be. “Too high” here is a strategy comment, not a distress comment.",
        ex_num="K5",
        work_formula="Proprietary ratio = Shareholders’ funds ÷ Total assets",
        work_pick="SF "
        + rupee(SF)
        + "; Total assets "
        + rupee(TA)
        + ".",
        work_arith=rupee(SF)
        + " ÷ "
        + rupee(TA)
        + " = 6,00,000 ÷ 9,50,000 = 60/95 = 12/19 = 0.631578…",
        work_answer="0.63 : 1 &nbsp;or 63.16%",
        kaveri_read="Owners finance about 63% of assets. Outsiders finance about 37% ("
        + rupee(TD)
        + " ÷ "
        + rupee(TA)
        + " = "
        + _pct(TD, TA)
        + "). A healthy owner-majority. Matches the low debt-equity of 0.33 : 1.",
        mistakes_list=[
            "Denominator = fixed assets only. Wrong. It is total assets.",
            "Numerator = equity share capital only, skipping reserves.",
            "Adding long-term debt to the numerator. That would be capital employed / total assets, a different ratio.",
        ],
        mem="Proprietary = proprietors’ piece of the pie = owners’ funds / total assets. Bigger slice, safer creditors.",
    )


def _bs_gear() -> str:
    return ratio_section(
        heading="5.6 Capital gearing ratio",
        bucket="Balance Sheet ratio. Purpose family: solvency / leverage.",
        ideal="A firm is low-geared when equity funds exceed fixed-charge funds (ratio < 1 in the version used here). High-geared when fixed-charge funds exceed equity (ratio > 1). Neither is “ideal”; high gearing magnifies both profit and loss.",
        meaning="Capital gearing measures the mix of fixed-interest (and fixed-dividend) funds versus equity owners’ funds. It is debt-equity with preference capital parked on the debt side, because preference pays a fixed dividend just as debt pays a fixed interest.",
        simple_txt="Gearing is a bicycle gear. In a high gear, a small push on the pedals (a rise in EBIT) moves the bicycle a long way (a big rise in profit for equity). Going uphill (a fall in EBIT) then becomes very hard. Low gear is safer and slower.",
        purpose="To see how sensitive equity earnings are to a change in EBIT, and to classify the firm as high-geared or low-geared. This is a favourite theory-plus-small-numerical question.",
        formula_expr="Capital gearing = (Preference share capital + Long-term debt) ÷ Equity shareholders’ funds",
        formula_note="This is the common MBA exam version (fixed-charge funds / equity funds). Some papers invert it: Equity funds ÷ (Preference + long-term debt). Some use equity share capital only in the denominator (excluding reserves). State the version. In these notes: numerator = pref + LTD; denominator = equity share capital + reserves (no pref in Kaveri).",
        components=[
            [
                "Fixed-charge funds",
                "Preference share capital (fixed dividend) + debentures + long-term loans (fixed interest).",
                "Kaveri: preference nil + LTD "
                + rupee(LTD)
                + " = "
                + rupee(LTD)
                + ".",
            ],
            [
                "Equity shareholders’ funds",
                "Equity share capital + reserves − fictitious assets. Do not put preference here.",
                "Kaveri: "
                + rupee(SF)
                + ".",
            ],
        ],
        pick="If there is no preference capital (Kaveri, and many numericals), capital gearing collapses to the same arithmetic as long-term debt-equity. Still write the full formula with “preference = 0”, so the examiner sees you know where preference would go.",
        steps_list=[
            "List preference capital and all long-term borrowings. Add them. This is the numerator.",
            "Equity share capital + reserves − fictitious assets. This is the denominator.",
            "Divide. If the ratio is less than 1, say “low geared”. If more than 1, say “high geared”.",
            "One sentence: high gearing helps equity in good years and hurts it in bad years.",
        ],
        high="High geared: a large share of capital carries a fixed charge. Equity earnings swing more than EBIT. Risk for equity holders and for lenders.",
        low="Low geared: most capital is equity. Earnings are more stable. Safer, less magnified.",
        too_high="A very high gearing next to a thin interest-coverage is a distress signal. Too low means unused leverage — a comment, not a crisis.",
        ex_num="K6",
        work_formula="Capital gearing = (Preference capital + Long-term debt) ÷ Equity shareholders’ funds",
        work_pick="Preference nil; LTD "
        + rupee(LTD)
        + "; Equity funds "
        + rupee(SF)
        + ".",
        work_arith="(0 + "
        + rupee(LTD)
        + ") ÷ "
        + rupee(SF)
        + " = 2,00,000 ÷ 6,00,000 = 1/3 = 0.33.",
        work_answer="0.33 &nbsp;(low geared, because 0.33 < 1)",
        kaveri_read="Low geared. Equity funds are three times fixed-charge funds. A fall in EBIT will not quickly wipe the equity residual. Combined with interest coverage of 5 times (computed later), gearing is comfortable.",
        mistakes_list=[
            "Putting preference capital in the denominator. Preference is a fixed-charge fund — numerator in this version.",
            "Using only equity share capital in the denominator and leaving out reserves, unless the paper’s formula is printed that way.",
            "Saying “high geared” because a 0.33 exists. High/low is judged against 1 in this version, or by the paper’s own wording.",
            "Confusing capital gearing with operating gearing (fixed operating costs). Capital gearing is about finance, not about rent and depreciation.",
        ],
        mem="Gearing = fixed-charge money over equity money. Preference sits with debt, not with equity. Below 1 = low gear = safer.",
        extra=keypoint(
            "If a paper prints Capital gearing = Equity / (Preference + Debentures), then a ratio greater than 1 is low geared (more equity). "
            "Always read the printed formula. The words “high geared” and “low geared” follow whichever version the paper chose, not a universal fraction."
        ),
    )


def _bs_falt() -> str:
    return ratio_section(
        heading="5.7 Fixed assets to long-term funds ratio",
        bucket="Balance Sheet ratio. Purpose family: solvency / asset-financing structure.",
        ideal="Should be less than 1 (or < 100%). Fixed assets should be financed by long-term funds, with some long-term funds left over for working capital. A ratio above 1 means part of the factory was paid for with money that has to be repaid this year — dangerous.",
        meaning="This ratio is net fixed assets divided by long-term funds (shareholders’ funds + long-term debt = capital employed). It asks: what fraction of long-term money is locked in long-term assets?",
        simple_txt="A godown should be paid for with a term loan or with owners’ money, not with next month’s creditor money. This ratio checks that matching: long-term assets against long-term funds.",
        purpose="To test whether the firm has used short-term funds to buy fixed assets (a classic way firms get into a liquidity trap). Also to see how much long-term finance remains for working capital.",
        formula_expr="Fixed assets to long-term funds = Net fixed assets ÷ Long-term funds",
        formula_note="Long-term funds = Shareholders’ funds + Long-term debt = Capital employed. Net fixed assets = gross FA − accumulated depreciation. Express as a ratio or as a percentage.",
        components=[
            [
                "Net fixed assets",
                "Property, plant and equipment after depreciation. Exclude current assets. Include capital work-in-progress if the question treats it as FA.",
                "Kaveri: "
                + rupee(FA)
                + ".",
            ],
            [
                "Long-term funds",
                "Equity + reserves + long-term borrowings. Same as capital employed.",
                "Kaveri: "
                + rupee(SF)
                + " + "
                + rupee(LTD)
                + " = "
                + rupee(CE)
                + ".",
            ],
        ],
        pick="Use net FA, not gross, unless the question gives only gross and no depreciation. Denominator is not total liabilities — current liabilities stay out.",
        steps_list=[
            "Pick net fixed assets from the asset side.",
            "Long-term funds = shareholders’ funds + long-term debt.",
            "Divide. If the answer is more than 1, write a warning sentence: part of FA is financed by current liabilities.",
            "The leftover fraction (1 − this ratio) is the share of long-term funds supporting working capital.",
        ],
        high="A larger share of long-term funds is locked in FA. If the ratio is still below 1, this is a structure comment, not yet distress.",
        low="Plenty of long-term funds sit in working capital. Very liquid structure. Check that WC itself is not idle (current ratio, stock turnover).",
        too_high="Above 1: the firm bought a machine with creditor money or with an overdraft. When the creditor asks to be paid, the machine cannot be sold overnight. This is a classic cause of failure. Too low (say 0.3 in a factory) may mean under-investment in capacity.",
        ex_num="K7",
        work_formula="FA to long-term funds = Net fixed assets ÷ (SF + LTD)",
        work_pick="Net FA "
        + rupee(FA)
        + "; long-term funds "
        + rupee(CE)
        + ".",
        work_arith=rupee(FA)
        + " ÷ "
        + rupee(CE)
        + " = 6,50,000 ÷ 8,00,000 = 65/80 = 13/16 = 0.8125.",
        work_answer="0.81 : 1 &nbsp;or 81.25%",
        kaveri_read="81.25% of long-term funds are in the godown and office; 18.75% ("
        + rupee(WC)
        + " out of "
        + rupee(CE)
        + ") supports working capital. The ratio is below 1, so no short-term money is trapped in FA. Healthy matching of funds.",
        mistakes_list=[
            "Using gross fixed assets when accumulated depreciation is given. Use net.",
            "Denominator = shareholders’ funds only, omitting long-term debt. That is a different (stricter) ratio.",
            "Comparing with 2 : 1 (the current-ratio ideal). Wrong family. Here the ceiling of comfort is 1 : 1.",
        ],
        mem="Match the life: long asset, long money. FA / long-term funds should stay under 1. Above 1 = a machine bought on a credit card.",
    )


def _bs_caprop() -> str:
    return ratio_section(
        heading="5.8 Current assets to proprietary funds ratio",
        bucket="Balance Sheet ratio. Purpose family: structure / liquidity of owners’ money.",
        ideal="No universal ideal. A high ratio means a large share of owners’ money is in working capital (typical of a trader). A low ratio means owners’ money is mostly in fixed assets (typical of a heavy manufacturer).",
        meaning="Current assets divided by shareholders’ funds. It asks: how many rupees of current assets does the firm hold for every rupee of owners’ funds?",
        simple_txt="It is a snapshot of where the owners’ money is sitting on the asset side — in stock, debtors and cash, versus in the building. A trader like Kaveri should show a noticeable slice of owners’ funds in current assets; a cement plant should not.",
        purpose="To judge whether owners’ funds are tied up in working capital (which should revolve) or in long-term assets. Useful when comparing a trader with a manufacturer, or this year with last year.",
        formula_expr="Current assets to proprietary funds = Current assets ÷ Shareholders’ funds",
        formula_note="Proprietary funds = shareholders’ funds. Same numerator as the current ratio; different denominator.",
        components=[
            [
                "Current assets",
                "Inventory + receivables + cash + prepaid + other CA.",
                "Kaveri: "
                + rupee(CA)
                + ".",
            ],
            [
                "Shareholders’ / proprietary funds",
                "Equity share capital + reserves − fictitious assets.",
                "Kaveri: "
                + rupee(SF)
                + ".",
            ],
        ],
        pick="Same CA as current ratio. Same SF as debt-equity and proprietary ratio. Do not use capital employed in the denominator — that would include long-term debt.",
        steps_list=[
            "Total current assets.",
            "Compute shareholders’ funds.",
            "Divide. Write as a ratio or as a percentage.",
            "Read it with the nature of the business (trader vs manufacturer).",
        ],
        high="A large part of owners’ money is in stock, debtors and cash. Fine for a wholesaler. For a factory it may mean idle WC or thin FA.",
        low="Owners’ money is mostly in fixed assets. Fine for a factory. For a trader it may mean the firm is under-stocked or under-banked.",
        too_high="Owners have funded a mountain of stock and debtors. Check stock turnover and collection period — the mountain may not be moving. Too low in a trading firm: possible stock-outs and lost sales.",
        ex_num="K8",
        work_formula="CA to proprietary funds = Current assets ÷ Shareholders’ funds",
        work_pick="CA "
        + rupee(CA)
        + "; SF "
        + rupee(SF)
        + ".",
        work_arith=rupee(CA)
        + " ÷ "
        + rupee(SF)
        + " = 3,00,000 ÷ 6,00,000 = 1/2 = 0.50.",
        work_answer="0.50 : 1 &nbsp;or 50%",
        kaveri_read="Half of owners’ funds sit in current assets — sensible for a trader. The other half, plus the entire long-term loan, sits in the godown (see FA to long-term funds 81%). Structure fits the business.",
        mistakes_list=[
            "Denominator = capital employed. That mixes lenders’ money into “proprietary” funds — the name of the ratio forbids it.",
            "Using working capital as the numerator. The name says current assets, not net current assets.",
        ],
        mem="CA over owners’ money. A trader’s number is higher than a factory’s. Do not hunt for a 2 : 1 ideal — that ideal belongs to the current ratio.",
    )


# ---------------------------------------------------------------------------
# 6. Revenue ratios
# ---------------------------------------------------------------------------


def _rev_intro() -> str:
    return (
        h2("6. Revenue (P&L) ratios", "rev")
        + lead(
            "Both figures come from the Statement of Profit and Loss. These are "
            + b("margin")
            + " ratios: how many paise of each sales-rupee survive at each layer of cost. "
            "No Balance-Sheet number is allowed in this section."
        )
        + p(
            "Picture the P&L as a staircase down from sales: COGS is cut first (gross profit remains), then operating expenses (operating profit remains), then interest (PBT remains), then tax (PAT remains). Each ratio is one step’s leftover, as a percentage of sales."
        )
        + formula(
            "Operating ratio + Operating profit ratio ≈ 100% &nbsp;(when other income is nil, as in Kaveri)",
            "If your two answers do not add to 100, you have either included interest in operating cost, or included other income in sales, or used PAT instead of operating profit. Check before you move on.",
        )
    )


def _rev_gp() -> str:
    return ratio_section(
        heading="6.1 Gross profit ratio (GP ratio)",
        bucket="Revenue ratio — both figures from the P&L. Purpose family: profitability (trading margin).",
        ideal="Depends on the trade. A grocer may live on 12%; a boutique on 50%. Kaveri’s 25% is a healthy wholesale-trading margin. Compare with last year and with rivals, not with a universal number.",
        meaning="Gross profit ratio is gross profit divided by revenue from operations (net sales), times 100. It is the margin left after paying for the goods themselves, and before paying people, rent, interest and tax.",
        simple_txt="Out of every ₹100 of sales, how many rupees are left after the cost of those goods? If GP ratio is 25%, ₹25 is left and ₹75 went to COGS.",
        purpose="To judge trading efficiency: buying well, selling well, not leaking goods. A fall in GP ratio, with selling prices unchanged, usually means cost of goods rose or stock was lost. It is the first profitability ratio any analyst computes.",
        formula_expr="Gross profit ratio = (Gross profit ÷ Revenue from operations) × 100",
        formula_note="Gross profit = Sales − COGS. COGS = Opening stock + Purchases − Closing stock (+ direct expenses if given). Use net sales (after returns). Do not use total assets or capital.",
        components=[
            [
                "Gross profit",
                "Sales minus cost of goods sold. The trading leftover.",
                "Kaveri: "
                + rupee(SALES)
                + " − "
                + rupee(COGS)
                + " = "
                + rupee(GP)
                + ". Also 25% × sales, by construction.",
            ],
            [
                "Revenue from operations / Net sales",
                "Sales of goods and services, after returns, usually excluding other income (interest, rent received, profit on sale of asset).",
                "Kaveri: "
                + rupee(SALES)
                + ". Other income is nil.",
            ],
            [
                "COGS (to build GP if GP is not given)",
                "Opening stock + purchases − closing stock (+ carriage inward, wages if the paper treats them as direct).",
                "Kaveri: "
                + rupee(OP_STOCK)
                + " + "
                + rupee(PURCHASES)
                + " − "
                + rupee(CL_STOCK)
                + " = "
                + rupee(COGS)
                + ".",
            ],
        ],
        pick="Use net sales, not cash sales only, and not sales + other income. If the question gives GP ratio and sales, GP = rate × sales. If it gives opening, purchases, closing, build COGS first, then GP = sales − COGS.",
        steps_list=[
            "Compute COGS if needed: opening stock + purchases − closing stock.",
            "GP = Sales − COGS. (Or GP = GP% × Sales if the rate is given.)",
            "GP ratio = GP ÷ Sales × 100. Unit is %.",
            "Comment: a fall is a trading problem (price, cost, or theft); a rise is a trading improvement — or a change in mix.",
        ],
        high="Strong trading margin. Either selling prices are firm, or the firm buys cheap, or the mix has shifted to richer goods.",
        low="Thin trading margin. A small rise in cost or a discount war will wipe GP. Danger if operating expenses are already high.",
        too_high="Prices may be too high and volume may be suffering (check sales trend and stock turnover). Or closing stock may have been overvalued — window dressing that inflates GP. Always read GP with stock turnover.",
        ex_num="K9",
        work_formula="GP ratio = (GP ÷ Sales) × 100",
        work_pick="GP "
        + rupee(GP)
        + "; Sales "
        + rupee(SALES)
        + ".",
        work_arith="("
        + rupee(GP)
        + " ÷ "
        + rupee(SALES)
        + ") × 100 = (2,50,000 ÷ 10,00,000) × 100 = 0.25 × 100 = 25%.",
        work_answer="25%",
        kaveri_read="A quarter of every sales-rupee is gross profit. For a wholesaler this is a solid trading margin. Whether it is “good” depends on rivals; as a standalone number it is healthy, and it leaves room for "
        + rupee(OPEX)
        + " of operating expenses, "
        + rupee(INTEREST)
        + " of interest and "
        + rupee(TAX)
        + " of tax, with "
        + rupee(PAT)
        + " still standing at the end.",
        mistakes_list=[
            "Using PAT or operating profit in the numerator. Those are different ratios.",
            "Using credit sales only. GP is on total sales (cash + credit).",
            "Adding other income to sales. Other income is not operations (unless the question says so).",
            "Computing GP as Sales − Purchases, ignoring stock. You must adjust for opening and closing inventory.",
        ],
        mem="GP sits on the top step: only COGS has been cut. GP / Sales × 100. If stock changes, Purchases ≠ COGS.",
    )


def _rev_np() -> str:
    return ratio_section(
        heading="6.2 Net profit ratio (NP ratio)",
        bucket="Revenue ratio. Purpose family: profitability (bottom-line margin).",
        ideal="Depends on the industry. A 9% net margin on a trading business is respectable. Always pair with GP ratio: the gap between GP% and NP% is everything that is not COGS.",
        meaning="Net profit ratio is profit after tax (the year’s leftover for owners) divided by sales, times 100. Some papers use profit before tax. Read the question. These notes use PAT as the default “net profit”.",
        simple_txt="Out of every ₹100 of sales, how many rupees finally belong to the owners after every cost, including interest and tax? For Kaveri, 9 rupees.",
        purpose="To judge overall profitability of sales. Investors, owners and the tax officer all look here. A stable GP ratio with a falling NP ratio means the leak is below GP — operating expenses, interest or tax.",
        formula_expr="Net profit ratio = (Profit after tax ÷ Revenue from operations) × 100",
        formula_note="MBA default in these notes: PAT / Sales × 100. PBT version = PBT / Sales × 100 — mention it if the question says “net profit before tax”. Do not deduct preference dividend unless the question asks for profit available to equity / net profit ratio for equity holders.",
        components=[
            [
                "Profit after tax (PAT)",
                "Profit for the year after interest and tax. The bottom line.",
                "Kaveri: "
                + rupee(PAT)
                + ".",
            ],
            [
                "Profit before tax (PBT version)",
                "EBIT − interest. Used when the paper says “net profit before tax”.",
                "Kaveri: "
                + rupee(PBT)
                + ", which would give "
                + _pct(PBT, SALES)
                + ".",
            ],
            [
                "Sales",
                "Revenue from operations, same as GP ratio.",
                "Kaveri: "
                + rupee(SALES)
                + ".",
            ],
        ],
        pick="Default numerator is PAT (after tax, after interest). If the trial balance gives only “net profit” with no tax line, use that figure and say so. Denominator is sales, not capital, not total assets (those become ROE and ROA).",
        steps_list=[
            "Identify whether the paper wants PAT or PBT.",
            "Pick sales (revenue from operations).",
            "Divide × 100. Unit is %.",
            "Read next to GP ratio: the gap is operating expenses + interest + tax (and other income, if any).",
        ],
        high="A large slice of sales reaches owners. Pricing, cost control and a light interest burden are all working.",
        low="Sales are busy but owners see little. Find the layer: GP low? Then trading. GP healthy but NP low? Then opex, interest or tax.",
        too_high="Unusually high NP% can mean under-investment (too little depreciation, too little marketing) or a one-time other income. Check quality of earnings. Too high is rare; more often “high” is simply good.",
        ex_num="K10",
        work_formula="NP ratio = (PAT ÷ Sales) × 100",
        work_pick="PAT "
        + rupee(PAT)
        + "; Sales "
        + rupee(SALES)
        + ".",
        work_arith="("
        + rupee(PAT)
        + " ÷ "
        + rupee(SALES)
        + ") × 100 = (90,000 ÷ 10,00,000) × 100 = 9%.",
        work_answer="9% &nbsp;(PBT version = "
        + _pct(PBT, SALES)
        + ")",
        kaveri_read="9 paise of every sales-rupee is leftover for owners. GP was 25 paise, so 16 paise were spent on employees, other opex, interest and tax (6 + 4 + 3 + 3). The margin is thin enough that an interest-rate rise or a wage rise would be felt, but it is a real profit, not a rounding error.",
        mistakes_list=[
            "Using EBIT in the numerator and still calling it net profit ratio. That is the operating profit ratio.",
            "Using shareholders’ funds in the denominator. That is ROE.",
            "Taking PAT after an extra deduction of drawings or dividend. Dividend is an appropriation, not an expense; NP ratio uses PAT.",
        ],
        mem="Net = the last leftover. PAT / Sales × 100. Default is after tax. If the paper says before tax, obey the paper.",
    )


def _rev_opr() -> str:
    return ratio_section(
        heading="6.3 Operating profit ratio",
        bucket="Revenue ratio. Purpose family: profitability of operations (before financing and tax).",
        ideal="Higher is better, given the industry. It should sit between GP% and NP%. For Kaveri: GP 25%, operating 15%, net 9% — a clean staircase.",
        meaning="Operating profit ratio is operating profit (EBIT / PBIT) divided by sales, times 100. Operating profit is profit from the core business, before interest (a financing choice) and before tax (a government claim).",
        simple_txt="Ignore how the firm is financed. Ignore tax. Just ask: of each sales-rupee, how much does the business itself produce as profit from operations? That is this ratio.",
        purpose="To compare two firms with different debt and different tax situations on the quality of the business, not the quality of the financing. Also the numerator of ROCE, so this ratio and capital turnover together drive ROCE (see DuPont later).",
        formula_expr="Operating profit ratio = (Operating profit ÷ Sales) × 100",
        formula_note="Operating profit = EBIT = GP − operating expenses (employee + other opex including depreciation), or = PBT + interest, or = PAT + tax + interest. Other income that is not operating is kept out.",
        components=[
            [
                "Operating profit / EBIT / PBIT",
                "Profit before interest and tax, from operations.",
                "Kaveri three checks: GP "
                + rupee(GP)
                + " − opex "
                + rupee(OPEX)
                + " = "
                + rupee(EBIT)
                + "; PBT "
                + rupee(PBT)
                + " + interest "
                + rupee(INTEREST)
                + " = "
                + rupee(EBIT)
                + "; PAT "
                + rupee(PAT)
                + " + tax "
                + rupee(TAX)
                + " + interest "
                + rupee(INTEREST)
                + " = "
                + rupee(EBIT)
                + ".",
            ],
            [
                "Sales",
                "Revenue from operations.",
                "Kaveri: "
                + rupee(SALES)
                + ".",
            ],
        ],
        pick="Build EBIT from whatever the paper gives. The safest rebuild is PBT + interest, because those two lines are almost always present. Do not use PAT. Do not deduct interest.",
        steps_list=[
            "Build operating profit: GP − operating expenses, or PBT + interest.",
            "Confirm interest is not already deducted (if you started from GP, do not deduct it; if you started from PBT, add it back).",
            "Divide by sales × 100.",
            "Check: operating profit% + operating ratio should be 100% if other income is nil.",
        ],
        high="The core business is earning well, regardless of how it is financed.",
        low="Operations are weak. Even a zero-debt firm would struggle. Look at GP (trading) and at opex (overheads).",
        too_high="May mean the firm is starving marketing, maintenance or depreciation. Check whether the profit is repeatable. Also check other income: a one-time sale of a building is not operating profit.",
        ex_num="K11",
        work_formula="Operating profit ratio = (EBIT ÷ Sales) × 100",
        work_pick="EBIT "
        + rupee(EBIT)
        + "; Sales "
        + rupee(SALES)
        + ".",
        work_arith="("
        + rupee(EBIT)
        + " ÷ "
        + rupee(SALES)
        + ") × 100 = (1,50,000 ÷ 10,00,000) × 100 = 15%.",
        work_answer="15%",
        kaveri_read="15 paise of every sales-rupee is operating profit. That is the pool from which interest "
        + rupee(INTEREST)
        + " (3 paise) and tax "
        + rupee(TAX)
        + " (3 paise) are paid, leaving 9 paise of PAT. Operations, not financing, are doing the work.",
        mistakes_list=[
            "Using PAT or PBT and still labelling it operating profit ratio.",
            "Deducting interest when you started from GP. Interest is not an operating expense.",
            "Including other income (rent received, profit on sale of FA) inside operating profit when the paper separates it. If the paper is silent and the amount is small, state your assumption.",
        ],
        mem="Operating profit = the business before the banker and the tax officer. EBIT / Sales × 100. Add interest back if you start from PBT.",
    )


def _rev_or() -> str:
    return ratio_section(
        heading="6.4 Operating ratio",
        bucket="Revenue ratio. Purpose family: cost / efficiency of operations. It is the cost-cousin of the operating profit ratio.",
        ideal="Lower is better. There is no universal number. For Kaveri it should be 85% because operating profit is 15% and other income is nil.",
        meaning="Operating ratio is operating cost divided by sales, times 100. Operating cost is COGS plus operating expenses (employee benefits, other expenses including depreciation, selling and admin). Interest and tax are not operating costs.",
        simple_txt="Out of every ₹100 of sales, how many rupees were spent on running the business (goods + people + rent + depreciation + selling)? The rest is operating profit. High operating ratio = a heavy cost stomach.",
        purpose="To measure the cost-heaviness of operations. A rising operating ratio is a warning even if sales are rising: costs are eating a bigger bite. Management uses the pieces (material, labour, overhead) as expense ratios to find the bite.",
        formula_expr="Operating ratio = (Operating cost ÷ Sales) × 100 &nbsp;&nbsp; where Operating cost = COGS + Operating expenses",
        formula_note="Interest is a finance cost, not an operating cost. Tax is not an operating cost. Operating ratio + operating profit ratio = 100% when other income is ignored.",
        components=[
            [
                "COGS",
                "Cost of the goods that were sold.",
                "Kaveri: "
                + rupee(COGS)
                + ".",
            ],
            [
                "Operating expenses",
                "Employee benefits, other expenses, depreciation, selling and distribution, admin. Not interest. Not tax. Not loss on sale of FA (non-operating) unless the paper dumps it in “other expenses” without a split.",
                "Kaveri: employee "
                + rupee(EMP)
                + " + other opex "
                + rupee(OTHER_OPEX)
                + " = "
                + rupee(OPEX)
                + ".",
            ],
            [
                "Operating cost",
                "COGS + operating expenses.",
                "Kaveri: "
                + rupee(COGS)
                + " + "
                + rupee(OPEX)
                + " = "
                + rupee(OP_COST)
                + ".",
            ],
            [
                "Sales",
                "Revenue from operations.",
                "Kaveri: "
                + rupee(SALES)
                + ".",
            ],
        ],
        pick="Add COGS and every operating expense. Stop before finance costs and tax. If the paper gives a single “expenses” total that includes interest, subtract interest before you call it operating cost.",
        steps_list=[
            "Build COGS.",
            "Add operating expenses. Do not add interest or tax.",
            "Operating ratio = operating cost ÷ sales × 100.",
            "Cross-check: 100% − operating profit% should equal this, if other income is nil.",
        ],
        high="Operations swallow most of the sales-rupee. Little left as EBIT. A high-cost business, or an inefficient one.",
        low="Lean operations. More of each sale survives as operating profit.",
        too_high="Above 100% means operations lose money before interest — the core business is sick. “Too low” is unusual; if operating ratio is 40% in a grocery, check whether COGS was forgotten.",
        ex_num="K12",
        work_formula="Operating ratio = (COGS + Operating expenses) ÷ Sales × 100",
        work_pick="COGS "
        + rupee(COGS)
        + " + opex "
        + rupee(OPEX)
        + " = operating cost "
        + rupee(OP_COST)
        + "; Sales "
        + rupee(SALES)
        + ".",
        work_arith="("
        + rupee(OP_COST)
        + " ÷ "
        + rupee(SALES)
        + ") × 100 = (8,50,000 ÷ 10,00,000) × 100 = 85%.",
        work_answer="85%",
        kaveri_read="85 paise of every sales-rupee go in operating cost, 15 paise remain as EBIT. Check: 85% + 15% = 100%. The arithmetic of the two cousins agrees, so neither figure is mis-picked.",
        mistakes_list=[
            "Including interest in operating cost. Interest is finance, not operations. That mistake would give ("
            + rupee(OP_COST + INTEREST)
            + " ÷ "
            + rupee(SALES)
            + ") × 100 = 88%, and then 88% + 15% ≠ 100%.",
            "Using only COGS (that is a COGS-to-sales expense ratio, 75% for Kaveri, not the operating ratio).",
            "Using PAT in a “100 − NP%” shortcut. 100 − 9 = 91, which is not the operating ratio. The shortcut is 100 − operating profit%.",
        ],
        mem="Operating ratio is the COST twin. Operating profit ratio is the PROFIT twin. They add to 100. Interest stays out of both twins’ cost.",
        extra=keypoint(
            "Kaveri cross-check, write this once in the answer booklet: operating ratio 85% + operating profit ratio 15% = 100%. "
            "If a numerical you are solving does not add to 100, you have mixed interest or other income into the wrong line."
        ),
    )


def _rev_exp() -> str:
    return (
        h3("6.5 Expense ratios")
        + p(b("Syllabus bucket. ") + "Revenue ratios. Purpose family: cost structure.")
        + p(b("Ideal / comment. ") + "Lower is better for each cost, but a zero employee-cost ratio means there are no people. Read the mix, not a single line.")
        + definition(
            "An expense ratio is any single expense (or a group of expenses) divided by sales, times 100. "
            "The syllabus wants you to be able to write the formula for each material, labour, overhead, interest or tax line."
        )
        + simple(
            "GP ratio told you that 75 paise of each Kaveri sales-rupee went to COGS. Expense ratios name the other paise: employees 6, other opex 4, interest 3, tax 3. Together they are a pie chart of the P&L."
        )
        + why(
            "A rising operating ratio is a fog. Expense ratios turn on the light: was it wages, was it rent, was it interest? Management can only attack a named cost."
        )
        + formula(
            "Expense ratio = (Particular expense ÷ Sales) × 100",
            "Use the same sales figure as GP ratio. Name the expense in the answer: “Employee-cost ratio 6%”, not “expense ratio 6%”.",
        )
        + table(
            ["Expense", "Amount", "Ratio = amount ÷ sales × 100", "What a rise would mean"],
            [
                [
                    "COGS / material",
                    rupee(COGS),
                    _pct(COGS, SALES),
                    "Buying cost up, or selling price down, or wastage / theft of goods",
                ],
                [
                    "Employee benefits",
                    rupee(EMP),
                    _pct(EMP, SALES),
                    "Wage rise, extra hiring, or sales falling faster than the payroll",
                ],
                [
                    "Other operating expenses",
                    rupee(OTHER_OPEX),
                    _pct(OTHER_OPEX, SALES),
                    "Rent, power, selling, depreciation heavier relative to sales",
                ],
                [
                    "Finance costs (interest)",
                    rupee(INTEREST),
                    _pct(INTEREST, SALES),
                    "More debt, or a higher interest rate — a financing problem, not an operating one",
                ],
                [
                    "Tax",
                    rupee(TAX),
                    _pct(TAX, SALES),
                    "Higher taxable profit or a higher rate; usually not “inefficiency”",
                ],
            ],
            caption="Kaveri expense ratios — every paise of the sales-rupee",
            foot="COGS 75 + employee 6 + other opex 4 = 85 (operating ratio). Then interest 3 + tax 3 = 6, and 85 + 6 + NP 9 = 100.",
        )
        + example(
            "K13",
            "Easy",
            "Employee-cost ratio and the 100% check, Kaveri",
            work_table(
                "Employee-cost ratio = Employee benefits ÷ Sales × 100",
                "Employee "
                + rupee(EMP)
                + "; Sales "
                + rupee(SALES),
                "("
                + rupee(EMP)
                + " ÷ "
                + rupee(SALES)
                + ") × 100 = (60,000 ÷ 10,00,000) × 100 = 6%.",
                "6%",
            )
            + p(
                b("Full sales-rupee. ")
                + "COGS 75 + employee 6 + other opex 4 + interest 3 + tax 3 + PAT 9 = 100. "
                "If your expense ratios plus NP ratio do not make 100, a line has been missed or double-counted."
            ),
        )
        + mistakes(
            [
                "Dividing the expense by GP or by PAT instead of by sales.",
                "Calling the interest-to-sales ratio an operating-expense ratio. Interest is a finance cost.",
                "Forgetting that a fall in the ratio can come from sales rising, not from the expense falling. Always look at the rupee amount too.",
            ]
        )
        + memory(
            "Every expense ratio is “this cost / sales × 100”. Name the cost. They are slices of the same sales-rupee; they must add up."
        )
    )


# ---------------------------------------------------------------------------
# 7. Combined ratios
# ---------------------------------------------------------------------------


def _comb_intro() -> str:
    return (
        h2("7. Combined ratios", "comb")
        + lead(
            "One figure from the P&L (a flow over the year) and one figure from the Balance Sheet (a position on a day). "
            "Because a day is not a year, we "
            + b("average")
            + " the opening and closing Balance-Sheet figures whenever the question gives both."
        )
        + p(
            "Two sub-families live here: "
            + b("(A) turnover / activity / efficiency")
            + " — how many times an asset flipped during the year, and how many days a flip takes; "
            + b("(B) return and coverage")
            + " — ROCE, ROE, ROA, EPS, interest coverage. Both are Combined by source."
        )
        + keypoint(
            "When the question does not give an opening figure, use the closing Balance-Sheet figure and write the assumption. "
            "When it does give opening (Kaveri does), you must use the average. Using only closing when opening was given is a named common mistake."
        )
        + formula(
            "Average of a BS item = (Opening + Closing) ÷ 2",
            "Kaveri averages: inventory "
            + rupee(AVG_INV)
            + "; trade receivables "
            + rupee(AVG_TR)
            + "; trade payables "
            + rupee(AVG_CL)
            + ".",
        )
    )


def _comb_ito() -> str:
    return ratio_section(
        heading="7.1 Inventory / stock turnover ratio",
        bucket="Combined ratio — COGS from P&L, average inventory from Balance Sheet. Purpose family: efficiency.",
        ideal="Higher generally means stock is moving. A wholesaler at 7–10 times is healthy; a jeweller at 2 times may also be healthy. Compare with the industry and with the holding period.",
        meaning="Stock turnover is the number of times, during the year, that the firm sold and replaced its average stock. The preferred formula uses cost of goods sold, because stock is valued at cost.",
        simple_txt="Imagine the godown holds "
        + rupee(AVG_INV)
        + " of goods, on average. In the year Kaveri sold goods that cost "
        + rupee(COGS)
        + ". So the godown was emptied and refilled 7.5 times. That is stock turnover.",
        purpose="To judge merchandising efficiency and to spot slow-moving or dead stock. A falling turnover with a rising current ratio often means the “liquidity” is unsold goods.",
        formula_expr="Inventory turnover = COGS ÷ Average inventory",
        formula_note="Preferred MBA version: COGS / average stock. Alternative (used in some papers): Sales / average stock — this mixes selling price with cost and overstates turnover. If the paper prints Sales in the formula, obey the paper and say so. Average inventory = (opening + closing) ÷ 2.",
        components=[
            [
                "COGS",
                "Cost of goods sold, at cost. Matches the valuation of stock.",
                "Kaveri: "
                + rupee(COGS)
                + ".",
            ],
            [
                "Average inventory",
                "Typical stock carried during the year.",
                "("
                + rupee(OP_STOCK)
                + " + "
                + rupee(CL_STOCK)
                + ") ÷ 2 = "
                + rupee(OP_STOCK + CL_STOCK)
                + " ÷ 2 = "
                + rupee(AVG_INV)
                + ".",
            ],
            [
                "Sales (alternative formula)",
                "Revenue from operations. Use only if the question says so.",
                "Kaveri alternative: "
                + rupee(SALES)
                + " ÷ "
                + rupee(AVG_INV)
                + " = "
                + _times(SALES, AVG_INV)
                + " — higher, because sales are at selling price.",
            ],
        ],
        pick="COGS is not purchases. Purchases for Kaveri are "
        + rupee(PURCHASES)
        + "; COGS is "
        + rupee(COGS)
        + ". If GP and sales are given, COGS = sales × (1 − GP%). Opening stock is on last year’s BS or in this year’s P&L working; closing stock is on this year’s BS.",
        steps_list=[
            "Build COGS (opening + purchases − closing, or sales − GP).",
            "Average inventory = (opening + closing) ÷ 2. If opening is missing, use closing and write the assumption.",
            "Divide COGS by average inventory. Unit: times.",
            "Optionally convert to days: 365 ÷ turnover (next ratio).",
        ],
        high="Stock is moving. Less money is locked in the godown. Lower risk of obsolescence.",
        low="Stock is sleeping. Cash is trapped. Possible dead stock, over-buying, or a weak sales season.",
        too_high="The godown is almost empty. Risk of stock-outs and lost sales. The firm may be buying in tiny lots and losing bulk discounts. “Higher” is not always “better” past a point.",
        ex_num="K14",
        work_formula="Inventory turnover = COGS ÷ Average inventory",
        work_pick="COGS "
        + rupee(COGS)
        + "; average inventory ("
        + rupee(OP_STOCK)
        + " + "
        + rupee(CL_STOCK)
        + ") ÷ 2 = "
        + rupee(AVG_INV)
        + ".",
        work_arith=rupee(COGS)
        + " ÷ "
        + rupee(AVG_INV)
        + " = 7,50,000 ÷ 1,00,000 = 7.5.",
        work_answer="7.5 times",
        kaveri_read="The godown flipped 7.5 times in the year — a little over once every two months. For a wholesaler this is a healthy pace. We will convert it to 48.67 days of holding next. The alternative (sales / average stock) would have given 10 times; we do not use it unless asked, because it mixes selling price with cost.",
        mistakes_list=[
            "Using sales instead of COGS when the paper did not ask for that version. This is the most common stock-turnover mistake in the paper.",
            "Using closing stock only when opening was given. Kaveri’s closing is "
            + rupee(CL_STOCK)
            + "; using it alone would give 7,50,000/1,20,000 = 6.25 times — wrong.",
            "Using purchases instead of COGS. Purchases feed the godown; COGS empties it. Turnover is about emptying.",
            "Comparing a COGS-based 7.5 with a rival’s sales-based 10 and concluding the rival is faster. They used different formulas.",
        ],
        mem="Stock lives at cost, so flip it at cost: COGS / average stock. Sales / stock is the second-best formula, used only when COGS cannot be built or the paper prints it.",
    )


def _comb_ihp() -> str:
    return ratio_section(
        heading="7.2 Inventory holding period (stock velocity in days)",
        bucket="Combined ratio (derived from stock turnover). Purpose family: efficiency / working-capital days.",
        ideal="Shorter is generally better, provided there are no stock-outs. Compare with the credit period you get from suppliers (payment period) and with the industry.",
        meaning="Holding period is the number of days, on average, for which goods sit in the godown before they are sold. It is 365 divided by the stock turnover (or 360, 12 months, 52 weeks — whatever the paper uses).",
        simple_txt="If stock turns 7.5 times in 365 days, one turn takes 365 ÷ 7.5 ≈ 49 days. Goods bought today are, on average, sold about seven weeks later.",
        purpose="Managers think in days more easily than in “times”. A holding period of 49 days next to a creditors’ payment period of 60 days means suppliers are financing the stock with 11 days to spare — a sweet working-capital position.",
        formula_expr="Inventory holding period (days) = 365 ÷ Inventory turnover &nbsp;&nbsp;or&nbsp;&nbsp; (Average inventory ÷ COGS) × 365",
        formula_note="Both formulas are the same algebra. If the paper says 360 days, use 360. If it asks for months, use 12 ÷ turnover. If weeks, 52 ÷ turnover.",
        components=[
            [
                "Inventory turnover",
                "COGS ÷ average inventory, already computed.",
                "Kaveri: 7.5 times.",
            ],
            [
                "Days in a year",
                "365 unless the paper says 360.",
                "We take 365. Write that sentence in the answer.",
            ],
        ],
        pick="Use the same turnover you just computed. Do not mix a sales-based turnover with a COGS-based days formula. If the paper asks “stock velocity in months”, do not give days.",
        steps_list=[
            "Compute inventory turnover in times.",
            "Read the required unit (days / weeks / months) and the day’s convention (365 or 360).",
            "Days = 365 ÷ turnover. Show the division.",
            "One sentence: goods sit for X days.",
        ],
        high="Goods sit for a long time. Cash trapped, obsolescence risk, godown cost.",
        low="Goods sit briefly. Fresh stock, less cash trapped.",
        too_high="Dead stock. Too low: empty shelves, lost sales, emergency purchases at poor prices.",
        ex_num="K15",
        work_formula="Holding period (days) = 365 ÷ Inventory turnover",
        work_pick="Turnover 7.5 times; 365 days in a year.",
        work_arith="365 ÷ 7.5. 7.5 = 15/2, so 365 × 2 ÷ 15 = 730 ÷ 15 = 48.666… . In months: 12 ÷ 7.5 = 1.6 months. In weeks: 52 ÷ 7.5 = 6.933… weeks.",
        work_answer="48.67 days &nbsp;(or 1.6 months, or 6.93 weeks)",
        kaveri_read="Stock sits for about 49 days. Combined with a 60-day payment period (computed later), Kaveri sells the goods before it has to pay the supplier. That is a working-capital plus.",
        mistakes_list=[
            "Using 365 ÷ average inventory (forgetting to use turnover, or forgetting × COGS).",
            "Mixing 365 with a 360-based industry benchmark.",
            "Writing “48.67 times” — the unit is days, not times.",
            "Using 365 ÷ Sales-based turnover and comparing with a COGS-based holding period from last year.",
        ],
        mem="Times go into the year: 365 / turnover = days in one turn. Months: 12 / turnover. Weeks: 52 / turnover. Same idea.",
    )


def _comb_dto() -> str:
    return ratio_section(
        heading="7.3 Debtors / receivables turnover ratio",
        bucket="Combined ratio — credit sales from P&L, average debtors from Balance Sheet. Purpose family: efficiency / credit control.",
        ideal="Higher means faster collection. A turnover of 10 times ≈ a 36.5-day collection period, which is tight and healthy for a wholesaler who might offer 30–45 days of credit.",
        meaning="Debtors turnover is the number of times, during the year, that average trade receivables were converted into cash. It is credit sales divided by average trade receivables.",
        simple_txt="Kaveri sold "
        + rupee(CREDIT_SALES)
        + " on credit and was owed, on average, "
        + rupee(AVG_TR)
        + ". So the debtors’ book was collected and refilled 10 times in the year.",
        purpose="To judge collection efficiency and the quality of debtors. A falling turnover means customers are taking longer to pay — a liquidity leak and a bad-debt risk.",
        formula_expr="Debtors turnover = Credit sales ÷ Average trade receivables",
        formula_note="Credit sales = total sales − cash sales. If the cash/credit split is not given, assume all sales are on credit and write the assumption. Average receivables = (opening + closing) ÷ 2. Use net receivables (after provision for doubtful debts) if a provision is given.",
        components=[
            [
                "Credit sales",
                "Sales made on credit, after returns. Cash sales do not create debtors, so they do not belong here.",
                "Kaveri: 80% of "
                + rupee(SALES)
                + " = "
                + rupee(CREDIT_SALES)
                + ". Cash sales "
                + rupee(CASH_SALES)
                + " stay out.",
            ],
            [
                "Average trade receivables",
                "Typical amount customers owed during the year. Include bills receivable if the paper lists them with debtors.",
                "("
                + rupee(OP_TR)
                + " + "
                + rupee(TR)
                + ") ÷ 2 = "
                + rupee(OP_TR + TR)
                + " ÷ 2 = "
                + rupee(AVG_TR)
                + ".",
            ],
        ],
        pick="If the question says “sales” and is silent on cash sales, write “assumed all credit”. Kaveri is not silent: 20% cash is given, so you must use 80%. Opening debtors, if given, must be averaged with closing. Closing debtors live on the BS as trade receivables.",
        steps_list=[
            "Compute credit sales. Subtract cash sales if given.",
            "Average debtors = (opening + closing) ÷ 2.",
            "Divide. Unit: times.",
            "Convert to days if asked (next ratio).",
        ],
        high="Customers pay fast. Cash comes in. Less bad-debt risk. Credit control is tight.",
        low="Customers delay. Cash is stuck in receivables. Possible weak credit checks, disputes, or a recession in the customer’s industry.",
        too_high="Credit policy may be so strict that sales are being refused. A turnover of 50 times (collection in a week) in a trade where 45 days is custom will lose customers to a rival who offers credit. High can be a marketing problem.",
        ex_num="K16",
        work_formula="Debtors turnover = Credit sales ÷ Average trade receivables",
        work_pick="Credit sales "
        + rupee(CREDIT_SALES)
        + "; average receivables "
        + rupee(AVG_TR)
        + ".",
        work_arith=rupee(CREDIT_SALES)
        + " ÷ "
        + rupee(AVG_TR)
        + " = 8,00,000 ÷ 80,000 = 10.",
        work_answer="10 times",
        kaveri_read="The debtors’ book flipped 10 times. Collection is brisk. If a student wrongly uses total sales "
        + rupee(SALES)
        + " ÷ "
        + rupee(AVG_TR)
        + " = 12.5 times, they have pretended that cash customers were also debtors. That is the classic mistake on this ratio.",
        mistakes_list=[
            "Using total sales when cash sales are given. Kaveri would then show 12.5 instead of 10.",
            "Using closing debtors only when opening was given: 8,00,000/1,00,000 = 8 times — wrong.",
            "Including cash-sales customers in “debtors”. They never were debtors.",
            "Forgetting to net off provision for doubtful debts when a provision is given.",
        ],
        mem="Only credit sales create debtors. Credit sales / average debtors. If the split is silent, assume all sales are credit and write that down.",
    )


def _comb_acp() -> str:
    return ratio_section(
        heading="7.4 Average collection period (debtors’ velocity in days)",
        bucket="Combined ratio (derived from debtors turnover). Purpose family: efficiency / liquidity of receivables.",
        ideal="Should sit at or inside the credit period the firm offers. If Kaveri offers 45 days and collects in 36.5, credit control is working. If it offers 30 days and collects in 70, it is not.",
        meaning="Average collection period is the number of days, on average, that a credit customer takes to pay. It is 365 divided by debtors turnover (or 360, as the paper says).",
        simple_txt="Turnover 10 times in 365 days means one collection-cycle is 36.5 days. A bill raised today is, on average, cash in a little over a month.",
        purpose="To compare with the stated credit period, with last year, and with the creditors’ payment period. Collection slower than payment is a cash-cycle hole.",
        formula_expr="Average collection period (days) = 365 ÷ Debtors turnover &nbsp;&nbsp;or&nbsp;&nbsp; (Average debtors ÷ Credit sales) × 365",
        formula_note="Same algebra. Months = 12 ÷ turnover. Weeks = 52 ÷ turnover.",
        components=[
            [
                "Debtors turnover",
                "Credit sales ÷ average debtors.",
                "Kaveri: 10 times.",
            ],
            [
                "Credit sales / average debtors",
                "Same figures as the turnover ratio.",
                rupee(CREDIT_SALES)
                + " and "
                + rupee(AVG_TR)
                + ".",
            ],
        ],
        pick="Use credit sales, not total sales, unless you assumed all sales are credit. Use the same 365/360 convention as for stock days, unless the paper mixes them (rare).",
        steps_list=[
            "Compute debtors turnover.",
            "Days = 365 ÷ turnover. Show 365 ÷ 10 = 36.5.",
            "Compare with the credit period allowed, if given.",
            "Write the unit: days.",
        ],
        high="Customers take long to pay. Cash delayed. Bad-debt risk up. Possible need to tighten credit or offer a cash discount.",
        low="Customers pay promptly. Cash is in. Credit policy is strict or the trade is cash-heavy.",
        too_high="A 90-day collection in a 30-day trade is a red flag — possible window-dressed sales (bills raised to friends who will never pay). Too low: refusing credit and losing volume.",
        ex_num="K17",
        work_formula="Collection period = 365 ÷ Debtors turnover",
        work_pick="Turnover 10 times; 365 days.",
        work_arith="365 ÷ 10 = 36.5. Alternative: ("
        + rupee(AVG_TR)
        + " ÷ "
        + rupee(CREDIT_SALES)
        + ") × 365 = (80,000 ÷ 8,00,000) × 365 = 0.10 × 365 = 36.5.",
        work_answer="36.5 days",
        kaveri_read="A credit customer pays in about 37 days. That is prompt. Set next to a 60-day payment period, Kaveri collects 23 days before it pays — a cash-cycle advantage.",
        mistakes_list=[
            "365 ÷ closing debtors, skipping the turnover step, and skipping credit sales.",
            "Using 365 ÷ total sales / debtors when cash sales exist.",
            "Writing 36.5 times. Unit is days.",
        ],
        mem="Days to collect = 365 / how many times debtors flipped. Same pattern as stock days.",
    )


def _comb_cto() -> str:
    return ratio_section(
        heading="7.5 Creditors / payables turnover ratio",
        bucket="Combined ratio — credit purchases from P&L working, average creditors from Balance Sheet. Purpose family: efficiency / trade-credit use.",
        ideal="There is no “higher is better”. A higher turnover means you pay faster (you use less free credit). A lower turnover means you pay slower (you use more free credit, but you may anger suppliers). Match it to the credit period allowed by suppliers.",
        meaning="Creditors turnover is the number of times, during the year, that average trade payables were paid off. It is credit purchases divided by average trade payables.",
        simple_txt="Kaveri bought "
        + rupee(PURCHASES)
        + " of goods, all on credit, and owed suppliers, on average, "
        + rupee(AVG_CL)
        + ". So the creditors’ book was paid and refilled about 6.08 times.",
        purpose="To see how the firm uses supplier credit — a free source of working capital — and whether it is stretching payables dangerously.",
        formula_expr="Creditors turnover = Credit purchases ÷ Average trade payables",
        formula_note="Credit purchases = total purchases − cash purchases. If the split is silent, assume all purchases are on credit. Purchases = COGS + closing stock − opening stock. Average payables = (opening + closing) ÷ 2.",
        components=[
            [
                "Credit purchases",
                "Goods bought on credit. Not COGS. Not sales.",
                "Kaveri: all purchases are credit = "
                + rupee(PURCHASES)
                + ". Working: COGS "
                + rupee(COGS)
                + " + closing "
                + rupee(CL_STOCK)
                + " − opening "
                + rupee(OP_STOCK)
                + " = "
                + rupee(PURCHASES)
                + ".",
            ],
            [
                "Average trade payables",
                "Typical amount owed to suppliers of goods. Include bills payable if grouped with creditors.",
                "("
                + rupee(OP_CL)
                + " + "
                + rupee(CL_)
                + ") ÷ 2 = "
                + rupee(OP_CL + CL_)
                + " ÷ 2 = "
                + rupee(AVG_CL)
                + ".",
            ],
        ],
        pick="Rebuild purchases from COGS and stock if purchases are not printed. Do not use COGS as the numerator (COGS is for stock turnover). Do not use sales. If opening creditors are given, average them.",
        steps_list=[
            "Build credit purchases. Purchases = COGS + closing stock − opening stock.",
            "Average creditors = (opening + closing) ÷ 2.",
            "Divide. Unit: times.",
            "Convert to days if asked.",
        ],
        high="You pay suppliers often / quickly. You may be missing free credit. Liquidity is used up faster.",
        low="You pay slowly. Free credit is being used. Cash is conserved — until a supplier stops supplying.",
        too_high="Paying cash-on-delivery when 45 days are on offer is a gift to the supplier, not a virtue, if your own cash is tight. Too low: suppliers may refuse credit, charge a premium, or take legal action. “Lower” is not a prize past the allowed credit period.",
        ex_num="K18",
        work_formula="Creditors turnover = Credit purchases ÷ Average trade payables",
        work_pick="Credit purchases "
        + rupee(PURCHASES)
        + "; average payables "
        + rupee(AVG_CL)
        + ".",
        work_arith=rupee(PURCHASES)
        + " ÷ "
        + rupee(AVG_CL)
        + " = 7,90,000 ÷ 1,30,000 = 79/13 = 6.0769…",
        work_answer="6.08 times &nbsp;(2 d.p.; exact 79/13)",
        kaveri_read="Suppliers are paid a little over 6 times a year. That will become about 60 days in the next ratio — two months of free credit, which is common in wholesale trade and longer than the 36.5 days Kaveri takes to collect. The cash cycle is in Kaveri’s favour.",
        mistakes_list=[
            "Using COGS instead of purchases. For Kaveri that would be 7,50,000/1,30,000 = 5.77 times — wrong. Purchases and COGS differ by the stock increase of "
            + rupee(CL_STOCK - OP_STOCK)
            + ".",
            "Using sales in the numerator.",
            "Using closing creditors only when opening was given: 7,90,000/1,50,000 = 5.27 times — wrong.",
            "Treating a loan creditor or outstanding wages as trade payables. This ratio is about suppliers of goods.",
        ],
        mem="Creditors come from purchases, not from sales, not from COGS. Credit purchases / average creditors. Rebuild purchases from COGS ± stock if needed.",
    )


def _comb_app() -> str:
    return ratio_section(
        heading="7.6 Average payment period (creditors’ velocity in days)",
        bucket="Combined ratio (derived from creditors turnover). Purpose family: efficiency / working-capital days.",
        ideal="Sit at the credit period the supplier allows. Paying 5 days early loses free cash; paying 40 days late costs reputation and future credit.",
        meaning="Average payment period is the number of days, on average, that the firm takes to pay its suppliers. It is 365 divided by creditors turnover.",
        simple_txt="If creditors turn 6.08 times in 365 days, one payment-cycle is about 60 days. A purchase billed today is paid in about two months.",
        purpose="To complete the operating-cycle story: holding days + collection days − payment days = net cash cycle. Also to check that the firm is not funding itself by starving suppliers.",
        formula_expr="Average payment period (days) = 365 ÷ Creditors turnover &nbsp;&nbsp;or&nbsp;&nbsp; (Average creditors ÷ Credit purchases) × 365",
        formula_note="Months = 12 ÷ turnover. Use 360 if the paper says so.",
        components=[
            [
                "Creditors turnover",
                "Credit purchases ÷ average creditors.",
                "Kaveri: 6.0769… times.",
            ],
            [
                "Credit purchases / average creditors",
                "Same figures as the turnover.",
                rupee(PURCHASES)
                + " and "
                + rupee(AVG_CL)
                + ".",
            ],
        ],
        pick="Use credit purchases, not COGS, not sales. Same 365/360 convention as the other day-ratios unless told otherwise.",
        steps_list=[
            "Compute creditors turnover.",
            "Days = 365 ÷ turnover. Show the long division.",
            "Compare with the credit period allowed by suppliers, if given.",
            "Place it next to collection period: collecting faster than paying is a cash plus.",
        ],
        high="The firm takes long to pay. Free credit, but strained suppliers.",
        low="The firm pays promptly. Good relations, less free credit.",
        too_high="A 120-day payment in a 45-day trade is a distress signal (or a bullying of small suppliers). Too low: paying at the counter when 60 days are free, while the firm itself borrows at 12% — a treasury mistake.",
        ex_num="K19",
        work_formula="Payment period = 365 ÷ Creditors turnover",
        work_pick="Turnover = 7,90,000 ÷ 1,30,000 = 79/13. 365 days.",
        work_arith="365 ÷ (79/13) = 365 × 13 ÷ 79 = 4,745 ÷ 79. 79 × 60 = 4,740, remainder 5, so 60 + 5/79 = 60.06 days.",
        work_answer="60.06 days &nbsp;(≈ 60 days)",
        kaveri_read="Suppliers are paid in about 60 days. Customers pay in 36.5 days. Stock sits 48.67 days. A rough cash-cycle check: 48.67 + 36.5 − 60.06 ≈ 25 days of net operating cycle — Kaveri needs about 25 days of its own working capital to run the trade, the rest is funded by suppliers. Comfortable.",
        mistakes_list=[
            "365 ÷ COGS / creditors, mixing stock formula with creditors.",
            "Using 365 ÷ purchases without averaging creditors when opening was given.",
            "Calling a longer payment period “more efficient”. It is cheaper cash, not more efficient operations, and it has a relationship cost.",
        ],
        mem="Days to pay = 365 / creditors turnover. Put it next to days to collect. Collect before you pay, and you sleep.",
        extra=formula(
            "Net operating / cash cycle (days) ≈ Holding period + Collection period − Payment period",
            "Kaveri: 48.67 + 36.50 − 60.06 = 25.11 days. A short cycle is a liquidity blessing. A negative cycle (paying after collecting-plus-holding) means suppliers finance the whole trade.",
        ),
    )


def _comb_wct() -> str:
    return ratio_section(
        heading="7.7 Working capital turnover ratio",
        bucket="Combined ratio — sales from P&L, working capital from Balance Sheet. Purpose family: efficiency.",
        ideal="Higher generally means each rupee of working capital is supporting more sales. Too high can mean WC is inadequate for the volume (overtrading).",
        meaning="Working capital turnover is sales divided by working capital (current assets minus current liabilities). It asks: how many rupees of sales does each rupee of net current assets support?",
        simple_txt="Kaveri has "
        + rupee(WC)
        + " of working capital and sells "
        + rupee(SALES)
        + ". Each rupee of WC supports ₹6.67 of sales.",
        purpose="To judge whether the firm is using its net current assets hard enough, and to spot overtrading (sales far too large for the WC, so a small delay in collection can freeze the firm).",
        formula_expr="Working capital turnover = Sales ÷ Working capital &nbsp;&nbsp;where Working capital = CA − CL",
        formula_note="Some papers use average working capital if a previous BS is fully given. Kaveri has only this year’s CA and CL (openings of stock, debtors, creditors are given, but not a full opening BS), so we use closing WC and state that.",
        components=[
            [
                "Sales",
                "Revenue from operations.",
                "Kaveri: "
                + rupee(SALES)
                + ".",
            ],
            [
                "Working capital",
                "Current assets − current liabilities. The net current cushion.",
                rupee(CA)
                + " − "
                + rupee(CL_)
                + " = "
                + rupee(WC)
                + ".",
            ],
        ],
        pick="WC is not current assets. It is CA minus CL. If CA = CL, WC is zero and this ratio is undefined — write that, do not divide by zero. If CL > CA, WC is negative and the ratio is not meaningful as a turnover; say “negative working capital”.",
        steps_list=[
            "CA − CL = working capital.",
            "Confirm it is positive.",
            "Sales ÷ WC. Unit: times.",
            "Comment on overtrading if the number is very high next to a thin current ratio.",
        ],
        high="Each WC-rupee is working hard. Good use of funds — unless it is overtrading.",
        low="A lot of WC is supporting little sales. Idle stock or idle cash, or a collapsed top line.",
        too_high="Overtrading: sales have outgrown the cushion. A slow month of collections and the firm cannot pay wages. Too low: capital stuck in WC, ROCE suffers.",
        ex_num="K20",
        work_formula="WC turnover = Sales ÷ (CA − CL)",
        work_pick="Sales "
        + rupee(SALES)
        + "; WC "
        + rupee(CA)
        + " − "
        + rupee(CL_)
        + " = "
        + rupee(WC)
        + ".",
        work_arith=rupee(SALES)
        + " ÷ "
        + rupee(WC)
        + " = 10,00,000 ÷ 1,50,000 = 100/15 = 20/3 = 6.666…",
        work_answer="6.67 times",
        kaveri_read="Each rupee of working capital supports ₹6.67 of sales. Paired with a current ratio of 2 : 1, this is use, not overtrading. Overtrading would look like WC turnover of 20 times next to a current ratio of 1.1.",
        mistakes_list=[
            "Dividing by current assets instead of working capital.",
            "Using COGS in the numerator. This ratio uses sales.",
            "Taking WC as CA + CL. It is CA − CL.",
        ],
        mem="Sales over the cushion. WC = CA − CL. High = hard-working cushion; extremely high = overtrading.",
    )


def _comb_fat() -> str:
    return ratio_section(
        heading="7.8 Fixed asset turnover ratio",
        bucket="Combined ratio — sales from P&L, net fixed assets from Balance Sheet. Purpose family: efficiency of long-term assets.",
        ideal="Higher means the factory/godown is generating more sales per rupee of FA. A trader (low FA) will show a higher number than a manufacturer (heavy FA). Compare within the industry.",
        meaning="Fixed asset turnover is sales divided by net fixed assets. It asks: how many rupees of sales does each rupee invested in the godown, plant and office generate?",
        simple_txt="Kaveri’s godown and office (net) cost "
        + rupee(FA)
        + " and produced "
        + rupee(SALES)
        + " of sales. About ₹1.54 of sales per rupee of net FA.",
        purpose="To judge capacity utilisation and the productivity of long-term assets. A falling FA turnover can mean idle capacity, or a newly bought asset that has not yet started selling (which is not a crime — mention it).",
        formula_expr="Fixed asset turnover = Sales ÷ Net fixed assets",
        formula_note="Use net FA (after depreciation). Some papers use gross FA; some use average net FA. Default: closing net FA. State it.",
        components=[
            [
                "Sales",
                "Revenue from operations.",
                "Kaveri: "
                + rupee(SALES)
                + ".",
            ],
            [
                "Net fixed assets",
                "PPE after accumulated depreciation. Exclude current assets and investments unless the paper says “capital assets” more broadly.",
                "Kaveri: "
                + rupee(FA)
                + ".",
            ],
        ],
        pick="Net, not gross, unless only gross is given. Do not add current assets (that would be total-asset turnover, which is ROA’s cousin).",
        steps_list=[
            "Pick net FA from the BS.",
            "Pick sales from the P&L.",
            "Divide. Unit: times.",
            "Read with the nature of the business (trader vs factory).",
        ],
        high="Assets are working hard. Good utilisation.",
        low="Idle capacity, over-investment, or a newly commissioned plant.",
        too_high="The firm may be sweating old, fully-depreciated assets (net FA is small because of accumulated depreciation, so the ratio looks brilliant). Check gross FA and the age of assets. Too low: money locked in a building that does not sell.",
        ex_num="K21",
        work_formula="FA turnover = Sales ÷ Net FA",
        work_pick="Sales "
        + rupee(SALES)
        + "; Net FA "
        + rupee(FA)
        + ".",
        work_arith=rupee(SALES)
        + " ÷ "
        + rupee(FA)
        + " = 10,00,000 ÷ 6,50,000 = 100/65 = 20/13 = 1.53846…",
        work_answer="1.54 times",
        kaveri_read="Each rupee of net FA produces ₹1.54 of sales. For a trader who owns a godown, this is modest (the godown is a large slice of the BS). It is not comparable with a stall-trader who rents and shows FA turnover of 20 times — different asset strategy.",
        mistakes_list=[
            "Using gross FA when net is given. Net is smaller, so using gross understates turnover.",
            "Adding working capital to FA (that is capital turnover).",
            "Using PAT in the numerator (that is a return, not a turnover).",
        ],
        mem="Sales over the godown. Net FA, not gross. High looks good; with fully-depreciated assets it can be an illusion.",
    )


def _comb_capt() -> str:
    return ratio_section(
        heading="7.9 Capital turnover ratio",
        bucket="Combined ratio — sales from P&L, capital employed from Balance Sheet. Purpose family: efficiency of long-term funds.",
        ideal="Higher means each rupee of long-term funds supports more sales. Pair it with operating profit ratio: ROCE ≈ operating profit% × capital turnover.",
        meaning="Capital turnover is sales divided by capital employed. It asks: how many rupees of sales does each rupee of long-term funds generate?",
        simple_txt="Kaveri has "
        + rupee(CE)
        + " of capital employed (owners + long-term lenders) and sells "
        + rupee(SALES)
        + ". Each long-term rupee supports ₹1.25 of sales.",
        purpose="To judge the activity of the total long-term pool. It is one of the two engines of ROCE (the other is operating profit margin). A firm can have a modest margin and a high capital turnover (a grocer) or a fat margin and a low capital turnover (a jeweller) and the same ROCE.",
        formula_expr="Capital turnover = Sales ÷ Capital employed",
        formula_note="Capital employed = Shareholders’ funds + Long-term debt = Net FA + Working capital. Use the same CE you will use for ROCE.",
        components=[
            [
                "Sales",
                "Revenue from operations.",
                "Kaveri: "
                + rupee(SALES)
                + ".",
            ],
            [
                "Capital employed",
                "Long-term funds in the business.",
                "Method 1: "
                + rupee(SF)
                + " + "
                + rupee(LTD)
                + " = "
                + rupee(CE)
                + ". Method 2: "
                + rupee(FA)
                + " + "
                + rupee(WC)
                + " = "
                + rupee(CE)
                + ".",
            ],
        ],
        pick="Do not use only share capital. Do not use total assets (that includes assets financed by current liabilities). CE is the long-term pool.",
        steps_list=[
            "Compute capital employed two ways and confirm they match.",
            "Sales ÷ CE. Unit: times.",
            "Keep the CE figure — you need it for ROCE in a moment.",
        ],
        high="Long-term funds are supporting a large top line. An activity-driven business.",
        low="Heavy capital for the sales achieved. Possible idle FA or idle WC.",
        too_high="Overtrading at the capital level: sales too big for the long-term funds, so the firm is leaning on current liabilities. Too low: over-capitalised, ROCE will sag.",
        ex_num="K22",
        work_formula="Capital turnover = Sales ÷ Capital employed",
        work_pick="Sales "
        + rupee(SALES)
        + "; CE "
        + rupee(CE)
        + ".",
        work_arith=rupee(SALES)
        + " ÷ "
        + rupee(CE)
        + " = 10,00,000 ÷ 8,00,000 = 10/8 = 1.25.",
        work_answer="1.25 times",
        kaveri_read="Each rupee of long-term funds supports ₹1.25 of sales. Combined with a 15% operating margin, ROCE should be 15% × 1.25 = 18.75%. We will confirm that identity in the ROCE section — it is a free arithmetic check.",
        mistakes_list=[
            "Denominator = equity share capital only.",
            "Denominator = total assets. That is total-asset turnover = "
            + _times(SALES, TA)
            + " for Kaveri, a different ratio.",
            "Mixing one CE definition for this ratio and another for ROCE in the same answer.",
        ],
        mem="Sales over the long-term pool. Capital turnover × operating profit% = ROCE. Use it as a check.",
    )


def _comb_roce() -> str:
    return ratio_section(
        heading="7.10 Return on capital employed (ROCE)",
        bucket="Combined ratio — EBIT from P&L, capital employed from Balance Sheet. Purpose family: profitability of long-term funds.",
        ideal="Should beat the cost of capital. As a rule of thumb, comfortably above the interest rate on the firm’s debt (Kaveri’s interest is "
        + rupee(INTEREST)
        + " on "
        + rupee(LTD)
        + " = 15% pre-tax coupon; ROCE of 18.75% clears it). Compare with industry and with last year.",
        meaning="ROCE is operating profit (EBIT) divided by capital employed, times 100. It is the return earned on every rupee of long-term funds, before the split between lenders (interest) and owners (the residual), and before tax.",
        simple_txt="The business, as a machine, was given "
        + rupee(CE)
        + " of long-term money and produced "
        + rupee(EBIT)
        + " of operating profit. That is an 18.75% return on the machine, before the banker and the tax officer take their cuts.",
        purpose="To judge the overall earning power of the firm’s long-term resources. It is the fairest profitability ratio for comparing two firms with different debt levels, because EBIT is before interest. Banks and boards quote it constantly.",
        formula_expr="ROCE = (EBIT ÷ Capital employed) × 100",
        formula_note="EBIT = PBIT = operating profit. Capital employed = SF + LTD = FA + WC. Some papers use PBT (after interest) — that is not ROCE, that is closer to a return on total long-term funds after debt cost; do not mix. Some use average CE; default here is closing CE.",
        components=[
            [
                "EBIT / operating profit",
                "Profit before interest and tax. The pool that belongs to both lenders and owners.",
                "Kaveri: "
                + rupee(EBIT)
                + ". Rebuild: PBT "
                + rupee(PBT)
                + " + interest "
                + rupee(INTEREST)
                + ".",
            ],
            [
                "Capital employed",
                "Shareholders’ funds + long-term debt. Equals net FA + working capital.",
                "Kaveri: "
                + rupee(CE)
                + " (both methods).",
            ],
        ],
        pick="Numerator is EBIT, not PAT, not PBT. PAT is for ROE. PBT has already paid the lenders, so it understates the return on the whole pool. Denominator includes debt — so the numerator must include the profit that debt helped to earn, i.e. before interest.",
        steps_list=[
            "Build EBIT (PBT + interest, or GP − opex).",
            "Build capital employed two ways; they must match.",
            "ROCE = EBIT ÷ CE × 100. Unit: %.",
            "Check: operating profit% × capital turnover should equal ROCE.",
        ],
        high="The long-term funds are earning well. Value is being created if ROCE exceeds the cost of those funds.",
        low="Funds are earning poorly. Either margins are thin, or capital is idle (low turnover), or both. DuPont (next sections) tells you which.",
        too_high="A spectacular ROCE can be a fully-depreciated plant (tiny CE) or a one-time operating windfall. Or it can be genuine. Check both years and the notes. Too low: the firm is destroying value if it is below what those funds could earn elsewhere.",
        ex_num="K23",
        work_formula="ROCE = (EBIT ÷ Capital employed) × 100",
        work_pick="EBIT "
        + rupee(EBIT)
        + "; CE "
        + rupee(CE)
        + ".",
        work_arith="("
        + rupee(EBIT)
        + " ÷ "
        + rupee(CE)
        + ") × 100 = (1,50,000 ÷ 8,00,000) × 100 = 0.1875 × 100 = 18.75%.",
        work_answer="18.75%",
        kaveri_read="Long-term funds earned 18.75% before interest and tax. Check: operating profit ratio 15% × capital turnover 1.25 = 18.75%. The two engines agree. The 18.75% is above the 15% coupon on the term loan (30,000/2,00,000), so the debt is earning its keep and leaving a surplus for owners.",
        mistakes_list=[
            "Using PAT in the numerator. That understates ROCE and confuses it with ROE. For Kaveri, PAT/CE = 90,000/8,00,000 = 11.25% — a different, unnamed number.",
            "Using only share capital as CE.",
            "Using total assets as CE (that is closer to ROA’s denominator).",
            "Using PBT (after interest) with a CE that still includes debt — the numerator and denominator then do not match.",
        ],
        mem="ROCE = return on the whole long-term pool = EBIT / CE × 100. EBIT, not PAT. CE includes debt, so the profit must be before interest. Check: OP% × capital turnover.",
        extra=keypoint(
            "Matching rule, write it once and it will save you in every paper: "
            "if the denominator includes a fund-provider, the numerator must be the profit before that provider has been paid. "
            "CE includes lenders → use EBIT. Equity includes only owners → use PAT (ROE). "
            "Break the matching rule and the ratio is meaningless."
        ),
    )


def _comb_roe() -> str:
    return ratio_section(
        heading="7.11 Return on equity (ROE / return on shareholders’ funds)",
        bucket="Combined ratio — PAT from P&L, equity shareholders’ funds from Balance Sheet. Purpose family: profitability for owners.",
        ideal="Higher is better for owners, provided it is not bought with reckless gearing. Compare with ROCE, with the interest rate, and with what owners could earn elsewhere. Kaveri’s 15% is a solid owners’ return for a trading company.",
        meaning="ROE is profit after tax (and after preference dividend, if any) divided by equity shareholders’ funds, times 100. It is the return on the owners’ own rupee.",
        simple_txt="Owners have left "
        + rupee(SF)
        + " in Kaveri. This year they earned "
        + rupee(PAT)
        + " after tax. That is 15 paise in the rupee, or 15%.",
        purpose="This is the owners’ scoreboard. It is what a shareholder compares with a bank-deposit rate, a mutual fund, or another company’s ROE. It is also the top of the DuPont identity.",
        formula_expr="ROE = (PAT ÷ Equity shareholders’ funds) × 100",
        formula_note="If preference dividend exists: numerator = PAT − preference dividend, denominator = equity funds (exclude preference capital). Kaveri has no preference. Do not use EBIT here — EBIT belongs to lenders as well.",
        components=[
            [
                "PAT (less preference dividend if any)",
                "Profit for equity owners after interest, tax and preference dividend.",
                "Kaveri: "
                + rupee(PAT)
                + ", no preference dividend.",
            ],
            [
                "Equity shareholders’ funds",
                "Equity share capital + reserves − fictitious assets. Exclude preference capital.",
                "Kaveri: "
                + rupee(ESC)
                + " + "
                + rupee(RES)
                + " = "
                + rupee(SF)
                + ".",
            ],
        ],
        pick="Denominator is not “equity share capital” alone. Reserves belong to owners. Numerator is PAT, not EBIT, not PBT (unless the paper says pre-tax ROE). If a P&L debit balance (loss) sits on the asset side, net it off equity.",
        steps_list=[
            "PAT, minus preference dividend if given.",
            "Equity funds = equity share capital + reserves − fictitious assets.",
            "Divide × 100. Unit: %.",
            "Compare with ROCE: if ROE > ROCE after tax, gearing is helping owners; if ROE < after-tax ROCE, gearing is hurting.",
        ],
        high="Owners are earning well on their money. The share is more attractive, other things equal.",
        low="Owners are earning poorly. Either the business is weak (low ROCE) or debt is eating the residual (high interest) or equity is bloated.",
        too_high="A 60% ROE with a debt-equity of 5 : 1 is a tightrope, not a triumph. A 60% ROE with tiny equity because of accumulated losses that just reversed can also mislead. Too low: owners would have been better off in a fixed deposit — a harsh but fair comment if it persists.",
        ex_num="K24",
        work_formula="ROE = (PAT ÷ Equity shareholders’ funds) × 100",
        work_pick="PAT "
        + rupee(PAT)
        + "; Equity funds "
        + rupee(SF)
        + ".",
        work_arith="("
        + rupee(PAT)
        + " ÷ "
        + rupee(SF)
        + ") × 100 = (90,000 ÷ 6,00,000) × 100 = 0.15 × 100 = 15%.",
        work_answer="15%",
        kaveri_read="Owners earned 15% after tax. ROCE was 18.75% before interest and tax. After paying 15% coupon on a small loan and 25% tax on PBT, 15% remains for owners — a fair translation, not a magic trick. Gearing is mild, so ROE is not being inflated by a mountain of debt.",
        mistakes_list=[
            "Denominator = equity share capital "
            + rupee(ESC)
            + " only, giving 90,000/4,00,000 = 22.5%. That ignores "
            + rupee(RES)
            + " of reserves which are also owners’ money. This is the most common ROE mistake in the paper.",
            "Numerator = EBIT. That is ROCE’s numerator. Matching rule broken.",
            "Including preference capital in the denominator while also not deducting preference dividend.",
        ],
        mem="ROE = owners’ leftover over owners’ money = PAT / (share capital + reserves) × 100. Never skip reserves. Never use EBIT.",
    )


def _comb_roa() -> str:
    return ratio_section(
        heading="7.12 Return on assets (ROA / return on total assets)",
        bucket="Combined ratio — profit from P&L, total assets from Balance Sheet. Purpose family: profitability of the whole asset base.",
        ideal="Higher is better. It will usually sit below ROCE because total assets (9.5 lakh) are bigger than capital employed (8 lakh) — current liabilities finance part of the assets.",
        meaning="Return on assets is profit divided by total assets, times 100. Two versions: (A) PAT / total assets — common “bottom-line” version; (B) EBIT / total assets — “operating” version, comparable across different debt levels. These notes compute both and lead with PAT.",
        simple_txt="Every rupee of asset — godown, stock, debtors, cash — earned how many paise of profit? For Kaveri, PAT version: 9.47 paise. EBIT version: 15.79 paise.",
        purpose="To judge how productively the whole asset base is used, including the slice financed by creditors. Useful for comparing firms with very different current-liability levels.",
        formula_expr="ROA = (PAT ÷ Total assets) × 100 &nbsp;&nbsp;(lead version); also (EBIT ÷ Total assets) × 100",
        formula_note="Total assets = Balance Sheet total. If fictitious assets exist, use tangible total assets. Average total assets if both years’ BS are given; Kaveri uses closing, stated.",
        components=[
            [
                "PAT (version A)",
                "Bottom-line profit.",
                "Kaveri: "
                + rupee(PAT)
                + ".",
            ],
            [
                "EBIT (version B)",
                "Operating profit, for a debt-neutral view.",
                "Kaveri: "
                + rupee(EBIT)
                + ".",
            ],
            [
                "Total assets",
                "FA + CA = BS total.",
                "Kaveri: "
                + rupee(TA)
                + ".",
            ],
        ],
        pick="Denominator is the BS total, not CE, not FA. Write which numerator you used. In a “compute ROA” question with no formula printed, PAT / TA is the safe MBA default; mention the EBIT version if marks are generous.",
        steps_list=[
            "Pick PAT (and EBIT if you want both).",
            "Pick total assets = BS total.",
            "Divide × 100.",
            "Place it next to ROCE and ROE: ROA < ROCE typically, because CL assets sit in the ROA denominator.",
        ],
        high="Assets are earning well, including those financed by creditors.",
        low="A large asset base is producing little profit. Idle FA, slow stock, or thin margins.",
        too_high="Can be a fully-depreciated asset base (same illusion as FA turnover). Too low: the firm is too fat in assets for its profit.",
        ex_num="K25",
        work_formula="ROA = (PAT ÷ Total assets) × 100",
        work_pick="PAT "
        + rupee(PAT)
        + "; Total assets "
        + rupee(TA)
        + ". Also EBIT "
        + rupee(EBIT)
        + ".",
        work_arith="PAT version: (90,000 ÷ 9,50,000) × 100 = 9.4736…%. EBIT version: (1,50,000 ÷ 9,50,000) × 100 = 15.789…%.",
        work_answer="9.47% (PAT) &nbsp;; 15.79% (EBIT version)",
        kaveri_read="The whole asset base earned 9.47% after tax. ROCE was 18.75% on a smaller, long-term, denominator. The gap is mostly the extra "
        + rupee(CL_)
        + " of assets that creditors financed, plus the fact that PAT is after interest and tax while EBIT is not. Both numbers can live in the same answer as long as you label them.",
        mistakes_list=[
            "Using capital employed as the denominator and calling it ROA.",
            "Using net FA only.",
            "Mixing PAT in the numerator with a comment that “this is before interest”.",
        ],
        mem="ROA = profit / whole pie of assets. PAT/TA is the default. EBIT/TA is the operating cousin. TA is the BS total.",
    )


def _comb_eps() -> str:
    return ratio_section(
        heading="7.13 Earnings per share (EPS)",
        bucket="Combined ratio — PAT from P&L, number of equity shares from the Balance Sheet / notes. Purpose family: profitability per owner-unit.",
        ideal="Higher is better, but EPS cannot be compared across companies with different face values or different retained-earnings histories without care. Compare with the same company’s previous EPS, and with the market price (P/E, which is not in this syllabus).",
        meaning="EPS is the profit after tax (minus preference dividend) that belongs to one equity share. It is PAT available to equity holders divided by the number of equity shares outstanding.",
        simple_txt="Kaveri has 40,000 equity shares and earned "
        + rupee(PAT)
        + ". Each share earned ₹2.25 this year. That ₹2.25 is not a dividend — it is earnings. Some of it may be kept as reserves.",
        purpose="To report the year’s earning power in the unit that a shareholder actually holds: one share. It is a compulsory line in a listed company’s P&L (Ind AS 33 / AS 20), and a standard MBA numerical.",
        formula_expr="EPS = (PAT − Preference dividend) ÷ Number of equity shares outstanding",
        formula_note="Number of shares = Equity share capital ÷ Face value. Kaveri: "
        + rupee(ESC)
        + " ÷ "
        + rupee(FV)
        + " = 40,000 shares. If new shares were issued mid-year, a weighted average is used (advanced; only if the paper gives dates). Face value is not market price.",
        components=[
            [
                "PAT − preference dividend",
                "Earnings for equity shareholders.",
                "Kaveri: "
                + rupee(PAT)
                + " − 0 = "
                + rupee(PAT)
                + ".",
            ],
            [
                "Number of equity shares",
                "Issued and outstanding equity shares, usually assumed equal to shares at year-end unless dates of issue are given.",
                rupee(ESC)
                + " ÷ "
                + rupee(FV)
                + " = 4,00,000 ÷ 10 = 40,000 shares.",
            ],
        ],
        pick="Do not divide PAT by share capital in rupees and call it EPS — that would be a return on face-capital, missing reserves and missing the “per share” unit. Do not use market price in the denominator (that is the P/E reciprocal when used with EPS). If preference dividend is given, subtract it.",
        steps_list=[
            "PAT minus preference dividend.",
            "Number of equity shares = equity share capital ÷ face value. (Or take the number if it is printed.)",
            "Divide. Unit: ₹ per share.",
            "One sentence: each equity share earned ₹X this year. Do not call it dividend.",
        ],
        high="Each share earned more. Owners are better off, other things equal.",
        low="Each share earned little. Either profit is weak or there are many shares (a recent issue, a bonus).",
        too_high="A bonus issue last year would have cut EPS in half without the business worsening — always check the number of shares. A one-time gain can spike EPS. Too low after a fresh issue may simply mean the new capital has not yet started earning.",
        ex_num="K26",
        work_formula="EPS = (PAT − Preference dividend) ÷ Number of equity shares",
        work_pick="PAT "
        + rupee(PAT)
        + "; preference dividend nil; shares = "
        + rupee(ESC)
        + " ÷ "
        + rupee(FV)
        + " = 40,000.",
        work_arith=rupee(PAT)
        + " ÷ 40,000 = 90,000 ÷ 40,000 = 9/4 = 2.25.",
        work_answer=rupee(2.25) + " per share",
        kaveri_read="Each of the 40,000 shares earned ₹2.25. Face value is ₹10, so earnings are 22.5% of face — but that is not ROE, because ROE uses share capital plus reserves. EPS is a per-share number for owners and for market ratios, not a substitute for ROE.",
        mistakes_list=[
            "Dividing PAT by share capital: 90,000/4,00,000 = 0.225, then writing “EPS = 0.225 times”. Wrong unit, wrong denominator.",
            "Forgetting to subtract preference dividend when preference shares exist.",
            "Using the market price of the share as the denominator.",
            "Calling EPS the dividend per share. DPS is a different number; Kaveri’s dividend is not even given.",
        ],
        mem="EPS = leftover for equity ÷ how many equity shares. Shares = capital / face value. Answer is ₹ per share, not %.",
    )


def _comb_icr() -> str:
    return ratio_section(
        heading="7.14 Interest coverage ratio (times interest earned)",
        bucket="Combined as a solvency companion (both figures can also be read from the P&L — see the classification note). Purpose family: solvency / debt-servicing.",
        ideal="Higher is safer. Below 2–3 times is usually uncomfortable. 5 times is a healthy cover for a trading firm. A term-loan covenant often demands a minimum (say 2.5 times).",
        meaning="Interest coverage is EBIT divided by interest (finance cost). It asks: how many times can the operating profit pay the interest bill?",
        simple_txt="Kaveri earned "
        + rupee(EBIT)
        + " of operating profit and owes "
        + rupee(INTEREST)
        + " of interest. It can pay the interest bill 5 times over. The banker sleeps.",
        purpose="To judge whether the debt load is serviceable from operations. Debt-equity tells you the stock of debt; interest coverage tells you whether this year’s profit can carry this year’s interest. You need both.",
        formula_expr="Interest coverage = EBIT ÷ Interest",
        formula_note="EBIT, not PAT, not PBT. PAT has already paid the interest (and tax), so PAT / interest understates cover and is the wrong matching. If interest is zero, the ratio is not defined — write “no interest, coverage not applicable”.",
        components=[
            [
                "EBIT",
                "Profit before interest and tax. The pool available to pay lenders.",
                "Kaveri: "
                + rupee(EBIT)
                + ".",
            ],
            [
                "Interest / finance cost",
                "Interest on long-term and short-term borrowings for the year. Not the principal repayment. Not preference dividend.",
                "Kaveri: "
                + rupee(INTEREST)
                + ".",
            ],
        ],
        pick="Add back interest if you are looking at PBT: EBIT = PBT + interest. Do not use “debt service” (principal + interest) unless the question asks for DSCR, which is a different ratio and not in this list.",
        steps_list=[
            "Build EBIT.",
            "Pick the interest line (finance costs).",
            "Divide. Unit: times.",
            "Comment with debt-equity: low D/E + high coverage = safe; high D/E + low coverage = danger.",
        ],
        high="Interest is easily earned. Lenders are safe. The firm can take a profit dip without defaulting.",
        low="A small fall in EBIT and interest cannot be paid. Distress. Fresh lending will be refused or expensive.",
        too_high="A coverage of 50 times usually means almost no debt — safe, but perhaps under-levered. Too low (under 1): EBIT does not even cover interest; the firm is paying interest by selling assets, raising new loans, or delaying other bills.",
        ex_num="K27",
        work_formula="Interest coverage = EBIT ÷ Interest",
        work_pick="EBIT "
        + rupee(EBIT)
        + "; Interest "
        + rupee(INTEREST)
        + ".",
        work_arith=rupee(EBIT)
        + " ÷ "
        + rupee(INTEREST)
        + " = 1,50,000 ÷ 30,000 = 15/3 = 5.",
        work_answer="5 times",
        kaveri_read="Operating profit can pay the interest bill five times. Combined with debt-equity of 0.33 : 1, Kaveri is a low-risk borrower. A drop of 80% in EBIT would still just cover interest (coverage of 1) — there is a wide buffer.",
        mistakes_list=[
            "Using PAT / interest = 90,000/30,000 = 3 times. That is after tax, after the interest has already been paid — it is not coverage.",
            "Using PBT / interest = 1,20,000/30,000 = 4 times. PBT is after interest, so this is “leftover / interest”, not coverage.",
            "Putting principal repayment in the denominator (that is DSCR territory).",
            "Using total debt in the denominator. Coverage is a flow/flow ratio, not a flow/stock ratio.",
        ],
        mem="Coverage = how many times EBIT can pay the interest. EBIT over Interest. PAT is too late; the interest has already left.",
    )


def _dupont() -> str:
    npm = PAT / SALES
    at = SALES / TA
    em = TA / SF
    return (
        h2("8. DuPont identity (short, useful in MBA papers)", "dupont")
        + definition(
            "The DuPont identity splits ROE into three Combined / Revenue pieces: "
            "a margin (net profit ratio), an activity ratio (asset turnover), and a leverage ratio (equity multiplier = total assets ÷ equity). "
            "ROE = Net profit margin × Asset turnover × Equity multiplier."
        )
        + simple(
            "Owners’ 15% return did not fall from the sky. It is 9% leftover on sales, times how hard the assets were worked, times how much the asset base is bigger than owners’ money. "
            "DuPont names the three knobs. If ROE falls, you know which knob moved."
        )
        + formula(
            "ROE = (PAT ÷ Sales) × (Sales ÷ Total assets) × (Total assets ÷ Equity)",
            "Sales and total assets cancel: the identity equals PAT ÷ Equity, which is ROE. The point is the split, not a new number.",
        )
        + example(
            "K28",
            "Moderate",
            "DuPont split of Kaveri’s 15% ROE",
            p(
                "Net profit margin = "
                + rupee(PAT)
                + " ÷ "
                + rupee(SALES)
                + " = 0.09 = 9%."
            )
            + p(
                "Asset turnover = "
                + rupee(SALES)
                + " ÷ "
                + rupee(TA)
                + " = 10,00,000 ÷ 9,50,000 = 20/19 = "
                + f"{at:.4f}"
                + " times."
            )
            + p(
                "Equity multiplier = "
                + rupee(TA)
                + " ÷ "
                + rupee(SF)
                + " = 9,50,000 ÷ 6,00,000 = 19/12 = "
                + f"{em:.4f}"
                + "."
            )
            + p(
                "Product = 0.09 × "
                + f"{at:.6f}"
                + " × "
                + f"{em:.6f}"
                + " = "
                + f"{npm * at:.6f}"
                + " × "
                + f"{em:.6f}"
                + " = "
                + f"{npm * at * em:.6f}"
                + " = 15%."
            )
            + p(
                b("Reading. ")
                + "Kaveri’s ROE is driven more by margin (9%) and a modest multiplier (1.58 — low gearing) than by furious asset turnover (only 1.05). "
                "To raise ROE without taking more debt, Meera must either lift the 9% margin or sweat the 9.5 lakh of assets harder. "
                "Taking more debt would lift the multiplier and ROE — and lift risk. DuPont makes that trade-off visible."
            ),
        )
        + exam_tip(
            "DuPont is optional in many B-school papers but scores easily as a 4-mark “explain ROE” add-on. "
            "Write the three-factor formula, plug in, and name which factor is the lever."
        )
        + memory(
            "M-A-L: Margin × Activity × Leverage = ROE. If ROE moved, circle which of the three moved."
        )
    )


def _kaveri_health() -> str:
    rows = [
        ["Current ratio", "BS / liquidity", _ratio_pair(CA, CL_), "Ideal ~ 2 : 1", "Exactly at ideal"],
        ["Quick ratio", "BS / liquidity", _ratio_pair(QA, CL_), "Ideal ~ 1 : 1", "Above ideal"],
        ["Cash ratio", "BS / liquidity", "0.53 : 1", "Ideal ~ 0.5 : 1", "At ideal"],
        ["Debt-equity (LT)", "BS / solvency", "0.33 : 1", "Comfortably under 1", "Conservative"],
        ["Debt-equity (total)", "BS / solvency", _ratio_pair(TD, SF), "Depends", "Still modest"],
        ["Proprietary ratio", "BS / solvency", "63.16%", "Higher = safer", "Owner-majority"],
        ["Capital gearing", "BS / solvency", "0.33 (low)", "< 1 = low geared", "Low geared"],
        ["FA to long-term funds", "BS / structure", "81.25%", "Should be < 100%", "Healthy matching"],
        ["CA to proprietary funds", "BS / structure", "50%", "Trader > factory", "Fits a trader"],
        ["GP ratio", "Rev / profitability", "25%", "Industry", "Solid trading margin"],
        ["Operating profit ratio", "Rev / profitability", "15%", "Industry", "Clean staircase"],
        ["NP ratio (PAT)", "Rev / profitability", "9%", "Industry", "Respectable"],
        ["Operating ratio", "Rev / cost", "85%", "Lower better", "Adds with OP% to 100"],
        ["Employee-cost ratio", "Rev / cost", "6%", "Mix", "Named slice"],
        ["Inventory turnover", "Comb / efficiency", "7.5 times", "Industry", "Healthy pace"],
        ["Holding period", "Comb / efficiency", "48.67 days", "Shorter better", "~ 7 weeks in godown"],
        ["Debtors turnover", "Comb / efficiency", "10 times", "Higher = faster", "Brisk collection"],
        ["Collection period", "Comb / efficiency", "36.5 days", "Vs credit allowed", "Prompt"],
        ["Creditors turnover", "Comb / efficiency", "6.08 times", "Vs credit taken", "About 6 turns"],
        ["Payment period", "Comb / efficiency", "60.06 days", "Vs credit allowed", "Two months’ free credit"],
        ["WC turnover", "Comb / efficiency", "6.67 times", "Watch overtrading", "Use, not overtrading"],
        ["FA turnover", "Comb / efficiency", "1.54 times", "Industry", "Modest (owns godown)"],
        ["Capital turnover", "Comb / efficiency", "1.25 times", "Engine of ROCE", "Checks with ROCE"],
        ["ROCE", "Comb / profitability", "18.75%", "Above cost of debt", "Debt is earning its keep"],
        ["ROE", "Comb / profitability", "15%", "Owners’ scoreboard", "Solid, not geared-up"],
        ["ROA (PAT)", "Comb / profitability", "9.47%", "Whole asset base", "Consistent with low gearing"],
        ["EPS", "Comb / profitability", rupee(2.25) + " / share", "Vs last year", "On 40,000 shares of ₹10"],
        ["Interest coverage", "Comb / solvency", "5 times", "Above 3 is comfortable", "Wide buffer"],
    ]
    return (
        h2("9. Kaveri at a glance — every ratio, then a health comment", "health")
        + p(
            "This is the page you should be able to rebuild, closed-book, from the two statements. "
            "Every figure traces to Kaveri Traders Ltd, year ended 31 March 2026."
        )
        + table(
            ["Ratio", "Bucket / family", "Kaveri", "Yardstick", "One-word reading"],
            rows,
            caption="Master result sheet — Kaveri Traders Ltd, 31 March 2026",
        )
        + h3("Four-to-five sentence health comment (this is what “interpret” looks like in the paper)")
        + exam_answer(
            "Kaveri Traders is liquid: the current ratio sits at the textbook 2 : 1, the acid test at 1.2 : 1 and the cash ratio at 0.53 : 1, so short-term bills are covered even if stock is ignored. "
            "The firm is conservatively financed — debt-equity 0.33 : 1, proprietary ratio 63%, low capital gearing, interest covered 5 times — and fixed assets are fully funded by long-term money (FA to long-term funds 81%). "
            "Profitability is decent for a wholesaler: gross 25%, operating 15%, net 9%, ROCE 18.75% and ROE 15%, with EPS ₹2.25; ROCE clears the 15% coupon on the term loan, so gearing is helping, not hurting. "
            "Efficiency is the quiet strength: stock turns 7.5 times (held ~49 days), debtors pay in 36.5 days and suppliers are paid in ~60 days, which produces a short net cash cycle of about 25 days. "
            "Watch-outs are modest rather than alarming — FA turnover is only 1.54 because the firm owns its godown, the 9% net margin will feel any wage or interest shock, and the current ratio of 2.0 is not a licence to let stock go stale (though 7.5 turns says it has not). "
            "Overall, Kaveri is a solvent, moderately profitable trader with a healthy operating cycle and unused debt capacity."
        )
        + keypoint(
            "A health comment always has four beats: liquidity, solvency, profitability, efficiency. Then one watch-out. Then one overall sentence. "
            "That structure scores even when your adjectives are cautious."
        )
    )


def _rebuild() -> str:
    # Set B arithmetic: CR 2.5, WC 1,50,000, QR 1.5
    cl_b = 100_000
    ca_b = 250_000
    qa_b = 150_000
    inv_b = 100_000
    # Set C: GP 20%, STO 5, op = cl = 40,000
    op_c = 40_000
    sto_c = 5
    gp_rate = 0.20
    cogs_c = sto_c * op_c  # 200_000 because opening = closing = avg
    sales_c = int(cogs_c / (1 - gp_rate))
    gp_c = sales_c - cogs_c
    return (
        h2("10. Reconstruction numericals — the exam favourite", "rebuild")
        + lead(
            "A large slice of MBA ratio marks does not give you a P&L and a BS. It gives you "
            + b("some ratios and one rupee figure")
            + ", and asks you to rebuild CA, CL, stock, COGS or sales. "
            "The method is algebra with the formula, not memory of Kaveri."
        )
        + p(
            b("Golden reconstruction rules. ")
            + "(1) Write the ratio formula. (2) Replace the words with letters (CA, CL, WC). (3) Write any extra identity (WC = CA − CL). "
            "(4) Solve the two equations. (5) Never treat “current ratio 2.5” as WC = 2.5."
        )
        + h3("Type A — Current ratio and working capital → CA and CL")
        + example(
            "R1",
            "Moderate",
            "Current ratio 2.5, working capital ₹1,50,000. Find CA and CL. Then quick ratio 1.5; find inventory.",
            p(
                b("Given. ")
                + "Current ratio = 2.5, Working capital = "
                + rupee(150000)
                + ", Quick ratio = 1.5. Prepaid expenses are nil. Find current assets, current liabilities and inventory."
            )
            + p(b("Step 1 — names."))
            + p("Let CL = x. Then CA = 2.5x, because current ratio = CA/CL = 2.5.")
            + p(b("Step 2 — working-capital identity."))
            + p("WC = CA − CL = 2.5x − x = 1.5x.")
            + p("1.5x = " + rupee(150000) + ".")
            + p(b("Step 3 — solve for x."))
            + p(
                "x = "
                + rupee(150000)
                + " ÷ 1.5 = "
                + rupee(150000)
                + " ÷ (3/2) = "
                + rupee(150000)
                + " × 2/3 = "
                + rupee(300000)
                + " ÷ 3 = "
                + rupee(cl_b)
                + "."
            )
            + p("So CL = " + rupee(cl_b) + ".")
            + p("CA = 2.5 × " + rupee(cl_b) + " = (5/2) × " + rupee(cl_b) + " = " + rupee(ca_b) + ".")
            + p(b("Check. ") + "CA − CL = " + rupee(ca_b) + " − " + rupee(cl_b) + " = " + rupee(ca_b - cl_b) + " = WC. And CA/CL = 2.5. Both given facts return.")
            + p(b("Step 4 — quick ratio."))
            + p("Quick ratio = Quick assets / CL = 1.5, so Quick assets = 1.5 × " + rupee(cl_b) + " = " + rupee(qa_b) + ".")
            + p(
                "Inventory = CA − Quick assets − Prepaid = "
                + rupee(ca_b)
                + " − "
                + rupee(qa_b)
                + " − 0 = "
                + rupee(inv_b)
                + "."
            )
            + p(
                b("Answer. ")
                + "Current assets "
                + rupee(ca_b)
                + ", current liabilities "
                + rupee(cl_b)
                + ", inventory "
                + rupee(inv_b)
                + "."
            )
            + warn(
                "If prepaid had been given, inventory would be CA − QA − prepaid, not CA − QA. "
                "If the paper gives “liquid assets include debtors and cash only”, you are already looking at QA."
            ),
        )
        + h3("Type B — GP ratio, stock turnover, opening = closing → COGS, sales, GP, purchases")
        + example(
            "R2",
            "Exam",
            "GP ratio 20%, stock turnover 5 times, opening stock ₹40,000 = closing stock. Find COGS, sales, GP and purchases.",
            p(
                b("Given. ")
                + "Gross profit ratio = 20% of sales. Inventory turnover = 5 times (COGS version). "
                "Opening stock = closing stock = "
                + rupee(op_c)
                + "."
            )
            + p(b("Step 1 — average stock."))
            + p(
                "Opening = closing, so average stock = "
                + rupee(op_c)
                + ". "
                "(If they had been different you would add and divide by 2.)"
            )
            + p(b("Step 2 — COGS from turnover."))
            + p(
                "Stock turnover = COGS / average stock = 5, so COGS = 5 × "
                + rupee(op_c)
                + " = "
                + rupee(cogs_c)
                + "."
            )
            + p(b("Step 3 — sales from GP ratio."))
            + p("GP = 20% of sales, so COGS = 80% of sales (because GP + COGS = Sales).")
            + p("0.80 × Sales = " + rupee(cogs_c) + ".")
            + p(
                "Sales = "
                + rupee(cogs_c)
                + " ÷ 0.80 = "
                + rupee(cogs_c)
                + " ÷ (4/5) = "
                + rupee(cogs_c)
                + " × 5/4 = "
                + rupee(cogs_c * 5)
                + " ÷ 4 = "
                + rupee(sales_c)
                + "."
            )
            + p(b("Step 4 — GP."))
            + p(
                "GP = Sales − COGS = "
                + rupee(sales_c)
                + " − "
                + rupee(cogs_c)
                + " = "
                + rupee(gp_c)
                + ". "
                "Check: 20% of "
                + rupee(sales_c)
                + " = "
                + rupee(gp_c)
                + "."
            )
            + p(b("Step 5 — purchases."))
            + p(
                "COGS = Opening + Purchases − Closing. Opening = closing, so Purchases = COGS = "
                + rupee(cogs_c)
                + "."
            )
            + p(
                b("Answer. ")
                + "COGS "
                + rupee(cogs_c)
                + ", Sales "
                + rupee(sales_c)
                + ", GP "
                + rupee(gp_c)
                + ", Purchases "
                + rupee(cogs_c)
                + "."
            ),
        )
        + h3("Type C — Opening ≠ closing, GP ratio and stock turnover → closing stock and sales")
        + example(
            "R3",
            "Exam",
            "Sales are not given. GP ratio 20%, stock turnover 8, opening stock ₹40,000, closing stock ₹60,000. Find COGS, sales and GP.",
            p(b("Given. ") + "GP ratio 20%. Stock turnover 8 (COGS / average stock). Opening " + rupee(40000) + ", closing " + rupee(60000) + ".")
            + p(b("Average stock."))
            + p("(" + rupee(40000) + " + " + rupee(60000) + ") ÷ 2 = " + rupee(100000) + " ÷ 2 = " + rupee(50000) + ".")
            + p(b("COGS."))
            + p("8 × " + rupee(50000) + " = " + rupee(400000) + ".")
            + p(b("Sales."))
            + p("COGS = 80% of sales, so Sales = " + rupee(400000) + " ÷ 0.80 = " + rupee(500000) + ".")
            + p(b("GP."))
            + p("20% of " + rupee(500000) + " = " + rupee(100000) + ". Check: " + rupee(500000) + " − " + rupee(400000) + " = " + rupee(100000) + ".")
            + p(b("Purchases, if asked."))
            + p(
                "Purchases = COGS + closing − opening = "
                + rupee(400000)
                + " + "
                + rupee(60000)
                + " − "
                + rupee(40000)
                + " = "
                + rupee(420000)
                + "."
            )
            + p(
                b("Answer. ")
                + "COGS "
                + rupee(400000)
                + ", Sales "
                + rupee(500000)
                + ", GP "
                + rupee(100000)
                + ", Purchases "
                + rupee(420000)
                + "."
            ),
        )
        + h3("Type D — Current ratio 3, WC ₹80,000 (a different number, so you cannot copy R1)")
        + example(
            "R4",
            "Moderate",
            "Current ratio 3 : 1, working capital ₹80,000. Find CA and CL.",
            p("Let CL = x, CA = 3x.")
            + p("3x − x = " + rupee(80000) + " so 2x = " + rupee(80000) + ", x = " + rupee(40000) + ".")
            + p("CL = " + rupee(40000) + ", CA = 3 × " + rupee(40000) + " = " + rupee(120000) + ".")
            + p(b("Check. ") + rupee(120000) + " − " + rupee(40000) + " = " + rupee(80000) + "; " + rupee(120000) + " ÷ " + rupee(40000) + " = 3.")
            + p(b("Answer. ") + "CA " + rupee(120000) + ", CL " + rupee(40000) + "."),
        )
        + identify(
            "If the question gives a ratio and working capital (or one of CA / CL) and asks for the missing BS items, it is Type A algebra. "
            "If it gives GP% and stock turnover and stock, it is Type B/C — build COGS first, then sales from the complement of GP%. "
            "If it gives proprietary ratio and total assets, SF = rate × TA. Always write the identity WC = CA − CL; it is the second equation you need."
        )
        + mistakes(
            [
                "Current ratio 2.5 and WC "
                + rupee(150000)
                + " → “CA = 2.5 × 1,50,000”. That treats WC as CL. The 2.5 applies to CL, not to WC.",
                "GP 20% and COGS "
                + rupee(200000)
                + " → “Sales = 20% × 2,00,000”. No: 20% is of sales, not of COGS. COGS is 80% of sales.",
                "Stock turnover 5, opening 40,000, closing 60,000 → “COGS = 5 × 40,000”. Use the average, not opening alone.",
                "Quick ratio 1.5, CA 2,50,000 → “Inventory = 1.5 × 2,50,000”. Quick ratio is QA/CL, not inventory/CA.",
            ]
        )
        + memory(
            "Two equations, two unknowns. Ratio gives you CA = k × CL. WC gives you CA − CL = a rupee amount. Solve. "
            "For GP% + turnover: turnover → COGS, complement of GP% → Sales."
        )
    )


def _identify() -> str:
    return (
        h2("11. How to identify the ratio the question wants", "identify")
        + lead(
            "Most numericals do not print the formula. They print a situation, or a table, or the words “comment on liquidity”. "
            "This table is the translation layer. Read the left column in the exam hall."
        )
        + table(
            ["If the question says / gives…", "You should reach for…", "Bucket"],
            [
                ["Current assets and current liabilities, or “ability to pay short-term dues”", "Current ratio (and WC as the rupee cousin)", "BS"],
                ["“Acid test / liquid / quick”, or CA, stock, prepaid, CL", "Quick ratio — deduct stock and prepaid", "BS"],
                ["Cash, marketable securities, CL; “immediate cash”", "Absolute liquid / cash ratio", "BS"],
                ["Long-term loan / debentures and shareholders’ funds; “capital structure / borrowed vs own”", "Debt-equity (say which version)", "BS"],
                ["“Owners’ slice of assets”, proprietary, tangible assets", "Proprietary ratio = SF / TA", "BS"],
                ["Preference capital + debt vs equity; “high geared / low geared”", "Capital gearing", "BS"],
                ["Fixed assets and long-term funds; “matching / FA financed by”", "FA to long-term funds — flag if > 1", "BS"],
                ["Current assets and proprietary funds", "CA to proprietary funds", "BS"],
                ["Gross profit and sales; “trading margin / mark-up on sales”", "GP ratio", "Rev"],
                ["PAT (or PBT) and sales; “net margin”", "NP ratio — state PAT or PBT", "Rev"],
                ["EBIT / operating profit / PBIT and sales", "Operating profit ratio", "Rev"],
                ["Operating cost, or COGS + opex, over sales; “cost-heaviness”", "Operating ratio (should pair with OP%)", "Rev"],
                ["A named expense over sales (wages, rent, interest)", "That expense ratio", "Rev"],
                ["“How quickly stock sells / stock velocity / godown flipped”", "Inventory turnover (COGS / avg stock) and holding days", "Comb"],
                ["Credit sales and debtors; “collection / receivables velocity”", "Debtors turnover and collection period", "Comb"],
                ["Credit purchases and creditors; “payment period / how fast we pay”", "Creditors turnover and payment period", "Comb"],
                ["Sales and working capital; “overtrading”", "WC turnover", "Comb"],
                ["Sales and net FA; “capacity / sweated assets”", "FA turnover", "Comb"],
                ["Sales and capital employed; “activity of long-term funds”", "Capital turnover", "Comb"],
                ["“ROCE / overall profitability of funds / return on long-term capital”", "EBIT / CE × 100 — not PAT", "Comb"],
                ["“ROE / return on owners’ / return on net worth / return on shareholders’ funds”", "PAT / (capital + reserves) × 100", "Comb"],
                ["Return on total assets / whole resource base", "PAT/TA or EBIT/TA — label it", "Comb"],
                ["Earnings per share, number of shares, face value", "EPS = (PAT − pref div) / number of equity shares", "Comb"],
                ["“Times interest earned / ability to pay interest / coverage”", "EBIT / Interest — not PAT / Interest", "Comb"],
                ["Current ratio + working capital, find CA and CL", "Algebra Type A (section 10)", "Rebuild"],
                ["Quick ratio after that, find inventory", "QA = QR × CL; Inventory = CA − QA − prepaid", "Rebuild"],
                ["GP% + stock turnover + stock, find sales / COGS", "Algebra Type B/C: turnover → COGS, complement of GP% → sales", "Rebuild"],
                ["“Comment on liquidity” with a full set of statements", "Current + quick + cash, then one sentence each", "Comment"],
                ["“Comment on solvency / capital structure”", "Debt-equity + proprietary + gearing + interest coverage", "Comment"],
                ["“Comment on profitability”", "GP, OP, NP, ROCE, ROE (and EPS if shares are given)", "Comment"],
                ["“Comment on efficiency / activity”", "Stock, debtors, creditors, FA, capital, WC turnovers + days", "Comment"],
            ],
            caption="Identification table — read the trigger, pick the ratio, name the bucket",
        )
        + exam_tip(
            "When a question gives a full P&L and BS and says “compute ratios” without naming them, do not compute all 27. "
            "Compute a balanced set: 2 liquidity, 2 solvency, 3 profitability, 3 efficiency — ten ratios, each with formula, figure, unit, one-line comment. "
            "That is a 16–20 mark answer. Dumping 27 numbers with no comment scores worse."
        )
    )


def _mistakes_all() -> str:
    return (
        h2("12. Common mistakes (chapter-wide)", "mistakes")
        + mistakes(
            [
                "Using sales instead of COGS for stock turnover. Stock is at cost. Kaveri would wrongly show 10 times instead of 7.5.",
                "Including prepaid expenses in quick assets. Prepaid will not pay a creditor.",
                "Using PAT instead of EBIT for ROCE. Matching rule: CE includes lenders, so profit must be before interest.",
                "Using only share capital instead of shareholders’ funds (capital + reserves) for ROE, debt-equity, proprietary ratio. Reserves are owners’ money.",
                "Mixing 365-day and 360-day conventions, or writing days as “times”.",
                "Not using averages when opening stock / debtors / creditors are given. Closing-only is allowed only when opening is not given, and you must say so.",
                "Reading current ratio 2 as CA − CL = 2. It means CA = 2 × CL.",
                "Using total sales for debtors turnover when cash sales are given.",
                "Using COGS (or sales) instead of credit purchases for creditors turnover.",
                "Including interest in operating cost, so that operating ratio + operating profit ratio no longer add to 100%.",
                "Calling every profitability ratio a Revenue ratio. ROCE, ROE, ROA, EPS are Combined by source.",
                "Comparing two firms’ GP% without checking that one includes depreciation in COGS and the other does not — policies differ.",
                "A beautiful ratio on 31 March after window dressing (repaying a creditor on 30 March, re-borrowing on 2 April).",
                "Writing a number with no unit and no sentence, and calling it “analysis”.",
                "Inverting a ratio (equity/debt when the paper asked debt/equity) and then applying the “high is risky” comment to the inverted number.",
                "Treating a high current ratio as automatically good, and a high stock turnover as automatically good. Both have a “too high” side.",
            ]
        )
        + warn(
            "If you remember only six mistakes for the night before the paper, remember these six: "
            "sales-for-COGS, prepaid-in-quick, PAT-for-ROCE, capital-without-reserves, no-average-when-opening-given, current-ratio-2-means-CA-minus-CL-equals-2."
        )
    )


def _memory_all() -> str:
    return (
        h2("13. Memory tricks for the whole chapter", "memory")
        + memory(
            "Three buckets: BS–BS structure, P&L–P&L margin, P&L–BS speed-or-return. "
            "Liquidity staircase: current (trust stock) → quick (drop stock and prepaid) → cash (already money). Ideals 2 : 1, 1 : 1, 0.5 : 1. "
            "Solvency: outsiders over owners (D/E); owners over the pie (proprietary); fixed-charge over equity (gearing); FA over long money (should be under 1). "
            "Margins staircase down the P&L: GP, then operating, then net. Operating ratio is the cost twin of operating profit%; they add to 100. "
            "Turnover = a flow over an average stock. Days = 365 / times. Stock at cost (COGS), debtors from credit sales, creditors from credit purchases. "
            "Matching rule: whoever is in the denominator must not already have been paid in the numerator. CE includes lenders → EBIT. Equity is owners → PAT. "
            "EPS is ₹ per share, not %. Shares = capital / face. "
            "Reconstruction: ratio is a k, WC is a rupee difference; two equations. GP% complement gives COGS/Sales."
        )
        + table(
            ["Ratio", "Pocket formula", "Ideal / flag"],
            [
                ["Current", "CA / CL", "2 : 1"],
                ["Quick", "(CA − stock − prepaid) / CL", "1 : 1"],
                ["Cash", "(cash + mkt sec) / CL", "0.5 : 1"],
                ["Debt-equity", "LTD / SF", "lower = safer"],
                ["Proprietary", "SF / TA", "higher = safer"],
                ["Gearing", "(pref + LTD) / equity funds", "< 1 low geared"],
                ["FA / long funds", "Net FA / CE", "< 1"],
                ["GP%", "GP / Sales × 100", "industry"],
                ["OP%", "EBIT / Sales × 100", "industry"],
                ["NP%", "PAT / Sales × 100", "industry"],
                ["Operating ratio", "(COGS + opex) / Sales × 100", "100 − OP%"],
                ["Stock turnover", "COGS / avg stock", "times; days = 365 / t"],
                ["Debtors turnover", "Credit sales / avg debtors", "times; days = 365 / t"],
                ["Creditors turnover", "Credit purchases / avg creditors", "times; days = 365 / t"],
                ["ROCE", "EBIT / CE × 100", "above cost of debt"],
                ["ROE", "PAT / SF × 100", "owners’ scoreboard"],
                ["EPS", "(PAT − pref div) / no. of equity shares", "₹ / share"],
                ["Interest cover", "EBIT / Interest", "times; above ~3"],
            ],
            caption="Pocket card — say it out loud once a day in the week of the exam",
        )
    )


def _formula_table() -> str:
    rows = [
        ["Current ratio", "BS", "CA ÷ CL", "times or x : 1", "Ideal ~ 2 : 1"],
        ["Quick / acid-test ratio", "BS", "(CA − Inventory − Prepaid) ÷ CL", "x : 1", "Ideal ~ 1 : 1"],
        ["Absolute liquid / cash ratio", "BS", "(Cash + Marketable securities) ÷ CL", "x : 1", "Ideal ~ 0.5 : 1"],
        ["Debt-equity (long-term)", "BS", "Long-term debt ÷ Shareholders’ funds", "x : 1", "Common MBA version; lower = safer"],
        ["Debt-equity (total)", "BS", "(LTD + CL) ÷ Shareholders’ funds", "x : 1", "Use when the question says total debt"],
        ["Proprietary ratio", "BS", "Shareholders’ funds ÷ Total assets", "ratio or %", "Higher = bigger owner-cushion"],
        ["Capital gearing", "BS", "(Preference capital + LTD) ÷ Equity funds", "ratio", "< 1 low geared (this version)"],
        ["FA to long-term funds", "BS", "Net FA ÷ (SF + LTD)", "ratio or %", "Should be < 1"],
        ["CA to proprietary funds", "BS", "CA ÷ Shareholders’ funds", "ratio or %", "Higher for traders"],
        ["Gross profit ratio", "Rev", "GP ÷ Sales × 100", "%", "Industry; GP = Sales − COGS"],
        ["Net profit ratio", "Rev", "PAT ÷ Sales × 100", "%", "PBT version if asked"],
        ["Operating profit ratio", "Rev", "EBIT ÷ Sales × 100", "%", "EBIT = PBT + interest"],
        ["Operating ratio", "Rev", "(COGS + Operating expenses) ÷ Sales × 100", "%", "≈ 100% − OP%; interest stays out"],
        ["Expense ratio", "Rev", "Particular expense ÷ Sales × 100", "%", "Name the expense"],
        ["Inventory turnover", "Comb", "COGS ÷ Average inventory", "times", "Preferred over Sales / stock"],
        ["Inventory holding period", "Comb", "365 ÷ Inventory turnover", "days", "Or 360 / 12 / 52 as asked"],
        ["Debtors turnover", "Comb", "Credit sales ÷ Average debtors", "times", "Assume all credit if split silent"],
        ["Average collection period", "Comb", "365 ÷ Debtors turnover", "days", "Compare with credit allowed"],
        ["Creditors turnover", "Comb", "Credit purchases ÷ Average creditors", "times", "Purchases = COGS + Δstock"],
        ["Average payment period", "Comb", "365 ÷ Creditors turnover", "days", "Compare with credit taken"],
        ["Working capital turnover", "Comb", "Sales ÷ (CA − CL)", "times", "Very high → overtrading"],
        ["Fixed asset turnover", "Comb", "Sales ÷ Net FA", "times", "Net, not gross"],
        ["Capital turnover", "Comb", "Sales ÷ Capital employed", "times", "CE = SF + LTD = FA + WC"],
        ["ROCE", "Comb", "EBIT ÷ Capital employed × 100", "%", "Not PAT; check OP% × cap. turnover"],
        ["ROE", "Comb", "PAT ÷ Equity shareholders’ funds × 100", "%", "Capital + reserves; not EBIT"],
        ["ROA (PAT)", "Comb", "PAT ÷ Total assets × 100", "%", "EBIT version also exists"],
        ["EPS", "Comb", "(PAT − Pref. dividend) ÷ No. of equity shares", "₹ / share", "Shares = ESC ÷ face value"],
        ["Interest coverage", "Comb", "EBIT ÷ Interest", "times", "Not PAT / interest"],
        ["DuPont ROE", "Comb", "NP margin × Asset turnover × Equity multiplier", "%", "Optional three-factor split"],
        ["Net cash cycle", "Comb", "Hold days + Collect days − Pay days", "days", "Kaveri ≈ 25 days"],
        ["Capital employed", "BS identity", "SF + LTD &nbsp;or&nbsp; Net FA + WC", "₹", "Both methods must match"],
        ["Working capital", "BS identity", "CA − CL", "₹", "Not a ratio; the rupee cousin of current ratio"],
        ["Shareholders’ funds", "BS identity", "ESC + Reserves − fictitious assets", "₹", "Not ESC alone"],
        ["Average of a BS item", "Working", "(Opening + Closing) ÷ 2", "₹", "When opening is given, you must average"],
    ]
    return (
        h2("14. Complete ratio formula table", "table")
        + p(
            "This is the last-night page. Every ratio in the syllabus is here, with bucket, formula, unit and the comment that belongs in the answer. "
            "If a paper prints a different version, obey the paper and write “as per the given formula”."
        )
        + table(
            ["Name", "Type", "Formula", "Unit", "Ideal / comment"],
            rows,
            caption="Chapter 7 — complete formula table (Balance Sheet / Revenue / Combined)",
            foot="Type = syllabus source-bucket. CE = capital employed. SF = shareholders’ funds. LTD = long-term debt. ESC = equity share capital.",
        )
    )


def _practice() -> str:
    # Practice 1 figures
    p1_ca, p1_inv, p1_pre, p1_cl = 400_000, 120_000, 20_000, 200_000
    p1_cr = p1_ca / p1_cl
    p1_qa = p1_ca - p1_inv - p1_pre
    p1_qr = p1_qa / p1_cl
    p1_cash = 80_000
    p1_cashr = p1_cash / p1_cl
    # Practice 4: Mini firm
    return (
        h2("15. Practice set with solutions", "practice")
        + p(
            "Do each question on paper before you open the solution. Copy the four-line working (formula, figures, arithmetic, answer with unit). "
            "Questions 1–2 are Easy, 3–5 Moderate, 6–8 Exam-level. Question 8 is a full Kaveri-style comment from a different company, so you cannot copy section 9."
        )
        + practice(
            "7.1",
            "Easy",
            "Current, quick and cash ratios from a list of assets",
            p(
                "From the following, compute current ratio, quick ratio and absolute liquid ratio. "
                "Current assets: inventory "
                + rupee(p1_inv)
                + ", trade receivables "
                + rupee(180000)
                + ", cash "
                + rupee(p1_cash)
                + ", prepaid insurance "
                + rupee(p1_pre)
                + ". "
                "Current liabilities: trade payables "
                + rupee(p1_cl)
                + ". "
                "There are no marketable securities."
            )
            + p(b("Hint. ") + "Add CA first. Deduct stock and prepaid for quick. Cash only for absolute liquid."),
            work_table(
                "CR = CA/CL; QR = (CA − inv − prepaid)/CL; Cash = (cash + mkt sec)/CL",
                "CA = "
                + rupee(p1_inv)
                + " + "
                + rupee(180000)
                + " + "
                + rupee(p1_cash)
                + " + "
                + rupee(p1_pre)
                + " = "
                + rupee(p1_ca)
                + ". CL = "
                + rupee(p1_cl)
                + ". Quick assets = "
                + rupee(p1_ca)
                + " − "
                + rupee(p1_inv)
                + " − "
                + rupee(p1_pre)
                + " = "
                + rupee(p1_qa)
                + ".",
                "CR = "
                + rupee(p1_ca)
                + " ÷ "
                + rupee(p1_cl)
                + " = 2. "
                "QR = "
                + rupee(p1_qa)
                + " ÷ "
                + rupee(p1_cl)
                + " = 2,60,000 ÷ 2,00,000 = 1.3. "
                "Cash ratio = "
                + rupee(p1_cash)
                + " ÷ "
                + rupee(p1_cl)
                + " = 0.40.",
                "Current 2 : 1; Quick 1.3 : 1; Cash 0.40 : 1",
            )
            + p(
                b("Comment. ")
                + "Current is at ideal. Quick is above 1 : 1 (prepaid was correctly dropped — leaving it in would have given 1.4). "
                "Cash is a little under 0.5 : 1, so the firm leans on debtors for immediate bills."
            ),
        )
        + practice(
            "7.2",
            "Easy",
            "GP, NP and operating ratios",
            p(
                "Sales "
                + rupee(500000)
                + ", COGS "
                + rupee(350000)
                + ", operating expenses "
                + rupee(50000)
                + ", interest "
                + rupee(20000)
                + ", tax "
                + rupee(20000)
                + ". "
                "Compute GP ratio, operating profit ratio, operating ratio and NP ratio. Show that operating ratio + operating profit ratio = 100%."
            ),
            p("GP = " + rupee(500000) + " − " + rupee(350000) + " = " + rupee(150000) + ".")
            + p("GP ratio = (1,50,000 ÷ 5,00,000) × 100 = 30%.")
            + p("EBIT = GP − opex = " + rupee(150000) + " − " + rupee(50000) + " = " + rupee(100000) + ".")
            + p("Operating profit ratio = (1,00,000 ÷ 5,00,000) × 100 = 20%.")
            + p("Operating cost = " + rupee(350000) + " + " + rupee(50000) + " = " + rupee(400000) + ".")
            + p("Operating ratio = (4,00,000 ÷ 5,00,000) × 100 = 80%.")
            + p("Check: 80% + 20% = 100%.")
            + p("PAT = EBIT − interest − tax = " + rupee(100000) + " − " + rupee(20000) + " − " + rupee(20000) + " = " + rupee(60000) + ".")
            + p("NP ratio = (60,000 ÷ 5,00,000) × 100 = 12%.")
            + p(b("Answer. ") + "GP 30%, OP 20%, operating ratio 80%, NP 12%."),
        )
        + practice(
            "7.3",
            "Moderate",
            "Rebuild CA, CL, inventory from ratios",
            p(
                "Current ratio 2.5, working capital "
                + rupee(150000)
                + ", quick ratio 1.5. Prepaid nil. Find current assets, current liabilities and inventory."
            ),
            p("This is reconstruction Type A (example R1).")
            + p("CL = x, CA = 2.5x, 2.5x − x = 1.5x = " + rupee(150000) + ", x = " + rupee(100000) + ".")
            + p("CA = " + rupee(250000) + ", CL = " + rupee(100000) + ".")
            + p("QA = 1.5 × " + rupee(100000) + " = " + rupee(150000) + ".")
            + p("Inventory = " + rupee(250000) + " − " + rupee(150000) + " = " + rupee(100000) + ".")
            + p(b("Answer. ") + "CA " + rupee(250000) + ", CL " + rupee(100000) + ", inventory " + rupee(100000) + "."),
        )
        + practice(
            "7.4",
            "Moderate",
            "GP 20%, stock turnover 5, opening = closing = ₹40,000",
            p("Find average stock, COGS, sales, GP and purchases."),
            p("Average stock = " + rupee(40000) + " (opening = closing).")
            + p("COGS = 5 × " + rupee(40000) + " = " + rupee(200000) + ".")
            + p("COGS = 80% of sales, so Sales = " + rupee(200000) + " ÷ 0.80 = " + rupee(250000) + ".")
            + p("GP = " + rupee(250000) + " − " + rupee(200000) + " = " + rupee(50000) + " = 20% of sales.")
            + p("Purchases = COGS (stock unchanged) = " + rupee(200000) + ".")
            + p(
                b("Answer. ")
                + "Avg stock "
                + rupee(40000)
                + ", COGS "
                + rupee(200000)
                + ", Sales "
                + rupee(250000)
                + ", GP "
                + rupee(50000)
                + ", Purchases "
                + rupee(200000)
                + "."
            ),
        )
        + practice(
            "7.5",
            "Moderate",
            "Stock turnover with unequal opening and closing",
            p(
                "GP ratio 20%. Stock turnover 8 times. Opening stock "
                + rupee(40000)
                + ", closing stock "
                + rupee(60000)
                + ". Find COGS, sales, GP and purchases."
            ),
            p("Average stock = (" + rupee(40000) + " + " + rupee(60000) + ") ÷ 2 = " + rupee(50000) + ".")
            + p("COGS = 8 × " + rupee(50000) + " = " + rupee(400000) + ".")
            + p("Sales = " + rupee(400000) + " ÷ 0.80 = " + rupee(500000) + ".")
            + p("GP = " + rupee(100000) + ".")
            + p("Purchases = " + rupee(400000) + " + " + rupee(60000) + " − " + rupee(40000) + " = " + rupee(420000) + ".")
            + p(
                b("Answer. ")
                + "COGS "
                + rupee(400000)
                + ", Sales "
                + rupee(500000)
                + ", GP "
                + rupee(100000)
                + ", Purchases "
                + rupee(420000)
                + "."
            ),
        )
        + practice(
            "7.6",
            "Exam",
            "ROCE, ROE, EPS and interest coverage from a short extract",
            p(
                "Equity share capital (₹10 shares) "
                + rupee(200000)
                + ", reserves "
                + rupee(100000)
                + ", long-term loan "
                + rupee(100000)
                + ". "
                "EBIT "
                + rupee(80000)
                + ", interest "
                + rupee(10000)
                + ", tax "
                + rupee(14000)
                + ". Compute capital employed, ROCE, PAT, ROE, number of shares, EPS, interest coverage. "
                "Does gearing help the owners? One sentence."
            ),
            p("SF = " + rupee(200000) + " + " + rupee(100000) + " = " + rupee(300000) + ".")
            + p("CE = " + rupee(300000) + " + " + rupee(100000) + " = " + rupee(400000) + ".")
            + p("ROCE = (80,000 ÷ 4,00,000) × 100 = 20%.")
            + p("PBT = 80,000 − 10,000 = 70,000. PAT = 70,000 − 14,000 = 56,000.")
            + p("ROE = (56,000 ÷ 3,00,000) × 100 = 18.67% (18.666…%).")
            + p("Shares = 2,00,000 ÷ 10 = 20,000. EPS = 56,000 ÷ 20,000 = " + rupee(2.80) + " per share.")
            + p("Interest coverage = 80,000 ÷ 10,000 = 8 times.")
            + p(
                b("Gearing sentence. ")
                + "ROCE is 20% pre-tax; the loan costs 10,000/1,00,000 = 10% pre-tax, so the extra return on borrowed money accrues to owners — gearing helps. "
                "After tax, ROE 18.67% is still a healthy owners’ return, and coverage of 8 times says the help is not reckless."
            )
            + p(
                b("Answer. ")
                + "CE "
                + rupee(400000)
                + ", ROCE 20%, PAT "
                + rupee(56000)
                + ", ROE 18.67%, 20,000 shares, EPS "
                + rupee(2.80)
                + ", coverage 8 times. Gearing helps owners."
            ),
        )
        + practice(
            "7.7",
            "Exam",
            "Debtors and creditors days, with a cash-cycle comment",
            p(
                "Credit sales "
                + rupee(600000)
                + ", opening debtors "
                + rupee(40000)
                + ", closing debtors "
                + rupee(60000)
                + ". "
                "Credit purchases "
                + rupee(360000)
                + ", opening creditors "
                + rupee(30000)
                + ", closing creditors "
                + rupee(50000)
                + ". "
                "Compute debtors turnover, collection period, creditors turnover, payment period (365 days). "
                "Holding period of stock is given as 40 days. Comment on the cash cycle in two sentences."
            ),
            p("Avg debtors = (40,000 + 60,000) ÷ 2 = " + rupee(50000) + ".")
            + p("Debtors turnover = 6,00,000 ÷ 50,000 = 12 times.")
            + p("Collection period = 365 ÷ 12 = 30.416… = 30.42 days.")
            + p("Avg creditors = (30,000 + 50,000) ÷ 2 = " + rupee(40000) + ".")
            + p("Creditors turnover = 3,60,000 ÷ 40,000 = 9 times.")
            + p("Payment period = 365 ÷ 9 = 40.555… = 40.56 days.")
            + p("Cash cycle ≈ 40 + 30.42 − 40.56 = 29.86 days.")
            + p(
                b("Comment. ")
                + "The firm collects in about 30 days and pays in about 41 days, so customers fund themselves 11 days before suppliers are paid. "
                "Adding 40 days of stock, the net cycle is about 30 days of the firm’s own working capital — a manageable cycle, not a trap."
            )
            + p(
                b("Answer. ")
                + "DTO 12 times, ACP 30.42 days, CTO 9 times, APP 40.56 days, cash cycle ≈ 30 days."
            ),
        )
        + practice(
            "7.8",
            "Exam",
            "A different company — pick, compute, comment (do not copy Kaveri)",
            p(
                b("Hemavati Stores Ltd")
                + ", year ended 31 March 2026. Sales "
                + rupee(800000)
                + " (all credit). GP ratio 25%. Opening stock "
                + rupee(50000)
                + ", closing stock "
                + rupee(70000)
                + ". Operating expenses "
                + rupee(80000)
                + ". Interest "
                + rupee(20000)
                + ". Tax "
                + rupee(25000)
                + ". "
                "Equity share capital "
                + rupee(200000)
                + " (₹10 shares), reserves "
                + rupee(100000)
                + ", long-term loan "
                + rupee(200000)
                + ", trade payables "
                + rupee(100000)
                + ". "
                "Closing debtors "
                + rupee(80000)
                + " (opening not given — use closing and state the assumption). Cash "
                + rupee(50000)
                + ". Prepaid nil."
            )
            + p(
                "Compute: COGS, GP, EBIT, PAT, CA, total assets, CE, WC; then current ratio, quick ratio, debt-equity, GP ratio (check), NP ratio, stock turnover, debtors turnover, ROCE, ROE, EPS, interest coverage. "
                "End with a 4-sentence health comment."
            ),
            p(b("Build the figures."))
            + p("GP = 25% × " + rupee(800000) + " = " + rupee(200000) + ". COGS = " + rupee(800000) + " − " + rupee(200000) + " = " + rupee(600000) + ".")
            + p("EBIT = " + rupee(200000) + " − " + rupee(80000) + " = " + rupee(120000) + ".")
            + p("PBT = 1,20,000 − 20,000 = 1,00,000. PAT = 1,00,000 − 25,000 = " + rupee(75000) + ".")
            + p("CA = stock 70,000 + debtors 80,000 + cash 50,000 = " + rupee(200000) + ".")
            + p("SF = 2,00,000 + 1,00,000 = " + rupee(300000) + ". CE = 3,00,000 + 2,00,000 = " + rupee(500000) + ".")
            + p("WC = 2,00,000 − 1,00,000 = " + rupee(100000) + ".")
            + p("FA = CE − WC = 5,00,000 − 1,00,000 = " + rupee(400000) + ". TA = FA + CA = 4,00,000 + 2,00,000 = " + rupee(600000) + ".")
            + p("Check BS: SF 3,00,000 + LTD 2,00,000 + CL 1,00,000 = 6,00,000 = TA.")
            + p(b("Ratios."))
            + p("Current = 2,00,000/1,00,000 = 2 : 1. Quick = (2,00,000 − 70,000)/1,00,000 = 1.3 : 1.")
            + p("Debt-equity = 2,00,000/3,00,000 = 0.67 : 1.")
            + p("GP ratio given 25% (check: 2,00,000/8,00,000 × 100 = 25%). NP = 75,000/8,00,000 × 100 = 9.375%.")
            + p("Avg stock = (50,000 + 70,000) ÷ 2 = 60,000. Stock turnover = 6,00,000/60,000 = 10 times. Holding = 365/10 = 36.5 days.")
            + p("Debtors turnover (closing used as proxy): 8,00,000/80,000 = 10 times. Collection = 36.5 days. Assumption written.")
            + p("ROCE = 1,20,000/5,00,000 × 100 = 24%. ROE = 75,000/3,00,000 × 100 = 25%.")
            + p("Shares = 2,00,000/10 = 20,000. EPS = 75,000/20,000 = " + rupee(3.75) + ".")
            + p("Interest coverage = 1,20,000/20,000 = 6 times.")
            + p(
                b("Health comment. ")
                + "Hemavati is liquid (current 2 : 1, quick 1.3 : 1). Solvency is moderate rather than conservative — debt-equity 0.67 is still under 1 and interest is covered 6 times, so the extra debt is serviceable. "
                "Profitability is strong: GP 25%, net 9.4%, ROCE 24% (well above the 10% coupon on the loan) and ROE 25%, which is slightly above ROCE-after-tax and shows gearing helping owners. "
                "Efficiency is brisk — stock and debtors both turn 10 times (36.5 days) — and EPS is ₹3.75. "
                "Watch-out: opening debtors were not given, so collection days rest on a closing-only assumption; and a 0.67 debt-equity leaves less unused debt capacity than Kaveri had. Overall, a profitable, liquid trader using moderate gearing well."
            ),
        )
        + practice(
            "7.9",
            "Easy",
            "Identify the ratio",
            p("Name the ratio (and the bucket) for each trigger:")
            + ol(
                [
                    "The paper gives CA, CL and asks “short-term solvency”.",
                    "The paper uses the words “acid test”.",
                    "“Overall profitability of long-term funds”.",
                    "“How quickly stock sells”.",
                    "GP 25% of sales, find leftover after COGS as a %.",
                    "PAT, 50,000 shares, preference dividend nil.",
                    "EBIT ₹1,50,000, interest ₹30,000, “ability to pay interest”.",
                    "Current ratio 2.5 and WC ₹1,50,000, find CA.",
                ]
            ),
            ol(
                [
                    "Current ratio — BS / liquidity.",
                    "Quick ratio — BS / liquidity.",
                    "ROCE = EBIT/CE — Combined / profitability.",
                    "Inventory turnover (COGS/avg stock) — Combined / efficiency.",
                    "GP ratio — Revenue / profitability.",
                    "EPS — Combined / profitability per share.",
                    "Interest coverage — Combined (solvency companion) / 5 times if the figures are Kaveri’s.",
                    "Reconstruction Type A: CL = 1,00,000, CA = 2,50,000.",
                ]
            ),
        )
    )


def _theory() -> str:
    return (
        h2("16. Theory questions (write these from memory)", "theory")
        + qna(
            "What is ratio analysis? Explain its need and importance. (8 marks)",
            exam_answer(
                "Ratio analysis is the computation, comparison and interpretation of arithmetical relationships between figures in the financial statements. "
                "It is needed because raw rupee totals of two years or two firms cannot be compared when size differs. "
                "Importance: (1) intra-firm trend comparison, (2) inter-firm benchmarking, (3) diagnosis of liquidity, solvency, profitability and efficiency, "
                "(4) simplification of bulky statements into a few indicators, (5) help to management for control, (6) help to lenders and investors for credit and investment decisions, "
                "(7) a base for forecasting. Ratios must be read against a benchmark and with their limitations."
            ),
            "8",
        )
        + qna(
            "State the limitations of ratio analysis. (8 marks)",
            exam_answer(
                "Ratios use historical data and may not continue. Management may window-dress year-end figures. "
                "Different accounting policies (stock, depreciation) destroy comparability. A ratio has no meaning in isolation and needs a benchmark. "
                "Qualitative factors are ignored. Inflation mixes old costs with current revenues. Year-end figures may be seasonal. "
                "A ratio identifies a symptom, not a cause. Therefore ratios must be read together, over several years, with notes and cash-flow information."
            ),
            "8",
        )
        + qna(
            "Classify ratios as Balance Sheet, Revenue and Combined, with two examples of each. (5 marks)",
            exam_answer(
                "Classification is by the source of the two figures. Balance Sheet ratios use two BS positions — e.g. current ratio, debt-equity. "
                "Revenue ratios use two P&L flows — e.g. gross profit ratio, operating ratio. "
                "Combined ratios use one flow and one position — e.g. inventory turnover, ROCE. "
                "This is different from the purpose classification into liquidity, solvency, profitability and efficiency."
            ),
            "5",
        )
        + qna(
            "Distinguish between current ratio and quick ratio. (5 marks)",
            exam_answer(
                "Both are Balance Sheet liquidity ratios with current liabilities in the denominator. "
                "Current ratio uses all current assets, including inventory and prepaid, and has a conventional ideal of 2 : 1. "
                "Quick (acid-test) ratio uses only quick assets = CA − inventory − prepaid, and has a conventional ideal of 1 : 1. "
                "Current ratio trusts stock; the acid test does not, because stock may be slow or overvalued and prepaid will not pay a creditor. "
                "A firm can look liquid on the current ratio and illiquid on the quick ratio when most CA is stock."
            ),
            "5",
        )
        + qna(
            "Distinguish between ROCE and ROE. (5 marks)",
            exam_answer(
                "ROCE = EBIT / Capital employed × 100. It is the return on the whole long-term pool (equity + long-term debt), before interest and tax, and is used to compare firms with different gearing. "
                "ROE = PAT / Equity shareholders’ funds × 100. It is the return on owners’ money only, after interest and tax. "
                "Matching rule: whoever is in the denominator must not already have been paid in the numerator. "
                "ROCE answers “how well did the business use long-term funds?”. ROE answers “how well did owners do?”. "
                "If ROE exceeds after-tax ROCE, gearing is helping owners; the reverse means gearing is hurting."
            ),
            "5",
        )
        + qna(
            "Operating ratio and operating profit ratio. (5 marks)",
            exam_answer(
                "Both are Revenue ratios with sales in the denominator. Operating ratio = operating cost / sales × 100, where operating cost = COGS + operating expenses (interest and tax excluded). "
                "Operating profit ratio = EBIT / sales × 100. They are cost and profit twins: when other income is nil, they add to 100%. "
                "A rising operating ratio is a cost warning; a rising operating profit ratio is an operations improvement. "
                "A common error is to include interest in operating cost, which breaks the 100% identity."
            ),
            "5",
        )
        + qna(
            "What is capital gearing? When is a firm said to be high geared? (5 marks)",
            exam_answer(
                "Capital gearing is the mix of fixed-charge funds (preference share capital + long-term debt) and equity shareholders’ funds. "
                "In the common MBA version, capital gearing = (preference + LTD) / equity funds. A firm is high geared when this ratio exceeds 1 (fixed-charge funds exceed equity) "
                "and low geared when it is less than 1. High gearing magnifies equity earnings in good years and magnifies losses in bad years. "
                "If the paper prints the inverted formula, high/low follows that formula — always read the printed version."
            ),
            "5",
        )
        + qna(
            "Why is COGS preferred to sales in stock turnover? (3 marks)",
            exam_answer(
                "Inventory is valued at cost. COGS is also at cost. Dividing a cost flow by a cost stock is consistent. "
                "Sales are at selling price; Sales / average stock mixes two valuations and overstates turnover by the GP margin. "
                "Use the sales version only when the paper prints it or when COGS cannot be built."
            ),
            "3",
        )
        + connect(
            "You now have the full analytical toolkit of this paper: the statements (Ch 4, Ch 6), the cash-flow story (Ch 5), and the ratio language (this chapter). "
            "In the exam, a 20-mark analysis question is almost always: compute a short set, then write the four-beat comment (liquidity, solvency, profitability, efficiency) plus one watch-out. "
            "That is the whole chapter, used as a professional uses it."
        )
    )







