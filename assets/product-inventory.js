// Real-Time Inventory Status
export function updateInventoryBadge(qty, el) {
  if (!el) return;
  if (qty > 5) el.innerText = 'In Stock';
  else if (qty > 0) el.innerText = `Only ${qty} left!`;
  else el.innerText = 'Out of Stock';
}
