
(function() {
  /* ==========================================================================
     1. VERIFIED CSV DATA FOR CORE BOOKS (Zero Fake Discounts/Reviews)
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
      dimensions: '21.5 × 14 × 1 cm', qty: 100,
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
      dimensions: '21.5 × 14 × 2 cm', qty: 100,
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
      dimensions: '21.5 × 14 × 1 cm', qty: 100,
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
      dimensions: '21.5 × 14 × 1 cm', qty: 100,
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
      dimensions: '21.5 × 14 × 1 cm', qty: 4005,
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
      dimensions: '21.5 × 14 × 2 cm', qty: 100,
      year: '1st (2015)',
      language: 'Hindi',
      image: 'https://images.rajkamalprakashan.com/products/--1776282566523.jpeg',
      description: 'Ila Chandra Joshi’s landmark psychological Hindi novel exploring human consciousness.'
    }
  ];

  /* ==========================================================================
     2. FORCE-CLOSE & UNSTICK OVERVIEW MODALS
     ========================================================================== */
  window.forceCloseOverviewAndModals = function() {
    var selectors = ['#overviewModalOverlay', '#indigo-overview-modal', '#overview-modal', '#indigo-order-success-modal', '.indigo-modal-overlay'];
    selectors.forEach(function(sel) {
      document.querySelectorAll(sel).forEach(function(el) {
        el.classList.remove('is-active', 'active', 'open', 'show');
        el.style.setProperty('display', 'none', 'important');
        el.style.removeProperty('opacity');
        el.style.removeProperty('pointer-events');
        el.style.opacity = '';
        el.style.pointerEvents = '';
      });
    });
    document.body.style.overflow = '';
  };
  window.closeOverviewModal = window.forceCloseOverviewAndModals;
  window.closeAllIndigoModals = window.forceCloseOverviewAndModals;

  window.forceOpenSoloPageWithBook = function(b) {
    if (typeof window.openDedicatedProductPage === 'function') {
      window.openDedicatedProductPage(b);
    }
  };

  document.addEventListener('click', function(e) {
    var btn = e.target.closest('button, a, span');
    if (btn) {
      var t = (btn.textContent || '').trim();
      var parentModal = btn.closest('[style*="position: fixed"], [class*="modal"]');
      if (parentModal && (t === '✕' || t === '×' || t === 'X' || btn.classList.contains('close'))) {
        e.preventDefault();
        window.forceCloseOverviewAndModals();
        return;
      }
      if (t.indexOf('Open Full Book Page') !== -1 || t.indexOf('Full Page') !== -1) {
        e.preventDefault();
        var bObj = window.CURRENT_OVERVIEW_BOOK || window.currentModalBook || (window.currentModalBookId && typeof window.resolveBookObject === 'function' ? window.resolveBookObject(window.currentModalBookId) : null) || HERO_BOOKS_CSV[0];
        window.forceCloseOverviewAndModals();
        window.forceOpenSoloPageWithBook(bObj);
        return;
      }
    }
  }, true);

  /* Home Button and Logo Navigation to Homepage */
  document.addEventListener('click', function(e) {
    var brand = e.target.closest('.brand-link, .brand-wordmark, [aria-label*="Homepage"]');
    if (brand) {
      e.preventDefault();
      if (typeof window.returnToHome === 'function') {
        window.returnToHome(e);
        return;
      }
    }
    var homeBtn = e.target.closest('a, button');
    if (homeBtn && (homeBtn.textContent || '').trim().toLowerCase() === 'home') {
      e.preventDefault();
      if (typeof window.returnToHome === 'function') {
        window.returnToHome(e);
        return;
      }
    }
  });

  /* ==========================================================================
     3. WIRE "BROWSE ALL 5,500+ BOOKS" & "SHOP ALL" BUTTONS
     ========================================================================== */
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('a, button');
    if (!btn) return;
    var txt = (btn.textContent || '').trim().toLowerCase();
    if (txt.indexOf('browse all') !== -1 || txt.indexOf('shop all') !== -1 || txt.indexOf('all books (5,500') !== -1) {
      e.preventDefault();
      if (typeof window.closeDedicatedProductPage === 'function') window.closeDedicatedProductPage();
      if (typeof window.closeSearchResultsView === 'function') window.closeSearchResultsView();
      if (typeof window.closeAllIndigoModals === 'function') window.closeAllIndigoModals();

      window.CATALOG_VISIBLE_LIMIT = (window.CATALOG_VISIBLE_LIMIT || 12) + 24;
      if (typeof window.filterCatalog === 'function') window.filterCatalog('all');
      if (typeof window.renderCatalog === 'function') window.renderCatalog();

      var catSec = document.getElementById('shop-all-catalog') || document.querySelector('[id*="catalog"]');
      if (catSec) catSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });

  function initMaster() {
    // Solo product page is handled by authoritative editorial video engine
    if (typeof window.openSoloBookPage === 'function') {
      window.openDedicatedProductPage = window.openSoloBookPage;
    }
    // Wire 2-character debounced search inputs
    ['hero-search-input', 'catalog-search-input', 'results-search-input'].forEach(function(id) {
      var input = document.getElementById(id);
      if (input && !input.getAttribute('data-wired')) {
        input.setAttribute('data-wired', 'true');
        var target = id.startsWith('hero') ? 'hero' : (id.startsWith('results') ? 'results' : 'catalog');
        input.addEventListener('input', function(e) {
          if (typeof window.handleSearchInput === 'function') {
            window.handleSearchInput(e.target.value, target);
          }
        });
        input.addEventListener('focus', function(e) {
          if (e.target.value.trim().length >= 2 && typeof window.handleSearchInput === 'function') {
            window.handleSearchInput(e.target.value, target);
          }
        });
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMaster);
  } else {
    initMaster();
  }
  setTimeout(initMaster, 500);
})();
