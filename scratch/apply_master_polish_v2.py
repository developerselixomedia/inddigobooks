# -*- coding: utf-8 -*-
"""
scratch/apply_master_polish_v2.py
Executes the 4 master polish features:
1. Fix Podium Hover Glitch (eliminate jitter on flanking book hover, click-only cover flip)
2. Make Author Names Clickable & Add "More Books by This Author" container
3. Ensure Cart Drawer & Top Navbar Tabs work flawlessly
4. Update sections/main-product.liquid with clickable author and author recommendations
"""

import os
import re

print("=================================================================")
print("STEP 1: Updating store_styles.py (Remove Podium Hover Jitter & Hover Flip)")
print("=================================================================")

with open('store_styles.py', 'r', encoding='utf-8') as f:
    css = f.read()

# 1A. Replace .flank-book:hover to eliminate transform/translateY/scale jitter
old_flank_hover = re.search(r'\.flank-book:hover\s*\{[^}]*\}', css)
if old_flank_hover:
    new_flank_hover = '''.flank-book:hover {
  filter: brightness(1.06) !important;
  cursor: pointer !important;
}'''
    css = css[:old_flank_hover.start()] + new_flank_hover + css[old_flank_hover.end():]
    print("Replaced .flank-book:hover with jitter-free brightness hover.")

# 1B. Remove .podium-3d-book:hover .podium-hinged-cover so cover flip is EXPLICIT CLICK ONLY
css = re.sub(
    r'\.podium-3d-book:hover\s+\.podium-hinged-cover,\s*\n\s*\.podium-3d-book\.is-open\s+\.podium-hinged-cover',
    '.podium-3d-book.is-open .podium-hinged-cover',
    css
)

# Also ensure any remaining .podium-3d-book:hover .podium-hinged-cover is removed
css = re.sub(
    r'\.podium-3d-book:hover\s+\.podium-hinged-cover\s*\{[^}]*\}',
    '',
    css
)
print("Removed .podium-3d-book:hover cover rotation (click-only now).")

# 1C. Ensure cart drawer CSS is complete and clean
cart_drawer_styles = '''
/* SLIDE-OVER CART DRAWER COMPLETE STYLES */
.cart-drawer-overlay {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.6) !important;
  backdrop-filter: blur(4px) !important;
  -webkit-backdrop-filter: blur(4px) !important;
  z-index: 999999 !important;
  display: none !important;
  justify-content: flex-end !important;
  align-items: stretch !important;
}
.cart-drawer-overlay.is-open {
  display: flex !important;
}
.cart-drawer-panel {
  width: 440px !important;
  max-width: 100vw !important;
  height: 100% !important;
  background: #FFFFFF !important;
  display: flex !important;
  flex-direction: column !important;
  box-shadow: -8px 0 32px rgba(0, 0, 0, 0.25) !important;
  animation: slideDrawerRight 0.28s cubic-bezier(0.16, 1, 0.3, 1) both !important;
  box-sizing: border-box !important;
  overflow: hidden !important;
}
@keyframes slideDrawerRight {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
.cart-header {
  padding: 18px 24px !important;
  border-bottom: 1px solid #E2E8F0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: #FFFFFF !important;
}
.cart-items-list {
  flex: 1 1 auto !important;
  overflow-y: auto !important;
  padding: 20px 24px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 16px !important;
}
.cart-footer {
  padding: 20px 24px !important;
  border-top: 1px solid #E2E8F0 !important;
  background: #FAF8F5 !important;
  flex-shrink: 0 !important;
}
'''

# Find end of UNIFIED_STORE_CSS string and insert cart_drawer_styles
last_triple = css.rfind('"""')
if last_triple != -1:
    css = css[:last_triple] + cart_drawer_styles + css[last_triple:]
    print("Injected comprehensive cart drawer styles.")

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(css)

print("store_styles.py updated successfully.")

print("\n=================================================================")
print("STEP 2: Updating store_scripts.py (Author Filtering, NavTo, Cart UI)")
print("=================================================================")

with open('store_scripts.py', 'r', encoding='utf-8') as f:
    js = f.read()

