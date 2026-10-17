"""Browser regression for the investor memo.

Requires Python Playwright and Chromium. Serve the repo before running:
    python3 tests/browser-qa.py --base-url http://127.0.0.1:8000
Optional axe-core script:
    python3 tests/browser-qa.py --axe /path/to/axe.min.js
No external links, emails or investor enquiries are submitted.
"""
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser()
parser.add_argument("--base-url", default="http://127.0.0.1:8000")
parser.add_argument("--chromium", default="/usr/bin/chromium")
parser.add_argument("--artifacts", default="/tmp/secha-memo-qa")
parser.add_argument("--axe", type=Path)
args = parser.parse_args()
base = args.base_url.rstrip("/") + "/"
artifacts = Path(args.artifacts)
artifacts.mkdir(parents=True, exist_ok=True)
checks = []

def passed(label):
    checks.append(label)
    print("PASS:", label, flush=True)

def audit(page, label):
    if not args.axe:
        return
    if not page.evaluate("typeof axe !== 'undefined'"):
        page.add_script_tag(path=str(args.axe))
    violations = page.evaluate("""async () => (await axe.run(document, {
        runOnly: {type: "tag", values: ["wcag2a", "wcag2aa", "wcag21aa"]}
    })).violations.map(v=>({id:v.id, nodes:v.nodes.map(n=>n.target)}))""")
    assert not violations, (label, violations)
    passed("Accessibility: " + label)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=args.chromium, headless=True, args=["--no-sandbox"])
    context = browser.new_context(viewport={"width":1440,"height":1000}, reduced_motion="reduce",
                                  permissions=["clipboard-read","clipboard-write"])
    page = context.new_page()
    errors, failed, external = [], [], []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("requestfailed", lambda r: failed.append(r.url))
    page.on("request", lambda r: external.append(r.url) if not r.url.startswith(base) and not r.url.startswith("data:") else None)
    assert page.goto(base, wait_until="networkidle").status == 200
    expect(page.locator("#opening")).not_to_be_visible()
    assert not page.locator("#opening-video").get_attribute("src")
    assert "The renovation" in page.locator("h1").inner_text()
    body = page.locator("body").inner_text()
    for excluded in ["Leonardi", "Co-Founder", "NTT", "Living OS"]:
        assert excluded not in body, excluded
    assert page.locator("#founder h2").inner_text().replace("\n"," ") == "Josephine Lovensa."
    expect(page.locator("#manifesto")).to_contain_text("Freedom in the choices.")
    passed("Memo, manifesto, Josephine-only founder and reduced-motion bypass")

    assert page.locator("body").evaluate("(el)=>getComputedStyle(el).fontFamily.startsWith('Inter')")
    assert page.locator("h1 em").evaluate("(el)=>getComputedStyle(el).fontFamily.startsWith('Inter')")
    for name in ["Antler", "Startupbootcamp", "BonBillo"]:
        expect(page.locator(".backer-strip")).to_contain_text(name)
    assert page.locator(".founder-profile-link").get_attribute("href") == "https://www.linkedin.com/in/josephinepetralovensa/"
    for section in ["market","promised-land","growth"]:
        expect(page.locator("#"+section)).to_be_visible()
    expect(page.locator(".market-sizing")).to_contain_text("PLANNING ASSUMPTIONS")
    expect(page.locator(".market-sizing")).to_contain_text("not independently researched TAM/SAM")
    passed("Inter, SECHA brand, founder-confirmed backers, market assumptions and growth case")
    expect(page.locator("#contribution")).to_have_text("US$2,700")
    expect(page.locator("#break-even")).to_have_text("8 jobs / month")
    expect(page.locator("#cash-gap")).to_have_text("US$2,000")
    expect(page.locator("#concurrent-gap")).to_have_text("US$20,000")
    page.locator("#cac").fill("500")
    page.locator("#support").fill("200")
    page.locator("#fixed-opex").fill("24000")
    page.locator("#deposit").fill("70")
    expect(page.locator("#contribution")).to_have_text("US$2,300")
    expect(page.locator("#break-even")).to_have_text("11 jobs / month")
    expect(page.locator("#cash-gap")).to_have_text("US$0")
    page.locator("#cac").fill("3000")
    page.locator("#support").fill("0")
    expect(page.locator("#break-even")).to_have_text("Not reached")
    page.locator("#cac").fill("3500")
    expect(page.locator("#contribution")).to_have_text("-US$500")
    expect(page.locator("#break-even")).to_have_text("Not reached")
    for field,value in [("cac","200"),("support","100"),("fixed-opex","20000"),("deposit","50")]:
        page.locator("#"+field).fill(value)
    page.locator(".cost-scope summary").click()
    expect(page.locator(".cost-scope")).to_have_attribute("open","")
    passed("Detailed unit economics: defaults, sensitivity, cash coverage, zero/negative contribution and cost scope")

    page.locator("#package-price").fill("20000")
    expect(page.locator("#ledger-price")).to_have_text("US$20,000")
    expect(page.locator("#ledger-cost")).to_have_text("− US$14,000")
    expect(page.locator("#ledger-gross")).to_have_text("US$6,000 / 30%")
    expect(page.locator("#contribution")).to_have_text("US$5,700")
    expect(page.locator("#project-value")).to_have_text("US$200M")
    expect(page.locator("#gross-profit")).to_have_text("US$60M")
    page.locator("#package-price").fill("5000")
    page.locator("#package-price").press("Tab")
    expect(page.locator("#package-price")).to_have_value("10000")
    expect(page.locator("#ledger-gross")).to_have_text("US$3,000 / 30%")
    expect(page.locator("#ledger-cost")).to_have_text("− US$7,000")
    expect(page.locator("#contribution")).to_have_text("US$2,700")
    passed("US$10,000 minimum enforced; 30% gross margin stays fixed for larger packages")
    expect(page.locator("#platform")).to_contain_text("Think The Sims")
    expect(page.locator("#platform")).to_contain_text("SECHA+ is the renovation playground")
    expect(page.locator(".material-stages > li")).to_have_count(4)
    for gate in ["Prove the composite.","Make the parts compatible.","Ship one complete renovation.","Turn play into a package."]:
        expect(page.locator(".materials-roadmap")).to_contain_text(gate)
    expect(page.locator(".materials-roadmap")).to_contain_text("Proposed development stages")
    assert "GX-100" not in body
    passed("SECHA+ Sims-like concept playground and four gated material-product releases")
    expect(page.locator("#renovacredit")).to_contain_text("THE PRODUCT WE ARE RAISING FOR")
    expect(page.locator("#investment")).to_contain_text("Fund RenovaCredit.")
    expect(page.locator("#renovacredit a").first).to_have_attribute("href","https://jplovensa.github.io/SECHA-Credit-Engine/")
    page.locator(".credit-capture").scroll_into_view_if_needed()
    page.wait_for_function("document.querySelector('.credit-capture img').naturalWidth === 1440")
    assert "AI-generated" not in body
    passed("RenovaCredit fundraising line, source capture, product link and requested material caption")
    for package, price, profit in [("refresh","US$10,000","US$3,000"),("livework","US$15,000","US$4,500"),("studio","US$20,000","US$6,000")]:
        page.locator(f'input[name="renovation-package"][value="{package}"]').check()
        expect(page.locator("#menu-total")).to_have_text(price)
        expect(page.locator("#menu-profit")).to_have_text(profit)
    page.locator('input[name="renovation-package"][value="livework"]').check()
    page.locator("#menu-panels").select_option("1")
    page.locator("#menu-tables").select_option("1")
    page.locator("#menu-finish").select_option("bronze")
    expect(page.locator("#menu-total")).to_have_text("US$19,500")
    expect(page.locator("#menu-cost")).to_have_text("US$13,650")
    expect(page.locator("#menu-profit")).to_have_text("US$5,850")
    expect(page.locator("#menu-components")).to_have_text("16 Snap panels · 2 tables · 1 partition")
    expect(page.locator("#menu-gap")).to_have_text("US$9,750")
    expect(page.locator("#menu-development")).to_contain_text("tip-over trials")
    expect(page.locator("#menu-packet")).to_contain_text("US$9,750 uncommitted gap")
    for cash,gap in [("0","US$19,500"),("100","US$0")]:
        page.locator("#menu-cash").fill(cash)
        expect(page.locator("#menu-gap")).to_have_text(gap)
    page.locator("#menu-partitions").select_option("2")
    expect(page.locator("#menu-total")).to_have_text("US$22,500")
    expect(page.locator("#menu-components")).to_contain_text("3 partitions")
    audit(page,"Configured renovation menu")
    page.locator("#menu-use-economics").click()
    expect(page.locator("#package-price")).to_have_value("22500")
    expect(page.locator("#ledger-gross")).to_have_text("US$6,750 / 30%")
    page.locator(".menu-reset").click()
    expect(page.locator("#menu-total")).to_have_text("US$10,000")
    expect(page.locator("#menu-gap")).to_have_text("US$5,000")
    expect(page.locator("#menu-components")).to_have_text("8 Snap panels · 1 table · 0 partitions")
    assert "Partition:" not in page.locator("#menu-development").inner_text()
    page.locator("#package-price").fill("10000")
    passed("Three menu packages, modules, finish, 70/30 costs, owner-cash extremes, material requirements, reset and unit-model handoff")
    page.locator(".material-concept").scroll_into_view_if_needed()
    page.wait_for_function("document.querySelector('.material-concept img').naturalWidth === 1536")
    expect(page.locator(".material-concept")).to_contain_text("Material development concept")
    for title in ["Snap panel / EPS-core walls.","EPS-core tables.","EPS-core partitions."]:
        expect(page.locator("#delivery")).to_contain_text(title)
    page.locator(".material-engineering summary").click()
    expect(page.locator(".material-engineering")).to_have_attribute("open","")
    passed("Generated material concept, wall/table/partition specifications and engineering disclosure")

    for anchor in page.locator('a[href^="#"]').all():
        assert page.locator(anchor.get_attribute("href")).count() == 1
    passed("All chapter and navigation destinations exist")

    for space in ["studio", "residence", "commercial"]:
        tab = page.locator('[data-studio="'+space+'"]')
        tab.click()
        expect(tab).to_have_attribute("aria-selected", "true")
        expect(page.locator("#studio-capture")).to_have_attribute("src", "assets/studio/playground-"+space+".webp")
        assert page.locator("#studio-capture").evaluate("(img)=>img.complete && img.naturalWidth === 1440")
        audit(page, "Studio+ " + space)
    page.locator("#studio-tab-studio").focus()
    page.keyboard.press("ArrowRight")
    expect(page.locator("#studio-tab-residence")).to_be_focused()
    page.keyboard.press("End")
    expect(page.locator("#studio-tab-commercial")).to_be_focused()
    page.keyboard.press("Home")
    expect(page.locator("#studio-tab-studio")).to_be_focused()
    assert page.locator(".studio-evidence-header>a").get_attribute("href") == "https://www.sechahome.com/studio/playground.html"
    passed("Three real Studio+ captures, full-size links, live route and keyboard tabs")

    for volume, project, profit in [("1000","US$10M","US$3M"),("5500","US$55M","US$16.5M"),("10000","US$100M","US$30M")]:
        page.locator("#packages").fill(volume)
        expect(page.locator("#project-value")).to_have_text(project)
        expect(page.locator("#gross-profit")).to_have_text(profit)
    passed("Illustrative economics at minimum, intermediate and maximum volumes")

    page.locator(".header-contact").click()
    expect(page.locator("#contact-dialog")).to_be_visible()
    page.locator("#copy-email").click()
    expect(page.locator("#copy-status")).to_have_text("Email address copied to your clipboard.")
    assert page.evaluate("navigator.clipboard.readText()") == "jplovensa@sechahome.com"
    audit(page, "Investor enquiry")
    page.keyboard.press("Escape")
    expect(page.locator("#contact-dialog")).not_to_be_visible()
    expect(page.locator(".header-contact")).to_be_focused()
    page.locator(".founder-contact").click()
    expect(page.locator("#contact-dialog")).to_be_visible()
    page.locator(".dialog-close").click()
    passed("Investor enquiry, founder contact, clipboard and focus restoration")

    with page.expect_download() as info:
        page.locator(".memo-download").click()
    info.value.save_as(artifacts / "downloaded-memo.pdf")
    assert (artifacts / "downloaded-memo.pdf").read_bytes().startswith(b"%PDF")
    page.locator(".faq details").first.locator("summary").click()
    expect(page.locator(".faq details").first).to_have_attribute("open", "")
    passed("Real investment memo PDF download and FAQ expansion")

    for width in [320,390,600,768,1024,1440]:
        page.set_viewport_size({"width":width,"height":844})
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), width
    page.set_viewport_size({"width":390,"height":844})
    page.locator(".menu-toggle").click()
    expect(page.locator(".menu-toggle")).to_have_attribute("aria-expanded", "true")
    page.locator('#main-nav a[href="#market"]').click()
    expect(page.locator(".menu-toggle")).to_have_attribute("aria-expanded", "false")
    assert page.url.endswith("#market")
    audit(page, "Mobile memo")
    passed("Six responsive widths and mobile chapter navigation")
    page.evaluate("document.activeElement.blur(); window.scrollTo(0,0)")
    page.screenshot(path=str(artifacts / "mobile.png"), full_page=True)
    page.screenshot(path=str(artifacts / "mobile-cover.png"))
    page.set_viewport_size({"width":1440,"height":1000})
    page.screenshot(path=str(artifacts / "desktop.png"), full_page=True)
    page.screenshot(path=str(artifacts / "desktop-cover.png"))

    page.locator("[data-replay-opening]").click()
    expect(page.locator("#opening")).to_be_visible()
    page.wait_for_function("document.querySelector('#opening-video').currentTime > 0.2")
    assert page.evaluate("document.querySelector('#opening-video').muted")
    assert page.evaluate("document.querySelector('#opening-video').playsInline")
    page.locator("#opening-pause").click()
    assert page.evaluate("document.querySelector('#opening-video').paused")
    page.set_viewport_size({"width":390,"height":844})
    audit(page, "Paused opening film on mobile")
    assert page.evaluate("document.querySelector('#opening').scrollWidth <= innerWidth")
    page.screenshot(path=str(artifacts / "opening.png"))
    page.locator("#opening-pause").click()
    assert not page.evaluate("document.querySelector('#opening-video').paused")
    page.keyboard.press("Escape")
    expect(page.locator("#opening")).not_to_be_visible()
    expect(page.locator("[data-replay-opening]")).to_be_focused()
    passed("Manual video replay, real playback, pause/resume, Escape and focus restoration")
    assert not errors, errors
    assert not failed, failed
    assert not external, external
    passed("No JavaScript errors, failed assets or external runtime dependencies")
    context.close()

    # A fresh normal load must really play, then reveal the memo automatically.
    auto = browser.new_context(viewport={"width":1440,"height":1000})
    film = auto.new_page()
    film.goto(base, wait_until="domcontentloaded")
    expect(film.locator("#opening")).to_be_visible()
    film.wait_for_function("document.querySelector('#opening-video').currentTime > 0.2")
    assert film.evaluate("document.querySelector('#opening-progress').value > 0")
    assert 8.9 <= film.locator("#opening-video").evaluate("v=>v.duration") <= 9.1
    expect(film.locator("#opening-phase")).to_contain_text("IMAGINE")
    expect(film.locator("#opening-phase")).to_contain_text("CONFIGURE", timeout=5000)
    film.screenshot(path=str(artifacts / "opening-desktop.png"))
    expect(film.locator("#opening-phase")).to_contain_text("SCALE TO ASIA", timeout=5000)
    passed("Original nine-second interface film advances from concept to configuration to Asia")
    expect(film.locator("#opening")).not_to_be_visible(timeout=11000)
    expect(film.locator("body")).not_to_have_class("opening-active")
    passed("Automatic film playback, media-tied progress and end-to-memo transition")
    film.reload(wait_until="domcontentloaded")
    expect(film.locator("#opening")).to_be_visible()
    film.locator("#opening-skip").click()
    expect(film.locator("#opening")).not_to_be_visible()
    passed("Refresh starts opening; Skip immediately releases the memo")
    auto.close()

    def failure_case(name, init_script=None, block_media=False):
        ctx = browser.new_context()
        pg = ctx.new_page()
        if init_script:
            pg.add_init_script(init_script)
        if block_media:
            pg.route("**/assets/film/opening.mp4", lambda route: route.abort())
        pg.goto(base, wait_until="domcontentloaded")
        expect(pg.locator("#opening")).not_to_be_visible(timeout=4000)
        expect(pg.locator("#hero-title")).to_be_visible()
        assert not pg.evaluate("document.body.classList.contains('opening-active')")
        passed(name)
        ctx.close()

    failure_case("Blocked autoplay fails open",
                 "HTMLMediaElement.prototype.play = function(){return Promise.reject(new Error('blocked autoplay'))}")
    failure_case("Unavailable media fails open", block_media=True)
    failure_case("Stalled video startup releases memo within 2.5 seconds",
                 "HTMLMediaElement.prototype.play = function(){return new Promise(()=>{})}")
    failure_case("Save-Data preference bypasses automatic media",
                 "Object.defineProperty(navigator,'connection',{value:{saveData:true},configurable:true})")

    nojs = browser.new_context(java_script_enabled=False)
    pg = nojs.new_page()
    pg.goto(base)
    expect(pg.locator("#opening")).not_to_be_visible()
    expect(pg.locator("#manifesto-title")).to_be_visible()
    passed("No JavaScript leaves the memo readable and the opening hidden")
    nojs.close()
    browser.close()

(artifacts / "results.json").write_text(json.dumps({"passed":len(checks),"checks":checks},indent=2))
print(str(len(checks)) + " checks passed.", flush=True)
