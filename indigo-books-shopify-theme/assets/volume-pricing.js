// Volume Pricing Tier Calculation (Bulk Bookstore orders)
export function calculateBulkDiscount(quantity, unitPrice, discountTiers = [
  { minQty: 5, discountPercent: 10 },
  { minQty: 10, discountPercent: 15 },
  { minQty: 25, discountPercent: 20 }
]) {
  let appliedDiscount = 0;
  for (const tier of discountTiers) {
    if (quantity >= tier.minQty) {
      appliedDiscount = tier.discountPercent;
    }
  }
  const discountedUnitPrice = unitPrice * (1 - (appliedDiscount / 100));
  return {
    discountPercent: appliedDiscount,
    unitPrice: discountedUnitPrice,
    total: discountedUnitPrice * quantity
  };
}
