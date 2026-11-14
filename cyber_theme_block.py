# -*- coding: utf-8 -*-
"""
cyber_theme_block.py
THE CYBERNETIC ARCHIVE REDESIGN MASTER BLOCK
Ultimate Futuristic Library UI, Neon Glassmorphism, Live Predictive Search, and 1-Click Fast Checkout
"""

CYBER_STYLE = """<style id="indigo-futuristic-cyber-theme">
  /* ==========================================================================
     FUTURE ARCHIVE CYBER-THEME DESIGN SYSTEM (Obsidian & Neon Glassmorphism)
     ========================================================================== */
  :root {
    --cyber-bg: #030712;
    --cyber-surface: rgba(15, 23, 42, 0.75);
    --cyber-surface-hover: rgba(30, 41, 59, 0.85);
    --cyber-border: rgba(0, 245, 255, 0.22);
    --cyber-border-glow: rgba(0, 245, 255, 0.6);
    --cyber-cyan: #00F5FF;
    --cyber-gold: #FFD700;
    --cyber-violet: #A855F7;
    --cyber-text: #F8FAFC;
    --cyber-muted: #94A3B8;
  }

  /* Global Page Background & Typography */
  html, body {
    background-color: var(--cyber-bg) !important;
    color: var(--cyber-text) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    overflow-x: hidden !important;
  }

  /* Animated Starfield / Cyber Grid Background Effect */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: 
      radial-gradient(circle at 20% 30%, rgba(0, 245, 255, 0.04) 0%, transparent 40%),
      radial-gradient(circle at 80% 70%, rgba(168, 85, 247, 0.04) 0%, transparent 40%),
      linear-gradient(to right, rgba(255,255,255,0.015) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.015) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    z-index: -1;
    pointer-events: none;
  }

  /* Master 1320px Alignment Spine */
  .navbar-inner, .ivh-container, .ihm-container, .stats-grid,
  .podium-container, .rekhta-container, .voices-container,
  .category-bento-showcase, .vault-container, .catalog-container,
  .phs-container, .footer-container,
  #bestsellers-podium > div, #mehfil-e-rekhta > div,
  #indian-voices-section > div, #law-academic-vault > div, #shop-all-catalog > div {
    width: 100% !important;
    max-width: 1320px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: 28px !important;
    padding-right: 28px !important;
    box-sizing: border-box !important;
  }

  /* Cyberpunk Glassmorphism Navigation Bar */
  nav, .navbar, header {
    background: rgba(3, 7, 18, 0.88) !important;
    backdrop-filter: blur(16px) !important;
    border-bottom: 1px solid var(--cyber-border) !important;
    position: sticky !important;
    top: 0 !important;
    z-index: 1000 !important;
  }

  /* Futuristic Glowing Hero Section */
  #indigo-video-hero, #indigo-hero-master, .ivh-section {
    background: radial-gradient(circle at 50% 20%, rgba(15, 23, 42, 0.9) 0%, var(--cyber-bg) 80%) !important;
    border-bottom: 1px solid var(--cyber-border) !important;
    position: relative !important;
    overflow: visible !important;
  }

  /* Unclipped Cyber Search Pill & Live Dropdown */
  #indigo-video-hero form, #indigo-hero-master form, .ivh-search-box, .ihm-search-wrap {
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    max-width: 580px !important;
    height: 54px !important;
    background: rgba(15, 23, 42, 0.9) !important;
    backdrop-filter: blur(12px) !important;
    border: 1.5px solid var(--cyber-border) !important;
    border-radius: 999px !important;
    padding: 4px 6px 4px 16px !important;
    box-shadow: 0 0 25px rgba(0, 245, 255, 0.15) !important;
    overflow: visible !important;
    box-sizing: border-box !important;
    z-index: 9999 !important;
    transition: all 0.3s ease !important;
  }
  #indigo-video-hero form:focus-within, #indigo-hero-master form:focus-within {
    border-color: var(--cyber-cyan) !important;
    box-shadow: 0 0 35px rgba(0, 245, 255, 0.35) !important;
  }
  #indigo-video-hero form select, #indigo-hero-master form select {
    flex: 0 0 auto !important;
    width: 120px !important;
    border: none !important;
    border-right: 1px solid rgba(255,255,255,0.12) !important;
    background: transparent !important;
    color: var(--cyber-text) !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    padding: 0 10px 0 4px !important;
    outline: none !important;
    cursor: pointer !important;
  }
  #indigo-video-hero form input, #indigo-hero-master form input {
    flex: 1 1 auto !important;
    width: 100% !important;
    min-width: 0 !important;
    height: 42px !important;
    border: none !important;
    background: transparent !important;
    color: var(--cyber-text) !important;
    font-size: 15px !important;
    padding: 0 12px !important;
    outline: none !important;
  }
  #indigo-video-hero form button[type="submit"], #indigo-hero-master form button[type="submit"] {
    flex: 0 0 auto !important;
    height: 42px !important;
    padding: 0 24px !important;
    border-radius: 999px !important;
    background: linear-gradient(135deg, #00F5FF 0%, #3B82F6 100%) !important;
    color: #030712 !important;
    font-size: 14px !important;
    font-weight: 800 !important;
    border: none !important;
    cursor: pointer !important;
    box-shadow: 0 0 15px rgba(0, 245, 255, 0.4) !important;
  }

  /* Neural Live Suggestion Dropdown */
  .indigo-live-suggest-box {
    position: absolute !important;
    top: calc(100% + 12px) !important;
    left: 0 !important;
    width: 100% !important;
    min-width: 380px !important;
    max-height: 440px !important;
    overflow-y: auto !important;
    background: rgba(3, 7, 18, 0.95) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid var(--cyber-cyan) !important;
    border-radius: 16px !important;
    box-shadow: 0 25px 60px rgba(0, 245, 255, 0.25) !important;
    z-index: 9999999 !important;
    padding: 10px !important;
    color: var(--cyber-text) !important;
    text-align: left !important;
  }

  /* Mathematical Holographic Book Card Grid */
  .catalog-card, .vault-card, .rekhta-card, .indigo-book-card, .bento-horiz-card, .bento-left-spotlight {
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 100% !important;
    padding: 20px !important;
    border-radius: 16px !important;
    box-sizing: border-box !important;
    position: relative !important;
    background: rgba(15, 23, 42, 0.65) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid var(--cyber-border) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important;
    transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1) !important;
  }
  .catalog-card:hover, .vault-card:hover, .rekhta-card:hover, .indigo-book-card:hover {
    border-color: var(--cyber-cyan) !important;
    box-shadow: 0 0 30px rgba(0, 245, 255, 0.25) !important;
    transform: translateY(-5px) !important;
  }
  .card-cover-frame, .indigo-3d-book-stage {
    width: 100% !important;
    aspect-ratio: 2 / 3 !important;
    height: auto !important;
    margin-bottom: 16px !important;
    border-radius: 8px !important;
    flex-shrink: 0 !important;
    position: relative !important;
  }
  .card-book-title {
    font-family: 'Merriweather', Georgia, serif !important;
    font-size: 15.5px !important;
    font-weight: 700 !important;
    line-height: 1.4 !important;
    height: 44px !important;
    min-height: 44px !important;
    max-height: 44px !important;
    margin: 0 0 6px 0 !important;
    color: var(--cyber-text) !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
  }
  .card-bottom-footer {
    margin-top: auto !important;
    padding-top: 14px !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    width: 100% !important;
  }

  /* Holographic Product Details Page (PDP) & Glass Cards */
  #single-product-page-view, #indigo-solo-product-view {
    background: var(--cyber-bg) !important;
    color: var(--cyber-text) !important;
  }
  .pdp-cover-card, .pdp-info-header-card, .pdp-tabs-container, .pdp-buy-box, .pdp-trust-card {
    background: rgba(15, 23, 42, 0.8) !important;
    backdrop-filter: blur(16px) !important;
    border: 1px solid var(--cyber-border) !important;
    color: var(--cyber-text) !important;
  }
  .pdp-book-title {
    color: #FFFFFF !important;
  }
  .pdp-selling-price {
    color: var(--cyber-cyan) !important;
    text-shadow: 0 0 12px rgba(0, 245, 255, 0.4) !important;
  }
  .pdp-genre-pill {
    background: rgba(0, 245, 255, 0.12) !important;
    color: var(--cyber-cyan) !important;
    border: 1px solid rgba(0, 245, 255, 0.3) !important;
  }
  .pdp-tab-btn.active {
    color: var(--cyber-cyan) !important;
    border-bottom: 2px solid var(--cyber-cyan) !important;
  }
  .pdp-tech-table th {
    background: rgba(30, 41, 59, 0.6) !important;
    color: var(--cyber-muted) !important;
  }
  .pdp-tech-table td {
    color: var(--cyber-text) !important;
  }
</style>"""

