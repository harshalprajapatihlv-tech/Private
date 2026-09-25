#!/usr/bin/env python3
"""Chapter 3 — Depreciation. Beginner-to-exam teaching notes (Indian MBA)."""

from __future__ import annotations

import sys

sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(
        chapter_open(
            "03",
            "Depreciation",
            "You will be able to explain what depreciation is (and what it is not), "
            "state why it is provided, compute it under the Straight Line Method and "
            "the Written Down Value Method — including part-year charges, a second "
            "asset, and sale — pass the journals, and present the asset in the "
            "Profit & Loss Account and the Balance Sheet, as expected in an Indian MBA exam.",
            [
                "Meaning of depreciation",
                "Reasons for providing depreciation",
                "Straight Line Method (SLM)",
                "Written Down Value Method (WDV)",
                "Numerical problems (part-year, installation, sale, comparison)",
            ],
        )
    )
    parts.append(_words())
    parts.append(_meaning())
    parts.append(_why_provide())
    parts.append(_causes())
    parts.append(_cost_of_asset())
    parts.append(_accounting())
    parts.append(_slm())
    parts.append(_wdv())
    parts.append(_comparison())
    parts.append(_provision_vs_asset())
    parts.append(_identify_mistakes_memory())
    parts.append(_practice())
    parts.append(_formula_sheet())
    parts.append(_theory_qna())
    parts.append(chapter_close())
    return "".join(parts)


# ---------------------------------------------------------------------------
# Tiny glossary
# ---------------------------------------------------------------------------
def _words() -> str:
    return (
        h2("Before you open a numerical — the words", "words")
        + lead(
            "Every depreciation question is built from six words. If you can name "
            "them on a blank page, the arithmetic becomes a recipe, not a puzzle."
        )
        + table(
            ["Word you will see", "What it actually means", "Exam alias"],
            [
                [
                    "Cost / original cost",
                    "What the business spent to bring the asset to working condition "
                    "(purchase + installation + freight + non-refundable taxes, minus trade discount).",
                    "Gross block, invoice price + extras",
                ],
                [
                    "Residual / scrap / salvage",
                    "Estimated amount we expect to recover at the end of useful life, after selling or scrapping the asset.",
                    "Scrap value, residual value",
                ],
                [
                    "Useful life",
                    "The period (usually in years) over which the business will use the asset.",
                    "Life, estimated life, n years",
                ],
                [
                    "Depreciable amount",
                    "Cost minus residual. This is the bundle of cost that must be expensed over the life.",
                    "Amount to be written off",
                ],
                [
                    "WDV / NBV / book value",
                    "Cost minus accumulated depreciation so far. The unexpired cost still sitting on the Balance Sheet.",
                    "Written down value, net book value, carrying amount",
                ],
                [
                    "Accumulated depreciation",
                    "The running total of depreciation charged from the date of purchase up to today. A contra-asset, not cash.",
                    "Provision for depreciation",
                ],
            ],
            caption="Six words that unlock every depreciation question",
        )
        + keypoint(
            "Depreciation is an <strong>allocation of cost already spent</strong>. "
            "It is not a valuation of the asset at today’s market price, and it is "
            "not cash leaving the business this year."
        )
    )


# ---------------------------------------------------------------------------
# Meaning
# ---------------------------------------------------------------------------
def _meaning() -> str:
    return (
        h2("1. Meaning of depreciation", "meaning")
        + definition(
            "Depreciation is the <strong>systematic allocation of the depreciable amount "
            "of a tangible fixed asset over its useful life</strong>. "
            "Depreciable amount = Cost − Residual (scrap) value. "
            "We charge this allocation as an expense of each year that enjoyed the asset’s services."
        )
        + simple(
            "You buy a delivery van for "
            + rupee(500000)
            + " and you will use it for 5 years. You did not “lose” "
            + rupee(500000)
            + " in year 1. You prepaid for five years of deliveries. Each year you "
            "expense a portion of that prepaid bundle. That portion is depreciation. "
            "No cash goes to the garage, the bank, or the owner when you pass the "
            "depreciation entry — the cash already left on the day you bought the van."
        )
        + why(
            "Without depreciation, year 1 would swallow the whole cost (profit would look terrible) "
            "and years 2–5 would ride free (profit would look fake). Depreciation spreads the cost "
            "so that each year is charged with the services it used. That is the matching concept."
        )
        + real_life(
            "A café buys an espresso machine for "
            + rupee(120000)
            + ". It will steam milk for about 6 years and then be sold as scrap for "
            + rupee(12000)
            + ". The café is not poorer by "
            + rupee(120000)
            + " on day one. It is poorer, each year, by the slice of machine-life that year consumed. "
            "Depreciation is the name of that slice."
        )
        + logic(
            "The accounting equation is Assets = Liabilities + Capital. "
            "When you buy the van with cash, one asset (van) replaces another (bank) — capital is unchanged. "
            "As the van is used, part of that asset is consumed. We reduce the asset (or raise a contra-asset) "
            "and reduce profit (which reduces capital). The business is honestly smaller by the cost consumed, "
            "not by a cash payment that never happened this year."
        )
        + exam_answer(
            "Depreciation is a non-cash expense representing the expired cost of a tangible fixed asset. "
            "It is charged to the Profit and Loss Account so that profit is not overstated, and deducted "
            "from the asset (directly or through accumulated depreciation) so that the Balance Sheet does "
            "not show the asset at a cost that has already been used up. It is not the same thing as a "
            "fall in market price: a building may rise in the property market and we still depreciate it, "
            "because we are allocating historical cost, not marking the asset to market."
        )
        + warn(
            "Three sentences students write that examiners cross out: "
            "(1) “Depreciation is cash paid for wear and tear.” — No cash is paid. "
            "(2) “Depreciation is the fall in market price of the asset.” — Not the definition; market may even rise. "
            "(3) “Accumulated depreciation is money kept aside to replace the asset.” — It is only a contra-asset "
            "on paper, unless the business separately invests cash in a replacement fund."
        )
        + connect(
            "In the Cash Flow Statement (later chapter) you will <strong>add depreciation back</strong> "
            "to net profit while computing cash from operations. That is because profit was reduced by a "
            "non-cash expense. If you treat depreciation as an outflow there, you double-count a payment "
            "that already happened when the asset was purchased. Remember the slogan: "
            "<em>depreciation is in the P&L; it is not in this year’s cash.</em>"
        )
    )


# ---------------------------------------------------------------------------
# Why provide
# ---------------------------------------------------------------------------
def _why_provide() -> str:
    reasons = [
        (
            "To show true profit (matching)",
            "The year that used the machine must bear a share of its cost. "
            "If we skip depreciation, profit is overstated. Owners may then withdraw or distribute "
            "cash that is not really “earned”. Matching concept: expenses of a period against revenue of that period.",
        ),
        (
            "To show a true asset value (not overstated)",
            "A three-year-old van is not worth its original cost on the Balance Sheet. "
            "We show cost less accumulated depreciation = net book value. "
            "This is still not market value — it is unexpired cost — but it is not a lie that the whole cost is still “there”.",
        ),
        (
            "Replacement-funds idea — with the common confusion named",
            "By charging depreciation we retain that amount of profit inside the business "
            "(we do not declare it as fully available). Over the life, retained earnings plus the "
            "reduced book value keep the accounting equation in balance. "
            "<strong>But accounting does not physically set cash aside.</strong> "
            "The cash from sales sits in the bank and can be spent on anything — inventory, salaries, dividends — "
            "unless management separately creates a <em>depreciation fund</em> and invests it. "
            "Most businesses do not. So: depreciation helps <em>in principle</em> to retain resources for replacement; "
            "it does <em>not</em> create a locked cash box.",
        ),
        (
            "Legal / true and fair view",
            "Under the Companies Act, 2013, financial statements must give a true and fair view. "
            "Schedule II indicates useful lives for companies. Skipping depreciation would overstate "
            "profit and assets — not true and fair. For MBA theory, write: “Depreciation is necessary "
            "to present a true and fair view of profit and of the financial position.”",
        ),
        (
            "The cost is a prepaid bundle of services",
            "A machine is not one day’s expense. It is a packet of future services bought in advance. "
            "Depreciation is how we open that packet, year by year. "
            "This is the same logic as prepaid insurance: you do not expense 3 years of premium in January of year 1.",
        ),
    ]
    rows = [[b(title), body] for title, body in reasons]
    return (
        h2("2. Why do we provide depreciation?", "why-provide")
        + why(
            "We provide depreciation for five interlocking reasons. Learn them as a 5-mark theory answer, "
            "not as a list you half-remember. The examiner wants the matching idea, the Balance Sheet idea, "
            "and the honesty that a “fund” is not automatic."
        )
        + table(
            ["Reason", "What to write in the exam"],
            rows,
            caption="Five reasons for providing depreciation (theory favourite)",
        )
        + exam_answer(
            "Depreciation is provided: (i) to ascertain true profit by matching the expired cost of the asset "
            "against the revenue of the period; (ii) to state assets at a true (unexpired) amount in the "
            "Balance Sheet rather than at original cost; (iii) to retain a portion of profit in the business "
            "which, in principle, is available towards replacement — though a separate invested fund is created "
            "only if management so decides; (iv) to comply with the true-and-fair requirement of company law; "
            "and (v) because the cost of a fixed asset is a prepaid bundle of services that must be allocated "
            "over the years that receive those services."
        )
        + memory(
            "Five fingers: <strong>Profit, Picture, Piggy-bank (optional), Police (law), Prepaid services.</strong> "
            "Profit = matching. Picture = Balance Sheet. Piggy-bank = replacement idea, cash not auto-locked. "
            "Police = Companies Act / true and fair. Prepaid = the asset is a bundle of future uses."
        )
    )


