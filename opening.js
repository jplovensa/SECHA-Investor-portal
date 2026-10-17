"use strict";

// A real, local video intro. Reading the memo never depends on media success.
(() => {
  const opening = document.getElementById("opening");
  const video = document.getElementById("opening-video");
  const skip = document.getElementById("opening-skip");
  const pause = document.getElementById("opening-pause");
  const progress = document.getElementById("opening-progress");
  const phase = document.getElementById("opening-phase");
  const time = document.getElementById("opening-time");
  const motion = matchMedia("(prefers-reduced-motion: reduce)");
  const replayButtons = document.querySelectorAll("[data-replay-opening]");
  let startupTimer;
  let maximumTimer;
  let automatic = false;
  let trigger = null;
  let closing = false;

  function clearTimers() {
    clearTimeout(startupTimer);
    clearTimeout(maximumTimer);
  }
  function clock(seconds) {
    return "00:" + String(Math.floor(seconds || 0)).padStart(2, "0");
  }
  function sync() {
    const duration =
      Number.isFinite(video.duration) && video.duration > 0
        ? video.duration
        : 8;
    const ratio = Math.min(video.currentTime / duration, 1);
    progress.value = ratio;
    time.textContent = clock(video.currentTime) + " / " + clock(duration);
    phase.textContent =
      ratio < 0.31
        ? "01 / FROM JAKARTA, INDONESIA"
        : ratio < 0.72
          ? "02 / MATERIALS TO FLATPACK"
          : "03 / THE INTERFACE FOR ASIA";
    pause.textContent = video.paused ? "Play film" : "Pause film";
    pause.setAttribute(
      "aria-label",
      video.paused ? "Play opening film" : "Pause opening film",
    );
  }
  function dismiss() {
    if (!opening.open || closing) return;
    closing = true;
    clearTimers();
    video.pause();
    opening.close();
    document.body.classList.remove("opening-active");
    if (trigger?.isConnected) trigger.focus({ preventScroll: true });
    closing = false;
  }
  function play() {
    try {
      const promise = video.play();
      promise?.catch(() => dismiss());
    } catch {
      dismiss();
    }
  }
  function begin(auto, button = null) {
    if (opening.open) return;
    automatic = auto;
    trigger = button;
    closing = false;
    progress.value = 0;
    video.muted = true;
    video.defaultMuted = true;
    video.playsInline = true;
    if (!video.getAttribute("src")) video.src = video.dataset.src;
    try {
      video.currentTime = 0;
    } catch {}
    opening.showModal();
    document.body.classList.add("opening-active");
    skip.focus({ preventScroll: true });
    sync();
    // A media stall or blocked autoplay must never gate the memo.
    startupTimer = setTimeout(dismiss, 2500);
    if (auto) maximumTimer = setTimeout(dismiss, 10500);
    play();
  }

  skip.addEventListener("click", dismiss);
  opening.addEventListener("cancel", (event) => {
    event.preventDefault();
    dismiss();
  });
  opening.addEventListener("close", () => {
    clearTimers();
    video.pause();
    document.body.classList.remove("opening-active");
  });
  video.addEventListener("playing", () => {
    clearTimeout(startupTimer);
    sync();
  });
  video.addEventListener("timeupdate", sync);
  video.addEventListener("pause", sync);
  video.addEventListener("ended", dismiss);
  video.addEventListener("error", dismiss);
  pause.addEventListener("click", () => {
    automatic = false;
    clearTimers();
    if (video.paused) play();
    else video.pause();
    sync();
  });
  replayButtons.forEach((button) =>
    button.addEventListener("click", () => begin(false, button)),
  );
  motion.addEventListener("change", (event) => {
    if (event.matches && automatic) dismiss();
  });
  document.addEventListener("visibilitychange", () => {
    if (!opening.open) return;
    if (document.hidden) {
      if (automatic) dismiss();
      else video.pause();
    }
  });
  const saveData = navigator.connection?.saveData === true;
  if (!motion.matches && !saveData) begin(true);
})();
