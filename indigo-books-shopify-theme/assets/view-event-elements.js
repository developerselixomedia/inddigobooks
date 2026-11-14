// View Event Tracker for Meta Ads & Google Analytics
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const eventName = el.dataset.viewEvent || 'ViewItem';
      if (typeof fbq === 'function' && el.dataset.productId) {
        fbq('track', 'ViewContent', {
          content_ids: [el.dataset.productId],
          content_type: 'product'
        });
      }
      observer.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-view-event]').forEach(el => observer.observe(el));
});