# ---------------------------------------------------------------------------
# Causes
# ---------------------------------------------------------------------------
def _causes() -> str:
    return (
        h2("3. Why depreciation occurs — the physical and economic causes", "causes")
        + simple(
            "Section 2 answered “why we <em>record</em> it”. This section answers “why the asset "
            "<em>loses service potential</em>”. Examiners ask both. Do not mix them up."
        )
        + table(
            ["Cause", "What is happening", "Typical assets", "One-line example"],
            [
                [
                    "Wear and tear",
                    "Physical use: friction, running hours, kilometres, copies printed.",
                    "Vehicles, plant, furniture",
                    "A delivery van’s engine after 80,000 km is not the engine you bought.",
                ],
                [
                    "Passage of time (effluxion of time)",
                    "Even an unused asset can expire: patents of time, leases, rust, weather.",
                    "Leasehold, buildings, seasonal plant left idle",
                    "A 9-year lease has 8 years left on 1 April next year whether you used the shop or not.",
                ],
                [
                    "Obsolescence",
                    "A better, cheaper, or legally required substitute arrives. The old asset is outdated, not necessarily broken.",
                    "Computers, phones, specialised machinery",
                    "A 5-year-old billing server still switches on; the business has moved to the cloud.",
                ],
                [
                    "Depletion",
                    "Extraction of a wasting resource. The “asset” is physically removed.",
                    "Mines, oil wells, quarries, timber tracts",
                    "Every tonne of ore taken out of the mine is a tonne that is gone.",
                ],
                [
                    "Accident / abnormal damage",
                    "Fire, flood, crash, beyond ordinary wear. Often written down immediately, not dribbled over remaining life.",
                    "Any tangible asset",
                    "A forklift dropped from a trailer is not “this year’s 10% WDV” — it may be a loss on write-off.",
                ],
            ],
            caption="Causes of depreciation (do not confuse with ‘reasons for providing’)",
            foot="Depletion is the word used for mines and wells; amortisation is the cousin-word used for intangible assets "
            "(patents, goodwill). Depreciation, in the strict exam sense, is for tangible fixed assets other than wasting assets.",
        )
        + keypoint(
            "<strong>Land is generally not depreciated</strong> — it has an unlimited useful life "
            "(the site does not get “used up”). The <em>building</em> on the land is depreciated. "
            "A mine is not “land” in this sense; a mine is depleted. If an MCQ says “which of the following "
            "is not depreciated?”, the answer is almost always freehold land."
        )
        + identify(
            "If the question says “state the causes of depreciation” → wear and tear, time, obsolescence, "
            "depletion, accident (the table above). "
            "If it says “state the reasons for providing depreciation” → true profit, true asset value, "
            "replacement idea, legal/true and fair, prepaid bundle (Section 2). "
            "Two different questions. Two different lists."
        )
    )


# ---------------------------------------------------------------------------
# Cost of the asset
# ---------------------------------------------------------------------------
def _cost_of_asset() -> str:
    return (
        h2("4. What is “cost”? (before any method)", "cost")
        + definition(
            "For depreciation, <strong>cost</strong> is the amount spent to acquire the asset and bring it "
            "to the location and condition necessary for it to be used. Residual value is an estimate of "
            "what will come back at the end. Neither figure is “the invoice alone” unless the question is that simple."
        )
        + format_box(
            "Cost of a tangible fixed asset",
            ul(
                [
                    "Purchase price (after trade discount; cash discount is usually a finance item, not a cut in cost)",
                    "+ Freight / carriage inward / transit insurance",
                    "+ Installation, erection, commissioning, trial-run costs (until ready for use)",
                    "+ Non-refundable taxes and duties",
                    "− Refundable GST / CENVAT (if the business can claim it input)",
                    "= <strong>Cost to capitalise</strong> — this is the figure you depreciate from",
                ]
            )
            + p(
                "Depreciation starts from the date the asset is ",
                b("put to use"),
                ", not merely the date of placing the order. "
                "If bought on 1 September and installed on 1 October, count from 1 October.",
            ),
        )
        + exam_tip(
            "“Installation ₹20,000” is not an expense of the year. Add it to cost. "
            "“Scrap 10% of cost” means 10% of this total cost, unless the question says 10% of purchase price. "
            "When in doubt, cost = all amounts spent to make the asset ready."
        )
        + example(
            "0",
            "Easy",
            "Build the cost figure before you touch a rate",
            p("Invoice price of a machine ", rupee(500000), ". Freight ", rupee(8000), ". Installation ", rupee(12000), ". Refundable GST ", rupee(90000), " (claimable). Scrap estimated at 10% of cost. Life 10 years. SLM.")
            + ol(
                [
                    "Cost = 5,00,000 + 8,000 + 12,000 = "
                    + rupee(520000)
                    + ". GST is refundable, so it is <em>not</em> added.",
                    "Scrap = 10% of "
                    + rupee(520000)
                    + " = "
                    + rupee(52000)
                    + ".",
                    "Depreciable amount = 5,20,000 − 52,000 = "
                    + rupee(468000)
                    + ".",
                    "Annual SLM depreciation = 4,68,000 ÷ 10 = "
                    + rupee(46800)
                    + ".",
                ]
            )
            + keypoint(
                "If you depreciate ₹5,00,000 and ignore installation, every later number is wrong. "
                "Cost is step zero of every numerical in this chapter."
            ),
        )
    )


# ---------------------------------------------------------------------------
# Accounting treatment
# ---------------------------------------------------------------------------
def _accounting() -> str:
    return (
        h2("5. Accounting treatment — journal, P&L, Balance Sheet", "accounting")
        + definition(
            "Recording depreciation means: (i) recognise an <strong>expense</strong> for the year, which reduces profit; "
            "and (ii) reduce the asset’s net book value, either by crediting the asset directly or by crediting "
            "a contra-asset called Accumulated Depreciation (also called Provision for Depreciation)."
        )
        + simple(
            "Two things move, and cash is not one of them. Expense goes up → profit goes down. "
            "Net book value of the asset goes down. Bank is untouched."
        )
        + logic(
            "Debit the expense (Depreciation Account) because expenses are debited. "
            "Credit Accumulated Depreciation (or the Asset) because that credit shrinks the net asset. "
            "Then close Depreciation Account to Profit and Loss — so the year’s profit bears the charge. "
            "MBA exams usually prefer the accumulated-depreciation (provision) method, because the Balance Sheet "
            "can then show cost and accumulated depreciation separately. Both methods are taught below."
        )
        + format_box(
            "The two journal entries every year (provision method)",
            journal(
                [
                    {
                        "date": "31 Mar",
                        "debit": "Depreciation A/c",
                        "credit": "Accumulated Depreciation A/c",
                        "amount": "xx",
                        "narration": "Being depreciation charged for the year",
                    },
                    {
                        "date": "31 Mar",
                        "debit": "Profit and Loss A/c",
                        "credit": "Depreciation A/c",
                        "amount": "xx",
                        "narration": "Being depreciation transferred to Profit and Loss Account",
                    },
                ],
                caption="Year-end recording and closing (provision / accumulated depreciation method)",
            )
            + p(
                "Some solutions skip the Depreciation Account and write a single entry: "
                "Profit and Loss A/c Dr. &nbsp; To Accumulated Depreciation A/c. "
                "Either form is accepted if the amounts and the two effects (expense + contra-asset) are clear."
            ),
        )
        + format_box(
            "Where it appears in the statements",
            p(b("Statement of Profit and Loss"), " (extract)")
            + table(
                ["Particulars", "₹"],
                [
                    ["Depreciation and amortisation expense", "18,000"],
                ],
                caption="P&L — depreciation is an operating expense, not a cash payment",
            )
            + p(b("Balance Sheet"), " (extract) — Companies Act vertical idea, asset side")
            + table(
                ["Particulars", "₹", "₹"],
                [
                    ["<strong>Non-current assets</strong>", "", ""],
                    ["Property, plant and equipment", "", ""],
                    ["Machinery (at cost)", "1,00,000", ""],
                    ["Less: Accumulated depreciation", "18,000", "82,000"],
                ],
                caption="Asset at cost less accumulated depreciation = net book value",
                foot="If the book charges depreciation directly to the asset, the Balance Sheet shows only the WDV figure (₹82,000) and the original cost is not visible. Examiners prefer the “at cost less accumulated depreciation” presentation.",
            ),
        )
        + steps(
            [
                "Compute the year’s depreciation under the method named in the question (SLM or WDV), for the months the asset was used.",
                "Pass: Depreciation A/c Dr. &nbsp; To Accumulated Depreciation A/c (or To Asset A/c).",
                "Close Depreciation A/c to Profit and Loss A/c.",
                "In the Balance Sheet, show Gross Block (cost) minus Accumulated Depreciation = Net Block (NBV).",
                "If the asset is sold during the year: first charge depreciation up to the date of sale, then remove cost and accumulated depreciation, then recognise profit or loss on sale.",
            ]
        )
        + two_col(
            t_account(
                "Depreciation A/c",
                [("To Accumulated Depreciation A/c", "18,000")],
                [("By Profit and Loss A/c", "18,000")],
            ),
            t_account(
                "Accumulated Depreciation A/c",
                [("To Balance c/d", "18,000")],
                [("By Depreciation A/c", "18,000")],
                cr_bal="",
            ),
        )
        + p(
            "The Depreciation Account is a ",
            b("nominal account"),
            " — it opens at zero, collects the year’s charge, and is emptied into P&L. "
            "The Accumulated Depreciation Account is a ",
            b("contra-asset"),
            " — it lives on from year to year, growing until the asset is sold or fully written off. "
            "It is not a pile of cash.",
        )
    )


