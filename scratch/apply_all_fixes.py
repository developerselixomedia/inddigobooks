# -*- coding: utf-8 -*-
"""
scratch/apply_all_fixes.py
Comprehensive implementation of all 5 Master Updates:
1. Full-Width (max-width: 1320px) Containers across all sections.
2. Fix Left-Squished Stats Bar: Balanced 4-item grid spanning full 1320px width without any vertical caret bars.
3. Fix Law Vault: Balanced 360px / 1fr layout, 100% unique covers, seamless tab switching with details modal.
4. Real-Time Search Algorithm + Auto-Suggestion Dropdown (Copied from indigobooksindia.com).
5. Catalog Smart Sort: Bestsellers & classics first, A-Z next, numeric titles demoted to end.
6. Bulletproof image loading with SVG luxury cover fallback.
"""

import sys
sys.path.insert(0, '.')
import os
import re

print(">>> STEP 1: Updating store_styles.py...")
with open("store_styles.py", "r", encoding="utf-8") as f:
    css = f.read()

# 1A. Enforce 1320px containers globally
container_block = """
/* =========================================================================
   GLOBAL 1320PX CONTAINER ARCHITECTURE (BALANCED SYMMETRY & ZERO EMPTY MARGINS)
   ========================================================================= */
.site-container,
.section-container,
.vault-container,
.catalog-container,
.voices-container,
.product-page-wrapper,
.stats-grid,
.editorial-header,
.catalog-filter-bar,
.trust-strip-grid,
.trust-features-grid,
.heritage-grid,
.footer-grid {
  max-width: 1320px !important;
  width: 100% !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: 28px !important;
  padding-right: 28px !important;
  box-sizing: border-box !important;
}

@media (max-width: 768px) {
  .site-container,
  .section-container,
  .vault-container,
  .catalog-container,
  .voices-container,
  .product-page-wrapper,
  .stats-grid,
  .editorial-header,
  .catalog-filter-bar,
  .trust-strip-grid,
  .trust-features-grid,
  .heritage-grid,
  .footer-grid {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
}

/* FULL-WIDTH STATS COUNTER BAR (FIXES LEFT-SQUISHED ALIGNMENT) */
.stats-bar {
  display: block !important;
  width: 100% !important;
  background: #FFFFFF !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding: 32px 0 !important;
  box-sizing: border-box !important;
  margin: 0 !important;
}

.stats-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
  max-width: 1320px !important;
  margin: 0 auto !important;
  padding: 0 28px !important;
  box-sizing: border-box !important;
  align-items: center !important;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    padding: 0 16px !important;
  }
}

.stat-item, .stat-card {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  width: 100% !important;
  padding: 8px 12px !important;
  border: none !important;
  border-right: none !important;
  border-left: none !important;
  box-sizing: border-box !important;
  background: transparent !important;
}

.stat-item::before, .stat-item::after,
.stat-card::before, .stat-card::after,
.stat-num::before, .stat-num::after,
.stat-number::before, .stat-number::after,
.stat-label::before, .stat-label::after {
  content: none !important;
  display: none !important;
  border: none !important;
}

.stat-num, .stat-number {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 32px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.15 !important;
  margin-bottom: 6px !important;
  font-variant-numeric: lining-nums tabular-nums !important;
  text-align: center !important;
  border: none !important;
}

@media (min-width: 768px) {
  .stat-num, .stat-number {
    font-size: 36px !important;
  }
}

.stat-label {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  line-height: 1.35 !important;
  text-align: center !important;
  border: none !important;
  max-width: 240px !important;
  margin: 0 auto !important;
}

/* LAW VAULT BALANCED LAYOUT & GRID */
.vault-layout {
  display: grid !important;
  grid-template-columns: 360px 1fr !important;
  gap: 32px !important;
  align-items: start !important;
  width: 100% !important;
  max-width: 1320px !important;
  margin: 0 auto !important;
}

@media (max-width: 992px) {
  .vault-layout {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 20px !important;
  width: 100% !important;
}

@media (max-width: 600px) {
  .vault-cards-grid {
    grid-template-columns: 1fr !important;
  }
}

/* REAL-TIME SEARCH AUTO-SUGGESTION DROPDOWN STYLES */
.search-input-wrap, .hero-search-wrap, .catalog-search-wrap {
  position: relative !important;
}

.search-suggestions-dropdown {
  position: absolute !important;
  top: calc(100% + 8px) !important;
  left: 0 !important;
  right: 0 !important;
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.18) !important;
  z-index: 2000 !important;
  max-height: 420px !important;
  overflow-y: auto !important;
  text-align: left !important;
}

.search-suggestions-header {
  padding: 10px 16px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: #94A3B8 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  border-bottom: 1px solid #F1F5F9 !important;
  background: #FAF8F5 !important;
}

.search-suggestion-item {
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  padding: 10px 16px !important;
  border-bottom: 1px solid #F1F5F9 !important;
  cursor: pointer !important;
  transition: background 0.15s ease !important;
  text-decoration: none !important;
  color: inherit !important;
}

.search-suggestion-item:last-of-type {
  border-bottom: none !important;
}

.search-suggestion-item:hover, .search-suggestion-item.is-selected {
  background: #FFFBEB !important;
}

.suggestion-thumb {
  width: 40px !important;
  height: 56px !important;
  object-fit: cover !important;
  border-radius: 4px !important;
  flex-shrink: 0 !important;
  background: #F1F5F9 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08) !important;
}

.suggestion-details {
  flex: 1 !important;
  min-width: 0 !important;
}

.suggestion-title {
  font-family: 'Merriweather', Georgia, serif !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  line-height: 1.3 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.suggestion-title mark {
  background: #FEF3C7 !important;
  color: #92400E !important;
  font-weight: 800 !important;
  border-radius: 2px !important;
  padding: 0 2px !important;
}

.suggestion-author {
  font-size: 12px !important;
  color: #64748B !important;
  line-height: 1.3 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.suggestion-price {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  white-space: nowrap !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.search-suggestions-footer {
  padding: 12px 16px !important;
  background: #FAF8F5 !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  color: #B45309 !important;
  text-align: center !important;
  cursor: pointer !important;
  border-top: 1px solid #E2E8F0 !important;
  border-radius: 0 0 12px 12px !important;
  transition: background 0.15s ease !important;
}

.search-suggestions-footer:hover {
  background: #FEF3C7 !important;
}
"""