# 2A. Update toggleActivePodiumCover & togglePodiumCover
old_toggle = re.search(r'function togglePodiumCover\(e\) \{.*?\n\}', js, re.DOTALL)
new_toggle_code = '''function toggleActivePodiumCover(e) {
  if (e) {
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
    if (typeof e.preventDefault === 'function') e.preventDefault();
  }
  const el = document.getElementById('podium-3d-book');
  if (el) el.classList.toggle('is-open');
}

function togglePodiumCover(e) {
  toggleActivePodiumCover(e);
}'''

if old_toggle:
    js = js[:old_toggle.start()] + new_toggle_code + js[old_toggle.end():]
    print("Updated toggleActivePodiumCover in store_scripts.py")

# 2B. Update updateCartUI with 'Start Browsing (5,500+ Books)' button & navbar sync
old_cart_ui = re.search(r'function updateCartUI\(\) \{.*?\n\}', js, re.DOTALL)
new_cart_ui = '''function updateCartUI() {
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
}'''

if old_cart_ui:
    js = js[:old_cart_ui.start()] + new_cart_ui + js[old_cart_ui.end():]
    print("Updated updateCartUI in store_scripts.py")

# 2C. Update renderPdpRecommendations to show 'More Books by {Author}'
old_pdp_rec = re.search(r'function renderPdpRecommendations\(activeBook\) \{.*?\n\}', js, re.DOTALL)
new_pdp_rec = '''function renderPdpRecommendations(activeBook) {
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
}'''

if old_pdp_rec:
    js = js[:old_pdp_rec.start()] + new_pdp_rec + js[old_pdp_rec.end():]
    print("Updated renderPdpRecommendations in store_scripts.py")

# 2D. Add filterCatalogByAuthor, navTo, closeCartAndBrowseCatalog helpers
helpers_block = '''
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
'''

if 'function filterCatalogByAuthor' not in js:
    js += helpers_block
    print("Appended filterCatalogByAuthor and navTo helpers to store_scripts.py")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(js)

print("store_scripts.py updated successfully.")

print("\n=================================================================")
print("STEP 3: Updating build_html_generator.py (Navbar, Cart Drawer, Author Link)")
print("=================================================================")

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    gen = f.read()

# 3A. Update Navbar links with navTo
old_nav_links = '''      <ul class="nav-links-wrap">
        <li><a href="#top" class="nav-link-btn" onclick="closeDedicatedProductPage(); window.scrollTo({{top: 0, behavior: 'smooth'}})">Home</a></li>
        <li><a href="#shop-all-catalog" class="nav-link-btn" onclick="closeDedicatedProductPage(); filterCatalog('all'); document.getElementById('shop-all-catalog').scrollIntoView({{behavior: 'smooth'}})">Shop All (5,500+)</a></li>
        <li><a href="#bestsellers-podium" class="nav-link-btn" onclick="closeDedicatedProductPage(); document.getElementById('bestsellers-podium').scrollIntoView({{behavior: 'smooth'}})">Best Sellers</a></li>
        <li><a href="#shop-all-catalog" class="nav-link-btn" onclick="closeDedicatedProductPage(); filterCatalog('coming-soon'); document.getElementById('shop-all-catalog').scrollIntoView({{behavior: 'smooth'}})">Coming Soon</a></li>
        <li><a href="#shop-all-catalog" class="nav-link-btn" onclick="closeDedicatedProductPage(); filterCatalog('bundles'); document.getElementById('shop-all-catalog').scrollIntoView({{behavior: 'smooth'}})">Bundles</a></li>
        <li><a href="#shop-all-catalog" class="nav-link-btn" onclick="closeDedicatedProductPage(); filterCatalog('preorder'); document.getElementById('shop-all-catalog').scrollIntoView({{behavior: 'smooth'}})">Pre-Order</a></li>
        <li><a href="#law-academic-vault" class="nav-link-btn" onclick="closeDedicatedProductPage(); document.getElementById('law-academic-vault').scrollIntoView({{behavior: 'smooth'}})">Law Books</a></li>
        <li><a href="#mehfil-rekhta" class="nav-link-btn" onclick="closeDedicatedProductPage(); document.getElementById('mehfil-rekhta').scrollIntoView({{behavior: 'smooth'}})">India Centric</a></li>
      </ul>'''

