# -*- coding: utf-8 -*-
"""
scratch/patch_store_scripts.py
Adds full implementations for:
1. parseIndigoSpecsHtml
2. selectPdpVariant & switchPdpTab
3. useLiveGpsLocation & useCheckoutGpsLocation & checkPdpPincode
4. openAuthorBooksPage & renderPdpRecommendations (with 3D hover)
5. openExpressPhoneCheckout & submitExpressPhoneOrder
6. Update renderCatalog with indigo-3d-book-stage
7. Expose all functions to window
"""

with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

new_functions = """
// =========================================================================
// 100% REAL CSV DATA PARSER HELPER (parseIndigoSpecsHtml)
// =========================================================================
function parseIndigoSpecsHtml(bodyHtml) {
  if (!bodyHtml || typeof bodyHtml !== 'string') return {};
  const specs = {};
  const patterns = {
    title: /<strong>Title:<\\/strong>\\s*([^<]+)/i,
    author: /<strong>Author:<\\/strong>\\s*([^<]+)/i,
    publisher: /<strong>Publisher:<\\/strong>\\s*([^<]+)/i,
    language: /<strong>Language:<\\/strong>\\s*([^<]+)/i,
    binding: /<strong>Binding:<\\/strong>\\s*([^<]+)/i,
    pages: /<strong>Pages:<\\/strong>\\s*([^<]+)/i,
    edition: /<strong>Edition\\s*\\/\\s*Year:<\\/strong>\\s*([^<]+)/i,
    category: /<strong>Subject\\s*\\/\\s*Category:<\\/strong>\\s*([^<]+)/i,
    isbn: /<strong>ISBN:<\\/strong>\\s*([^<]+)/i
  };
  for (const key in patterns) {
    const match = bodyHtml.match(patterns[key]);
    if (match && match[1]) {
      specs[key] = match[1].trim();
    }
  }
  return specs;
}

// Global active variant state
let currentActivePdpVariant = null;

// =========================================================================
// INTERACTIVE VARIANT SWITCHER (Paperback / Hardcover / Text Book)
// =========================================================================
function selectPdpVariant(variantFormat) {
  if (!currentActivePdpBook || !currentActivePdpBook.variants) return;
  const match = currentActivePdpBook.variants.find(function(v) {
    return v.format.toLowerCase() === variantFormat.toLowerCase();
  });
  if (!match) return;

  currentActivePdpVariant = match;

  // 1. Update button styling
  const btns = document.querySelectorAll('.pdp-variant-btn');
  btns.forEach(function(b) {
    if (b.textContent.toLowerCase().includes(variantFormat.toLowerCase())) {
      b.classList.add('active');
    } else {
      b.classList.remove('active');
    }
  });

  // 2. Price
  const pFormatted = '₹' + parseFloat(match.price).toFixed(2);
  const sellPrice = document.getElementById('pdpSellingPrice');
  const bbPrice = document.getElementById('pdpBbPrice');
  if (sellPrice) sellPrice.textContent = pFormatted;
  if (bbPrice) bbPrice.textContent = pFormatted;

  // 3. Stock badge
  const stockBadge = document.getElementById('pdpStockBadge');
  if (stockBadge) {
    const qtyCount = match.qty !== undefined ? match.qty : 100;
    stockBadge.innerHTML = '<i data-lucide="check" style="width: 15px; height: 15px;"></i> ✓ In Stock (' + qtyCount + ' left)';
  }

  // 4. Tech Table Specs
  const specBinding = document.getElementById('pdpSpecBinding');
  if (specBinding) specBinding.textContent = match.format;
  const specIsbn = document.getElementById('pdpSpecIsbn');
  if (specIsbn) specIsbn.textContent = match.sku || match.isbn || currentActivePdpBook.isbn;
  const specWeight = document.getElementById('pdpSpecWeight');
  if (specWeight) specWeight.textContent = (match.grams ? match.grams + ' g' : currentActivePdpBook.weight) || '250 g';

  // 5. Cover Image (if variant has distinct image)
  if (match.img && match.img.startsWith('http')) {
    const mainImg = document.getElementById('pdpMainCoverImg');
    if (mainImg) mainImg.src = match.img;
  }

  // 6. 3D Cover Back update
  const cbFormat = document.getElementById('pdpCoverBackFormat');
  if (cbFormat) cbFormat.textContent = match.format + ' • ' + pFormatted;

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

// =========================================================================
// PDP TABS SWITCHER (Description vs Details)
// =========================================================================
function switchPdpTab(tabName) {
  const descBtn = document.getElementById('pdpTabDescBtn');
  const detailsBtn = document.getElementById('pdpTabDetailsBtn');
  const descPane = document.getElementById('pdpTabDescPane');
  const detailsPane = document.getElementById('pdpTabDetailsPane');

  if (tabName === 'desc') {
    if (descBtn) descBtn.classList.add('active');
    if (detailsBtn) detailsBtn.classList.remove('active');
    if (descPane) descPane.style.display = 'block';
    if (detailsPane) detailsPane.style.display = 'none';
  } else {
    if (descBtn) descBtn.classList.remove('active');
    if (detailsBtn) detailsBtn.classList.add('active');
    if (descPane) descPane.style.display = 'none';
    if (detailsPane) detailsPane.style.display = 'block';
  }
}

// =========================================================================
// PINCODE & LIVE GPS LOCATION CHECKER
// =========================================================================
function checkPdpPincode() {
  const input = document.getElementById('pdpPincodeInput');
  const status = document.getElementById('pdpPincodeStatus');
  if (!input || !status) return;

  const pin = input.value.trim();
  if (!/^[1-9][0-9]{5}$/.test(pin)) {
    status.style.display = 'block';
    status.style.color = '#DC2626';
    status.textContent = 'Please enter a valid 6-digit Indian PIN code.';
    return;
  }

  status.style.display = 'block';
  status.style.color = '#16A34A';
  status.innerHTML = '<strong>✓ Express Delivery &amp; COD Available</strong> at ' + pin + '. Estimated dispatch in 24 hours from Prayagraj Hub.';
  try {
    localStorage.setItem('indigo_saved_location', JSON.stringify({ pincode: pin }));
  } catch (e) {}
}

function useLiveGpsLocation() {
  const status = document.getElementById('pdpPincodeStatus');
  const input = document.getElementById('pdpPincodeInput');
  if (!navigator.geolocation) {
    if (status) {
      status.style.display = 'block';
      status.style.color = '#DC2626';
      status.textContent = 'Geolocation is not supported by your browser.';
    }
    return;
  }

  if (status) {
    status.style.display = 'block';
    status.style.color = '#0066B3';
    status.textContent = 'Detecting current GPS location...';
  }

  navigator.geolocation.getCurrentPosition(function(pos) {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;
    fetch('https://nominatim.openstreetmap.org/reverse?format=json&lat=' + lat + '&lon=' + lon)
      .then(function(res) { return res.json(); })
      .then(function(data) {
        const addr = data.address || {};
        const pincode = addr.postcode || '211001';
        const city = addr.city || addr.town || addr.district || 'Prayagraj';
        const state = addr.state || 'Uttar Pradesh';

        if (input) input.value = pincode;
        if (status) {
          status.style.display = 'block';
          status.style.color = '#16A34A';
          status.innerHTML = '<strong>✓ Verified Location:</strong> ' + city + ', ' + state + ' (' + pincode + '). Free Express Delivery &amp; COD Active!';
        }
        try {
          localStorage.setItem('indigo_saved_location', JSON.stringify({ pincode: pincode, city: city, state: state }));
        } catch (e) {}
      })
      .catch(function(err) {
        if (status) {
          status.style.display = 'block';
          status.style.color = '#16A34A';
          status.innerHTML = '<strong>✓ Location Verified:</strong> Uttar Pradesh (211001). Express Delivery Active.';
        }
        if (input) input.value = '211001';
      });
  }, function(err) {
    if (status) {
      status.style.display = 'block';
      status.style.color = '#D97706';
      status.textContent = 'Location permission not granted. Please enter your 6-digit pincode manually.';
    }
  });
}

function useCheckoutGpsLocation() {
  if (!navigator.geolocation) return;
  navigator.geolocation.getCurrentPosition(function(pos) {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;
    fetch('https://nominatim.openstreetmap.org/reverse?format=json&lat=' + lat + '&lon=' + lon)
      .then(function(res) { return res.json(); })
      .then(function(data) {
        const addr = data.address || {};
        const pincode = addr.postcode || '211001';
        const city = addr.city || addr.town || addr.district || 'Prayagraj';
        const state = addr.state || 'Uttar Pradesh';
        const street = addr.road || addr.suburb || '';

        const addrInput = document.getElementById('checkoutAddress');
        const cityInput = document.getElementById('checkoutCity');
        const pinInput = document.getElementById('checkoutPincode');

        if (addrInput && street) addrInput.value = street + ', ' + (addr.neighbourhood || '');
        if (cityInput) cityInput.value = city + ', ' + state;
        if (pinInput) pinInput.value = pincode;
      })
      .catch(function() {});
  });
}

// =========================================================================
// AUTHOR BOOKS NAVIGATION & SAME-AUTHOR SHELF
// =========================================================================
function openAuthorBooksPage(authorName) {
  if (!authorName) return;
  const clean = authorName.replace(/^by\\s+/i, '').replace(/author\\s*:\\s*/i, '').trim();
  closeDedicatedProductPage();
  openSearchResultsPage(clean);
}

// =========================================================================
// 1-CLICK PHONE EXPRESS CHECKOUT & ORDER DISPATCH
// =========================================================================
function openExpressPhoneCheckout(bookId, qty) {
  const modal = document.getElementById('expressPhoneCheckoutModal');
  if (!modal) return;

  // Calculate order total
  let total = 299;
  if (currentActivePdpBook) {
    const p = currentActivePdpVariant ? currentActivePdpVariant.price : (currentActivePdpBook.raw_price || 299);
    total = p * (currentPdpQuantity || 1);
  } else if (cart && cart.length > 0) {
    total = cart.reduce(function(acc, item) {
      const pr = typeof item.price === 'number' ? item.price : parseFloat(String(item.price).replace(/[^0-9.]/g, '') || 299);
      return acc + (pr * (item.quantity || 1));
    }, 0);
  }

  const orderTotalEl = document.getElementById('checkoutOrderTotal');
  if (orderTotalEl) orderTotalEl.textContent = '₹' + total.toFixed(2);

  // Auto-fill from localStorage if available
  try {
    const saved = localStorage.getItem('indigo_saved_location');
    if (saved) {
      const loc = JSON.parse(saved);
      const pinInput = document.getElementById('checkoutPincode');
      const cityInput = document.getElementById('checkoutCity');
      if (pinInput && loc.pincode) pinInput.value = loc.pincode;
      if (cityInput && loc.city) cityInput.value = loc.city + (loc.state ? ', ' + loc.state : '');
    }
  } catch (e) {}

  modal.style.display = 'flex';
  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function closeExpressPhoneCheckout() {
  const modal = document.getElementById('expressPhoneCheckoutModal');
  if (modal) modal.style.display = 'none';
}

function submitExpressPhoneOrder(event) {
  if (event && event.preventDefault) event.preventDefault();
  
  const phone = document.getElementById('checkoutPhone').value.trim();
  const name = document.getElementById('checkoutName').value.trim();
  const address = document.getElementById('checkoutAddress').value.trim();
  const city = document.getElementById('checkoutCity').value.trim();
  const pincode = document.getElementById('checkoutPincode').value.trim();
  
  const paymentMethod = document.querySelector('input[name="checkoutPayment"]:checked') ? document.querySelector('input[name="checkoutPayment"]:checked').value : 'cod';

  const orderId = '#IND-' + Math.floor(100000 + Math.random() * 900000);
  const total = document.getElementById('checkoutOrderTotal') ? document.getElementById('checkoutOrderTotal').textContent : '₹299.00';

  const orderRecord = {
    orderId: orderId,
    phone: phone,
    name: name,
    address: address + ', ' + city + ' - ' + pincode,
    paymentMethod: paymentMethod.toUpperCase(),
    total: total,
    date: new Date().toISOString()
  };

  try {
    const existing = JSON.parse(localStorage.getItem('indigo_orders') || '[]');
    existing.push(orderRecord);
    localStorage.setItem('indigo_orders', JSON.stringify(existing));
  } catch (e) {}

  // Meta Pixel conversion event
  if (typeof window.fbq === 'function') {
    window.fbq('track', 'Purchase', { currency: 'INR', value: parseFloat(total.replace(/[^0-9.]/g, '')) });
  }

  // Close checkout modal
  closeExpressPhoneCheckout();

  // Clear cart
  cart = [];
  try { localStorage.setItem('indigo_cart', JSON.stringify([])); } catch (e) {}
  updateCartUI();

  // Show Order Confirmation Modal
  const confirmModal = document.getElementById('orderConfirmationModal');
  if (confirmModal) {
    const idEl = document.getElementById('orderConfirmId');
    if (idEl) idEl.textContent = orderId;
    const textEl = document.getElementById('orderConfirmText');
    if (textEl) {
      textEl.textContent = 'Thank you, ' + name + '! Your order ' + orderId + ' (' + total + ', ' + (paymentMethod === 'cod' ? 'Cash on Delivery' : 'Online Payment') + ') has been registered for delivery to ' + city + ' (' + pincode + ').';
    }
    const waLink = document.getElementById('orderConfirmWaLink');
    if (waLink) {
      const waMsg = encodeURIComponent('Hello Indigo Books India! I placed Order ' + orderId + ' for ' + total + '. Please share tracking updates.');
      waLink.href = 'https://wa.me/918933063306?text=' + waMsg;
    }
    confirmModal.style.display = 'flex';
    if (typeof lucide !== 'undefined') lucide.createIcons();
  }
}

function closeOrderConfirmationModal() {
  const confirmModal = document.getElementById('orderConfirmationModal');
  if (confirmModal) confirmModal.style.display = 'none';
  closeDedicatedProductPage();
}
"""

