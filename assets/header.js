// Sticky Header Scroll Behavior
let lastScroll = 0;
window.addEventListener('scroll', () => {
  const current = window.scrollY;
  const header = document.querySelector('.site-header');
  if (!header) return;
  if (current > 100 && current > lastScroll) {
    header.classList.add('site-header--hidden');
  } else {
    header.classList.remove('site-header--hidden');
  }
  lastScroll = current;
}, { passive: true });
