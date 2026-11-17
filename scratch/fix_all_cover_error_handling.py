import os

print("=== FIXING COVER ERROR HANDLING ACROSS ALL VIEWS ===")

# 1. Update store_scripts.py
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    sc_text = f.read()

# Make sure handleBookCoverError is defined globally in store_scripts.py
old_handle_fn = """// --- UNIVERSAL ASSET URL RESOLVER ---
function getAssetUrl(url, bookId, defaultTitle, defaultAuthor) {"""

new_handle_fn = """window.handleBookCoverError = function(img, title, author) {
  if (!img) return;
  img.onerror = null;
  const t = title || img.alt || 'Indigo Books Edition';
  const a = author || 'Indigo Archive';
  if (typeof getFallbackCover === 'function') {
    img.src = getFallbackCover(t, a);
  } else if (typeof window.getFallbackCoverSvg === 'function') {
    img.src = window.getFallbackCoverSvg(t, a);
  }
};

// --- UNIVERSAL ASSET URL RESOLVER ---
function getAssetUrl(url, bookId, defaultTitle, defaultAuthor) {"""

if old_handle_fn in sc_text:
    sc_text = sc_text.replace(old_handle_fn, new_handle_fn, 1)
    print("1A. Added global handleBookCoverError to store_scripts.py")

# Update search cards in renderCurrentSearchResults to call handleBookCoverError
old_search_img = """          <div style="width: 100%; aspect-ratio: 2 / 3; background-color: #FAF7F0; background-image: url(&quot;${fallbackSvg}&quot;); background-size: cover; background-position: center; border-radius: 8px; overflow: hidden; margin-bottom: 14px; box-shadow: -4px 8px 18px rgba(0,0,0,0.18); position: relative;">
            <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block;" onerror="this.onerror=null; this.src='${fallbackSvg}';" />"""

new_search_img = """          <div style="width: 100%; aspect-ratio: 2 / 3; background-color: #FAF7F0; border-radius: 8px; overflow: hidden; margin-bottom: 14px; box-shadow: -4px 8px 18px rgba(0,0,0,0.18); position: relative;">
            <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, '${escapeJs(titleSafe)}', '${escapeJs(authorSafe)}');" />"""

if old_search_img in sc_text:
    sc_text = sc_text.replace(old_search_img, new_search_img, 1)
    print("1B. Updated search card img tag with handleBookCoverError in store_scripts.py")
else:
    print("WARNING: old_search_img not found in store_scripts.py")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(sc_text)
print("Saved store_scripts.py")

# 2. Update editorial_video_theme.py
with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    ev_text = f.read()

# Update handleBookCoverError in editorial_video_theme.py
old_ev_handle = """function handleBookCoverError(img, title, author) {
    if (!img) return;
    img.onerror = null;
    var bookTitle = title || img.alt || 'Indigo Books';
    var bookAuthor = author || '';
    if (window.getFallbackCoverSvg) {
      img.src = window.getFallbackCoverSvg(bookTitle, bookAuthor);
    }
  }
  window.handleBookCoverError = handleBookCoverError;"""

new_ev_handle = """function handleBookCoverError(img, title, author) {
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

if old_ev_handle in ev_text:
    ev_text = ev_text.replace(old_ev_handle, new_ev_handle, 1)
    print("2A. Updated handleBookCoverError in editorial_video_theme.py")

# Update renderArchiveGrid img tag
old_arch_img = """'<img src="' + cover + '" alt="' + safeTitle + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=&quot;' + fallbackSvg + '&quot;;" />'"""
new_arch_img = """'<img src="' + cover + '" alt="' + safeTitle + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, \\'' + safeTitle.replace(/'/g, "\\\\'") + '\\', \\'' + safeAuthor.replace(/'/g, "\\\\'") + '\\');" />'"""

if old_arch_img in ev_text:
    ev_text = ev_text.replace(old_arch_img, new_arch_img, 1)
    print("2B. Updated renderArchiveGrid img tag in editorial_video_theme.py")
else:
    print("WARNING: old_arch_img not found in editorial_video_theme.py")

# Update renderShelfRow img tag
old_shelf_img = """'<img src="' + coverUrl + '" alt="' + b.title + '" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=&quot;' + shelfFallback + '&quot;;" />'"""
new_shelf_img = """'<img src="' + coverUrl + '" alt="' + b.title + '" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, \\'' + (b.title || '').replace(/'/g, "\\\\'") + '\\', \\'' + (b.author || '').replace(/'/g, "\\\\'") + '\\');" />'"""

if old_shelf_img in ev_text:
    ev_text = ev_text.replace(old_shelf_img, new_shelf_img, 1)
    print("2C. Updated renderShelfRow img tag in editorial_video_theme.py")
else:
    print("WARNING: old_shelf_img not found in editorial_video_theme.py")

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(ev_text)
print("Saved editorial_video_theme.py")

print("\n=== Master Fixes Applied ===")
