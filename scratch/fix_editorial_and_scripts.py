import os

# =========================================================================
# 1. FIX STORE_SCRIPTS.PY
# =========================================================================
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    scripts_content = f.read()

# Fix 1: Cart initialization & persistence in localStorage
old_cart_init = "let cart = [];"
new_cart_init = """let cart = [];
try {
  const savedCart = localStorage.getItem('indigo_cart');
  if (savedCart) {
    const parsed = JSON.parse(savedCart);
    if (Array.isArray(parsed)) cart = parsed;
  }
} catch (e) {
  cart = [];
}

function saveCartToStorage() {
  try {
    localStorage.setItem('indigo_cart', JSON.stringify(cart));
  } catch (e) {}
}"""

if old_cart_init in scripts_content:
    scripts_content = scripts_content.replace(old_cart_init, new_cart_init, 1)
    print("Updated cart initialization with localStorage persistence")

# Fix 2: saveCartToStorage after modifying cart
old_add_cart = """  updateCartUI();
  toggleCartDrawer(true);
}"""
new_add_cart = """  saveCartToStorage();
  updateCartUI();
  toggleCartDrawer(true);
}"""
scripts_content = scripts_content.replace(old_add_cart, new_add_cart)

old_qty_cart = """  item.qty += delta;
  if (item.qty <= 0) {
    cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  }
  updateCartUI();"""
new_qty_cart = """  item.qty += delta;
  if (item.qty <= 0) {
    cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  }
  saveCartToStorage();
  updateCartUI();"""
scripts_content = scripts_content.replace(old_qty_cart, new_qty_cart)

old_remove_cart = """function removeFromCart(bookId) {
  const idStr = String(bookId);
  cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  updateCartUI();
}"""
new_remove_cart = """function removeFromCart(bookId) {
  const idStr = String(bookId);
  cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  saveCartToStorage();
  updateCartUI();
}"""
scripts_content = scripts_content.replace(old_remove_cart, new_remove_cart)

# Fix 3: In openExpressPhoneCheckout, ensure modal is z-index 30000000 and bind 10-digit/6-digit auto cleaners
old_open_express = """  modal.classList.add('is-active');
  modal.style.setProperty('display', 'flex', 'important');
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
  if (typeof lucide !== 'undefined') lucide.createIcons();
}"""

new_open_express = """  modal.classList.add('is-active');
  modal.style.setProperty('display', 'flex', 'important');
  modal.style.display = 'flex';
  modal.style.setProperty('z-index', '30000000', 'important');
  modal.style.zIndex = '30000000';
  document.body.style.overflow = 'hidden';

  // Double-defense input auto-cleaning & pattern conformance
  const pInput = document.getElementById('checkoutPhone');
  if (pInput && !pInput.dataset.cleanerBound) {
    pInput.dataset.cleanerBound = 'true';
    pInput.setAttribute('pattern', '[0-9]{10}');
    pInput.setAttribute('maxlength', '10');
    pInput.setAttribute('minlength', '10');
    pInput.addEventListener('input', function() {
      this.value = this.value.replace(/\\D/g, '').slice(0, 10);
    });
  }
  const pinInput = document.getElementById('checkoutPincode');
  if (pinInput && !pinInput.dataset.cleanerBound) {
    pinInput.dataset.cleanerBound = 'true';
    pinInput.setAttribute('pattern', '[0-9]{6}');
    pinInput.setAttribute('maxlength', '6');
    pinInput.setAttribute('minlength', '6');
    pinInput.addEventListener('input', function() {
      this.value = this.value.replace(/\\D/g, '').slice(0, 6);
    });
  }

  if (typeof lucide !== 'undefined') lucide.createIcons();
}"""
scripts_content = scripts_content.replace(old_open_express, new_open_express)

