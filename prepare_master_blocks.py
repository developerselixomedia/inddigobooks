# -*- coding: utf-8 -*-
"""
prepare_master_blocks.py
Creates the verified, clean style and script blocks.
"""

MASTER_STYLE = """<style id="indigo-master-production-styles">
  /* =========================================================================
     1. UNIVERSAL 1320PX ALIGNMENT SPINE & ZERO-OVERFLOW SHIELD
     ========================================================================= */
  html, body {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
    position: relative !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  *, *:before, *:after {
    box-sizing: border-box !important;
  }

  .navbar-inner, .ivh-container, .ihm-container, .stats-grid,
  .podium-container, .rekhta-container, .voices-container,
  .category-bento-showcase, .vault-container, .catalog-container,
  .phs-container, .footer-container, .editorial-header, .catalog-filter-bar,
  .trust-strip-grid, .trust-features-grid, .heritage-grid, .footer-grid,
  .product-page-wrapper,
  #bestsellers-podium > div, #mehfil-e-rekhta > div, #mehfil-rekhta > div,
  #indian-voices-section > div, #category-bento-showcase > div,
  #law-academic-vault > div, #shop-all-catalog > div {
    width: 100% !important;
    max-width: 1320px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: 24px !important;
    padding-right: 24px !important;
    box-sizing: border-box !important;
  }

  @media (max-width: 640px) {
    .navbar-inner, .site-container, .section-container, .ivh-container, .ihm-container,
    .stats-grid, .podium-container, .rekhta-container, .voices-container,
    .category-bento-showcase, .vault-container, .catalog-container, .phs-container,
    .footer-container, .editorial-header, .catalog-filter-bar, .trust-strip-grid,
    .trust-features-grid, .heritage-grid, .footer-grid, .product-page-wrapper,
    #bestsellers-podium > div, #mehfil-e-rekhta > div, #mehfil-rekhta > div,
    #indian-voices-section > div, #category-bento-showcase > div,
    #law-academic-vault > div, #shop-all-catalog > div {
      padding-left: 14px !important;
      padding-right: 14px !important;
      max-width: 100% !important;
      overflow-x: hidden !important;
    }
  }

  /* =========================================================================
     2. UNCLIPPED RESPONSIVE HERO SEARCH PILL & PREDICTIVE DROPDOWN
     ========================================================================= */
  #indigo-video-hero form, #indigo-hero-master form,
  .hero-search-wrap, .search-input-wrap, .search-input-group,
  .ivh-search-box, .ihm-search-wrap, .catalog-search-wrap {
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    max-width: 540px !important;
    height: 52px !important;
    background: #FFFFFF !important;
    border-radius: 999px !important;
    padding: 4px 6px 4px 14px !important;
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.35) !important;
    overflow: visible !important;
    box-sizing: border-box !important;
    z-index: 999999 !important;
  }

  #indigo-video-hero form select, #indigo-hero-master form select,
  .search-category-select, #heroSearchCategory, #catalogSearchCategory,
  .hero-search-wrap select {
    flex: 0 0 auto !important;
    width: 110px !important;
    border: none !important;
    border-right: 1px solid #CBD5E1 !important;
    background: transparent !important;
    color: #09132C !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 0 8px 0 4px !important;
    outline: none !important;
    cursor: pointer !important;
  }

  #indigo-video-hero form input, #indigo-hero-master form input,
  .hero-search-wrap input, #hero-search-input,
  .catalog-search-wrap input, #catalog-search-input {
    flex: 1 1 auto !important;
    width: 100% !important;
    min-width: 0 !important;
    height: 42px !important;
    border: none !important;
    background: transparent !important;
    color: #09132C !important;
    font-size: 14.5px !important;
    padding: 0 10px !important;
    outline: none !important;
  }

  #indigo-video-hero form button[type="submit"], #indigo-hero-master form button[type="submit"],
  .hero-search-wrap button, .catalog-search-wrap button {
    flex: 0 0 auto !important;
    height: 40px !important;
    padding: 0 20px !important;
    border-radius: 999px !important;
    background: #09132C !important;
    color: #FFFFFF !important;
    font-size: 13.5px !important;
    font-weight: 700 !important;
    border: none !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
  }

  #hero-search-suggestions,
  #catalog-search-suggestions,
  #results-search-suggestions,
  .search-suggestions-dropdown,
  .indigo-live-suggest-box {
    position: absolute !important;
    top: calc(100% + 8px) !important;
    left: 0 !important;
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;
    max-height: 420px !important;
    overflow-y: auto !important;
    background: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 12px !important;
    box-shadow: 0 24px 60px rgba(9, 19, 44, 0.45) !important;
    z-index: 99999999 !important;
    padding: 8px !important;
    color: #09132C !important;
    text-align: left !important;
    box-sizing: border-box !important;
  }
  .search-suggestion-item:hover,
  .indigo-suggest-row:hover {
    background: #FEF3C7 !important;
  }

  /* Mobile Search Pill Fit on <= 640px */
  @media (max-width: 640px) {
    #indigo-video-hero form, #indigo-hero-master form,
    .hero-search-wrap, .search-input-wrap, .search-input-group,
    .ivh-search-box, .ihm-search-wrap, .catalog-search-wrap {
      height: 46px !important;
      padding: 3px 4px 3px 8px !important;
      gap: 4px !important;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.28) !important;
      margin-bottom: 14px !important;
      max-width: 100% !important;
      width: 100% !important;
    }
    #indigo-video-hero form select, #indigo-hero-master form select,
    .search-category-select, #heroSearchCategory, #catalogSearchCategory,
    .hero-search-wrap select {
      flex: 0 0 76px !important;
      width: 76px !important;
      max-width: 76px !important;
      font-size: 11px !important;
      padding: 0 4px 0 2px !important;
      height: 36px !important;
      text-overflow: ellipsis !important;
    }
    .hero-search-wrap svg,
    .hero-search-wrap [data-lucide="search"],
    .catalog-search-wrap svg {
      width: 15px !important;
      height: 15px !important;
      margin-left: 2px !important;
      flex-shrink: 0 !important;
    }
    #indigo-video-hero form input, #indigo-hero-master form input,
    .hero-search-wrap input, #hero-search-input,
    .catalog-search-wrap input, #catalog-search-input {
      font-size: 12.5px !important;
      padding: 0 6px !important;
      height: 36px !important;
      min-width: 0 !important;
    }
    #indigo-video-hero form button[type="submit"], #indigo-hero-master form button[type="submit"],
    .hero-search-wrap button, .catalog-search-wrap button {
      height: 36px !important;
      padding: 0 12px !important;
      font-size: 11.5px !important;
      margin-right: 2px !important;
    }
  }

  /* Suppress rogue Shopify predictive search empty overlay completely */
  .predictive-search,
  .predictive-search-empty,
  .predictive-search-empty__message,
  .predictive-search-suggestions,
  .predictive-search-wa-prompt,
  #predictive-search-results,
  [data-predictive-search],
  predictive-search [tabindex="-1"],
  .predictive-search__results-groups-wrapper {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
    height: 0 !important;
    overflow: hidden !important;
    z-index: -9999 !important;
  }

  /* =========================================================================
     3. HERO SECTION MOBILE PERFECTION (ZERO OVERFLOW, STACKED CTAs, SCALED WHEEL)
     ========================================================================= */
  @media (max-width: 768px) {
    #indigo-video-hero, #indigo-hero-master, .hero-section, .ivh-section {
      overflow-x: clip !important;
      overflow: hidden !important;
      padding: 24px 0 36px 0 !important;
      min-height: auto !important;
      width: 100% !important;
      max-width: 100% !important;
    }
    .hero-bg-clip {
      overflow: hidden !important;
      max-width: 100% !important;
    }
    .hero-bg-clip svg {
      max-width: 100vw !important;
    }
    .hero-main-grid, .hero-inner-container {
      grid-template-columns: 1fr !important;
      gap: 24px !important;
      width: 100% !important;
      padding: 0 14px !important;
    }
    .hero-left-col, .ivh-left {
      width: 100% !important;
      max-width: 100% !important;
      text-align: left !important;
      padding: 0 !important;
    }
    .ivh-title, .hero-left-col h1 {
      font-size: 26px !important;
      line-height: 1.25 !important;
      margin-bottom: 8px !important;
      word-wrap: break-word !important;
    }
    .hero-left-col p, .ivh-left p {
      font-size: 13px !important;
      line-height: 1.45 !important;
      margin-bottom: 14px !important;
      color: #CBD5E1 !important;
    }
  }

  @media (max-width: 640px) {
    .hero-cta-row {
      display: flex !important;
      flex-direction: column !important;
      width: 100% !important;
      gap: 10px !important;
      margin-top: 14px !important;
      box-sizing: border-box !important;
    }
    .hero-shop-btn, .hero-wa-cod-btn {
      width: 100% !important;
      height: 44px !important;
      justify-content: center !important;
      text-align: center !important;
      font-size: 13.5px !important;
      padding: 0 16px !important;
      box-sizing: border-box !important;
      border-radius: 8px !important;
      display: inline-flex !important;
      align-items: center !important;
    }

    .hero-right-col, .ivh-right, .hero-stage-col {
      width: 100% !important;
      max-width: 100% !important;
      overflow: hidden !important;
      margin-top: 24px !important;
      position: relative !important;
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      min-height: 280px !important;
      padding: 6px 0 !important;
      box-sizing: border-box !important;
    }
    .hero-rangoli-wrapper, .hero-wheel-wrap, .hero-rangoli-bg {
      width: 260px !important;
      height: 260px !important;
      max-width: 85vw !important;
      max-height: 85vw !important;
      left: 50% !important;
      top: 50% !important;
      transform: translate(-50%, -50%) !important;
      position: absolute !important;
      z-index: 5 !important;
      pointer-events: none !important;
    }
    .hero-wheel-svg, .hero-rangoli-svg {
      width: 260px !important;
      height: 260px !important;
      max-width: 100% !important;
      max-height: 100% !important;
      display: block !important;
    }
    .hero-books-grid-video, .ivh-books-grid {
      position: relative !important;
      z-index: 25 !important;
      display: grid !important;
      grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
      grid-template-rows: auto !important;
      gap: 8px !important;
      width: 100% !important;
      max-width: 320px !important;
      margin: 0 auto !important;
      justify-content: center !important;
      box-sizing: border-box !important;
    }
    .hero-video-book-card, .ivh-book-card {
      width: 100% !important;
      max-width: 98px !important;
      padding: 6px !important;
      border-radius: 8px !important;
      box-sizing: border-box !important;
    }
    .hero-video-book-card .hero-book-thumb, .ivh-book-card .hero-book-thumb {
      width: 100% !important;
      height: 110px !important;
      aspect-ratio: 2 / 3 !important;
      border-radius: 4px !important;
      overflow: hidden !important;
      margin-bottom: 6px !important;
    }
    .hero-video-book-card .hero-book-thumb img, .ivh-book-card .hero-book-thumb img {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
    }
    .hero-book-title {
      font-size: 10.5px !important;
      line-height: 1.2 !important;
      white-space: nowrap !important;
      overflow: hidden !important;
      text-overflow: ellipsis !important;
    }
    .hero-book-author {
      font-size: 9px !important;
      white-space: nowrap !important;
      overflow: hidden !important;
      text-overflow: ellipsis !important;
    }
    .hero-book-price {
      font-size: 10.5px !important;
      font-weight: 700 !important;
    }
  }

  /* =========================================================================
     4. NAVBAR & CATEGORY PILLS HORIZONTAL SCROLL DISCIPLINE
     ========================================================================= */
  @media (max-width: 640px) {
    .nav-links-wrap,
    header .nav-links-wrap,
    .navbar-links {
      order: 3 !important;
      width: 100% !important;
      flex-basis: 100% !important;
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
      overflow-x: auto !important;
      overflow-y: hidden !important;
      white-space: nowrap !important;
      padding: 6px 2px 6px 2px !important;
      margin: 4px 0 0 0 !important;
      border-top: 1px solid rgba(15, 23, 42, 0.08) !important;
      background-color: #FAF8F5 !important;
      -webkit-overflow-scrolling: touch !important;
      scrollbar-width: none !important;
      box-sizing: border-box !important;
    }
    .nav-links-wrap::-webkit-scrollbar {
      display: none !important;
    }

    .cat-pills-row,
    .catalog-filter-pills,
    .poet-pills-row {
      display: flex !important;
      flex-wrap: nowrap !important;
      overflow-x: auto !important;
      overflow-y: hidden !important;
      white-space: nowrap !important;
      -webkit-overflow-scrolling: touch !important;
      scrollbar-width: none !important;
      padding: 4px 2px 8px 2px !important;
      gap: 8px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .cat-pills-row::-webkit-scrollbar,
    .poet-pills-row::-webkit-scrollbar {
      display: none !important;
    }
    .cat-pill, .poet-pill {
      flex-shrink: 0 !important;
      font-size: 12px !important;
      padding: 6px 14px !important;
    }
  }

  /* =========================================================================
     5. PODIUM 3D TURNTABLE & FLANKING BOOKS SCALING ON MOBILE
     ========================================================================= */
  @media (max-width: 480px) {
    .podium-turntable-track {
      height: 270px !important;
      max-width: 100% !important;
      overflow: hidden !important;
    }
    .flank-book {
      width: 105px !important;
      height: 155px !important;
    }
    .flank-left-2 { transform: translateX(-85px) scale(0.65) rotateY(28deg) !important; }
    .flank-left-1 { transform: translateX(-48px) scale(0.8) rotateY(18deg) !important; }
    .flank-right-1 { transform: translateX(48px) scale(0.8) rotateY(-18deg) !important; }
    .flank-right-2 { transform: translateX(85px) scale(0.65) rotateY(-28deg) !important; }
  }

  /* =========================================================================
     6. PDP AUTHOR SHELF EQUAL HEIGHT & PADDING ALIGNMENT
     ========================================================================= */
  .shelf-scroll-row {
    display: flex !important;
    gap: 16px !important;
    overflow-x: auto !important;
    padding: 12px 4px 20px 4px !important;
    box-sizing: border-box !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: thin !important;
  }
  .shelf-book-card {
    flex: 0 0 200px !important;
    width: 200px !important;
    max-width: 200px !important;
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px !important;
    padding: 14px !important;
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 410px !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
  }
  .shelf-book-card:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08) !important;
  }
  .shelf-book-card .indigo-3d-book-stage {
    width: 100% !important;
    height: 240px !important;
    aspect-ratio: 2 / 3 !important;
    margin: 0 auto 12px auto !important;
    position: relative !important;
  }
  .shelf-book-card .indigo-3d-cover-front img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    aspect-ratio: 2 / 3 !important;
    border-radius: 6px !important;
  }
  @media (max-width: 640px) {
    .shelf-book-card {
      flex: 0 0 160px !important;
      width: 160px !important;
      max-width: 160px !important;
      padding: 10px !important;
      height: 350px !important;
    }
    .shelf-book-card .indigo-3d-book-stage {
      height: 190px !important;
      margin-bottom: 8px !important;
    }
    .shelf-book-card .card-book-title {
      font-size: 13px !important;
      height: 36px !important;
      min-height: 36px !important;
      max-height: 36px !important;
    }
  }

  /* =========================================================================
     7. MATHEMATICAL BOOK CARD ALIGNMENT
     ========================================================================= */
  .catalog-card, .vault-card, .rekhta-card, .indigo-book-card {
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 100% !important;
    padding: 16px !important;
    border-radius: 14px !important;
    box-sizing: border-box !important;
    position: relative !important;
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
  }
  .card-cover-frame, .indigo-3d-book-stage {
    width: 100% !important;
    aspect-ratio: 2 / 3 !important;
    height: auto !important;
    margin-bottom: 14px !important;
    border-radius: 6px !important;
    flex-shrink: 0 !important;
    position: relative !important;
  }
  .card-book-title {
    font-family: 'Merriweather', Georgia, serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    line-height: 1.4 !important;
    height: 42px !important;
    min-height: 42px !important;
    max-height: 42px !important;
    margin: 0 0 4px 0 !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
  }
  .card-bottom-footer {
    margin-top: auto !important;
    padding-top: 10px !important;
    border-top: 1px solid rgba(148, 163, 184, 0.16) !important;
    width: 100% !important;
  }

  /* =========================================================================
     8. LAW & ACADEMIC VAULT DISCIPLINE
     ========================================================================= */
  #law-academic-vault {
    width: 100% !important;
    padding: 56px 0 !important;
    box-sizing: border-box !important;
  }
  #law-academic-vault .site-container,
  #law-academic-vault > div,
  .vault-container {
    max-width: 1320px !important;
    width: 100% !important;
    margin: 0 auto !important;
    padding: 0 24px !important;
    box-sizing: border-box !important;
  }
  .vault-layout {
    display: grid !important;
    grid-template-columns: 260px 1fr !important;
    gap: 28px !important;
    width: 100% !important;
    align-items: start !important;
    box-sizing: border-box !important;
  }
  .vault-cards-grid {
    display: grid !important;
    grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
    gap: 18px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  @media (max-width: 1100px) {
    .vault-cards-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 16px !important;
    }
  }
  @media (max-width: 900px) {
    .vault-layout {
      display: flex !important;
      flex-direction: column !important;
      width: 100% !important;
      gap: 16px !important;
      box-sizing: border-box !important;
      padding: 0 !important;
      margin: 0 !important;
    }
    .vault-nav-col {
      display: flex !important;
      flex-direction: row !important;
      overflow-x: auto !important;
      flex-wrap: nowrap !important;
      gap: 8px !important;
      width: 100% !important;
      padding: 2px 2px 10px !important;
      -webkit-overflow-scrolling: touch !important;
      scrollbar-width: none !important;
      box-sizing: border-box !important;
    }
    .vault-nav-col::-webkit-scrollbar {
      display: none !important;
    }
    .vault-tab-btn {
      flex-shrink: 0 !important;
      padding: 8px 14px !important;
      font-size: 12px !important;
      border-radius: 9999px !important;
      white-space: nowrap !important;
      background: #FFFFFF !important;
      border: 1px solid #CBD5E1 !important;
      color: #334155 !important;
    }
    .vault-tab-btn.active {
      background: #0F172A !important;
      border-color: #0F172A !important;
      color: #FFFFFF !important;
    }
    .vault-tab-btn i:last-child {
      display: none !important;
    }
    .vault-concierge-card {
      display: none !important; /* Eliminates the empty left gap completely on mobile */
    }
    .vault-cards-grid {
      display: grid !important;
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important; /* 2 COLUMNS ON MOBILE */
      gap: 12px !important;
      width: 100% !important;
      box-sizing: border-box !important;
      padding: 0 !important;
      margin: 0 !important;
    }
    .vault-card {
      width: 100% !important;
      max-width: 100% !important;
      padding: 12px 10px !important;
      box-sizing: border-box !important;
      border-radius: 10px !important;
    }
    .vault-card .indigo-3d-book-stage {
      height: 200px !important;
      width: 100% !important;
      margin: 0 auto 10px !important;
    }
    .vault-card h3 {
      font-size: 13px !important;
      line-height: 1.3 !important;
      margin-bottom: 4px !important;
    }
  }
  .vault-card {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px !important;
    padding: 14px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 100% !important;
    box-sizing: border-box !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
  }
  .vault-card-thumb {
    width: 100% !important;
    max-height: 280px !important;
    aspect-ratio: 2 / 3 !important;
    border-radius: 6px !important;
    overflow: hidden !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    background: #F8FAFC !important;
    margin-bottom: 12px !important;
  }
  .vault-card-thumb img {
    width: 100% !important;
    height: 100% !important;
    max-height: 280px !important;
    object-fit: cover !important;
  }

  /* =========================================================================
     PRODUCT DETAILS PAGE (PDP) MOBILE & DESKTOP ALIGNMENT SHIELD
     ========================================================================= */
  #single-product-page-view {
    min-height: auto !important;
  }
  .product-page-wrapper {
    padding: 20px 20px 24px !important;
  }
  .product-pdp-grid {
    display: grid !important;
    grid-template-columns: 340px 1fr 310px !important;
    gap: 20px !important;
    align-items: start !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-bottom: 20px !important;
    box-sizing: border-box !important;
  }
  .pdp-left-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-trust-card {
    margin: 0 !important;
    padding: 16px 18px !important;
  }
  .pdp-center-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 0 !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-info-header-card {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-bottom: none !important;
    border-radius: 14px 14px 0 0 !important;
    padding: 22px 24px 16px !important;
    margin: 0 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
  }
  .pdp-tabs-container {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-top: 1px solid #F1F5F9 !important;
    border-radius: 0 0 14px 14px !important;
    padding: 0 24px 22px !important;
    margin: 0 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
  }
  .pdp-tab-nav {
    display: flex !important;
    gap: 12px !important;
    border-bottom: 2px solid #E2E8F0 !important;
    margin: 10px 0 14px !important;
  }
  .pdp-right-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-buy-box {
    padding: 20px !important;
  }
  .pdp-recommendations-sec {
    margin-top: 24px !important;
    padding-top: 20px !important;
    border-top: 1px solid #E2E8F0 !important;
  }

  @media (max-width: 1100px) {
    .product-pdp-grid {
      grid-template-columns: 300px 1fr 280px !important;
      gap: 16px !important;
    }
  }

  @media (max-width: 900px) {
    .product-page-wrapper {
      padding: 12px 14px 40px !important;
      max-width: 100vw !important;
      width: 100% !important;
      box-sizing: border-box !important;
      overflow-x: hidden !important;
    }
    .product-breadcrumb-bar {
      display: flex !important;
      flex-wrap: wrap !important;
      justify-content: space-between !important;
      align-items: center !important;
      gap: 8px !important;
      padding: 8px 0 14px !important;
      margin-bottom: 16px !important;
      font-size: 11.5px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .product-breadcrumb-bar .breadcrumb-nav {
      flex: 1 1 100% !important;
      line-height: 1.4 !important;
      word-break: break-word !important;
    }
    .btn-back-to-store {
      padding: 6px 12px !important;
      font-size: 12px !important;
      width: auto !important;
    }

    /* FULL-WIDTH RESPONSIVE FLOW ON MOBILE (ZERO SQUEEZED COLUMNS) */
    .product-pdp-grid {
      display: flex !important;
      flex-direction: column !important;
      gap: 16px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .pdp-left-col,
    .pdp-center-col,
    .pdp-right-col {
      display: contents !important;
    }

    /* 1. Cover Card */
    .pdp-cover-card {
      order: 1 !important;
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
      padding: 18px 14px !important;
      background: #FFFFFF !important;
      border: 1px solid #E2E8F0 !important;
      border-radius: 14px !important;
      box-sizing: border-box !important;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
      text-align: center !important;
    }
    .pdp-cover-card .indigo-3d-book-stage {
      max-width: 240px !important;
      height: 240px !important;
      margin: 0 auto 14px !important;
    }
    .pdp-look-inside-btn {
      width: 100% !important;
      padding: 10px 14px !important;
      font-size: 12.5px !important;
    }

    /* 2. Book Info Header Card */
    .pdp-info-header-card {
      order: 2 !important;
      width: 100% !important;
      max-width: 100% !important;
      background: #FFFFFF !important;
      border: 1px solid #E2E8F0 !important;
      border-radius: 14px !important;
      padding: 20px 16px !important;
      box-sizing: border-box !important;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
    }
    .pdp-book-title {
      font-size: 22px !important;
      line-height: 1.3 !important;
      margin: 0 0 10px !important;
      word-break: break-word !important;
    }
    .pdp-author-pill-wrap {
      margin-bottom: 12px !important;
    }
    .pdp-price-wrap {
      margin-bottom: 12px !important;
    }
    .pdp-selling-price {
      font-size: 26px !important;
    }
    .pdp-variant-selector-box {
      padding: 12px !important;
      margin: 12px 0 !important;
      border-radius: 10px !important;
    }
    .pdp-variant-buttons {
      gap: 8px !important;
    }
    .pdp-variant-btn {
      padding: 8px 12px !important;
      font-size: 12px !important;
    }

    /* 3. Buy Box */
    .pdp-buy-box {
      order: 3 !important;
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
      padding: 20px 16px !important;
      border-radius: 14px !important;
      box-sizing: border-box !important;
      background: #FFFFFF !important;
      border: 1px solid #E2E8F0 !important;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
    }
    .pdp-bb-price {
      font-size: 26px !important;
      margin-bottom: 12px !important;
    }

    /* 4. Description & Technical Specs Tabs (100% FULL WIDTH!) */
    .pdp-tabs-container {
      order: 4 !important;
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
      background: #FFFFFF !important;
      border: 1px solid #E2E8F0 !important;
      border-radius: 14px !important;
      padding: 16px !important;
      box-sizing: border-box !important;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
    }
    .pdp-tech-table {
      width: 100% !important;
      border-collapse: collapse !important;
    }
    .pdp-tech-table th {
      width: 36% !important;
      padding: 10px 10px !important;
      font-size: 12px !important;
      white-space: nowrap !important;
      background: #F8FAFC !important;
      color: #64748B !important;
      font-weight: 600 !important;
      border-bottom: 1px solid #F1F5F9 !important;
    }
    .pdp-tech-table td {
      width: 64% !important;
      padding: 10px 10px !important;
      font-size: 12.5px !important;
      color: #0F172A !important;
      font-weight: 500 !important;
      border-bottom: 1px solid #F1F5F9 !important;
      word-break: normal !important;
      line-height: 1.4 !important;
    }

    /* 5. Trust Perks Card */
    .pdp-trust-card {
      order: 5 !important;
      width: 100% !important;
      max-width: 100% !important;
      background: #FFFFFF !important;
      border: 1px solid #E2E8F0 !important;
      border-radius: 14px !important;
      padding: 18px 16px !important;
      box-sizing: border-box !important;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
      margin: 0 !important;
    }
    .pdp-perks-checklist {
      list-style: none !important;
      padding: 0 !important;
      margin: 0 !important;
      display: flex !important;
      flex-direction: column !important;
      gap: 12px !important;
    }
    .pdp-perks-checklist li {
      display: flex !important;
      align-items: flex-start !important;
      gap: 10px !important;
      font-size: 12.5px !important;
      line-height: 1.4 !important;
      color: #334155 !important;
    }
  }

  /* AUTH MODAL STYLING (CRISP SOLID WHITE CARD WITH HIGH CONTRAST) */
  .modal-card,
  #loginModalOverlay .modal-card,
  #indigo-signin-modal .modal-card {
    background: #FFFFFF !important;
    color: #0F172A !important;
    border-radius: 16px !important;
    width: 100% !important;
    max-width: 440px !important;
    max-height: 90vh !important;
    overflow-y: auto !important;
    padding: 32px 28px !important;
    box-sizing: border-box !important;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.45) !important;
    border: 1px solid #E2E8F0 !important;
    position: relative !important;
    z-index: 1000001 !important;
    margin: auto !important;
  }


  /* =========================================================================
     FOOTER & FLOATING WHATSAPP BUTTON MOBILE ALIGNMENT SHIELD
     ========================================================================= */
  .wa-tooltip {
    display: none !important;
  }
  @media (min-width: 901px) {
    .floating-wa-btn:hover .wa-tooltip,
    .whatsapp-float-btn:hover .wa-tooltip {
      display: block !important;
      position: absolute !important;
      right: 64px !important;
      background: #0F172A !important;
      color: #FFFFFF !important;
      padding: 6px 12px !important;
      border-radius: 6px !important;
      font-size: 12px !important;
      white-space: nowrap !important;
      font-weight: 600 !important;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
      pointer-events: none !important;
    }
  }

  @media (max-width: 900px) {
    .site-footer {
      padding: 36px 16px 84px !important; /* Extra bottom clearance so button never covers text */
      text-align: left !important;
      box-sizing: border-box !important;
      width: 100% !important;
      max-width: 100vw !important;
      overflow-x: hidden !important;
    }
    .footer-grid {
      display: flex !important;
      flex-direction: column !important;
      gap: 28px !important;
      margin-bottom: 32px !important;
      padding: 0 !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .footer-col h4 {
      margin-bottom: 12px !important;
      font-size: 14px !important;
    }
    .footer-links-list {
      gap: 8px !important;
    }
    .footer-links-list a {
      font-size: 13px !important;
    }
    .footer-bottom-bar {
      flex-direction: column !important;
      gap: 10px !important;
      text-align: center !important;
      padding-top: 20px !important;
      font-size: 11px !important;
      line-height: 1.5 !important;
    }

    /* Floating WhatsApp Button on Mobile: Compact circle, NO overflowing text */
    .whatsapp-float-btn,
    .floating-wa-btn,
    .floating-whatsapp-btn {
      position: fixed !important;
      bottom: 16px !important;
      right: 16px !important;
      width: 48px !important;
      height: 48px !important;
      border-radius: 50% !important;
      background: #25D366 !important;
      box-shadow: 0 4px 16px rgba(37, 211, 102, 0.5) !important;
      z-index: 99999 !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      padding: 0 !important;
      overflow: hidden !important;
    }
    .whatsapp-float-btn .wa-tooltip,
    .floating-wa-btn .wa-tooltip,
    .floating-whatsapp-btn .wa-tooltip {
      display: none !important; /* NEVER spill or overflow text on mobile screen */
    }
    .whatsapp-float-btn i,
    .whatsapp-float-btn svg,
    .floating-wa-btn i,
    .floating-wa-btn svg {
      width: 26px !important;
      height: 26px !important;
      display: block !important;
      margin: 0 !important;
    }
  }


  /* Universal 3D Book Opening Animation */
  .indigo-3d-book-stage:hover .indigo-3d-cover-leaf,
  .vault-card:hover .indigo-3d-cover-leaf,
  .podium-center-book:hover .podium-cover-leaf,
  .indigo-3d-book-stage.opened .indigo-3d-cover-leaf {
    transform: rotateY(-128deg) !important;
    box-shadow: -14px 18px 28px rgba(0,0,0,0.35) !important;
  }

</style>"""

MASTER_SCRIPT = """<script id="indigo-master-production-script">
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
    var brand = e.target.closest('.brand-link, .brand-wordmark, .brand-editorial-title, [aria-label*="Homepage"]');
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
</script>"""

if __name__ == '__main__':
    # Validate JS with Node
    import subprocess
    js_only = MASTER_SCRIPT.replace('<script id="indigo-master-production-script">', '').replace('</script>', '')
    with open('temp_master_check.js', 'w', encoding='utf-8') as f:
        f.write(js_only)
    res = subprocess.run(["node", "-c", "temp_master_check.js"], capture_output=True, text=True)
    if res.returncode == 0:
        print("✓ MASTER_SCRIPT has 0 JS syntax errors (validated by Node.js)")
    else:
        print("❌ Syntax error:", res.stderr)
        exit(1)
    import os
    os.remove('temp_master_check.js')
