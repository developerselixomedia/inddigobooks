// Tiered Price Per Item Calculator
export function calculateTierPrice(qty, basePrice, tiers = []) {
  for (const t of tiers) {
    if (qty >= t.min_quantity) return t.price;
  }
  return basePrice;
}