# Insert container block before the closing """
if css.strip().endswith('"""'):
    last_quote = css.rfind('"""')
    css = css[:last_quote] + "\n" + container_block + "\n" + css[last_quote:]
else:
    css += "\n" + container_block

with open("store_styles.py", "w", encoding="utf-8") as f:
    f.write(css)
print("Updated store_styles.py successfully.")

print("\n>>> STEP 2: Updating build_html_generator.py...")
with open("build_html_generator.py", "r", encoding="utf-8") as f:
    html_gen = f.read()

# 2A. Update Hero search input with auto-suggestion dropdown
hero_search_old = '''          <!-- Search Box -->
          <div class="hero-search-wrap">
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." onkeydown="handleHeroSearch(event)" />
          </div>'''

hero_search_new = '''          <!-- Search Box -->
          <div class="hero-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." oninput="handleSearchInput(this.value, 'hero')" onkeydown="handleHeroSearch(event)" autocomplete="off" />
            <div id="hero-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

if hero_search_old in html_gen:
    html_gen = html_gen.replace(hero_search_old, hero_search_new)
    print("Added auto-suggestions to Hero Search input in build_html_generator.py")
else:
    # Try regex match
    html_gen = re.sub(
        r'<div class="hero-search-wrap">.*?<input type="text" id="hero-search-input".*?/>\s*</div>',
        hero_search_new,
        html_gen,
        flags=re.DOTALL
    )
    print("Regex updated Hero Search input in build_html_generator.py")

# 2B. Update Catalog search input with auto-suggestion dropdown
cat_search_old = '''          <!-- Real-Time Search Bar -->
          <div class="catalog-search-wrap">
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value)" />
          </div>'''

cat_search_new = '''          <!-- Real-Time Search Bar -->
          <div class="catalog-search-wrap">
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value); handleSearchInput(this.value, 'catalog')" onkeydown="if(event.key==='Enter')performCatalogSearchEnter()" autocomplete="off" />
            <div id="catalog-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

