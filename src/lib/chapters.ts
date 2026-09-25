export type Chapter = {
  slug: string;
  num: string;
  title: string;
  blurb: string;
  file: string;
  kind: "core" | "prep";
};

export const CHAPTERS: Chapter[] = [
  {
    slug: "bootcamp",
    num: "00",
    title: "Accounting Basics Bootcamp",
    blurb: "Assets, liabilities, capital, debit, credit, and the accounting equation — from zero.",
    file: "/notes/chapters/bootcamp.html",
    kind: "core",
  },
  {
    slug: "introduction",
    num: "01",
    title: "Introduction to Accounting",
    blurb: "Concepts, transactions, journal, ledger, and trial balance as one continuous flow.",
    file: "/notes/chapters/ch01.html",
    kind: "core",
  },
  {
    slug: "inventory",
    num: "02",
    title: "Inventory Valuation",
    blurb: "Why stock value changes profit. FIFO and weighted average with full workings.",
    file: "/notes/chapters/ch02.html",
    kind: "core",
  },
  {
    slug: "depreciation",
    num: "03",
    title: "Depreciation",
    blurb: "SLM and WDV, part-year, sale of asset, and how depreciation is not cash.",
    file: "/notes/chapters/ch03.html",
    kind: "core",
  },
  {
    slug: "company-accounts",
    num: "04",
    title: "Company Accounts",
    blurb: "Schedule III P&L, Balance Sheet, notes, and exam adjustments.",
    file: "/notes/chapters/ch04.html",
    kind: "core",
  },
  {
    slug: "cash-flow",
    num: "05",
    title: "Cash Flow Statements",
    blurb: "Profit is not cash. Indirect method, every add/less explained.",
    file: "/notes/chapters/ch05.html",
    kind: "core",
  },
  {
    slug: "annual-reports",
    num: "06",
    title: "Annual Reports & Analysis",
    blurb: "What an annual report contains and how the sections connect.",
    file: "/notes/chapters/ch06.html",
    kind: "core",
  },
  {
    slug: "ratios",
    num: "07",
    title: "Ratio Analysis",
    blurb: "Balance sheet, revenue, and combined ratios — formulas with meaning.",
    file: "/notes/chapters/ch07.html",
    kind: "core",
  },
  {
    slug: "formulas",
    num: "A",
    title: "Master Formula Sheet",
    blurb: "Every important formula in one place.",
    file: "/notes/chapters/formulas.html",
    kind: "prep",
  },
  {
    slug: "rules",
    num: "B",
    title: "Accounting Rules Cheat Sheet",
    blurb: "Debit, credit, and the journal patterns you will actually write.",
    file: "/notes/chapters/rules.html",
    kind: "prep",
  },
  {
    slug: "identify",
    num: "C",
    title: "Question Identification Guide",
    blurb: "If the question says X, use method Y.",
    file: "/notes/chapters/identify.html",
    kind: "prep",
  },
  {
    slug: "formats",
    num: "D",
    title: "Important Formats",
    blurb: "Journal, ledger, trial balance, P&L, BS, cash flow — exam layouts.",
    file: "/notes/chapters/formats.html",
    kind: "prep",
  },
  {
    slug: "theory",
    num: "E",
    title: "Theory Question Bank",
    blurb: "1-mark to long answers, with exam-tone solutions.",
    file: "/notes/chapters/theory.html",
    kind: "prep",
  },
  {
    slug: "practice",
    num: "F",
    title: "Numerical Practice & Solutions",
    blurb: "Easy to exam-level numericals with complete workings.",
    file: "/notes/chapters/practice.html",
    kind: "prep",
  },
  {
    slug: "mistakes",
    num: "G",
    title: "Common Mistakes Checklist",
    blurb: "Chapter-wise traps that cost marks.",
    file: "/notes/chapters/mistakes.html",
    kind: "prep",
  },
  {
    slug: "revision",
    num: "H",
    title: "Last 30 Minutes Revision",
    blurb: "What to glance at before you walk into the hall.",
    file: "/notes/chapters/revision.html",
    kind: "prep",
  },
];

export function getChapter(slug: string) {
  return CHAPTERS.find((c) => c.slug === slug);
}

export function neighbors(slug: string) {
  const i = CHAPTERS.findIndex((c) => c.slug === slug);
  return {
    prev: i > 0 ? CHAPTERS[i - 1] : undefined,
    next: i >= 0 && i < CHAPTERS.length - 1 ? CHAPTERS[i + 1] : undefined,
  };
}

export const PDF_HREF = "/Accounting-for-Managers-Complete-Notes.pdf";
