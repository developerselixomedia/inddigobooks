# -*- coding: utf-8 -*-
import sys
import re

print("Starting Master 4 Bugs Application...")

# =========================================================================
# PART 1: UPDATE store_scripts.py
# =========================================================================
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    scripts_text = f.read()

# 1A. Replace findBookByAnyIdentifier with window.resolveBookObject
resolve_book_code = '''// --- COMPREHENSIVE BOOK RESOLUTION ENGINE (NEVER FALLS BACK TO GODAN) ---
window.resolveBookObject = function(bookOrId, triggerEl) {
  var pool = []
    .concat(window.MASTER_BOOKS || [])
    .concat(window.SHOPIFY_LIVE_PRODUCTS || [])
    .concat(window.PODIUM_BOOKS || [])
    .concat(window.REKHTA_BOOKS || [])
    .concat(window.VAULT_BOOKS || [])
    .concat(window.CATALOG_BOOKS || []);

  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    for (var k in MODAL_METADATA_DATABASE) {
      if (MODAL_METADATA_DATABASE[k]) {
        pool.push(Object.assign({ id: k }, MODAL_METADATA_DATABASE[k]));
      }
    }
  }

  if (bookOrId && typeof bookOrId === 'object' && bookOrId.title) {
    return bookOrId;
  }

  var key = String(bookOrId || '').trim().toLowerCase().replace(/^\\/products\\//, '').replace(/^#\\/product\\//, '');
  if (key) {
    var found = pool.find(function(b) {
      if (!b) return false;
      var bId = String(b.id || '').trim().toLowerCase();
      var bHandle = String(b.handle || '').trim().toLowerCase();
      var bSku = String(b.sku || '').trim().toLowerCase();
      var bTitle = String(b.title || '').trim().toLowerCase();
      var slugTitle = bTitle.replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
      return bId === key || bHandle === key || bSku === key || bTitle === key || slugTitle === key || (key.length > 3 && bTitle.indexOf(key) !== -1);
    });
    if (found) {
      return {
        id: found.id || key,
        title: found.title,
        handle: found.handle || found.id,
        author: found.author || found.vendor || 'Indigo Books Author',
        price: found.price ? (String(found.price).startsWith('₹') ? found.price : '₹' + found.price) : '₹299.00',
        oldPrice: found.oldPrice || '',
        discount: found.discount || 'IN STOCK',
        cover: getAssetUrl(found.cover || found.coverUrl || found.image),
        coverUrl: getAssetUrl(found.coverUrl || found.cover || found.image),
        binding: found.binding || found.format || 'Paperback',
        pub: found.publisher || found.pub || found.vendor || 'Authorized Publisher',
        isbn: found.isbn || found.sku || '978-81-267-XXXX-X',
        pages: found.pages || '280 Pages',
        lang: found.lang || found.language || 'Hindi / English',
        dispatch: found.dispatch || 'Same-Day Prayagraj Hub Dispatch',
        overview: found.overview || found.desc || found.description || found.quote || ('Masterpiece edition of ' + found.title + ' curated by Indigo Books India.'),
        firstPageExcerpt: found.firstPageExcerpt || found.excerpt || found.overview || 'First page preview available upon book dispatch.',
        highlights: found.highlights || [
          '100% Authentic Publisher Original Edition',
          'Direct express dispatch from Prayagraj warehouse',
          'Protective moisture-proof bookstore packaging',
          'Cash on Delivery available nationwide'
        ]
      };
    }
  }

  // Fallback: Scrape exact book data from the clicked DOM card itself so it NEVER opens Godan by mistake!
  var card = triggerEl ? triggerEl.closest('[data-book-id], [data-title], .book-card, .catalog-card, .vault-card, .rekhta-card, .ihm-book-item, .ivh-book-card, .feat-book-card, .mini-book-card') : null;
  if (card) {
    var domTitle = card.getAttribute('data-title') || (card.querySelector('h3, h4, .book-title, .card-title') ? card.querySelector('h3, h4, .book-title, .card-title').textContent.trim() : '');
    if (domTitle) {
      var byDomTitle = pool.find(function(b) {
        return b && String(b.title || '').trim().toLowerCase() === domTitle.toLowerCase();
      });
      if (byDomTitle) return byDomTitle;
    }
    var domAuthor = card.getAttribute('data-author') || (card.querySelector('.book-author, .card-author, p') ? card.querySelector('.book-author, .card-author, p').textContent.trim() : 'Indigo Books Archive');
    var domPriceText = card.getAttribute('data-price') || (card.querySelector('.book-price, .price, [class*="price"]') ? card.querySelector('.book-price, .price, [class*="price"]').textContent : '299');
    var domPrice = parseFloat(String(domPriceText).replace(/[^0-9.]/g, '')) || 299;
    var domImg = card.querySelector('img') ? card.querySelector('img').src : '';
    var domBinding = card.getAttribute('data-binding') || (card.textContent.toLowerCase().indexOf('hardcover') !== -1 ? 'Hardcover' : 'Paperback');
    return {
      id: (domTitle || 'book').toLowerCase().replace(/[^a-z0-9]+/g, '-'),
      title: domTitle || 'Selected Book',
      handle: (domTitle || 'book').toLowerCase().replace(/[^a-z0-9]+/g, '-'),
      author: domAuthor,
      vendor: card.getAttribute('data-publisher') || domAuthor,
      pub: card.getAttribute('data-publisher') || domAuthor,
      price: '₹' + domPrice.toFixed(2),
      binding: domBinding,
      image: domImg,
      cover: domImg,
      coverUrl: domImg,
      category: card.getAttribute('data-category') || 'Literature',
      isbn: card.getAttribute('data-isbn') || '978-81-267-XXXX-X',
      dimensions: card.getAttribute('data-dimensions') || '21.5 x 14.0 x 1.8 cm',
      weight: card.getAttribute('data-weight') || '320 g',
      pages: card.getAttribute('data-pages') || '280 Pages',
      lang: card.getAttribute('data-language') || 'Hindi',
      dispatch: 'Ships in 24 Hours from Prayagraj Hub',
      overview: card.getAttribute('data-description') || (domTitle + ' by ' + domAuthor + ' — 100% authentic publisher edition dispatched directly from Indigo Books India, Prayagraj.'),
      firstPageExcerpt: 'Authentic unabridged text curated by Indigo Books India.',
      highlights: [
        '100% Authentic Publisher Edition',
        'Direct express dispatch from Prayagraj warehouse',
        'Protective bookstore packaging',
        'Cash on Delivery available nationwide'
      ]
    };
  }
  return null;
};

// Aliases
window.findBookByAnyIdentifier = window.resolveBookObject;
'''

