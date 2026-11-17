import os, re

print("=== Starting Master Refactoring ===")

# ==============================================================================
# 1. Update editorial_video_theme.py
# ==============================================================================
with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    ev_text = f.read()

# 1A. Fix getCoverUrl: remove rajkamalprakashan interception & support (coverPath, defaultTitle, defaultAuthor)
old_getcover = """function getCoverUrl(coverPath, defaultTitle) {
    if (!coverPath) {
      if (defaultTitle && window.getFallbackCoverSvg) {
        return window.getFallbackCoverSvg(defaultTitle, '');
      }
      if (window.getFallbackCoverSvg) {
        return window.getFallbackCoverSvg(defaultTitle || 'Indigo Books', '');
      }
      return (window.PODIUM_CDN_COVERS && (window.PODIUM_CDN_COVERS['hero-godan.jpg'] || window.PODIUM_CDN_COVERS['assets/hero-godan.jpg'])) ||
             (window.SHOPIFY_ASSET_URL_ROOT ? window.SHOPIFY_ASSET_URL_ROOT + 'hero-godan.jpg' : 'assets/hero-godan.jpg');
    }
    // Intercept dead remote domain to eliminate net::ERR_CONNECTION_CLOSED
    if (coverPath.indexOf('images.rajkamalprakashan.com') !== -1 || coverPath.indexOf('rajkamalprakashan.com') !== -1) {
      if (window.getFallbackCoverSvg) {
        return window.getFallbackCoverSvg(defaultTitle || 'Indigo Books Archive', '');
      }
      return 'assets/hero-godan.jpg';
    }
    // If already absolute HTTP/HTTPS, protocol-relative '//', or data URI, return DIRECTLY without tampering
    if (coverPath.indexOf('http://') === 0 || coverPath.indexOf('https://') === 0 || coverPath.indexOf('//') === 0 || coverPath.indexOf('data:') === 0) {
      return coverPath;
    }"""

new_getcover = """function getCoverUrl(coverPath, defaultTitle, defaultAuthor) {
    if (!coverPath) {
      if (window.getFallbackCoverSvg) {
        return window.getFallbackCoverSvg(defaultTitle || 'Indigo Books Edition', defaultAuthor || 'Indigo Literary Archive');
      }
      return (window.PODIUM_CDN_COVERS && (window.PODIUM_CDN_COVERS['hero-godan.jpg'] || window.PODIUM_CDN_COVERS['assets/hero-godan.jpg'])) ||
             (window.SHOPIFY_ASSET_URL_ROOT ? window.SHOPIFY_ASSET_URL_ROOT + 'hero-godan.jpg' : 'assets/hero-godan.jpg');
    }
    // If already absolute HTTP/HTTPS, protocol-relative '//', or data URI, return DIRECTLY without tampering
    if (coverPath.indexOf('http://') === 0 || coverPath.indexOf('https://') === 0 || coverPath.indexOf('//') === 0 || coverPath.indexOf('data:') === 0) {
      return coverPath;
    }"""

if old_getcover in ev_text:
    ev_text = ev_text.replace(old_getcover, new_getcover, 1)
    print("1A. Successfully updated getCoverUrl in editorial_video_theme.py")
else:
    print("WARNING: old_getcover not found in editorial_video_theme.py")

# 1B. Fix renderArchiveGrid to use instant SVG background and fade-in image
old_archive_card_html = """card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18);">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.92);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;backdrop-filter:blur(4px);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +"""

new_archive_card_html = """var fallbackSvg = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #1A1412; background-image: url(' + fallbackSvg + '); background-size: cover; background-position: center;">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" decoding="async" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block; opacity:0; transition:opacity 0.35s ease;" onload="this.style.opacity=\\'1\\';" onerror="this.style.display=\\'none\\';" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +"""

if old_archive_card_html in ev_text:
    ev_text = ev_text.replace(old_archive_card_html, new_archive_card_html, 1)
    print("1B. Successfully updated renderArchiveGrid with instant SVG background")
else:
    print("WARNING: old_archive_card_html not found in editorial_video_theme.py")

# 1C. Fix renderShelfRow to use instant SVG background
old_shelf_card_html = """var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" referrerpolicy="no-referrer" loading="lazy" />' +
          '</div>' +
        '</div>' +"""

