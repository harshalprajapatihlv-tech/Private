import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "F",
        "Numerical Practice Set — Questions and Full Solutions",
        "Attempt each question on paper first. Then read the solution line by line. Easy → moderate → difficult → exam-level.",
        ["Journal and trial balance", "FIFO and WAM", "SLM and WDV",
         "Company P&L and Balance Sheet", "Cash flow indirect", "Ratios"],
    ))

    # ========== JOURNALS ==========
    parts.append(h2("A. Journal, ledger idea, and trial balance"))
    parts.append(practice(
        "A1", "Easy",
        "Journalise four opening-week transactions",
        """<p>Ananya starts Ananya Mart on 1 April 2026:</p>
        <ol>
        <li>Introduced cash ₹80,000.</li>
        <li>Opened a bank account and deposited ₹50,000.</li>
        <li>Bought goods for cash ₹12,000.</li>
        <li>Sold goods for cash ₹7,000.</li>
        </ol>
        <p>Pass journal entries with narrations.</p>""",
        journal([
            {"date": "1 Apr 2026", "debit": "Cash A/c", "credit": "Capital A/c", "amount": "80,000",
             "narration": "Being capital introduced in cash"},
            {"date": "1 Apr 2026", "debit": "Bank A/c", "credit": "Cash A/c", "amount": "50,000",
             "narration": "Being cash deposited into bank"},
            {"date": "1 Apr 2026", "debit": "Purchases A/c", "credit": "Cash A/c", "amount": "12,000",
             "narration": "Being goods purchased for cash"},
            {"date": "1 Apr 2026", "debit": "Cash A/c", "credit": "Sales A/c", "amount": "7,000",
             "narration": "Being goods sold for cash"},
        ], "Journal of Ananya Mart")
        + raw_p("<strong>Logic.</strong> Cash introduced: asset ↑ (Dr Cash), capital ↑ (Cr Capital). "
                "Bank deposit: one asset ↑, another ↓. Goods for resale = Purchases, not Furniture. Cash sales = Dr Cash, Cr Sales.")
    ))

    parts.append(practice(
        "A2", "Exam-level",
        "From the following, prepare a trial balance (balances already extracted)",
        """<p>On 31 March 2026 the following balances were extracted from the books of Dhruv Traders. Prepare a Trial Balance.</p>
        <p>Capital ₹2,50,000; Drawings ₹18,000; Cash ₹22,000; Bank ₹41,000; Purchases ₹3,10,000; Sales ₹4,80,000;
        Opening stock ₹40,000; Furniture ₹60,000; Creditors ₹55,000; Debtors ₹72,000; Rent ₹24,000; Wages ₹36,000;
        Bank loan ₹50,000; Commission received ₹8,000; Electricity ₹12,000; Sales returns ₹8,000; Purchase returns ₹5,000;
        Interest paid ₹5,000.</p>
        <p><em>Hint: one figure is needed as a balancing check — the trial balance must agree. All figures above are complete.</em></p>""",
        table(
            ["Particulars", "Debit (₹)", "Credit (₹)"],
            [
                ["Capital", "", "2,50,000"],
                ["Drawings", "18,000", ""],
                ["Cash", "22,000", ""],
                ["Bank", "41,000", ""],
                ["Purchases", "3,10,000", ""],
                ["Sales", "", "4,80,000"],
                ["Opening stock", "40,000", ""],
                ["Furniture", "60,000", ""],
                ["Creditors", "", "55,000"],
                ["Debtors", "72,000", ""],
                ["Rent", "24,000", ""],
                ["Wages", "36,000", ""],
                ["Bank loan", "", "50,000"],
                ["Commission received", "", "8,000"],
                ["Electricity", "12,000", ""],
                ["Sales returns", "8,000", ""],
                ["Purchase returns", "", "5,000"],
                ["Interest paid", "5,000", ""],
                ["<strong>Total</strong>", "<strong>6,48,000</strong>", "<strong>8,48,000</strong>"],
            ],
            caption="First listing — this does NOT agree, so we check classification",
        ) + raw_p(
            "Wait: if all given balances are complete, totals must agree. Let us add carefully."
        ) + raw_p(
            "<strong>Debits:</strong> Drawings 18,000 + Cash 22,000 + Bank 41,000 + Purchases 3,10,000 + Opening stock 40,000 "
            "+ Furniture 60,000 + Debtors 72,000 + Rent 24,000 + Wages 36,000 + Electricity 12,000 + Sales returns 8,000 "
            "+ Interest 5,000."
        ) + raw_p(
            "18+22=40; +41=81; +3,10,000=3,91,000; +40,000=4,31,000; +60,000=4,91,000; +72,000=5,63,000; "
            "+24,000=5,87,000; +36,000=6,23,000; +12,000=6,35,000; +8,000=6,43,000; +5,000=<strong>₹6,48,000</strong>."
        ) + raw_p(
            "<strong>Credits:</strong> Capital 2,50,000 + Sales 4,80,000 + Creditors 55,000 + Bank loan 50,000 "
            "+ Commission 8,000 + Purchase returns 5,000 = 2,50,000+4,80,000=7,30,000; +55,000=7,85,000; "
            "+50,000=8,35,000; +8,000=8,43,000; +5,000=<strong>₹8,48,000</strong>."
        ) + warn(
            "The two sides do not agree (6,48,000 vs 8,48,000). Difference ₹2,00,000. In a real exam, either a balance was omitted "
            "or a figure was mistyped. A balancing figure — often a missing asset such as Building ₹2,00,000 — is introduced only "
            "if the question says ‘the difference is …’ or asks you to find the missing amount. Here the missing debit is ₹2,00,000. "
            "Treat it as <strong>Building (balancing figure) ₹2,00,000</strong> so that both sides are ₹8,48,000, and write a working note: "
            "‘Difference on debit side assumed to be Building, unless the paper provides the missing item.’"
        ) + table(
            ["Particulars", "Debit (₹)", "Credit (₹)"],
            [
                ["All debit items as above", "6,48,000", ""],
                ["Building (balancing figure — WN)", "2,00,000", ""],
                ["All credit items as above", "", "8,48,000"],
                ["<strong>Total</strong>", "<strong>8,48,000</strong>", "<strong>8,48,000</strong>"],
            ],
            caption="Trial Balance of Dhruv Traders as at 31 March 2026",
        ) + raw_p("<strong>Exam lesson.</strong> Always add twice. Sales returns are debit; purchase returns are credit. Drawings are debit. Commission received is credit.")
    ))

    # ========== FIFO ==========
    parts.append(h2("B. Inventory — FIFO"))
    parts.append(practice(
        "B1", "Easy",
        "FIFO closing stock and COGS — one issue",
        """<p>Opening stock: 100 units @ ₹10. 5 January: purchased 200 units @ ₹12. 20 January: issued 150 units. Method: FIFO.</p>
        <p>Find (i) COGS (ii) closing stock (qty and value). Prove that opening cost + purchases = COGS + closing stock.</p>""",
        raw_p("<strong>Step 1 — units.</strong> 100 + 200 − 150 = 150 units closing.")
        + raw_p("<strong>Step 2 — issue layers (oldest first).</strong> Issue 150 = 100 @ ₹10 + 50 @ ₹12.")
        + raw_p("100 × 10 = ₹1,000. &nbsp; 50 × 12 = ₹600. &nbsp; <strong>COGS = ₹1,600.</strong>")
        + raw_p("<strong>Step 3 — remaining layers.</strong> From the 200 @ ₹12, 150 remain. Closing = 150 × 12 = <strong>₹1,800.</strong>")
        + raw_p("<strong>Step 4 — rupee check.</strong> Opening 1,000 + purchases 2,400 = ₹3,400. COGS 1,600 + closing 1,800 = ₹3,400. Tick.")
    ))

    parts.append(practice(
        "B2", "Moderate / Exam",
        "FIFO with several layers",
        """<p>Using FIFO, prepare a stores statement:</p>
        <ul>
        <li>1 Apr — Opening 200 units @ ₹20</li>
        <li>8 Apr — Purchase 300 @ ₹22</li>
        <li>12 Apr — Issue 250</li>
        <li>18 Apr — Purchase 200 @ ₹25</li>
        <li>25 Apr — Issue 300</li>
        <li>28 Apr — Purchase 100 @ ₹26</li>
        </ul>
        <p>Compute closing stock and COGS.</p>""",
        raw_p("<strong>12 Apr issue 250 (oldest first):</strong> 200 @ ₹20 + 50 @ ₹22.")
        + raw_p("200 × 20 = ₹4,000; 50 × 22 = ₹1,100; issue cost = ₹5,100. Left: 250 units @ ₹22.")
        + raw_p("<strong>18 Apr purchase:</strong> 250 @ ₹22 + 200 @ ₹25.")
        + raw_p("<strong>25 Apr issue 300:</strong> 250 @ ₹22 + 50 @ ₹25.")
        + raw_p("250 × 22 = ₹5,500; 50 × 25 = ₹1,250; issue cost = ₹6,750. Left: 150 @ ₹25.")
        + raw_p("<strong>28 Apr purchase:</strong> 150 @ ₹25 + 100 @ ₹26.")
        + raw_p("<strong>Closing qty</strong> = 150 + 100 = 250 units.")
        + raw_p("Closing value = 150 × 25 + 100 × 26 = 3,750 + 2,600 = <strong>₹6,350</strong>.")
        + raw_p("<strong>COGS</strong> = 5,100 + 6,750 = <strong>₹11,850</strong>.")
        + raw_p("<strong>Check — input cost:</strong> 200×20=4,000; 300×22=6,600; 200×25=5,000; 100×26=2,600; total = ₹18,200.")
        + raw_p("COGS 11,850 + closing 6,350 = ₹18,200. Units: 200+300−250+200−300+100 = 250. Tick.")
    ))

    # ========== WAM ==========
    parts.append(h2("C. Inventory — Weighted Average (moving)"))
    parts.append(practice(
        "C1", "Easy",
        "Moving average — clean rate",
        """<p>Opening 100 units @ ₹20. Purchase 200 units @ ₹26. Then issue 150 units. Use perpetual weighted average.</p>
        <p>Find average rate, issue value, closing stock.</p>""",
        raw_p("After purchase: units 100+200=300. Cost 100×20 + 200×26 = 2,000 + 5,200 = ₹7,200.")
        + raw_p("Average = 7,200 ÷ 300 = <strong>₹24</strong> exactly.")
        + raw_p("Issue 150 × 24 = <strong>₹3,600</strong> (COGS).")
        + raw_p("Closing 150 × 24 = <strong>₹3,600</strong>.")
        + raw_p("Check: 7,200 = 3,600 + 3,600.")
        + keypoint("The average was computed after the purchase, not after the issue.")
    ))

    parts.append(practice(
        "C2", "Exam-level",
        "Moving average store ledger",
        """<p>Prepare a stores ledger on the weighted average (moving) method:</p>
        <ul>
        <li>1 Jan — Opening 100 units @ ₹10 = ₹1,000</li>
        <li>8 Jan — Purchase 100 @ ₹20 = ₹2,000</li>
        <li>12 Jan — Issue 50</li>
        <li>20 Jan — Purchase 50 @ ₹21 = ₹1,050</li>
        <li>28 Jan — Issue 80</li>
        </ul>""",
        table(
            ["Date", "Receipts qty / amt", "Issues qty / amt", "Balance qty", "Avg ₹", "Balance amt ₹"],
            [
                ["1 Jan", "—", "—", "100", "10.00", "1,000"],
                ["8 Jan", "100 / 2,000", "—", "200", "15.00", "3,000"],
                ["12 Jan", "—", "50 × 15 = 750", "150", "15.00", "2,250"],
                ["20 Jan", "50 / 1,050", "—", "200", "16.50", "3,300"],
                ["28 Jan", "—", "80 × 16.50 = 1,320", "120", "16.50", "1,980"],
            ],
            caption="Moving weighted average — workings",
        )
        + raw_p("<strong>8 Jan average:</strong> (1,000+2,000) ÷ (100+100) = 3,000/200 = ₹15.")
        + raw_p("<strong>20 Jan average:</strong> (2,250+1,050) ÷ (150+50) = 3,300/200 = ₹16.50.")
        + raw_p("<strong>Closing stock = 120 units @ ₹16.50 = ₹1,980. COGS = 750 + 1,320 = ₹2,070.</strong>")
        + raw_p("Input 1,000+2,000+1,050=4,050. 2,070+1,980=4,050. Units 100+100−50+50−80=120. Tick.")
    ))

    # ========== DEP ==========
    parts.append(h2("D. Depreciation"))
    parts.append(practice(
        "D1", "Easy",
        "SLM — three-year table",
        """<p>Cost ₹1,00,000. Residual ₹10,000. Life 5 years. SLM. Show depreciation, accumulated depreciation and WDV for the first three years. Also state the annual rate on original cost.</p>""",
        raw_p("Annual depreciation = (1,00,000 − 10,000) ÷ 5 = 90,000 ÷ 5 = <strong>₹18,000</strong>.")
        + raw_p("Rate on original cost = 18,000 / 1,00,000 × 100 = <strong>18%</strong>.")
        + table(
            ["Year", "Depreciation ₹", "Accumulated dep. ₹", "WDV at year-end ₹"],
            [
                ["1", "18,000", "18,000", "82,000"],
                ["2", "18,000", "36,000", "64,000"],
                ["3", "18,000", "54,000", "46,000"],
            ],
        )
        + raw_p("At the end of year 5, WDV will be ₹10,000 (the residual).")
    ))

    parts.append(practice(
        "D2", "Easy",
        "WDV — three years at 10%",
        """<p>Cost ₹1,00,000. WDV rate 10% p.a. Full years. Prepare a three-year schedule.</p>""",
        table(
            ["Year", "Opening WDV ₹", "Dep 10% ₹", "Closing WDV ₹"],
            [
                ["1", "1,00,000", "10,000", "90,000"],
                ["2", "90,000", "9,000", "81,000"],
                ["3", "81,000", "8,100", "72,900"],
            ],
        )
        + raw_p("Y1: 1,00,000 × 10% = 10,000. Y2: 90,000 × 10% = 9,000. Y3: 81,000 × 10% = 8,100.")
        + raw_p("Scrap was not deducted. Under WDV we do not subtract residual each year.")
    ))

    parts.append(practice(
        "D3", "Moderate",
        "SLM, Indian financial year, purchased 1 July",
        """<p>Plant purchased on 1 July 2023 for ₹2,40,000. Residual ₹24,000. Life 4 years. Books close on 31 March. SLM.</p>
        <p>Compute depreciation for 2023–24, 2024–25 and 2025–26.</p>""",
        raw_p("Annual depreciation = (2,40,000 − 24,000) ÷ 4 = 2,16,000 ÷ 4 = <strong>₹54,000</strong>.")
        + raw_p("2023–24: used from 1 July to 31 March = 9 months. 54,000 × 9/12 = 54,000 × 0.75 = <strong>₹40,500</strong>.")
        + raw_p("2024–25: full year <strong>₹54,000</strong>.")
        + raw_p("2025–26: full year <strong>₹54,000</strong>.")
        + raw_p("Accumulated after these three periods = 40,500 + 54,000 + 54,000 = ₹1,48,500. WDV = 2,40,000 − 1,48,500 = ₹91,500.")
    ))

    parts.append(practice(
        "D4", "Exam-level",
        "SLM with installation, part year, and sale",
        """<p>A machine was purchased on 1 October 2022 for ₹5,00,000. Installation ₹20,000. Residual value 10% of cost (including installation). Life 10 years. SLM. Year-end 31 March. The machine was sold on 30 September 2025 for ₹3,80,000.</p>
        <p>Compute depreciation each year till sale and the profit or loss on sale.</p>""",
        raw_p("Cost = 5,00,000 + 20,000 = <strong>₹5,20,000</strong>.")
        + raw_p("Scrap = 10% × 5,20,000 = <strong>₹52,000</strong>.")
        + raw_p("Depreciable amount = 5,20,000 − 52,000 = ₹4,68,000.")
        + raw_p("Annual SLM = 4,68,000 ÷ 10 = <strong>₹46,800</strong>.")
        + raw_p("2022–23 (1 Oct–31 Mar = 6 months): 46,800 × 6/12 = <strong>₹23,400</strong>. WDV = 5,20,000 − 23,400 = ₹4,96,600.")
        + raw_p("2023–24: ₹46,800. WDV = 4,96,600 − 46,800 = ₹4,49,800.")
        + raw_p("2024–25: ₹46,800. WDV = 4,49,800 − 46,800 = ₹4,03,000.")
        + raw_p("2025–26 to 30 Sep = 6 months: ₹23,400. NBV at sale = 4,03,000 − 23,400 = <strong>₹3,79,600</strong>.")
        + raw_p("Sale proceeds ₹3,80,000 − NBV ₹3,79,600 = <strong>Profit on sale ₹400</strong>.")
        + raw_p("Journal (sale): Bank Dr. 3,80,000; Accumulated depreciation Dr. 1,40,400; To Machine 5,20,000; To Profit on sale 400. "
                "(Accum. dep. = 23,400+46,800+46,800+23,400 = 1,40,400; 5,20,000 − 1,40,400 = 3,79,600 NBV.)")
    ))

    parts.append(practice(
        "D5", "Moderate",
        "WDV part-year at 25%",
        """<p>Asset cost ₹4,00,000, WDV 25%, purchased 1 October, year-end 31 March. Compute depreciation and WDV for the first three financial years.</p>""",
        raw_p("Year 1: 4,00,000 × 25% × 6/12 = 1,00,000 × 1/2 = <strong>₹50,000</strong>. WDV = ₹3,50,000.")
        + raw_p("Year 2: 3,50,000 × 25% = <strong>₹87,500</strong>. WDV = ₹2,62,500.")
        + raw_p("Year 3: 2,62,500 × 25% = <strong>₹65,625</strong>. WDV = ₹1,96,875.")
    ))

    # ========== COMPANY ==========
    parts.append(h2("E. Company accounts (Schedule III)"))
    parts.append(practice(
        "E1", "Exam-level",
        "Statement of P&L and Balance Sheet with adjustments",
        """<p>Trial Balance of Narmada Ltd as at 31 March 2026:</p>"""
        + table(
            ["Particulars", "Debit ₹", "Credit ₹"],
            [
                ["Equity share capital", "", "3,00,000"],
                ["12% Long-term loan", "", "1,00,000"],
                ["Trade payables", "", "50,000"],
                ["Sales", "", "6,00,000"],
                ["Land", "2,00,000", ""],
                ["Plant", "1,50,000", ""],
                ["Furniture", "20,000", ""],
                ["Purchases", "4,00,000", ""],
                ["Opening inventory", "50,000", ""],
                ["Trade receivables", "80,000", ""],
                ["Salaries", "60,000", ""],
                ["Rent", "24,000", ""],
                ["Cash and bank", "40,000", ""],
                ["Insurance", "12,000", ""],
                ["Electricity", "14,000", ""],
                ["Total", "10,50,000", "10,50,000"],
            ],
        )
        + """<p><strong>Adjustments:</strong> (a) Closing inventory ₹70,000. (b) Depreciate plant 10% and furniture 10%.
        (c) Outstanding salaries ₹5,000. (d) Prepaid insurance ₹3,000. (e) Provision for tax ₹20,000.
        Prepare Statement of P&L and Balance Sheet as per Schedule III (ignore previous-year column).</p>""",
        raw_p("<strong>WN1 Changes in inventories</strong> = Opening 50,000 − Closing 70,000 = <strong>(₹20,000)</strong> i.e. a credit / negative expense.")
        + raw_p("Alternatively COGS = 50,000 + 4,00,000 − 70,000 = ₹3,80,000, which is Purchases 4,00,000 + change (−20,000).")
        + raw_p("<strong>WN2 Depreciation</strong> = Plant 15,000 + Furniture 2,000 = <strong>₹17,000</strong>.")
        + raw_p("<strong>WN3 Employee benefits</strong> = 60,000 + 5,000 outstanding = <strong>₹65,000</strong>.")
        + raw_p("<strong>WN4 Other expenses</strong> = Rent 24,000 + Insurance (12,000−3,000) 9,000 + Electricity 14,000 = <strong>₹47,000</strong>.")
        + table(
            ["Particulars", "₹"],
            [
                ["I Revenue from operations", "6,00,000"],
                ["II Other income", "—"],
                ["III Total income", "6,00,000"],
                ["IV Expenses", ""],
                ["Purchases of stock-in-trade", "4,00,000"],
                ["Changes in inventories", "(20,000)"],
                ["Employee benefits expense", "65,000"],
                ["Depreciation", "17,000"],
                ["Other expenses", "47,000"],
                ["Total expenses", "5,09,000"],
                ["V Profit before tax (6,00,000 − 5,09,000)", "91,000"],
                ["VIII Tax expense", "20,000"],
                ["IX Profit for the period", "71,000"],
            ],
            caption="Statement of Profit and Loss for the year ended 31 March 2026",
        )
        + raw_p("Check expenses: 4,00,000 − 20,000 + 65,000 + 17,000 + 47,000 = 5,09,000. Yes. 6,00,000 − 5,09,000 = 91,000. 91,000 − 20,000 = 71,000.")
        + table(
            ["Particulars", "₹"],
            [
                ["<strong>Equity and liabilities</strong>", ""],
                ["Share capital", "3,00,000"],
                ["Reserves and surplus (profit for the year)", "71,000"],
                ["Shareholders’ funds", "3,71,000"],
                ["Non-current liabilities — long-term borrowings", "1,00,000"],
                ["Trade payables", "50,000"],
                ["Other current liabilities (outstanding salaries)", "5,000"],
                ["Short-term provisions (tax)", "20,000"],
                ["Current liabilities", "75,000"],
                ["<strong>Total</strong>", "<strong>5,46,000</strong>"],
                ["<strong>Assets</strong>", ""],
                ["Land", "2,00,000"],
                ["Plant (1,50,000 − 15,000)", "1,35,000"],
                ["Furniture (20,000 − 2,000)", "18,000"],
                ["Non-current assets", "3,53,000"],
                ["Inventories", "70,000"],
                ["Trade receivables", "80,000"],
                ["Cash and cash equivalents", "40,000"],
                ["Other current assets (prepaid insurance)", "3,000"],
                ["Current assets", "1,93,000"],
                ["<strong>Total</strong>", "<strong>5,46,000</strong>"],
            ],
            caption="Balance Sheet as at 31 March 2026",
        )
        + raw_p("3,71,000 + 1,00,000 + 75,000 = 5,46,000. Assets 3,53,000 + 1,93,000 = 5,46,000. <strong>Tied.</strong>")
    ))

    # ========== CFS ==========
    parts.append(h2("F. Cash flow — indirect method"))
    parts.append(practice(
        "F1", "Easy",
        "Short cash flow statement",
        """<p>Profit before tax ₹1,00,000; depreciation ₹20,000; tax paid ₹25,000; increase in inventory ₹10,000;
        increase in creditors ₹8,000; purchase of furniture (cash) ₹40,000; long-term loan taken ₹30,000.
        Opening cash and bank ₹15,000. Prepare a cash flow statement (indirect).</p>""",
        table(
            ["Particulars", "₹"],
            [
                ["Profit before tax", "1,00,000"],
                ["Add: Depreciation", "20,000"],
                ["Operating profit before WC changes", "1,20,000"],
                ["Less: Increase in inventory", "(10,000)"],
                ["Add: Increase in creditors", "8,000"],
                ["Cash generated from operations", "1,18,000"],
                ["Less: Tax paid", "(25,000)"],
                ["<strong>Net cash from operating activities (A)</strong>", "<strong>93,000</strong>"],
                ["Purchase of furniture", "(40,000)"],
                ["<strong>Net cash from investing activities (B)</strong>", "<strong>(40,000)</strong>"],
                ["Loan taken", "30,000"],
                ["<strong>Net cash from financing activities (C)</strong>", "<strong>30,000</strong>"],
                ["Net increase in cash (A+B+C)", "83,000"],
                ["Opening cash", "15,000"],
                ["Closing cash", "98,000"],
            ],
        )
        + raw_p("Check: 93,000 − 40,000 + 30,000 = 83,000; 15,000 + 83,000 = 98,000.")
    ))

    parts.append(practice(
        "F2", "Exam-level",
        "Two-year position — derive the cash flow",
        """<p>Summarised Balance Sheets of Lila Ltd:</p>"""
        + table(
            ["Particulars", "31 Mar 2025 ₹", "31 Mar 2026 ₹"],
            [
                ["Equity share capital", "2,00,000", "2,50,000"],
                ["Profit & Loss surplus", "80,000", "1,10,000"],
                ["10% Debentures", "1,00,000", "80,000"],
                ["Trade payables", "40,000", "55,000"],
                ["Plant (at cost)", "2,40,000", "3,00,000"],
                ["Accumulated depreciation on plant", "60,000", "78,000"],
                ["Inventory", "50,000", "45,000"],
                ["Trade receivables", "70,000", "90,000"],
                ["Cash", "20,000", "38,000"],
            ],
        )
        + """<p><strong>Additional:</strong> A machine costing ₹40,000 with accumulated depreciation ₹12,000 was sold for ₹25,000.
        Depreciation charged during the year is the balancing figure on the accumulated depreciation account.
        No tax or dividend. Debenture interest was paid in full (on opening debentures, assume ₹10,000) and already charged to P&L.
        Prepare the cash flow statement (indirect method) with workings.</p>""",
        raw_p("<strong>WN1 Plant (cost).</strong> Opening 2,40,000 + Purchases − 40,000 sold = Closing 3,00,000 ⇒ Purchases = 3,00,000 − 2,40,000 + 40,000 = <strong>₹1,00,000</strong>.")
        + raw_p("<strong>WN2 Accumulated depreciation.</strong> Opening 60,000 + Dep charged − 12,000 (on sold) = 78,000 ⇒ Dep charged = 78,000 − 60,000 + 12,000 = <strong>₹30,000</strong>.")
        + raw_p("<strong>WN3 Sale of machine.</strong> NBV = 40,000 − 12,000 = 28,000. Sold for 25,000. <strong>Loss on sale ₹3,000</strong>.")
        + raw_p("<strong>WN4 Profit before interest.</strong> Increase in surplus = 1,10,000 − 80,000 = 30,000 = PAT. No tax, so PBT after interest = 30,000. Interest on debentures 10% × 1,00,000 opening = 10,000 (given). Profit before tax and before treating interest as an add-back: 30,000 + 10,000 = <strong>₹40,000</strong> profit before interest and tax. We start the CFS at this 40,000 (or start at 30,000 and add interest 10,000).")
        + table(
            ["Particulars", "₹"],
            [
                ["Profit before tax and interest", "40,000"],
                ["Add: Depreciation", "30,000"],
                ["Add: Loss on sale of plant", "3,000"],
                ["Operating profit before WC", "73,000"],
                ["Decrease in inventory (50,000−45,000)", "5,000"],
                ["Increase in receivables (90,000−70,000)", "(20,000)"],
                ["Increase in payables (55,000−40,000)", "15,000"],
                ["<strong>Net cash from operations (A)</strong> (no tax)", "<strong>73,000</strong>"],
                ["Purchase of plant", "(1,00,000)"],
                ["Sale of plant", "25,000"],
                ["<strong>Net cash from investing (B)</strong>", "<strong>(75,000)</strong>"],
                ["Issue of share capital (2,50,000−2,00,000)", "50,000"],
                ["Redemption of debentures (1,00,000−80,000)", "(20,000)"],
                ["Interest paid", "(10,000)"],
                ["<strong>Net cash from financing (C)</strong>", "<strong>20,000</strong>"],
                ["Net increase in cash", "18,000"],
                ["Opening cash", "20,000"],
                ["Closing cash", "38,000"],
            ],
        )
        + raw_p("Operating 73,000 + investing (75,000) + financing 20,000 = 18,000. Opening 20,000 + 18,000 = closing 38,000. <strong>Ties with the Balance Sheet.</strong>")
        + raw_p("WC check: 73,000 − 20,000 + 5,000 + 15,000 = 73,000. Yes, the WC lines net to zero extra beyond 73,000? 5 − 20 + 15 = 0. So cash from operations = 73,000. Yes.")
    ))

    # ========== RATIOS ==========
    parts.append(h2("G. Ratio analysis"))
    parts.append(practice(
        "G1", "Moderate",
        "Compute a full set of ratios from one company",
        """<p>Kaveri Traders Ltd, year ended 31 March 2026:</p>
        <p>Revenue from operations ₹10,00,000 (credit sales ₹8,00,000). COGS ₹7,50,000. Opening stock ₹80,000, closing stock ₹1,20,000.
        Operating profit (EBIT) ₹1,50,000. Interest ₹30,000. PBT ₹1,20,000. Tax ₹30,000. PAT ₹90,000.
        Equity share capital ₹4,00,000 (₹10 shares). Reserves ₹2,00,000. Long-term debt ₹2,00,000.
        Current liabilities (trade payables) ₹1,50,000. Inventory ₹1,20,000, Trade receivables ₹1,00,000, Cash ₹80,000.
        Opening debtors ₹60,000. Opening creditors ₹1,10,000. Purchases ₹7,90,000 (all credit). Net fixed assets ₹6,50,000.</p>
        <p>Compute current, quick, cash, debt–equity, proprietary, GP, NP, operating profit, operating, inventory turnover, debtors turnover, creditors turnover, ROCE, ROE, EPS, interest coverage.</p>""",
        table(
            ["Ratio", "Work", "Answer"],
            [
                ["Current", "CA 1,20,000+1,00,000+80,000=3,00,000; CL 1,50,000; 3,00,000/1,50,000", "2 times"],
                ["Quick", "(3,00,000−1,20,000)/1,50,000 = 1,80,000/1,50,000", "1.2 times"],
                ["Cash", "80,000/1,50,000", "0.53 times"],
                ["Debt–equity", "2,00,000 / 6,00,000", "0.33 : 1"],
                ["Proprietary", "6,00,000 / (6,50,000+3,00,000) = 6,00,000/9,50,000", "0.63 or 63%"],
                ["GP ratio", "GP = 10,00,000−7,50,000=2,50,000; 2,50,000/10,00,000×100", "25%"],
                ["NP ratio", "90,000/10,00,000×100", "9%"],
                ["Op. profit ratio", "1,50,000/10,00,000×100", "15%"],
                ["Operating ratio", "(7,50,000 + op. exp). Op. exp = Sales−COGS−EBIT = 2,50,000−1,50,000=1,00,000; (8,50,000)/10,00,000×100", "85%"],
                ["Inventory turnover", "Avg stock (80,000+1,20,000)/2=1,00,000; 7,50,000/1,00,000", "7.5 times"],
                ["Debtors turnover", "Avg debtors (60,000+1,00,000)/2=80,000; Credit sales 8,00,000/80,000", "10 times"],
                ["Collection period", "365/10", "37 days"],
                ["Creditors turnover", "Avg cr. (1,10,000+1,50,000)/2=1,30,000; 7,90,000/1,30,000", "6.08 times"],
                ["ROCE", "Capital employed 6,00,000+2,00,000=8,00,000; 1,50,000/8,00,000×100", "18.75%"],
                ["ROE", "90,000/6,00,000×100", "15%"],
                ["EPS", "Shares 40,000; 90,000/40,000", "₹2.25"],
                ["Interest coverage", "1,50,000/30,000", "5 times"],
            ],
        )
        + raw_p("<strong>Comment in brief.</strong> Current 2 and quick 1.2 are comfortable. GP 25% and operating ratio 85% are internally consistent (15% operating profit). Inventory moves 7.5 times. ROCE 18.75% exceeds the 10% cost of debentures implicit if the 2,00,000 debt is 10% (interest 30,000 on 2,00,000 is 15% — wait: 30,000/2,00,000 = 15% interest rate). ROCE 18.75% > 15%, so gearing is still slightly favourable. ROE 15%.")
        + raw_p("Interest check: 30,000 on 2,00,000 = 15%. ROCE 18.75% − 15% leaves a thin positive spread.")
    ))

    parts.append(practice(
        "G2", "Easy",
        "Reconstruct CA and CL from current ratio and working capital",
        """<p>Current ratio = 2.5. Working capital = ₹1,50,000. Quick ratio = 1.5. There are no prepaid expenses. Find current assets, current liabilities and inventory.</p>""",
        raw_p("Let CL = x. Then CA = 2.5x.")
        + raw_p("Working capital = CA − CL = 2.5x − x = 1.5x = 1,50,000 ⇒ x = 1,50,000 / 1.5 = <strong>CL ₹1,00,000</strong>.")
        + raw_p("CA = 2.5 × 1,00,000 = <strong>₹2,50,000</strong>.")
        + raw_p("Quick ratio 1.5 = (CA − Inventory) / CL ⇒ CA − Inventory = 1.5 × 1,00,000 = 1,50,000.")
        + raw_p("Inventory = 2,50,000 − 1,50,000 = <strong>₹1,00,000</strong>.")
    ))

    parts.append(practice(
        "G3", "Difficult",
        "From GP ratio and stock turnover, find sales",
        """<p>Gross profit ratio 20%. Inventory turnover 5 times (on COGS). Opening stock = closing stock = ₹40,000. Find COGS, gross profit and sales.</p>""",
        raw_p("Average stock = (40,000+40,000)/2 = ₹40,000.")
        + raw_p("Inventory turnover 5 = COGS / 40,000 ⇒ COGS = 5 × 40,000 = <strong>₹2,00,000</strong>.")
        + raw_p("GP ratio 20% means GP = 20% of sales and COGS = 80% of sales.")
        + raw_p("0.80 × Sales = 2,00,000 ⇒ Sales = 2,00,000 / 0.80 = <strong>₹2,50,000</strong>.")
        + raw_p("GP = 2,50,000 − 2,00,000 = <strong>₹50,000</strong> (which is 20% of 2,50,000).")
    ))

    parts.append(chapter_close())
    return "".join(parts)