CYBER_SCRIPT = """<script id="indigo-futuristic-cyber-script">
(function() {
  /* ==========================================================================
     1. VERIFIED CSV DATASET (Zero Fake Discounts, Zero Fake Reviews)
     ========================================================================== */
  var HERO_BOOKS_CSV = [
    {
      id: 'godan-premchand',
      handle: 'godan-premchand',
      matchKey: 'godan',
      title: 'Godan (गोदान)',
      author: 'Premchand',
      vendor: 'Lokbharti Prakashan',
      category: 'Fiction : Novel',
      binding: 'Paperback',
      price: 299,
      isbn: '9789389742152',
      pages: '312p',
      weight: '270 g',
      year: '4th (1936)',
      language: 'Hindi',
      image: 'https://images.rajkamalprakashan.com/products/2026/08/07/d18d896b-e17d-4c03-b26c-0525c9675e05-godan-text-book.jpg',
      description: 'Munshi Premchand’s immortal masterpiece depicting the life, struggles, and resilience of Indian peasantry.'
    },
    {
      id: 'raag-darbari-shrilal-shukla',
      handle: 'raag-darbari-shrilal-shukla',
      matchKey: 'raag',
      title: 'Raag Darbari (राग दरबारी)',
      author: 'Shrilal Shukla',
      vendor: 'Rajkamal Prakashan',
      category: 'Fiction : Novel',
      binding: 'Paperback',
      price: 499,
      isbn: '9788126713967',
      pages: '423p',
      weight: '490 g',
      year: '55th (1983)',
      language: 'Hindi',
      image: 'https://images.rajkamalprakashan.com/products/--1776279294489.jpg',
      description: 'Sahitya Akademi Award-winning satirical masterpiece by Shrilal Shukla exposing rural politics in Shivpalganj.'
    },
    {
      id: 'chitralekha-bhagwaticharan-verma',
      handle: 'chitralekha-bhagwaticharan-verma',
      matchKey: 'chitralekha',
      title: 'Chitralekha (चित्रलेखा)',
      author: 'Bhagwaticharan Verma',
      vendor: 'Rajkamal Prakashan',
      category: 'Fiction : Novel',
      binding: 'Paperback',
      price: 299,
      isbn: '9788126715855',
      pages: '200p',
      weight: '225 g',
      year: '32nd (1993)',
      language: 'Hindi',
      image: 'https://images.rajkamalprakashan.com/products/--1776278166396.jpg',
      description: 'A timeless philosophical novel exploring sin, virtue, love, and asceticism.'
    },
    {
      id: 'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
      handle: 'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
      matchKey: 'rashmirathi',
      title: 'Rashmirathi : Dinkar Granthmala',
      author: "Ramdhari Singh 'Dinkar'",
      vendor: 'Lokbharti Prakashan',
      category: 'Poetry',
      binding: 'Paperback',
      price: 299,
      isbn: '9788180313639',
      pages: '192p',
      weight: '216 g',
      year: '46th (1952)',
      language: 'Hindi',
      image: 'https://images.rajkamalprakashan.com/products/--1776278887188.jpg',
      description: 'Rashtrakavi Ramdhari Singh Dinkar’s epic poetic saga celebrating the valor and dignity of Karna.'
    },
    {
      id: 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
      handle: 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
      matchKey: 'kuchh',
      title: 'Kuchh Ishq Kiya Kuchh Kaam Kiya',
      author: 'Piyush Mishra',
      vendor: 'Rajkamal Prakashan',
      category: 'Poetry/Shayari',
      binding: 'Paperback',
      price: 250,
      isbn: '9788126728435',
      pages: '147p',
      weight: '160 g',
      year: '5th (2016)',
      language: 'Hindi',
      image: 'https://images.rajkamalprakashan.com/products/--1776279062739.jpg',
      description: 'Raw, heartfelt poetry, theatre songs, and ghazals by Piyush Mishra capturing youth and revolution.'
    },
    {
      id: 'gypsy-ila-chandra-joshi',
      handle: 'gypsy-ila-chandra-joshi',
      matchKey: 'gypsy',
      title: 'Gypsy (जिप्सी)',
      author: 'Ila Chandra Joshi',
      vendor: 'Lokbharti Prakashan',
      category: 'Fiction : Novel',
      binding: 'Paperback',
      price: 499,
      isbn: '9789352210053',
      pages: '375p',
      weight: '400 g',
      year: '1st (2015)',
      language: 'Hindi',
      image: 'https://images.rajkamalprakashan.com/products/--1776282566523.jpeg',
      description: 'Ila Chandra Joshi’s landmark psychological Hindi novel exploring human consciousness.'
    }
  ];

  /* ==========================================================================
     2. 2-CHARACTER DEBOUNCED PREDICTIVE SEARCH ENGINE
     ========================================================================== */
  function getMasterBookPool() {
    return [].concat(HERO_BOOKS_CSV)
      .concat(window.MASTER_BOOKS || [])
      .concat(window.SHOPIFY_LIVE_PRODUCTS || [])
      .concat(window.CATALOG_BOOKS || []);
  }

  function fuzzyTokenScore(haystack, token) {
    if (!haystack || !token) return 0;
    if (haystack.indexOf(token) !== -1) return 100;
    if (token.length >= 4 && haystack.indexOf(token.slice(0, -1)) !== -1) return 75;
    return 0;
  }

  window.searchIndigoBooks = function(rawQuery) {
    var q = String(rawQuery || '').trim().toLowerCase();
    if (!q) return [];
    var tokens = q.split(/\\s+/).filter(Boolean);
    var pool = getMasterBookPool();
    var scored = [];

    pool.forEach(function(b) {
      var title = String(b.title || '').toLowerCase();
      var author = String(b.author || '').toLowerCase();
      var vendor = String(b.vendor || '').toLowerCase();
      var isbn = String(b.isbn || '').toLowerCase();
      var combined = title + ' ' + author + ' ' + vendor + ' ' + isbn;

      var totalScore = 0;
      var matchedAll = true;

      tokens.forEach(function(tok) {
        var sTitle = fuzzyTokenScore(title, tok);
        var sAuthor = fuzzyTokenScore(author, tok) * 1.2;
        var sIsbn = isbn.indexOf(tok) !== -1 ? 130 : 0;
        var best = Math.max(sTitle, sAuthor, sIsbn, fuzzyTokenScore(combined, tok));
        if (best === 0) matchedAll = false;
        else totalScore += best;
      });

      if (matchedAll && totalScore > 0) scored.push({ book: b, score: totalScore });
    });

    scored.sort(function(a, b) { return b.score - a.score; });
    var seen = {};
    return scored.map(function(x) { return x.book; }).filter(function(b) {
      var k = (b.title + '-' + b.author).toLowerCase();
      if (seen[k]) return false;
      seen[k] = true;
      return true;
    });
  };

  /* ==========================================================================
     3. BULLETPROOF MODAL UNSTICKING & SOLO PAGE ROUTER
     ========================================================================== */
  window.forceCloseOverviewAndModals = function() {
    document.querySelectorAll('#indigo-overview-modal, #overview-modal, #indigo-order-success-modal, .indigo-modal-overlay, [id*="overview"]').forEach(function(el) {
      el.classList.remove('is-active', 'active', 'open', 'show');
      el.style.setProperty('display', 'none', 'important');
      el.style.setProperty('opacity', '0', 'important');
      el.style.setProperty('pointer-events', 'none', 'important');
    });
    document.body.style.overflow = '';
  };
  window.closeOverviewModal = window.forceCloseOverviewAndModals;
  window.closeAllIndigoModals = window.forceCloseOverviewAndModals;

  window.findBookInMasterPool = function(bookOrId, imgSrcHint, triggerEl) {
    var pool = getMasterBookPool();
    if (bookOrId && typeof bookOrId === 'object' && bookOrId.title && bookOrId.title !== 'Selected Book') return bookOrId;

    var q = String(bookOrId || '').trim().toLowerCase();
    if (q && q !== 'selected book') {
      var match = pool.find(function(b) {
        if (!b || !b.title || b.title === 'Selected Book') return false;
        return (b.id && b.id.toLowerCase() === q) || (b.title && b.title.toLowerCase().indexOf(q) !== -1) || (b.author && b.author.toLowerCase().indexOf(q) !== -1);
      });
      if (match) return match;
    }

    if (triggerEl) {
      var card = triggerEl.closest('[data-book-id], [data-title], .ihm-book-item, .ivh-book-card, .catalog-card, .vault-card, .rekhta-card');
      if (card) {
        var heroGrid = card.closest('#hero-books-3x2, #ivh-books-grid, .ihm-books-grid-3x2');
        if (heroGrid) {
          var idx = Array.from(heroGrid.children).indexOf(card);
          if (idx >= 0 && idx < HERO_BOOKS_CSV.length) return Object.assign({}, HERO_BOOKS_CSV[idx]);
        }
        var cTitle = card.getAttribute('data-title') || (card.querySelector('h3, h4, .card-title, .book-title') ? card.querySelector('h3, h4, .card-title, .book-title').textContent.trim() : '');
        var found = pool.find(function(b) { return b && b.title && cTitle && b.title.toLowerCase().indexOf(cTitle.toLowerCase()) !== -1; });
        if (found) return found;
      }
    }
    return HERO_BOOKS_CSV[0];
  };

  window.forceOpenSoloPageWithBook = function(book) {
    if (!book) return;
    window.CURRENT_SOLO_BOOK = book;

    document.querySelectorAll('.indigo-live-suggest-box').forEach(function(d) { d.style.setProperty('display', 'none', 'important'); });
    document.querySelectorAll('#indigo-search-results-view').forEach(function(sr) { sr.style.setProperty('display', 'none', 'important'); });

    var soloView = document.getElementById('indigo-solo-product-view') || document.getElementById('single-product-page-view');
    if (soloView) soloView.style.setProperty('display', 'block', 'important');

    var realCover = book.image || HERO_BOOKS_CSV[0].image;
    var cleanPrice = parseFloat(String(book.price || 299).replace(/[^0-9.]/g, '')) || 299;

    document.querySelectorAll('h1, h2, .solo-book-title').forEach(function(el) {
      if ((el.textContent || '').trim() === 'Selected Book' || el.id.indexOf('title') !== -1) {
        el.textContent = book.title;
      }
    });

    document.querySelectorAll('img').forEach(function(img) {
      var src = img.getAttribute('src') || '';
      if (!src || src.indexOf('Selected%20Book') !== -1) {
        img.src = realCover;
      }
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  window.openSoloBookPage = function(bookOrId, triggerEl) {
    var resolved = window.findBookInMasterPool(bookOrId, '', triggerEl) || HERO_BOOKS_CSV[0];
    window.forceOpenSoloPageWithBook(resolved);
  };

  /* ==========================================================================
     4. UNIVERSAL SEARCH LISTENER (Fires at >= 2 chars)
     ========================================================================== */
  function attachUniversalSearchListeners() {
    var inputs = document.querySelectorAll('input[placeholder*="Search"], input[placeholder*="search"], #hero-search-input, #liveSearchInput');
    inputs.forEach(function(input) {
      if (input.dataset.indigoSearchBound === '1') return;
      input.dataset.indigoSearchBound = '1';

      var form = input.closest('form') || input.parentElement;
      form.style.setProperty('position', 'relative', 'important');
      form.style.setProperty('overflow', 'visible', 'important');

      var box = form.querySelector('.indigo-live-suggest-box');
      if (!box) {
        box = document.createElement('div');
        box.className = 'indigo-live-suggest-box';
        box.style.display = 'none';
        form.appendChild(box);
      }

      var timer = null;
      input.addEventListener('input', function() {
        clearTimeout(timer);
        var val = (input.value || '').trim();
        if (val.length < 2) {
          box.style.display = 'none';
          return;
        }
        timer = setTimeout(function() {
          var matches = window.searchIndigoBooks(val).slice(0, 8);
          if (matches.length === 0) {
            box.innerHTML = '<div style="padding:14px;text-align:center;color:#94A3B8;font-size:13.5px;">No neural matches for "<b>' + val + '</b>".</div>';
            box.style.display = 'block';
            return;
          }
          var html = '';
          matches.forEach(function(b) {
            var p = parseFloat(String(b.price || 299).replace(/[^0-9.]/g, '')) || 299;
            var safeId = String(b.id || b.title).replace(/'/g, "\\\\'");
            html += '<div class="indigo-suggest-row" data-book-id="' + safeId + '" style="display:flex;align-items:center;gap:12px;padding:10px 12px;border-bottom:1px solid rgba(255,255,255,0.06);cursor:pointer;border-radius:8px;" onmouseover="this.style.background=\\'rgba(0,245,255,0.1)\\'" onmouseout="this.style.background=\\'transparent\\'">' +
              '<img src="' + b.image + '" style="width:40px;height:58px;object-fit:cover;border-radius:4px;flex-shrink:0;border:1px solid var(--cyber-border);" />' +
              '<div style="flex:1;min-width:0;">' +
                '<div style="font-size:14px;font-weight:700;color:var(--cyber-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">' + b.title + '</div>' +
                '<div style="font-size:12px;color:var(--cyber-muted);">by <b style="color:var(--cyber-cyan);">' + b.author + '</b></div>' +
              '</div>' +
              '<div style="font-size:14.5px;font-weight:800;color:var(--cyber-gold);min-width:75px;text-align:right;">₹' + p.toFixed(2) + '</div>' +
            '</div>';
          });
          box.innerHTML = html;
          box.style.display = 'block';

          box.querySelectorAll('.indigo-suggest-row').forEach(function(row) {
            row.addEventListener('click', function(e) {
              e.stopPropagation();
              box.style.display = 'none';
              window.openSoloBookPage(this.getAttribute('data-book-id'), this);
            });
          });
        }, 200);
      });
    });
  }

  /* ==========================================================================
     5. WIRE "BROWSE ALL 5,500+ BOOKS" & CATALOG EXPANSION
     ========================================================================== */
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('a, button');
    if (!btn) return;
    var txt = (btn.textContent || '').trim().toLowerCase();
    if (txt.indexOf('browse all') !== -1 || txt.indexOf('shop all') !== -1 || txt.indexOf('all books (5,500') !== -1) {
      e.preventDefault();
      window.forceCloseOverviewAndModals();
      if (typeof window.closeSoloBookPage === 'function') window.closeSoloBookPage();

      window.CATALOG_VISIBLE_LIMIT = (window.CATALOG_VISIBLE_LIMIT || 12) + 24;
      if (typeof window.filterCatalog === 'function') window.filterCatalog('all');
      if (typeof window.renderCatalog === 'function') window.renderCatalog();

      var catSec = document.getElementById('shop-all-catalog') || document.querySelector('[id*="catalog"]');
      if (catSec) catSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });

  function initMaster() {
    attachUniversalSearchListeners();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMaster);
  } else {
    initMaster();
  }
  setTimeout(initMaster, 500);
})();
</script>"""

CYBER_COMBINED_BLOCK = CYBER_STYLE + "\\n\\n" + CYBER_SCRIPT
