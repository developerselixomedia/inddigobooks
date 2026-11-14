// Indigo Books India - Store Client Engine

let BOOKS = [];

// Reactive Shopping Cart State
let cart = [];
try {
  const saved = localStorage.getItem('indigo_cart');
  if (saved) cart = JSON.parse(saved);
} catch(e) {}

// Solo Spotlight Mode Logic (Preserved)
let activeHoveredIndex = null;
function handleBookHover(index) {
  activeHoveredIndex = index;
  const items = document.querySelectorAll('.book-shelf-item');
  items.forEach((item, i) => {
    if (i === index) {
      item.classList.add('is-spotlight');
      item.classList.remove('is-dimmed');
    } else {
      item.classList.remove('is-spotlight');
      item.classList.add('is-dimmed');
    }
  });
}
function handleBookLeave() {
  activeHoveredIndex = null;
  const items = document.querySelectorAll('.book-shelf-item');
  items.forEach(item => {
    item.classList.remove('is-spotlight');
    item.classList.remove('is-dimmed');
  });
}

// Sparkles Generator (Preserved)
function initSparkles() {
  const container = document.getElementById('sparklesContainer');
  if (!container) return;
  container.innerHTML = '';
  for (let i = 0; i < 22; i++) {
    const span = document.createElement('span');
    span.className = 'sparkle-particle';
    const size = Math.random() * 5 + 3;
    span.style.width = size + 'px';
    span.style.height = size + 'px';
    span.style.left = (Math.random() * 60 + 35) + '%';
    span.style.bottom = (Math.random() * 70 + 5) + '%';
    span.style.animationDelay = (Math.random() * 3.5) + 's';
    span.style.animationDuration = (Math.random() * 3 + 3) + 's';
    container.appendChild(span);
  }
}

// 4-Phase Choreography (Preserved)
function runChoreography() {
  const hero = document.getElementById('heroSection');
  if (!hero) return;
  hero.classList.remove('phase-1-active', 'phase-2-active', 'phase-3-active');

  setTimeout(() => {
    hero.classList.add('phase-1-active');
    initSparkles();
  }, 50);

  setTimeout(() => {
    hero.classList.add('phase-2-active');
  }, 800);

  setTimeout(() => {
    hero.classList.add('phase-3-active');
  }, 1800);
}

// Cart Management
function saveCart() {
  try {
    localStorage.setItem('indigo_cart', JSON.stringify(cart));
  } catch(e) {}
  renderCart();
}

function addToCart(bookId) {
  const book = BOOKS.find(b => b.id === bookId);
  if (!book) return;
  const existing = cart.find(item => item.id === bookId);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({
      id: book.id,
      title: book.title,
      author: book.author,
      price: book.price,
      cover: book.cover,
      qty: 1
    });
  }
  saveCart();
  showToast('Added to Cart!', `"${book.title}" is in your cart.`, 'success');
}

function removeFromCart(bookId) {
  cart = cart.filter(item => item.id !== bookId);
  saveCart();
}

function updateCartQty(bookId, delta) {
  const item = cart.find(i => i.id === bookId);
  if (!item) return;
  item.qty += delta;
  if (item.qty <= 0) {
    removeFromCart(bookId);
  } else {
    saveCart();
  }
}