new_shelf_card_html = """var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var shelfFallback = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf" style="position:relative; background-color:#1A1412; background-image:url(' + shelfFallback + '); background-size:cover; background-position:center;">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" referrerpolicy="no-referrer" loading="lazy" decoding="async" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; transition:opacity 0.35s ease;" onload="this.style.opacity=\\'1\\';" onerror="this.style.display=\\'none\\';" />' +
          '</div>' +
        '</div>' +"""

if old_shelf_card_html in ev_text:
    ev_text = ev_text.replace(old_shelf_card_html, new_shelf_card_html, 1)
    print("1C. Successfully updated renderShelfRow with instant SVG background")
else:
    print("WARNING: old_shelf_card_html not found in editorial_video_theme.py")

# 1D. Replace applyFormat and variant handling in openSoloBookPage
old_format_block = """    // Format Selection Handlers (Paperback vs Hardcover Deluxe)
    var btnPb = document.getElementById('v2FormatPaperback');
    var btnHc = document.getElementById('v2FormatHardcover');
    var basePrice = found.rawPrice || 299;

    function applyFormat(fmt) {
      found.selectedFormat = fmt;
      var metaFmt = document.getElementById('v2MetaFormat');
      var priceEl = document.getElementById('v2SoloPrice');
      var metaEd = document.getElementById('v2MetaEdition');
      var mobPrice = document.getElementById('v2MobileBuyBarPrice');
      var mobFmt = document.getElementById('v2MobileBuyBarFormat');
      var pPages = found.pages || '320p';

      if (fmt === 'Hardcover') {
        if (btnHc) btnHc.classList.add('active');
        if (btnPb) btnPb.classList.remove('active');
        var hcPrice = basePrice + 150;
        found.selectedPrice = hcPrice;
        if (priceEl) priceEl.textContent = '₹' + hcPrice.toFixed(2);
        if (metaFmt) metaFmt.textContent = 'Hardcover Deluxe • ' + pPages;
        if (metaEd) metaEd.textContent = 'Deluxe Gold-Embossed Library Edition';
        if (mobPrice) mobPrice.textContent = '₹' + hcPrice.toFixed(2);
        if (mobFmt) mobFmt.textContent = 'Hardcover Deluxe';
      } else {
        if (btnPb) btnPb.classList.add('active');
        if (btnHc) btnHc.classList.remove('active');
        found.selectedPrice = basePrice;
        if (priceEl) priceEl.textContent = '₹' + basePrice.toFixed(2);
        if (metaFmt) metaFmt.textContent = 'Paperback • ' + pPages;
        if (metaEd) metaEd.textContent = found.edition || 'Official Standard Edition';
        if (mobPrice) mobPrice.textContent = '₹' + basePrice.toFixed(2);
        if (mobFmt) mobFmt.textContent = 'Paperback';
      }
    }

    if (btnPb) {
      btnPb.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Paperback');
      };
    }
    if (btnHc) {
      btnHc.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Hardcover');
      };
    }
    applyFormat('Paperback');"""

