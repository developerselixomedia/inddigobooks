// Auto Close Details
document.addEventListener('click', (e) => {
  document.querySelectorAll('details[data-auto-close]').forEach(det => {
    if (det.open && !det.contains(e.target)) det.removeAttribute('open');
  });
});