function renderCart() {
  const totalCount = cart.reduce((sum, i) => sum + i.qty, 0);
  const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);

  // Nav Badge & Price
  const badge = document.getElementById('cartCountBadge');
  if (badge) badge.textContent = totalCount;
  const navTotal = document.getElementById('cartTotalNav');
  if (navTotal) navTotal.textContent = '₹' + subtotal.toFixed(2);

  // Drawer Pill & Subtotal
  const drawerCountPill = document.getElementById('cartDrawerCountPill');
  if (drawerCountPill) drawerCountPill.textContent = totalCount + ' Items';
  const subtotalEl = document.getElementById('cartSubtotalText');
  if (subtotalEl) subtotalEl.textContent = '₹' + subtotal.toFixed(2);
  const totalEl = document.getElementById('cartTotalText');
  if (totalEl) totalEl.textContent = '₹' + subtotal.toFixed(2);

  // Free shipping progress meter (target: ₹999)
  const freeShippingBar = document.getElementById('freeShippingBar');
  const freeShippingText = document.getElementById('freeShippingText');
  if (freeShippingBar && freeShippingText) {
    if (subtotal >= 999) {
      freeShippingBar.style.width = '100%';
      freeShippingBar.className = 'h-full bg-emerald-500 transition-all duration-300';
      freeShippingText.innerHTML = '<span class="text-emerald-700 font-bold"> You have unlocked FREE Express Delivery!</span>';
    } else {
      const pct = Math.min(100, Math.round((subtotal / 999) * 100));
      freeShippingBar.style.width = pct + '%';
      freeShippingBar.className = 'h-full bg-[#D99B26] transition-all duration-300';
      const needed = 999 - subtotal;
      freeShippingText.innerHTML = `<span>Add <strong>₹${needed.toFixed(2)}</strong> more for Free Delivery!</span><span class="font-bold text-[#D99B26]">Free &gt; ₹999</span>`;
    }
  }

  // Items Container
  const container = document.getElementById('cartItemsContainer');
  if (!container) return;
  if (cart.length === 0) {
    container.innerHTML = `
      <div class="text-center py-12 text-slate-400">
        <svg class="w-12 h-12 mx-auto mb-3 text-slate-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/></svg>
        <p class="text-sm font-serif font-bold text-slate-700">Your Cart is Empty</p>
        <p class="text-xs text-slate-500 mt-1">Explore our bestsellers and regional gems to add books!</p>
        <button onclick="closeCartDrawer(); window.location.hash = '#bestsellersSection';" class="mt-4 bg-[#D99B26] text-slate-950 font-bold text-xs px-4 py-2 rounded-lg hover:bg-[#B88019] transition">
          Browse Best Sellers
        </button>
      </div>
    `;
    return;
  }

  container.innerHTML = cart.map(item => `
    <div class="py-3 flex items-center gap-3">
      <img src="${item.cover}" alt="${item.title}" class="w-14 h-20 object-cover rounded shadow-sm border border-slate-200 shrink-0">
      <div class="flex-1 min-w-0">
        <h4 class="text-xs font-serif font-bold text-slate-900 truncate">${item.title}</h4>
        <p class="text-[11px] text-slate-500 truncate">${item.author}</p>
        <div class="text-xs font-black text-[#0A1128] mt-1">₹${item.price}.00</div>
      </div>
      <div class="flex flex-col items-end gap-1.5">
        <button onclick="removeFromCart('${item.id}')" class="text-slate-400 hover:text-rose-600 transition p-1" title="Remove">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
        </button>
        <div class="flex items-center border border-slate-200 rounded-md bg-white">
          <button onclick="updateCartQty('${item.id}', -1)" class="px-2 py-0.5 text-xs text-slate-600 hover:bg-slate-100 font-bold">-</button>
          <span class="px-2 text-xs font-bold text-slate-900">${item.qty}</span>
          <button onclick="updateCartQty('${item.id}', 1)" class="px-2 py-0.5 text-xs text-slate-600 hover:bg-slate-100 font-bold">+</button>
        </div>
      </div>
    </div>
  `).join('');
}

// Cart Drawer Toggle
function openCartDrawer() {
  const backdrop = document.getElementById('cartDrawerBackdrop');
  const panel = document.getElementById('cartDrawerPanel');
  if (backdrop && panel) {
    backdrop.classList.remove('pointer-events-none', 'opacity-0');
    backdrop.classList.add('opacity-100');
    panel.classList.remove('translate-x-full');
  }
}
function closeCartDrawer() {
  const backdrop = document.getElementById('cartDrawerBackdrop');
  const panel = document.getElementById('cartDrawerPanel');
  if (backdrop && panel) {
    backdrop.classList.remove('opacity-100');
    backdrop.classList.add('opacity-0', 'pointer-events-none');
    panel.classList.add('translate-x-full');
  }
}

// WhatsApp Cart Checkout Order
function checkoutWhatsApp() {
  if (cart.length === 0) {
    alert('Your shopping cart is empty! Please add books first.');
    return;
  }
  const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
  let msg = "Hello Indigo Books India (Prayagraj)! \n\nI would like to place an order via Cash on Delivery (COD):\n\n";
  cart.forEach((item, idx) => {
    msg += `${idx + 1}. *${item.title}* (Qty: ${item.qty}) - ₹${item.price * item.qty}\n`;
  });
  msg += `\n*Total Amount:* ₹${subtotal.toFixed(2)}\n\nPlease confirm book availability and share dispatch details for delivery!`;
  const url = "https://wa.me/918881122722?text=" + encodeURIComponent(msg);
  window.open(url, '_blank');
}

