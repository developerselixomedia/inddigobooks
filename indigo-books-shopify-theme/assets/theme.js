/**
 * Indigo Books - Horizon Theme Core JavaScript
 */

document.addEventListener('DOMContentLoaded', function () {
  initCartDrawer();
  initPredictiveSearch();
  initProductPdp();
  initCarousels();
  initCascadeBookSlider();
  initHeroFestivalAnimation();
});

/* Cart Drawer Logic */
function initCartDrawer() {
  const drawer = document.getElementById('CartDrawer');
  const overlay = document.getElementById('CartDrawerOverlay');
  if (!drawer || !overlay) return;

  function openDrawer() {
    drawer.classList.add('active');
    overlay.classList.add('active');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('active');
    overlay.classList.remove('active');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('[data-action="open-cart-drawer"]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openDrawer();
    });
  });

  document.querySelectorAll('[data-action="close-cart-drawer"]').forEach(btn => {
    btn.addEventListener('click', closeDrawer);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('active')) closeDrawer();
  });

  // AJAX Add to Cart handler
  document.addEventListener('click', function (e) {
    const addBtn = e.target.closest('[data-action="add-to-cart"]');
    if (addBtn) {
      e.preventDefault();
      const variantId = addBtn.dataset.variantId;
      if (!variantId) return;

      addBtn.disabled = true;
      const originalText = addBtn.innerText;
      addBtn.innerText = 'Adding...';

      fetch(window.ShopifyTheme.routes.cart_add_url + '.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: variantId, quantity: 1 })
      })
      .then(res => res.json())
      .then(item => {
        addBtn.innerText = 'Added! ';
        setTimeout(() => {
          addBtn.disabled = false;
          addBtn.innerText = originalText;
        }, 1500);

        // Refresh Cart and open drawer
        refreshCartDrawer();
        openDrawer();

        // Dispatch Meta Pixel AddToCart
        if (window.IndigoTracking) {
          window.IndigoTracking.trackAddToCart(item);
        }
      })
      .catch(err => {
        console.error(err);
        addBtn.disabled = false;
        addBtn.innerText = originalText;
      });
    }
  });

  // Quantity updates in drawer
  drawer.addEventListener('click', function(e) {
    const decreaseBtn = e.target.closest('[data-action="decrease-qty"]');
    const increaseBtn = e.target.closest('[data-action="increase-qty"]');
    const removeBtn = e.target.closest('[data-action="remove-item"]');

    if (decreaseBtn || increaseBtn || removeBtn) {
      const line = (decreaseBtn || increaseBtn || removeBtn).dataset.line;
      let newQty = 0;
      if (decreaseBtn) {
        const input = decreaseBtn.parentElement.querySelector('.qty-input');
        newQty = Math.max(0, parseInt(input.value) - 1);
      } else if (increaseBtn) {
        const input = increaseBtn.parentElement.querySelector('.qty-input');
        newQty = parseInt(input.value) + 1;
      }

      updateCartLine(line, newQty);
    }
  });
}

function updateCartLine(line, quantity) {
  fetch(window.ShopifyTheme.routes.cart_change_url + '.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ line: line, quantity: quantity })
  })
  .then(res => res.json())
  .then(() => {
    refreshCartDrawer();
  })
  .catch(err => console.error(err));
}

function refreshCartDrawer() {
  fetch('/?section_id=cart-drawer-section')
    .then(res => res.text())
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const newDrawer = doc.getElementById('CartDrawer');
      const currentDrawer = document.getElementById('CartDrawer');
      if (newDrawer && currentDrawer) {
        currentDrawer.innerHTML = newDrawer.innerHTML;
      }

      // Update badge counts
      const newBadge = doc.querySelector('.cart-drawer__count');
      const headerBadge = document.getElementById('CartBadgeCount');
      if (newBadge && headerBadge) {
        headerBadge.innerText = newBadge.innerText.replace(/[()]/g, '');
      }
    });
}

/* Live Predictive Search */
function initPredictiveSearch() {
  const searchInput = document.getElementById('HeaderSearchInput');
  const resultsContainer = document.getElementById('PredictiveSearchResults');
  if (!searchInput || !resultsContainer) return;

  let debounceTimer;

  searchInput.addEventListener('input', function () {
    clearTimeout(debounceTimer);
    const query = this.value.trim();

    if (query.length < 2) {
      resultsContainer.style.display = 'none';
      resultsContainer.innerHTML = '';
      return;
    }

    debounceTimer = setTimeout(() => {
      fetch(`${window.ShopifyTheme.routes.predictive_search_url}?q=${encodeURIComponent(query)}&section_id=predictive-search`)
        .then(res => res.text())
        .then(html => {
          resultsContainer.innerHTML = html;
          resultsContainer.style.display = 'block';
        })
        .catch(err => console.error(err));
    }, 250);
  });

  document.addEventListener('click', function(e) {
    if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
      resultsContainer.style.display = 'none';
    }
  });
}

/* Product Detail Page Enhancements */
function initProductPdp() {
  // Thumbnail switching
  document.querySelectorAll('.thumb-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.thumb-btn').forEach(b => b.classList.remove('thumb-btn--active'));
      this.classList.add('thumb-btn--active');
      const mainImg = document.getElementById('ProductMainImage');
      if (mainImg) mainImg.src = this.dataset.fullSrc;
    });
  });

  // Quantity increase / decrease
  const qtyInput = document.getElementById('ProductQuantity');
  document.getElementById('QtyDecrease')?.addEventListener('click', () => {
    if (qtyInput) qtyInput.value = Math.max(1, parseInt(qtyInput.value) - 1);
  });
  document.getElementById('QtyIncrease')?.addEventListener('click', () => {
    if (qtyInput) qtyInput.value = parseInt(qtyInput.value) + 1;
  });

  // Instant Buy Now (Direct Checkout)
  document.getElementById('InstantBuyNowBtn')?.addEventListener('click', function() {
    const variantId = document.getElementById('SelectedVariantId')?.value;
    const qty = document.getElementById('ProductQuantity')?.value || 1;
    if (!variantId) return;

    fetch(window.ShopifyTheme.routes.cart_add_url + '.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: variantId, quantity: parseInt(qty) })
    })
    .then(() => {
      window.location.href = '/checkout';
    });
  });

  // Sticky Bar Add to Cart
  document.getElementById('StickyAddToCartBtn')?.addEventListener('click', function() {
    document.getElementById('AddToCartBtn')?.click();
  });
}

/* Horizontal Carousels */
function initCarousels() {
  document.querySelectorAll('[data-carousel-prev]').forEach(btn => {
    btn.addEventListener('click', function() {
      const trackId = this.dataset.carouselPrev;
      const track = document.getElementById(trackId);
      if (track) track.scrollBy({ left: -300, behavior: 'smooth' });
    });
  });

  document.querySelectorAll('[data-carousel-next]').forEach(btn => {
    btn.addEventListener('click', function() {
      const trackId = this.dataset.carouselNext;
      const track = document.getElementById(trackId);
      if (track) track.scrollBy({ left: 300, behavior: 'smooth' });
    });
  });
}

/* 3D Cascading Book Slider (Showcase Video Animation) */
function initCascadeBookSlider() {
  const slider = document.getElementById('CascadeBookSlider');
  if (!slider) return;

  const cards = Array.from(slider.querySelectorAll('.cascade-card'));
  if (cards.length === 0) return;

  let currentIndex = 0;
  const progressBar = document.getElementById('CascadeProgressBar');
  let autoTimer;

  function updateCards() {
    cards.forEach((card, i) => {
      card.className = 'cascade-card';
      const diff = (i - currentIndex + cards.length) % cards.length;
      if (diff === 0) {
        card.classList.add('cascade-card--active');
      } else if (diff === 1) {
        card.classList.add('cascade-card--next');
      } else if (diff === 2) {
        card.classList.add('cascade-card--back');
      } else {
        card.classList.add('cascade-card--hidden');
      }
    });

    if (progressBar) {
      progressBar.style.transition = 'none';
      progressBar.style.width = '0%';
      requestAnimationFrame(() => {
        setTimeout(() => {
          progressBar.style.transition = 'width 3.8s linear';
          progressBar.style.width = '100%';
        }, 30);
      });
    }
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % cards.length;
    updateCards();
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + cards.length) % cards.length;
    updateCards();
  }

  function startAutoplay() {
    clearInterval(autoTimer);
    autoTimer = setInterval(nextSlide, 4000);
  }

  document.getElementById('CascadeNextBtn')?.addEventListener('click', () => {
    nextSlide();
    startAutoplay();
  });

  document.getElementById('CascadePrevBtn')?.addEventListener('click', () => {
    prevSlide();
    startAutoplay();
  });

  cards.forEach((card, index) => {
    card.addEventListener('click', () => {
      currentIndex = index;
      updateCards();
      startAutoplay();
    });
  });

  updateCards();
  startAutoplay();
}



/* ==========================================================================
   BOOK QUICK-VIEW MODAL (MINI OVERVIEW MODAL)
   ========================================================================== */
window.openQuickView = function (bookData) {
  const backdrop = document.getElementById('quickViewBackdrop');
  const card = document.getElementById('quickViewCard');
  if (!backdrop || !card) return;

  let book = bookData;
  if (typeof bookData === 'string') {
    try {
      book = JSON.parse(bookData);
    } catch (e) {
      book = { title: bookData };
    }
  }

  // Populate metadata fields
  const elCover = document.getElementById('qvCover');
  const elBadge = document.getElementById('qvBadge');
  const elDiscount = document.getElementById('qvDiscountBadge');
  const elBinding = document.getElementById('qvBinding');
  const elTitle = document.getElementById('qvTitle');
  const elAuthor = document.getElementById('qvAuthor');
  const elPrice = document.getElementById('qvPrice');
  const elOriginal = document.getElementById('qvOriginal');
  const elRating = document.getElementById('qvRating');
  const elIsbn = document.getElementById('qvIsbn');
  const elPublisher = document.getElementById('qvPublisher');
  const elLanguage = document.getElementById('qvLanguage');
  const elPages = document.getElementById('qvPages');
  const elDesc = document.getElementById('qvDesc');
  const btnAddToCart = document.getElementById('qvAddToCartBtn');
  const btnWhatsApp = document.getElementById('qvWhatsAppBtn');

  if (elCover && book.cover) elCover.src = book.cover;
  if (elBadge) elBadge.innerText = book.badge || (book.discount ? book.discount : 'Curated Choice');
  if (elDiscount) {
    if (book.discount) {
      elDiscount.innerText = book.discount;
      elDiscount.style.display = 'inline-block';
    } else {
      elDiscount.style.display = 'none';
    }
  }
  if (elBinding) elBinding.innerText = book.binding || 'Paperback';
  if (elTitle) elTitle.innerText = book.title || 'Curated Book';
  if (elAuthor) elAuthor.innerText = book.author ? 'by ' + book.author : 'by Celebrated Author';
  if (elPrice) elPrice.innerText = book.price || '₹399.00';
  if (elOriginal) elOriginal.innerText = book.originalPrice || book.original || '';
  if (elRating && book.reviews) elRating.innerText = '4.9 (' + book.reviews + ' reviews)';
  if (elIsbn) elIsbn.innerText = book.isbn || '978-8193859214';
  if (elPublisher) elPublisher.innerText = book.publisher || 'Indigo Books India';
  if (elLanguage) elLanguage.innerText = book.language || 'Hindi / English';
  if (elPages) elPages.innerText = book.pages || '280 pp';
  if (elDesc) elDesc.innerText = book.desc || 'An acclaimed literary work available for express delivery across India with Cash on Delivery (COD) and 100% genuine publisher guarantee.';

  // Add to Cart handler inside quick view
  if (btnAddToCart) {
    btnAddToCart.onclick = function () {
      const drawer = document.getElementById('CartDrawer');
      const overlay = document.getElementById('CartDrawerOverlay');
      if (drawer && overlay) {
        closeQuickView();
        drawer.classList.add('active');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    };
  }

  // WhatsApp 1-Click Order handler inside quick view
  if (btnWhatsApp) {
    btnWhatsApp.onclick = function () {
      const title = book.title || 'Curated Book';
      const author = book.author || 'Author';
      const price = elPrice ? elPrice.innerText : '₹399.00';
      const binding = book.binding || 'Paperback';
      const msg = 'Hello Indigo Books! \nI want to order: *' + title + '*\nAuthor: ' + author + '\nPrice: ' + price + '\nBinding: ' + binding + '\nPlease confirm availability for COD delivery!';
      window.open('https://wa.me/918933063306?text=' + encodeURIComponent(msg), '_blank');
    };
  }

  // Show modal with smooth scale & opacity transition
  backdrop.classList.remove('opacity-0', 'pointer-events-none');
  backdrop.classList.add('opacity-100');
  card.classList.remove('scale-95');
  card.classList.add('scale-100');
  document.body.style.overflow = 'hidden';
};

window.closeQuickView = function () {
  const backdrop = document.getElementById('quickViewBackdrop');
  const card = document.getElementById('quickViewCard');
  if (!backdrop || !card) return;

  backdrop.classList.remove('opacity-100');
  backdrop.classList.add('opacity-0', 'pointer-events-none');
  card.classList.remove('scale-100');
  card.classList.add('scale-95');
  document.body.style.overflow = '';
};

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') closeQuickView();
});

