import sys
sys.path.insert(0, "/workspace/notes")
from html_lib import *


def body() -> str:
    parts = []
    parts.append(chapter_open(
        "E",
        "Theory Question Bank with Answers",
        "Answers are written in examination tone: definition, points, tiny example, close. Adjust length to the marks.",
        ["1-mark", "Short 3-mark", "5-mark", "Long 8–10 mark"],
    ))
    parts.append(lead(
        "How to use this bank: cover the answer and write your own first. Then compare. 1-mark = one precise sentence. "
        "3-mark = definition + two points. 5-mark = definition + four or five explained points + example. "
        "Long = short intro, headed points, example, one limitation, conclusion."
    ))

    # ---------- Bootcamp / Ch1 ----------
    parts.append(h2("Bootcamp and Chapter 1 — Introduction to Accounting"))
    parts.append(h3("1-mark questions"))
    parts.append(qna("Define accounting.",
        "<p>Accounting is the process of identifying, measuring, recording, classifying, summarising, analysing and communicating financial information of a business to users for decision-making.</p>",
        "1"))
    parts.append(qna("State the accounting equation.",
        "<p>Assets = Liabilities + Capital.</p>", "1"))
    parts.append(qna("What is a business transaction?",
        "<p>A business transaction is a monetary event that changes the financial position of the business and is supported by evidence.</p>", "1"))
    parts.append(qna("Give the golden rule of nominal accounts.",
        "<p>Debit all expenses and losses; credit all incomes and gains.</p>", "1"))
    parts.append(qna("What is a journal?",
        "<p>The journal is the book of original entry in which transactions are recorded chronologically as debit and credit with narration.</p>", "1"))
    parts.append(qna("What is a trial balance?",
        "<p>A trial balance is a statement of all ledger account balances at a date, listed as debit or credit, to test the arithmetical accuracy of double entry.</p>", "1"))
    parts.append(qna("State the dual aspect concept.",
        "<p>Every transaction has two aspects — a debit and a credit of equal amount — so that Assets = Liabilities + Capital always holds.</p>", "1"))
    parts.append(qna("What are drawings?",
        "<p>Drawings are value withdrawn by the owner for personal use. They reduce capital and are not a business expense.</p>", "1"))

    parts.append(h3("Short answers (3 marks)"))
    parts.append(qna("Distinguish bookkeeping from accounting.",
        """<p><strong>Bookkeeping</strong> is the recording of transactions in the books (journal and ledger).
        <strong>Accounting</strong> includes bookkeeping and goes further: classifying, summarising into financial statements, analysing and interpreting.
        Bookkeeping is the foundation; accounting is the full language used by managers.</p>""", "3"))
    parts.append(qna("Explain the business entity concept with an example.",
        """<p>The business is treated as separate from its owner. Only business transactions are recorded in the business books.
        If Rahul starts a shop with ₹1,00,000, the shop records Cash Dr. and Capital Cr. If Rahul then pays his home electricity from the shop, it is drawings, not a shop expense.
        Without this concept, personal and business money would be mixed and profit would be meaningless.</p>""", "3"))
    parts.append(qna("Why is a trial balance prepared? State two limitations.",
        """<p><strong>Why:</strong> to check that total debits equal total credits after posting, and to assemble balances for preparing financial statements.</p>
        <p><strong>Limitations:</strong> (i) It does not catch errors of omission, principle, or compensating errors. (ii) Agreement of the trial balance does not guarantee that the books are correct — only that they are arithmetically balanced.</p>""", "3"))
    parts.append(qna("State three differences between journal and ledger.",
        """<p>(i) Journal is chronological; ledger is account-wise.<br/>
        (ii) Journal is the book of original entry; ledger is the book of principal entry / classified record.<br/>
        (iii) Journal does not show the closing balance of an account; the ledger is balanced and those balances go to the trial balance.</p>""", "3"))

    parts.append(h3("5-mark questions"))
    parts.append(qna("Explain the accounting equation with an example.",
        """<p>The accounting equation is <strong>Assets = Liabilities + Capital</strong>. It is the dual aspect concept in numbers: resources of the business are always equal to claims on those resources (outsiders + owner).</p>
        <p><strong>Example.</strong> Rahul starts with cash ₹1,00,000. Assets ₹1,00,000 = Capital ₹1,00,000. He buys furniture ₹20,000 cash: Cash falls, furniture rises; assets still ₹1,00,000. He buys stock ₹30,000 on credit: Assets ₹1,30,000 = Liabilities ₹30,000 + Capital ₹1,00,000. The equation holds after every transaction. Profit increases capital; drawings decrease it.</p>""",
        "5"))
    parts.append(qna("Explain any five accounting concepts.",
        """<p>(i) <strong>Entity</strong> — business separate from owner.<br/>
        (ii) <strong>Money measurement</strong> — only facts expressible in money are recorded (skill of a manager is not in the books).<br/>
        (iii) <strong>Going concern</strong> — the business is assumed to continue; assets are not all valued at fire-sale prices.<br/>
        (iv) <strong>Accrual</strong> — incomes and expenses are recognised when earned or incurred, not only when cash moves.<br/>
        (v) <strong>Prudence</strong> — anticipate losses, do not anticipate profits; stock at cost or NRV, whichever is lower.</p>
        <p>Each concept exists so that different accountants would, in similar situations, record in a comparable way.</p>""", "5"))
    parts.append(qna("What are the objectives and limitations of a trial balance?",
        """<p><strong>Objectives:</strong> (i) arithmetical check of double entry; (ii) source list of balances for Trading, P&L and Balance Sheet; (iii) locating some errors when totals disagree.</p>
        <p><strong>Limitations:</strong> it will still agree if a transaction is fully omitted, posted to the wrong account of the same side, recorded at the wrong amount on both sides, or offset by a compensating error. It is not proof of correctness, only of equality.</p>""", "5"))

    parts.append(h3("Long answer"))
    parts.append(qna("Describe the process from a transaction to the trial balance. Why is each stage needed?",
        """<p><strong>Introduction.</strong> Accounting converts business events into a trial of balances that can become financial statements. The chain is transaction → voucher → journal → ledger → trial balance.</p>
        <p><strong>Transaction and voucher.</strong> Only events that change value and have evidence enter the books. The voucher (invoice, cash memo, cheque leaf) is the proof.</p>
        <p><strong>Journal.</strong> Events are written in date order as equal debit and credit with a narration. This preserves the story of <em>when</em> and <em>why</em>.</p>
        <p><strong>Ledger.</strong> The same lines are sorted account-wise so we can see, for example, everything that happened to Bank or to Rent. Accounts are totalled and balanced.</p>
        <p><strong>Trial balance.</strong> All balances are listed. If total debits equal total credits, double entry has at least been arithmetically completed. Financial statements are then prepared from these balances plus adjustments.</p>
        <p><strong>Conclusion.</strong> Skipping the journal loses chronology; skipping the ledger loses a running picture of each account; skipping the trial balance hides posting errors until the Balance Sheet fails to tally.</p>""",
        "8–10"))

    # ---------- Ch2 ----------
    parts.append(h2("Chapter 2 — Inventory Valuation"))
    parts.append(h3("1-mark"))
    parts.append(qna("What is inventory for a trader?",
        "<p>Inventory (stock) is goods held for sale in the ordinary course of business, valued usually at cost or net realisable value, whichever is lower.</p>", "1"))
    parts.append(qna("State the FIFO rule in one sentence.",
        "<p>Goods purchased first are assumed to be issued or sold first, so closing stock consists of the most recent purchases.</p>", "1"))
    parts.append(qna("Give the formula for weighted average cost.",
        "<p>Weighted average cost = Total cost of goods available (opening + purchases) ÷ Total units available, recomputed after each purchase under the moving-average method.</p>", "1"))
    parts.append(qna("Write the COGS formula.",
        "<p>Cost of goods sold = Opening stock + Purchases + Direct expenses − Closing stock.</p>", "1"))
    parts.append(qna("Why is LIFO generally not used in India?",
        "<p>Accounting Standard 2 (and Ind AS 2) does not permit LIFO as an inventory cost formula.</p>", "1"))
    parts.append(qna("If closing stock is overvalued, what happens to profit?",
        "<p>Overvalued closing stock understates COGS and overstates profit of that year (and overstates current assets).</p>", "1"))

    parts.append(h3("3-mark"))
    parts.append(qna("Why is inventory valuation important?",
        """<p>Closing inventory appears in the Balance Sheet as a current asset and is deducted in arriving at COGS. A higher value raises profit and assets; a lower value does the opposite. Managers, lenders and tax authorities therefore need a consistent, prudent value — cost or NRV, whichever is lower — otherwise profit can be managed by merely changing the stock figure.</p>""", "3"))
    parts.append(qna("Distinguish FIFO and weighted average (any three points).",
        """<p>(i) FIFO issues oldest costs; WAM issues a blended cost.<br/>
        (ii) In a period of rising prices, FIFO closing stock is higher (latest costs remain) and profit is higher than under WAM.<br/>
        (iii) FIFO tracks layers; WAM tracks one average rate, recomputed after purchases (perpetual).</p>""", "3"))

    parts.append(h3("5-mark"))
    parts.append(qna("Explain FIFO with a small numerical illustration.",
        """<p>FIFO assumes the first goods purchased are the first goods sold. Remaining stock is the latest lots.</p>
        <p><strong>Illustration.</strong> Opening 100 units @ ₹10; purchase 200 @ ₹12; issue 150. Issue is 100 @ ₹10 + 50 @ ₹12 = ₹1,600 (COGS). Closing 150 @ ₹12 = ₹1,800. Check: 1,000 + 2,400 = 3,400 = 1,600 + 1,800.</p>""", "5"))
    parts.append(qna("Explain the weighted average method of inventory valuation.",
        """<p>Each unit in stock is treated as having the same average cost. After every purchase, a new average is computed: total rupees in hand ÷ total units in hand. Issues are valued at that average. The method smooths price changes and is permitted by AS-2. Care: the average is not recalculated at the time of an issue.</p>""", "5"))

    parts.append(h3("Long"))
    parts.append(qna("Discuss the need for inventory valuation and compare FIFO with the weighted average method.",
        """<p><strong>Need.</strong> Inventory is often a large current asset. Its value changes both the Balance Sheet and the profit for the year through COGS. Valuation must be consistent and prudent so that profit is not manipulated and so that comparisons across years remain meaningful. AS-2 requires valuation at cost or NRV, whichever is lower, and permits FIFO or weighted average as cost formulae.</p>
        <p><strong>FIFO.</strong> Logical physical flow for many traders. Closing stock approximates recent replacement cost. In inflation, profits look higher.</p>
        <p><strong>WAM.</strong> Simple when goods are mixed. Smooths unit cost. Closing stock and COGS sit between old and new prices.</p>
        <p><strong>Choice.</strong> Follow the question. If silent, state the assumption. Do not use LIFO in an Indian statutory setting.</p>
        <p><strong>Conclusion.</strong> The method must be disclosed and applied consistently (consistency convention).</p>""", "8–10"))

    # ---------- Ch3 ----------
    parts.append(h2("Chapter 3 — Depreciation"))
    parts.append(h3("1-mark"))
    parts.append(qna("Define depreciation.",
        "<p>Depreciation is the systematic allocation of the depreciable amount of a tangible fixed asset over its useful life.</p>", "1"))
    parts.append(qna("Give the SLM formula.",
        "<p>Annual depreciation = (Cost − Residual value) ÷ Useful life in years.</p>", "1"))
    parts.append(qna("Give the WDV formula.",
        "<p>Depreciation for the year = Book value of the asset at the beginning of the period × specified rate.</p>", "1"))
    parts.append(qna("Is depreciation a cash expense?",
        "<p>No. Depreciation is a non-cash expense. Cash left when the asset was purchased; each year we only allocate that old cost.</p>", "1"))
    parts.append(qna("Name two causes of depreciation.",
        "<p>Wear and tear from use, and obsolescence due to technology or fashion. (Also passage of time, depletion, accident.)</p>", "1"))
    parts.append(qna("What is residual value?",
        "<p>The estimated amount that the business expects to obtain from the asset at the end of its useful life, net of disposal costs.</p>", "1"))

    parts.append(h3("3-mark"))
    parts.append(qna("State three reasons for providing depreciation.",
        """<p>(i) To match the cost of the asset with the periods that benefit from it, so that profit is not overstated.<br/>
        (ii) To state the asset at a realistic amount (cost less accumulated depreciation) on the Balance Sheet.<br/>
        (iii) To retain profits in the business (depreciation reduces distributable profit), which may help replacement — though it does not by itself create a cash fund.</p>""", "3"))
    parts.append(qna("Distinguish SLM and WDV (three points).",
        """<p>(i) SLM charges a constant amount each full year; WDV charges a reducing amount.<br/>
        (ii) SLM applies the rate to original cost; WDV applies the rate to book value.<br/>
        (iii) SLM reaches residual value exactly at the end of life if estimates are correct; WDV approaches residual and is often used for assets that lose more value when new (vehicles, electronics).</p>""", "3"))

    parts.append(h3("5-mark"))
    parts.append(qna("Explain the straight line method of depreciation.",
        """<p>Under SLM, the depreciable amount (cost minus residual value) is spread equally over useful life. Annual depreciation = (Cost − Scrap) / Life. The charge is the same every full year, so profit is not distorted by a falling depreciation number. It is suitable for assets whose benefit is roughly even (buildings, furniture). For part of a year, charge months/12 of the annual amount. On the Balance Sheet the asset is shown at cost less accumulated depreciation.</p>""", "5"))
    parts.append(qna("Explain the written down value method of depreciation.",
        """<p>Each year a fixed percentage is applied to the book value (cost less depreciation already provided). The rupee charge is high in early years and low later. Residual value is not deducted each year; the rate is expected to leave a small book value. Suitable where repairs rise with age, so that depreciation + repairs stay more even, and for assets that become obsolete quickly. Part-year: apply rate × months/12 to the relevant book value.</p>""", "5"))

    parts.append(h3("Long"))
    parts.append(qna("What is depreciation? Why is it provided? Compare SLM and WDV.",
        """<p><strong>Meaning.</strong> Depreciation allocates the cost of a long-lived tangible asset over the years that consume its service potential. It is not a valuation of market price and it is not cash paid that year.</p>
        <p><strong>Why provided.</strong> Matching of cost to benefit; true and fair asset values; legal true-and-fair view; avoidance of overstated profit and over-distribution of dividends.</p>
        <p><strong>SLM vs WDV.</strong> Equal versus reducing charge; rate on cost versus rate on WDV; exact residual versus approaching residual; buildings versus plant that ages fast.</p>
        <p><strong>Example.</strong> Cost ₹1,00,000, scrap ₹10,000, life 5 years → SLM ₹18,000 every year. The same cost at 10% WDV → ₹10,000, ₹9,000, ₹8,100 …</p>
        <p><strong>Conclusion.</strong> The method should match the pattern of benefits and be applied consistently, with disclosure.</p>""", "8–10"))

    # ---------- Ch4 ----------
    parts.append(h2("Chapter 4 — Company Accounts"))
    parts.append(h3("1-mark"))
    parts.append(qna("What is Schedule III of the Companies Act, 2013?",
        "<p>Schedule III prescribes the format and presentation of the Balance Sheet and Statement of Profit and Loss (and related instructions) for companies in India.</p>", "1"))
    parts.append(qna("Name the two sides (major parts) of a company Balance Sheet.",
        "<p>Equity and Liabilities, and Assets.</p>", "1"))
    parts.append(qna("What is ‘other income’?",
        "<p>Income other than revenue from operations — for example interest, dividend, and profit on sale of investments or assets.</p>", "1"))
    parts.append(qna("Give two examples of current liabilities.",
        "<p>Trade payables; short-term borrowings; outstanding expenses; short-term provisions (any two).</p>", "1"))
    parts.append(qna("What are notes to accounts?",
        "<p>Notes are explanations, breakdowns and accounting-policy disclosures that support the face of the financial statements and form part of them.</p>", "1"))
    parts.append(qna("Classify outstanding salaries.",
        "<p>Other current liability (an accrued expense), not a trade payable unless the question groups it so.</p>", "1"))

    parts.append(h3("3-mark"))
    parts.append(qna("Why must companies prepare financial statements?",
        """<p>A company is a separate legal entity with shareholders who are not all managers. The Companies Act requires annual statements that give a true and fair view so that owners, lenders, tax authorities and regulators can assess performance and position. Format is standardised by Schedule III to aid comparison.</p>""", "3"))
    parts.append(qna("Distinguish current and non-current items.",
        """<p>An asset or liability is current if it is expected to be realised or settled within the company’s operating cycle or twelve months, or is held primarily for trading, or is cash. Other items are non-current (PPE, long-term loans, term loans not due within a year).</p>""", "3"))

    parts.append(h3("5-mark"))
    parts.append(qna("What is Schedule III? State the major heads of the Balance Sheet.",
        """<p>Schedule III to the Companies Act, 2013 is the legally prescribed presentation for company financial statements.</p>
        <p><strong>Equity and liabilities:</strong> Shareholders’ funds (share capital, reserves and surplus); share application money pending allotment; non-current liabilities (long-term borrowings, deferred tax, other long-term liabilities, long-term provisions); current liabilities (short-term borrowings, trade payables, other current liabilities, short-term provisions).</p>
        <p><strong>Assets:</strong> Non-current assets (PPE, intangibles, non-current investments, long-term loans and advances, other); current assets (inventories, trade receivables, cash and cash equivalents, short-term loans and advances, other current assets).</p>""", "5"))
    parts.append(qna("Explain the purpose of notes to accounts.",
        """<p>The face of the P&L and Balance Sheet would be unreadable if every breakdown were printed there. Notes (i) unpack totals (share capital, PPE movement, revenue), (ii) state accounting policies, (iii) disclose contingent liabilities, related parties and other legally required facts, and (iv) are part of the financial statements — figures cannot be understood without them. In an exam, referencing Note numbers is part of correct Schedule III presentation.</p>""", "5"))

    parts.append(h3("Long"))
    parts.append(qna("Explain the Schedule III presentation of company financial statements, including the role of adjustments and notes.",
        """<p><strong>Intro.</strong> Indian companies must present a Statement of Profit and Loss and a Balance Sheet in the form set out in Schedule III, with previous-year figures and notes.</p>
        <p><strong>P&L.</strong> Revenue from operations, other income, then specified expense heads including employee benefits, finance costs, depreciation and other expenses, then tax and profit.</p>
        <p><strong>Balance Sheet.</strong> Claims (equity and liabilities) classified as current or non-current, and assets similarly. Totals agree.</p>
        <p><strong>Adjustments.</strong> Accrual items (outstanding, prepaid, depreciation, provisions) are processed so that the statements show the year’s true income and the year-end position, not merely the cash book.</p>
        <p><strong>Notes.</strong> Policies, breakdowns, contingencies. They are not optional decoration.</p>
        <p><strong>Conclusion.</strong> Format + adjustments + notes together produce a true and fair, comparable set of statements.</p>""", "8–10"))

    # ---------- Ch5 ----------
    parts.append(h2("Chapter 5 — Cash Flow Statements"))
    parts.append(h3("1-mark"))
    parts.append(qna("Why is profit not the same as cash?",
        "<p>Profit is computed on accrual: sales on credit, non-cash expenses such as depreciation, and capital purchases that are not expenses. Cash can therefore move differently from profit.</p>", "1"))
    parts.append(qna("Name the three activities in a cash flow statement.",
        "<p>Operating, investing, and financing activities.</p>", "1"))
    parts.append(qna("How is depreciation treated in the indirect method?",
        "<p>It is added back to profit because it reduced profit but did not use cash.</p>", "1"))
    parts.append(qna("Classify purchase of machinery (cash).",
        "<p>Investing outflow.</p>", "1"))
    parts.append(qna("Classify repayment of a long-term loan.",
        "<p>Financing outflow.</p>", "1"))
    parts.append(qna("What are cash equivalents?",
        "<p>Short-term, highly liquid investments that are readily convertible to known amounts of cash and are subject to insignificant risk of change in value (typically original maturity of three months or less).</p>", "1"))

    parts.append(h3("3-mark"))
    parts.append(qna("State the need and importance of a cash flow statement.",
        """<p>It shows how cash was generated and used, which the P&L (accrual) and Balance Sheet (position) do not directly show. Lenders judge repayment capacity; managers plan liquidity; investors see whether profits are collected. It is a required statement under AS-3 / Ind AS-7 for prescribed companies.</p>""", "3"))
    parts.append(qna("Give two examples each of operating, investing and financing cash flows.",
        """<p>Operating: cash from customers; cash paid to suppliers and employees.<br/>
        Investing: purchase of plant; sale of investments; interest received (AS-3).<br/>
        Financing: issue of shares; repayment of debentures; interest paid; dividend paid (AS-3).</p>""", "3"))

    parts.append(h3("5-mark"))
    parts.append(qna("Explain the indirect method of preparing a cash flow statement.",
        """<p>The indirect method starts with net profit before tax and converts it to cash from operations. Non-cash expenses (depreciation, amortisation, losses on sale) are added back; non-cash and non-operating incomes (profit on sale, interest income to be shown under investing) are deducted. Working-capital changes are then applied: an increase in current assets other than cash is deducted; an increase in current liabilities is added. Tax paid is deducted. Investing and financing sections are prepared from actual cash receipts and payments. The sum of the three sections equals the change in cash and cash equivalents.</p>""", "5"))
    parts.append(qna("How is profit on sale of a fixed asset treated in the cash flow statement?",
        """<p>The profit is included inside reported profit but is not an operating cash inflow. It is therefore deducted in the operating section. The full sale proceeds (NBV + profit) are shown as an investing inflow. If this deduction is missed, the profit is counted twice.</p>""", "5"))

    parts.append(h3("Long"))
    parts.append(qna("‘Profit is not cash.’ Explain. How does the cash flow statement (indirect method) help users?",
        """<p><strong>Intro.</strong> A firm can report a profit and still run out of cash, or report a loss and still hold cash. Accrual accounting is the reason.</p>
        <p><strong>Why they differ.</strong> Credit sales raise profit before cash arrives. Depreciation reduces profit without a cash payment this year. Buying machinery uses cash but is capitalised, not fully expensed. Taking a loan raises cash without raising profit.</p>
        <p><strong>Indirect CFS.</strong> It reconverts profit to cash from operations, then separately shows investing and financing. Users see the quality of earnings (are profits collected?), the capex burden, and dependence on new borrowing.</p>
        <p><strong>Conclusion.</strong> P&L, Balance Sheet and CFS are three views of the same story. An MBA should read all three.</p>""", "8–10"))

    # ---------- Ch6 ----------
    parts.append(h2("Chapter 6 — Annual Reports"))
    parts.append(h3("1-mark"))
    parts.append(qna("What is an annual report?",
        "<p>An annual report is the yearly published document through which a company reports its activities, governance and audited financial statements to shareholders and other stakeholders.</p>", "1"))
    parts.append(qna("Name two users of an annual report.",
        "<p>Shareholders (or prospective investors) and lenders; also employees, analysts, regulators, tax authorities (any two).</p>", "1"))
    parts.append(qna("What is MD&A?",
        "<p>Management Discussion and Analysis is management’s narrative of performance, risks, outlook and operational factors behind the numbers.</p>", "1"))
    parts.append(qna("What is an unmodified audit opinion?",
        "<p>The auditor’s opinion that the financial statements give a true and fair view (or are fairly presented) in accordance with the applicable financial reporting framework — commonly called a clean opinion.</p>", "1"))
    parts.append(qna("Name two financial statements found inside an annual report.",
        "<p>Balance Sheet and Statement of Profit and Loss; also Cash Flow Statement and Statement of Changes in Equity (any two).</p>", "1"))
    parts.append(qna("What is a Directors’ Report?",
        "<p>The Board’s statutory report to members on the state of affairs, dividends, directors’ responsibility, and other matters required by the Companies Act.</p>", "1"))

    parts.append(h3("3-mark"))
    parts.append(qna("State the importance of an annual report.",
        """<p>It discharges legal accountability, gives a comparable yearly record of performance and position, communicates strategy and risks, and is the raw material for ratio and cash-flow analysis. Without it, outside shareholders would have no standardised window into the company.</p>""", "3"))
    parts.append(qna("List six contents of a typical listed company’s annual report.",
        """<p>Corporate information; Chairman’s / MD’s statement; Directors’ Report; Management Discussion and Analysis; Corporate governance report; Audited financial statements with notes and the auditor’s report. (Also BRSR, AGM notice, highlights.)</p>""", "3"))

    parts.append(h3("5-mark"))
    parts.append(qna("Explain the composition and contents of an annual report.",
        """<p>An annual report typically has (i) narrative sections — highlights, Chairman’s letter, MD&A, Directors’ Report, governance; (ii) the auditor’s report; (iii) standalone and, if a group, consolidated financial statements — Balance Sheet, P&L, cash flows, changes in equity, policies and notes; (iv) statutory annexures (CSR, related party, secretarial). The narrative explains; the statements measure; the notes detail; the auditor opines. They must be read together.</p>""", "5"))
    parts.append(qna("Who uses an annual report and for what?",
        """<p>Shareholders: performance, dividend, stewardship. Investors: valuation and risk. Lenders: debt-service and security. Employees: stability and bonus capacity. Analysts: ratios and forecasts. Government and tax: compliance. Customers and vendors: going-concern comfort. Each user leans on a different section, but all should notice the auditor’s opinion first.</p>""", "5"))

    parts.append(h3("Long"))
    parts.append(qna("What is an annual report? Discuss its need, importance, composition, and how a manager should read it.",
        """<p><strong>Meaning.</strong> The annual report is the company’s yearly public account of what it did, how it was governed, and how it performed financially, including audited statements.</p>
        <p><strong>Need and importance.</strong> Separation of ownership and control; legal mandate; capital-market communication; basis of analysis.</p>
        <p><strong>Composition.</strong> Narrative, governance, auditor, financial statements, notes, statutory annexures.</p>
        <p><strong>How to read.</strong> Auditor’s opinion → P&L, BS, CFS → notes and policies → MD&A claims tested against the numbers → governance and related-party disclosures if something looks unusual.</p>
        <p><strong>Limitation.</strong> Historical, aggregated, policy choices, possible window dressing. Still the best standardised packet a manager has.</p>""", "8–10"))

    # ---------- Ch7 ----------
    parts.append(h2("Chapter 7 — Ratio Analysis"))
    parts.append(h3("1-mark"))
    parts.append(qna("What is a ratio in accounting analysis?",
        "<p>A ratio is a mathematical relationship between two figures from the financial statements, used to interpret liquidity, solvency, profitability or efficiency.</p>", "1"))
    parts.append(qna("Give the current ratio formula.",
        "<p>Current ratio = Current assets ÷ Current liabilities.</p>", "1"))
    parts.append(qna("Give the quick ratio formula.",
        "<p>Quick ratio = (Current assets − Inventory − Prepaid expenses) ÷ Current liabilities.</p>", "1"))
    parts.append(qna("What is a Balance Sheet ratio?",
        "<p>A ratio whose numerator and denominator are both taken from the Balance Sheet (for example current ratio, debt–equity).</p>", "1"))
    parts.append(qna("What is a combined ratio? Give one example.",
        "<p>A ratio that uses one figure from the P&L and one from the Balance Sheet, for example inventory turnover or ROCE.</p>", "1"))
    parts.append(qna("State the ideal current ratio commonly cited.",
        "<p>2 : 1 is the traditional textbook ideal, to be interpreted with industry context.</p>", "1"))

    parts.append(h3("3-mark"))
    parts.append(qna("Why are ratios needed? State two limitations.",
        """<p><strong>Need:</strong> absolute figures are hard to compare across firms and years; ratios standardise performance (liquidity, solvency, profitability, turnover) for diagnosis and decisions.</p>
        <p><strong>Limitations:</strong> they use historical data; they can be distorted by window dressing and by different accounting policies; a ratio without a benchmark is a number, not a conclusion.</p>""", "3"))
    parts.append(qna("Distinguish Balance Sheet ratios, revenue ratios and combined ratios.",
        """<p>Balance Sheet ratios use only position figures (current ratio). Revenue ratios use only P&L figures (GP ratio). Combined ratios mix a flow from the P&L with a stock from the Balance Sheet (debtors turnover, ROCE). This is the classification used in this syllabus.</p>""", "3"))

    parts.append(h3("5-mark"))
    parts.append(qna("Explain any four liquidity and solvency ratios.",
        """<p>(i) Current ratio = CA/CL — short-term paying ability.<br/>
        (ii) Quick ratio = (CA − stock − prepaid)/CL — ability to pay without waiting to sell stock.<br/>
        (iii) Debt–equity = long-term debt / shareholders’ funds — gearing; higher means more financial risk.<br/>
        (iv) Proprietary ratio = shareholders’ funds / total assets — portion of assets financed by owners.</p>
        <p>Always state the unit and comment; do not stop at the arithmetic.</p>""", "5"))
    parts.append(qna("Explain ROCE and ROE. Why can they differ?",
        """<p>ROCE = EBIT / Capital employed × 100, where capital employed is shareholders’ funds plus long-term debt. It measures return on all long-term funds, before interest and tax. ROE = PAT / Equity shareholders’ funds × 100, the residual return for owners. They differ because ROCE includes debt in the denominator and uses a pre-interest numerator; if the firm earns more on borrowed funds than the interest rate, ROE is levered above the unlevered return, and vice versa.</p>""", "5"))

    parts.append(h3("Long"))
    parts.append(qna("Discuss the need and importance of ratio analysis. Classify ratios as per this syllabus and explain one ratio from each class, including limitations of ratio analysis.",
        """<p><strong>Need.</strong> Managers and outsiders must compare, trend, and diagnose. Raw rupees hide size differences.</p>
        <p><strong>Classification.</strong> Balance Sheet ratios (e.g. current ratio = CA/CL). Revenue ratios (e.g. GP ratio = GP/Sales × 100). Combined ratios (e.g. inventory turnover = COGS/average stock; ROCE = EBIT/capital employed).</p>
        <p><strong>Importance.</strong> Liquidity planning, credit decisions, profitability control, inter-firm comparison, highlighting areas for investigation.</p>
        <p><strong>Limitations.</strong> Historical; window dressing; different year-ends and policies; need for industry norms; ratios do not replace reading the notes and the cash flow statement.</p>
        <p><strong>Conclusion.</strong> Ratios ask good questions; they are not themselves the answers.</p>""", "8–10"))

    parts.append(chapter_close())
    return "".join(parts)
