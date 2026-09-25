import { Link } from "@tanstack/react-router";
import { BookOpen, Download, Menu, X } from "lucide-react";
import { useState } from "react";
import { CHAPTERS, PDF_HREF } from "@/lib/chapters";

export function Shell({
  children,
  active,
}: {
  children: React.ReactNode;
  active?: string;
}) {
  const [open, setOpen] = useState(false);

  return (
    <div className="min-h-dvh bg-bg text-ink">
      <header className="sticky top-0 z-30 border-b border-line/80 bg-bg/90 backdrop-blur-md">
        <div className="mx-auto flex h-14 max-w-6xl items-center justify-between gap-3 px-4">
          <Link to="/" className="flex min-w-0 items-center gap-2.5">
            <span className="flex size-8 items-center justify-center rounded-lg bg-navy text-[#f7f4ec]">
              <BookOpen className="size-4" strokeWidth={1.75} />
            </span>
            <span className="truncate font-display text-[15px] font-semibold tracking-tight text-navy">
              Accounting for Managers
            </span>
          </Link>
          <nav className="hidden items-center gap-1 md:flex">
            <Link
              to="/"
              className="rounded-lg px-3 py-2 text-sm font-medium text-muted hover:bg-surface hover:text-ink"
            >
              Contents
            </Link>
            <Link
              to="/read/$slug"
              params={{ slug: "formulas" }}
              className="rounded-lg px-3 py-2 text-sm font-medium text-muted hover:bg-surface hover:text-ink"
            >
              Formulas
            </Link>
            <a
              href={PDF_HREF}
              download
              className="inline-flex h-10 items-center gap-1.5 rounded-lg bg-navy px-3.5 pr-3 text-sm font-semibold text-[#f7f4ec] transition-opacity hover:opacity-90"
            >
              <Download className="size-4" strokeWidth={1.75} />
              Download PDF
            </a>
          </nav>
          <button
            type="button"
            className="inline-flex size-11 items-center justify-center rounded-lg text-navy md:hidden"
            aria-label={open ? "Close menu" : "Open menu"}
            onClick={() => setOpen((v) => !v)}
          >
            {open ? <X className="size-5" /> : <Menu className="size-5" />}
          </button>
        </div>
        {open ? (
          <div className="border-t border-line bg-surface px-4 py-3 md:hidden">
            <a
              href={PDF_HREF}
              download
              className="mb-3 flex h-11 items-center justify-center gap-2 rounded-lg bg-navy text-sm font-semibold text-[#f7f4ec]"
            >
              <Download className="size-4" />
              Download complete PDF
            </a>
            <p className="mb-2 text-xs font-semibold uppercase tracking-[0.14em] text-muted">
              Chapters
            </p>
            <div className="grid max-h-[60vh] gap-0.5 overflow-auto">
              {CHAPTERS.map((c) => (
                <Link
                  key={c.slug}
                  to="/read/$slug"
                  params={{ slug: c.slug }}
                  onClick={() => setOpen(false)}
                  className={`rounded-lg px-3 py-2.5 text-sm ${
                    active === c.slug
                      ? "bg-navy text-[#f7f4ec]"
                      : "text-ink hover:bg-surface-2"
                  }`}
                >
                  <span className="mr-2 font-semibold text-accent">
                    {c.num}
                  </span>
                  {c.title}
                </Link>
              ))}
            </div>
          </div>
        ) : null}
      </header>
      {children}
    </div>
  );
}
