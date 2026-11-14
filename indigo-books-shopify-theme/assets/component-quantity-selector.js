// Product Page Quantity Selector
class QuantitySelector extends HTMLElement {
  connectedCallback() {
    const input = this.querySelector('input');
    this.querySelector('[data-qty-decrease]')?.addEventListener('click', () => {
      if (input) input.value = Math.max(1, parseInt(input.value || 1) - 1);
    });
    this.querySelector('[data-qty-increase]')?.addEventListener('click', () => {
      if (input) input.value = parseInt(input.value || 1) + 1;
    });
  }
}
if (!customElements.get('quantity-selector')) customElements.define('quantity-selector', QuantitySelector);
