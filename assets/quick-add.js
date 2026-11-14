// Quick Add Modal & Trigger
export function openQuickAdd(productId) {
  fetch(`/products/${productId}?view=quick-add`).then(r => r.text()).then(html => {
    // Open modal
  });
}
