// Slideshow Auto-Play & Navigation
class ThemeSlideshow extends HTMLElement {
  connectedCallback() {
    this.slides = this.querySelectorAll('.slideshow-slide');
  }
}
if (!customElements.get('theme-slideshow')) customElements.define('theme-slideshow', ThemeSlideshow);
