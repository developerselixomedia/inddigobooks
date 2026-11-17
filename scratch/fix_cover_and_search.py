import os

print("=== FIXING COVER VISIBILITY & SOLO SEARCH BUTTON ===")

with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    ev_text = f.read()

# 1. Update activateUniversalSearch to reliably close solo book page and focus search input
old_activate_search = """window.activateUniversalSearch = function(e) {
    if (e && typeof e.stopPropagation === 'function') {
      e.stopPropagation();
    }
    var searchInput = document.getElementById('editorialSearchInput');
    var resultsBox = document.getElementById('editorialSearchResults');
    if (!searchInput) {
      window.location.href = '/search';
      return;
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(function() {
      searchInput.focus();
      searchInput.select();
      if (typeof window.showSearchSuggestionsPopup === 'function') {
        window.showSearchSuggestionsPopup();
      }
      if (resultsBox) {
        resultsBox.style.display = 'block';
      }
    }, 40);
  };"""

new_activate_search = """window.activateUniversalSearch = function(e) {
    if (e && typeof e.stopPropagation === 'function') {
      e.stopPropagation();
    }
    // 1. Immediately close solo book page so search bar and results are 100% visible
    if (typeof window.closeSoloBookPage === 'function') {
      window.closeSoloBookPage();
    } else {
      var soloView = document.getElementById('indigo-solo-product-view');
      if (soloView) {
        soloView.classList.remove('is-active');
        soloView.style.display = 'none';
      }
      document.documentElement.classList.remove('solo-page-active');
      document.body.classList.remove('solo-page-active');
      document.body.style.removeProperty('overflow');
      document.documentElement.style.removeProperty('overflow');
    }

    var searchInput = document.getElementById('editorialSearchInput');
    var resultsBox = document.getElementById('editorialSearchResults');
    if (!searchInput) {
      window.location.href = '/search';
      return;
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(function() {
      searchInput.focus();
      searchInput.select();
      if (typeof window.showSearchSuggestionsPopup === 'function') {
        window.showSearchSuggestionsPopup();
      }
      if (resultsBox) {
        resultsBox.style.display = 'block';
      }
    }, 60);
  };"""

assert old_activate_search in ev_text, "old_activate_search not found in editorial_video_theme.py"
ev_text = ev_text.replace(old_activate_search, new_activate_search, 1)
print("1. Successfully updated activateUniversalSearch to close solo page and focus search input!")

# 2. Fix Solo Book Page Cover Leaf: define coverImg before applyFormat and set fallback onerror without black box
target_solo_cover_leaf = """    // Populate 3D Book Cover & Inside Pages (Strict Monolingual with Instant SVG preview)
    var soloFallbackSvg = getFallbackCoverSvg(found.title, found.author);
    var coverLeafFront = document.getElementById('v2CoverLeaf');
    if (coverLeafFront) {
      coverLeafFront.style.backgroundColor = '#1A1412';
      coverLeafFront.style.backgroundImage = 'url(' + soloFallbackSvg + ')';
      coverLeafFront.style.backgroundSize = 'cover';
      coverLeafFront.style.backgroundPosition = 'center';
    }

    var coverImg = document.getElementById('v2CoverLeafImg');
    if (coverImg) {
      coverImg.style.opacity = '0';
      coverImg.style.transition = 'opacity 0.35s ease';
      coverImg.onload = function() { this.style.opacity = '1'; };
      coverImg.onerror = function() { this.style.display = 'none'; };
      coverImg.setAttribute('referrerpolicy', 'no-referrer');
      coverImg.setAttribute('decoding', 'async');
      coverImg.src = found.cover;
    }"""

replacement_solo_cover_leaf = """    // Populate 3D Book Cover & Inside Pages (Strict Monolingual with Guaranteed Visible Cover)
    var soloFallbackSvg = getFallbackCoverSvg(found.title, found.author);
    var coverLeafFront = document.getElementById('v2CoverLeaf');
    if (coverLeafFront) {
      coverLeafFront.style.backgroundColor = '#FAF7F0';
      coverLeafFront.style.backgroundImage = 'url(\"' + soloFallbackSvg + '\")';
      coverLeafFront.style.backgroundSize = 'cover';
      coverLeafFront.style.backgroundPosition = 'center';
    }

    var coverImg = document.getElementById('v2CoverLeafImg');
    if (coverImg) {
      coverImg.style.display = 'block';
      coverImg.style.opacity = '1';
      coverImg.style.width = '100%';
      coverImg.style.height = '100%';
      coverImg.style.objectFit = 'cover';
      coverImg.setAttribute('referrerpolicy', 'no-referrer');
      coverImg.onerror = function() {
        this.onerror = null;
        if (window.getFallbackCoverSvg) {
          this.src = window.getFallbackCoverSvg(found.title, found.author);
        }
      };
      var targetCover = getCoverUrl(found.cover, found.title, found.author);
      coverImg.src = targetCover;
    }"""

assert target_solo_cover_leaf in ev_text, "target_solo_cover_leaf not found in editorial_video_theme.py"
ev_text = ev_text.replace(target_solo_cover_leaf, replacement_solo_cover_leaf, 1)
print("2. Successfully updated solo page cover leaf to guarantee visible cover and fallback!")

# 3. Fix renderArchiveGrid in editorial_video_theme.py: reliable image loading & fallback
target_archive_card = """var fallbackSvg = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #1A1412; background-image: url(' + fallbackSvg + '); background-size: cover; background-position: center;">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" decoding="async" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block; opacity:0; transition:opacity 0.35s ease;" onload="this.style.opacity=1;" onerror="this.remove();" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +"""