# Find findBookByAnyIdentifier definition and replace it
find_book_pattern = r'function findBookByAnyIdentifier\(query\) \{[\s\S]*?\n\}'
match = re.search(find_book_pattern, scripts_text)
if match:
    scripts_text = scripts_text[:match.start()] + resolve_book_code + scripts_text[match.end():]
    print("1A. Replaced findBookByAnyIdentifier with window.resolveBookObject!")
else:
    print("1A. findBookByAnyIdentifier pattern not matched!")

# 1B. Update handleBookAction to pass trigger element
old_hba = '''function handleBookAction(bookId, bookUrl, event) {
  if (event) {
    if (typeof event.preventDefault === 'function') event.preventDefault();
    if (typeof event.stopPropagation === 'function') event.stopPropagation();
  }
  // Open dedicated Amazon-style single product details view instantly (zero 404 risk)
  openDedicatedProductPage(bookId || bookUrl);
}'''

new_hba = '''function handleBookAction(bookId, bookUrl, event) {
  var e = event || (typeof window !== 'undefined' && window.event);
  var triggerEl = e && (e.currentTarget || e.target);
  if (e) {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
  }
  // Open dedicated Amazon-style single product details view instantly (zero 404 risk)
  openDedicatedProductPage(bookId || bookUrl, triggerEl);
}'''

if old_hba in scripts_text:
    scripts_text = scripts_text.replace(old_hba, new_hba)
    print("1B. Updated handleBookAction to pass triggerEl!")
else:
    print("1B. old_hba not found!")

# 1C. Update openDedicatedProductPage signature and check
old_odpp = '''function openDedicatedProductPage(bookIdOrHandle) {
  const book = findBookByAnyIdentifier(bookIdOrHandle);
  if (!book) return;'''

new_odpp = '''function openDedicatedProductPage(bookIdOrHandle, triggerEl) {
  const book = window.resolveBookObject(bookIdOrHandle, triggerEl);
  if (!book) {
    console.warn("Indigo Books: Could not resolve book for", bookIdOrHandle);
    return;
  }'''

if old_odpp in scripts_text:
    scripts_text = scripts_text.replace(old_odpp, new_odpp)
    print("1C. Updated openDedicatedProductPage to use resolveBookObject without Godan fallback!")
else:
    print("1C. old_odpp not found!")

# 1D. Update updateCartUI for Fix 2 (Empty state and footer display)
old_ucui_start = '''function updateCartUI() {
  const countEl = document.getElementById('cartTotalCount');
  const priceEl = document.getElementById('cartTotalPrice');
  const badgeEl = document.getElementById('cartDrawerBadge');
  const subtotalEl = document.getElementById('cartDrawerSubtotal');
  const navCountEl = document.getElementById('nav-cart-count');
  const navTotalEl = document.getElementById('nav-cart-total');
  const drawerItemCountEl = document.getElementById('cartItemCount');
  const list = document.getElementById('cartDrawerItemsList');'''