# Fix 4: In submitExpressPhoneOrder, clean phone value before checking
old_submit_phone = """  const phone = document.getElementById('checkoutPhone').value.trim();"""
new_submit_phone = """  const rawPhone = document.getElementById('checkoutPhone').value.trim();
  const phone = rawPhone.replace(/\\D/g, '').slice(-10);
  if (phone.length !== 10) {
    alert('Please enter a valid 10-digit mobile number.');
    return;
  }"""
scripts_content = scripts_content.replace(old_submit_phone, new_submit_phone)

# Fix 5: In openSearchResultsPage, do NOT delegate back to performDedicatedSearch
old_search_delegate = """function openSearchResultsPage(query) {
  if (!query) return;
  if (typeof window.performDedicatedSearch === 'function') {
    window.performDedicatedSearch(query);
    return;
  }"""
new_search_delegate = """function openSearchResultsPage(query) {
  if (!query) return;"""
scripts_content = scripts_content.replace(old_search_delegate, new_search_delegate)

# Fix 6: Add pageshow event listener to rehydrate cart on back button
if "window.addEventListener('pageshow'" not in scripts_content:
    pageshow_code = """
window.addEventListener('pageshow', function(event) {
  try {
    const savedCart = localStorage.getItem('indigo_cart');
    if (savedCart) {
      const parsed = JSON.parse(savedCart);
      if (Array.isArray(parsed)) cart = parsed;
    }
  } catch (e) {}
  if (typeof updateCartUI === 'function') updateCartUI();
});
"""
    scripts_content += pageshow_code
    print("Added pageshow event listener to store_scripts.py")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(scripts_content)
print("Updated store_scripts.py successfully!")


# =========================================================================
# 2. FIX EDITORIAL_VIDEO_THEME.PY
# =========================================================================
with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    editorial_content = f.read()

# Fix 1: performDedicatedSearch & filterByAuthorDirect opening #indigo-search-results-view
old_perform_dedicated = """  /* GLOBAL AUTHOR FILTER & DEDICATED SEARCH ENGINE */
  window.performDedicatedSearch = function(query) {
    if (!query) return;
    var q = query.trim();

    // Standalone Shopify non-home page without SPA
    var isShopifyNonHome = (typeof window !== 'undefined' && 
      (window.location.pathname.indexOf('/products/') !== -1 || window.location.pathname.indexOf('/cart') !== -1 || window.location.pathname.indexOf('/collections') !== -1) &&
      !document.getElementById('homepage-view')
    );
    if (isShopifyNonHome) {
      window.location.href = '/search?q=' + encodeURIComponent(q);
      return;
    }

    // Close solo book page if open & unlock body
    var soloV = document.getElementById('indigo-solo-product-view');
    if (soloV) {
      soloV.classList.remove('is-active');
      soloV.style.display = 'none';
    }
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';

    // Hide legacy search view if present
    var sView = document.getElementById('indigo-search-results-view');
    if (sView) sView.style.display = 'none';

    // Show homepage view
    var homeV = document.getElementById('homepage-view');
    if (homeV) homeV.style.display = 'block';

    // Apply search query to Modern Archive Section
    archiveCurrentGenre = 'all';
    archiveSearchQuery = q.toLowerCase();
    archivePage = 1;

    // Reset category chips
    var chips = document.querySelectorAll('#v2ArchiveFilterChips .v2-chip');
    chips.forEach(function(c, idx) {
      if (idx === 0) c.classList.add('active');
      else c.classList.remove('active');
    });

    var arcSearchInput = document.getElementById('v2ArchiveSearchInput');
    if (arcSearchInput) arcSearchInput.value = q;

    renderArchiveGrid(false);

    var arcEl = document.getElementById('all-books-archive-section') || document.getElementById('v2-archive-section');
    if (arcEl) {
      arcEl.scrollIntoView({ behavior: 'smooth' });
    }
  };

  window.filterByAuthorDirect = function(authorName) {
    if (!authorName) return;
    
    // Close solo book page if open
    var soloView = document.getElementById('indigo-solo-product-view');
    if (soloView) {
      soloView.classList.remove('is-active');
      soloView.style.display = 'none';
    }
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';

    var homeV = document.getElementById('homepage-view');
    if (homeV) homeV.style.display = 'block';

    var sView = document.getElementById('indigo-search-results-view');
    if (sView) sView.style.display = 'none';

    // CRITICAL: Always reset genre to 'all' so no category restrictions hide the author's books!
    archiveCurrentGenre = 'all';
    archiveSearchQuery = authorName.trim().toLowerCase();
    archivePage = 1;

    // Reset category chips
    var chips = document.querySelectorAll('#v2ArchiveFilterChips .v2-chip');
    chips.forEach(function(c, idx) {
      if (idx === 0) c.classList.add('active');
      else c.classList.remove('active');
    });

    var arcSearchInput = document.getElementById('v2ArchiveSearchInput');
    if (arcSearchInput) arcSearchInput.value = authorName;

    renderArchiveGrid(false);

    var arcEl = document.getElementById('all-books-archive-section') || document.getElementById('v2-archive-section');
    if (arcEl) {
      arcEl.scrollIntoView({ behavior: 'smooth' });
    }
  };

  window.filterByAuthorFromSolo = function(authorName) {
    window.filterByAuthorDirect(authorName);
  };"""

