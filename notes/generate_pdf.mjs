import { chromium } from "playwright";
import { fileURLToPath } from "node:url";
import path from "node:path";

const notesDir = path.dirname(fileURLToPath(import.meta.url));
const book = path.join(notesDir, "../public/notes/book.html");
const out = path.join(notesDir, "../public/Accounting-for-Managers-Complete-Notes.pdf");
const fileUrl = "file://" + book;

const browser = await chromium.launch({ args: ["--font-render-hinting=none"] });
const page = await browser.newPage();
await page.goto(fileUrl, { waitUntil: "load", timeout: 120000 });
await page.emulateMedia({ media: "print" });
await page.pdf({
  path: out,
  format: "A4",
  printBackground: true,
  preferCSSPageSize: true,
  displayHeaderFooter: false,
});
await browser.close();
console.log("PDF written", out);
