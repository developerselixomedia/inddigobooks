// Modal Dialog
export class ModalDialog extends HTMLElement {
  connectedCallback() {
    this.querySelector('[data-close-dialog]')?.addEventListener('click', () => this.close());
  }
  open() { this.setAttribute('open', ''); }
  close() { this.removeAttribute('open'); }
}
if (!customElements.get('modal-dialog')) customElements.define('modal-dialog', ModalDialog);