new_perform_dedicated = """  /* GLOBAL AUTHOR FILTER & DEDICATED SEARCH ENGINE */
  window.performDedicatedSearch = function(query) {
    if (!query) return;
    var q = query.trim();

    // Standalone Shopify non-home page without SPA
    var isShopifyNonHome = (typeof window !== 'undefined' && 
      (window.location.pathname.indexOf('/products/') !== -1 || window.location.pathname.indexOf('/cart') !== -1 || window.location.pathname.indexOf('/collections') !== -1) &&
      !document.getElementById('indigo-search-results-view')
    );
    if (isShopifyNonHome) {
      window.location.href = '/search?q=' + encodeURIComponent(q);
      return;
    }

    // Close solo book page if open & unlock body
    if (typeof window.closeSoloBookPage === 'function') {
      window.closeSoloBookPage();
    } else {
      var soloV = document.getElementById('indigo-solo-product-view');
      if (soloV) {
        soloV.classList.remove('is-active');
        soloV.style.display = 'none';
      }
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
    }

    // Close any search dropdowns
    var resultsBox = document.getElementById('editorialSearchResults');
    if (resultsBox) resultsBox.style.display = 'none';

    // Open dedicated search results view (#indigo-search-results-view)
    if (typeof window.openSearchResultsPage === 'function') {
      window.openSearchResultsPage(q);
    } else {
      window.location.href = '/search?q=' + encodeURIComponent(q);
    }
  };

  window.filterByAuthorDirect = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };

  window.filterByAuthorFromSolo = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };"""

if old_perform_dedicated in editorial_content:
    editorial_content = editorial_content.replace(old_perform_dedicated, new_perform_dedicated)
    print("Updated performDedicatedSearch & filterByAuthorDirect to open #indigo-search-results-view")
else:
    print("Warning: old_perform_dedicated block not found exactly in editorial_video_theme.py")

# Fix 2: Search input keydown on Enter: always open dedicated search results page!
old_search_enter = """    searchInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        var q = (searchInput.value || '').trim();
        if (q) {
          // If search results dropdown has a highlighted or top match, open it directly!
          var firstItem = resultsBox.querySelector('.editorial-search-item');
          if (firstItem && resultsBox.style.display === 'block') {
            var bid = firstItem.getAttribute('data-id');
            var bHandle = firstItem.getAttribute('data-handle');
            resultsBox.style.display = 'none';
            searchInput.value = '';
            if (typeof window.openSoloBookPage === 'function') {
              window.openSoloBookPage(bid || bHandle);
              return;
            } else if (bHandle) {
              window.location.href = '/products/' + bHandle;
              return;
            }
          }

          resultsBox.style.display = 'none';
          if (typeof window.performDedicatedSearch === 'function') {
            window.performDedicatedSearch(q);
          } else {
            window.location.href = '/search?q=' + encodeURIComponent(q);
          }
        }
      }
    });"""