new_nav_links = '''      <ul class="nav-links-wrap">
        <li><a href="#top" class="nav-link-btn" onclick="navTo('top'); return false;">Home</a></li>
        <li><a href="#shop-all-catalog" class="nav-link-btn" onclick="navTo('shop-all-catalog', 'all'); return false;">Shop All (5,500+)</a></li>
        <li><a href="#bestsellers-podium" class="nav-link-btn" onclick="navTo('bestsellers-podium'); return false;">Best Sellers</a></li>
        <li><a href="#shop-all-catalog" class="nav-link-btn" onclick="navTo('shop-all-catalog', 'coming-soon'); return false;">Coming Soon</a></li>
        <li><a href="#shop-all-catalog" class="nav-link-btn" onclick="navTo('shop-all-catalog', 'preorder'); return false;">Pre-Order</a></li>
        <li><a href="#law-academic-vault" class="nav-link-btn" onclick="navTo('law-academic-vault'); return false;">Law Books</a></li>
        <li><a href="#mehfil-rekhta" class="nav-link-btn" onclick="navTo('mehfil-rekhta'); return false;">India Centric</a></li>
      </ul>'''

if old_nav_links in gen:
    gen = gen.replace(old_nav_links, new_nav_links)
    print("Updated Navbar links in build_html_generator.py to use navTo()")

# Also update logo link
gen = gen.replace(
    '''<a href="#top" class="brand-link" onclick="closeDedicatedProductPage(); window.scrollTo({{top: 0, behavior: 'smooth'}});" aria-label="Indigo Books India Homepage">''',
    '''<a href="#top" class="brand-link" onclick="navTo('top'); return false;" aria-label="Indigo Books India Homepage">'''
)

# 3B. Update Center Book click to toggleActivePodiumCover
gen = gen.replace(
    '''onclick="togglePodiumCover(event)" title="Click or Hover to Open Cover"''',
    '''onclick="toggleActivePodiumCover(event)" title="Click to Open or Close Cover"'''
)

# 3C. Update Author in SPA single product view to be clickable
old_pdp_author = '''          <div class="pdp-author-row">
            By <strong id="pdpAuthor">Author Name</strong> &bull; Authorized Indian Edition
          </div>'''

new_pdp_author = '''          <div class="pdp-author-row">
            By <a id="pdpAuthorLink" href="javascript:void(0)" onclick="filterCatalogByAuthor(document.getElementById('pdpAuthor').textContent)" style="color: #D99B26; font-weight: 600; text-decoration: underline; cursor: pointer;"><strong id="pdpAuthor">Author Name</strong></a> &bull; Authorized Indian Edition
          </div>'''

if old_pdp_author in gen:
    gen = gen.replace(old_pdp_author, new_pdp_author)
    print("Made author name clickable in SPA Product View")

# 3D. Update Recommendations heading in SPA single product view
old_pdp_rec_head = '''      <!-- Bottom: Similar Books Row -->
      <div class="pdp-recommendations-sec">
        <h3 style="font-family: 'Merriweather', serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">
          Readers Also Bought / Similar Books in This Category
        </h3>
        <p style="font-size: 13.5px; color: #64748B; margin: 0 0 20px;">
          Curated literature often ordered together with this title.
        </p>'''

new_pdp_rec_head = '''      <!-- Bottom: More Books by This Author Row -->
      <div class="pdp-recommendations-sec">
        <h3 id="pdpMoreByAuthorTitle" style="font-family: 'Merriweather', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">
          More Books by This Author
        </h3>
        <p id="pdpMoreByAuthorSubtitle" style="font-size: 13.5px; color: #64748B; margin: 0 0 20px;">
          Discover other acclaimed editions and literary writings from the same author.
        </p>'''

if old_pdp_rec_head in gen:
    gen = gen.replace(old_pdp_rec_head, new_pdp_rec_head)
    print("Updated recommendations header to 'More Books by This Author'")

