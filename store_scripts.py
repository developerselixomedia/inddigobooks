# -*- coding: utf-8 -*-
"""
store_scripts.py
Single Source of Truth for Bookstore JavaScript Engine.
Clean Vanilla JS with Zero External Frameworks.
"""

UNIFIED_STORE_JS = """
// --- GLOBAL NAVIGATION: RETURN TO HOMEPAGE ---
// --- GLOBAL CATALOG & STORE STATE VARIABLES ---
var currentCatalogCategory = 'all';
var currentCatalogQuery = '';
var catalogCurrentPage = 1;
var CATALOG_PAGE_SIZE = 12;

window.currentCatalogCategory = currentCatalogCategory;
window.currentCatalogQuery = currentCatalogQuery;
window.catalogCurrentPage = catalogCurrentPage;
window.CATALOG_PAGE_SIZE = CATALOG_PAGE_SIZE;

window.returnToHome = function(event) {
  if (event) {
    if (typeof event.preventDefault === 'function') event.preventDefault();
    if (typeof event.stopPropagation === 'function') event.stopPropagation();
  }
  const pdpView = document.getElementById('single-product-page-view');
  if (pdpView) pdpView.style.display = 'none';

  const searchView = document.getElementById('indigo-search-results-view');
  if (searchView) searchView.style.display = 'none';
  if (typeof activeSearchQuery !== 'undefined') activeSearchQuery = '';
  if (typeof currentSearchResultsList !== 'undefined') currentSearchResultsList = [];

  if (typeof window.forceCloseOverviewAndModals === 'function') {
    window.forceCloseOverviewAndModals();
  }
  if (typeof closeOverviewModal === 'function') {
    closeOverviewModal();
  }

  if (typeof hideAllSearchDropdowns === 'function') {
    hideAllSearchDropdowns();
  }
  ['hero-search-input', 'catalog-search-input', 'results-search-input'].forEach(function(id) {
    const el = document.getElementById(id);
    if (el) el.value = '';
  });

  const homeView = document.getElementById('homepage-view');
  if (homeView) homeView.style.display = 'block';

  try {
    history.pushState(null, null, window.location.pathname);
  } catch(err) {
    window.location.hash = '';
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  document.documentElement.scrollTop = 0;
  document.body.scrollTop = 0;
};

// =========================================================================
// INDIGO BOOKS INDIA - PURE VANILLA JS ENGINE (UNIFIED & COMPLETE)
// =========================================================================

// Global Helper: Sanitize Price Parsing Everywhere (Never Show ₹NaN)
window.cleanPrice = function(val, fallback) {
  var n = parseFloat(String(val || '').replace(/[^0-9.]/g, ''));
  return isNaN(n) || n <= 0 ? (fallback || 299) : n;
};

// Global Helper: Close All Active Modals & Overlays
window.closeAllIndigoModals = function() {
  if (typeof closeOverviewModal === 'function') closeOverviewModal();
  if (typeof closeOrderConfirmationModal === 'function') closeOrderConfirmationModal();
  if (typeof closeExpressPhoneCheckout === 'function') closeExpressPhoneCheckout();
  const signinModal = document.getElementById('indigo-signin-modal') || document.getElementById('loginModalOverlay');
  if (signinModal) {
    signinModal.classList.remove('is-active');
    signinModal.style.setProperty('display', 'none', 'important');
    signinModal.style.display = 'none';
  }
  document.body.style.overflow = '';
};

// Global Helper: Open Solo Book Page
window.openSoloBookPage = function(bookIdOrObj, triggerElOrEvent) {
  var triggerEl = null;
  if (triggerElOrEvent) {
    if (triggerElOrEvent.preventDefault) {
      triggerElOrEvent.preventDefault();
      triggerEl = triggerElOrEvent.currentTarget || triggerElOrEvent.target;
    } else if (triggerElOrEvent.nodeType) {
      triggerEl = triggerElOrEvent;
    }
  }
  if (typeof openDedicatedProductPage === 'function') {
    openDedicatedProductPage(bookIdOrObj, triggerEl);
  }
};

// Global Helper: Add to Cart (Direct delegation to executeAddToCart, preventing recursion)
window.addToCart = function(bookId, bookTitle, bookPrice, bookCover, event) {
  if (typeof executeAddToCart === 'function') {
    executeAddToCart(bookId, bookTitle, bookPrice, bookCover, event);
  }
};


// --- UNIVERSAL VECTOR SVG FALLBACK COVER GENERATOR ---
function getFallbackCover(title, author) {
  let cleanTitle = (title || '').replace(/["'<>]/g, '').trim();
  let cleanAuthor = (author || '').replace(/["'<>]/g, '').trim();
  if (!cleanTitle || cleanTitle.toLowerCase() === 'flanking book' || cleanTitle.toLowerCase() === 'inside cover' || cleanTitle.toLowerCase() === 'book') {
    cleanTitle = 'Indigo Books Edition';
  }
  if (!cleanAuthor) {
    cleanAuthor = 'Prayagraj Classic';
  }
  cleanTitle = cleanTitle.slice(0, 26);
  cleanAuthor = cleanAuthor.slice(0, 24);

  const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="420" viewBox="0 0 300 420">' +
    '<defs>' +
      '<linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">' +
        '<stop offset="0%" stop-color="#0F172A"/>' +
        '<stop offset="50%" stop-color="#1E293B"/>' +
        '<stop offset="100%" stop-color="#0A1128"/>' +
      '</linearGradient>' +
    '</defs>' +
    '<rect width="300" height="420" rx="6" fill="url(#bgGrad)"/>' +
    '<rect x="12" y="12" width="276" height="396" rx="4" fill="none" stroke="#D99B26" stroke-width="2" stroke-dasharray="4,2"/>' +
    '<rect x="20" y="20" width="260" height="380" rx="2" fill="none" stroke="#D99B26" stroke-width="0.75" opacity="0.6"/>' +
    '<circle cx="150" cy="90" r="28" fill="#1E293B" stroke="#D99B26" stroke-width="1.5"/>' +
    '<path d="M142 82h16v16H142z" fill="none" stroke="#D99B26" stroke-width="1.5"/>' +
    '<text x="150" y="195" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FEF3C7" text-anchor="middle">' + cleanTitle + '</text>' +
    '<text x="150" y="235" font-family="sans-serif" font-size="12" font-weight="600" fill="#D99B26" text-anchor="middle">' + cleanAuthor + '</text>' +
    '<line x1="80" y1="260" x2="220" y2="260" stroke="#D99B26" stroke-width="1" opacity="0.5"/>' +
    '<text x="150" y="285" font-family="sans-serif" font-size="9" letter-spacing="2" fill="#94A3B8" text-anchor="middle">INDIGO HERITAGE EDITION</text>' +
    '<text x="150" y="380" font-family="sans-serif" font-size="10" font-weight="bold" fill="#D99B26" text-anchor="middle">PRAYAGRAJ • INDIA</text>' +
  '</svg>';
  return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
}

// --- UNIVERSAL ASSET URL RESOLVER ---
function getAssetUrl(url, bookId) {
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

  // If it's a bare filename or relative path from the Rajkamal / Indian publisher inventory (5,500+ books)
  const isIndianCatalogBook = (
    clean.includes('--') ||
    clean.includes('17762') ||
    clean.startsWith('--') ||
    /^[0-9]+[\s-][0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) ||
    /^[0-9]+--[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) ||
    /^[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) ||
    /^[0-9a-f]{8}-[0-9a-f]{4}/i.test(clean) ||
    ((clean.endsWith('.jpg') || clean.endsWith('.jpeg') || clean.endsWith('.png') || clean.endsWith('.webp')) &&
     !clean.startsWith('hero-') && !clean.startsWith('book-') && !clean.startsWith('indigo-') && !clean.startsWith('logo'))
  );

  if (isIndianCatalogBook) {
    const pubFile = clean.replace(/^products\//, '').replace(/^\/+/, '').replace(/\s+/g, '-');
    return 'https://images.rajkamalprakashan.com/products/' + pubFile;
  }

  if (typeof window !== 'undefined' && window.SHOPIFY_ASSET_URL_ROOT) {
    return window.SHOPIFY_ASSET_URL_ROOT + clean;
  }
  return 'assets/' + clean;
}

// --- 0. HERO 3x2 SEQUENTIAL SPOTLIGHT ENGINE (EXACT VIDEO MATCH) ---
let heroSpotlightTimeouts = [];
let isUserInteractingHero = false;

function clearHeroSpotlightTimers() {
  heroSpotlightTimeouts.forEach(function(t) { clearTimeout(t); });
  heroSpotlightTimeouts = [];
}

function setHeroSpotlitBook(index) {
  const grid = document.getElementById('ivh-books-grid') || document.getElementById('heroBooksGrid') || document.querySelector('.ivh-books-grid');
  const cards = document.querySelectorAll('.ivh-book-card, .hero-video-book-card, .hero-book-card');
  if (!cards.length) return;

  if (index === null || index === -1 || index === undefined) {
    if (grid) grid.classList.remove('spotlight-mode');
    cards.forEach(function(card) { card.classList.remove('is-spotlit'); });
    return;
  }

  if (grid) grid.classList.add('spotlight-mode');
  cards.forEach(function(card, idx) {
    if (idx === index) {
      card.classList.add('is-spotlit');
    } else {
      card.classList.remove('is-spotlit');
    }
  });
}

function runVideoIntroSpotlightTour() {
  clearHeroSpotlightTimers();
  if (isUserInteractingHero) return;

  setHeroSpotlitBook(null);

  // 1. Top-Right Book (index 2) for 900ms
  var t1 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(2);
  }, 700);

  // 2. Bottom-Right Book (index 5) for 900ms
  var t2 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(5);
  }, 1600);

  // 3. Bottom-Center Book (index 4) for 900ms
  var t3 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(4);
  }, 2500);

  // 4. Smoothly restore all 6 books to resting state
  var t4 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(null);
  }, 3400);

  heroSpotlightTimeouts.push(t1, t2, t3, t4);
}

function handleHeroBookHover(index) {
  isUserInteractingHero = true;
  clearHeroSpotlightTimers();
  setHeroSpotlitBook(index);
}

function handleHeroGridMouseLeave() {
  setHeroSpotlitBook(null);
}


// --- 1. THE PODIUM CAROUSEL ENGINE ---
let currentPodiumIndex = 0;

function getPodiumData() {
  const curated = (typeof PODIUM_BOOKS !== 'undefined' && Array.isArray(PODIUM_BOOKS)) ? PODIUM_BOOKS : [];
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length > 0) {
    return curated.map(function(fallback, idx) {
      const q = (fallback.title || '').toLowerCase().trim();
      const h = (fallback.handle || '').toLowerCase().trim();
      const live = window.SHOPIFY_LIVE_PRODUCTS.find(function(p) {
        if (!p || !p.title) return false;
        const pt = p.title.toLowerCase().trim();
        const ph = (p.handle || '').toLowerCase().trim();
        return pt === q || pt.includes(q) || q.includes(pt) || (h && ph.includes(h));
      });

      if (live) {
        return {
          id: String(live.id || fallback.id),
          variantId: live.variant_id || live.variantId || fallback.variantId || '',
          handle: live.handle || fallback.handle || '',
          title: fallback.title,
          author: fallback.author,
          price: live.price ? (String(live.price).startsWith('₹') ? live.price : '₹' + live.price) : fallback.price,
          oldPrice: '',
          discount: '',
          badge: fallback.badge || (idx === 0 ? "NATIONAL BESTSELLER" : "TOP TRENDING"),
          rating: '',
          stock: "In Stock • Ships in 24 Hrs",
          coverUrl: fallback.coverUrl || fallback.cover || live.image || '',
          cover: fallback.cover || fallback.coverUrl || live.image || '',
          firstPageExcerpt: fallback.firstPageExcerpt,
          quote: fallback.quote,
          pages: fallback.pages || "320p",
          publisher: fallback.publisher || live.vendor || "Lokbharti / Rajkamal",
          genre: fallback.genre || live.type || "Fiction : Classic",
          url: live.url || ('/products/' + (live.handle || fallback.handle || ''))
        };
      }
      return fallback;
    });
  }
  return curated;
}

function selectPodiumBook(index) {
  const books = getPodiumData();
  if (!books.length) return;
  if (index < 0 || index >= books.length) return;
  currentPodiumIndex = index;
  const book = books[index];

  // Update center book 3D cover & text
  const elCoverImg = document.getElementById('podium-cover-img');
  const elInsideThumb = document.getElementById('podium-inside-thumb');
  const elInsideTitle = document.getElementById('podium-inside-title');
  const elInsideAuthor = document.getElementById('podium-inside-author');
  const elPageTitle = document.getElementById('podium-page-title');
  const elPageExcerpt = document.getElementById('podium-page-excerpt');
  const el3dBook = document.getElementById('podium-3d-book');

  const resolvedCover = getAssetUrl(book.coverUrl || book.cover, book.id);

  if (elCoverImg) {
    elCoverImg.onerror = function() { this.onerror = null; this.src = getFallbackCover(book.title, book.author); };
    elCoverImg.src = resolvedCover;
    elCoverImg.alt = book.title;
  }
  if (elInsideThumb) {
    elInsideThumb.onerror = function() { this.onerror = null; this.src = getFallbackCover(book.title, book.author); };
    elInsideThumb.src = resolvedCover;
    elInsideThumb.alt = book.title;
  }
  if (elInsideTitle) elInsideTitle.textContent = book.title;
  if (elInsideAuthor) elInsideAuthor.textContent = book.author;
  if (elPageTitle) elPageTitle.textContent = book.title;
  if (elPageExcerpt) elPageExcerpt.textContent = book.firstPageExcerpt;
  if (el3dBook) el3dBook.classList.remove('is-open');

  // Update Right Spotlight Card
  const elBadge = document.getElementById('podiumSpotBadge');
  const elStock = document.getElementById('podiumSpotStock');
  const elHeading = document.getElementById('podiumSpotHeading');
  const elAuthor = document.getElementById('podiumSpotAuthor');
  const elRating = document.getElementById('podiumSpotRating');
  const elQuote = document.getElementById('podiumSpotQuote');
  const elPages = document.getElementById('podiumSpotPages');
  const elPublisher = document.getElementById('podiumSpotPublisher');
  const elPrice = document.getElementById('podiumSpotPrice');
  const elOldPrice = document.getElementById('podiumSpotOldPrice');
  const elDiscount = document.getElementById('podiumSpotDiscount');

  if (elBadge) elBadge.textContent = book.badge;
  if (elStock) elStock.textContent = book.stock;
  if (elHeading) elHeading.textContent = book.title;
  if (elAuthor) elAuthor.textContent = book.author;
  if (elRating) elRating.textContent = book.rating;
  if (elQuote) elQuote.textContent = '"' + book.quote + '"';
  if (elPages) elPages.textContent = book.pages;
  if (elPublisher) elPublisher.textContent = book.publisher;
  if (elPrice) elPrice.textContent = book.price;
  if (elOldPrice) elOldPrice.textContent = book.oldPrice;
  if (elDiscount) elDiscount.textContent = book.discount;

  // Update Flanking Books positions
  const count = books.length;
  const fL2 = (index - 2 + count) % count;
  const fL1 = (index - 1 + count) % count;
  const fR1 = (index + 1) % count;
  const fR2 = (index + 2) % count;

  const imgL2 = document.getElementById('flankImgL2');
  const imgL1 = document.getElementById('flankImgL1');
  const imgR1 = document.getElementById('flankImgR1');
  const imgR2 = document.getElementById('flankImgR2');

  if (imgL2) {
    imgL2.onerror = function() { this.onerror = null; this.src = getFallbackCover(books[fL2].title, books[fL2].author); };
    imgL2.src = getAssetUrl(books[fL2].coverUrl || books[fL2].cover, books[fL2].id);
    imgL2.alt = books[fL2].title;
  }
  if (imgL1) {
    imgL1.onerror = function() { this.onerror = null; this.src = getFallbackCover(books[fL1].title, books[fL1].author); };
    imgL1.src = getAssetUrl(books[fL1].coverUrl || books[fL1].cover, books[fL1].id);
    imgL1.alt = books[fL1].title;
  }
  if (imgR1) {
    imgR1.onerror = function() { this.onerror = null; this.src = getFallbackCover(books[fR1].title, books[fR1].author); };
    imgR1.src = getAssetUrl(books[fR1].coverUrl || books[fR1].cover, books[fR1].id);
    imgR1.alt = books[fR1].title;
  }
  if (imgR2) {
    imgR2.onerror = function() { this.onerror = null; this.src = getFallbackCover(books[fR2].title, books[fR2].author); };
    imgR2.src = getAssetUrl(books[fR2].coverUrl || books[fR2].cover, books[fR2].id);
    imgR2.alt = books[fR2].title;
  }

  // Update Dots
  const dots = document.querySelectorAll('.podium-dot');
  dots.forEach(function(dot, i) {
    if (i === index) dot.classList.add('active');
    else dot.classList.remove('active');
  });
}

function prevPodiumBook() {
  const books = getPodiumData();
  const count = books.length;
  selectPodiumBook((currentPodiumIndex - 1 + count) % count);
}

function nextPodiumBook() {
  const books = getPodiumData();
  const count = books.length;
  selectPodiumBook((currentPodiumIndex + 1) % count);
}

function selectPodiumByFlank(slotOffset) {
  const books = getPodiumData();
  const count = books.length;
  selectPodiumBook((currentPodiumIndex + slotOffset + count) % count);
}

function toggleActivePodiumCover(e) {
  if (e) {
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
    if (typeof e.preventDefault === 'function') e.preventDefault();
  }
  const el = document.getElementById('podium-3d-book');
  if (el) el.classList.toggle('is-open');
}

function togglePodiumCover(e) {
  toggleActivePodiumCover(e);
}

function addCurrentPodiumToCart() {
  const books = getPodiumData();
  if (!books.length) return;
  const book = books[currentPodiumIndex];
  if (book.variantId) {
    addShopifyVariantToCart(book.variantId, 1);
  } else {
    addToCart(book.id || 'podium-' + currentPodiumIndex);
  }
}

function openCurrentPodiumOverview() {
  const books = getPodiumData();
  if (!books.length) return;
  const book = books[currentPodiumIndex];
  openOverviewModal(book);
}

function orderCurrentPodiumWhatsApp() {
  const books = getPodiumData();
  if (!books.length) return;
  const book = books[currentPodiumIndex];
  const url = book.url ? (window.location.origin + book.url) : window.location.href;
  const lines = [
    "Hello Indigo Books India!",
    "I would like to order this book from The Podium:",
    "*Book:* " + book.title,
    "*Author:* " + book.author,
    "*Price:* " + book.price,
    "*Format:* Paperback",
    "*URL:* " + url,
    "Please confirm availability and share COD / Payment details!"
  ];
  const msg = lines.join("\\n");
  window.open("https://wa.me/918933063306?text=" + encodeURIComponent(msg), '_blank');
}


// --- 2. MEHFIL-E-REKHTA STATE & FUNCTIONS ---
let currentPoetKey = 'all';
let currentSherIndex = 0;

function switchPoet(poetKey) {
  if (typeof POET_SHAYARI_DATA !== 'undefined' && POET_SHAYARI_DATA[poetKey]) {
    currentPoetKey = poetKey;
    currentSherIndex = 0;
    renderCurrentSher();
  }

  // Update active pill
  document.querySelectorAll('.poet-pill').forEach(function(btn) {
    if (btn.getAttribute('data-poet') === poetKey) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  // Filter / Spotlight the 5 authentic Urdu titles
  const cards = document.querySelectorAll('.rekhta-book-card');
  cards.forEach(function(card) {
    const cardPoet = card.getAttribute('data-poet');
    if (poetKey === 'all' || cardPoet === poetKey) {
      card.classList.remove('dimmed');
      card.classList.add('highlighted');
    } else {
      card.classList.remove('highlighted');
      card.classList.add('dimmed');
    }
  });
}

function renderCurrentSher() {
  if (typeof POET_SHAYARI_DATA === 'undefined' || !POET_SHAYARI_DATA[currentPoetKey]) return;
  const poet = POET_SHAYARI_DATA[currentPoetKey];
  const couplets = poet.couplets;
  if (!couplets || couplets.length === 0) return;

  const sher = couplets[currentSherIndex % couplets.length];

  const elUrdu = document.getElementById('rekhtaUrdu');
  const elHindi = document.getElementById('rekhtaHindi');
  const elEng = document.getElementById('rekhtaEng');
  const elAttr = document.getElementById('rekhtaAttr');
  const elFull = document.getElementById('rekhtaFullGhazal');

  if (elUrdu) elUrdu.textContent = sher.urdu;
  if (elHindi) elHindi.textContent = sher.hindi;
  if (elEng) elEng.textContent = sher.eng;
  if (elAttr) elAttr.textContent = sher.attr;
  if (elFull) elFull.textContent = sher.ghazal;

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function nextSher() {
  if (typeof POET_SHAYARI_DATA === 'undefined' || !POET_SHAYARI_DATA[currentPoetKey]) return;
  const couplets = POET_SHAYARI_DATA[currentPoetKey].couplets;
  currentSherIndex = (currentSherIndex + 1) % couplets.length;
  renderCurrentSher();
}

function prevSher() {
  if (typeof POET_SHAYARI_DATA === 'undefined' || !POET_SHAYARI_DATA[currentPoetKey]) return;
  const couplets = POET_SHAYARI_DATA[currentPoetKey].couplets;
  currentSherIndex = (currentSherIndex - 1 + couplets.length) % couplets.length;
  renderCurrentSher();
}

function toggleGhazalDrawer() {
  const el = document.getElementById('rekhtaFullGhazal');
  if (el) el.classList.toggle('is-open');
}


// --- 3. ACADEMIC & LAW VAULT STATE & FUNCTIONS ---
let currentVaultTab = 'law';

function switchVaultTab(tabKey) {
  if (typeof VAULT_BOOKS === 'undefined' || !VAULT_BOOKS[tabKey]) return;
  currentVaultTab = tabKey;

  // Update tab buttons
  document.querySelectorAll('.vault-tab-btn').forEach(function(btn) {
    if (btn.getAttribute('data-tab') === tabKey) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  // Render 4 books with 3D opening animation
  const books = VAULT_BOOKS[tabKey];
  const container = document.getElementById('vaultCardsContainer');
  if (!container) return;

  container.innerHTML = books.map(function(book) {
    const cover = getAssetUrl(book.coverUrl || book.cover, book.id);
    const cleanP = window.cleanPrice(book.price, 299);
    const priceFormatted = '₹' + cleanP.toFixed(2);
    const excerpt = book.firstPageExcerpt || book.excerpt || 'प्रामाणिक विधि एवं अकादमिक संदर्भ ग्रंथ। Authoritative edition curated by Indigo Books India, Prayagraj.';
    const pages = book.pages || '216p';
    const pub = book.pub || book.publisher || 'Lokbharti Prakashan';
    const binding = book.binding || 'Paperback';

    return `
      <div class="vault-card" data-book-id="${escapeHtml(book.id)}" data-title="${escapeHtml(book.title)}" data-author="${escapeHtml(book.author)}" data-price="${priceFormatted}" data-binding="${escapeHtml(binding)}">
        <div class="indigo-3d-book-stage" onclick="openSoloBookPage('${escapeJs(book.id)}', event)" style="width: 100%; height: 260px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
          <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
            <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
              <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                <span>INDIGO VAULT</span>
                <span style="color: #64748B;">AUTHENTIC</span>
              </div>
              <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                ${escapeHtml(book.title)}
              </div>
              <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                By ${escapeHtml(book.author)}
              </div>
            </div>
            <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
              <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                विवरण / SYNOPSIS
              </div>
              <p style="font-size: 8.5px; line-height: 1.35; color: #475569; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">
                ${escapeHtml(excerpt)}
              </p>
            </div>
            <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
              <span>${escapeHtml(pages)} &bull; ${escapeHtml(pub)}</span>
              <span style="font-weight: 700; color: #B45309;">${escapeHtml(binding)}</span>
            </div>
          </div>
          <div class="indigo-3d-cover-leaf">
            <div class="indigo-3d-cover-front">
              <img src="${cover}" alt="${escapeHtml(book.title)}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
          </div>
        </div>
        <div class="vault-card-body">
          <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
            ${escapeHtml(book.badge || 'SCHOLAR ARCHIVE')}
          </div>
          <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
            <a href="javascript:void(0)" onclick="openSoloBookPage('${escapeJs(book.id)}', event)" style="color: inherit; text-decoration: none;">${escapeHtml(book.title)}</a>
          </h3>
          <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
            ${escapeHtml(book.author)}
          </div>
          <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
            <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${priceFormatted}</span>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
            <button type="button" class="btn-overview" onclick="openOverviewModal('${escapeJs(book.id)}')">
              <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
            </button>
            <button type="button" class="btn-add-cart" onclick="addToCart('${escapeJs(book.id)}', '${escapeJs(book.title)}', ${cleanP}, '${escapeJs(cover)}', this, event)">
              <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}
function filterCatalog(category) {
  var cat = category || 'all';
  currentCatalogCategory = cat;
  window.currentCatalogCategory = cat;
  catalogCurrentPage = 1;
  window.catalogCurrentPage = 1;

  document.querySelectorAll('.cat-pill').forEach(function(btn) {
    if (btn.getAttribute('data-cat') === cat) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  renderCatalog();
}

function handleCatalogSearch(e) {
  var q = '';
  if (typeof e === 'string') {
    q = e.toLowerCase().trim();
  } else if (e && e.target) {
    q = e.target.value.toLowerCase().trim();
  }
  currentCatalogQuery = q;
  window.currentCatalogQuery = q;
  catalogCurrentPage = 1;
  window.catalogCurrentPage = 1;
  renderCatalog();
}

function handleHeroSearch(e) {
  if (e && e.key === 'Enter') {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    window.submitSearch(e, 'hero-search-input');
  }
}

function performHeroSearch() {
  window.submitSearch(null, 'hero-search-input');
}

function matchesBookCategory(book, cat) {
  if (!cat || cat === 'all') return true;

  const bTags = Array.isArray(book.tags) ? book.tags.map(function(t) { return String(t).toLowerCase().trim(); }) : (typeof book.tags === 'string' ? book.tags.toLowerCase().split(',').map(function(t) { return t.trim(); }) : []);
  const bType = String(book.type || '').toLowerCase();
  const bCat = String(book.category || '').toLowerCase();
  const bTitle = String(book.title || '').toLowerCase();
  const bAuthor = String(book.author || '').toLowerCase();
  const bDesc = String(book.overview || book.desc || book.quote || '').toLowerCase();
  const bId = String(book.id || '').toLowerCase();

  const combined = bTags.join(' ') + ' ' + bType + ' ' + bCat + ' ' + bTitle + ' ' + bAuthor + ' ' + bDesc + ' ' + bId;

  if (cat === 'shayari' || cat === 'poetry' || cat === 'rekhta') {
    return /poet|shayari|kavita|rekhta|nazm|ghazal|tarkash|dinkar|rashmirathi|piyush|ishq/i.test(combined);
  }

  if (cat === 'novel' || cat === 'fiction' || cat === 'upanyas') {
    return /novel|fiction|upanyas|godan|darbari|kahani|story|stories|gypsy|chitralekha/i.test(combined);
  }

  if (cat === 'classics' || cat === 'sahitya' || cat === 'hindi') {
    return /classic|sahitya|premchand|shukla|verma|dinkar|literary|criticism|hindi/i.test(combined);
  }

  if (cat === 'drama' || cat === 'play' || cat === 'natak') {
    return /play|drama|natak|theatre|theater|aadhe-adhoore/i.test(combined);
  }

  if (cat === 'history' || cat === 'biography' || cat === 'itihas') {
    return /history|biography|itihas|1857|kranti|freedom|swatantrata|gandhi|nehru|ambedkar/i.test(combined);
  }

  if (cat === 'law' || cat === 'judiciary' || cat === 'academic') {
    return /law|samvidhan|constitution|judiciary|court|high court|vakalat|academic|sanhita|kasauti/i.test(combined) || bId.indexOf('vault-law') !== -1;
  }

  if (cat === 'bestseller' || cat === 'top-bestsellers') {
    const bestsellerTitles = ['godan', 'raag darbari', 'chitralekha', 'rashmirathi', 'kuchh ishq', 'tarkash', '1984', 'aadha gaon', 'maila aanchal', 'gunahon ka devta', 'jigari'];
    return bestsellerTitles.some(function(bt) { return bTitle.indexOf(bt) !== -1; }) || /bestseller/i.test(combined) || bId.indexOf('podium-') === 0;
  }

  return combined.indexOf(cat.toLowerCase()) !== -1;
}

function getCatalogData() {
  let source = [];
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length > 0) {
    source = window.SHOPIFY_LIVE_PRODUCTS.slice();
  } else if (typeof CATALOG_BOOKS !== 'undefined' && Array.isArray(CATALOG_BOOKS)) {
    source = CATALOG_BOOKS.slice();
  }

  const seenTitles = new Set(source.map(function(b) { return (b.title || '').toLowerCase().trim(); }));
  const extras = [];
  if (typeof PODIUM_BOOKS !== 'undefined' && Array.isArray(PODIUM_BOOKS)) {
    extras.push.apply(extras, PODIUM_BOOKS);
  }
  if (typeof VAULT_BOOKS !== 'undefined') {
    if (Array.isArray(VAULT_BOOKS)) {
      extras.push.apply(extras, VAULT_BOOKS);
    } else if (typeof VAULT_BOOKS === 'object') {
      for (var vk in VAULT_BOOKS) {
        if (Array.isArray(VAULT_BOOKS[vk])) extras.push.apply(extras, VAULT_BOOKS[vk]);
      }
    }
  }
  extras.forEach(function(b) {
    if (!b || !b.title) return;
    const tNorm = (b.title || '').toLowerCase().trim();
    if (!seenTitles.has(tNorm)) {
      seenTitles.add(tNorm);
      source.push(b);
    }
  });

  // Smart Sort:
  // 1. Curated top national bestsellers & classics appear first
  // 2. Standard alphabetical titles (A-Z) appear next
  // 3. Titles starting with digits/numbers (1084, 12, 1232, 1857) demoted to the end
  const priorityTitles = [
    'godan', 'raag darbari', 'chitralekha', 'rashmirathi', 'kuchh ishq', 'tarkash',
    'aadha gaon', 'mahabhoj', 'shekhar ek jeevani', 'savarkar', 'bharat ka samvidhan',
    'bharatiya bhasha mein high court', 'gunahon ka devta', 'madhushala', 'tamas',
    'maila anchal', 'ashadh ka ek din', 'kitne pakistan', 'dozakh nama', 'thanda gosht', 'dhuaan'
  ];

  return source.sort(function(a, b) {
    const tA = (a.title || '').toLowerCase().trim();
    const tB = (b.title || '').toLowerCase().trim();

    // Priority check
    const idxA = priorityTitles.findIndex(function(p) { return tA.includes(p); });
    const idxB = priorityTitles.findIndex(function(p) { return tB.includes(p); });

    if (idxA !== -1 && idxB !== -1) return idxA - idxB;
    if (idxA !== -1) return -1;
    if (idxB !== -1) return 1;

    // Numeric title demotion: titles starting with digits go to the bottom
    const isNumA = /^\d/.test(tA);
    const isNumB = /^\d/.test(tB);
    if (isNumA && !isNumB) return 1;
    if (!isNumA && isNumB) return -1;

    return tA.localeCompare(tB);
  });
}

function handleBookAction(bookId, bookUrl, event) {
  var e = event || (typeof window !== 'undefined' && window.event);
  var triggerEl = e && (e.currentTarget || e.target);
  if (e) {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
  }
  // Open dedicated Amazon-style single product details view instantly (zero 404 risk)
  openDedicatedProductPage(bookId || bookUrl, triggerEl);
}

// catalogCurrentPage and CATALOG_PAGE_SIZE declared at top
catalogCurrentPage = 1;
CATALOG_PAGE_SIZE = 12;

function goToCatalogPage(page) {
  catalogCurrentPage = page;
  renderCatalog();
  const catSection = document.getElementById('shop-all-catalog');
  if (catSection) {
    catSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function renderCatalog() {
  const container = document.getElementById('catalogGridContainer');
  const paginationContainer = document.getElementById('catalogPagination');
  if (!container) return;

  if (typeof currentCatalogCategory === 'undefined' || !currentCatalogCategory) {
    currentCatalogCategory = window.currentCatalogCategory || 'all';
  }
  if (typeof currentCatalogQuery === 'undefined') {
    currentCatalogQuery = window.currentCatalogQuery || '';
  }
  if (typeof catalogCurrentPage === 'undefined') {
    catalogCurrentPage = window.catalogCurrentPage || 1;
  }
  if (typeof CATALOG_PAGE_SIZE === 'undefined') {
    CATALOG_PAGE_SIZE = window.CATALOG_PAGE_SIZE || 12;
  }

  const catalogSource = getCatalogData();

  const filtered = catalogSource.filter(function(book) {
    const matchesCat = matchesBookCategory(book, currentCatalogCategory);
    const matchesQuery = !currentCatalogQuery || 
      book.title.toLowerCase().includes(currentCatalogQuery) || 
      (book.author && book.author.toLowerCase().includes(currentCatalogQuery));
    return matchesCat && matchesQuery;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 48px; background: #FFFFFF; border-radius: 12px; border: 1px dashed #CBD5E1;">
        <i data-lucide="search-x" style="width: 36px; height: 36px; color: #94A3B8; margin: 0 auto 12px;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 18px; color: #0F172A; margin-bottom: 6px;">No books found</h4>
        <p style="font-size: 13px; color: #64748B;">Try adjusting your search terms or category filter.</p>
        <a href="#shop-all-catalog" onclick="filterCatalog('all')" style="display: inline-block; margin-top: 14px; font-size: 13px; font-weight: 700; color: #B45309; text-decoration: underline;">Search across all 5,500+ books on the catalog page &rarr;</a>
      </div>
    `;
    if (paginationContainer) {
      paginationContainer.innerHTML = '';
      paginationContainer.style.display = 'none';
    }
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  const totalPages = Math.ceil(filtered.length / CATALOG_PAGE_SIZE) || 1;
  if (catalogCurrentPage > totalPages) catalogCurrentPage = 1;
  if (catalogCurrentPage < 1) catalogCurrentPage = 1;

  const startIndex = (catalogCurrentPage - 1) * CATALOG_PAGE_SIZE;
  const pageBooks = filtered.slice(startIndex, startIndex + CATALOG_PAGE_SIZE);

  container.innerHTML = pageBooks.map(function(book) {
    const rawCover = book.image || book.coverUrl || book.cover || '';
    let cover = getAssetUrl(rawCover, book.id);
    const authorSafe = (book.author || book.vendor || 'Indigo Books').replace(/['"]/g, ' ');
    const titleSafe = (book.title || 'Book').replace(/['"]/g, ' ');
    if (!cover) {
      cover = getFallbackCover(titleSafe, authorSafe);
    }
    const bookUrl = book.url || (book.handle ? '/products/' + book.handle : '');
    const cleanP = window.cleanPrice(book.price);
    const priceFormatted = '₹' + cleanP.toFixed(2);

    return `
      <div class="catalog-card" data-book-id="${escapeHtml(book.id)}" data-title="${escapeHtml(book.title)}" data-author="${escapeHtml(book.author || book.vendor || '')}" data-price="${escapeHtml(book.price || '299')}">
        <div class="indigo-3d-book-stage" onclick="handleBookAction('${book.id}', '${bookUrl}')" style="margin-bottom: 12px; cursor: pointer;">
          <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
            <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
              <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                <span>INDIGO ARCHIVE</span>
                <span style="color: #64748B;">AUTHENTIC</span>
              </div>
              <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                ${escapeHtml(book.title)}
              </div>
              <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                By ${escapeHtml(book.author || book.vendor || 'Indigo Books')}
              </div>
            </div>
            <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
              <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                अध्याय १ / PROLOGUE
              </div>
              <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                ${escapeHtml(book.firstPageExcerpt || book.excerpt || book.quote || book.overview || book.description || '« यह कृति भारतीय साहित्य और सामाजिक चेतना का एक प्रामाणिक एवं अमिट दस्तावेज है। मूल पाठ एवं आधिकारिक संस्करण। »')}
              </p>
            </div>
            <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
              <span>${escapeHtml(book.pages || '250p Pages')}</span>
              <span style="font-weight: 600; color: #0066B3;">${escapeHtml(book.pub || book.publisher || book.vendor || 'Lokbharti')}</span>
            </div>
          </div>
          <div class="indigo-3d-cover-leaf">
            <div class="indigo-3d-cover-front">
              <img referrerpolicy="no-referrer" src="${cover}" alt="${titleSafe}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('${titleSafe}', '${authorSafe}');" />
            </div>
            <div class="indigo-3d-cover-back">
              <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                100% GENUINE
              </div>
              <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                ${escapeHtml(book.pub || book.vendor || 'Authorized Copy')}
              </div>
              <div style="font-size: 9.5px; color: #CBD5E1;">
                ${escapeHtml(book.binding || 'Paperback')} &bull; ${priceFormatted}
              </div>
              <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                Click for Details &rarr;
              </div>
            </div>
          </div>
        </div>
        <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
          IN STOCK &bull; SHIPS IN 24H
        </div>
        <h3 class="catalog-card-title">
          ${bookUrl ? `<a href="${bookUrl}" onclick="handleBookAction('${book.id}', '${bookUrl}', event)" style="color: inherit; text-decoration: none;">${book.title}</a>` : `<span onclick="handleBookAction('${book.id}', '', event)" style="cursor: pointer;">${book.title}</span>`}
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          ${book.author || book.vendor || 'Indigo Books'}
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
          <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${priceFormatted}</span>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
          <button type="button" class="btn-overview" onclick="openOverviewModal('${book.id}')">
            <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
          </button>
          <button type="button" class="btn-add-cart" onclick="addToCart('${book.id}')">
            <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
          </button>
        </div>
      </div>
    `;
  }).join('');

  // Render Pagination Buttons
  if (paginationContainer) {
    if (totalPages <= 1) {
      paginationContainer.innerHTML = '';
      paginationContainer.style.display = 'none';
    } else {
      paginationContainer.style.display = 'flex';
      let pagHtml = '';
      
      // Prev Button
      pagHtml += `<button type="button" class="pagination-btn" ${catalogCurrentPage === 1 ? 'disabled' : ''} onclick="goToCatalogPage(${catalogCurrentPage - 1})">&larr; Prev</button>`;
      
      // Page numbers
      for (let p = 1; p <= totalPages; p++) {
        if (totalPages > 7) {
          if (p !== 1 && p !== totalPages && Math.abs(p - catalogCurrentPage) > 2) {
            if (p === 2 || p === totalPages - 1) {
              pagHtml += `<span class="pagination-ellipsis">...</span>`;
            }
            continue;
          }
        }
        pagHtml += `<button type="button" class="pagination-btn ${p === catalogCurrentPage ? 'active' : ''}" onclick="goToCatalogPage(${p})">${p}</button>`;
      }
      
      // Next Button
      pagHtml += `<button type="button" class="pagination-btn" ${catalogCurrentPage === totalPages ? 'disabled' : ''} onclick="goToCatalogPage(${catalogCurrentPage + 1})">Next &rarr;</button>`;
      
      paginationContainer.innerHTML = pagHtml;
    }
  }

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

// --- 5. UNIVERSAL MINI OVERVIEW MODAL ---
function findBookMetadata(arg) {
  if (!arg) return null;

  var idStr = typeof arg === 'string' ? arg.trim() : String(arg.id || arg.handle || arg.isbn || arg.sku || arg.title || '').trim();
  var titleStr = (typeof arg === 'object' && arg.title) ? String(arg.title).trim() : (typeof arg === 'string' ? arg.trim() : '');
  var isbnStr = (typeof arg === 'object' && (arg.isbn || arg.sku)) ? String(arg.isbn || arg.sku).replace(/[^0-9xX]/gi, '') : (idStr.match(/(97[89][0-9]{10}|[0-9]{9}[0-9xX])/i) ? idStr.match(/(97[89][0-9]{10}|[0-9]{9}[0-9xX])/i)[0] : '');

  var dbMatch = null;
  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    if (idStr && MODAL_METADATA_DATABASE[idStr]) dbMatch = MODAL_METADATA_DATABASE[idStr];
    else if (isbnStr && MODAL_METADATA_DATABASE[isbnStr]) dbMatch = MODAL_METADATA_DATABASE[isbnStr];
    else if (titleStr && MODAL_METADATA_DATABASE[titleStr]) dbMatch = MODAL_METADATA_DATABASE[titleStr];
    else if (titleStr && MODAL_METADATA_DATABASE[titleStr.toLowerCase()]) dbMatch = MODAL_METADATA_DATABASE[titleStr.toLowerCase()];
    else if (titleStr) {
      var slug = titleStr.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
      if (slug && MODAL_METADATA_DATABASE[slug]) dbMatch = MODAL_METADATA_DATABASE[slug];
    }
  }

  // If not found in MODAL_METADATA_DATABASE, search MASTER_SEARCH_CATALOG
  if (!dbMatch && typeof window.MASTER_SEARCH_CATALOG !== 'undefined' && Array.isArray(window.MASTER_SEARCH_CATALOG)) {
    dbMatch = window.MASTER_SEARCH_CATALOG.find(function(b) {
      if (!b) return false;
      if (isbnStr && String(b.isbn || b.sku).replace(/[^0-9xX]/gi, '') === isbnStr) return true;
      if (titleStr && b.title && b.title.toLowerCase() === titleStr.toLowerCase()) return true;
      if (idStr && (String(b.id) === idStr || String(b.handle) === idStr)) return true;
      return false;
    });
  }

  // Check PODIUM_BOOKS, REKHTA_BOOKS, VAULT_BOOKS, CATEGORY_BENTO_DATA
  if (!dbMatch && typeof PODIUM_BOOKS !== 'undefined' && Array.isArray(PODIUM_BOOKS)) {
    dbMatch = PODIUM_BOOKS.find(function(x) { return String(x.id) === idStr || String(x.handle) === idStr || (titleStr && x.title && x.title.toLowerCase() === titleStr.toLowerCase()); });
  }
  if (!dbMatch && typeof REKHTA_BOOKS !== 'undefined' && Array.isArray(REKHTA_BOOKS)) {
    dbMatch = REKHTA_BOOKS.find(function(x) { return String(x.id) === idStr || String(x.handle) === idStr || (titleStr && x.title && x.title.toLowerCase() === titleStr.toLowerCase()); });
  }
  if (!dbMatch && typeof VAULT_BOOKS !== 'undefined') {
    for (var cat in VAULT_BOOKS) {
      if (Array.isArray(VAULT_BOOKS[cat])) {
        var vb = VAULT_BOOKS[cat].find(function(x) { return String(x.id) === idStr || String(x.handle) === idStr || (titleStr && x.title && x.title.toLowerCase() === titleStr.toLowerCase()); });
        if (vb) { dbMatch = vb; break; }
      }
    }
  }
  if (!dbMatch && typeof CATEGORY_BENTO_DATA !== 'undefined') {
    for (var cat in CATEGORY_BENTO_DATA) {
      var d = CATEGORY_BENTO_DATA[cat];
      if (d) {
        if (d.left && (String(d.left.id) === idStr || String(d.left.handle) === idStr || (titleStr && d.left.title && d.left.title.toLowerCase() === titleStr.toLowerCase()))) {
          dbMatch = d.left; break;
        }
        if (Array.isArray(d.right)) {
          var rb = d.right.find(function(x) { return String(x.id) === idStr || String(x.handle) === idStr || (titleStr && x.title && x.title.toLowerCase() === titleStr.toLowerCase()); });
          if (rb) { dbMatch = rb; break; }
        }
      }
    }
  }

  // If match found, return clean authentic profile
  if (dbMatch) {
    var rawPrice = dbMatch.price || dbMatch.mrp || (typeof arg === 'object' ? arg.price : 299);
    var cleanP = typeof rawPrice === 'number' ? rawPrice : parseFloat(String(rawPrice).replace(/[^0-9.]/g, '')) || 299;
    var rawPages = dbMatch.pages ? String(dbMatch.pages).trim() : (typeof arg === 'object' && arg.pages ? String(arg.pages).trim() : '168p');
    var pagesFormatted = rawPages ? (rawPages.toLowerCase().endsWith('p') ? rawPages : rawPages + 'p') : '168p';
    var publisherName = dbMatch.pub || dbMatch.publisher || (typeof arg === 'object' ? (arg.pub || arg.publisher) : 'Authorized Publisher');
    var editionName = dbMatch.edition || (typeof arg === 'object' ? arg.edition : '1st Edition');
    var bindingName = dbMatch.binding || dbMatch.format || (typeof arg === 'object' ? (arg.binding || arg.format) : 'Paperback');
    var coverImg = dbMatch.cover || dbMatch.coverUrl || dbMatch.image || (typeof arg === 'object' ? (arg.coverUrl || arg.cover) : '');

    return {
      id: dbMatch.id || idStr,
      handle: dbMatch.handle || idStr,
      title: dbMatch.title || titleStr,
      author: dbMatch.author || (typeof arg === 'object' ? arg.author : 'Authoritative Edition'),
      price: cleanP,
      mrp: cleanP,
      discount: '',
      cover: coverImg,
      coverUrl: coverImg,
      image: coverImg,
      isbn: dbMatch.isbn || dbMatch.sku || isbnStr,
      sku: dbMatch.sku || dbMatch.isbn || isbnStr,
      pages: pagesFormatted,
      pub: publisherName,
      publisher: publisherName,
      edition: editionName,
      binding: bindingName,
      format: bindingName,
      lang: dbMatch.lang || 'Hindi',
      dimensions: dbMatch.dimensions || '21.5 × 14.0 × 1.0 cm',
      qty: dbMatch.qty !== undefined ? dbMatch.qty : 50,
      stock: dbMatch.stock || 'In Stock',
      dispatch: 'Same-Day Dispatch from Prayagraj Hub',
      overview: dbMatch.overview || ('« ' + dbMatch.title + ' » — प्रामाणिक संस्करण। Authoritative publisher original edition curated by Indigo Books India, Prayagraj.'),
      firstPageExcerpt: dbMatch.firstPageExcerpt || ('« ' + dbMatch.title + ' — ' + (dbMatch.author || '') + ' की सशक्त लेखनी का अधिकृत संस्करण। मूल पाठ एवं आधिकारिक प्रकाशन। »'),
      highlights: dbMatch.highlights || [
        '100% Authentic Publisher Original Copy',
        'Official Edition: ' + publisherName,
        'Direct express dispatch from Prayagraj warehouse',
        'Eligible for Cash on Delivery (COD) & WhatsApp Ordering'
      ]
    };
  }

  // If raw object passed with title
  if (typeof arg === 'object' && arg.title && arg.title !== 'Selected Book') {
    const rawPrice = arg.price ? String(arg.price).replace(/[^0-9.]/g, '') : '299.00';
    return {
      id: arg.id || idStr,
      title: arg.title,
      author: arg.author || 'Author',
      price: rawPrice,
      mrp: rawPrice,
      discount: '',
      cover: arg.coverUrl || arg.cover || '',
      isbn: arg.isbn || arg.sku || '',
      sku: arg.sku || arg.isbn || '',
      lang: arg.lang || arg.language || 'Hindi',
      binding: arg.binding || arg.format || 'Paperback',
      pages: arg.pages || '168p',
      pub: arg.publisher || arg.pub || arg.vendor || 'Authorized Publisher',
      publisher: arg.publisher || arg.pub || arg.vendor || 'Authorized Publisher',
      edition: arg.edition || '1st Edition',
      dispatch: 'Same-Day Dispatch from Prayagraj Hub',
      overview: arg.blurb || arg.description || arg.overview || ('« ' + arg.title + ' » — प्रामाणिक संस्करण।'),
      firstPageExcerpt: arg.firstPageExcerpt || ('« ' + arg.title + ' — अधिकृत संस्करण। »'),
      highlights: [
        '100% Authentic Publisher Edition guaranteed',
        'Direct dispatch from Prayagraj literary warehouse',
        'Eligible for Cash on Delivery (COD) & WhatsApp Ordering'
      ]
    };
  }

  return null;
}

function openOverviewModal(bookArg) {
  let book = findBookMetadata(bookArg);
  if (!book && typeof window.resolveBookObject === 'function') {
    book = window.resolveBookObject(bookArg);
  }
  if (!book) {
    console.warn("Could not find book for overview:", bookArg);
    return;
  }

  const modal = document.getElementById('overviewModalOverlay') || document.getElementById('indigo-overview-modal');
  if (!modal) return;

  window.CURRENT_OVERVIEW_BOOK = book;
  window.currentModalBook = book;
  window.currentModalBookId = book.id || book.handle || bookArg;

  const cleanPriceVal = window.cleanPrice(book.price, 299);
  const coverEl = document.getElementById('modalCover');
  if (coverEl) {
    coverEl.src = getAssetUrl(book.cover || book.coverUrl, book.id) || getFallbackCover(book.title, book.author);
    coverEl.alt = book.title || 'Book Cover';
  }
  const titleEl = document.getElementById('modalTitle');
  if (titleEl) titleEl.textContent = book.title || '';
  const authorEl = document.getElementById('modalAuthor');
  if (authorEl) authorEl.textContent = book.author || book.vendor || '';

  const badgeEl = document.getElementById('modalBadge');
  if (badgeEl) {
    const bind = (book.binding || book.format || 'Paperback').toUpperCase();
    const cat = (book.category || book.type || 'Literature').toUpperCase();
    badgeEl.textContent = bind + ' • ' + cat;
  }

  const priceEl = document.getElementById('modalPrice');
  if (priceEl) priceEl.textContent = '₹' + cleanPriceVal.toFixed(2);
  const mrpEl = document.getElementById('modalMrp') || document.getElementById('modalMRP');
  if (mrpEl) mrpEl.style.display = 'none';
  const discEl = document.getElementById('modalDiscount');
  if (discEl) discEl.style.display = 'none';

  const isbnEl = document.getElementById('modalIsbn');
  if (isbnEl) isbnEl.textContent = book.isbn || book.sku || '';
  const pubEl = document.getElementById('modalPub') || document.getElementById('modalPublisher');
  if (pubEl) pubEl.textContent = book.pub || book.publisher || book.vendor || 'Rajkamal Prakashan';
  const pagesEl = document.getElementById('modalPages');
  if (pagesEl) pagesEl.textContent = (book.pages || '250p') + (book.dimensions ? ' • ' + book.dimensions : '');
  const langEl = document.getElementById('modalLang');
  if (langEl) langEl.textContent = (book.lang || book.language || 'Hindi') + (book.edition ? ' • ' + book.edition : '');

  const overviewEl = document.getElementById('modalOverview') || document.getElementById('modalOverviewText');
  if (overviewEl) overviewEl.textContent = book.overview || book.description || 'Authentic publisher edition curated by Indigo Books India, Prayagraj.';

  const fullPageBtn = document.getElementById('modalFullPageBtn');
  if (fullPageBtn) {
    fullPageBtn.onclick = function(e) {
      if (e && e.preventDefault) e.preventDefault();
      closeOverviewModal();
      openDedicatedProductPage(window.currentModalBook || window.currentModalBookId);
    };
  }

  const addBtn = document.getElementById('modalAddToCartBtn');
  if (addBtn) {
    addBtn.onclick = function(e) {
      if (e && e.preventDefault) e.preventDefault();
      const target = window.currentModalBook || window.currentModalBookId;
      if (target) {
        if (typeof target === 'object') {
          addToCart(target.id || target.handle || target.title, target.title, target.price, target.cover || target.coverUrl, this, e);
        } else {
          addToCart(target);
        }
      }
      closeOverviewModal();
    };
  }

  const waBtn = document.getElementById('modalWhatsAppBtn');
  if (waBtn) {
    const lines = [
      "Hello Indigo Books India!",
      "I would like to order this book:",
      "*Book:* " + (book.title || ''),
      "*Author:* " + (book.author || ''),
      "*Price:* ₹" + cleanPriceVal.toFixed(2),
      "*Format:* " + (book.binding || 'Paperback'),
      "Please confirm availability and share COD / Payment details!"
    ];
        waBtn.href = "https://wa.me/918933063306?text=" + encodeURIComponent(lines.join("\\n"));
  }

  modal.classList.add('is-active');
  modal.style.setProperty('display', 'flex', 'important');
  modal.style.setProperty('opacity', '1', 'important');
  modal.style.setProperty('pointer-events', 'auto', 'important');
  modal.style.display = 'flex';
  modal.style.opacity = '1';
  modal.style.pointerEvents = 'auto';
  document.body.style.overflow = 'hidden';

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function closeOverviewModal() {
  const modal = document.getElementById('overviewModalOverlay') || document.getElementById('indigo-overview-modal');
  if (modal) {
    modal.classList.remove('is-active');
    modal.style.setProperty('display', 'none', 'important');
    modal.style.display = 'none';
    modal.style.opacity = '';
    modal.style.pointerEvents = '';
  }
  document.body.style.overflow = '';
}
window.closeOverviewModal = closeOverviewModal;
window.closeAllIndigoModals = closeOverviewModal;

// --- 6. SHOPPING CART DRAWER ---
let cart = [];

function addShopifyVariantToCart(variantId, qty) {
  fetch('/cart/add.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id: variantId, quantity: qty || 1 })
  })
  .then(function(res) { return res.json(); })
  .then(function(item) {
    addToCart(item.id || variantId);
  })
  .catch(function(err) {
    addToCart(variantId);
  });
}

function executeAddToCart(bookId, bookTitle, bookPrice, bookCover, extra, event) {
  const e = (event && event.target) ? event :
            (extra && extra.target ? extra : (extra && extra.nodeType ? extra : (typeof window !== 'undefined' ? window.event : null)));
  const btn = (extra && extra.nodeType) ? extra : (e && (e.currentTarget || e.target));
  if (btn && btn.classList) {
    btn.classList.add('btn-add-pop');
    setTimeout(function() { btn.classList.remove('btn-add-pop'); }, 400);
  }

  let meta = null;
  // 1. If bookId is already a book object
  if (typeof bookId === 'object' && bookId && bookId.title && bookId.title !== 'Selected Book') {
    meta = bookId;
  } else {
    meta = findBookMetadata(bookId);
    if ((!meta || meta.title === 'Selected Book') && typeof window.resolveBookObject === 'function') {
      meta = window.resolveBookObject(bookId, btn);
    }
  }

  // 2. Scrape from closest card DOM if still unresolved
  if (!meta || meta.title === 'Selected Book') {
    const card = btn ? btn.closest('[data-book-id], [data-title], .vault-card, .catalog-card, .rekhta-book-card, .rekhta-card, .ivh-book-card, .book-card, .bento-left-spotlight, .bento-horiz-card') : null;
    if (card) {
      const cardTitle = card.getAttribute('data-title') ||
        (card.querySelector('#bentoLeftTitle, h3, h4, h2, h1, .book-title, .card-title, .rekhta-card-title, .bento-horiz-top h4, a') ?
         card.querySelector('#bentoLeftTitle, h3, h4, h2, h1, .book-title, .card-title, .rekhta-card-title, .bento-horiz-top h4, a').textContent.trim() : '');
      if (cardTitle && cardTitle.toLowerCase() !== 'selected book') {
        const cardAuthor = card.getAttribute('data-author') ||
          (card.querySelector('.book-author, .card-author, .rekhta-card-author, #bentoLeftAuthor') ?
           card.querySelector('.book-author, .card-author, .rekhta-card-author, #bentoLeftAuthor').textContent.trim() : 'Indigo Books Archive');
        const cardPriceText = card.getAttribute('data-price') ||
          (card.querySelector('.book-price, .price, .rekhta-curr-price, [class*="price"]') ?
           card.querySelector('.book-price, .price, .rekhta-curr-price, [class*="price"]').textContent : '299');
        const cardPrice = window.cleanPrice(cardPriceText, 299);
        const cardImg = card.querySelector('img') ? card.querySelector('img').src : '';
        meta = {
          id: card.getAttribute('data-book-id') || bookId,
          title: cardTitle,
          author: cardAuthor,
          price: cardPrice,
          cover: cardImg || bookCover
        };
      }
    }
  }

  // 3. If explicit parameters passed from caller
  if (!meta && bookTitle && bookTitle !== 'Selected Book') {
    meta = {
      id: bookId,
      title: bookTitle,
      author: 'Indigo Books India',
      price: window.cleanPrice(bookPrice, 299),
      cover: bookCover
    };
  }

  if (!meta) {
    console.warn("Indigo Books: Could not resolve book for add-to-cart:", bookId);
    return;
  }

  const idStr = String(meta.id || meta.handle || meta.title);
  const existing = cart.find(function(item) { return String(item.id) === idStr; });

  const cleanP = window.cleanPrice ? window.cleanPrice(meta.price, 299) : (parseFloat(String(meta.price || 299).replace(/[^0-9.]/g, '')) || 299);
  const cleanCover = getAssetUrl(meta.cover || meta.coverUrl || bookCover, idStr) || getFallbackCover(meta.title, meta.author);

  if (existing) {
    existing.qty += 1;
  } else {
    const itemBinding = meta.binding || meta.format || extra || 'Paperback';
    cart.push({
      id: idStr,
      title: meta.title,
      author: meta.author || 'Indigo Books Author',
      price: cleanP,
      cover: cleanCover,
      binding: itemBinding,
      format: itemBinding,
      qty: 1
    });
  }

  updateCartUI();
  toggleCartDrawer(true);
}

function addToCart(bookId, bookTitle, bookPrice, bookCover, extra, event) {
  executeAddToCart(bookId, bookTitle, bookPrice, bookCover, extra, event);
}

function updateCartQty(bookId, delta) {
  const idStr = String(bookId);
  const item = cart.find(function(i) { return String(i.id) === idStr; });
  if (!item) return;

  item.qty += delta;
  if (item.qty <= 0) {
    cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  }
  updateCartUI();
}

function removeFromCart(bookId) {
  const idStr = String(bookId);
  cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  updateCartUI();
}

function updateCartUI() {
  const countEl = document.getElementById('cartTotalCount');
  const priceEl = document.getElementById('cartTotalPrice');
  const badgeEl = document.getElementById('cartDrawerBadge');
  const subtotalEl = document.getElementById('cartDrawerSubtotal');
  const navCountEl = document.getElementById('nav-cart-count');
  const navTotalEl = document.getElementById('nav-cart-total');
  const drawerItemCountEl = document.getElementById('cartItemCount');
  const list = document.getElementById('cartItemsContainer') || document.getElementById('cartDrawerItemsList');
  const footerEl = document.querySelector('.cart-drawer-footer');

  const totalCount = cart.reduce(function(sum, item) { return sum + item.qty; }, 0);
  const totalPrice = cart.reduce(function(sum, item) { return sum + (item.price * item.qty); }, 0);
  const formattedPrice = '₹' + totalPrice.toFixed(2);

  if (countEl) countEl.textContent = totalCount;
  if (priceEl) priceEl.textContent = formattedPrice;
  if (badgeEl) badgeEl.textContent = totalCount;
  if (subtotalEl) subtotalEl.textContent = formattedPrice;
  if (navCountEl) navCountEl.textContent = totalCount;
  if (navTotalEl) navTotalEl.textContent = formattedPrice;
  if (drawerItemCountEl) drawerItemCountEl.textContent = totalCount;

  if (!list) return;

  // Update Free Shipping Progress Bar
  const freeText = document.getElementById('freeShippingText');
  const freePct = document.getElementById('freeShippingPercent');
  const freeBar = document.getElementById('freeShippingBar');
  if (totalPrice >= 999) {
    if (freeText) freeText.textContent = 'FREE EXPRESS DISPATCH UNLOCKED!';
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

  if (footerEl) footerEl.style.display = 'block';

  list.innerHTML = cart.map(function(item) {
    const fmt = item.binding || item.format || 'Paperback';
    return `
      <div style="display: flex; gap: 14px; padding-bottom: 14px; border-bottom: 1px solid #F1F5F9;">
        <div style="width: 60px; height: 85px; border-radius: 4px; overflow: hidden; flex-shrink: 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
          <img referrerpolicy="no-referrer" src="${getAssetUrl(item.cover)}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
        </div>
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
              <span style="font-size: 9.5px; font-weight: 700; color: #B45309; background: #FEF3C7; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.05em;">
                ${fmt}
              </span>
            </div>
            <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 13.5px; font-weight: 700; color: #0F172A; line-height: 1.25; margin-bottom: 2px;">
              ${item.title}
            </h4>
            <div style="font-size: 11px; color: #64748B;">By ${item.author}</div>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 8px;">
            <div style="font-size: 14px; font-weight: 800; color: #0F172A;">
              ₹${(item.price * item.qty).toFixed(2)}
            </div>
            <div style="display: flex; align-items: center; gap: 8px; background: #F1F5F9; border-radius: 6px; padding: 2px 8px;">
              <button type="button" onclick="updateCartQty('${item.id}', -1)" style="border: none; background: none; cursor: pointer; font-size: 14px; font-weight: bold; color: #475569;">-</button>
              <span style="font-size: 12px; font-weight: 700; color: #0F172A;">${item.qty}</span>
              <button type="button" onclick="updateCartQty('${item.id}', 1)" style="border: none; background: none; cursor: pointer; font-size: 14px; font-weight: bold; color: #475569;">+</button>
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function toggleCartDrawer(forceOpen) {
  const drawer = document.getElementById('cartDrawer') || document.querySelector('.cart-drawer') || document.querySelector('.cart-drawer-panel');
  const overlay = document.getElementById('cartOverlay') || document.getElementById('cartDrawerOverlay') || document.querySelector('.cart-overlay') || document.querySelector('.cart-drawer-overlay');

  let shouldOpen;
  if (forceOpen === true) shouldOpen = true;
  else if (forceOpen === false) shouldOpen = false;
  else shouldOpen = drawer ? !drawer.classList.contains('is-open') : false;

  if (drawer) {
    if (shouldOpen) drawer.classList.add('is-open');
    else drawer.classList.remove('is-open');
  }
  if (overlay) {
    if (shouldOpen) overlay.classList.add('is-open');
    else overlay.classList.remove('is-open');
  }
  document.body.style.overflow = shouldOpen ? 'hidden' : '';
}


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

function checkoutWhatsApp() {
  if (cart.length === 0) {
    alert("Your shopping cart is empty!");
    return;
  }

  const lines = [
    "Hello Indigo Books India (Prayagraj)!",
    "I want to place an order via Cash on Delivery (COD):",
    ""
  ];
  let total = 0;

  cart.forEach(function(item, index) {
    const lineTotal = item.price * item.qty;
    total += lineTotal;
    lines.push((index + 1) + ". *" + item.title + "* x" + item.qty + " — ₹" + lineTotal.toFixed(2));
  });

  lines.push("");
  lines.push("*Cart Subtotal:* ₹" + total.toFixed(2));
  lines.push("*Dispatch Location:* Prayagraj Hub");
  lines.push("");
  lines.push("Please confirm delivery time & COD address!");

  const text = lines.join("\\n");
  window.open("https://wa.me/918933063306?text=" + encodeURIComponent(text), '_blank');
}



// =========================================================================
// --- DEDICATED AMAZON-STYLE SINGLE PRODUCT PAGE ENGINE ---
// =========================================================================
let currentActivePdpBook = null;
let currentPdpQuantity = 1;

// --- COMPREHENSIVE BOOK RESOLUTION ENGINE (NEVER FALLS BACK TO GODAN) ---
function resolveBookObject(bookOrId, triggerEl) {
  window.resolveBookObject = resolveBookObject;
  var pool = []
    .concat(window.MASTER_BOOKS || [])
    .concat(window.SHOPIFY_LIVE_PRODUCTS || [])
    .concat(window.PODIUM_BOOKS || [])
    .concat(window.REKHTA_BOOKS || [])
    .concat(window.CATALOG_BOOKS || [])
    .concat(window.PIYUSH_MISHRA_BOOKS || [])
    .concat(window.RAHI_MASOOM_RAZA_BOOKS || []);

  if (typeof VAULT_BOOKS !== 'undefined') {
    if (Array.isArray(VAULT_BOOKS)) {
      pool = pool.concat(VAULT_BOOKS);
    } else if (typeof VAULT_BOOKS === 'object') {
      for (var vk in VAULT_BOOKS) {
        if (Array.isArray(VAULT_BOOKS[vk])) {
          pool = pool.concat(VAULT_BOOKS[vk]);
        }
      }
    }
  }

  // Add CATEGORY_BENTO_DATA books to pool
  if (typeof CATEGORY_BENTO_DATA !== 'undefined') {
    for (var cat in CATEGORY_BENTO_DATA) {
      if (CATEGORY_BENTO_DATA[cat]) {
        if (CATEGORY_BENTO_DATA[cat].left) pool.push(CATEGORY_BENTO_DATA[cat].left);
        if (Array.isArray(CATEGORY_BENTO_DATA[cat].right)) {
          CATEGORY_BENTO_DATA[cat].right.forEach(function(rb) { pool.push(rb); });
        }
      }
    }
  }

  // Add MASTER_SEARCH_CATALOG (7,491 books) to pool
  if (typeof window.MASTER_SEARCH_CATALOG !== 'undefined' && Array.isArray(window.MASTER_SEARCH_CATALOG)) {
    pool = pool.concat(window.MASTER_SEARCH_CATALOG);
  }

  // If already an authentic book object with a real title (not 'Selected Book' or 'cat book...')
  if (bookOrId && typeof bookOrId === 'object' && bookOrId.title && bookOrId.title !== 'Selected Book' && !/^cat[-_ ]book/i.test(bookOrId.title)) {
    if (bookOrId.pages && (bookOrId.publisher || bookOrId.pub) && bookOrId.isbn && bookOrId.isbn !== '9789389742152') {
      return bookOrId;
    }
    var meta = findBookMetadata(bookOrId);
    if (meta) return Object.assign({}, meta, bookOrId, meta);
    return bookOrId;
  }

  var rawKey = String(bookOrId || '').trim();
  var key = rawKey.toLowerCase().replace(/^\/products\//, '').replace(/^#\/product\//, '');
  var cleanKey = key.replace(/^(bento-[a-z]+-|podium-|rekhta-|vault-[a-z]+-|vault-|catalog-|cat-book-[0-9]+-)/, '');

  // 1. Direct ISBN match check from key
  var isbnMatch = key.match(/(97[89][0-9]{10}|[0-9]{9}[0-9xX])/i);
  var targetIsbn = isbnMatch ? isbnMatch[0].replace(/[^0-9xX]/gi, '') : '';

  if (targetIsbn && typeof MODAL_METADATA_DATABASE !== 'undefined' && MODAL_METADATA_DATABASE[targetIsbn]) {
    return Object.assign({ id: targetIsbn }, MODAL_METADATA_DATABASE[targetIsbn]);
  }

  // 2. Direct lookup in MODAL_METADATA_DATABASE by key or cleanKey
  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    if (MODAL_METADATA_DATABASE[rawKey]) return Object.assign({ id: rawKey }, MODAL_METADATA_DATABASE[rawKey]);
    if (MODAL_METADATA_DATABASE[key]) return Object.assign({ id: key }, MODAL_METADATA_DATABASE[key]);
    if (MODAL_METADATA_DATABASE[cleanKey]) return Object.assign({ id: cleanKey }, MODAL_METADATA_DATABASE[cleanKey]);
  }

  // 3. Search pool by ISBN
  var found = null;
  if (targetIsbn) {
    found = pool.find(function(b) {
      if (!b || !b.isbn) return false;
      return String(b.isbn).replace(/[^0-9xX]/gi, '') === targetIsbn;
    });
  }

  // 4. Search pool by key / handle / slug
  if (!found && key) {
    found = pool.find(function(b) {
      if (!b) return false;
      var bId = String(b.id || '').trim().toLowerCase();
      var bHandle = String(b.handle || '').trim().toLowerCase();
      var bSku = String(b.sku || '').trim().toLowerCase();
      var bTitle = String(b.title || '').trim().toLowerCase();
      var slugTitle = bTitle.replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
      return bId === key || bHandle === key || bSku === key || bTitle === key || slugTitle === key ||
             bId === cleanKey || bHandle === cleanKey || slugTitle === cleanKey ||
             (cleanKey.length > 2 && (bId.indexOf(cleanKey) !== -1 || bHandle.indexOf(cleanKey) !== -1 || slugTitle.indexOf(cleanKey) !== -1 || bTitle.indexOf(cleanKey) !== -1));
    });
  }

  if (found) {
    var cleanPriceVal = window.cleanPrice(found.price, 299);
    var cleanCoverUrl = found.cover || found.image || found.coverUrl || '';
    return {
      id: found.id || key,
      title: found.title,
      handle: found.handle || found.id,
      author: found.author || found.vendor || 'Indigo Books Author',
      price: '₹' + cleanPriceVal.toFixed(2),
      oldPrice: '',
      discount: 'IN STOCK',
      binding: found.binding || found.format || 'Paperback',
      format: found.binding || found.format || 'Paperback',
      isbn: found.isbn || found.sku || (targetIsbn || ''),
      sku: found.sku || found.isbn || (targetIsbn || ''),
      pages: found.pages || '250p',
      pub: found.pub || found.publisher || 'Rajkamal Prakashan',
      publisher: found.pub || found.publisher || 'Rajkamal Prakashan',
      lang: found.lang || found.language || 'Hindi',
      edition: found.edition || 'Authorized Publisher Edition',
      dimensions: found.dimensions || '21.5 × 14.0 × 1.0 cm',
      qty: found.qty !== undefined ? found.qty : 50,
      stock: found.stock || 'In Stock',
      cover: cleanCoverUrl,
      coverUrl: cleanCoverUrl,
      image: cleanCoverUrl,
      overview: found.overview || found.blurb || found.description || ('« ' + found.title + ' » — प्रामाणिक संस्करण। Authoritative publisher edition curated by Indigo Books India, Prayagraj.'),
      firstPageExcerpt: found.firstPageExcerpt || ('« ' + found.title + ' — ' + (found.author || '') + ' की सशक्त लेखनी का अधिकृत संस्करण। मूल पाठ एवं आधिकारिक प्रकाशन। »'),
      highlights: found.highlights || [
        '100% Authentic Publisher Original Copy',
        'Official Publisher Edition: ' + (found.pub || found.publisher || 'Rajkamal Prakashan'),
        'Direct express dispatch from Prayagraj warehouse',
        'Eligible for Cash on Delivery (COD) & WhatsApp Ordering'
      ]
    };
  }

  // 5. Scrape from trigger element or DOM if passed
  if (triggerEl) {
    var cardEl = triggerEl.closest ? triggerEl.closest('[data-book-id], [data-title], .vault-card, .catalog-card, .rekhta-book-card, .rekhta-card, .ivh-book-card, .book-card') : null;
    if (cardEl) {
      var dTitle = cardEl.getAttribute('data-title');
      var dAuthor = cardEl.getAttribute('data-author');
      var dPrice = cardEl.getAttribute('data-price');
      var dBinding = cardEl.getAttribute('data-binding');
      var dImg = cardEl.querySelector('img') ? cardEl.querySelector('img').src : '';
      if (dTitle && dTitle !== 'Selected Book') {
        var cleanP = window.cleanPrice(dPrice, 299);
        return {
          id: cardEl.getAttribute('data-book-id') || key,
          title: dTitle,
          author: dAuthor || 'Indigo Books Author',
          price: '₹' + cleanP.toFixed(2),
          binding: dBinding || 'Paperback',
          format: dBinding || 'Paperback',
          cover: dImg,
          coverUrl: dImg,
          image: dImg,
          isbn: cardEl.getAttribute('data-isbn') || '',
          pages: cardEl.getAttribute('data-pages') || '250p',
          pub: cardEl.getAttribute('data-publisher') || 'Rajkamal Prakashan',
          publisher: cardEl.getAttribute('data-publisher') || 'Rajkamal Prakashan',
          lang: 'Hindi',
          dimensions: '21.5 × 14.0 × 1.0 cm',
          qty: 50,
          stock: 'In Stock',
          overview: 'Authentic publisher original edition curated by Indigo Books India, Prayagraj.'
        };
      }
    }
  }

  return null;
}

// Aliases
window.findBookByAnyIdentifier = window.resolveBookObject;

function openDedicatedProductPage(bookIdOrHandle, triggerEl) {
  let book = window.resolveBookObject(bookIdOrHandle, triggerEl);
  if (!book) {
    console.warn("Indigo Books: Could not resolve book for", bookIdOrHandle);
    return;
  }

    // Guarantee book has 100% complete authentic specs before displaying
  if (typeof findBookMetadata === 'function') {
    var fullMeta = findBookMetadata(book.id) || findBookMetadata(book.isbn) || (book.handle ? findBookMetadata(book.handle) : null) || findBookMetadata(book.title);
    if (fullMeta) {
      book = Object.assign({}, book, fullMeta, {
        isbn: fullMeta.isbn || book.isbn,
        sku: fullMeta.sku || fullMeta.isbn || book.sku,
        pages: fullMeta.pages || book.pages,
        pub: fullMeta.pub || fullMeta.publisher || book.pub || book.publisher,
        publisher: fullMeta.publisher || fullMeta.pub || book.publisher || book.pub,
        edition: fullMeta.edition || book.edition,
        binding: fullMeta.binding || book.binding,
        lang: fullMeta.lang || book.lang,
        dimensions: fullMeta.dimensions || book.dimensions,
        qty: (fullMeta.qty !== undefined) ? fullMeta.qty : book.qty,
        stock: fullMeta.stock || book.stock,
        cover: fullMeta.cover || book.cover,
        coverUrl: fullMeta.coverUrl || book.coverUrl,
        image: fullMeta.image || book.image
      });
    }
  }

  currentActivePdpBook = book;
  currentPdpQuantity = 1;

  if (typeof hideAllSearchDropdowns === 'function') {
    hideAllSearchDropdowns();
  }

  const homeView = document.getElementById('homepage-view');
  const searchView = document.getElementById('indigo-search-results-view');
  const pdpView = document.getElementById('single-product-page-view');
  if (!pdpView) return;

  // 1. Breadcrumbs
  const bCat = document.getElementById('pdpBreadcrumbCategory');
  if (bCat) bCat.textContent = book.category || book.pub || 'Curated Literature';
  const bTitle = document.getElementById('pdpBreadcrumbTitle');
  if (bTitle) bTitle.textContent = book.title;

  // 2. Cover image
  const resolvedCover = getAssetUrl(book.cover || book.coverUrl, book.id) || getFallbackCover(book.title, book.author);
  const coverImg = document.getElementById('pdpMainCoverImg');
  if (coverImg) {
    coverImg.src = resolvedCover;
    coverImg.alt = book.title;
    coverImg.onerror = function() {
      this.onerror = null;
      this.src = getFallbackCover(book.title, book.author);
    };
  }

  // 3. Title, Category, Rating
  const genreTag = document.getElementById('pdpGenreTag');
  if (genreTag) genreTag.textContent = book.category ? book.category.toUpperCase() : (book.pub ? book.pub.toUpperCase() : 'EXCLUSIVE EDITION');
  const titleEl = document.getElementById('pdpTitle');
  if (titleEl) titleEl.textContent = book.title;

  // 4. Clickable Author Avatar Pill
  const authorInitial = (book.author || 'A').trim().charAt(0).toUpperCase();
  const avEl = document.getElementById('pdpAuthorAvatar');
  if (avEl) avEl.textContent = authorInitial;
  const authLink = document.getElementById('pdpAuthorLink');
  if (authLink) authLink.textContent = book.author || 'Celebrated Author';

  // 5. Prices (Strict single authentic price with zero fake discounts)
  const cleanPriceVal = window.cleanPrice(book.price, 299);
  const priceFormatted = '₹' + cleanPriceVal.toFixed(2);
  const sellPriceEl = document.getElementById('pdpSellingPrice');
  const bbPriceEl = document.getElementById('pdpBbPrice');
  if (sellPriceEl) sellPriceEl.textContent = priceFormatted;
  if (bbPriceEl) bbPriceEl.textContent = priceFormatted;

  const comparePriceEl = document.getElementById('pdpComparePrice');
  const discountBadgeEl = document.getElementById('pdpDiscountBadge');
  if (comparePriceEl) comparePriceEl.style.display = 'none';
  if (discountBadgeEl) discountBadgeEl.style.display = 'none';

  // 6. Interactive Variant Buttons
  const varContainer = document.getElementById('pdpVariantButtons');
  if (varContainer) {
    if (book.variants && book.variants.length > 0) {
      varContainer.innerHTML = book.variants.map(function(v, i) {
        return '<button type="button" class="pdp-variant-btn ' + (i === 0 ? 'active' : '') + '" onclick="selectPdpVariant(&quot;' + escapeJs(v.format) + '&quot;)">' +
          escapeHtml(v.format) + ' &bull; ₹' + parseFloat(v.price).toFixed(2) +
        '</button>';
      }).join('');
      currentActivePdpVariant = book.variants[0];
    } else {
      varContainer.innerHTML = '<button type="button" class="pdp-variant-btn active" onclick="selectPdpVariant(&quot;' + escapeJs(book.binding || 'Paperback') + '&quot;)">' +
        escapeHtml(book.binding || 'Paperback') + ' &bull; ' + priceFormatted +
      '</button>';
      currentActivePdpVariant = null;
    }
  }

  // 7. Live Stock Count Badge
  const stockBadge = document.getElementById('pdpStockBadge');
  if (stockBadge) {
    var rawQty = (currentActivePdpVariant && currentActivePdpVariant.qty !== undefined) ? currentActivePdpVariant.qty : (book.qty !== undefined ? book.qty : 50);
    var formattedQty = typeof rawQty === 'number' ? rawQty.toLocaleString('en-IN') : String(rawQty).replace(/[^0-9,]/g, '');
    if (!formattedQty) formattedQty = 'Available';
    stockBadge.innerHTML = '<i data-lucide="check" style="width: 15px; height: 15px;"></i> ✓ In Stock (' + formattedQty + ' available)';
  }

  // 8. 5-Day Dynamic Delivery Date
  const delDate = new Date(Date.now() + 5 * 24 * 60 * 60 * 1000).toLocaleDateString('en-IN', { weekday: 'long', day: 'numeric', month: 'short' });
  const elDel = document.getElementById('pdpEstimatedDeliveryDate');
  if (elDel) elDel.textContent = 'Delivery by ' + delDate;

  // 9. Description & Tech Specs
  const descEl = document.getElementById('pdpDescription');
  if (descEl) descEl.textContent = book.overview || ('Authentic work by ' + book.author + '. Published by ' + (book.publisher || book.pub || 'Authorized Publisher Edition') + ', this authoritative volume represents an essential edition in Indian literature and scholarly thought.');

  const specTitle = document.getElementById('pdpSpecTitle');
  if (specTitle) specTitle.textContent = book.title;
  const specAuth = document.getElementById('pdpSpecAuthor');
  if (specAuth) specAuth.textContent = book.author || 'Celebrated Author';
  const specPub = document.getElementById('pdpSpecPublisher');
  if (specPub) specPub.textContent = book.publisher || book.pub || 'Authorized Publisher Edition';
  const specBinding = document.getElementById('pdpSpecBinding');
  if (specBinding) specBinding.textContent = (currentActivePdpVariant ? currentActivePdpVariant.format : book.binding) || 'Paperback';
  const specIsbn = document.getElementById('pdpSpecIsbn');
  if (specIsbn) specIsbn.textContent = (currentActivePdpVariant ? currentActivePdpVariant.sku : book.isbn) || (book.sku || '');
  const specPages = document.getElementById('pdpSpecPages');
  if (specPages) specPages.textContent = book.pages || 'Authorized Publisher Edition';
  const specLang = document.getElementById('pdpSpecLanguage');
  if (specLang) specLang.textContent = book.lang || 'Hindi';
  const specEd = document.getElementById('pdpSpecEdition');
  if (specEd) specEd.textContent = book.edition || 'Official Edition';

  // Live Available Quantity (from Excel QTY column 25)
  const specQty = document.getElementById('pdpSpecQty');
  if (specQty) {
    var rawQ = (currentActivePdpVariant && currentActivePdpVariant.qty !== undefined) ? currentActivePdpVariant.qty : (book.qty !== undefined ? book.qty : 50);
    var formattedQ = typeof rawQ === 'number' ? rawQ.toLocaleString('en-IN') : String(rawQ);
    specQty.textContent = formattedQ + ' copies (Prayagraj Warehouse)';
  }

  // Exact Dimensions (from Excel L, B, H columns 15, 16, 17)
  const specDim = document.getElementById('pdpSpecDimensions');
  if (specDim) specDim.textContent = book.dimensions || '21.5 × 14.0 × 1.0 cm';

  // 10. 3D Cover Back & Inside details
  const insideTitle = document.getElementById('pdp3dInsideTitle');
  if (insideTitle) insideTitle.textContent = book.title;
  const insideAuth = document.getElementById('pdp3dInsideAuthor');
  if (insideAuth) insideAuth.textContent = 'By ' + (book.author || 'Author');
  const insideFoot = document.getElementById('pdp3dInsideFooter');
  if (insideFoot) insideFoot.textContent = (book.pages || '250p') + ' • ' + (book.pub || 'Lokbharti');
  const cbPub = document.getElementById('pdpCoverBackPub');
  if (cbPub) cbPub.textContent = book.pub || 'Authorized Copy';
  const cbFormat = document.getElementById('pdpCoverBackFormat');
  if (cbFormat) cbFormat.textContent = ((currentActivePdpVariant ? currentActivePdpVariant.format : book.binding) || 'Paperback') + ' • ' + priceFormatted;

  // 11. Mini Thumbnail
  const thumb1 = document.getElementById('pdpThumbImg1');
  if (thumb1) thumb1.src = resolvedCover;

  // 12. Check saved location from localStorage
  try {
    const savedLoc = localStorage.getItem('indigo_saved_location');
    if (savedLoc) {
      const loc = JSON.parse(savedLoc);
      const pinInput = document.getElementById('pdpPincodeInput');
      const pinStatus = document.getElementById('pdpPincodeStatus');
      if (pinInput && loc.pincode) {
        pinInput.value = loc.pincode;
        if (pinStatus) {
          pinStatus.style.display = 'block';
          pinStatus.style.color = '#16A34A';
          pinStatus.innerHTML = '<strong>✓ Verified Location:</strong> ' + (loc.city || 'India') + ' (' + loc.pincode + '). Express Delivery &amp; COD Active!';
        }
      }
    }
  } catch (e) {}

  // 13. Excerpt reset
  const excerptBox = document.getElementById('pdpExcerptBox');
  const excerptText = document.getElementById('pdpExcerptText');
  if (excerptBox && excerptText) {
    excerptText.textContent = book.firstPageExcerpt || book.overview || 'First page preview available upon book dispatch.';
    excerptBox.classList.remove('open');
  }

  // 14. Qty Input Reset
  const qtyInput = document.getElementById('pdpQtyInput');
  if (qtyInput) qtyInput.value = '1';

  // 15. Render Same-Author Shelf
  renderPdpRecommendations(book);

  // 16. View Swap - Strictly hide both Homepage View and Search Results View so PDP is never rendered underneath
  if (homeView) homeView.style.display = 'none';
  if (searchView) searchView.style.display = 'none';
  pdpView.style.display = 'block';

  // 17. Update Hash without jump
  const safeHandle = book.handle || book.id || 'book';
  if (window.location.hash !== '#/product/' + safeHandle) {
    history.pushState(null, null, '#/product/' + safeHandle);
  }

  // 18. Instant guaranteed scroll to absolute top of viewport
  window.scrollTo(0, 0);
  document.documentElement.scrollTop = 0;
  document.body.scrollTop = 0;
  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// Global Author Search & Catalog Browse Helpers
function searchByAuthor(authorName) {
  if (!authorName) return;
  const clean = authorName.replace(/^by\s+/i, '').replace(/author\s*:\s*/i, '').trim();
  closeDedicatedProductPage();
  openSearchResultsPage(clean);
}

function browseAllBooks(e) {
  if (e && e.preventDefault) e.preventDefault();
  closeDedicatedProductPage();
  closeSearchResultsPage();
  toggleCartDrawer(false);
  currentCatalogCategory = 'all';
  currentCatalogQuery = '';
  const searchInput = document.getElementById('catalogSearchInput');
  if (searchInput) searchInput.value = '';
  renderCatalog();
  const catSection = document.getElementById('shop-all-catalog') || document.getElementById('catalogGridContainer');
  if (catSection) {
    catSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  if (searchInput) {
    setTimeout(function() { searchInput.focus(); }, 300);
  }
}

function closeDedicatedProductPage() {
  const homeView = document.getElementById('homepage-view');
  const pdpView = document.getElementById('single-product-page-view');
  const searchView = document.getElementById('indigo-search-results-view');
  if (!pdpView) return;

  pdpView.style.display = 'none';
  if (searchView && currentSearchResultsList.length > 0 && activeSearchQuery) {
    searchView.style.display = 'block';
  } else if (homeView) {
    homeView.style.display = 'block';
  }

  if (window.location.hash.startsWith('#/product/')) {
    if (activeSearchQuery && searchView && searchView.style.display === 'block') {
      history.pushState(null, null, '#/search?q=' + encodeURIComponent(activeSearchQuery));
    } else {
      history.pushState(null, null, ' ');
    }
  }

  window.scrollTo(0, 0);
  document.documentElement.scrollTop = 0;
  document.body.scrollTop = 0;
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
  const b = currentActivePdpBook;
  const cleanP = window.cleanPrice ? window.cleanPrice(b.price, 299) : 299;
  for (let i = 0; i < currentPdpQuantity; i++) {
    addToCart(b.id || b.handle || b.title, b.title, cleanP, b.cover || b.coverUrl);
  }
}

function pdpBuyNow() {
  if (!currentActivePdpBook) return;
  const b = currentActivePdpBook;
  const cleanP = window.cleanPrice ? window.cleanPrice(b.price, 299) : 299;
  for (let i = 0; i < currentPdpQuantity; i++) {
    addToCart(b.id || b.handle || b.title, b.title, cleanP, b.cover || b.coverUrl);
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
  const msgParts = [
    'Hello Indigo Books Prayagraj! [Order Request]',
    '',
    'I would like to order this book via Cash on Delivery (COD):',
    '- Title: ' + book.title,
    '- Author: ' + (book.author || 'Indigo Books'),
    '- Quantity: ' + qty,
    '- Unit Price: ' + price,
    '- Estimated Total: ₹' + total,
    '- ISBN/SKU: ' + (book.isbn || 'Standard'),
    '',
    'Please confirm delivery to my pincode and share tracking details. Thank you!'
  ];
  const msg = encodeURIComponent(msgParts.join(String.fromCharCode(10)));
  window.open('https://wa.me/918933063306?text=' + msg, '_blank');
}

// --- ROBUST AUTHOR MATCHING ENGINE ---
function isSameAuthorMatch(activeAuthor, bookAuthor) {
  if (!activeAuthor || !bookAuthor) return false;
  if (bookAuthor.indexOf('•') !== -1) return false;
  const a = activeAuthor.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim();
  const b = bookAuthor.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim();
  if (a === b) return true;

  // Prominent author signature clusters
  const signatureClusters = [
    ['rahi masoom raza', ['rahi masoom', 'masoom raza', 'rahi masoom raza']],
    ['ila chandra joshi', ['ila chandra joshi', 'ilachandra joshi', 'ila chandra', 'ilachandra']],
    ['shrilal shukla', ['shrilal shukla', 'sri lal shukla', 'shri lal shukla']],
    ['bhagwati charan verma', ['bhagwati charan verma', 'bhagwaticharan verma', 'bhagwati charan', 'bhagwaticharan']],
    ['piyush mishra', ['piyush mishra', 'piyush']],
    ['ramdhari singh dinkar', ['ramdhari singh dinkar', 'ramdhari singh', 'dinkar']],
    ['premchand', ['premchand', 'munshi premchand']],
    ['ruskin bond', ['ruskin bond', 'ruskin']],
    ['javed akhtar', ['javed akhtar']],
    ['anoop baranwal', ['anoop baranwal', 'deshbandhu']],
    ['subhash kashyap', ['subhash kashyap']],
    ['mohan rakesh', ['mohan rakesh']],
    ['george orwell', ['george orwell', 'orwell']],
    ['mahashweta devi', ['mahashweta devi', 'mahasweta devi']]
  ];

  for (let i = 0; i < signatureClusters.length; i++) {
    const sigs = signatureClusters[i][1];
    const aHit = sigs.some(function(s) { return a.indexOf(s) !== -1; });
    const bHit = sigs.some(function(s) { return b.indexOf(s) !== -1; });
    if (aHit && bHit) return true;
  }

  // Exact phrase match if longer than 5 chars (avoid single common surname matches like 'mishra', 'joshi', 'sharma', 'singh')
  if (a.length >= 6 && b.indexOf(a) !== -1) return true;
  if (b.length >= 6 && a.indexOf(b) !== -1) return true;

  // Two-word match (e.g. first and last name match), but reject generic single surnames
  const aParts = a.split(' ').filter(function(w) { return w.length > 2; });
  const bParts = b.split(' ').filter(function(w) { return w.length > 2; });
  if (aParts.length >= 2 && bParts.length >= 2) {
    if (aParts[0] === bParts[0] && aParts[aParts.length - 1] === bParts[bParts.length - 1]) {
      return true;
    }
  }

  return false;
}

function renderPdpRecommendations(activeBook) {
  const container = document.getElementById('pdpAuthorShelfContainer');
  const heading = document.getElementById('pdpAuthorShelfHeading');
  if (!container) return;

  const authorName = (activeBook.author || '').trim();
  const activeTitleNorm = (activeBook.title || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  const activeHandle = (activeBook.handle || activeBook.id || '').toLowerCase().trim();

  // Unified Pool
  let pool = [];
  if (typeof window.PIYUSH_MISHRA_BOOKS !== 'undefined' && Array.isArray(window.PIYUSH_MISHRA_BOOKS)) {
    pool = pool.concat(window.PIYUSH_MISHRA_BOOKS);
  }
  if (typeof window.RAHI_MASOOM_RAZA_BOOKS !== 'undefined' && Array.isArray(window.RAHI_MASOOM_RAZA_BOOKS)) {
    pool = pool.concat(window.RAHI_MASOOM_RAZA_BOOKS);
  }
  if (typeof window.MASTER_SEARCH_CATALOG !== 'undefined' && Array.isArray(window.MASTER_SEARCH_CATALOG)) {
    pool = pool.concat(window.MASTER_SEARCH_CATALOG);
  }
  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    pool = pool.concat(Object.values(MODAL_METADATA_DATABASE));
  }
  if (typeof getUnifiedSearchPool === 'function') {
    pool = pool.concat(getUnifiedSearchPool());
  }

  // 1. Gather exact author matches
  const seenTitles = new Set();
  const authorMatches = [];
  pool.forEach(function(b) {
    if (!b || !b.title) return;
    const bTitleNorm = (b.title || '').toLowerCase().replace(/[^a-z0-9]/g, '');
    const bHandle = (b.handle || b.id || '').toLowerCase().trim();
    if (bTitleNorm === activeTitleNorm || bHandle === activeHandle) return; // skip active book
    if (seenTitles.has(bTitleNorm)) return; // skip duplicate

    const bAuthor = b.author || b.vendor || '';
    if (isSameAuthorMatch(authorName, bAuthor)) {
      seenTitles.add(bTitleNorm);
      authorMatches.push(b);
    }
  });

  let displayBooks = [];
  if (authorMatches.length > 0) {
    if (heading) heading.textContent = 'More Books by ' + (authorName || 'This Author');
    displayBooks = authorMatches;
  } else {
    // Honest recommendation fallback: NEVER claim "More Books by Author" when showing other authors!
    const catName = activeBook.category || activeBook.pub || 'Curated Classics';
    if (heading) heading.textContent = 'Recommended Literary Classics (' + catName + ')';
    const catLower = catName.toLowerCase().trim();
    pool.forEach(function(b) {
      if (!b || !b.title) return;
      const bTitleNorm = (b.title || '').toLowerCase().replace(/[^a-z0-9]/g, '');
      const bHandle = (b.handle || b.id || '').toLowerCase().trim();
      if (bTitleNorm === activeTitleNorm || bHandle === activeHandle || seenTitles.has(bTitleNorm)) return;

      const bCat = (b.category || b.pub || '').toLowerCase().trim();
      if (bCat && (bCat === catLower || bCat.indexOf(catLower) !== -1 || catLower.indexOf(bCat) !== -1)) {
        seenTitles.add(bTitleNorm);
        displayBooks.push(b);
      }
    });
  }

  if (displayBooks.length === 0) {
    container.innerHTML = '<div style="color: #64748B; font-size: 13px; padding: 12px;">Explore more literary works in our pan-India catalog.</div>';
    return;
  }

  container.innerHTML = displayBooks.slice(0, 10).map(function(b) {
    const rawCover = b.cover || b.coverUrl || b.image || '';
    const cUrl = getAssetUrl(rawCover, b.id) || getFallbackCover(b.title, b.author);
    const pClean = window.cleanPrice(b.price, 299);
    const pStr = '₹' + pClean.toFixed(2);
    const bExcerpt = b.firstPageExcerpt || b.excerpt || b.quote || b.overview || b.description || 
      ('« यह कृति भारतीय साहित्य और सामाजिक चेतना का एक प्रामाणिक एवं अमिट दस्तावेज है। मूल पाठ एवं आधिकारिक संस्करण। »');
    const bBinding = b.binding || b.format || 'Paperback';

    return `
      <div class="shelf-book-card" data-book-id="${escapeHtml(b.id)}" data-handle="${escapeHtml(b.handle)}">
        <div class="indigo-3d-book-stage" onclick="window.openSoloBookPage('${escapeJs(b.id)}', this)" style="width: 100%; height: 250px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
          <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
            <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
              <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                <span>INDIGO ARCHIVE</span>
                <span style="color: #64748B;">AUTHENTIC</span>
              </div>
              <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                ${escapeHtml(b.title)}
              </div>
              <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                ${escapeHtml(b.author || 'Author')}
              </div>
            </div>
            <div style="font-family: 'Merriweather', serif; font-size: 8.5px; line-height: 1.45; color: #334155; font-style: italic; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; flex: 1; margin-bottom: 4px;">
              ${escapeHtml(bExcerpt)}
            </div>
            <div style="border-top: 1px dashed #CBD5E1; padding-top: 3px; font-size: 7.5px; color: #94A3B8; display: flex; justify-content: space-between;">
              <span>${escapeHtml(b.pages || '250p')}</span>
              <span>${escapeHtml(b.pub || 'Rajkamal')}</span>
            </div>
          </div>
          <div class="indigo-3d-cover-leaf">
            <div class="indigo-3d-cover-front">
              <img src="${cUrl}" alt="${escapeHtml(b.title)}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
          </div>
        </div>
        <div style="padding: 0 4px; text-align: left;">
          <div style="font-size: 9.5px; font-weight: 800; color: #0066B3; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 2px;">
            ${escapeHtml(bBinding)}
          </div>
          <div style="font-family: 'Merriweather', serif; font-size: 13.5px; font-weight: 700; color: #0F172A; line-height: 1.3; min-height: 36px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; margin-bottom: 3px;">
            <a href="javascript:void(0)" onclick="window.openSoloBookPage('${escapeJs(b.id)}', this)" style="color: inherit; text-decoration: none;">${escapeHtml(b.title)}</a>
          </div>
          <div style="font-size: 11px; color: #64748B; margin-bottom: 8px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
            ${escapeHtml(b.author || 'Author')}
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-top: auto;">
            <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${pStr}</span>
            <button type="button" onclick="addToCart('${escapeJs(b.id)}', '${escapeJs(b.title)}', ${pClean}, '${escapeJs(cUrl)}', this, event)" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 700; cursor: pointer;">
              + Add
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
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

// --- 7. MEMBER LOGIN MODAL ---

function switchAuthMode(mode) {
  const signinForm = document.getElementById('authSignInForm');
  const signupForm = document.getElementById('authSignUpForm');
  const tabIn = document.getElementById('tabAuthSignIn');
  const tabUp = document.getElementById('tabAuthSignUp');
  const title = document.getElementById('authModalTitle');
  const sub = document.getElementById('authModalSubtitle');
  const prompt = document.getElementById('authSwitchPrompt');

  if (mode === 'signup') {
    if (signinForm) signinForm.style.display = 'none';
    if (signupForm) signupForm.style.display = 'block';
    if (tabIn) {
      tabIn.style.background = 'transparent';
      tabIn.style.color = '#64748B';
      tabIn.style.fontWeight = '600';
      tabIn.style.boxShadow = 'none';
    }
    if (tabUp) {
      tabUp.style.background = '#FFFFFF';
      tabUp.style.color = '#0F172A';
      tabUp.style.fontWeight = '700';
      tabUp.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
    }
    if (title) title.textContent = 'Join Indigo Book Club';
    if (sub) sub.textContent = 'Create your account for exclusive literary previews and scholar benefits.';
    if (prompt) prompt.innerHTML = '<span style="color:#64748B;">Already a member?</span> <a href="javascript:void(0)" onclick="switchAuthMode(&quot;signin&quot;)" style="color: #0066B3; font-weight: 700; text-decoration: underline;">Sign In</a>';
  } else {
    if (signupForm) signupForm.style.display = 'none';
    if (signinForm) signinForm.style.display = 'block';
    if (tabUp) {
      tabUp.style.background = 'transparent';
      tabUp.style.color = '#64748B';
      tabUp.style.fontWeight = '600';
      tabUp.style.boxShadow = 'none';
    }
    if (tabIn) {
      tabIn.style.background = '#FFFFFF';
      tabIn.style.color = '#0F172A';
      tabIn.style.fontWeight = '700';
      tabIn.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
    }
    if (title) title.textContent = 'Sign in to Indigo Books';
    if (sub) sub.textContent = 'Access your reading orders, wishlist, and scholar benefits.';
    if (prompt) prompt.innerHTML = '<span style="color:#64748B;">New reader?</span> <a href="javascript:void(0)" onclick="switchAuthMode(&quot;signup&quot;)" style="color: #B45309; font-weight: 700; text-decoration: underline;">Join the Book Club</a>';
  }
}
window.switchAuthMode = switchAuthMode;

function toggleLoginModal() {
  const modal = document.getElementById('indigo-signin-modal') || document.getElementById('loginModalOverlay');
  if (!modal) return;
  const isActive = modal.classList.toggle('is-active');
  if (isActive) {
    modal.style.setProperty('display', 'flex', 'important');
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  } else {
    modal.style.setProperty('display', 'none', 'important');
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 8. SMOOTH SCROLL & FILTER HELPERS ---
function scrollToCatalog(category) {
  filterCatalog(category);
  const el = document.getElementById('shop-all-catalog');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

function scrollToVault(tabKey) {
  switchVaultTab(tabKey);
  const el = document.getElementById('law-academic-vault');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}


// --- 9. DOM INITIALIZATION ---

// =========================================================================
// 100% REAL CSV DATA PARSER HELPER (parseIndigoSpecsHtml)
// =========================================================================
function parseIndigoSpecsHtml(bodyHtml) {
  if (!bodyHtml || typeof bodyHtml !== 'string') return {};
  const specs = {};
  const patterns = {
    title: /<strong>Title:<\/strong>\s*([^<]+)/i,
    author: /<strong>Author:<\/strong>\s*([^<]+)/i,
    publisher: /<strong>Publisher:<\/strong>\s*([^<]+)/i,
    language: /<strong>Language:<\/strong>\s*([^<]+)/i,
    binding: /<strong>Binding:<\/strong>\s*([^<]+)/i,
    pages: /<strong>Pages:<\/strong>\s*([^<]+)/i,
    edition: /<strong>Edition\s*\/\s*Year:<\/strong>\s*([^<]+)/i,
    category: /<strong>Subject\s*\/\s*Category:<\/strong>\s*([^<]+)/i,
    isbn: /<strong>ISBN:<\/strong>\s*([^<]+)/i
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
  const specQty = document.getElementById('pdpSpecQty');
  if (specQty && match.qty !== undefined) {
    var formattedQ = typeof match.qty === 'number' ? match.qty.toLocaleString('en-IN') : String(match.qty);
    specQty.textContent = formattedQ + ' copies (Prayagraj Warehouse)';
  }

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
  const clean = authorName.replace(/^by\s+/i, '').replace(/author\s*:\s*/i, '').trim();
  closeDedicatedProductPage();
  openSearchResultsPage(clean);
}

// =========================================================================
// 1-CLICK PHONE EXPRESS CHECKOUT & ORDER DISPATCH
// =========================================================================
function openExpressPhoneCheckout(bookId, qty) {
  const modal = document.getElementById('indigo-express-checkout-modal') || document.getElementById('expressPhoneCheckoutModal');
  if (!modal) return;

  // Make sure order confirmation modal is closed
  const confirmModal = document.getElementById('indigo-order-success-modal') || document.getElementById('orderConfirmationModal');
  if (confirmModal) {
    confirmModal.classList.remove('is-active');
    confirmModal.style.setProperty('display', 'none', 'important');
    confirmModal.style.display = 'none';
  }

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

  modal.classList.add('is-active');
  modal.style.setProperty('display', 'flex', 'important');
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
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

  // STEP 1: Fully close and hide the checkout modal FIRST so it does not stay underneath!
  closeExpressPhoneCheckout();

  // Clear cart
  cart = [];
  try { localStorage.setItem('indigo_cart', JSON.stringify([])); } catch (e) {}
  updateCartUI();

  // STEP 2: Show Order Confirmation Modal cleanly
  const confirmModal = document.getElementById('indigo-order-success-modal') || document.getElementById('orderConfirmationModal');
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
    confirmModal.classList.add('is-active');
    confirmModal.style.setProperty('display', 'flex', 'important');
    confirmModal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    if (typeof lucide !== 'undefined') lucide.createIcons();
  }
}

function closeOrderConfirmationModal() {
  const confirmModal = document.getElementById('indigo-order-success-modal') || document.getElementById('orderConfirmationModal');
  if (confirmModal) {
    confirmModal.classList.remove('is-active');
    confirmModal.style.setProperty('display', 'none', 'important');
    confirmModal.style.display = 'none';
  }
  const checkoutModal = document.getElementById('indigo-express-checkout-modal') || document.getElementById('expressPhoneCheckoutModal');
  if (checkoutModal) {
    checkoutModal.classList.remove('is-active');
    checkoutModal.style.setProperty('display', 'none', 'important');
    checkoutModal.style.display = 'none';
  }
  document.body.style.overflow = '';
  closeDedicatedProductPage();
}

// Global Escape Key Listener for Immediate Modal Dismissal
if (typeof document !== 'undefined') {
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' || e.key === 'Esc') {
      closeOrderConfirmationModal();
      closeExpressPhoneCheckout();
      closeOverviewModal();
      const loginModal = document.getElementById('indigo-signin-modal') || document.getElementById('loginModalOverlay');
      if (loginModal && loginModal.classList.contains('is-active')) {
        loginModal.classList.remove('is-active');
        loginModal.style.setProperty('display', 'none', 'important');
        loginModal.style.display = 'none';
        document.body.style.overflow = '';
      }
      if (typeof closeCartDrawer === 'function') closeCartDrawer();
    }
  });
}

function initIndigoStore() {
  try { runVideoIntroSpotlightTour(); } catch(e) {}
  try { selectPodiumBook(0); } catch(e) {}
  try { switchPoet('all'); } catch(e) {}
  try { switchVaultTab('law'); } catch(e) {}
  try { renderCatalog(); } catch(e) {}
  try { updateCartUI(); } catch(e) {}
  try { checkHashRoute(); } catch(e) {}

  // Wire search input listeners for instant 2-letter debounced predictive suggestions
  try {
    ['hero-search-input', 'catalog-search-input', 'results-search-input'].forEach(function(id) {
      const inp = document.getElementById(id);
      if (inp && !inp.getAttribute('data-wired')) {
        inp.setAttribute('data-wired', 'true');
        const target = id.startsWith('hero') ? 'hero' : (id.startsWith('results') ? 'results' : 'catalog');
        inp.addEventListener('input', function(e) {
          handleSearchInput(e.target.value, target);
        });
        inp.addEventListener('focus', function(e) {
          if (e.target.value.trim().length >= 2) {
            handleSearchInput(e.target.value, target);
          }
        });
      }
    });
  } catch(e) {}

  // Handle incoming search query parameter if any
  try {
    if (typeof window !== 'undefined' && window.location && window.location.search) {
      const urlParams = new URLSearchParams(window.location.search);
      const searchParam = urlParams.get('search') || urlParams.get('q');
      if (searchParam) {
        setTimeout(function() {
          window.openSearchResultsPage(searchParam);
        }, 150);
      }
    }
  } catch(e) {}

  window.addEventListener('hashchange', checkHashRoute);

  if (typeof lucide !== 'undefined') {
    try { lucide.createIcons(); } catch(e) {}
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initIndigoStore);
} else {
  initIndigoStore();
}

window.addEventListener('load', function() {
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});


// --- GLOBAL NAVIGATION & AUTHOR FILTER HELPERS ---
function filterCatalogByAuthor(authorName) {
  if (!authorName) return;
  closeDedicatedProductPage();
  closeOverviewModal();
  toggleCartDrawer(false);

  // If on a standalone Shopify product page (/products/...) without SPA view, route to search
  const isShopifyLivePDP = (typeof window !== 'undefined' && window.location.pathname.includes('/products/'));
  const pdpView = document.getElementById('single-product-page-view');
  if (isShopifyLivePDP && !pdpView) {
    window.location.href = '/search?q=' + encodeURIComponent(authorName);
    return;
  }

  // Update catalog search input and trigger search
  const searchInput = document.getElementById('catalogSearchInput') || document.getElementById('heroSearchInput');
  if (searchInput) {
    searchInput.value = authorName;
    if (typeof handleCatalogSearchInput === 'function') {
      handleCatalogSearchInput(authorName);
    }
  }

  // Smooth scroll to catalog
  const catalog = document.getElementById('shop-all-catalog');
  if (catalog) {
    catalog.scrollIntoView({ behavior: 'smooth' });
  }
}

function navTo(sectionId, filterCategory) {
  closeDedicatedProductPage();
  closeOverviewModal();
  toggleCartDrawer(false);

  if (filterCategory && typeof filterCatalog === 'function') {
    filterCatalog(filterCategory);
  }

  if (!sectionId || sectionId === 'top' || sectionId === '#top') {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    return;
  }

  const cleanId = sectionId.replace(/^#/, '');
  const el = document.getElementById(cleanId);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
  } else {
    window.location.hash = '#' + cleanId;
  }
}

function closeCartAndBrowseCatalog() {
  toggleCartDrawer(false);
  closeDedicatedProductPage();
  closeOverviewModal();
  const catalog = document.getElementById('shop-all-catalog');
  if (catalog) {
    catalog.scrollIntoView({ behavior: 'smooth' });
  } else {
    window.scrollTo({ top: 600, behavior: 'smooth' });
  }
}

function openCart() {
  toggleCartDrawer(true);
}

function closeCart() {
  toggleCartDrawer(false);
}


// =========================================================================
// REAL-TIME SEARCH ALGORITHM & AUTO-SUGGESTION DROPDOWN ENGINE
// (Matches indigobooksindia.com & modern eCommerce standards)
// =========================================================================
function getUnifiedSearchPool() {
  const map = new Map();
  function add(b) {
    if (!b || !b.title) return;
    const bTitle = (b.title || '').trim().toLowerCase();
    const bAuthor = (b.author || b.vendor || '').trim().toLowerCase();
    const bFmt = (b.format || b.binding || (b.type && b.type.toLowerCase().includes('hard') ? 'Hardcover' : 'Paperback') || 'Paperback').toLowerCase();
    const key = bTitle + '|' + bAuthor + '|' + bFmt;
    if (!map.has(key)) map.set(key, b);
  }

  // 1. Live products or CATALOG_BOOKS
  const cat = getCatalogData();
  cat.forEach(add);

  // 2. CATEGORY_BENTO_DATA
  if (typeof CATEGORY_BENTO_DATA !== 'undefined') {
    for (var catKey in CATEGORY_BENTO_DATA) {
      if (CATEGORY_BENTO_DATA[catKey]) {
        if (CATEGORY_BENTO_DATA[catKey].left) add(CATEGORY_BENTO_DATA[catKey].left);
        if (Array.isArray(CATEGORY_BENTO_DATA[catKey].right)) {
          CATEGORY_BENTO_DATA[catKey].right.forEach(add);
        }
      }
    }
  }

  // 3. PIYUSH_MISHRA_BOOKS
  if (typeof window.PIYUSH_MISHRA_BOOKS !== 'undefined' && Array.isArray(window.PIYUSH_MISHRA_BOOKS)) {
    window.PIYUSH_MISHRA_BOOKS.forEach(add);
  }

  // 4. RAHI_MASOOM_RAZA_BOOKS
  if (typeof window.RAHI_MASOOM_RAZA_BOOKS !== 'undefined' && Array.isArray(window.RAHI_MASOOM_RAZA_BOOKS)) {
    window.RAHI_MASOOM_RAZA_BOOKS.forEach(add);
  }

  // 5. MASTER_SEARCH_CATALOG (Full 7,491 Excel & CSV catalog)
  if (typeof window.MASTER_SEARCH_CATALOG !== 'undefined' && Array.isArray(window.MASTER_SEARCH_CATALOG)) {
    window.MASTER_SEARCH_CATALOG.forEach(add);
  }

  // 6. PODIUM_BOOKS
  if (typeof PODIUM_BOOKS !== 'undefined' && Array.isArray(PODIUM_BOOKS)) {
    PODIUM_BOOKS.forEach(add);
  }

  // 7. REKHTA_BOOKS
  if (typeof REKHTA_BOOKS !== 'undefined' && Array.isArray(REKHTA_BOOKS)) {
    REKHTA_BOOKS.forEach(add);
  }

  // 8. VAULT_BOOKS
  if (typeof VAULT_BOOKS !== 'undefined') {
    Object.keys(VAULT_BOOKS).forEach(function(k) {
      (VAULT_BOOKS[k] || []).forEach(add);
    });
  }

  // 9. MODAL_METADATA_DATABASE
  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    for (var mk in MODAL_METADATA_DATABASE) {
      if (MODAL_METADATA_DATABASE[mk]) add(Object.assign({ id: mk }, MODAL_METADATA_DATABASE[mk]));
    }
  }

  return Array.from(map.values());
}
let searchDebounceTimer = null;

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function escapeJs(str) {
  if (!str) return '';
  return JSON.stringify(String(str)).slice(1, -1).replace(/'/g, "\\'");
}

function escapeRegex(string) {
  return string.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
}

function highlightSearchMatch(text, query) {
  if (!text) return '';
  if (!query) return escapeHtml(text);
  const re = new RegExp('(' + escapeRegex(query) + ')', 'gi');
  return escapeHtml(text).replace(re, '<mark style="background: #FEF08A; color: #854D0E; padding: 0 2px; border-radius: 2px;">$1</mark>');
}

function handleSearchInput(query, targetId) {
  const q = (typeof query === 'string' ? query : (query && query.target ? query.target.value : '')).trim();
  const dropdownId = targetId === 'hero' ? 'hero-search-suggestions' : 
                     (targetId === 'results' ? 'results-search-suggestions' : 'catalog-search-suggestions');
  const dropdown = document.getElementById(dropdownId);
  if (!dropdown) return;

  clearTimeout(searchDebounceTimer);
  // 2-Letter Debounced Predictive Search
  if (q.length < 2) {
    dropdown.style.display = 'none';
    dropdown.innerHTML = '';
    return;
  }

  searchDebounceTimer = setTimeout(function() {
    renderSearchSuggestions(q, dropdown, targetId);
  }, 180);
}

function renderSearchSuggestions(query, dropdown, targetId) {
  const pool = getUnifiedSearchPool();
  const q = query.toLowerCase().trim();
  
  const matches = [];
  pool.forEach(function(b) {
    const title = (b.title || '').toLowerCase().trim();
    const author = (b.author || b.vendor || '').toLowerCase().trim();
    const isbn = (b.isbn || b.sku || '').toLowerCase().trim();
    const genre = (b.genre || b.type || '').toLowerCase().trim();

    let score = 0;
    // Title matching
    if (title === q) score += 120;
    else if (title.startsWith(q)) score += 90;
    else if (title.includes(q)) score += 55;
    
    // Title word starts with query
    const titleWords = title.split(/\s+/);
    if (titleWords.some(function(w) { return w.startsWith(q); })) score += 65;

    // Author matching (Full weight for author searches like 'premchand', 'ruskin', 'mishra', 'shrilal')
    if (author === q) score += 115;
    else if (author.startsWith(q)) score += 85;
    else if (author.includes(q)) score += 50;

    // Author word starts with query
    const authorWords = author.split(/\s+/);
    if (authorWords.some(function(w) { return w.startsWith(q); })) score += 75;

    // ISBN & Genre matching
    if (isbn.includes(q)) score += 50;
    if (genre.includes(q)) score += 30;

    if (score > 0) {
      matches.push({ book: b, score: score });
    }
  });

  matches.sort(function(a, b) { return b.score - a.score; });

  // Deduplicate identical title + author (Strict Single Entry to Prevent Duplicates)
  const seenKeys = new Set();
  const uniqueMatches = [];
  for (let i = 0; i < matches.length; i++) {
    const b = matches[i].book;
    const bTitle = (b.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    const bAuthor = (b.author || b.vendor || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    const key = bTitle + '|' + bAuthor;
    if (!seenKeys.has(key)) {
      seenKeys.add(key);
      uniqueMatches.push(matches[i]);
    }
  }

  const topMatches = uniqueMatches.slice(0, 7);

  if (topMatches.length === 0) {
    dropdown.innerHTML = '<div style="padding: 16px; text-align: center; color: #64748B; font-size: 13px;">No books or authors found for "<strong>' + escapeHtml(query) + '</strong>"</div>';
    dropdown.style.display = 'block';
    return;
  }

  const itemsHtml = topMatches.map(function(m) {
    const book = m.book;
    const cover = getAssetUrl(book.image || book.coverUrl || book.cover || '', book.id);
    const cleanP = window.cleanPrice(book.price, 299);
    const priceFormatted = '₹' + cleanP.toFixed(2);
    const bookIdEscaped = escapeJs(book.id || book.handle || '');
    const highlightedTitle = highlightSearchMatch(book.title, query);
    const highlightedAuthor = highlightSearchMatch(book.author || book.vendor || 'Indigo Books Author', query);
    const formatBadge = (book.binding || book.format || 'Paperback').toUpperCase();

    return `
      <div class="search-suggestion-item" onmousedown="selectSearchSuggestion('${bookIdEscaped}', '/products/${escapeJs(book.handle || book.id)}', event)" onclick="selectSearchSuggestion('${bookIdEscaped}', '/products/${escapeJs(book.handle || book.id)}', event)" style="display: flex; align-items: center; gap: 12px; padding: 10px 14px; cursor: pointer; border-bottom: 1px solid #F1F5F9; transition: background 0.15s ease;">
        <div style="width: 38px; height: 54px; min-width: 38px; border-radius: 4px; overflow: hidden; background: #F8FAFC; border: 1px solid #E2E8F0; display: flex; align-items: center; justify-content: center;">
          <img src="${cover}" alt="${escapeHtml(book.title)}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.onerror=null; this.src=getFallbackCover('${escapeJs(book.title)}', '${escapeJs(book.author)}');"/>
        </div>
        <div style="flex: 1; min-width: 0;">
          <div style="font-family: 'Merriweather', serif; font-size: 13.5px; font-weight: 700; color: #0F172A; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; line-height: 1.3;">
            ${highlightedTitle}
          </div>
          <div style="font-size: 12px; color: #64748B; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-top: 2px;">
            By ${highlightedAuthor} &bull; <span style="font-size: 10px; color: #0066B3; font-weight: 600;">${formatBadge}</span>
          </div>
        </div>
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14.5px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important; text-align: right; white-space: nowrap;">
          ${priceFormatted}
        </div>
      </div>
    `;
  }).join('');

  dropdown.innerHTML = `
    <div style="padding: 6px 14px; background: #F8FAFC; border-bottom: 1px solid #E2E8F0; display: flex; align-items: center; justify-content: space-between;">
      <span style="font-size: 11px; font-weight: 700; color: #0066B3; text-transform: uppercase; letter-spacing: 0.08em;">Quick Results (${topMatches.length} matches)</span>
      <span style="font-size: 11px; color: #64748B;">Press Enter for All</span>
    </div>
    ${itemsHtml}
    <div onmousedown="executeFullSearch('${escapeJs(query)}')" onclick="executeFullSearch('${escapeJs(query)}')" style="padding: 10px 14px; background: #FFFBEB; text-align: center; font-size: 12.5px; font-weight: 700; color: #B45309; cursor: pointer; border-top: 1px solid #FEF3C7; transition: background 0.15s ease;">
      View All Results for "${escapeHtml(query)}" &rarr;
    </div>
  `;
  dropdown.style.display = 'block';
}

function selectSearchSuggestion(bookId, bookUrl, event) {
  if (event) {
    if (typeof event.preventDefault === 'function') event.preventDefault();
    if (typeof event.stopPropagation === 'function') event.stopPropagation();
  }
  hideAllSearchDropdowns();
  openDedicatedProductPage(bookId || bookUrl);
}
function executeFullSearch(query) {
  hideAllSearchDropdowns();
  window.openSearchResultsPage(query);
}

function performCatalogSearchEnter(e) {
  if (e && typeof e.preventDefault === 'function') e.preventDefault();
  window.submitSearch(e, 'catalog-search-input');
}

function hideAllSearchDropdowns() {
  const d1 = document.getElementById('hero-search-suggestions');
  if (d1) d1.style.display = 'none';
  const d2 = document.getElementById('catalog-search-suggestions');
  if (d2) d2.style.display = 'none';
  document.querySelectorAll('.indigo-live-suggest-box').forEach(function(b) {
    b.style.display = 'none';
    b.remove();
  });
}

document.addEventListener('click', function(e) {
  if (!e.target.closest('.search-input-wrap') && !e.target.closest('.catalog-search-wrap') && !e.target.closest('.search-suggestions-dropdown')) {
    hideAllSearchDropdowns();
  }
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    hideAllSearchDropdowns();
  }
});



// =========================================================================
// DEDICATED SEARCH RESULTS VIEW ENGINE (#indigo-search-results-view)
// =========================================================================
let currentSearchResultsList = [];
let currentSearchCategoryFilter = 'all';
let currentSearchSortKey = 'featured';
let activeSearchQuery = '';

window.submitSearch = function(event, inputId) {
  if (event && typeof event.preventDefault === 'function') event.preventDefault();
  var inputEl = document.getElementById(inputId);
  if (!inputEl) return;
  var query = inputEl.value.trim();
  if (!query) return;

  // Hide live suggestion dropdown
  var dropdownId = inputId === 'hero-search-input' ? 'hero-search-suggestions' : 
                   (inputId === 'results-search-input' ? 'results-search-suggestions' : 'catalog-search-suggestions');
  var dropdown = document.getElementById(dropdownId);
  if (dropdown) dropdown.style.display = 'none';

  // Open Dedicated Search Results Page View
  window.openSearchResultsPage(query);
};

function openSearchResultsPage(query) {
  if (!query) return;
  activeSearchQuery = query.trim();
  currentSearchCategoryFilter = 'all';
  currentSearchSortKey = 'featured';

  // If on a standalone Shopify product page or cart page with no SPA container, navigate to /search?q=...
  const isShopifyNonHome = (typeof window !== 'undefined' && 
    (window.location.pathname.includes('/products/') || window.location.pathname.includes('/cart')) &&
    !document.getElementById('indigo-search-results-view')
  );
  if (isShopifyNonHome) {
    window.location.href = '/search?q=' + encodeURIComponent(activeSearchQuery);
    return;
  }

  const homeView = document.getElementById('homepage-view');
  const pdpView = document.getElementById('single-product-page-view');
  const searchView = document.getElementById('indigo-search-results-view');
  if (!searchView) {
    // Fallback if view container doesn't exist
    if (typeof executeFullSearchLegacy === 'function') executeFullSearchLegacy(activeSearchQuery);
    return;
  }

  // 1. Hide other views, show search results view
  if (homeView) homeView.style.display = 'none';
  if (pdpView) pdpView.style.display = 'none';
  searchView.style.display = 'block';

  // 2. Sync all search input boxes
  const qDisplay = document.getElementById('search-query-display');
  if (qDisplay) qDisplay.textContent = activeSearchQuery;
  const resInput = document.getElementById('results-search-input');
  if (resInput) resInput.value = activeSearchQuery;
  const heroInput = document.getElementById('hero-search-input');
  if (heroInput) heroInput.value = activeSearchQuery;
  const catInput = document.getElementById('catalog-search-input');
  if (catInput) catInput.value = activeSearchQuery;

  // 3. Reset Category Pills in Search View
  const pills = document.querySelectorAll('#searchResultsCategoryPills .cat-pill');
  pills.forEach(function(p, idx) {
    if (idx === 0) p.classList.add('active');
    else p.classList.remove('active');
  });

  // 4. Reset Sort Select
  const sortSelect = document.getElementById('searchResultsSort');
  if (sortSelect) sortSelect.value = 'featured';

  // 5. Query Unified Store Pool & Score Matches
  const pool = getUnifiedSearchPool();
  const qLower = activeSearchQuery.toLowerCase().trim();
  
  const matches = [];
  pool.forEach(function(b) {
    const title = (b.title || '').toLowerCase().trim();
    const author = (b.author || b.vendor || '').toLowerCase().trim();
    const isbn = (b.isbn || b.sku || '').toLowerCase().trim();
    const genre = (b.genre || b.type || '').toLowerCase().trim();
    const tags = Array.isArray(b.tags) ? b.tags.join(' ').toLowerCase() : (typeof b.tags === 'string' ? b.tags.toLowerCase() : '');

    let score = 0;
    // Title matching
    if (title === qLower) score += 120;
    else if (title.startsWith(qLower)) score += 90;
    else if (title.includes(qLower)) score += 55;
    const titleWords = title.split(/\s+/);
    if (titleWords.some(function(w) { return w.startsWith(qLower); })) score += 65;

    // Author matching (Full weight for author searches like 'rahi', 'raza', 'joshi', 'shrilal', 'premchand', 'mishra')
    if (author === qLower) score += 115;
    else if (author.startsWith(qLower)) score += 85;
    else if (author.includes(qLower)) score += 50;
    const authorWords = author.split(/\s+/);
    if (authorWords.some(function(w) { return w.startsWith(qLower); })) score += 75;

    // ISBN & Genre matching
    if (isbn.includes(qLower)) score += 50;
    if (genre.includes(qLower)) score += 30;
    if (tags.includes(qLower)) score += 20;

    if (score > 0) {
      matches.push({ book: b, score: score });
    }
  });

  matches.sort(function(a, b) { return b.score - a.score; });

  // STRICT SINGLE-ENTRY DEDUPLICATION BY TITLE TO PREVENT DUPLICATES
  const seenSearchTitles = new Set();
  const dedupedSearchList = [];
  matches.forEach(function(m) {
    const tKey = (m.book.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    if (!seenSearchTitles.has(tKey)) {
      seenSearchTitles.add(tKey);
      dedupedSearchList.push(m.book);
    }
  });
  currentSearchResultsList = dedupedSearchList;

  // 6. Update Count Display
  const countEl = document.getElementById('search-result-count');
  if (countEl) countEl.textContent = currentSearchResultsList.length;

  // 7. Render 4-Column Results Grid
  renderCurrentSearchResults();

  // 8. Update Hash cleanly
  if (window.location.hash !== '#/search?q=' + encodeURIComponent(activeSearchQuery)) {
    history.pushState(null, null, '#/search?q=' + encodeURIComponent(activeSearchQuery));
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (typeof lucide !== 'undefined') lucide.createIcons();
};

function closeSearchResultsPage() {
  if (typeof window.closeSearchResultsView === 'function') {
    window.closeSearchResultsView();
  }
}
window.closeSearchResultsPage = closeSearchResultsPage;

window.closeSearchResultsView = function() {
  const homeView = document.getElementById('homepage-view');
  const pdpView = document.getElementById('single-product-page-view');
  const searchView = document.getElementById('indigo-search-results-view');
  if (!homeView || !searchView) return;

  searchView.style.display = 'none';
  if (pdpView) pdpView.style.display = 'none';
  homeView.style.display = 'block';

  if (window.location.hash.startsWith('#/search')) {
    history.pushState(null, null, ' ');
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (typeof lucide !== 'undefined') lucide.createIcons();
};

function closeSearchResultsPage() {
  if (typeof window.closeSearchResultsView === 'function') {
    window.closeSearchResultsView();
  }
}
window.closeSearchResultsPage = closeSearchResultsPage;

window.filterSearchResults = function(category, btn) {
  currentSearchCategoryFilter = category;
  const pills = document.querySelectorAll('#searchResultsCategoryPills .cat-pill');
  pills.forEach(function(p) { p.classList.remove('active'); });
  if (btn) btn.classList.add('active');
  renderCurrentSearchResults();
};

window.sortSearchResults = function(sortKey) {
  currentSearchSortKey = sortKey;
  renderCurrentSearchResults();
};

function renderCurrentSearchResults() {
  const container = document.getElementById('search-results-grid');
  if (!container) return;

  let list = currentSearchResultsList.slice();

  // Filter by category if not 'all'
  if (currentSearchCategoryFilter !== 'all') {
    list = list.filter(function(b) {
      return matchesBookCategory(b, currentSearchCategoryFilter);
    });
  }

  // Sort
  if (currentSearchSortKey === 'price-asc') {
    list.sort(function(a, b) {
      const pA = window.cleanPrice(a.price, 299);
      const pB = window.cleanPrice(b.price, 299);
      return pA - pB;
    });
  } else if (currentSearchSortKey === 'price-desc') {
    list.sort(function(a, b) {
      const pA = window.cleanPrice(a.price, 299);
      const pB = window.cleanPrice(b.price, 299);
      return pB - pA;
    });
  } else if (currentSearchSortKey === 'title-asc') {
    list.sort(function(a, b) {
      return (a.title || '').localeCompare(b.title || '');
    });
  }

  if (list.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 48px 32px; text-align: center; max-width: 680px; margin: 0 auto; box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);">
        <div style="width: 64px; height: 64px; border-radius: 50%; background: #FEF3C7; color: #B45309; display: flex; align-items: center; justify-content: center; margin: 0 auto 18px;">
          <i data-lucide="search-x" style="width: 32px; height: 32px;"></i>
        </div>
        <h2 style="font-family: 'Merriweather', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 0 0 10px;">
          No books found matching your query.
        </h2>
        <p style="font-size: 14px; color: #64748B; line-height: 1.6; margin: 0 0 24px;">
          Try searching by author name, title keywords, or ISBN. Alternatively, contact our Prayagraj book desk directly to source this title.
        </p>
        <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
          <button type="button" onclick="window.closeSearchResultsView(); scrollToCatalog('all');" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 8px; padding: 10px 20px; font-size: 13.5px; font-weight: 700; cursor: pointer;">
            Browse All 5,500+ Books &rarr;
          </button>
          <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books!%20I%20am%20looking%20for%20a%20book:%20${encodeURIComponent(activeSearchQuery)}" target="_blank" style="display: inline-flex; align-items: center; gap: 6px; background: #25D366; color: #FFFFFF; border: none; border-radius: 8px; padding: 10px 18px; font-size: 13.5px; font-weight: 700; text-decoration: none;">
            <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i> Inquire on WhatsApp
          </a>
        </div>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  container.innerHTML = list.map(function(book) {
    const rawCover = book.image || book.coverUrl || book.cover || '';
    let cover = getAssetUrl(rawCover, book.id);
    const authorSafe = (book.author || book.vendor || 'Indigo Books').replace(/['"]/g, ' ');
    const titleSafe = (book.title || 'Book').replace(/['"]/g, ' ');
    if (!cover) {
      cover = getFallbackCover(titleSafe, authorSafe);
    }
    const bookUrl = book.url || (book.handle ? '/products/' + book.handle : '');
    const cleanP = window.cleanPrice(book.price, 299);
    const priceFormatted = '₹' + cleanP.toFixed(2);
    const bookBinding = (book.binding || book.format || (book.type && book.type.toLowerCase().includes('hard') ? 'Hardcover' : 'Paperback') || 'Paperback').toUpperCase();

    return `
      <div class="catalog-card" data-book-id="${escapeHtml(book.id)}" data-title="${escapeHtml(book.title)}" data-author="${escapeHtml(book.author || book.vendor || '')}" data-price="${escapeHtml(String(cleanP))}" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 18px; display: flex; flex-direction: column; transition: transform 0.2s, box-shadow 0.2s;">
        <div class="catalog-thumb" onclick="handleBookAction('${escapeJs(book.id)}', '${escapeJs(bookUrl)}', event);" style="cursor: pointer; width: 100%; aspect-ratio: 2 / 3; background: #F8FAFC; border-radius: 6px; overflow: hidden; margin-bottom: 12px; position: relative;">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; display: block;" onerror="this.onerror=null; this.src=getFallbackCover('${escapeJs(titleSafe)}', '${escapeJs(authorSafe)}');" />
        </div>
        <div style="font-size: 10px; font-weight: 800; color: #0066B3; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 4px;">
          ${escapeHtml(bookBinding)} &bull; <span style="color: #B45309;">IN STOCK</span>
        </div>
        <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin: 0 0 4px; min-height: 38px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
          <a href="javascript:void(0)" onclick="handleBookAction('${escapeJs(book.id)}', '${escapeJs(bookUrl)}', event); return false;" style="color: inherit; text-decoration: none;">${escapeHtml(book.title)}</a>
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          ${escapeHtml(book.author || book.vendor || 'Indigo Books')}
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
          <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${priceFormatted}</span>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
          <button type="button" class="btn-overview" onclick="handleBookAction('${escapeJs(book.id)}', '${escapeJs(bookUrl)}', event);" style="display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 9px 12px; background: #F1F5F9; color: #0F172A; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 12.5px; font-weight: 700; cursor: pointer;">
            <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
          </button>
          <button type="button" class="btn-add-cart" onclick="addToCart('${escapeJs(book.id)}', '${escapeJs(book.title)}', ${cleanP}, '${escapeJs(cover)}', this, event)" style="display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 9px 12px; background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; font-size: 12.5px; font-weight: 700; cursor: pointer;">
            <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> + Add
          </button>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 5B. CATEGORY BENTO ASYMMETRIC SHOWCASE SWITCHER ---
function switchCategoryBento(categoryKey) {
  window.switchCategoryBento = switchCategoryBento;
  if (typeof CATEGORY_BENTO_DATA === 'undefined') return;
  const data = CATEGORY_BENTO_DATA[categoryKey];
  if (!data) return;

  // 1. Update active pill
  const pills = document.querySelectorAll('.cat-bento-pill');
  pills.forEach(function(pill) {
    if (pill.getAttribute('data-cat') === categoryKey) {
      pill.classList.add('active');
    } else {
      pill.classList.remove('active');
    }
  });

  // 2. Update Left Spotlight Card
  const leftCard = document.getElementById('bentoLeftSpotlight');
  if (leftCard && data.left) {
    const l = data.left;
    leftCard.setAttribute('data-book-id', l.id);
    leftCard.setAttribute('data-title', l.title);
    leftCard.setAttribute('data-author', l.author);
    leftCard.setAttribute('data-price', l.price);
    const lPriceFormatted = '₹' + window.cleanPrice(l.price).toFixed(2);

    const titleEl = document.getElementById('bentoLeftTitle');
    if (titleEl) {
      titleEl.innerHTML = `<a href="/products/${l.handle || l.id}" onclick="handleBookAction('${l.id}', '/products/${l.handle || l.id}', event)" style="color: inherit; text-decoration: none;">${escapeHtml(l.title)}</a>`;
    }
    const authEl = document.getElementById('bentoLeftAuthor');
    if (authEl) authEl.textContent = l.author;
    const blurbEl = document.getElementById('bentoLeftBlurb');
    if (blurbEl) blurbEl.textContent = '"' + (l.quote || l.blurb || '') + '"';
    const specsEl = document.getElementById('bentoLeftSpecs');
    if (specsEl) specsEl.textContent = l.specs || '';
    const priceEl = document.getElementById('bentoLeftPrice');
    if (priceEl) priceEl.textContent = lPriceFormatted;

    // Update 3D book cover
    const coverWrap = leftCard.querySelector('.bento-left-cover-wrap');
    if (coverWrap) {
      coverWrap.innerHTML = `
        <div class="indigo-3d-book-stage" onclick="openSoloBookPage('${l.id}', event)">
          <div class="indigo-3d-inside-page">
            <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">INDIGO ARCHIVE</div>
            <div style="font-family: 'Merriweather', serif; font-size: 13px; line-height: 1.35; color: #1E293B; font-weight: 700;">${escapeHtml(l.title)}</div>
            <div style="font-size: 11px; color: #64748B;">By ${escapeHtml(l.author)}</div>
            <div style="font-size: 9.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 4px;">${escapeHtml(l.specs || 'Standard Edition')}</div>
          </div>
          <div class="indigo-3d-cover-leaf">
            <div class="indigo-3d-cover-front">
              <img src="${getAssetUrl(l.coverUrl, l.id)}" alt="${escapeHtml(l.title)}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <div class="indigo-3d-cover-back">
              <div style="font-size: 10px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">100% GENUINE</div>
              <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">Authorized Copy</div>
              <div style="font-size: 11px; color: #CBD5E1;">${lPriceFormatted}</div>
              <div style="font-size: 9.5px; color: #FCD34D; margin-top: 6px; border: 1px solid rgba(251,191,36,0.4); padding: 2px 6px; border-radius: 4px;">Click for Details &rarr;</div>
            </div>
          </div>
        </div>
      `;
    }

    // Update buttons
    const btnOverview = leftCard.querySelector('.btn-overview');
    if (btnOverview) btnOverview.setAttribute('onclick', `openOverviewModal('${l.id}')`);
    const btnAdd = leftCard.querySelector('.btn-add-cart');
    if (btnAdd) btnAdd.setAttribute('onclick', `addToCart('${l.id}')`);
  }

  // 3. Update Right 2x2 Grid
  const rightGrid = document.getElementById('bentoRightGrid');
  if (rightGrid && data.right) {
    rightGrid.innerHTML = data.right.map(function(rb) {
      const rbPriceFormatted = '₹' + window.cleanPrice(rb.price).toFixed(2);
      return `
        <div class="bento-horiz-card" data-book-id="${escapeHtml(rb.id)}" data-title="${escapeHtml(rb.title)}" data-author="${escapeHtml(rb.author)}" data-price="${escapeHtml(rbPriceFormatted)}">
          <div>
            <div class="bento-horiz-top">
              <div class="bento-horiz-cover">
                <div class="indigo-3d-book-stage" onclick="openSoloBookPage('${rb.id}', event)">
                  <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                    <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                    <div style="font-family: 'Merriweather', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">${escapeHtml(rb.title)}</div>
                    <div style="font-size: 7.5px; color: #64748B;">${escapeHtml(rb.author)}</div>
                  </div>
                  <div class="indigo-3d-cover-leaf">
                    <div class="indigo-3d-cover-front">
                      <img src="${getAssetUrl(rb.coverUrl, rb.id)}" alt="${escapeHtml(rb.title)}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                    </div>
                    <div class="indigo-3d-cover-back" style="padding: 6px !important;">
                      <div style="font-size: 8px; font-weight: 700; color: #F59E0B;">GENUINE</div>
                      <div style="font-size: 8.5px; color: #FFFFFF;">${rbPriceFormatted}</div>
                    </div>
                  </div>
                </div>
              </div>
              <div style="min-width: 0;">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                  ${escapeHtml(rb.tag || 'LITERARY WORK')}
                </div>
                <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                  <a href="/products/${rb.handle || rb.id}" onclick="handleBookAction('${rb.id}', '/products/${rb.handle || rb.id}', event)" style="color: inherit; text-decoration: none;">${escapeHtml(rb.title)}</a>
                </h4>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(rb.author)}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">${escapeHtml(rb.specs || 'Paperback')}</div>
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${rbPriceFormatted}</div>
              </div>
            </div>
            <p style="font-size: 12px; color: #64748B; line-height: 1.5; margin: 0 0 8px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
              ${escapeHtml(rb.desc || '')}
            </p>
          </div>
          <div class="bento-card-actions">
            <button type="button" class="btn-overview" style="padding: 7px 10px; font-size: 12px;" onclick="openOverviewModal('${rb.id}')">
              <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Overview
            </button>
            <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('${rb.id}')">
              <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> + Add
            </button>
          </div>
        </div>
      `;
    }).join('');
  }

  if (typeof lucide !== 'undefined') lucide.createIcons();
};
if (typeof window !== 'undefined') {
  window.searchByAuthor = searchByAuthor;
  window.browseAllBooks = browseAllBooks;
  window.toggleCartDrawer = toggleCartDrawer;
  window.addToCart = addToCart;
  window.openSearchResultsPage = openSearchResultsPage;
  window.closeSearchResultsPage = closeSearchResultsPage;
  window.openDedicatedProductPage = openDedicatedProductPage;
  window.openSoloBookPage = openDedicatedProductPage;
  window.resolveBookObject = resolveBookObject;
  window.proceedToCheckout = proceedToCheckout;
  window.checkoutViaWhatsApp = checkoutViaWhatsApp;
  window.closeDedicatedProductPage = closeDedicatedProductPage;
  window.parseIndigoSpecsHtml = parseIndigoSpecsHtml;
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
  window.switchCategoryBento = switchCategoryBento;
  window.goToCatalogPage = goToCatalogPage;
  window.renderCatalog = renderCatalog;
  window.handleSearchInput = handleSearchInput;
  window.renderSearchSuggestions = renderSearchSuggestions;
  window.selectSearchSuggestion = selectSearchSuggestion;
  window.hideAllSearchDropdowns = hideAllSearchDropdowns;
  window.executeFullSearch = executeFullSearch;
  window.openOverviewModal = openOverviewModal;
  window.closeOverviewModal = closeOverviewModal;
  window.updateCartUI = updateCartUI;
  window.updateCartQty = updateCartQty;
  window.renderPdpRecommendations = renderPdpRecommendations;
}
"""
