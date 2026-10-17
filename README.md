# SECHA Investment Memo

An investment pitch in SECHA navy, ivory and bronze, using self-hosted Inter throughout. Includes a manifesto and promised-land vision, a proposed beachhead, explicit market-sizing assumptions, actual Studio+ captures, detailed unit/cash sensitivities, growth gates, Josephine's pedigree, founder-confirmed previous backers and the US$1M raise.

## Run

Requires Python 3. No dependency installation, build, API keys or backend is needed.

    python3 -m http.server 8000 --bind 0.0.0.0

Use the existing isolated checkout; no Git worktree is needed. All runtime imagery, film, fonts, scripts and styles are local. External links open SECHA's Studio+ playground or the visitor's email client.

## Experience

- Memo cover and chapter index.
- Manifesto, promised-land vision and Josephine-only founder presentation.
- Proposed Greater Jakarta beachhead and bottom-up market model with explicitly labelled annual-volume assumptions.
- Founder-confirmed previous backers: Antler, Startupbootcamp and BonBillo.
- Three captures from the actual public Studio+ playground source, with keyboard-accessible selectors and a live-product link.
- US$10,000 minimum package value with a fixed 30% gross margin, including higher-package examples and updated annual-volume, contribution, break-even and working-capital calculations.
- AI-generated realistic EPS-composite wall, table and partition concept; flatpack and modular assembly development specifications.
- Expandable investor FAQs and an enquiry dialog with clipboard support.
- Downloadable seven-page investment memo with material-development imagery and specifications.

The roughly eight-second Indonesia-to-Asia opening film starts on each full page load. Skip or Escape dismisses it; Pause/Resume and manual replay are available. Automatic playback is bypassed for reduced motion and Save-Data. Media failures and timeouts reveal the memo. JavaScript-disabled visitors can read the memo without the film.

The Studio+ captures are product evidence, not embedded operational dashboards. The portal does not process renovation orders, credit applications or enquiry submissions.

## Browser regression

The optional QA tool requires Python Playwright and a compatible system Chromium:

    python3 tests/browser-qa.py --base-url http://127.0.0.1:8000

Use --chromium to select another binary and --artifacts to set the screenshot directory. To run automated accessibility scans, pass --axe /path/to/axe.min.js (validated with axe-core 4.10.3). No enquiries or external transactions are submitted.

See [content provenance](docs/content-notes.md), [design QA](design-qa.md) and the [editable print memo](docs/investor-brief.html).

Regenerate the film with bash scripts/render-opening.sh /path/to/original/furniture-assembly.mp4 (requires ffmpeg and Python matplotlib). Use the original SECHA website source clip, not the generated output. The renderer first builds a local Natural Earth map of Asia centred on SECHA’s Jakarta origin, then dissolves into the modular assembly film.
