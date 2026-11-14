
// =========================================================================
// INDIGO BOOKS INDIA - PURE VANILLA JS ENGINE (UNIFIED & COMPLETE)
// =========================================================================


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
    /^[0-9]+-[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) ||
    /^[0-9]+--[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) ||
    /^[0-9]+\.(jpg|jpeg|png|webp)$/i.test(clean) ||
    /^[0-9a-f]{8}-[0-9a-f]{4}/i.test(clean) ||
    ((clean.endsWith('.jpg') || clean.endsWith('.jpeg') || clean.endsWith('.png') || clean.endsWith('.webp')) &&
     !clean.startsWith('hero-') && !clean.startsWith('book-') && !clean.startsWith('indigo-') && !clean.startsWith('logo'))
  );

  if (isIndianCatalogBook) {
    const pubFile = clean.replace(/^products\//, '').replace(/^\/+/, '');
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
          oldPrice: live.compare_at_price ? (String(live.compare_at_price).startsWith('₹') ? live.compare_at_price : '₹' + live.compare_at_price) : fallback.oldPrice,
          discount: fallback.discount || '25% OFF',
          badge: fallback.badge || (idx === 0 ? "NATIONAL BESTSELLER" : "TOP TRENDING"),
          rating: fallback.rating || "4.9 (10,000+)",
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
          <img referrerpolicy="no-referrer" src="${cover}" alt="${book.title}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
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
  if (typeof e === 'string') {
    currentCatalogQuery = e.toLowerCase().trim();
  } else if (e && e.target) {
    currentCatalogQuery = e.target.value.toLowerCase().trim();
  }
  renderCatalog();
}

function handleHeroSearch(e) {
  if (e) {
    if (e.key === 'Enter') {
      if (typeof e.preventDefault === 'function') e.preventDefault();
      performHeroSearch();
    }
  }
}

function performHeroSearch() {
  const input = document.getElementById('hero-search-input');
  if (input) {
    const val = input.value.trim();
    executeFullSearch(val);
  }
}

function getCatalogData() {
  let source = [];
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length > 0) {
    source = window.SHOPIFY_LIVE_PRODUCTS.slice();
  } else if (typeof CATALOG_BOOKS !== 'undefined' && Array.isArray(CATALOG_BOOKS)) {
    source = CATALOG_BOOKS.slice();
  }

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
  if (event) {
    if (typeof event.preventDefault === 'function') event.preventDefault();
    if (typeof event.stopPropagation === 'function') event.stopPropagation();
  }
  // Open dedicated Amazon-style single product details view instantly (zero 404 risk)
  openDedicatedProductPage(bookId || bookUrl);
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
    const rawCover = book.image || book.coverUrl || book.cover || '';
    let cover = getAssetUrl(rawCover, book.id);
    const authorSafe = (book.author || book.vendor || 'Indigo Books').replace(/['"]/g, ' ');
    const titleSafe = (book.title || 'Book').replace(/['"]/g, ' ');
    if (!cover) {
      cover = getFallbackCover(titleSafe, authorSafe);
    }
    const bookUrl = book.url || (book.handle ? '/products/' + book.handle : '');
    const priceFormatted = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';
    const oldPriceFormatted = book.oldPrice ? (String(book.oldPrice).startsWith('₹') ? book.oldPrice : '₹' + book.oldPrice) : '';

    return `
      <div class="catalog-card">
        <div class="catalog-thumb" onclick="handleBookAction('${book.id}', '${bookUrl}')" style="${bookUrl ? 'cursor: pointer;' : ''}">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${titleSafe}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('${titleSafe}', '${authorSafe}');" />
        </div>
        <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
          ${book.discount || 'IN STOCK'}
        </div>
        <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; min-height: 38px;">
          ${bookUrl ? `<a href="${bookUrl}" onclick="handleBookAction('${book.id}', '${bookUrl}', event)" style="color: inherit; text-decoration: none;">${book.title}</a>` : `<span onclick="handleBookAction('${book.id}', '', event)" style="cursor: pointer;">${book.title}</span>`}
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          ${book.author || book.vendor || 'Indigo Books'}
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
          <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${priceFormatted}</span>
          ${oldPriceFormatted ? `<span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 12px; text-decoration: line-through; color: #94A3B8; font-variant-numeric: lining-nums tabular-nums !important;">${oldPriceFormatted}</span>` : ''}
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
  const navCountEl = document.getElementById('nav-cart-count');
  const navTotalEl = document.getElementById('nav-cart-total');
  const drawerItemCountEl = document.getElementById('cartItemCount');
  const list = document.getElementById('cartDrawerItemsList');

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

  if (cart.length === 0) {
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
  }

  list.innerHTML = cart.map(function(item) {
    return `
      <div style="display: flex; gap: 14px; padding-bottom: 14px; border-bottom: 1px solid #F1F5F9;">
        <div style="width: 60px; height: 85px; border-radius: 4px; overflow: hidden; flex-shrink: 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
          <img referrerpolicy="no-referrer" src="${getAssetUrl(item.cover)}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
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



// =========================================================================
// --- DEDICATED AMAZON-STYLE SINGLE PRODUCT PAGE ENGINE ---
// =========================================================================
let currentActivePdpBook = null;
let currentPdpQuantity = 1;

function findBookByAnyIdentifier(query) {
  if (!query) return null;
  const qStr = String(query).toLowerCase().trim().replace(/^\/products\//, '').replace(/^#\/product\//, '');
  
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

function renderPdpRecommendations(activeBook) {
  const container = document.getElementById('pdpRecContainer');
  if (!container) return;

  const author = (activeBook.author || activeBook.vendor || '').trim();
  const titleEl = document.getElementById('pdpMoreByAuthorTitle');
  if (titleEl) {
    titleEl.textContent = author ? `More Books by ${author}` : 'Readers Also Bought / Curated Selections';
  }
  const subtitleEl = document.getElementById('pdpMoreByAuthorSubtitle');
  if (subtitleEl) {
    subtitleEl.textContent = author ? `Explore more acclaimed editions and literary works by ${author}.` : 'Curated literature often ordered together with this title.';
  }

  const catalog = getCatalogData();
  
  // 1. Same author books (excluding active book)
  const sameAuthor = catalog.filter(function(b) {
    if (String(b.id) === String(activeBook.id) || b.title === activeBook.title) return false;
    const bAuthor = (b.author || b.vendor || '').toLowerCase().trim();
    const targetAuthor = author.toLowerCase().trim();
    return bAuthor && targetAuthor && (bAuthor.includes(targetAuthor) || targetAuthor.includes(bAuthor));
  });

  // 2. Fill up to 4 books with same genre / category
  let recommendations = [...sameAuthor];
  if (recommendations.length < 4) {
    const sameGenre = catalog.filter(function(b) {
      if (String(b.id) === String(activeBook.id) || b.title === activeBook.title) return false;
      if (recommendations.some(r => String(r.id) === String(b.id))) return false;
      return b.type && activeBook.type && b.type === activeBook.type;
    });
    recommendations = recommendations.concat(sameGenre);
  }

  // 3. Fill up to 4 books from general catalog if still needed
  if (recommendations.length < 4) {
    const remaining = catalog.filter(function(b) {
      if (String(b.id) === String(activeBook.id) || b.title === activeBook.title) return false;
      return !recommendations.some(r => String(r.id) === String(b.id));
    });
    recommendations = recommendations.concat(remaining);
  }

  const finalFour = recommendations.slice(0, 4);

  container.innerHTML = finalFour.map(function(book) {
    const rawCover = book.image || book.coverUrl || book.cover || '';
    const cover = getAssetUrl(rawCover, book.id) || getFallbackCover(book.title, book.author);
    const priceFormatted = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';

    return `
      <div class="catalog-card">
        <div class="catalog-thumb" onclick="openDedicatedProductPage('${book.id || book.handle}')" style="cursor: pointer;">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${book.title}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('${book.title}', '${book.author}');" />
        </div>
        <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
          ${book.discount || 'CURATED'}
        </div>
        <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 14px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; min-height: 36px;">
          <a href="javascript:void(0)" onclick="openDedicatedProductPage('${book.id || book.handle}')" style="color: inherit; text-decoration: none;">${book.title}</a>
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 10px;">
          <a href="javascript:void(0)" onclick="filterCatalogByAuthor('${book.author || book.vendor || 'Indigo Books'}')" style="color: inherit; text-decoration: none;">
            ${book.author || book.vendor || 'Indigo Books'}
          </a>
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
  try { runVideoIntroSpotlightTour(); } catch(e) {}
  try { selectPodiumBook(0); } catch(e) {}
  try { switchPoet('all'); } catch(e) {}
  try { switchVaultTab('law'); } catch(e) {}
  try { renderCatalog(); } catch(e) {}
  try { updateCartUI(); } catch(e) {}
  try { checkHashRoute(); } catch(e) {}

  // Handle incoming search query parameter if any
  try {
    if (typeof window !== 'undefined' && window.location && window.location.search) {
      const urlParams = new URLSearchParams(window.location.search);
      const searchParam = urlParams.get('search') || urlParams.get('q');
      if (searchParam) {
        currentCatalogQuery = searchParam.toLowerCase().trim();
        const heroIn = document.getElementById('hero-search-input');
        if (heroIn) heroIn.value = searchParam;
        const catIn = document.getElementById('catalog-search-input');
        if (catIn) catIn.value = searchParam;
        setTimeout(function() {
          scrollToCatalog('all');
          renderCatalog();
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
  // 1. From live products or CATALOG_BOOKS
  const cat = getCatalogData();
  cat.forEach(function(b) {
    if (b && b.title) map.set(String(b.id || b.title), b);
  });
  // 2. From PODIUM_BOOKS
  if (typeof PODIUM_BOOKS !== 'undefined' && Array.isArray(PODIUM_BOOKS)) {
    PODIUM_BOOKS.forEach(function(b) {
      if (b && b.title && !map.has(String(b.id || b.title))) map.set(String(b.id || b.title), b);
    });
  }
  // 3. From VAULT_BOOKS
  if (typeof VAULT_BOOKS !== 'undefined') {
    Object.keys(VAULT_BOOKS).forEach(function(k) {
      (VAULT_BOOKS[k] || []).forEach(function(b) {
        if (b && b.title && !map.has(String(b.id || b.title))) map.set(String(b.id || b.title), b);
      });
    });
  }
  return Array.from(map.values());
}

let searchDebounceTimer = null;

function escapeRegex(string) {
  return string.replace(/[-\/\^$*+?.()|[\]{}]/g, '\$&');
}

function highlightSearchMatch(text, query) {
  if (!text) return '';
  if (!query) return escapeHtml(text);
  const re = new RegExp('(' + escapeRegex(query) + ')', 'gi');
  return escapeHtml(text).replace(re, '<mark>$1</mark>');
}

function handleSearchInput(query, targetId) {
  const q = (typeof query === 'string' ? query : (query && query.target ? query.target.value : '')).trim();
  const dropdownId = targetId === 'hero' ? 'hero-search-suggestions' : 'catalog-search-suggestions';
  const dropdown = document.getElementById(dropdownId);
  if (!dropdown) return;

  clearTimeout(searchDebounceTimer);
  if (q.length < 2) {
    dropdown.style.display = 'none';
    dropdown.innerHTML = '';
    return;
  }

  searchDebounceTimer = setTimeout(function() {
    renderSearchSuggestions(q, dropdown, targetId);
  }, 120);
}

function renderSearchSuggestions(query, dropdown, targetId) {
  const pool = getUnifiedSearchPool();
  const q = query.toLowerCase();
  
  const matches = [];
  pool.forEach(function(b) {
    const title = (b.title || '').toLowerCase();
    const author = (b.author || b.vendor || '').toLowerCase();
    const isbn = (b.isbn || b.sku || '').toLowerCase();
    const genre = (b.genre || b.type || '').toLowerCase();

    let score = 0;
    if (title === q) score += 100;
    else if (title.startsWith(q)) score += 50;
    else if (title.includes(q)) score += 30;

    if (author.startsWith(q)) score += 25;
    else if (author.includes(q)) score += 15;

    if (isbn.includes(q)) score += 40;
    if (genre.includes(q)) score += 10;

    if (score > 0) {
      matches.push({ book: b, score: score });
    }
  });

  matches.sort(function(a, b) { return b.score - a.score; });
  const topMatches = matches.slice(0, 6);

  if (topMatches.length === 0) {
    dropdown.innerHTML = '<div style="padding: 16px; text-align: center; color: #64748B; font-size: 13px;">No titles found for "<strong>' + escapeHtml(query) + '</strong>"</div>';
    dropdown.style.display = 'block';
    return;
  }

  const itemsHtml = topMatches.map(function(m) {
    const book = m.book;
    const cover = getAssetUrl(book.image || book.coverUrl || book.cover || '', book.id);
    const titleSafe = (book.title || 'Book').replace(/['"]/g, ' ');
    const authorSafe = (book.author || book.vendor || 'Indigo Books').replace(/['"]/g, ' ');
    const priceFormatted = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';
    const bookUrl = book.url || (book.handle ? '/products/' + book.handle : '');

    return `
      <div class="search-suggestion-item" onclick="selectSearchSuggestion('${escapeJs(book.id)}', '${escapeJs(bookUrl)}')">
        <img class="suggestion-thumb" src="${cover}" alt="${titleSafe}" onerror="this.onerror=null; this.src=getFallbackCover('${escapeJs(titleSafe)}', '${escapeJs(authorSafe)}');" />
        <div class="suggestion-details">
          <div class="suggestion-title">${highlightSearchMatch(book.title || '', query)}</div>
          <div class="suggestion-author">${highlightSearchMatch(book.author || book.vendor || 'Indigo Books', query)}</div>
        </div>
        <div class="suggestion-price">${priceFormatted}</div>
      </div>
    `;
  }).join('');

  dropdown.innerHTML = `
    <div class="search-suggestions-header">Quick Results (${matches.length} matches)</div>
    ${itemsHtml}
    <div class="search-suggestions-footer" onclick="executeFullSearch('${escapeJs(query)}')">
      View all ${matches.length} results in Catalog &rarr;
    </div>
  `;
  dropdown.style.display = 'block';
}

function selectSearchSuggestion(bookId, bookUrl) {
  hideAllSearchDropdowns();
  openDedicatedProductPage(bookId || bookUrl);
}

function executeFullSearch(query) {
  hideAllSearchDropdowns();
  const q = (query || '').trim();
  const catSection = document.getElementById('shop-all-catalog');
  if (catSection) {
    currentCatalogQuery = q.toLowerCase();
    const catInput = document.getElementById('catalog-search-input');
    if (catInput) catInput.value = q;
    const heroInput = document.getElementById('hero-search-input');
    if (heroInput) heroInput.value = q;
    scrollToCatalog('all');
    renderCatalog();
  } else {
    window.location.href = '/?search=' + encodeURIComponent(q) + '#shop-all-catalog';
  }
}

function performCatalogSearchEnter(e) {
  if (e && typeof e.preventDefault === 'function') e.preventDefault();
  const catInput = document.getElementById('catalog-search-input');
  if (catInput) {
    executeFullSearch(catInput.value);
  }
}

function hideAllSearchDropdowns() {
  const d1 = document.getElementById('hero-search-suggestions');
  if (d1) d1.style.display = 'none';
  const d2 = document.getElementById('catalog-search-suggestions');
  if (d2) d2.style.display = 'none';
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