// Quick View Modal
let currentQvBook = null;
function openQuickView(bookId) {
  const book = BOOKS.find(b => b.id === bookId);
  if (!book) return;
  currentQvBook = book;

  document.getElementById('qvCover').src = book.cover;
  document.getElementById('qvDiscountBadge').textContent = book.discount;
  document.getElementById('qvTitle').textContent = book.title;
  document.getElementById('qvAuthor').textContent = "By " + book.author;
  document.getElementById('qvReviews').textContent = `(${book.reviews} verified reviews)`;
  document.getElementById('qvPrice').textContent = "₹" + book.price + ".00";
  document.getElementById('qvOriginalPrice').textContent = "₹" + book.originalPrice + ".00";
  const savings = book.originalPrice - book.price;
  document.getElementById('qvSavingsText').textContent = `Save ₹${savings} (${book.discount})`;
  document.getElementById('qvDesc').textContent = book.desc;
  document.getElementById('qvLanguage').textContent = book.language;
  document.getElementById('qvBinding').textContent = book.binding;
  document.getElementById('qvPublisher').textContent = book.publisher;
  document.getElementById('qvISBN').textContent = book.isbn;

  document.getElementById('qvAddBtn').onclick = () => {
    addToCart(book.id);
    closeQuickView();
    openCartDrawer();
  };

  document.getElementById('qvWhatsAppBtn').onclick = () => {
    const msg = `Hello Indigo Books! \nI want to order: *${book.title}*\nAuthor: ${book.author}\nPrice: ₹${book.price}\nBinding: ${book.binding}\nPlease confirm availability for COD delivery!`;
    window.open('https://wa.me/918881122722?text=' + encodeURIComponent(msg), '_blank');
  };

  const res = document.getElementById('pincodeResult');
  if (res) res.classList.add('hidden');
  const pinInput = document.getElementById('pincodeInput');
  if (pinInput) pinInput.value = '';

  const backdrop = document.getElementById('quickViewBackdrop');
  const card = document.getElementById('quickViewCard');
  if (backdrop && card) {
    backdrop.classList.remove('pointer-events-none', 'opacity-0');
    backdrop.classList.add('opacity-100');
    card.classList.remove('scale-95');
    card.classList.add('scale-100');
  }
}

function closeQuickView() {
  const backdrop = document.getElementById('quickViewBackdrop');
  const card = document.getElementById('quickViewCard');
  if (backdrop && card) {
    backdrop.classList.remove('opacity-100');
    backdrop.classList.add('opacity-0', 'pointer-events-none');
    card.classList.remove('scale-100');
    card.classList.add('scale-95');
  }
}

// Indian Pincode Delivery Checker
function checkPincode() {
  const input = document.getElementById('pincodeInput');
  const res = document.getElementById('pincodeResult');
  if (!input || !res) return;
  const pin = input.value.trim();
  if (!/^[1-9][0-9]{5}$/.test(pin)) {
    res.className = 'text-[11px] mt-1.5 font-medium text-rose-600 block';
    res.textContent = 'Please enter a valid 6-digit Indian Postal Pincode.';
    return;
  }
  res.className = 'text-[11px] mt-1.5 font-medium text-emerald-700 block bg-emerald-50 p-2 rounded border border-emerald-200';
  res.innerHTML = ` Express Delivery available to Pincode <strong>${pin}</strong> in 2&ndash;3 business days. Cash on Delivery (COD) eligible!`;
}

// Member Login Modal
let authMode = 'signin';
function openLoginModal() {
  const backdrop = document.getElementById('loginModalBackdrop');
  const card = document.getElementById('loginModalCard');
  if (backdrop && card) {
    backdrop.classList.remove('pointer-events-none', 'opacity-0');
    backdrop.classList.add('opacity-100');
    card.classList.remove('scale-95');
    card.classList.add('scale-100');
  }
}
function closeLoginModal() {
  const backdrop = document.getElementById('loginModalBackdrop');
  const card = document.getElementById('loginModalCard');
  if (backdrop && card) {
    backdrop.classList.remove('opacity-100');
    backdrop.classList.add('opacity-0', 'pointer-events-none');
    card.classList.remove('scale-100');
    card.classList.add('scale-95');
  }
}
function switchAuthTab(tab) {
  authMode = tab;
  const h = document.getElementById('authModalHeading');
  const btn = document.getElementById('authSubmitBtn');
  const nameField = document.getElementById('authNameField');
  const remRow = document.getElementById('authRememberRow');
  const tabSign = document.getElementById('tabSignIn');
  const tabReg = document.getElementById('tabRegister');

  if (tab === 'register') {
    h.textContent = 'Create an Account';
    btn.textContent = 'Register Account';
    nameField.classList.remove('hidden');
    remRow.classList.add('hidden');
    tabReg.className = 'flex-1 pb-2.5 text-xs font-bold border-b-2 border-[#D99B26] text-[#0A1128]';
    tabSign.className = 'flex-1 pb-2.5 text-xs font-bold border-b-2 border-transparent text-slate-400 hover:text-slate-700';
  } else {
    h.textContent = 'Welcome Back';
    btn.textContent = 'Sign In';
    nameField.classList.add('hidden');
    remRow.classList.remove('hidden');
    tabSign.className = 'flex-1 pb-2.5 text-xs font-bold border-b-2 border-[#D99B26] text-[#0A1128]';
    tabReg.className = 'flex-1 pb-2.5 text-xs font-bold border-b-2 border-transparent text-slate-400 hover:text-slate-700';
  }
}
function handleAuthSubmit(e) {
  e.preventDefault();
  const msg = authMode === 'register' ? 'Account successfully registered!' : 'Signed in successfully!';
  showToast(msg, 'Welcome to Indigo Books India.', 'success');
  closeLoginModal();
}

