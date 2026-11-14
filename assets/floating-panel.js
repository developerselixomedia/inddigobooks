// Floating Panel Controller
export class FloatingPanel extends HTMLElement {
  connectedCallback() {
    window.addEventListener('scroll', () => {
      this.classList.toggle('visible', window.scrollY > 300);
    }, { passive: true });
  }
}
if (!customElements.get('floating-panel')) customElements.define('floating-panel', FloatingPanel);
