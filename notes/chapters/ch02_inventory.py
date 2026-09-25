#!/usr/bin/env python3
"""Chapter 02 — Inventory Valuation. Accounting for Managers notes."""

from __future__ import annotations

import sys

sys.path.insert(0, "/workspace/notes")
from html_lib import *


# ---------------------------------------------------------------------------
# Tiny local helpers (keep the chapter body readable)
# ---------------------------------------------------------------------------

def _chk(units: str, rupees: str) -> str:
    return box(
        "key",
        "Unit and rupee check — do this on every numerical",
        f"<p><strong>Units.</strong> {units}</p>"
        f"<p><strong>Rupees.</strong> {rupees}</p>",
    )


def _layer_table(rows: list, caption: str) -> str:
    """Oldest layer first — the FIFO 'pile' of goods."""
    return table(
        ["Layer (oldest first)", "Quantity", "Rate", "Amount", "What happens to this layer"],
        rows,
        caption=caption,
    )


def _work(headers, rows, caption: str = "") -> str:
    return table(headers, rows, caption=caption)


def body() -> str:
    parts: list[str] = []

    parts.append(
        chapter_open(
            "02",
            "Inventory Valuation",
            "By the end of this chapter you will value inventory under FIFO and the weighted-average method (periodic and perpetual), compute closing stock and cost of goods sold from a dated stores ledger, add freight to the correct lot, and explain how the choice of method changes profit and the balance sheet.",
            [
                "Introduction to inventory — raw material, work-in-progress, finished goods, stock-in-trade",
                "Importance of inventory valuation — effect on COGS, profit and financial position",
                "Cost or net realisable value (NRV), whichever is lower (AS-2 / Ind AS-2)",
                "Cost of goods sold formula",
                "FIFO (first-in, first-out) — perpetual layers and closing stock",
                "Weighted average method (WAM) — periodic average and moving (perpetual) average",
                "Numerical problems — closing stock, COGS, freight on a purchase lot",
                "FIFO versus WAM when prices are rising or falling",
            ],
        )
    )

    parts.append(
        lead(
            "Inventory is the goods a business is holding. The rupee value you put on those goods "
            "is not a small bookkeeping choice — it changes this year’s profit, this year’s assets, "
            "and next year’s profit too. Indian MBA exams test two costing methods: "
            "<strong>FIFO</strong> and the <strong>weighted average method (WAM)</strong>. "
            "You will learn both, with every multiplication shown, and a check that units and rupees both tally."
        )
    )

    # ======================================================================
    # 1. INTRODUCTION TO INVENTORY
    # ======================================================================
    parts.append(h2("1. Introduction to inventory", "intro"))

    parts.append(
        definition(
            "Inventory (also called <strong>stock</strong>) is the tangible goods a business holds "
            "for sale in the ordinary course of business, or for use in producing goods that will be sold. "
            "Under AS-2 / Ind AS-2, inventories include goods purchased and held for resale, finished goods, "
            "work-in-progress, and materials and supplies waiting to be consumed in production."
        )
    )
    parts.append(
        simple(
            "Think of a shop’s godown, a factory’s raw-material store, and the half-made goods on the "
            "factory floor. All of that is inventory. For a <strong>trader</strong> (a wholesaler or retailer "
            "who does not manufacture), inventory is mainly the goods bought for resale — "
            "<strong>stock-in-trade</strong>. For a <strong>manufacturer</strong>, inventory has three layers: "
            "raw material, work-in-progress (WIP), and finished goods."
        )
    )
    parts.append(
        why(
            "You cannot compute cost of goods sold, gross profit, or current assets without a figure for stock. "
            "Closing stock is the goods that did <em>not</em> get sold this period — they are still an asset. "
            "Opening stock is last period’s leftover that this period starts with."
        )
    )
    parts.append(
        real_life(
            "A kirana store on 31 March still has rice bags, soap cartons and a crate of cold drinks. "
            "Those items are inventory. A steel plant has iron ore in the yard (raw material), molten steel "
            "in process (WIP), and rolled sheets waiting for dispatch (finished goods). A laptop dealer "
            "has laptops on the shelf (stock-in-trade) — that dealer is a trader, not a manufacturer."
        )
    )
    parts.append(
        logic(
            "Until goods are sold (or issued to production), they are an <strong>asset</strong>. "
            "The moment they are sold, their cost leaves the Balance Sheet and becomes an "
            "<strong>expense</strong> — Cost of Goods Sold (COGS) — in the Trading Account / Statement of Profit and Loss. "
            "Valuation is the rule that decides <em>how many rupees</em> sit in the asset column and "
            "<em>how many rupees</em> sit in the expense column. The two columns always move in opposite directions."
        )
    )

    parts.append(h3("The four names you will see in questions"))
    parts.append(
        table(
            ["Name", "Who holds it", "What it is", "Exam language"],
            [
                [
                    "<strong>Raw material</strong>",
                    "Manufacturer",
                    "Inputs waiting to be used — cloth, steel, sugarcane, chemicals",
                    "RM / stores / materials",
                ],
                [
                    "<strong>Work-in-progress (WIP)</strong>",
                    "Manufacturer",
                    "Goods started but not finished — a car on the assembly line",
                    "WIP / work-in-process / semi-finished",
                ],
                [
                    "<strong>Finished goods</strong>",
                    "Manufacturer",
                    "Completed goods ready for sale — packed shirts, bottled oil",
                    "FG / manufactured stock",
                ],
                [
                    "<strong>Stock-in-trade</strong>",
                    "Trader",
                    "Goods bought ready-made, held only to be resold",
                    "Stock / merchandise / goods / closing stock",
                ],
            ],
            caption="Types of inventory — learn the four names; a trader mainly has the last one",
        )
    )
    parts.append(
        keypoint(
            "In this chapter’s numericals, ‘units in the stores ledger’ are treated as goods whose "
            "outflow is COGS. That is the standard MBA trading-concern question. If the firm is a factory "
            "and the ledger is of raw material, the same FIFO / WAM arithmetic applies — the issue is then "
            "material consumed, not COGS. The method does not change."
        )
    )

    parts.append(h3("Where inventory appears in the financial statements"))
    parts.append(
        format_box(
            "Two places, one figure",
            "<p>The <strong>same closing-stock rupees</strong> appear in two statements:</p>"
            "<ul>"
            "<li><strong>Balance Sheet</strong> — under Current Assets → Inventories. "
            "It is an asset because the goods are still with you on the reporting date.</li>"
            "<li><strong>Trading Account</strong> (traditional MBA format) — closing stock is shown on the "
            "<em>credit</em> side (or deducted from the debit side). Opening stock is on the "
            "<em>debit</em> side. Together with purchases and sales they produce gross profit.</li>"
            "</ul>"
            "<p>In the Companies Act 2013 / Schedule III Statement of Profit and Loss you will instead see "
            "<em>changes in inventories of finished goods, work-in-progress and stock-in-trade</em> "
            "as a line that adjusts purchases to arrive at COGS. The arithmetic is the same formula you learn next.</p>",
        )
    )
    parts.append(
        connect(
            "Chapter 1 (final accounts) already used opening stock, purchases, sales and closing stock "
            "to find gross profit. This chapter answers the question that chapter assumed: "
            "<em>how did we get the rupee figure for closing stock?</em> "
            "Once you can value stock, you can finish a Trading Account with confidence."
        )
    )
    parts.append(
        exam_answer(
            "Inventory means the goods held by a business for sale in the ordinary course of business, "
            "or materials and work-in-progress used in production. A trader’s inventory is mainly "
            "stock-in-trade. A manufacturer’s inventory comprises raw materials, work-in-progress and "
            "finished goods. Inventory is shown as a current asset in the Balance Sheet. Closing stock "
            "reduces cost of goods sold and therefore affects gross profit."
        )
    )

    # ======================================================================
    # 2. WHY VALUATION MATTERS
    # ======================================================================
    parts.append(h2("2. Why inventory valuation matters", "why-val"))

    parts.append(
        definition(
            "Inventory valuation is the process of assigning a rupee amount to the units on hand at the "
            "reporting date (and, under a perpetual system, to each issue as it happens). "
            "The amount is used both as the closing-stock asset and as the figure that is subtracted "
            "to arrive at cost of goods sold."
        )
    )
    parts.append(
        simple(
            "You counted 150 bags in the godown. That is the <em>quantity</em>. Valuation answers: "
            "at how many rupees per bag should those 150 bags enter the books? "
            "Different rules (FIFO, weighted average, or a fall in market price) give different rupees. "
            "The bags do not change. The profit figure does."
        )
    )
    parts.append(
        why(
            "Closing stock is the one figure that sits in <strong>both</strong> the income statement and "
            "the Balance Sheet. Push it up, and profit goes up <em>and</em> assets go up. "
            "Push it down, and both fall. A wrong value therefore misstates performance and financial position "
            "together. That is why the examiner cares, and why AS-2 is conservative."
        )
    )
    parts.append(
        real_life(
            "Two partners value the same 200 unsold mixers. Partner A uses the latest (higher) purchase rate. "
            "Partner B uses an average rate. A reports a higher profit and a stronger current-asset position. "
            "The mixers on the shelf are identical. Only the rule changed. Banks, tax authorities and "
            "the other partner will all look at that profit — so the rule must be consistent and disclosed."
        )
    )
    parts.append(
        logic(
            "Goods available this period are either sold or still in stock. "
            "Cost of goods available = Opening stock + Purchases (and other costs of bringing goods in). "
            "That total cost has to be split: some rupees become COGS (expense), the rest remain as the asset. "
            "Valuation is that split. There is no third place for the rupees to go. "
            "So if you give more rupees to closing stock, you have automatically given fewer rupees to COGS, "
            "and profit is higher."
        )
    )

    parts.append(h3("The seesaw you must memorise"))
    parts.append(
        table(
            ["If closing stock is…", "then COGS…", "then gross profit…", "then current assets…"],
            [
                [
                    f"<strong>Overstated</strong> (too high)",
                    "understated (too low)",
                    "overstated (too high)",
                    "overstated (too high)",
                ],
                [
                    f"<strong>Understated</strong> (too low)",
                    "overstated (too high)",
                    "understated (too low)",
                    "understated (too low)",
                ],
            ],
            caption="Closing stock, COGS, profit and assets always move as a set",
            foot="Shortcut: closing stock and profit move in the SAME direction. Closing stock and COGS move in OPPOSITE directions.",
        )
    )
    parts.append(
        keypoint(
            "Closing stock ↑ → COGS ↓ → profit ↑ → assets ↑. "
            "Closing stock ↓ → COGS ↑ → profit ↓ → assets ↓. "
            "Write this on the top of your exam rough sheet. Half the theory questions are this seesaw in words."
        )
    )

    parts.append(h3("A tiny numbers picture — same shop, two values"))
    parts.append(
        p(
            "Sales for the year are ₹80,000. Opening stock is ₹10,000. Purchases are ₹50,000. "
            "The only disagreement is closing stock."
        )
    )
    parts.append(
        table(
            ["Particulars", "Valuation A (closing ₹18,000)", "Valuation B (closing ₹12,000)", "Difference"],
            [
                ["Sales", rupee(80000), rupee(80000), "—"],
                [
                    "Opening stock",
                    rupee(10000),
                    rupee(10000),
                    "—",
                ],
                ["Add: Purchases", rupee(50000), rupee(50000), "—"],
                ["Less: Closing stock", rupee(18000), rupee(12000), f"{rupee(6000)} lower in B"],
                [
                    "<strong>COGS</strong>",
                    f"<strong>{rupee(42000)}</strong>",
                    f"<strong>{rupee(48000)}</strong>",
                    f"B’s COGS is {rupee(6000)} higher",
                ],
                [
                    "<strong>Gross profit (Sales − COGS)</strong>",
                    f"<strong>{rupee(38000)}</strong>",
                    f"<strong>{rupee(32000)}</strong>",
                    f"B’s profit is {rupee(6000)} lower",
                ],
                [
                    "Closing stock in the Balance Sheet",
                    rupee(18000),
                    rupee(12000),
                    f"B’s assets are {rupee(6000)} lower",
                ],
            ],
            caption="A ₹6,000 change in closing stock changes profit by ₹6,000 and assets by ₹6,000",
        )
    )
    parts.append(
        p(
            "Working for A: COGS = ₹10,000 + ₹50,000 − ₹18,000 = ₹42,000. "
            "Gross profit = ₹80,000 − ₹42,000 = ₹38,000."
        )
    )
    parts.append(
        p(
            "Working for B: COGS = ₹10,000 + ₹50,000 − ₹12,000 = ₹48,000. "
            "Gross profit = ₹80,000 − ₹48,000 = ₹32,000."
        )
    )
    parts.append(
        p(
            "The ₹6,000 extra closing stock in A is ₹6,000 extra profit <em>and</em> ₹6,000 extra current assets. "
            "Nothing else in the shop changed."
        )
    )

    parts.append(h3("It reverses next year — a classic 4-mark point"))
    parts.append(
        logic(
            "This year’s closing stock becomes next year’s opening stock. "
            "If you overstate this year’s closing stock by ₹10,000, this year’s profit is ₹10,000 too high. "
            "Next year that same ₹10,000 sits in opening stock, so next year’s COGS is ₹10,000 too high and "
            "next year’s profit is ₹10,000 too low. Over two years the error cancels. "
            "Each single year is still wrong — and the Balance Sheet on 31 March of year 1 is still wrong. "
            "That is why a consistent method, applied every year, matters."
        )
    )
    parts.append(
        exam_tip(
            "If the question says ‘closing stock of 2025-26 was overvalued by ₹20,000, effect on 2026-27’, "
            "answer: 2025-26 profit overstated ₹20,000; 2026-27 opening stock overstated ₹20,000, "
            "so 2026-27 profit understated ₹20,000. Combined two-year profit is not affected."
        )
    )

    parts.append(h3("Conservatism: do not overvalue stock"))
    parts.append(
        definition(
            "The principle of conservatism (prudence) says: anticipate no profit, but provide for all "
            "probable losses. Applied to inventory, it becomes the AS-2 / Ind AS-2 rule: "
            "value inventory at <strong>cost or net realisable value (NRV), whichever is lower</strong>."
        )
    )
    parts.append(
        simple(
            "If the goods cost you ₹50 and you can still sell them (after selling expenses) for ₹70, "
            "keep them at ₹50 — do not book the ₹20 profit until you actually sell. "
            "If they cost you ₹50 but you can now sell them (after selling expenses) for only ₹40, "
            "write them down to ₹40 now — book the ₹10 loss immediately. "
            "Never value stock at selling price just because selling price is higher."
        )
    )
    parts.append(
        formula(
            "Inventory value = lower of Cost and Net Realisable Value (NRV)",
            "NRV = estimated selling price in the ordinary course of business − estimated costs of completion − estimated costs necessary to make the sale.",
        )
    )

    parts.append(
        example(
            "A",
            "Easy",
            "Lower of cost and NRV — one item",
            "<p>A dealer holds <strong>40 fans</strong>. Cost is ₹2,000 each, so cost of the lot is "
            f"40 × ₹2,000 = {rupee(80000)}. A new model has arrived. The fans can now be sold at ₹1,800 each. "
            "Selling expenses are ₹50 per fan.</p>"
            + ol(
                [
                    "Cost per fan = ₹2,000.",
                    "NRV per fan = selling price ₹1,800 − selling expenses ₹50 = <strong>₹1,750</strong>.",
                    "Lower of cost ₹2,000 and NRV ₹1,750 is <strong>₹1,750</strong>.",
                    f"Value of 40 fans = 40 × ₹1,750 = <strong>{rupee(70000)}</strong>.",
                    f"Write-down (expense this year) = {rupee(80000)} − {rupee(70000)} = <strong>{rupee(10000)}</strong>.",
                ]
            )
            + p(
                "If NRV had been ₹2,200, we would have kept the fans at cost ₹2,000. "
                "Unrealised profit is never booked on stock."
            ),
        )
    )

    parts.append(
        example(
            "B",
            "Easy",
            "Lower of cost and NRV is applied item by item — you cannot offset",
            "<p>AS-2 requires the comparison of cost and NRV for each item (or group of similar items). "
            "A surplus on one item must <em>not</em> cancel a deficit on another.</p>"
            + table(
                ["Item", "Cost (₹)", "NRV (₹)", "Value to use (lower)", "Wrong global netting"],
                [
                    ["Item A (phones)", rupee(10000), rupee(12000), rupee(10000) + " (cost)", ""],
                    ["Item B (cases)", rupee(8000), rupee(6500), rupee(6500) + " (NRV)", ""],
                    [
                        "<strong>Total</strong>",
                        f"<strong>{rupee(18000)}</strong>",
                        f"<strong>{rupee(18500)}</strong>",
                        f"<strong>{rupee(16500)}</strong>",
                        f"Cost {rupee(18000)} looks lower than NRV {rupee(18500)}, so a lazy student writes {rupee(18000)} — that is wrong.",
                    ],
                ],
                caption="Item-wise lower of cost and NRV = ₹16,500, not ₹18,000",
            )
            + p(
                "The correct inventory figure is ₹10,000 + ₹6,500 = <strong>₹16,500</strong>. "
                "The ₹2,000 ‘surplus’ on phones is unrealised and cannot rescue the ₹1,500 fall on cases."
            ),
        )
    )

    parts.append(
        warn(
            "Never value closing stock at selling price, list price, or MRP. Cost (FIFO or WAM) first; "
            "then compare with NRV; take the lower. Selling price is used only inside the NRV calculation, "
            "and even then you deduct the costs of making the sale."
        )
    )

    parts.append(
        box(
            "miss",
            "Exam extra mark — LIFO is not allowed in India",
            "<p>AS-2 and Ind AS-2 <strong>do not permit LIFO</strong> (last-in, first-out) as a cost formula "
            "for inventory. If a question mentions LIFO, write one sentence: "
            "<em>LIFO is not an accepted method of inventory valuation in India under AS-2 / Ind AS-2.</em> "
            "Do not compute a LIFO closing stock unless the paper specifically demands a working for comparison. "
            "This chapter therefore teaches only FIFO and the weighted average method — the two methods the examiner wants you to use.</p>",
        )
    )

    parts.append(
        exam_answer(
            "Inventory valuation matters because closing stock appears both in the Trading Account "
            "(affecting COGS and gross profit) and in the Balance Sheet (as a current asset). "
            "An overstatement of closing stock understates COGS, overstates profit and overstates assets. "
            "The error reverses in the following year because this year’s closing stock is next year’s opening stock. "
            "Following conservatism, AS-2 / Ind AS-2 require inventory to be valued at cost or net realisable value, "
            "whichever is lower, compared item by item."
        )
    )

    # ======================================================================
    # 3. COGS FORMULA
    # ======================================================================
    parts.append(h2("3. Cost of goods sold (COGS) formula", "cogs"))

    parts.append(
        definition(
            "Cost of goods sold is the cost of the inventory that left the business during the period "
            "(sold to customers, or issued from the store). It is the expense matched against sales to "
            "arrive at gross profit."
        )
    )
    parts.append(
        formula(
            "Cost of goods sold = Opening stock + Purchases − Closing stock",
            "Purchases here means net purchases at cost (invoice price − trade discount + freight inward / carriage inward of the goods that came in). Cash discount is not deducted from purchases for this purpose.",
        )
    )
    parts.append(
        formula(
            "Gross profit = Sales − Cost of goods sold",
            "If COGS is higher than sales, the result is a gross loss.",
        )
    )
    parts.append(
        simple(
            "Imagine a tank of goods. You start with some water (opening stock). You pour more in (purchases). "
            "You look at what is still in the tank at the end (closing stock). "
            "Whatever disappeared from the tank was used / sold — that is COGS. "
            "Gross profit is the money customers paid you minus what those sold goods cost you."
        )
    )
    parts.append(
        why(
            "Almost every inventory numerical ends with two figures the examiner wants: "
            "<strong>value of closing stock</strong> and <strong>COGS</strong>. "
            "Once you have closing stock in rupees, COGS is one subtraction away from the cost of goods available. "
            "You do not need a second independent method for COGS if the rupee check already holds — "
            "but in FIFO / WAM you will also build COGS issue by issue, and then confirm with this formula."
        )
    )
    parts.append(
        real_life(
            "A bookshop starts April with books that cost ₹40,000. It buys more books costing ₹1,20,000. "
            "On 30 April unsold books (valued at cost) are ₹35,000. "
            f"COGS = {rupee(40000)} + {rupee(120000)} − {rupee(35000)} = <strong>{rupee(125000)}</strong>. "
            f"If April sales are {rupee(180000)}, gross profit = {rupee(180000)} − {rupee(125000)} = <strong>{rupee(55000)}</strong>."
        )
    )
    parts.append(
        logic(
            "Opening stock + Purchases = cost of goods <em>available</em> for sale. "
            "Available goods go to two destinations only: sold (COGS) or unsold (closing stock). "
            "So: Available = COGS + Closing stock. Rearrange: COGS = Available − Closing stock. "
            "This identity is your rupee check in every FIFO and WAM sum."
        )
    )

    parts.append(
        format_box(
            "Cost of goods available, then the split",
            table(
                ["Step", "What you write", "What it means"],
                [
                    ["1", "Opening stock", "Cost of leftover units from last period"],
                    ["2", "+ Purchases (at cost, including freight inward of those lots)", "Goods that came in this period"],
                    ["3", "= Cost of goods available for sale", "All rupees that must be split"],
                    ["4", "− Closing stock (FIFO or WAM, then lower of cost and NRV)", "Rupees that stay as an asset"],
                    ["5", "= Cost of goods sold", "Rupees that become the expense"],
                    ["6", "Sales − COGS = Gross profit", "Trading result"],
                ],
            ),
        )
    )

    parts.append(
        steps(
            [
                "Pick up opening quantity and opening rate. Opening cost = quantity × rate.",
                "Add every purchase at that purchase’s own cost (invoice + freight inward of that lot).",
                "Add: this is cost of goods available. Also add the quantities: this is units available.",
                "Find closing quantity: units available − units issued / sold. (This must match a physical count if given.)",
                "Value those closing units by the method named in the question (FIFO or WAM). That is closing stock in ₹.",
                "COGS in ₹ = cost of goods available − closing stock. Also add up the issue amounts as a cross-check.",
                "Gross profit = sales − COGS, if sales are given.",
            ]
        )
    )

    parts.append(
        keypoint(
            "Two identities that must both hold, every time: "
            "(1) Opening qty + Purchase qty − Issue qty = Closing qty. "
            "(2) Opening cost + Purchase cost − COGS = Closing stock (₹). "
            "If either fails, an arithmetic slip is hiding in the layers or the average."
        )
    )

    # ======================================================================
    # 4. FIFO
    # ======================================================================
    parts.append(h2("4. FIFO — First-In, First-Out", "fifo"))

    parts.append(
        definition(
            "FIFO assumes that the goods purchased first are issued (sold) first. "
            "Therefore the units remaining in stock are the units purchased most recently, "
            "and closing stock is valued at the latest purchase rates."
        )
    )
    parts.append(
        simple(
            "Picture a narrow godown where bags are pushed in from the back. The oldest bags sit at the front "
            "and are taken out first. What you see at the end of the month are the newest bags. "
            "Accounting FIFO is that picture in rupees — even if the physical bags were actually picked at random. "
            "It is an <strong>assumption for costing</strong>, not a CCTV record of which bag left."
        )
    )
    parts.append(
        why(
            "When prices change during the period, you must decide which rate applies to the units sold and "
            "which rate applies to the units left. FIFO gives a closing-stock figure that is close to current "
            "replacement cost (because leftover units carry the latest rates). That is useful for the Balance Sheet. "
            "It is also the method AS-2 / Ind AS-2 explicitly allow, along with weighted average."
        )
    )
    parts.append(
        real_life(
            "A milk booth receives crates every morning. It sells yesterday’s leftover milk first so it does not spoil. "
            "That is physical FIFO. A clothing store may pick any shirt from the pile, but the accountant still "
            "costs issues as if the oldest purchase left first. Same rule, two reasons: perishable goods actually "
            "move FIFO; other goods use FIFO as a costing convention."
        )
    )
    parts.append(
        logic(
            "You keep inventory as <strong>layers</strong> (lots). Each purchase is a new layer with its own rate. "
            "An issue eats the oldest remaining layer first. If that layer is not enough, it eats the next oldest, "
            "and so on. After the issue, you write the leftover layers. You never ‘remix’ the rates. "
            "A later purchase never changes the rate of an earlier leftover layer."
        )
    )

    parts.append(h3("The layer picture (this is FIFO)"))
    parts.append(
        p(
            "Start of January: 100 units bought earlier at ₹10, then a new purchase of 200 units at ₹12. "
            "The pile looks like this before any issue:"
        )
    )
    parts.append(
        _layer_table(
            [
                ["Layer 1 — oldest (opening)", "100", "₹10", rupee(1000), "These will be issued first"],
                ["Layer 2 — newest (5 Jan purchase)", "200", "₹12", rupee(2400), "These stay until layer 1 is finished"],
            ],
            "FIFO pile before the issue — oldest layer listed first",
        )
    )
    parts.append(
        p(
            "Now 150 units are issued. FIFO takes the entire oldest layer (100) and 50 from the next layer:"
        )
    )
    parts.append(
        _layer_table(
            [
                ["Layer 1 — opening (fully issued)", "100", "₹10", rupee(1000), "Gone — this ₹1,000 is COGS"],
                ["Layer 2 — 5 Jan (partly issued)", "50 issued; 150 left", "₹12", f"Issued {rupee(600)}; left {rupee(1800)}", "Remaining 150 @ ₹12 sit in closing stock"],
            ],
            "FIFO pile after issuing 150 — only the latest layer remains",
        )
    )
    parts.append(
        memory(
            "FIFO: <strong>old goods leave first; new goods remain.</strong> "
            "Closing stock = latest lots. COGS = oldest lots."
        )
    )

    parts.append(
        format_box(
            "FIFO stores ledger (exam presentation)",
            "<p>Indian MBA numericals are usually a <strong>stores ledger</strong> with dates. "
            "Draw three blocks of columns: Receipts, Issues, Balance. Each block has Qty, Rate, Amount. "
            "Under FIFO the Balance block often needs <em>more than one row</em> because two layers can sit side by side.</p>"
            + table(
                [
                    "Date",
                    "Particulars",
                    "Receipts<br/>Qty",
                    "Receipts<br/>Rate",
                    "Receipts<br/>Amt",
                    "Issues<br/>Qty",
                    "Issues<br/>Rate",
                    "Issues<br/>Amt",
                    "Balance<br/>Qty",
                    "Balance<br/>Rate",
                    "Balance<br/>Amt",
                ],
                [
                    ["(row)", "Balance b/d or Purchase or Issue", "units in", "that lot’s rate", "qty × rate", "units out", "oldest remaining rate", "qty × rate", "what is left", "layer’s rate", "qty × rate"],
                ],
                caption="Column plan — copy this into the answer booklet before posting the first line",
            )
            + "<p>After every purchase, add a new layer in the Balance columns. "
            "After every issue, eat layers from the top (oldest) and rewrite the leftover layers. "
            "Never average the leftover rates together — that would be WAM, not FIFO.</p>",
        )
    )

    parts.append(
        steps(
            [
                "Write opening stock as the first layer: quantity, rate, amount = qty × rate.",
                "On a purchase date: add a new layer at that purchase’s own rate. If freight inward is given for that invoice, add the freight to that lot only, then divide by that lot’s quantity to get the lot rate. Do not spread freight over other lots.",
                "On an issue date: start with the oldest remaining layer. Issue as many units as that layer has. If you still need more units, move to the next oldest layer. Cost of the issue = sum of (units taken from each layer × that layer’s rate).",
                "Rewrite leftover layers. Do not combine two leftover layers that have different rates.",
                "At the end: closing quantity = sum of leftover layer quantities. Closing stock (₹) = sum of leftover layer amounts. COGS (₹) = sum of all issue amounts.",
                "Check units: opening + purchases − issues = closing. Check rupees: cost available − COGS = closing stock.",
            ]
        )
    )

    parts.append(h3("Periodic FIFO versus perpetual FIFO"))
    parts.append(
        p(
            "A <strong>perpetual</strong> (running) ledger updates the store after every receipt and every issue. "
            "MBA questions with dates almost always want this. "
            "A <strong>periodic</strong> shortcut ignores the dates of issues and, at period-end, simply takes "
            "the closing quantity from the latest purchases, working backwards."
        )
    )
    parts.append(
        keypoint(
            "For FIFO, perpetual and periodic give the <strong>same closing stock</strong> "
            "(and therefore the same COGS), because both leave the latest lots in hand. "
            "Use perpetual (issue by issue) in the answer. Use the periodic ‘latest lots’ shortcut as a 20-second check."
        )
    )
    parts.append(
        exam_tip(
            "If the question is silent on perpetual vs periodic but gives a list of dated receipts and issues, "
            "prepare a perpetual FIFO stores ledger. Then verify closing stock by the latest-lots shortcut."
        )
    )

    # ----- FIFO Easy -----
    parts.append(
        example(
            "1",
            "Easy",
            "FIFO — one opening layer, one purchase, one issue",
            "<p><strong>Question.</strong> The stores ledger of Mehta Traders shows:</p>"
            + ul(
                [
                    "Opening stock: 100 units @ ₹10",
                    "5 Jan: purchased 200 units @ ₹12",
                    "20 Jan: issued 150 units",
                ]
            )
            + "<p>Value closing stock and COGS under FIFO.</p>"
            + h4("Step 1 — Opening layer")
            + _layer_table(
                [["Opening", "100", "₹10", f"100 × ₹10 = {rupee(1000)}", "Oldest layer"]],
                "After opening",
            )
            + h4("Step 2 — 5 Jan purchase (new layer on top of the pile)")
            + p("200 × ₹12 = " + rupee(2400) + ". Cost now sitting in the store:")
            + _layer_table(
                [
                    ["Opening (oldest)", "100", "₹10", rupee(1000), "Still waiting — will leave first"],
                    ["5 Jan purchase (newest)", "200", "₹12", rupee(2400), "Sits behind the opening lot"],
                ],
                "After 5 Jan — 300 units; cost available = ₹1,000 + ₹2,400 = ₹3,400",
            )
            + h4("Step 3 — 20 Jan issue of 150 units (eat oldest first)")
            + _work(
                ["Taken from", "Quantity", "Rate", "Working", "Amount"],
                [
                    ["Opening layer", "100 (whole layer)", "₹10", "100 × ₹10", rupee(1000)],
                    ["5 Jan layer", "50 (part of 200)", "₹12", "50 × ₹12", rupee(600)],
                    ["<strong>COGS</strong>", "<strong>150</strong>", "", "", f"<strong>{rupee(1600)}</strong>"],
                ],
                caption="Issue working — 100 from the old layer + 50 from the new layer",
            )
            + h4("Step 4 — leftover layers = closing stock")
            + _layer_table(
                [
                    [
                        "5 Jan purchase (only layer left)",
                        "150",
                        "₹12",
                        "150 × ₹12 = " + rupee(1800),
                        "Opening layer is fully gone; 50 of this layer were issued, 150 remain",
                    ]
                ],
                "Closing stock under FIFO",
            )
            + h4("Step 5 — the two checks")
            + _chk(
                "100 + 200 − 150 = <strong>150</strong> units closing. Matches leftover quantity.",
                f"Cost available {rupee(3400)} − COGS {rupee(1600)} = closing {rupee(1800)}. "
                f"Check: {rupee(1000)} + {rupee(2400)} = {rupee(3400)}; {rupee(3400)} − {rupee(1600)} = {rupee(1800)}.",
            )
            + h4("Periodic shortcut (same answer, 20 seconds)")
            + p(
                "Closing quantity 150. Latest purchase is 200 units @ ₹12, which is enough to cover 150. "
                f"So closing stock = 150 × ₹12 = {rupee(1800)}. Same as perpetual. "
                f"COGS = {rupee(3400)} − {rupee(1800)} = {rupee(1600)}."
            )
            + p(
                f"<strong>Answer.</strong> FIFO closing stock = {rupee(1800)} (150 units @ ₹12). "
                f"COGS = {rupee(1600)}."
            ),
        )
    )

    # ----- FIFO Moderate -----
    parts.append(
        example(
            "2",
            "Moderate",
            "FIFO — several layers, two issues (show the pile after every date)",
            "<p><strong>Question.</strong> Prepare a FIFO stores ledger from the following and find closing stock and COGS.</p>"
            + table(
                ["Date", "Transaction", "Quantity", "Rate (₹)"],
                [
                    ["1 Apr", "Opening stock", "200", "20"],
                    ["8 Apr", "Purchase", "300", "22"],
                    ["12 Apr", "Issue", "250", "—"],
                    ["18 Apr", "Purchase", "200", "25"],
                    ["25 Apr", "Issue", "300", "—"],
                    ["28 Apr", "Purchase", "100", "26"],
                ],
                caption="Dated receipts and issues — use perpetual FIFO",
            )
            + h4("1 Apr — opening")
            + _layer_table(
                [["Opening", "200", "₹20", "200 × ₹20 = " + rupee(4000), "Only layer"]],
                "After 1 Apr",
            )
            + h4("8 Apr — purchase 300 @ ₹22")
            + p("300 × ₹22 = " + rupee(6600) + ".")
            + _layer_table(
                [
                    ["Opening (oldest)", "200", "₹20", rupee(4000), "Will be issued first"],
                    ["8 Apr purchase", "300", "₹22", rupee(6600), "Newer layer"],
                ],
                "After 8 Apr — 500 units; cost = ₹4,000 + ₹6,600 = ₹10,600",
            )
            + h4("12 Apr — issue 250 (eat 200 @ ₹20, then 50 @ ₹22)")
            + _work(
                ["Taken from", "Qty", "Rate", "Working", "Amount"],
                [
                    ["Opening", "200", "₹20", "200 × ₹20", rupee(4000)],
                    ["8 Apr layer", "50", "₹22", "50 × ₹22", rupee(1100)],
                    ["<strong>This issue</strong>", "<strong>250</strong>", "", "", f"<strong>{rupee(5100)}</strong>"],
                ],
                caption="12 Apr issue working",
            )
            + _layer_table(
                [
                    [
                        "8 Apr purchase (leftover)",
                        "250",
                        "₹22",
                        "250 × ₹22 = " + rupee(5500),
                        "Opening fully issued; 300 − 50 = 250 of the 8 Apr lot remain",
                    ]
                ],
                "After 12 Apr — one layer left",
            )
            + h4("18 Apr — purchase 200 @ ₹25")
            + p("200 × ₹25 = " + rupee(5000) + ".")
            + _layer_table(
                [
                    ["8 Apr leftover (oldest now)", "250", "₹22", rupee(5500), "Will be issued first next"],
                    ["18 Apr purchase (newest)", "200", "₹25", rupee(5000), "New layer"],
                ],
                "After 18 Apr — 450 units; cost = ₹5,500 + ₹5,000 = ₹10,500",
            )
            + h4("25 Apr — issue 300 (eat 250 @ ₹22, then 50 @ ₹25)")
            + _work(
                ["Taken from", "Qty", "Rate", "Working", "Amount"],
                [
                    ["8 Apr leftover", "250", "₹22", "250 × ₹22", rupee(5500)],
                    ["18 Apr layer", "50", "₹25", "50 × ₹25", rupee(1250)],
                    ["<strong>This issue</strong>", "<strong>300</strong>", "", "", f"<strong>{rupee(6750)}</strong>"],
                ],
                caption="25 Apr issue working",
            )
            + _layer_table(
                [
                    [
                        "18 Apr leftover",
                        "150",
                        "₹25",
                        "150 × ₹25 = " + rupee(3750),
                        "200 − 50 = 150 of the 18 Apr lot remain",
                    ]
                ],
                "After 25 Apr",
            )
            + h4("28 Apr — purchase 100 @ ₹26")
            + p("100 × ₹26 = " + rupee(2600) + ".")
            + _layer_table(
                [
                    ["18 Apr leftover (oldest now)", "150", "₹25", rupee(3750), "Remains in closing stock"],
                    ["28 Apr purchase (newest)", "100", "₹26", rupee(2600), "Remains in closing stock"],
                ],
                "After 28 Apr — this is closing stock",
            )
            + h4("Closing stock and COGS")
            + p(
                f"Closing quantity = 150 + 100 = <strong>250 units</strong>. "
                f"Closing stock = 150 × ₹25 + 100 × ₹26 = {rupee(3750)} + {rupee(2600)} = <strong>{rupee(6350)}</strong>."
            )
            + p(
                f"COGS = 12 Apr issue {rupee(5100)} + 25 Apr issue {rupee(6750)} = <strong>{rupee(11850)}</strong>."
            )
            + p(
                "COGS by lots, fully expanded: "
                "200 × ₹20 = ₹4,000; 50 × ₹22 = ₹1,100; 250 × ₹22 = ₹5,500; 50 × ₹25 = ₹1,250. "
                f"₹4,000 + ₹1,100 + ₹5,500 + ₹1,250 = {rupee(11850)}."
            )
            + _chk(
                "200 + 300 − 250 + 200 − 300 + 100 = <strong>250</strong>. "
                "Running: 200 + 300 = 500; 500 − 250 = 250; 250 + 200 = 450; 450 − 300 = 150; 150 + 100 = 250.",
                f"Available = 200 × ₹20 + 300 × ₹22 + 200 × ₹25 + 100 × ₹26 "
                f"= {rupee(4000)} + {rupee(6600)} + {rupee(5000)} + {rupee(2600)} = {rupee(18200)}. "
                f"{rupee(18200)} − COGS {rupee(11850)} = closing {rupee(6350)}. "
                f"Check: {rupee(11850)} + {rupee(6350)} = {rupee(18200)}.",
            )
            + h4("Periodic latest-lots check")
            + p(
                "Closing 250 units come from the end of the purchase list: "
                "latest lot 100 @ ₹26 = ₹2,600; still need 150, taken from the 200 @ ₹25 lot → 150 × ₹25 = ₹3,750. "
                f"Closing = {rupee(2600)} + {rupee(3750)} = {rupee(6350)}. Matches the ledger."
            )
            + p(
                f"<strong>Answer.</strong> FIFO closing stock = {rupee(6350)} (250 units). "
                f"COGS = {rupee(11850)}."
            ),
        )
    )

    # ----- FIFO Exam -----
    parts.append(
        example(
            "3",
            "Exam-level",
            "FIFO with freight inward added only to that purchase lot",
            "<p><strong>Question.</strong> The following transactions took place in the stores of Rao and Co. "
            "in April. The firm uses FIFO. Freight / carriage inward is part of the cost of the lot it belongs to. "
            "Prepare the FIFO working and compute closing stock and COGS.</p>"
            + table(
                ["Date", "Transaction", "Quantity", "Invoice rate / note"],
                [
                    ["1 Apr", "Opening stock", "200 units", "₹25 per unit"],
                    ["5 Apr", "Purchase", "400 units", "₹30 per unit, plus freight inward ₹800"],
                    ["12 Apr", "Issue", "350 units", "—"],
                    ["20 Apr", "Purchase", "300 units", "₹35 per unit, plus carriage inward ₹600"],
                    ["25 Apr", "Issue", "400 units", "—"],
                    ["28 Apr", "Purchase", "150 units", "₹40 per unit (no freight)"],
                ],
                caption="Freight is attached to its own invoice — do not spread it over all stock",
            )
            + h4("Step 0 — convert each purchase into a cost-per-unit for THAT lot")
            + _work(
                ["Lot", "Invoice", "Add freight", "Total cost of lot", "Quantity", "Rate to use"],
                [
                    [
                        "5 Apr",
                        "400 × ₹30 = " + rupee(12000),
                        rupee(800),
                        f"{rupee(12000)} + {rupee(800)} = {rupee(12800)}",
                        "400",
                        f"{rupee(12800)} ÷ 400 = <strong>₹32</strong>  (₹30 + ₹800/400 = ₹30 + ₹2)",
                    ],
                    [
                        "20 Apr",
                        "300 × ₹35 = " + rupee(10500),
                        rupee(600),
                        f"{rupee(10500)} + {rupee(600)} = {rupee(11100)}",
                        "300",
                        f"{rupee(11100)} ÷ 300 = <strong>₹37</strong>  (₹35 + ₹600/300 = ₹35 + ₹2)",
                    ],
                    [
                        "28 Apr",
                        "150 × ₹40 = " + rupee(6000),
                        "nil",
                        rupee(6000),
                        "150",
                        "<strong>₹40</strong>",
                    ],
                ],
                caption="Each rupee of freight is loaded only on the units that travelled",
            )
            + warn(
                "A common mistake is to add ₹800 + ₹600 = ₹1,400 to the whole of stock, or to opening stock. "
                "Wrong. Freight inward of a consignment is a cost of bringing <em>those</em> units to the godown. "
                "The 5 Apr units cost ₹32; the 20 Apr units cost ₹37. Opening was already in the godown — no extra freight."
            )
            + h4("1 Apr — opening")
            + _layer_table(
                [["Opening", "200", "₹25", "200 × ₹25 = " + rupee(5000), "Oldest"]],
                "After 1 Apr",
            )
            + h4("5 Apr — purchase 400 @ ₹32 (not ₹30)")
            + _layer_table(
                [
                    ["Opening", "200", "₹25", rupee(5000), "Oldest"],
                    ["5 Apr (invoice + freight)", "400", "₹32", "400 × ₹32 = " + rupee(12800), "New layer"],
                ],
                "After 5 Apr — 600 units; cost = ₹5,000 + ₹12,800 = ₹17,800",
            )
            + h4("12 Apr — issue 350")
            + _work(
                ["Taken from", "Qty", "Rate", "Working", "Amount"],
                [
                    ["Opening", "200", "₹25", "200 × ₹25", rupee(5000)],
                    ["5 Apr layer", "150", "₹32", "150 × ₹32", rupee(4800)],
                    ["<strong>This issue</strong>", "<strong>350</strong>", "", "", f"<strong>{rupee(9800)}</strong>"],
                ],
                caption="12 Apr issue — opening finished, then 150 from the ₹32 layer",
            )
            + _layer_table(
                [
                    [
                        "5 Apr leftover",
                        "250",
                        "₹32",
                        "250 × ₹32 = " + rupee(8000),
                        "400 − 150 = 250 remain @ ₹32",
                    ]
                ],
                "After 12 Apr",
            )
            + h4("20 Apr — purchase 300 @ ₹37")
            + _layer_table(
                [
                    ["5 Apr leftover (oldest)", "250", "₹32", rupee(8000), "Will leave first"],
                    ["20 Apr (invoice + carriage)", "300", "₹37", "300 × ₹37 = " + rupee(11100), "New layer"],
                ],
                "After 20 Apr — 550 units; cost = ₹8,000 + ₹11,100 = ₹19,100",
            )
            + h4("25 Apr — issue 400")
            + _work(
                ["Taken from", "Qty", "Rate", "Working", "Amount"],
                [
                    ["5 Apr leftover", "250", "₹32", "250 × ₹32", rupee(8000)],
                    ["20 Apr layer", "150", "₹37", "150 × ₹37", rupee(5550)],
                    ["<strong>This issue</strong>", "<strong>400</strong>", "", "", f"<strong>{rupee(13550)}</strong>"],
                ],
                caption="25 Apr issue — ₹32 layer finished, then 150 from the ₹37 layer",
            )
            + _layer_table(
                [
                    [
                        "20 Apr leftover",
                        "150",
                        "₹37",
                        "150 × ₹37 = " + rupee(5550),
                        "300 − 150 = 150 remain @ ₹37",
                    ]
                ],
                "After 25 Apr",
            )
            + h4("28 Apr — purchase 150 @ ₹40")
            + _layer_table(
                [
                    ["20 Apr leftover", "150", "₹37", rupee(5550), "In closing stock"],
                    ["28 Apr purchase", "150", "₹40", "150 × ₹40 = " + rupee(6000), "In closing stock"],
                ],
                "Closing layers",
            )
            + h4("Closing stock, COGS, checks")
            + p(
                "Closing quantity = 150 + 150 = <strong>300 units</strong>. "
                f"Closing stock = 150 × ₹37 + 150 × ₹40 = {rupee(5550)} + {rupee(6000)} = <strong>{rupee(11550)}</strong>."
            )
            + p(
                f"COGS = 12 Apr {rupee(9800)} + 25 Apr {rupee(13550)} = <strong>{rupee(23350)}</strong>."
            )
            + _chk(
                "200 + 400 − 350 + 300 − 400 + 150 = <strong>300</strong>. "
                "Running: 200 + 400 = 600; 600 − 350 = 250; 250 + 300 = 550; 550 − 400 = 150; 150 + 150 = 300. "
                "Available units = 200 + 400 + 300 + 150 = 1,050; issues 350 + 400 = 750; 1,050 − 750 = 300.",
                "Available cost = 200 × ₹25 + 400 × ₹32 + 300 × ₹37 + 150 × ₹40 "
                f"= {rupee(5000)} + {rupee(12800)} + {rupee(11100)} + {rupee(6000)} = {rupee(34900)}. "
                f"{rupee(34900)} − COGS {rupee(23350)} = closing {rupee(11550)}. "
                f"Check: {rupee(23350)} + {rupee(11550)} = {rupee(34900)}.",
            )
            + h4("Periodic latest-lots check")
            + p(
                "Need 300 closing units from the end: 150 @ ₹40 = ₹6,000, plus 150 @ ₹37 = ₹5,550. "
                f"Closing = {rupee(6000)} + {rupee(5550)} = {rupee(11550)}. Same answer, so the layers were posted correctly."
            )
            + p(
                f"<strong>Answer.</strong> FIFO closing stock = {rupee(11550)} (300 units). "
                f"COGS = {rupee(23350)}."
            ),
        )
    )

    parts.append(
        identify(
            "Use FIFO when the question says any of: <strong>FIFO</strong>, <strong>first-in first-out</strong>, "
            "<strong>first in first out</strong>, <strong>latest lots remain in stock</strong>, "
            "<strong>closing stock is of recent purchases</strong>, or <strong>issues are made from the earliest lots</strong>. "
            "If freight / carriage inward is given against a named purchase, load it on that lot’s rate before you FIFO the issues."
        )
    )
    parts.append(
        mistakes(
            [
                "Mixing leftover layers after an issue (adding two rates together). FIFO leftover layers keep their own rates until they are issued.",
                "Issuing from the newest lot first. That would be LIFO, which you must not use.",
                "Spreading freight over opening stock and all purchases. Freight of a consignment joins that consignment only.",
                "Forgetting opening stock — then both units and rupees fail the check.",
                "Valuing leftover units at selling price or at the issue’s selling rate.",
                "Skipping the unit check. If 200 + 300 − 250 is written as 350, every later layer is fiction.",
                "Using the periodic shortcut as the only working when the question asked for a stores ledger. Show the ledger; use the shortcut as a check.",
            ]
        )
    )
    parts.append(
        exam_answer(
            "FIFO assumes that goods purchased first are issued first, so closing stock consists of the most recent purchases and is valued at the latest rates. "
            "Each purchase is kept as a separate layer. An issue exhausts the oldest remaining layer before touching the next. "
            "Freight inward of a purchase is added to that purchase only. "
            "Closing stock (₹) is the sum of leftover layer amounts; COGS is the sum of issue amounts. "
            "Under FIFO, a perpetual ledger and a periodic ‘latest lots’ valuation give the same closing stock."
        )
    )

    # ======================================================================
    # 5. WAM
    # ======================================================================
    parts.append(h2("5. Weighted average method (WAM)", "wam"))

    parts.append(
        definition(
            "The weighted average method values issues and closing stock at an average cost in which "
            "each lot is weighted by its quantity. "
            "Weighted average cost = total cost of stock on hand ÷ total units on hand. "
            "There are two ways to apply it: <strong>periodic</strong> (one average for the whole period) and "
            "<strong>perpetual / moving average</strong> (a new average after every purchase)."
        )
    )
    parts.append(
        simple(
            "FIFO kept every lot’s rate separate, like boxes on a shelf. "
            "WAM pours all the boxes into one soup. Each ladle (issue) tastes the same as the pot at that moment. "
            "When a new box is poured in (a purchase), you stir again and the taste (average) changes. "
            "You do <em>not</em> stir when you only take a ladle out — the remaining soup still tastes the same."
        )
    )
    parts.append(
        why(
            "When goods are mixed in a bin (oil, grain, chemicals, identical spare parts) you cannot say which "
            "molecule is ‘old’ or ‘new’. An average is the honest costing rule. "
            "AS-2 / Ind AS-2 allow the weighted average cost formula. MBA papers love it because it tests "
            "whether you recalculate at the right moment."
        )
    )
    parts.append(
        real_life(
            "A petrol pump’s underground tank already holds 2,000 litres that cost ₹90 a litre. "
            "A tanker delivers 2,000 litres that cost ₹100 a litre. The liquids mix. "
            "The average is (2,000 × 90 + 2,000 × 100) ÷ 4,000 = ₹95. "
            "Every litre sold after that delivery is costed at ₹95 until the next tanker arrives."
        )
    )
    parts.append(
        logic(
            "Cost has to be assigned to units. FIFO assigns by age of the lot. WAM assigns the same rate to every "
            "unit that is in the mix. After a purchase the mix has changed, so the rate must be recomputed. "
            "After an issue the mix has <em>not</em> changed in rate — only the quantity of the same soup has fallen — "
            "so the rate is left untouched. That last sentence is the whole game."
        )
    )

    parts.append(
        formula(
            "Weighted average rate = Total cost of units in hand ÷ Total units in hand",
            "Perpetual (moving) average: recompute this after every purchase (and after a receipt of returned goods, if ever given). Never recompute it merely because you issued goods. Periodic average: compute it once at the end, using opening + all purchases of the period.",
        )
    )

    parts.append(h3("Two flavours — label which one you are using"))
    parts.append(
        table(
            ["", "Perpetual / moving weighted average", "Periodic weighted average"],
            [
                [
                    "When the average is computed",
                    "After <strong>every purchase</strong>. Issues go out at the average then ruling.",
                    "Once, at period-end, from opening + all purchases.",
                ],
                [
                    "What an issue costs",
                    "Quantity issued × current moving average (the average from the last purchase).",
                    "All issues of the period × the single period average. Dates of issues do not matter.",
                ],
                [
                    "Closing stock",
                    "Closing qty × last moving average.",
                    "Closing qty × the single period average.",
                ],
                [
                    "Do they agree?",
                    "Same closing quantity. <strong>Rupee amounts usually differ</strong> when purchases and issues are interleaved.",
                    "Same closing quantity. Different rupees from perpetual, except in simple one-purchase cases.",
                ],
                [
                    "What MBA papers usually want",
                    "<strong>This one</strong>, whenever dates of receipts and issues are given. Draw a stores ledger.",
                    "When the question says ‘periodic’, ‘weighted average for the period’, or gives no issue dates.",
                ],
            ],
            caption="Always write the words ‘perpetual / moving average’ or ‘periodic average’ above your working",
        )
    )
    parts.append(
        warn(
            "NEVER recalculate the average on the date of an issue. "
            "The issue does not change the rate; it only reduces quantity and amount at the existing rate. "
            "This is the most common WAM mistake in MBA scripts, and it costs full marks on the ledger."
        )
    )

    parts.append(
        format_box(
            "WAM stores ledger (perpetual / moving average)",
            "<p>Same 10-column paper as FIFO, but the Balance rate is <strong>one</strong> figure — the current average. "
            "On a purchase row you add qty and amount, then divide to get a new rate. "
            "On an issue row you copy that rate into the Issue columns.</p>"
            + table(
                ["On this row…", "What you do to Qty", "What you do to Amount", "What happens to Rate"],
                [
                    [
                        "Opening (Balance b/d)",
                        "Write opening qty in Balance",
                        "Write opening cost in Balance",
                        "Opening rate = opening cost ÷ opening qty",
                    ],
                    [
                        "Purchase",
                        "Balance qty = old qty + purchased qty",
                        "Balance amount = old amount + (purchased qty × that lot’s rate, including freight of that lot)",
                        "<strong>New average = new amount ÷ new qty.</strong> Write it in the Balance rate column.",
                    ],
                    [
                        "Issue",
                        "Balance qty = old qty − issued qty",
                        "Issue amount = issued qty × <em>existing</em> average. Balance amount falls by the same figure.",
                        "<strong>Rate does not change.</strong> Copy the previous Balance rate into the Issue rate and the new Balance rate.",
                    ],
                ],
                caption="The rate changes only on a receipt, never on an issue",
            ),
        )
    )

    parts.append(
        steps(
            [
                "Read the question and label the method: ‘Perpetual (moving) weighted average’ or ‘Periodic weighted average’.",
                "Perpetual: open a 10-column stores ledger. Post opening into the Balance columns. Rate = amount ÷ qty.",
                "On each purchase: add the lot’s quantity and the lot’s cost (invoice + freight of that lot) to the Balance. New rate = new total cost ÷ new total qty. Show the division.",
                "On each issue: do not divide. Issue rate = the Balance rate already sitting on the previous line. Issue amount = qty × that rate. Subtract qty and amount from the Balance. Rewrite the same rate.",
                "Closing stock = last Balance amount. COGS = sum of the Issue amount column.",
                "Periodic (if asked): ignore issue dates. Average = (opening cost + all purchase costs) ÷ (opening qty + all purchase qtys). Closing stock = closing qty × that average. COGS = issue qty × that average (or available − closing).",
                "Run the unit check and the rupee check.",
            ]
        )
    )

    # ----- WAM Easy -----
    parts.append(
        example(
            "4",
            "Easy",
            "Perpetual (moving) weighted average — average comes out in whole rupees",
            "<p><strong>Question.</strong> Use the moving weighted average. Show the average after the purchase, then value the issue and the closing stock.</p>"
            + ul(
                [
                    "1 Jan: opening 100 units @ ₹20",
                    "8 Jan: purchased 200 units @ ₹26",
                    "15 Jan: issued 150 units",
                ]
            )
            + h4("1 Jan — opening")
            + p("100 × ₹20 = " + rupee(2000) + ". Balance: 100 units @ ₹20 = " + rupee(2000) + ".")
            + h4("8 Jan — purchase: NOW we recompute the average")
            + _work(
                ["", "Quantity", "Rate", "Amount"],
                [
                    ["Opening", "100", "₹20", rupee(2000)],
                    ["Purchase 8 Jan", "200", "₹26", "200 × ₹26 = " + rupee(5200)],
                    ["<strong>Total in hand</strong>", "<strong>300</strong>", "", f"<strong>{rupee(7200)}</strong>"],
                ],
                caption="Stir the soup on a purchase date",
            )
            + p(
                f"New average = {rupee(7200)} ÷ 300 = <strong>₹24 exactly</strong>. "
                "Balance after 8 Jan: 300 units @ ₹24 = " + rupee(7200) + "."
            )
            + h4("15 Jan — issue: do NOT recompute")
            + p(
                "The average on the shelf is still ₹24. We only ladle out 150 units."
            )
            + _work(
                ["", "Quantity", "Rate", "Working", "Amount"],
                [
                    ["Issue 15 Jan", "150", "₹24", "150 × ₹24", rupee(3600)],
                    ["Balance left", "150", "₹24 (unchanged)", "150 × ₹24", rupee(3600)],
                ],
                caption="Issue at the existing average — the rate does not move",
            )
            + p(
                f"COGS = {rupee(3600)}. Closing stock = {rupee(3600)}."
            )
            + _chk(
                "100 + 200 − 150 = <strong>150</strong> units.",
                f"Available {rupee(7200)} − COGS {rupee(3600)} = closing {rupee(3600)}.",
            )
            + box(
                "miss",
                "What a wrong script does on 15 Jan",
                "<p>A panicked student ‘recalculates’ on 15 Jan, perhaps averaging ₹24 with something else, "
                "or taking the last purchase rate ₹26 for the issue. Both are wrong. "
                "Nothing new came in on 15 Jan, so nothing about the rate can change. "
                "Issue 150 × ₹24 = ₹3,600. Stop.</p>",
            )
            + h4("Same data under periodic WAM")
            + p(
                "Only one purchase, and it happened before the issue, so the periodic average is the same soup: "
                f"({rupee(2000)} + {rupee(5200)}) ÷ (100 + 200) = {rupee(7200)} ÷ 300 = ₹24. "
                f"Closing 150 × ₹24 = {rupee(3600)}. COGS 150 × ₹24 = {rupee(3600)}. "
                "Periodic and perpetual agree here. They will <em>not</em> always agree — see the comparison example after the moderate sum."
            )
            + p(
                f"<strong>Answer (perpetual WAM).</strong> Closing stock = {rupee(3600)} (150 @ ₹24). "
                f"COGS = {rupee(3600)}."
            ),
        )
    )

    # ----- WAM Moderate -----
    parts.append(
        example(
            "5",
            "Moderate",
            "Moving average with two purchases and two issues — rate changes only on purchases",
            "<p><strong>Question.</strong> Prepare a perpetual weighted-average stores ledger.</p>"
            + table(
                ["Date", "Transaction", "Quantity", "Rate (₹)"],
                [
                    ["1 Feb", "Opening stock", "100", "20"],
                    ["5 Feb", "Purchase", "200", "32"],
                    ["12 Feb", "Issue", "150", "—"],
                    ["20 Feb", "Purchase", "150", "36"],
                    ["26 Feb", "Issue", "100", "—"],
                ],
                caption="Two stirs (purchases), two ladles (issues)",
            )
            + h4("1 Feb — opening")
            + p("100 × ₹20 = " + rupee(2000) + ". Balance 100 @ ₹20 = " + rupee(2000) + ".")
            + h4("5 Feb — purchase 200 @ ₹32 (recompute)")
            + p("200 × ₹32 = " + rupee(6400) + ".")
            + p(
                f"Total qty = 100 + 200 = 300. Total cost = {rupee(2000)} + {rupee(6400)} = {rupee(8400)}."
            )
            + p(
                f"Average = {rupee(8400)} ÷ 300 = <strong>₹28 exactly</strong>. "
                f"Balance: 300 @ ₹28 = {rupee(8400)}."
            )
            + h4("12 Feb — issue 150 (do not recompute)")
            + p("Issue rate = ₹28 (the average already in the Balance).")
            + p("Issue amount = 150 × ₹28 = " + rupee(4200) + " → this is part of COGS.")
            + p(
                "Left qty = 300 − 150 = 150. Left amount = "
                f"{rupee(8400)} − {rupee(4200)} = {rupee(4200)}. "
                "Rate still ₹28. Check: 150 × ₹28 = " + rupee(4200) + "."
            )
            + h4("20 Feb — purchase 150 @ ₹36 (recompute)")
            + p("150 × ₹36 = " + rupee(5400) + ".")
            + p(
                f"Total qty = 150 + 150 = 300. Total cost = {rupee(4200)} + {rupee(5400)} = {rupee(9600)}."
            )
            + p(
                f"Average = {rupee(9600)} ÷ 300 = <strong>₹32 exactly</strong>. "
                f"Balance: 300 @ ₹32 = {rupee(9600)}."
            )
            + h4("26 Feb — issue 100 (do not recompute)")
            + p("Issue rate = ₹32.")
            + p("Issue amount = 100 × ₹32 = " + rupee(3200) + ".")
            + p(
                "Left qty = 300 − 100 = 200. Left amount = "
                f"{rupee(9600)} − {rupee(3200)} = {rupee(6400)}. "
                "Check: 200 × ₹32 = " + rupee(6400) + "."
            )
            + h4("Stores ledger (perpetual WAM)")
            + table(
                [
                    "Date",
                    "Particulars",
                    "Rec Qty",
                    "Rec Rate",
                    "Rec Amt",
                    "Iss Qty",
                    "Iss Rate",
                    "Iss Amt",
                    "Bal Qty",
                    "Bal Rate",
                    "Bal Amt",
                ],
                [
                    ["1 Feb", "Balance b/d", "—", "—", "—", "—", "—", "—", "100", "20", rupee(2000)],
                    ["5 Feb", "Purchase", "200", "32", rupee(6400), "—", "—", "—", "300", "28", rupee(8400)],
                    ["12 Feb", "Issue", "—", "—", "—", "150", "28", rupee(4200), "150", "28", rupee(4200)],
                    ["20 Feb", "Purchase", "150", "36", rupee(5400), "—", "—", "—", "300", "32", rupee(9600)],
                    ["26 Feb", "Issue", "—", "—", "—", "100", "32", rupee(3200), "200", "32", rupee(6400)],
                ],
                caption="Notice: Balance rate changes on 5 Feb and 20 Feb only — the purchase dates",
            )
            + p(
                f"Closing stock = {rupee(6400)} (200 units @ ₹32). "
                f"COGS = {rupee(4200)} + {rupee(3200)} = <strong>{rupee(7400)}</strong>."
            )
            + _chk(
                "100 + 200 − 150 + 150 − 100 = <strong>200</strong>. "
                "Running: 100 + 200 = 300; 300 − 150 = 150; 150 + 150 = 300; 300 − 100 = 200.",
                f"Available = {rupee(2000)} + {rupee(6400)} + {rupee(5400)} = {rupee(13800)}. "
                f"{rupee(13800)} − COGS {rupee(7400)} = closing {rupee(6400)}.",
            )
            + p(
                f"<strong>Answer (perpetual WAM).</strong> Closing stock = {rupee(6400)}. COGS = {rupee(7400)}."
            ),
        )
    )

    # periodic vs perpetual difference
    parts.append(
        example(
            "6",
            "Moderate",
            "Same facts, two WAM answers — why periodic ≠ perpetual",
            "<p>When a purchase happens <em>after</em> an issue, the periodic method lets that later (usually dearer) "
            "purchase leak into the cost of an earlier issue. The moving average does not, because the later purchase "
            "had not yet been stirred in. This is why the two WAM answers differ, and why you must label the method.</p>"
            + p("<strong>Facts.</strong>")
            + ul(
                [
                    "Opening 100 units @ ₹20 = ₹2,000",
                    "Purchase 100 units @ ₹30 = ₹3,000  → (perpetual) 200 units, ₹5,000, average ₹25",
                    "Issue 50 units",
                    "Purchase 50 units @ ₹45 = ₹2,250",
                ]
            )
            + h4("Perpetual (moving) average")
            + ol(
                [
                    "After first purchase: (₹2,000 + ₹3,000) ÷ (100 + 100) = ₹5,000 ÷ 200 = <strong>₹25</strong>.",
                    f"Issue 50 × ₹25 = <strong>{rupee(1250)}</strong> (this is the whole of COGS). Left 150 × ₹25 = {rupee(3750)}.",
                    f"Second purchase: {rupee(3750)} + {rupee(2250)} = {rupee(6000)}; qty 150 + 50 = 200. Average = {rupee(6000)} ÷ 200 = <strong>₹30</strong>.",
                    f"Closing stock = 200 × ₹30 = <strong>{rupee(6000)}</strong>. COGS = <strong>{rupee(1250)}</strong>.",
                ]
            )
            + h4("Periodic average (one average for the whole period)")
            + p(
                f"Total cost of goods available = {rupee(2000)} + {rupee(3000)} + {rupee(2250)} = <strong>{rupee(7250)}</strong>."
            )
            + p("Total units available = 100 + 100 + 50 = <strong>250</strong>.")
            + p(f"Period average = {rupee(7250)} ÷ 250 = <strong>₹29</strong>.")
            + p("Closing quantity is still 200 (units do not depend on the method).")
            + p(f"Closing stock = 200 × ₹29 = <strong>{rupee(5800)}</strong>.")
            + p(f"COGS = 50 × ₹29 = <strong>{rupee(1450)}</strong>  (or {rupee(7250)} − {rupee(5800)} = {rupee(1450)}).")
            + table(
                ["", "Perpetual WAM", "Periodic WAM", "Difference"],
                [
                    ["Closing stock", rupee(6000), rupee(5800), f"Perpetual higher by {rupee(200)}"],
                    ["COGS", rupee(1250), rupee(1450), f"Periodic higher by {rupee(200)}"],
                    ["Sum (must equal available)", rupee(7250), rupee(7250), "Both split the same ₹7,250"],
                ],
                caption="Same units, different rupee split — always name the method",
            )
            + p(
                "The ₹200 difference is exactly this: periodic charged the 50 issued units at ₹29 instead of ₹25. "
                "50 × (₹29 − ₹25) = ₹200. Periodic let the later ₹45 purchase pull the issue’s cost up. "
                "Perpetual refused, because on the issue date that purchase had not happened."
            ),
        )
    )

    # ----- WAM Exam -----
    parts.append(
        example(
            "7",
            "Exam-level",
            "Full moving-average stores ledger (seven dated lines, including paise)",
            "<p><strong>Question.</strong> From the following, prepare a stores ledger under the "
            "<strong>perpetual weighted average (moving average)</strong> method. Show the rate after every purchase. "
            "Find closing stock and COGS.</p>"
            + table(
                ["Date", "Transaction", "Quantity", "Rate (₹)"],
                [
                    ["1 Apr", "Opening stock", "250", "40"],
                    ["8 Apr", "Purchase", "150", "48"],
                    ["12 Apr", "Issue", "200", "—"],
                    ["18 Apr", "Purchase", "200", "52"],
                    ["22 Apr", "Issue", "150", "—"],
                    ["28 Apr", "Purchase", "50", "62.50"],
                    ["30 Apr", "Issue", "80", "—"],
                ],
                caption="Six movements plus opening — a full exam ledger",
            )
            + h4("Workings before the ledger (every division shown)")
            + p(
                "<strong>1 Apr.</strong> Opening 250 × ₹40 = "
                + rupee(10000)
                + ". Balance 250 @ ₹40 = "
                + rupee(10000)
                + "."
            )
            + p(
                "<strong>8 Apr purchase.</strong> 150 × ₹48 = "
                + rupee(7200)
                + ". "
                + f"Qty 250 + 150 = 400. Amount {rupee(10000)} + {rupee(7200)} = {rupee(17200)}. "
                + f"Average = {rupee(17200)} ÷ 400 = <strong>₹43</strong>."
            )
            + p(
                "<strong>12 Apr issue.</strong> 200 × ₹43 = "
                + rupee(8600)
                + ". "
                + f"Left qty 400 − 200 = 200. Left amount {rupee(17200)} − {rupee(8600)} = {rupee(8600)}. "
                + "Rate still ₹43. Check: 200 × ₹43 = "
                + rupee(8600)
                + "."
            )
            + p(
                "<strong>18 Apr purchase.</strong> 200 × ₹52 = "
                + rupee(10400)
                + ". "
                + f"Qty 200 + 200 = 400. Amount {rupee(8600)} + {rupee(10400)} = {rupee(19000)}. "
                + f"Average = {rupee(19000)} ÷ 400 = <strong>₹47.50</strong>."
            )
            + p(
                "<strong>22 Apr issue.</strong> 150 × ₹47.50 = "
                + rupee(7125)
                + ". "
                "Working: 150 × ₹47 = ₹7,050; 150 × ₹0.50 = ₹75; total ₹7,125. "
                + f"Left qty 400 − 150 = 250. Left amount {rupee(19000)} − {rupee(7125)} = {rupee(11875)}. "
                + "Check: 250 × ₹47.50 = 250 × ₹47 + 250 × ₹0.50 = ₹11,750 + ₹125 = "
                + rupee(11875)
                + "."
            )
            + p(
                "<strong>28 Apr purchase.</strong> 50 × ₹62.50 = "
                + rupee(3125)
                + ". "
                "Working: 50 × ₹62 = ₹3,100; 50 × ₹0.50 = ₹25; total ₹3,125. "
                + f"Qty 250 + 50 = 300. Amount {rupee(11875)} + {rupee(3125)} = {rupee(15000)}. "
                + f"Average = {rupee(15000)} ÷ 300 = <strong>₹50</strong>."
            )
            + p(
                "<strong>30 Apr issue.</strong> 80 × ₹50 = "
                + rupee(4000)
                + ". "
                + f"Left qty 300 − 80 = 220. Left amount {rupee(15000)} − {rupee(4000)} = {rupee(11000)}. "
                + "Check: 220 × ₹50 = "
                + rupee(11000)
                + "."
            )
            + h4("Stores ledger")
            + table(
                [
                    "Date",
                    "Particulars",
                    "Rec Qty",
                    "Rec Rate (₹)",
                    "Rec Amt (₹)",
                    "Iss Qty",
                    "Iss Rate (₹)",
                    "Iss Amt (₹)",
                    "Bal Qty",
                    "Bal Rate (₹)",
                    "Bal Amt (₹)",
                ],
                [
                    ["1 Apr", "Balance b/d", "—", "—", "—", "—", "—", "—", "250", "40.00", rupee(10000)],
                    ["8 Apr", "Purchase", "150", "48.00", rupee(7200), "—", "—", "—", "400", "43.00", rupee(17200)],
                    ["12 Apr", "Issue", "—", "—", "—", "200", "43.00", rupee(8600), "200", "43.00", rupee(8600)],
                    ["18 Apr", "Purchase", "200", "52.00", rupee(10400), "—", "—", "—", "400", "47.50", rupee(19000)],
                    ["22 Apr", "Issue", "—", "—", "—", "150", "47.50", rupee(7125), "250", "47.50", rupee(11875)],
                    ["28 Apr", "Purchase", "50", "62.50", rupee(3125), "—", "—", "—", "300", "50.00", rupee(15000)],
                    ["30 Apr", "Issue", "—", "—", "—", "80", "50.00", rupee(4000), "220", "50.00", rupee(11000)],
                ],
                caption="Perpetual weighted average stores ledger — seven lines",
                foot="Balance rate moved on 8 Apr, 18 Apr and 28 Apr only. On every issue row the rate is copied, not recalculated.",
            )
            + p(
                f"Closing stock = <strong>{rupee(11000)}</strong> (220 units @ ₹50). "
                f"COGS = {rupee(8600)} + {rupee(7125)} + {rupee(4000)} = <strong>{rupee(19725)}</strong>."
            )
            + _chk(
                "250 + 150 − 200 + 200 − 150 + 50 − 80 = <strong>220</strong>. "
                "Running: 250 + 150 = 400; 400 − 200 = 200; 200 + 200 = 400; 400 − 150 = 250; 250 + 50 = 300; 300 − 80 = 220. "
                "Available units = 250 + 150 + 200 + 50 = 650; issues 200 + 150 + 80 = 430; 650 − 430 = 220.",
                f"Available cost = {rupee(10000)} + {rupee(7200)} + {rupee(10400)} + {rupee(3125)} = {rupee(30725)}. "
                f"{rupee(30725)} − COGS {rupee(19725)} = closing {rupee(11000)}. "
                f"Check: {rupee(19725)} + {rupee(11000)} = {rupee(30725)}.",
            )
            + h4("If the same facts had been asked under periodic WAM (short note, not the main answer)")
            + p(
                f"Period average = {rupee(30725)} ÷ 650 units available. "
                "₹30,725 ÷ 650 = ₹47.269… (not a clean rate — this is why the paper usually wants moving average when dates are given). "
                "Do not mix this figure into the perpetual ledger."
            )
            + p(
                f"<strong>Answer (perpetual WAM).</strong> Closing stock = {rupee(11000)}. COGS = {rupee(19725)}."
            ),
        )
    )

    parts.append(
        identify(
            "Use WAM when the question says any of: <strong>weighted average</strong>, <strong>average cost</strong>, "
            "<strong>WAM</strong>, <strong>weighted average cost</strong>, <strong>moving average</strong>, "
            "<strong>perpetual average</strong>, or <strong>periodic average</strong>. "
            "If it says moving / perpetual / ‘stores ledger with rates after each receipt’, use the moving average. "
            "If it says ‘weighted average for the period’ or gives no issue dates, use periodic. "
            "If it only says ‘weighted average’ but prints a dated list of receipts and issues, "
            "use perpetual and write that assumption in one line at the top of the ledger."
        )
    )
    parts.append(
        mistakes(
            [
                "Recalculating the average on an issue date. The average changes only when goods come in.",
                "Taking the latest purchase rate as the issue rate (that is a FIFO/LIFO confusion, not WAM).",
                "Periodic average used inside a dated stores ledger, or moving average used when the question said periodic.",
                "Adding freight to the average of all stock instead of to the purchase amount of that lot before dividing.",
                "Rounding the average too early and never showing the division. Keep two decimal places consistently, and show ₹47.50 as ₹47.50, not ₹48.",
                "Forgetting that leftover units after an issue keep the same average — students sometimes switch the leftover onto the next purchase rate before that purchase is posted.",
            ]
        )
    )
    parts.append(
        memory(
            "WAM: <strong>mix the soup, then ladle.</strong> "
            "You mix (recompute the average) when a new ingredient is poured in (a purchase). "
            "You ladle (issue) at whatever the pot currently tastes of. You do not remix just because you ladled."
        )
    )
    parts.append(
        exam_answer(
            "Under the weighted average method, the rate is total cost of units in hand divided by total units in hand. "
            "In the perpetual (moving average) system the rate is revised after every purchase; issues are costed at the rate then ruling, and the rate is not revised on issue. "
            "In the periodic system a single average is computed from opening stock plus all purchases of the period; closing stock and COGS both use that one rate. "
            "The two systems generally give different rupee answers when purchases and issues alternate. "
            "AS-2 / Ind AS-2 permit the weighted average cost formula."
        )
    )

    # ======================================================================
    # 6. COMPARISON
    # ======================================================================
    parts.append(h2("6. FIFO versus WAM — what happens when prices move", "compare"))

    parts.append(
        p(
            "Take the easy data already used: opening 100 @ ₹20, purchase 200 @ ₹26, issue 150. "
            "Prices are <strong>rising</strong> (₹20 then ₹26). Cost available = "
            f"100 × ₹20 + 200 × ₹26 = {rupee(2000)} + {rupee(5200)} = {rupee(7200)}. Closing quantity = 150."
        )
    )
    parts.append(
        table(
            ["", "FIFO", "WAM (here perpetual = periodic, one purchase)"],
            [
                [
                    "How the 150 issued units are costed",
                    "Oldest first: 100 × ₹20 + 50 × ₹26 = ₹2,000 + ₹1,300 = <strong>₹3,300</strong>",
                    "Average ₹24: 150 × ₹24 = <strong>₹3,600</strong>",
                ],
                [
                    "How the 150 leftover units are costed",
                    "Latest lot: 150 × ₹26 = <strong>₹3,900</strong>",
                    "Average ₹24: 150 × ₹24 = <strong>₹3,600</strong>",
                ],
                [
                    "Check",
                    f"{rupee(3300)} + {rupee(3900)} = {rupee(7200)}",
                    f"{rupee(3600)} + {rupee(3600)} = {rupee(7200)}",
                ],
            ],
            caption="Same goods, two splits of the same ₹7,200",
        )
    )
    parts.append(
        table(
            ["When purchase prices are…", "FIFO closing stock", "WAM closing stock", "FIFO COGS", "WAM COGS", "FIFO profit versus WAM"],
            [
                [
                    "<strong>Rising</strong> (inflation)",
                    "Higher (latest dear lots remain)",
                    "Lower (average is pulled down by old cheap lots)",
                    "Lower (old cheap lots issued)",
                    "Higher",
                    "FIFO profit is <strong>higher</strong>",
                ],
                [
                    "<strong>Falling</strong>",
                    "Lower (latest cheap lots remain)",
                    "Higher (average still holds some old dear lots)",
                    "Higher",
                    "Lower",
                    "FIFO profit is <strong>lower</strong>",
                ],
                [
                    "Constant",
                    "Same",
                    "Same",
                    "Same",
                    "Same",
                    "No difference",
                ],
            ],
            caption="Memorise the rising-price row — it is the standard 4-to-6 mark comparison",
        )
    )
    parts.append(
        keypoint(
            "In a period of rising prices: FIFO closing stock > WAM closing stock, FIFO COGS < WAM COGS, "
            "FIFO gross profit > WAM gross profit, FIFO current assets > WAM current assets. "
            "Both methods still split the same cost of goods available. They do not create or destroy rupees; they allocate them."
        )
    )
    parts.append(
        two_col(
            "<h4>FIFO, in one breath</h4>"
            "<p>Layers stay separate. Oldest leaves first. Closing stock looks ‘up to date’. "
            "Balance Sheet asset is closer to replacement cost. "
            "In inflation, profit is relatively higher (cheap costs in COGS).</p>",
            "<h4>WAM, in one breath</h4>"
            "<p>Layers are mixed. Every unit in the pot has the same rate. "
            "Profit is smoother because a price jump is spread over sold and unsold units. "
            "Useful when goods are identical and physically mixed.</p>",
        )
    )

    # ======================================================================
    # 7. HOW TO IDENTIFY
    # ======================================================================
    parts.append(h2("7. How to identify the question", "identify"))
    parts.append(
        identify(
            "Read the method word before you draw a single column. "
            "If you see <strong>FIFO / first in first out / latest lots in stock / earliest issues</strong> → FIFO layers. "
            "If you see <strong>weighted average / average cost / WAM / moving average / periodic average</strong> → WAM, "
            "and then decide perpetual vs periodic from the wording and from whether dates of issues are given. "
            "If the question is <strong>silent</strong> on the method, do not guess quietly: write one line, "
            "‘Assumption: inventory is valued at FIFO (or WAM) cost’, pick one, and proceed. "
            "An unnamed method with a dated stores ledger is most often FIFO or moving average — "
            "state which one you are using so the examiner can mark the working."
        )
    )
    parts.append(
        table(
            ["Phrase in the question", "What you do"],
            [
                ["‘FIFO’ / ‘first-in, first-out’ / ‘oldest stock issued first’", "Perpetual FIFO layers. Latest lots = closing stock."],
                ["‘Latest purchases remain in stock’", "FIFO (that sentence is the definition of FIFO closing stock)."],
                ["‘Weighted average’ + dates of receipts and issues", "Perpetual / moving WAM stores ledger. State it."],
                ["‘Moving average’ / ‘perpetual average’", "Recompute after every purchase only."],
                ["‘Periodic weighted average’ / no issue dates", "One average from opening + all purchases."],
                ["Freight inward / carriage inward against a named purchase", "Add it to that lot’s cost; new lot rate = (invoice + freight) ÷ qty of that lot."],
                ["‘Cost or NRV whichever lower’ / damaged / obsolete / prices have fallen", "First find cost by FIFO or WAM, then cap at NRV, item by item."],
                ["‘LIFO’", "One sentence: LIFO is not permitted under AS-2 / Ind AS-2 in India. Do not use it as your method."],
                ["Silent on method", "State the assumption in the first line of the answer."],
            ],
            caption="Question decoder — 30 seconds that save the numerical",
        )
    )

    # ======================================================================
    # 8. COMMON MISTAKES (chapter-level)
    # ======================================================================
    parts.append(h2("8. Common mistakes (whole chapter)", "mistakes"))
    parts.append(
        mistakes(
            [
                "Recalculating the weighted average at the time of issue. Average changes only on a receipt.",
                "Mixing FIFO layers after an issue — leftover lots with different rates must not be blended.",
                "Forgetting opening stock, which breaks both the unit identity and the rupee identity.",
                "Using selling price, MRP or list price to value stock. Cost first; NRV only as a ceiling.",
                "Units that do not reconcile: opening + purchases − issues must equal closing units. If this fails, stop and find the missing posting before you compute rupees.",
                "Loading freight inward onto all stock, or onto issues. It belongs to the purchase lot that travelled.",
                "Treating cash discount as a reduction of inventory cost. Trade discount is deducted; cash discount is not (it is a financial item).",
                "Computing FIFO by issuing from the newest lot. That is LIFO, and LIFO is not allowed.",
                "Leaving the method unnamed when the question was silent. Always write the assumption.",
                "Skipping the rupee check (available − COGS = closing). A one-minute check catches 90% of arithmetic slips.",
            ]
        )
    )

    # ======================================================================
    # 9. MEMORY
    # ======================================================================
    parts.append(h2("9. Memory tricks", "memory"))
    parts.append(
        memory(
            "FIFO: <strong>old goods leave first; new goods remain.</strong> "
            "Closing stock is a photograph of the latest invoices. "
            "WAM: <strong>mix the soup, then ladle.</strong> "
            "Stir on purchase, never on issue. "
            "Seesaw: closing stock and profit sit on the same side of the seesaw; COGS sits on the other side. "
            "Conservatism: cost or NRV, whichever is lower — and compare item by item. "
            "India: FIFO and WAM yes; LIFO no."
        )
    )

    # ======================================================================
    # 10. EXAM THEORY
    # ======================================================================
    parts.append(h2("10. Exam-ready theory answers", "theory"))
    parts.append(
        qna(
            "What is inventory? Where is it shown in the financial statements? (4 marks)",
            "<p>Inventory is the goods held for sale in the ordinary course of business, together with materials "
            "and work-in-progress used in production. A trader holds stock-in-trade. A manufacturer holds raw "
            "material, WIP and finished goods. Closing inventory is a current asset in the Balance Sheet. "
            "It is also used in the Trading Account / Statement of Profit and Loss to arrive at cost of goods sold "
            "and gross profit. Opening inventory is last period’s closing inventory brought forward.</p>",
            "4 marks",
        )
    )
    parts.append(
        qna(
            "Why is the valuation of inventory important? (4–6 marks)",
            "<p>Closing stock is the rare figure that appears in both the income statement and the Balance Sheet. "
            "Cost of goods sold = opening stock + purchases − closing stock, and gross profit = sales − COGS. "
            "If closing stock is overstated, COGS is understated, profit is overstated and current assets are overstated. "
            "The opposite follows from understatement. The error reverses next year because this year’s closing stock "
            "is next year’s opening stock, but each year’s accounts and the year-end financial position are still wrong. "
            "Hence a consistent, conservative method (cost or NRV, whichever is lower, under AS-2 / Ind AS-2) is required.</p>",
            "4–6 marks",
        )
    )
    parts.append(
        qna(
            "State the AS-2 rule for valuation of inventories. Why is LIFO not used in India? (4 marks)",
            "<p>Inventories are valued at the lower of cost and net realisable value. Cost is determined using "
            "FIFO or the weighted average cost formula. NRV is estimated selling price less costs of completion "
            "and costs to sell. The comparison is made item by item (or by group of similar items); a surplus on "
            "one item cannot offset a deficit on another. LIFO is not a permitted cost formula under AS-2 or Ind AS-2, "
            "so Indian companies do not value inventory on a LIFO basis.</p>",
            "4 marks",
        )
    )
    parts.append(
        qna(
            "Distinguish between FIFO and the weighted average method. (6 marks)",
            "<p><strong>FIFO</strong> assumes the earliest lots are issued first, so closing stock is the latest lots "
            "at the latest rates. Lots are kept as separate layers. In a period of rising prices FIFO reports higher "
            "closing stock, lower COGS and higher profit than WAM.</p>"
            "<p><strong>WAM</strong> applies an average rate = total cost of units in hand ÷ units in hand. "
            "Under the moving-average (perpetual) system the average is revised after every purchase and issues go out "
            "at the current average. Under the periodic system one average is computed for the period. "
            "WAM is natural when units are identical and mixed. Both methods are permitted by AS-2; LIFO is not.</p>",
            "6 marks",
        )
    )
    parts.append(
        qna(
            "Write the formulae for cost of goods sold and gross profit. (2 marks)",
            f"<p>COGS = Opening stock + Purchases − Closing stock. "
            "Gross profit = Sales − COGS. "
            "Equivalently, Opening stock + Purchases = COGS + Closing stock (the rupee identity used to check numericals).</p>",
            "2 marks",
        )
    )

    # ======================================================================
    # 11. PRACTICE
    # ======================================================================
    parts.append(h2("11. Practice questions — try them, then open the solution", "practice"))
    parts.append(
        p(
            "Sit with rough paper. Do the unit check and the rupee check before you look. "
            "Easy is FIFO, moderate is moving WAM, exam-level is FIFO with freight loaded on the correct lot."
        )
    )

    parts.append(
        practice(
            "1",
            "Easy",
            "FIFO — one purchase, one issue",
            "<p>Opening stock 80 units @ ₹15. Purchased 120 units @ ₹18. Issued 100 units. "
            "Find FIFO closing stock and COGS. Show layers and both checks.</p>",
            h4("Layers before the issue")
            + _layer_table(
                [
                    ["Opening (oldest)", "80", "₹15", "80 × ₹15 = " + rupee(1200), "Issued first"],
                    ["Purchase (newest)", "120", "₹18", "120 × ₹18 = " + rupee(2160), "Sits behind"],
                ],
                "200 units; cost available = ₹1,200 + ₹2,160 = ₹3,360",
            )
            + h4("Issue of 100 — oldest first")
            + _work(
                ["Taken from", "Qty", "Rate", "Working", "Amount"],
                [
                    ["Opening", "80", "₹15", "80 × ₹15", rupee(1200)],
                    ["Purchase", "20", "₹18", "20 × ₹18", rupee(360)],
                    ["<strong>COGS</strong>", "<strong>100</strong>", "", "", f"<strong>{rupee(1560)}</strong>"],
                ],
            )
            + p(
                "Leftover layer: 120 − 20 = 100 units @ ₹18. "
                f"Closing stock = 100 × ₹18 = <strong>{rupee(1800)}</strong>."
            )
            + _chk(
                "80 + 120 − 100 = <strong>100</strong> units.",
                f"Available {rupee(3360)} − COGS {rupee(1560)} = closing {rupee(1800)}.",
            )
            + p(
                f"<strong>Answer.</strong> Closing stock {rupee(1800)}; COGS {rupee(1560)}."
            ),
        )
    )

    parts.append(
        practice(
            "2",
            "Moderate",
            "Perpetual weighted average — two purchases, two issues",
            "<p>Prepare a moving-average stores ledger and find closing stock and COGS.</p>"
            + table(
                ["Date", "Transaction", "Quantity", "Rate (₹)"],
                [
                    ["1 May", "Opening", "120", "25"],
                    ["8 May", "Purchase", "180", "35"],
                    ["15 May", "Issue", "90", "—"],
                    ["22 May", "Purchase", "90", "41"],
                    ["28 May", "Issue", "110", "—"],
                ],
            )
            + "<p>State the method at the top of the ledger. Recalculate the average only after purchases.</p>",
            h4("Method: perpetual (moving) weighted average")
            + p(
                "<strong>1 May.</strong> 120 × ₹25 = "
                + rupee(3000)
                + ". Balance 120 @ ₹25 = "
                + rupee(3000)
                + "."
            )
            + p(
                "<strong>8 May purchase.</strong> 180 × ₹35 = "
                + rupee(6300)
                + ". "
                + f"Qty 120 + 180 = 300. Amount {rupee(3000)} + {rupee(6300)} = {rupee(9300)}. "
                + f"Average = {rupee(9300)} ÷ 300 = <strong>₹31</strong>."
            )
            + p(
                "<strong>15 May issue.</strong> 90 × ₹31 = "
                + rupee(2790)
                + ". "
                + f"Left 300 − 90 = 210 units. Amount {rupee(9300)} − {rupee(2790)} = {rupee(6510)}. "
                + "Rate still ₹31. Check: 210 × ₹31 = "
                + rupee(6510)
                + "."
            )
            + p(
                "<strong>22 May purchase.</strong> 90 × ₹41 = "
                + rupee(3690)
                + ". "
                + f"Qty 210 + 90 = 300. Amount {rupee(6510)} + {rupee(3690)} = {rupee(10200)}. "
                + f"Average = {rupee(10200)} ÷ 300 = <strong>₹34</strong>."
            )
            + p(
                "<strong>28 May issue.</strong> 110 × ₹34 = "
                + rupee(3740)
                + ". "
                + f"Left 300 − 110 = 190 units. Amount {rupee(10200)} − {rupee(3740)} = {rupee(6460)}. "
                + "Check: 190 × ₹34 = "
                + rupee(6460)
                + "."
            )
            + table(
                [
                    "Date",
                    "Particulars",
                    "Rec Qty",
                    "Rec Rate",
                    "Rec Amt",
                    "Iss Qty",
                    "Iss Rate",
                    "Iss Amt",
                    "Bal Qty",
                    "Bal Rate",
                    "Bal Amt",
                ],
                [
                    ["1 May", "Balance b/d", "—", "—", "—", "—", "—", "—", "120", "25", rupee(3000)],
                    ["8 May", "Purchase", "180", "35", rupee(6300), "—", "—", "—", "300", "31", rupee(9300)],
                    ["15 May", "Issue", "—", "—", "—", "90", "31", rupee(2790), "210", "31", rupee(6510)],
                    ["22 May", "Purchase", "90", "41", rupee(3690), "—", "—", "—", "300", "34", rupee(10200)],
                    ["28 May", "Issue", "—", "—", "—", "110", "34", rupee(3740), "190", "34", rupee(6460)],
                ],
                caption="Moving-average ledger",
            )
            + p(
                f"COGS = {rupee(2790)} + {rupee(3740)} = <strong>{rupee(6530)}</strong>. "
                f"Closing stock = <strong>{rupee(6460)}</strong> (190 @ ₹34)."
            )
            + _chk(
                "120 + 180 − 90 + 90 − 110 = <strong>190</strong>. "
                "Running: 120 + 180 = 300; 300 − 90 = 210; 210 + 90 = 300; 300 − 110 = 190.",
                f"Available {rupee(3000)} + {rupee(6300)} + {rupee(3690)} = {rupee(12990)}. "
                f"{rupee(12990)} − {rupee(6530)} = {rupee(6460)}.",
            )
            + p(
                f"<strong>Answer.</strong> Closing stock {rupee(6460)}; COGS {rupee(6530)}."
            ),
        )
    )

    parts.append(
        practice(
            "3",
            "Exam-level",
            "FIFO with freight on two different lots",
            "<p>The stores of Kapoor Agencies (FIFO) showed the following in June. "
            "Carriage / freight inward is a cost of the lot to which it relates. "
            "Compute FIFO closing stock and COGS. Show the lot rates, every layer after every date, and both checks.</p>"
            + table(
                ["Date", "Transaction", "Quantity", "Other information"],
                [
                    ["1 Jun", "Opening stock", "150 units", "@ ₹40"],
                    ["6 Jun", "Purchase", "250 units", "@ ₹44, plus freight ₹1,000"],
                    ["14 Jun", "Issue", "200 units", "—"],
                    ["21 Jun", "Purchase", "200 units", "@ ₹50, plus carriage ₹800"],
                    ["27 Jun", "Issue", "280 units", "—"],
                    ["30 Jun", "Purchase", "100 units", "@ ₹56, no freight"],
                ],
            ),
            h4("Lot rates (freight loaded on its own invoice)")
            + _work(
                ["Lot", "Invoice", "Freight", "Total", "Qty", "Rate"],
                [
                    [
                        "6 Jun",
                        "250 × ₹44 = " + rupee(11000),
                        rupee(1000),
                        rupee(12000),
                        "250",
                        f"{rupee(12000)} ÷ 250 = <strong>₹48</strong>  (₹44 + ₹1,000/250 = ₹44 + ₹4)",
                    ],
                    [
                        "21 Jun",
                        "200 × ₹50 = " + rupee(10000),
                        rupee(800),
                        rupee(10800),
                        "200",
                        f"{rupee(10800)} ÷ 200 = <strong>₹54</strong>  (₹50 + ₹800/200 = ₹50 + ₹4)",
                    ],
                    ["30 Jun", "100 × ₹56 = " + rupee(5600), "nil", rupee(5600), "100", "<strong>₹56</strong>"],
                ],
            )
            + h4("1 Jun — opening")
            + _layer_table(
                [["Opening", "150", "₹40", "150 × ₹40 = " + rupee(6000), "Oldest"]],
                "After 1 Jun",
            )
            + h4("6 Jun — purchase 250 @ ₹48")
            + _layer_table(
                [
                    ["Opening", "150", "₹40", rupee(6000), "Oldest"],
                    ["6 Jun (incl. freight)", "250", "₹48", "250 × ₹48 = " + rupee(12000), "New"],
                ],
                "400 units; cost = ₹6,000 + ₹12,000 = ₹18,000",
            )
            + h4("14 Jun — issue 200")
            + _work(
                ["Taken from", "Qty", "Rate", "Working", "Amount"],
                [
                    ["Opening", "150", "₹40", "150 × ₹40", rupee(6000)],
                    ["6 Jun", "50", "₹48", "50 × ₹48", rupee(2400)],
                    ["<strong>This issue</strong>", "<strong>200</strong>", "", "", f"<strong>{rupee(8400)}</strong>"],
                ],
            )
            + _layer_table(
                [
                    [
                        "6 Jun leftover",
                        "200",
                        "₹48",
                        "200 × ₹48 = " + rupee(9600),
                        "250 − 50 = 200 remain",
                    ]
                ],
                "After 14 Jun",
            )
            + h4("21 Jun — purchase 200 @ ₹54")
            + _layer_table(
                [
                    ["6 Jun leftover (oldest)", "200", "₹48", rupee(9600), "Will leave first"],
                    ["21 Jun (incl. carriage)", "200", "₹54", "200 × ₹54 = " + rupee(10800), "New"],
                ],
                "400 units; cost = ₹9,600 + ₹10,800 = ₹20,400",
            )
            + h4("27 Jun — issue 280")
            + _work(
                ["Taken from", "Qty", "Rate", "Working", "Amount"],
                [
                    ["6 Jun leftover", "200", "₹48", "200 × ₹48", rupee(9600)],
                    ["21 Jun", "80", "₹54", "80 × ₹54", rupee(4320)],
                    ["<strong>This issue</strong>", "<strong>280</strong>", "", "", f"<strong>{rupee(13920)}</strong>"],
                ],
            )
            + p("80 × ₹54: 80 × ₹50 = ₹4,000; 80 × ₹4 = ₹320; total ₹4,320.")
            + _layer_table(
                [
                    [
                        "21 Jun leftover",
                        "120",
                        "₹54",
                        "120 × ₹54 = " + rupee(6480),
                        "200 − 80 = 120 remain. 120 × ₹54: 120 × ₹50 = ₹6,000; 120 × ₹4 = ₹480; total ₹6,480.",
                    ]
                ],
                "After 27 Jun",
            )
            + h4("30 Jun — purchase 100 @ ₹56")
            + _layer_table(
                [
                    ["21 Jun leftover", "120", "₹54", rupee(6480), "In closing stock"],
                    ["30 Jun", "100", "₹56", "100 × ₹56 = " + rupee(5600), "In closing stock"],
                ],
                "Closing layers",
            )
            + p(
                "Closing quantity = 120 + 100 = <strong>220 units</strong>. "
                f"Closing stock = {rupee(6480)} + {rupee(5600)} = <strong>{rupee(12080)}</strong>."
            )
            + p(
                f"COGS = {rupee(8400)} + {rupee(13920)} = <strong>{rupee(22320)}</strong>."
            )
            + _chk(
                "150 + 250 − 200 + 200 − 280 + 100 = <strong>220</strong>. "
                "Running: 150 + 250 = 400; 400 − 200 = 200; 200 + 200 = 400; 400 − 280 = 120; 120 + 100 = 220. "
                "Available units 150 + 250 + 200 + 100 = 700; issues 200 + 280 = 480; 700 − 480 = 220.",
                f"Available cost = 150 × ₹40 + 250 × ₹48 + 200 × ₹54 + 100 × ₹56 "
                f"= {rupee(6000)} + {rupee(12000)} + {rupee(10800)} + {rupee(5600)} = {rupee(34400)}. "
                f"{rupee(34400)} − COGS {rupee(22320)} = closing {rupee(12080)}. "
                f"Check: {rupee(22320)} + {rupee(12080)} = {rupee(34400)}.",
            )
            + h4("Latest-lots shortcut")
            + p(
                "Closing 220 from the end: 100 @ ₹56 = ₹5,600, plus 120 @ ₹54 = ₹6,480. "
                f"₹5,600 + ₹6,480 = {rupee(12080)}. Matches."
            )
            + p(
                f"<strong>Answer.</strong> FIFO closing stock {rupee(12080)} (220 units). "
                f"COGS {rupee(22320)}."
            ),
        )
    )

    parts.append(
        exam_tip(
            "In the hall: (1) write the method in the heading, (2) convert freight into a lot rate before posting, "
            "(3) after every date rewrite the layers or the average, (4) box closing stock and COGS, "
            "(5) spend one minute on the unit identity and the rupee identity. "
            "Those five habits convert a 12-mark numerical into a full-score numerical."
        )
    )

    parts.append(chapter_close())
    return "".join(parts)
