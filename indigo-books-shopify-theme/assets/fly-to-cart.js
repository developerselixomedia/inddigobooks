// Fly to Cart Animation
export function flyToCart(imgEl) {
  const cartIcon = document.querySelector('.header-action-btn--cart');
  if (!imgEl || !cartIcon) return;
  const clone = imgEl.cloneNode(true);
  const rect = imgEl.getBoundingClientRect();
  clone.style.cssText = `position:fixed;top:${rect.top}px;left:${rect.left}px;width:${rect.width}px;height:${rect.height}px;z-index:9999;transition:all 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);pointer-events:none;`;
  document.body.appendChild(clone);
  const target = cartIcon.getBoundingClientRect();
  requestAnimationFrame(() => {
    clone.style.top = `${target.top}px`;
    clone.style.left = `${target.left}px`;
    clone.style.width = '20px';
    clone.style.height = '20px';
    clone.style.opacity = '0';
  });
  setTimeout(() => clone.remove(), 600);
}
