// Product Form Handler
document.addEventListener('submit', (e) => {
  const form = e.target.closest('#ProductPdpForm');
  if (!form) return;
  e.preventDefault();
  const formData = new FormData(form);
  fetch('/cart/add.js', { method: 'POST', body: formData })
    .then(r => r.json())
    .then(item => {
      document.getElementById('CartDrawer')?.classList.add('active');
      document.getElementById('CartDrawerOverlay')?.classList.add('active');
    });
});
