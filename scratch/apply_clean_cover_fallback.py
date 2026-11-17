with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    ev_text = f.read()

# 1. Update handleBookCoverError in editorial_video_theme.py
old_handle = """function handleBookCoverError(img, title, author) {
    if (!img) return;
    img.onerror = null;
    var bookTitle = title || img.alt || 'Indigo Books Edition';
    var bookAuthor = author || 'Indigo Archive';
    if (typeof window.getFallbackCoverSvg === 'function') {
      img.src = window.getFallbackCoverSvg(bookTitle, bookAuthor);
    } else if (typeof getFallbackCover === 'function') {
      img.src = getFallbackCover(bookTitle, bookAuthor);
    }
  }
  window.handleBookCoverError = handleBookCoverError;"""

new_handle = """function handleBookCoverError(img, title, author) {
    if (!img) return;
    img.onerror = null;
    var bookTitle = title || img.getAttribute('data-title') || img.alt || 'Indigo Books Edition';
    var bookAuthor = author || img.getAttribute('data-author') || 'Indigo Archive';
    if (typeof window.getFallbackCoverSvg === 'function') {
      img.src = window.getFallbackCoverSvg(bookTitle, bookAuthor);
    } else if (typeof getFallbackCover === 'function') {
      img.src = getFallbackCover(bookTitle, bookAuthor);
    }
  }
  window.handleBookCoverError = handleBookCoverError;"""

assert old_handle in ev_text, "old_handle not found"
ev_text = ev_text.replace(old_handle, new_handle, 1)

# 2. Update renderArchiveGrid in editorial_video_theme.py
idx_arch = ev_text.find("card.className = 'v2-archive-card';")
assert idx_arch != -1, "idx_arch not found"
idx_end = ev_text.find("card.appendChild(document.createElement('div'));", idx_arch)
if idx_end == -1:
    idx_end = ev_text.find("grid.appendChild(card);", idx_arch)

# Let's inspect the card.innerHTML assignment in renderArchiveGrid
idx_cin = ev_text.find("card.innerHTML =", idx_arch)
idx_cin_end = ev_text.find("card.onclick = function()", idx_cin)

new_arch_inner = """card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #FAF7F0;">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" data-author="' + safeAuthor + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="window.handleBookCoverError && window.handleBookCoverError(this);" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +
        '<div>' +
          '<div class="v2-archive-card-price">' + priceStr + '</div>' +
          '<div style="display:flex;gap:6px;">' +
            '<button type="button" class="v2-btn-archive-preview" style="flex:1;">Preview &rarr;</button>' +
            '<button type="button" class="v2-btn-archive-add" onclick="event.stopPropagation(); window.addToBagDirect ? window.addToBagDirect(\\'' + bId + '\\') : null;" style="flex:1;">+ Add</button>' +
          '</div>' +
        '</div>';

      """

ev_text = ev_text[:idx_cin] + new_arch_inner + ev_text[idx_cin_end:]
print("Updated renderArchiveGrid in editorial_video_theme.py")

# 3. Update renderShelfRow in editorial_video_theme.py
idx_shelf = ev_text.find("function renderShelfRow")
idx_scin = ev_text.find("card.innerHTML =", idx_shelf)
idx_scin_end = ev_text.find("var cImg = card.querySelector", idx_scin)

new_shelf_inner = """card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf" style="position:relative; background-color:#FAF7F0;">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" data-author="' + b.author + '" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="window.handleBookCoverError && window.handleBookCoverError(this);" />' +
          '</div>' +
        '</div>' +
        '<div class="v2-card-details-sheet">' +
          '<div>' +
            '<div class="v2-card-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>' +
            '<h3 class="v2-card-title">' + b.title + '</h3>' +
            '<div class="v2-card-author">By ' + b.author + '</div>' +
          '</div>' +
          '<div>' +
            '<div class="v2-card-price">' + b.price + '</div>' +
            '<div class="v2-card-btn-row">' +
              '<button type="button" class="v2-card-preview-btn">Preview &rarr;</button>' +
              '<button type="button" class="v2-card-quick-btn">1-Click Buy</button>' +
            '</div>' +
          '</div>' +
        '</div>';

      """

ev_text = ev_text[:idx_scin] + new_shelf_inner + ev_text[idx_scin_end:]
print("Updated renderShelfRow in editorial_video_theme.py")

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(ev_text)

# 4. Update store_scripts.py
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    sc_text = f.read()

# Update handleBookCoverError in store_scripts.py
old_sc_handle = """window.handleBookCoverError = function(img, title, author) {
  if (!img) return;
  img.onerror = null;
  const t = title || img.alt || 'Indigo Books Edition';
  const a = author || 'Indigo Archive';
  if (typeof getFallbackCover === 'function') {
    img.src = getFallbackCover(t, a);
  } else if (typeof window.getFallbackCoverSvg === 'function') {
    img.src = window.getFallbackCoverSvg(t, a);
  }
};"""

new_sc_handle = """window.handleBookCoverError = function(img, title, author) {
  if (!img) return;
  img.onerror = null;
  const t = title || img.getAttribute('data-title') || img.alt || 'Indigo Books Edition';
  const a = author || img.getAttribute('data-author') || 'Indigo Archive';
  if (typeof getFallbackCover === 'function') {
    img.src = getFallbackCover(t, a);
  } else if (typeof window.getFallbackCoverSvg === 'function') {
    img.src = window.getFallbackCoverSvg(t, a);
  }
};"""

if old_sc_handle in sc_text:
    sc_text = sc_text.replace(old_sc_handle, new_sc_handle, 1)

# Ensure search card in renderCurrentSearchResults uses this clean onerror
old_sc_card_search = """onerror="window.handleBookCoverError && window.handleBookCoverError(this, '${escapeJs(titleSafe)}', '${escapeJs(authorSafe)}');" />"""
new_sc_card_search = """data-author="${escapeHtml(authorSafe)}" onerror="window.handleBookCoverError && window.handleBookCoverError(this);" />"""

if old_sc_card_search in sc_text:
    sc_text = sc_text.replace(old_sc_card_search, new_sc_card_search, 1)
    print("Updated search card in store_scripts.py")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(sc_text)

print("Saved all updates cleanly!")
