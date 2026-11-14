// Responsive Media Helper
export function initMedia(container = document) {
  container.querySelectorAll('video[autoplay]').forEach(v => v.play().catch(() => {}));
}
