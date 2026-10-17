# SECHA investment pitch — design and functional QA

Final result: passed

## Scope and source evidence

This revision redesigns the film opening and investment case in the main SECHA website's Inter typography and navy/ivory/bronze palette. The memo adds a promised-land vision, a proposed Greater Jakarta beachhead, an explicit market-sizing model, detailed unit/cash sensitivities, growth gates, pedigree and founder-confirmed previous backers.

The user named Antler, Startupbootcamp and BonBillo in this conversation and supplied Josephine's LinkedIn profile. These are treated as founder-confirmed names, without invented cheque sizes, instruments, education or exit proceeds. Existing founder credentials come from the supplied business deck.

The source-backed Studio+ captures are retained. Source revisions and the live-domain access limit are recorded in docs/content-notes.md. The current production deployment is not independently verified.

## Visual verification

Inspected desktop/mobile covers, the redesigned navy opening with ivory video exhibit and bronze progress, full-page captures, market and beachhead sections, detailed economics, previous backing and the six-page printable investment memo.

All editable typography uses Inter, including headings, italic-style emphasis replacements, labels, controls and print. Main SECHA source tokens: navy #162638, ivory #f4efe4, off-white #fffdf9, bronze #806847, light bronze #c4a578 and border #dcd5c8. Previous green and serif styling is removed.

The supplied assembly film is slowed to six seconds and regraded with restrained saturation, contrast and warm colour balance. Native UI text remains accessible, separate from the video raster. Progress is driven by actual media time.

## Verified checks

24 browser checks passed with tests/browser-qa.py and axe-core 4.10.3:

- Investment memo and manifesto; Josephine-only founder presentation.
- Inter, founder-confirmed previous backers and profile link, explicit market assumptions, promised-land and growth sections.
- Unit model defaults, changed acquisition/support/overhead/deposit assumptions, fully deposit-covered fulfilment, zero/negative contribution, break-even handling and cost-ledger disclosure.
- Every chapter destination; three real Studio+ capture states and keyboard tabs; full-size image and live-product routes.
- Annual package calculator minimum, intermediate and maximum values.
- Contact and founder enquiry, actual clipboard copying, Escape and focus restoration.
- Real PDF download and FAQ expansion.
- No horizontal overflow at 320, 390, 600, 768, 1024 and 1440 pixels; functioning mobile navigation.
- Real muted inline video playback, pause/resume, manual replay, Escape, focus restoration, media-tied progress, automatic completion, refresh and Skip.
- Rejected autoplay, unavailable media and startup-stall recovery; Save-Data and reduced-motion bypass; readable no-JavaScript fallback.
- No runtime JavaScript errors, failed assets or external runtime dependencies in the main user journey.

Automated WCAG 2 A/AA and WCAG 2.1 AA scans reported no violations across all three Studio+ states, investor enquiry, mobile memo and paused opening-film dialog. Automated scans do not replace a full manual accessibility audit.

JavaScript syntax, renderer shell syntax, whitespace, six-page PDF count, PDF content and footer/layout checks passed. The PDF uses Inter, contains the confirmed backer names and model qualifications, and excludes the earlier partner branding and other founder profiles.

## Financial and research boundaries

- US$300K project value is historical company-reported project value, not revenue.
- US$5,000/US$3,500/US$1,500 and 30% margin are designed target economics, not realised results.
- National and Greater Jakarta eligible annual job counts are explicit planning assumptions, not externally validated market research. The sizing model is annual project value, not revenue or a forecast.
- Acquisition/support/overhead/deposit inputs are underwriting assumptions. No actual subcategory fulfilment costs are invented.
- Growth volumes are proposed gates, not achieved traction or committed pipeline.
- Backer names are founder-confirmed; awards/media/programme participation are not counted as funding events.
- LinkedIn was network-blocked. The profile is linked, but unseen education/employer information was not inferred.