// Catalog Directory Filtering Engine
let activeCategoryPill = 'All Categories';
function selectCategoryPill(cat) {
  activeCategoryPill = cat;
  const pills = document.querySelectorAll('.cat-pill');
  pills.forEach(p => {
    if (p.textContent.trim() === cat) {
      p.className = 'cat-pill active px-4 py-2 rounded-full text-xs font-semibold whitespace-nowrap border transition-all bg-[#0A1128] text-white border-[#0A1128] shadow-sm';
    } else {
      p.className = 'cat-pill px-4 py-2 rounded-full text-xs font-semibold whitespace-nowrap border transition-all bg-white text-slate-700 border-amber-900/20 hover:border-[#D99B26] hover:bg-amber-50';
    }
  });

  if (cat === 'Rekhta Publications') {
    window.location.hash = '#rekhtaSection';
    return;
  } else if (cat === 'Law Books') {
    window.location.hash = '#lawSection';
    return;
  } else if (cat === 'Hindi Sahitya') {
    window.location.hash = '#academicSection';
    return;
  }

  const checkboxes = document.querySelectorAll('input[name="catFilter"]');
  checkboxes.forEach(cb => {
    cb.checked = (cat !== 'All Categories' && cb.value.includes(cat));
  });
  filterCatalog();
  window.location.hash = '#shopAllSection';
}

