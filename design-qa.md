# SECHA investment memo — design and functional QA

Final result: passed

## Reference and scope

The requested revision converts the portal into an investment memo with a manifesto, presents Josephine as the only founder, replaces the hypothetical product mockup with actual Studio+ source captures, and adds a video opening.

Source evidence is the supplied business update and the actual public Studio+ code at revision 8d0c074fd7cd73bb86770cc5707a9f6af7e9f5a4. The website's deployment integration identifies that repository and the /studio/playground.html route. The live domain is blocked by this environment's network policy; production deployment parity is not claimed. See docs/content-notes.md for exact sources and media provenance.

## Visual verification

Inspected the source playground in Studio, Residence and Commercial states; the memo cover, manifesto, product chapter and founder chapter; desktop and mobile page captures; the opening-film state; and the three-page printable memo.

The product chapter preserves the actual app's layout, controls and 3D scene through screenshots. Its own tab controls and full-size links work; a separate action opens the real playground. The authored manifesto is presented as editorial copy, not a historical founder quotation.

## Browser verification

22 checks passed with tests/browser-qa.py in Chromium:

- Memo, manifesto, Josephine-only founder, reduced-motion bypass and all chapter destinations.
- Three real source captures, selected states, accessible tab keys, full-size image links and live route.
- Calculator minimum, intermediate and maximum values.
- Investor enquiry and founder contact, actual clipboard copying, Escape and focus restoration.
- Real PDF download and FAQ expansion.
- No horizontal overflow at 320, 390, 600, 768, 1024 and 1440px; working mobile navigation.
- Video playback, muted/inline mode, pause/resume, manual replay, Escape and focus restoration.
- Automatic playback and end-to-memo transition, real media-tied progress, refresh replay and Skip.
- Recovery from rejected autoplay, unavailable media and stalled startup.
- Save-Data bypass and readable no-JavaScript fallback.
- No runtime JavaScript errors, failed page assets or external runtime dependencies in the main user journey.

axe-core 4.10.3 reported no WCAG 2 A/AA or WCAG 2.1 AA violations for all three Studio+ states, the mobile memo, investor enquiry dialog and paused opening-film dialog.

JavaScript syntax, whitespace, PDF page count and extracted-content checks passed. The three-page PDF contains only Josephine's founder profile, the intended business facts and no excluded partner branding. Automated accessibility scans are not a full manual audit.

## Boundaries

Current production deployment parity is unverified because the live domain is network-blocked. All product rendering evidence was captured from the exact public source identified by the website's deployment integration. The portal was validated locally and was not deployed. Company financial claims remain unverified; target margins and illustrative scale cases remain labelled.
