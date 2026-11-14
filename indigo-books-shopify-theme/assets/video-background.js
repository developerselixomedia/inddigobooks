// Background Video Autoplay Helper
class VideoBackground extends HTMLElement {
  connectedCallback() {
    const video = this.querySelector('video');
    if (video) {
      video.muted = true;
      video.play().catch(() => {});
    }
  }
}
if (!customElements.get('video-background')) customElements.define('video-background', VideoBackground);
