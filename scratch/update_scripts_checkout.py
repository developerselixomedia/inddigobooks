with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "function openExpressPhoneCheckout(bookId, qty) {"
end_marker = "function closeOrderConfirmationModal() {"

start = text.find(start_marker)
end = text.find(end_marker)

assert start != -1, "start_marker not found in store_scripts.py"
assert end != -1, "end_marker not found in store_scripts.py"

new_checkout_block = """function openExpressPhoneCheckout(bookId, qty) {
  const modal = document.getElementById('indigo-express-checkout-modal') || document.getElementById('expressPhoneCheckoutModal');
  if (!modal) return;

  // Make sure order confirmation modal is closed
  const confirmModal = document.getElementById('indigo-order-success-modal') || document.getElementById('orderConfirmationModal');
  if (confirmModal) {
    confirmModal.classList.remove('is-active');
    confirmModal.style.setProperty('display', 'none', 'important');
    confirmModal.style.display = 'none';
  }

  // Resolve book if bookId provided (supports Object or string ID)
  if (bookId) {
    let resolved = null;
    if (typeof bookId === 'object' && bookId !== null) {
      resolved = bookId;
    }
    if (!resolved && typeof window.resolveBookObject === 'function') {
      resolved = window.resolveBookObject(bookId);
    }
    if (!resolved && typeof POPULAR_BOOKS !== 'undefined') {
      for (let i = 0; i < POPULAR_BOOKS.length; i++) {
        if (POPULAR_BOOKS[i].id === bookId || POPULAR_BOOKS[i].isbn === bookId) { resolved = POPULAR_BOOKS[i]; break; }
      }
    }
    if (!resolved && typeof MASTER_SEARCH_CATALOG !== 'undefined') {
      for (let j = 0; j < MASTER_SEARCH_CATALOG.length; j++) {
        if (MASTER_SEARCH_CATALOG[j].id === bookId || MASTER_SEARCH_CATALOG[j].handle === bookId || MASTER_SEARCH_CATALOG[j].isbn === bookId) {
          resolved = MASTER_SEARCH_CATALOG[j]; break;
        }
      }
    }
    if (resolved) {
      currentActivePdpBook = resolved;
      currentPdpQuantity = qty || 1;
    }
  }

  // Populate book preview strip in modal
  const prevWrap = document.getElementById('checkoutBookPreview');
  const prevThumb = document.getElementById('checkoutBookThumb');
  const prevTitle = document.getElementById('checkoutBookTitle');
  const prevMeta = document.getElementById('checkoutBookMeta');
  if (currentActivePdpBook) {
    if (prevWrap) prevWrap.style.display = 'flex';
    if (prevThumb) {
      prevThumb.src = currentActivePdpBook.cover || '';
      prevThumb.style.display = currentActivePdpBook.cover ? 'block' : 'none';
    }
    if (prevTitle) prevTitle.textContent = currentActivePdpBook.title || 'Book';
    if (prevMeta) {
      const fmt = currentActivePdpBook.selectedFormat || currentActivePdpBook.binding || currentActivePdpBook.format || 'Paperback';
      const auth = currentActivePdpBook.author || 'Indigo Books';
      prevMeta.textContent = fmt + ' • ' + auth;
    }
  } else {
    if (prevWrap) prevWrap.style.display = 'none';
  }

  // Calculate order total with authentic pricing
  let total = 299;
  if (currentActivePdpBook) {
    const rawP = currentActivePdpBook.selectedPrice || (currentActivePdpVariant ? currentActivePdpVariant.price : (currentActivePdpBook.rawPrice || currentActivePdpBook.raw_price || currentActivePdpBook.mrp || currentActivePdpBook.price || 299));
    total = window.cleanPrice(rawP, 299) * (currentPdpQuantity || 1);
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

  modal.classList.add('is-active');
  modal.style.setProperty('display', 'flex', 'important');
  modal.style.display = 'flex';
  modal.style.setProperty('z-index', '30000000', 'important');
  modal.style.zIndex = '30000000';
  document.body.style.overflow = 'hidden';

  // Ensure Form has novalidate to prevent browser "Please match the format requested" popover
  const checkoutForm = document.getElementById('expressPhoneCheckoutForm');
  if (checkoutForm) checkoutForm.setAttribute('novalidate', 'true');

  // Phone input handling: REMOVE blocking pattern attributes & gracefully sanitize
  const pInput = document.getElementById('checkoutPhone');
  if (pInput) {
    pInput.removeAttribute('pattern');
    pInput.removeAttribute('minlength');
    pInput.removeAttribute('title');
    pInput.setAttribute('maxlength', '15');
    if (!pInput.dataset.cleanerBound) {
      pInput.dataset.cleanerBound = 'true';
      pInput.addEventListener('input', function() {
        let val = this.value.replace(/\\D/g, '');
        if (val.startsWith('91') && val.length > 10) val = val.slice(2);
        else if (val.startsWith('0') && val.length > 10) val = val.slice(1);
        this.value = val.slice(0, 10);
      });
      pInput.addEventListener('paste', function(e) {
        setTimeout(function() {
          let val = pInput.value.replace(/\\D/g, '');
          if (val.startsWith('91') && val.length > 10) val = val.slice(2);
          else if (val.startsWith('0') && val.length > 10) val = val.slice(1);
          pInput.value = val.slice(0, 10);
        }, 10);
      });
    }
  }

  // Pincode input handling: REMOVE blocking pattern attributes & gracefully sanitize
  const pinInput = document.getElementById('checkoutPincode');
  if (pinInput) {
    pinInput.removeAttribute('pattern');
    pinInput.removeAttribute('minlength');
    pinInput.removeAttribute('title');
    pinInput.setAttribute('maxlength', '10');
    if (!pinInput.dataset.cleanerBound) {
      pinInput.dataset.cleanerBound = 'true';
      pinInput.addEventListener('input', function() {
        this.value = this.value.replace(/\\D/g, '').slice(0, 6);
      });
      pinInput.addEventListener('paste', function(e) {
        setTimeout(function() {
          pinInput.value = pinInput.value.replace(/\\D/g, '').slice(0, 6);
        }, 10);
      });
    }
  }

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function closeExpressPhoneCheckout() {
  const modal = document.getElementById('indigo-express-checkout-modal') || document.getElementById('expressPhoneCheckoutModal');
  if (modal) {
    modal.classList.remove('is-active');
    modal.style.setProperty('display', 'none', 'important');
    modal.style.display = 'none';
  }
  const confirmModal = document.getElementById('indigo-order-success-modal') || document.getElementById('orderConfirmationModal');
  if (!confirmModal || !confirmModal.classList.contains('is-active')) {
    document.body.style.overflow = '';
  }
}

function submitExpressPhoneOrder(event) {
  if (event && event.preventDefault) event.preventDefault();
  
  const phoneEl = document.getElementById('checkoutPhone');
  const rawPhone = phoneEl ? phoneEl.value.trim() : '';
  let phone = rawPhone.replace(/\\D/g, '');
  if (phone.startsWith('91') && phone.length > 10) phone = phone.slice(2);
  else if (phone.startsWith('0') && phone.length > 10) phone = phone.slice(1);
  phone = phone.slice(-10);

  if (phone.length !== 10) {
    alert('Please enter a valid 10-digit mobile number (e.g. 8840818783).');
    if (phoneEl) phoneEl.focus();
    return false;
  }

  const nameEl = document.getElementById('checkoutName');
  const name = nameEl ? nameEl.value.trim() : '';
  if (!name) {
    alert('Please enter your full delivery name.');
    if (nameEl) nameEl.focus();
    return false;
  }

  const addressEl = document.getElementById('checkoutAddress');
  const address = addressEl ? addressEl.value.trim() : '';
  if (!address) {
    alert('Please enter your delivery address (House / Street / Area).');
    if (addressEl) addressEl.focus();
    return false;
  }

  const cityEl = document.getElementById('checkoutCity');
  const city = cityEl ? cityEl.value.trim() : 'Prayagraj';

  const pinEl = document.getElementById('checkoutPincode');
  const pincode = pinEl ? pinEl.value.trim().replace(/\\D/g, '').slice(0, 6) : '';
  if (pincode.length !== 6) {
    alert('Please enter a valid 6-digit postal PIN code (e.g. 211003).');
    if (pinEl) pinEl.focus();
    return false;
  }
  
  const paymentMethod = document.querySelector('input[name="checkoutPayment"]:checked') ? document.querySelector('input[name="checkoutPayment"]:checked').value : 'cod';

  const orderId = '#IND-' + Math.floor(100000 + Math.random() * 900000);
  const totalEl = document.getElementById('checkoutOrderTotal');
  const total = totalEl ? totalEl.textContent : '₹299.00';
  const numericTotal = parseFloat(total.replace(/[^0-9.]/g, '')) || 299;

  const bookInfo = currentActivePdpBook ? (currentActivePdpBook.title + ' (' + (currentActivePdpBook.selectedFormat || currentActivePdpBook.binding || currentActivePdpBook.format || 'Book') + ')') : 'Indigo Books Collection';

  const orderRecord = {
    orderId: orderId,
    phone: phone,
    name: name,
    address: address + ', ' + city + ' - ' + pincode,
    paymentMethod: paymentMethod.toUpperCase(),
    total: total,
    book: bookInfo,
    date: new Date().toISOString()
  };

  try {
    const existing = JSON.parse(localStorage.getItem('indigo_orders') || '[]');
    existing.push(orderRecord);
    localStorage.setItem('indigo_orders', JSON.stringify(existing));
  } catch (e) {}

  // Meta Pixel conversion event
  if (typeof window.fbq === 'function') {
    window.fbq('track', 'Purchase', { currency: 'INR', value: numericTotal });
  }

  // STEP 1: Fully close and hide the checkout modal FIRST so it does not stay underneath!
  closeExpressPhoneCheckout();

  // Clear cart if ordered from general cart
  if (!currentActivePdpBook) {
    cart = [];
    try { localStorage.setItem('indigo_cart', JSON.stringify([])); } catch (e) {}
    updateCartUI();
  }

  // STEP 2: Show Order Confirmation Modal cleanly
  const confirmModal = document.getElementById('indigo-order-success-modal') || document.getElementById('orderConfirmationModal');
  if (confirmModal) {
    const idEl = document.getElementById('orderConfirmId');
    if (idEl) idEl.textContent = orderId;

    const headingEl = document.getElementById('orderConfirmHeading');
    const badgeEl = document.getElementById('orderConfirmBadge');
    const textEl = document.getElementById('orderConfirmText');
    const payActionWrap = document.getElementById('orderConfirmPayActionWrap');
    const upiPayBtn = document.getElementById('orderConfirmUpiBtn');
    const upiQrImg = document.getElementById('orderConfirmUpiQr');
    const waLink = document.getElementById('orderConfirmWaLink');

    const isUpi = (paymentMethod === 'upi' || paymentMethod === 'online');

    if (badgeEl) {
      badgeEl.textContent = isUpi ? 'ORDER PLACED • COMPLETE PAYMENT' : 'ORDER CONFIRMED • CASH ON DELIVERY';
      badgeEl.style.color = isUpi ? '#B45309' : '#16A34A';
    }
    if (headingEl) {
      headingEl.textContent = isUpi ? 'Complete Instant UPI Payment' : 'Thank You for Your Order!';
    }
    if (textEl) {
      if (isUpi) {
        textEl.innerHTML = 'Thank you, <strong>' + name + '</strong>! Your order <strong>' + orderId + '</strong> for <strong>' + bookInfo + '</strong> (' + total + ') is reserved. Tap below to pay via GPay / PhonePe / Paytm / BHIM, or scan the QR code.';
      } else {
        textEl.innerHTML = 'Thank you, <strong>' + name + '</strong>! Your order <strong>' + orderId + '</strong> for <strong>' + bookInfo + '</strong> (' + total + ') has been registered for <strong>Cash on Delivery</strong> to ' + city + ' (' + pincode + ').';
      }
    }

    // Dynamic UPI Intent Link for mobile & dynamic QR code
    const upiUrl = 'upi://pay?pa=8933063306@paytm&pn=Indigo%20Books%20India&am=' + numericTotal.toFixed(2) + '&cu=INR&tn=' + encodeURIComponent('Order ' + orderId);

    if (payActionWrap) {
      payActionWrap.style.display = isUpi ? 'block' : 'none';
    }
    if (upiPayBtn) {
      upiPayBtn.href = upiUrl;
      upiPayBtn.innerHTML = '⚡ Pay ' + total + ' via UPI App (GPay / PhonePe / Paytm)';
    }
    if (upiQrImg) {
      upiQrImg.src = 'https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=' + encodeURIComponent(upiUrl);
    }

    if (waLink) {
      const waMsg = isUpi 
        ? encodeURIComponent('Hello Indigo Books India! I placed Order ' + orderId + ' for ' + bookInfo + ' (' + total + ') via UPI. Attaching payment screenshot.')
        : encodeURIComponent('Hello Indigo Books India! I placed Order ' + orderId + ' for ' + bookInfo + ' (' + total + ') with Cash on Delivery. Please confirm dispatch.');
      waLink.href = 'https://wa.me/918933063306?text=' + waMsg;
      waLink.innerHTML = isUpi 
        ? '<i data-lucide="message-circle" style="width: 16px; height: 16px;"></i> Send UPI Confirmation on WhatsApp (+91 8933063306)'
        : '<i data-lucide="message-circle" style="width: 16px; height: 16px;"></i> Track Order via WhatsApp (+91 8933063306)';
    }

    confirmModal.classList.add('is-active');
    confirmModal.style.setProperty('display', 'flex', 'important');
    confirmModal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    if (typeof lucide !== 'undefined') lucide.createIcons();

    // If mobile UPI, auto-open UPI payment intent
    if (isUpi && /Android|iPhone|iPad|iPod/i.test(navigator.userAgent)) {
      setTimeout(function() {
        window.location.href = upiUrl;
      }, 500);
    }
  }
  return false;
}

"""

text = text[:start] + new_checkout_block + text[end:]

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated store_scripts.py checkout and payment functions!")
