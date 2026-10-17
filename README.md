# SECHA Investment Memo

An editorial investor portal with a manifesto, actual Studio+ product captures, GX-100 operating thesis, package economics, Josephine Lovensa's founder profile and the US$1M raise.

## Run

Requires Python 3. No dependency installation, build, API keys or backend is needed.

    python3 -m http.server 8000 --bind 0.0.0.0

Use the existing isolated checkout; no Git worktree is needed. All runtime imagery, film, fonts, scripts and styles are local. External links open SECHA's Studio+ playground or the visitor's email client.

## Experience

- Memo cover and chapter index.
- Manifesto and Josephine-only founder presentation.
- Three captures from the actual public Studio+ playground source, with keyboard-accessible selectors and a live-product link.
- Illustrative annual-volume calculator, expandable investor FAQs and enquiry dialog with clipboard support.
- Downloadable three-page investment memo.

The five-second, silent opening film starts on each full page load. Skip or Escape dismisses it; Pause/Resume and manual replay are available. Automatic playback is bypassed for reduced motion and Save-Data. Media failures and timeouts reveal the memo. JavaScript-disabled visitors can read the memo without the film.

The Studio+ captures are product evidence, not embedded operational dashboards. The portal does not process renovation orders, credit applications or enquiry submissions.

## Browser regression

The optional QA tool requires Python Playwright and a compatible system Chromium:

    python3 tests/browser-qa.py --base-url http://127.0.0.1:8000

Use --chromium to select another binary and --artifacts to set the screenshot directory. To run automated accessibility scans, pass --axe /path/to/axe.min.js (validated with axe-core 4.10.3). No enquiries or external transactions are submitted.

See [content provenance](docs/content-notes.md), [design QA](design-qa.md) and the [editable print memo](docs/investor-brief.html).
