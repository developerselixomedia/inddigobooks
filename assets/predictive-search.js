// Predictive Search Controller
export class PredictiveSearch extends HTMLElement {
  connectedCallback() {
    this.input = this.querySelector('input[type="search"]');
  }
}
if (!customElements.get('predictive-search')) customElements.define('predictive-search', PredictiveSearch);
