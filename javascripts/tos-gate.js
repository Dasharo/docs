function revealGated(cb) {
  const el = document.getElementById(cb.dataset.section);
  const proseEls = cb.dataset.proseSection
    ? document.querySelectorAll(`[data-prose-group="${cb.dataset.proseSection}"]`)
    : [];

  if (!cb.checked) {
    el.innerHTML = "";
    proseEls.forEach(p => { p.style.display = "none"; });
    return;
  }

  const files = JSON.parse(atob(el.dataset.payload));
  // rel="noreferrer" is intentionally absent — it would strip the Referer
  // header and break the MinIO bucket policy gate
  el.innerHTML = files.map(f => {
    if (f.group) {
      const btns = f.items.map(item =>
        `<a href="${item.url}" class="md-button">${item.label}</a>`
      ).join(" ");
      const note = f.note ? ` <span>${f.note}</span>` : "";
      return `<h4>${f.group}</h4><p>${btns}${note}</p>`;
    }
    return `<a href="${f.url}" class="md-button">${f.label}</a>`;
  }).join("\n");

  proseEls.forEach(p => { p.style.display = ""; });
}
