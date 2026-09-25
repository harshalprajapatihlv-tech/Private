# Chapter writer contract

You write ONE Python module that returns a complete HTML chapter string.

## File
The file must define:

```python
from html_lib import *

def body() -> str:
    parts = []
    parts.append(...)
    return "".join(parts)
```

Import with: `import sys; sys.path.insert(0, "/workspace/notes"); from html_lib import *`

## Teaching style (mandatory)
Assume a complete beginner. Simple English. Indian ₹ examples.
For every MAJOR concept use this sequence (use the helper functions):
1. definition()
2. simple()
3. why()
4. real_life()
5. logic()
6. format_box() where a format exists
7. steps() exam procedure
8. example() solved — Easy, then Moderate, then Exam-level
9. identify() "If the question says ___ I should use ___"
10. mistakes()
11. memory()
12. exam_answer() where theory is asked

Never skip intermediate arithmetic. Show every multiplication.
Use rupee() for amounts where convenient, or type ₹1,00,000 with Indian commas.
Do NOT invent topics outside the assigned syllabus slice.
Do NOT write a summary. TEACH. Target density: a student can sit and learn only from this chapter.

## HTML
Use only html_lib helpers plus raw strings of simple tags (<p>, <strong>, <em>, <br/>).
Do not include <html>, <body>, css, or chapter_open/close unless asked — the build script wraps chapters.
Start with chapter_open(num, title, outcome, syllabus_list) and end with chapter_close().

## Accuracy
- Golden rules and modern debit/credit rules must be textbook-correct.
- Journal: Debit left, Credit right; narration in brackets.
- Accounting equation: Assets = Liabilities + Capital.
- FIFO: first goods purchased are issued first.
- WAM: weighted average cost = total cost of goods available / total units available (periodic) OR moving average after each purchase (perpetual). Teach BOTH and state which one you are using in each example. For MBA exams, perpetual/moving weighted average is common; also show periodic.
- SLM: (Cost − Residual) / Life. Rate = (1/Life)*100 on original cost.
- WDV: Depreciation = Book value × rate. Residual is NOT deducted each year; the rate already aims toward residual.
- Schedule III: Equity & Liabilities on one side, Assets on the other. Use Companies Act 2013 vertical format used in Indian MBA exams.
- Cash flow: Indirect method, AS-3 / Ind AS-7 classification. Profit ≠ cash.
- Ratios: write formula, plug numbers, interpret (higher/lower meaning).

## Indian number format
1,00,000 not 100,000. 10,00,000 for ten lakh.