document.addEventListener('click', function (e) {
  const backdrop = document.getElementById('quickViewBackdrop');
  if (e.target === backdrop) closeQuickView();
});


// ==========================================================================
// INDIGO BOOKS - 6 ARCHITECTURAL SECTIONS INTERACTIVE LOGIC
// ==========================================================================

// 1. 3D Curator's Podium Logic
const PODIUM_BESTSELLERS = [
  {
    id: "podium-1",
    title: "Diary of a Wimpy Kid: Hot Mess",
    author: "Jeff Kinney",
    price: 349,
    mrp: 499,
    save: "30% OFF",
    rating: "4.9 (420+)",
    rank: "#1 IN GLOBAL BESTSELLERS",
    stock: "38 copies left in Prayagraj",
    pages: "224 Pages • Hardcover • Puffin",
    publisher: "Puffin Books India",
    quote: "Hilarious, chaotic family road trips that resonate with readers of all generations worldwide."
  },
  {
    id: "podium-2",
    title: "Ujli Raaten (White Nights)",
    author: "Fyodor Dostoevsky",
    price: 299,
    mrp: 399,
    save: "25% OFF",
    rating: "4.8 (310+)",
    rank: "#1 IN TRANSLATED RUSSIAN CLASSICS",
    stock: "14 copies left in Prayagraj",
    pages: "112 Pages • Paperback • Penguin Classics",
    publisher: "Penguin Hindi Classics",
    quote: "A poetic, sentimental exploration of loneliness, love, and twilight reveries on the canals of St. Petersburg."
  },
  {
    id: "podium-3",
    title: "Kasaibada",
    author: "Manoj Rajan Tripathi",
    price: 299,
    mrp: 395,
    save: "24% OFF",
    rating: "4.9 (540+)",
    rank: "#1 IN CONTEMPORARY HINDI FICTION",
    stock: "22 copies left in Prayagraj",
    pages: "192 Pages • Paperback • Vani",
    publisher: "Vani Prakashan",
    quote: "A gripping social allegory on power structures, moral struggle, and raw human resilience in northern India."
  },
  {
    id: "podium-4",
    title: "Alchemised",
    author: "Contemporary Philosophy",
    price: 399,
    mrp: 550,
    save: "27% OFF",
    rating: "4.7 (190+)",
    rank: "#1 IN SPIRITUAL & THOUGHT",
    stock: "19 copies left in Prayagraj",
    pages: "256 Pages • Paperback • HarperCollins",
    publisher: "HarperCollins India",
    quote: "Transmuting personal adversity into enduring wisdom through timeless parables and deep introspective prose."
  },
  {
    id: "podium-5",
    title: "Ratan Tata: A Life",
    author: "Thomas Mathew",
    price: 699,
    mrp: 999,
    save: "30% OFF",
    rating: "5.0 (860+)",
    rank: "#1 IN BIOGRAPHIES & MEMOIRS",
    stock: "45 copies left in Prayagraj",
    pages: "544 Pages • Hardcover • HarperCollins",
    publisher: "HarperCollins India",
    quote: "The definitive authorized biography tracing the integrity, trials, and unparalleled vision of an Indian icon."
  }
];

let activePodiumIdx = 2;

function updatePodiumStageShopify() {
  const cards = document.querySelectorAll('.podium-book-card');
  if (!cards.length) return;
  const count = PODIUM_BESTSELLERS.length;

  cards.forEach((card, i) => {
    let offset = i - activePodiumIdx;
    if (offset < -2) offset += count;
    if (offset > 2) offset -= count;

    card.classList.remove('is-active');
    
    if (offset === 0) {
      card.classList.add('is-active');
      card.style.transform = 'translateX(0px) scale(1.15) rotateY(-8deg)';
      card.style.zIndex = '30';
      card.style.opacity = '1';
    } else if (offset === -1) {
      card.style.transform = 'translateX(-110px) scale(0.9) rotateY(22deg)';
      card.style.zIndex = '20';
      card.style.opacity = '0.85';
    } else if (offset === 1) {
      card.style.transform = 'translateX(110px) scale(0.9) rotateY(-22deg)';
      card.style.zIndex = '20';
      card.style.opacity = '0.85';
    } else if (offset <= -2) {
      card.style.transform = 'translateX(-210px) scale(0.75) rotateY(35deg)';
      card.style.zIndex = '10';
      card.style.opacity = '0.45';
    } else if (offset >= 2) {
      card.style.transform = 'translateX(210px) scale(0.75) rotateY(-35deg)';
      card.style.zIndex = '10';
      card.style.opacity = '0.45';
    }
  });

  const book = PODIUM_BESTSELLERS[activePodiumIdx];
  if (book) {
    const rankEl = document.getElementById('spotlightRank');
    const titleEl = document.getElementById('spotlightTitle');
    const authEl = document.getElementById('spotlightAuthor');
    const rateEl = document.getElementById('spotlightRating');
    const quoteEl = document.getElementById('spotlightQuote');
    const pagesEl = document.getElementById('spotlightPages');
    const pubEl = document.getElementById('spotlightPublisher');
    const priceEl = document.getElementById('spotlightPrice');
    const mrpEl = document.getElementById('spotlightMRP');
    const saveEl = document.getElementById('spotlightSave');
    const stockEl = document.getElementById('spotlightStock');
    const waEl = document.getElementById('spotlightWhatsAppBtn');

    if (rankEl) rankEl.innerText = book.rank;
    if (titleEl) titleEl.innerText = book.title;
    if (authEl) authEl.innerText = book.author;
    if (rateEl) rateEl.innerText = book.rating;
    if (quoteEl) quoteEl.innerText = `"${book.quote}"`;
    if (pagesEl) pagesEl.innerText = book.pages;
    if (pubEl) pubEl.innerText = book.publisher;
    if (priceEl) priceEl.innerText = `₹${book.price}.00`;
    if (mrpEl) mrpEl.innerText = `₹${book.mrp}.00`;
    if (saveEl) saveEl.innerText = book.save;
    if (stockEl) {
      stockEl.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span> ${book.stock}`;
    }
    if (waEl) {
      const waText = encodeURIComponent(`Hello Indigo Books, I want to order ${book.title} by ${book.author} at ₹${book.price}.`);
      waEl.href = `https://wa.me/918933063306?text=${waText}`;
    }
  }

  const dots = document.querySelectorAll('#podiumIndicators button');
  dots.forEach((dot, idx) => {
    if (idx === activePodiumIdx) {
      dot.className = 'w-7 h-2.5 rounded-full bg-[#D99B26] transition-all duration-300';
    } else {
      dot.className = 'w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300';
    }
  });
}

window.selectPodiumBook = function(index) {
  activePodiumIdx = index;
  updatePodiumStageShopify();
};

window.nextPodiumBook = function() {
  activePodiumIdx = (activePodiumIdx + 1) % PODIUM_BESTSELLERS.length;
  updatePodiumStageShopify();
};

window.prevPodiumBook = function() {
  activePodiumIdx = (activePodiumIdx - 1 + PODIUM_BESTSELLERS.length) % PODIUM_BESTSELLERS.length;
  updatePodiumStageShopify();
};

window.addCurrentPodiumToCart = function() {
  const book = PODIUM_BESTSELLERS[activePodiumIdx];
  if (book && typeof addToCart === 'function') {
    addToCart(book.id, book.title, book.price, '');
  }
};

// 2. Mehfil-e-Rekhta Poet Switcher
const POET_VERSES = {
  elia: {
    name: "Jaun Elia",
    pen: "क़तील-ए-अना",
    urdu: "شاید مجھے نکال کے پچھتا رہے ہوں آپ • محفل میں اس خیال سے پھر آ گیا ہوں میں",
    hindi: "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं",
    eng: "Perhaps you regret having cast me out; it is merely with this thought that I returned to the gathering."
  },
  faraz: {
    name: "Ahmad Faraz",
    pen: "शायर-ए-इश्क़",
    urdu: "رنجش ہی سہی دل ہی دکھانے کے لیے آ • آ پھر سے مجھے چھوڑ کے جانے کے لیے آ",
    hindi: "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ",
    eng: "Even if in resentment, come just to break my heart; come, if only to leave me once again."
  },
  manto: {
    name: "Saadat Hasan Manto",
    pen: "बागी अफ़सानानिगार",
    urdu: "اگر آپ میرے افسانوں کو برداشت نہیں کر سکتے، تو اس کا مطلب ہے کہ زمانہ ناقابل برداشت ہے",
    hindi: "अगर आप मेरे अफ़सानों को बर्दाश्त नहीं कर सकते, तो इसका मतलब है कि ज़माना नाक़ाबिले-बर्दाश्त है।",
    eng: "If you cannot bear my stories, it means the society we live in is unbearable."
  },
  ghalib: {
    name: "Mirza Ghalib",
    pen: "असद-उल्लाह ख़ान",
    urdu: "ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے • بہت نکلے مرے ارمان لیکن پھر بھی کم نکلے",
    hindi: "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले • बहुत निकले मिरे अरमान लेकिन फिर भी कम निकले",
    eng: "Thousands of desires, each one worth dying for; many were fulfilled, yet so many remain."
  }
};

window.selectPoetQuote = function(poetKey) {
  const q = POET_VERSES[poetKey];
  if (!q) return;

  const pills = document.querySelectorAll('#poetSelectorPills button');
  pills.forEach(p => {
    p.className = 'poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all';
  });
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.className = 'poet-pill active px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/50 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(217,155,38,0.3)] transition-all';
  }

  const urduEl = document.getElementById('poetUrduVerse');
  const hindiEl = document.getElementById('poetHindiVerse');
  const engEl = document.getElementById('poetEngVerse');
  const attrEl = document.getElementById('poetAttribution');

  if (urduEl) urduEl.style.opacity = '0';
  if (hindiEl) hindiEl.style.opacity = '0';
  if (engEl) engEl.style.opacity = '0';

  setTimeout(() => {
    if (urduEl) { urduEl.innerText = q.urdu; urduEl.style.opacity = '1'; }
    if (hindiEl) { hindiEl.innerText = `"${q.hindi}"`; hindiEl.style.opacity = '1'; }
    if (engEl) { engEl.innerText = q.eng; engEl.style.opacity = '1'; }
    if (attrEl) attrEl.innerText = `— ${q.name} (${q.pen})`;
  }, 200);
};

// 3. Vault Drawer Selector
window.selectVaultDrawer = function(drawerKey) {
  const buttons = document.querySelectorAll('#vaultDrawerTabs button');
  buttons.forEach(b => b.classList.remove('active'));
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.classList.add('active');
  }
};

// 4. Live Counters Observer
function initMarqueeCounters() {
  const counterElements = document.querySelectorAll('.live-counter');
  let animated = false;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animated = true;
        counterElements.forEach(el => {
          const target = parseInt(el.getAttribute('data-target') || '0', 10);
          const duration = 1500;
          const startTime = performance.now();

          function updateNumber(now) {
            const progress = Math.min((now - startTime) / duration, 1);
            const current = Math.floor(progress * target);
            el.innerText = current.toLocaleString('en-IN');
            if (progress < 1) {
              requestAnimationFrame(updateNumber);
            } else {
              el.innerText = target.toLocaleString('en-IN');
            }
          }
          requestAnimationFrame(updateNumber);
        });
      }
    });
  }, { threshold: 0.3 });

  const section = document.getElementById('literaryMarqueeSection');
  if (section) observer.observe(section);
}

