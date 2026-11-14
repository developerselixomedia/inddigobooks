// Jumbo Text Responsive Scaler
class JumboText extends HTMLElement {
  connectedCallback() {
    this.style.fontSize = 'clamp(2rem, 5vw, 5rem)';
  }
}
if (!customElements.get('jumbo-text')) customElements.define('jumbo-text', JumboText);
