/**
 * Indigo Books - WhatsApp Commerce & Automation JavaScript
 */

(function () {
  document.addEventListener('DOMContentLoaded', function () {
    initWhatsAppCartCheckout();
    initWhatsAppFloatingWidget();
    initWhatsAppTracking();
  });

  /* WhatsApp Cart Checkout - Generates Instant Order Summary */
  function initWhatsAppCartCheckout() {
    document.addEventListener('click', function (e) {
      const btn = e.target.closest('#whatsappCartCheckoutBtn');
      if (!btn) return;

      e.preventDefault();
      const phone = btn.dataset.phone || window.ShopifyTheme.whatsappNumber || '918933063306';
      const shopName = btn.dataset.shop || 'Indigo Books India';

      // Fetch current cart contents
      fetch('/cart.js')
        .then(res => res.json())
        .then(cart => {
          if (!cart.items || cart.items.length === 0) {
            alert('Your reading cart is empty!');
            return;
          }

          let message = `*Hello ${shopName}! *\nI would like to place an order for the following books:\n\n`;

          cart.items.forEach((item, index) => {
            const format = item.variant_title ? ` (${item.variant_title})` : '';
            message += `${index + 1}. *${item.product_title}*${format}\n`;
            message += `   Qty: ${item.quantity} | Price: ${(item.line_price / 100).toFixed(2)}\n`;
          });

          const totalFormatted = (cart.total_price / 100).toFixed(2);
          message += `\n*Total Order Amount:* ${cart.currency} ${totalFormatted}\n`;
          message += `\nPlease confirm book availability and share Payment / Cash on Delivery (COD) details.`;

          // Track Meta Conversion
          if (typeof fbq === 'function') {
            fbq('trackCustom', 'WhatsAppCartCheckout', {
              value: totalFormatted,
              currency: cart.currency,
              num_items: cart.item_count
            });
          }

          // Open WhatsApp
          const whatsappUrl = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
          window.open(whatsappUrl, '_blank');
        })
        .catch(err => {
          console.error('Error fetching cart for WhatsApp order:', err);
        });
    });
  }

  /* Floating WhatsApp Notification Widget Timer */
  function initWhatsAppFloatingWidget() {
    const tooltip = document.getElementById('whatsappFloatingTooltip');
    if (!tooltip) return;

    // Show tooltip after 6 seconds of browsing if user hasn't closed it
    setTimeout(() => {
      tooltip.style.opacity = '1';
      tooltip.style.transform = 'translateY(0)';
    }, 6000);
  }

  /* Meta Ads Tracking for WhatsApp actions */
  function initWhatsAppTracking() {
    document.addEventListener('click', function (e) {
      const waLink = e.target.closest('[data-whatsapp-track]');
      if (!waLink) return;

      const trackSource = waLink.dataset.whatsappTrack;
      const bookTitle = waLink.dataset.bookTitle || 'General Catalog';
      const bookPrice = waLink.dataset.bookPrice || '0';

      if (typeof fbq === 'function') {
        fbq('trackCustom', 'WhatsAppLead', {
          source: trackSource,
          book_title: bookTitle,
          value: bookPrice,
          currency: 'INR'
        });
      }
    });
  }
})();

