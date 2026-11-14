// Local Store Pickup Inspector
export function checkLocalPickup(variantId) {
  return fetch(`/variants/${variantId}/?section_id=pickup-availability`).then(r => r.text());
}
