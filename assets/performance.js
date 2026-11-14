// Performance Optimizations
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img[loading="lazy"]').forEach(img => {
    if (img.dataset.src) img.src = img.dataset.src;
  });
}
