# -*- coding: utf-8 -*-
"""
store_scripts.py
Single Source of Truth for Bookstore JavaScript Engine.
Clean Vanilla JS with Zero External Frameworks.
"""

UNIFIED_STORE_JS = """
// =========================================================================
// INDIGO BOOKS INDIA - PURE VANILLA JS ENGINE (UNIFIED & COMPLETE)
// =========================================================================

// --- UNIVERSAL ASSET URL RESOLVER ---
function getAssetUrl(url) {
  if (!url) return '';
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) return url;
  let clean = url.replace(/^assets\//, '')
                 .replace(/^\{\{\s*['"]?/, '')
                 .replace(/['"]?\s*\|\s*asset_url\s*\}\}$/, '')
                 .trim();
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
  const grid = document.getElementById('heroBooksGrid');
  const cards = document.querySelectorAll('.hero-video-book-card');
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
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length >= 5) {
    return window.SHOPIFY_LIVE_PRODUCTS.slice(0, 5).map(function(prod, idx) {
      const fallback = (typeof PODIUM_BOOKS !== 'undefined' && PODIUM_BOOKS[idx]) ? PODIUM_BOOKS[idx] : {};
      return {
        id: prod.id ? String(prod.id) : (fallback.id || 'podium-' + idx),
        variantId: prod.variantId || fallback.variantId || '',
        handle: prod.handle || fallback.handle || '',
        title: prod.title || fallback.title || 'Featured Classic',
        author: prod.author || fallback.author || 'Renowned Author',
        price: prod.price || fallback.price || '₹299.00',
        oldPrice: prod.oldPrice || fallback.oldPrice || '₹400.00',
        discount: prod.discount || fallback.discount || '25% OFF',
        badge: idx === 0 ? "NATIONAL BESTSELLER" : (idx === 1 ? "SAHITYA AKADEMI" : (idx === 2 ? "TIMELESS CLASSIC" : "TOP TRENDING")),
        rating: fallback.rating || "4.9 (10,000+)",
        stock: "In Stock • Ships in 24 Hrs",
        coverUrl: prod.coverUrl || fallback.coverUrl || '',
        cover: prod.coverUrl || fallback.coverUrl || '',
        firstPageExcerpt: fallback.firstPageExcerpt || prod.description || "A masterwork of Indian literature capturing the essence of storytelling.",
        quote: fallback.quote || (prod.description ? prod.description.slice(0, 100) + '...' : "Essential reading for every book lover in India."),
        pages: fallback.pages || "320p",
        publisher: fallback.publisher || prod.author || "Lokbharti / Rajkamal",
        genre: prod.type || fallback.genre || "Fiction : Classic",
        url: prod.url || fallback.url || ''
      };
    });
  }
  return typeof PODIUM_BOOKS !== 'undefined' ? PODIUM_BOOKS : [];
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

  const resolvedCover = getAssetUrl(book.coverUrl || book.cover);

  if (elCoverImg) {
    elCoverImg.src = resolvedCover;
    elCoverImg.alt = book.title;
  }
  if (elInsideThumb) {
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

  if (imgL2) { imgL2.src = getAssetUrl(books[fL2].coverUrl || books[fL2].cover); imgL2.alt = books[fL2].title; }
  if (imgL1) { imgL1.src = getAssetUrl(books[fL1].coverUrl || books[fL1].cover); imgL1.alt = books[fL1].title; }
  if (imgR1) { imgR1.src = getAssetUrl(books[fR1].coverUrl || books[fR1].cover); imgR1.alt = books[fR1].title; }
  if (imgR2) { imgR2.src = getAssetUrl(books[fR2].coverUrl || books[fR2].cover); imgR2.alt = books[fR2].title; }

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

function togglePodiumCover(e) {
  if (e) e.stopPropagation();
  const el = document.getElementById('podium-3d-book');
  if (el) el.classList.toggle('is-open');
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
  const msg = lines.join("\n");
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

  // Render 4 books
  const books = VAULT_BOOKS[tabKey];
  const container = document.getElementById('vaultCardsContainer');
  if (!container) return;

  container.innerHTML = books.map(function(book) {
    const cover = getAssetUrl(book.coverUrl || book.cover);
    return `
      <div class="vault-card">
        <div class="vault-card-thumb">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${book.title}" loading="lazy" />
        </div>
        <div class="vault-card-body">
          <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
            ${book.badge}
          </div>
          <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
            ${book.title}
          </h3>
          <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
            ${book.author}
          </div>
          <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
            <span style="font-size: 18px; font-weight: 800; color: #0F172A;">${book.price}</span>
            <span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">${book.oldPrice}</span>
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
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 4. PAN-INDIA CATALOG FILTERING ---
let currentCatalogCategory = 'all';
let currentCatalogQuery = '';

function filterCatalog(category) {
  currentCatalogCategory = category;

  document.querySelectorAll('.cat-pill').forEach(function(btn) {
    if (btn.getAttribute('data-cat') === category) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  renderCatalog();
}

function handleCatalogSearch(e) {
  currentCatalogQuery = e.target.value.toLowerCase().trim();
  renderCatalog();
}

function handleHeroSearch(e) {
  if (e.key === 'Enter') {
    performHeroSearch();
  }
}

function performHeroSearch() {
  const input = document.getElementById('hero-search-input');
  if (input) {
    const val = input.value.trim();
    currentCatalogQuery = val.toLowerCase();
    const catInput = document.getElementById('catalog-search-input');
    if (catInput) catInput.value = val;

    if (typeof window !== 'undefined' && val.length > 0 && (window.location.hostname.includes('myshopify.com') || window.location.hostname.includes('indigobooks'))) {
      const source = getCatalogData();
      const hasLocalMatch = source.some(function(b) {
        return b.title.toLowerCase().includes(currentCatalogQuery) || (b.author && b.author.toLowerCase().includes(currentCatalogQuery));
      });
      if (!hasLocalMatch) {
        window.location.href = '/search?q=' + encodeURIComponent(val) + '&type=product';
        return;
      }
    }

    scrollToCatalog('all');
    renderCatalog();
  }
}

function getCatalogData() {
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length > 0) {
    return window.SHOPIFY_LIVE_PRODUCTS;
  }
  return typeof CATALOG_BOOKS !== 'undefined' ? CATALOG_BOOKS : [];
}

function handleBookAction(bookId, bookUrl) {
  if (bookUrl && typeof bookUrl === 'string' && bookUrl.startsWith('/products/')) {
    window.location.href = bookUrl;
    return;
  }
  openOverviewModal(bookId);
}

function renderCatalog() {
  const container = document.getElementById('catalogGridContainer');
  if (!container) return;

  const catalogSource = getCatalogData();

  const filtered = catalogSource.filter(function(book) {
    const bTags = Array.isArray(book.tags) ? book.tags : (typeof book.tags === 'string' ? book.tags.split(',') : []);
    const matchesCat = currentCatalogCategory === 'all' || 
      bTags.some(function(t) { return t.trim().toLowerCase() === currentCatalogCategory; }) ||
      (book.type && book.type.toLowerCase().includes(currentCatalogCategory));
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
        <a href="/collections/all" style="display: inline-block; margin-top: 14px; font-size: 13px; font-weight: 700; color: #B45309; text-decoration: underline;">Search across all 5,500+ books on the catalog page &rarr;</a>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  container.innerHTML = filtered.map(function(book) {
    const cover = getAssetUrl(book.coverUrl || book.cover);
    return `
      <div class="catalog-card">
        <div class="catalog-thumb" onclick="handleBookAction('${book.id}', '${book.url || ''}')" style="${book.url ? 'cursor: pointer;' : ''}">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${book.title}" loading="lazy" />
        </div>
        <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
          ${book.discount || 'IN STOCK'}
        </div>
        <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
          ${book.url ? `<a href="${book.url}" style="color: inherit; text-decoration: none;">${book.title}</a>` : book.title}
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          ${book.author}
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
          <span style="font-size: 18px; font-weight: 800; color: #0F172A;">${book.price}</span>
          ${book.oldPrice ? `<span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">${book.oldPrice}</span>` : ''}
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

  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 5. UNIVERSAL MINI OVERVIEW MODAL ---
function findBookMetadata(arg) {
  if (!arg) return null;
  if (typeof arg === 'object' && arg.title) {
    const rawPrice = arg.price ? String(arg.price).replace(/[^0-9.]/g, '') : '299.00';
    const rawMrp = arg.oldPrice ? String(arg.oldPrice).replace(/[^0-9.]/g, '') : (Number(rawPrice) * 1.3).toFixed(2);
    return {
      id: arg.id || '',
      title: arg.title,
      author: arg.author || 'Renowned Author',
      price: rawPrice,
      mrp: rawMrp,
      discount: arg.discount || '25% OFF',
      cover: arg.coverUrl || arg.cover || '',
      lang: 'Hindi / Hindustani',
      binding: arg.format || 'Paperback',
      pages: arg.pages || '320p',
      pub: arg.publisher || arg.author || 'Lokbharti / Rajkamal',
      dispatch: 'Same-Day Dispatch from Prayagraj Hub',
      overview: arg.blurb || arg.description || arg.quote || 'An essential literary work published and archived by Indigo Books India.',
      highlights: [
        '100% Authentic Publisher Edition guaranteed',
        'Direct dispatch from Prayagraj literary warehouse',
        'Eligible for Cash on Delivery (COD) & WhatsApp Ordering'
      ]
    };
  }

  const idStr = String(arg);

  if (typeof MODAL_METADATA_DATABASE !== 'undefined' && MODAL_METADATA_DATABASE[idStr]) {
    return MODAL_METADATA_DATABASE[idStr];
  }

  // Check PODIUM_BOOKS
  if (typeof PODIUM_BOOKS !== 'undefined') {
    const b = PODIUM_BOOKS.find(function(x) { return String(x.id) === idStr; });
    if (b) return findBookMetadata(b);
  }

  // Check REKHTA_BOOKS
  if (typeof REKHTA_BOOKS !== 'undefined') {
    const b = REKHTA_BOOKS.find(function(x) { return String(x.id) === idStr; });
    if (b) return findBookMetadata(b);
  }

  // Check VAULT_BOOKS
  if (typeof VAULT_BOOKS !== 'undefined') {
    for (const cat in VAULT_BOOKS) {
      const b = VAULT_BOOKS[cat].find(function(x) { return String(x.id) === idStr; });
      if (b) return findBookMetadata(b);
    }
  }

  // Check live products / catalog
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS)) {
    const b = window.SHOPIFY_LIVE_PRODUCTS.find(function(x) {
      return String(x.id) === idStr || String(x.variantId) === idStr || x.handle === idStr;
    });
    if (b) return findBookMetadata(b);
  }

  if (typeof CATALOG_BOOKS !== 'undefined') {
    const b = CATALOG_BOOKS.find(function(x) { return String(x.id) === idStr; });
    if (b) return findBookMetadata(b);
  }

  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    const keys = Object.keys(MODAL_METADATA_DATABASE);
    if (keys.length > 0) return MODAL_METADATA_DATABASE[keys[0]];
  }

  return null;
}

function openOverviewModal(bookArg) {
  const book = findBookMetadata(bookArg);
  if (!book) return;

  const modal = document.getElementById('overviewModalOverlay');
  if (!modal) return;

  const coverEl = document.getElementById('modalCover');
  if (coverEl) {
    coverEl.src = getAssetUrl(book.cover);
    coverEl.alt = book.title;
  }
  const titleEl = document.getElementById('modalTitle');
  if (titleEl) titleEl.textContent = book.title;
  const authorEl = document.getElementById('modalAuthor');
  if (authorEl) authorEl.textContent = book.author;
  const discEl = document.getElementById('modalDiscount');
  if (discEl) discEl.textContent = book.discount || '25% OFF';
  const priceEl = document.getElementById('modalPrice');
  if (priceEl) priceEl.textContent = '₹' + Number(book.price).toFixed(2);
  const mrpEl = document.getElementById('modalMRP');
  if (mrpEl) mrpEl.textContent = '₹' + Number(book.mrp).toFixed(2);

  const langEl = document.getElementById('modalLang');
  if (langEl) langEl.textContent = book.lang || 'Hindi';
  const bindEl = document.getElementById('modalBinding');
  if (bindEl) bindEl.textContent = book.binding || 'Paperback';
  const pagesEl = document.getElementById('modalPages');
  if (pagesEl) pagesEl.textContent = book.pages || '320p';
  const pubEl = document.getElementById('modalPublisher');
  if (pubEl) pubEl.textContent = book.pub || 'Lokbharti / Rajkamal';
  const dispEl = document.getElementById('modalDispatch');
  if (dispEl) dispEl.textContent = book.dispatch || 'Same-Day Prayagraj';

  const overviewEl = document.getElementById('modalOverviewText');
  if (overviewEl) overviewEl.textContent = book.overview || '';

  const highlightsContainer = document.getElementById('modalHighlightsList');
  if (highlightsContainer && book.highlights) {
    highlightsContainer.innerHTML = book.highlights.map(function(h) {
      return `
        <li style="display: flex; align-items: flex-start; gap: 8px; font-size: 12.5px; color: #334155;">
          <i data-lucide="check" style="width: 16px; height: 16px; color: #16A34A; flex-shrink: 0; margin-top: 2px;"></i>
          <span>${h}</span>
        </li>
      `;
    }).join('');
  }

  // Update modal actions
  const addBtn = document.getElementById('modalAddToCartBtn');
  if (addBtn) {
    addBtn.onclick = function() {
      addToCart(book.id || bookArg);
      closeOverviewModal();
    };
  }

  const waBtn = document.getElementById('modalWhatsAppBtn');
  if (waBtn) {
    const lines = [
      "Hello Indigo Books India!",
      "I would like to order this book:",
      "*Book:* " + book.title,
      "*Author:* " + book.author,
      "*Price:* ₹" + Number(book.price).toFixed(2),
      "*Format:* " + (book.binding || 'Paperback'),
      "Please confirm availability and share COD / Payment details!"
    ];
    const msg = lines.join("\n");
    waBtn.href = "https://wa.me/918933063306?text=" + encodeURIComponent(msg);
  }

  modal.classList.add('is-active');
  document.body.style.overflow = 'hidden';

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function closeOverviewModal() {
  const modal = document.getElementById('overviewModalOverlay');
  if (modal) modal.classList.remove('is-active');
  document.body.style.overflow = '';
}


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

function addToCart(bookId) {
  let meta = findBookMetadata(bookId);
  if (!meta) {
    meta = {
      id: bookId,
      title: 'Selected Book',
      author: 'Indigo Books India',
      price: '299.00',
      cover: 'assets/hero-godan.jpg'
    };
  }

  const idStr = String(bookId);
  const existing = cart.find(function(item) { return String(item.id) === idStr; });

  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({
      id: idStr,
      title: meta.title,
      author: meta.author,
      price: parseFloat(meta.price) || 299.00,
      cover: getAssetUrl(meta.cover),
      qty: 1
    });
  }

  updateCartUI();
  toggleCartDrawer(true);
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
  const list = document.getElementById('cartDrawerItemsList');

  const totalCount = cart.reduce(function(sum, item) { return sum + item.qty; }, 0);
  const totalPrice = cart.reduce(function(sum, item) { return sum + (item.price * item.qty); }, 0);

  if (countEl) countEl.textContent = totalCount;
  if (priceEl) priceEl.textContent = '₹' + totalPrice.toFixed(2);
  if (badgeEl) badgeEl.textContent = totalCount;
  if (subtotalEl) subtotalEl.textContent = '₹' + totalPrice.toFixed(2);

  if (!list) return;

  if (cart.length === 0) {
    list.innerHTML = `
      <div style="text-align: center; padding: 48px 16px; color: #64748B;">
        <i data-lucide="shopping-bag" style="width: 48px; height: 48px; color: #CBD5E1; margin: 0 auto 12px;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 16px; color: #0F172A; margin-bottom: 4px;">Your cart is empty</h4>
        <p style="font-size: 13px;">Add some books to read!</p>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  list.innerHTML = cart.map(function(item) {
    return `
      <div style="display: flex; gap: 14px; padding-bottom: 14px; border-bottom: 1px solid #F1F5F9;">
        <div style="width: 60px; height: 85px; border-radius: 4px; overflow: hidden; flex-shrink: 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
          <img referrerpolicy="no-referrer" src="${getAssetUrl(item.cover)}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;" />
        </div>
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14px; font-weight: 700; color: #0F172A; line-height: 1.25; margin-bottom: 2px;">
              ${item.title}
            </h4>
            <div style="font-size: 11px; color: #64748B;">${item.author}</div>
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
  const drawer = document.getElementById('cartDrawerOverlay');
  if (!drawer) return;

  if (forceOpen === true) {
    drawer.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  } else if (forceOpen === false) {
    drawer.classList.remove('is-open');
    document.body.style.overflow = '';
  } else {
    drawer.classList.toggle('is-open');
    document.body.style.overflow = drawer.classList.contains('is-open') ? 'hidden' : '';
  }
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

  const text = lines.join("\n");
  window.open("https://wa.me/918933063306?text=" + encodeURIComponent(text), '_blank');
}


// --- 7. MEMBER LOGIN MODAL ---
function toggleLoginModal() {
  const modal = document.getElementById('loginModalOverlay');
  if (!modal) return;
  modal.classList.toggle('is-active');
  document.body.style.overflow = modal.classList.contains('is-active') ? 'hidden' : '';
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
function initIndigoStore() {
  try { runVideoIntroSpotlightTour(); } catch(e) { console.warn("Spotlight:", e); }
  try { selectPodiumBook(0); } catch(e) { console.warn("Podium:", e); }
  try { switchPoet('all'); } catch(e) { console.warn("Poet:", e); }
  try { switchVaultTab('law'); } catch(e) { console.warn("Vault:", e); }
  try { renderCatalog(); } catch(e) { console.warn("Catalog:", e); }
  try { updateCartUI(); } catch(e) { console.warn("Cart:", e); }

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
"""

print("store_scripts.py created successfully.")
