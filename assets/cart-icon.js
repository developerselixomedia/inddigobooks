// Cart Icon Counter Update
window.addEventListener('cart:updated', (e) => {
  const count = e.detail?.item_count ?? 0;
  document.querySelectorAll('.cart-badge-count').forEach(el => el.innerText = count);
});