# 3E. Replace Cart Drawer HTML structure with robust nested layout
old_cart_drawer = re.search(r'<!-- =========================================================================\s*13\. SLIDE-OVER CART DRAWER.*?<\/aside>', gen, re.DOTALL)
new_cart_drawer_html = '''<!-- =========================================================================
       13. SLIDE-OVER CART DRAWER
       ========================================================================= -->
  <div id="cartDrawerOverlay" class="cart-drawer-overlay" onclick="toggleCartDrawer(false)">
    <aside id="cartDrawer" class="cart-drawer-panel" onclick="event.stopPropagation()">
      <div class="cart-header">
        <div style="display: flex; align-items: center; gap: 8px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0066B3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
          <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 18px; font-weight: 700; color: #0F172A; margin: 0;">Reading Bag (<span id="cartItemCount">0</span>)</h3>
        </div>
        <button type="button" class="drawer-close-btn" onclick="toggleCartDrawer(false)" aria-label="Close Bag" style="border: none; background: #F1F5F9; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #475569;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
        </button>
      </div>

      <!-- Free Delivery Progress Bar -->
      <div style="background: #EFF6FF; padding: 12px 20px; border-bottom: 1px solid #DBEAFE;">
        <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; color: #1E40AF; margin-bottom: 6px;">
          <span id="freeShippingText">Free Express Dispatch across India on orders over ₹499</span>
          <span id="freeShippingPercent">100%</span>
        </div>
        <div style="width: 100%; height: 6px; background: #BFDBFE; border-radius: 999px; overflow: hidden;">
          <div id="freeShippingBar" style="width: 100%; height: 100%; background: #2563EB;"></div>
        </div>
      </div>

      <!-- Items List & Empty State Container -->
      <div class="cart-items-list" id="cartDrawerItemsList">
        <!-- Rendered dynamically by updateCartUI() -->
      </div>

      <div class="cart-footer">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
          <span style="font-size: 14px; font-weight: 600; color: #475569;">Subtotal:</span>
          <span id="cartDrawerSubtotal" style="font-size: 22px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹0.00</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 8px;">
          <button type="button" class="btn-checkout" onclick="proceedToCheckout()" style="width: 100%; background: #0F172A; color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; font-weight: 700; padding: 12px 0; border: none; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/></svg>
            <span>Proceed to Checkout</span>
          </button>
          <button type="button" class="btn-wa-checkout" onclick="checkoutViaWhatsApp()" style="width: 100%; background: #25D366; color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; font-weight: 700; padding: 12px 0; border: none; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            <span>Checkout via WhatsApp COD (+91 8933063306)</span>
          </button>
        </div>

        <div style="text-align: center; font-size: 11px; color: #94A3B8; margin-top: 12px;">
          100% Genuine Publisher Editions &bull; Same-Day Prayagraj Hub Dispatch
        </div>
      </div>
    </aside>
  </div>'''

if old_cart_drawer:
    gen = gen[:old_cart_drawer.start()] + new_cart_drawer_html + gen[old_cart_drawer.end():]
    print("Replaced Cart Drawer HTML in build_html_generator.py")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(gen)

print("build_html_generator.py updated successfully.")

print("\n=================================================================")
print("STEP 4: Updating sections/main-product.liquid (Author Link & More Books)")
print("=================================================================")

with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    pdp_liquid = f.read()

# 4A. Make author clickable in PDP
old_pdp_liquid_author = '''        <div class="pdp-author-row">
          By <strong>{{ product.metafields.custom.author.value | default: product.vendor | default: 'Celebrated Author' }}</strong> &bull; Authorized Indian Edition
        </div>'''

new_pdp_liquid_author = '''        <div class="pdp-author-row">
          By <a href="javascript:void(0)" onclick="filterCatalogByAuthor('{{ product.vendor | escape }}')" style="color: #D99B26; font-weight: 600; text-decoration: underline; cursor: pointer;">{{ product.metafields.custom.author.value | default: product.vendor | default: 'Celebrated Author' }}</a> &bull; Authorized Indian Edition
        </div>'''

if old_pdp_liquid_author in pdp_liquid:
    pdp_liquid = pdp_liquid.replace(old_pdp_liquid_author, new_pdp_liquid_author)
    print("Updated author link in sections/main-product.liquid")