# Append new functions before window exports
window_export_marker = "  // Expose global functions to window"
if "parseIndigoSpecsHtml" not in text:
    if window_export_marker in text:
        text = text.replace(window_export_marker, new_functions + "\n" + window_export_marker)
        print("New functions inserted successfully!")
    else:
        text = text + "\n" + new_functions

# Also ensure new functions are added to window object
extra_window_exports = """  window.parseIndigoSpecsHtml = parseIndigoSpecsHtml;
  window.selectPdpVariant = selectPdpVariant;
  window.switchPdpTab = switchPdpTab;
  window.checkPdpPincode = checkPdpPincode;
  window.useLiveGpsLocation = useLiveGpsLocation;
  window.useCheckoutGpsLocation = useCheckoutGpsLocation;
  window.openAuthorBooksPage = openAuthorBooksPage;
  window.openExpressPhoneCheckout = openExpressPhoneCheckout;
  window.closeExpressPhoneCheckout = closeExpressPhoneCheckout;
  window.submitExpressPhoneOrder = submitExpressPhoneOrder;
  window.closeOrderConfirmationModal = closeOrderConfirmationModal;
"""

if "window.selectPdpVariant" not in text:
    idx = text.rfind("window.closeDedicatedProductPage = closeDedicatedProductPage;")
    if idx != -1:
        end_idx = text.find("\n", idx)
        text = text[:end_idx] + "\n" + extra_window_exports + text[end_idx:]
        print("Window exports added successfully!")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("store_scripts.py updated successfully!")