# ---------------------------------------------------------------------------
# SLM
# ---------------------------------------------------------------------------
def _slm() -> str:
    return (
        h2("6. Straight Line Method (SLM)", "slm")
        + definition(
            "Under the Straight Line Method (also called the Original Cost Method or the Fixed Instalment Method), "
            "a <strong>constant amount</strong> of depreciation is charged every full year. "
            "The line of remaining book value, plotted against time, is a straight line falling from cost to scrap."
        )
        + simple(
            "Take the amount that will die (cost minus scrap), cut it into equal yearly slices, "
            "and serve one slice each year. Year 1’s slice = year 5’s slice. "
            "If you owned the asset for only part of a year, serve a matching fraction of the slice."
        )
        + why(
            "SLM is simple, and it is fair when the asset gives roughly equal service every year — "
            "buildings, furniture, patents of time, a lease. It is a poor fit for assets that collapse in "
            "usefulness in the first years (phones, laptops), which is why WDV exists."
        )
        + real_life(
            "A shop’s display counters cost "
            + rupee(100000)
            + ", will be used 5 years, and will fetch "
            + rupee(10000)
            + " as scrap. Every year the shop “uses up” "
            + rupee(18000)
            + " of counter. Customers see the same counters in year 1 and year 4 — equal service, equal charge."
        )
        + logic(
            "Depreciable amount is a finite pie. SLM assumes each year eats an equal piece of the pie. "
            "When the years are done, the pie is gone and only scrap remains. "
            "That is why, if residual and life are honoured, WDV at the end of life equals scrap — exactly."
        )
        + formula(
            "Annual depreciation = (Cost − Residual) ÷ Useful life in years",
            "Rate on original cost = (Annual depreciation ÷ Cost) × 100. "
            "Part-year depreciation = Annual depreciation × (months used ÷ 12). "
            "The rate is always applied to original cost, never to the falling WDV.",
        )
        + format_box(
            "Depreciation schedule (keep four columns every time)",
            table(
                ["Year / FY", "Depreciation for the year (₹)", "Accumulated depreciation (₹)", "WDV / NBV at year-end (₹)"],
                [
                    ["Opening (date put to use)", "—", "0", "Cost"],
                    ["Year 1", "same each full year", "running total", "Cost − accum."],
                    ["…", "…", "…", "…"],
                    ["Last year of life", "last slice (maybe a stub period)", "Cost − Residual", "Residual"],
                ],
                caption="The four-column schedule that stops most SLM mistakes",
            ),
        )
        + steps(
            [
                "Build cost (add installation, freight; exclude refundable tax).",
                "Read residual. If “10% of cost”, compute 10% of the cost you just built.",
                "Depreciable amount = Cost − Residual.",
                "Annual depreciation = Depreciable amount ÷ life in years. Show the division.",
                "Rate % (if asked) = (Annual depreciation ÷ Cost) × 100. This rate is on original cost.",
                "Count months from date put to use to the accounting year-end. Indian FY: 1 April to 31 March. "
                "1 October → 6 months; 1 July → 9 months; 1 January → 3 months; 1 April → 12 months.",
                "First year (and last year, and year of sale) = Annual × months/12. Intervening years = full annual amount.",
                "Useful life is a clock starting on the date put to use, not “n financial years”. "
                "A 4-year life from 1 July 2023 ends on 30 June 2027 — there will be a 3-month stub in FY 2027–28.",
                "Fill the schedule. Check: last WDV = residual (if you have charged the full life).",
            ]
        )
        + _slm_easy()
        + _slm_moderate()
        + _slm_exam()
        + identify(
            "Use SLM when the question says any of: <strong>straight line, original cost method, "
            "equal instalment, fixed instalment, equal amount each year, rate % per annum on cost / on original cost</strong>. "
            "If it gives life and residual and is silent on the method, many Indian MBA papers still expect SLM — "
            "but if a WDV rate is printed, that wins. Never apply an SLM rate to the falling book value."
        )
        + mistakes(
            [
                "Applying the SLM rate to WDV in year 2 onwards. The rate is on original cost. Every full year the rupee charge is identical.",
                "Forgetting to add installation / freight to cost, then taking scrap as 10% of the invoice only.",
                "Charging a full year when the asset was put to use on 1 October (that is 6/12, not 12/12).",
                "Treating “life 4 years” as four financial years when the asset arrived on 1 July — you will miss the 3-month stub and will not land on scrap.",
                "Stopping depreciation in the year of sale. You must charge up to the date of sale, then compute profit or loss on the NBV of that date.",
                "Writing residual off every year. Residual is subtracted <em>once</em>, when you compute the annual slice.",
            ]
        )
        + memory(
            "SLM = <strong>Same Load every year</strong>, like equal slices of a cake. "
            "The cake is (Cost − Scrap). The number of slices is the life. "
            "A part-year is a part-slice. At the end of the last slice you are staring at scrap."
        )
    )


def _slm_easy() -> str:
    body = (
        p(
            b("Given. "),
            "Cost ",
            rupee(100000),
            ", scrap ",
            rupee(10000),
            ", useful life 5 years. Method: SLM. Prepare a 5-year schedule and the rate of depreciation.",
        )
        + h4("Step 1 — depreciable amount and annual charge")
        + p("Depreciable amount = Cost − Scrap = 1,00,000 − 10,000 = ", rupee(90000), ".")
        + p("Annual depreciation = 90,000 ÷ 5 = ", rupee(18000), " every full year.")
        + p(
            "Rate on original cost = (18,000 ÷ 1,00,000) × 100 = ",
            b("18%"),
            ". Check: 1,00,000 × 18% = 18,000, but remember this 18% is ",
            i("not"),
            " applied to the falling WDV — we only used cost to find the rate.",
        )
        + h4("Step 2 — the schedule (show every year’s arithmetic)")
        + table(
            ["Year", "Opening WDV (₹)", "Depreciation (₹)", "Accumulated dep. (₹)", "Closing WDV (₹)"],
            [
                ["1", "1,00,000", "18,000", "18,000", "82,000"],
                ["2", "82,000", "18,000", "36,000", "64,000"],
                ["3", "64,000", "18,000", "54,000", "46,000"],
                ["4", "46,000", "18,000", "72,000", "28,000"],
                ["5", "28,000", "18,000", "90,000", "10,000"],
            ],
            caption="SLM schedule — charge is identical every year; WDV falls in a straight line",
            foot="Closing WDV of year 5 = ₹10,000 = scrap. If this check fails, a year’s arithmetic is wrong.",
        )
        + p("How the WDV column is built (year 1 as a model): 1,00,000 − 18,000 = 82,000. Year 2: 82,000 − 18,000 = 64,000. And so on.")
        + p("Accumulated depreciation of year 3 = 18,000 × 3 = ", rupee(54000), ". Closing WDV = 1,00,000 − 54,000 = ", rupee(46000), ".")
        + h4("Step 3 — journals of year 1 (provision method)")
        + journal(
            [
                {
                    "date": "31 Mar Yr 1",
                    "debit": "Depreciation A/c",
                    "credit": "Accumulated Depreciation A/c",
                    "amount": "18,000",
                    "narration": "Being SLM depreciation for the year at 18% on original cost",
                },
                {
                    "date": "31 Mar Yr 1",
                    "debit": "Profit and Loss A/c",
                    "credit": "Depreciation A/c",
                    "amount": "18,000",
                    "narration": "Being depreciation transferred to Profit and Loss Account",
                },
            ],
            caption="Year 1 journals — years 2 to 5 use the same amounts under SLM",
        )
        + h4("Step 4 — Balance Sheet extract, end of year 3")
        + table(
            ["Particulars", "₹", "₹"],
            [
                ["Machinery (at cost)", "1,00,000", ""],
                ["Less: Accumulated depreciation (18,000 × 3)", "54,000", "46,000"],
            ],
            caption="After 3 years the asset is not shown at ₹1,00,000 and not at market value — at unexpired cost ₹46,000",
        )
    )
    return example("1", "Easy", "SLM from cost, scrap and life — the master template", body)


def _slm_moderate() -> str:
    body = (
        p(
            b("Given. "),
            "Plant purchased on ",
            b("1 July 2023"),
            " for ",
            rupee(240000),
            ". Residual ",
            rupee(24000),
            ". Useful life ",
            b("4 years"),
            ". Books close on ",
            b("31 March"),
            " (Indian financial year). Method: SLM. Compute depreciation for each financial year until the asset is fully depreciated down to scrap.",
        )
        + h4("Step 1 — annual slice")
        + p("Depreciable amount = 2,40,000 − 24,000 = ", rupee(216000), ".")
        + p("Annual depreciation = 2,16,000 ÷ 4 = ", rupee(54000), ".")
        + p("Depreciation per month = 54,000 ÷ 12 = ", rupee(4500), ".")
        + h4("Step 2 — the life is a clock, not “four FYs”")
        + p(
            "Put to use: 1 July 2023. Life of 4 years ends on ",
            b("30 June 2027"),
            ". Total months of service = 4 × 12 = ",
            b("48 months"),
            ". 48 × 4,500 = ",
            rupee(216000),
            " — the whole depreciable amount.",
        )
        + p(
            "FY 2023–24 (1 July 2023 to 31 March 2024) = July, August, September, October, November, December, January, February, March = ",
            b("9 months"),
            ".",
        )
        + p("Year-1 depreciation = 54,000 × 9/12.")
        + p("54,000 × 9 = 4,86,000.")
        + p("4,86,000 ÷ 12 = ", rupee(40500), ".")
        + p("Or: 4,500 × 9 = ", rupee(40500), ".")
        + h4("Step 3 — every financial year until the clock hits 48 months")
        + table(
            ["Financial year", "Months used", "Working", "Depreciation (₹)", "Accum. dep. (₹)", "Closing WDV (₹)"],
            [
                ["2023–24 (from 1 Jul)", "9", "54,000 × 9/12", "40,500", "40,500", "1,99,500"],
                ["2024–25", "12", "full year", "54,000", "94,500", "1,45,500"],
                ["2025–26", "12", "full year", "54,000", "1,48,500", "91,500"],
                ["2026–27", "12", "full year", "54,000", "2,02,500", "37,500"],
                ["2027–28 (to 30 Jun)", "3", "54,000 × 3/12", "13,500", "2,16,000", "24,000"],
            ],
            caption="Part-year first, full years in the middle, stub year at the end — WDV lands on scrap",
            foot="Check the months: 9 + 12 + 12 + 12 + 3 = 48. Check the rupees: 40,500 + 54,000 + 54,000 + 54,000 + 13,500 = 2,16,000. Check the WDV: 2,40,000 − 2,16,000 = 24,000 = residual.",
        )
        + p("Last-year working, shown fully: 54,000 × 3/12 = (54,000 × 3) ÷ 12 = 1,62,000 ÷ 12 = ", rupee(13500), ".")
        + p("Closing WDV after FY 2023–24: 2,40,000 − 40,500 = ", rupee(199500), ".")
        + p("After FY 2024–25: 1,99,500 − 54,000 = ", rupee(145500), ".")
        + p("After FY 2025–26: 1,45,500 − 54,000 = ", rupee(91500), ".")
        + p("After FY 2026–27: 91,500 − 54,000 = ", rupee(37500), ".")
        + p("After the 3-month stub: 37,500 − 13,500 = ", rupee(24000), " = scrap. The clock has run out.")
        + warn(
            "A very common wrong answer is to charge ₹40,500 + three full years of ₹54,000 and stop "
            "(total 9 + 36 = 45 months). That leaves ₹13,500 of depreciable amount hanging, and WDV would be "
            "₹37,500 instead of scrap ₹24,000. Life is measured from the date put to use."
        )
        + exam_tip(
            "On the answer sheet, write the month-count in words once (“July to March = 9 months”) "
            "before you multiply. Examiners award method marks for the 9/12 even if a later total slips."
        )
    )
    return example(
        "2",
        "Moderate",
        "SLM with Indian financial year — purchased 1 July, last year is a stub",
        body,
    )


