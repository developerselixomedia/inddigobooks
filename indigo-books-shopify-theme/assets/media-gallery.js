// Media Gallery for PDP
class MediaGallery extends HTMLElement {
  connectedCallback() {
    this.querySelectorAll('.thumb-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const main = this.querySelector('.product-main-cover');
        if (main && btn.dataset.fullSrc) main.src = btn.dataset.fullSrc;
      });
    });
  }
}
if (!customElements.get('media-gallery')) customElements.define('media-gallery', MediaGallery);
