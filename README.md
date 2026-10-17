# SECHA Investor Portal

A responsive, static investor overview based on SECHA's supplied 2026 business update. Covers the renovation package model, controlled job files, GX-100 delivery, package economics, distribution, founders and US$1M raise.

## Run locally

Requires Python 3. No dependency installation or build is needed.

From this checkout:

    python3 -m http.server 8000 --bind 0.0.0.0

Use the existing checkout in the isolated cloud workspace; no Git worktree is needed. Open the served root in your browser. Deploy this directory with any static web host.

All fonts, imagery, scripts and styles are local; no API keys, backend or external CDN access is required.

## Interactions

- Accessible journey tabs with arrow-key, Home and End navigation.
- Illustrative annual-volume calculator using US$5,000 per package and a target 30% margin.
- Mobile menu, anchored section navigation and expandable investor FAQs.
- Investor enquiry dialog with email link and clipboard action.
- Downloadable, business-only investor overview PDF.

Product screenshots are source illustrations. This investor portal does not process renovation orders, credit applications or enquiry submissions.

See [content provenance](docs/content-notes.md) for source mapping, metric qualifications and exclusions. The editable brief is [docs/investor-brief.html](docs/investor-brief.html).