new_format_block = """    // Format Selection Handlers: Sibling Variant Lookup from Master Catalog
    var btnPb = document.getElementById('v2FormatPaperback');
    var btnHc = document.getElementById('v2FormatHardcover');

    // Scan MASTER_SEARCH_CATALOG and POPULAR_BOOKS for sibling variants of found.title
    var normTitle = String(found.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    var pbVariant = null;
    var hcVariant = null;

    function checkVariantMatch(v) {
      if (!v || !v.title) return;
      var vt = String(v.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
      if (vt === normTitle) {
        var b = String(v.binding || v.format || '').toLowerCase();
        if (b.indexOf('hard') !== -1) {
          if (!hcVariant) hcVariant = v;
        } else {
          if (!pbVariant) pbVariant = v;
        }
      }
    }

    if (window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) {
      for (var vi = 0; vi < window.MASTER_SEARCH_CATALOG.length; vi++) {
        checkVariantMatch(window.MASTER_SEARCH_CATALOG[vi]);
        if (pbVariant && hcVariant) break;
      }
    }
    if (!pbVariant || !hcVariant) {
      for (var pj = 0; pj < POPULAR_BOOKS.length; pj++) {
        checkVariantMatch(POPULAR_BOOKS[pj]);
        if (pbVariant && hcVariant) break;
      }
    }

    // Determine clicked book format
    var clickedBinding = String(found.binding || found.format || '').toLowerCase();
    var isClickedHc = clickedBinding.indexOf('hard') !== -1;
    if (isClickedHc && !hcVariant) hcVariant = found;
    if (!isClickedHc && !pbVariant) pbVariant = found;

    // Active format: if clicked book was Hardcover, start with Hardcover active!
    var activeInitialFmt = (isClickedHc && hcVariant) ? 'Hardcover' : (pbVariant ? 'Paperback' : (hcVariant ? 'Hardcover' : 'Paperback'));

    // Update Format Buttons visibility & text based on real catalog data
    if (btnPb) {
      if (pbVariant) {
        btnPb.style.display = 'inline-flex';
        var pbP = pbVariant.rawPrice || pbVariant.mrp || (parseFloat(String(pbVariant.price).replace(/[^0-9.]/g, '')) || 0);
        btnPb.innerHTML = 'Paperback' + (pbP > 0 ? ' (₹' + Math.round(pbP) + ')' : '');
      } else {
        btnPb.style.display = 'none';
      }
    }

    if (btnHc) {
      if (hcVariant) {
        btnHc.style.display = 'inline-flex';
        var hcP = hcVariant.rawPrice || hcVariant.mrp || (parseFloat(String(hcVariant.price).replace(/[^0-9.]/g, '')) || 0);
        btnHc.innerHTML = 'Hardcover Deluxe' + (hcP > 0 ? ' (₹' + Math.round(hcP) + ')' : '');
      } else {
        btnHc.style.display = 'none';
      }
    }

    function applyFormat(fmt) {
      found.selectedFormat = fmt;
      var metaFmt = document.getElementById('v2MetaFormat');
      var priceEl = document.getElementById('v2SoloPrice');
      var metaEd = document.getElementById('v2MetaEdition');
      var mobPrice = document.getElementById('v2MobileBuyBarPrice');
      var mobFmt = document.getElementById('v2MobileBuyBarFormat');
      var isbnEl = document.getElementById('v2MetaIsbn');

      var currentVar = (fmt === 'Hardcover' && hcVariant) ? hcVariant : (pbVariant || found);
      var exactPrice = currentVar.rawPrice || currentVar.mrp || (parseFloat(String(currentVar.price).replace(/[^0-9.]/g, '')) || 299);
      var exactIsbn = currentVar.isbn || currentVar.sku || found.isbn;
      var exactPages = currentVar.pages || found.pages || '280p';
      var exactCover = currentVar.cover || currentVar.coverUrl || found.cover;

      found.selectedPrice = exactPrice;
      found.selectedIsbn = exactIsbn;
      found.isbn = exactIsbn;
      found.price = '₹' + exactPrice.toFixed(2);

      if (fmt === 'Hardcover') {
        if (btnHc) btnHc.classList.add('active');
        if (btnPb) btnPb.classList.remove('active');
        if (priceEl) priceEl.textContent = '₹' + exactPrice.toFixed(2);
        if (metaFmt) metaFmt.textContent = 'Hardcover Deluxe • ' + exactPages;
        if (metaEd) metaEd.textContent = 'Deluxe Gold-Embossed Library Edition';
        if (mobPrice) mobPrice.textContent = '₹' + exactPrice.toFixed(2);
        if (mobFmt) mobFmt.textContent = 'Hardcover Deluxe';
      } else {
        if (btnPb) btnPb.classList.add('active');
        if (btnHc) btnHc.classList.remove('active');
        if (priceEl) priceEl.textContent = '₹' + exactPrice.toFixed(2);
        if (metaFmt) metaFmt.textContent = 'Paperback • ' + exactPages;
        if (metaEd) metaEd.textContent = currentVar.edition || found.edition || 'Official Standard Edition';
        if (mobPrice) mobPrice.textContent = '₹' + exactPrice.toFixed(2);
        if (mobFmt) mobFmt.textContent = 'Paperback';
      }

      if (isbnEl) isbnEl.textContent = exactIsbn;

      // Update cover preview if variant has distinct cover
      if (exactCover && coverImg) {
        coverImg.src = getCoverUrl(exactCover, found.title, found.author);
      }
    }

    if (btnPb) {
      btnPb.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Paperback');
      };
    }
    if (btnHc) {
      btnHc.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Hardcover');
      };
    }
    applyFormat(activeInitialFmt);"""

if old_format_block in ev_text:
    ev_text = ev_text.replace(old_format_block, new_format_block, 1)
    print("1D. Successfully replaced applyFormat with catalog variant resolution in editorial_video_theme.py")