document.addEventListener('DOMContentLoaded', () => {
  updatePodiumStageShopify();
  initMarqueeCounters();
});



// ==========================================================================
// INDIGO BOOKS - WIDE COVER OPEN & POET FILTERING LOGIC
// ==========================================================================
let isShopifyPodiumOpen = false;

window.togglePodiumCoverOpen = function() {
  isShopifyPodiumOpen = !isShopifyPodiumOpen;
  const activeCard = document.querySelector('.podium-book-card.is-active');
  const btnText = document.getElementById('flipCoverBtnText');
  if (activeCard) {
    if (isShopifyPodiumOpen) {
      activeCard.classList.add('is-open');
      if (btnText) btnText.innerText = "Cover Open (-140°) • Click to Close";
    } else {
      activeCard.classList.remove('is-open');
      if (btnText) btnText.innerText = "Hover or Click Book to Open Cover (-140°)";
    }
  }
};

window.filterMehfilPoet = function(poetKey) {
  const pills = document.querySelectorAll('#poetSelectorPills button');
  pills.forEach(p => {
    p.className = 'poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all font-sans';
  });
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.className = 'poet-pill active px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/50 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(217,155,38,0.3)] transition-all font-sans';
  }

  if (typeof POET_VERSES !== 'undefined') {
    const q = POET_VERSES[poetKey] || POET_VERSES['elia'];
    const urduEl = document.getElementById('poetUrduVerse');
    const hindiEl = document.getElementById('poetHindiVerse');
    const engEl = document.getElementById('poetEngVerse');
    const attrEl = document.getElementById('poetAttribution');

    if (urduEl && hindiEl && engEl && attrEl && q) {
      urduEl.style.opacity = '0';
      hindiEl.style.opacity = '0';
      engEl.style.opacity = '0';

      setTimeout(() => {
        urduEl.innerText = q.urdu;
        hindiEl.innerText = `"${q.hindi}"`;
        engEl.innerText = q.eng;
        attrEl.innerText = `— ${q.name} (${q.pen})`;

        urduEl.style.opacity = '1';
        hindiEl.style.opacity = '1';
        engEl.style.opacity = '1';
      }, 200);
    }
  }

  const cards = document.querySelectorAll('.rekhta-book-card');
  cards.forEach(card => {
    const cardPoet = card.getAttribute('data-poet');
    if (poetKey === 'all' || cardPoet === poetKey) {
      card.style.opacity = '1';
      card.style.transform = 'scale(1)';
      card.style.borderColor = (cardPoet === poetKey) ? '#F59E0B' : 'rgba(245, 158, 11, 0.2)';
      if (cardPoet === poetKey) {
        card.style.boxShadow = '0 0 25px rgba(217, 155, 38, 0.35)';
      } else {
        card.style.boxShadow = '';
      }
    } else {
      card.style.opacity = '0.35';
      card.style.transform = 'scale(0.96)';
      card.style.borderColor = 'rgba(255, 255, 255, 0.05)';
      card.style.boxShadow = '';
    }
  });
};



// Universal Mini Overview Toggle for all Book Cards
window.toggleMiniOverview = function(cardId, event) {
  if (event) event.stopPropagation();
  const drawer = document.getElementById('miniOverview-' + cardId);
  if (!drawer) return;
  if (drawer.classList.contains('hidden')) {
    drawer.classList.remove('hidden');
    drawer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  } else {
    drawer.classList.add('hidden');
  }
};

// First Page Excerpt Toggle
window.toggleExcerpt = function(cardId, event) {
  if (event) event.stopPropagation();
  const excerpt = document.getElementById('excerpt-' + cardId);
  if (!excerpt) return;
  if (excerpt.classList.contains('hidden')) {
    excerpt.classList.remove('hidden');
  } else {
    excerpt.classList.add('hidden');
  }
};


