with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    // Scan MASTER_SEARCH_CATALOG and POPULAR_BOOKS for sibling variants of found.title
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
    }"""

replacement = """    // Scan MASTER_SEARCH_CATALOG and POPULAR_BOOKS for sibling variants of found.title
    var normTitle = String(found.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    var pbVariant = null;
    var hcVariant = null;

    function checkVariantMatch(v) {
      if (!v || !v.title) return;
      var vt = String(v.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
      if (vt === normTitle) {
        var va = String(v.author || '').trim().toLowerCase().split(',')[0].replace(/[^a-z0-9]/g, '');
        var fa = String(found.author || '').trim().toLowerCase().split(',')[0].replace(/[^a-z0-9]/g, '');
        if (va && fa && va.indexOf(fa) === -1 && fa.indexOf(va) === -1) {
          return;
        }
        var b = String(v.binding || v.format || '').toLowerCase();
        if (b.indexOf('hard') !== -1) {
          if (!hcVariant) hcVariant = v;
        } else if (b.indexOf('paper') !== -1 || b.indexOf('text') !== -1) {
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

    // Strict Rule: ONLY show format toggle if BOTH formats actually exist in catalog!
    var hasBothFormats = !!(pbVariant && hcVariant);
    var formatWrap = document.getElementById('v2SoloFormatWrap');
    if (formatWrap) {
      formatWrap.style.display = hasBothFormats ? 'block' : 'none';
    }

    // Active format: if clicked book was Hardcover, start with Hardcover active!
    var activeInitialFmt = (isClickedHc && hcVariant) ? 'Hardcover' : (pbVariant ? 'Paperback' : (hcVariant ? 'Hardcover' : 'Paperback'));

    // Update Format Buttons visibility & text based on real catalog data
    if (btnPb) {
      if (hasBothFormats && pbVariant) {
        btnPb.style.display = 'inline-flex';
        var pbP = pbVariant.rawPrice || pbVariant.mrp || (parseFloat(String(pbVariant.price).replace(/[^0-9.]/g, '')) || 0);
        btnPb.innerHTML = 'Paperback' + (pbP > 0 ? ' (₹' + Math.round(pbP) + ')' : '');
      } else {
        btnPb.style.display = 'none';
      }
    }

    if (btnHc) {
      if (hasBothFormats && hcVariant) {
        btnHc.style.display = 'inline-flex';
        var hcP = hcVariant.rawPrice || hcVariant.mrp || (parseFloat(String(hcVariant.price).replace(/[^0-9.]/g, '')) || 0);
        btnHc.innerHTML = 'Hardcover Deluxe' + (hcP > 0 ? ' (₹' + Math.round(hcP) + ')' : '');
      } else {
        btnHc.style.display = 'none';
      }
    }"""

assert target in text, "Target not found in editorial_video_theme.py"
text = text.replace(target, replacement)
with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated format logic in editorial_video_theme.py")
