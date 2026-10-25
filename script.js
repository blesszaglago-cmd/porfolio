(() => {
  "use strict";
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");
  const preference = window.matchMedia("(prefers-color-scheme: dark)");
  let stored;
  try {
    stored =
      localStorage.getItem("portfolio-theme") || localStorage.getItem("theme");
  } catch {
    /* Storage may be disabled. */
  }
  if (stored !== "light" && stored !== "dark") stored = undefined;
  const applyTheme = (dark) => {
    root.dataset.theme = dark ? "dark" : "light";
    toggle?.setAttribute("aria-pressed", String(dark));
    toggle?.setAttribute(
      "aria-label",
      "Switch to " + (dark ? "light" : "dark") + " theme",
    );
    document
      .querySelector('meta[name="theme-color"]')
      ?.setAttribute("content", dark ? "#101c1c" : "#f5f8f5");
  };
  applyTheme(stored === "dark" || (stored !== "light" && preference.matches));
  toggle?.addEventListener("click", () => {
    const dark = root.dataset.theme !== "dark";
    stored = dark ? "dark" : "light";
    applyTheme(dark);
    try {
      localStorage.setItem("portfolio-theme", stored);
    } catch {
      /* Keep this page usable. */
    }
  });
  preference.addEventListener?.("change", (event) => {
    if (!stored) applyTheme(event.matches);
  });
  const filters = Array.from(document.querySelectorAll("[data-filter]"));
  const projects = Array.from(document.querySelectorAll("[data-project]"));
  const status = document.getElementById("filter-status");
  filters.forEach((button) =>
    button.addEventListener("click", () => {
      const filter = button.dataset.filter;
      let count = 0;
      projects.forEach((project) => {
        project.hidden = filter !== "all" && project.dataset.project !== filter;
        if (!project.hidden) count += 1;
      });
      filters.forEach((control) =>
        control.setAttribute("aria-pressed", String(control === button)),
      );
      if (status)
        status.textContent =
          "Showing " +
          count +
          " " +
          (filter === "ml"
            ? "machine learning"
            : filter === "software"
              ? "software"
              : "featured") +
          " projects.";
    }),
  );
  // Native anchors and every section remain usable without JavaScript.
})();
