// Cart Drawer Controller
export class CartDrawer extends HTMLElement {
  connectedCallback() {
    this.overlay = document.getElementById('CartDrawerOverlay');
  }
  open() { this.classList.add('active'); if (this.overlay) this.overlay.classList.add('active'); }
  close() { this.classList.remove('active'); if (this.overlay) this.overlay.classList.remove('active'); }
}
if (!customElements.get('cart-drawer')) customElements.define('cart-drawer', CartDrawer);
