// Drag Zoom for Book Covers
export class DragZoomWrapper extends HTMLElement {
  connectedCallback() {
    const img = this.querySelector('img');
    this.addEventListener('mousemove', (e) => {
      if (!img) return;
      const rect = this.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width * 100;
      const y = (e.clientY - rect.top) / rect.height * 100;
      img.style.transformOrigin = `${x}% ${y}%`;
    });
  }
}
if (!customElements.get('drag-zoom-wrapper')) customElements.define('drag-zoom-wrapper', DragZoomWrapper);
