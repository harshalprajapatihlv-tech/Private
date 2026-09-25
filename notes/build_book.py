#!/usr/bin/env python3
"""Assemble chapter modules into book.html and per-chapter fragments."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path("/workspace")
NOTES = ROOT / "notes"
CH_DIR = NOTES / "chapters"
OUT = ROOT / "public" / "notes"
FRAG = OUT / "chapters"
PDF_HTML = OUT / "book.html"

sys.path.insert(0, str(NOTES))

CHAPTERS = [
    ("ch00_bootcamp.py", "bootcamp.html", "00", "Accounting Basics Bootcamp"),
    ("ch01_intro.py", "ch01.html", "01", "Introduction to Accounting"),
    ("ch02_inventory.py", "ch02.html", "02", "Inventory Valuation"),
    ("ch03_depreciation.py", "ch03.html", "03", "Depreciation"),
    ("ch04_company.py", "ch04.html", "04", "Company Accounts"),
    ("ch05_cashflow.py", "ch05.html", "05", "Cash Flow Statements"),
    ("ch06_annual.py", "ch06.html", "06", "Understanding Annual Reports & Analysis"),
    ("ch07_ratios.py", "ch07.html", "07", "Ratio Analysis"),
    ("app_formulas.py", "formulas.html", "A", "Master Formula Sheet"),
    ("app_rules.py", "rules.html", "B", "Accounting Rules Cheat Sheet"),
    ("app_identify.py", "identify.html", "C", "Numerical Question Identification Guide"),
    ("app_formats.py", "formats.html", "D", "Most Important Formats"),
    ("app_theory.py", "theory.html", "E", "Theory Question Bank"),
    ("app_practice.py", "practice.html", "F", "Numerical Practice Set"),
    ("app_mistakes.py", "mistakes.html", "G", "Common Mistakes Checklist"),
    ("app_revision.py", "revision.html", "H", "Last 30 Minutes + Quick Revision"),
]


def load_body(path: Path) -> str:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "body"):
        raise RuntimeError(f"{path} has no body()")
    html = mod.body()
    if not isinstance(html, str) or len(html) < 200:
        raise RuntimeError(f"{path} body() too short ({0 if not html else len(html)} chars)")
    return html


COVER = """
<section class="cover">
  <div>
    <p class="eyebrow">MBA / PGPM · Semester I</p>
    <div class="rule"></div>
    <h1>Accounting<br/>for Managers</h1>
    <p class="subtitle">Complete Beginner-to-Exam Study Notes</p>
    <p class="meta">Official syllabus covered in full · Journal to ratio analysis ·
    Taught from first principles with rupee workings, exam formats, and a last-30-minutes revision kit.</p>
  </div>
  <p class="cover-foot">Standalone textbook + examination workbook</p>
</section>
"""


def toc_html(found: list[tuple[str, str, str]]) -> str:
    items = []
    for num, title, _html in found:
        items.append(f"<li><span>{num} &nbsp; {title}</span></li>")
    return f"""
<section class="toc">
  <p class="toc-kicker">Contents</p>
  <h1>How to use these notes</h1>
  <p>Start with the Bootcamp even if the exam syllabus begins at Chapter 1.
  Accounting is a language. The bootcamp teaches the alphabet; the chapters teach the sentences.
  Read in order. When you meet a numerical, copy the format onto paper and solve it yourself
  before you look at the solution. The last section is a revision kit — do not skip it the night before the paper.</p>
  <ol class="toc-list">
    {''.join(items)}
  </ol>
</section>
"""


def wrap_book(inner: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Accounting for Managers — Complete Beginner-to-Exam Study Notes</title>
  <link rel="stylesheet" href="book.css" />
</head>
<body>
<article class="book">
{inner}
</article>
</body>
</html>
"""


def main() -> None:
    FRAG.mkdir(parents=True, exist_ok=True)
    found = []
    missing = []
    for py_name, frag_name, num, title in CHAPTERS:
        path = CH_DIR / py_name
        if not path.exists():
            missing.append(py_name)
            continue
        html = load_body(path)
        (FRAG / frag_name).write_text(html, encoding="utf-8")
        found.append((num, title, html))
        print(f"OK  {py_name:24} {len(html):7d} chars → {frag_name}")
    if missing:
        print("MISSING:", ", ".join(missing))
        if not found:
            raise SystemExit("No chapters built")
    inner = COVER + toc_html(found) + "\n".join(h for _, _, h in found)
    PDF_HTML.write_text(wrap_book(inner), encoding="utf-8")
    print(f"Wrote {PDF_HTML} ({PDF_HTML.stat().st_size} bytes) from {len(found)} sections")


if __name__ == "__main__":
    main()