else:
    print("WARNING: old_format_block not found in editorial_video_theme.py")

# 1E. Update Solo cover leaf with zero-latency SVG background
old_cover_populate = """    // Populate 3D Book Cover & Inside Pages (Strict Monolingual)
    var coverImg = document.getElementById('v2CoverLeafImg');
    if (coverImg) {
      coverImg.onerror = function() { window.handleBookCoverError && window.handleBookCoverError(this, found.title, found.author); };
      coverImg.setAttribute('referrerpolicy', 'no-referrer');
      coverImg.src = found.cover;
    }"""

new_cover_populate = """    // Populate 3D Book Cover & Inside Pages (Strict Monolingual with Instant SVG preview)
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

if old_cover_populate in ev_text:
    ev_text = ev_text.replace(old_cover_populate, new_cover_populate, 1)
    print("1E. Successfully updated Solo Book Page cover leaf with instant SVG preview")
else:
    print("WARNING: old_cover_populate not found in editorial_video_theme.py")

# 1F. Prevent subsequent static overrides of v2MetaFormat & v2MetaIsbn
old_spec_override = """    var sFmt = document.getElementById('v2MetaFormat');
    if (sFmt) sFmt.textContent = (found.format || 'Paperback') + ' • ' + (found.pages || '320p');
    var sIsbn = document.getElementById('v2MetaIsbn');
    if (sIsbn) sIsbn.textContent = found.isbn || '9788126702749';"""

new_spec_override = """    // Sibling variant resolution handles v2MetaFormat and v2MetaIsbn authoritatively"""

if old_spec_override in ev_text:
    ev_text = ev_text.replace(old_spec_override, new_spec_override, 1)
    print("1F. Successfully removed static spec override")
else:
    print("WARNING: old_spec_override not found in editorial_video_theme.py")

# 1G. Update Mobile CSS for solo view: make .v2-solo-left-panel compact and ensure clean layout
old_solo_mobile_css = """.v2-solo-left-panel {
      width: 100% !important;
      height: 380px !important;
      min-height: 380px !important;
      padding: 20px !important;
      overflow: hidden !important;
    }"""

new_solo_mobile_css = """.v2-solo-left-panel {
      width: 100% !important;
      height: auto !important;
      min-height: 0 !important;
      max-height: 180px !important;
      padding: 12px 16px !important;
      overflow: hidden !important;
    }
    .v2-solo-left-panel .v2-solo-quote-block {
      margin: 6px 0 !important;
    }
    .v2-solo-left-panel .v2-solo-quote-text {
      font-size: 13px !important;
      line-height: 1.4 !important;
      max-height: 52px !important;
      overflow: hidden !important;
      display: -webkit-box !important;
      -webkit-line-clamp: 2 !important;
      -webkit-box-orient: vertical !important;
    }"""

if old_solo_mobile_css in ev_text:
    ev_text = ev_text.replace(old_solo_mobile_css, new_solo_mobile_css, 1)
    print("1G. Successfully updated mobile solo view CSS")
else:
    print("WARNING: old_solo_mobile_css not found in editorial_video_theme.py")

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(ev_text)
print("Saved editorial_video_theme.py")

# ==============================================================================
# 2. Update store_scripts.py (renderCurrentSearchResults with instant SVG)
# ==============================================================================
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    sc_text = f.read()

old_search_card = """    return `
      <div class="v2-search-book-card" onclick="window.openSoloBookPage('${escapeJs(bookIdSafe)}');" style="background: #FFFFFF; border: 1px solid #EAE5DC; border-radius: 14px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
        <div>
          <div style="width: 100%; aspect-ratio: 2 / 3; background: #FAF7F0; border-radius: 8px; overflow: hidden; margin-bottom: 14px; box-shadow: -4px 8px 18px rgba(0,0,0,0.12); position: relative;">
            <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; display: block;" onerror="this.onerror=null; this.src='assets/hero-godan.jpg';" />
          </div>"""

