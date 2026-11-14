// Faceted Search & Filtering for 2000+ Books
document.addEventListener('change', (e) => {
  const form = e.target.closest('#FacetFiltersForm');
  if (!form) return;
  const formData = new FormData(form);
  const searchParams = new URLSearchParams(formData).toString();
  const url = `${window.location.pathname}?${searchParams}`;
  window.history.pushState({}, '', url);

  fetch(url)
    .then(r => r.text())
    .then(html => {
      const doc = new DOMParser().parseFromString(html, 'text/html');
      const newGrid = doc.getElementById('ProductGrid');
      const curGrid = document.getElementById('ProductGrid');
      if (newGrid && curGrid) curGrid.innerHTML = newGrid.innerHTML;
    });
});
