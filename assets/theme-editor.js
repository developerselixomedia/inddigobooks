// Shopify Theme Customizer Events Listener
document.addEventListener('shopify:section:load', (e) => {
  console.log('Section reloaded:', e.detail.sectionId);
});