def _slm_exam() -> str:
    body = (
        p(
            b("Given. "),
            "A machine is bought on ",
            b("1 October 2022"),
            " for ",
            rupee(500000),
            ". Installation costs ",
            rupee(20000),
            ". Scrap is ",
            b("10% of cost"),
            ". Useful life 10 years. Year-end 31 March. SLM.",
        )
        + p(
            "The machine is ",
            b("sold on 30 September 2025"),
            " for ",
            rupee(380000),
            ". Prepare the depreciation schedule up to the date of sale, compute profit or loss on sale, and pass the journals on the date of sale. Use the accumulated-depreciation method.",
        )
        + h4("Step 1 — cost, scrap, annual depreciation")
        + p("Cost = 5,00,000 + 20,000 = ", rupee(520000), " (installation is capitalised).")
        + p("Scrap = 10% of 5,20,000 = (10/100) × 5,20,000 = ", rupee(52000), ".")
        + p("Depreciable amount = 5,20,000 − 52,000 = ", rupee(468000), ".")
        + p("Annual depreciation = 4,68,000 ÷ 10 = ", rupee(46800), ".")
        + p("Rate on original cost = (46,800 ÷ 5,20,000) × 100 = 9%. Check: 5,20,000 × 9% = 46,800.")
        + h4("Step 2 — months in the first year")
        + p("1 October 2022 to 31 March 2023 = October, November, December, January, February, March = ", b("6 months"), ".")
        + p("FY 2022–23 depreciation = 46,800 × 6/12 = (46,800 × 6) ÷ 12 = 2,80,800 ÷ 12 = ", rupee(23400), ".")
        + p("Or: 46,800 × 1/2 = ", rupee(23400), ".")
        + h4("Step 3 — schedule until 30 September 2025")
        + table(
            ["Financial year", "Months", "Working", "Depreciation (₹)", "Accum. dep. (₹)", "NBV at period-end (₹)"],
            [
                ["2022–23 (1 Oct–31 Mar)", "6", "46,800 × 6/12", "23,400", "23,400", "4,96,600"],
                ["2023–24", "12", "full year", "46,800", "70,200", "4,49,800"],
                ["2024–25", "12", "full year", "46,800", "1,17,000", "4,03,000"],
                ["2025–26 (1 Apr–30 Sep)", "6", "46,800 × 6/12", "23,400", "1,40,400", "3,79,600"],
            ],
            caption="Charge depreciation in the year of sale up to the date of sale — then stop and sell",
            foot="NBV walk: 5,20,000 − 23,400 = 4,96,600; − 46,800 = 4,49,800; − 46,800 = 4,03,000; − 23,400 = 3,79,600.",
        )
        + p("Accumulated depreciation on the date of sale = 23,400 + 46,800 + 46,800 + 23,400.")
        + p("23,400 + 23,400 = 46,800.")
        + p("46,800 + 46,800 = 93,600.")
        + p("93,600 + 46,800 = ", rupee(140400), ".")
        + p("NBV on 30 September 2025 = Cost − Accum. dep. = 5,20,000 − 1,40,400 = ", rupee(379600), ".")
        + h4("Step 4 — profit or loss on sale")
        + formula(
            "Profit / (Loss) on sale = Sale proceeds − NBV on the date of sale",
            "If proceeds > NBV → profit (credited to P&L). If proceeds < NBV → loss (debited to P&L).",
        )
        + p("Sale proceeds ", rupee(380000), " − NBV ", rupee(379600), " = ", b(rupee(400) + " profit"), ".")
        + p("A profit of four hundred rupees is still a profit. Write it. Do not round it away.")
        + h4("Step 5 — journals on 30 September 2025")
        + p(b("Entry 1 — depreciation for the 6 months of FY 2025–26 up to the date of sale."))
        + journal(
            [
                {
                    "date": "30 Sep 2025",
                    "debit": "Depreciation A/c",
                    "credit": "Accumulated Depreciation A/c",
                    "amount": "23,400",
                    "narration": "Being SLM depreciation for 6 months up to the date of sale",
                }
            ],
            caption="Always depreciate up to the date of sale before you touch the asset account",
        )
        + p(
            b("Entry 2 — take the asset off the books."),
            " Debit whatever came in (bank + the contra-asset you have built + any loss). "
            "Credit the asset’s cost. If there is a profit, it sits on the credit side so that the entry balances.",
        )
        + journal(
            [
                {
                    "date": "30 Sep 2025",
                    "lines": [
                        {"account": "Bank A/c", "side": "dr", "amount": "3,80,000"},
                        {"account": "Accumulated Depreciation A/c", "side": "dr", "amount": "1,40,400"},
                        {"account": "Machinery A/c", "side": "cr", "amount": "5,20,000"},
                        {"account": "Profit on Sale of Machinery A/c", "side": "cr", "amount": "400"},
                    ],
                    "narration": "Being machinery sold; accumulated depreciation and profit on sale accounted for",
                }
            ],
            caption="Sale of the asset — the four figures must cross-add to the same total on both sides",
        )
        + p(
            "Cross-add the debit side: 3,80,000 + 1,40,400 = ",
            rupee(520400),
            ". Cross-add the credit side: 5,20,000 + 400 = ",
            rupee(520400),
            ". If these two totals disagree, the profit or the accumulated depreciation is wrong.",
        )
        + p(b("Entry 3 — close the profit to P&L (and close this year’s depreciation too)."))
        + journal(
            [
                {
                    "date": "30 Sep 2025",
                    "debit": "Profit on Sale of Machinery A/c",
                    "credit": "Profit and Loss A/c",
                    "amount": "400",
                    "narration": "Being profit on sale transferred to Profit and Loss Account",
                },
                {
                    "date": "31 Mar 2026",
                    "debit": "Profit and Loss A/c",
                    "credit": "Depreciation A/c",
                    "amount": "23,400",
                    "narration": "Being current-period depreciation (up to date of sale) transferred to P&L",
                },
            ],
            caption="Nominal accounts are emptied into P&L — profit on sale is income; depreciation is expense",
        )
        + h4("Machinery account after the sale (so you can see it close)")
        + t_account(
            "Machinery A/c",
            [
                ("To Bank / Vendor (1 Oct 2022) — cost", "5,20,000"),
            ],
            [
                ("By Accumulated Depreciation A/c", "1,40,400"),
                ("By Bank A/c (sale)", "3,80,000"),
                ("By Profit on Sale of Machinery A/c", "400"),
            ],
        )
        + p("Debit total 5,20,000. Credit total 1,40,400 + 3,80,000 + 400 = 5,20,000. The account closes. That is the proof the profit is ₹400 and not some other figure.")
        + exam_tip(
            "Date discipline wins this question. FY 2022–23 is 6 months, FY 2023–24 and 2024–25 are full, "
            "FY 2025–26 up to 30 September is 6 months. Students who charge three full years and then sell "
            "from a wrong NBV lose the 4-mark tail of the question."
        )
    )
    return example(
        "3",
        "Exam",
        "Installation added to cost, part-year SLM, then sale — profit of ₹400",
        body,
    )


# ---------------------------------------------------------------------------
# WDV
# ---------------------------------------------------------------------------
def _wdv() -> str:
    return (
        h2("7. Written Down Value Method (WDV)", "wdv")
        + definition(
            "Under the Written Down Value Method (also called the Diminishing Balance Method or the Reducing Balance Method), "
            "depreciation for a year is a <strong>fixed percentage of the book value at the start of that year</strong> "
            "(or of the cost, in year 1, because year-1 book value <em>is</em> cost). "
            "The rupee charge falls every full year. Residual is "
            "<strong>not subtracted each year</strong> — the rate is designed (or given) so that book value declines towards scrap."
        )
        + simple(
            "Each year you tax a smaller number with the same percentage. "
            "Year 1: 10% of "
            + rupee(100000)
            + " = "
            + rupee(10000)
            + ". Year 2: 10% of the leftover "
            + rupee(90000)
            + " = "
            + rupee(9000)
            + ". The asset never quite hits zero if you keep going, which is why a residual usually remains."
        )
        + why(
            "A new laptop loses a lot of usefulness in year 1 (new model, falling resale) and less in year 4. "
            "WDV front-loads the expense to match that pattern. It is also the method many tax rules historically favoured, "
            "so Indian papers are full of “20% p.a. on WDV”."
        )
        + real_life(
            "You buy a phone for "
            + rupee(80000)
            + ". On a resale app it is worth far less after 12 months than after the next 12. "
            "Charging the same SLM slice every year would under-charge year 1 and over-charge year 4. "
            "WDV follows the gadget."
        )
        + logic(
            "Book value at the start of the year is the unexpired cost. WDV says: expire a constant "
            "<em>fraction</em> of whatever is still unexpired. Because the base shrinks, the rupee amount shrinks. "
            "You do not deduct scrap from the base each year — if you did, you would mix SLM arithmetic into a WDV question."
        )
        + formula(
            "Depreciation for the year = Opening WDV × Rate × (months used ÷ 12)",
            "Year 1 opening WDV = Cost. Residual is NOT deducted in the annual working. "
            "If the exam gives life and residual but no rate, there is a formula "
            "R = 1 − (Scrap ÷ Cost)<sup>1/n</sup> — shown below for completeness. "
            "MBA numericals almost always <strong>give the rate</strong>. Use the rate you are given.",
        )
        + format_box(
            "WDV rate when life and scrap are given (completeness, rarely needed)",
            p("R = 1 − (Scrap / Cost)<sup>(1/n)</sup>, where n is useful life in years.")
            + p(
                "Illustration: Cost ",
                rupee(500000),
                ", scrap ",
                rupee(50000),
                ", n = 5. Scrap/Cost = 0.10. "
                "(0.10)<sup>1/5</sup> ≈ 0.63096. R ≈ 1 − 0.63096 = 0.3690 = ",
                b("36.90%"),
                ". You would then apply 36.90% each year on WDV, and after 5 years WDV would be very close to scrap.",
            )
            + p(
                "In the exam, if you are given “20% p.a. on WDV”, do ",
                b("not"),
                " invent this formula. The given rate already is the answer. "
                "With an arbitrary given rate, WDV at the end of life will usually ",
                i("not"),
                " equal the residual — and that is acceptable.",
            ),
        )
        + steps(
            [
                "Build cost (same as SLM). Residual is noted but not subtracted from the yearly base.",
                "Read the rate. Confirm it is “on WDV / on book value / diminishing / reducing”.",
                "Year 1: Depreciation = Cost × Rate × months/12. Closing WDV = Cost − that depreciation.",
                "Year 2: Depreciation = Closing WDV of year 1 × Rate × 1 (if a full year). Never go back to original cost.",
                "Repeat. Each closing WDV becomes the next opening WDV.",
                "Part-year: multiply that year’s full-year WDV charge by months/12. "
                "Do this in two multiplications: first Rate on opening WDV, then the month fraction.",
                "On sale: charge WDV depreciation up to the date of sale (opening WDV × Rate × months/12), then compare sale proceeds with the NBV of that date.",
            ]
        )
        + _wdv_easy()
        + _wdv_moderate()
        + _wdv_exam()
        + identify(
            "Use WDV when the question says any of: <strong>written down value, WDV, diminishing balance, "
            "reducing balance, on book value, on the reducing balance</strong>. "
            "“Rate % per annum on WDV” is the giveaway. "
            "“Rate % per annum on cost / on original cost” is SLM, even if the word “rate” made you think WDV."
        )
        + mistakes(
            [
                "Deducting scrap every year before applying the WDV rate. Scrap is not part of the yearly working.",
                "Applying the rate to original cost in year 2 and year 3. Year 2’s base is year 1’s closing WDV.",
                "Using the SLM formula (Cost − Scrap) / n when the question has clearly given a WDV rate.",
                "Forgetting the 6/12 (or 9/12, 3/12) in the year of purchase or the year of sale. WDV part-year is still months/12.",
                "Adding a second asset into the first asset’s WDV and applying one rate to a mixed lump — always keep a column per asset, then add the depreciation.",
            ]
        )
        + memory(
            "WDV = <strong>What Decreases Yearly</strong> in rupees, even though the percentage is fixed. "
            "New gadgets lose more in year 1 — that is the picture to hold. "
            "Base next year = leftover, never the original price tag."
        )
    )


