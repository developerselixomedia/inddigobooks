// Cart Discount Handler
export function applyCartDiscount(code) {
  return fetch(`/discount/${encodeURIComponent(code)}`);
}
