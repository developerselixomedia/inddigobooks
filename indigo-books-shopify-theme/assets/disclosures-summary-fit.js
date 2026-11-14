// Disclosures Summary Fit
document.querySelectorAll('details.disclosure').forEach(d => {
  d.addEventListener('toggle', () => d.classList.toggle('is-open', d.open));
});