def _wdv_easy() -> str:
    body = (
        p(
            b("Given. "),
            "Cost ",
            rupee(100000),
            ", rate ",
            b("10% p.a. on WDV"),
            ". Prepare a 3-year schedule.",
        )
        + h4("Year 1")
        + p("Opening WDV = cost = ", rupee(100000), ".")
        + p("Depreciation = 1,00,000 × 10/100 = ", rupee(10000), ".")
        + p("Closing WDV = 1,00,000 − 10,000 = ", rupee(90000), ".")
        + h4("Year 2")
        + p("Opening WDV = ", rupee(90000), " (not 1,00,000).")
        + p("Depreciation = 90,000 × 10/100 = ", rupee(9000), ".")
        + p("Closing WDV = 90,000 − 9,000 = ", rupee(81000), ".")
        + h4("Year 3")
        + p("Depreciation = 81,000 × 10/100 = ", rupee(8100), ".")
        + p("Closing WDV = 81,000 − 8,100 = ", rupee(72900), ".")
        + table(
            ["Year", "Opening WDV (₹)", "Rate", "Working", "Depreciation (₹)", "Closing WDV (₹)"],
            [
                ["1", "1,00,000", "10%", "1,00,000 × 10/100", "10,000", "90,000"],
                ["2", "90,000", "10%", "90,000 × 10/100", "9,000", "81,000"],
                ["3", "81,000", "10%", "81,000 × 10/100", "8,100", "72,900"],
            ],
            caption="WDV easy — the rupee charge falls; the percentage does not",
            foot="Notice residual was never mentioned and never deducted. After 3 years ₹72,900 is still on the books.",
        )
        + journal(
            [
                {
                    "date": "31 Mar Yr 2",
                    "debit": "Depreciation A/c",
                    "credit": "Accumulated Depreciation A/c",
                    "amount": "9,000",
                    "narration": "Being 10% WDV depreciation on opening book value ₹90,000",
                }
            ],
            caption="The journal looks exactly like SLM — only the amount was computed differently",
        )
    )
    return example("4", "Easy", "WDV at 10% for three years — falling charge, fixed rate", body)


def _wdv_moderate() -> str:
    body = (
        p(
            b("Given. "),
            "Cost ",
            rupee(400000),
            ", rate ",
            b("25% p.a. on WDV"),
            ", purchased ",
            b("1 October"),
            ", year-end 31 March. Compute depreciation and WDV for the first three financial years.",
        )
        + h4("Year 1 — six months")
        + p("1 October to 31 March = 6 months.")
        + p("Full-year depreciation on cost = 4,00,000 × 25/100 = ", rupee(100000), ".")
        + p("Part-year depreciation = 1,00,000 × 6/12 = (1,00,000 × 6) ÷ 12 = 6,00,000 ÷ 12 = ", rupee(50000), ".")
        + p("Combined in one line: 4,00,000 × 25/100 × 6/12 = 4,00,000 × 1/4 × 1/2 = 1,00,000 × 1/2 = ", rupee(50000), ".")
        + p("Closing WDV = 4,00,000 − 50,000 = ", rupee(350000), ".")
        + h4("Year 2 — full year, new base")
        + p("Opening WDV = ", rupee(350000), ".")
        + p("Depreciation = 3,50,000 × 25/100 = 3,50,000 × 1/4.")
        + p("3,50,000 ÷ 4 = ", rupee(87500), ".")
        + p("Closing WDV = 3,50,000 − 87,500 = ", rupee(262500), ".")
        + h4("Year 3 — full year")
        + p("Depreciation = 2,62,500 × 25/100 = 2,62,500 × 1/4.")
        + p("2,62,500 ÷ 4 = ", rupee(65625), ".")
        + p("Closing WDV = 2,62,500 − 65,625 = ", rupee(196875), ".")
        + table(
            ["FY", "Opening WDV (₹)", "Working", "Depreciation (₹)", "Closing WDV (₹)"],
            [
                ["Year 1 (6 months)", "4,00,000", "4,00,000 × 25% × 6/12", "50,000", "3,50,000"],
                ["Year 2 (12 months)", "3,50,000", "3,50,000 × 25%", "87,500", "2,62,500"],
                ["Year 3 (12 months)", "2,62,500", "2,62,500 × 25%", "65,625", "1,96,875"],
            ],
            caption="WDV part-year — fraction in year 1 only; later years use the already-reduced base for a full year",
        )
        + warn(
            "Wrong path: “Year 2 = 4,00,000 × 25% = ₹1,00,000.” That is SLM-on-cost thinking. "
            "Once year 1 has been charged, original cost is retired as a base forever."
        )
        + keypoint(
            "A useful identity: 25% for 6 months is not 25%. It is 12.5% of the opening WDV of that year. "
            "Write it as Rate × months/12 so the examiner sees the method, even if you then multiply in one step."
        )
    )
    return example(
        "5",
        "Moderate",
        "WDV 25% with purchase on 1 October — 6/12 then falling full years",
        body,
    )


def _wdv_exam() -> str:
    body = (
        p(
            b("Given. "),
            "Year-end 31 March. Depreciation 20% p.a. on WDV.",
        )
        + ul(
            [
                "1 April 2022: purchased Machinery A for " + rupee(800000) + ".",
                "1 October 2023: purchased Machinery B for " + rupee(300000) + ".",
                "1 January 2025: sold Machinery A for " + rupee(420000) + ".",
            ]
        )
        + p("Compute depreciation for FY 2022–23, 2023–24 and 2024–25, and the profit or loss on sale of A. Keep a separate column for each machine.")
        + h4("Machinery A (bought 1 April 2022 — a full year from day one)")
        + p(b("FY 2022–23."), " Opening WDV = ", rupee(800000), ".")
        + p("Depreciation = 8,00,000 × 20/100 = ", rupee(160000), ".")
        + p("Closing WDV = 8,00,000 − 1,60,000 = ", rupee(640000), ".")
        + p(b("FY 2023–24."), " Opening WDV = ", rupee(640000), ".")
        + p("Depreciation = 6,40,000 × 20/100 = ", rupee(128000), ".")
        + p("Closing WDV = 6,40,000 − 1,28,000 = ", rupee(512000), ".")
        + p(
            b("FY 2024–25, used until 1 January 2025."),
            " 1 April 2024 to 1 January 2025 = April to December = ",
            b("9 months"),
            ".",
        )
        + p("Full-year depreciation on 5,12,000 = 5,12,000 × 20/100 = ", rupee(102400), ".")
        + p("Part-year = 1,02,400 × 9/12 = (1,02,400 × 9) ÷ 12.")
        + p("1,02,400 × 9 = 9,21,600.")
        + p("9,21,600 ÷ 12 = ", rupee(76800), ".")
        + p("Or: 1,02,400 × 3/4 = ", rupee(76800), ".")
        + p("NBV on the date of sale = 5,12,000 − 76,800 = ", rupee(435200), ".")
        + p("Sale proceeds ", rupee(420000), " − NBV ", rupee(435200), " = ", b(rupee(-15200) + " — a loss of ₹15,200"), ".")
        + p("Accumulated depreciation on A at sale = 1,60,000 + 1,28,000 + 76,800 = ", rupee(364800), ".")
        + p("Check: cost 8,00,000 − accum. 3,64,800 = NBV 4,35,200. Loss = 4,35,200 − 4,20,000 = ", rupee(15200), ".")
        + h4("Machinery B (bought 1 October 2023)")
        + p(b("FY 2023–24."), " 1 October 2023 to 31 March 2024 = 6 months.")
        + p("Depreciation = 3,00,000 × 20/100 × 6/12 = 60,000 × 6/12 = ", rupee(30000), ".")
        + p("Closing WDV = 3,00,000 − 30,000 = ", rupee(270000), ".")
        + p(b("FY 2024–25."), " Full year on 2,70,000.")
        + p("Depreciation = 2,70,000 × 20/100 = ", rupee(54000), ".")
        + p("Closing WDV = 2,70,000 − 54,000 = ", rupee(216000), ".")
        + h4("Combined depreciation (what actually goes to P&L)")
        + table(
            ["Financial year", "Dep. on A (₹)", "Dep. on B (₹)", "Total to P&L (₹)"],
            [
                ["2022–23", "1,60,000", "— (not yet bought)", "1,60,000"],
                ["2023–24", "1,28,000", "30,000", "1,58,000"],
                ["2024–25", "76,800 (9 months, then sold)", "54,000", "1,30,800"],
            ],
            caption="Two assets, one rate, separate columns — then add",
            foot="1,28,000 + 30,000 = 1,58,000. 76,800 + 54,000 = 1,30,800.",
        )
        + h4("Journals on 1 January 2025 for the sale of A")
        + journal(
            [
                {
                    "date": "1 Jan 2025",
                    "debit": "Depreciation A/c",
                    "credit": "Accumulated Depreciation A/c",
                    "amount": "76,800",
                    "narration": "Being 20% WDV depreciation on Machinery A for 9 months up to the date of sale",
                },
                {
                    "date": "1 Jan 2025",
                    "lines": [
                        {"account": "Bank A/c", "side": "dr", "amount": "4,20,000"},
                        {"account": "Accumulated Depreciation A/c", "side": "dr", "amount": "3,64,800"},
                        {"account": "Loss on Sale of Machinery A/c", "side": "dr", "amount": "15,200"},
                        {"account": "Machinery A/c", "side": "cr", "amount": "8,00,000"},
                    ],
                    "narration": "Being Machinery A sold at a loss of ₹15,200",
                },
            ],
            caption="Sale under WDV — same journal shape as SLM; the amounts came from a different computation",
        )
        + p(
            "Debit cross-add: 4,20,000 + 3,64,800 + 15,200 = ",
            rupee(800000),
            " = cost credited. The loss is whatever is needed to make this identity true. "
            "If your three debits do not add to cost, you have the wrong loss or the wrong accumulated depreciation.",
        )
        + exam_tip(
            "When a second asset arrives, draw two mini-ledgers on the rough page. "
            "Never apply 20% to (A’s WDV + B’s cost) as one soup. B has its own 6-month first year; A does not."
        )
    )
    return example(
        "6",
        "Exam",
        "WDV with a second asset and a sale — keep columns apart",
        body,
    )


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------
def _comparison() -> str:
    return (
        h2("8. SLM versus WDV — comparison the examiner actually wants", "comparison")
        + simple(
            "Same asset, two stories about how its cost dies. SLM kills it in equal rupees. "
            "WDV kills a larger rupee chunk up front and a smaller one later. "
            "The journals look the same. The numbers, the profit pattern, and the end-of-life book value do not."
        )
        + table(
            ["Point", "Straight Line (SLM)", "Written Down Value (WDV)"],
            [
                [
                    "Base of the rate",
                    "Original cost, every year",
                    "Opening book value of that year",
                ],
                [
                    "Amount pattern",
                    "Same rupees every full year",
                    "Falling rupees every full year",
                ],
                [
                    "Residual in the yearly working",
                    "Subtracted once, in the formula (Cost − Scrap) / n",
                    "Not subtracted yearly; rate is supposed to steer towards it",
                ],
                [
                    "End of life",
                    "WDV hits residual exactly (if life and scrap are honoured)",
                    "Approaches residual; hits it only if the rate was derived from R = 1 − (S/C)<sup>1/n</sup>",
                ],
                [
                    "Effect on profit",
                    "Equal charge → comparable profits across years (other things equal)",
                    "Heavier charge in early years → lower early profits, higher later profits",
                ],
                [
                    "Best suited for",
                    "Buildings, furniture, leases — equal service each year",
                    "Plant, vehicles, electronics — heavier usefulness (and repair later) in a skewed pattern",
                ],
                [
                    "Repairs pattern (theory extra)",
                    "Repairs usually rise as the asset ages, so total “dep + repairs” rises over time",
                    "Falling dep + rising repairs can keep the combined charge smoother",
                ],
                [
                    "Calculation comfort",
                    "One division, then copy the answer each year",
                    "Must recompute every year on a new base; part-year needs two multiplications",
                ],
                [
                    "Question-paper flags",
                    "“straight line / original cost / equal / fixed instalment / on cost”",
                    "“WDV / diminishing / reducing / on book value”",
                ],
            ],
            caption="SLM vs WDV — eight rows that cover a 5-to-8 mark distinguish question",
        )
        + exam_answer(
            "Under SLM a fixed amount equal to (Cost − Residual) / Life is written off each full year, "
            "so book value falls in a straight line and meets residual exactly. Under WDV a fixed rate is "
            "applied to the book value brought forward, so the charge is higher in early years and lower later, "
            "and residual is not deducted annually. SLM suits assets with even service (buildings); WDV suits "
            "assets that lose efficiency or resale value quickly (plant, electronics). Total depreciation over "
            "the whole life equals the depreciable amount under SLM; under WDV it equals Cost minus the leftover "
            "book value, which equals residual only if the rate was derived from the residual formula."
        )
        + _comparison_example()
    )


