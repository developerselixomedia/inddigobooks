// Book Cover Zoom Dialog
export class ZoomDialog extends HTMLElement {
  connectedCallback() {
    this.img = this.querySelector('img');
    this.querySelector('.close-zoom')?.addEventListener('click', () => this.close());
  }
  open(src) {
    if (this.img) this.img.src = src;
    this.classList.add('is-open');
  }
  close() {
    this.classList.remove('is-open');
  }
}
if (!customElements.get('zoom-dialog')) customElements.define('zoom-dialog', ZoomDialog);
