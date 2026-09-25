#!/usr/bin/env python3
"""Chapter 06 — Understanding Annual Reports and Analysis.

Accounting for Managers. Beginner-to-exam teaching notes.
A student who has never opened an annual report should be able to sit with
only this chapter and then (a) name every major section, (b) read an
auditor's opinion, (c) walk from a management claim to the notes, cash flow
and ratios, and (d) write 1 / 5 / 8–10 mark answers.
"""

from __future__ import annotations

import sys

sys.path.insert(0, "/workspace/notes")
from html_lib import *


def ar_block(
    title: str,
    what: str,
    simple_w: str,
    why_t: str,
    who: str,
    question: str,
    link: str,
    sagar: str,
) -> str:
    """Compact teaching card for one section of the annual report."""
    inner = (
        f"<p><strong>What it is.</strong> {what}</p>"
        f"<p><strong>In simple words.</strong> {simple_w}</p>"
        f"<p><strong>Why it is in the report.</strong> {why_t}</p>"
        f"<p><strong>Who reads it.</strong> {who}</p>"
        f"<p><strong>Question it answers.</strong> {question}</p>"
        f"<p><strong>How it connects to other sections.</strong> {link}</p>"
        f"<p><strong>Sagar snapshot.</strong> {sagar}</p>"
    )
    return h3(title) + box("format", title, inner)