function filterCatalog() {
  const query = (document.getElementById('catalogSearchInput')?.value || '').toLowerCase().trim();
  const checkedBoxes = Array.from(document.querySelectorAll('input[name="catFilter"]:checked')).map(c => c.value);
  const priceRange = document.querySelector('input[name="priceRange"]:checked')?.value || 'all';
  const sortVal = document.getElementById('sortSelect')?.value || 'popular';

  let results = BOOKS.filter(book => {
    if (query) {
      const matchTitle = book.title.toLowerCase().includes(query);
      const matchAuthor = book.author.toLowerCase().includes(query);
      const matchIsbn = (book.isbn || '').toLowerCase().includes(query);
      const matchCat = book.category.toLowerCase().includes(query);
      if (!matchTitle && !matchAuthor && !matchIsbn && !matchCat) return false;
    }

    if (checkedBoxes.length > 0) {
      if (!checkedBoxes.some(c => book.category.includes(c) || c.includes(book.category))) {
        return false;
      }
    }

    if (priceRange === 'under200' && book.price >= 200) return false;
    if (priceRange === '200-500' && (book.price < 200 || book.price > 500)) return false;
    if (priceRange === '500-1000' && (book.price < 500 || book.price > 1000)) return false;
    if (priceRange === 'above1000' && book.price <= 1000) return false;

    return true;
  });

  if (sortVal === 'price-asc') {
    results.sort((a, b) => a.price - b.price);
  } else if (sortVal === 'price-desc') {
    results.sort((a, b) => b.price - a.price);
  } else if (sortVal === 'discount') {
    results.sort((a, b) => (b.originalPrice - b.price) - (a.originalPrice - a.price));
  } else {
    results.sort((a, b) => b.reviews - a.reviews);
  }

  const grid = document.getElementById('dynamicCatalogGrid');
  const empty = document.getElementById('catalogEmptyState');
  const countEl = document.getElementById('filteredCountText');

  if (countEl) countEl.textContent = results.length;

  if (!grid || !empty) return;
  if (results.length === 0) {
    grid.innerHTML = '';
    empty.classList.remove('hidden');
  } else {
    empty.classList.add('hidden');
    grid.innerHTML = results.map(b => {
      const badgeBg = (b.discount && b.discount.includes('%') && parseInt(b.discount) < 20) ? 'bg-[#D99B26]' : 'bg-rose-600';
      return `
        <div class="book-product-card group bg-white rounded-xl border border-slate-200/90 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between overflow-hidden relative">
          <span class="absolute top-2.5 left-2.5 z-20 ${badgeBg} text-white text-[10px] font-black uppercase px-2 py-0.5 rounded shadow">
            ${b.discount}
          </span>
          <div class="relative aspect-[2/3] w-full bg-slate-100 overflow-hidden cursor-pointer" onclick="openQuickView('${b.id}')">
            <img src="${b.cover}" alt="${b.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2 p-3">
              <button onclick="event.stopPropagation(); openQuickView('${b.id}')" class="bg-white text-slate-900 text-xs font-bold px-3 py-1.5 rounded-full shadow hover:bg-amber-400 transition-colors">
                Quick View
              </button>
            </div>
          </div>
          <div class="p-3.5 flex flex-col flex-1 justify-between">
            <div>
              <div class="flex items-center gap-1 text-amber-500 text-xs mb-1">
                 <span class="text-[10px] text-slate-400">(${b.reviews})</span>
              </div>
              <h3 class="font-serif font-bold text-sm text-slate-900 line-clamp-1 group-hover:text-[#D99B26] transition-colors cursor-pointer" onclick="openQuickView('${b.id}')" title="${b.title}">
                ${b.title}
              </h3>
              <p class="text-xs text-slate-500 mt-0.5 truncate">${b.author}</p>
            </div>
            <div class="mt-3 pt-2.5 border-t border-slate-100 flex items-center justify-between">
              <div>
                <span class="text-base font-black text-[#0A1128]">₹${b.price}.00</span>
                <span class="text-xs text-slate-400 line-through ml-1.5">₹${b.originalPrice}.00</span>
              </div>
              <button onclick="addToCart('${b.id}')" class="bg-[#FAF8F5] hover:bg-[#D99B26] text-[#0A1128] hover:text-white border border-slate-300 hover:border-[#D99B26] font-bold p-2 rounded-lg transition-all active:scale-95 shadow-sm" title="Add to Cart">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
              </button>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }
}

function resetFilters() {
  const search = document.getElementById('catalogSearchInput');
  if (search) search.value = '';
  const checkboxes = document.querySelectorAll('input[name="catFilter"]');
  checkboxes.forEach(c => c.checked = false);
  const radio = document.querySelector('input[name="priceRange"][value="all"]');
  if (radio) radio.checked = true;
  const sort = document.getElementById('sortSelect');
  if (sort) sort.value = 'popular';
  filterCatalog();
}

function focusCatalogSearch() {
  window.location.hash = '#shopAllSection';
  setTimeout(() => {
    const search = document.getElementById('catalogSearchInput');
    if (search) {
      search.focus();
      search.select();
    }
  }, 300);
}

// Forms
function handleContactSubmit(e) {
  e.preventDefault();
  showToast('Message Sent!', 'Thank you! The Indigo Books concierge will reach out to you shortly.', 'success');
  e.target.reset();
}

function handleNewsletterSubmit(e) {
  e.preventDefault();
  showToast('Subscribed!', 'You are now subscribed to Indigo Books India literary updates.', 'success');
  e.target.reset();
}

// Toast Notifications
function showToast(title, msg, type = 'info') {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'pointer-events-auto bg-slate-900 text-white p-4 rounded-xl shadow-2xl border border-slate-800 flex items-start gap-3 w-80 transform transition-all duration-300 translate-y-4 opacity-0';
  
  const iconSvg = type === 'success' 
    ? '<svg class="w-5 h-5 text-emerald-400 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>'
    : '<svg class="w-5 h-5 text-[#D99B26] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>';

  toast.innerHTML = `
    ${iconSvg}
    <div class="flex-1 min-w-0">
      <div class="text-xs font-bold text-white">${title}</div>
      <div class="text-[11px] text-slate-300 mt-0.5 leading-snug">${msg}</div>
    </div>
  `;

  container.appendChild(toast);
  setTimeout(() => {
    toast.classList.remove('translate-y-4', 'opacity-0');
  }, 10);

  setTimeout(() => {
    toast.classList.add('opacity-0', 'translate-y-4');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// Initial on DOM Loaded
window.addEventListener('DOMContentLoaded', () => {
  runChoreography();
  renderCart();
  filterCatalog();
});

