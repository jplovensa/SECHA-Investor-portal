# SECHA investor portal — design and functional QA

Final result: passed

## Reference and scope

The existing portal and the supplied 2026 business update were reviewed before implementation. The redesigned portal uses the update's warm material imagery and business model as its reference; this is a redesign, not a pixel-for-pixel reproduction of the submission.

Desktop (1440 × 1000) and mobile (390 × 844) screenshots, full-page captures and the two-page investor PDF were visually inspected. Final viewport captures are in docs/previews/.

## Verified

- 13 browser smoke checks passed in Chromium: root response and local font loading; updated narrative; anchor destinations; four journey states; keyboard tab navigation; calculator boundary and intermediate values; both enquiry CTAs, email link, actual clipboard copy, Escape and focus restoration; PDF download; FAQ expansion; six responsive widths; mobile navigation; no runtime errors, failed resources or external runtime requests; automated accessibility scan.
- No horizontal overflow at 320, 390, 600, 768, 1024 and 1440px.
- axe-core 4.10.3 reported zero WCAG 2 A/AA and WCAG 2.1 AA violations for the main page, each of the four journey tab states on mobile, and the enquiry dialog.
- PDF download produces a valid two-page A4 document. Text extraction confirms the raise, traction, founders and planned allocations; excluded partner branding is absent.
- JavaScript syntax and git whitespace checks passed.
- Reported project value, target margin and illustrative annual scale are clearly distinguished. No signed bank partnerships, investment commitments, valuation or achieved margin were invented.
- Source imagery, fonts and library icons load locally. Font and icon licenses are included.

## Corrections made during QA

- Increased contrast for supporting text on light surfaces and inside the enquiry dialog.
- Corrected economics-panel overflow at 320px.
- Replaced unsupported arrow glyphs with bundled Bootstrap Icons.
- Corrected the printable brief's page overflow and footer collision.

## Boundaries

Automated scans do not replace a full manual accessibility audit. Email enquiries use the visitor's email client; the site does not submit forms or send emails. Product screenshots and financing/tracking explanations illustrate the supplied business model rather than a connected operating system. Business figures are supplied company claims and were not independently verified. The site has been run locally, not deployed to a public host.