def body() -> str:
    parts: list[str] = []

    parts.append(
        chapter_open(
            "06",
            "Understanding Annual Reports and Analysis",
            "After this chapter you will be able to open a real Indian listed-company annual report without panic, name every major section in the order it usually appears, explain why the report exists and who uses it, read the auditor's opinion before trusting the numbers, walk from a management claim down to the supporting note, cash flow and ratio, and write 1-mark, 5-mark and 8–10-mark exam answers on need, importance, composition, Directors' Report and Auditor's Report.",
            [
                "Need and importance of Annual Report",
                "Composition of Annual Report",
                "Contents of Annual Report",
            ],
        )
    )

    # ------------------------------------------------------------------
    # 6.1 Opening picture
    # ------------------------------------------------------------------
    parts.append(h2("6.1 Opening picture — you have never seen an annual report. Here is one.", "s61"))
    parts.append(
        lead(
            "Imagine a company that makes pickles, spices and ready-to-eat meals. "
            "It has thousands of shareholders who do not sit in the factory. "
            "Once a year the company publishes a thick document — often 150 to 400 pages, "
            "sometimes a glossy printed book, almost always a PDF on the company website "
            "and on the BSE / NSE website. That document is the <strong>annual report</strong>. "
            "This chapter teaches you to open it, not fear it, and use it."
        )
    )
    parts.append(
        p(
            "Think of two school objects taped together. First, a ",
            b("report card"),
            ": marks, ranks, attendance, the class teacher's remarks, and the principal's stamp. "
            "Second, a ",
            b("storybook"),
            ": photographs of the annual day, a letter from the principal, a page on sports day, "
            "and a paragraph on how the school served the neighbourhood. "
            "An annual report is exactly that mix. The financial statements are the report card. "
            "The Chairman's letter, photographs of plants, Management Discussion and Analysis, "
            "CSR stories and governance pages are the storybook. "
            "An MBA who reads only the storybook is being sold a narrative. "
            "An MBA who reads only the last page of the profit and loss account is missing the plot. "
            "You must read both, and you must check that the story and the report card agree.",
        )
    )
    parts.append(
        keypoint(
            "You do not read an annual report like a novel, from page 1 to page 400. "
            "You navigate it like a reference book: identity → auditor's stamp → dashboard → "
            "face of the statements → notes → story → stewardship. "
            "Section 6.14 gives you a 30-minute sequence. Learn the map first."
        )
    )

    parts.append(h3("Meet the company we will live with for the whole chapter"))
    parts.append(
        p(
            "Every illustration below uses one fictional listed company so the pages feel real. "
            "The numbers are invented for teaching. They are internally consistent. "
            "Memorise the name; exam answers become easier when you can drop a concrete line."
        )
    )
    parts.append(
        table(
            ["Particulars", "Sagar Consumer Products Ltd (SCPL)"],
            [
                ["What it does", "Packaged foods: spices, pickles, ready-to-eat meals"],
                ["Legal identity", "Public company, listed on BSE and NSE"],
                [
                    "CIN (imagined)",
                    "L15490MH2010PLC123456 — the L at the front signals a listed company",
                ],
                ["Registered office", "Andheri, Mumbai"],
                ["Financial year in this chapter", "1 April 2024 to 31 March 2025 (FY 2024–25)"],
                ["Revenue from operations (standalone)", "₹420 crore (previous year ₹350 crore)"],
                ["Profit after tax (standalone)", "₹38 crore (previous year ₹31 crore)"],
                ["Equity share capital", "₹10 crore (1 crore shares of face value ₹10)"],
                ["Dividend proposed", "₹4 per share, total ₹4 crore"],
                ["Chairman", "Mrs Meera Sagar (non-executive)"],
                ["Managing Director", "Mr Arjun Sagar"],
                ["Statutory auditor", "Mehta &amp; Kale LLP, Chartered Accountants"],
                [
                    "Subsidiaries",
                    "Sagar Spices Pvt Ltd (100%, India) and Sagar Foods USA Inc (100%, USA)",
                ],
            ],
            caption="Running illustration used throughout Chapter 6",
            foot="Standalone = Sagar as one legal entity. Consolidated = Sagar plus its two subsidiaries treated as one group.",
        )
    )
    parts.append(
        real_life(
            "A first-year MBA downloads 'Sagar Consumer Products Ltd Annual Report 2024–25.pdf' "
            "from the investor-relations page. Page 1 is a photograph of a pickle jar and a bowl of "
            "dal. Page 4 lists the board, bankers, auditors and the CIN. Page 12 is a dashboard: "
            "Revenue ₹420 crore, up 20%. Page 48 is the Independent Auditor's Report. Page 54 is "
            "the Balance Sheet. Page 90 is Note 21 Related Party Disclosures. Page 140 is the Notice "
            "calling the 15th Annual General Meeting on 12 August 2025. That PDF is the object this "
            "chapter is about. By the last section you will know what to do with each of those pages."
        )
    )

    # ------------------------------------------------------------------
    # 6.2 What is an Annual Report?
    # ------------------------------------------------------------------
    parts.append(h2("6.2 What is an Annual Report?", "s62"))
    parts.append(
        definition(
            "An <strong>annual report</strong> is the yearly published document through which a company "
            "reports to its shareholders (and to the wider public) on its activities, performance, "
            "financial position, cash flows, governance and future outlook for a financial year. "
            "It is both a <strong>statutory document</strong> (the law and, for listed companies, SEBI "
            "require a large part of it) and a <strong>communication document</strong> (management uses "
            "it to tell the company's story, attract capital and protect reputation)."
        )
    )
    parts.append(
        simple(
            "Once a year the company sits down and says: 'This is who we are, this is what we did, "
            "this is the money we made and the money we owe, this is how we behaved, this is what "
            "an independent auditor thinks of our numbers, and this is when we will meet you to vote.' "
            "That sitting-down is printed (or PDFed) as the annual report. "
            "It is not a brochure, though it contains brochure-like pages. "
            "It is not 'only the Balance Sheet', though the Balance Sheet lives inside it."
        )
    )
    parts.append(
        why(
            "Shareholders are owners who usually do not manage the company day to day. "
            "Directors and managers are stewards of other people's money. "
            "Without a yearly, audited, standardised report, owners cannot judge the stewards, "
            "lenders cannot price credit, analysts cannot compare two companies, and the law "
            "cannot enforce accountability. The annual report is the main public accountability pack."
        )
    )
    parts.append(
        logic(
            "Accounting already produces a Balance Sheet, a Statement of Profit and Loss, a Cash Flow "
            "Statement, a Statement of Changes in Equity and Notes (Chapters 4 and 5). "
            "Those statements are necessary but not sufficient. Users also need: who is on the board, "
            "whether the auditor agrees, whether related parties were used, whether internal controls "
            "exist, what risks management sees, and what will be voted at the AGM. "
            "The annual report wraps the financial statements in that stewardship and narrative layer. "
            "The numbers remain the evidence. The wrapping is the context."
        )
    )
    parts.append(
        format_box(
            "Two natures of the same document",
            table(
                ["Nature", "What it means", "What you will find"],
                [
                    [
                        "Statutory / legal",
                        "Companies Act, 2013 (and SEBI LODR if listed) require specified contents, audit, board approval, sending to members, filing.",
                        "Board's Report, audited financial statements, auditor's report, specified annexures, notice of AGM.",
                    ],
                    [
                        "Communication / voluntary packaging",
                        "The company wants capital, reputation and a clear story. It is allowed to add photographs, a Chairman's letter, a highlights dashboard, brand history.",
                        "Cover design, MD's letter, infographics, product photographs, 'awards' pages. These are useful but they are not audited in the same way as the financial statements.",
                    ],
                ],
            )
            + p(
                "Exam line you can write: <em>The annual report is a statutory-cum-communication document "
                "issued yearly to shareholders, containing audited financial statements together with "
                "the Board's Report, auditor's report and other narrative and governance disclosures.</em>"
            ),
        )
    )
    parts.append(
        keypoint(
            "An annual report is bigger than 'the accounts'. The financial statements are the core. "
            "The annual report is the core plus the story, the board's legal report, governance, "
            "sustainability, the auditor's opinion and the AGM notice. "
            "If an exam question says 'contents of annual report' and you write only Balance Sheet "
            "and Profit and Loss, you will lose marks."
        )
    )
    parts.append(
        warn(
            "Do not confuse <strong>annual report</strong> with <strong>annual return</strong>. "
            "The annual report is the document for shareholders (this chapter). "
            "The annual return is a filing with the Registrar of Companies (Form MGT-7) giving "
            "shareholding, directors and other registry facts. Different document, different purpose. "
            "MBA answers that mix the two lose easy marks."
        )
    )

    parts.append(h3("Who must prepare what — listed vs unlisted, in one minute"))
    parts.append(
        p(
            "Every company that is not dormant still has a yearly accountability cycle: books of account, "
            "financial statements, a Board's Report, an audit, an Annual General Meeting. "
            "What people call a 'full annual report' — the thick listed-company PDF — is the most complete "
            "version, because SEBI's Listing Obligations and Disclosure Requirements (LODR) add "
            "Management Discussion and Analysis, a Corporate Governance Report, and (for specified listed "
            "entities) a Business Responsibility and Sustainability Report. "
            "This chapter teaches that full listed-company pack, which is what MBA questions mean by "
            "'composition of annual report'. A small private company still has accounts + Board's Report "
            "+ auditor's report; it may not have a glossy MD&amp;A booklet."
        )
    )
    parts.append(
        table(
            ["Company type", "Must it prepare yearly accounts + Board's Report + audit?", "Typical 'annual report' pack"],
            [
                [
                    "Private company (unlisted)",
                    "Yes, under the Companies Act (with some exemptions by size).",
                    "Thinner. Financial statements, Board's Report, auditor's report. Often no MD&amp;A, no BRSR, no SEBI governance report.",
                ],
                [
                    "Public unlisted company",
                    "Yes.",
                    "Board's Report is fuller. Still usually no SEBI MD&amp;A / BRSR unless voluntarily given.",
                ],
                [
                    "Listed company (like Sagar)",
                    "Yes, plus SEBI (LODR).",
                    "The full pack taught below: story + stewardship + standalone + consolidated + auditor + BRSR + AGM notice.",
                ],
            ],
            caption="Same legal family, different thickness of the published pack",
        )
    )

    # ------------------------------------------------------------------
    # 6.3 Why companies prepare it
    # ------------------------------------------------------------------
    parts.append(h2("6.3 Why do companies prepare an Annual Report?", "s63"))
    parts.append(
        p(
            "A beginner sometimes thinks: 'They prepare it because the printer asked for a brochure.' "
            "No. There are legal reasons and business reasons. Write both in an 8-mark answer."
        )
    )
    parts.append(
        table(
            ["Reason", "Simple meaning", "Sagar illustration"],
            [
                [
                    "Companies Act, 2013",
                    "Directors must lay audited financial statements and a Board's Report before the AGM, send copies to members, and file with the ROC. This is not optional.",
                    "Sagar's Board approves the FY 2024–25 statements in May 2025, the auditor signs, the pack is sent to members, and the 15th AGM is called for 12 August 2025 (within six months of 31 March).",
                ],
                [
                    "SEBI (LODR), if listed",
                    "Listed companies must give extra disclosures: MD&amp;A, corporate governance, BRSR for specified companies, submission to stock exchanges, website hosting.",
                    "Sagar files the annual report with BSE and NSE and puts the PDF on sagarfoods.example/investors.",
                ],
                [
                    "Accountability / stewardship",
                    "Managers run the company with shareholders' money. The report is the yearly rendering of account: what we did with your money.",
                    "Mrs Meera Sagar's letter and the Directors' Report both answer: we grew revenue, we propose a ₹4 dividend, we spent ₹72 lakh on CSR.",
                ],
                [
                    "Decision-useful information",
                    "Investors, lenders and analysts need a standardised, audited pack to decide: buy, hold, sell, lend, rate.",
                    "A banker looking at Sagar's cash flow and receivables ageing decides the working-capital limit. An analyst builds a ratio sheet from the same PDF (Chapter 7).",
                ],
                [
                    "Capital-raising reputation",
                    "A clear, clean, timely annual report is a reputation asset. A qualified audit or a late, thin report raises the cost of capital.",
                    "If Sagar wants to issue shares next year, the FY 2024–25 report is the document the new investor will read first.",
                ],
                [
                    "Comparison across years and with peers",
                    "The same format every year lets you see change. Two companies in the same industry can be compared (with care — policies may differ).",
                    "Sagar's 'performance at a glance' shows five years of revenue. You can also compare Sagar's margin with another FMCG company.",
                ],
                [
                    "Internal discipline",
                    "Knowing that numbers will be audited and published forces better records, better controls, and a yearly pause to think about risks.",
                    "Sagar's CFO cannot 'leave stock uncounted' because the auditor will visit, and the Board must sign a Directors' Responsibility Statement.",
                ],
            ],
            caption="Why the annual report exists — legal plus business",
        )
    )
    parts.append(
        why(
            "If companies did not publish an annual report, ownership would be a blind trust. "
            "The stock market could not price shares on public information. Banks would lend on "
            "private, uneven packs. Employees would guess at job security. Tax officers would "
            "reconstruct profit from scratch. The annual report is the public information spine "
            "of corporate India."
        )
    )

    # ------------------------------------------------------------------
    # 6.4 Who uses it
    # ------------------------------------------------------------------
    parts.append(h2("6.4 Who uses the Annual Report? A user → 'what they look for' table", "s64"))
    parts.append(
        simple(
            "The same PDF is read by ten different people looking for ten different things. "
            "That is why the report is thick. A shareholder wants dividend and honesty. "
            "A banker wants cash and collateral. An employee wants stability. "
            "An analyst wants the notes. Learn this table; it is a ready 5-mark answer "
            "('users of annual report' / 'importance to various parties')."
        )
    )
    parts.append(
        table(
            ["User", "Why they open the report", "What they look for first", "Sagar example"],
            [
                [
                    "Existing shareholders",
                    "They already own the company. They want to know if the stewards did a decent job and whether to hold or exit.",
                    "Profit, dividend, going concern, related-party deals, auditor's opinion, governance.",
                    "Is the ₹4 dividend covered by cash? Did promoters sell goods to a private firm they own?",
                ],
                [
                    "Prospective investors",
                    "They are deciding whether to buy the share.",
                    "Growth, margins, return on equity, risks in MD&amp;A, quality of earnings, valuation context.",
                    "Revenue 20% up looks exciting until they see receivables also jumped. They read the cash flow next.",
                ],
                [
                    "Lenders / bankers",
                    "They want the loan repaid with interest.",
                    "Debt, interest coverage, operating cash flow, contingent liabilities, security, current ratio.",
                    "Sagar's borrowings ₹55 crore vs CFO ₹32 crore. Any court cases in the contingent-liability note?",
                ],
                [
                    "Employees and unions",
                    "Job security, bonus, ESOP, expansion vs closure.",
                    "Profit, segment outlook, employee-benefit note, MD&amp;A on strategy.",
                    "The ready-to-eat line grew 54% — that plant's jobs look safer than a flat spices line.",
                ],
                [
                    "Tax authorities",
                    "Tax is computed from profit and from specific adjustments.",
                    "Profit, tax note, related-party pricing, contingent tax demands.",
                    "Note on income tax: current tax, deferred tax, any dispute with the department.",
                ],
                [
                    "Financial analysts and credit-rating agencies",
                    "They turn the report into models, ratios and ratings.",
                    "Everything, especially notes, segments, accounting policies, related parties, cash flow, KAMs.",
                    "They rebuild Sagar's EBITDA, adjust for one-time items, and compare debtor days year on year.",
                ],
                [
                    "Customers and suppliers",
                    "They need Sagar to exist next year (going concern) and to pay on time.",
                    "Scale, cash, debt, any distress language, concentration of customers.",
                    "A large retailer checks that Sagar is not about to shut the pickle factory.",
                ],
                [
                    "Media, public, NGOs",
                    "Stories, controversies, environment, labour, product quality.",
                    "BRSR, CSR annexure, governance failures, large related-party numbers, auditor qualifications.",
                    "CSR ₹72 lakh — which villages, which projects? Any labour incident in BRSR?",
                ],
                [
                    "Government and regulators (MCA, SEBI, stock exchanges)",
                    "Compliance, investor protection, public interest.",
                    "Filing completeness, governance, fraud reporting, insider / related-party compliance.",
                    "Was the report filed on time? Is the Board's Report complete under Section 134?",
                ],
                [
                    "Board itself and the audit committee",
                    "The pack is also the board's own yearly mirror.",
                    "Internal control weaknesses, auditor KAMs, frauds, risk section of MD&amp;A.",
                    "The audit committee reads Mehta &amp; Kale's KAM on a ₹12 crore distributor receivable before it recommends the accounts.",
                ],
            ],
            caption="Users of the annual report and what each one hunts for",
            foot="Exam hint: write at least six users, and against each write the information need — not just the name.",
        )
    )
    parts.append(
        memory(
            "Users mnemonic — <strong>SALE TEAM CG</strong>: "
            "<strong>S</strong>hareholders, <strong>A</strong>nalysts, <strong>L</strong>enders, "
            "<strong>E</strong>mployees, <strong>T</strong>ax authorities, <strong>E</strong>xternal public / media, "
            "<strong>A</strong>spirants (prospective investors), <strong>M</strong>anagement / board itself, "
            "<strong>C</strong>ustomers and suppliers, <strong>G</strong>overnment / regulators. "
            "If the question is 5 marks, pick any six and write two lines each."
        )
    )

    # ------------------------------------------------------------------
    # 6.5 Need and importance
    # ------------------------------------------------------------------
    parts.append(h2("6.5 Need and importance of the Annual Report (5–8 mark material)", "s65"))
    parts.append(
        p(
            "This is the most common theory question in the chapter. "
            "The examiner is not asking you to praise the printing quality. "
            "The examiner wants: why the document is needed in a company economy, and what it enables. "
            "Write in numbered points. Give a one-line explanation under each heading. "
            "Drop Sagar or any company name for colour if you have time."
        )
    )
    parts.append(definition(
        "<strong>Need</strong> of the annual report means the gap it fills: without it, owners, lenders and "
        "regulators would lack a yearly, comparable, audited public account of the company. "
        "<strong>Importance</strong> means the uses and benefits that follow once the report exists: "
        "transparency, stewardship, comparison, legal compliance, analysis, and capital-market confidence."
    ))
    parts.append(simple(
        "Need = why we cannot do without it. Importance = what good it does once we have it. "
        "In an MBA answer you may treat them together as 'need and importance' and write 8–10 points."
    ))
    parts.append(
        format_box(
            "Need and importance — write these points in the answer booklet",
            ol(
                [
                    "<strong>Transparency.</strong> The report makes performance, position, cash, risks and related-party dealings visible to people who do not sit in the head office. Hidden companies cannot be trusted with public money.",
                    "<strong>Stewardship / accountability.</strong> Directors are trustees of shareholders' funds. The Board's Report, the Directors' Responsibility Statement and the audited accounts are the yearly rendering of that trusteeship.",
                    "<strong>Legal compliance.</strong> The Companies Act requires financial statements, a Board's Report, audit, circulation to members and filing. Listed companies have extra SEBI duties. The annual report is how those duties are discharged in one pack.",
                    "<strong>Decision-useful information.</strong> Buy / hold / sell / lend / rate / join as an employee — each of those decisions needs information. The report is the primary public source.",
                    "<strong>Comparison across years.</strong> Five-year highlights and consistent statements let you see whether Sagar is growing, stalling or dressing up one year.",
                    "<strong>Comparison across companies.</strong> Schedule III and Ind AS / AS give a common skeleton, so an analyst can (carefully) compare Sagar with another FMCG company.",
                    "<strong>Basis for ratio analysis (Chapter 7).</strong> Every ratio you will study — current ratio, debt-equity, net profit margin, debtor days, ROE — is computed from the face of the statements and the notes inside this report. No annual report, no honest ratio.",
                    "<strong>Basis for cash-flow analysis (Chapter 5).</strong> Profit is not cash. The Cash Flow Statement inside the annual report tells you whether Sagar's 20% sales growth actually came in as collections.",
                    "<strong>Credit and investment decisions.</strong> Banks, bond investors and rating agencies underwrite on the back of this pack (plus their own due diligence).",
                    "<strong>Reputation and capital raising.</strong> A timely, clean, unmodified audit plus clear governance lowers the cost of equity and debt. A qualified opinion or a related-party shock does the opposite.",
                    "<strong>Corporate governance signal.</strong> Independent directors, board committees, related-party policy, auditor rotation — these pages tell you how power is checked inside the company.",
                    "<strong>Non-financial and public accountability.</strong> CSR, BRSR, employee and environment disclosures answer stakeholders who are not only interested in EPS.",
                    "<strong>Internal control and discipline.</strong> The knowledge that an independent auditor will opine, and that directors must sign a responsibility statement, forces better books and better controls.",
                    "<strong>Communication with the AGM.</strong> The report (with the notice) is the briefing pack for the yearly meeting at which owners vote on dividend, directors and auditors.",
                ]
            ),
        )
    )
    parts.append(
        connect(
            "Chapter 4 taught you the face of the financial statements. Chapter 5 taught you the Cash Flow "
            "Statement. Chapter 7 will teach you ratios. All three live <em>inside</em> the annual report, "
            "and all three are dangerous if you ignore the notes and the auditor's opinion. "
            "This chapter is the map of the house; those chapters are the rooms."
        )
    )
    parts.append(
        exam_tip(
            "For <strong>5 marks</strong>: write 5–6 points (transparency, stewardship, legal compliance, "
            "decision usefulness, comparison, basis for analysis) with two sentences each. "
            "For <strong>8–10 marks</strong>: add users (a short table in words), add how financial and "
            "non-financial parts connect, and close with one limitation so the answer looks mature. "
            "Never write a single paragraph of praise."
        )
    )

    # ------------------------------------------------------------------
    # 6.6 Composition / structure
    # ------------------------------------------------------------------
    parts.append(h2("6.6 Composition and structure — typical Indian listed-company order", "s66"))
    parts.append(
        definition(
            "<strong>Composition of an annual report</strong> means the parts it is made of and the order "
            "in which they usually appear in an Indian listed company's published report. "
            "There is no one page-number law that says 'MD&amp;A must start on page 21', but practice "
            "and SEBI / Companies Act contents have settled into a recognisable sequence. "
            "Exams expect you to list that sequence with a one-line role for each part."
        )
    )
    parts.append(
        simple(
            "Open Sagar's PDF. You will almost always travel in this order: "
            "who they are (cover and corporate information) → a human greeting (Chairman / MD) → "
            "faces of the board → a numbers dashboard → management's story (MD&amp;A) → "
            "the board's legal report → how they govern themselves → how they treat society (BRSR) → "
            "the standalone accounts → the group accounts → the auditor's stamp → the fine print "
            "(policies and notes) → the meeting notice. Story first, evidence later, meeting last."
        )
    )
    parts.append(
        why(
            "The order is psychological and legal. Humans want a story and a dashboard before a 40-page "
            "note on leases. The law wants the Board's Report and the auditor's report next to the "
            "accounts they cover. The AGM notice is last because it is the action document: date, venue, "
            "resolutions. Once you memorise the order, a 400-page PDF stops being a jungle."
        )
    )
    parts.append(
        format_box(
            "Typical contents, in the order they usually appear",
            table(
                ["#", "Section", "Layer", "One-line job"],
                [
                    ["1", "Cover", "Identity", "Name, year, a picture. The face of the document."],
                    [
                        "2",
                        "Corporate information",
                        "Identity",
                        "CIN, registered office, board, committees, bankers, auditors, registrars, website.",
                    ],
                    [
                        "3",
                        "Chairman's / MD's message",
                        "Story",
                        "A signed letter: how the year felt, strategy, thanks, outlook.",
                    ],
                    ["4", "Board of Directors", "Identity", "Names, photos, who is independent, who is executive."],
                    [
                        "5",
                        "Highlights / performance at a glance",
                        "Dashboard",
                        "5-year numbers: revenue, PAT, EPS, debt, maybe graphs.",
                    ],
                    [
                        "6",
                        "Management Discussion and Analysis (MD&amp;A)",
                        "Story",
                        "Industry, strategy, segment performance, risks, outlook — management's narrative.",
                    ],
                    [
                        "7",
                        "Directors' Report (Board's Report) + annexures",
                        "Stewardship",
                        "Statutory report under Section 134: state of affairs, dividend, DRS, CSR, secretarial, related party.",
                    ],
                    [
                        "8",
                        "Corporate Governance Report",
                        "Stewardship",
                        "Board structure, committees, meetings, director attendance, shareholder rights — SEBI LODR.",
                    ],
                    [
                        "9",
                        "Business Responsibility and Sustainability Report (BRSR)",
                        "Stewardship",
                        "Environment, social, governance metrics for specified listed companies.",
                    ],
                    [
                        "10a",
                        "Standalone financial statements",
                        "Evidence",
                        "Sagar alone: Balance Sheet, P&amp;L, Cash Flow, Changes in Equity, Notes.",
                    ],
                    [
                        "10b",
                        "Consolidated financial statements",
                        "Evidence",
                        "Sagar plus subsidiaries as one group, after eliminating intra-group deals.",
                    ],
                    [
                        "11",
                        "Independent Auditor's Report (often placed just before the statements it covers)",
                        "Evidence stamp",
                        "Unmodified / qualified / adverse / disclaimer. KAMs. Basis of opinion.",
                    ],
                    [
                        "12",
                        "Significant accounting policies",
                        "Fine print",
                        "How revenue, inventory, depreciation, leases, taxes are measured. Usually Note 1.",
                    ],
                    [
                        "13",
                        "Notes to accounts (other notes)",
                        "Fine print",
                        "Breakdowns, related parties, contingencies, segments, subsequent events.",
                    ],
                    [
                        "14",
                        "Notice of the AGM",
                        "Action",
                        "Date, time, venue / video link, ordinary and special business, explanatory statement.",
                    ],
                ],
                foot="Some companies place the auditor's report immediately before the financial statements (which is logically correct). Some put highlights or MD&amp;A after the Directors' Report. Your exam list should still name all of these parts.",
            ),
        )
    )
    parts.append(
        memory(
            "Order mnemonic — walk into the AGM hall: "
            "<strong>Cover the Chair, Board Highlights MD&amp;A; Directors Govern BRSR; "
            "Standalone then Consolidated; Auditor, Policies, Notes, Notice.</strong> "
            "Shorter code: <strong>C-C-B-H-M-D-G-B | S-C | A-P-N-N</strong> "
            "(Cover, Chair, Board, Highlights, MD&amp;A, Directors, Governance, BRSR, "
            "Standalone, Consolidated, Auditor, Policies, Notes, Notice). "
            "Three layers: <strong>Story → Stewardship → Evidence</strong>, then the meeting card."
        )
    )
    parts.append(
        keypoint(
            "A listed-company annual report has three layers plus an action page. "
            "<strong>Story layer:</strong> Chairman, highlights, MD&amp;A (persuasive, only partly assured). "
            "<strong>Stewardship layer:</strong> Directors' Report, governance, BRSR (legal accountability). "
            "<strong>Evidence layer:</strong> financial statements, policies, notes, auditor's opinion. "
            "<strong>Action:</strong> Notice of AGM. Always finish in the evidence layer. Never stop in the story."
        )
    )
    parts.append(
        real_life(
            "Sagar's PDF has 168 pages. Pages 1–3 cover and contents. Pages 4–5 corporate information. "
            "Pages 6–8 Chairman and MD letters. Pages 9–10 board. Pages 11–13 highlights. "
            "Pages 14–28 MD&amp;A. Pages 29–52 Directors' Report and annexures (CSR, secretarial audit, "
            "related party, conservation of energy). Pages 53–62 Corporate Governance. Pages 63–78 BRSR. "
            "Pages 79–83 Independent Auditor's Report on standalone statements. Pages 84–128 standalone "
            "statements and notes. Pages 129–133 auditor on consolidated statements. Pages 134–160 "
            "consolidated statements and notes. Pages 161–168 Notice of the 15th AGM. "
            "That is a normal shape. Once you have seen one, the next ten look familiar."
        )
    )

    # ------------------------------------------------------------------
    # 6.7 Each major section
    # ------------------------------------------------------------------
    parts.append(h2("6.7 Teach every major section — what, why, who, which question, which link", "s67"))
    parts.append(
        p(
            "Below, each section of Sagar's annual report is taught in the same six lines plus a snapshot. "
            "Read them slowly the first time. On revision, read only the bold labels and the Sagar snapshot. "
            "Directors' Report and Auditor's Report are introduced here and taught in full in 6.9 and 6.10, "
            "because those two are favourite 5-mark questions."
        )
    )

    parts.append(
        ar_block(
            "1. Cover",
            "The front page of the printed book or PDF: company name, 'Annual Report 2024–25', usually a product or plant photograph, sometimes a theme ('25 years of flavour').",
            "The school report-card cover. It tells you whose report this is and which year. It is not audited.",
            "Identity and first impression. Shareholders picking up a pile of reports at the AGM need to know they are holding Sagar, not another company.",
            "Everyone, for one second. Then they turn the page. Analysts skip it. Brand teams care a lot.",
            "Which company? Which year? Listed or not (sometimes the exchanges are printed on the cover)?",
            "The year on the cover must match the year on the Balance Sheet heading and the auditor's report. If you are comparing two years, do not mix FY 2024–25 highlights with FY 2023–24 notes.",
            "Sagar's cover: a glass jar of mango pickle, the words 'Sagar Consumer Products Ltd — Annual Report 2024–25', and small print 'BSE / NSE'. Theme printed on the flap: 'Taste that travels'. Pretty. Not evidence.",
        )
    )
    parts.append(
        ar_block(
            "2. Corporate information",
            "A dense identity page: Corporate Identity Number (CIN), registered office, corporate office, Board of Directors (often repeated), board committees, Chief Financial Officer, Company Secretary, statutory auditor, internal auditor, secretarial auditor, bankers, registrars and transfer agents, website, email for investor grievances.",
            "The company's visiting card plus the list of adults responsible. If you ever need to write to Sagar, or to check who the auditor is, this is the page.",
            "Law and practice require the company to be identifiable. CIN is the unique government ID. Shareholders need a grievance address. Lenders want to know the bankers. Researchers want the auditor's name.",
            "Company secretaries, lawyers, lenders, journalists, anyone verifying that they have the right entity. Students should copy the CIN and auditor's name into their notes before analysing.",
            "Who is legally responsible? Where is the registered office? Who audits? Who is the Company Secretary I email?",
            "The auditor named here must be the auditor who signs the Independent Auditor's Report. The directors named here reappear in the Board's Report, the governance report and related-party notes (if they have transactions).",
            "Sagar's page: CIN L15490MH2010PLC123456, registered office Andheri East, Mumbai; MD Arjun Sagar; CFO Ms Kavita Rao; CS Mr Farhan Qureshi; statutory auditor Mehta &amp; Kale LLP; bankers State Bank of India and HDFC Bank; RTA KFintech; website and a designated email investors@sagar.example.",
        )
    )
    parts.append(
        ar_block(
            "3. Chairman's / Managing Director's message",
            "A signed letter from the Chairman and/or the MD to shareholders. It summarises the year in narrative language, thanks employees and partners, comments on the economy, and states strategy and outlook. It is not a substitute for the financial statements and it is not independently audited as a whole.",
            "The principal's speech on annual day. Warm, selective, forward-looking. Read it for tone and claims — then verify every number against the statements.",
            "Owners want a human voice. Markets want a strategy story. The letter is the company's chance to explain a bad year or celebrate a good one in plain English.",
            "Shareholders, media, employees, prospective investors. Analysts read it for claims they will later test. Examiners may ask you to distinguish it from the Directors' Report (this is narrative; that is statutory).",
            "How does leadership describe the year? What are they proud of? What risks do they admit? What do they promise next year?",
            "Every quantitative claim ('sales grew 20%', 'we are debt-free', 'we doubled RTE') must be checked on the highlights page, the P&amp;L, the segment note and the cash flow. If the letter is glowing and the auditor is qualified, believe the auditor.",
            "Mrs Meera Sagar writes: 'Your company grew revenue 20% to ₹420 crore, led by pickles in North India and our new ready-to-eat line. We remain committed to quality and to a modest dividend of ₹4 per share.' Warm, and — as we will check in 6.12 — only partly the whole truth, because spices were almost flat and cash did not fully follow sales.",
        )
    )
    parts.append(
        ar_block(
            "4. Board of Directors",
            "Names, often photographs, designations (Chairman, MD, whole-time director, independent director, woman director, nominee), and sometimes a one-paragraph profile: age, qualification, other directorships.",
            "A family photograph of the people who are legally in charge. You are looking at who has power, and how many of them are independent of the promoters.",
            "Shareholders vote on directors. Independence is a governance requirement for listed companies. Related-party risk is higher when the board is only a family.",
            "Governance analysts, proxy advisors, large investors, students looking for promoter dominance or independent-director strength.",
            "Who runs Sagar? How many independent directors? Is the Chair separate from the MD? Is there a woman director?",
            "These names reappear in: related-party notes (Did we sell to a director's private firm?), remuneration note, governance report (attendance, committees), and Directors' Report (appointments, resignations). A director who never attends meetings is a red flag in the governance report.",
            "Sagar: Chairman Mrs Meera Sagar (non-executive, promoter); MD Mr Arjun Sagar (executive, promoter); three independent directors including Ms Leela Krishnan (chair of audit committee); one non-executive non-independent; total six. Chair and MD are different people — a good governance signal. Both Sagars will show up again in the related-party note if the company rents a godown from a promoter firm.",
        )
    )
    parts.append(
        ar_block(
            "5. Highlights / performance at a glance",
            "A dashboard, usually 3–5 years in columns: revenue, EBITDA, PAT, EPS, dividend, net worth, debt, maybe production volumes, maybe graphs. Sometimes '10-year highlights' at the back.",
            "The scoreboard. Fast numbers, no notes, no auditor paragraph. Excellent for a first look, dangerous if you stop here, because dashboards can cherry-pick.",
            "Users need a one-page trend before drowning in notes. Management wants to show progress. Comparison across years is a stated purpose of the annual report.",
            "Busy shareholders, journalists, students starting a ratio sheet. Analysts use it only as a trailer.",
            "Is the company growing? Are profits growing as fast as sales? Is leverage falling or rising? What is EPS and dividend?",
            "Every figure here should be reconcilable with the face of the P&amp;L and Balance Sheet of those years. If 'revenue' on the dashboard is 'gross' and the P&amp;L shows 'net', you will mismatch. After the dashboard, go to cash flow: a rising PAT with falling CFO is a classic warning.",
            "Sagar's five-year strip: Revenue ₹280 → ₹310 → ₹330 → ₹350 → ₹420 crore. PAT ₹22 → ₹25 → ₹27 → ₹31 → ₹38 crore. FY 2024–25 is a jump year. That is exactly why you must open the revenue note and the cash flow before you celebrate.",
        )
    )
    parts.append(
        ar_block(
            "6. Management Discussion and Analysis (MD&amp;A)",
            "A narrative report by management, required for listed companies under SEBI (LODR). Typical headings: economic / industry structure, opportunities and threats, segment-wise performance, outlook, risks and concerns, internal control systems, discussion on financial performance versus last year (often with ratio commentary).",
            "Management sits across the table and explains the year in paragraphs. It is the 'story of the numbers'. It is not the auditor's story. It is not the Board's statutory report, though some themes overlap.",
            "Numbers without context are mute. Users need to know: was the 20% growth volume or price? One product or all? India or exports? One-time or sustainable? What could go wrong next year?",
            "Investors and analysts first; examiners when the question says MD&amp;A; employees reading strategy. Credit analysts read the risk subsection carefully.",
            "Why did performance move? Which segments? What is the outlook? Which risks does management admit?",
            "MD&amp;A claims → P&amp;L line items → notes (revenue disaggregation, segments) → cash flow → ratios (Ch 7) → auditor KAMs. Section 6.12 walks this chain on Sagar. Do not confuse MD&amp;A with the Directors' Report: MD&amp;A is analytical narrative; Directors' Report is the legal Board's Report under Section 134.",
            "Sagar's MD&amp;A says: industry packaged-foods growing in double digits; SCPL revenue +20%; pickles and RTE led; spices 'stable'; risk table lists monsoon, branded competition, a large distributor's credit; internal controls 'adequate'. We will test the word 'stable' (spices grew only about 3%) and the distributor (auditor KAM of ₹12 crore).",
        )
    )
    parts.append(
        ar_block(
            "7. Directors' Report (Board's Report), including annexures",
            "The Board's statutory report to members under Section 134 of the Companies Act, 2013, with annexures prescribed by the Act and Rules: CSR, secretarial audit report, details of related-party contracts, conservation of energy / technology / foreign exchange, extract or web-link of annual return, particulars of loans/guarantees/investments, and others. Full contents are in 6.10.",
            "The Board's official case-sheet. Not a speech. Not MD&amp;A. Directors sign responsibility for true and fair accounts, going concern and internal controls. Annexures are the legal attachments.",
            "The Act requires it. Shareholders cannot hold a proper AGM without it. It is the place where dividend is formally recommended, material post-balance-sheet events are reported, and frauds (if any) are disclosed.",
            "Shareholders, ROC, SEBI, examiners (very common 5-mark), lawyers, governance professionals.",
            "What is the official state of affairs? What dividend? What do directors take responsibility for? Any fraud, any CSR, any secretarial qualification?",
            "The financial statements the Directors' Report talks about are the ones later in the book. The Directors' Responsibility Statement must be consistent with the auditor's opinion. CSR numbers should match the notes. Related-party contracts listed here should appear in the related-party note. Secretarial audit (Form MR-3) sits as an annexure — a second 'auditor' for law, not for numbers.",
            "Sagar's Board's Report: state of affairs healthy; dividend ₹4 per share recommended; ₹6 crore transferred to general reserve; DRS in full; CSR spend ₹72 lakh (2% of average net profit ₹36 crore); no fraud reported under Section 134; secretarial auditor's MR-3 with no qualification; related-party sales of ₹8 crore to Sagar Spices Pvt Ltd in the ordinary course, at arm's length.",
        )
    )
    parts.append(
        ar_block(
            "8. Corporate Governance Report",
            "A report, mainly under SEBI (LODR) Schedule V for listed entities: company's philosophy on code of governance, board composition, attendance, independent directors, audit / nomination / stakeholder / risk committees, remuneration, general body meetings, means of communication, general shareholder information (AGM, book closure, listing, ISIN, registrar).",
            "The rule-book of how power is organised: who sits on which committee, who turned up, how directors are paid, how shareholders can complain. It is about process, not pickle recipes.",
            "Listed-company law wants visible checks on promoter power: independent directors, an audit committee that actually meets, a whistle-blower mechanism, separation of chair and MD where required.",
            "Institutional investors, proxy advisors, SEBI, students looking for red flags (related parties + weak independents + poor attendance).",
            "Is the board independent enough? Did the audit committee meet? Are related-party transactions going through a proper committee? When and where is the AGM?",
            "Read this beside the related-party note and the auditor's report. A clean governance report plus a qualified audit is a contradiction you must notice. Director attendance here should match the 'number of meetings' in the Directors' Report.",
            "Sagar: audit committee of three, all independent, four meetings in the year; Chair and MD separated; whistle-blower policy in place; AGM details repeated; no pending listing fees. No flashing red light — the real heat, if any, is in the ₹12 crore receivable KAM, not in this chapter of the PDF.",
        )
    )
    parts.append(
        ar_block(
            "9. Business Responsibility and Sustainability Report (BRSR)",
            "A SEBI-mandated report for specified listed companies (rolled out first to the largest by market capitalisation, replacing the older Business Responsibility Report). It discloses environmental, social and governance (ESG) indicators: energy, water, waste, greenhouse gases, employees, communities, product responsibility, governance of sustainability.",
            "One paragraph in your exam is enough: listed companies of specified size must tell not only how much profit they made, but how they treated workers, communities and the environment, in a standard BRSR format. It is not a second Profit and Loss account.",
            "Investors and regulators now treat sustainability risks as financial risks (a polluted river can close a plant; a labour scandal can destroy a brand). BRSR standardises that disclosure.",
            "ESG analysts, lenders with green policies, NGOs, employees, large overseas buyers of Sagar's pickles who ask for supplier standards.",
            "Is the company only a profit machine, or does it measure its footprint and its people?",
            "CSR in the Directors' Report is the Companies Act 2% spend on development projects. BRSR is the broader SEBI ESG questionnaire. Do not mix them. A factory fire that BRSR discusses should also appear as a subsequent event or contingent matter in the notes if it is financially material.",
            "Sagar, being listed, includes a BRSR: energy intensity of the pickle plant, 1,240 employees, no child labour, a water-recycling figure, and community kitchens in three districts. An MBA reads it for red flags, not to memorise every KPI.",
        )
    )
    parts.append(
        ar_block(
            "10. Standalone financial statements",
            "The financial statements of Sagar as one legal entity: Statement of Profit and Loss, Balance Sheet (Statement of Financial Position), Statement of Cash Flows, Statement of Changes in Equity, and Notes including accounting policies. Prepared as per Companies Act Schedule III and applicable Ind AS / AS. Taught in depth in Chapters 4 and 5.",
            "Sagar-the-company only. If Sagar owns a subsidiary, the subsidiary's sales are not added here. What you see is the parent's own revenue, own assets, own cash, and the parent's investment in subsidiaries shown as an asset.",
            "The law still looks at each company as a separate legal person. Dividend is declared from standalone profits. Many loan covenants are written on standalone numbers. You cannot skip this set just because a consolidated set exists.",
            "Everyone who cares about the legal entity: the dividend decision, tax (entity-wise), lenders to the parent, ROC filing.",
            "How did the parent company itself perform and stand at the year-end? Can it legally pay this dividend?",
            "Standalone P&amp;L revenue should match the revenue note. Standalone cash flow is the one that tells you whether the parent collected cash. Investment in Sagar Spices Pvt Ltd sits on the standalone Balance Sheet; in the consolidated Balance Sheet that line disappears and the subsidiary's assets and liabilities come in instead.",
            "Sagar standalone: Revenue ₹420 crore, PAT ₹38 crore, equity share capital ₹10 crore, other equity ₹142 crore, borrowings ₹55 crore, inventories ₹62 crore, trade receivables ₹74 crore, cash ₹18 crore, investment in subsidiaries at cost. Dividend is recommended from these standalone profits.",
        )
    )
    parts.append(
        ar_block(
            "11. Consolidated financial statements (the group)",
            "Financial statements of the parent and its subsidiaries presented as if they were one economic entity (Ind AS 110 / AS 21 idea). Intra-group sales, balances and unrealised profits are eliminated. Non-controlling interest is shown if a subsidiary is not 100% owned.",
            "The family photo of the money, not the legal visiting cards. Sagar plus Sagar Spices Pvt Ltd plus Sagar Foods USA Inc, after cancelling the pickles Sagar sold to itself via the subsidiary.",
            "Owners of the parent effectively own the group. If you look only at standalone, a parent can look rich just because it sold goods to its own subsidiary or holds investments at cost. Consolidation stops that self-dealing from inflating the story.",
            "Investors and analysts first — they value the group. Lenders to the parent still care about standalone. Examiners love 'difference between standalone and consolidated'.",
            "If we treat the group as one, what did 'we' sell to the outside world, and what do 'we' owe outsiders?",
            "Always glance at both. If standalone revenue is ₹420 crore and consolidated is ₹474 crore, the difference is outside-group sales of subsidiaries, net of eliminations. Related-party sales of ₹8 crore parent-to-subsidiary vanish in consolidation — they should.",
            "Sagar group: subsidiary India revenue ₹40 crore, USA ₹22 crore, minus ₹8 crore intra-group sales = extra ₹54 crore. Consolidated revenue ≈ ₹474 crore. The ₹8 crore related-party sale that worried you in standalone is eliminated here. USA cash and inventory now sit inside group assets.",
        )
    )
    parts.append(
        p(
            "<strong>Parent vs subsidiary, said to a beginner.</strong> "
            "A <em>parent</em> is a company that controls another company (usually by owning more than half the voting power, or by other control rights). "
            "The company that is controlled is a <em>subsidiary</em>. "
            "Sagar Consumer Products Ltd is the parent. Sagar Spices Pvt Ltd is an Indian subsidiary. "
            "Sagar Foods USA Inc is a foreign subsidiary. "
            "Each of the three is a separate legal person with its own bank account and its own audit. "
            "Consolidation is an accounting camera trick that says: for reporting to Sagar's shareholders, "
            "point the camera at the whole family and hide the money that moved from one family member to another. "
            "It does not merge the legal entities. It does not let the parent spend the subsidiary's cash without following the law."
        )
    )
    parts.append(
        ar_block(
            "12. Independent Auditor's Report",
            "A signed report by the statutory auditor (a chartered accountant / audit firm) giving an opinion on whether the financial statements give a true and fair view, in accordance with the applicable financial reporting framework. For many companies it also reports on internal financial controls and includes a CARO annexure. Types of opinion are taught in 6.9.",
            "An independent second doctor looking at the same lab reports. The doctor does not prepare the reports (management does). The doctor says: clean, or clean except for X, or not true and fair, or I could not form an opinion.",
            "Without this, the annual report is management talking about itself. The whole idea of published accounts is that someone independent has checked them against evidence.",
            "Everyone — but an MBA should read this <strong>before</strong> believing the highlights. Lenders often have a covenant that the opinion must be unmodified.",
            "Can I trust these numbers? Is there a qualification, an adverse opinion, a disclaimer, an emphasis of matter, a key audit matter I should chase into the notes?",
            "The opinion is on the statements that follow (or precede) it. A KAM about revenue points you to the revenue note and accounting policy. A qualification about inventory points you to the inventory note and maybe to MD&amp;A silence. Emphasis of matter points you to a specific note the auditor wants you to actually read.",
            "Sagar standalone: unmodified (clean) opinion from Mehta &amp; Kale LLP. Key Audit Matter: revenue schemes / discounts, and recoverability of a ₹12 crore receivable from a large distributor. No qualification. That KAM is your homework, not a decoration.",
        )
    )
    parts.append(
        ar_block(
            "13. Significant accounting policies",
            "Usually Note 1 (or a separate statement) describing the measurement rules the company chose and applied: basis of preparation (Ind AS), revenue recognition, inventories (FIFO / weighted average), depreciation (SLM / WDV and useful lives), financial instruments, leases, impairment, employee benefits, foreign currency, taxes. Comparative information is prepared on the same policies unless a change is disclosed.",
            "The rulebook for the numbers. Two honest companies can show different profit from the same factory if one uses SLM over 15 years and the other uses WDV at 30%. Policies tell you which game is being played.",
            "True and fair is 'true and fair in accordance with the framework and the policies'. Users cannot interpret ₹62 crore of inventory without knowing cost formula and write-down rules.",
            "Analysts, auditors (they test consistency), examiners when they ask 'notes' or 'limitations of financial statements', anyone comparing two companies.",
            "How is revenue booked? How is stock valued? How fast is the plant depreciated? Any policy change this year?",
            "A policy change that boosts profit should appear here, in the notes, often in MD&amp;A, and the auditor watches it. Inventory policy here + inventory note + cash flow (change in inventory) is one chain. Revenue policy here + revenue note + KAM on schemes is another.",
            "Sagar Note 1: Ind AS; revenue when control of goods passes, net of schemes and discounts; inventories at lower of cost and net realisable value, cost on weighted average; plant SLM over 15 years; lease accounting under Ind AS 116. No policy change this year — good, last year is comparable.",
        )
    )
    parts.append(
        ar_block(
            "14. Notes to accounts (the rest of the notes)",
            "Explanatory notes that complete the financial statements: breakdowns of face-line items (property, borrowings, revenue, other income, employee cost), related parties, contingent liabilities and commitments, segment information, subsequent events, EPS, employee-benefit valuations, fair values, and anything else required for true and fair view. They are part of the financial statements, not an optional booklet.",
            "The working of the sums. The face says 'Trade receivables ₹74 crore'. The note says how much is overdue, how much is from related parties, what loss allowance was made. If you skip notes, you have not read the accounts.",
            "Schedule III faces are summarised. Material detail, risk and judgement live in the notes. Contingent liabilities (court cases, guarantees) often live only here — they are not on the Balance Sheet total.",
            "Anyone who is serious: analysts, lenders, tax officers, forensic readers, MBA students who want marks in analysis questions.",
            "What is inside this total? Who do we owe, who owes us, what might hit us later, what happened after 31 March, who are our related parties?",
            "Face ↔ matching note is a law of reading. MD&amp;A claim ↔ note evidence is the second law. Contingent liability note ↔ governance / legal proceedings in Directors' Report is the third. Section 6.11 is devoted to this.",
            "Sagar Note 12 Trade receivables: ₹74 crore, of which ₹12 crore from one distributor, overdue 120+ days, loss allowance ₹1 crore. Note 21 Related parties: ₹8 crore sales to subsidiary. Note 27 Contingent liabilities: excise demand ₹3 crore under appeal. Note 29 Subsequent events: none material. That is the real annual report.",
        )
    )
    parts.append(
        ar_block(
            "15. Notice of the Annual General Meeting",
            "A formal notice convening the AGM: company name, day, date, time, venue or video-conferencing link, ordinary business (accounts, dividend, director retirement, auditor) and special business, with an explanatory statement for special business (Section 102). Often accompanied by notes on e-voting, proxy, and how to inspect documents.",
            "The appointment card for the owners' yearly meeting. The rest of the annual report is the briefing pack. This page tells you when to come and what you will vote on.",
            "Company law: an AGM must be called, with prescribed notice period (21 clear days in ordinary cases), and members must receive the audited statements and Board's Report beforehand (Section 136).",
            "Every shareholder who will vote; company secretary; proxy advisors. Students: so you understand the report is not a magazine — it is papers for a meeting.",
            "When is the meeting? What resolutions? Any special business (preferential issue, related-party approval, remuneration) hidden after the ordinary items?",
            "Ordinary business includes adoption of the very financial statements you just studied, declaration of the dividend recommended in the Directors' Report, and appointment of the auditor who signed the opinion. Special business may be the related-party contract you saw in Note 21.",
            "Sagar Notice: 15th AGM, Tuesday 12 August 2025, 11:00 a.m. IST, video conference. Ordinary: adopt standalone and consolidated accounts, declare ₹4 dividend, reappoint a retiring director, ratify auditor remuneration. Special: approval of a material related-party transaction with Sagar Spices Pvt Ltd. That special item is why you read Note 21 before you voted.",
        )
    )

    # ------------------------------------------------------------------
    # 6.8 Financial statements inside the AR
    # ------------------------------------------------------------------
    parts.append(h2("6.8 Financial statements inside the annual report — recap and fit", "s68"))
    parts.append(
        p(
            "Chapters 4 and 5 already taught you how to <em>prepare</em> these statements. "
            "Here you learn where they <em>sit</em> in the annual report and how the four statements plus notes "
            "answer four different questions. Do not skip this even if you are confident on formats: "
            "exam questions on 'contents of annual report' expect the four statements by name."
        )
    )
    parts.append(
        table(
            ["Statement", "Question it answers", "Sagar FY 2024–25 snapshot", "Where students go wrong"],
            [
                [
                    "Statement of Profit and Loss",
                    "How much income and expense for the year? What profit?",
                    "Revenue ₹420 crore, PAT ₹38 crore, growth vs ₹350 crore and ₹31 crore.",
                    "Reading PAT and ignoring that 'other income' or a one-time gain is doing the work.",
                ],
                [
                    "Balance Sheet",
                    "What does the company own and owe on 31 March? What is the residual equity?",
                    "Equity ₹152 crore (capital ₹10 + other equity ₹142), borrowings ₹55 crore, receivables ₹74 crore, inventory ₹62 crore, cash ₹18 crore.",
                    "Looking only at total assets and missing that receivables ate the growth.",
                ],
                [
                    "Statement of Cash Flows (Ch 5)",
                    "Where did cash come from and go? Operating / investing / financing? Profit vs cash?",
                    "CFO ₹32 crore vs PAT ₹38 crore. Working-capital outflow driven by +₹28 crore receivables.",
                    "Celebrating PAT without opening this statement — the classic MBA trap.",
                ],
                [
                    "Statement of Changes in Equity",
                    "How did capital and reserves move: profit, dividend, OCI, shares issued?",
                    "Opening other equity + PAT ₹38 crore − dividend ₹4 crore (when recognised) ± OCI.",
                    "Forgetting that dividend is an equity movement, not a P&amp;L expense.",
                ],
                [
                    "Notes (including policies)",
                    "What do the totals mean? What is off-balance-sheet? Who are related parties?",
                    "Revenue split, receivable ageing, related party ₹8 crore, contingent excise ₹3 crore.",
                    "Treating notes as optional reading. They are part of the statements.",
                ],
            ],
            caption="The five-piece financial core inside every annual report",
        )
    )
    parts.append(
        logic(
            "The four statements are not four rival stories. They are four camera angles on the same year. "
            "Profit and Loss is a movie of performance. Balance Sheet is a photograph of position on 31 March. "
            "Cash Flow explains why the cash on that photograph is not equal to profit from the movie. "
            "Changes in Equity explains why the owners' residual moved. Notes print the screenplay. "
            "The annual report then puts a director's commentary (MD&amp;A), a legal cover letter (Board's Report) "
            "and an independent review (auditor) around those four angles."
        )
    )
    parts.append(
        connect(
            "When you later compute ratios (Chapter 7), you will pull the numerator from one statement and "
            "the denominator from another, often using averages of opening and closing Balance Sheet figures, "
            "and you will adjust using notes (extra-ordinary items, off-balance-sheet claims). "
            "That is 'analysis of annual report' — not a separate magical document."
        )
    )
    parts.append(
        format_box(
            "Tiny arithmetic you should always do when the highlights say 'sales grew 20%'",
            p(
                "Sagar revenue this year ₹420 crore. Last year ₹350 crore. "
                "Increase = 420 − 350 = ₹70 crore. "
                "Growth % = 70 ÷ 350 = 0.20 = <strong>20%</strong>. "
                "The MD&amp;A claim matches the face of the P&amp;L. That is step 1, not the end. "
                "PAT last year ₹31 crore, this year ₹38 crore. Increase = 7. Growth % = 7 ÷ 31 ≈ 0.2258 = "
                "<strong>22.6%</strong>. Profit grew a little faster than sales — margin expanded slightly. "
                "PAT margin this year = 38 ÷ 420 ≈ 0.0905 = <strong>9.05%</strong>. "
                "Last year 31 ÷ 350 = 0.0886 = <strong>8.86%</strong>. A small improvement, not a miracle. "
                "Now open cash flow before you write 'excellent year' in your project."
            ),
        )
    )

    # ------------------------------------------------------------------
    # 6.9 Auditor's report
    # ------------------------------------------------------------------
    parts.append(h2("6.9 Auditor's Report — read this FIRST, in simple language", "s69"))
    parts.append(
        definition(
            "The <strong>Independent Auditor's Report</strong> is the statutory auditor's written opinion "
            "on whether the financial statements give a <strong>true and fair view</strong> in accordance "
            "with the applicable financial reporting framework (Ind AS / AS and the Companies Act). "
            "The auditor does not prepare the statements — management does. The auditor obtains evidence "
            "and then reports. For listed companies the report also includes <strong>Key Audit Matters</strong> "
            "(SA 701) and, where applicable, an opinion on internal financial controls and a CARO annexure."
        )
    )
    parts.append(
        simple(
            "Management writes the exam paper (the accounts). The auditor is the external examiner. "
            "A clean (unmodified) mark means: based on the evidence I gathered, these accounts are true and fair. "
            "A qualified mark means: true and fair EXCEPT for this problem. "
            "An adverse mark means: these accounts as a whole are not true and fair. "
            "A disclaimer means: I could not get enough evidence, so I refuse to mark the paper. "
            "Emphasis of matter is a yellow sticky note on a clean paper: still a pass, but read this page."
        )
    )
    parts.append(
        why(
            "If you believe the highlights without the auditor, you are believing the examinee without the examiner. "
            "Window dressing, honest mistakes, and aggressive policy choices are why the law insists on an "
            "independent CA firm. Lenders, SEBI, and courts treat the opinion as a public signal. "
            "An MBA who quotes 'PAT ₹38 crore' without knowing the opinion is quoting a number that might be qualified."
        )
    )
    parts.append(
        real_life(
            "You open Sagar's report on page 79. The heading says Independent Auditor's Report. "
            "The last paragraph of the 'Opinion' section says the standalone statements give a true and fair view. "
            "That is unmodified. You still read Key Audit Matters: recoverability of a ₹12 crore distributor "
            "balance. You now know where the judgement sits. You jump to Note 12 before you jump to MD&amp;A."
        )
    )
    parts.append(
        logic(
            "Audit evidence is sample-based. An unmodified opinion is not a guarantee, not a certificate that "
            "the company is a good investment, and not a promise of future profits. It is a reasonable-assurance "
            "opinion on the statements taken as a whole, for this year, under this framework. "
            "That is already enormously useful — and it is not a halo."
        )
    )

    parts.append(h3("The four opinions, in words you can write in an exam"))
    parts.append(
        table(
            ["Opinion (modern SA name)", "Older textbook name", "When it is used", "What it means in human language", "Sagar-style example"],
            [
                [
                    "Unmodified",
                    "Unqualified / clean / true and fair",
                    "Statements are free from material misstatement; auditor got enough evidence.",
                    "I agree. You may use these statements.",
                    "Mehta &amp; Kale on Sagar: unmodified. The KAM does not change the opinion.",
                ],
                [
                    "Qualified",
                    "Qualified / 'except for'",
                    "There is a material misstatement, or a lack of evidence, but it is <strong>not pervasive</strong>.",
                    "True and fair except for this one (or few) issues. Do not ignore the exception.",
                    "Auditor could not attend the year-end count at one depot holding inventory of ₹18 crore. Rest is fine. Opinion: qualified — 'except for the possible effect of the depot stock'.",
                ],
                [
                    "Adverse",
                    "Adverse",
                    "Misstatements are <strong>material and pervasive</strong>. The statements as a whole are wrong.",
                    "Do not rely on these statements. They do not give a true and fair view.",
                    "Sagar (imagined disaster): revenue systematically booked on dispatch to own godowns treated as sales, inflating a large part of revenue and receivables. Auditor says the P&amp;L and Balance Sheet do not give a true and fair view.",
                ],
                [
                    "Disclaimer of opinion",
                    "Disclaimer",
                    "Auditor could not obtain sufficient appropriate evidence, and the possible effects are material and pervasive. Or multiple uncertainties.",
                    "I am not giving you an opinion. I could not examine the paper.",
                    "A fire destroyed stock records and the only computer server; opening and closing inventory and a large part of sales cannot be verified. Auditor disclaims.",
                ],
            ],
            caption="Types of audit opinion — learn the material vs pervasive line",
            foot="Material = big enough to affect a user's decision. Pervasive = not confined to particular items, or a substantial proportion of the statements, or fundamental to users' understanding.",
        )
    )
    parts.append(
        keypoint(
            "The exam distinction: <strong>qualified</strong> = material but not pervasive ('except for'). "
            "<strong>Adverse</strong> = material and pervasive ('do not present true and fair'). "
            "<strong>Disclaimer</strong> = could not get evidence, possible effects material and pervasive "
            "('we do not express an opinion'). Unmodified is the default you hope to see."
        )
    )

    parts.append(h3("Emphasis of Matter, Other Matter, Key Audit Matters — not qualifications"))
    parts.append(
        table(
            ["Paragraph", "Is the opinion still clean?", "What it is", "What you should do"],
            [
                [
                    "Emphasis of Matter (EOM)",
                    "Yes, unmodified (unless separately qualified)",
                    "Auditor draws attention to a matter already properly presented or disclosed in the notes, that is fundamental to users' understanding (SA 706). Examples: a major litigation disclosed, a fire after the reporting date disclosed, a going-concern uncertainty that is adequately disclosed.",
                    "Open the note the auditor points to. EOM is a spotlight, not a fail mark. Ignoring it is a student mistake.",
                ],
                [
                    "Other Matter",
                    "Yes (usually)",
                    "A matter not presented in the financial statements but relevant to users' understanding of the audit, the auditor's responsibilities, or the report (for example, that comparatives were audited by a previous auditor).",
                    "Read it. Do not treat it as a qualification.",
                ],
                [
                    "Key Audit Matters (KAMs)",
                    "Yes — KAMs are not a qualification",
                    "For listed companies (SA 701): matters of most significance in the audit of this period, selected from matters communicated to those charged with governance. Typical: revenue recognition, impairment, doubtful debts, inventory, litigations.",
                    "Treat KAMs as a free map of where judgement sits. Open those notes. Sagar's KAM on a ₹12 crore receivable is a gift to the analyst.",
                ],
            ],
            caption="Paragraphs that sit next to the opinion without being the opinion",
        )
    )
    parts.append(
        warn(
            "A Key Audit Matter is <strong>not</strong> a qualified opinion. Students lose marks by writing "
            "'the auditor qualified revenue because it is a KAM'. Wrong. The auditor is saying: "
            "I still give a clean opinion, but this is where I spent my hardest work — you should look too."
        )
    )
    parts.append(
        steps(
            [
                "Find the Independent Auditor's Report (often just before each of standalone and consolidated statements). There may be two reports.",
                "Read the 'Opinion' paragraph first — one of the four types. Copy the exact phrase 'true and fair' or 'except for' or 'do not' or 'we do not express'.",
                "Read the Basis for Opinion. If qualified / adverse / disclaimer, the reasons are here.",
                "Scan Emphasis of Matter / going concern paragraphs. Open the note they cite.",
                "Read Key Audit Matters. Write down the topics. Those are your note-reading list.",
                "Only now open the highlights and MD&amp;A. You now know whether you are reading a clean paper.",
            ],
            title="7. Step-by-step — how an MBA reads the auditor's report (2 minutes)",
        )
    )
    parts.append(
        memory(
            "Auditor opinions mnemonic — <strong>U-QAD</strong>: "
            "<strong>U</strong>nmodified (all good), <strong>Q</strong>ualified (good except), "
            "<strong>A</strong>dverse (not true and fair), <strong>D</strong>isclaimer (no opinion). "
            "Sticky notes on a clean paper: <strong>EOM</strong> and <strong>KAM</strong> are not U-QAD. "
            "Rule of life: <strong>auditor first, highlights second</strong>."
        )
    )
    parts.append(
        exam_answer(
            "<em>Definition.</em> The auditor's report is the independent statutory auditor's opinion on whether "
            "the financial statements give a true and fair view in accordance with the applicable framework. "
            "<em>Why an MBA reads it first.</em> The rest of the annual report is largely management's voice; "
            "the auditor is the independent check. A qualification, adverse opinion or disclaimer changes the "
            "reliability of every ratio you might compute. <em>Types.</em> Unmodified (clean); qualified "
            "(material but not pervasive exception); adverse (material and pervasive misstatement); disclaimer "
            "(insufficient evidence, effects material and pervasive). Emphasis of matter and key audit matters "
            "draw attention without, by themselves, changing a clean opinion."
        )
    )

    # ------------------------------------------------------------------
    # 6.10 Directors' Report in detail
    # ------------------------------------------------------------------
    parts.append(h2("6.10 Directors' Report in detail — Companies Act Section 134 flavour", "s610"))
    parts.append(
        definition(
            "The <strong>Directors' Report</strong> (the Act calls it the <strong>Board's Report</strong>) is "
            "the report attached to the financial statements under <strong>Section 134</strong> of the "
            "Companies Act, 2013, by which the Board of Directors explains the state of the company's affairs "
            "to the members and makes the statutory declarations, including the "
            "<strong>Directors' Responsibility Statement</strong> in Section 134(5)."
        )
    )
    parts.append(
        simple(
            "If MD&amp;A is management chatting about the year, the Directors' Report is the Board signing "
            "a legal form. Dividend is recommended here. Directors say, in writing, that the accounts are "
            "true and fair, that the company is a going concern, and that internal controls exist. "
            "Annexures hang off it: CSR, secretarial audit, related-party contracts, energy and foreign exchange."
        )
    )
    parts.append(
        why(
            "The AGM cannot honestly adopt accounts if the Board has not formally reported. "
            "Section 134 exists so that accountability is not left to a glossy letter. "
            "When something goes wrong later — a fraud, a collapse — this report is Exhibit A: "
            "what did the directors claim they had done?"
        )
    )
    parts.append(
        real_life(
            "Sagar's Board meets on 12 May 2025, approves the accounts, approves the Board's Report, "
            "recommends ₹4 per share dividend, and authorises the MD and the CS to sign. "
            "That report is printed as pages 29–52 of the annual report. Shareholders read it before they "
            "vote on 12 August."
        )
    )

    parts.append(h3("Contents of the Board's Report — the 5-mark list"))
    parts.append(
        p(
            "Section 134 and the Companies (Accounts) Rules require a cluster of items. "
            "MBA exams want a clean list with a few words of explanation. Write these."
        )
    )
    parts.append(
        table(
            ["#", "Content (exam heading)", "What you write in one line", "Sagar FY 2024–25"],
            [
                [
                    "1",
                    "State of the company's affairs",
                    "How the business did: operations, performance, maybe segment colour.",
                    "Packaged foods; revenue ₹420 crore; PAT ₹38 crore; RTE and pickles led.",
                ],
                [
                    "2",
                    "Dividend",
                    "Amount recommended or that no dividend is recommended, and any interim already paid.",
                    "Final dividend ₹4 per share (40% on ₹10 face), total ₹4 crore.",
                ],
                [
                    "3",
                    "Transfer to reserves",
                    "Amount proposed to be carried to reserves.",
                    "₹6 crore to general reserve; balance of profit left in retained earnings.",
                ],
                [
                    "4",
                    "Material changes and commitments after year-end",
                    "Events after 31 March that affect financial position (factory fire, big acquisition, strike).",
                    "None material up to the date of the report. (If there were, the notes would also speak.)",
                ],
                [
                    "5",
                    "Directors' Responsibility Statement (134(5))",
                    "The six (listed) declarations — see the table below. This is a sub-question of its own.",
                    "Reproduced in full in Sagar's report; no departure from Ind AS.",
                ],
                [
                    "6",
                    "Frauds reported by the auditor (other than those reportable to the Central Government)",
                    "Whether any fraud against the company by officers or employees was reported to the Board.",
                    "None reported.",
                ],
                [
                    "7",
                    "Conservation of energy, technology absorption, foreign exchange earnings and outgo",
                    "Rule 8 particulars — often an annexure of units saved, R&amp;D, FX earned / spent.",
                    "A new steam boiler; FX earnings from USA subsidiary dividend / exports ₹4 crore; outgo on imported packing ₹2 crore.",
                ],
                [
                    "8",
                    "CSR (if Section 135 applies)",
                    "Policy, committee, amount required, amount spent, projects — detailed annexure.",
                    "Average net profit ₹36 crore; 2% = ₹72 lakh; spent ₹72 lakh on school kitchens.",
                ],
                [
                    "9",
                    "Secretarial audit report",
                    "For listed and prescribed companies, MR-3 from a company secretary in practice, annexed.",
                    "No qualification. Board confirms compliance systems.",
                ],
                [
                    "10",
                    "Related-party particulars",
                    "Contracts / arrangements with related parties (AOC-2 where applicable) and a statement that they were in ordinary course / arm's length, or a disclosure if not.",
                    "Sales ₹8 crore to 100% subsidiary in ordinary course at arm's length; AOC-2 accordingly.",
                ],
                [
                    "11",
                    "Number of Board meetings; directors' appointments / resignations",
                    "How often the Board met; who joined or left; statement on independent directors.",
                    "Five Board meetings; one independent director reappointed.",
                ],
                [
                    "12",
                    "Risk management, internal financial controls, loans/guarantees/investments, web-link of annual return, employee particulars (if prescribed), orders passed by courts / tribunals if material",
                    "The remaining Rule / SEBI items. Group them in an exam if pressed for time; name the important ones.",
                    "IFC adequate; web-link to annual return given (MGT-7); no material court order.",
                ],
            ],
            caption="Board's Report — Section 134 flavour, exam list",
            foot="Older questions may still say 'extract of annual return (MGT-9)'. Current law: Section 92(3) web-link of the annual return. Write the modern position and you will not be marked down; if the question paper itself says MGT-9, name MGT-9.",
        )
    )

    parts.append(h3("Directors' Responsibility Statement — Section 134(5) — learn all six"))
    parts.append(
        p(
            "This is the paragraph examiners love. Directors cannot hide behind 'the CFO did it'. "
            "They must state the following. Learn the legal flavour and the simple meaning side by side."
        )
    )
    parts.append(
        table(
            ["Clause", "Exam / legal flavour (write this)", "Simple meaning"],
            [
                [
                    "(a) Accounting standards",
                    "In the preparation of annual accounts, the applicable accounting standards had been followed, along with proper explanation of material departures.",
                    "We used Ind AS / AS. If we departed, we said so and why.",
                ],
                [
                    "(b) Policies, judgements, true and fair",
                    "Directors had selected such accounting policies and applied them consistently, and made judgements and estimates that are reasonable and prudent, so as to give a true and fair view of the state of affairs at year-end and of the profit or loss for the period.",
                    "We did not hop policies to decorate profit. Our estimates (doubtful debts, useful lives) are honest.",
                ],
                [
                    "(c) Accounting records, assets, fraud",
                    "Directors had taken proper and sufficient care for the maintenance of adequate accounting records in accordance with the Act, for safeguarding assets, and for preventing and detecting fraud and other irregularities.",
                    "The books exist, assets are guarded, fraud is watched for.",
                ],
                [
                    "(d) Going concern",
                    "Directors had prepared the annual accounts on a going concern basis.",
                    "We assume Sagar will continue, not liquidate next month. If that were untrue, we would have to say so and change the basis.",
                ],
                [
                    "(e) Internal financial controls (listed companies)",
                    "Directors, in the case of a listed company, had laid down internal financial controls to be followed by the company and that such internal financial controls are adequate and were operating effectively.",
                    "The listed-company extra: the control system over money and reporting actually works.",
                ],
                [
                    "(f) Compliance systems",
                    "Directors had devised proper systems to ensure compliance with all applicable laws and that such systems were adequate and operating effectively.",
                    "Not only accounting law — factories, labour, SEBI, food safety — and the system is real, not a binder on a shelf.",
                ],
            ],
            caption="Directors' Responsibility Statement — six clauses you should be able to reproduce",
        )
    )
    parts.append(
        memory(
            "DRS six-clause mnemonic — <strong>SPRFGC</strong>: "
            "<strong>S</strong>tandards followed, <strong>P</strong>olicies consistent + prudent estimates, "
            "<strong>R</strong>ecords / assets / fraud care, <strong>G</strong>oing concern, "
            "<strong>F</strong>inancial controls (listed), <strong>C</strong>ompliance systems. "
            "Or a sentence: <strong>'Standards, Policies, Records; Going concern, Financial controls, Compliance.'</strong>"
        )
    )
    parts.append(
        exam_tip(
            "If the question is 'contents of Directors' Report' (5 marks), list 8–10 headings from the big table "
            "and write the DRS as one heading with 3–4 of its clauses. "
            "If the question is specifically 'Directors' Responsibility Statement', reproduce all six clauses "
            "in legal flavour. That alone can be 5 marks."
        )
    )

    parts.append(h3("Annexures students mix up — keep them separate"))
    parts.append(
        table(
            ["Annexure / report", "Who prepares it", "On what", "Where it lives"],
            [
                [
                    "CSR annual report / annexure",
                    "Board (CSR committee recommends)",
                    "2% spend, projects, unspent amounts",
                    "Annexure to Directors' Report",
                ],
                [
                    "Secretarial audit report (MR-3)",
                    "Practising Company Secretary",
                    "Compliance with company law, SEBI, board processes — not the numbers",
                    "Annexure to Directors' Report",
                ],
                [
                    "AOC-2 related-party contracts",
                    "Board",
                    "Related-party contracts not in ordinary course / not arm's length (and prescribed particulars)",
                    "Annexure to Directors' Report; the numbers also appear in notes",
                ],
                [
                    "Statutory auditor's report",
                    "Chartered accountant firm",
                    "True and fair view of financial statements",
                    "With the financial statements, not as a CSR-style annexure",
                ],
                [
                    "BRSR",
                    "Management, approved as part of the annual report",
                    "ESG indicators",
                    "Its own section, not the same as CSR annexure",
                ],
            ],
            caption="Do not staple the wrong report to the wrong parent",
        )
    )

    # ------------------------------------------------------------------
    # 6.11 Notes vs face
    # ------------------------------------------------------------------
    parts.append(h2("6.11 Notes to accounts versus the face of the statements", "s611"))
    parts.append(
        definition(
            "The <strong>face</strong> of the financial statements is the main summarised statement itself "
            "(the Balance Sheet page, the Profit and Loss page, the Cash Flow page, the Changes in Equity page) "
            "prepared in the Schedule III vertical form. "
            "The <strong>notes to accounts</strong> are the numbered explanations, breakdowns and additional "
            "disclosures that <em>form part of</em> those statements. Together, face + notes + policies = "
            "the complete financial statements."
        )
    )
    parts.append(
        simple(
            "The face is the newspaper headline and the first paragraph. The notes are the rest of the article, "
            "the table of figures, and the correction box. If you quote only the headline 'Trade receivables "
            "₹74 crore', you have not told anyone that ₹12 crore is one overdue distributor."
        )
    )
    parts.append(
        why(
            "Schedule III forces a comparable one-page skeleton so two companies can be lined up. "
            "That skeleton cannot hold ageing, related parties, contingent liabilities, policy choices, "
            "segment splits or subsequent events. Those would make the face unreadable. So the law puts "
            "them in notes and says they are not optional."
        )
    )
    parts.append(
        table(
            ["Item", "What the face typically shows", "What the note adds", "Why the note can change your decision"],
            [
                [
                    "Revenue",
                    "Revenue from operations ₹420 crore",
                    "Disaggregation: spices ₹180, pickles ₹140, RTE ₹100; geography; reconciling discounts",
                    "Growth is in RTE and pickles, not in the old spices cash-cow. Strategy looks different.",
                ],
                [
                    "Trade receivables",
                    "₹74 crore as one line under current assets",
                    "Ageing, expected credit loss, related-party receivables, movement in allowance",
                    "₹12 crore stuck with one distributor. Credit risk is concentrated.",
                ],
                [
                    "Borrowings",
                    "Current + non-current totals",
                    "Security, interest rates, defaults, repayment schedule, unused limits",
                    "A current ratio that looks fine may hide a large loan due in 4 months.",
                ],
                [
                    "Contingent liabilities",
                    "Usually <strong>nothing on the face totals</strong>",
                    "Guarantees, disputed tax, court cases (to the extent not provided)",
                    "Sagar's ₹3 crore excise demand is invisible if you never open the note.",
                ],
                [
                    "Related parties",
                    "Rarely obvious on the face",
                    "Names, nature of relationship, sales, purchases, balances, terms",
                    "₹8 crore parent-to-subsidiary sales: real in standalone, gone in consolidated.",
                ],
                [
                    "Subsequent events",
                    "Balance Sheet is still 31 March",
                    "Events after reporting date that are adjusting or non-adjusting",
                    "A 10 April factory fire may not change 31 March numbers but must be read.",
                ],
            ],
            caption="Face versus notes — same year, different resolution",
        )
    )
    parts.append(
        keypoint(
            "If it is material and it is not on the face, it is in the notes. "
            "If you skip the notes, you have not read the financial statements. "
            "That sentence is worth underlining in your exam pad."
        )
    )
    parts.append(
        mistakes(
            [
                "Treating notes as 'extra information for CA students' — they are part of the statements for everyone.",
                "Comparing two companies' faces without checking that inventory and revenue policies in Note 1 are similar.",
                "Missing contingent liabilities because they are not added into the Balance Sheet total.",
                "Missing related-party balances that sit inside 'trade receivables' on the face.",
                "Using dashboard 'revenue' that is gross, while the face is net of discounts — always reconcile.",
            ]
        )
    )

    # ------------------------------------------------------------------
    # 6.12 How sections connect — walkthrough
    # ------------------------------------------------------------------
    parts.append(h2("6.12 How the sections connect — a full walkthrough of Sagar", "s612"))
    parts.append(
        p(
            "This is the skill the chapter title means by 'analysis'. "
            "You do not analyse an annual report by computing one ratio in a vacuum. "
            "You walk a claim from the story layer down to the evidence layer. "
            "Below is one walk, slow, with every multiplication shown. "
            "On the exam, even a short version of this walk scores, because it shows you understand composition, "
            "not just a memorised list of contents."
        )
    )
    parts.append(
        steps(
            [
                "<strong>Claim (MD&amp;A / Chairman).</strong> 'Sales grew 20%, driven by strong demand for Sagar Pickles in North India and the new ready-to-eat line.'",
                "<strong>Face of P&amp;L.</strong> Revenue from operations ₹420 crore versus ₹350 crore. Increase = 420 − 350 = ₹70 crore. 70 ÷ 350 = 0.20 = 20%. The headline matches.",
                "<strong>Revenue note (disaggregation).</strong> Spices ₹180 crore versus ₹175 crore: increase 5; 5 ÷ 175 ≈ 0.0286 = 2.9% (almost flat). Pickles ₹140 versus ₹110: increase 30; 30 ÷ 110 ≈ 0.2727 = 27.3%. Ready-to-eat ₹100 versus ₹65: increase 35; 35 ÷ 65 ≈ 0.5385 = 53.8%. The story is true for pickles and RTE, generous for 'the company' as a whole, and spicy-side silent.",
                "<strong>Segment / geography note.</strong> North India ₹200 crore versus ₹150 crore: increase 50; 50 ÷ 150 ≈ 0.333 = 33%. North India really did pull. West was quiet. The 'North India pickles' clause survives.",
                "<strong>Cash Flow Statement.</strong> PAT ₹38 crore. CFO ₹32 crore. Trade receivables on the Balance Sheet ₹74 crore versus ₹46 crore last year. Increase in receivables = 74 − 46 = ₹28 crore. A large part of the extra sales is still stuck with customers. Growth was booked; it was not fully collected.",
                "<strong>Receivables note.</strong> ₹12 crore from one distributor, 120+ days overdue, loss allowance only ₹1 crore. This is the same balance the auditor put in a Key Audit Matter. MD&amp;A mentioned 'distributor credit' as a risk — good — but the highlights page did not.",
                "<strong>Ratios (preview of Chapter 7).</strong> Debtor days this year: (74 ÷ 420) × 365 ≈ 0.1762 × 365 ≈ 64.3 days. Last year: (46 ÷ 350) × 365 ≈ 0.1314 × 365 ≈ 48.0 days. Collections slowed by about 16 days. Net profit margin 38 ÷ 420 ≈ 9.05% versus 8.86% — a small gain that looks weaker once you know cash lagged.",
                "<strong>Auditor.</strong> Unmodified opinion. You may still use the statements. You may not ignore the KAM. There is no qualification to hide behind and no excuse to skip the note.",
                "<strong>Governance / related party.</strong> Parent sold ₹8 crore of goods to Sagar Spices Pvt Ltd. In standalone that is revenue. In consolidated it is eliminated (420 + 40 + 22 − 8 = ₹474 crore group revenue). Check AOC-2 and the audit committee: ordinary course, arm's length. If it had been a sale to the MD's brother's private firm at a strange price, the governance report would become the main chapter, not a side page.",
            ],
            title="7. The claim-to-cash walk — Sagar's 20% growth",
        )
    )
    parts.append(
        table(
            ["Layer", "What it said", "Verdict after the walk"],
            [
                ["Chairman / MD&amp;A", "Sales grew 20%, pickles + North + RTE", "Headline true; spices almost flat; say so."],
                ["P&amp;L face", "₹420 vs ₹350 crore", "Matches the 20%."],
                ["Notes", "Product and geography split; ₹12 crore overdue", "Quality of growth is mixed; credit risk concentrated."],
                ["Cash flow", "CFO ₹32 crore; receivables +₹28 crore", "Accrual growth richer than cash growth."],
                ["Ratios", "Debtor days 48 → 64", "Collections deteriorated."],
                ["Auditor", "Unmodified + KAM on that receivable", "Numbers usable; spotlight on the distributor."],
                ["Governance", "₹8 crore to 100% subsidiary", "Eliminated in consol; watch arm's length, but not a scandal on these facts."],
            ],
            caption="One claim, seven checkpoints — this is 'analysis of annual report'",
        )
    )
    parts.append(
        logic(
            "Why this walk is the whole subject in miniature: the annual report is designed so that "
            "narrative, legal stewardship, numbers, notes and independent opinion can be reconciled. "
            "If they cannot, either you have found a red flag or you have misread a policy. "
            "That reconciliation is the MBA's job. Memorising the list of contents without this walk "
            "is the 5-mark version of the chapter. Doing the walk is the 10-mark version."
        )
    )

    # ------------------------------------------------------------------
    # 6.13 Limitations
    # ------------------------------------------------------------------
    parts.append(h2("6.13 Limitations of annual reports", "s613"))
    parts.append(
        definition(
            "<strong>Limitations of annual reports</strong> are the reasons a careful user cannot treat the "
            "report as a complete, current, bias-free photograph of the company. They do not make the report "
            "useless. They make naive reading dangerous. A mature 8-mark answer on 'importance' often "
            "closes with three limitations."
        )
    )
    parts.append(simple(
        "The report is a very good yearly pack. It is not CCTV. It is not a crystal ball. "
        "It is not immune to clever presentation. That is all 'limitations' means."
    ))
    parts.append(
        table(
            ["Limitation", "Simple meaning", "Sagar sting"],
            [
                [
                    "Historical",
                    "The year ended on 31 March. You may be reading the PDF in August. The world has moved.",
                    "A new competitor launched in June. The report cannot tell you that unless a subsequent-event note exists.",
                ],
                [
                    "Aggregation",
                    "Totals hide mix. One number for 'revenue', one for 'receivables'.",
                    "₹420 crore hid a flat spices line. ₹74 crore hid one sick distributor.",
                ],
                [
                    "Accounting policy choices",
                    "Honest alternatives (SLM vs WDV, weighted average vs FIFO, useful lives) change profit and ratios. Two companies are not always comparable.",
                    "If a peer depreciates plant over 10 years and Sagar over 15, Sagar's PAT looks kinder.",
                ],
                [
                    "Estimates and judgements",
                    "Doubtful debts, impairment, fair values, warranty — these are opinions with evidence, not tape-measures.",
                    "₹1 crore loss allowance on a ₹12 crore overdue balance is a judgement. Another CFO might have provided ₹4 crore.",
                ],
                [
                    "Window dressing / creative accounting",
                    "Legal but cosmetic tricks around year-end: channel stuffing, reclassification, delaying maintenance, pushing sales.",
                    "If Sagar pushed ₹20 crore of pickle into distributors on 30 March with a right of return, revenue is 'up' and January will hurt. Cash flow and subsequent returns expose it.",
                ],
                [
                    "Non-financial not fully captured",
                    "Brand, culture, food-safety culture, founder health, employee morale — BRSR helps, it does not complete.",
                    "A legendary Sagar pickle recipe is an asset the Balance Sheet never names.",
                ],
                [
                    "Delay / time lag",
                    "AGM can be as late as 30 September for a 31 March year. Analysis in April has to live on quarterly results.",
                    "You cannot wait for the annual report to make every decision. Listed companies also publish quarters.",
                ],
                [
                    "Narrative bias in the story layer",
                    "Chairman's letter and MD&amp;A are partly investor-relations writing. They rarely lead with bad news.",
                    "'Spices stable' for +2.9% is a soft word. The note was harder and better.",
                ],
                [
                    "Inflation and current values",
                    "Historical-cost accounts do not restate a 2012 factory at 2025 prices. Comparability across high-inflation years suffers.",
                    "Sagar's land in Andheri is almost certainly worth more than book value. ROE on book equity can mislead.",
                ],
                [
                    "Off-balance-sheet and contingent items",
                    "Some risks live only in notes (disputes, guarantees, certain commitments).",
                    "The ₹3 crore excise demand never entered the total of equity and liabilities.",
                ],
            ],
            caption="Limitations — write any six with a one-line sting in the exam",
        )
    )
    parts.append(
        why(
            "If annual reports had no limitations, we would not need quarterly results, credit-rating visits, "
            "forensic audits, or Chapter 7's habit of interrogating every ratio. "
            "Teaching limitations is not cynicism. It is the difference between a reader and a believer."
        )
    )
    parts.append(
        memory(
            "Limitations mnemonic — <strong>HAPPY WINDOW</strong> is too long; use "
            "<strong>HAD WIN</strong>: <strong>H</strong>istorical, <strong>A</strong>ggregation, "
            "<strong>D</strong>elay, <strong>W</strong>indow dressing, <strong>I</strong>nflation / incomplete "
            "non-financial, <strong>N</strong>otes-only (contingent) plus policy/estimate judgement. "
            "Three in an importance answer is enough; six in a dedicated 'limitations' question."
        )
    )

    # ------------------------------------------------------------------
    # 6.14 30-minute reading sequence
    # ------------------------------------------------------------------
    parts.append(h2("6.14 How an MBA should read an annual report in 30 minutes", "s614"))
    parts.append(
        simple(
            "You will rarely have a free Sunday for all 168 pages. You need a repeatable sequence that "
            "hits identity, reliability, dashboard, faces, notes that matter, story-versus-evidence, "
            "and stewardship. This is that sequence. It is also an exam-friendly 'steps' answer: "
            "'Explain how you would analyse an annual report.'"
        )
    )
    parts.append(
        steps(
            [
                "<strong>Minutes 0–2 — Identity.</strong> Cover, corporate information. Write down: name, CIN, year-end, listed or not, auditor's name, MD, Chairman (same person?). Confirm you are not mixing two companies with similar names.",
                "<strong>Minutes 2–5 — Auditor first.</strong> Standalone opinion type. Consolidated opinion type. Basis paragraph. Emphasis of matter. Key Audit Matters. If qualified / adverse / disclaimer, the rest of the 25 minutes is about that problem. If clean, write the KAM topics on your pad — they are the note list.",
                "<strong>Minutes 5–8 — Dashboard.</strong> Highlights / 5-year figures. Compute two growth rates yourself (revenue, PAT). Look at debt and EPS direction. Do not accept a graph without reading the axis.",
                "<strong>Minutes 8–13 — Faces.</strong> P&amp;L: revenue, gross profit if given, other income, PAT. Balance Sheet: equity, borrowings, inventory, receivables, cash. Cash flow: CFO vs PAT, big investing outflows, financing (debt drawn or repaid, dividend). Glance at consolidated vs standalone revenue to see how big the group is.",
                "<strong>Minutes 13–20 — Notes that matter.</strong> (1) Significant accounting policies — any change? (2) Revenue breakdown. (3) Receivables ageing and related-party receivables. (4) Borrowings — current portion, defaults. (5) Contingent liabilities. (6) Related parties. (7) Subsequent events. (8) Whatever the KAM named. This block is the highest-value seven minutes in the half-hour.",
                "<strong>Minutes 20–25 — Story versus evidence.</strong> Read MD&amp;A headings and the Chairman's letter now, not earlier. Tick claims that you have already verified. Circle claims that the notes contradict or that cash flow weakens. You are doing Section 6.12 at speed.",
                "<strong>Minutes 25–28 — Stewardship.</strong> Directors' Report: dividend, DRS (any departure from standards?), material changes, frauds, CSR. Secretarial audit: qualified or not?",
                "<strong>Minutes 28–30 — Governance red flags.</strong> Independent directors, audit committee, related-party approvals, auditor rotation / remuneration, any special business in the AGM notice that reveals a transaction the notes already flagged.",
            ],
            title="7. Step-by-step method — 30 minutes, exam-friendly",
        )
    )
    parts.append(
        format_box(
            "What you write on a one-page working paper in those 30 minutes",
            ul(
                [
                    "Company / year / auditor / opinion type / KAM topics.",
                    "Revenue this year vs last, PAT this year vs last, CFO vs PAT (three pairs of numbers).",
                    "One good news, one worry from the notes (Sagar: RTE growth; distributor ₹12 crore).",
                    "Dividend and any qualification in Board's Report or secretarial audit.",
                    "One question you still cannot answer (then you know where to spend hour two, if you get it).",
                ]
            )
            + p(
                "If the exam asks for 'steps in analysis of annual report', turn the eight minute-blocks "
                "into eight numbered steps without the clock. The clock is for real life; the order is for marks."
            ),
        )
    )
    parts.append(
        exam_tip(
            "A 5-mark 'procedure to read / analyse annual report' answer is this sequence, compressed: "
            "(1) identity (2) auditor (3) highlights (4) faces of FS including cash flow (5) notes and policies "
            "(6) MD&amp;A versus numbers (7) Directors' Report (8) governance. "
            "Starting with MD&amp;A is a common mistake — that is how you get sold the story."
        )
    )
    parts.append(
        keypoint(
            "Practical habit after this chapter: download one real annual report of an FMCG company you know "
            "(a listed pickle, biscuit or tea company) and run the 30-minute sequence once. "
            "The fictional Sagar pack is the rehearsal. A live PDF is the stage."
        )
    )

    # ------------------------------------------------------------------
    # 6.15 Solved examples
    # ------------------------------------------------------------------
    parts.append(h2("6.15 Solved examples", "s615"))

    parts.append(
        example(
            "1",
            "Easy",
            "Which section of the annual report do I open?",
            p("For each user need, name the first section you would open, and one backup section.")
            + table(
                ["Need", "First section", "Backup section", "Why"],
                [
                    [
                        "Is the profit figure trustworthy?",
                        "Independent Auditor's Report",
                        "Notes on revenue and receivables; KAM",
                        "Opinion first; then the places judgement hides.",
                    ],
                    [
                        "Did sales really grow 20%?",
                        "Statement of Profit and Loss",
                        "Revenue note; then cash flow",
                        "Face gives the %, note gives the mix, cash flow gives collection.",
                    ],
                    [
                        "Can the company pay the proposed dividend?",
                        "Standalone P&amp;L and Balance Sheet (distributable profits / cash)",
                        "Cash flow — financing section; Directors' Report dividend para",
                        "Dividend is a standalone legal act, paid in cash.",
                    ],
                    [
                        "Are promoters dealing with themselves?",
                        "Related-party note",
                        "AOC-2 / Directors' Report; governance report; AGM special business",
                        "Numbers in notes, approval in stewardship, vote in the notice.",
                    ],
                    [
                        "Any court case that could explode?",
                        "Contingent liabilities note",
                        "Directors' Report (material changes / legal); EOM in audit report",
                        "Often invisible on the face.",
                    ],
                    [
                        "How does management explain a bad year?",
                        "MD&amp;A",
                        "Chairman's letter — then verify against notes",
                        "Story layer, then evidence.",
                    ],
                ],
            )
            + p(
                "<strong>Teaching point.</strong> Matching the need to the section is half of this chapter. "
                "If you can fill a table like this in the exam, you have 'composition' plus 'use'."
            ),
        )
    )

    parts.append(
        example(
            "2",
            "Moderate",
            "Sagar's growth: verify the claim and comment on cash quality",
            p(
                "<strong>Given (from Sagar's annual report).</strong> MD&amp;A: 'Revenue grew 20%.' "
                "P&amp;L: revenue ₹420 crore (last year ₹350 crore), PAT ₹38 crore (last year ₹31 crore). "
                "Revenue note: spices ₹180 cr (LY ₹175 cr); pickles ₹140 cr (LY ₹110 cr); RTE ₹100 cr (LY ₹65 cr). "
                "Balance Sheet: trade receivables ₹74 cr (LY ₹46 cr). Cash flow: cash from operations ₹32 cr. "
                "Auditor: unmodified, KAM on a ₹12 cr distributor receivable. "
                "Loss allowance on that distributor: ₹1 cr."
            )
            + p("<strong>Required.</strong> (a) Verify the 20% claim with arithmetic. (b) Identify which products grew. "
                "(c) Comment on cash quality. (d) What should an MBA write in a 4-mark 'analysis' note?")
            + h4("(a) Headline growth")
            + p("Increase in revenue = 420 − 350 = ₹70 crore.")
            + p("Growth rate = 70 ÷ 350 = 0.20 = <strong>20.00%</strong>. The MD&amp;A claim matches the face.")
            + p("PAT increase = 38 − 31 = ₹7 crore. PAT growth = 7 ÷ 31 = 0.225806… ≈ <strong>22.58%</strong>.")
            + p("PAT margin now = 38 ÷ 420 = 0.090476… ≈ <strong>9.05%</strong>. Last year 31 ÷ 350 = 0.088571… ≈ <strong>8.86%</strong>.")
            + h4("(b) Product mix — do not skip this multiplication")
            + p("Spices: 180 − 175 = ₹5 crore increase. 5 ÷ 175 = 0.028571… ≈ <strong>2.86%</strong> — almost flat.")
            + p("Pickles: 140 − 110 = ₹30 crore. 30 ÷ 110 = 0.272727… ≈ <strong>27.27%</strong>.")
            + p("RTE: 100 − 65 = ₹35 crore. 35 ÷ 65 = 0.538461… ≈ <strong>53.85%</strong>.")
            + p("Check the three products add up: 180 + 140 + 100 = ₹420 crore. Last year 175 + 110 + 65 = ₹350 crore. The note agrees with the face.")
            + p("Share of the ₹70 crore increase: spices 5/70 ≈ 7%; pickles 30/70 ≈ 43%; RTE 35/70 = 50%. RTE and pickles did the work.")
            + h4("(c) Cash quality")
            + p("Increase in trade receivables = 74 − 46 = ₹28 crore.")
            + p("CFO ₹32 crore versus PAT ₹38 crore. Gap = 6, and the receivables jump of 28 is the smoking gun that collections lagged bookings.")
            + p("Debtor days ≈ (74 ÷ 420) × 365. 74 ÷ 420 = 0.176190… × 365 ≈ 64.31 days.")
            + p("Last year (46 ÷ 350) × 365. 46 ÷ 350 = 0.131429… × 365 ≈ 47.97 days. Slowdown ≈ 16 days.")
            + p("Of ₹74 crore, ₹12 crore is one overdue distributor with only ₹1 crore provided. 12 ÷ 74 ≈ 16.2% of book is concentrated and sick-looking.")
            + h4("(d) Four-mark analysis note you could write")
            + p(
                "The 20% revenue growth is arithmetically correct but uneven: ready-to-eat (+53.85%) and pickles (+27.27%) "
                "explain almost all of the ₹70 crore increase; spices grew only 2.86%. Cash did not fully follow accrual: "
                "CFO ₹32 crore against PAT ₹38 crore, with receivables up ₹28 crore and debtor days up from ~48 to ~64. "
                "The auditor's unmodified opinion lets us use the figures, but the KAM on a ₹12 crore overdue distributor "
                "(allowance only ₹1 crore) is the quality-of-earnings issue. An MBA should not describe the year as "
                "'excellent growth' without those two qualifications: mix and collections."
            ),
        )
    )

    parts.append(
        example(
            "3",
            "Exam",
            "Write the 5-mark 'contents of annual report' and the 5-mark 'Directors' Report' as the examiner wants them",
            h4("Question A (5 marks): 'Enumerate the contents of an annual report of a listed company.'")
            + p("<strong>Answer (write this shape).</strong> An annual report of a typical Indian listed company usually contains the following, in something like this order:")
            + ol(
                [
                    "<strong>Cover and corporate information</strong> — name, year, CIN, registered office, board, bankers, auditors.",
                    "<strong>Chairman's / MD's message</strong> — narrative of the year and outlook.",
                    "<strong>Board of Directors</strong> — names, categories (executive / independent).",
                    "<strong>Financial highlights / performance at a glance</strong> — multi-year dashboard.",
                    "<strong>Management Discussion and Analysis</strong> — industry, segments, risks, internal control, financial review (SEBI LODR).",
                    "<strong>Directors' Report (Board's Report) and annexures</strong> — Section 134: state of affairs, dividend, reserves, DRS, CSR, secretarial audit, related party, etc.",
                    "<strong>Corporate Governance Report</strong> — board, committees, attendance, shareholder information.",
                    "<strong>Business Responsibility and Sustainability Report</strong> — ESG disclosures for specified listed companies.",
                    "<strong>Standalone financial statements</strong> — Balance Sheet, Statement of Profit and Loss, Cash Flow, Changes in Equity, notes.",
                    "<strong>Consolidated financial statements</strong> — parent plus subsidiaries after elimination of intra-group items.",
                    "<strong>Independent Auditor's Report(s)</strong> — opinion on the statements, KAMs, perhaps IFC and CARO.",
                    "<strong>Significant accounting policies and notes to accounts</strong> — measurement rules and detailed disclosures.",
                    "<strong>Notice of the AGM</strong> — date, time, ordinary and special business.",
                ]
            )
            + p("Even 10 of these 13, each with a 4–8 word explanation, fills 5 marks. A bare list of five words ('balance sheet, P&amp;L, cash flow…') does not.")
            + h4("Question B (5 marks): 'What are the contents of the Directors' Report under the Companies Act, 2013?'")
            + p("<strong>Answer (write this shape).</strong> The Board's Report under Section 134 (read with the Accounts Rules) includes:")
            + ol(
                [
                    "State of the company's affairs.",
                    "Amount of dividend, if any, recommended.",
                    "Amount, if any, proposed to be carried to reserves.",
                    "Material changes and commitments affecting financial position occurring after the end of the year.",
                    "Directors' Responsibility Statement (Section 134(5) — standards, policies and estimates, records/assets/fraud, going concern, internal financial controls for listed companies, compliance systems).",
                    "Details of frauds reported by the auditor (other than those reportable to the Central Government), if any.",
                    "Conservation of energy, technology absorption, foreign exchange earnings and outgo.",
                    "CSR particulars (where Section 135 applies), secretarial audit report, related-party contracts (AOC-2), number of meetings, director changes, risk and IFC, web-link of annual return, and other prescribed matters.",
                ]
            )
            + p(
                "If marks remain, unpack DRS as the six clauses. That single unpacking often separates a 3/5 from a 5/5."
            ),
        )
    )

    parts.append(
        example(
            "4",
            "Exam",
            "Auditor's report types — choose the opinion",
            p("For each situation, name the opinion (or paragraph) and say why. This is a typical 4–6 mark application.")
            + table(
                ["Situation", "Opinion / paragraph", "Why"],
                [
                    [
                        "Inventory at 19 depots counted; one small depot of ₹0.4 crore not visited; total inventory ₹62 crore; nothing else wrong.",
                        "Unmodified (the amount is almost certainly immaterial)",
                        "Qualification requires materiality. ₹0.4 crore on a ₹420 crore company is not decision-changing.",
                    ],
                    [
                        "Same, but the unvisited depot holds ₹18 crore and is material; rest of the statements are all right.",
                        "Qualified ('except for')",
                        "Material lack of evidence, not pervasive — confined to inventory / related COGS at that depot.",
                    ],
                    [
                        "Management refuses to write down a clearly dead technology plant that is half the total assets; profit is thereby hugely overstated.",
                        "Adverse",
                        "Material and pervasive — the statements as a whole do not give a true and fair view.",
                    ],
                    [
                        "A flood destroyed all stock records and the accounting server; opening stock, closing stock and a large slice of sales cannot be tested.",
                        "Disclaimer",
                        "Insufficient evidence; possible effects material and pervasive; auditor does not opine.",
                    ],
                    [
                        "A factory fire on 10 April is properly disclosed in a subsequent-event note; 31 March numbers are fairly stated; going concern intact.",
                        "Unmodified + Emphasis of Matter pointing to that note",
                        "Spotlight, not a fail. The matter is disclosed; the opinion remains clean.",
                    ],
                    [
                        "Revenue schemes are complex; auditor spent the most hours there; evidence supports the number.",
                        "Unmodified + Key Audit Matter on revenue schemes",
                        "KAM ≠ qualification. It is a map of audit effort.",
                    ],
                ],
            ),
        )
    )

    # ------------------------------------------------------------------
    # 6.16 Identify
    # ------------------------------------------------------------------
    parts.append(h2("6.16 How to identify the question", "s616"))
    parts.append(
        identify(
            "This chapter is theory-heavy, so the first 15 seconds in the exam hall are about labelling the question. "
            "If the question says <strong>'define annual report'</strong> / 'what is an annual report' → 1–2 mark definition: "
            "yearly statutory-cum-communication document for shareholders, containing audited financial statements plus Board's Report, auditor's report and other disclosures. "
            "If it says <strong>'contents'</strong> / 'composition' / 'enumerate the parts' → the ordered list in 6.6 (story, stewardship, evidence, notice). "
            "If it says <strong>'need'</strong> / <strong>'importance'</strong> / 'why annual reports are prepared' → the 8–10 points in 6.5 plus users. "
            "If it says <strong>'users'</strong> / 'parties interested' → the user table in 6.4. "
            "If it says <strong>'Directors' Report'</strong> / 'Board's Report' / 'Section 134' → contents list + DRS six clauses. "
            "If it says <strong>'Directors' Responsibility Statement'</strong> alone → only the six clauses, in legal flavour. "
            "If it says <strong>'auditor's report'</strong> / 'types of opinion' / 'true and fair' → 6.9, U-QAD + EOM + KAM. "
            "If it says <strong>'MD&amp;A'</strong> / 'Management Discussion' → what it is, SEBI listed-company context, typical headings, and how it differs from the Directors' Report. "
            "If it says <strong>'notes to accounts'</strong> → face vs notes, examples, 'notes are part of the statements'. "
            "If it says <strong>'limitations'</strong> → HAD WIN table. "
            "If it says <strong>'how to analyse'</strong> / 'procedure to read' → the 30-minute / eight-step sequence. "
            "If it says <strong>'standalone vs consolidated'</strong> → parent legal entity vs group after elimination. "
            "A mixed 8–10 mark question ('importance of annual report to various parties' or 'financial and non-financial parts') is 6.5 + 6.4 + a paragraph on how story, stewardship and evidence must be read together (6.12)."
        )
    )
    parts.append(
        table(
            ["Question stem (as printed)", "Marks usually", "Your opening move", "Do not"],
            [
                [
                    "What is an annual report?",
                    "1–2",
                    "One tight definition + statutory and communication natures",
                    "Dump the 13-item contents list",
                ],
                [
                    "Contents / composition of annual report",
                    "5",
                    "Numbered list, one line each, listed-company order",
                    "Write only BS and P&amp;L",
                ],
                [
                    "Need and importance",
                    "5–8",
                    "8 numbered points with explanation; add users if 8 marks",
                    "Write 'it is very important for all' in one paragraph",
                ],
                [
                    "Directors' Report",
                    "5",
                    "Section 134 list; mention DRS",
                    "Confuse with MD&amp;A",
                ],
                [
                    "DRS / Section 134(5)",
                    "4–5",
                    "All six clauses",
                    "Write only 'directors are responsible'",
                ],
                [
                    "Auditor's report / types of opinion",
                    "5",
                    "U-QAD table + why MBA reads it first",
                    "Call a KAM a qualification",
                ],
                [
                    "MD&amp;A",
                    "4–5",
                    "SEBI narrative; typical heads; not statutory Board's Report",
                    "Say it is audited like the P&amp;L",
                ],
                [
                    "Limitations of annual report / of financial statements",
                    "5",
                    "HAD WIN with examples",
                    "Say 'annual reports are useless'",
                ],
                [
                    "How would you analyse / read",
                    "5–8",
                    "Auditor-first eight steps; claim-to-cash walk",
                    "Start with the Chairman's photograph",
                ],
            ],
            caption="Question identifier — look at the verb before you look at your memory sheet",
        )
    )

    # ------------------------------------------------------------------
    # 6.17 Exam-ready answers
    # ------------------------------------------------------------------
    parts.append(h2("6.17 Exam-ready answers (1 mark, 5 mark, 8–10 mark)", "s617"))

    parts.append(
        qna(
            "Define annual report.",
            p(
                "An annual report is the yearly statutory-cum-communication document published by a company "
                "for its shareholders and other users, setting out its activities, performance, financial "
                "position, cash flows, governance and outlook for the financial year. It contains the audited "
                "financial statements (with notes), the Board's Report, the independent auditor's report, and, "
                "in a listed company, MD&amp;A, a corporate governance report and other prescribed disclosures, "
                "together with the notice of the AGM."
            ),
            "1–2 marks",
        )
    )
    parts.append(
        qna(
            "Enumerate the contents / composition of the annual report of a listed company.",
            p("A typical Indian listed-company annual report contains, usually in this order:")
            + ol(
                [
                    "Cover and corporate information (CIN, board, bankers, auditors, registered office).",
                    "Chairman's / Managing Director's message.",
                    "Board of Directors.",
                    "Highlights / performance at a glance.",
                    "Management Discussion and Analysis (MD&amp;A).",
                    "Directors' Report (Board's Report) with statutory annexures (CSR, secretarial audit, related party, energy / FX).",
                    "Corporate Governance Report.",
                    "Business Responsibility and Sustainability Report (BRSR), for specified listed companies.",
                    "Standalone financial statements: Balance Sheet, Statement of Profit and Loss, Cash Flow Statement, Statement of Changes in Equity, and notes.",
                    "Consolidated financial statements of the group.",
                    "Independent Auditor's Report (often placed immediately before the statements it covers; separate reports for standalone and consolidated).",
                    "Significant accounting policies and other notes to accounts.",
                    "Notice of the Annual General Meeting.",
                ]
            )
            + p(
                "These parts fall in three layers plus an action page: story (Chairman, highlights, MD&amp;A), "
                "stewardship (Directors' Report, governance, BRSR), evidence (statements, policies, notes, auditor), "
                "and the AGM notice."
            ),
            "5 marks",
        )
    )
    parts.append(
        qna(
            "Explain the need and importance of annual reports. Who are the users?",
            p(
                "<strong>Need.</strong> Shareholders do not manage the company day to day. Without a yearly, "
                "comparable, audited public pack, stewardship cannot be judged, capital cannot be priced, and "
                "the Companies Act / SEBI duties cannot be discharged. The annual report fills that gap."
            )
            + p("<strong>Importance</strong> (write 8 points):")
            + ol(
                [
                    "<strong>Transparency</strong> — performance, position, cash, related parties and risks are made visible.",
                    "<strong>Stewardship</strong> — directors render account of shareholders' money through the Board's Report and audited statements.",
                    "<strong>Legal compliance</strong> — Companies Act (accounts, Board's Report, audit, circulation, filing) and SEBI LODR for listed companies.",
                    "<strong>Decision-useful information</strong> — basis for buy / hold / sell / lend / rate / join.",
                    "<strong>Comparison</strong> — across years (highlights, consistent statements) and, with care, across companies.",
                    "<strong>Basis for analysis</strong> — ratio analysis (Ch 7) and cash-flow analysis (Ch 5) are computed from this pack, especially the notes.",
                    "<strong>Capital-market reputation</strong> — a clean, timely report lowers the cost of capital; a qualification raises it.",
                    "<strong>Governance and public accountability</strong> — independent directors, CSR, BRSR, related-party transparency.",
                ]
            )
            + p(
                "<strong>Users and what they look for.</strong> Shareholders (dividend, honesty, going concern); "
                "prospective investors (growth, margins, risks); lenders (debt, CFO, contingencies); employees "
                "(stability); tax authorities (profit, related party, tax notes); analysts and rating agencies "
                "(notes, segments, quality of earnings); customers and suppliers (going concern); media / public "
                "(CSR, controversies); government / regulators (compliance). "
                "The financial parts (statements, notes, auditor) and the non-financial parts (MD&amp;A, governance, "
                "BRSR) must be read together: a claim in MD&amp;A is tested on the P&amp;L, the note, the cash flow "
                "and the auditor's KAM. <em>Limitation in one line:</em> the report is historical, aggregated, "
                "policy-dependent and can be window-dressed, so it is necessary but not sufficient."
            ),
            "8–10 marks",
        )
    )
    parts.append(
        qna(
            "Write a note on the Directors' Report / Board's Report.",
            p(
                "The Directors' Report is the Board's statutory report to members under Section 134 of the "
                "Companies Act, 2013, attached to the financial statements. It is a stewardship document, "
                "not the same as MD&amp;A."
            )
            + p("Principal contents: state of affairs; dividend; transfer to reserves; material post-balance-sheet changes; Directors' Responsibility Statement; frauds reported by the auditor; conservation of energy, technology absorption and foreign exchange; CSR annexure; secretarial audit report; related-party particulars; number of meetings and director changes; risk, internal financial controls, and other prescribed items including the web-link of the annual return.")
            + p(
                "<strong>Directors' Responsibility Statement (134(5))</strong> — directors state that: "
                "(a) applicable accounting standards were followed, with explanation of material departures; "
                "(b) accounting policies were selected and applied consistently, with reasonable and prudent "
                "judgements, so as to give a true and fair view; (c) proper care was taken of accounting records, "
                "safeguarding of assets, and prevention and detection of fraud; (d) accounts were prepared on a "
                "going concern basis; (e) in a listed company, internal financial controls were laid down, adequate "
                "and operating effectively; (f) proper systems for compliance with applicable laws were devised, "
                "adequate and operating effectively."
            ),
            "5–8 marks",
        )
    )
    parts.append(
        qna(
            "Write a note on the auditor's report. Why should an MBA read it first?",
            p(
                "The Independent Auditor's Report is the statutory auditor's opinion on whether the financial "
                "statements give a true and fair view in accordance with the applicable financial reporting "
                "framework. Management prepares the statements; the auditor examines evidence and reports. "
                "For listed companies the report includes Key Audit Matters and, where applicable, internal "
                "financial controls and a CARO annexure."
            )
            + p(
                "<strong>Types of opinion:</strong> (1) Unmodified (clean) — true and fair. "
                "(2) Qualified — material exception, not pervasive ('except for'). "
                "(3) Adverse — material and pervasive misstatement; statements do not give a true and fair view. "
                "(4) Disclaimer — insufficient evidence, possible effects material and pervasive; no opinion expressed. "
                "Emphasis of Matter and Key Audit Matters highlight issues without, by themselves, being qualifications."
            )
            + p(
                "<strong>Why read it first.</strong> Highlights, MD&amp;A and the Chairman's letter are management's "
                "voice. Ratios computed from qualified or adverse statements are unsafe. An MBA therefore reads "
                "the opinion, the basis paragraph, EOM and KAMs before believing any dashboard number, then "
                "follows each KAM into the matching note."
            ),
            "5–8 marks",
        )
    )
    parts.append(
        qna(
            "What is Management Discussion and Analysis? How is it different from the Directors' Report?",
            p(
                "MD&amp;A is a narrative analysis by management, required for listed companies under SEBI (LODR). "
                "It typically covers industry structure, opportunities and threats, segment-wise or product-wise "
                "performance, outlook, risks, internal control systems, and a discussion of financial performance "
                "versus the previous year. It is the 'story of the numbers'."
            )
            + p(
                "It differs from the Directors' Report: MD&amp;A is analytical / communication (SEBI), not the "
                "Board's Section 134 legal report. MD&amp;A is not a substitute for the financial statements and "
                "is not independently audited as a whole. Every quantitative claim in MD&amp;A should be traced "
                "to the P&amp;L, the notes and the cash flow. The Directors' Report, by contrast, recommends "
                "dividend, includes the Directors' Responsibility Statement, and carries statutory annexures "
                "(CSR, secretarial audit, related party)."
            ),
            "4–5 marks",
        )
    )

    # ------------------------------------------------------------------
    # 6.18 Common mistakes
    # ------------------------------------------------------------------
    parts.append(h2("6.18 Common mistakes (the ones that lose marks, and the ones that lose money)", "s618"))
    parts.append(
        mistakes(
            [
                "<strong>Thinking the annual report is only the financial statements.</strong> The statements are the core. The report also has the story layer, the Board's Report, governance, BRSR, the auditor and the AGM notice. A 'contents' answer that stops at Balance Sheet and P&amp;L is incomplete.",
                "<strong>Ignoring the notes.</strong> Face totals are headlines. Contingent liabilities, related parties, ageing, policy choices and subsequent events live in the notes. Skipping notes = not having read the accounts.",
                "<strong>Ignoring auditor qualifications (and confusing KAM / EOM with a qualification).</strong> Always read the opinion first. A KAM is a spotlight on a clean opinion, not a fail mark. A qualification is an 'except for'. Treat them differently.",
                "<strong>Mixing Directors' Report with MD&amp;A.</strong> Directors' Report = Section 134 legal stewardship (dividend, DRS, annexures). MD&amp;A = SEBI analytical narrative. Examiners set this trap on purpose.",
                "<strong>Mixing annual report with annual return.</strong> Annual report → shareholders (this chapter). Annual return (MGT-7) → Registrar of Companies. Different documents.",
                "<strong>Mixing CSR annexure with BRSR, and secretarial audit with statutory audit.</strong> CSR is Companies Act 2% spend. BRSR is SEBI ESG. Secretarial audit (CS, MR-3) checks law and process. Statutory audit (CA) checks whether the numbers are true and fair.",
                "<strong>Using only standalone or only consolidated without knowing which question you are answering.</strong> Dividend and legal entity covenants → standalone. 'How did the group do for owners of Sagar?' → consolidated. Intra-group sales die on consolidation.",
                "<strong>Believing the Chairman's 20% without checking mix and cash.</strong> Sagar's spices were flat; receivables jumped ₹28 crore; CFO lagged PAT. Story layer is a claim generator, not evidence.",
                "<strong>Starting the 30-minute read with photographs and MD&amp;A.</strong> Identity, then auditor, then dashboard, then faces, then notes, then story. Reverse order is how window dressing works on you.",
                "<strong>Treating an unmodified opinion as an investment recommendation.</strong> True and fair ≠ cheap share, ≠ safe loan, ≠ no fraud anywhere, ≠ next year will be good. It means this year's statements, as a whole, under this framework, are fairly presented.",
                "<strong>Forgetting that the report is historical, delayed, aggregated and policy-dependent.</strong> Limitations belong in a mature 8-mark importance answer.",
                "<strong>Writing one long paragraph for a 5-mark 'contents' question.</strong> Numbered headings with one-line explanations. That is the format of marks in this chapter.",
            ]
        )
    )

    # ------------------------------------------------------------------
    # 6.19 Practice
    # ------------------------------------------------------------------
    parts.append(h2("6.19 Practice questions (with answers to check yourself)", "s619"))

    parts.append(
        practice(
            "1",
            "Easy",
            "One-mark definitions",
            p("Define, in two or three sentences each: (a) annual report (b) MD&amp;A (c) consolidated financial statements."),
            p("<strong>(a)</strong> Yearly statutory-cum-communication document for shareholders containing audited financial statements, Board's Report, auditor's report and other disclosures.")
            + p("<strong>(b)</strong> Management's SEBI-required narrative for listed companies covering industry, performance, risks, outlook and financial review — the story of the numbers, to be tested against the statements.")
            + p("<strong>(c)</strong> Statements of the parent and subsidiaries presented as one economic entity after eliminating intra-group transactions and balances, for the owners of the parent."),
        )
    )
    parts.append(
        practice(
            "2",
            "Easy",
            "Match the user",
            p("Who looks first at (a) contingent liabilities (b) CSR annexure (c) debtor days and CFO (d) Directors' Responsibility Statement (e) BRSR energy numbers?"),
            p("<strong>(a)</strong> Lender / analyst — hidden claims. <strong>(b)</strong> Regulator / NGO / exam on Section 135 — also a shareholder who cares about stewardship. <strong>(c)</strong> Banker and quality-of-earnings analyst. <strong>(d)</strong> Shareholder / court / exam on Section 134 — the Board's signed accountability. <strong>(e)</strong> ESG analyst / overseas buyer / BRSR reader."),
        )
    )
    parts.append(
        practice(
            "3",
            "Moderate",
            "Standalone versus consolidated",
            p(
                "Sagar standalone revenue ₹420 crore. Sagar Spices Pvt Ltd (100% subsidiary) revenue ₹40 crore, of which ₹8 crore was sold to Sagar. Sagar Foods USA Inc revenue ₹22 crore, no intra-group sales. Compute consolidated revenue. In one sentence, say what happened to the ₹8 crore in each set of statements."
            ),
            p("Outside-group revenue of subsidiaries = (40 − 8) + 22 = 32 + 22 = ₹54 crore.")
            + p("Consolidated revenue = 420 + 54 = <strong>₹474 crore</strong>. Check: 420 + 40 + 22 − 8 = 482 − 8 = ₹474 crore.")
            + p("The ₹8 crore is <em>included</em> in standalone revenue of the parent (it sold to another legal entity). It is <em>eliminated</em> on consolidation because the group cannot sell to itself."),
        )
    )
    parts.append(
        practice(
            "4",
            "Moderate",
            "Pick the opinion",
            p("Sagar's auditor was blocked from testing a branch that holds inventory of ₹18 crore and receivables of ₹9 crore. Everything else was tested and looked fair. Total assets are ₹240 crore. Which opinion, and why not the others?"),
            p("Likely <strong>qualified</strong> — material scope limitation, confined to that branch (inventory + receivables), not said to poison the whole statements, so not pervasive → not adverse, and not a full-book evidence failure → not disclaimer. Not unmodified, because ₹18 + ₹9 = ₹27 crore is material on ₹240 crore assets (27 ÷ 240 = 0.1125 = 11.25% of assets). EOM is wrong because EOM is used when the matter is already fairly stated and the opinion stays clean."),
        )
    )
    parts.append(
        practice(
            "5",
            "Exam",
            "Eight-mark mixed question",
            p(
                "'An annual report is more than a set of financial statements.' Explain, with reference to need, users, and how the financial and non-financial parts should be read together. Use a company of your choice."
            ),
            p("Shape of the answer (use Sagar or any company):")
            + ol(
                [
                    "Definition of annual report as statutory + communication pack (not only FS).",
                    "Need: stewardship gap, legal duty, public information spine.",
                    "Importance: transparency, compliance, comparison, basis for ratios and cash-flow analysis, capital raising, governance.",
                    "Users: at least six, with information needs (table in sentences).",
                    "Composition in three layers: story (MD&amp;A, Chairman), stewardship (Board's Report, governance, BRSR), evidence (FS, notes, auditor).",
                    "Worked connection: Sagar's 20% claim → P&amp;L → revenue note → cash flow → debtor days → auditor KAM. This paragraph is the 'more than financial statements' proof.",
                    "Close with two limitations (historical, window dressing) so you do not sound naive.",
                ]
            ),
        )
    )
    parts.append(
        practice(
            "6",
            "Exam",
            "Directors' Responsibility Statement",
            p("List the six clauses of the Directors' Responsibility Statement. Against each, write one sentence of simple meaning and one Sagar-style illustration."),
            p("Use the SPRFGC table in Section 6.10. Sample illustration for (d): Sagar's Board states accounts are prepared as a going concern — they do not expect to liquidate the pickle plants in the next twelve months; if a mega-loan default were likely, this clause would be the first to break and the auditor would add a going-concern paragraph.")
            + p("Sample for (e): as a listed company Sagar's directors confirm internal financial controls over billing, inventory counts and related-party approvals are adequate and operating — the same system the auditor also reports on."),
        )
    )

    parts.append(
        connect(
            "You now have the map of the house. Chapter 4 gave you the furniture of the financial statements. "
            "Chapter 5 gave you the plumbing of cash flow. Chapter 7 will give you the measuring tape of ratios. "
            "Whenever a later chapter says 'take current assets from the Balance Sheet', remember: that number "
            "lives in an annual report, under an auditor's opinion, next to a note, after a story that may be "
            "trying to sell you 20%. Read the house, then measure the room."
        )
    )

    parts.append(chapter_close())
    return "".join(parts)