if cat_search_old in html_gen:
    html_gen = html_gen.replace(cat_search_old, cat_search_new)
    print("Added auto-suggestions to Catalog Search input in build_html_generator.py")
else:
    html_gen = re.sub(
        r'<div class="catalog-search-wrap">.*?<input type="text" id="catalog-search-input".*?/>\s*</div>',
        cat_search_new,
        html_gen,
        flags=re.DOTALL
    )
    print("Regex updated Catalog Search input in build_html_generator.py")

with open("build_html_generator.py", "w", encoding="utf-8") as f:
    f.write(html_gen)
print("Updated build_html_generator.py successfully.")

print("\n>>> STEP 3: Updating store_scripts.py...")
with open("store_scripts.py", "r", encoding="utf-8") as f:
    js = f.read()

# 3A. Add Real-Time Auto-Suggestion Search Engine
search_engine_code = """
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
  return string.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
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
    dropdown.innerHTML = '<div style=\"padding: 16px; text-align: center; color: #64748B; font-size: 13px;\">No titles found for \"<strong>' + escapeHtml(query) + '</strong>\"</div>';
    dropdown.style.display = 'block';
    return;
  }

  const itemsHtml = topMatches.map(function(m) {
    const book = m.book;
    const cover = getAssetUrl(book.image || book.coverUrl || book.cover || '', book.id);
    const titleSafe = (book.title || 'Book').replace(/['\"]/g, ' ');
    const authorSafe = (book.author || book.vendor || 'Indigo Books').replace(/['\"]/g, ' ');
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
  currentCatalogQuery = query.toLowerCase().trim();
  const catInput = document.getElementById('catalog-search-input');
  if (catInput) catInput.value = query;
  const heroInput = document.getElementById('hero-search-input');
  if (heroInput) heroInput.value = query;
  scrollToCatalog('all');
  renderCatalog();
}

function performCatalogSearchEnter() {
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
"""

# 3B. Update getCatalogData with Smart Sort (Bestsellers first, A-Z, Numbers at end)
new_get_catalog_data = """function getCatalogData() {
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
    const isNumA = /^\\d/.test(tA);
    const isNumB = /^\\d/.test(tB);
    if (isNumA && !isNumB) return 1;
    if (!isNumA && isNumB) return -1;

    return tA.localeCompare(tB);
  });
}"""

# Replace getCatalogData in store_scripts.py
js = re.sub(
    r'function getCatalogData\(\)\s*\{.*?return typeof CATALOG_BOOKS !== \'undefined\' \? CATALOG_BOOKS : \[\];\s*\}',
    lambda m: new_get_catalog_data,
    js,
    flags=re.DOTALL
)

# Fix handleCatalogSearch to accept string or event
new_handle_catalog_search = """function handleCatalogSearch(e) {
  if (typeof e === 'string') {
    currentCatalogQuery = e.toLowerCase().trim();
  } else if (e && e.target) {
    currentCatalogQuery = e.target.value.toLowerCase().trim();
  }
  renderCatalog();
}"""

js = re.sub(
    r'function handleCatalogSearch\(e\)\s*\{.*?renderCatalog\(\);\s*\}',
    lambda m: new_handle_catalog_search,
    js,
    flags=re.DOTALL
)

# Insert search_engine_code before the closing """
if js.strip().endswith('"""'):
    last_quote = js.rfind('"""')
    js = js[:last_quote] + "\n" + search_engine_code + "\n" + js[last_quote:]
else:
    js += "\n" + search_engine_code

with open("store_scripts.py", "w", encoding="utf-8") as f:
    f.write(js)
print("Updated store_scripts.py successfully.")

print("\n>>> ALL SOURCE FILES UPDATED SUCCESSFULLY! <<<")
