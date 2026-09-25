#!/usr/bin/env python3
"""Shared HTML helpers for Accounting for Managers notes."""

from __future__ import annotations

from html import escape as _esc
from typing import Iterable, Sequence


def e(text) -> str:
    if text is None:
        return ""
    return _esc(str(text), quote=True)


def h1(text: str, anchor: str = "") -> str:
    aid = f' id="{e(anchor)}"' if anchor else ""
    return f"<h1{aid}>{e(text)}</h1>\n"


def h2(text: str, anchor: str = "") -> str:
    aid = f' id="{e(anchor)}"' if anchor else ""
    return f"<h2{aid}>{e(text)}</h2>\n"


def h3(text: str, anchor: str = "") -> str:
    aid = f' id="{e(anchor)}"' if anchor else ""
    return f"<h3{aid}>{e(text)}</h3>\n"


def h4(text: str) -> str:
    return f"<h4>{e(text)}</h4>\n"


def p(*parts: str, cls: str = "") -> str:
    attr = f' class="{cls}"' if cls else ""
    body = " ".join(parts)
    return f"<p{attr}>{body}</p>\n"


def raw_p(*parts: str, cls: str = "") -> str:
    """Paragraph that already contains safe HTML (bold, ₹, etc.)."""
    attr = f' class="{cls}"' if cls else ""
    return f"<p{attr}>{''.join(parts)}</p>\n"


def b(text: str) -> str:
    return f"<strong>{e(text)}</strong>"


def i(text: str) -> str:
    return f"<em>{e(text)}</em>"


def rupee(n) -> str:
    """Format a number as Indian-style rupees. Accepts int/float/str."""
    if isinstance(n, str):
        return f"₹{n}"
    if n is None:
        return "₹0"
    neg = n < 0
    n = abs(n)
    if isinstance(n, float) and not n.is_integer():
        s = f"{n:,.2f}"
    else:
        s = f"{int(n):,}"
    # Indian grouping for integer part when >= 1000
    if "." in s:
        whole, dec = s.split(".")
        s = _indian(whole) + "." + dec
    else:
        s = _indian(s.replace(",", ""))
    return f"{'−' if neg else ''}₹{s}"