def _comparison_example() -> str:
    body = (
        p(
            b("Given. "),
            "Cost ",
            rupee(500000),
            ", residual ",
            rupee(50000),
            ", life 5 years. Compute depreciation for 3 years under (i) SLM and (ii) WDV at 20% p.a. Comment.",
        )
        + h4("(i) SLM")
        + p("Annual depreciation = (5,00,000 − 50,000) ÷ 5 = 4,50,000 ÷ 5 = ", rupee(90000), ".")
        + p("Rate on original cost = (90,000 ÷ 5,00,000) × 100 = 18%.")
        + table(
            ["Year", "Depreciation (₹)", "Accum. dep. (₹)", "WDV (₹)"],
            [
                ["1", "90,000", "90,000", "4,10,000"],
                ["2", "90,000", "1,80,000", "3,20,000"],
                ["3", "90,000", "2,70,000", "2,30,000"],
                ["4 (shown for the comment)", "90,000", "3,60,000", "1,40,000"],
                ["5 (shown for the comment)", "90,000", "4,50,000", "50,000 = scrap"],
            ],
            caption="SLM — equal charge, lands on residual",
        )
        + h4("(ii) WDV at 20% (rate is given — do not derive it)")
        + p("Year 1: 5,00,000 × 20/100 = ", rupee(100000), ". WDV = 5,00,000 − 1,00,000 = ", rupee(400000), ".")
        + p("Year 2: 4,00,000 × 20/100 = ", rupee(80000), ". WDV = 4,00,000 − 80,000 = ", rupee(320000), ".")
        + p("Year 3: 3,20,000 × 20/100 = ", rupee(64000), ". WDV = 3,20,000 − 64,000 = ", rupee(256000), ".")
        + p("Year 4: 2,56,000 × 20/100 = ", rupee(51200), ". WDV = 2,56,000 − 51,200 = ", rupee(204800), ".")
        + p("Year 5: 2,04,800 × 20/100 = ", rupee(40960), ". WDV = 2,04,800 − 40,960 = ", rupee(163840), ".")
        + table(
            ["Year", "SLM dep. (₹)", "WDV dep. (₹)", "Which method charges more this year?"],
            [
                ["1", "90,000", "1,00,000", "WDV (front-loaded)"],
                ["2", "90,000", "80,000", "SLM"],
                ["3", "90,000", "64,000", "SLM"],
                ["Total of 3 years", "2,70,000", "2,44,000", "SLM has charged ₹26,000 more by the end of year 3"],
            ],
            caption="Three-year comparison the question asked for",
            foot="1,00,000 + 80,000 + 64,000 = 2,44,000. 90,000 × 3 = 2,70,000. Difference = 26,000.",
        )
        + h4("Comment (write this, not a vague “they are different”)")
        + ol(
            [
                "WDV charges more in year 1 (₹1,00,000 vs ₹90,000) and less thereafter. Early profits are lower under WDV; later profits are higher.",
                "After 5 years SLM has written the asset down to residual ₹50,000 exactly. WDV at the given 20% still shows ₹1,63,840 — because 20% was not the residual-derived rate (that would have been about 36.90%).",
                "Total depreciation over the whole life is therefore not the same: SLM takes the full depreciable amount ₹4,50,000; WDV at 20% has taken only 5,00,000 − 1,63,840 = ₹3,36,160 after 5 years.",
                "If the question had asked which method is “conservative” in the early years, the answer is WDV — it recognises more expense sooner.",
            ]
        )
    )
    return example(
        "7",
        "Exam",
        "Compute both methods for 3 years and comment — the comparison numerical",
        body,
    )


# ---------------------------------------------------------------------------
# Provision vs charging to asset
# ---------------------------------------------------------------------------
def _provision_vs_asset() -> str:
    return (
        h2("9. Two presentations: charge the asset, or keep a provision", "provision")
        + definition(
            "There are two bookkeeping styles for the same depreciation number. "
            "<strong>Direct method:</strong> credit the asset; the ledger then shows WDV as the asset’s balance. "
            "<strong>Indirect / provision / accumulated-depreciation method:</strong> credit a separate contra-asset; "
            "the asset ledger continues to show original cost. MBA papers usually want the provision method."
        )
        + simple(
            "Think of a price tag and a stack of “already-used” stickers. Direct method rewrites the price tag every year. "
            "Provision method leaves the price tag (cost) alone and piles stickers next to it. "
            "Anyone reading the Balance Sheet under the provision method can still see what you originally paid."
        )
        + why(
            "Companies Act / Schedule III style statements show Gross Block, Accumulated Depreciation and Net Block. "
            "That layout is impossible if you have already credited the asset and thrown cost away. "
            "So the provision method is the one you should default to in an exam unless told otherwise."
        )
        + format_box(
            "Same ₹18,000, two journals, two Balance Sheets (from Example 1, year 1)",
            two_col(
                p(b("Direct method"))
                + journal(
                    [
                        {
                            "date": "31 Mar",
                            "debit": "Depreciation A/c",
                            "credit": "Machinery A/c",
                            "amount": "18,000",
                            "narration": "Being depreciation charged directly to the asset",
                        }
                    ],
                    caption="Credit the asset",
                )
                + table(
                    ["Balance Sheet extract", "₹"],
                    [["Machinery (at WDV)", "82,000"]],
                    caption="Cost has disappeared from the face of the statement",
                ),
                p(b("Provision method (preferred)"))
                + journal(
                    [
                        {
                            "date": "31 Mar",
                            "debit": "Depreciation A/c",
                            "credit": "Accumulated Depreciation A/c",
                            "amount": "18,000",
                            "narration": "Being depreciation transferred to the provision / accumulated account",
                        }
                    ],
                    caption="Credit the contra-asset",
                )
                + table(
                    ["Balance Sheet extract", "₹", "₹"],
                    [
                        ["Machinery (at cost)", "1,00,000", ""],
                        ["Less: Accumulated depreciation", "18,000", "82,000"],
                    ],
                    caption="Cost remains visible — this is the MBA default",
                ),
            ),
        )
        + keypoint(
            "Profit is identical under both presentations — ₹18,000 expense either way. "
            "Only the <em>display</em> of the asset changes. Do not compute depreciation twice because you saw two methods."
        )
        + p(
            b("On sale, the direct method is shorter"),
            " because the asset already sits at NBV. After charging dep up to the date of sale "
            "(Example 3’s machine, NBV ₹3,79,600; sold for ₹3,80,000):",
        )
        + journal(
            [
                {
                    "date": "30 Sep 2025",
                    "lines": [
                        {"account": "Bank A/c", "side": "dr", "amount": "3,80,000"},
                        {"account": "Machinery A/c", "side": "cr", "amount": "3,79,600"},
                        {"account": "Profit on Sale of Machinery A/c", "side": "cr", "amount": "400"},
                    ],
                    "narration": "Direct method — asset already at NBV, so we credit NBV and recognise the ₹400 profit",
                }
            ],
            caption="Sale under the direct method — no accumulated-depreciation line, because that account does not exist",
        )
        + p(
            "Under the provision method (already shown in Example 3) you must debit Accumulated Depreciation "
            "to kill the contra-asset, and credit Machinery with original cost. Same profit of ₹400. "
            "If the question has been using a Provision for Depreciation account all along, stay with that account on the sale date."
        )
    )


