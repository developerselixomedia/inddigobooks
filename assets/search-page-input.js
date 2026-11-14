// Search Page Input Auto-Focus
document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('.search-input-lg');
  if (input && !input.value) input.focus();
});
