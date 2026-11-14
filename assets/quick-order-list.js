// Quick Order List Multi-Item Calculator
export function recalculateQuickOrder() {
  let count = 0;
  document.querySelectorAll('.bulk-qty-field').forEach(input => count += (parseInt(input.value) || 0));
  const el = document.getElementById('QuickOrderTotalCount');
  if (el) el.innerText = count;
}
