// Recommendations Dynamic Fetcher
export class ProductRecommendations extends HTMLElement {
  connectedCallback() {
    const url = this.dataset.url;
    if (url) fetch(url).then(r => r.text()).then(html => this.innerHTML = html);
  }
}
if (!customElements.get('product-recommendations')) customElements.define('product-recommendations', ProductRecommendations);