new_search_card = """    const fallbackSvg = getFallbackCover(titleSafe, authorSafe);
    return `
      <div class="v2-search-book-card" onclick="window.openSoloBookPage('${escapeJs(bookIdSafe)}');" style="background: #FFFFFF; border: 1px solid #EAE5DC; border-radius: 14px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
        <div>
          <div style="width: 100%; aspect-ratio: 2 / 3; background-color: #1A1412; background-image: url('${fallbackSvg}'); background-size: cover; background-position: center; border-radius: 8px; overflow: hidden; margin-bottom: 14px; box-shadow: -4px 8px 18px rgba(0,0,0,0.18); position: relative;">
            <img referrerpolicy="no-referrer" src="${cover}" alt="${escapeHtml(titleSafe)}" loading="lazy" decoding="async" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 0.35s ease;" onload="this.style.opacity='1';" onerror="this.style.display='none';" />
            <span style="position: absolute; top: 8px; left: 8px; font-size: 9.5px; font-weight: 800; color: #E04F33; background: rgba(255,255,255,0.95); padding: 2px 7px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.1em; z-index: 2; box-shadow: 0 2px 6px rgba(0,0,0,0.12);">
              ${escapeHtml(bookBinding)}
            </span>
          </div>"""

if old_search_card in sc_text:
    sc_text = sc_text.replace(old_search_card, new_search_card, 1)
    print("2. Successfully updated store_scripts.py search cards with instant SVG background")
else:
    print("WARNING: old_search_card not found in store_scripts.py")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(sc_text)
print("Saved store_scripts.py")

# ==============================================================================
# 3. Update store_modals_and_search.py (Phone number & PIN input validation)
# ==============================================================================
with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    modals_text = f.read()

old_phone_input = '<input type="tel" id="checkoutPhone" placeholder="Enter 10-digit mobile number" required pattern="[0-9]{10}" maxlength="10" minlength="10" inputmode="numeric" style="flex: 1; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />'
new_phone_input = '<input type="tel" id="checkoutPhone" placeholder="Enter 10-digit mobile number" required pattern="[0-9]{10}" maxlength="10" minlength="10" inputmode="numeric" title="Please enter a valid 10-digit mobile number (e.g. 8840818783)" oninput="this.value = this.value.replace(/[^0-9]/g, \\\'\\\').slice(0, 10);" style="flex: 1; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />'

old_pin_input = '<input type="text" id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" minlength="6" required pattern="[0-9]{6}" inputmode="numeric" style="width: 100%; box-sizing: border-box; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />'
new_pin_input = '<input type="text" id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" minlength="6" required pattern="[0-9]{6}" inputmode="numeric" title="Please enter a 6-digit postal PIN code (e.g. 211003)" oninput="this.value = this.value.replace(/[^0-9]/g, \\\'\\\').slice(0, 6);" style="width: 100%; box-sizing: border-box; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />'

if old_phone_input in modals_text:
    modals_text = modals_text.replace(old_phone_input, new_phone_input, 1)
    print("3A. Successfully updated checkoutPhone input in store_modals_and_search.py")
else:
    print("WARNING: old_phone_input not found in store_modals_and_search.py")

if old_pin_input in modals_text:
    modals_text = modals_text.replace(old_pin_input, new_pin_input, 1)
    print("3B. Successfully updated checkoutPincode input in store_modals_and_search.py")
else:
    print("WARNING: old_pin_input not found in store_modals_and_search.py")

with open('store_modals_and_search.py', 'w', encoding='utf-8') as f:
    f.write(modals_text)
print("Saved store_modals_and_search.py")

# ==============================================================================
# 4. Suppress Tailwind CDN console warning in build_html_generator.py & layout/theme.liquid
# ==============================================================================
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    bh_text = f.read()

old_tw_script = '<script src="https://cdn.tailwindcss.com"></script>'
new_tw_script = """<script>
    (function(){
      var _w = console.warn;
      console.warn = function() {
        if (arguments[0] && typeof arguments[0] === 'string' && arguments[0].indexOf('cdn.tailwindcss.com') !== -1) return;
        _w.apply(console, arguments);
      };
    })();
  </script>
  <script src="https://cdn.tailwindcss.com"></script>"""

if old_tw_script in bh_text:
    bh_text = bh_text.replace(old_tw_script, new_tw_script, 1)
    print("4A. Successfully suppressed Tailwind console warning in build_html_generator.py")
    with open('build_html_generator.py', 'w', encoding='utf-8') as f:
        f.write(bh_text)

with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    tl_text = f.read()

if old_tw_script in tl_text:
    tl_text = tl_text.replace(old_tw_script, new_tw_script, 1)
    print("4B. Successfully suppressed Tailwind console warning in layout/theme.liquid")
    with open('layout/theme.liquid', 'w', encoding='utf-8') as f:
        f.write(tl_text)

print("\n=== Master Refactoring Code Changes Applied! ===")