// MASTER BOOK DATABASE FOR THE "MINI OVERVIEW" POP-UP INFO BOX
const ALL_BOOKS_DATABASE = {
  // --- Hero Shelf Books ---
  'hero-0': {
    id: 'hero-0', title: 'Ujli Raaten (White Nights)', author: 'Fyodor Dostoevsky',
    price: 220, mrp: 299, discount: '26% OFF', category: 'World Classics',
    cover: 'assets/hero-book-ujli-raaten.jpg', reviews: '310+',
    about: 'The poignant sentimental story of a lonely dreamer in St. Petersburg and four magical white nights with Nastenka.',
    sig: 'One of the most celebrated lyrical short novels in Russian literature, translated into pristine Hindi.',
    reader: 'Lovers of classical romance, nocturnal introspection, and Saint Petersburg literary lore.',
    pages: '160 Pages', binding: 'Paperback', lang: 'Hindi / Russian', pub: 'Penguin Classics', isbn: '978-9388423106',
    excerpt: 'वह एक अद्भुत रात थी, ऐसी रात जो केवल जवानी के दिनों में ही नसीब हो सकती है। आकाश तारों से इतना भरा था कि उसे देखकर बरबस यह पूछने का मन होता था कि क्या इतने तारों भरे आसमान के नीचे भी दुखी और क्रोधी लोग रह सकते हैं?'
  },
  'hero-1': {
    id: 'hero-1', title: 'दोज़ख़नामा (Dozakhnama)', author: 'Rabisankar Bal',
    price: 649, mrp: 749, discount: '13% OFF', category: 'Literary Historical',
    cover: 'assets/hero-book-dozakh.jpg', reviews: '295+',
    about: 'A transcendental conversation in hell between Mirza Ghalib and Saadat Hasan Manto speaking from their graves.',
    sig: 'Landmark cross-border historical masterpiece bridging Lucknow, Delhi, and Lahore.',
    reader: 'Admirers of Delhi history, Urdu poetry, literary biographies, and Manto-Ghalib lore.',
    pages: '528 Pages', binding: 'Hardcover', lang: 'Hindi Translation', pub: 'Penguin Vintage', isbn: '978-8184003055',
    excerpt: 'कब्र की मिट्टी जब बोलती है, तो इतिहास अपनी गलती स्वीकार करता है। ग़ालिब और मंटो के बीच की यह दास्तान सदियों का दर्द समेटे है...'
  },
  'hero-2': {
    id: 'hero-2', title: 'ठंडा गोश्त (Thanda Gosht)', author: 'Saadat Hasan Manto',
    price: 200, mrp: 249, discount: '20% OFF', category: 'Partition Realism',
    cover: 'assets/hero-book-thanda-ghost.jpg', reviews: '480+',
    about: 'Unflinching, masterfully crafted short stories dissecting human psychology and communal madness during Partition.',
    sig: 'Manto\'s most controversial and celebrated literary court-trial piece, defining modern South Asian realism.',
    reader: 'Students of psychoanalysis, modern Indian history, and fearless progressive writing.',
    pages: '160 Pages', binding: 'Paperback', lang: 'Hindi / Urdu', pub: 'Rekhta Publications', isbn: '978-9350293112',
    excerpt: 'ईश्वर सिंह जब होटल के कमरे में दाखिल हुआ, तो उसके चेहरे पर एक अजीब सी वहशत थी। कुलवंत कौर ने उसकी तरफ देखा और समझ गई कि कुछ अनहोनी हो चुकी है...'
  },
  'hero-3': {
    id: 'hero-3', title: 'कसाईबाड़ा (Kasaibada)', author: 'Manoj Rajan Tripathi',
    price: 299, mrp: 395, discount: '24% OFF', category: 'Hindi Contemporary',
    cover: 'assets/hero-book-kasaibada.jpg', reviews: '540+',
    about: 'A gripping social allegory on rural power structures, journalistic integrity, and human resilience in northern India.',
    sig: 'Widely discussed and enacted contemporary Hindi literary masterpiece with multiple reprints.',
    reader: 'Readers of gripping rural realism, social thrillers, and award-winning northern fiction.',
    pages: '210 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Vani Prakashan', isbn: '978-9390315895',
    excerpt: 'जब व्यवस्था खुद कसाई बन जाए, तो न्याय की गुहार लगाने वाला भी संदिग्ध हो जाता है। कसाईबाड़े की दीवारें हर उस चीख की गवाह हैं जो सत्ता के कानों तक कभी नहीं पहुंची...'
  },
  'hero-4': {
    id: 'hero-4', title: 'धुआँ (Dhuaan)', author: 'Saadat Hasan Manto',
    price: 200, mrp: 249, discount: '20% OFF', category: 'Urdu Literature',
    cover: 'assets/hero-book-dhuaan.jpg', reviews: '367+',
    about: 'Raw, evocative tales of adolescence, taboo human desires, and unspoken psychological truths.',
    sig: 'A brilliant demonstration of Manto\'s psychoanalytical prowess that challenged colonial obscenity laws.',
    reader: 'Psychology scholars, short story writers, and classic progressive literature enthusiasts.',
    pages: '176 Pages', binding: 'Paperback', lang: 'Hindi / Urdu', pub: 'Rekhta Publications', isbn: '978-9350293129',
    excerpt: 'धुआँ केवल सिगरेट से नहीं निकलता, इंसान के भीतर सुलगती तमन्नाएँ जब घुटती हैं, तो रूह से भी धुआँ उठता है...'
  },
  'hero-5': {
    id: 'hero-5', title: 'Arundhati Roy (1998-2016)', author: 'Arundhati Roy',
    price: 595, mrp: 799, discount: '25% OFF', category: 'Essays & Dissent',
    cover: 'assets/hero-book-arundhati.jpg', reviews: '290+',
    about: 'An expansive collection of Arundhati Roy\'s visionary political essays, speeches, and meditations on democracy.',
    sig: 'From the Booker-winning author of The God of Small Things, articulating two decades of grassroots resistance.',
    reader: 'Scholars of political ecology, social justice, and high literary non-fiction.',
    pages: '440 Pages', binding: 'Paperback Deluxe', lang: 'Hindi', pub: 'Rajkamal Prakashan', isbn: '978-8126732907',
    excerpt: 'लोकतंत्र जब केवल चुनावों का तमाशा बनकर रह जाता है, तब सबसे दबे-कुचले लोगों की आवाज सुनने के लिए साहित्य को ही आगे आना पड़ता है...'
  },

  // --- Curator Podium Books ---
  'podium-0': {
    id: 'podium-0', title: 'Diary of a Wimpy Kid: Fight or Flight', author: 'Jeff Kinney',
    price: 349, mrp: 499, discount: '30% OFF', category: 'Children & YA Bestseller',
    cover: 'assets/hero-book-wimpy-kid.jpg', reviews: '420+',
    about: 'Greg Heffley faces uproarious family vacation disasters, airport security chaos, and airborne misadventures.',
    sig: 'The global #1 children\'s publishing phenomenon with over 275 million copies sold globally.',
    reader: 'School students, young readers, and families seeking hearty, hilarious reading.',
    pages: '224 Pages', binding: 'Hardcover', lang: 'English', pub: 'Puffin Books India', isbn: '978-0141385679',
    excerpt: 'First of all, let me get something straight: this is a JOURNAL, not a diary. The other thing I want to clear up right away is that this was MUM\'s idea, not mine...'
  },
  'podium-1': {
    id: 'podium-1', title: 'Ujli Raaten (White Nights)', author: 'Fyodor Dostoevsky',
    price: 220, mrp: 299, discount: '26% OFF', category: 'World Classics',
    cover: 'assets/hero-book-ujli-raaten.jpg', reviews: '310+',
    about: 'The poignant sentimental story of a lonely dreamer in St. Petersburg and four magical white nights with Nastenka.',
    sig: 'One of the most celebrated lyrical short novels in Russian literature, translated into pristine Hindi.',
    reader: 'Lovers of classical romance, nocturnal introspection, and Saint Petersburg literary lore.',
    pages: '160 Pages', binding: 'Paperback', lang: 'Hindi / Russian', pub: 'Penguin Classics', isbn: '978-9388423106',
    excerpt: 'वह एक अद्भुत रात थी, ऐसी रात जो केवल जवानी के दिनों में ही नसीब हो सकती है। आकाश तारों से इतना भरा था कि उसे देखकर बरबस यह पूछने का मन होता था...'
  },
  'podium-2': {
    id: 'podium-2', title: 'कसाईबाड़ा (Kasaibada)', author: 'Manoj Rajan Tripathi',
    price: 299, mrp: 395, discount: '24% OFF', category: 'Hindi Contemporary',
    cover: 'assets/hero-book-kasaibada.jpg', reviews: '540+',
    about: 'A gripping social allegory on rural power structures, journalistic integrity, and human resilience in northern India.',
    sig: 'Widely discussed and enacted contemporary Hindi literary masterpiece with multiple reprints.',
    reader: 'Readers of gripping rural realism, social thrillers, and award-winning northern fiction.',
    pages: '210 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Vani Prakashan', isbn: '978-9390315895',
    excerpt: 'जब व्यवस्था खुद कसाई बन जाए, तो न्याय की गुहार लगाने वाला भी संदिग्ध हो जाता है। कसाईबाड़े की दीवारें हर उस चीख की गवाह हैं...'
  },
  'podium-3': {
    id: 'podium-3', title: 'The Masnavi: Teachings of Rumi', author: 'Maryam Mafi',
    price: 399, mrp: 499, discount: '20% OFF', category: 'Sufi Poetry & Philosophy',
    cover: 'assets/hero-book-rumi.png', reviews: '215+',
    about: 'The sublime spiritual verses and profound allegories of Jalal al-Din Rumi beautifully translated for modern seekers.',
    sig: 'Often revered as the Persian Quran in verse, exploring divine love, detachment, and human consciousness.',
    reader: 'Seekers of spiritual wisdom, poetry lovers, and meditation practitioners.',
    pages: '304 Pages', binding: 'Hardcover', lang: 'English', pub: 'Rider Books', isbn: '978-1846045585',
    excerpt: 'Do not grieve. Anything you lose comes round in another form. The wound is the place where the Light enters you...'
  },
  'podium-4': {
    id: 'podium-4', title: 'Best of Haruki Murakami', author: 'Haruki Murakami',
    price: 1259, mrp: 1799, discount: '30% OFF', category: 'Contemporary World Fiction',
    cover: 'assets/hero-book-murakami.jpg', reviews: '875+',
    about: 'A collector\'s set comprising Norwegian Wood, Kafka on the Shore, and The Wind-Up Bird Chronicle.',
    sig: 'The defining trio of novels that placed modern Japanese magical realism on global bestseller lists.',
    reader: 'Literary fiction lovers, university students, and admirers of surreal urban narratives.',
    pages: '980 Pages', binding: 'Paperback 3-Set', lang: 'English', pub: 'Vintage Classics', isbn: '978-0099511649',
    excerpt: 'Memories warm you up from the inside. But they also tear you apart. If you only read the books that everyone else is reading, you can only think what everyone else is thinking...'
  },

  // --- Mehfil-e-Rekhta Books ---
  'mehfil-1': {
    id: 'mehfil-1', title: 'क्यों (Kyon)', author: 'Jaun Elia',
    price: 350, mrp: 450, discount: '22% OFF', category: 'Urdu Poetry / Rekhta',
    cover: 'assets/book-kyon-jaun-elia.jpg', reviews: '421+',
    about: 'An intimate anthology of Jaun Elia\'s most piercing ghazals on existential longing, heartbreak, and rebellion.',
    sig: 'The seminal collection that redefined modern Urdu shayari across the entire subcontinent.',
    reader: 'Poetry lovers, ghazal enthusiasts, and students of Urdu literature and philosophy.',
    pages: '280 Pages', binding: 'Hardcover', lang: 'Urdu / Hindi', pub: 'Rekhta Publications', isbn: '978-8193859214',
    excerpt: 'शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं...'
  },
  'mehfil-2': {
    id: 'mehfil-2', title: 'रंजिश ही सही (Ranjish Hi Sahi)', author: 'Ahmad Faraz',
    price: 399, mrp: 499, discount: '20% OFF', category: 'Urdu Poetry / Ghazals',
    cover: 'assets/book-ranjish-hi-sahi.jpg', reviews: '310+',
    about: 'Timeless Urdu romantic poetry celebrating love, separation, melancholy, and resilient revolutionary spirit.',
    sig: 'One of the most recited and recorded ghazal collections in South Asian history.',
    reader: 'Lovers of melody, verse, and profound romantic literature.',
    pages: '320 Pages', binding: 'Hardcover', lang: 'Urdu / Hindi', pub: 'Vani Prakashan', isbn: '978-8193859221',
    excerpt: 'रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ...'
  },
  'mehfil-3': {
    id: 'mehfil-3', title: 'दोज़ख़नामा (Dozakhnama)', author: 'Rabisankar Bal',
    price: 649, mrp: 749, discount: '13% OFF', category: 'Historical Fiction',
    cover: 'assets/hero-book-dozakh.jpg', reviews: '295+',
    about: 'A posthumous conversation between Mirza Ghalib and Saadat Hasan Manto speaking from their graves.',
    sig: 'Cross-border literary masterpiece bridging Lucknow, Delhi, and Lahore.',
    reader: 'Readers of historical fiction, Delhi\'s bygone culture, and literary biographies.',
    pages: '528 Pages', binding: 'Hardcover', lang: 'Hindi Translation', pub: 'Penguin Vintage', isbn: '978-8184003055',
    excerpt: 'कब्र की मिट्टी जब बोलती है, तो इतिहास अपनी गलती स्वीकार करता है...'
  },
  'mehfil-4': {
    id: 'mehfil-4', title: 'ठंडा गोश्त (Thanda Gosht)', author: 'Saadat Hasan Manto',
    price: 200, mrp: 249, discount: '20% OFF', category: 'Partition Realism',
    cover: 'assets/hero-book-thanda-ghost.jpg', reviews: '480+',
    about: 'Unflinching, masterfully crafted short stories dissecting human psychology during Partition.',
    sig: 'Manto\'s most controversial and celebrated literary court-trial piece.',
    reader: 'Fans of fearless progressive writing and realism.',
    pages: '160 Pages', binding: 'Paperback', lang: 'Hindi / Urdu', pub: 'Rekhta Publications', isbn: '978-9350293112',
    excerpt: 'ईश्वर सिंह जब होटल के कमरे में दाखिल हुआ, तो उसके चेहरे पर एक अजीब सी वहशत थी...'
  },
  'mehfil-5': {
    id: 'mehfil-5', title: 'धुआँ (Dhuaan)', author: 'Saadat Hasan Manto',
    price: 200, mrp: 249, discount: '20% OFF', category: 'Urdu Literature',
    cover: 'assets/hero-book-dhuaan.jpg', reviews: '367+',
    about: 'Raw, evocative tales of adolescence, society, and unspoken human truths.',
    sig: 'A brilliant demonstration of Manto\'s psychoanalytical storytelling.',
    reader: 'Students of psychoanalysis, short story writers, and classic literature lovers.',
    pages: '176 Pages', binding: 'Paperback', lang: 'Hindi / Urdu', pub: 'Rekhta Publications', isbn: '978-9350293129',
    excerpt: 'धुआँ केवल सिगरेट से नहीं निकलता, इंसान के भीतर सुलगती तमन्नाएँ जब घुटती हैं, तो रूह से भी धुआँ उठता है...'
  },

  // --- Indian Voices / Regional Fiction ---
  'ind-hero': {
    id: 'ind-hero', title: 'चीलवाली कोठी (Cheelwali Kothi)', author: 'Sara Rai',
    price: 299, mrp: 395, discount: '24% OFF', category: 'Hindi Literature',
    cover: 'assets/book-cheelwali-kothi.jpg', reviews: '142+',
    about: 'A haunting poetic novel on aristocratic mansions, lost family memories, and quiet human dignity in Uttar Pradesh.',
    sig: 'Authored by the granddaughter of Munshi Premchand, carrying forward India\'s purest prose tradition.',
    reader: 'Admirers of atmospheric literary prose, family chronicles, and high Hindi literature.',
    pages: '248 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Rajkamal Prakashan', isbn: '978-8126731023',
    excerpt: 'हवेली के ऊंचे दालानों में चीलों की छाया जब ढलती धूप के साथ फैलती, तो ऐसा लगता मानो समय वहीं ठहर गया हो...'
  },
  'ind-1': {
    id: 'ind-1', title: 'नर-नारीश्वर (Nar-Nareeshwar)', author: 'Vishnu Prabhakar',
    price: 320, mrp: 425, discount: '25% OFF', category: 'Sahitya Akademi Classic',
    cover: 'assets/book-nar-nareeshwar.jpg', reviews: '230+',
    about: 'A monumental exploration of gender duality, psychology, and spiritual synthesis in Indian society.',
    sig: 'Conferred the prestigious Sahitya Akademi Award and Bharatiya Jnanpith recognition.',
    reader: 'Discerning readers of deep Hindi psychological fiction and philosophical literature.',
    pages: '524 Pages', binding: 'Hardcover', lang: 'Hindi', pub: 'Radhakrishna Prakashan', isbn: '978-0143444851',
    excerpt: 'पुरुष में नारी और नारी में पुरुष का अस्तित्व केवल जैविक नहीं, चेतना का सनातन सत्य है...'
  },
  'ind-2': {
    id: 'ind-2', title: 'पत्थर और अलपत्थर', author: 'Surendra Verma',
    price: 240, mrp: 300, discount: '20% OFF', category: 'Modern Hindi Theatre',
    cover: 'assets/book-patthar-alpatthar.jpg', reviews: '185+',
    about: 'A razor-sharp satirical drama questioning institutional dogma, personal vanity, and human compromise.',
    sig: 'Performed across premier national theatre festivals with thunderous critical acclaim.',
    reader: 'Theatre aficionados, Hindi drama scholars, and cultural critics.',
    pages: '184 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Radhakrishna Prakashan', isbn: '978-8171192348',
    excerpt: 'पत्थर पर जब शब्द उकेरे जाते हैं, तो इतिहास बनता है; लेकिन जब पत्थर को ही पूजने की होड़ लग जाए, तो विवेक मौन हो जाता है...'
  },
  'ind-3': {
    id: 'ind-3', title: 'औरत फ़रोश', author: 'Kanhaiyalal Nandan',
    price: 280, mrp: 360, discount: '22% OFF', category: 'Social Realism',
    cover: 'assets/book-aurat-farosh.jpg', reviews: '210+',
    about: 'A searing social critique unveiling trafficking, urban hypocrisy, and the resilience of womanhood.',
    sig: 'Authored by one of modern Hindi journalism and literature\'s most fearless voices.',
    reader: 'Readers engaged in social journalism, progressive women\'s studies, and realism.',
    pages: '210 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Rajpal & Sons', isbn: '978-8170289123',
    excerpt: 'महानगरों की चकाचौंध के पीछे जो अंधेरी गलियां हैं, वहां सांस लेना भी एक जद्दोजहद है...'
  },
  'ind-4': {
    id: 'ind-4', title: 'लगभग सिंगल', author: 'Divya Prakash Dubey',
    price: 195, mrp: 240, discount: '18% OFF', category: 'Nai Wali Hindi',
    cover: 'assets/book-lagbhag-single.jpg', reviews: '620+',
    about: 'Relatable, warm, and witty contemporary stories exploring love, modern career dilemmas, and loneliness in India.',
    sig: 'The vanguard text of \'Nai Wali Hindi\' making literature accessible to youth nationwide.',
    reader: 'College students, young professionals, and fans of brisk urban Hindi storytelling.',
    pages: '160 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Hind Yugm', isbn: '978-9387464018',
    excerpt: 'जिंदगी में कुछ लोग सिर्फ इसलिए खास नहीं होते कि वे आपके साथ हैं, बल्कि इसलिए कि उनके बिना कोई और खास नहीं लगता...'
  },

  // --- Academic Vault & Law Books ---
  'law-1': {
    id: 'law-1', title: 'Modi Medical Jurisprudence & Toxicology', author: 'Kannan & K. Mathiharan',
    price: 1850, mrp: 2195, discount: '15% OFF', category: 'LexisNexis Law',
    cover: 'assets/book-medical-jurisprudence.jpg', reviews: '310+',
    about: 'The definitive encyclopaedia on forensic medicine, post-mortem pathology, and Indian judicial evidence.',
    sig: 'The undisputed legal standard cited across High Courts and Supreme Court of India.',
    reader: 'High Court advocates, judicial magistrates, forensic surgeons, and criminal law scholars.',
    pages: '1,480 Pages', binding: 'Hardcover Deluxe', lang: 'English', pub: 'LexisNexis Butterworths', isbn: '978-9390529810',
    excerpt: 'Medical Jurisprudence is that branch of science which applies medical and scientific knowledge to legal determinations...'
  },
  'law-2': {
    id: 'law-2', title: 'Lawful Awful: Life in Law & Courtrooms', author: 'Justice Venkataswami',
    price: 450, mrp: 599, discount: '25% OFF', category: 'Penguin Law Memoir',
    cover: 'assets/book-lawful-awful.jpg', reviews: '260+',
    about: 'Witty, sharp, and illuminating courtroom memoirs dissecting constitutional battles and human folly.',
    sig: 'A beloved contemporary memoir by a distinguished Supreme Court justice.',
    reader: 'Law students, junior litigators, judges, and avid biography readers.',
    pages: '310 Pages', binding: 'Hardcover', lang: 'English', pub: 'Penguin Law', isbn: '978-9357021456',
    excerpt: 'The law is often described as an ass; but those who ride it every morning know it requires both stubborn patience and a sense of humour...'
  },
  'law-3': {
    id: 'law-3', title: '१० फ़ैसले जिन्होंने देश बदल दिया', author: 'Zia Mody',
    price: 320, mrp: 395, discount: '20% OFF', category: 'Constitutional History',
    cover: 'assets/book-10-faisle.jpg', reviews: '490+',
    about: 'Deep analysis of 10 landmark Supreme Court verdicts from Kesavananda Bharati to Maneka Gandhi in accessible Hindi.',
    sig: 'The definitive guide to India\'s living constitution and basic structure doctrine.',
    reader: 'UPSC & State PCS aspirants, legal novices, journalists, and civic activists.',
    pages: '232 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Prabhat Prakashan', isbn: '978-9390315482',
    excerpt: 'सर्वोच्च न्यायालय के फैसले केवल कानूनी दस्तावेज नहीं होते, वे एक संप्रभु राष्ट्र की आत्मा का दर्पण होते हैं...'
  },
  'law-4': {
    id: 'law-4', title: 'The Bench, The Bar & The Bizarre', author: 'Tushar Mehta',
    price: 1995, mrp: 2490, discount: '20% OFF', category: 'Rupa Legal 2-Set',
    cover: 'assets/book-bench-bar.jpg', reviews: '180+',
    about: 'A captivating 2-book set exploring courtroom humour, judicial eccentricities, and profound legal turning points.',
    sig: 'Intimate reflections from the Solicitor General of India offering unprecedented insights into jurisprudence.',
    reader: 'Legal professionals, law historians, and observers of the Indian judicial system.',
    pages: '640 Pages', binding: 'Hardcover 2-Set', lang: 'English', pub: 'Rupa Legal', isbn: '978-9357022804',
    excerpt: 'Between the solemn gravity of constitutional arguments and the final gavel of justice lie countless moments of sheer human absurdity...'
  },

  // --- Catalog Directory Books ---
  'cat-1': {
    id: 'cat-1', title: 'चीलवाली कोठी (Cheelwali Kothi)', author: 'Sara Rai',
    price: 299, mrp: 395, discount: '24% OFF', category: 'fiction',
    cover: 'assets/book-cheelwali-kothi.jpg', reviews: '142+',
    about: 'A haunting poetic novel on aristocratic mansions, ancestral memory, and quiet human dignity in Uttar Pradesh.',
    sig: 'Winner of major literary laurels, crafted by the granddaughter of Premchand and daughter of Sripat Rai.',
    reader: 'Admirers of atmospheric literary prose, family chronicles, and high Hindi literature.',
    pages: '248 Pages', binding: 'Paperback', lang: 'Hindi', pub: 'Rajkamal Prakashan', isbn: '978-8126731023',
    excerpt: 'हवेली के ऊंचे दालानों में चीलों की छाया जब ढलती धूप के साथ फैलती, तो ऐसा लगता मानो समय वहीं ठहर गया हो...'
  },
  'cat-2': {
    id: 'cat-2', title: 'Diary of a Wimpy Kid: Fight or Flight', author: 'Jeff Kinney',
    price: 349, mrp: 499, discount: '30% OFF', category: 'bestsellers',
    cover: 'assets/hero-book-wimpy-kid.jpg', reviews: '420+',
    about: 'Greg Heffley faces uproarious family vacation disasters, airport blunders, and chaotic airborne misadventures.',
    sig: 'The global #1 children\'s and YA phenomenon with over 275 million copies in print worldwide.',
    reader: 'Young readers, school students, and anyone looking for hearty, hilarious family reading.',
    pages: '224 Pages', binding: 'Hardcover', lang: 'English', pub: 'Puffin Books India', isbn: '978-0141385679',
    excerpt: 'First of all, let me get something straight: this is a JOURNAL, not a diary. And airport security is definitely not my thing...'
  },
  'cat-3': {
    id: 'cat-3', title: 'क्यों (Kyon)', author: 'Jaun Elia',
    price: 350, mrp: 450, discount: '22% OFF', category: 'rekhta',
    cover: 'assets/book-kyon-jaun-elia.jpg', reviews: '421+',
    about: 'An intimate anthology of Jaun Elia\'s most piercing ghazals on existential longing, heartbreak, and rebellion.',
    sig: 'The seminal collection that redefined modern Urdu shayari across the entire subcontinent.',
    reader: 'Poetry lovers, ghazal enthusiasts, and students of Urdu literature and philosophy.',
    pages: '280 Pages', binding: 'Hardcover', lang: 'Urdu / Hindi', pub: 'Rekhta Publications', isbn: '978-8193859214',
    excerpt: 'शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं...'
  },
  'cat-4': {
    id: 'cat-4', title: 'Modi Medical Jurisprudence', author: 'Kannan & Mathiharan',
    price: 1850, mrp: 2195, discount: '15% OFF', category: 'law',
    cover: 'assets/book-medical-jurisprudence.jpg', reviews: '310+',
    about: 'The definitive encyclopaedia on forensic medicine, post-mortem pathology, and Indian judicial evidence.',
    sig: 'The undisputed legal standard cited across High Courts and Supreme Court of India.',
    reader: 'High Court advocates, judicial magistrates, forensic surgeons, and criminal law scholars.',
    pages: '1,480 Pages', binding: 'Hardcover Deluxe', lang: 'English', pub: 'LexisNexis Butterworths', isbn: '978-9390529810',
    excerpt: 'Medical Jurisprudence is that branch of science which applies medical and scientific knowledge to legal determinations...'
  },

  // --- Bundles ---
  'bundle-1': {
    id: 'bundle-1', title: 'Arundhati Roy Definitive Duo Boxset', author: 'Arundhati Roy',
    price: 799, mrp: 1198, discount: '33% OFF', category: 'Collector Slipcase',
    cover: 'assets/hero-book-arundhati.jpg', reviews: '380+',
    about: 'Complete 2-volume box set pairing The God of Small Things (Silver Jubilee Edition) with The Ministry of Utmost Happiness.',
    sig: 'Man Booker Prize triumph celebrating thirty years of Roy\'s incandescent prose.',
    reader: 'Collectors of contemporary masterpieces, fiction devotees, and gift shoppers.',
    pages: '780 Pages', binding: 'Hardcover Box Set', lang: 'English', pub: 'Penguin Vintage', isbn: '978-0143445678',
    excerpt: 'May in Ayemenem is a hot, brooding month. The river shrinks and black crows gorge on bright mangoes in still, dustgreen trees...'
  },
  'bundle-2': {
    id: 'bundle-2', title: 'A Court of Thorns and Roses (5-Book Boxset)', author: 'Sarah J. Maas',
    price: 2199, mrp: 3299, discount: '33% OFF', category: 'Fantasy Box Set',
    cover: 'assets/book-acotar.jpg', reviews: '1120+',
    about: 'The entire BookTok fantasy phenomenon following Feyre Archeron across the treacherous faerie courts of Prythian.',
    sig: 'Global #1 New York Times bestselling romantic fantasy saga with over 35 million copies sold.',
    reader: 'YA fantasy readers, high-fantasy lovers, and lovers of grand worldbuilding.',
    pages: '2,100 Pages', binding: 'Paperback Boxset', lang: 'English', pub: 'Bloomsbury', isbn: '978-1526626585',
    excerpt: 'The forest had become a labyrinth of snow and ice. I had been monitoring our dwindling food supplies for days...'
  },
  'bundle-3': {
    id: 'bundle-3', title: 'Best of Haruki Murakami (3-Book Set)', author: 'Haruki Murakami',
    price: 1259, mrp: 1799, discount: '30% OFF', category: 'Vintage Classics',
    cover: 'assets/hero-book-murakami.jpg', reviews: '875+',
    about: 'Norwegian Wood, Kafka on the Shore, and The Wind-Up Bird Chronicle in uniform vintage design.',
    sig: 'The definitive triumvirate of magical realist fiction by Japan\'s most influential contemporary author.',
    reader: 'College students, surrealist fiction readers, and collectors of modern classics.',
    pages: '980 Pages', binding: 'Paperback 3-Set', lang: 'English', pub: 'Vintage Classics', isbn: '978-0099511649',
    excerpt: 'Memories warm you up from the inside. But they also tear you apart...'
  }
};

