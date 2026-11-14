// Results List Component
class ResultsList extends HTMLElement {
  connectedCallback() {
    // Manages results list
  }
}
if (!customElements.get('results-list')) customElements.define('results-list', ResultsList);
