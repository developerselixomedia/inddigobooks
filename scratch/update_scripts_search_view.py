# -*- coding: utf-8 -*-
import sys
import re
import subprocess

with open('store_scripts.py', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add escapeHtml and escapeJs before escapeRegex
escape_helpers = """function escapeHtml(str) {
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
  return String(str)
    .replace(/\\\\/g, '\\\\\\\\')
    .replace(/'/g, "\\\\'")
    .replace(/"/g, '\\\\"')
    .replace(/\\n/g, '\\\\n')
    .replace(/\\r/g, '');
}

"""

if 'function escapeHtml' not in js:
    js = js.replace('function escapeRegex(string) {', escape_helpers + 'function escapeRegex(string) {')
    print("Added escapeHtml and escapeJs helper functions.")

# 2. Add Dedicated Search Results Page Engine
search_results_engine = """
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

window.openSearchResultsPage = function(query) {
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
  const qLower = activeSearchQuery.toLowerCase();
  
  const matches = [];
  pool.forEach(function(b) {
    const title = (b.title || '').toLowerCase();
    const author = (b.author || b.vendor || '').toLowerCase();
    const isbn = (b.isbn || b.sku || '').toLowerCase();
    const genre = (b.genre || b.type || '').toLowerCase();
    const tags = Array.isArray(b.tags) ? b.tags.join(' ').toLowerCase() : (typeof b.tags === 'string' ? b.tags.toLowerCase() : '');

    let score = 0;
    if (title === qLower) score += 100;
    else if (title.startsWith(qLower)) score += 50;
    else if (title.includes(qLower)) score += 30;

    if (author.startsWith(qLower)) score += 30;
    else if (author.includes(qLower)) score += 20;

    if (isbn.includes(qLower)) score += 40;
    if (genre.includes(qLower)) score += 15;
    if (tags.includes(qLower)) score += 15;

    if (score > 0) {
      matches.push({ book: b, score: score });
    }
  });

  matches.sort(function(a, b) { return b.score - a.score; });
  currentSearchResultsList = matches.map(function(m) { return m.book; });

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
      const bTags = Array.isArray(b.tags) ? b.tags : (typeof b.tags === 'string' ? b.tags.split(',') : []);
      const matchesTag = bTags.some(function(t) { return t.trim().toLowerCase().includes(currentSearchCategoryFilter); });
      const matchesType = b.type && b.type.toLowerCase().includes(currentSearchCategoryFilter);
      return matchesTag || matchesType;
    });
  }

  // Sort
  if (currentSearchSortKey === 'price-asc') {
    list.sort(function(a, b) {
      const pA = parseFloat(String(a.price || '').replace(/[^\\d.]/g, '')) || 0;
      const pB = parseFloat(String(b.price || '').replace(/[^\\d.]/g, '')) || 0;
      return pA - pB;
    });
  } else if (currentSearchSortKey === 'price-desc') {
    list.sort(function(a, b) {
      const pA = parseFloat(String(a.price || '').replace(/[^\\d.]/g, '')) || 0;
      const pB = parseFloat(String(b.price || '').replace(/[^\\d.]/g, '')) || 0;
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
    const priceFormatted = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';
    const oldPriceFormatted = book.oldPrice ? (String(book.oldPrice).startsWith('₹') ? book.oldPrice : '₹' + book.oldPrice) : '';

    return `
      <div class="catalog-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 18px; display: flex; flex-direction: column; transition: transform 0.2s, box-shadow 0.2s;">
        <div class="catalog-thumb" onclick="handleBookAction('${escapeJs(book.id)}', '${escapeJs(bookUrl)}')" style="cursor: pointer; width: 100%; aspect-ratio: 2 / 3; background: #F8FAFC; border-radius: 6px; overflow: hidden; margin-bottom: 12px; position: relative;">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; display: block;" onerror="this.onerror=null; this.src=getFallbackCover('${escapeJs(titleSafe)}', '${escapeJs(authorSafe)}');" />
        </div>
        <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
          ${escapeHtml(book.discount || 'IN STOCK')}
        </div>
        <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin: 0 0 4px; min-height: 38px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
          <a href="${bookUrl || '#'}" onclick="handleBookAction('${escapeJs(book.id)}', '${escapeJs(bookUrl)}', event); return false;" style="color: inherit; text-decoration: none;">${escapeHtml(book.title)}</a>
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          ${escapeHtml(book.author || book.vendor || 'Indigo Books')}
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
          <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">${priceFormatted}</span>
          ${oldPriceFormatted ? `<span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 12px; text-decoration: line-through; color: #94A3B8; font-variant-numeric: lining-nums tabular-nums !important;">${oldPriceFormatted}</span>` : ''}
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
          <button type="button" class="btn-overview" onclick="handleBookAction('${escapeJs(book.id)}', '${escapeJs(bookUrl)}')" style="display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 9px 12px; background: #F1F5F9; color: #0F172A; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 12.5px; font-weight: 700; cursor: pointer;">
            <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
          </button>
          <button type="button" class="btn-add-cart" onclick="addToCart('${escapeJs(book.id)}', '${escapeJs(book.variantId || book.id)}')" style="display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 9px 12px; background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; font-size: 12.5px; font-weight: 700; cursor: pointer;">
            <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> + Add
          </button>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}
"""

# Replace executeFullSearch in store_scripts.py
old_execute = """function executeFullSearch(query) {
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
}"""

new_execute = """function executeFullSearch(query) {
  hideAllSearchDropdowns();
  window.openSearchResultsPage(query);
}"""

if old_execute in js:
    js = js.replace(old_execute, new_execute)
    print("Replaced executeFullSearch to invoke window.openSearchResultsPage.")

# Replace handleHeroSearch and performHeroSearch
old_hero_handlers = """function handleHeroSearch(e) {
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
}"""

new_hero_handlers = """function handleHeroSearch(e) {
  if (e && e.key === 'Enter') {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    window.submitSearch(e, 'hero-search-input');
  }
}

function performHeroSearch() {
  window.submitSearch(null, 'hero-search-input');
}"""

if old_hero_handlers in js:
    js = js.replace(old_hero_handlers, new_hero_handlers)
    print("Updated handleHeroSearch and performHeroSearch.")

# Replace performCatalogSearchEnter
old_cat_enter = """function performCatalogSearchEnter(e) {
  if (e && typeof e.preventDefault === 'function') e.preventDefault();
  const catInput = document.getElementById('catalog-search-input');
  if (catInput) {
    executeFullSearch(catInput.value);
  }
}"""

new_cat_enter = """function performCatalogSearchEnter(e) {
  if (e && typeof e.preventDefault === 'function') e.preventDefault();
  window.submitSearch(e, 'catalog-search-input');
}"""

if old_cat_enter in js:
    js = js.replace(old_cat_enter, new_cat_enter)
    print("Updated performCatalogSearchEnter.")

# Update checkHashRoute
old_check_hash = """function checkHashRoute() {
  const hash = window.location.hash;
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
}"""

new_check_hash = """function checkHashRoute() {
  const hash = window.location.hash;
  if (hash.startsWith('#/product/')) {
    const handleOrId = hash.replace('#/product/', '');
    openDedicatedProductPage(handleOrId);
  } else if (hash.startsWith('#/search')) {
    const qMatch = hash.match(/[?&]q=([^&]+)/);
    const q = qMatch ? decodeURIComponent(qMatch[1]) : '';
    if (q) {
      window.openSearchResultsPage(q);
    }
  } else if (!hash || hash === '#' || hash === '#top') {
    const pdpView = document.getElementById('single-product-page-view');
    const searchView = document.getElementById('indigo-search-results-view');
    const homeView = document.getElementById('homepage-view');
    if (pdpView && pdpView.style.display === 'block') {
      pdpView.style.display = 'none';
      if (homeView) homeView.style.display = 'block';
    }
    if (searchView && searchView.style.display === 'block') {
      searchView.style.display = 'none';
      if (homeView) homeView.style.display = 'block';
    }
  }
}"""

if old_check_hash in js:
    js = js.replace(old_check_hash, new_check_hash)
    print("Updated checkHashRoute to handle #/search?q=...")

# Update closeDedicatedProductPage
old_close_pdp = """function closeDedicatedProductPage() {
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
}"""

new_close_pdp = """function closeDedicatedProductPage() {
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

  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (typeof lucide !== 'undefined') lucide.createIcons();
}"""

if old_close_pdp in js:
    js = js.replace(old_close_pdp, new_close_pdp)
    print("Updated closeDedicatedProductPage.")

# Update initIndigoStore for URL search param
old_init_search = """      const urlParams = new URLSearchParams(window.location.search);
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
      }"""

new_init_search = """      const urlParams = new URLSearchParams(window.location.search);
      const searchParam = urlParams.get('search') || urlParams.get('q');
      if (searchParam) {
        setTimeout(function() {
          window.openSearchResultsPage(searchParam);
        }, 150);
      }"""

if old_init_search in js:
    js = js.replace(old_init_search, new_init_search)
    print("Updated initIndigoStore to invoke window.openSearchResultsPage on ?search=...")

# Append search_results_engine before closing quotes
if js.strip().endswith('"""'):
    last_quote = js.rfind('"""')
    js = js[:last_quote] + "\n" + search_results_engine + "\n" + js[last_quote:]
else:
    js += "\n" + search_results_engine

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated store_scripts.py successfully.")

# Validate with Node.js
temp_file = 'scratch/temp_val_search.js'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(js.split('"""')[1] if '"""' in js else js)

res = subprocess.run(['node', '-c', temp_file], capture_output=True, text=True)
if res.returncode == 0:
    print("Node.js syntax check PASSED with ZERO errors!")
else:
    print("Node.js syntax ERROR:")
    print(res.stderr)
    sys.exit(1)