let currentMoBook = null;

// UNIVERSAL FUNCTION: Open the "Mini Overview" Pop-Up Info Box
window.openMiniOverview = function(bookDataOrId, event) {
  if (event) event.stopPropagation();

  let book = null;
  if (typeof bookDataOrId === 'string') {
    if (bookDataOrId.trim().startsWith('{')) {
      try { book = JSON.parse(bookDataOrId); } catch(e) {}
    }
    if (!book) {
      book = ALL_BOOKS_DATABASE[bookDataOrId];
    }
    if (!book && typeof BOOKS !== 'undefined') {
      const found = BOOKS.find(b => b.id === bookDataOrId);
      if (found) {
        book = {
          id: found.id, title: found.title, author: found.author,
          price: found.price, mrp: found.originalPrice || (found.price + 100),
          discount: found.discount || '20% OFF', category: found.category || 'Featured Collection',
          cover: found.cover || found.image, reviews: `${found.reviews || 150}+ verified readers`,
          about: found.desc || 'A masterfully written literary work capturing readers nationwide with profound storytelling.',
          sig: 'Highly acclaimed work published with authentic typographical elegance.',
          reader: 'Literary enthusiasts, students, and general readers seeking exceptional books.',
          pages: found.pages || '280 Pages', binding: found.binding || 'Paperback',
          lang: found.language || 'Hindi / English', pub: found.publisher || 'Indigo Books',
          isbn: found.isbn || '978-8193859214',
          excerpt: found.quote || 'This book opens a gateway to timeless reflections, human warmth, and unforgettable truths...'
        };
      }
    }
  } else if (typeof bookDataOrId === 'object' && bookDataOrId !== null) {
    book = bookDataOrId;
  }

  // Fallback defaults if still null
  if (!book) {
    book = {
      id: 'general', title: 'Selected Literary Classic', author: 'Indigo Books Curations',
      price: 299, mrp: 395, discount: '24% OFF', category: 'Handpicked Read',
      cover: 'assets/hero-book-dozakh.jpg', reviews: '320+ verified readers',
      about: 'A handpicked classic from the Prayagraj literary archives of Indigo Books India.',
      sig: 'Authentic verified edition with publisher quality guarantee.',
      reader: 'Discerning readers of Indian and world literature.',
      pages: '240 Pages', binding: 'Paperback', lang: 'Hindi / English', pub: 'Indigo Books India',
      isbn: '978-8193859214',
      excerpt: 'हर किताब अपने साथ एक पूरी दुनिया लेकर आती है। जब आप पहला पन्ना पलटते हैं, तो यात्रा शुरू होती है...'
    };
  }

  currentMoBook = book;

  // Populate Pop-Up Modal elements
  const elCover = document.getElementById('moCover');
  const elDiscount = document.getElementById('moDiscountBadge');
  const elCategory = document.getElementById('moCategoryBadge');
  const elReviews = document.getElementById('moReviews');
  const elTitle = document.getElementById('moTitle');
  const elAuthor = document.getElementById('moAuthor');
  const elPrice = document.getElementById('moPrice');
  const elMrp = document.getElementById('moMrp');
  const elSave = document.getElementById('moSave');
  const elAbout = document.getElementById('moAbout');
  const elSig = document.getElementById('moSignificance');
  const elReader = document.getElementById('moReader');
  const elPages = document.getElementById('moPages');
  const elBinding = document.getElementById('moBinding');
  const elLang = document.getElementById('moLanguage');
  const elPub = document.getElementById('moPublisher');
  const elIsbn = document.getElementById('moIsbn');
  const elExcerptText = document.getElementById('moExcerptText');
  const elWhatsAppBtn = document.getElementById('moWhatsAppBtn');

  if (elCover) elCover.src = book.cover || book.image || 'assets/hero-book-dozakh.jpg';
  if (elDiscount) elDiscount.textContent = book.discount || '20% OFF';
  if (elCategory) elCategory.textContent = book.category || 'Curated Book';
  if (elReviews) elReviews.textContent = `(${book.reviews || '350+'} verified readers)`;
  if (elTitle) elTitle.textContent = book.title;
  if (elAuthor) elAuthor.textContent = `By ${book.author} • ${book.pub || book.publisher || 'Indigo Books'}`;
  
  const numPrice = typeof book.price === 'number' ? book.price : parseInt(String(book.price).replace(/[^0-9]/g, '')) || 299;
  const numMrp = typeof book.mrp === 'number' ? book.mrp : parseInt(String(book.mrp || book.originalPrice || (numPrice * 1.3)).replace(/[^0-9]/g, '')) || (numPrice + 100);
  const diff = numMrp - numPrice;

  if (elPrice) elPrice.textContent = `₹${numPrice}.00`;
  if (elMrp) elMrp.textContent = `₹${numMrp}.00`;
  if (elSave) elSave.textContent = `Save ₹${diff > 0 ? diff : 96} (${book.discount || '20% OFF'})`;

  if (elAbout) elAbout.textContent = book.about || book.desc || 'A celebrated literary masterpiece from the Prayagraj collection.';
  if (elSig) elSig.textContent = book.sig || 'A landmark work loved by readers and recognized across institutions.';
  if (elReader) elReader.textContent = book.reader || 'Readers of serious fiction, students, and literature connoisseurs.';

  if (elPages) elPages.textContent = book.pages || '240 Pages';
  if (elBinding) elBinding.textContent = book.binding || 'Paperback';
  if (elLang) elLang.textContent = book.lang || book.language || 'Hindi';
  if (elPub) elPub.textContent = book.pub || book.publisher || 'Indigo Books India';
  if (elIsbn) elIsbn.textContent = book.isbn || '978-8193859214';

  if (elExcerptText) elExcerptText.textContent = `"${book.excerpt || 'पहला पन्ना पलटते ही कहानी अपनी पूरी शिद्दत के साथ सामने आ खड़ी होती है...'}"`;

  // WhatsApp Order Link
  if (elWhatsAppBtn) {
    const safeTitle = encodeURIComponent(book.title.replace(/['"]/g, ''));
    elWhatsAppBtn.href = `https://wa.me/918933063306?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20the%20book%20*${safeTitle}*%20at%20%E2%82%B9${numPrice}.%20Please%20confirm%20COD%20availability!`;
  }

  // Reset Excerpt and Pincode
  const excerptBox = document.getElementById('moExcerptBox');
  const excerptArrow = document.getElementById('moExcerptArrow');
  if (excerptBox) excerptBox.classList.add('hidden');
  if (excerptArrow) excerptArrow.textContent = '▾';
  const pinRes = document.getElementById('moPincodeResult');
  if (pinRes) pinRes.classList.add('hidden');

  // Display Pop-Up Modal
  const modal = document.getElementById('miniOverviewModal');
  const box = document.getElementById('miniOverviewBox');
  if (modal && box) {
    modal.classList.remove('pointer-events-none', 'opacity-0');
    modal.classList.add('opacity-100', 'is-open', 'active');
    modal.style.display = 'flex';
    modal.style.opacity = '1';
    modal.style.pointerEvents = 'auto';
    box.classList.remove('scale-95');
    box.classList.add('scale-100');
    box.style.transform = 'scale(1)';
    document.body.style.overflow = 'hidden';
  }
};

// Universal Close Modal
window.closeMiniOverview = function() {
  const modal = document.getElementById('miniOverviewModal');
  const box = document.getElementById('miniOverviewBox');
  if (modal && box) {
    modal.classList.remove('opacity-100', 'is-open', 'active');
    modal.classList.add('opacity-0', 'pointer-events-none');
    modal.style.display = 'none';
    modal.style.opacity = '0';
    modal.style.pointerEvents = 'none';
    box.classList.remove('scale-100');
    box.classList.add('scale-95');
    box.style.transform = 'scale(0.95)';
    document.body.style.overflow = '';
  }
};

// Aliases for compatibility
window.openQuickView = window.openMiniOverview;
window.closeQuickView = window.closeMiniOverview;
window.toggleMiniOverview = function(cardId, event) {
  window.openMiniOverview(cardId, event);
};

// Toggle Excerpt inside Pop-Up
window.toggleMoExcerpt = function() {
  const box = document.getElementById('moExcerptBox');
  const arrow = document.getElementById('moExcerptArrow');
  if (!box) return;
  if (box.classList.contains('hidden')) {
    box.classList.remove('hidden');
    if (arrow) arrow.textContent = '▴';
  } else {
    box.classList.add('hidden');
    if (arrow) arrow.textContent = '▾';
  }
};

// Pincode Delivery Check
window.checkMoPincode = function() {
  const input = document.getElementById('moPincodeInput');
  const result = document.getElementById('moPincodeResult');
  if (!input || !result) return;
  const pin = input.value.trim();
  if (/^[1-9][0-9]{5}$/.test(pin)) {
    result.className = 'text-[11px] mt-1 font-bold text-emerald-700 block';
    result.textContent = ` Express Delivery & Cash on Delivery Available to Pincode ${pin}! (Dispatches in 24 hrs)`;
  } else {
    result.className = 'text-[11px] mt-1 font-bold text-rose-600 block';
    result.textContent = 'Please enter a valid 6-digit Indian Postal Pincode.';
  }
};

// Add Current Book to Cart from Modal
window.addCurrentMoBookToCart = function() {
  if (!currentMoBook) return;
  const numPrice = typeof currentMoBook.price === 'number' ? currentMoBook.price : parseInt(String(currentMoBook.price).replace(/[^0-9]/g, '')) || 299;
  if (typeof addToCart === 'function') {
    addToCart(currentMoBook.id, currentMoBook.title, numPrice, currentMoBook.cover);
  }
  closeMiniOverview();
};

// Escape Key to Close
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    closeMiniOverview();
  }
});

