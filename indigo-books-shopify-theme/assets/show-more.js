// Show More / Show Less Collapsible Text
document.querySelectorAll('[data-show-more-btn]').forEach(btn => {
  btn.addEventListener('click', () => {
    const target = document.getElementById(btn.dataset.target);
    if (!target) return;
    target.classList.toggle('is-expanded');
    btn.innerText = target.classList.contains('is-expanded') ? 'Show Less' : 'Read More';
  });
});
