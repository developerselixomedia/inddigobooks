// Product SKU & ISBN Updater
export function updateSku(sku, el) {
  if (el) el.innerText = sku || 'N/A';
}