def _indian(digits: str) -> str:
    digits = digits.replace(",", "")
    if len(digits) <= 3:
        return digits
    last3 = digits[-3:]
    rest = digits[:-3]
    parts = []
    while len(rest) > 2:
        parts.append(rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.append(rest)
    return ",".join(reversed(parts)) + "," + last3


def ul(items: Sequence[str], ordered: bool = False) -> str:
    tag = "ol" if ordered else "ul"
    lis = "".join(f"<li>{item}</li>\n" for item in items)
    return f"<{tag}>\n{lis}</{tag}>\n"


def ol(items: Sequence[str]) -> str:
    return ul(items, ordered=True)


def box(kind: str, title: str, body: str) -> str:
    return (
        f'<aside class="box box-{kind}">'
        f'<div class="box-label">{e(title)}</div>'
        f'<div class="box-body">{body}</div>'
        f"</aside>\n"
    )


def definition(text: str) -> str:
    return box("def", "1. What is it? — Definition", f"<p>{text}</p>")


def simple(text: str) -> str:
    return box("simple", "2. In simple words", f"<p>{text}</p>")


def why(text: str) -> str:
    return box("why", "3. Why do we need it?", f"<p>{text}</p>")


def real_life(text: str) -> str:
    return box("life", "4. Real-life example", f"<p>{text}</p>")


def logic(text: str) -> str:
    return box("logic", "5. Accounting logic", f"<p>{text}</p>")


def format_box(title: str, body: str) -> str:
    return box("format", f"6. Format — {title}", body)


def steps(items: Sequence[str], title: str = "7. Step-by-step method (exam procedure)") -> str:
    return box("steps", title, ol(items))


def identify(text: str) -> str:
    return box("id", "9. How to identify the question", f"<p>{text}</p>")


def mistakes(items: Sequence[str]) -> str:
    return box("miss", "10. Common mistakes", ul(items))


def memory(text: str) -> str:
    return box("mem", "11. Memory trick", f"<p>{text}</p>")


def exam_answer(text: str) -> str:
    return box("exam", "12. Exam-ready answer", f"<p>{text}</p>")


def exam_tip(text: str) -> str:
    return box("tip", "Exam tip", f"<p>{text}</p>")


def formula(expr: str, note: str = "") -> str:
    extra = f'<p class="formula-note">{note}</p>' if note else ""
    return box("formula", "Formula", f'<p class="formula">{expr}</p>{extra}')


def keypoint(text: str) -> str:
    return box("key", "Key point", f"<p>{text}</p>")


def connect(text: str) -> str:
    return box("connect", "Connect the chapters", f"<p>{text}</p>")


def warn(text: str) -> str:
    return box("miss", "Watch out", f"<p>{text}</p>")


def table(headers: Sequence[str], rows: Sequence[Sequence[str]], caption: str = "", foot: str = "", cls: str = "") -> str:
    cap = f"<caption>{e(caption)}</caption>" if caption else ""
    th = "".join(f"<th>{h}</th>" for h in headers)
    body_rows = []
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        body_rows.append(f"<tr>{tds}</tr>")
    foot_html = ""
    if foot:
        foot_html = f'<p class="table-foot">{foot}</p>'
    return (
        f'<div class="table-wrap {cls}">'
        f"<table>{cap}<thead><tr>{th}</tr></thead>"
        f"<tbody>{''.join(body_rows)}</tbody></table>"
        f"{foot_html}</div>\n"
    )


def journal(entries: Sequence[dict], caption: str = "Journal") -> str:
    """
    entries: list of {
      date, debit (str or list), credit (str or list), amount (str) or
      dr_amt, cr_amt, narration
    }
    For compound: debit can be list of (name, amt), credit list of (name, amt)
    """
    rows_html = []
    for ent in entries:
        date = e(ent.get("date", ""))
        narr = ent.get("narration", "")
        if "lines" in ent:
            first = True
            for line in ent["lines"]:
                acc = e(line["account"])
                if line["side"] == "dr":
                    part = f"{acc} {'…' * 2} Dr."
                    dr, cr = line.get("amount", ""), ""
                else:
                    part = f'<span class="indent">To {acc}</span>'
                    dr, cr = "", line.get("amount", "")
                d = date if first else ""
                rows_html.append(
                    f"<tr><td>{d}</td><td>{part}</td><td></td>"
                    f"<td class='num'>{dr}</td><td class='num'>{cr}</td></tr>"
                )
                first = False
            if narr:
                rows_html.append(
                    f"<tr class='narr'><td></td><td colspan='4'>"
                    f"<em>({e(narr)})</em></td></tr>"
                )
            continue
        debit = ent.get("debit", "")
        credit = ent.get("credit", "")
        amt = ent.get("amount", "")
        rows_html.append(
            f"<tr><td>{date}</td><td>{e(debit)} {'…' * 2} Dr.</td><td></td>"
            f"<td class='num'>{amt}</td><td></td></tr>"
        )
        rows_html.append(
            f"<tr><td></td><td class='indent'>To {e(credit)}</td><td></td>"
            f"<td></td><td class='num'>{amt}</td></tr>"
        )
        if narr:
            rows_html.append(
                f"<tr class='narr'><td></td><td colspan='4'><em>({e(narr)})</em></td></tr>"
            )
    cap = f"<caption>{e(caption)}</caption>"
    return (
        '<div class="table-wrap journal">'
        f"<table>{cap}"
        "<thead><tr><th style='width:14%'>Date</th><th>Particulars</th>"
        "<th style='width:8%'>L.F.</th><th style='width:16%'>Debit (₹)</th>"
        "<th style='width:16%'>Credit (₹)</th></tr></thead>"
        f"<tbody>{''.join(rows_html)}</tbody></table></div>\n"
    )


def t_account(name: str, dr: Sequence[tuple], cr: Sequence[tuple], dr_bal: str = "", cr_bal: str = "") -> str:
    """dr/cr are list of (particulars, amount)."""
    n = max(len(dr) + (1 if dr_bal else 0), len(cr) + (1 if cr_bal else 0), 1)
    rows = []
    for i in range(n):
        if i < len(dr):
            dl, da = dr[i]
            left = f"<td>{e(dl)}</td><td class='num'>{da}</td>"
        elif i == len(dr) and dr_bal:
            left = f"<td><strong>Balance c/d</strong></td><td class='num'><strong>{dr_bal}</strong></td>"
        else:
            left = "<td></td><td></td>"
        if i < len(cr):
            cl, ca = cr[i]
            right = f"<td>{e(cl)}</td><td class='num'>{ca}</td>"
        elif i == len(cr) and cr_bal:
            right = f"<td><strong>Balance c/d</strong></td><td class='num'><strong>{cr_bal}</strong></td>"
        else:
            right = "<td></td><td></td>"
        rows.append(f"<tr>{left}{right}</tr>")
    return (
        f'<div class="t-account"><h4>Dr &nbsp; {e(name)} &nbsp; Cr</h4>'
        "<table><thead><tr>"
        "<th>Particulars</th><th>₹</th><th>Particulars</th><th>₹</th>"
        "</tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table></div>\n"
    )


def example(num: str, level: str, title: str, body: str) -> str:
    return (
        f'<section class="example level-{level.lower()}">'
        f'<header class="ex-head"><span class="ex-kicker">Solved example {e(num)} · {e(level)}</span>'
        f"<h4>{e(title)}</h4></header>"
        f'<div class="ex-body">{body}</div></section>\n'
    )


def practice(num: str, level: str, title: str, q: str, a: str = "") -> str:
    ans = f'<div class="practice-ans"><p class="ans-label">Answer / solution</p>{a}</div>' if a else ""
    return (
        f'<section class="practice level-{level.lower()}">'
        f'<header class="ex-head"><span class="ex-kicker">Practice {e(num)} · {e(level)}</span>'
        f"<h4>{e(title)}</h4></header>"
        f'<div class="ex-body"><div class="practice-q">{q}</div>{ans}</div></section>\n'
    )


def two_col(left: str, right: str) -> str:
    return f'<div class="two-col"><div>{left}</div><div>{right}</div></div>\n'


def hr() -> str:
    return "<hr />\n"


def chapter_open(num: str, title: str, outcome: str, syllabus: Sequence[str]) -> str:
    items = "".join(f"<li>{e(s)}</li>" for s in syllabus)
    return f"""
<section class="chapter" id="ch-{e(num)}">
  <header class="chapter-head">
    <p class="kicker">Chapter {e(num)}</p>
    <h1>{e(title)}</h1>
    <p class="outcome"><strong>Learning outcome.</strong> {e(outcome)}</p>
    <div class="syllabus-box">
      <p class="box-label">What this chapter covers (official syllabus)</p>
      <ul>{items}</ul>
    </div>
  </header>
  <div class="chapter-body">
"""


def chapter_close() -> str:
    return "</div></section>\n"


def qna(q: str, a: str, marks: str = "") -> str:
    mk = f'<span class="marks">{e(marks)}</span>' if marks else ""
    return (
        f'<article class="qna">{mk}<h4 class="q">{e(q)}</h4>'
        f'<div class="a">{a}</div></article>\n'
    )


def numbered_steps_inline(items: Sequence[str]) -> str:
    return ol(items)


def lead(text: str) -> str:
    return raw_p(text, cls="lead")
