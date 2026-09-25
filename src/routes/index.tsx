import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowRight, BookOpen, Download, ListChecks, PenLine } from "lucide-react";
import { CHAPTERS, PDF_HREF } from "@/lib/chapters";
import { Shell } from "@/components/shell";

export const Route = createFileRoute("/")({ component: Home });

function Home() {
  const core = CHAPTERS.filter((c) => c.kind === "core");
  const prep = CHAPTERS.filter((c) => c.kind === "prep");

  return (
    <Shell>
      <main>
        <section className="relative overflow-hidden bg-navy-2 text-[#f4f1ea]">
          <div className="mx-auto grid max-w-6xl gap-10 px-4 py-14 md:grid-cols-[1.2fr_0.8fr] md:py-20">
            <div>
              <p className="font-sans text-[11px] font-semibold uppercase tracking-[0.22em] text-[#c5cdd8]">
                MBA / PGPM · Semester I
              </p>
              <h1 className="mt-4 font-display text-[2.35rem] font-semibold leading-[1.12] tracking-tight md:text-5xl">
                Accounting for Managers
              </h1>
              <p className="mt-3 font-display text-xl text-[#d7ddd6] md:text-2xl">
                Complete beginner-to-exam study notes.
              </p>
              <p className="mt-5 max-w-xl text-[15px] leading-relaxed text-[#c5cdd8]">
                Written for students who have never studied accounting. Every
                concept is taught in plain English, then taken to exam-level
                journals, FIFO, depreciation, Schedule III, cash flow, and
                ratios. The PDF is the full textbook — this companion lets you
                read chapter by chapter.
              </p>
              <div className="mt-8 flex flex-wrap gap-3">
                <Link
                  to="/read/$slug"
                  params={{ slug: "bootcamp" }}
                  className="inline-flex h-12 items-center gap-2 rounded-xl bg-[#f4f1ea] px-5 pr-4 text-sm font-semibold text-navy-2"
                >
                  Start the bootcamp
                  <ArrowRight className="size-4" />
                </Link>
                <a
                  href={PDF_HREF}
                  download
                  className="inline-flex h-12 items-center gap-2 rounded-xl px-5 text-sm font-semibold text-[#f4f1ea] shadow-[0_0_0_1px_rgba(244,241,234,0.22)]"
                >
                  <Download className="size-4" />
                  Download PDF
                </a>
              </div>
            </div>
            <aside className="self-end rounded-2xl bg-[#243044] p-5 shadow-[0_0_0_1px_rgba(244,241,234,0.08)]">
              <p className="text-[11px] font-semibold uppercase tracking-[0.18em] text-[#9aa6b5]">
                Official syllabus inside
              </p>
              <ul className="mt-4 space-y-2.5 text-sm text-[#d7ddd6]">
                {[
                  "Journal, ledger, trial balance",
                  "FIFO and weighted average",
                  "SLM and WDV depreciation",
                  "Schedule III company statements",
                  "Cash flow — indirect method",
                  "Annual reports",
                  "Ratio analysis with interpretation",
                ].map((t) => (
                  <li key={t} className="flex gap-2">
                    <span className="mt-2 size-1.5 shrink-0 rounded-full bg-[#c5cdd8]" />
                    {t}
                  </li>
                ))}
              </ul>
            </aside>
          </div>
        </section>

        <section className="mx-auto max-w-6xl px-4 py-10">
          <div className="grid gap-3 md:grid-cols-3">
            {[
              {
                icon: BookOpen,
                title: "Taught, not summarised",
                body: "Definition, simple words, why it exists, a rupee example, then the exam format.",
              },
              {
                icon: PenLine,
                title: "Numericals first",
                body: "Easy → moderate → exam-level. Every multiplication is shown. Traps are marked.",
              },
              {
                icon: ListChecks,
                title: "Exam kit at the back",
                body: "Formula sheet, identification table, theory bank, practice set, last-30-minutes sheet.",
              },
            ].map((c) => (
              <div
                key={c.title}
                className="rounded-2xl bg-surface p-5 shadow-[var(--shadow-border)]"
              >
                <c.icon className="size-5 text-accent" strokeWidth={1.75} />
                <h2 className="mt-3 font-display text-lg font-semibold text-navy">
                  {c.title}
                </h2>
                <p className="mt-1.5 text-sm leading-relaxed text-muted">{c.body}</p>
              </div>
            ))}
          </div>

          <h2 className="mt-12 font-display text-2xl font-semibold tracking-tight text-navy">
            Core chapters
          </h2>
          <p className="mt-1 text-sm text-muted">
            Read in order. The bootcamp is not optional if you are new.
          </p>
          <ol className="mt-5 grid gap-3 md:grid-cols-2">
            {core.map((c) => (
              <li key={c.slug}>
                <Link
                  to="/read/$slug"
                  params={{ slug: c.slug }}
                  className="group flex h-full gap-4 rounded-2xl bg-surface p-4 shadow-[var(--shadow-border)] transition-shadow hover:shadow-[0_0_0_1px_rgba(36,48,68,0.14),0_10px_24px_-12px_rgba(28,25,23,0.16)]"
                >
                  <span className="font-display text-xl font-semibold text-accent">
                    {c.num}
                  </span>
                  <span className="min-w-0">
                    <span className="block font-semibold text-navy group-hover:underline">
                      {c.title}
                    </span>
                    <span className="mt-1 block text-sm leading-relaxed text-muted">
                      {c.blurb}
                    </span>
                  </span>
                </Link>
              </li>
            ))}
          </ol>

          <h2 className="mt-12 font-display text-2xl font-semibold tracking-tight text-navy">
            Exam kit
          </h2>
          <ol className="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
            {prep.map((c) => (
              <li key={c.slug}>
                <Link
                  to="/read/$slug"
                  params={{ slug: c.slug }}
                  className="flex h-full flex-col rounded-2xl bg-surface p-4 shadow-[var(--shadow-border)]"
                >
                  <span className="text-xs font-semibold uppercase tracking-[0.14em] text-accent">
                    {c.num}
                  </span>
                  <span className="mt-2 font-semibold text-navy">{c.title}</span>
                  <span className="mt-1 text-sm text-muted">{c.blurb}</span>
                </Link>
              </li>
            ))}
          </ol>
        </section>
      </main>
    </Shell>
  );
}