// =========================================================================
// MEHFIL-E-REKHTA DYNAMIC SHAYARI SWITCHER & INTERACTIVE READER ENGINE
// =========================================================================
const POET_SHAYARI_DATA = {
  'all': {
    name: "Mehfil-e-Rekhta Anthology",
    pen: "मुंतख़ब कलाम (ग़ालिब • जौन • फ़राज़ • मंटो)",
    couplets: [
      {
        urdu: "ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے • بہت نکلے مرے ارمان لیکن پھر بھی کم نکلے",
        hindi: "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले • बहुत निकले मिरे अरमान लेकिन फिर भी कम निकले",
        eng: "Thousands of desires, each worth dying for; many of my longings were fulfilled, yet still they felt too few.",
        attr: "— MIRZA GHALIB (दीवान-ए-ग़ालिब)"
      },
      {
        urdu: "شاید مجھے نکال کے پچھتا رہے ہوں آپ • محفل میں اس خیال سے پھر آ گیا ہوں میں",
        hindi: "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं",
        eng: "Perhaps you regret having cast me out; it is merely with this thought that I returned to the gathering.",
        attr: "— JAUN ELIA (शायद)"
      },
      {
        urdu: "رنجش ہی سہی دل ہی دکھانے کے لیے آ • آ پھر سے مجھے چھوڑ کے جانے کے لیے آ",
        hindi: "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ",
        eng: "Even if out of bitterness, come just to break my heart; come, even if only to abandon me all over again.",
        attr: "— AHMAD FARAZ (दर्द-ए-आशूफ़्ता)"
      }
    ],
    fullNazm: [
      "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले • बहुत निकले मिरे अरमान लेकिन फिर भी कम निकले",
      "निकलना ख़ुल्द से आदम का सुनते आए हैं लेकिन • बहुत बे-आबरू होकर तिरे कूचे से हम निकले",
      "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं",
      "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ"
    ],
    bookTarget: 'mehfil-1'
  },
  'elia': {
    name: "Jaun Elia",
    pen: "क़तील-ए-अना • कामिल कलाम",
    couplets: [
      {
        urdu: "شاید مجھے نکال کے پچھتا رہے ہوں آپ • محفل میں اس خیال سے پھر آ گیا ہوں میں",
        hindi: "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं",
        eng: "Perhaps you regret having cast me out; it is merely with this thought that I returned to the gathering.",
        attr: "— JAUN ELIA (क़तील-ए-अना • कामिल कलाम)"
      },
      {
        urdu: "کتنی دلکش ہو تم کتنا دل جو ہوں میں • کیا ستم ہے کہ ہم لوگ مر جائیں گے",
        hindi: "कितनी दिलकश हो तुम कितना दिल-जू हूँ मैं • क्या सितम है कि हम लोग मर जाएँगे",
        eng: "How utterly enchanting you are, how passionately devoted I am; what tragic cruelty it is that we both must one day die.",
        attr: "— JAUN ELIA (यानी)"
      },
      {
        urdu: "جو گزاری نہ جا سکی ہم سے • ہم نے وہ زندگی گزاری ہے",
        hindi: "जो गुज़ारी न जा सकी हम से • हम ने वो ज़िंदगी गुज़ारी है",
        eng: "That very life which could never be endured—that is the life we have lived.",
        attr: "— JAUN ELIA (गुमान)"
      }
    ],
    fullNazm: [
      "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं",
      "कितनी दिलकश हो तुम कितना दिल-जू हूँ मैं • क्या सितम है कि हम लोग मर जाएँगे",
      "जो गुज़ारी न जा सकी हम से • हम ने वो ज़िंदगी गुज़ारी है",
      "मैं भी बहुत अजीब हूँ इतना अजीब हूँ कि बस • ख़ुद को तबाह कर लिया और मलाल भी नहीं"
    ],
    bookTarget: 'mehfil-1'
  },
  'faraz': {
    name: "Ahmad Faraz",
    pen: "रंजिश ही सही • दर्द-ए-आशूफ़्ता",
    couplets: [
      {
        urdu: "رنجش ہی سہی دل ہی دکھانے کے لیے آ • آ پھر سے مجھے چھوڑ کے جانے کے لیے آ",
        hindi: "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ",
        eng: "Even if out of bitterness, come just to break my heart; come, even if only to abandon me all over again.",
        attr: "— AHMAD FARAZ (रंजिश ही सही • दर्द-ए-आशूफ़्ता)"
      },
      {
        urdu: "اب کے ہم بچھڑے تو شاید کبھی خوابوں میں ملیں • جس طرح سوکھے ہوئے پھول کتابوں میں ملیں",
        hindi: "अब के हम बिछड़े तो शायद कभी ख़्वाबों में मिलें • जिस तरह सूखे हुए फूल किताबों में मिलें",
        eng: "If we part now, perhaps we will meet only in dreams; like withered blossoms pressed between the pages of old books.",
        attr: "— AHMAD FARAZ (नायाफ़्त)"
      },
      {
        urdu: "سنا ہے لوگ اسے آنکھ بھر کے دیکھتے ہیں • سو اس کے شہر میں کچھ دن قیام کر کے دیکھیں",
        hindi: "सुना है लोग उसे आँख भर के देखते हैं • सो उस के शहर में कुछ दिन क़ियाम कर के देखें",
        eng: "I have heard that people gaze upon her in breathless wonder; let us linger for a few days in her city and see for ourselves.",
        attr: "— AHMAD FARAZ (जानाँ जानाँ)"
      }
    ],
    fullNazm: [
      "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ",
      "पहले से मरासिम न सही फिर भी कभी तो • रस्म-ओ-रह-ए-दुनिया ही निभाने के लिए आ",
      "अब के हम बिछड़े तो शायद कभी ख़्वाबों में मिलें • जिस तरह सूखे हुए फूल किताबों में मिलें",
      "सुना है लोग उसे आँख भर के देखते हैं • सो उस के शहर में कुछ दिन क़ियाम कर के देखें"
    ],
    bookTarget: 'mehfil-2'
  },
  'manto': {
    name: "Saadat Hasan Manto",
    pen: "ठंडा गोश्त • सियाह हाशिए",
    couplets: [
      {
        urdu: "اگر آپ میرے افسانے برداشت نہیں کر سکتے تو اس کا مطلب ہے کہ یہ زمانہ ہی ناقابلِ برداشت ہے",
        hindi: "अगर आप मेरे अफ़साने बर्दाश्त नहीं कर सकते, तो इसका मतलब है कि यह ज़माना ही नाक़ाबिल-ए-बर्दाश्त है।",
        eng: "If you cannot bear my stories, it is because the times we live in are unbearable. My writing is merely a mirror to society.",
        attr: "— SAADAT HASAN MANTO (ठंडा गोश्त • सियाह हाशिए)"
      },
      {
        urdu: "ادھر خاردار تاروں کے پیچھے ہندوستان تھا اور ادھر ویسے ہی تاروں کے پیچھے پاکستان۔ درمیان میں زمین کے اس ٹکڑے پر جس کا کوئی نام نہیں تھا، ٹوبہ ٹیک سنگھ پڑا تھا",
        hindi: "उधर ख़ारदार तारों के पीछे हिंदुस्तान था और इधर वैसे ही तारों के पीछे पाकिस्तान। दरमियान में ज़मीन के उस टुकड़े पर जिसका कोई नाम नहीं था, टोबा टेक सिंह पड़ा था।",
        eng: "There, behind barbed wire, lay India; here, behind identical wire, lay Pakistan. In between, upon a nameless stretch of dirt, lay Toba Tek Singh.",
        attr: "— SAADAT HASAN MANTO (टोबा टेक सिंह)"
      },
      {
        urdu: "مجھ پر فحاشی کا الزام لگانے والو! اگر تم سچائی کو ننگا دیکھ کر شرماتے ہو تو اپنے کپڑے اتار کر خود کو دیکھو",
        hindi: "मुझ पर अश्लीलता का इल्ज़ाम लगाने वालो! अगर तुम सच्चाई को नंगा देखकर शरमाते हो, तो अपने गिरेबान में झांक कर देखो।",
        eng: "Those who accuse me of obscenity! If you blush seeing truth unclad, look into the mirror of your own conscience.",
        attr: "— SAADAT HASAN MANTO (दस्तावेज़)"
      }
    ],
    fullNazm: [
      "अगर आप मेरे अफ़साने बर्दाश्त नहीं कर सकते, तो इसका मतलब है कि यह ज़माना ही नाक़ाबिल-ए-बर्दाश्त है।",
      "टोबा टेक सिंह: उधर ख़ारदार तारों के पीछे हिंदुस्तान था और इधर वैसे ही तारों के पीछे पाकिस्तान। दरमियान में ज़मीन के उस टुकड़े पर जिसका कोई नाम नहीं था, टोबा टेक सिंह पड़ा था।",
      "धुआँ: धुआँ केवल सिगरेट से नहीं निकलता, इंसान के भीतर सुलगती तमन्नाएँ जब घुटती हैं, तो रूह से भी धुआँ उठता है।",
      "साआदत हसन मर सकता है, मगर 'मंटो' कभी नहीं मरेगा, क्योंकि जब तक समाज में पाखंड ज़िंदा है, मंटो की क़लम ज़िंदा रहेगी।"
    ],
    bookTarget: 'mehfil-4'
  },
  'ghalib': {
    name: "Mirza Ghalib",
    pen: "दीवान-ए-ग़ालिब • दोज़ख़नामा",
    couplets: [
      {
        urdu: "ہم کو معلوم ہے جنت کی حقیقت لیکن • دل کے خوش رکھنے کو غالب یہ خیال اچھا ہے",
        hindi: "हम को मालूम है जन्नत की हक़ीक़त लेकिन • दिल के ख़ुश रखने को 'ग़ालिब' ये ख़याल अच्छा है",
        eng: "We know the reality of paradise all too well, O Ghalib; yet to keep the heart content, it is a lovely illusion.",
        attr: "— MIRZA GHALIB (दीवान-ए-ग़ालिब • दोज़ख़नामा)"
      },
      {
        urdu: "عشق پر زور نہیں ہے یہ وہ آتش غالب • کہ لگائے نہ لگے اور بجھائے نہ بجھے",
        hindi: "इश्क़ पर ज़ोर नहीं है ये वो आतिश 'ग़ालिब' • कि लगाए न लगे और बुझाए न बुझे",
        eng: "Love answers to no command, O Ghalib; it is that fire which cannot be ignited by force, nor extinguished when ablaze.",
        attr: "— MIRZA GHALIB (नुस्ख़ा-ए-हमीदिया)"
      },
      {
        urdu: "ہیں اور بھی دنیا میں سخن ور بہت اچھے • کہتے ہیں کہ غالب کا ہے اندازِ بیاں اور",
        hindi: "हैं और भी दुनिया में सुख़न-वर बहुत अच्छे • कहते हैं कि 'ग़ालिब' का है अंदाज़-ए-बयाँ और",
        eng: "There are countless eloquent poets in this world; yet everyone agrees that Ghalib's poetic style is in a realm of its own.",
        attr: "— MIRZA GHALIB (मख़दूम)"
      }
    ],
    fullNazm: [
      "हम को मालूम है जन्नत की हक़ीक़त लेकिन • दिल के ख़ुश रखने को 'ग़ालिब' ये ख़याल अच्छा है",
      "इश्क़ पर ज़ोर नहीं है ये वो आतिश 'ग़ालिब' • कि लगाए न लगे और बुझाए न बुझे",
      "हैं और भी दुनिया में सुख़न-वर बहुत अच्छे • कहते हैं कि 'ग़ालिब' का है अंदाज़-ए-बयाँ और",
      "दर्द मिन्नत-कश-ए-दवा न हुआ • मैं न अच्छा हुआ बुरा न हुआ"
    ],
    bookTarget: 'mehfil-3'
  }
};