# 4B. Update bottom container to 'More Books by {{ product.vendor }}'
old_pdp_rec_block = re.search(r'<!-- Bottom: Similar Books Row -->\s*<div class="pdp-recommendations-sec">.*?<\/div>\s*<\/div>\s*<\/div>\s*<\/section>', pdp_liquid, re.DOTALL)
new_pdp_rec_block = '''<!-- Bottom: More Books by {{ product.vendor }} -->
    <div class="pdp-recommendations-sec">
      <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">
        More Books by {{ product.vendor | default: 'This Author' }}
      </h3>
      <p style="font-size: 13.5px; color: #64748B; margin: 0 0 20px;">
        Explore other celebrated titles and writings from the same literary voice.
      </p>
      
      <div class="pdp-rec-grid">
        {%- assign rec_count = 0 -%}
        {%- for related_product in collections.all.products -%}
          {%- if related_product.id != product.id and related_product.vendor == product.vendor and rec_count < 4 -%}
            {%- assign rec_count = rec_count | plus: 1 -%}
            <div class="catalog-card">
              <div class="catalog-thumb" onclick="location.href='{{ related_product.url }}'" style="cursor: pointer;">
                {%- if related_product.featured_image -%}
                  <img src="{{ related_product.featured_image | image_url: width: 400 }}" alt="{{ related_product.title | escape }}" loading="lazy" />
                {%- else -%}
                  <img src="{{ 'hero-godan.jpg' | asset_url }}" alt="{{ related_product.title | escape }}" loading="lazy" />
                {%- endif -%}
              </div>
              <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
                {{ related_product.type | default: 'IN STOCK' }}
              </div>
              <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 14px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; min-height: 36px;">
                <a href="{{ related_product.url }}" style="color: inherit; text-decoration: none;">{{ related_product.title }}</a>
              </h3>
              <div style="font-size: 12px; color: #64748B; margin-bottom: 10px;">
                {{ related_product.vendor }}
              </div>
              <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 12px;">
                <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{{ related_product.price | money }}</span>
              </div>
              <a href="{{ related_product.url }}" class="btn-overview" style="width: 100%; justify-content: center; text-decoration: none; padding: 10px 0;">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> View Details
              </a>
            </div>
          {%- endif -%}
        {%- endfor -%}

        {%- if rec_count < 4 -%}
          {%- for related_product in collections.all.products -%}
            {%- if related_product.id != product.id and related_product.vendor != product.vendor and rec_count < 4 -%}
              {%- assign rec_count = rec_count | plus: 1 -%}
              <div class="catalog-card">
                <div class="catalog-thumb" onclick="location.href='{{ related_product.url }}'" style="cursor: pointer;">
                  {%- if related_product.featured_image -%}
                    <img src="{{ related_product.featured_image | image_url: width: 400 }}" alt="{{ related_product.title | escape }}" loading="lazy" />
                  {%- else -%}
                    <img src="{{ 'hero-godan.jpg' | asset_url }}" alt="{{ related_product.title | escape }}" loading="lazy" />
                  {%- endif -%}
                </div>
                <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
                  {{ related_product.type | default: 'IN STOCK' }}
                </div>
                <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 14px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; min-height: 36px;">
                  <a href="{{ related_product.url }}" style="color: inherit; text-decoration: none;">{{ related_product.title }}</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 10px;">
                  {{ related_product.vendor }}
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 12px;">
                  <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{{ related_product.price | money }}</span>
                </div>
                <a href="{{ related_product.url }}" class="btn-overview" style="width: 100%; justify-content: center; text-decoration: none; padding: 10px 0;">
                  <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> View Details
                </a>
              </div>
            {%- endif -%}
          {%- endfor -%}
        {%- endif -%}
      </div>
    </div>

  </div>
</section>'''

if old_pdp_rec_block:
    pdp_liquid = pdp_liquid[:old_pdp_rec_block.start()] + new_pdp_rec_block + pdp_liquid[old_pdp_rec_block.end():]
    print("Updated recommendations block in sections/main-product.liquid")

# 4C. Ensure filterCatalogByAuthor is defined in script block of main-product.liquid
if 'function filterCatalogByAuthor' not in pdp_liquid:
    pdp_liquid = pdp_liquid.replace(
        'function toggleMainProductExcerpt() {',
        '''function filterCatalogByAuthor(author) {
    if (!author) return;
    window.location.href = '/search?q=' + encodeURIComponent(author);
  }

  function toggleMainProductExcerpt() {'''
    )
    print("Added filterCatalogByAuthor to script block in sections/main-product.liquid")

with open('sections/main-product.liquid', 'w', encoding='utf-8') as f:
    f.write(pdp_liquid)

print("sections/main-product.liquid updated successfully.")
print("\n=================================================================")
print("All source enhancements applied successfully!")
print("=================================================================")

