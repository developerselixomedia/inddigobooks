/**
 * Indigo Books - Meta Ads & Conversions API Frontend Tracking
 */

window.IndigoTracking = {
  trackAddToCart: function(item) {
    if (typeof fbq === 'function') {
      fbq('track', 'AddToCart', {
        content_name: item.title,
        content_ids: [item.variant_id || item.id],
        content_type: 'product',
        value: (item.price / 100),
        currency: (item.currency || 'INR')
      });
    }
  },

  trackInitiateCheckout: function(totalValue, currency, numItems) {
    if (typeof fbq === 'function') {
      fbq('track', 'InitiateCheckout', {
        value: totalValue,
        currency: currency,
        num_items: numItems
      });
    }
  }
};

document.addEventListener('DOMContentLoaded', function() {
  // Track InitiateCheckout on checkout button click
  document.querySelectorAll('a[href="/checkout"], button[name="checkout"], #CartDrawerCheckoutBtn').forEach(btn => {
    btn.addEventListener('click', function() {
      if (typeof fbq === 'function') {
        fbq('track', 'InitiateCheckout');
      }
    });
  });
});

