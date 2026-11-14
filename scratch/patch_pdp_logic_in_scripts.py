# -*- coding: utf-8 -*-
"""
scratch/patch_pdp_logic_in_scripts.py
Replaces openDedicatedProductPage and renderPdpRecommendations with full
multi-variant, GPS pincode auto-fill, dynamic delivery date, and 3D hover shelf support.
"""

with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace openDedicatedProductPage
old_open_start = text.find('function openDedicatedProductPage(bookIdOrHandle, triggerEl) {')
old_open_end = text.find('// Global Author Search & Catalog Browse Helpers', old_open_start)

if old_open_start != -1 and old_open_end != -1:
    print(f"Found openDedicatedProductPage from {old_open_start} to {old_open_end}")
    new_open_code = """function openDedicatedProductPage(bookIdOrHandle, triggerEl) {
  const book = window.resolveBookObject(bookIdOrHandle, triggerEl);
  if (!book) {
    console.warn("Indigo Books: Could not resolve book for", bookIdOrHandle);
    return;
  }

  currentActivePdpBook = book;
  currentPdpQuantity = 1;

  const homeView = document.getElementById('homepage-view');
  const pdpView = document.getElementById('single-product-page-view');
  if (!pdpView) return;

  // 1. Breadcrumbs
  const bCat = document.getElementById('pdpBreadcrumbCategory');
  if (bCat) bCat.textContent = book.category || book.pub || 'Curated Literature';
  const bTitle = document.getElementById('pdpBreadcrumbTitle');
  if (bTitle) bTitle.textContent = book.title;

  // 2. Cover image
  const resolvedCover = getAssetUrl(book.cover || book.coverUrl, book.id) || getFallbackCover(book.title, book.author);
  const coverImg = document.getElementById('pdpMainCoverImg');
  if (coverImg) {
    coverImg.src = resolvedCover;
    coverImg.alt = book.title;
    coverImg.onerror = function() {
      this.onerror = null;
      this.src = getFallbackCover(book.title, book.author);
    };
  }

  // 3. Title, Category, Rating
  const genreTag = document.getElementById('pdpGenreTag');
  if (genreTag) genreTag.textContent = book.category ? book.category.toUpperCase() : (book.pub ? book.pub.toUpperCase() : 'EXCLUSIVE EDITION');
  const titleEl = document.getElementById('pdpTitle');
  if (titleEl) titleEl.textContent = book.title;

  // 4. Clickable Author Avatar Pill
  const authorInitial = (book.author || 'A').trim().charAt(0).toUpperCase();
  const avEl = document.getElementById('pdpAuthorAvatar');
  if (avEl) avEl.textContent = authorInitial;
  const authLink = document.getElementById('pdpAuthorLink');
  if (authLink) authLink.textContent = book.author || 'Celebrated Author';

  // 5. Prices
  const priceFormatted = book.price ? (String(book.price).startsWith('₹') ? book.price : '₹' + book.price) : '₹299.00';
  const sellPriceEl = document.getElementById('pdpSellingPrice');
  const bbPriceEl = document.getElementById('pdpBbPrice');
  if (sellPriceEl) sellPriceEl.textContent = priceFormatted;
  if (bbPriceEl) bbPriceEl.textContent = priceFormatted;

  const comparePriceEl = document.getElementById('pdpComparePrice');
  const discountBadgeEl = document.getElementById('pdpDiscountBadge');
  if (book.oldPrice && book.oldPrice !== book.price && book.oldPrice !== '') {
    const oldFormatted = String(book.oldPrice).startsWith('₹') ? book.oldPrice : '₹' + book.oldPrice;
    if (comparePriceEl) {
      comparePriceEl.textContent = oldFormatted;
      comparePriceEl.style.display = 'inline';
    }
    if (discountBadgeEl) {
      discountBadgeEl.textContent = book.discount || 'SPECIAL OFFER';
      discountBadgeEl.style.display = 'inline-block';
    }
  } else {
    if (comparePriceEl) comparePriceEl.style.display = 'none';
    if (discountBadgeEl) discountBadgeEl.style.display = 'none';
  }

  // 6. Interactive Variant Buttons
  const varContainer = document.getElementById('pdpVariantButtons');
  if (varContainer) {
    if (book.variants && book.variants.length > 0) {
      varContainer.innerHTML = book.variants.map(function(v, i) {
        return '<button type="button" class="pdp-variant-btn ' + (i === 0 ? 'active' : '') + '" onclick="selectPdpVariant(\\'' + escapeJs(v.format) + '\\')">' +
          escapeHtml(v.format) + ' &bull; ₹' + parseFloat(v.price).toFixed(2) +
        '</button>';
      }).join('');
      currentActivePdpVariant = book.variants[0];
    } else {
      varContainer.innerHTML = '<button type="button" class="pdp-variant-btn active" onclick="selectPdpVariant(\\'' + escapeJs(book.binding || 'Paperback') + '\\')">' +
        escapeHtml(book.binding || 'Paperback') + ' &bull; ' + priceFormatted +
      '</button>';
      currentActivePdpVariant = null;
    }
  }

  // 7. Live Stock Count Badge
  const stockBadge = document.getElementById('pdpStockBadge');
  if (stockBadge) {
    const sCount = (currentActivePdpVariant && currentActivePdpVariant.qty !== undefined) ? currentActivePdpVariant.qty : (book.stock || 100);
    stockBadge.innerHTML = '<i data-lucide="check" style="width: 15px; height: 15px;"></i> ✓ In Stock (' + sCount + ' left)';
  }

  // 8. 5-Day Dynamic Delivery Date
  const delDate = new Date(Date.now() + 5 * 24 * 60 * 60 * 1000).toLocaleDateString('en-IN', { weekday: 'long', day: 'numeric', month: 'short' });
  const elDel = document.getElementById('pdpEstimatedDeliveryDate');
  if (elDel) elDel.textContent = 'Delivery by ' + delDate;

  // 9. Description & Tech Specs
  const descEl = document.getElementById('pdpDescription');
  if (descEl) descEl.textContent = book.overview || ('Authentic work by ' + book.author + '. Published by ' + (book.pub || 'Lokbharti Prakashan') + ', this authoritative volume represents an essential edition in Indian literature and scholarly thought.');

  const specTitle = document.getElementById('pdpSpecTitle');
  if (specTitle) specTitle.textContent = book.title;
  const specAuth = document.getElementById('pdpSpecAuthor');
  if (specAuth) specAuth.textContent = book.author || 'Celebrated Author';
  const specPub = document.getElementById('pdpSpecPublisher');
  if (specPub) specPub.textContent = book.pub || 'Lokbharti Prakashan';
  const specBinding = document.getElementById('pdpSpecBinding');
  if (specBinding) specBinding.textContent = (currentActivePdpVariant ? currentActivePdpVariant.format : book.binding) || 'Paperback';
  const specIsbn = document.getElementById('pdpSpecIsbn');
  if (specIsbn) specIsbn.textContent = (currentActivePdpVariant ? currentActivePdpVariant.sku : book.isbn) || '9789389742152';
  const specPages = document.getElementById('pdpSpecPages');
  if (specPages) specPages.textContent = book.pages || '250p';
  const specLang = document.getElementById('pdpSpecLanguage');
  if (specLang) specLang.textContent = book.lang || 'Hindi';
  const specEd = document.getElementById('pdpSpecEdition');
  if (specEd) specEd.textContent = book.edition || '1st Edition';
  const specWeight = document.getElementById('pdpSpecWeight');
  if (specWeight) specWeight.textContent = (currentActivePdpVariant && currentActivePdpVariant.grams ? currentActivePdpVariant.grams + ' g' : book.weight) || '250 g';
  const specDim = document.getElementById('pdpSpecDimensions');
  if (specDim) specDim.textContent = book.dimensions || '21.6 × 14.0 × 1.5 cm';

  // 10. 3D Cover Back & Inside details
  const insideTitle = document.getElementById('pdp3dInsideTitle');
  if (insideTitle) insideTitle.textContent = book.title;
  const insideAuth = document.getElementById('pdp3dInsideAuthor');
  if (insideAuth) insideAuth.textContent = 'By ' + (book.author || 'Author');
  const insideFoot = document.getElementById('pdp3dInsideFooter');
  if (insideFoot) insideFoot.textContent = (book.pages || '250p') + ' • ' + (book.pub || 'Lokbharti');
  const cbPub = document.getElementById('pdpCoverBackPub');
  if (cbPub) cbPub.textContent = book.pub || 'Authorized Copy';
  const cbFormat = document.getElementById('pdpCoverBackFormat');
  if (cbFormat) cbFormat.textContent = ((currentActivePdpVariant ? currentActivePdpVariant.format : book.binding) || 'Paperback') + ' • ' + priceFormatted;

  // 11. Mini Thumbnail
  const thumb1 = document.getElementById('pdpThumbImg1');
  if (thumb1) thumb1.src = resolvedCover;

  // 12. Check saved location from localStorage
  try {
    const savedLoc = localStorage.getItem('indigo_saved_location');
    if (savedLoc) {
      const loc = JSON.parse(savedLoc);
      const pinInput = document.getElementById('pdpPincodeInput');
      const pinStatus = document.getElementById('pdpPincodeStatus');
      if (pinInput && loc.pincode) {
        pinInput.value = loc.pincode;
        if (pinStatus) {
          pinStatus.style.display = 'block';
          pinStatus.style.color = '#16A34A';
          pinStatus.innerHTML = '<strong>✓ Verified Location:</strong> ' + (loc.city || 'India') + ' (' + loc.pincode + '). Express Delivery &amp; COD Active!';
        }
      }
    }
  } catch (e) {}

  // 13. Excerpt reset
  const excerptBox = document.getElementById('pdpExcerptBox');
  const excerptText = document.getElementById('pdpExcerptText');
  if (excerptBox && excerptText) {
    excerptText.textContent = book.firstPageExcerpt || book.overview || 'First page preview available upon book dispatch.';
    excerptBox.classList.remove('open');
  }

  // 14. Qty Input Reset
  const qtyInput = document.getElementById('pdpQtyInput');
  if (qtyInput) qtyInput.value = '1';

  // 15. Render Same-Author Shelf
  renderPdpRecommendations(book);

  // 16. View Swap
  if (homeView) homeView.style.display = 'none';
  pdpView.style.display = 'block';

  // 17. Update Hash without jump
  const safeHandle = book.handle || book.id || 'book';
  if (window.location.hash !== '#/product/' + safeHandle) {
    history.pushState(null, null, '#/product/' + safeHandle);
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (typeof lucide !== 'undefined') lucide.createIcons();
}
\n\n"""
    text = text[:old_open_start] + new_open_code + text[old_open_end:]
    print("openDedicatedProductPage upgraded successfully!")

