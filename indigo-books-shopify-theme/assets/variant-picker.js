// Variant Picker (Format, Edition, Binding)
export class VariantPicker extends HTMLElement {
  connectedCallback() {
    this.addEventListener('change', this.onVariantChange.bind(this));
  }

  onVariantChange(e) {
    const radio = e.target.closest('input[type="radio"]');
    if (!radio) return;

    const variantId = radio.value;
    const price = radio.dataset.price;
    const available = radio.dataset.available === 'true';

    // Update hidden input in product form
    const formInput = document.getElementById('SelectedVariantId');
    if (formInput) formInput.value = variantId;

    // Update price display
    const priceEl = document.querySelector('.product-pdp-price .price-item--current');
    if (priceEl && price) priceEl.innerText = price;

    // Update Add to Cart button state
    const addBtn = document.getElementById('AddToCartBtn');
    if (addBtn) {
      addBtn.disabled = !available;
      addBtn.innerText = available ? 'Add to Reading Cart' : 'Out of Stock';
    }

    // Fire variant change event for Meta tracking and WhatsApp updates
    window.dispatchEvent(new CustomEvent('variant:changed', {
      detail: { variantId, price, available }
    }));
  }
}
if (!customElements.get('variant-picker')) customElements.define('variant-picker', VariantPicker);