new_search_enter = """    searchInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        var q = (searchInput.value || '').trim();
        if (q) {
          resultsBox.style.display = 'none';
          if (typeof window.performDedicatedSearch === 'function') {
            window.performDedicatedSearch(q);
          } else if (typeof window.openSearchResultsPage === 'function') {
            window.openSearchResultsPage(q);
          } else {
            window.location.href = '/search?q=' + encodeURIComponent(q);
          }
        }
      }
    });"""

if old_search_enter in editorial_content:
    editorial_content = editorial_content.replace(old_search_enter, new_search_enter)
    print("Updated searchInput Enter handler to always open dedicated search results page")
else:
    print("Warning: old_search_enter block not found exactly in editorial_video_theme.py")

# Fix 3: Add "View All Results for [query]" footer in renderMatches
old_render_end = """      resultsBox.innerHTML = html;
      resultsBox.style.display = 'block';"""

new_render_end = """      html += '<div class="editorial-search-view-all" onclick="window.performDedicatedSearch(document.getElementById(\\'editorialSearchInput\\').value)" style="padding:11px 16px;text-align:center;font-size:12.5px;font-weight:700;color:#E04F33;cursor:pointer;background:#FFF9F7;border-top:1px solid #FFE4DD;letter-spacing:0.02em;">View All Results for &ldquo;' + (searchInput.value || '').trim() + '&rdquo; &rarr;</div>';
      resultsBox.innerHTML = html;
      resultsBox.style.display = 'block';"""

if old_render_end in editorial_content:
    editorial_content = editorial_content.replace(old_render_end, new_render_end, 1)
    print("Added View All Results footer to editorial search dropdown")

# Fix 4: closeSoloBookPage calls updateCartUI
old_close_solo = """  window.closeSoloBookPage = function() {
    var v = document.getElementById('indigo-solo-product-view');
    if (v) {
      v.classList.remove('is-active');
      v.style.display = 'none';
    }
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';"""

new_close_solo = """  window.closeSoloBookPage = function() {
    var v = document.getElementById('indigo-solo-product-view');
    if (v) {
      v.classList.remove('is-active');
      v.style.display = 'none';
    }
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';
    if (typeof window.updateCartUI === 'function') {
      window.updateCartUI();
    }"""

if old_close_solo in editorial_content:
    editorial_content = editorial_content.replace(old_close_solo, new_close_solo)
    print("Updated closeSoloBookPage to refresh cart UI")

# Fix 5: Pass currentActiveBook object in handleSoloBuyNow
old_solo_buy = """  window.handleSoloBuyNow = function() {
    if (!currentActiveBook) return;
    if (typeof window.openExpressPhoneCheckout === 'function') {
      window.openExpressPhoneCheckout(currentActiveBook.id);
    } else if (typeof window.openQuickOrderModal === 'function') {
      window.openQuickOrderModal(currentActiveBook.id);
    }
  };"""

new_solo_buy = """  window.handleSoloBuyNow = function() {
    if (!currentActiveBook) return;
    if (typeof window.openExpressPhoneCheckout === 'function') {
      window.openExpressPhoneCheckout(currentActiveBook);
    } else if (typeof window.openQuickOrderModal === 'function') {
      window.openQuickOrderModal(currentActiveBook);
    }
  };"""

if old_solo_buy in editorial_content:
    editorial_content = editorial_content.replace(old_solo_buy, new_solo_buy)
    print("Updated handleSoloBuyNow to pass currentActiveBook")

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(editorial_content)
print("Updated editorial_video_theme.py successfully!")
