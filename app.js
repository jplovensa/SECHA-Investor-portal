"use strict";

const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#main-nav");
function closeMenu() {
  menuToggle.setAttribute("aria-expanded", "false");
  navigation.classList.remove("open");
  menuToggle.textContent = "Menu";
}
menuToggle.addEventListener("click", () => {
  const open = menuToggle.getAttribute("aria-expanded") !== "true";
  menuToggle.setAttribute("aria-expanded", String(open));
  navigation.classList.toggle("open", open);
  menuToggle.textContent = open ? "Close" : "Menu";
});
navigation
  .querySelectorAll("a")
  .forEach((link) => link.addEventListener("click", closeMenu));
document.addEventListener("keydown", (event) => {
  if (
    event.key === "Escape" &&
    menuToggle.getAttribute("aria-expanded") === "true"
  ) {
    closeMenu();
    menuToggle.focus();
  }
});
matchMedia("(min-width: 601px)").addEventListener("change", (event) => {
  if (event.matches) closeMenu();
});

const links = [...navigation.querySelectorAll("a")];
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        links.forEach((link) => {
          if (link.hash === "#" + entry.target.id)
            link.setAttribute("aria-current", "location");
          else link.removeAttribute("aria-current");
        });
      }
    }
  },
  { rootMargin: "-15% 0px -55% 0px", threshold: 0 },
);
links.forEach((link) => observer.observe(document.querySelector(link.hash)));

const journey = {
  choose: {
    eyebrow: "A MENU, NOT A BLANK CANVAS",
    title: "The scope is clear.<br>The choice is yours.",
    description:
      "Customers select a package with a visible outcome, price and timeline. Standard choices make demand easier to fulfil.",
    points: [
      "Defined package inclusions",
      "Transparent pricing and timelines",
      "One consistent customer experience",
    ],
    media:
      '<img src="assets/package-interface.jpg" alt="SECHA package selection interface showing Essential, Plus and Signature packages" width="1257" height="618">',
  },
  personalise: {
    eyebrow: "CURATED CHOICES. CONTROLLED SCOPE.",
    title: "Make it personal.<br>Keep it repeatable.",
    description:
      "Customers choose finishes and GX-100 modules within a defined package. The price and timeline stay visible as choices are made.",
    points: [
      "Curated finish palettes",
      "Visible package inclusions",
      "Choices feed the controlled job file",
    ],
    media:
      '<img src="assets/personalisation-interface.jpg" alt="SECHA personalisation interface with a room preview, finish palette and package summary" width="1920" height="1080">',
  },
  finance: {
    eyebrow: "AFFORDABILITY INSIDE THE FLOW",
    title: "A clearer path<br>from intent to yes.",
    description:
      "Financing supports package affordability and conversion. Renovation delivery remains the core of the business model.",
    points: [
      "Package cost stays visible",
      "Down payment and term inform affordability",
      "Final terms depend on lender approval",
    ],
    media:
      '<div class="finance-preview"><span class="eyebrow">FINANCING / CUSTOMER FLOW</span><h4>Understand the commitment.</h4><div class="finance-step"><span>01</span> Choose a renovation package</div><div class="finance-step"><span>02</span> Explore down payment and term</div><div class="finance-step"><span>03</span> Confirm terms with lending partners</div><p>More accessible packages. The same controlled delivery.</p><small>Product concept. No credit application or financing offer is made on this investor website.</small></div>',
  },
  track: {
    eyebrow: "ONE JOB FILE. VISIBLE ACCOUNTABILITY.",
    title: "From a customer choice<br>to delivery proof.",
    description:
      "The package becomes a controlled job file: materials, supplier allocation and installer sequence, connected to milestones and quality evidence.",
    points: [
      "Milestone visibility",
      "Quality proof tied to the job",
      "Margin control through delivery",
    ],
    media:
      '<div class="job-file"><div class="card-heading mono"><span>JOB FILE / DELIVERY MODEL</span><span>CONCEPT</span></div><h4>The package becomes the plan.</h4><div class="job-file-row"><span>Scope</span><strong>Package-defined</strong></div><div class="job-file-row"><span>Materials</span><strong>Bill of materials</strong></div><div class="job-file-row"><span>Fulfilment</span><strong>Supplier + installer sequence</strong></div><div class="job-file-row"><span>Delivery</span><strong>Milestones + quality proof</strong></div></div>',
  },
};
const tabs = [...document.querySelectorAll("[data-step]")];
function selectStep(tab) {
  const step = journey[tab.dataset.step];
  tabs.forEach((item) => {
    const selected = item === tab;
    item.setAttribute("aria-selected", String(selected));
    item.tabIndex = selected ? 0 : -1;
  });
  document
    .getElementById("journey-panel")
    .setAttribute("aria-labelledby", tab.id);
  document.getElementById("journey-eyebrow").textContent = step.eyebrow;
  document.getElementById("journey-title").innerHTML = step.title;
  document.getElementById("journey-description").textContent = step.description;
  const points = document.getElementById("journey-points");
  points.replaceChildren(
    ...step.points.map((text) => {
      const item = document.createElement("li");
      item.textContent = text;
      return item;
    }),
  );
  document.getElementById("journey-media").innerHTML = step.media;
}
tabs.forEach((tab, index) => {
  tab.addEventListener("click", () => selectStep(tab));
  tab.addEventListener("keydown", (event) => {
    let target;
    if (event.key === "ArrowRight") target = tabs[(index + 1) % tabs.length];
    if (event.key === "ArrowLeft")
      target = tabs[(index + tabs.length - 1) % tabs.length];
    if (event.key === "Home") target = tabs[0];
    if (event.key === "End") target = tabs[tabs.length - 1];
    if (target) {
      event.preventDefault();
      selectStep(target);
      target.focus();
    }
  });
});

const packages = document.getElementById("packages");
const formatMillions = (value) =>
  "US$" +
  new Intl.NumberFormat("en-US", { maximumFractionDigits: 2 }).format(
    value / 1e6,
  ) +
  "M";
function updateScale() {
  const count = Number(packages.value);
  document.getElementById("package-count").textContent =
    count.toLocaleString("en-US");
  document.getElementById("project-value").textContent = formatMillions(
    count * 5000,
  );
  document.getElementById("gross-profit").textContent = formatMillions(
    count * 1500,
  );
}
packages.addEventListener("input", updateScale);
updateScale();

const dialog = document.getElementById("contact-dialog");
document.querySelectorAll("[data-contact]").forEach((button) =>
  button.addEventListener("click", () => {
    document.getElementById("copy-status").textContent = "";
    document.getElementById("copy-email").textContent = "Copy address";
    dialog.showModal();
  }),
);
dialog
  .querySelector(".dialog-close")
  .addEventListener("click", () => dialog.close());
dialog.addEventListener("click", (event) => {
  const bounds = dialog.getBoundingClientRect();
  if (
    event.target === dialog &&
    (event.clientX < bounds.left ||
      event.clientX > bounds.right ||
      event.clientY < bounds.top ||
      event.clientY > bounds.bottom)
  )
    dialog.close();
});
document
  .getElementById("copy-email")
  .addEventListener("click", async (event) => {
    try {
      await navigator.clipboard.writeText("jplovensa@sechahome.com");
      event.target.textContent = "Copied";
      document.getElementById("copy-status").textContent =
        "Email address copied to your clipboard.";
    } catch {
      document.getElementById("copy-status").textContent =
        "Copy is unavailable. Select the email address above to copy it, or use Open email.";
    }
  });
