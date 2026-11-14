# -*- coding: utf-8 -*-
import sys

with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update getAssetUrl
old_gau = '''  // If it's a bare filename or relative path from the Rajkamal / Indian publisher inventory (5,500+ books)
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
  }'''

new_gau = '''  // If it's a bare filename or relative path from the Rajkamal / Indian publisher inventory (5,500+ books)
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
  }'''

if old_gau in text:
    text = text.replace(old_gau, new_gau)
    print("1. Updated getAssetUrl!")
else:
    print("1. old_gau not found (might already be updated)")

# 2. Update renderSearchSuggestions
old_rss = '''  matches.sort(function(a, b) { return b.score - a.score; });
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
  dropdown.style.display = 'block';'''

new_rss = '''  matches.sort(function(a, b) { return b.score - a.score; });

  // Deduplicate identical title + format (Paperback vs Hardcover separation)
  const seenKeys = new Set();
  const uniqueMatches = [];
  for (let i = 0; i < matches.length; i++) {
    const b = matches[i].book;
    const bFmt = (b.format || b.binding || (b.type && b.type.toLowerCase().includes('hard') ? 'Hardcover' : 'Paperback') || 'Paperback').toLowerCase();
    const key = (b.title || '').toLowerCase().trim() + '|' + bFmt;
    if (!seenKeys.has(key)) {
      seenKeys.add(key);
      uniqueMatches.push(matches[i]);
    }
  }

  const topMatches = uniqueMatches.slice(0, 6);

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
    const binding = book.format || book.binding || (book.type && book.type.toLowerCase().includes('hard') ? 'Hardcover' : 'Paperback') || 'Paperback';
    const bClass = binding.toLowerCase().includes('hard') ? 'hardcover' : 'paperback';

    return `
      <div class="search-suggestion-item" onclick="selectSearchSuggestion('${escapeJs(book.id)}', '${escapeJs(bookUrl)}')">
        <img class="suggestion-thumb" src="${cover}" alt="${titleSafe}" onerror="this.onerror=null; this.src=getFallbackCover('${escapeJs(titleSafe)}', '${escapeJs(authorSafe)}');" />
        <div class="suggestion-details">
          <div class="suggestion-title">${highlightSearchMatch(book.title || '', query)} <span class="badge-binding ${bClass}">${escapeHtml(binding)}</span></div>
          <div class="suggestion-author">${highlightSearchMatch(book.author || book.vendor || 'Indigo Books', query)}</div>
        </div>
        <div class="suggestion-price">${priceFormatted}</div>
      </div>
    `;
  }).join('');

  dropdown.innerHTML = `
    <div class="search-suggestions-header">Quick Results (${uniqueMatches.length} matches)</div>
    ${itemsHtml}
    <div class="search-suggestions-footer" onclick="openSearchResultsPage('${escapeJs(query)}')">
      View all ${uniqueMatches.length} matching titles &rarr;
    </div>
  `;
  dropdown.style.display = 'block';'''

if old_rss in text:
    text = text.replace(old_rss, new_rss)
    print("2. Updated renderSearchSuggestions!")
else:
    print("2. old_rss not found")

# 3. Update toggleCartDrawer
old_tcd = '''function toggleCartDrawer(forceOpen) {
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
}'''

new_tcd = '''function toggleCartDrawer(forceOpen) {
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
}'''

if old_tcd in text:
    text = text.replace(old_tcd, new_tcd)
    print("3. Updated toggleCartDrawer!")
else:
    print("3. old_tcd not found")

# 4. Update addToCart
old_atc = '''function addToCart(bookId) {
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
}'''

new_atc = '''function addToCart(bookId, bookTitle, bookPrice, bookCover, event) {
  const e = event || (typeof window !== 'undefined' && window.event);
  const btn = e && (e.currentTarget || e.target);
  if (btn && btn.classList) {
    btn.classList.add('btn-add-pop');
    setTimeout(function() { btn.classList.remove('btn-add-pop'); }, 400);
  }

  let meta = findBookMetadata(bookId);
  if (!meta) {
    meta = {
      id: bookId,
      title: bookTitle || 'Selected Book',
      author: 'Indigo Books India',
      price: bookPrice || '299.00',
      cover: bookCover || 'assets/hero-godan.jpg'
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
      price: parseFloat(meta.price) || (parseFloat(String(meta.price).replace(/[^0-9.]/g, '')) || 299.00),
      cover: getAssetUrl(meta.cover || meta.coverUrl || bookCover),
      qty: 1
    });
  }

  updateCartUI();
  toggleCartDrawer(true);
}'''

if old_atc in text:
    text = text.replace(old_atc, new_atc)
    print("4. Updated addToCart!")
else:
    print("4. old_atc not found")

# 5. Add searchByAuthor and browseAllBooks helpers
helper_funcs = '''
// Global Author Search & Catalog Browse Helpers
function searchByAuthor(authorName) {
  if (!authorName) return;
  const clean = authorName.replace(/^by\\s+/i, '').replace(/author\\s*:\\s*/i, '').trim();
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
'''

if 'function searchByAuthor' not in text:
    target_pos = 'function closeDedicatedProductPage() {'
    if target_pos in text:
        text = text.replace(target_pos, helper_funcs + '\n' + target_pos)
        print("5. Added searchByAuthor and browseAllBooks!")
    else:
        print("5. target_pos for helper_funcs not found")

# 6. Expose window functions
window_exports = '''  window.searchByAuthor = searchByAuthor;
  window.browseAllBooks = browseAllBooks;
  window.toggleCartDrawer = toggleCartDrawer;
  window.addToCart = addToCart;'''

if 'window.searchByAuthor = searchByAuthor;' not in text:
    target_exp = 'window.openSearchResultsPage = openSearchResultsPage;'
    if target_exp in text:
        text = text.replace(target_exp, target_exp + '\n' + window_exports)
        print("6. Exposed window functions!")
    else:
        print("6. target_exp not found")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully written updated store_scripts.py!")

