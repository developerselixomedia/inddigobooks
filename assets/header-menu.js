// Header Megamenu Hover and Focus
document.querySelectorAll('.site-nav__item--has-dropdown').forEach(item => {
  item.addEventListener('mouseenter', () => item.classList.add('is-hovered'));
  item.addEventListener('mouseleave', () => item.classList.remove('is-hovered'));
});