# Replace renderPdpRecommendations
old_rec_start = text.find('function renderPdpRecommendations(activeBook) {')
old_rec_end = text.find('function checkHashRoute() {', old_rec_start)

if old_rec_start != -1 and old_rec_end != -1:
    print(f"Found renderPdpRecommendations from {old_rec_start} to {old_rec_end}")
    new_rec_code = """function renderPdpRecommendations(activeBook) {
  const container = document.getElementById('pdpAuthorShelfContainer');
  const heading = document.getElementById('pdpAuthorShelfHeading');
  if (!container) return;

  const authorName = (activeBook.author || '').toLowerCase();
  const isPiyush = authorName.includes('piyush');

  let recs = [];
  const metaSource = (typeof MODAL_METADATA_DATABASE !== 'undefined') ? Object.values(MODAL_METADATA_DATABASE) : [];

  if (isPiyush) {
    if (heading) heading.textContent = 'More Books by Piyush Mishra';
    recs = metaSource.filter(function(b) {
      return b && b.author && b.author.toLowerCase().includes('piyush') && b.handle !== activeBook.handle;
    });
  } else {
    if (heading) heading.textContent = 'More Books by ' + (activeBook.author || 'This Author');
    recs = metaSource.filter(function(b) {
      return b && b.author && b.author.toLowerCase() === authorName && b.handle !== activeBook.handle;
    });
    if (recs.length < 4) {
      const cat = (activeBook.category || '').toLowerCase();
      const sameCat = metaSource.filter(function(b) {
        return b && b.handle !== activeBook.handle && !recs.includes(b) && (b.category || '').toLowerCase() === cat;
      });
      recs = recs.concat(sameCat);
    }
  }

  // Deduplicate by handle
  const seen = new Set();
  const deduped = [];
  recs.forEach(function(b) {
    if (b && b.handle && !seen.has(b.handle)) {
      seen.add(b.handle);
      deduped.push(b);
    }
  });

  if (deduped.length === 0) {
    container.innerHTML = '<div style="color: #64748B; font-size: 13px; padding: 12px;">Explore more literary works in our pan-India catalog.</div>';
    return;
  }

  container.innerHTML = deduped.slice(0, 8).map(function(b) {
    const rawCover = b.cover || b.coverUrl || '';
    const cUrl = getAssetUrl(rawCover, b.id) || getFallbackCover(b.title, b.author);
    const pStr = b.price ? (String(b.price).startsWith('₹') ? b.price : '₹' + b.price) : '₹299.00';
    return `
      <div class="shelf-book-card" data-book-id="${escapeHtml(b.id)}" data-handle="${escapeHtml(b.handle)}">
        <div class="indigo-3d-book-stage" onclick="window.openSoloBookPage('${escapeJs(b.id)}', this)">
          <div class="indigo-3d-inside-page">
            <div style="font-size: 8.5px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">
              INDIGO ARCHIVE
            </div>
            <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.35; color: #1E293B; font-weight: 700;">
              ${escapeHtml(b.title)}
            </div>
            <div style="font-size: 9.5px; color: #64748B;">
              By ${escapeHtml(b.author)}
            </div>
            <div style="font-size: 8.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 3px;">
              ${escapeHtml(b.pages || '250p')} &bull; ${escapeHtml(b.pub || 'Lokbharti')}
            </div>
          </div>
          <div class="indigo-3d-cover-leaf">
            <div class="indigo-3d-cover-front">
              <img src="${cUrl}" alt="${escapeHtml(b.title)}" loading="lazy" />
            </div>
            <div class="indigo-3d-cover-back">
              <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                100% GENUINE
              </div>
              <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                ${escapeHtml(b.pub || 'Publisher Copy')}
              </div>
              <div style="font-size: 9.5px; color: #CBD5E1;">
                ${escapeHtml(b.binding || 'Paperback')} &bull; ${pStr}
              </div>
              <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                Click for Details &rarr;
              </div>
            </div>
          </div>
        </div>
        <div style="margin-top: 10px; display: flex; flex-direction: column; flex: 1; justify-content: space-between;">
          <div>
            <div style="font-family: 'Merriweather', serif; font-size: 13.5px; font-weight: 700; color: #0F172A; line-height: 1.3; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; cursor: pointer;" onclick="window.openSoloBookPage('${escapeJs(b.id)}', this)" title="${escapeHtml(b.title)}">
              ${escapeHtml(b.title)}
            </div>
            <div style="font-size: 12px; color: #64748B; margin-top: 2px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
              ${escapeHtml(b.author)}
            </div>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
            <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; font-weight: 800; color: #0F172A;">${pStr}</span>
            <button type="button" onclick="window.addToCart('${escapeJs(b.id)}', '${escapeJs(b.title)}', '${escapeJs(b.price)}', '${escapeJs(cUrl)}', '${escapeJs(b.binding || 'Paperback')}', this)" style="background: #0F172A; color: #FFFFFF; border: none; border-radius: 6px; padding: 4px 10px; font-size: 11.5px; font-weight: 700; cursor: pointer;">
              Add
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}
\n\n"""
    text = text[:old_rec_start] + new_rec_code + text[old_rec_end:]
    print("renderPdpRecommendations upgraded successfully!")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("store_scripts.py PDP logic updated successfully!")

