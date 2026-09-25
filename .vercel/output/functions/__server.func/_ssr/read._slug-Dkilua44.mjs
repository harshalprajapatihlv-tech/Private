import { i as __toESM } from "../_runtime.mjs";
import { J as require_react, q as notFound, x as require_jsx_runtime, y as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { c as ArrowRight, l as ArrowLeft, o as Download } from "../_libs/lucide-react.mjs";
import { n as Route } from "./router-CB1p7aQ6.mjs";
import { a as neighbors, i as getChapter, n as PDF_HREF, r as Shell, t as CHAPTERS } from "./shell-2JKb5iTH.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/read._slug-Dkilua44.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function ReadChapter() {
	const { slug } = Route.useParams();
	const chapter = getChapter(slug);
	if (!chapter) throw notFound();
	const { prev, next } = neighbors(slug);
	const [html, setHtml] = (0, import_react.useState)(null);
	const [error, setError] = (0, import_react.useState)(false);
	(0, import_react.useEffect)(() => {
		let cancelled = false;
		setHtml(null);
		setError(false);
		fetch(chapter.file).then((r) => {
			if (!r.ok) throw new Error("missing");
			return r.text();
		}).then((t) => {
			if (!cancelled) setHtml(t);
		}).catch(() => {
			if (!cancelled) setError(true);
		});
		return () => {
			cancelled = true;
		};
	}, [chapter.file]);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Shell, {
		active: slug,
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "mx-auto grid max-w-6xl gap-6 px-4 py-6 lg:grid-cols-[220px_minmax(0,1fr)]",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("aside", {
				className: "hidden lg:block",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("nav", {
					className: "sticky top-20 max-h-[calc(100dvh-6rem)] overflow-auto pr-1",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "px-2 text-[11px] font-semibold uppercase tracking-[0.16em] text-muted",
							children: "Contents"
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
							className: "mt-2 space-y-0.5",
							children: CHAPTERS.map((c) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
								to: "/read/$slug",
								params: { slug: c.slug },
								className: `block rounded-lg px-2 py-2 text-[13px] leading-snug ${c.slug === slug ? "bg-navy text-[#f7f4ec]" : "text-ink/90 hover:bg-surface"}`,
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "mr-1.5 font-semibold opacity-70",
									children: c.num
								}), c.title]
							}) }, c.slug))
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("a", {
							href: PDF_HREF,
							download: true,
							className: "mt-4 flex h-10 items-center justify-center gap-2 rounded-lg bg-navy text-xs font-semibold text-[#f7f4ec]",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Download, { className: "size-3.5" }), "Full PDF"]
						})
					]
				})
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("article", {
				className: "min-w-0",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "rounded-[24px] bg-surface px-5 py-8 shadow-[var(--shadow-border)] md:px-10 md:py-10",
					children: error ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "text-muted",
						children: "This chapter could not be loaded. Download the complete PDF — it contains the full notes."
					}) : html === null ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "space-y-3",
						"aria-busy": "true",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "h-7 w-2/3 rounded-md bg-surface-2" }),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "h-4 w-full rounded-md bg-surface-2" }),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "h-4 w-5/6 rounded-md bg-surface-2" }),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "h-24 rounded-xl bg-surface-2" })
						]
					}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "notes-html",
						dangerouslySetInnerHTML: { __html: html }
					})
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("nav", {
					className: "mt-6 mb-10 flex flex-col gap-3 sm:flex-row sm:justify-between",
					children: [prev ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
						to: "/read/$slug",
						params: { slug: prev.slug },
						className: "inline-flex min-h-12 items-center gap-2 rounded-xl bg-surface px-4 text-sm font-medium text-navy shadow-[var(--shadow-border)]",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(ArrowLeft, { className: "size-4" }), prev.title]
					}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {}), next ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
						to: "/read/$slug",
						params: { slug: next.slug },
						className: "inline-flex min-h-12 items-center justify-end gap-2 rounded-xl bg-navy px-4 pr-3.5 text-sm font-semibold text-[#f7f4ec]",
						children: [next.title, /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ArrowRight, { className: "size-4" })]
					}) : null]
				})]
			})]
		})
	});
}
//#endregion
export { ReadChapter as component };
