// Live Product Price Updates
export function updatePrice(variant, container) {
  if (!variant || !container) return;
  const cur = container.querySelector('.price-item--current');
  if (cur) cur.innerText = variant.price;
}