# ---------------------------------------------------------------------------
# Identify / mistakes / memory (chapter-level, as specified)
# ---------------------------------------------------------------------------
def _identify_mistakes_memory() -> str:
    return (
        h2("10. How to identify, what to avoid, how to remember", "identify")
        + identify(
            "<strong>Straight line / original cost / equal / fixed instalment / “rate % p.a. on cost”</strong> → SLM. "
            "Annual amount = (Cost − Residual) / Life, or Cost × the given on-cost rate. "
            "<strong>WDV / diminishing / reducing balance / written down / “on WDV” / “on book value”</strong> → WDV. "
            "Amount = Opening WDV × Rate. "
            "Part-year: always count months from the date <em>put to use</em> to the year-end (or to the date of sale). "
            "Indian year-end 31 March and “put to use on 1 October” → 6/12. "
            "A second asset → a second column. A sale → depreciate first, then remove the asset, then profit or loss."
        )
        + mistakes(
            [
                "Applying an SLM rate to WDV (or a WDV rate to original cost after year 1).",
                "Deducting scrap every year under WDV.",
                "Forgetting installation, freight or non-refundable duty in cost.",
                "Charging a full year when the asset was purchased on 1 January (3/12) or 1 October (6/12).",
                "Treating depreciation as a cash outflow in a cash-flow question (that belongs to the cash-flow chapter — add it back).",
                "Skipping depreciation in the year of sale.",
                "Taking “10% of cost” as 10% of the invoice when installation has been added — scrap follows total cost.",
                "Mixing two machines into one WDV base.",
                "Calling accumulated depreciation a cash reserve or a replacement fund.",
            ]
        )
        + memory(
            "SLM = <strong>Same Load every year</strong>, like equal slices (equal “principal” in an EMI picture). "
            "WDV = <strong>new gadgets lose more in year 1</strong>. "
            "Part-year = months/12, always. "
            "Sale = depreciate → strip the accounts → proceeds versus NBV. "
            "Cash left the business on the purchase date, not on the depreciation date."
        )
        + exam_tip(
            "Before you multiply, write one heading on the rough page: “SLM on cost” or “WDV on book”. "
            "Circle the date put to use and the year-end. Circle installation. Circle “sold on”. "
            "Those four circles are the entire exam technique for this chapter."
        )
    )


# ---------------------------------------------------------------------------
# Practice
# ---------------------------------------------------------------------------
def _practice() -> str:
    return (
        h2("11. Practice questions (try, then open the solution)", "practice")
        + p(
            "Three questions, rising in difficulty, using numbers you have ",
            i("not"),
            " already seen in the worked examples. Write the full working — including the multiplications — before you scroll.",
        )
        + _practice_1()
        + _practice_2()
        + _practice_3()
    )


def _practice_1() -> str:
    q = (
        p("Furniture is purchased for ", rupee(80000), ". Residual value ", rupee(8000), ". Useful life 8 years. SLM.")
        + p(b("Required:"))
        + ol(
            [
                "Annual depreciation and the rate on original cost.",
                "A 3-year schedule showing cost, depreciation, accumulated depreciation and WDV.",
                "WDV at the end of year 8 (without listing every year).",
                "The year-1 journal under the provision method, and the Balance Sheet extract after 3 years.",
            ]
        )
    )
    a = (
        p(b("Step 1. "), "Depreciable amount = 80,000 − 8,000 = ", rupee(72000), ".")
        + p("Annual depreciation = 72,000 ÷ 8 = ", rupee(9000), ".")
        + p("Rate on original cost = (9,000 ÷ 80,000) × 100 = ", b("11.25%"), ".")
        + p("Check: 80,000 × 11.25/100 = 80,000 × 0.1125. 80,000 × 0.10 = 8,000; 80,000 × 0.0125 = 1,000; total 9,000.")
        + p(b("Step 2. Schedule of 3 years."))
        + table(
            ["Year", "Cost (₹)", "Depreciation (₹)", "Accum. dep. (₹)", "WDV (₹)"],
            [
                ["1", "80,000", "9,000", "9,000", "71,000"],
                ["2", "80,000", "9,000", "18,000", "62,000"],
                ["3", "80,000", "9,000", "27,000", "53,000"],
            ],
            caption="Practice 1 — SLM schedule",
            foot="Year-1 WDV: 80,000 − 9,000 = 71,000. Year-2: 71,000 − 9,000 = 62,000. Year-3: 62,000 − 9,000 = 53,000. Accum. year 3 = 9,000 × 3 = 27,000.",
        )
        + p(b("Step 3. "), "After 8 years accumulated depreciation = 9,000 × 8 = ", rupee(72000), ".")
        + p("WDV at the end of year 8 = 80,000 − 72,000 = ", rupee(8000), " = scrap. That is the SLM landing-check.")
        + p(b("Step 4. Journals and presentation."))
        + journal(
            [
                {
                    "date": "Year 1, year-end",
                    "debit": "Depreciation A/c",
                    "credit": "Accumulated Depreciation A/c",
                    "amount": "9,000",
                    "narration": "Being SLM depreciation for the year",
                },
                {
                    "date": "Year 1, year-end",
                    "debit": "Profit and Loss A/c",
                    "credit": "Depreciation A/c",
                    "amount": "9,000",
                    "narration": "Being depreciation transferred to P&L",
                },
            ],
            caption="Practice 1 — year-1 journals",
        )
        + table(
            ["Balance Sheet extract after 3 years", "₹", "₹"],
            [
                ["Furniture (at cost)", "80,000", ""],
                ["Less: Accumulated depreciation", "27,000", "53,000"],
            ],
        )
    )
    return practice("1", "Easy", "SLM furniture — annual charge, 3-year schedule, residual check", q, a)


def _practice_2() -> str:
    q = (
        p(
            "A plant costs ",
            rupee(600000),
            ". It is put to use on ",
            b("1 January 2024"),
            ". Depreciation is charged at ",
            b("20% p.a. on WDV"),
            ". The accounting year ends on 31 March.",
        )
        + p(b("Required:"), " depreciation and closing WDV for FY 2023–24, 2024–25 and 2025–26. Show every multiplication. Then pass the FY 2023–24 journal.")
    )
    a = (
        p(b("FY 2023–24."), " Put to use 1 January 2024 to 31 March 2024 = January, February, March = ", b("3 months"), ".")
        + p("Full-year depreciation on cost = 6,00,000 × 20/100 = ", rupee(120000), ".")
        + p("Part-year = 1,20,000 × 3/12 = (1,20,000 × 3) ÷ 12 = 3,60,000 ÷ 12 = ", rupee(30000), ".")
        + p("Combined: 6,00,000 × 20/100 × 3/12 = 6,00,000 × 1/5 × 1/4 = 1,20,000 × 1/4 = ", rupee(30000), ".")
        + p("Closing WDV = 6,00,000 − 30,000 = ", rupee(570000), ".")
        + p(b("FY 2024–25."), " Full year on ", rupee(570000), ".")
        + p("Depreciation = 5,70,000 × 20/100 = 5,70,000 × 1/5 = ", rupee(114000), ".")
        + p("Closing WDV = 5,70,000 − 1,14,000 = ", rupee(456000), ".")
        + p(b("FY 2025–26."), " Full year on ", rupee(456000), ".")
        + p("Depreciation = 4,56,000 × 20/100 = 4,56,000 × 1/5 = ", rupee(91200), ".")
        + p("Closing WDV = 4,56,000 − 91,200 = ", rupee(364800), ".")
        + table(
            ["FY", "Months", "Opening WDV (₹)", "Working", "Depreciation (₹)", "Closing WDV (₹)"],
            [
                ["2023–24", "3", "6,00,000", "6,00,000 × 20% × 3/12", "30,000", "5,70,000"],
                ["2024–25", "12", "5,70,000", "5,70,000 × 20%", "1,14,000", "4,56,000"],
                ["2025–26", "12", "4,56,000", "4,56,000 × 20%", "91,200", "3,64,800"],
            ],
            caption="Practice 2 — WDV with a 3-month first year",
        )
        + journal(
            [
                {
                    "date": "31 Mar 2024",
                    "debit": "Depreciation A/c",
                    "credit": "Accumulated Depreciation A/c",
                    "amount": "30,000",
                    "narration": "Being 20% WDV depreciation for 3 months (1 Jan to 31 Mar 2024)",
                }
            ],
            caption="Practice 2 — first-year journal",
        )
        + p(
            b("Trap you should have avoided: "),
            "charging ₹1,20,000 in FY 2023–24 (a full year) even though the plant worked only 3 months. "
            "1 January to 31 March is the shortest common part-year in Indian papers — and the most often missed.",
        )
    )
    return practice("2", "Moderate", "WDV 20% — purchased 1 January, year-end 31 March", q, a)


