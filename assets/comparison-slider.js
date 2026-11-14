// Comparison Slider
class ComparisonSlider extends HTMLElement {
  connectedCallback() {
    const range = this.querySelector('input[type="range"]');
    if (range) range.addEventListener('input', (e) => this.style.setProperty('--pos', e.target.value + '%'));
  }
}
if (!customElements.get('comparison-slider')) customElements.define('comparison-slider', ComparisonSlider);
