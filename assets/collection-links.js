// Collection Links Scrolling
document.querySelectorAll('.collection-pills-scroll').forEach(el => {
  el.addEventListener('wheel', (evt) => {
    if (evt.deltaY !== 0) { evt.preventDefault(); el.scrollLeft += evt.deltaY; }
  }, { passive: false });
});
