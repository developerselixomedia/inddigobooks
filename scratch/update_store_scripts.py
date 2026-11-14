# -*- coding: utf-8 -*-
import re

with open('store_scripts.py', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace any old phone number
js = js.replace('918881122722', '918933063306')
js = js.replace('+91 8881122722', '+91 8933063306')
js = js.replace('8881122722', '8933063306')

# Check getAssetUrl function
old_get_asset_url = """function getAssetUrl(url, bookId) {
  if (bookId && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[bookId]) {
    return window.PODIUM_CDN_COVERS[bookId];
  }
  if (!url) return '';
  if (url.startsWith('//')) {
    return 'https:' + url;
  }
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) {
    return url;
  }
  let clean = url.replace(/^assets\//, '')
                 .replace(/^\{\{\s*['"]?/, '')
                 .replace(/['"]?\s*\|\s*asset_url\s*\}\}$/, '')
                 .trim();

  // If it's a bare filename or relative path from the Rajkamal / Indian publisher inventory (e.g. 1857--1776285215509.jpg)
  if (clean.includes('--') || /^[0-9]+--[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) || /^[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean)) {
    clean = clean.replace(/^products\//, '');
    return 'https://images.rajkamalprakashan.com/products/' + clean;
  }

  if (typeof window !== 'undefined' && window.PODIUM_CDN_COVERS) {
    if (window.PODIUM_CDN_COVERS[clean]) {
      return window.PODIUM_CDN_COVERS[clean];
    }
    for (let k in window.PODIUM_CDN_COVERS) {
      if (window.PODIUM_CDN_COVERS[k] && window.PODIUM_CDN_COVERS[k].indexOf(clean) !== -1) {
        return window.PODIUM_CDN_COVERS[k];
      }
    }
  }
  if (typeof window !== 'undefined' && window.SHOPIFY_ASSET_URL_ROOT) {
    return window.SHOPIFY_ASSET_URL_ROOT + clean;
  }
  return 'assets/' + clean;
}"""

new_get_asset_url = """function getAssetUrl(url, bookId) {
  if (!url && !bookId) return '';
  if (bookId && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[bookId]) {
    return window.PODIUM_CDN_COVERS[bookId];
  }
  if (url && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[url]) {
    return window.PODIUM_CDN_COVERS[url];
  }
  if (!url) return '';
  if (url.startsWith('//')) {
    return 'https:' + url;
  }
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) {
    return url;
  }
  let clean = url.replace(/^assets\//, '')
                 .replace(/^\{\{\s*['"]?/, '')
                 .replace(/['"]?\s*\|\s*asset_url\s*\}\}$/, '')
                 .trim();

  if (typeof window !== 'undefined' && window.PODIUM_CDN_COVERS) {
    if (window.PODIUM_CDN_COVERS[clean]) {
      return window.PODIUM_CDN_COVERS[clean];
    }
    for (let k in window.PODIUM_CDN_COVERS) {
      if (window.PODIUM_CDN_COVERS[k] && window.PODIUM_CDN_COVERS[k].indexOf(clean) !== -1) {
        return window.PODIUM_CDN_COVERS[k];
      }
    }
  }

  // If it's a bare filename or relative path from the Rajkamal / Indian publisher inventory
  if (clean.includes('--') || /^[0-9]+--[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) || /^[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean)) {
    clean = clean.replace(/^products\//, '');
    return 'https://images.rajkamalprakashan.com/products/' + clean;
  }

  if (typeof window !== 'undefined' && window.SHOPIFY_ASSET_URL_ROOT) {
    return window.SHOPIFY_ASSET_URL_ROOT + clean;
  }
  return 'assets/' + clean;
}"""

if old_get_asset_url in js:
    js = js.replace(old_get_asset_url, new_get_asset_url)
    print("Updated getAssetUrl")
else:
    print("old_get_asset_url not matched exactly")

# Update handleBookAction
old_handle_book = """function handleBookAction(bookId, bookUrl) {
  if (bookUrl && typeof bookUrl === 'string' && bookUrl.startsWith('/products/')) {
    window.location.href = bookUrl;
    return;
  }
  openOverviewModal(bookId);
}"""

new_handle_book = """function handleBookAction(bookId, bookUrl, event) {
  if (event) {
    event.preventDefault();
  }
  const isShopifyLivePDP = (typeof window !== 'undefined' && window.location.pathname.includes('/products/'));
  // In SPA preview mode or if on main page, open dedicated SPA product page
  if (!isShopifyLivePDP) {
    openDedicatedProductPage(bookId || bookUrl);
    return;
  }
  if (bookUrl && typeof bookUrl === 'string' && bookUrl.startsWith('/products/')) {
    window.location.href = bookUrl;
    return;
  }
  openDedicatedProductPage(bookId);
}"""

if old_handle_book in js:
    js = js.replace(old_handle_book, new_handle_book)
    print("Updated handleBookAction")
else:
    print("old_handle_book not matched exactly")

# Now add Dedicated Product Page Engine before section 7
pdp_engine = """
// =========================================================================
// --- DEDICATED AMAZON-STYLE SINGLE PRODUCT PAGE ENGINE ---
// =========================================================================
let currentActivePdpBook = null;
let currentPdpQuantity = 1;

function findBookByAnyIdentifier(query) {
  if (!query) return null;
  const qStr = String(query).toLowerCase().trim().replace(/^\\/products\\//, '').replace(/^#\\/product\\//, '');
  
  // 1. Search in MODAL_METADATA_DATABASE
  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    if (MODAL_METADATA_DATABASE[query]) return { ...MODAL_METADATA_DATABASE[query], id: query };
    for (const key in MODAL_METADATA_DATABASE) {
      const item = MODAL_METADATA_DATABASE[key];
      const h = (item.handle || '').toLowerCase().trim();
      const t = (item.title || '').toLowerCase().trim();
      if (key.toLowerCase() === qStr || h === qStr || t === qStr || t.includes(qStr)) {
        return { ...item, id: key };
      }
    }
  }

  // 2. Search in window.SHOPIFY_LIVE_PRODUCTS
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS)) {
    const live = window.SHOPIFY_LIVE_PRODUCTS.find(function(p) {
      if (!p) return false;
      const id = String(p.id || '').toLowerCase();
      const h = (p.handle || '').toLowerCase().trim();
      const t = (p.title || '').toLowerCase().trim();
      return id === qStr || h === qStr || t === qStr || t.includes(qStr);
    });
    if (live) {
      return {
        id: String(live.id),
        title: live.title,
        handle: live.handle,
        author: live.author || live.vendor || 'Indigo Books',
        price: live.price ? (String(live.price).startsWith('₹') ? live.price : '₹' + live.price) : '₹299.00',
        oldPrice: live.oldPrice || '',
        discount: live.discount || 'IN STOCK',
        cover: live.image || live.coverUrl || '',
        isbn: live.variantId || '978-INDIGO-ED',
        pages: '320p Standard Print Pages',
        pub: live.vendor || 'Authorized Publisher',
        lang: 'Hindi / English (Unabridged)',
        binding: live.format || 'Paperback',
        dispatch: 'Ships in 24 Hours from Prayagraj Hub',
        overview: live.description || 'Authentic publisher edition curated by Indigo Books India.',
        highlights: [
          '100% Genuine Author Edition',
          'Dispatched directly from Prayagraj warehouse',
          'Protective moisture-proof bookstore packaging',
          'Cash on Delivery available nationwide'
        ]
      };
    }
  }

  // 3. Search in PODIUM_BOOKS
  if (typeof PODIUM_BOOKS !== 'undefined' && Array.isArray(PODIUM_BOOKS)) {
    const p = PODIUM_BOOKS.find(function(b) {
      const id = String(b.id || '').toLowerCase();
      const h = (b.handle || '').toLowerCase().trim();
      const t = (b.title || '').toLowerCase().trim();
      return id === qStr || h === qStr || t === qStr || t.includes(qStr);
    });
    if (p) {
      return {
        id: p.id,
        title: p.title,
        handle: p.handle,
        author: p.author,
        price: p.price,
        oldPrice: p.oldPrice || '',
        discount: p.discount || 'NATIONAL BESTSELLER',
        cover: p.coverUrl || p.cover,
        isbn: p.id || '978-PODIUM',
        pages: p.pages || '312 Pages',
        pub: p.publisher || 'Lokbharti / Rajkamal',
        lang: 'Hindi (देवनागरी)',
        binding: 'Paperback',
        dispatch: 'Same-Day Prayagraj Hub Dispatch',
        overview: p.quote || 'Celebrated masterpiece and national bestseller.',
        firstPageExcerpt: p.firstPageExcerpt,
        highlights: [
          'Top 5 Trending Reads in India',
          'Authentic unabridged publisher edition',
          'Same-day priority dispatch from Prayagraj',
          'Eligible for Cash on Delivery'
        ]
      };
    }
  }

  // 4. Search in REKHTA_BOOKS
  if (typeof REKHTA_BOOKS !== 'undefined' && Array.isArray(REKHTA_BOOKS)) {
    const r = REKHTA_BOOKS.find(function(b) {
      const id = String(b.id || '').toLowerCase();
      const h = (b.handle || '').toLowerCase().trim();
      const t = (b.title || '').toLowerCase().trim();
      return id === qStr || h === qStr || t === qStr || t.includes(qStr);
    });
    if (r) {
      return {
        id: r.id,
        title: r.title,
        handle: r.handle,
        author: r.author,
        price: r.price,
        oldPrice: r.oldPrice || '',
        discount: r.discount || 'URDU HERITAGE',
        cover: r.coverUrl || r.cover,
        isbn: r.id || '978-REKHTA',
        pages: '240 Pages',
        pub: 'Rekhta / Rajkamal Publications',
        lang: 'Urdu / Hindi (Devanagari)',
        binding: 'Paperback',
        dispatch: 'Ships in 24 Hours from Prayagraj Hub',
        overview: r.desc || 'Timeless poetry and literary classic from the Rekhta collection.',
        highlights: [
          'Authentic Rekhta Poetry Archive Edition',
          'Original Shayari, Ghazals & Nazms with Commentary',
          'Collector Quality Printing with Aesthetic Typography',
          'Express Dispatch with Protective Bookstore Packaging'
        ]
      };
    }
  }

  // Fallback to first book if available
  if (typeof PODIUM_BOOKS !== 'undefined' && PODIUM_BOOKS.length > 0) {
    return PODIUM_BOOKS[0];
  }
  return null;
}

function openDedicatedProductPage(bookIdOrHandle) {
  const book = findBookByAnyIdentifier(bookIdOrHandle);
  if (!book) return;

  currentActivePdpBook = book;
  currentPdpQuantity = 1;

  const homeView = document.getElementById('homepage-view');
  const pdpView = document.getElementById('single-product-page-view');
  if (!pdpView) return;

  // 1. Breadcrumbs
  const bCat = document.getElementById('pdpBreadcrumbCategory');
  if (bCat) bCat.textContent = book.pub || 'Curated Literature';
  const bTitle = document.getElementById('pdpBreadcrumbTitle');
  if (bTitle) bTitle.textContent = book.title;

  // 2. Cover image
  const coverImg = document.getElementById('pdpMainCoverImg');
  if (coverImg) {
    const resolved = getAssetUrl(book.cover || book.coverUrl, book.id);
    coverImg.src = resolved || getFallbackCover(book.title, book.author);
    coverImg.alt = book.title;
    coverImg.onerror = function() {
      this.onerror = null;
      this.src = getFallbackCover(book.title, book.author);
    };
  }

  // 3. Title, Author, Rating
  const genreTag = document.getElementById('pdpGenreTag');
  if (genreTag) genreTag.textContent = book.badge || (book.pub ? book.pub.toUpperCase() : 'EXCLUSIVE EDITION');
  const titleEl = document.getElementById('pdpTitle');
  if (titleEl) titleEl.textContent = book.title;
  const authorEl = document.getElementById('pdpAuthor');
  if (authorEl) authorEl.textContent = book.author || 'Celebrated Author';

  // 4. Prices
  const sellPriceEl = document.getElementById('pdpSellingPrice');
  const bbPriceEl = document.getElementById('pdpBbPrice');
  const priceFormatted = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';
  if (sellPriceEl) sellPriceEl.textContent = priceFormatted;
  if (bbPriceEl) bbPriceEl.textContent = priceFormatted;

  const comparePriceEl = document.getElementById('pdpComparePrice');
  const discountBadgeEl = document.getElementById('pdpDiscountBadge');
  if (book.oldPrice && book.oldPrice !== book.price && book.oldPrice !== '') {
    const oldFormatted = String(book.oldPrice).startsWith('₹') ? book.oldPrice : '₹' + book.oldPrice;
    if (comparePriceEl) {
      comparePriceEl.textContent = oldFormatted;
      comparePriceEl.style.display = 'inline';
    }
    if (discountBadgeEl) {
      discountBadgeEl.textContent = book.discount || 'SPECIAL OFFER';
      discountBadgeEl.style.display = 'inline-block';
    }
  } else {
    if (comparePriceEl) comparePriceEl.style.display = 'none';
    if (discountBadgeEl) discountBadgeEl.style.display = 'none';
  }

  // 5. Format & Excerpt
  const formatEl = document.getElementById('pdpFormatPill');
  if (formatEl) formatEl.textContent = book.binding || 'Paperback Edition';

  const excerptBox = document.getElementById('pdpExcerptBox');
  const excerptText = document.getElementById('pdpExcerptText');
  if (excerptBox && excerptText) {
    excerptText.textContent = book.firstPageExcerpt || book.overview || 'First page preview available upon book dispatch.';
    excerptBox.classList.remove('open');
  }

  // 6. Description & Tech Specs
  const descEl = document.getElementById('pdpDescription');
  if (descEl) descEl.textContent = book.overview || 'Authentic publisher edition curated by Indigo Books India.';

  const isbnEl = document.getElementById('pdpSpecIsbn');
  if (isbnEl) isbnEl.textContent = book.isbn || '978-IND-EDITION';
  const pubEl = document.getElementById('pdpSpecPublisher');
  if (pubEl) pubEl.textContent = book.pub || 'Authorized Publisher';
  const pagesEl = document.getElementById('pdpSpecPages');
  if (pagesEl) pagesEl.textContent = book.pages || 'Standard Print Pages';
  const langEl = document.getElementById('pdpSpecLanguage');
  if (langEl) langEl.textContent = book.lang || 'Hindi / English';
  const dispatchEl = document.getElementById('pdpSpecDispatch');
  if (dispatchEl) dispatchEl.textContent = book.dispatch || 'Ships in 24 Hours from Prayagraj Hub';

  // 7. Qty Input Reset
  const qtyInput = document.getElementById('pdpQtyInput');
  if (qtyInput) qtyInput.value = '1';

  // 8. Render Recommendations Row (4 books)
  renderPdpRecommendations(book);

  // 9. View Swap
  if (homeView) homeView.style.display = 'none';
  pdpView.style.display = 'block';

  // 10. Update Hash without jump
  const safeHandle = book.handle || book.id || 'book';
  if (window.location.hash !== '#/product/' + safeHandle) {
    history.pushState(null, null, '#/product/' + safeHandle);
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function closeDedicatedProductPage() {
  const homeView = document.getElementById('homepage-view');
  const pdpView = document.getElementById('single-product-page-view');
  if (!homeView || !pdpView) return;

  pdpView.style.display = 'none';
  homeView.style.display = 'block';

  if (window.location.hash.startsWith('#/product/')) {
    history.pushState(null, null, ' ');
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function togglePdpLookInside() {
  const box = document.getElementById('pdpExcerptBox');
  if (box) {
    box.classList.toggle('open');
  }
}

function pdpQtyDecrease() {
  if (currentPdpQuantity > 1) {
    currentPdpQuantity--;
    const input = document.getElementById('pdpQtyInput');
    if (input) input.value = currentPdpQuantity;
  }
}

function pdpQtyIncrease() {
  if (currentPdpQuantity < 99) {
    currentPdpQuantity++;
    const input = document.getElementById('pdpQtyInput');
    if (input) input.value = currentPdpQuantity;
  }
}

function pdpAddToCart() {
  if (!currentActivePdpBook) return;
  for (let i = 0; i < currentPdpQuantity; i++) {
    addToCart(currentActivePdpBook.id);
  }
}

function pdpBuyNow() {
  if (!currentActivePdpBook) return;
  for (let i = 0; i < currentPdpQuantity; i++) {
    addToCart(currentActivePdpBook.id);
  }
  // If in Shopify environment, redirect to checkout
  if (window.location.hostname.includes('shopify') || window.location.hostname.includes('indigobooks.shop')) {
    window.location.href = '/checkout';
  } else {
    toggleCartDrawer(true);
  }
}

function pdpWhatsAppOrder() {
  if (!currentActivePdpBook) return;
  const book = currentActivePdpBook;
  const price = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';
  const qty = currentPdpQuantity;
  const total = (parseFloat(String(price).replace(/[^0-9.]/g, '')) * qty).toFixed(2);
  const msg = encodeURIComponent(
    'Hello Indigo Books Prayagraj! 📚\\n\\n' +
    'I would like to order this book via Cash on Delivery (COD):\\n' +
    '• *Title:* ' + book.title + '\\n' +
    '• *Author:* ' + (book.author || 'Indigo Books') + '\\n' +
    '• *Quantity:* ' + qty + '\\n' +
    '• *Unit Price:* ' + price + '\\n' +
    '• *Estimated Total:* ₹' + total + '\\n' +
    '• *ISBN/SKU:* ' + (book.isbn || 'Standard') + '\\n\\n' +
    'Please confirm delivery to my pincode and share tracking details. Thank you!'
  );
  window.open('https://wa.me/918933063306?text=' + msg, '_blank');
}

function renderPdpRecommendations(activeBook) {
  const container = document.getElementById('pdpRecContainer');
  if (!container) return;

  const catalog = getCatalogData();
  const filtered = catalog.filter(function(b) {
    return String(b.id) !== String(activeBook.id) && b.title !== activeBook.title;
  }).slice(0, 4);

  container.innerHTML = filtered.map(function(book) {
    const rawCover = book.image || book.coverUrl || book.cover || '';
    const cover = getAssetUrl(rawCover, book.id) || getFallbackCover(book.title, book.author);
    const bookUrl = book.url || (book.handle ? '/products/' + book.handle : '');
    const priceFormatted = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';

    return `
      <div class="catalog-card">
        <div class="catalog-thumb" onclick="openDedicatedProductPage('${book.id || book.handle}')" style="cursor: pointer;">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${book.title}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('${book.title}', '${book.author}');" />
        </div>
        <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
          ${book.discount || 'RECOMMENDED'}
        </div>
        <h3 style="font-family: 'Merriweather', serif; font-size: 14px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; min-height: 36px;">
          <a href="javascript:void(0)" onclick="openDedicatedProductPage('${book.id || book.handle}')" style="color: inherit; text-decoration: none;">${book.title}</a>
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 10px;">
          ${book.author || book.vendor || 'Indigo Books'}
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 12px;">
          <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${priceFormatted}</span>
        </div>
        <button type="button" class="btn-add-cart" style="width: 100%; justify-content: center;" onclick="addToCart('${book.id}')">
          <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add to Cart
        </button>
      </div>
    `;
  }).join('');
}

function checkHashRoute() {
  const hash = window.location.hash || '';
  if (hash.startsWith('#/product/')) {
    const handleOrId = hash.replace('#/product/', '');
    openDedicatedProductPage(handleOrId);
  } else if (!hash || hash === '#' || hash === '#top') {
    const pdpView = document.getElementById('single-product-page-view');
    const homeView = document.getElementById('homepage-view');
    if (pdpView && pdpView.style.display === 'block') {
      pdpView.style.display = 'none';
      if (homeView) homeView.style.display = 'block';
    }
  }
}
"""

# Insert pdp_engine before section 7
if 'DEDICATED AMAZON-STYLE SINGLE PRODUCT PAGE ENGINE' not in js:
    target_marker = "// --- 7. MEMBER LOGIN MODAL ---"
    if target_marker in js:
        js = js.replace(target_marker, pdp_engine + "\n" + target_marker)
        print("Inserted pdp_engine")
    else:
        print("target_marker not found; appending to bottom")
        js += "\n" + pdp_engine

# Update initIndigoStore to register hash listener and check hash
old_init = """function initIndigoStore() {
  try { runVideoIntroSpotlightTour(); } catch(e) {}
  try { selectPodiumBook(0); } catch(e) {}
  try { switchPoet('all'); } catch(e) {}
  try { switchVaultTab('law'); } catch(e) {}
  try { renderCatalog(); } catch(e) {}
  try { updateCartUI(); } catch(e) {}

  if (typeof lucide !== 'undefined') {
    try { lucide.createIcons(); } catch(e) {}
  }
}"""

new_init = """function initIndigoStore() {
  try { runVideoIntroSpotlightTour(); } catch(e) {}
  try { selectPodiumBook(0); } catch(e) {}
  try { switchPoet('all'); } catch(e) {}
  try { switchVaultTab('law'); } catch(e) {}
  try { renderCatalog(); } catch(e) {}
  try { updateCartUI(); } catch(e) {}
  try { checkHashRoute(); } catch(e) {}

  window.addEventListener('hashchange', checkHashRoute);

  if (typeof lucide !== 'undefined') {
    try { lucide.createIcons(); } catch(e) {}
  }
}"""

if old_init in js:
    js = js.replace(old_init, new_init)
    print("Updated initIndigoStore")
else:
    print("old_init not matched exactly")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(js)

print("store_scripts.py updated successfully!")