let currentActivePoet = 'all';
let currentSherIndex = 0;

// Universal Filter Function for Poet Tabs
window.filterMehfilPoet = function(poetKey) {
  if (!POET_SHAYARI_DATA[poetKey]) poetKey = 'all';
  currentActivePoet = poetKey;
  currentSherIndex = 0;

  // 1. Update Tab Pills Styling
  const pills = document.querySelectorAll('#poetSelectorPills .poet-pill');
  pills.forEach(p => {
    if (p.getAttribute('data-poet-tab') === poetKey) {
      p.className = 'poet-pill active px-4 py-2 rounded-full text-xs font-bold tracking-wide border border-amber-500/60 bg-amber-500/25 text-amber-100 shadow-[0_0_20px_rgba(217,155,38,0.4)] transition-all font-sans cursor-pointer hover:scale-105 active:scale-95';
    } else {
      p.className = 'poet-pill px-4 py-2 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/80 hover:bg-white/10 hover:text-amber-100 transition-all font-sans cursor-pointer hover:scale-105 active:scale-95';
    }
  });

  // 2. Render Couplet into Quote Box with smooth crossfade
  renderCurrentCouplet();

  // 3. Highlight / Filter Matching Rekhta Book Cards Below
  filterRekhtaCards(poetKey);
};

// Cycle through couplets using Prev / Next
window.cyclePoetSher = function(direction) {
  const data = POET_SHAYARI_DATA[currentActivePoet];
  if (!data || !data.couplets.length) return;

  currentSherIndex = (currentSherIndex + direction + data.couplets.length) % data.couplets.length;
  renderCurrentCouplet();
};

function renderCurrentCouplet() {
  const data = POET_SHAYARI_DATA[currentActivePoet];
  if (!data) return;
  const couplet = data.couplets[currentSherIndex] || data.couplets[0];

  const urduEl = document.getElementById('poetUrduVerse');
  const hindiEl = document.getElementById('poetHindiVerse');
  const engEl = document.getElementById('poetEngVerse');
  const attrEl = document.getElementById('poetAttribution');
  const badgeEl = document.getElementById('sherCounterBadge');

  if (urduEl && hindiEl && engEl && attrEl) {
    urduEl.style.opacity = '0';
    hindiEl.style.opacity = '0';
    engEl.style.opacity = '0';

    setTimeout(() => {
      urduEl.textContent = couplet.urdu;
      hindiEl.textContent = `"${couplet.hindi}"`;
      engEl.textContent = couplet.eng;
      attrEl.textContent = couplet.attr;
      if (badgeEl) badgeEl.textContent = `Couplet ${currentSherIndex + 1} of ${data.couplets.length}`;

      urduEl.style.opacity = '1';
      hindiEl.style.opacity = '1';
      engEl.style.opacity = '1';
    }, 180);
  }

  // Update reader panel if already open
  updateReaderPanel();
}

// Toggle Full Reader Panel
window.toggleShayariReader = function() {
  const panel = document.getElementById('fullShayariReaderPanel');
  const toggleBtnText = document.getElementById('readerToggleText');
  if (!panel) return;

  if (panel.classList.contains('hidden')) {
    panel.classList.remove('hidden');
    if (toggleBtnText) toggleBtnText.textContent = 'Close Full Reader ▴';
    updateReaderPanel();
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  } else {
    panel.classList.add('hidden');
    if (toggleBtnText) toggleBtnText.textContent = 'Read Full Ghazal / Excerpt';
  }
};

function updateReaderPanel() {
  const data = POET_SHAYARI_DATA[currentActivePoet];
  if (!data) return;

  const titleEl = document.getElementById('readerPoetTitle');
  const subEl = document.getElementById('readerPoetSubtitle');
  const listEl = document.getElementById('readerCoupletsList');

  if (titleEl) titleEl.textContent = data.name;
  if (subEl) subEl.textContent = data.pen;

  if (listEl) {
    listEl.innerHTML = data.fullNazm.map((line, idx) => `
      <div class="p-2.5 rounded-lg ${idx % 2 === 0 ? 'bg-white/[0.04]' : 'bg-transparent'} border-l-2 border-amber-400/40">
        <p class="font-serif text-amber-100 text-sm sm:text-base leading-relaxed">"${line}"</p>
      </div>
    `).join('');
  }
}

// Copy Current Shayari to Clipboard
window.copyCurrentShayari = function() {
  const data = POET_SHAYARI_DATA[currentActivePoet];
  if (!data) return;
  const couplet = data.couplets[currentSherIndex] || data.couplets[0];

  const fullText = `${couplet.urdu}\n${couplet.hindi}\n"${couplet.eng}"\n${couplet.attr}\n— Indigo Books India (https://www.indigobooksindia.com/)`;

  if (navigator.clipboard) {
    navigator.clipboard.writeText(fullText).then(() => {
      const btn = document.getElementById('copyBtnLabel');
      if (btn) {
        btn.textContent = ' Copied!';
        setTimeout(() => { btn.textContent = 'Copy Shayari'; }, 2200);
      }
    });
  }
};

// Scroll down to the matching poet book card
window.scrollToPoetBook = function() {
  const data = POET_SHAYARI_DATA[currentActivePoet];
  const targetId = data ? data.bookTarget : 'rekhtaCardsContainer';
  const el = document.getElementById(targetId) || document.getElementById('rekhtaCardsContainer');
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
};

