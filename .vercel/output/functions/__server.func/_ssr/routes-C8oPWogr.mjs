import { x as require_jsx_runtime, y as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { a as ListChecks, c as ArrowRight, o as Download, r as PenLine, s as BookOpen } from "../_libs/lucide-react.mjs";
import { n as PDF_HREF, r as Shell, t as CHAPTERS } from "./shell-2JKb5iTH.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/routes-C8oPWogr.js
var import_jsx_runtime = require_jsx_runtime();
function Home() {
	const core = CHAPTERS.filter((c) => c.kind === "core");
	const prep = CHAPTERS.filter((c) => c.kind === "prep");
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Shell, { children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", {
		className: "relative overflow-hidden bg-navy-2 text-[#f4f1ea]",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "mx-auto grid max-w-6xl gap-10 px-4 py-14 md:grid-cols-[1.2fr_0.8fr] md:py-20",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "font-sans text-[11px] font-semibold uppercase tracking-[0.22em] text-[#c5cdd8]",
					children: "MBA / PGPM · Semester I"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
					className: "mt-4 font-display text-[2.35rem] font-semibold leading-[1.12] tracking-tight md:text-5xl",
					children: "Accounting for Managers"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-3 font-display text-xl text-[#d7ddd6] md:text-2xl",
					children: "Complete beginner-to-exam study notes."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-5 max-w-xl text-[15px] leading-relaxed text-[#c5cdd8]",
					children: "Written for students who have never studied accounting. Every concept is taught in plain English, then taken to exam-level journals, FIFO, depreciation, Schedule III, cash flow, and ratios. The PDF is the full textbook — this companion lets you read chapter by chapter."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-8 flex flex-wrap gap-3",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
						to: "/read/$slug",
						params: { slug: "bootcamp" },
						className: "inline-flex h-12 items-center gap-2 rounded-xl bg-[#f4f1ea] px-5 pr-4 text-sm font-semibold text-navy-2",
						children: ["Start the bootcamp", /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ArrowRight, { className: "size-4" })]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("a", {
						href: PDF_HREF,
						download: true,
						className: "inline-flex h-12 items-center gap-2 rounded-xl px-5 text-sm font-semibold text-[#f4f1ea] shadow-[0_0_0_1px_rgba(244,241,234,0.22)]",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Download, { className: "size-4" }), "Download PDF"]
					})]
				})
			] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("aside", {
				className: "self-end rounded-2xl bg-[#243044] p-5 shadow-[0_0_0_1px_rgba(244,241,234,0.08)]",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "text-[11px] font-semibold uppercase tracking-[0.18em] text-[#9aa6b5]",
					children: "Official syllabus inside"
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
					className: "mt-4 space-y-2.5 text-sm text-[#d7ddd6]",
					children: [
						"Journal, ledger, trial balance",
						"FIFO and weighted average",
						"SLM and WDV depreciation",
						"Schedule III company statements",
						"Cash flow — indirect method",
						"Annual reports",
						"Ratio analysis with interpretation"
					].map((t) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
						className: "flex gap-2",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { className: "mt-2 size-1.5 shrink-0 rounded-full bg-[#c5cdd8]" }), t]
					}, t))
				})]
			})]
		})
	}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
		className: "mx-auto max-w-6xl px-4 py-10",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
				className: "grid gap-3 md:grid-cols-3",
				children: [
					{
						icon: BookOpen,
						title: "Taught, not summarised",
						body: "Definition, simple words, why it exists, a rupee example, then the exam format."
					},
					{
						icon: PenLine,
						title: "Numericals first",
						body: "Easy → moderate → exam-level. Every multiplication is shown. Traps are marked."
					},
					{
						icon: ListChecks,
						title: "Exam kit at the back",
						body: "Formula sheet, identification table, theory bank, practice set, last-30-minutes sheet."
					}
				].map((c) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "rounded-2xl bg-surface p-5 shadow-[var(--shadow-border)]",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)(c.icon, {
							className: "size-5 text-accent",
							strokeWidth: 1.75
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
							className: "mt-3 font-display text-lg font-semibold text-navy",
							children: c.title
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-1.5 text-sm leading-relaxed text-muted",
							children: c.body
						})
					]
				}, c.title))
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
				className: "mt-12 font-display text-2xl font-semibold tracking-tight text-navy",
				children: "Core chapters"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-1 text-sm text-muted",
				children: "Read in order. The bootcamp is not optional if you are new."
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ol", {
				className: "mt-5 grid gap-3 md:grid-cols-2",
				children: core.map((c) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
					to: "/read/$slug",
					params: { slug: c.slug },
					className: "group flex h-full gap-4 rounded-2xl bg-surface p-4 shadow-[var(--shadow-border)] transition-shadow hover:shadow-[0_0_0_1px_rgba(36,48,68,0.14),0_10px_24px_-12px_rgba(28,25,23,0.16)]",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "font-display text-xl font-semibold text-accent",
						children: c.num
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
						className: "min-w-0",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "block font-semibold text-navy group-hover:underline",
							children: c.title
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "mt-1 block text-sm leading-relaxed text-muted",
							children: c.blurb
						})]
					})]
				}) }, c.slug))
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
				className: "mt-12 font-display text-2xl font-semibold tracking-tight text-navy",
				children: "Exam kit"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ol", {
				className: "mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-4",
				children: prep.map((c) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
					to: "/read/$slug",
					params: { slug: c.slug },
					className: "flex h-full flex-col rounded-2xl bg-surface p-4 shadow-[var(--shadow-border)]",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "text-xs font-semibold uppercase tracking-[0.14em] text-accent",
							children: c.num
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "mt-2 font-semibold text-navy",
							children: c.title
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "mt-1 text-sm text-muted",
							children: c.blurb
						})
					]
				}) }, c.slug))
			})
		]
	})] }) });
}
//#endregion
export { Home as component };
