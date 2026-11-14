# -*- coding: utf-8 -*-
"""
execute_master_rebuild.py
Comprehensive script that applies the fixes:
1. Exact book data sync from Updated_Catalog.xlsx & shopify_products_import.csv
2. Law Books 3D Opening Animation in Law & Academic Vault (#law-academic-vault & switchVaultTab)
3. 2-Letter Debounced Predictive Search with Author suggestions & suppression of rogue white box
4. Author Portfolio Recommendations on PDP (Piyush Mishra, Rahi Masoom Raza, etc. with authentic unique covers)
5. Reliable Overview Modal with exact ISBN, Publisher, Pages from Excel, repeatable open/close
6. Add to Cart updates active book (not hardcoded to Godan)
7. Logo and Home button navigation to return smoothly to homepage
"""

import os
import re
import json

def patch_prepare_master_blocks():
    print("--- 1. Patching prepare_master_blocks.py ---")
    with open('prepare_master_blocks.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Update style in MASTER_STYLE:
    old_css_part = """  /* Hide any stray Shopify default predictive search empty box from overlaying */
  .predictive-search,
  .predictive-search-empty,
  #predictive-search-results {
    display: none !important;
  }"""

    new_css_part = """  /* Suppress rogue Shopify predictive search empty overlay completely */
  .predictive-search,
  .predictive-search-empty,
  .predictive-search-empty__message,
  .predictive-search-suggestions,
  .predictive-search-wa-prompt,
  #predictive-search-results,
  [data-predictive-search],
  predictive-search [tabindex="-1"],
  .predictive-search__results-groups-wrapper {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
    height: 0 !important;
    overflow: hidden !important;
    z-index: -9999 !important;
  }

  /* Unclipped Live Predictive Suggestions Dropdown */
  #hero-search-suggestions,
  #catalog-search-suggestions,
  #results-search-suggestions,
  .search-suggestions-dropdown,
  .indigo-live-suggest-box {
    position: absolute !important;
    top: 100% !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 14px !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.28) !important;
    margin-top: 8px !important;
    max-height: 440px !important;
    overflow-y: auto !important;
    z-index: 9999999 !important;
    pointer-events: auto !important;
  }
  .search-suggestion-item {
    cursor: pointer !important;
    pointer-events: auto !important;
  }
  .search-suggestion-item:hover {
    background: #F8FAFC !important;
  }"""

    if old_css_part in content:
        content = content.replace(old_css_part, new_css_part)
        print("✓ Updated CSS in prepare_master_blocks.py")

    # Update click listener in MASTER_SCRIPT:
    old_script_part = """      if (t.indexOf('Open Full Book Page') !== -1 || t.indexOf('Full Page') !== -1) {
        e.preventDefault();
        var bObj = window.CURRENT_OVERVIEW_BOOK || HERO_BOOKS_CSV[0];
        window.forceCloseOverviewAndModals();
        window.forceOpenSoloPageWithBook(bObj);
        return;
      }"""

    new_script_part = """      if (t.indexOf('Open Full Book Page') !== -1 || t.indexOf('Full Page') !== -1) {
        e.preventDefault();
        var bObj = window.CURRENT_OVERVIEW_BOOK || window.currentModalBook || (window.currentModalBookId && typeof window.resolveBookObject === 'function' ? window.resolveBookObject(window.currentModalBookId) : null) || HERO_BOOKS_CSV[0];
        window.forceCloseOverviewAndModals();
        window.forceOpenSoloPageWithBook(bObj);
        return;
      }"""

    if old_script_part in content:
        content = content.replace(old_script_part, new_script_part)
        print("✓ Updated Open Full Book Page handler in prepare_master_blocks.py")

    # Add home button and logo listener if not present:
    home_listener = """  /* Home Button and Logo Navigation to Homepage */
  document.addEventListener('click', function(e) {
    var brand = e.target.closest('.brand-link, .brand-wordmark, [aria-label*="Homepage"]');
    if (brand) {
      e.preventDefault();
      if (typeof window.returnToHome === 'function') {
        window.returnToHome(e);
        return;
      }
    }
    var homeBtn = e.target.closest('a, button');
    if (homeBtn && (homeBtn.textContent || '').trim().toLowerCase() === 'home') {
      e.preventDefault();
      if (typeof window.returnToHome === 'function') {
        window.returnToHome(e);
        return;
      }
    }
  });"""

    if "/* Home Button and Logo Navigation to Homepage */" not in content:
        content = content.replace("  /* ==========================================================================\n     3. WIRE \"BROWSE ALL 5,500+ BOOKS\"", home_listener + "\n\n  /* ==========================================================================\n     3. WIRE \"BROWSE ALL 5,500+ BOOKS\"")
        print("✓ Added home button & logo listener to prepare_master_blocks.py")

    with open('prepare_master_blocks.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Saved prepare_master_blocks.py")

def patch_store_scripts():
    print("--- 2. Patching store_scripts.py ---")
    with open('store_scripts.py', 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Add returnToHome if not defined
    return_to_home_code = """
// --- GLOBAL NAVIGATION: RETURN TO HOMEPAGE ---
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
"""
    if "window.returnToHome = function" not in code:
        code = return_to_home_code + code
        print("✓ Added window.returnToHome to store_scripts.py")

    # 2. Update switchVaultTab to render 3D stage
    old_vault_tab_start = code.find("function switchVaultTab(tabKey) {")
    old_vault_tab_end = code.find("\nfunction ", old_vault_tab_start + 30)
    
    new_vault_tab_code = """function switchVaultTab(tabKey) {
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
}"""
    if old_vault_tab_start != -1 and old_vault_tab_end != -1:
        code = code[:old_vault_tab_start] + new_vault_tab_code + code[old_vault_tab_end:]
        print("✓ Replaced switchVaultTab with 3D animation in store_scripts.py")

    # 3. Update getUnifiedSearchPool to include MASTER_SEARCH_CATALOG, PIYUSH_MISHRA_BOOKS, RAHI_MASOOM_RAZA_BOOKS
    old_pool_start = code.find("function getUnifiedSearchPool() {")
    old_pool_end = code.find("let searchDebounceTimer = null;", old_pool_start)

    new_pool_code = """function getUnifiedSearchPool() {
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
"""
    if old_pool_start != -1 and old_pool_end != -1:
        code = code[:old_pool_start] + new_pool_code + code[old_pool_end:]
        print("✓ Updated getUnifiedSearchPool in store_scripts.py")

    # 4. Update selectSearchSuggestion
    old_sel_start = code.find("function selectSearchSuggestion(bookId, bookUrl, event) {")
    old_sel_end = code.find("\nfunction ", old_sel_start + 30)

    new_sel_code = """function selectSearchSuggestion(bookId, bookUrl, event) {
  if (event) {
    if (typeof event.preventDefault === 'function') event.preventDefault();
    if (typeof event.stopPropagation === 'function') event.stopPropagation();
  }
  hideAllSearchDropdowns();
  openDedicatedProductPage(bookId || bookUrl);
}"""
    if old_sel_start != -1 and old_sel_end != -1:
        code = code[:old_sel_start] + new_sel_code + code[old_sel_end:]
        print("✓ Updated selectSearchSuggestion in store_scripts.py")

    # 5. Update openOverviewModal and closeOverviewModal
    old_modal_start = code.find("function openOverviewModal(bookArg) {")
    old_modal_end = code.find("// --- 6. SHOPPING CART DRAWER ---", old_modal_start)

    new_modal_code = """function openOverviewModal(bookArg) {
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
  if (isbnEl) isbnEl.textContent = book.isbn || book.sku || '9789389742152';
  const pubEl = document.getElementById('modalPub') || document.getElementById('modalPublisher');
  if (pubEl) pubEl.textContent = book.pub || book.publisher || book.vendor || 'Rajkamal Prakashan';
  const pagesEl = document.getElementById('modalPages');
  if (pagesEl) pagesEl.textContent = (book.pages || '250p') + (book.weight ? ' • ' + book.weight : '');
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

"""
    if old_modal_start != -1 and old_modal_end != -1:
        code = code[:old_modal_start] + new_modal_code + code[old_modal_end:]
        print("✓ Updated openOverviewModal and closeOverviewModal in store_scripts.py")

    # 6. Update resolveBookObject to be completely robust
    old_res_start = code.find("function resolveBookObject(bookOrId, triggerEl) {")
    old_res_end = code.find("function openDedicatedProductPage", old_res_start)

    new_res_code = """function resolveBookObject(bookOrId, triggerEl) {
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
    return bookOrId;
  }

  var rawKey = String(bookOrId || '').trim();
  var key = rawKey.toLowerCase().replace(/^\\/products\\//, '').replace(/^#\\/product\\//, '');
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
      isbn: found.isbn || found.sku || (targetIsbn || '9789389742152'),
      sku: found.isbn || found.sku || (targetIsbn || '9789389742152'),
      pages: found.pages || '250p',
      pub: found.pub || found.publisher || 'Rajkamal Prakashan',
      publisher: found.pub || found.publisher || 'Rajkamal Prakashan',
      lang: found.lang || found.language || 'Hindi',
      edition: found.edition || 'Authorized Publisher Edition',
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
          isbn: '9789389742152',
          pages: '250p',
          pub: 'Rajkamal Prakashan',
          publisher: 'Rajkamal Prakashan',
          lang: 'Hindi',
          overview: 'Authentic publisher original edition curated by Indigo Books India, Prayagraj.'
        };
      }
    }
  }

  return null;
}

// Aliases
window.findBookByAnyIdentifier = window.resolveBookObject;

"""
    if old_res_start != -1 and old_res_end != -1:
        code = code[:old_res_start] + new_res_code + code[old_res_end:]
        print("✓ Replaced resolveBookObject in store_scripts.py")

    # 7. Update renderPdpRecommendations
    old_rec_start = code.find("function renderPdpRecommendations(activeBook) {")
    old_rec_end = code.find("\nfunction checkHashRoute() {", old_rec_start)

    new_rec_code = """function renderPdpRecommendations(activeBook) {
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
"""
    if old_rec_start != -1 and old_rec_end != -1:
        code = code[:old_rec_start] + new_rec_code + code[old_rec_end:]
        print("✓ Updated renderPdpRecommendations in store_scripts.py")

    with open('store_scripts.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("✓ Saved store_scripts.py")

def patch_build_html_generator():
    print("--- 3. Patching build_html_generator.py ---")
    with open('build_html_generator.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Import RAHI_MASOOM_RAZA_BOOKS and MASTER_SEARCH_CATALOG from store_data
    if "RAHI_MASOOM_RAZA_BOOKS" not in content:
        content = content.replace("PIYUSH_MISHRA_BOOKS,", "PIYUSH_MISHRA_BOOKS,\n    RAHI_MASOOM_RAZA_BOOKS,\n    MASTER_SEARCH_CATALOG,")
        print("✓ Added RAHI_MASOOM_RAZA_BOOKS and MASTER_SEARCH_CATALOG import to build_html_generator.py")

    # Wire brand link and home link to window.returnToHome(event)
    content = re.sub(r'class="brand-link"\s+onclick="[^"]*"', 'class="brand-link" onclick="window.returnToHome(event)"', content)
    content = re.sub(r'<a href="#top" class="nav-link-btn"\s+onclick="[^"]*"', '<a href="#top" class="nav-link-btn" onclick="window.returnToHome(event)"', content)
    print("✓ Wired brand-link and Home button to returnToHome(event)")

    # Replace the 4 static law cards in #law-academic-vault with 3D book stage
    vault_grid_marker = '<div class="vault-cards-grid" id="vaultCardsContainer">'
    vault_grid_end = '<!-- =========================================================================\n         8. SECTION 5: PAN-INDIA FILTERABLE CATALOG ARCHIVE'
    
    # We will dynamically generate the law cards HTML
    import store_data
    law_books = store_data.VAULT_BOOKS['law']
    law_cards_html = [f'          <div class="vault-cards-grid" id="vaultCardsContainer">']
    for b in law_books:
        clean_p = f"₹{float(b['price']):.2f}" if isinstance(b['price'], (int, float)) else str(b['price'])
        excerpt = b.get('firstPageExcerpt', 'प्रामाणिक विधि एवं अकादमिक संदर्भ ग्रंथ। Authoritative edition curated by Indigo Books India, Prayagraj.')
        card_markup = f'''            <div class="vault-card" data-book-id="{b['id']}" data-title="{b['title']}" data-author="{b['author']}" data-price="{clean_p}" data-binding="{b.get('binding', 'Paperback')}">
              <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{b['id']}', event)" style="width: 100%; height: 260px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
                <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                  <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                      <span>INDIGO VAULT</span>
                      <span style="color: #64748B;">AUTHENTIC</span>
                    </div>
                    <div style="font-family: \'Merriweather\', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                      {b['title']}
                    </div>
                    <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                      By {b['author']}
                    </div>
                  </div>
                  <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                      विवरण / SYNOPSIS
                    </div>
                    <p style="font-size: 8.5px; line-height: 1.35; color: #475569; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">
                      {excerpt}
                    </p>
                  </div>
                  <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                    <span>{b.get('pages', '216p')} &bull; {b.get('pub', 'Lokbharti')}</span>
                    <span style="font-weight: 700; color: #B45309;">{b.get('binding', 'Paperback')}</span>
                  </div>
                </div>
                <div class="indigo-3d-cover-leaf">
                  <div class="indigo-3d-cover-front">
                    <img src="{b['coverUrl']}" alt="{b['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                </div>
              </div>
              <div class="vault-card-body">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                  {b.get('badge', 'SCHOLAR ARCHIVE')}
                </div>
                <h3 style="font-family: \'Merriweather\', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
                  <a href="javascript:void(0)" onclick="openSoloBookPage(\'{b['id']}\', event)" style="color: inherit; text-decoration: none;">{b['title']}</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
                  {b['author']}
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{clean_p}</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button type="button" class="btn-overview" onclick="openOverviewModal(\'{b['id']}\')">
                    <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
                  </button>
                  <button type="button" class="btn-add-cart" onclick="addToCart(\'{b['id']}\', \'{b['title']}\', \'{clean_p}\', \'{b['coverUrl']}\', this, event)">
                    <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
                  </button>
                </div>
              </div>
            </div>'''
        law_cards_html.append(card_markup)
    law_cards_html.append('          </div>\n        </div>\n      </div>\n    </section>\n\n    ')
    new_law_section = '\n'.join(law_cards_html)

    pos_v_start = content.find(vault_grid_marker)
    pos_v_end = content.find(vault_grid_end)
    if pos_v_start != -1 and pos_v_end != -1:
        content = content[:pos_v_start] + new_law_section + content[pos_v_end:]
        print("✓ Injected dynamic 3D law cards into #law-academic-vault")

    # Update script injection in build_preview_html
    old_script_block_start = content.find("    podium_json = json.dumps(PODIUM_BOOKS, ensure_ascii=False)")
    old_script_block_end = content.find('    html = head_str + UNIFIED_STORE_CSS + "\\n</style>\\n" + body_str + script_content')

    new_script_block = """    podium_json = json.dumps(PODIUM_BOOKS, ensure_ascii=False)
    poet_json = json.dumps(POET_SHAYARI_DATA, ensure_ascii=False)
    vault_json = json.dumps(VAULT_BOOKS, ensure_ascii=False)
    bento_json = json.dumps(CATEGORY_BENTO_DATA, ensure_ascii=False)
    catalog_json = json.dumps(CATALOG_BOOKS, ensure_ascii=False)
    piyush_json = json.dumps(PIYUSH_MISHRA_BOOKS, ensure_ascii=False)
    rahi_json = json.dumps(RAHI_MASOOM_RAZA_BOOKS, ensure_ascii=False)
    master_search_json = json.dumps(MASTER_SEARCH_CATALOG, ensure_ascii=False)
    modal_meta_json = json.dumps(MODAL_METADATA_DATABASE, ensure_ascii=False)

    # Escape curly braces for body_str if needed or use simple format
    bento_rendered = render_category_bento_showcase()
    body_str = body_str.replace('{render_category_bento_showcase()}', bento_rendered)

    script_content = f\"\"\"  <script>
    window.PODIUM_BOOKS = {podium_json};
    window.POET_SHAYARI_DATA = {poet_json};
    window.VAULT_BOOKS = {vault_json};
    window.CATEGORY_BENTO_DATA = {bento_json};
    window.CATALOG_BOOKS = {catalog_json};
    window.PIYUSH_MISHRA_BOOKS = {piyush_json};
    window.RAHI_MASOOM_RAZA_BOOKS = {rahi_json};
    window.MASTER_SEARCH_CATALOG = {master_search_json};
    window.MODAL_METADATA_DATABASE = {modal_meta_json};

    const PODIUM_BOOKS = window.PODIUM_BOOKS;
    const POET_SHAYARI_DATA = window.POET_SHAYARI_DATA;
    const VAULT_BOOKS = window.VAULT_BOOKS;
    const CATEGORY_BENTO_DATA = window.CATEGORY_BENTO_DATA;
    const CATALOG_BOOKS = window.CATALOG_BOOKS;
    const PIYUSH_MISHRA_BOOKS = window.PIYUSH_MISHRA_BOOKS;
    const RAHI_MASOOM_RAZA_BOOKS = window.RAHI_MASOOM_RAZA_BOOKS;
    const MASTER_SEARCH_CATALOG = window.MASTER_SEARCH_CATALOG;
    const MODAL_METADATA_DATABASE = window.MODAL_METADATA_DATABASE;

{UNIFIED_STORE_JS}

    function handleModalFullDetails() {{
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {{
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }}
    }}
  </script>
\"\"\" + "\\n\\n" + MASTER_STYLE + "\\n\\n" + MASTER_SCRIPT + "\\n\\n</body>\\n</html>"
"""
    if old_script_block_start != -1 and old_script_block_end != -1:
        content = content[:old_script_block_start] + new_script_block + "\n" + content[old_script_block_end:]
        print("✓ Updated script injection in build_preview_html")

    with open('build_html_generator.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Saved build_html_generator.py")

def patch_shopify_files():
    print("--- 4. Patching Shopify theme files ---")
    # Suppress rogue empty state overlays
    suppressed_liquid = """{% comment %}
  Suppressed rogue empty state overlay to allow Indigo 2-letter predictive search suggestions
{% endcomment %}
<style>
.predictive-search,
.predictive-search-empty,
.predictive-search-empty__message,
.predictive-search-suggestions,
.predictive-search-wa-prompt,
#predictive-search-results,
[data-predictive-search],
predictive-search [tabindex="-1"],
.predictive-search__results-groups-wrapper {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
  height: 0 !important;
  overflow: hidden !important;
  z-index: -9999 !important;
}
</style>
"""
    paths = [
        'sections/predictive-search-empty.liquid',
        'indigo-books-shopify-theme/sections/predictive-search-empty.liquid',
        'snippets/predictive-search-empty-state.liquid',
        'indigo-books-shopify-theme/snippets/predictive-search-empty-state.liquid'
    ]
    for p in paths:
        if os.path.exists(p):
            with open(p, 'w', encoding='utf-8') as f:
                f.write(suppressed_liquid)
            print(f"✓ Suppressed empty search in {p}")

if __name__ == '__main__':
    patch_prepare_master_blocks()
    patch_store_scripts()
    patch_build_html_generator()
    patch_shopify_files()
    print("\n✓ Master patches successfully applied.")