// Select poet from a book card and open sample shayari
window.selectPoetAndReadShayari = function(poetKey, event) {
  if (event) event.stopPropagation();
  filterMehfilPoet(poetKey);
  const quoteCard = document.getElementById('poetQuoteCard');
  if (quoteCard) {
    quoteCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
  const panel = document.getElementById('fullShayariReaderPanel');
  if (panel && panel.classList.contains('hidden')) {
    toggleShayariReader();
  }
};

// Filter / Highlight book cards below
function filterRekhtaCards(poetKey) {
  const cards = document.querySelectorAll('#rekhtaCardsContainer .rekhta-book-card');
  cards.forEach(card => {
    const poets = (card.getAttribute('data-poet') || '').split(' ');
    if (poetKey === 'all') {
      card.style.opacity = '1';
      card.style.filter = 'none';
      card.style.transform = 'none';
      card.classList.remove('border-amber-400', 'shadow-[0_0_30px_rgba(217,155,38,0.5)]');
      card.classList.add('border-amber-500/20');
    } else if (poets.includes(poetKey)) {
      card.style.opacity = '1';
      card.style.filter = 'none';
      card.style.transform = 'scale(1.03)';
      card.classList.remove('border-amber-500/20');
      card.classList.add('border-amber-400', 'shadow-[0_0_30px_rgba(217,155,38,0.5)]');
    } else {
      card.style.opacity = '0.35';
      card.style.filter = 'blur(0.5px)';
      card.style.transform = 'scale(0.96)';
      card.classList.remove('border-amber-400', 'shadow-[0_0_30px_rgba(217,155,38,0.5)]');
      card.classList.add('border-amber-500/20');
    }
  });
}

// =========================================================================
// CURATOR'S PODIUM PURE VANILLA JS CONTROLLER
// 100% Synchronous state management between #podium-3d-book and spotlight panel
// =========================================================================
const PODIUM_DATA = [
  {
    id: 'podium-0',
    title: 'Diary of a Wimpy Kid: Fight or Flight',
    author: 'Jeff Kinney',
    rank: '#1 IN CHILDREN FICTION',
    rating: '4.8 (890+ reviews)',
    quote: '"First of all, let me get something straight: this is a JOURNAL, not a diary. The hilarious misadventures of Greg Heffley continue."',
    excerpt: '"First of all, let me get something straight: this is a JOURNAL, not a diary. I know what it says on the cover, but when Mom went out to buy this thing I specifically told her to get one that didn\'t say \'diary\' on it."',
    pages: '224 Pages • Hardcover',
    publisher: 'Puffin Books',
    price: '₹399.00',
    mrp: '₹499.00',
    save: '20% OFF',
    discountBadge: '20% OFF',
    stock: '18 copies in Prayagraj',
    cover: 'hero-book-wimpy-kid.jpg',
    chapter: 'Chapter 1'
  },
  {
    id: 'podium-1',
    title: 'उजली रातें (Ujli Raaten)',
    author: 'Fyodor Dostoevsky',
    rank: '#2 IN CLASSIC TRANSLATIONS',
    rating: '4.9 (420+ reviews)',
    quote: '"सेंट पीटर्सबर्ग की जादुई रातों में एक भावुक स्वप्नद्रष्टा और एकाकी स्त्री की आत्मा को छू लेने वाली अमर प्रेम कथा।"',
    excerpt: '"वह एक अद्भुत रात थी, ऐसी रात जो केवल जवानी के दिनों में ही नसीब हो सकती है। आकाश तारों से भरा था, इतना चमकता हुआ कि उसे देखकर मन अपने-आप पूछ बैठता था—क्या ऐसे आसमान के नीचे भी उदास लोग रह सकते हैं?"',
    pages: '160 Pages • Paperback',
    publisher: 'Penguin Classics',
    price: '₹220.00',
    mrp: '₹299.00',
    save: '26% OFF',
    discountBadge: '26% OFF',
    stock: '35 copies in Prayagraj',
    cover: 'hero-book-ujli-raaten.jpg',
    chapter: 'पहला प्रहर / Night One'
  },
  {
    id: 'podium-2',
    title: 'कसाईबाड़ा (Kasaibada)',
    author: 'Manoj Rajan Tripathi',
    rank: '#1 IN CONTEMPORARY HINDI FICTION',
    rating: '4.9 (540+ reviews)',
    quote: '"A gripping social allegory on rural power structures, journalistic integrity, and human resilience in northern India."',
    excerpt: '"शहर की तंग गलियों में जहाँ सत्ता और संघर्ष की दास्तान हर दीवार पर लिखी थी, वहाँ इंसानियत की एक नई कहानी जन्म ले रही थी। सत्ता, व्यवस्था और आत्मसम्मान की जद्दोजहद..."',
    pages: '192 Pages • Paperback',
    publisher: 'Vani Prakashan',
    price: '₹299.00',
    mrp: '₹395.00',
    save: '24% OFF',
    discountBadge: '24% OFF',
    stock: '22 copies in Prayagraj',
    cover: 'hero-book-kasaibada.jpg',
    chapter: 'अध्याय १ • First Page Preview'
  },
  {
    id: 'podium-3',
    title: 'The Masnavi: Rumi',
    author: 'Maryam Mafi',
    rank: '#1 IN SPIRITUAL CLASSICS',
    rating: '5.0 (610+ reviews)',
    quote: '"The timeless spiritual poetry and divine allegories of Jalal al-Din Rumi beautifully translated for modern seekers."',
    excerpt: '"Listen to the reed as it tells its tale, complaining of separation: \'Ever since I was parted from the reed-bed, my lament has caused men and women to weep. Anyone who is left far from his origin longs for the day he is reunited.\'"',
    pages: '304 Pages • Hardcover',
    publisher: 'Rider Books',
    price: '₹399.00',
    mrp: '₹499.00',
    save: '20% OFF',
    discountBadge: '20% OFF',
    stock: '14 copies in Prayagraj',
    cover: 'hero-book-rumi.png',
    chapter: 'Book 1 • Prologue'
  },
  {
    id: 'podium-4',
    title: 'The Best of Haruki Murakami',
    author: 'Haruki Murakami',
    rank: '#1 IN GLOBAL CONTEMPORARY',
    rating: '4.9 (780+ reviews)',
    quote: '"An intoxicating exploration of surrealism, urban loneliness, jazz rhythms, and metaphysical mysteries."',
    excerpt: '"I was thirty-seven then, strapped in my seat as the huge 747 plunged through dense cloud on its way into Hamburg airport. Cold November rain drenched the airfield, turning it into a gloomy Flemish painting..."',
    pages: '980 Pages • 3-Book Set',
    publisher: 'Vintage Classics',
    price: '₹1,299.00',
    mrp: '₹1,799.00',
    save: '28% OFF',
    discountBadge: '28% OFF',
    stock: '12 sets in Prayagraj',
    cover: 'hero-book-murakami.jpg',
    chapter: 'Norwegian Wood • Ch. 1'
  }
];

let currentPodiumIndex = 2; // Default to Center Book (Kasaibada)

function getAssetUrl(filename) {
  if (typeof window.ShopifyAssetBaseUrl !== 'undefined') {
    return window.ShopifyAssetBaseUrl + filename;
  }
  return 'assets/' + filename;
}

function selectPodiumBook(index) {
  if (index < 0 || index >= PODIUM_DATA.length) return;
  currentPodiumIndex = index;
  const book = PODIUM_DATA[index];

  // 1. Update 3D Book Cover & Inside Page
  const elCoverImg = document.getElementById('podium-cover-img');
  const elPageTitle = document.getElementById('podium-page-title');
  const elPageExcerpt = document.getElementById('podium-page-excerpt');
  const el3dBook = document.getElementById('podium-3d-book');

  if (elCoverImg) {
    elCoverImg.src = getAssetUrl(book.cover);
    elCoverImg.alt = book.title;
  }
  if (elPageTitle) elPageTitle.textContent = book.title;
  if (elPageExcerpt) elPageExcerpt.textContent = book.excerpt;

  // Reset cover open state when changing books
  if (el3dBook) el3dBook.classList.remove('is-open');

  // 2. Update Flanking Books Around Active Index
  const slotIndices = [
    (index + 3) % 5, // Far left
    (index + 4) % 5, // Near left
    (index + 1) % 5, // Near right
    (index + 2) % 5  // Far right
  ];

  const elFlank0 = document.getElementById('flankImg0');
  const elFlank1 = document.getElementById('flankImg1');
  const elFlank3 = document.getElementById('flankImg3');
  const elFlank4 = document.getElementById('flankImg4');

  if (elFlank0) elFlank0.src = getAssetUrl(PODIUM_DATA[slotIndices[0]].cover);
  if (elFlank1) elFlank1.src = getAssetUrl(PODIUM_DATA[slotIndices[1]].cover);
  if (elFlank3) elFlank3.src = getAssetUrl(PODIUM_DATA[slotIndices[2]].cover);
  if (elFlank4) elFlank4.src = getAssetUrl(PODIUM_DATA[slotIndices[3]].cover);

  // 3. Update Indicator Dots
  const dots = document.querySelectorAll('.podium-dot');
  dots.forEach((dot, i) => {
    if (i === index) {
      dot.className = 'podium-dot active w-7 h-2.5 rounded-full bg-[#D99B26] transition-all duration-300 cursor-pointer';
    } else {
      dot.className = 'podium-dot w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300 cursor-pointer';
    }
  });

  // 4. Update Right Spotlight Panel
  const elRank = document.getElementById('spotlightRank');
  const elStock = document.getElementById('spotlightStock');
  const elTitle = document.getElementById('spotlightTitle');
  const elAuthor = document.getElementById('spotlightAuthor');
  const elRating = document.getElementById('spotlightRating');
  const elQuote = document.getElementById('spotlightQuote');
  const elPages = document.getElementById('spotlightPages');
  const elPub = document.getElementById('spotlightPublisher');
  const elPrice = document.getElementById('spotlightPrice');
  const elMRP = document.getElementById('spotlightMRP');
  const elSave = document.getElementById('spotlightSave');
  const elWABtn = document.getElementById('spotlightWhatsAppBtn');

  if (elRank) elRank.textContent = book.rank;
  if (elStock) elStock.innerHTML = '<span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span><span>' + book.stock + '</span>';
  if (elTitle) elTitle.textContent = book.title;
  if (elAuthor) elAuthor.textContent = book.author;
  if (elRating) elRating.textContent = book.rating;
  if (elQuote) elQuote.textContent = book.quote;
  if (elPages) elPages.textContent = book.pages;
  if (elPub) elPub.textContent = book.publisher;
  if (elPrice) elPrice.textContent = book.price;
  if (elMRP) elMRP.textContent = book.mrp;
  if (elSave) elSave.textContent = book.save;

  if (elWABtn) {
    const rawPrice = book.price.replace(/[^0-9.]/g, '');
    const cleanNum = '918933063306';
    const waMsg = 'Hello Indigo Books Prayagraj! \nI would like to order: *' + book.title + '*\nAuthor: ' + book.author + '\nPrice: ' + book.price + '\nPlease confirm availability and share COD delivery details!';
    elWABtn.href = 'https://wa.me/' + cleanNum + '?text=' + encodeURIComponent(waMsg);
  }
}

function selectPodiumBookByFlank(slotPosition) {
  if (slotPosition === 0) selectPodiumBook((currentPodiumIndex + 3) % 5);
  else if (slotPosition === 1) selectPodiumBook((currentPodiumIndex + 4) % 5);
  else if (slotPosition === 3) selectPodiumBook((currentPodiumIndex + 1) % 5);
  else if (slotPosition === 4) selectPodiumBook((currentPodiumIndex + 2) % 5);
}

function prevPodiumBook() {
  const nextIdx = (currentPodiumIndex - 1 + PODIUM_DATA.length) % PODIUM_DATA.length;
  selectPodiumBook(nextIdx);
}

function nextPodiumBook() {
  const nextIdx = (currentPodiumIndex + 1) % PODIUM_DATA.length;
  selectPodiumBook(nextIdx);
}

function addCurrentPodiumToCart() {
  const book = PODIUM_DATA[currentPodiumIndex];
  if (typeof addToCart === 'function') {
    addToCart(book.id, 1);
  } else {
    const drawer = document.getElementById('CartDrawer');
    const overlay = document.getElementById('CartDrawerOverlay');
    if (drawer && overlay) {
      drawer.classList.add('active');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }
}

// Auto-run on load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => selectPodiumBook(2));
} else {
  selectPodiumBook(2);
}
window.addEventListener('load', () => selectPodiumBook(2));
document.addEventListener('shopify:section:load', () => selectPodiumBook(2));
document.addEventListener('shopify:section:select', () => selectPodiumBook(2));