// Cart Items Component
class ComponentCartItems extends HTMLElement {
  connectedCallback() {
    this.addEventListener('change', (e) => {
      const line = e.target.dataset.line;
      const qty = e.target.value;
      if (line && qty !== undefined) {
        fetch('/cart/change.js', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ line: parseInt(line), quantity: parseInt(qty) })
        }).then(r => r.json()).then(cart => {
          window.dispatchEvent(new CustomEvent('cart:updated', { detail: cart }));
        });
      }
    });
  }
}
if (!customElements.get('component-cart-items')) customElements.define('component-cart-items', ComponentCartItems);
