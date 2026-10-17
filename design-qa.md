# SECHA — Indonesia-to-Asia pitch and material system QA

Final result: passed

## Current request

The portal now uses a US$10,000 minimum package and a fixed 30% gross-margin pricing rule at every package value. The new film starts in Jakarta/Indonesia, shows wider Asia, and dissolves into modular assembly under the headline "The renovation interface for Asia".

The physical-system narrative now covers material development, EPS-core wall panels, framed composite tables and modular partitions, flatpack packaging and modular site assembly. The founder/backer record and actual Studio+ source captures remain intact. Copy uses a direct venture-pitch approach without claiming YC/a16z affiliation.

## Visual and media evidence

Inspected desktop/mobile covers, the geographic opening, new material concept in the page and PDF, and seven print pages with no footer collisions.

The new photorealistic EPS/flatpack image is generated concept art, labelled as such. It depicts EPS inside rigid facings and frames, not unsupported structural foam. The development specification makes validation status clear and claims no certifications or load/performance ratings.

The opening map uses bundled public-domain Natural Earth outlines, highlights Indonesia and plots Jakarta at 106.8456 E, 6.2088 S. The geographic animation expresses origin and ambition, not operating coverage. The source modular film follows through a dissolve. The final H.264 film is approximately 8.08 seconds, 960 × 540, silent, with a map-phase poster. Renderer cache configuration and asset regeneration were exercised successfully.

All editable typography remains Inter and the native palette remains SECHA navy/ivory/bronze.

## Browser checks

26 checks passed with tests/browser-qa.py, Chromium and axe-core 4.10.3:

- Memo, manifesto, Josephine-only founder, reduced-motion bypass, Inter, confirmed backers and profile link.
- Market assumptions, promised-land and growth sections.
- Entry-unit defaults: US$10,000 package, US$7,000 fulfilment, US$3,000 gross profit, US$2,700 illustrative contribution, eight monthly break-even jobs and US$2,000 delivery gap.
- Higher-price test: US$20,000 price, US$14,000 fulfilment, US$6,000 gross profit and US$5,700 illustrative contribution; annual scale updates to US$200M / US$60M.
- Below-minimum input normalises to US$10,000. Margin stays exactly 30%, with no rate input.
- Changed acquisition/support/overhead/deposit scenarios; zero and negative contribution; no break-even when contribution is not positive.
- Generated material image loads at its expected resolution; wall/table/partition specifications and engineering disclosure work.
- Every chapter destination; three Studio+ capture tabs, keyboard operation, full-size image and live route.
- Volume-calculator minimum/intermediate/maximum cases: US$10M/US$3M, US$55M/US$16.5M, US$100M/US$30M.
- Enquiry dialogs, clipboard, Escape/focus restoration, PDF download and FAQs.
- No horizontal overflow at 320, 390, 600, 768, 1024 and 1440px, plus functioning mobile navigation.
- Actual muted inline film playback, pause/resume, replay, Escape, media progress, completion, refresh and Skip.
- Rejected autoplay, unavailable media and startup-stall recovery; Save-Data and no-JavaScript fallbacks.
- No runtime JavaScript errors, failed main-journey assets or external runtime dependencies.

WCAG 2 A/AA and WCAG 2.1 AA automated scans reported no violations for Studio+ states, the mobile memo, investor enquiry and paused opening dialog. This is not a complete manual accessibility audit.

## Print and source checks

The updated PDF has seven A4 pages. All page content stays within its page and clears the footer (minimum measured clearance 24px). Text checks verify the minimum price, 70/30 split, recomputed scale figures, EPS section and confirmed backers, with prior lower pricing and excluded partner/founder material removed from current business claims.

JavaScript syntax, renderer shell syntax and whitespace checks passed. The EPS image and geographic source assets are local. The optional film renderer uses Python matplotlib and ffmpeg; the application needs neither at runtime.

## Claim boundaries

The pricing policy is a current founder instruction, not a restatement of historical realised margins. Contribution varies after acquisition/support while gross margin stays fixed at 30%. Market volumes and CAC/support/overhead/deposit values remain labelled modelling assumptions. US$300K remains historical company-reported project value, not revenue.

The material image is a development concept, not evidence of manufacturing readiness. The source-backed Studio+ screenshots are not proof of operational quoting/lending/fulfilment integrations. The live product domain remains independently unverified because of network-policy restrictions. Prior backers are founder-confirmed; cheque sizes and instruments are not invented.
