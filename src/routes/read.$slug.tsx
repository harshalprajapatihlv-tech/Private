import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { ArrowLeft, ArrowRight, Download } from "lucide-react";
import { useEffect, useState } from "react";
import { CHAPTERS, getChapter, neighbors, PDF_HREF } from "@/lib/chapters";
import { Shell } from "@/components/shell";

export const Route = createFileRoute("/read/$slug")({
  component: ReadChapter,
});

function ReadChapter() {
  const { slug } = Route.useParams();
  const chapter = getChapter(slug);
  if (!chapter) throw notFound();
  const { prev, next } = neighbors(slug);
  const [html, setHtml] = useState<string | null>(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setHtml(null);
    setError(false);
    fetch(chapter.file)
      .then((r) => {
        if (!r.ok) throw new Error("missing");
        return r.text();
      })
      .then((t) => {
        if (!cancelled) setHtml(t);
      })
      .catch(() => {
        if (!cancelled) setError(true);
      });
    return () => {
      cancelled = true;
    };
  }, [chapter.file]);

  return (
    <Shell active={slug}>
      <div className="mx-auto grid max-w-6xl gap-6 px-4 py-6 lg:grid-cols-[220px_minmax(0,1fr)]">
        <aside className="hidden lg:block">
          <nav className="sticky top-20 max-h-[calc(100dvh-6rem)] overflow-auto pr-1">
            <p className="px-2 text-[11px] font-semibold uppercase tracking-[0.16em] text-muted">
              Contents
            </p>
            <ul className="mt-2 space-y-0.5">
              {CHAPTERS.map((c) => (
                <li key={c.slug}>
                  <Link
                    to="/read/$slug"
                    params={{ slug: c.slug }}
                    className={`block rounded-lg px-2 py-2 text-[13px] leading-snug ${
                      c.slug === slug
                        ? "bg-navy text-[#f7f4ec]"
                        : "text-ink/90 hover:bg-surface"
                    }`}
                  >
                    <span className="mr-1.5 font-semibold opacity-70">{c.num}</span>
                    {c.title}
                  </Link>
                </li>
              ))}
            </ul>
            <a
              href={PDF_HREF}
              download
              className="mt-4 flex h-10 items-center justify-center gap-2 rounded-lg bg-navy text-xs font-semibold text-[#f7f4ec]"
            >
              <Download className="size-3.5" />
              Full PDF
            </a>
          </nav>
        </aside>

        <article className="min-w-0">
          <div className="rounded-[24px] bg-surface px-5 py-8 shadow-[var(--shadow-border)] md:px-10 md:py-10">
            {error ? (
              <p className="text-muted">
                This chapter could not be loaded. Download the complete PDF —
                it contains the full notes.
              </p>
            ) : html === null ? (
              <div className="space-y-3" aria-busy="true">
                <div className="h-7 w-2/3 rounded-md bg-surface-2" />
                <div className="h-4 w-full rounded-md bg-surface-2" />
                <div className="h-4 w-5/6 rounded-md bg-surface-2" />
                <div className="h-24 rounded-xl bg-surface-2" />
              </div>
            ) : (
              <div
                className="notes-html"
                dangerouslySetInnerHTML={{ __html: html }}
              />
            )}
          </div>

          <nav className="mt-6 mb-10 flex flex-col gap-3 sm:flex-row sm:justify-between">
            {prev ? (
              <Link
                to="/read/$slug"
                params={{ slug: prev.slug }}
                className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-surface px-4 text-sm font-medium text-navy shadow-[var(--shadow-border)]"
              >
                <ArrowLeft className="size-4" />
                {prev.title}
              </Link>
            ) : (
              <span />
            )}
            {next ? (
              <Link
                to="/read/$slug"
                params={{ slug: next.slug }}
                className="inline-flex min-h-12 items-center justify-end gap-2 rounded-xl bg-navy px-4 pr-3.5 text-sm font-semibold text-[#f7f4ec]"
              >
                {next.title}
                <ArrowRight className="size-4" />
              </Link>
            ) : null}
          </nav>
        </article>
      </div>
    </Shell>
  );
}
