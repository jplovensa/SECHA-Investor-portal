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

const studioViews = {
  studio: {
    image: "assets/studio/playground-studio.webp",
    alt: "Studio+ playground: 48 square metre studio apartment with editable 3D furniture, material controls and an illustrative budget",
    description:
      "48 m² studio · editable furniture · moodboards & finishes · concept budget",
  },
  residence: {
    image: "assets/studio/playground-residence.webp",
    alt: "Studio+ playground: residence with a room divider, living and bedroom furniture, floor controls and an illustrative budget",
    description:
      "Residence · room planning · floor controls · material directions",
  },
  commercial: {
    image: "assets/studio/playground-commercial.webp",
    alt: "Studio+ playground: Café Sol commercial layout with café counters, dining tables, furniture schedule and an illustrative budget",
    description:
      "Café Sol · commercial layout · furniture schedule · concept budget",
  },
};
const studioTabs = [...document.querySelectorAll("[data-studio]")];
function selectStudio(tab) {
  const view = studioViews[tab.dataset.studio];
  studioTabs.forEach((item) => {
    const selected = item === tab;
    item.setAttribute("aria-selected", String(selected));
    item.tabIndex = selected ? 0 : -1;
  });
  const image = document.getElementById("studio-capture");
  image.src = view.image;
  image.alt = view.alt;
  const link = document.getElementById("studio-capture-link");
  link.href = view.image;
  link.setAttribute(
    "aria-label",
    "View full-size " +
      tab.textContent.trim().replace(/^0[123]\s*/, "") +
      " source capture",
  );
  document.getElementById("studio-capture-description").textContent =
    view.description;
  document
    .getElementById("studio-capture-panel")
    .setAttribute("aria-labelledby", tab.id);
}
studioTabs.forEach((tab, index) => {
  tab.addEventListener("click", () => selectStudio(tab));
  tab.addEventListener("keydown", (event) => {
    let next;
    if (event.key === "ArrowRight")
      next = studioTabs[(index + 1) % studioTabs.length];
    if (event.key === "ArrowLeft")
      next = studioTabs[(index + studioTabs.length - 1) % studioTabs.length];
    if (event.key === "Home") next = studioTabs[0];
    if (event.key === "End") next = studioTabs.at(-1);
    if (next) {
      event.preventDefault();
      selectStudio(next);
      next.focus();
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

// Underwriting sensitivities. These values are assumptions, not reported costs.
const unitInputs = ["cac", "support", "fixed-opex", "deposit"].map((id) =>
  document.getElementById(id),
);
const usd = (value) =>
  new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  })
    .format(value)
    .replace("$", "US$");
function modelValue(id, maximum) {
  const value = document.getElementById(id).valueAsNumber;
  return Number.isFinite(value) ? Math.min(maximum, Math.max(0, value)) : 0;
}
function updateContribution() {
  const cac = modelValue("cac", 5000);
  const support = modelValue("support", 5000);
  const fixed = modelValue("fixed-opex", 1000000);
  const deposit = modelValue("deposit", 100);
  const contribution = 1500 - cac - support;
  const cashGap = Math.max(3500 - (5000 * deposit) / 100, 0);
  const contributionOutput = document.getElementById("contribution");
  contributionOutput.textContent = usd(contribution);
  contributionOutput.classList.toggle("negative", contribution <= 0);
  document.getElementById("contribution-margin").textContent =
    ((contribution / 5000) * 100).toFixed(1) + "% of package value";
  document.getElementById("break-even").textContent =
    contribution > 0
      ? Math.ceil(fixed / contribution).toLocaleString("en-US") +
        " jobs / month"
      : "Not reached";
  document.getElementById("break-even-note").textContent =
    contribution > 0
      ? "Before tax, financing and exceptional costs"
      : "Positive contribution is required before fixed-cost break-even";
  document.getElementById("cash-gap").textContent = usd(cashGap);
  document.getElementById("concurrent-gap").textContent = usd(cashGap * 10);
}
unitInputs.forEach((input) =>
  input.addEventListener("input", updateContribution),
);
updateContribution();
