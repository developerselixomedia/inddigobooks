// Currency & Country Localization Form
document.querySelectorAll('form[action*="/localization"]').forEach(form => {
  form.addEventListener('change', () => form.submit());
});
