// Smooth Scroll Utility
export function smoothScrollTo(element, offset = 80) {
  const top = element.getBoundingClientRect().top + window.pageYOffset - offset;
  window.scrollTo({ top, behavior: 'smooth' });
}
