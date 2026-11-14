// Cart Qty Selector
class CartQuantitySelector extends HTMLElement {
  connectedCallback() {
    this.input = this.querySelector('input');
    this.querySelector('[data-decrease]')?.addEventListener('click', () => this.update(-1));
    this.querySelector('[data-increase]')?.addEventListener('click', () => this.update(1));
  }
  update(change) {
    if (!this.input) return;
    const val = Math.max(0, parseInt(this.input.value || 0) + change);
    this.input.value = val;
    this.input.dispatchEvent(new Event('change', { bubbles: true }));
  }
}
if (!customElements.get('cart-quantity-selector')) customElements.define('cart-quantity-selector', CartQuantitySelector);
