// Variant Resolution Helper
export function resolveVariantFromOptions(product, selectedOptions = []) {
  if (!product || !product.variants) return null;
  return product.variants.find(variant => {
    return selectedOptions.every((opt, index) => variant.options[index] === opt);
  });
}
