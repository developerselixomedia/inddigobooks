// Horizontal Scroll Container
export class ScrollContainer extends HTMLElement {
  scrollBy(amount) { this.scrollLeft += amount; }
}
if (!customElements.get('scroll-container')) customElements.define('scroll-container', ScrollContainer);
