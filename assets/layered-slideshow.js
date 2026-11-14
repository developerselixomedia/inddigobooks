// Layered Slideshow Controller
export class LayeredSlideshow extends HTMLElement {
  connectedCallback() {
    this.slides = this.querySelectorAll('.layered-slide');
    this.current = 0;
  }
}
if (!customElements.get('layered-slideshow')) customElements.define('layered-slideshow', LayeredSlideshow);
