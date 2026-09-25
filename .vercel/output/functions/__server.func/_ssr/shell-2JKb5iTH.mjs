import { i as __toESM } from "../_runtime.mjs";
import { J as require_react, x as require_jsx_runtime, y as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { i as Menu, o as Download, s as BookOpen, t as X } from "../_libs/lucide-react.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/shell-2JKb5iTH.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
var CHAPTERS = [
	{
		slug: "bootcamp",
		num: "00",
		title: "Accounting Basics Bootcamp",
		blurb: "Assets, liabilities, capital, debit, credit, and the accounting equation — from zero.",
		file: "/notes/chapters/bootcamp.html",
		kind: "core"
	},
	{
		slug: "introduction",
		num: "01",
		title: "Introduction to Accounting",
		blurb: "Concepts, transactions, journal, ledger, and trial balance as one continuous flow.",
		file: "/notes/chapters/ch01.html",
		kind: "core"
	},
	{
		slug: "inventory",
		num: "02",
		title: "Inventory Valuation",
		blurb: "Why stock value changes profit. FIFO and weighted average with full workings.",
		file: "/notes/chapters/ch02.html",
		kind: "core"
	},
	{
		slug: "depreciation",
		num: "03",
		title: "Depreciation",
		blurb: "SLM and WDV, part-year, sale of asset, and how depreciation is not cash.",
		file: "/notes/chapters/ch03.html",
		kind: "core"
	},
	{
		slug: "company-accounts",
		num: "04",
		title: "Company Accounts",
		blurb: "Schedule III P&L, Balance Sheet, notes, and exam adjustments.",
		file: "/notes/chapters/ch04.html",
		kind: "core"
	},
	{
		slug: "cash-flow",
		num: "05",
		title: "Cash Flow Statements",
		blurb: "Profit is not cash. Indirect method, every add/less explained.",
		file: "/notes/chapters/ch05.html",
		kind: "core"
	},
	{
		slug: "annual-reports",
		num: "06",
		title: "Annual Reports & Analysis",
		blurb: "What an annual report contains and how the sections connect.",
		file: "/notes/chapters/ch06.html",
		kind: "core"
	},
	{
		slug: "ratios",
		num: "07",
		title: "Ratio Analysis",
		blurb: "Balance sheet, revenue, and combined ratios — formulas with meaning.",
		file: "/notes/chapters/ch07.html",
		kind: "core"
	},
	{
		slug: "formulas",
		num: "A",
		title: "Master Formula Sheet",
		blurb: "Every important formula in one place.",
		file: "/notes/chapters/formulas.html",
		kind: "prep"
	},
	{
		slug: "rules",
		num: "B",
		title: "Accounting Rules Cheat Sheet",
		blurb: "Debit, credit, and the journal patterns you will actually write.",
		file: "/notes/chapters/rules.html",
		kind: "prep"
	},
	{
		slug: "identify",
		num: "C",
		title: "Question Identification Guide",
		blurb: "If the question says X, use method Y.",
		file: "/notes/chapters/identify.html",
		kind: "prep"
	},
	{
		slug: "formats",
		num: "D",
		title: "Important Formats",
		blurb: "Journal, ledger, trial balance, P&L, BS, cash flow — exam layouts.",
		file: "/notes/chapters/formats.html",
		kind: "prep"
	},
	{
		slug: "theory",
		num: "E",
		title: "Theory Question Bank",
		blurb: "1-mark to long answers, with exam-tone solutions.",
		file: "/notes/chapters/theory.html",
		kind: "prep"
	},
	{
		slug: "practice",
		num: "F",
		title: "Numerical Practice & Solutions",
		blurb: "Easy to exam-level numericals with complete workings.",
		file: "/notes/chapters/practice.html",
		kind: "prep"
	},
	{
		slug: "mistakes",
		num: "G",
		title: "Common Mistakes Checklist",
		blurb: "Chapter-wise traps that cost marks.",
		file: "/notes/chapters/mistakes.html",
		kind: "prep"
	},
	{
		slug: "revision",
		num: "H",
		title: "Last 30 Minutes Revision",
		blurb: "What to glance at before you walk into the hall.",
		file: "/notes/chapters/revision.html",
		kind: "prep"
	}
];
function getChapter(slug) {
	return CHAPTERS.find((c) => c.slug === slug);
}
function neighbors(slug) {
	const i = CHAPTERS.findIndex((c) => c.slug === slug);
	return {
		prev: i > 0 ? CHAPTERS[i - 1] : void 0,
		next: i >= 0 && i < CHAPTERS.length - 1 ? CHAPTERS[i + 1] : void 0
	};
}
var PDF_HREF = "/Accounting-for-Managers-Complete-Notes.pdf";
function Shell({ children, active }) {
	const [open, setOpen] = (0, import_react.useState)(false);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-ink",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("header", {
			className: "sticky top-0 z-30 border-b border-line/80 bg-bg/90 backdrop-blur-md",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mx-auto flex h-14 max-w-6xl items-center justify-between gap-3 px-4",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
						to: "/",
						className: "flex min-w-0 items-center gap-2.5",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "flex size-8 items-center justify-center rounded-lg bg-navy text-[#f7f4ec]",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(BookOpen, {
								className: "size-4",
								strokeWidth: 1.75
							})
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "truncate font-display text-[15px] font-semibold tracking-tight text-navy",
							children: "Accounting for Managers"
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("nav", {
						className: "hidden items-center gap-1 md:flex",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
								to: "/",
								className: "rounded-lg px-3 py-2 text-sm font-medium text-muted hover:bg-surface hover:text-ink",
								children: "Contents"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
								to: "/read/$slug",
								params: { slug: "formulas" },
								className: "rounded-lg px-3 py-2 text-sm font-medium text-muted hover:bg-surface hover:text-ink",
								children: "Formulas"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("a", {
								href: PDF_HREF,
								download: true,
								className: "inline-flex h-10 items-center gap-1.5 rounded-lg bg-navy px-3.5 pr-3 text-sm font-semibold text-[#f7f4ec] transition-opacity hover:opacity-90",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Download, {
									className: "size-4",
									strokeWidth: 1.75
								}), "Download PDF"]
							})
						]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						className: "inline-flex size-11 items-center justify-center rounded-lg text-navy md:hidden",
						"aria-label": open ? "Close menu" : "Open menu",
						onClick: () => setOpen((v) => !v),
						children: open ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(X, { className: "size-5" }) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Menu, { className: "size-5" })
					})
				]
			}), open ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "border-t border-line bg-surface px-4 py-3 md:hidden",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("a", {
						href: PDF_HREF,
						download: true,
						className: "mb-3 flex h-11 items-center justify-center gap-2 rounded-lg bg-navy text-sm font-semibold text-[#f7f4ec]",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Download, { className: "size-4" }), "Download complete PDF"]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mb-2 text-xs font-semibold uppercase tracking-[0.14em] text-muted",
						children: "Chapters"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "grid max-h-[60vh] gap-0.5 overflow-auto",
						children: CHAPTERS.map((c) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
							to: "/read/$slug",
							params: { slug: c.slug },
							onClick: () => setOpen(false),
							className: `rounded-lg px-3 py-2.5 text-sm ${active === c.slug ? "bg-navy text-[#f7f4ec]" : "text-ink hover:bg-surface-2"}`,
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "mr-2 font-semibold text-accent",
								children: c.num
							}), c.title]
						}, c.slug))
					})
				]
			}) : null]
		}), children]
	});
}
//#endregion
export { neighbors as a, getChapter as i, PDF_HREF as n, Shell as r, CHAPTERS as t };