def _practice_3() -> str:
    q = (
        p(
            "On ",
            b("1 April 2021"),
            " a company bought a machine for ",
            rupee(400000),
            ". Installation ",
            rupee(40000),
            ". Residual is 10% of cost. Useful life 8 years. SLM. Year-end 31 March.",
        )
        + p("On ", b("1 October 2024"), " the machine was sold for ", rupee(250000), ".")
        + p(b("Required:"))
        + ol(
            [
                "Cost, scrap, annual depreciation and the SLM rate.",
                "Depreciation for each financial year up to the date of sale, and NBV on 1 October 2024.",
                "Profit or loss on sale.",
                "Journal entries on the date of sale (provision method), with a cross-add check.",
            ]
        )
    )
    a = (
        p(b("(a) Cost, scrap, annual dep, rate."))
        + p("Cost = 4,00,000 + 40,000 = ", rupee(440000), ".")
        + p("Scrap = 10% of 4,40,000 = (10/100) × 4,40,000 = ", rupee(44000), ".")
        + p("Depreciable amount = 4,40,000 − 44,000 = ", rupee(396000), ".")
        + p("Annual depreciation = 3,96,000 ÷ 8 = ", rupee(49500), ".")
        + p("Rate on original cost = (49,500 ÷ 4,40,000) × 100 = 11.25%.")
        + p("Check: 4,40,000 × 11.25/100 = 4,40,000 × 0.1125. 4,40,000 × 0.10 = 44,000; 4,40,000 × 0.0125 = 5,500; total 49,500.")
        + p(b("(b) Year-by-year up to sale."))
        + p("Bought 1 April 2021, so FY 2021–22, 2022–23 and 2023–24 are full years.")
        + p("Sold 1 October 2024 → FY 2024–25 from 1 April to 1 October = April to September = ", b("6 months"), ".")
        + p("6-month depreciation = 49,500 × 6/12 = 49,500 × 1/2 = ", rupee(24750), ".")
        + table(
            ["FY", "Months", "Depreciation (₹)", "Accum. dep. (₹)", "NBV (₹)"],
            [
                ["2021–22", "12", "49,500", "49,500", "3,90,500"],
                ["2022–23", "12", "49,500", "99,000", "3,41,000"],
                ["2023–24", "12", "49,500", "1,48,500", "2,91,500"],
                ["2024–25 to 1 Oct", "6", "24,750", "1,73,250", "2,66,750"],
            ],
            caption="Practice 3 — SLM until the morning of the sale",
            foot="NBV walk: 4,40,000 − 49,500 = 3,90,500; − 49,500 = 3,41,000; − 49,500 = 2,91,500; − 24,750 = 2,66,750. Accum. = 49,500 × 3 + 24,750 = 1,48,500 + 24,750 = 1,73,250. Cost − accum. = 4,40,000 − 1,73,250 = 2,66,750.",
        )
        + p(b("(c) Profit or loss."))
        + p("Sale proceeds ", rupee(250000), " − NBV ", rupee(266750), " = ", b("loss of " + rupee(16750)), ".")
        + p("Working: 2,66,750 − 2,50,000 = 16,750.")
        + p(b("(d) Journals on 1 October 2024."))
        + journal(
            [
                {
                    "date": "1 Oct 2024",
                    "debit": "Depreciation A/c",
                    "credit": "Accumulated Depreciation A/c",
                    "amount": "24,750",
                    "narration": "Being SLM depreciation for 6 months up to the date of sale",
                },
                {
                    "date": "1 Oct 2024",
                    "lines": [
                        {"account": "Bank A/c", "side": "dr", "amount": "2,50,000"},
                        {"account": "Accumulated Depreciation A/c", "side": "dr", "amount": "1,73,250"},
                        {"account": "Loss on Sale of Machinery A/c", "side": "dr", "amount": "16,750"},
                        {"account": "Machinery A/c", "side": "cr", "amount": "4,40,000"},
                    ],
                    "narration": "Being machinery sold at a loss of ₹16,750",
                },
            ],
            caption="Practice 3 — date-of-sale journals (provision method)",
        )
        + p(
            "Cross-add the sale entry, debit side: 2,50,000 + 1,73,250 + 16,750."
        )
        + p("2,50,000 + 1,73,250 = 4,23,250.")
        + p("4,23,250 + 16,750 = ", rupee(440000), " = cost credited. The identity holds, so the loss is correct.")
    )
    return practice(
        "3",
        "Exam",
        "Installation, 10% scrap, SLM, sold on 1 October — loss and journals",
        q,
        a,
    )


# ---------------------------------------------------------------------------
# Formula sheet
# ---------------------------------------------------------------------------
def _formula_sheet() -> str:
    return (
        h2("12. Formula sheet (this chapter on one page)", "formulas")
        + p("Copy this page into your formula book. Every numerical in the chapter is one of these lines.")
        + table(
            ["#", "Name", "Formula", "Notes"],
            [
                [
                    "1",
                    "Cost to capitalise",
                    "Purchase + freight + installation + non-refundable taxes − trade discount",
                    "Start of every question. GST claimed as input is not cost.",
                ],
                [
                    "2",
                    "Depreciable amount",
                    "Cost − Residual",
                    "The pie that SLM slices equally.",
                ],
                [
                    "3",
                    "SLM annual depreciation",
                    "(Cost − Residual) / Useful life in years",
                    "Same rupees every full year.",
                ],
                [
                    "4",
                    "SLM rate on original cost",
                    "(Annual depreciation / Cost) × 100",
                    "Never apply this rate to falling WDV.",
                ],
                [
                    "5",
                    "Part-year (both methods)",
                    "Full-year depreciation × (months used / 12)",
                    "From date put to use (or to date of sale). 1 Oct → 6/12; 1 Jul → 9/12; 1 Jan → 3/12.",
                ],
                [
                    "6",
                    "WDV depreciation",
                    "Opening WDV × Rate × (months / 12)",
                    "Year-1 opening WDV = Cost. Do not deduct scrap in the working.",
                ],
                [
                    "7",
                    "Closing WDV / NBV",
                    "Opening WDV − Depreciation of the period",
                    "Also = Cost − Accumulated depreciation.",
                ],
                [
                    "8",
                    "Accumulated depreciation",
                    "Sum of every charge from purchase up to today (including the current stub)",
                    "Contra-asset. Not cash. Not a replacement fund.",
                ],
                [
                    "9",
                    "WDV rate from scrap (rare)",
                    "R = 1 − (Scrap / Cost)<sup>(1/n)</sup>",
                    "Only if life and scrap are given and the rate is not. MBA usually gives the rate.",
                ],
                [
                    "10",
                    "Profit / (Loss) on sale",
                    "Sale proceeds − NBV on the date of sale",
                    "Positive = profit (credit). Negative = loss (debit). Depreciate first.",
                ],
                [
                    "11",
                    "Sale entry (provision method) identity",
                    "Bank + Accum. dep. + Loss = Cost + Profit",
                    "Exactly one of Loss or Profit is present. The two sides equal cost ± the result.",
                ],
            ],
            caption="Depreciation formula sheet — twelve identities, one chapter",
        )
        + formula(
            "Indian FY month-count (year-end 31 March): "
            "1 April = 12/12 &nbsp;|&nbsp; 1 July = 9/12 &nbsp;|&nbsp; 1 October = 6/12 &nbsp;|&nbsp; 1 January = 3/12",
            "Life in years is a clock from the date put to use. A 4-year life from 1 July 2023 ends 30 June 2027 "
            "(a 3-month stub in the fifth financial year), not on 31 March of the fourth financial year.",
        )
        + keypoint(
            "Method flags: “on cost / original cost / equal / straight line / fixed instalment” = SLM. "
            "“on WDV / book value / diminishing / reducing / written down” = WDV. "
            "Journals do not change with the method — only the amount does."
        )
    )


# ---------------------------------------------------------------------------
# Theory Q&A
# ---------------------------------------------------------------------------
def _theory_qna() -> str:
    return (
        h2("13. Theory answers in exam English", "theory")
        + p(
            "Numericals score method marks even when the last rupee is slightly off. "
            "Theory scores nothing if you write “depreciation is fall in value” and sit down. "
            "Learn these four as they stand."
        )
        + qna(
            "Define depreciation. Why is it charged even if the market price of the asset has increased? (4–6 marks)",
            exam_answer(
                "Depreciation is the systematic allocation of the depreciable amount (cost less residual value) "
                "of a tangible fixed asset over its useful life. It is a non-cash expense. "
                "It is charged even if market price has increased because depreciation is not an attempt to track "
                "market value. It is an allocation of historical cost to the periods that used the asset (matching). "
                "The Balance Sheet figure is unexpired cost, not a valuation. A rise in the property market may be "
                "relevant to a revaluation discussion, but it does not cancel the fact that part of the original cost "
                "has been consumed in earning this year’s revenue."
            ),
            "6 marks",
        )
        + qna(
            "State five reasons for providing depreciation. (5 marks)",
            exam_answer(
                "(i) To ascertain true profit by matching expired cost against the period’s revenue. "
                "(ii) To state the asset at a true amount (cost less accumulated depreciation) so that the Balance Sheet "
                "is not overstated. "
                "(iii) To retain a portion of profit in the business which may, in principle, support replacement — "
                "though a separate cash fund is created only if management invests it. "
                "(iv) To present a true and fair view as required by company law. "
                "(v) Because the cost of a fixed asset is a prepaid bundle of services that must be opened year by year."
            ),
            "5 marks",
        )
        + qna(
            "Distinguish between the Straight Line Method and the Written Down Value Method. (6–8 marks)",
            p("Write the comparison table from Section 8 in sentences:")
            + exam_answer(
                "SLM charges a constant amount each full year, computed as (Cost − Residual) / Life, and the rate "
                "(if expressed) is on original cost; book value falls in a straight line and equals residual at the end "
                "of life. WDV charges a constant rate on the book value brought forward, so the rupee amount falls each "
                "year; residual is not deducted annually, and book value equals residual only if the rate was derived "
                "from R = 1 − (S/C)<sup>1/n</sup>. SLM suits assets of even service such as buildings; WDV suits plant "
                "and electronics that lose more usefulness early. Early-year profits are lower under WDV. Journals are "
                "the same shape; only the amount differs."
            ),
            "8 marks",
        )
        + qna(
            "Is depreciation a source of funds? Is accumulated depreciation cash kept aside for replacement? (4 marks)",
            exam_answer(
                "No, and no. Depreciation is a non-cash expense. It reduces reported profit without reducing cash this year "
                "(the cash left when the asset was purchased). In a funds-flow or cash-flow statement we add it back to "
                "profit to undo that non-cash deduction — that is a working, not evidence that depreciation “generated” cash. "
                "Accumulated depreciation is a contra-asset, a running total of expired cost. It becomes a replacement "
                "fund only if the business separately withdraws cash and invests it. Most businesses do not; the cash "
                "from operations is free to be spent on anything."
            ),
            "4 marks",
        )
        + qna(
            "From which date is depreciation charged, and how is a part year computed? (3 marks)",
            exam_answer(
                "Depreciation is charged from the date the asset is put to use, not from the date of order. "
                "A part year is computed as Full-year depreciation × (number of months used / 12). "
                "When books close on 31 March, an asset put to use on 1 October is charged for 6 months; "
                "on 1 July, 9 months; on 1 January, 3 months; on 1 April, a full year. "
                "In the year of sale, charge up to the date of sale by the same fraction, then compute profit or loss on the NBV of that date."
            ),
            "3 marks",
        )
    )


if __name__ == "__main__":
    html = body()
    print(f"ch03 ok: {len(html)} chars, {html.count('<h2')} h2s, {html.count('example')} example-markers")
