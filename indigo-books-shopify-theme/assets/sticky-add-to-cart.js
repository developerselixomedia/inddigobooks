// Mobile Sticky Buy & WhatsApp Bar
window.addEventListener('scroll', () => {
  const bar = document.getElementById('StickyMobileBar');
  const mainBtn = document.getElementById('AddToCartBtn');
  if (!bar || !mainBtn) return;
  const rect = mainBtn.getBoundingClientRect();
  bar.style.display = rect.bottom < 0 ? 'flex' : 'none';
}, { passive: true });
