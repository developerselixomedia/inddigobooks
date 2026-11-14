// Bookshelf Interactive Hotspots
document.querySelectorAll('.hotspot-dot').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const popup = btn.nextElementSibling;
    if (popup) popup.classList.toggle('active');
  });
});