replacement_archive_card = """var fallbackSvg = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #FAF7F0; background-image: url(\\'\"\\' + fallbackSvg + \\\'\"\\'); background-size: cover; background-position: center;">' +
            '<img src=\"' + cover + '\" alt=\"' + safeTitle + '\" class=\"v2-archive-cover-img\" referrerpolicy=\"no-referrer\" loading=\"lazy\" style=\"position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;\" onerror=\"this.onerror=null; this.src=\\'\"\\' + fallbackSvg + \\\'\"\\';\" />' +
            '<span style=\"position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);\">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class=\"v2-archive-card-title\" title=\"' + safeTitle + '\">' + safeTitle + '</h3>' +
          '<div class=\"v2-archive-card-author\">By ' + safeAuthor + '</div>' +
        '</div>' +"""

# Let's check if target_archive_card matches
if target_archive_card in ev_text:
    ev_text = ev_text.replace(target_archive_card, replacement_archive_card, 1)
    print("3. Successfully updated renderArchiveGrid with reliable cover fallback!")
else:
    print("WARNING: target_archive_card not found directly in editorial_video_theme.py")

# 4. Fix renderShelfRow in editorial_video_theme.py
target_shelf_card = """var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var shelfFallback = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf" style="position:relative; background-color:#1A1412; background-image:url(' + shelfFallback + '); background-size:cover; background-position:center;">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" referrerpolicy="no-referrer" loading="lazy" decoding="async" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; transition:opacity 0.35s ease;" onload="this.style.opacity=1;" onerror="this.remove();" />' +
          '</div>' +
        '</div>' +"""

replacement_shelf_card = """var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var shelfFallback = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div class=\"v2-card-cover-wrap\">' +
          '<div class=\"v2-card-cover-leaf\" style=\"position:relative; background-color:#FAF7F0; background-image:url(\\'\"\\' + shelfFallback + \\\'\"\\'); background-size:cover; background-position:center;\">' +
            '<img src=\"' + coverUrl + '\" alt=\"' + b.title + '\" referrerpolicy=\"no-referrer\" loading=\"lazy\" style=\"position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;\" onerror=\"this.onerror=null; this.src=\\'\"\\' + shelfFallback + \\\'\"\\';\" />' +
          '</div>' +
        '</div>' +"""

if target_shelf_card in ev_text:
    ev_text = ev_text.replace(target_shelf_card, replacement_shelf_card, 1)
    print("4. Successfully updated renderShelfRow with reliable cover fallback!")
else:
    print("WARNING: target_shelf_card not found directly in editorial_video_theme.py")

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(ev_text)

print("Saved editorial_video_theme.py")

# ==============================================================================
# 5. Fix store_scripts.py search card rendering
# ==============================================================================
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    sc_text = f.read()

target_search_card = """    const fallbackSvg = getFallbackCover(titleSafe, authorSafe);
    return `
      <div class="v2-search-book-card" onclick="window.openSoloBookPage('${escapeJs(bookIdSafe)}');" style="background: #FFFFFF; border: 1px solid #EAE5DC; border-radius: 14px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
        <div>
          <div style="width: 100%; aspect-ratio: 2 / 3; background-color: #1A1412; background-image: url('${fallbackSvg}'); background-size: cover; background-position: center; border-radius: 8px; overflow: hidden; margin-bottom: 14px; box-shadow: -4px 8px 18px rgba(0,0,0,0.18); position: relative;">
            <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" decoding="async" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 0.35s ease;" onload="this.style.opacity=1;" onerror="this.remove();" />
            <span style="position: absolute; top: 8px; left: 8px; font-size: 9.5px; font-weight: 800; color: #E04F33; background: rgba(255,255,255,0.95); padding: 2px 7px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.1em; z-index: 2; box-shadow: 0 2px 6px rgba(0,0,0,0.12);">
              ${escapeHtml(bookBinding)}
            </span>
          </div>"""

replacement_search_card = """    const fallbackSvg = getFallbackCover(titleSafe, authorSafe);
    return `
      <div class="v2-search-book-card" onclick="window.openSoloBookPage('${escapeJs(bookIdSafe)}');" style="background: #FFFFFF; border: 1px solid #EAE5DC; border-radius: 14px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
        <div>
          <div style="width: 100%; aspect-ratio: 2 / 3; background-color: #FAF7F0; background-image: url(&quot;${fallbackSvg}&quot;); background-size: cover; background-position: center; border-radius: 8px; overflow: hidden; margin-bottom: 14px; box-shadow: -4px 8px 18px rgba(0,0,0,0.18); position: relative;">
            <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block;" onerror="this.onerror=null; this.src='${fallbackSvg}';" />
            <span style="position: absolute; top: 8px; left: 8px; font-size: 9.5px; font-weight: 800; color: #E04F33; background: rgba(255,255,255,0.95); padding: 2px 7px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.1em; z-index: 2; box-shadow: 0 2px 6px rgba(0,0,0,0.12);">
              ${escapeHtml(bookBinding)}
            </span>
          </div>"""

assert target_search_card in sc_text, "target_search_card not found in store_scripts.py"
sc_text = sc_text.replace(target_search_card, replacement_search_card, 1)

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(sc_text)

print("5. Successfully updated store_scripts.py with reliable cover fallback!")