new_ucui_start = '''function updateCartUI() {
  const countEl = document.getElementById('cartTotalCount');
  const priceEl = document.getElementById('cartTotalPrice');
  const badgeEl = document.getElementById('cartDrawerBadge');
  const subtotalEl = document.getElementById('cartDrawerSubtotal');
  const navCountEl = document.getElementById('nav-cart-count');
  const navTotalEl = document.getElementById('nav-cart-total');
  const drawerItemCountEl = document.getElementById('cartItemCount');
  const list = document.getElementById('cartItemsContainer') || document.getElementById('cartDrawerItemsList');
  const footerEl = document.querySelector('.cart-drawer-footer');'''

if old_ucui_start in scripts_text:
    scripts_text = scripts_text.replace(old_ucui_start, new_ucui_start)
    print("1D. Updated updateCartUI targets!")
else:
    print("1D. old_ucui_start not found!")

# 1E. Update updateCartUI empty state handling and footer toggle
old_empty_block = '''  if (cart.length === 0) {
    list.innerHTML = `
      <div style="text-align: center; padding: 48px 16px; color: #64748B;">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#CBD5E1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 12px; display: block;">
          <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
        <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 18px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">Your Reading Bag is Empty</h4>
        <p style="font-size: 13.5px; color: #64748B; margin: 0 0 20px; line-height: 1.5;">Explore India's premier collection of 5,500+ curated publisher editions.</p>
        <button type="button" onclick="closeCartAndBrowseCatalog()" style="background: #0066B3; color: #FFFFFF; border: none; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13.5px; font-weight: 700; padding: 12px 24px; border-radius: 8px; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 12px rgba(0,102,179,0.25);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
          Start Browsing (5,500+ Books)
        </button>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }'''

new_empty_block = '''  // Update Free Shipping Progress Bar
  const freeText = document.getElementById('freeShippingText');
  const freePct = document.getElementById('freeShippingPercent');
  const freeBar = document.getElementById('freeShippingBar');
  if (totalPrice >= 999) {
    if (freeText) freeText.textContent = '🎉 You unlocked Free Express Dispatch!';
    if (freePct) freePct.textContent = '100%';
    if (freeBar) freeBar.style.width = '100%';
  } else {
    const diff = (999 - totalPrice).toFixed(0);
    const pct = Math.min(100, Math.round((totalPrice / 999) * 100));
    if (freeText) freeText.textContent = 'Add ₹' + diff + ' for Free Express Dispatch';
    if (freePct) freePct.textContent = pct + '%';
    if (freeBar) freeBar.style.width = pct + '%';
  }

  if (cart.length === 0) {
    if (footerEl) footerEl.style.display = 'none';
    list.innerHTML = `
      <div style="text-align: center; padding: 60px 20px; color: #94A3B8;">
        <i data-lucide="book-open" style="width: 48px; height: 48px; margin: 0 auto 12px; stroke-width: 1.5; color: #CBD5E1;"></i>
        <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 17px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">Your reading bag is empty</h4>
        <p style="font-size: 13px; color: #64748B; margin: 0 0 20px; line-height: 1.5;">Explore our 5,500+ curated books and add your next read.</p>
        <button type="button" class="hero-shop-btn" style="margin: 0 auto; display: inline-flex; align-items: center; justify-content: center;" onclick="browseAllBooks(event)">
          <span>Start Browsing &rarr;</span>
        </button>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  if (footerEl) footerEl.style.display = 'block';'''

if old_empty_block in scripts_text:
    scripts_text = scripts_text.replace(old_empty_block, new_empty_block)
    print("1E. Updated updateCartUI empty/full state and shipping progress!")
else:
    print("1E. old_empty_block not found!")

# 1F. Ensure proceedToCheckout and checkoutViaWhatsApp are defined
checkout_helpers = '''
function proceedToCheckout() {
  if (cart.length === 0) {
    alert("Your shopping cart is empty!");
    return;
  }
  window.location.href = '/checkout';
}

function checkoutViaWhatsApp() {
  checkoutWhatsApp();
}
'''

if 'function proceedToCheckout' not in scripts_text:
    scripts_text = scripts_text.replace('function checkoutWhatsApp() {', checkout_helpers + '\nfunction checkoutWhatsApp() {')
    print("1F. Added proceedToCheckout and checkoutViaWhatsApp!")

# 1G. Add to window exports
if 'window.openSoloBookPage = openDedicatedProductPage;' not in scripts_text:
    target_exp = 'window.openDedicatedProductPage = openDedicatedProductPage;'
    replacement_exp = 'window.openDedicatedProductPage = openDedicatedProductPage;\n  window.openSoloBookPage = openDedicatedProductPage;\n  window.resolveBookObject = resolveBookObject;\n  window.proceedToCheckout = proceedToCheckout;\n  window.checkoutViaWhatsApp = checkoutViaWhatsApp;'
    scripts_text = scripts_text.replace(target_exp, replacement_exp)
    print("1G. Added window aliases!")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(scripts_text)

print("Finished updating store_scripts.py successfully!")

