// Gift Card Recipient Form
document.addEventListener('change', (e) => {
  if (e.target.id === 'Recipient-Checkbox') {
    const fields = document.getElementById('RecipientFields');
    if (fields) fields.style.display = e.target.checked ? 'block' : 'none';
  }
});
