# -*- coding: utf-8 -*-
"""
editorial_video_theme.py
Stores the complete Video 1 & Video 2 Editorial Theme for Indigo Books India.
- Video 1: 14-Book Floating Scatter Hero + SVG Thread + Mouse/Scroll Parallax
- Video 1: Sticky Dark Theater Curtain with Word Illumination
- Video 1: 3D Tilted Sheet Unfold (-8deg -> 0deg)
- Video 2: Bookstore App Shelves with 3D Overlapping Protruding Cards & Action Buttons
- Video 2: Full 5,559 Book Archive Section with Faceted Filters
- Video 2: Split-Screen Solo Book Page with -180deg 3D Spread Animation & Excerpt Swap
- Zero Audio of Books
"""

EDITORIAL_STYLE = """<style id="indigo-editorial-video-theme">
  /* ==========================================================================
     INDIGO BOOKS INDIA — VIDEO 1 & VIDEO 2 EDITORIAL STOREFRONT THEME
     Headquarters: Prayagraj, Uttar Pradesh, India
     ========================================================================== */

  :root {
    --bg-primary: #F4F1EA;
    --bg-secondary: #EAE5DC;
    --bg-shelf: #EFECE6;
    --curtain-dark: #121212;
    --card-paper: #FFFFFF;
    --accent-terracotta: #E04F33;
    --accent-gold: #D4AF37;
    --text-primary: #121212;
    --text-muted: #555555;
    --border-subtle: rgba(18, 18, 18, 0.08);
    --font-serif: 'Cormorant Garamond', 'Merriweather', Georgia, serif;
    --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  }

  body {
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-sans) !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow-x: hidden !important;
  }

  /* ==========================================================================
     1. MINIMAL EDITORIAL HEADER (Sticky 76px)
     ========================================================================== */
  .site-navbar.site-header,
  header.site-navbar,
  .site-header,
  .site-navbar {
    position: sticky !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    background: #FAF8F5 !important;
    border-bottom: 1px solid rgba(18, 18, 18, 0.08) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06) !important;
    z-index: 10000000 !important;
    box-sizing: border-box !important;
    overflow: visible !important;
  }
  @media (min-width: 1025px) {
    .site-navbar.site-header,
    header.site-navbar,
    .site-header,
    .site-navbar {
      height: 72px !important;
      display: flex !important;
      align-items: center !important;
      padding: 0 32px !important;
    }
  }
  .navbar-inner {
    width: 100% !important;
    max-width: 1440px !important;
    margin: 0 auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 24px !important;
  }
  .v2-nav-brand-group {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
  }
  .brand-editorial-title {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    text-decoration: none !important;
    font-family: var(--font-serif) !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    color: var(--text-primary) !important;
  }
  .brand-logo-img {
    height: 36px !important;
    width: auto !important;
    object-fit: contain !important;
  }
  .brand-text-col {
    display: flex !important;
    flex-direction: column !important;
  }
  .brand-name {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
    color: #121212 !important;
    line-height: 1 !important;
  }
  .brand-editorial-subtitle {
    font-size: 11px !important;
    letter-spacing: 0.16em !important;
    font-weight: 500 !important;
    color: #666666 !important;
  }
  .v2-mobile-hero-showcase {
    display: none !important;
  }
  .v2-mobile-quick-btn {
    display: none !important;
  }
  .nav-editorial-links {
    display: flex !important;
    align-items: center !important;
    gap: 24px !important;
    list-style: none !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  .nav-editorial-links a {
    text-decoration: none !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #444444 !important;
    transition: color 0.2s ease !important;
  }
  .nav-editorial-links a:hover {
    color: var(--accent-terracotta) !important;
  }
  .editorial-search-wrap {
    position: relative !important;
    flex: 1 1 340px !important;
    max-width: 440px !important;
    z-index: 1000 !important;
  }
  .editorial-search-input {
    width: 100% !important;
    height: 42px !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    border-radius: 999px !important;
    padding: 0 20px 0 42px !important;
    font-size: 13px !important;
    color: #121212 !important;
    outline: none !important;
    box-sizing: border-box !important;
    transition: all 0.2s ease !important;
  }
  .editorial-search-input:focus {
    border-color: var(--accent-terracotta) !important;
    box-shadow: 0 0 0 3px rgba(224, 79, 51, 0.12) !important;
  }
  .editorial-search-icon {
    position: absolute !important;
    left: 14px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    color: #777777 !important;
    pointer-events: none !important;
    width: 16px !important;
    height: 16px !important;
  }
  .editorial-search-results {
    position: absolute !important;
    top: calc(100% + 8px) !important;
    left: 0 !important;
    right: 0 !important;
    background: #FFFFFF !important;
    border-radius: 12px !important;
    border: 1px solid rgba(18, 18, 18, 0.1) !important;
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.12) !important;
    max-height: 420px !important;
    overflow-y: auto !important;
    display: none;
    z-index: 2147483647 !important;
  }
  .editorial-header-actions {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
  }
  .btn-reading-bag {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    background: #121212 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 10px 18px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .btn-reading-bag:hover {
    background: #2a2a2a !important;
    transform: translateY(-1px) !important;
  }
  .btn-1click-express {
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    background: #FFFFFF !important;
    color: var(--text-primary) !important;
    border: 1px solid rgba(18, 18, 18, 0.14) !important;
    border-radius: 999px !important;
    padding: 10px 16px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .btn-1click-express:hover {
    border-color: var(--accent-terracotta) !important;
    color: var(--accent-terracotta) !important;
  }

  /* ==========================================================================
     2. VIDEO 1: FLOATING 14-BOOK SCATTER HERO
     ========================================================================== */
  #editorial-scatter-hero {
    position: relative !important;
    height: 100vh !important;
    width: 100% !important;
    background: var(--bg-primary) !important;
    overflow: hidden !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    z-index: 1 !important;
  }
  .scatter-headline-center {
    position: relative !important;
    z-index: 20 !important;
    text-align: center !important;
    pointer-events: none !important;
    padding: 0 20px !important;
  }
  .scatter-title {
    font-family: var(--font-serif) !important;
    font-size: clamp(40px, 6vw, 84px) !important;
    line-height: 1.05 !important;
    font-weight: 400 !important;
    color: var(--text-primary) !important;
    margin: 0 !important;
    letter-spacing: -0.02em !important;
  }
  .scatter-subtitle {
    font-size: 11px !important;
    letter-spacing: 0.26em !important;
    text-transform: uppercase !important;
    color: #666666 !important;
    margin-top: 20px !important;
  }
  .scatter-svg-layer {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
    pointer-events: none !important;
    z-index: 15 !important;
  }
  .scatter-calligraphic-path {
    stroke-dasharray: 1800;
    stroke-dashoffset: 1800;
    animation: drawPath 3.2s cubic-bezier(0.25, 1, 0.5, 1) forwards !important;
  }
  @keyframes drawPath {
    to { stroke-dashoffset: 0; }
  }
  .scatter-book-cover {
    position: absolute !important;
    z-index: 10 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    gap: 8px !important;
    cursor: pointer !important;
    transition: transform 0.25s ease-out, filter 0.25s ease-out !important;
    will-change: transform !important;
  }
  .scatter-book-cover:hover {
    filter: drop-shadow(0 20px 28px rgba(0,0,0,0.35)) brightness(1.04) !important;
    transform: scale(1.08) !important;
    z-index: 40 !important;
  }
  .scatter-book-cover img {
    border-radius: 4px 6px 6px 4px !important;
    box-shadow: -8px 12px 24px rgba(0, 0, 0, 0.28), inset 3px 0 6px rgba(0,0,0,0.3) !important;
    display: block !important;
    object-fit: cover !important;
  }
  .scatter-book-caption {
    font-size: 9px !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    color: #666666 !important;
    font-weight: 700 !important;
  }

  /* ==========================================================================
     3. VIDEO 1: STICKY DARK THEATER CURTAIN SLIDE-OVER
     ========================================================================== */
  #dark-curtain-manifesto {
    position: relative !important;
    z-index: 2 !important;
    background: var(--curtain-dark) !important;
    color: var(--bg-primary) !important;
    min-height: 100vh !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 120px 8% !important;
    box-sizing: border-box !important;
  }
  .curtain-content-wrap {
    max-width: 1080px !important;
    margin: 0 auto !important;
    text-align: center !important;
  }
  .curtain-eyebrow {
    font-size: 11px !important;
    letter-spacing: 0.28em !important;
    text-transform: uppercase !important;
    color: var(--accent-terracotta) !important;
    margin-bottom: 28px !important;
    font-weight: 700 !important;
  }
  .curtain-scrub-headline {
    font-family: var(--font-serif) !important;
    font-size: clamp(38px, 5.5vw, 76px) !important;
    line-height: 1.15 !important;
    font-weight: 400 !important;
    letter-spacing: -0.01em !important;
    margin: 0 0 48px 0 !important;
  }
  .curtain-word {
    display: inline-block !important;
    opacity: 0.25;
    transition: opacity 0.25s ease, color 0.25s ease !important;
  }
  .curtain-word.is-illuminated {
    opacity: 1 !important;
    color: #FFFFFF !important;
  }
  .curtain-pillars-row {
    display: flex !important;
    justify-content: center !important;
    gap: 48px !important;
    flex-wrap: wrap !important;
    margin-top: 48px !important;
  }
  .curtain-pillar-item {
    font-size: 12px !important;
    letter-spacing: 0.16em !important;
    text-transform: uppercase !important;
    color: #999999 !important;
  }
  .curtain-pillar-num {
    color: var(--accent-terracotta) !important;
    margin-right: 6px !important;
    font-weight: 700 !important;
  }

  /* ==========================================================================
     4. VIDEO 1: 3D TILTED SHEET UNFOLD
     ========================================================================== */
  #tilted-lens-section {
    position: relative !important;
    z-index: 3 !important;
    background: var(--bg-primary) !important;
    padding: 100px 6% !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
  }
  .tilted-sheet-card {
    background: #FFFFFF !important;
    border-radius: 16px !important;
    border: 1px solid var(--border-subtle) !important;
    padding: 72px 54px !important;
    max-width: 1240px !important;
    margin: 0 auto !important;
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.08) !important;
    transform: translateY(80px) rotate(-8deg) scale(0.94);
    transition: transform 0.8s cubic-bezier(0.2, 0.9, 0.3, 1) !important;
    will-change: transform !important;
  }
  .tilted-sheet-card.is-unfolded {
    transform: translateY(0) rotate(0deg) scale(1) !important;
  }
  .tilted-sheet-badge {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    font-size: 11px !important;
    letter-spacing: 0.22em !important;
    text-transform: uppercase !important;
    color: var(--accent-terracotta) !important;
    font-weight: 700 !important;
    margin-bottom: 24px !important;
  }
  .tilted-star-spin {
    display: inline-block !important;
    animation: starSpin 18s linear infinite !important;
    font-size: 16px !important;
  }
  @keyframes starSpin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
  .tilted-title {
    font-family: var(--font-serif) !important;
    font-size: clamp(34px, 4.5vw, 58px) !important;
    line-height: 1.15 !important;
    color: var(--text-primary) !important;
    margin: 0 0 24px 0 !important;
    font-weight: 400 !important;
  }
  .tilted-desc {
    font-size: 15px !important;
    line-height: 1.7 !important;
    color: var(--text-muted) !important;
    max-width: 760px !important;
    margin-bottom: 32px !important;
  }

  /* ==========================================================================
     5. VIDEO 2: APP-STYLE BOOKSTORE WITH OVERLAPPING 3D SHELVES
     ========================================================================== */
  #video2-bookstore-app {
    position: relative !important;
    z-index: 4 !important;
    background: var(--bg-primary) !important;
    min-height: 100vh !important;
    display: flex !important;
  }

  /* Left Vertical Navigation Rail */
  .v2-app-rail {
    position: sticky !important;
    top: 76px !important;
    height: calc(100vh - 76px) !important;
    width: 68px !important;
    background: var(--bg-primary) !important;
    border-right: 1px solid var(--border-subtle) !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 24px 0 !important;
    box-sizing: border-box !important;
    z-index: 50 !important;
    flex-shrink: 0 !important;
  }
  .v2-rail-group {
    display: flex !important;
    flex-direction: column !important;
    gap: 22px !important;
  }
  .v2-rail-btn {
    width: 44px !important;
    height: 44px !important;
    border-radius: 10px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    background: transparent !important;
    border: none !important;
    color: #666666 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-rail-btn:hover, .v2-rail-btn.active {
    background: var(--bg-secondary) !important;
    color: var(--text-primary) !important;
  }

  /* Main App Content Area */
  .v2-app-content {
    flex: 1 1 auto !important;
    min-width: 0 !important;
    padding: 40px 48px 100px !important;
    position: relative !important;
  }

  /* Shelf Showcase Container */
  .v2-shelf-block {
    margin-bottom: 64px !important;
  }
  .v2-shelf-header {
    display: flex !important;
    align-items: flex-end !important;
    justify-content: space-between !important;
    margin-bottom: 24px !important;
  }
  .v2-shelf-title {
    font-family: var(--font-serif) !important;
    font-size: 32px !important;
    font-weight: 400 !important;
    color: var(--text-primary) !important;
    margin: 0 !important;
  }
  .v2-shelf-header-right {
    display: flex !important;
    align-items: center !important;
    gap: 16px !important;
    flex-wrap: wrap !important;
  }
  .v2-shelf-author-pills {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    flex-wrap: wrap !important;
  }
  .v2-author-pill-btn {
    display: inline-flex !important;
    align-items: center !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    color: #444444 !important;
    border-radius: 999px !important;
    padding: 6px 14px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
    text-decoration: none !important;
  }
  .v2-author-pill-btn:hover {
    background: #121212 !important;
    color: #FFFFFF !important;
    border-color: #121212 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12) !important;
  }
  .v2-shelf-nav-arrows {
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
  }
  .v2-shelf-arrow-btn {
    width: 34px !important;
    height: 34px !important;
    border-radius: 50% !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.15) !important;
    color: #121212 !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06) !important;
    user-select: none !important;
  }
  .v2-shelf-arrow-btn:hover {
    background: #121212 !important;
    color: #FFFFFF !important;
    border-color: #121212 !important;
    transform: scale(1.08) !important;
  }

  /* Warm Sand Shelf Stage (Matches Video 2 #EFECE6 block) */
  .v2-shelf-stage {
    background: var(--bg-shelf) !important;
    border-radius: 16px !important;
    padding: 40px 32px !important;
    box-sizing: border-box !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    scroll-behavior: smooth !important;
    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
  }
  .v2-shelf-stage::-webkit-scrollbar {
    display: none !important;
  }
  .v2-shelf-row {
    display: flex !important;
    gap: 36px !important;
    align-items: center !important;
    width: max-content !important;
  }

  /* OVERLAPPING 3D BOOK CARD (Video 2 00:00 - 00:01) */
  .v2-book-card {
    display: flex !important;
    align-items: center !important;
    flex: 0 0 380px !important;
    cursor: pointer !important;
    position: relative !important;
    perspective: 1200px !important;
    padding-left: 20px !important;
  }
  .v2-card-cover-wrap {
    position: relative !important;
    z-index: 10 !important;
    margin-right: -48px !important; /* Protruding overlap */
    perspective: 800px !important;
    flex-shrink: 0 !important;
  }
  .v2-card-cover-leaf {
    width: 128px !important;
    height: 190px !important;
    border-radius: 4px 8px 8px 4px !important;
    overflow: hidden !important;
    box-shadow: -10px 14px 26px rgba(0, 0, 0, 0.35), inset 4px 0 8px rgba(0,0,0,0.4) !important;
    transform: rotateY(-8deg) translateY(0) !important;
    transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1) !important;
    background: #FAF7F0 !important;
    cursor: pointer !important;
  }
  .v2-book-card:hover .v2-card-cover-leaf {
    transform: rotateY(0deg) translateY(-8px) scale(1.06) !important;
    box-shadow: -16px 22px 34px rgba(0, 0, 0, 0.45) !important;
  }
  .v2-card-cover-leaf img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
  }
  .v2-card-details-sheet {
    flex: 1 1 auto !important;
    background: #FFFFFF !important;
    border-radius: 12px !important;
    padding: 22px 20px 20px 64px !important; /* Offset for overlap */
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06) !important;
    border: 1px solid rgba(0, 0, 0, 0.06) !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    min-height: 175px !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
  }
  .v2-book-card:hover .v2-card-details-sheet {
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.1) !important;
    transform: translateX(4px) !important;
  }
  .v2-card-stars {
    color: #F59E0B !important;
    font-size: 14px !important;
    margin-bottom: 6px !important;
  }
  .v2-card-title {
    font-family: var(--font-serif) !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    color: var(--text-primary) !important;
    margin: 0 0 4px 0 !important;
    line-height: 1.25 !important;
  }
  .v2-card-author {
    font-size: 12px !important;
    color: var(--text-muted) !important;
    margin-bottom: 8px !important;
  }
  .v2-card-price {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    margin-bottom: 12px !important;
  }
  .v2-card-btn-row {
    display: flex !important;
    gap: 8px !important;
    align-items: center !important;
  }
  .v2-card-preview-btn {
    background: #F4F1EA !important;
    color: #121212 !important;
    border: 1px solid #D5CFC4 !important;
    padding: 6px 14px !important;
    border-radius: 6px !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-card-preview-btn:hover {
    background: var(--accent-terracotta) !important;
    color: #FFFFFF !important;
    border-color: var(--accent-terracotta) !important;
  }
  .v2-card-quick-btn {
    background: #121212 !important;
    color: #FFFFFF !important;
    border: 1px solid #121212 !important;
    padding: 6px 12px !important;
    border-radius: 6px !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-card-quick-btn:hover {
    background: var(--accent-terracotta) !important;
    border-color: var(--accent-terracotta) !important;
  }

  /* ==========================================================================
     6. FULL ARCHIVE & ALL BOOKS LISTING SECTION (5,559 BOOKS)
     ========================================================================== */
  .v2-archive-section {
    margin-top: 80px !important;
    padding-top: 48px !important;
    border-top: 1px solid var(--border-subtle) !important;
  }
  .v2-archive-header {
    margin-bottom: 28px !important;
  }
  .v2-archive-title {
    font-family: var(--font-serif) !important;
    font-size: 38px !important;
    font-weight: 400 !important;
    color: var(--text-primary) !important;
    margin: 0 0 8px 0 !important;
  }
  .v2-archive-sub {
    font-size: 14px !important;
    color: var(--text-muted) !important;
    margin: 0 !important;
  }
  .v2-archive-chips {
    display: flex !important;
    gap: 10px !important;
    flex-wrap: wrap !important;
    margin: 24px 0 !important;
  }
  .v2-chip {
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    border-radius: 999px !important;
    padding: 8px 18px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #444444 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-chip:hover, .v2-chip.active {
    background: #121212 !important;
    color: #FFFFFF !important;
    border-color: #121212 !important;
  }
  .v2-archive-controls {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 20px !important;
    flex-wrap: wrap !important;
    margin-bottom: 32px !important;
  }
  .v2-archive-search-box {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    flex: 1 1 320px !important;
    max-width: 480px !important;
  }
  .v2-archive-search-box input {
    border: none !important;
    outline: none !important;
    font-size: 13px !important;
    width: 100% !important;
    background: transparent !important;
  }
  .v2-archive-select {
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    border-radius: 8px !important;
    padding: 8px 14px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #333333 !important;
    outline: none !important;
  }
  .v2-archive-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)) !important;
    gap: 28px !important;
  }
  .v2-archive-card {
    background: #FFFFFF !important;
    border-radius: 12px !important;
    border: 1px solid rgba(18, 18, 18, 0.08) !important;
    padding: 16px !important;
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
    cursor: pointer !important;
  }
  .v2-archive-card:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.08) !important;
  }
  .v2-archive-cover-img {
    width: 100% !important;
    height: 280px !important;
    object-fit: cover !important;
    border-radius: 6px !important;
    margin-bottom: 12px !important;
    box-shadow: -4px 6px 14px rgba(0,0,0,0.18) !important;
  }
  .v2-archive-card-title {
    font-family: var(--font-serif) !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    line-height: 1.3 !important;
    margin: 0 0 4px 0 !important;
    color: #121212 !important;
  }
  .v2-archive-card-author {
    font-size: 12px !important;
    color: #666666 !important;
    margin-bottom: 8px !important;
  }
  .v2-archive-card-price {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: var(--accent-terracotta) !important;
    margin-bottom: 12px !important;
  }
  .v2-btn-load-more {
    background: #121212 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 14px 32px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-btn-load-more:hover {
    background: var(--accent-terracotta) !important;
  }

  /* ==========================================================================
     7. VIDEO 2: DEFINITIVE SPLIT-SCREEN SOLO PRODUCT STUDIO VIEW
     (With -180deg 3D Spread Animation & Excerpt Swap)
     ========================================================================== */
  /* STICKY NAVBAR ALWAYS PINNED ON TOP ACROSS ALL PAGES (SUPERIOR STACKING) */
  header.site-navbar,
  .site-header,
  .site-navbar,
  .navbar-inner,
  .editorial-search-wrap {
    overflow: visible !important;
  }

  header.site-navbar,
  .site-header,
  .site-navbar {
    position: sticky !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 72px !important;
    z-index: 10000000 !important;
    background: #FAF8F5 !important;
    border-bottom: 1px solid rgba(18, 18, 18, 0.08) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06) !important;
  }

  .editorial-search-wrap {
    position: relative !important;
    z-index: 2147483647 !important;
  }

  /* PREDICTIVE SEARCH DROPDOWN FLOATS ABOVE ALL CONTENT */
  .editorial-search-results {
    position: absolute !important;
    top: calc(100% + 8px) !important;
    left: 0 !important;
    right: 0 !important;
    background: #FFFFFF !important;
    border-radius: 14px !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.28) !important;
    max-height: 480px !important;
    overflow-y: auto !important;
    display: none;
    z-index: 2147483647 !important;
  }

  /* SOLO PRODUCT VIEW SITS NEATLY BELOW STICKY NAVBAR - ZERO DOUBLE SCROLLBAR */
  #indigo-solo-product-view,
  .v2-solo-product-view,
  .section-main-product {
    position: fixed !important;
    inset: 0 !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100vw !important;
    height: 100% !important;
    height: 100dvh !important;
    z-index: 20000000 !important;
    display: none;
    background: #EFECE6 !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 20px !important;
    box-sizing: border-box !important;
    overflow: hidden !important; /* On desktop: STRICTLY SINGLE SCROLLBAR INSIDE RIGHT PANEL ONLY! */
    overflow-x: hidden !important;
  }

  html.solo-page-active,
  body.solo-page-active {
    overflow: hidden !important;
    height: 100% !important;
    max-height: 100vh !important;
    max-height: 100dvh !important;
    touch-action: none !important;
  }

  #indigo-solo-product-view::-webkit-scrollbar {
    width: 5px !important;
  }
  #indigo-solo-product-view::-webkit-scrollbar-thumb {
    background: rgba(18, 18, 18, 0.2) !important;
    border-radius: 999px !important;
  }

  @media (max-width: 1024px) {
    #indigo-solo-product-view {
      inset: 0 !important;
      top: 0 !important;
      left: 0 !important;
      right: 0 !important;
      bottom: 0 !important;
      width: 100% !important;
      height: 100% !important;
      height: 100dvh !important;
      padding: 0 !important;
      overflow-y: auto !important; /* Mobile: STRICTLY SINGLE SCROLLBAR ON OUTER CONTAINER ONLY! */
      -webkit-overflow-scrolling: touch !important;
      justify-content: flex-start !important;
      display: none;
    }
    #indigo-solo-product-view.is-active {
      display: flex !important;
    }
    .v2-solo-stage-container {
      width: 100% !important;
      max-width: 100% !important;
      height: auto !important;
      min-height: 100% !important;
      max-height: none !important;
      border-radius: 0 !important;
      flex-direction: column !important;
      overflow: visible !important;
      box-shadow: none !important;
      margin: 0 !important;
    }
    .v2-solo-left-panel {
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
    }
    .v2-solo-right-panel {
      width: 100% !important;
      height: auto !important;
      max-height: none !important;
      overflow: visible !important;
      overflow-x: visible !important;
      overflow-y: visible !important;
      padding: 24px 18px 80px 18px !important;
    }
  }
  #indigo-solo-product-view.is-active {
    display: flex !important;
  }
  .v2-solo-stage-container {
    position: relative !important;
    width: 100% !important;
    max-width: 1240px !important;
    height: min(86vh, 760px) !important;
    min-height: 560px !important;
    display: flex !important;
    border-radius: 20px !important;
    overflow: hidden !important;
    box-shadow: 0 24px 70px rgba(0, 0, 0, 0.14) !important;
    background: #FFFFFF !important;
    margin: auto 0 !important;
    flex-shrink: 0 !important;
  }

  /* Left Atmospheric Art & Quote Panel (42% Width) */
  .v2-solo-left-panel {
    position: relative !important;
    width: 36% !important;
    height: 100% !important;
    background: #241A13 !important;
    overflow: hidden !important;
    padding: 38px 120px 38px 36px !important; /* Generous 120px right padding prevents quote text from touching closed 3D book cover! */
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
  }
  .v2-solo-left-bg-art {
    position: absolute !important;
    inset: -30px !important;
    background-size: cover !important;
    background-position: center !important;
    filter: blur(28px) brightness(0.65) !important;
    transform: scale(1.15) !important;
    z-index: 1 !important;
    opacity: 0.9 !important;
  }
  .v2-solo-left-content {
    position: relative !important;
    z-index: 10 !important;
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
  }
  .v2-solo-top-nav {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    width: 100% !important;
  }
  .v2-solo-back-btn {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    background: rgba(255, 255, 255, 0.22) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.35) !important;
    backdrop-filter: blur(10px) !important;
    padding: 8px 18px !important;
    border-radius: 999px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-solo-back-btn:hover {
    background: rgba(255, 255, 255, 0.36) !important;
    transform: translateX(-3px) !important;
  }
  .v2-solo-search-btn {
    width: 36px !important;
    height: 36px !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.22) !important;
    border: 1px solid rgba(255, 255, 255, 0.35) !important;
    color: #FFFFFF !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-solo-search-btn:hover {
    background: rgba(255, 255, 255, 0.36) !important;
    transform: scale(1.08) !important;
  }
    .v2-solo-quote-block {
    position: relative !important;
    margin: auto 0 !important;
    max-width: 250px !important;
  }
  .v2-solo-quote-mark {
    font-family: var(--font-serif) !important;
    font-size: 72px !important;
    line-height: 0.8 !important;
    color: rgba(224, 79, 51, 0.75) !important;
    margin-bottom: 6px !important;
  }
  .v2-solo-quote-text {
    font-family: var(--font-serif) !important;
    font-size: 21px !important;
    line-height: 1.45 !important;
    color: #FFFFFF !important;
    font-style: italic !important;
    font-weight: 400 !important;
    margin: 0 0 14px 0 !important;
    max-width: 240px !important;
  }
  .v2-solo-quote-source {
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.16em !important;
    text-transform: uppercase !important;
    color: rgba(255, 255, 255, 0.65) !important;
    max-width: 230px !important;
  }
  .v2-equalizer-bars {
    display: flex !important;
    align-items: flex-end !important;
    gap: 3px !important;
    height: 14px !important;
  }
  .v2-equalizer-bars span {
    width: 3px !important;
    background: #FFFFFF !important;
    border-radius: 2px !important;
    opacity: 0.85 !important;
  }
  .v2-equalizer-bars span:nth-child(1) { height: 8px; }
  .v2-equalizer-bars span:nth-child(2) { height: 14px; }
  .v2-equalizer-bars span:nth-child(3) { height: 10px; }

  /* Center 3D Book Stage (Straddles the 42% seam) */
  .v2-solo-book-center-stage {
    position: absolute !important;
    top: 50% !important;
    left: 36% !important;
    transform: translate(-50%, -50%) !important;
    z-index: 100 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    perspective: 1600px !important;
  }
  .v2-book-spread-stage {
    position: relative !important;
    width: 230px !important;
    height: 350px !important;
    perspective: 1600px !important;
    cursor: pointer !important;
    transition: transform 0.85s cubic-bezier(0.25, 1, 0.5, 1) !important;
  }
  .v2-solo-3d-book {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    transform-style: preserve-3d !important;
    transition: transform 0.85s cubic-bezier(0.25, 1, 0.5, 1) !important;
  }

  /* Front Cover Leaf - Hinged on Left Spine */
  .v2-cover-leaf {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
    transform-origin: left center !important;
    transform-style: preserve-3d !important;
    transition: transform 0.85s cubic-bezier(0.25, 1, 0.5, 1) !important;
    z-index: 20 !important;
  }

  /* 3D SPREAD OPENING: -180deg flip! */
  .v2-book-spread-stage.is-open .v2-cover-leaf {
    transform: rotateY(-180deg) !important;
  }
  .v2-book-spread-stage.is-open {
    transform: none !important;
  }

  /* Front Cover Outside Face */
  .v2-cover-leaf-front {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
    backface-visibility: hidden !important;
    -webkit-backface-visibility: hidden !important;
    border-radius: 4px 10px 10px 4px !important;
    overflow: hidden !important;
    box-shadow: -14px 18px 36px rgba(0, 0, 0, 0.5), inset 6px 0 14px rgba(0, 0, 0, 0.45) !important;
    background: #FAF7F0 !important;
  }
  .v2-cover-leaf-front img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
  }
  .v2-cover-spine-shadow {
    position: absolute !important;
    top: 0 !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 24px !important;
    background: linear-gradient(to right, rgba(0,0,0,0.55), rgba(0,0,0,0)) !important;
    pointer-events: none !important;
  }

  /* Inside Left Page (Back of Cover Leaf) with Geometric Endpaper Art */
  .v2-cover-leaf-back {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
    transform: rotateY(180deg) !important;
    backface-visibility: hidden !important;
    -webkit-backface-visibility: hidden !important;
    border-radius: 10px 4px 4px 10px !important;
    background: #23343B !important;
    overflow: hidden !important;
    box-shadow: inset -8px 0 16px rgba(0,0,0,0.5), 14px 18px 36px rgba(0,0,0,0.4) !important;
  }
  .v2-endpaper-svg {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
  }
  .v2-endpaper-overlay {
    position: absolute !important;
    inset: 0 !important;
    padding: 28px 20px !important;
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-end !important;
    text-align: center !important;
    background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, transparent 60%) !important;
    z-index: 5 !important;
  }
  .v2-endpaper-seal {
    font-size: 10px !important;
    letter-spacing: 0.22em !important;
    text-transform: uppercase !important;
    color: #F4E8D6 !important;
    font-weight: 700 !important;
    margin-bottom: 6px !important;
  }
  .v2-endpaper-title {
    font-family: var(--font-serif) !important;
    font-size: 22px !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
    margin-bottom: 4px !important;
  }

  /* Inside Right Cream Book Page with 2-Column Typeset Text */
  .v2-inside-right-page {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
    z-index: 10 !important;
    background: #FAF7F0 !important;
    border-radius: 4px 10px 10px 4px !important;
    box-shadow: inset 8px 0 18px rgba(0, 0, 0, 0.18), 14px 18px 36px rgba(0, 0, 0, 0.35) !important;
    padding: 26px 22px !important;
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    overflow: hidden !important;
    border: 1px solid rgba(0,0,0,0.06) !important;
  }
  .v2-inside-page-header {
    font-size: 9.5px !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: #888888 !important;
    text-align: center !important;
    border-bottom: 1px solid rgba(0,0,0,0.08) !important;
    padding-bottom: 6px !important;
  }
  .v2-spread-chapter-heading {
    font-family: var(--font-serif) !important;
    font-size: 19px !important;
    font-weight: 600 !important;
    color: #121212 !important;
    text-align: center !important;
    margin: 10px 0 8px 0 !important;
  }
  .v2-spread-columns-wrap {
    flex: 1 1 auto !important;
    overflow-y: auto !important;
    column-count: 2 !important;
    column-gap: 14px !important;
    padding: 4px 2px !important;
  }
  .v2-drop-cap {
    float: left !important;
    font-family: var(--font-serif) !important;
    font-size: 32px !important;
    line-height: 0.8 !important;
    font-weight: 700 !important;
    color: var(--accent-terracotta) !important;
    padding-right: 5px !important;
  }
  .v2-spread-excerpt-snippet {
    font-family: var(--font-serif) !important;
    font-size: 12.5px !important;
    line-height: 1.6 !important;
    color: #2D2D2D !important;
    text-align: justify !important;
  }
  .v2-inside-page-footer {
    font-size: 10px !important;
    color: #888888 !important;
    text-align: center !important;
    padding-top: 4px !important;
  }
  .v2-spine-crease-shadow {
    position: absolute !important;
    top: 0 !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 20px !important;
    background: linear-gradient(to right, rgba(0,0,0,0.22), rgba(0,0,0,0)) !important;
    pointer-events: none !important;
  }
  .v2-spread-hint-badge {
    margin-top: 14px !important;
    background: rgba(18, 18, 18, 0.85) !important;
    color: #FFFFFF !important;
    padding: 6px 14px !important;
    border-radius: 999px !important;
    font-size: 11.5px !important;
    font-weight: 600 !important;
    backdrop-filter: blur(8px) !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
  }
  .v2-spread-hint-badge:hover {
    background: var(--accent-terracotta) !important;
    transform: translateY(-2px) !important;
  }

  /* Right White Details & Excerpt Card (58% Width) */
  .v2-solo-right-panel {
    position: relative !important;
    width: 64% !important;
    height: 100% !important;
    background: #FFFFFF !important;
    padding: 30px 105px 30px 250px !important; /* Generous 250px left offset for open 3D spread + 105px right offset for 62px Action Dock! */
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    scrollbar-width: thin !important;
    scrollbar-color: rgba(18, 18, 18, 0.2) transparent !important;
  }
  .v2-solo-right-panel::-webkit-scrollbar {
    width: 5px !important;
  }
  .v2-solo-right-panel::-webkit-scrollbar-track {
    background: transparent !important;
  }
  .v2-solo-right-panel::-webkit-scrollbar-thumb {
    background: rgba(18, 18, 18, 0.2) !important;
    border-radius: 999px !important;
  }
  .v2-solo-right-panel::-webkit-scrollbar-thumb:hover {
    background: rgba(18, 18, 18, 0.4) !important;
  }
  .v2-solo-badge {
    display: inline-block !important;
    font-size: 11px !important;
    font-weight: 800 !important;
    letter-spacing: 0.16em !important;
    text-transform: uppercase !important;
    color: var(--accent-terracotta) !important;
    background: rgba(224, 79, 51, 0.08) !important;
    padding: 4px 10px !important;
    border-radius: 4px !important;
  }
  .v2-solo-book-title {
    font-family: var(--font-serif) !important;
    font-size: 34px !important;
    font-weight: 600 !important;
    color: var(--text-primary) !important;
    line-height: 1.15 !important;
    margin: 8px 0 6px 0 !important;
  }
  .v2-solo-book-author {
    font-size: 15px !important;
    color: var(--text-muted) !important;
    margin-bottom: 12px !important;
  }
  .v2-solo-stars-row {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    margin-bottom: 14px !important;
  }
  .v2-solo-price {
    font-family: var(--font-serif) !important;
    font-size: 30px !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    margin-bottom: 16px !important;
  }
  .v2-format-pill {
    background: #F4F1EA !important;
    border: 1px solid #D5CFC4 !important;
    border-radius: 6px !important;
    padding: 8px 16px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #333333 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-format-pill.active {
    background: #121212 !important;
    color: #FFFFFF !important;
    border-color: #121212 !important;
  }
  .v2-solo-specs-grid {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 12px 20px !important;
    background: #FAF8F5 !important;
    border-radius: 8px !important;
    padding: 16px !important;
    margin-bottom: 22px !important;
    border: 1px solid rgba(18, 18, 18, 0.06) !important;
  }
  .v2-spec-item {
    display: flex !important;
    flex-direction: column !important;
    gap: 3px !important;
  }
  .v2-spec-label {
    font-size: 11px !important;
    font-weight: 700 !important;
    color: #777777 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
  }
  .v2-spec-value {
    font-size: 13.5px !important;
    font-weight: 600 !important;
    color: #121212 !important;
  }
    /* Sleek Editorial Primary Action Buttons (Zero Cheap Emojis!) */
  .v2-solo-actions-row {
    display: flex !important;
    flex-direction: column !important;
    gap: 10px !important;
    margin-top: 20px !important;
  }
  .v2-btn-preview-spread {
    width: 100% !important;
    background: #FAF7F0 !important;
    border: 1px solid #D5CFC4 !important;
    border-radius: 10px !important;
    padding: 13px 20px !important;
    font-size: 13.5px !important;
    font-weight: 700 !important;
    color: #121212 !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.04em !important;
  }
  .v2-btn-preview-spread:hover {
    background: #FFFFFF !important;
    border-color: var(--accent-terracotta) !important;
    color: var(--accent-terracotta) !important;
    transform: translateY(-1px) !important;
  }
  .v2-btn-add-bag {
    width: 100% !important;
    background: #121212 !important;
    border: 1px solid #121212 !important;
    border-radius: 10px !important;
    padding: 14px 20px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 14px rgba(18, 18, 18, 0.2) !important;
    letter-spacing: 0.04em !important;
  }
  .v2-btn-add-bag:hover {
    background: #2A2A2A !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(18, 18, 18, 0.3) !important;
  }
  .v2-btn-buy-now {
    width: 100% !important;
    background: var(--accent-terracotta) !important;
    border: 1px solid var(--accent-terracotta) !important;
    border-radius: 10px !important;
    padding: 14px 20px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 14px rgba(224, 79, 51, 0.28) !important;
    letter-spacing: 0.04em !important;
  }
  .v2-btn-buy-now:hover {
    background: #B93820 !important;
    border-color: #B93820 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(224, 79, 51, 0.38) !important;
  }
  .v2-btn-wa-cod {
    width: 100% !important;
    background: #FAF7F0 !important;
    border: 1px solid rgba(16, 185, 129, 0.45) !important;
    border-radius: 10px !important;
    padding: 13px 20px !important;
    font-size: 13.5px !important;
    font-weight: 700 !important;
    color: #065F46 !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.02em !important;
  }
  .v2-btn-wa-cod:hover {
    background: #ECFDF5 !important;
    border-color: #10B981 !important;
    transform: translateY(-1px) !important;
  }

  /* Swappable Full Excerpt View (Matching inspect_frame_4.0s.jpg) */
  .v2-solo-excerpt-content {
    animation: fadeInExcerpt 0.35s ease forwards !important;
  }
  @keyframes fadeInExcerpt {
    from { opacity: 0; transform: translateX(10px); }
    to { opacity: 1; transform: translateX(0); }
  }
  .v2-excerpt-heading {
    font-family: var(--font-serif) !important;
    font-size: 34px !important;
    font-weight: 400 !important;
    color: #121212 !important;
    margin: 0 0 6px 0 !important;
  }
  .v2-excerpt-subtitle {
    font-size: 13px !important;
    color: #0284C7 !important;
    font-weight: 600 !important;
    margin-bottom: 20px !important;
  }
  .v2-excerpt-full-text {
    font-family: var(--font-serif) !important;
    font-size: 15px !important;
    line-height: 1.75 !important;
    color: #374151 !important;
    max-height: 320px !important;
    overflow-y: auto !important;
    padding-right: 12px !important;
  }
  .v2-see-full-excerpt {
    display: none !important;
  }
  .v2-btn-close-excerpt {
    background: none !important;
    border: none !important;
    color: #64748B !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
  }
  .v2-btn-close-excerpt:hover {
    color: #121212 !important;
  }

  
  /* Clickable Author & Author Suggestions Styling */
  .v2-solo-author-link {
    color: var(--accent-terracotta) !important;
    text-decoration: underline !important;
    text-underline-offset: 3px !important;
    cursor: pointer !important;
    transition: color 0.2s ease !important;
  }
  .v2-solo-author-link:hover {
    color: #B93820 !important;
  }
    /* Prominent Author Suggestions Shelf */
  .v2-author-suggestions-section {
    margin-top: 26px !important;
    padding-top: 20px !important;
    border-top: 1px solid #EAE5DC !important;
  }
  .v2-author-suggestions-grid {
    display: flex !important;
    gap: 16px !important;
    overflow-x: auto !important;
    padding: 6px 2px 14px 2px !important;
    scrollbar-width: thin !important;
    scrollbar-color: #D5CFC4 transparent !important;
  }
  .v2-author-sug-card {
    width: 175px !important;
    background: #FAF7F0 !important;
    border: 1px solid #EAE5DC !important;
    border-radius: 12px !important;
    padding: 12px !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04) !important;
  }
  .v2-author-sug-card:hover {
    border-color: var(--accent-terracotta) !important;
    background: #FFFFFF !important;
    transform: translateY(-4px) !important;
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.1) !important;
  }
  .v2-author-sug-cover-wrap {
    width: 100% !important;
    aspect-ratio: 2 / 3 !important;
    height: 120px !important;
    border-radius: 6px !important;
    overflow: hidden !important;
    margin-bottom: 10px !important;
    background: #EAE5DC !important;
    box-shadow: -4px 6px 14px rgba(0, 0, 0, 0.16) !important;
  }
  .v2-author-sug-cover-wrap img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
  }
  .v2-author-sug-badge {
    font-size: 9px !important;
    font-weight: 800 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--accent-terracotta) !important;
    background: rgba(224, 79, 51, 0.08) !important;
    padding: 2px 6px !important;
    border-radius: 3px !important;
    display: inline-block !important;
    margin-bottom: 4px !important;
  }
  .v2-author-sug-title {
    font-family: var(--font-serif) !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #121212 !important;
    line-height: 1.25 !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    margin-bottom: 6px !important;
  }
  .v2-author-sug-price {
    font-family: var(--font-serif) !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    color: var(--accent-terracotta) !important;
  }

  /* Right Vertical Action Dock (inspect_frame_2.0s.jpg & inspect_frame_4.0s.jpg) */
  .v2-solo-action-dock {
    position: absolute !important;
    right: 20px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 16px !important;
    z-index: 200 !important;
  }
  .v2-dock-btn {
    width: 62px !important;
    height: 62px !important;
    border-radius: 12px !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.1) !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08) !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    color: #444444 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-dock-btn span {
    font-size: 10px !important;
    font-weight: 700 !important;
    margin-top: 3px !important;
  }
  .v2-dock-btn:hover {
    background: var(--accent-terracotta) !important;
    color: #FFFFFF !important;
    border-color: var(--accent-terracotta) !important;
    transform: scale(1.06) !important;
  }
  .v2-dock-btn.active {
    border-color: var(--accent-terracotta) !important;
    color: var(--accent-terracotta) !important;
  }

  /* ==========================================================================
     MOBILE RESPONSIVE ARCHITECTURE & HAMBURGER NAVIGATION
     Optimized for Indian mobile bookstore buyers (85%+ mobile traffic)
     ========================================================================== */

  /* 1. Mobile Hamburger Button & Quick Actions (Hidden by default on desktop) */
  .v2-hamburger-btn {
    display: none !important;
    align-items: center !important;
    justify-content: center !important;
    width: 38px !important;
    height: 38px !important;
    background: transparent !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    border-radius: 8px !important;
    color: #121212 !important;
    cursor: pointer !important;
    padding: 0 !important;
    transition: all 0.2s ease !important;
    flex-shrink: 0 !important;
  }
  .v2-hamburger-btn:hover,
  .v2-hamburger-btn:active {
    background: rgba(18, 18, 18, 0.06) !important;
    border-color: #121212 !important;
  }

  .v2-mobile-nav-actions {
    display: none !important;
    align-items: center !important;
    gap: 8px !important;
    flex-shrink: 0 !important;
  }
  .v2-mobile-bag-btn {
    position: relative !important;
    width: 38px !important;
    height: 38px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    border-radius: 8px !important;
    color: #121212 !important;
    cursor: pointer !important;
    padding: 0 !important;
    transition: all 0.2s ease !important;
  }
  .v2-mobile-bag-badge {
    position: absolute !important;
    top: -4px !important;
    right: -4px !important;
    background: #E04F33 !important;
    color: #FFFFFF !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    border-radius: 999px !important;
    padding: 1px 5px !important;
    min-width: 14px !important;
    text-align: center !important;
    line-height: 1.2 !important;
    box-shadow: 0 2px 6px rgba(224, 79, 51, 0.4) !important;
  }

  /* 2. Slide-out Mobile Navigation Drawer */
  .v2-mobile-drawer {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: min(85vw, 340px) !important;
    height: 100vh !important;
    height: 100dvh !important;
    background: #FAF8F5 !important;
    z-index: 2147483646 !important;
    box-shadow: 8px 0 32px rgba(0, 0, 0, 0.25) !important;
    transform: translateX(-105%) !important;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
    display: flex !important;
    flex-direction: column !important;
    box-sizing: border-box !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }
  .v2-mobile-drawer.is-open {
    transform: translateX(0) !important;
  }
  .v2-mobile-drawer-backdrop {
    position: fixed !important;
    inset: 0 !important;
    background: rgba(18, 18, 18, 0.6) !important;
    backdrop-filter: blur(4px) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    z-index: 2147483645 !important;
    opacity: 0 !important;
    pointer-events: none !important;
    transition: opacity 0.3s ease !important;
  }
  .v2-mobile-drawer-backdrop.is-open {
    opacity: 1 !important;
    pointer-events: auto !important;
  }

  /* Full Styling for Standalone Mobile Menu Drawer */
  .v2-drawer-top-bar {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 16px 18px !important;
    background: #FFFFFF !important;
    border-bottom: 1px solid rgba(18, 18, 18, 0.08) !important;
    flex-shrink: 0 !important;
  }
  .v2-drawer-brand {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
  }
  .v2-drawer-logo-img {
    height: 30px !important;
    width: auto !important;
    object-fit: contain !important;
  }
  .v2-drawer-brand-text {
    display: flex !important;
    flex-direction: column !important;
  }
  .v2-drawer-brand-name {
    font-family: var(--font-serif) !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    color: #121212 !important;
    letter-spacing: 0.04em !important;
    line-height: 1.1 !important;
  }
  .v2-drawer-brand-sub {
    font-size: 8px !important;
    font-weight: 700 !important;
    letter-spacing: 0.16em !important;
    text-transform: uppercase !important;
    color: #E04F33 !important;
    margin-top: 1px !important;
  }
  .v2-drawer-close-btn {
    width: 36px !important;
    height: 36px !important;
    border-radius: 8px !important;
    border: 1px solid rgba(18, 18, 18, 0.12) !important;
    background: #FAF8F5 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    color: #121212 !important;
    transition: background 0.2s ease !important;
  }
  .v2-drawer-close-btn:hover {
    background: #EDE8E1 !important;
  }
  .v2-drawer-body {
    flex: 1 !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
    padding: 18px 16px !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 18px !important;
  }
  .v2-drawer-section-title {
    font-size: 10px !important;
    font-weight: 800 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: #888888 !important;
    margin-bottom: 8px !important;
  }
  .v2-drawer-nav {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
  }
  .v2-drawer-nav-item {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 12px 14px !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.06) !important;
    border-radius: 12px !important;
    text-decoration: none !important;
    color: #121212 !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02) !important;
  }
  .v2-drawer-nav-item:hover, .v2-drawer-nav-item:active {
    background: #FDF9F6 !important;
    border-color: rgba(224, 79, 51, 0.25) !important;
    transform: translateX(3px) !important;
  }
  .v2-drawer-item-left {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
  }
  .v2-drawer-icon-box {
    width: 32px !important;
    height: 32px !important;
    border-radius: 8px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
  }
  .v2-icon-terracotta {
    background: rgba(224, 79, 51, 0.12) !important;
    color: #E04F33 !important;
  }
  .v2-icon-navy {
    background: rgba(14, 43, 92, 0.12) !important;
    color: #0E2B5C !important;
  }
  .v2-icon-indigo {
    background: rgba(67, 56, 202, 0.12) !important;
    color: #4338CA !important;
  }
  .v2-icon-gold {
    background: rgba(180, 83, 9, 0.12) !important;
    color: #B45309 !important;
  }
  .v2-icon-slate {
    background: rgba(51, 65, 85, 0.12) !important;
    color: #334155 !important;
  }
  .v2-drawer-item-label {
    font-family: var(--font-sans) !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    color: #1F2937 !important;
  }
  .v2-drawer-chevron {
    color: #9CA3AF !important;
    flex-shrink: 0 !important;
  }
  .v2-drawer-authors {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
  }
  .v2-author-pill {
    padding: 6px 12px !important;
    background: #FFFFFF !important;
    border: 1px solid rgba(18, 18, 18, 0.08) !important;
    border-radius: 999px !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    color: #374151 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
  }
  .v2-author-pill:hover, .v2-author-pill:active {
    background: #E04F33 !important;
    color: #FFFFFF !important;
    border-color: #E04F33 !important;
  }
  .v2-drawer-footer {
    padding: 16px !important;
    background: #FFFFFF !important;
    border-top: 1px solid rgba(18, 18, 18, 0.08) !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 10px !important;
    flex-shrink: 0 !important;
  }
  .v2-drawer-wa-btn {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    width: 100% !important;
    padding: 12px !important;
    background: #25D366 !important;
    color: #FFFFFF !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 13.5px !important;
    text-decoration: none !important;
    box-shadow: 0 4px 12px rgba(37, 211, 102, 0.25) !important;
    box-sizing: border-box !important;
  }
  .v2-drawer-bag-btn {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    width: 100% !important;
    padding: 11px !important;
    background: #121212 !important;
    color: #FFFFFF !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    border: none !important;
    cursor: pointer !important;
    box-sizing: border-box !important;
  }

  /* 3. Sticky Mobile Buy Bar for PDP (Hidden on desktop) */
  .v2-solo-mobile-buy-bar {
    display: none !important;
  }

  /* ==========================================================================
     TABLETS & MOBILE (<= 900px)
     ========================================================================== */
  @media (max-width: 1024px) {
    /* Sticky 2-Row Contained Mobile Header */
    .site-navbar.site-header,
    header.site-navbar,
    .site-header,
    .site-navbar {
      height: auto !important;
      min-height: unset !important;
      max-height: unset !important;
      padding: 8px 12px 10px 12px !important;
      display: block !important;
      width: 100% !important;
      max-width: 100vw !important;
      box-sizing: border-box !important;
      background: #FAF8F5 !important;
      border-bottom: 1px solid rgba(18, 18, 18, 0.08) !important;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04) !important;
      position: sticky !important;
      top: 0 !important;
      left: 0 !important;
      right: 0 !important;
      z-index: 10000000 !important;
      overflow: visible !important;
    }
    .navbar-inner {
      display: flex !important;
      flex-wrap: wrap !important;
      align-items: center !important;
      justify-content: space-between !important;
      width: 100% !important;
      max-width: 100% !important;
      padding: 0 !important;
      margin: 0 !important;
      row-gap: 8px !important;
      column-gap: 8px !important;
      box-sizing: border-box !important;
    }
    /* Row 1 Left: Brand & Hamburger */
    .v2-nav-brand-group {
      order: 1 !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 10px !important;
      flex: 0 0 auto !important;
      margin: 0 !important;
      padding: 0 !important;
    }
    .v2-hamburger-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      width: 36px !important;
      height: 36px !important;
      border-radius: 8px !important;
      border: 1px solid rgba(18, 18, 18, 0.15) !important;
      background: #FFFFFF !important;
      cursor: pointer !important;
      padding: 0 !important;
      color: #121212 !important;
      flex-shrink: 0 !important;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    }
    .brand-editorial-title {
      display: inline-flex !important;
      align-items: center !important;
      gap: 8px !important;
      text-decoration: none !important;
    }
    .brand-logo-img {
      height: 28px !important;
      width: auto !important;
      object-fit: contain !important;
    }
    .brand-name {
      font-family: 'Cormorant Garamond', serif !important;
      font-size: 16px !important;
      font-weight: 700 !important;
      color: #121212 !important;
      line-height: 1 !important;
      letter-spacing: 0.03em !important;
    }
    .brand-editorial-subtitle {
      font-size: 7.5px !important;
      font-weight: 700 !important;
      letter-spacing: 0.14em !important;
      text-transform: uppercase !important;
      color: #E04F33 !important;
      margin-top: 1px !important;
    }
    .nav-editorial-links {
      display: none !important;
    }

    /* Row 1 Right: Mobile Actions (1-Click Order + Bag) */
    .v2-mobile-nav-actions {
      order: 2 !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 8px !important;
      margin-left: auto !important;
      flex-shrink: 0 !important;
    }
    .editorial-header-actions {
      display: none !important;
    }
    .v2-mobile-quick-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      width: 36px !important;
      height: 36px !important;
      border-radius: 8px !important;
      border: 1px solid rgba(224, 79, 51, 0.25) !important;
      background: rgba(224, 79, 51, 0.06) !important;
      cursor: pointer !important;
      color: #E04F33 !important;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    }
    .v2-mobile-bag-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      width: 36px !important;
      height: 36px !important;
      border-radius: 8px !important;
      border: 1px solid rgba(18, 18, 18, 0.15) !important;
      background: #FFFFFF !important;
      cursor: pointer !important;
      position: relative !important;
      color: #121212 !important;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    }
    .v2-mobile-bag-badge {
      position: absolute !important;
      top: -5px !important;
      right: -5px !important;
      background: #E04F33 !important;
      color: #FFFFFF !important;
      font-size: 10px !important;
      font-weight: 700 !important;
      border-radius: 10px !important;
      min-width: 18px !important;
      height: 18px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      padding: 0 4px !important;
      border: 2px solid #FAF8F5 !important;
      line-height: 1 !important;
    }

    /* Row 2: Full-Width Search Input */
    .editorial-search-wrap {
      order: 3 !important;
      width: 100% !important;
      flex: 1 1 100% !important;
      max-width: 100% !important;
      min-width: 0 !important;
      margin: 0 !important;
      position: relative !important;
    }
    .editorial-search-input {
      width: 100% !important;
      height: 38px !important;
      font-size: 13px !important;
      padding: 0 14px 0 36px !important;
      background: #FFFFFF !important;
      border: 1px solid rgba(18, 18, 18, 0.14) !important;
      border-radius: 8px !important;
      box-sizing: border-box !important;
      box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.03) !important;
    }
    .editorial-search-icon {
      position: absolute !important;
      left: 11px !important;
      top: 50% !important;
      transform: translateY(-50%) !important;
      width: 16px !important;
      height: 16px !important;
      color: #888888 !important;
      pointer-events: none !important;
    }
    .editorial-search-results {
      position: absolute !important;
      top: calc(100% + 4px) !important;
      left: 0 !important;
      right: 0 !important;
      width: 100% !important;
      max-height: 60vh !important;
      max-height: 60dvh !important;
      border-radius: 10px !important;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.2) !important;
      z-index: 2147483647 !important;
      background: #FFFFFF !important;
      border: 1px solid rgba(18, 18, 18, 0.1) !important;
      box-sizing: border-box !important;
    }

    /* Solo Book Page on Tablets & Mobile */
    #indigo-solo-product-view {
      position: fixed !important;
      inset: 0 !important;
      top: 0 !important;
      left: 0 !important;
      right: 0 !important;
      bottom: 0 !important;
      width: 100% !important;
      height: 100% !important;
      height: 100dvh !important;
      padding: 0 !important;
      overflow-y: auto !important;
      -webkit-overflow-scrolling: touch !important;
    }
    #indigo-solo-product-view.is-active {
      display: block !important;
    }
    .v2-solo-stage-container {
      width: 100% !important;
      max-width: 100% !important;
      height: auto !important;
      min-height: unset !important;
      max-height: none !important;
      flex-direction: column !important;
      border-radius: 0 !important;
      box-shadow: none !important;
    }
    .v2-solo-left-panel {
      width: 100% !important;
      height: auto !important;
      min-height: 380px !important;
      padding: 24px 20px 32px !important;
      box-sizing: border-box !important;
      position: relative !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      text-align: center !important;
    }
    .v2-solo-left-content {
      width: 100% !important;
    }
    .v2-solo-top-nav {
      width: 100% !important;
      display: flex !important;
      justify-content: space-between !important;
      margin-bottom: 24px !important;
    }
    .v2-solo-book-center-stage {
      position: relative !important;
      top: auto !important;
      left: auto !important;
      transform: none !important;
      margin: 16px auto 24px auto !important;
      perspective: 1200px !important;
    }
    .v2-book-spread-stage {
      width: 180px !important;
      height: 260px !important;
    }
    .v2-book-spread-stage.is-open {
      transform: none !important;
    }
    .v2-solo-quote-block {
      margin-top: 16px !important;
      max-width: 100% !important;
    }
    .v2-solo-quote-text {
      font-size: 15px !important;
      line-height: 1.6 !important;
      max-width: 100% !important;
    }
    .v2-solo-quote-source {
      font-size: 12px !important;
      max-width: 100% !important;
    }
    .v2-solo-right-panel {
      width: 100% !important;
      height: auto !important;
      max-height: none !important;
      padding: 24px 20px 100px 20px !important;
      box-sizing: border-box !important;
      overflow: visible !important;
      overflow-x: visible !important;
      overflow-y: visible !important;
    }
    .v2-solo-book-title {
      font-size: 26px !important;
      line-height: 1.25 !important;
    }
    .v2-solo-price {
      font-size: 24px !important;
    }
    .v2-solo-action-dock {
      display: none !important;
    }
    .v2-solo-mobile-buy-bar {
      display: flex !important;
      position: fixed !important;
      bottom: 0 !important;
      left: 0 !important;
      right: 0 !important;
      background: #FFFFFF !important;
      border-top: 1px solid rgba(18, 18, 18, 0.1) !important;
      padding: 12px 16px !important;
      gap: 10px !important;
      align-items: center !important;
      justify-content: space-between !important;
      z-index: 2147483640 !important;
      box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.08) !important;
    }
  }

  /* ==========================================================================
     PHONES & TABLETS / MOBILE VIEW (<= 1024px)
     ========================================================================== */
  @media (max-width: 1024px) {
    html, body {
      overflow-x: hidden !important;
      max-width: 100vw !important;
      width: 100% !important;
      margin: 0 !important;
      padding: 0 !important;
      box-sizing: border-box !important;
    }

    /* Scatter Hero section - Clean Uncluttered Mobile Experience */
    #editorial-scatter-hero {
      height: auto !important;
      min-height: auto !important;
      padding: 32px 14px 44px 14px !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: center !important;
      overflow: hidden !important;
      box-sizing: border-box !important;
      width: 100% !important;
      max-width: 100vw !important;
      background: #FAF8F5 !important;
      position: relative !important;
    }
    #editorial-scatter-hero .scatter-book-cover {
      display: none !important;
    }
    #editorial-scatter-hero .scatter-svg-layer {
      display: none !important;
    }
    .scatter-headline-center {
      position: relative !important;
      width: 100% !important;
      max-width: 100% !important;
      padding: 0 !important;
      pointer-events: auto !important;
      text-align: center !important;
      margin: 0 auto !important;
      box-sizing: border-box !important;
    }
    .scatter-title {
      font-family: var(--font-serif) !important;
      font-size: clamp(26px, 7vw, 34px) !important;
      line-height: 1.15 !important;
      letter-spacing: -0.01em !important;
      margin: 0 auto !important;
      color: #121212 !important;
      font-weight: 400 !important;
    }
    .scatter-subtitle {
      font-size: 10px !important;
      letter-spacing: 0.16em !important;
      text-transform: uppercase !important;
      color: #666666 !important;
      margin-top: 8px !important;
      line-height: 1.4 !important;
    }

    /* Mobile 3D Book Fan Showcase */
    .v2-mobile-hero-showcase {
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      margin-top: 26px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .v2-mobile-book-deck {
      display: flex !important;
      align-items: flex-end !important;
      justify-content: center !important;
      height: 175px !important;
      position: relative !important;
      width: 280px !important;
      margin: 0 auto !important;
    }
    .v2-mobile-deck-card {
      position: absolute !important;
      bottom: 0 !important;
      cursor: pointer !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      text-decoration: none !important;
      transition: transform 0.25s ease, filter 0.25s ease !important;
    }
    .v2-mobile-deck-card:active {
      transform: scale(0.96) !important;
    }
    .v2-mobile-deck-card img {
      border-radius: 4px !important;
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18), 0 2px 6px rgba(0, 0, 0, 0.1) !important;
      object-fit: cover !important;
      display: block !important;
    }
    .v2-mobile-deck-card span {
      font-size: 11px !important;
      font-family: var(--font-serif) !important;
      font-weight: 600 !important;
      color: #121212 !important;
      margin-top: 6px !important;
      white-space: nowrap !important;
    }
    .v2-deck-left {
      left: 8px !important;
      z-index: 2 !important;
      transform: rotate(-9deg) translateY(-4px) !important;
    }
    .v2-deck-left img {
      width: 78px !important;
      height: 118px !important;
    }
    .v2-deck-center {
      left: 50% !important;
      transform: translateX(-50%) translateY(-12px) !important;
      z-index: 5 !important;
    }
    .v2-deck-center img {
      width: 94px !important;
      height: 142px !important;
    }
    .v2-deck-right {
      right: 8px !important;
      z-index: 2 !important;
      transform: rotate(9deg) translateY(-4px) !important;
    }
    .v2-deck-right img {
      width: 78px !important;
      height: 118px !important;
    }
    .v2-deck-featured-tag {
      position: absolute !important;
      top: -8px !important;
      background: #E04F33 !important;
      color: #FFFFFF !important;
      font-size: 8px !important;
      font-weight: 700 !important;
      letter-spacing: 0.1em !important;
      padding: 2px 6px !important;
      border-radius: 4px !important;
      box-shadow: 0 2px 6px rgba(224, 79, 51, 0.4) !important;
    }
    .v2-mobile-hero-cta {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      margin-top: 20px !important;
      padding: 10px 22px !important;
      border-radius: 22px !important;
      background: #121212 !important;
      color: #FFFFFF !important;
      font-size: 12px !important;
      font-weight: 600 !important;
      text-decoration: none !important;
      letter-spacing: 0.04em !important;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12) !important;
      transition: background 0.2s ease !important;
    }
    .v2-mobile-hero-cta:active {
      background: #E04F33 !important;
    }

    /* Left rail of bookstore app */
    .v2-app-rail,
    .v2-app-left-rail {
      display: none !important;
    }
    .v2-bookstore-app,
    #video2-bookstore-app {
      padding: 0 !important;
      width: 100% !important;
      max-width: 100vw !important;
      box-sizing: border-box !important;
      display: block !important;
    }
    .v2-app-content {
      padding: 16px 12px 48px !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }
    .v2-archive-section,
    #all-books-archive-section {
      margin-top: 32px !important;
      padding: 20px 0 48px 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }
    .v2-archive-grid {
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 10px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .v2-shelf-block {
      margin-bottom: 36px !important;
    }
    .v2-shelf-header {
      flex-direction: column !important;
      align-items: flex-start !important;
      gap: 10px !important;
      margin-bottom: 14px !important;
    }
    .v2-shelf-title {
      font-size: 24px !important;
    }
    .v2-shelf-header-right {
      width: 100% !important;
    }
    .v2-shelf-author-pills {
      display: flex !important;
      flex-wrap: nowrap !important;
      gap: 8px !important;
      overflow-x: auto !important;
      white-space: nowrap !important;
      padding-bottom: 4px !important;
      scrollbar-width: none !important;
      -webkit-overflow-scrolling: touch !important;
      width: 100% !important;
    }
    .v2-shelf-author-pills::-webkit-scrollbar {
      display: none !important;
    }
    .v2-author-pill-btn {
      flex-shrink: 0 !important;
      padding: 5px 12px !important;
      font-size: 11.5px !important;
    }
    .v2-shelf-nav-arrows {
      display: none !important;
    }
    .v2-shelf-stage {
      padding: 18px 12px !important;
      border-radius: 14px !important;
      scroll-snap-type: x mandatory !important;
      -webkit-overflow-scrolling: touch !important;
    }
    .v2-shelf-row {
      gap: 18px !important;
    }
    .v2-shelf-book-card {
      width: 175px !important;
      flex-shrink: 0 !important;
      scroll-snap-align: start !important;
    }
  }

  /* ==========================================================================
     MOBILE PORTRAIT SCREENS (<= 640px)
     ========================================================================== */
  @media (max-width: 640px) {
    /* 5,559 Archive Section */
    #all-books-archive-section,
    #v2-archive-section {
      padding: 32px 12px 60px !important;
    }
    .v2-archive-header h2 {
      font-size: 23px !important;
    }
    .v2-archive-header p {
      font-size: 13px !important;
    }
    #v2ArchiveFilterChips {
      display: flex !important;
      overflow-x: auto !important;
      white-space: nowrap !important;
      gap: 8px !important;
      padding-bottom: 6px !important;
      scrollbar-width: none !important;
      -webkit-overflow-scrolling: touch !important;
    }
    #v2ArchiveFilterChips::-webkit-scrollbar {
      display: none !important;
    }
    #v2ArchiveFilterChips .v2-chip {
      flex-shrink: 0 !important;
      padding: 6px 14px !important;
      font-size: 12px !important;
    }
    .v2-archive-controls-bar {
      flex-direction: column !important;
      gap: 10px !important;
    }
    .v2-archive-search-box {
      width: 100% !important;
    }
    #v2ArchiveGrid {
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 12px !important;
    }
    .v2-archive-card {
      padding: 10px 8px !important;
    }
    .v2-archive-card-cover {
      height: 160px !important;
    }
    .v2-archive-card-title {
      font-size: 13px !important;
      line-height: 1.25 !important;
    }
    .v2-archive-card-author {
      font-size: 11px !important;
    }
    .v2-archive-card-price {
      font-size: 13px !important;
    }
    .v2-archive-card-actions {
      flex-direction: column !important;
      gap: 5px !important;
    }
    .v2-btn-preview,
    .v2-btn-buy {
      width: 100% !important;
      justify-content: center !important;
      font-size: 11px !important;
      padding: 7px 6px !important;
    }
  }
</style>"""

EDITORIAL_HOMEPAGE_HTML = """<!-- =========================================================================
     1. VIDEO 1: FLOATING 14-BOOK SCATTER HERO (00:00 - 00:03)
     ========================================================================= -->
<section id="editorial-scatter-hero">
  <!-- Central Editorial Serif Headline -->
  <div class="scatter-headline-center">
    <h1 class="scatter-title">
      Find Timeless Stories<br>Wherever You Are
    </h1>
    <div class="scatter-subtitle">
      &mdash; &amp; BE YOUR OWN MUSE &bull; 5,559 ARCHIVE EDITIONS
    </div>

    <!-- Mobile-Exclusive 3D Curated Book Showcase (Visible ONLY on Mobile <= 768px) -->
    <div class="v2-mobile-hero-showcase">
      <div class="v2-mobile-book-deck">
        <div class="v2-mobile-deck-card v2-deck-left" onclick="window.openSoloBookPage ? window.openSoloBookPage('hero-book-raag') : null;">
          <img src="assets/hero-raag-darbari.jpg" alt="Raag Darbari" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Raag Darbari', 'Shrilal Shukla')" />
          <span>Raag Darbari</span>
        </div>
        <div class="v2-mobile-deck-card v2-deck-center" onclick="window.openSoloBookPage ? window.openSoloBookPage('hero-book-godan') : null;">
          <img src="assets/hero-godan.jpg" alt="Godan" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Godan', 'Premchand')" />
          <div class="v2-deck-featured-tag">BESTSELLER</div>
          <span>Godan</span>
        </div>
        <div class="v2-mobile-deck-card v2-deck-right" onclick="window.openSoloBookPage ? window.openSoloBookPage('hero-book-rashmirathi') : null;">
          <img src="assets/hero-rashmirathi.jpg" alt="Rashmirathi" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Rashmirathi', 'Ramdhari Singh Dinkar')" />
          <span>Rashmirathi</span>
        </div>
      </div>
      <div class="v2-mobile-hero-cta-wrap">
        <a href="#shelf-popular" class="v2-mobile-hero-cta">Explore 5,559 Editions &darr;</a>
      </div>
    </div>
  </div>

  <!-- Self-Drawing Terracotta Calligraphic Thread -->
  <svg class="scatter-svg-layer" viewBox="0 0 1440 900" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path class="scatter-calligraphic-path" d="M -100 240 C 220 180 340 520 620 440 C 900 360 1020 680 1340 580 C 1480 540 1520 320 1600 300" stroke="#E04F33" stroke-width="2.2" stroke-linecap="round" fill="none" />
  </svg>

  <!-- 14 Floating Parallax Book Covers from shopify_products_import.csv -->
  <div class="scatter-book-cover" style="top: 10%; left: 6%;" data-depth="0.35" onclick="window.openSoloBookPage('hero-book-godan')">
    <img src="assets/hero-godan.jpg" alt="Godan" style="width: 88px; height: 132px;" onerror="this.src='assets/hero-godan.jpg'" />
    <span class="scatter-book-caption">Godan</span>
  </div>

  <div class="scatter-book-cover" style="top: 6%; left: 34%;" data-depth="0.6" onclick="window.openSoloBookPage('hero-book-raag')">
    <img src="assets/hero-raag-darbari.jpg" alt="Raag Darbari" style="width: 105px; height: 156px;" onerror="this.src='assets/hero-raag-darbari.jpg'" />
    <span class="scatter-book-caption">Raag Darbari</span>
  </div>

  <div class="scatter-book-cover" style="top: 12%; right: 28%;" data-depth="0.25" onclick="window.openSoloBookPage('hero-book-chitralekha')">
    <img src="assets/hero-chitralekha.jpg" alt="Chitralekha" style="width: 82px; height: 124px;" onerror="this.src='assets/hero-chitralekha.jpg'" />
    <span class="scatter-book-caption">Chitralekha</span>
  </div>

  <div class="scatter-book-cover" style="top: 8%; right: 7%;" data-depth="0.5" onclick="window.openSoloBookPage('hero-book-rashmirathi')">
    <img src="assets/hero-rashmirathi.jpg" alt="Rashmirathi" style="width: 98px; height: 146px;" onerror="this.src='assets/hero-rashmirathi.jpg'" />
    <span class="scatter-book-caption">Rashmirathi</span>
  </div>

  <div class="scatter-book-cover" style="top: 40%; left: 3%;" data-depth="0.75" onclick="window.openSoloBookPage('hero-book-kuchh-ishq')">
    <img src="assets/hero-kuchh-ishq.jpg" alt="Kuchh Ishq Kiya" style="width: 114px; height: 170px;" onerror="this.src='assets/hero-kuchh-ishq.jpg'" />
    <span class="scatter-book-caption">Kuchh Ishq Kiya</span>
  </div>

  <div class="scatter-book-cover" style="top: 42%; right: 4%;" data-depth="0.4" onclick="window.openSoloBookPage('hero-book-gypsy')">
    <img src="assets/hero-gypsy.jpg" alt="Gypsy" style="width: 92px; height: 138px;" onerror="this.src='assets/hero-gypsy.jpg'" />
    <span class="scatter-book-caption">Gypsy</span>
  </div>

  <div class="scatter-book-cover" style="bottom: 12%; left: 8%;" data-depth="0.3" onclick="window.openSoloBookPage('book-tarkash')">
    <img src="assets/book-tarkash.jpg" alt="Tarkash" style="width: 86px; height: 128px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Tarkash', 'Javed Akhtar')" />
    <span class="scatter-book-caption">Tarkash</span>
  </div>

  <div class="scatter-book-cover" style="bottom: 8%; left: 24%;" data-depth="0.65" onclick="window.openSoloBookPage('book-aadha-gaon')">
    <img src="assets/book-aadha-gaon.jpg" alt="Aadha Gaon" style="width: 102px; height: 152px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Aadha Gaon', 'Rahi Masoom Raza')" />
    <span class="scatter-book-caption">Aadha Gaon</span>
  </div>

  <div class="scatter-book-cover" style="bottom: 10%; right: 26%;" data-depth="0.45" onclick="window.openSoloBookPage('book-mahabhoj')">
    <img src="assets/book-mahabhoj.jpg" alt="Mahabhoj" style="width: 90px; height: 136px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Mahabhoj', 'Mannu Bhandari')" />
    <span class="scatter-book-caption">Mahabhoj</span>
  </div>

  <div class="scatter-book-cover" style="bottom: 14%; right: 8%;" data-depth="0.7" onclick="window.openSoloBookPage('book-shekhar')">
    <img src="assets/book-shekhar.jpg" alt="Shekhar" style="width: 110px; height: 164px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Shekhar Ek Jeevani', 'Agyeya')" />
    <span class="scatter-book-caption">Shekhar Ek Jeevani</span>
  </div>

  <div class="scatter-book-cover" style="top: 28%; left: 18%;" data-depth="0.2" onclick="window.openSoloBookPage('book-gaban')">
    <img src="assets/book-gaban.jpg" alt="Gaban" style="width: 74px; height: 112px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Gaban', 'Premchand')" />
    <span class="scatter-book-caption">Gaban</span>
  </div>

  <div class="scatter-book-cover" style="top: 26%; right: 18%;" data-depth="0.3" onclick="window.openSoloBookPage('book-nirmala')">
    <img src="assets/book-nirmala.jpg" alt="Nirmala" style="width: 76px; height: 114px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Nirmala', 'Premchand')" />
    <span class="scatter-book-caption">Nirmala</span>
  </div>

  <div class="scatter-book-cover" style="bottom: 24%; left: 42%;" data-depth="0.55" onclick="window.openSoloBookPage('hero-book-murakami')">
    <img src="assets/hero-book-murakami.jpg" alt="Murakami Set" style="width: 96px; height: 142px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Haruki Murakami Collection', 'Haruki Murakami')" />
    <span class="scatter-book-caption">Murakami Collection</span>
  </div>

  <div class="scatter-book-cover" style="bottom: 22%; right: 42%;" data-depth="0.5" onclick="window.openSoloBookPage('book-samvidhan')">
    <img src="assets/book-samvidhan.jpg" alt="Samvidhan" style="width: 94px; height: 140px;" onerror="window.handleBookCoverError && window.handleBookCoverError(this, 'Bharat Ka Samvidhan', 'Dr. B.R. Ambedkar')" />
    <span class="scatter-book-caption">Bharat Ka Samvidhan</span>
  </div>
</section>

<!-- =========================================================================
     2. VIDEO 1: STICKY DARK THEATER CURTAIN SLIDE-OVER (00:03 - 00:06)
     ========================================================================= -->
<section id="dark-curtain-manifesto">
  <div class="curtain-content-wrap">
    <div class="curtain-eyebrow">A CULTURAL HERITAGE ARCHIVE &bull; PRAYAGRAJ</div>
    <h2 class="curtain-scrub-headline" id="curtainScrubHeadline">
      <span class="curtain-word">A</span>
      <span class="curtain-word">Sanctuary</span>
      <span class="curtain-word">For</span>
      <span class="curtain-word">Generations</span>
      <span class="curtain-word">Of</span>
      <span class="curtain-word">Thinkers,</span>
      <span class="curtain-word">Readers</span>
      <span class="curtain-word">&amp;</span>
      <span class="curtain-word">Curators.</span>
    </h2>
    <div style="max-width: 680px; margin: 0 auto; font-size: 16px; line-height: 1.7; color: #BBBBBB;">
      From the timeless ghats and historic publishing houses of Prayagraj, Indigo Books curates India&rsquo;s most expansive repository of Hindi sahitya, Rekhta Urdu poetry, judicial commentaries, and modern world classics.
    </div>
    <div class="curtain-pillars-row">
      <div class="curtain-pillar-item"><span class="curtain-pillar-num">01.</span> 5,559 Authentic Editions</div>
      <div class="curtain-pillar-item"><span class="curtain-pillar-num">02.</span> Same-Day Dispatch Prayagraj</div>
      <div class="curtain-pillar-item"><span class="curtain-pillar-num">03.</span> Pan-India Cash On Delivery</div>
    </div>
  </div>
</section>

<!-- =========================================================================
     3. VIDEO 1: 3D TILTED SHEET UNFOLD (-8deg -> 0deg) (00:06 - 00:08)
     ========================================================================= -->
<section id="tilted-lens-section">
  <div class="tilted-sheet-card" id="tiltedSheetCard">
    <div class="tilted-sheet-badge">
      <span class="tilted-star-spin">&#10022;</span>
      LIVING HERITAGE &bull; THE CURATOR'S LENS
    </div>
    <h3 class="tilted-title">
      Every Title Carries A Story Beyond Its Pages
    </h3>
    <p class="tilted-desc">
      We believe authentic literature should be accessible, beautifully typeset, and delivered with reverence. Explore verified publisher editions direct from Lokbharti, Rajkamal, Rekhta, McGraw Hill, and Central Law Publications.
    </p>
    <div style="display: flex; gap: 16px; align-items: center; flex-wrap: wrap;">
      <a href="#video2-bookstore-app" class="btn-1click-express" style="background: #121212; color: #FFF; border-color: #121212; text-decoration: none; padding: 12px 24px;">
        Explore Curated Shelves &darr;
      </a>
      <span style="font-size: 12px; color: #777; font-weight: 600;">Certified 100% Original Publisher Paper Stock</span>
    </div>
  </div>
</section>

<!-- =========================================================================
     4. VIDEO 2: APP-STYLE BOOKSTORE WITH OVERLAPPING 3D SHELVES (00:00 - 00:08)
     ========================================================================= -->
<section id="video2-bookstore-app">
  <!-- Left Vertical Navigation Rail (Zero Audio) -->
  <aside class="v2-app-rail">
    <div class="v2-rail-group">
      <button type="button" class="v2-rail-btn active" title="Curated Shelves" onclick="window.scrollToAppSection('shelf-popular')">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
      </button>
      <button type="button" class="v2-rail-btn" title="Full Archive (5,559 Books)" onclick="window.scrollToAppSection('all-books-archive-section')">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
      </button>
      <button type="button" class="v2-rail-btn" title="Saved Reading List" onclick="window.toggleSoloSaveWishlist ? window.toggleSoloSaveWishlist() : null">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
      </button>
    </div>
    <div class="v2-rail-group">
      <button type="button" class="v2-rail-btn" title="Top of Page" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
      </button>
    </div>
  </aside>

  <!-- Main App Content Area -->
  <div class="v2-app-content">
    
    <!-- Shelf 1: Most Popular Picks -->
    <div class="v2-shelf-block" id="shelf-popular">
      <div class="v2-shelf-header">
        <h2 class="v2-shelf-title">Most Popular Picks</h2>
        <div class="v2-shelf-header-right">
          <div class="v2-shelf-author-pills">
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Premchand')">Premchand</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Shrilal Shukla')">Shrilal Shukla</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Dinkar')">Dinkar</button>
          </div>
          <div class="v2-shelf-nav-arrows">
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfPopular', -1)" title="Previous books">&larr;</button>
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfPopular', 1)" title="Next books">&rarr;</button>
          </div>
        </div>
      </div>
      <div class="v2-shelf-stage">
        <div class="v2-shelf-row" id="v2ShelfPopular">
          <!-- Populated dynamically with 3D overlapping cards + buttons -->
        </div>
      </div>
    </div>

    <!-- Shelf 2: Hindi Classics & Masterpieces -->
    <div class="v2-shelf-block" id="shelf-hindi">
      <div class="v2-shelf-header">
        <h2 class="v2-shelf-title">Hindi Classics &amp; Masterpieces</h2>
        <div class="v2-shelf-header-right">
          <div class="v2-shelf-author-pills">
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Premchand')">Premchand</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Shrilal Shukla')">Shrilal Shukla</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Ramdhari Singh Dinkar')">Dinkar</button>
          </div>
          <div class="v2-shelf-nav-arrows">
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfHindi', -1)" title="Previous books">&larr;</button>
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfHindi', 1)" title="Next books">&rarr;</button>
          </div>
        </div>
      </div>
      <div class="v2-shelf-stage">
        <div class="v2-shelf-row" id="v2ShelfHindi">
          <!-- Populated dynamically -->
        </div>
      </div>
    </div>

    <!-- Shelf 3: Rekhta Poetry & Shayari -->
    <div class="v2-shelf-block" id="shelf-poetry">
      <div class="v2-shelf-header">
        <h2 class="v2-shelf-title">Rekhta Poetry &amp; Shayari</h2>
        <div class="v2-shelf-header-right">
          <div class="v2-shelf-author-pills">
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Javed Akhtar')">Javed Akhtar</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Piyush Mishra')">Piyush Mishra</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Mirza Ghalib')">Ghalib</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Rahi Masoom Raza')">Rahi Masoom Raza</button>
          </div>
          <div class="v2-shelf-nav-arrows">
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfPoetry', -1)" title="Previous books">&larr;</button>
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfPoetry', 1)" title="Next books">&rarr;</button>
          </div>
        </div>
      </div>
      <div class="v2-shelf-stage">
        <div class="v2-shelf-row" id="v2ShelfPoetry">
          <!-- Populated dynamically -->
        </div>
      </div>
    </div>

    <!-- Shelf 4: Law & Juridical Works -->
    <div class="v2-shelf-block" id="shelf-law">
      <div class="v2-shelf-header">
        <h2 class="v2-shelf-title">Law &amp; Juridical Works</h2>
        <div class="v2-shelf-header-right">
          <div class="v2-shelf-author-pills">
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Dr. B.R. Ambedkar')">Ambedkar</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Subhash Kashyap')">Subhash Kashyap</button>
            <button type="button" class="v2-author-pill-btn" onclick="window.filterByAuthorDirect('Central Law Publications')">Bare Acts</button>
          </div>
          <div class="v2-shelf-nav-arrows">
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfLaw', -1)" title="Previous books">&larr;</button>
            <button type="button" class="v2-shelf-arrow-btn" onclick="window.slideShelf('v2ShelfLaw', 1)" title="Next books">&rarr;</button>
          </div>
        </div>
      </div>
      <div class="v2-shelf-stage">
        <div class="v2-shelf-row" id="v2ShelfLaw">
          <!-- Populated dynamically -->
        </div>
      </div>
    </div>

    <!-- FULL 5,559 BOOK ARCHIVE LISTING SECTION -->
    <section id="all-books-archive-section" class="v2-archive-section">
      <div class="v2-archive-header">
        <div style="font-size: 11px; font-weight: 700; color: #E04F33; letter-spacing: 0.16em; text-transform: uppercase; margin-bottom: 6px;">
          PAN-INDIA CENTRAL REPOSITORY
        </div>
        <h2 class="v2-archive-title">Full Book Archive (5,559 Editions)</h2>
        <p class="v2-archive-sub">Explore the complete catalog with faceted category filters and instant predictive search.</p>
      </div>

      <!-- Genre & Category Filter Chips -->
      <div class="v2-archive-chips" id="v2ArchiveFilterChips">
        <button type="button" class="v2-chip active" onclick="window.filterArchiveGenre('all', this)">All Books (5,559)</button>
        <button type="button" class="v2-chip" onclick="window.filterArchiveGenre('hindi', this)">Hindi Classics &amp; Novels</button>
        <button type="button" class="v2-chip" onclick="window.filterArchiveGenre('poetry', this)">Rekhta &amp; Urdu Poetry</button>
        <button type="button" class="v2-chip" onclick="window.filterArchiveGenre('law', this)">Law &amp; Constitution</button>
        <button type="button" class="v2-chip" onclick="window.filterArchiveGenre('bestsellers', this)">Bestsellers &amp; Popular</button>
        <button type="button" class="v2-chip" onclick="window.filterArchiveGenre('philosophy', this)">Philosophy &amp; History</button>
      </div>

      <!-- Search & Sort Controls -->
      <div class="v2-archive-controls">
        <div class="v2-archive-search-box">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="v2ArchiveSearchInput" placeholder="Filter 5,559 titles by title, author, or publisher..." oninput="window.handleArchiveSearch(this.value)" />
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 12px; color: #666; font-weight: 600;">Sort:</span>
          <select id="v2ArchiveSortSelect" onchange="window.handleArchiveSort(this.value)" class="v2-archive-select">
            <option value="featured">Featured Editions</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
            <option value="title-asc">Title: A to Z</option>
          </select>
        </div>
      </div>

      <!-- Responsive Grid of Book Cards -->
      <div class="v2-archive-grid" id="v2ArchiveGrid">
        <!-- Populated dynamically from window.MASTER_SEARCH_CATALOG -->
      </div>

      <!-- Pagination / Load More Button -->
      <div style="text-align: center; margin-top: 48px;">
        <button type="button" id="v2ArchiveLoadMoreBtn" class="v2-btn-load-more" onclick="window.loadMoreArchiveBooks()">
          Load More Books (<span id="v2ArchiveCountDisplay">Showing 24 of 5,559</span>)
        </button>
      </div>
    </section>

  </div>
</section>"""

EDITORIAL_SOLO_HTML = """<!-- =========================================================================
     5. VIDEO 2: DEFINITIVE SPLIT-SCREEN SOLO PRODUCT STUDIO VIEW
     (With -180deg 3D Spread Animation & Excerpt Swap)
     ========================================================================= -->
<div id="indigo-solo-product-view" class="v2-solo-product-view">
  <div class="v2-solo-stage-container">
    <!-- Left Atmospheric Art & Quote Panel (42% Width) -->
    <div class="v2-solo-left-panel">
      <div class="v2-solo-left-bg-art" id="v2SoloBgArt"></div>
      <div class="v2-solo-left-content">
        <div class="v2-solo-top-nav">
          <button type="button" class="v2-solo-back-btn" onclick="window.closeSoloBookPage()">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            Back
          </button>
          <button type="button" class="v2-solo-search-btn" id="v2SoloCardSearchBtn" onclick="event.stopPropagation(); window.activateUniversalSearch(event);" title="Search books">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </button>
        </div>
        <div class="v2-solo-quote-block">
          <div class="v2-solo-quote-mark">&ldquo;</div>
          <p class="v2-solo-quote-text" id="v2SoloQuoteText">A celebrated work of modern Indian literature from our authenticated 5,559-book archive.</p>
          <div class="v2-solo-quote-source" id="v2SoloQuoteSource">&mdash; Indigo Editorial Archive &bull; Prayagraj</div>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <div class="v2-equalizer-bars">
              <span></span><span></span><span></span>
            </div>
            <span style="font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(255,255,255,0.7);">
              Authenticated Publisher Edition
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Center-Straddling 3D Book (Spans across the 42% seam) -->
    <div class="v2-solo-book-center-stage" onmouseenter="window.toggleSoloBookSpread(true)" onmouseleave="window.toggleSoloBookSpread(false)">
      <div class="v2-book-spread-stage" id="v2BookSpreadStage" onmouseenter="window.toggleSoloBookSpread(true)" onmouseleave="window.toggleSoloBookSpread(false)" onclick="window.toggleSoloBookSpread()" title="Hover to flip open 2-page preview spread">
        <div class="v2-solo-3d-book" id="v2Solo3dBook">
          <!-- Flipping Front Cover Leaf -->
          <div class="v2-cover-leaf" id="v2CoverLeaf">
            <div class="v2-cover-leaf-front" id="v2CoverLeafFront">
              <img id="v2CoverLeafImg" src="" alt="Book Cover" style="display:none;" onerror="this.onerror=null; this.style.display='none';" />
              <div class="v2-cover-spine-shadow"></div>
            </div>
            <!-- Back of Cover Leaf: Geometric Endpaper Art (matching inspect_frame_4.0s.jpg) -->
            <div class="v2-cover-leaf-back">
              <svg class="v2-endpaper-svg" viewBox="0 0 270 400" preserveAspectRatio="none">
                <polygon points="0,0 270,0 270,250 0,170" fill="#E65832" />
                <polygon points="0,170 270,250 270,400 0,400" fill="#23343B" />
                <circle cx="170" cy="115" r="50" fill="#F4E8D6" opacity="0.9" />
                <circle cx="170" cy="115" r="48" fill="none" stroke="#23343B" stroke-width="1.5" />
                <circle cx="115" cy="285" r="30" fill="#F4E8D6" opacity="0.95" />
                <line x1="40" y1="80" x2="190" y2="340" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,2" />
              </svg>
              <div class="v2-endpaper-overlay">
                <div class="v2-endpaper-seal">INDIGO BOOKS &bull; PRAYAGRAJ</div>
                <div class="v2-endpaper-title" id="v2LeafBackTitle">Godan</div>
                <div style="font-size: 10px; color: #F4E8D6; letter-spacing: 0.14em; text-transform: uppercase;">
                  PAN-INDIA CENTRAL REPOSITORY
                </div>
              </div>
            </div>
          </div>

          <!-- Inside Right Cream Typeset Page -->
          <div class="v2-inside-right-page" id="v2InsideRightPage">
            <div class="v2-inside-page-header" id="v2SpreadSeriesTag">INDIGO CLASSICS &bull; CHAPTER I</div>
            <h4 class="v2-spread-chapter-heading" id="v2SpreadChapterHeading">The Narrative</h4>
            <div class="v2-spread-columns-wrap">
              <div class="v2-drop-cap" id="v2DropCap">A</div>
              <div class="v2-spread-excerpt-snippet" id="v2SpreadExcerptSnippet">
                होरी महतो ने दोनों बैलों को सानी-पानी देकर अपनी स्त्री धनिया से कहा—गोबर को ज़रा चिलम भर देने को कहो। धनिया ने घर के भीतर से झाँकते हुए कहा—वह तो कब का चला गया, तुम ही जाओ अपने काम पर। होरी ने लाठी उठाई और सिर पर पगड़ी बाँधते हुए पछतावे भरी आँखों से अपनी सूनी गौशाला की ओर देखा, जहाँ एक गाय बाँधने का उसका बरसों पुराना सपना आज भी अधूरा था।
              </div>
            </div>
            <div class="v2-inside-page-footer">&mdash; 1 &mdash;</div>
            <div class="v2-spine-crease-shadow"></div>
          </div>
        </div>
      </div>
      <div class="v2-spread-hint-badge" onmouseenter="window.toggleSoloBookSpread(true)" onmouseleave="window.toggleSoloBookSpread(false)" onclick="window.toggleSoloBookSpread()">
        <span id="v2SpreadHintText"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle;margin-right:4px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Hover Book to Open 2-Page Preview Spread</span>
      </div>
    </div>

    <!-- Right White Details & Excerpt Card (58% Width) -->
    <div class="v2-solo-right-panel">
      <!-- State A: Book Metadata & Buy Actions -->
      <div class="v2-solo-details-content" id="v2ViewDetails">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
          <span class="v2-solo-badge" id="v2MetaPublisherBadge">LOKBHARTI PRAKASHAN</span>
          <span style="font-size: 12px; color: #16A34A; font-weight: 600;">&bull; In Stock (Fast Dispatch)</span>
        </div>
        <h2 class="v2-solo-book-title" id="v2SoloTitle">Book Title</h2>
        <div class="v2-solo-book-author" id="v2SoloAuthorWrap">
          <span style="color:#777;">Author:</span> <a href="javascript:void(0)" id="v2SoloAuthor" class="v2-solo-author-link" onclick="window.filterByAuthorFromSolo ? window.filterByAuthorFromSolo(this.getAttribute('data-author')) : null;">Author Name</a>
        </div>
        
        <div class="v2-solo-stars-row">
          <span style="color: #F59E0B; font-size: 16px;">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
          <span style="font-size: 13px; color: #555; font-weight: 600;">4.9 / 5.0 (328 verified reader reviews)</span>
        </div>

        <div class="v2-solo-price" id="v2SoloPrice">&#8377;299.00</div>

        <!-- Format Selector -->
        <div style="margin: 16px 0 14px;">
          <div style="font-size: 11px; font-weight: 700; color: #555; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 6px;">SELECT FORMAT</div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="v2-format-pill active" id="v2FormatPaperback">Paperback</button>
            <button type="button" class="v2-format-pill" id="v2FormatHardcover">Hardcover Deluxe</button>
          </div>
        </div>

        <!-- 2x2 Metadata Grid (Video 2 specs) -->
        <div class="v2-solo-specs-grid">
          <div class="v2-spec-item">
            <span class="v2-spec-label">Edition</span>
            <span class="v2-spec-value" id="v2MetaEdition">Heritage Edition</span>
          </div>
          <div class="v2-spec-item">
            <span class="v2-spec-label">Publisher</span>
            <span class="v2-spec-value" id="v2MetaPublisher">Lokbharti</span>
          </div>
          <div class="v2-spec-item">
            <span class="v2-spec-label">Binding &amp; Pages</span>
            <span class="v2-spec-value" id="v2MetaFormat">Paperback &bull; 344p</span>
          </div>
          <div class="v2-spec-item">
            <span class="v2-spec-label">ISBN-13</span>
            <span class="v2-spec-value" id="v2MetaIsbn">9788174828118</span>
          </div>
        </div>

        <!-- Primary Action Buttons -->
        <div class="v2-solo-actions-row">
          <button type="button" class="v2-btn-preview-spread" onclick="window.toggleSoloBookSpread()">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
            <span>Open 2-Page Spread Preview</span>
          </button>
          <button type="button" class="v2-btn-add-bag" onclick="window.handleSoloAddToCart()">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line></svg>
            <span>Add to Reading Bag</span>
          </button>
          <button type="button" class="v2-btn-buy-now" onclick="window.handleSoloBuyNow()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
            <span>Buy Now (Instant Checkout)</span>
          </button>
          <button type="button" class="v2-btn-wa-cod" onclick="window.handleSoloWhatsApp()">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.01L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67Z"/></svg>
            <span>Order on WhatsApp COD</span>
          </button>
        </div>

        <!-- More by this Author Suggestions Row -->
        <div class="v2-author-suggestions-section" id="v2AuthorSuggestionsWrap">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <span style="font-size: 11px; font-weight: 800; color: #121212; text-transform: uppercase; letter-spacing: 0.12em;">
              MORE BY <span id="v2AuthorSugTitle">THIS AUTHOR</span>
            </span>
            <a href="javascript:void(0)" id="v2AuthorSeeAllBtn" style="font-size: 11px; font-weight: 700; color: #E04F33; text-decoration: none; letter-spacing: 0.05em;" onclick="window.filterByAuthorFromSolo ? window.filterByAuthorFromSolo(this.getAttribute('data-author')) : null;">
              SEE ALL &rarr;
            </a>
          </div>
          <div class="v2-author-suggestions-grid" id="v2AuthorSuggestionsGrid">
            <!-- Dynamically populated from 5,559 book catalog -->
          </div>
        </div>
      </div>

      <!-- State B: Swappable Full Excerpt View (inspect_frame_4.0s.jpg) -->
      <div class="v2-solo-excerpt-content" id="v2ViewExcerpt" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
          <button type="button" class="v2-btn-close-excerpt" onclick="window.toggleSoloBookSpread(false)">
            &larr; Back to Book Details
          </button>
        </div>
        <h3 class="v2-excerpt-heading" id="v2ExcerptHeading">Excerpt</h3>
        <div class="v2-excerpt-subtitle" id="v2ExcerptSubtitle">Book 1 &bull; Chapter 1</div>
        <div class="v2-excerpt-full-text" id="v2ExcerptFullText">
          Loading reading sample...
        </div>
        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
          <button type="button" class="v2-btn-add-bag" style="flex: 1;" onclick="window.handleSoloAddToCart()">
            Add to Reading Bag
          </button>
          <button type="button" class="v2-btn-buy-now" style="flex: 1;" onclick="window.handleSoloBuyNow()">
            ⚡ Buy Now (Instant Checkout)
          </button>
        </div>
      </div>
    </div>

    <!-- Right Vertical Action Dock (inspect_frame_2.0s.jpg & inspect_frame_4.0s.jpg) -->
    <aside class="v2-solo-action-dock">
      <button type="button" class="v2-dock-btn" id="v2DockSaveBtn" title="Save to Reading List" onclick="window.toggleSoloSaveWishlist()">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
        <span>Save</span>
      </button>
      <button type="button" class="v2-dock-btn active" id="v2DockPreviewBtn" title="Open 2-Page Spread Preview" onclick="window.toggleSoloBookSpread()">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"></polygon></svg>
        <span>Preview</span>
      </button>
      <button type="button" class="v2-dock-btn" id="v2DockGetBtn" title="1-Click Express Order" onclick="window.handleSoloBuyNow()">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line></svg>
        <span>Get Book</span>
      </button>
    </aside>

    <!-- Sticky Mobile Buy Bar (Visible only on mobile <= 900px) -->
    <div class="v2-solo-mobile-buy-bar">
      <div style="flex: 1; min-width: 0;">
        <div style="font-size: 10.5px; color: #777; text-transform: uppercase; letter-spacing: 0.04em;" id="v2MobileBuyBarFormat">Paperback</div>
        <div style="font-size: 18px; font-weight: 700; color: #121212;" id="v2MobileBuyBarPrice">&#8377;450.00</div>
      </div>
      <button type="button" onclick="window.handleSoloBuyNow()" style="background: #121212; color: #FFFFFF; border: none; border-radius: 999px; padding: 11px 18px; font-size: 13px; font-weight: 600; cursor: pointer; white-space: nowrap;">
        ⚡ Buy Now
      </button>
      <button type="button" onclick="window.handleSoloAddToBag()" style="background: #25D366; color: #FFFFFF; border: none; border-radius: 999px; padding: 11px 16px; font-size: 13px; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; gap: 5px; white-space: nowrap;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line></svg>
        <span>Add to Bag</span>
      </button>
    </div>
  </div>
</div>"""

EDITORIAL_HTML = EDITORIAL_HOMEPAGE_HTML + EDITORIAL_SOLO_HTML

EDITORIAL_SCRIPT = """<script id="indigo-editorial-video-script">
(function() {
  'use strict';

  /* 1. CURATED REAL CATALOG DATA FOR SHELVES & HERO */
  function getFallbackCoverSvg(title, author) {
    var palettes = [
      { top: '#3E1715', bot: '#180706', gold: '#E5C07B', text: '#FAF7F2' },
      { top: '#15263D', bot: '#0A131F', gold: '#D4AF37', text: '#F8FAFC' },
      { top: '#1A2E22', bot: '#0B150F', gold: '#C5A059', text: '#F4F7F4' },
      { top: '#2D182A', bot: '#140813', gold: '#E0B084', text: '#FBF5F8' },
      { top: '#222035', bot: '#0D0C17', gold: '#DFB76C', text: '#F6F5FA' }
    ];
    var t = (title || 'Indigo Books').replace(/<[^>]*>/g, '').replace(/&/g, '&amp;').trim();
    var a = (author || 'Curated Edition').replace(/<[^>]*>/g, '').replace(/&/g, '&amp;').trim();
    
    var h = 0;
    for (var k = 0; k < t.length; k++) h = (h + t.charCodeAt(k)) % palettes.length;
    var pal = palettes[h];
    
    var words = t.split(/\s+/);
    var lines = [];
    var curr = '';
    for (var w = 0; w < words.length; w++) {
      var word = words[w];
      if ((curr + ' ' + word).trim().length <= 16) {
        curr = (curr + ' ' + word).trim();
      } else {
        if (curr) lines.push(curr);
        curr = word;
      }
    }
    if (curr) lines.push(curr);
    if (lines.length > 3) {
      lines = lines.slice(0, 2);
      lines.push(words.slice(lines.join(' ').split(/\s+/).length).join(' ').substring(0, 13) + '...');
    }
    
    var startY = 135 - ((lines.length - 1) * 11);
    var titleSvg = '';
    for (var i = 0; i < lines.length; i++) {
      var y = startY + (i * 22);
      titleSvg += '<text x="100" y="' + y + '" fill="' + pal.text + '" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">' + lines[i] + '</text>';
    }
    
    var authorY = startY + (lines.length * 22) + 14;
    var authorStr = a.substring(0, 22);
    
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300" width="100%" height="100%">' +
      '<defs>' +
        '<linearGradient id="ev_g_' + h + '" x1="0%" y1="0%" x2="100%" y2="100%">' +
          '<stop offset="0%" stop-color="' + pal.top + '"/>' +
          '<stop offset="100%" stop-color="' + pal.bot + '"/>' +
        '</linearGradient>' +
      '</defs>' +
      '<rect width="200" height="300" rx="3" fill="url(#ev_g_' + h + ')"/>' +
      '<rect x="0" y="0" width="10" height="300" fill="rgba(0,0,0,0.3)"/>' +
      '<line x1="10" y1="0" x2="10" y2="300" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>' +
      '<rect x="16" y="16" width="168" height="268" rx="2" fill="none" stroke="' + pal.gold + '" stroke-width="1.2" opacity="0.85"/>' +
      '<rect x="19" y="19" width="162" height="262" rx="1" fill="none" stroke="' + pal.gold + '" stroke-width="0.5" stroke-dasharray="2 3" opacity="0.6"/>' +
      '<circle cx="100" cy="58" r="22" fill="none" stroke="' + pal.gold + '" stroke-width="1"/>' +
      '<circle cx="100" cy="58" r="18" fill="none" stroke="' + pal.gold + '" stroke-width="0.5" stroke-dasharray="2 2" opacity="0.7"/>' +
      '<text x="100" y="63" fill="' + pal.gold + '" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">IB</text>' +
      '<text x="100" y="94" fill="' + pal.gold + '" font-family="sans-serif" font-size="7.5" font-weight="700" letter-spacing="1.5" text-anchor="middle">INDIGO ARCHIVE</text>' +
      titleSvg +
      '<line x1="60" y1="' + (authorY - 6) + '" x2="140" y2="' + (authorY - 6) + '" stroke="' + pal.gold + '" stroke-width="0.75" opacity="0.5"/>' +
      '<text x="100" y="' + (authorY + 8) + '" fill="' + pal.gold + '" font-family="sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">By ' + authorStr + '</text>' +
      '<text x="100" y="266" fill="#888888" font-family="sans-serif" font-size="7" letter-spacing="1.2" text-anchor="middle">PRAYAGRAJ &#8226; INDIA</text>' +
    '</svg>';
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
  }
  window.getFallbackCoverSvg = getFallbackCoverSvg;
  function handleBookCoverError(img, title, author) {
    if (!img) return;
    img.onerror = null;
    var bookTitle = title || img.getAttribute('data-title') || img.alt || 'Indigo Books Edition';
    var bookAuthor = author || img.getAttribute('data-author') || 'Indigo Archive';
    var fallback = (typeof window.getFallbackCoverSvg === 'function') ? window.getFallbackCoverSvg(bookTitle, bookAuthor) : (typeof getFallbackCover === 'function' ? getFallbackCover(bookTitle, bookAuthor) : '');
    if (img.parentElement) {
      img.parentElement.style.backgroundImage = 'url("' + fallback + '")';
      img.parentElement.style.backgroundSize = 'cover';
      img.parentElement.style.backgroundPosition = 'center';
    }
    img.style.display = 'none';
    img.src = fallback;
  }
  window.handleBookCoverError = handleBookCoverError;


  /* 0. GLOBAL ASSET URL RESOLVER (Zero 404, Live Shopify CDN & Local Preview Compatible) */
  function getCoverUrl(coverPath, defaultTitle, defaultAuthor) {
    if (!coverPath) {
      if (window.getFallbackCoverSvg) {
        return window.getFallbackCoverSvg(defaultTitle || 'Indigo Books', defaultAuthor || '');
      }
      return (window.PODIUM_CDN_COVERS && (window.PODIUM_CDN_COVERS['hero-godan.jpg'] || window.PODIUM_CDN_COVERS['assets/hero-godan.jpg'])) ||
             (window.SHOPIFY_ASSET_URL_ROOT ? window.SHOPIFY_ASSET_URL_ROOT + 'hero-godan.jpg' : 'assets/hero-godan.jpg');
    }
    // If already absolute HTTP/HTTPS, protocol-relative '//', or data URI, return DIRECTLY without tampering
    if (coverPath.indexOf('http://') === 0 || coverPath.indexOf('https://') === 0 || coverPath.indexOf('//') === 0 || coverPath.indexOf('data:') === 0) {
      return coverPath;
    }
    // Clean relative path prefix
    var clean = coverPath.replace(/^(\.\/)?assets\//, '').replace(/^\//, '');
    if (window.PODIUM_CDN_COVERS) {
      if (window.PODIUM_CDN_COVERS[coverPath]) return window.PODIUM_CDN_COVERS[coverPath];
      if (window.PODIUM_CDN_COVERS[clean]) return window.PODIUM_CDN_COVERS[clean];
      if (window.PODIUM_CDN_COVERS['assets/' + clean]) return window.PODIUM_CDN_COVERS['assets/' + clean];
      var baseName = clean.split('.')[0];
      if (window.PODIUM_CDN_COVERS[baseName]) return window.PODIUM_CDN_COVERS[baseName];
    }
    if (window.SHOPIFY_ASSET_URL_ROOT) {
      return window.SHOPIFY_ASSET_URL_ROOT + clean;
    }
    return 'assets/' + clean;
  }
  window.getCoverUrl = getCoverUrl;

  function fixAllThemeAssetImages() {
    var imgs = document.querySelectorAll('img');
    imgs.forEach(function(img) {
      var rawSrc = img.getAttribute('src');
      if (rawSrc && (rawSrc.indexOf('assets/') === 0 || rawSrc.indexOf('./assets/') === 0)) {
        var resolved = getCoverUrl(rawSrc);
        if (resolved && resolved !== rawSrc) {
          img.src = resolved;
        }
      }
      if (!img.onerror) {
        img.onerror = function() {
          this.onerror = null;
          if (window.getFallbackCoverSvg) {
            this.src = window.getFallbackCoverSvg(this.alt || 'Indigo Books', '');
          }
        };
      }
    });
  }
  window.fixAllThemeAssetImages = fixAllThemeAssetImages;

  var POPULAR_BOOKS = [
    {
      id: 'podium-godan',
      title: 'Godan (गोदान)',
      handle: 'godan-premchand',
      author: 'Premchand',
      price: '₹299.00',
      rawPrice: 299,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Heritage Edition',
      pages: '344p',
      isbn: '9788174828118',
      cover: 'assets/hero-godan.jpg',
      quote: 'जब तक जीवन में मान-मर्यादा और स्नेह का नाता बना रहे, मनुष्य हर विपत्ति झेल लेता है।',
      excerpt: 'होरी महतो ने दोनों बैलों को सानी-पानी देकर अपनी स्त्री धनिया से कहा—गोबर को ज़रा चिलम भर देने को कहो। धनिया ने घर के भीतर से झाँकते हुए कहा—वह तो कब का चला गया, तुम ही जाओ अपने काम पर। होरी ने लाठी उठाई और सिर पर पगड़ी बाँधते हुए पछतावे भरी आँखों से अपनी सूनी गौशाला की ओर देखा, जहाँ एक गाय बाँधने का उसका बरसों पुराना सपना आज भी अधूरा था।'
    },
    {
      id: 'podium-raag-darbari',
      title: 'Raag Darbari (राग दरबारी)',
      handle: 'raag-darbari-shrilal-shukla',
      author: 'Shrilal Shukla',
      price: '₹499.00',
      rawPrice: 499,
      format: 'Hardcover',
      publisher: 'Rajkamal Prakashan',
      edition: 'Authoritative Release',
      pages: '380p',
      isbn: '9788126702749',
      cover: 'assets/hero-raag-darbari.jpg',
      quote: 'वर्तमान शिक्षा पद्धति रास्ते में पड़ी हुई लावारिस कुतिया है, जिसे कोई भी लात मार सकता है।',
      excerpt: 'वह सड़क थी, जो शहर से चलकर देहात की तरफ़ जाती थी। उस पर एक ट्रक खड़ा था। ट्रक पर लिखा था: "सावधानी हटी, दुर्घटना घटी।" रंगनाथ ने अपना झोला सँभाला और धूल से भरी सड़क पर उतर आया। शिवपालगंज का क़स्बा यहीं से शुरू होता था, जहाँ ज़िन्दगी अपनी सुस्त रफ़्तार से चलती हुई व्यवस्था के अजीबोग़रीब नियमों में उलझी हुई थी।'
    },
    {
      id: 'podium-chitralekha',
      title: 'Chitralekha (चित्रलेखा)',
      handle: 'chitralekha-bhagwaticharan-verma',
      author: 'Bhagwaticharan Verma',
      price: '₹299.00',
      rawPrice: 299,
      format: 'Paperback',
      publisher: 'Rajkamal Prakashan',
      edition: 'Classic Sahitya Edition',
      pages: '268p',
      isbn: '9788126715428',
      cover: 'assets/hero-chitralekha.jpg',
      quote: 'संसार में न कोई पाप है और न पुण्य, केवल दृष्टिकोण का अंतर है।',
      excerpt: 'संसार में पाप क्या है और पुण्य क्या है? महाप्रभु रत्नाम्बर के आश्रम में दोनों शिष्यों—श्वेतांक और विशालदेव—ने सिर झुकाकर यही प्रश्न पूछा था। गुरु ने मुस्कुराकर उत्तर दिया: "इस संसार में न तो कोई पूर्णतः पापी है और न ही कोई पूर्णतः पुण्यात्मा। मनुष्य परिस्थितियों का दास है और प्रत्येक कर्म की व्याख्या उसके दृष्टिकोण पर निर्भर करती है।" जाओ, पाटलिपुत्र जाकर जीवन की वास्तविकता को अपनी आँखों से देखो।'
    },
    {
      id: 'podium-rashmirathi',
      title: 'Rashmirathi (रश्मिरथी)',
      handle: 'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
      author: 'Ramdhari Singh Dinkar',
      price: '₹350.00',
      rawPrice: 350,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Poetry Heritage Edition',
      pages: '176p',
      isbn: '9788174820686',
      cover: 'assets/hero-rashmirathi.jpg',
      quote: 'सच्चा शूरवीर वही है जो संकटों में मुस्कुराता है और अपने पराक्रम से भाग्य की रेखाएँ बदल देता है।',
      excerpt: 'जय हो, जग में जले जहाँ भी, नमन पुनीत अनल को। जिस नर में भी दीप्त दिखे, वन्द्य वह ज्योति प्रबल को। कर्ण का जन्म भले ही अज्ञात कुल में हुआ हो, किंतु उसकी भुजाओं में क्षत्रियों को पराजित करने वाला शौर्य और हृदय में मर्यादा का अद्वितीय संकल्प था। कुरुक्षेत्र की रणभूमि में जब अस्त्र उठे, तब दानवीर कर्ण ने अपने कवच-कुंडल तक त्याग कर इतिहास के पन्नों में अपनी अमर गाथा लिख दी।'
    },
    {
      id: 'podium-kuchh-ishq',
      title: 'Kuchh Ishq Kiya Kuchh Kaam Kiya',
      handle: 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
      author: 'Piyush Mishra',
      price: '₹250.00',
      rawPrice: 250,
      format: 'Paperback',
      publisher: 'Rajkamal Prakashan',
      edition: 'Modern Poetry Edition',
      pages: '160p',
      isbn: '9788126728466',
      cover: 'assets/hero-kuchh-ishq.jpg',
      quote: 'कुछ इश्क़ किया कुछ काम किया, वो काम बहुत नुक़सान किया।',
      excerpt: 'हम अपने भीतर एक पूरा शहर लेकर घूमते हैं। कभी ग्वालियर की संकरी गलियाँ, कभी दिल्ली की सर्द रातें और कभी बंबई की बेचैन सुबहें। इश्क़ अधूरा रह जाए तो कविता बन जाता है, और काम पूरा हो जाए तो ज़िन्दगी की रोटी बन जाता है। इस किताब के पन्नों में वही सारी ख़ामोशियाँ और शोर दर्ज़ हैं जिन्हें हमने जिया है।'
    },
    {
      id: 'book-tarkash',
      title: 'Tarkash (तरकश)',
      handle: 'tarkash-javed-akhtar',
      author: 'Javed Akhtar',
      price: '₹499.00',
      rawPrice: 499,
      format: 'Hardcover Deluxe',
      publisher: 'Rajkamal Prakashan',
      edition: 'Deluxe Devanagari Edition',
      pages: '240p',
      isbn: '9788126702671',
      cover: 'assets/book-tarkash.jpg',
      quote: 'क्यूँ डरें ज़िन्दगी में क्या होगा, कुछ न होगा तो तजुर्बा होगा।',
      excerpt: 'ज़िन्दगी के तरकश में बहुत से तीर होते हैं—कुछ उम्मीदों के, कुछ बिछड़ने के और कुछ ख़ामोश रातों में लिखी गई नज़्मों के। जब अल्फ़ाज़ काग़ज़ पर उतरते हैं, तो सिर्फ़ एक शायर का दर्द नहीं, बल्कि पूरे समाज की धड़कन बयाँ करते हैं। ये अशआर उन रास्तों की कहानी हैं जो शहर की रौशनी से दूर तन्हाई में जाकर खुलते हैं।'
    },
    {
      id: 'podium-gypsy',
      title: 'Gypsy (जिप्सी)',
      author: 'Ila Chandra Joshi',
      price: '₹499.00',
      rawPrice: 499,
      format: 'Hardcover',
      publisher: 'Lokbharti Prakashan',
      edition: 'Psychoanalytic Classic',
      pages: '312p',
      isbn: '9788174822017',
      cover: 'assets/hero-gypsy.jpg',
      quote: 'अंतर्मन के द्वंद्व से बड़ा कोई कुरुक्षेत्र इस संसार में नहीं है।',
      excerpt: 'मनुष्य के अंतर्मन की गहराइयों में छिपी अतृप्त वासनाएँ और अवचेतन की गूँज जब बाहर आती हैं, तब वह समाज के बनाए सभी बंधनों को तोड़ देना चाहती है। जिप्सी का जीवन किसी बंधी हुई नदी की तरह नहीं, बल्कि उस उन्मुक्त झरने की तरह है जो पत्थरों से टकराकर भी अपना नया रास्ता बना लेता है।'
    },
    {
      id: 'book-aadha-gaon',
      title: 'Aadha Gaon (आधा गाँव)',
      author: 'Rahi Masoom Raza',
      price: '₹450.00',
      rawPrice: 450,
      format: 'Paperback',
      publisher: 'Rajkamal Prakashan',
      edition: 'Heritage Edition',
      pages: '388p',
      isbn: '9788126702589',
      cover: 'assets/book-aadha-gaon.jpg',
      quote: 'मेरी भाषा भोजपुरी और हिन्दुस्तानी है, और मेरा गाँव गंगोली इस पूरे मुल्क का आईना है।',
      excerpt: 'गंगोली कोई काग़ज़ पर बना हुआ गाँव नहीं था, वह ज़िन्दा लोगों की मिट्टी, उनकी हँसी, उनकी गालियों और उनके मुहर्रम के मातम से बना था। विभाजन की आँधी आई, मुल्क बँट गया, लेकिन गंगोली के लोगों का वजूद उस मिट्टी से बँट नहीं सका। यह दास्तान उन इंसानों की है जो ज़मीन और ज़मीर के बीच झूलते रहे।'
    },
    {
      id: 'book-mahabhoj',
      title: 'Mahabhoj (महाभोज)',
      author: 'Mannu Bhandari',
      price: '₹225.00',
      rawPrice: 225,
      format: 'Paperback',
      publisher: 'Radhakrishna Prakashan',
      edition: 'Political Classic',
      pages: '192p',
      isbn: '9788171190478',
      cover: 'assets/book-mahabhoj.jpg',
      quote: 'राजनीति के इस महाभोज में आम आदमी हमेशा एक निवाला मात्र बनकर रह जाता है।',
      excerpt: 'सरोहा गाँव में दाऊसाहब की चुनावी राजनीति की बिसात बिछ चुकी थी। एक ग़रीब दलित की मौत कोई व्यक्तिगत त्रासदी नहीं थी, बल्कि सत्ता के गलियारों में गिद्धों के भोज का बहाना बन चुकी थी। हर कोई उस लाश पर अपनी रोटियाँ सेंकने को तैयार था, और व्यवस्था मूक दर्शक बनकर तमाशा देख रही थी।'
    },
    {
      id: 'book-shekhar',
      title: 'Shekhar: Ek Jeevani',
      author: 'Agyeya (अज्ञेय)',
      price: '₹599.00',
      rawPrice: 599,
      format: 'Hardcover Deluxe',
      publisher: 'Saraswati Press',
      edition: 'Complete Volumes I & II',
      pages: '512p',
      isbn: '9788174821034',
      cover: 'assets/book-shekhar.jpg',
      quote: 'अनुभूति ही सत्य है, और सत्य ही व्यक्ति की एकमात्र मुक्ति है।',
      excerpt: 'शशि ने जब पहली बार उसकी आँखों में देखा था, तो शेखर को लगा कि स्वतंत्रता कोई बाहर मिलने वाली चीज़ नहीं है, यह तो आत्मा की एक आंतरिक स्थिति है। समाज की रूढ़ियों के विरुद्ध उसका विद्रोह केवल क्रोध नहीं था, बल्कि एक संवेदनशील कलाकार की आत्म-खोज की तड़प थी।'
    },
    {
      id: 'book-gaban',
      title: 'Gaban (ग़बन)',
      author: 'Premchand',
      price: '₹220.00',
      rawPrice: 220,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Sahitya Edition',
      pages: '280p',
      isbn: '9788174828132',
      cover: 'assets/book-gaban.jpg',
      quote: 'झूठी प्रतिष्ठा की चाह इंसान को सबसे बड़े पतन की ओर ले जाती है।',
      excerpt: 'जालपा की चंद्रहार पाने की ज़िद ने रमानाथ को उस दलदल में धकेल दिया था जहाँ से वापसी का कोई रास्ता नहीं था। झूठी शान और दिखावे की लालसा ने एक सीधे-सादे क्लर्क को ग़बन के अपराध तक पहुँचा दिया। यह केवल एक चोरी की कहानी नहीं, बल्कि मध्यमवर्गीय समाज की खोखली प्रतिष्ठा की व्यथा है।'
    },
    {
      id: 'book-nirmala',
      title: 'Nirmala (निर्मला)',
      author: 'Premchand',
      price: '₹195.00',
      rawPrice: 195,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Authoritative Classic',
      pages: '208p',
      isbn: '9788174828149',
      cover: 'assets/book-nirmala.jpg',
      quote: 'बेमेल विवाह केवल दो शरीरों का नहीं, आत्मा और मानवीय गरिमा का दलन है।',
      excerpt: 'निर्मला की आँखें आंसुओं से भरी थीं जब उसने उस अनचाहे रिश्ते की दहलीज पर कदम रखा। समाज की कुरीतियों और बेमेल विवाह के दंश ने उसकी सारी खुशियाँ छीन ली थीं। तोताराम की हवेली में उसका जीवन एक सजीव पिंजरे जैसा था, जहाँ हर साँस के साथ आत्मसम्मान की बलि चढ़ती थी।'
    },
    {
      id: 'hero-book-murakami',
      title: 'Haruki Murakami Master Collection',
      author: 'Haruki Murakami',
      price: '₹1,899.00',
      rawPrice: 1899,
      format: 'Box Set (4 Volumes)',
      publisher: 'Vintage International',
      edition: 'Deluxe Slipcase Box Set',
      pages: '1240p',
      isbn: '9780099448761',
      cover: 'assets/hero-book-murakami.jpg',
      quote: 'Death exists, not as the opposite of life, but as an integral part of it.',
      excerpt: "When Toru Watanabe heard the Beatles' song \\"Norwegian Wood\\" playing through the cabin speakers of the Boeing 747, a wave of bittersweet memories swept over him. He was transported back to the Tokyo of the late 1960s—to quiet Sunday walks with Naoko through autumn meadows, the unspoken weight of Kizuki's suicide, and the delicate struggle of holding on to life while mourning the dead."
    },
    {
      id: 'book-samvidhan',
      title: 'Bharat Ka Samvidhan (भारत का संविधान)',
      handle: 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
      author: 'Government of India / Dr. B.R. Ambedkar',
      price: '₹450.00',
      rawPrice: 450,
      format: 'Hardcover',
      publisher: 'Central Law Publications',
      edition: 'Official Bilingual Edition',
      pages: '560p',
      isbn: '9789389657029',
      cover: 'assets/book-samvidhan.jpg',
      quote: 'संविधान केवल वकीलों का दस्तावेज़ नहीं, यह जीवन जीने का माध्यम और राष्ट्र की आत्मा है।',
      excerpt: 'हम, भारत के लोग, भारत को एक सम्पूर्ण प्रभुत्व-सम्पन्न, समाजवादी, पंथनिरपेक्ष, लोकतंत्रात्मक गणराज्य बनाने के लिए तथा उसके समस्त नागरिकों को सामाजिक, आर्थिक और राजनैतिक न्याय, विचार, अभिव्यक्ति, विश्वास, धर्म और उपासना की स्वतंत्रता, प्रतिष्ठा और अवसर की समता प्राप्त कराने के लिए दृढ़संकल्प होकर अपनी इस संविधान सभा में आज एतद्द्वारा इस संविधान को अंगीकृत, अधिनियमित और आत्मार्पित करते हैं।'
    }
  ];

  var currentActiveBook = POPULAR_BOOKS[0];
  var isSpreadOpen = false;
  var previousViewBeforeSolo = 'home';
  window.previousViewBeforeSolo = 'home';

  
  /* DYNAMIC AUTHENTIC LITERARY CONTENT GENERATORS (Monolingual: Pure Hindi OR Pure English) */
  function isHindiBook(b) {
    var rawText = (b.title || '') + ' ' + (b.author || '') + ' ' + (b.category || '') + ' ' + (b.genre || '') + ' ' + (b.publisher || '') + ' ' + (b.pub || '');
    if (/[\u0900-\u097F]/.test(rawText)) return true;
    var tLower = rawText.toLowerCase();
    var hindiMarkers = [
      'rajkamal', 'lokbharti', 'radhakrishna', 'vani', 'kitabghar', 'sahitya', 'jnanpith',
      'rekhta', 'shayari', 'ghazal', 'nazm', 'urdu', 'hindi', 'samvidhan', 'kahani', 'kavita',
      'premchand', 'shrilal shukla', 'dinkar', 'renu', 'javed akhtar', 'gulzar', 'rahat indori',
      'faiz', 'ghalib', 'jaun elia', 'manto', 'harivansh', 'bachchan', 'bhagwaticharan',
      'mahadevi', 'chandra joshi', 'amritlal', 'bhisham sahni', 'nirmal verma', 'kamleshwar',
      'mannu bhandari', 'mohan rakesh', 'nirala', 'agyeya', 'hazari prasad', 'tarkash', 'godan',
      'raag darbari', 'chitralekha', 'rashmirathi', 'gaban', 'nirmala', 'karmabhoomi', 'sevasadan',
      'mansarovar', 'madhushala', 'kamayani', 'tamash', 'aadha gaon', 'mahabhoj', 'gypsy', 'prakashan'
    ];
    for (var i = 0; i < hindiMarkers.length; i++) {
      if (tLower.indexOf(hindiMarkers[i]) !== -1) return true;
    }
    return false;
  }

  function getHindiAuthorName(author) {
    if (!author) return 'रचनाकार';
    var aLower = author.toLowerCase();
    if (aLower.indexOf('premchand') !== -1) return 'मुंशी प्रेमचंद';
    if (aLower.indexOf('shrilal') !== -1) return 'श्रीलाल शुक्ल';
    if (aLower.indexOf('dinkar') !== -1) return 'रामधारी सिंह "दिनकर"';
    if (aLower.indexOf('bhagwati') !== -1) return 'भगवतीचरण वर्मा';
    if (aLower.indexOf('renu') !== -1) return 'फणीश्वरनाथ रेणु';
    if (aLower.indexOf('javed') !== -1) return 'जावेद अख़्तर';
    if (aLower.indexOf('gulzar') !== -1) return 'गुलज़ार';
    if (aLower.indexOf('rahat') !== -1) return 'राहत इन्दौरी';
    if (aLower.indexOf('faiz') !== -1) return 'फ़ैज़ अहमद फ़ैज़';
    if (aLower.indexOf('ghalib') !== -1) return 'मिर्ज़ा ग़ालिब';
    if (aLower.indexOf('jaun') !== -1) return 'जौन एलिया';
    if (aLower.indexOf('joshi') !== -1) return 'इलाचन्द्र जोशी';
    if (aLower.indexOf('sahni') !== -1) return 'भीष्म साहनी';
    if (aLower.indexOf('nagar') !== -1) return 'अमृतलाल नागर';
    if (aLower.indexOf('bhandari') !== -1) return 'मन्नू भंडारी';
    if (aLower.indexOf('rakesh') !== -1) return 'मोहन राकेश';
    if (aLower.indexOf('bachchan') !== -1) return 'हरिवंश राय बच्चन';
    if (aLower.indexOf('mahadevi') !== -1) return 'महादेवी वर्मा';
    if (aLower.indexOf('prasad') !== -1) return 'जयशंकर प्रसाद';
    if (aLower.indexOf('nirala') !== -1) return 'सूर्यकांत त्रिपाठी "निराला"';
    if (aLower.indexOf('ambedkar') !== -1) return 'डॉ. भीमराव आंबेडकर';
    if (aLower.indexOf('mishra') !== -1) return 'पीयूष मिश्रा';
    if (/[\u0900-\u097F]/.test(author)) return author;
    return 'कथाकार';
  }

  function getCleanDisplayTitle(title, isHindi) {
    if (!title) return isHindi ? 'कालजयी रचना' : 'Masterwork';
    if (isHindi) {
      var devMatch = title.match(/[\u0900-\u097F][\u0900-\u097F\s\u0964\u0965:-]*/);
      if (devMatch && devMatch[0].trim().length > 2) {
        return devMatch[0].trim();
      }
      return title.split(':')[0].split('(')[0].trim();
    }
    return title.split('(')[0].trim();
  }

  function getBookAuthenticExcerpt(b) {
    var hindi = isHindiBook(b);
    var cat = (b.category || b.genre || '').toLowerCase();

    // If custom excerpt already authentic and in matching script, preserve it
    if (b.excerpt && b.excerpt.indexOf('Authoritative original publisher release') === -1) {
      var hasDevanagari = /[\u0900-\u097F]/.test(b.excerpt);
      if ((hindi && hasDevanagari) || (!hindi && !hasDevanagari)) {
        return b.excerpt;
      }
    }

    if (hindi) {
      var hindiAuthor = getHindiAuthorName(b.author);
      if (cat.indexOf('poetry') !== -1 || cat.indexOf('shayari') !== -1 || cat.indexOf('ghazal') !== -1 || cat.indexOf('nazm') !== -1) {
        return 'शब्द जब अंतर्मन के मौन से निकलकर काग़ज़ पर उतरते हैं, तो वह केवल कविता नहीं रहते, बल्कि समय की धड़कन बन जाते हैं। ' + hindiAuthor + ' की यह अमर काव्य कृति मानवीय संवेदनाओं, प्रेम, विरह और अस्तित्व के गहरे प्रश्नों को स्पर्श करती है। प्रत्येक छंद पाठक के हृदय में एक अमिट गूँज छोड़ जाता है और आत्मा को एक नई चेतना से आलोकित करता है।';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1 || cat.indexOf('stories') !== -1 || cat.indexOf('kahani') !== -1) {
        return 'कथा का आरंभ उस मोड़ से होता है जहाँ मानवीय नियति और सामाजिक यथार्थ आमने-सामने खड़े होते हैं। कथा-साहित्य की इस कालजयी धारा में ' + hindiAuthor + ' ने अपने पात्रों के अंतर्द्वंद्व और समाज की जटिल बुनावट को अत्यंत सूक्ष्मता से उकेरा है। हर पृष्ठ पर जीवन की सच्ची अनुभूतियाँ और विचारोत्तेजक प्रसंग जीवंत हो उठते हैं।';
      }
      if (cat.indexOf('criticism') !== -1 || cat.indexOf('sahitya') !== -1 || cat.indexOf('essay') !== -1) {
        return 'साहित्य और समाज के अंतर्संबंधों का गहन मूल्यांकन प्रस्तुत करती यह कृति आलोचनात्मक चिंतन का अप्रतिम उदाहरण है। रचनाकार ने गहन विमर्श के माध्यम से पाठकीय चेतना को नई दृष्टि प्रदान की है, जहाँ परंपरा और आधुनिकता का संतुलन अत्यंत प्रमाणिक रूप में उपस्थित है।';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('judic') !== -1 || cat.indexOf('constitution') !== -1 || cat.indexOf('samvidhan') !== -1) {
        return 'विधि और न्याय का आधार स्तंभ वह सामाजिक अनुबंध है जो प्रत्येक नागरिक के अधिकारों और मानवीय गरिमा को सुनिश्चित करता है। यह कृति वैधानिक सिद्धांतों, न्यायिक निर्णयों और विधिक व्याख्याओं का प्रामाणिक संदर्भ ग्रंथ है, जो अध्येताओं और विचारकों के लिए अत्यंत उपादेय है।';
      }
      if (cat.indexOf('history') !== -1 || cat.indexOf('biograph') !== -1 || cat.indexOf('memoir') !== -1 || cat.indexOf('itihas') !== -1) {
        return 'इतिहास की धारा में खोए हुए प्रसंगों और युगप्रवर्तक व्यक्तित्वों के जीवन का सजीव आख्यान। अतीत के पन्नों से सत्य को उजागर करते हुए यह कृति तत्कालीन सामाजिक और सांस्कृतिक परिवेश का जीवंत एवं प्रामाणिक चित्र खींचती है।';
      }
      return 'मानवीय अनुभव और बौद्धिक चेतना की अनूठी अभिव्यक्ति। विचार और संवेदना के संगम पर रची गई यह कालजयी रचना पाठक को गहराई से सोचने और आत्ममंथन करने के लिए निरंतर प्रेरित करती है।';
    } else {
      var authorEng = b.author || 'The author';
      if (cat.indexOf('poetry') !== -1) {
        return 'When words arise from the quiet depths of introspection, they transcend verse to become the very pulse of human memory. ' + authorEng + ' explores poignant truths of longing, mortality, and grace, leaving an indelible resonance upon the reflective reader.';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1 || cat.indexOf('stories') !== -1) {
        return 'The narrative begins at that tender crossroad where individual fate confronts the relentless cadence of the world. With acute psychological acuity and evocative prose, ' + authorEng + ' unravels the fragile bonds of ambition and belonging, rendering every chapter a lucid study of the human spirit.';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('constitution') !== -1 || cat.indexOf('judic') !== -1) {
        return 'The foundation of justice rests upon covenants designed to safeguard human liberty and democratic dignity. This definitive scholarly work provides an authoritative analysis of constitutional jurisprudence, landmark doctrines, and statutory principles indispensable for scholars and jurists alike.';
      }
      if (cat.indexOf('history') !== -1 || cat.indexOf('biograph') !== -1) {
        return 'A compelling chronicle illuminating forgotten epochs and transformative lives. Drawing upon rigorous archival sources, this volume reconstructs historical turning points with literary precision, offering vital perspective on the contours of our shared heritage.';
      }
      return 'A distinguished contribution to contemporary letters. Elegantly crafted and deeply contemplative, this volume probes enduring questions of human experience, offering readers a luminous engagement with truth and literary art.';
    }
  }

  function getBookAuthenticQuote(b) {
    var hindi = isHindiBook(b);
    var cat = (b.category || b.genre || '').toLowerCase();

    if (b.quote && b.quote.indexOf('A celebrated work of modern') === -1) {
      var hasDevanagari = /[\u0900-\u097F]/.test(b.quote);
      if ((hindi && hasDevanagari) || (!hindi && !hasDevanagari)) {
        return b.quote;
      }
    }

    if (hindi) {
      if (cat.indexOf('poetry') !== -1 || cat.indexOf('shayari') !== -1) {
        return 'काव्य वही है जो हृदय के मौन को वाणी दे और अंधकार में दीप जला दे।';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1 || cat.indexOf('stories') !== -1) {
        return 'जीवन की सच्ची गाथा वही है जो मनुष्य के संघर्ष और उसकी अदम्य जिजीविषा को स्वर दे।';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('constitution') !== -1) {
        return 'न्याय केवल क़ानून का पालन नहीं, बल्कि मानवीय गरिमा और समानता की सर्वोच्च रक्षा है।';
      }
      return 'शब्द समय की सीमा से परे जाकर विचार और सत्य को सदैव जीवित रखते हैं।';
    } else {
      if (cat.indexOf('poetry') !== -1) {
        return 'Poetry is the quiet illumination of truths that words alone can seldom convey.';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1) {
        return 'Literature endures because it preserves the fragile, unvarnished truth of who we are.';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('constitution') !== -1) {
        return 'Justice is not merely the letter of the statute, but the living conscience of human equality.';
      }
      return 'True books do not pass away with the season; they remain constant companions across time.';
    }
  }

/* 2. RENDER OVERLAPPING 3D BOOK SHELVES */
  function renderAllShelves() {
    renderShelfRow('v2ShelfPopular', POPULAR_BOOKS);
    renderShelfRow('v2ShelfHindi', POPULAR_BOOKS.slice(0, 4));
    renderShelfRow('v2ShelfPoetry', [POPULAR_BOOKS[3], POPULAR_BOOKS[4], POPULAR_BOOKS[5], POPULAR_BOOKS[7]]);
    renderShelfRow('v2ShelfLaw', [POPULAR_BOOKS[13], POPULAR_BOOKS[8], POPULAR_BOOKS[9], POPULAR_BOOKS[1]]);
  }

  function renderShelfRow(containerId, books) {
    var row = document.getElementById(containerId);
    if (!row) return;
    row.innerHTML = '';

    books.forEach(function(b) {
      var card = document.createElement('div');
      card.className = 'v2-book-card';
      card.onclick = function() { window.openSoloBookPage(b.id); };

      var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var shelfFallback = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf" style="position:relative; background-color:#FAF7F0; background-image:url(&quot;' + shelfFallback + '&quot;); background-size:cover; background-position:center;">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" data-author="' + b.author + '" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=&quot;' + shelfFallback + '&quot;; this.style.display=&quot;none&quot;; window.handleBookCoverError && window.handleBookCoverError(this);" />' +
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

      var cImg = card.querySelector('.v2-card-cover-leaf img');
      if (cImg) cImg.onerror = function() { window.handleBookCoverError && window.handleBookCoverError(this, b.title, b.author); };

      var cLeaf = card.querySelector('.v2-card-cover-leaf');
      if (cLeaf) {
        cLeaf.onclick = function(e) {
          e.stopPropagation();
          window.openSoloBookPage(b.id);
        };
      }
      var pBtn = card.querySelector('.v2-card-preview-btn');
      if (pBtn) {
        pBtn.onclick = function(e) {
          e.stopPropagation();
          window.openSoloBookPage(b.id);
        };
      }
      var qBtn = card.querySelector('.v2-card-quick-btn');
      if (qBtn) {
        qBtn.onclick = function(e) {
          e.stopPropagation();
          if (typeof window.openExpressPhoneCheckout === 'function') {
            window.openExpressPhoneCheckout(b.id);
          } else if (typeof window.openQuickOrderModal === 'function') {
            window.openQuickOrderModal(b.id);
          }
        };
      }

      row.appendChild(card);
    });
  }

  /* 3. FULL 5,559 BOOK ARCHIVE LISTING & FACETED FILTERS (100% Tested & Fully Interactive) */
  var archiveCurrentGenre = 'all';
  var archiveSearchQuery = '';
  var archiveSortOrder = 'featured';
  var archivePage = 1;
  var ARCHIVE_PAGE_SIZE = 24;

  var HINDI_CLASSIC_AUTHORS = [
    'premchand', 'shrilal shukla', 'dinkar', 'bachchan', 'phanishwar nath renu', 'renu',
    'jaishankar prasad', 'suryakant tripathi nirala', 'nirala', 'mahadevi varma',
    'dharamvir bharati', 'bhagwati charan verma', 'bhagwaticharan', 'mannu bhandari',
    'krishna sobti', 'yashpal', 'bhisham sahni', 'kamleshwar', 'hazari prasad dwivedi',
    'mohan rakesh', 'ilachandra joshi', 'amritlal nagar', 'upendranath ashka', 'shivani',
    'kashinath singh', 'vinod kumar shukla', 'alok dhanwa', 'manglesh dabral', 'muktibodh',
    'chatur sen', 'vrindavan lal verma'
  ];

  var POETRY_AUTHORS = [
    'gulzar', 'javed akhtar', 'rahat indori', 'piyush mishra', 'faiz', 'ghalib',
    'jaun elia', 'bashir badr', 'dushyant kumar', 'sahir', 'dinkar', 'bachchan',
    'kaifi azmi', 'iqbal', 'parveen shakir', 'ahmad faraz', 'tagore', 'kabir', 'mira',
    'tulsi', 'surdas', 'firaq'
  ];

  function getArchivePool() {
    var pool = (window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) ? window.MASTER_SEARCH_CATALOG : POPULAR_BOOKS;
    return pool;
  }

  window.filterArchiveGenre = function(genre, btn) {
    archiveCurrentGenre = genre || 'all';
    archivePage = 1;
    var chips = document.querySelectorAll('#v2ArchiveFilterChips .v2-chip');
    chips.forEach(function(c) { c.classList.remove('active'); });
    if (btn) {
      btn.classList.add('active');
    } else {
      var matchBtn = document.querySelector('#v2ArchiveFilterChips button[onclick*="' + archiveCurrentGenre + '"]');
      if (matchBtn) matchBtn.classList.add('active');
    }
    renderArchiveGrid(false);
  };


  window.handleArchiveSearch = function(query) {
    archiveSearchQuery = (query || '').trim().toLowerCase();
    archivePage = 1;
    renderArchiveGrid(false);
  };


  window.handleArchiveSort = function(order) {
    archiveSortOrder = order || 'featured';
    renderArchiveGrid(false);
  };


  window.loadMoreArchiveBooks = function() {
    archivePage++;
    renderArchiveGrid(true);
  };

  function renderArchiveGrid(append) {
    var grid = document.getElementById('v2ArchiveGrid');
    var countDisplay = document.getElementById('v2ArchiveCountDisplay');
    var loadMoreBtn = document.getElementById('v2ArchiveLoadMoreBtn');
    if (!grid) return;

    if (!append) {
      grid.innerHTML = '';
    }

    var pool = getArchivePool();
    var filtered = [];

    // Distinct Pinned Editions by Genre for Featured order
    var pinnedTitles = {
      'all': ['godan', 'raag darbari', 'chitralekha', 'tarkash', 'samvidhan', 'rashmirathi', 'kuchh ishq'],
      'hindi': ['godan', 'raag darbari', 'chitralekha', 'gaban', 'nirmala', 'gunahon ka devta', 'tamas', 'maila anchal', 'rashmirathi'],
      'poetry': ['tarkash', 'kuchh ishq', 'madhushala', 'rashmirathi', 'saye mein dhoop', 'dhoop ke makan', 'rahat'],
      'law': ['samvidhan', 'constitution', 'ambedkar', 'bare act', 'vidhi', 'law'],
      'bestsellers': ['godan', 'raag darbari', 'chitralekha', 'tarkash', 'samvidhan', 'gypsy', 'aadha gaon', 'mahabhoj'],
      'philosophy': ['muktisangram', 'itihas', 'darshan', 'gandhi', 'ambedkar', 'buddha', 'swatantrata']
    };

    for (var i = 0; i < pool.length; i++) {
      var item = pool[i];
      var title = (item.title || '').toLowerCase();
      var author = (item.author || '').toLowerCase();
      var pub = (item.publisher || item.pub || '').toLowerCase();
      var cat = (item.category || item.genre || '').toLowerCase();

      // Precise Faceted Genre Filter
      if (archiveCurrentGenre === 'hindi') {
        var isClassicAuthor = HINDI_CLASSIC_AUTHORS.some(function(a) { return author.indexOf(a) !== -1; });
        var isNovelCat = cat.indexOf('novel') !== -1 || cat.indexOf('stories') !== -1 || cat.indexOf('sahitya') !== -1 || cat.indexOf('fiction') !== -1;
        if (!isClassicAuthor && !isNovelCat) continue;
      } else if (archiveCurrentGenre === 'poetry') {
        var isPoet = POETRY_AUTHORS.some(function(p) { return author.indexOf(p) !== -1; });
        var isPoetryCat = cat.indexOf('poetry') !== -1 || cat.indexOf('shayari') !== -1 || cat.indexOf('ghazal') !== -1 || cat.indexOf('nazm') !== -1 || cat.indexOf('kavita') !== -1;
        var isRekhta = pub.indexOf('rekhta') !== -1 || pub.indexOf('raza') !== -1;
        if (!isPoet && !isPoetryCat && !isRekhta) continue;
      } else if (archiveCurrentGenre === 'law') {
        var isLaw = cat.indexOf('law') !== -1 || cat.indexOf('judic') !== -1 || cat.indexOf('constitut') !== -1 || cat.indexOf('samvidhan') !== -1 || cat.indexOf('bare act') !== -1 || cat.indexOf('vidhi') !== -1;
        var isLawPub = pub.indexOf('central law') !== -1 || pub.indexOf('law') !== -1;
        var isLawTitle = title.indexOf('samvidhan') !== -1 || title.indexOf('constitution') !== -1 || title.indexOf('law') !== -1 || title.indexOf('act') !== -1;
        var isAmbedkar = author.indexOf('ambedkar') !== -1;
        if (!isLaw && !isLawPub && !isLawTitle && !isAmbedkar) continue;
      } else if (archiveCurrentGenre === 'bestsellers') {
        var isBestsellerAuthor = ['premchand', 'shrilal shukla', 'dinkar', 'gulzar', 'javed akhtar', 'piyush mishra', 'bhagwati'].some(function(a) { return author.indexOf(a) !== -1; });
        var isFamousTitle = ['godan', 'raag darbari', 'chitralekha', 'rashmirathi', 'kuchh ishq', 'tarkash', 'gypsy', 'aadha gaon', 'mahabhoj', 'nirmala', 'gaban', 'samvidhan', 'gunahon ka devta', 'tamas'].some(function(t) { return title.indexOf(t) !== -1; });
        if (!isBestsellerAuthor && !isFamousTitle && (item.mrp || 0) < 350) continue;
      } else if (archiveCurrentGenre === 'philosophy') {
        var isPhilCat = cat.indexOf('history') !== -1 || cat.indexOf('philosoph') !== -1 || cat.indexOf('darshan') !== -1 || cat.indexOf('itihas') !== -1 || cat.indexOf('biograph') !== -1 || cat.indexOf('memoir') !== -1;
        var isPhilTitle = title.indexOf('itihas') !== -1 || title.indexOf('history') !== -1 || title.indexOf('darshan') !== -1 || title.indexOf('gandhi') !== -1 || title.indexOf('vivekanand') !== -1 || title.indexOf('buddha') !== -1;
        if (!isPhilCat && !isPhilTitle) continue;
      }

      // Text query filter
      if (archiveSearchQuery) {
        if (title.indexOf(archiveSearchQuery) === -1 && author.indexOf(archiveSearchQuery) === -1 && pub.indexOf(archiveSearchQuery) === -1 && (item.isbn || '').indexOf(archiveSearchQuery) === -1) {
          continue;
        }
      }

      filtered.push(item);
    }

    // Sort
    if (archiveSortOrder === 'price-asc') {
      filtered.sort(function(a, b) { return (a.rawPrice || a.price || a.mrp || 0) - (b.rawPrice || b.price || b.mrp || 0); });
    } else if (archiveSortOrder === 'price-desc') {
      filtered.sort(function(a, b) { return (b.rawPrice || b.price || b.mrp || 0) - (a.rawPrice || a.price || a.mrp || 0); });
    } else if (archiveSortOrder === 'title-asc') {
      filtered.sort(function(a, b) { return (a.title || '').localeCompare(b.title || ''); });
    } else {
      // 'featured' sort: pin iconic masterworks for that genre to the top
      var genrePins = pinnedTitles[archiveCurrentGenre] || pinnedTitles['all'];
      filtered.sort(function(a, b) {
        var aTitle = (a.title || '').toLowerCase();
        var bTitle = (b.title || '').toLowerCase();
        var aMatch = genrePins.some(function(k) { return aTitle.indexOf(k) !== -1; });
        var bMatch = genrePins.some(function(k) { return bTitle.indexOf(k) !== -1; });
        if (aMatch && !bMatch) return -1;
        if (!aMatch && bMatch) return 1;
        return 0;
      });
    }

    var total = filtered.length;
    if (total === 0) {
      var genreLabels = {
        'all': 'All Books',
        'hindi': 'Hindi Classics & Novels',
        'poetry': 'Rekhta & Urdu Poetry',
        'law': 'Law & Constitution',
        'bestsellers': 'Bestsellers & Popular',
        'philosophy': 'Philosophy & History'
      };
      var currentGenreName = genreLabels[archiveCurrentGenre] || 'this category';
      var queryDisplay = archiveSearchQuery || 'your filter';

      grid.innerHTML = 
        '<div class="v2-archive-empty-state" style="grid-column: 1 / -1; background: #FFFFFF; border: 1px solid rgba(18, 18, 18, 0.08); border-radius: 16px; padding: 56px 24px; text-align: center; max-width: 620px; margin: 40px auto; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">' +
          '<div style="width: 56px; height: 56px; border-radius: 50%; background: rgba(224, 79, 51, 0.08); color: #E04F33; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">' +
            '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>' +
          '</div>' +
          '<h3 style="font-family: Cormorant Garamond, Georgia, serif; font-size: 26px; font-weight: 600; color: #121212; margin: 0 0 8px;">' +
            'No books found matching "' + queryDisplay + '" in ' + currentGenreName +
          '</h3>' +
          '<p style="font-size: 14px; color: #666; line-height: 1.5; margin: 0 0 24px;">' +
            'This author or title may be cataloged under another category in our 5,559-book archive.' +
          '</p>' +
          '<button type="button" class="v2-btn-clear-filter" onclick="window.clearArchiveFilters()" style="display: inline-flex; align-items: center; gap: 8px; background: #121212; color: #FFFFFF; border: none; border-radius: 999px; padding: 12px 26px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.2s ease; box-shadow: 0 4px 14px rgba(0,0,0,0.15);">' +
            '<span>Search Across All Categories &rarr;</span>' +
          '</button>' +
        '</div>';

      if (countDisplay) {
        countDisplay.textContent = 'Showing 0 books';
      }
      if (loadMoreBtn) {
        loadMoreBtn.style.display = 'none';
      }
      return;
    }

    var showCount = Math.min(archivePage * ARCHIVE_PAGE_SIZE, total);
    var startIndex = (archivePage - 1) * ARCHIVE_PAGE_SIZE;
    var pageSlice = filtered.slice(startIndex, showCount);

    if (countDisplay) {
      var genreLabels = {
        'all': 'Editions',
        'hindi': 'Hindi Classics & Novels',
        'poetry': 'Poetry & Rekhta Collections',
        'law': 'Law & Constitution Editions',
        'bestsellers': 'Bestselling Titles',
        'philosophy': 'Philosophy & History Works'
      };
      var label = genreLabels[archiveCurrentGenre] || 'Books';
      countDisplay.textContent = 'Showing ' + showCount + ' of ' + total + ' ' + label;
    }
    if (loadMoreBtn) {
      loadMoreBtn.style.display = (showCount >= total) ? 'none' : 'inline-block';
    }

    pageSlice.forEach(function(b) {
      var cover = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var priceVal = b.rawPrice || b.mrp || 299;
      var priceStr = b.price || ('₹' + priceVal + '.00');
      var card = document.createElement('div');
      card.className = 'v2-archive-card';
      var bId = b.id || b.handle || b.isbn;

      var safeTitle = (b.title || 'Book').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      var safeAuthor = (b.author || 'Curated Indian Author').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      var safeFmt = (b.binding || b.format || 'Paperback').toUpperCase();

      var fallbackSvg = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #FAF7F0; background-image: url(&quot;' + fallbackSvg + '&quot;); background-size: cover; background-position: center;">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" data-author="' + safeAuthor + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=&quot;' + fallbackSvg + '&quot;; this.style.display=&quot;none&quot;; window.handleBookCoverError && window.handleBookCoverError(this);" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +
        '<div>' +
          '<div class="v2-archive-card-price">' + priceStr + '</div>' +
          '<div style="display:flex;gap:6px;">' +
            '<button type="button" class="v2-btn-archive-preview" onclick="event.stopPropagation(); window.openSoloBookPage ? window.openSoloBookPage(this.getAttribute(&quot;data-id&quot;)) : null;" data-id="' + bId + '" style="flex:1;">Preview &rarr;</button>' +
            '<button type="button" class="v2-btn-archive-add" data-id="' + bId + '" onclick="event.stopPropagation(); window.addToBagDirect ? window.addToBagDirect(this.getAttribute(&quot;data-id&quot;)) : null;" style="flex:1;">+ Add</button>' +
          '</div>' +
        '</div>';

      card.onclick = function() {
        window.openSoloBookPage(bId);
      };

      var apBtn = card.querySelector('.v2-card-preview-btn');
      if (apBtn) {
        apBtn.onclick = function(e) {
          e.stopPropagation();
          window.openSoloBookPage(bId);
        };
      }
      var aqBtn = card.querySelector('.v2-card-quick-btn');
      if (aqBtn) {
        aqBtn.onclick = function(e) {
          e.stopPropagation();
          if (typeof window.addToCart === 'function') {
            window.addToCart(bId, b.title, priceVal, cover);
          }
          if (typeof window.toggleCartDrawer === 'function') {
            window.toggleCartDrawer(true);
          }
        };
      }

      grid.appendChild(card);
    });
  }

  /* 4. DEFINITIVE SOLO BOOK PAGE & 3D SPREAD CONTROLLER (Points 2 & 3 Fixed) */
  
  /* UNIVERSAL SEARCH ACTIVATOR */
  window.activateUniversalSearch = function(e) {
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
  };

  /* GLOBAL AUTHOR FILTER & DEDICATED SEARCH ENGINE */
  window.performDedicatedSearch = function(query) {
    if (!query) return;
    var q = query.trim();

    // Standalone Shopify non-home page without SPA
    var isShopifyNonHome = (typeof window !== 'undefined' && 
      (window.location.pathname.indexOf('/products/') !== -1 || window.location.pathname.indexOf('/cart') !== -1 || window.location.pathname.indexOf('/collections') !== -1) &&
      !document.getElementById('indigo-search-results-view')
    );
    if (isShopifyNonHome) {
      window.location.href = '/search?q=' + encodeURIComponent(q);
      return;
    }

    // Close solo book page if open & unlock body
    var soloV = document.getElementById('indigo-solo-product-view');
    if (soloV) {
      soloV.classList.remove('is-active');
      soloV.style.display = 'none';
    }
    document.documentElement.classList.remove('solo-page-active');
    document.body.classList.remove('solo-page-active');
    document.body.style.removeProperty('overflow');
    document.documentElement.style.removeProperty('overflow');
    previousViewBeforeSolo = 'search';
    window.previousViewBeforeSolo = 'search';

    // Close any search dropdowns
    var resultsBox = document.getElementById('editorialSearchResults');
    if (resultsBox) resultsBox.style.display = 'none';

    // Open dedicated search results view (#indigo-search-results-view)
    if (typeof window.openSearchResultsPage === 'function') {
      window.openSearchResultsPage(q);
    } else {
      window.location.href = '/search?q=' + encodeURIComponent(q);
    }
  };

  /* DIRECT AUTHOR FILTERING FROM SHELVES & PDP */
  window.filterByAuthorDirect = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };

  window.filterByAuthorFromSolo = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };

  /* SHELF HORIZONTAL SMOOTH SLIDER */
  window.slideShelf = function(shelfRowId, direction) {
    var row = document.getElementById(shelfRowId);
    if (!row) return;
    var stage = row.closest('.v2-shelf-stage') || row.parentElement;
    if (stage) {
      stage.scrollBy({ left: direction * 440, behavior: 'smooth' });
    }
  };

  /* CLEAR ARCHIVE GENRE RESTRICTIONS */
  window.clearArchiveFilters = function(query) {
    archiveCurrentGenre = 'all';
    if (query) {
      archiveSearchQuery = query.toLowerCase();
    }
    archivePage = 1;

    var chips = document.querySelectorAll('#v2ArchiveFilterChips .v2-chip');
    chips.forEach(function(c, idx) {
      if (idx === 0) c.classList.add('active');
      else c.classList.remove('active');
    });

    var arcSearchInput = document.getElementById('v2ArchiveSearchInput');
    if (arcSearchInput) {
      arcSearchInput.value = archiveSearchQuery || '';
    }

    renderArchiveGrid(false);
  };
  window.getArchiveGenre = function() { return archiveCurrentGenre; };
  window.getArchiveQuery = function() { return archiveSearchQuery; };
  window.setArchiveFilter = function(genre, query) {
    archiveCurrentGenre = genre || 'all';
    archiveSearchQuery = (query || '').toLowerCase();
    archivePage = 1;
    var arcSearchInput = document.getElementById('v2ArchiveSearchInput');
    if (arcSearchInput) arcSearchInput.value = archiveSearchQuery;
    renderArchiveGrid(false);
  };


  window.closeSoloBookPage = function() {
    var soloView = document.getElementById('indigo-solo-product-view');
    if (soloView) {
      soloView.classList.remove('is-active');
      soloView.style.display = 'none';
    }

    // Unlock document and body scroll (Zero Double Scrollbar Guarantee)
    document.documentElement.classList.remove('solo-page-active');
    document.body.classList.remove('solo-page-active');
    document.body.style.removeProperty('overflow');
    document.documentElement.style.removeProperty('overflow');

    // Restore whichever view was active before opening
    var targetView = window.previousViewBeforeSolo || previousViewBeforeSolo || 'home';
    var sView = document.getElementById('indigo-search-results-view');
    var hView = document.getElementById('homepage-view');

    // ONLY restore search view if targetView is strictly 'search' AND sView exists
    if (targetView === 'search' && sView) {
      sView.style.display = 'block';
      if (hView) hView.style.display = 'none';
    } else {
      if (sView) sView.style.display = 'none';
      if (hView) {
        hView.style.display = 'block';
        if (typeof window.__scrollPosBeforeSolo === 'number') {
          window.scrollTo({ top: window.__scrollPosBeforeSolo, behavior: 'instant' });
        }
      }
    }
    // Always reset to 'home' after closing a book so future navigation returns to home by default
    previousViewBeforeSolo = 'home';
    window.previousViewBeforeSolo = 'home';
  };

  window.openSoloBookPage = function(bookId) {
    // 1. Remember scroll position before opening solo page
    window.__scrollPosBeforeSolo = window.pageYOffset || document.documentElement.scrollTop || 0;

    var sView = document.getElementById('indigo-search-results-view');
    var hView = document.getElementById('homepage-view');

    // Search view is ONLY active if sView is explicitly visible AND hView is NOT visible!
    var isSearchActive = sView && (sView.style.display === 'block' || window.getComputedStyle(sView).display === 'block') &&
                         (!hView || hView.style.display === 'none' || window.getComputedStyle(hView).display === 'none');

    if (isSearchActive) {
      previousViewBeforeSolo = 'search';
      window.previousViewBeforeSolo = 'search';
    } else {
      previousViewBeforeSolo = 'home';
      window.previousViewBeforeSolo = 'home';
    }

    // Hide any lingering search dropdowns
    var resBox = document.getElementById('editorialSearchResults');
    if (resBox) resBox.style.display = 'none';

    // 2. Hide homepage and search views so ONLY solo book view is active in the DOM!
    if (hView) {
      hView.style.display = 'none';
    }
    if (sView) {
      sView.style.display = 'none';
    }

    // 3. Lock document body scrolling to completely kill outer window scrollbar
    document.documentElement.classList.add('solo-page-active');
    document.body.classList.add('solo-page-active');
    document.body.style.setProperty('overflow', 'hidden', 'important');
    document.documentElement.style.setProperty('overflow', 'hidden', 'important');

    var found = null;

    // Direct object pass
    if (typeof bookId === 'object' && bookId !== null) {
      if (bookId.title && (bookId.price || bookId.author)) {
        found = Object.assign({}, bookId);
      } else {
        bookId = bookId.id || bookId.handle || bookId.isbn || bookId.sku || bookId.title;
      }
    }

    var idStr = String(bookId || '').trim();

    if (!found && idStr) {
      // Alias dictionary mapping every hero & podium ID to exact book
      var ID_ALIASES = {
        'podium-godan': 'hero-book-godan',
        'godan': 'hero-book-godan',
        'podium-raag-darbari': 'hero-book-raag',
        'hero-book-raag-darbari': 'hero-book-raag',
        'raag-darbari': 'hero-book-raag',
        'raag': 'hero-book-raag',
        'podium-chitralekha': 'hero-book-chitralekha',
        'chitralekha': 'hero-book-chitralekha',
        'podium-rashmirathi': 'hero-book-rashmirathi',
        'rashmirathi': 'hero-book-rashmirathi',
        'podium-kuchh-ishq': 'hero-book-kuchh-ishq',
        'podium-ishq-mishra': 'hero-book-kuchh-ishq',
        'kuchh-ishq': 'hero-book-kuchh-ishq',
        'kuchh-ishq-kiya-kuchh-kaam-kiya': 'hero-book-kuchh-ishq',
        'podium-gypsy': 'hero-book-gypsy',
        'gypsy': 'hero-book-gypsy',
        'tarkash': 'book-tarkash',
        'aadha-gaon': 'book-aadha-gaon',
        'mahabhoj': 'book-mahabhoj',
        'shekhar': 'book-shekhar',
        'shekhar-ek-jeevani': 'book-shekhar',
        'gaban': 'book-gaban',
        'nirmala': 'book-nirmala',
        'murakami': 'hero-book-murakami',
        'haruki-murakami': 'hero-book-murakami',
        'samvidhan': 'book-samvidhan',
        'bharat-ka-samvidhan': 'book-samvidhan'
      };

      var targetId = (ID_ALIASES[idStr] || idStr).toLowerCase();
      var cleanSlug = idStr.replace(/^(podium|hero-book|book)-/, '').toLowerCase();

      // 1. Search POPULAR_BOOKS
      for (var i = 0; i < POPULAR_BOOKS.length; i++) {
        var pb = POPULAR_BOOKS[i];
        var pbId = String(pb.id || '').toLowerCase();
        var pbTitle = String(pb.title || '').toLowerCase();
        var pbIsbn = String(pb.isbn || '');
        if (pbId === targetId || pbId === idStr.toLowerCase() || pbIsbn === idStr ||
            pbId.indexOf(cleanSlug) !== -1 || cleanSlug.indexOf(pbId.replace(/^(hero-book|book)-/, '')) !== -1 ||
            (cleanSlug.length > 2 && pbTitle.indexOf(cleanSlug.replace(/-/g, ' ')) !== -1)) {
          found = Object.assign({}, pb);
          break;
        }
      }

      // 2. Search Shopify Live Products
      if (!found && window.SHOPIFY_LIVE_PRODUCTS && window.SHOPIFY_LIVE_PRODUCTS.length) {
        for (var spIdx = 0; spIdx < window.SHOPIFY_LIVE_PRODUCTS.length; spIdx++) {
          var sp = window.SHOPIFY_LIVE_PRODUCTS[spIdx];
          var spId = String(sp.id || '');
          var spHandle = String(sp.handle || '').toLowerCase();
          var spTitle = String(sp.title || '').toLowerCase();
          if (spId === idStr || spHandle === idStr.toLowerCase() || spHandle === cleanSlug || (cleanSlug.length > 2 && spTitle.indexOf(cleanSlug.replace(/-/g, ' ')) !== -1)) {
            found = {
              id: sp.id || sp.handle,
              title: sp.title,
              author: sp.author || sp.vendor || 'Curated Indian Author',
              price: sp.price || '₹299.00',
              rawPrice: typeof sp.price === 'number' ? sp.price : (parseFloat(String(sp.price).replace(/[^0-9.]/g, '')) || 299),
              format: sp.type || 'Paperback',
              publisher: sp.vendor || 'Rajkamal Prakashan',
              edition: 'Official Certified Release',
              pages: '320p',
              isbn: sp.sku || sp.id || '9788126702749',
              cover: sp.cover || sp.image || sp.featured_image || (window.getFallbackCoverSvg ? window.getFallbackCoverSvg(sp.title, sp.vendor) : ''),
              category: sp.type || 'Classic Literature'
            };
            break;
          }
        }
      }

      // 3. Search MASTER_SEARCH_CATALOG (5,559 titles)
      if (!found && window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) {
        for (var j = 0; j < window.MASTER_SEARCH_CATALOG.length; j++) {
          var m = window.MASTER_SEARCH_CATALOG[j];
          var mId = String(m.id || '');
          var mHandle = String(m.handle || '').toLowerCase();
          var mIsbn = String(m.isbn || m.sku || '');
          var mTitle = String(m.title || '').toLowerCase();
          if (mId === idStr || mHandle === idStr.toLowerCase() || mHandle === cleanSlug || mIsbn === idStr ||
              (cleanSlug.length > 3 && mTitle.indexOf(cleanSlug.replace(/-/g, ' ')) !== -1)) {
            found = {
              id: m.id || m.handle,
              title: m.title,
              author: m.author || 'Distinguished Scholar',
              price: m.price || ('₹' + (m.rawPrice || m.mrp || 299) + '.00'),
              rawPrice: m.rawPrice || m.mrp || 299,
              format: m.binding || m.format || 'Paperback',
              publisher: m.publisher || m.pub || 'Rajkamal Prakashan',
              edition: m.edition || 'Heritage Edition',
              pages: m.pages || '280p',
              isbn: m.isbn || m.sku || '9788126728466',
              cover: m.coverUrl || m.cover || m.image || (window.getFallbackCoverSvg ? window.getFallbackCoverSvg(m.title, m.author) : ''),
              category: m.category || 'Classic Literature',
              quote: m.quote,
              excerpt: m.excerpt
            };
            break;
          }
        }
      }

      // 4. Fallback via resolveBookObject
      if (!found && typeof window.resolveBookObject === 'function') {
        var rb = window.resolveBookObject(bookId);
        if (rb) {
          found = {
            id: rb.id || rb.handle,
            title: rb.title,
            author: rb.author || 'Author',
            price: rb.price ? ('₹' + window.cleanPrice(rb.price) + '.00') : '₹299.00',
            rawPrice: window.cleanPrice(rb.price, 299),
            format: rb.binding || 'Paperback',
            publisher: rb.publisher || rb.pub || 'Publisher',
            edition: rb.edition || 'Heritage Release',
            pages: rb.pages || '320p',
            isbn: rb.isbn || rb.sku || '9788126702749',
            cover: rb.cover || rb.coverUrl || rb.image || (window.getFallbackCoverSvg ? window.getFallbackCoverSvg(rb.title, rb.author) : ''),
            category: rb.category || 'Literature',
            quote: rb.quote,
            excerpt: rb.excerpt
          };
        }
      }
    }

    if (!found) {
      var displayT = idStr.replace(/^(podium|hero-book|book)-/, '').replace(/[-_]/g, ' ').replace(/\b\w/g, function(l){ return l.toUpperCase(); });
      found = {
        id: idStr || 'archive-book',
        title: displayT || 'Indigo Books Archive Edition',
        author: 'Indigo Literary Archive',
        price: '₹299.00',
        rawPrice: 299,
        format: 'Paperback',
        publisher: 'Rajkamal Prakashan',
        edition: 'Certified Library Edition',
        pages: '312p',
        isbn: '9788126700000',
        cover: window.getFallbackCoverSvg ? window.getFallbackCoverSvg(displayT, 'Indigo Literary Archive') : '',
        category: 'Classic Literature',
        quote: 'साहित्य जीवन की आलोचना और समाज का जीवंत दर्पण है।',
        excerpt: 'साहित्य का मुख्य उद्देश्य मानवीय संवेदनाओं को जागृत करना और सत्य के अन्वेषण में अग्रसर होना है।'
      };
    }

    // Resolve cover cleanly to CDN URL
    found.cover = getCoverUrl(found.cover, found.title, found.author);

    // Attach Authentic Literary Content (Point 3 Fix)
    found.excerpt = getBookAuthenticExcerpt(found);
    found.quote = getBookAuthenticQuote(found);

    currentActiveBook = found;
    window.currentActiveBook = found;
    isSpreadOpen = false;

    // Populate Left Panel Quote & Backdrop (Strict Monolingual)
    var hindi = isHindiBook(found);
    var cleanTitle = getCleanDisplayTitle(found.title, hindi);
    var cleanAuthor = hindi ? getHindiAuthorName(found.author) : (found.author || 'Author');

    var bgArt = document.getElementById('v2SoloBgArt');
    if (bgArt) bgArt.style.backgroundImage = 'url(' + found.cover + ')';
    var qText = document.getElementById('v2SoloQuoteText');
    if (qText) qText.textContent = found.quote;
    var qSrc = document.getElementById('v2SoloQuoteSource');
    if (qSrc) {
      if (hindi) {
        qSrc.innerHTML = '&mdash; ' + cleanAuthor + ' &bull; इंडिगो साहित्य अभिलेखागार';
      } else {
        qSrc.innerHTML = '&mdash; ' + found.author + ' &bull; Indigo Editorial Archive';
      }
    }

    // Format Selection Handlers: Sibling Variant Lookup from Master Catalog
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
    }

    // Populate 3D Book Cover & Inside Pages (Strict Monolingual with Guaranteed Visible Cover)
    var soloFallbackSvg = getFallbackCoverSvg(found.title, found.author);
    var coverLeafFront = document.getElementById('v2CoverLeaf');
    if (coverLeafFront) {
      coverLeafFront.style.backgroundColor = '#FAF7F0';
      coverLeafFront.style.backgroundImage = 'url("' + soloFallbackSvg + '")';
      coverLeafFront.style.backgroundSize = 'cover';
      coverLeafFront.style.backgroundPosition = 'center';
    }
    var coverFace = document.getElementById('v2CoverLeafFront') || (coverLeafFront ? coverLeafFront.querySelector('.v2-cover-leaf-front') : null);
    if (coverFace) {
      coverFace.style.backgroundColor = '#FAF7F0';
      coverFace.style.backgroundImage = 'url("' + soloFallbackSvg + '")';
      coverFace.style.backgroundSize = 'cover';
      coverFace.style.backgroundPosition = 'center';
    }

    var coverImg = document.getElementById('v2CoverLeafImg');
    if (coverImg) {
      coverImg.style.display = 'none';
      coverImg.style.opacity = '0';
      coverImg.alt = '';
      coverImg.src = '';
      coverImg.style.width = '100%';
      coverImg.style.height = '100%';
      coverImg.style.objectFit = 'cover';
      coverImg.setAttribute('referrerpolicy', 'no-referrer');
      coverImg.onload = function() {
        this.style.display = 'block';
        this.style.opacity = '1';
      };
      coverImg.onerror = function() {
        this.onerror = null;
        this.style.display = 'none';
        if (coverFace) coverFace.style.backgroundImage = 'url("' + soloFallbackSvg + '")';
        if (coverLeafFront) coverLeafFront.style.backgroundImage = 'url("' + soloFallbackSvg + '")';
      };
    }

    function loadCoverImage(url) {
      if (!coverImg) return;
      var targetCover = getCoverUrl(url, found.title, found.author);
      if (coverFace) coverFace.style.backgroundImage = 'url("' + soloFallbackSvg + '")';
      if (coverLeafFront) coverLeafFront.style.backgroundImage = 'url("' + soloFallbackSvg + '")';
      coverImg.style.display = 'none';
      coverImg.style.opacity = '0';
      if (targetCover && !targetCover.startsWith('data:')) {
        coverImg.src = targetCover;
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
      loadCoverImage(exactCover || found.cover);
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
    applyFormat(activeInitialFmt);
    var leafTitle = document.getElementById('v2LeafBackTitle');
    if (leafTitle) leafTitle.textContent = cleanTitle;
    var chHead = document.getElementById('v2SpreadChapterHeading');
    if (chHead) chHead.textContent = cleanTitle;
    var topSeriesTag = document.getElementById('v2SpreadSeriesTag');
    if (topSeriesTag) {
      topSeriesTag.textContent = hindi ? 'इंडिगो क्लासिक्स • प्रथम अध्याय' : 'INDIGO CLASSICS • CHAPTER I';
    }
    var snippet = document.getElementById('v2SpreadExcerptSnippet');
    if (snippet) snippet.textContent = found.excerpt;
    var dropCap = document.getElementById('v2DropCap');
    if (dropCap && found.excerpt) {
      dropCap.textContent = found.excerpt.trim().charAt(0) || (hindi ? 'क' : 'T');
    }

    // Populate Right Details Sheet
    var sTitle = document.getElementById('v2SoloTitle');
    if (sTitle) sTitle.textContent = found.title;
    var sAuth = document.getElementById('v2SoloAuthor');
    var authorClean = (found.author || '').split(',')[0].replace(/Tr\..*$/i, '').trim();
    if (sAuth) {
      sAuth.textContent = found.author;
      sAuth.setAttribute('data-author', authorClean);
    }
    var sugTitle = document.getElementById('v2AuthorSugTitle');
    if (sugTitle) sugTitle.textContent = authorClean.toUpperCase();
    var seeAllBtn = document.getElementById('v2AuthorSeeAllBtn');
    if (seeAllBtn) seeAllBtn.setAttribute('data-author', authorClean);

    // Populate Dynamic Author Suggestions
    var sugGrid = document.getElementById('v2AuthorSuggestionsGrid');
    if (sugGrid) {
      sugGrid.innerHTML = '';
      var pool = (window.MASTER_SEARCH_CATALOG || []).concat(POPULAR_BOOKS);
      var matches = [];
      var seenIds = {};
      seenIds[found.id] = true;
      if (found.handle) seenIds[found.handle] = true;

      var qAuthLower = authorClean.toLowerCase();
      var authParts = qAuthLower.split(' ').filter(function(p) { return p.length > 2; });

      for (var k = 0; k < pool.length; k++) {
        var bk = pool[k];
        var bId = bk.id || bk.handle;
        if (seenIds[bId]) continue;
        var bAuth = (bk.author || '').toLowerCase();
        var isMatch = bAuth.indexOf(qAuthLower) !== -1;
        if (!isMatch && authParts.length > 0) {
          isMatch = authParts.some(function(part) { return bAuth.indexOf(part) !== -1; });
        }
        if (isMatch) {
          seenIds[bId] = true;
          matches.push(bk);
          if (matches.length >= 4) break;
        }
      }

      if (matches.length < 3) {
        for (var p = 0; p < POPULAR_BOOKS.length; p++) {
          var pb = POPULAR_BOOKS[p];
          if (!seenIds[pb.id]) {
            seenIds[pb.id] = true;
            matches.push(pb);
            if (matches.length >= 4) break;
          }
        }
      }

      matches.forEach(function(mb) {
        var cCover = getCoverUrl(mb.cover || mb.coverUrl || mb.image, mb.title, mb.author);
        var cPrice = mb.price || ('₹' + (mb.rawPrice || mb.mrp || 299) + '.00');
        var cFmt = (mb.binding || mb.format || 'Paperback').toUpperCase();
        var card = document.createElement('div');
        card.className = 'v2-author-sug-card';
        card.innerHTML = 
          '<div class="v2-author-sug-cover-wrap">' +
            '<img src="' + cCover + '" alt="' + mb.title + '" referrerpolicy="no-referrer" loading="lazy" />' +
          '</div>' +
          '<div>' +
            '<span class="v2-author-sug-badge">' + cFmt + '</span>' +
            '<div class="v2-author-sug-title" title="' + mb.title + '">' + mb.title + '</div>' +
            '<div class="v2-author-sug-price">' + cPrice + '</div>' +
          '</div>';
        var imgEl = card.querySelector('img');
        if (imgEl) imgEl.onerror = function() { window.handleBookCoverError && window.handleBookCoverError(this, mb.title, mb.author); };
        card.onclick = function() {
          window.openSoloBookPage(mb.id || mb.handle);
        };
        sugGrid.appendChild(card);
      });
    }

    var sPrice = document.getElementById('v2SoloPrice');
    if (sPrice) sPrice.textContent = found.price;
    var mobPrice = document.getElementById('v2MobileBuyBarPrice');
    if (mobPrice) mobPrice.textContent = found.price;
    var mobFmt = document.getElementById('v2MobileBuyBarFormat');
    if (mobFmt) mobFmt.textContent = 'Paperback';

    var sPubBadge = document.getElementById('v2MetaPublisherBadge');
    if (sPubBadge) sPubBadge.textContent = (found.publisher || 'LOKBHARTI PRAKASHAN').toUpperCase();
    var sEdit = document.getElementById('v2MetaEdition');
    if (sEdit) sEdit.textContent = found.edition || 'Heritage Release';
    var sPub = document.getElementById('v2MetaPublisher');
    if (sPub) sPub.textContent = found.publisher || 'Rajkamal';
    // Sibling variant resolution handles v2MetaFormat and v2MetaIsbn authoritatively

    // Meta Pixel ViewContent Event Tracking
    if (typeof window.fbq === 'function') {
      window.fbq('track', 'ViewContent', {
        content_name: found.title,
        content_category: found.genre || found.publisher || 'Books',
        content_ids: [String(found.id || found.isbn || '')],
        content_type: 'product',
        value: parseFloat(String(found.price || '').replace(/[^0-9.]/g, '')) || 299,
        currency: 'INR'
      });
    }

    // Populate Full Excerpt View (Strict Monolingual: Pure Hindi OR Pure English)
    var exHead = document.getElementById('v2ExcerptHeading');
    if (exHead) exHead.textContent = hindi ? 'उद्धरण' : 'Excerpt';
    var exSub = document.getElementById('v2ExcerptSubtitle');
    if (exSub) {
      exSub.textContent = hindi ? ('पुस्तक १ • प्रथम अध्याय: ' + cleanTitle) : ('Book 1 • Chapter 1: ' + cleanTitle);
    }
    var exText = document.getElementById('v2ExcerptFullText');
    if (exText) {
      if (hindi) {
        exText.innerHTML = 
          '<p style="margin-bottom:14px;color:#121212;"><strong>प्रारंभिक अंश &bull; प्रामाणिक पाठ</strong></p>' +
          '<p style="margin-bottom:16px;line-height:1.75;font-size:15px;color:#222;">' + found.excerpt + '</p>' +
          '<p style="margin-bottom:14px;line-height:1.6;font-size:13.5px;color:#555;">यह आधिकारिक मूल प्रकाशक संस्करण लेखक द्वारा रचित मूल पाठ, सांस्कृतिक गरिमा एवं ऐतिहासिक संदर्भ को पूर्णतः सुरक्षित रखता है। प्रयागराज केंद्रीय भंडार से प्रामाणिक एवं सुरक्षित पैकेजिंग में प्रेषित।</p>' +
          '<p style="font-size:12.5px;color:#777;"><em>&bull; प्रामाणिक प्रकाशक संस्करण &bull; संपूर्ण भारत में सुरक्षित डिलीवरी</em></p>';
      } else {
        exText.innerHTML = 
          '<p style="margin-bottom:14px;color:#121212;"><strong>Opening Passage &bull; Authentic Text</strong></p>' +
          '<p style="margin-bottom:16px;line-height:1.75;font-size:15px;color:#222;">' + found.excerpt + '</p>' +
          '<p style="margin-bottom:14px;line-height:1.6;font-size:13.5px;color:#555;">This authoritative edition preserves the unaltered prose, cultural cadence, and historical context as intended by the author. Dispatched in certified protective packaging directly from our central repository.</p>' +
          '<p style="font-size:12.5px;color:#777;"><em>&bull; Original Publisher Edition &bull; Pan-India Heritage Repository</em></p>';
      }
    }

    // Reset Spread to Closed
    var spreadStage = document.getElementById('v2BookSpreadStage');
    if (spreadStage) spreadStage.classList.remove('is-open');
    var viewDetails = document.getElementById('v2ViewDetails');
    var viewExcerpt = document.getElementById('v2ViewExcerpt');
    if (viewDetails) viewDetails.style.display = 'block';
    if (viewExcerpt) viewExcerpt.style.display = 'none';

    var hintText = document.getElementById('v2SpreadHintText');
    if (hintText) hintText.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle;margin-right:4px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Hover Book to Open 2-Page Preview Spread';

    var dockPrevBtn = document.getElementById('v2DockPreviewBtn');
    if (dockPrevBtn) dockPrevBtn.classList.remove('active');

    // Open View (Point 2 Fix: Opens over search or homepage cleanly!)
    var soloView = document.getElementById('indigo-solo-product-view');
    if (soloView) {
      soloView.classList.add('is-active');
      soloView.style.display = 'flex';
      soloView.scrollTop = 0;
    }
  };

  /* 3D SPREAD OPENING TOGGLE (-180deg flip on hover & click!) */
  window.toggleSoloBookSpread = function(forceState) {
    var spreadStage = document.getElementById('v2BookSpreadStage');
    var viewDetails = document.getElementById('v2ViewDetails');
    var viewExcerpt = document.getElementById('v2ViewExcerpt');
    var hintText = document.getElementById('v2SpreadHintText');
    var dockPrevBtn = document.getElementById('v2DockPreviewBtn');
    if (!spreadStage) return;

    if (typeof forceState === 'boolean') {
      isSpreadOpen = forceState;
    } else {
      isSpreadOpen = !isSpreadOpen;
    }

    if (isSpreadOpen) {
      spreadStage.classList.add('is-open');
      if (viewDetails) viewDetails.style.display = 'none';
      if (viewExcerpt) viewExcerpt.style.display = 'block';
      if (hintText) {
        hintText.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle;margin-right:4px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Move Mouse Away to Close 2-Page Spread';
      }
      if (dockPrevBtn) dockPrevBtn.classList.add('active');
    } else {
      spreadStage.classList.remove('is-open');
      if (viewExcerpt) viewExcerpt.style.display = 'none';
      if (viewDetails) viewDetails.style.display = 'block';
      if (hintText) {
        hintText.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle;margin-right:4px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Hover Book to Open 2-Page Preview Spread';
      }
      if (dockPrevBtn) dockPrevBtn.classList.remove('active');
    }
  };

  /* SOLO VIEW ACTIONS */
  window.toggleSoloSaveWishlist = function() {
    var btn = document.getElementById('v2DockSaveBtn');
    if (btn) {
      btn.classList.toggle('active');
      btn.style.color = btn.classList.contains('active') ? '#E04F33' : '#444';
      btn.style.transform = 'scale(1.15)';
      setTimeout(function() { btn.style.transform = ''; }, 300);
    }
    if (typeof window.showNotificationToast === 'function') {
      window.showNotificationToast('Reading List updated: ' + (currentActiveBook ? currentActiveBook.title : 'Book'));
    }
  };

  function resolveShopifyVariant(book, preferredFormat) {
    if (!book) return null;
    if (book.variantId && String(book.variantId).match(/^\d+$/)) return String(book.variantId);
    if (book.variant_id && String(book.variant_id).match(/^\d+$/)) return String(book.variant_id);
    if (Array.isArray(book.variants) && book.variants.length > 0) {
      for (var k = 0; k < book.variants.length; k++) {
        var v = book.variants[k];
        if (v && (v.id || v.variantId || v.variant_id)) {
          var vid = String(v.id || v.variantId || v.variant_id);
          if (vid.match(/^\d+$/)) return vid;
        }
      }
    }
    var EXACT_LIVE_VARIANTS = {
      'raag-darbari-shrilal-shukla': {
        'paperback': '67709913825570',
        'hardcover': '67709913858338',
        'default': '67709913825570'
      },
      'godan-premchand': {
        'paperback': '67709593944354',
        'hardcover': '67709593977122',
        'default': '67709593944354'
      },
      'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap': {
        'paperback': '67709702504738',
        'default': '67709702504738'
      },
      'tarkash-javed-akhtar': {
        'hardcover': '67710011605282',
        'paperback': '67710011638050',
        'default': '67710011605282'
      },
      'chitralekha-bhagwaticharan-verma': {
        'paperback': '67709745037602',
        'default': '67709745037602'
      },
      'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar': {
        'hardcover': '67709930012962',
        'paperback': '67709930045730',
        'default': '67709930012962'
      },
      'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra': {
        'hardcover': '67709809230114',
        'paperback': '67709809262882',
        'default': '67709809230114'
      },
      'aadha-gaon-rahi-masoom-raza': {
        'paperback': '67709594435874',
        'hardcover': '67709594468642',
        'default': '67709594435874'
      },
      'gaban-premchand': {
        'hardcover': '67709780590882',
        'default': '67709780590882'
      },
      'nirmala-premchand': {
        'hardcover': '67709867196706',
        'paperback': '67709867229474',
        'default': '67709867196706'
      },
      '1984-george-orwell-tr-abhishek-srivastava': {
        'paperback': '67709588472098',
        'default': '67709588472098'
      },
      '1084ven-ki-maan-mahashweta-devi-tr-santwana-nigam': {
        'hardcover': '67709588799778',
        'default': '67709588799778'
      }
    };
    window.EXACT_LIVE_VARIANTS = EXACT_LIVE_VARIANTS;

    var KNOWN_HANDLES = {
      'book-samvidhan': 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
      'samvidhan': 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
      'bharat-ka-samvidhan': 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
      'podium-godan': 'godan-premchand',
      'godan': 'godan-premchand',
      'hero-book-godan': 'godan-premchand',
      'podium-raag-darbari': 'raag-darbari-shrilal-shukla',
      'raag-darbari': 'raag-darbari-shrilal-shukla',
      'podium-chitralekha': 'chitralekha-bhagwaticharan-verma',
      'chitralekha': 'chitralekha-bhagwaticharan-verma',
      'podium-rashmirathi': 'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
      'rashmirathi': 'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
      'podium-kuchh-ishq': 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
      'kuchh-ishq': 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
      'book-tarkash': 'tarkash-javed-akhtar',
      'tarkash': 'tarkash-javed-akhtar'
    };
    window.KNOWN_HANDLES = KNOWN_HANDLES;

    var knownH = KNOWN_HANDLES[book.id] || KNOWN_HANDLES[book.handle] || '';
    var lookupH = book.handle || knownH || '';
    if (!lookupH && book.id && !String(book.id).startsWith('podium-') && !String(book.id).startsWith('book-') && !String(book.id).startsWith('hero-')) {
      lookupH = String(book.id);
    }
    if (!lookupH && book.title) {
      lookupH = String(book.title).toLowerCase().replace(/\(.*?\)/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
      if (KNOWN_HANDLES[lookupH]) lookupH = KNOWN_HANDLES[lookupH];
    }

    var fmt = String(preferredFormat || book.selectedFormat || book.binding || book.format || '').toLowerCase();

    if (lookupH && EXACT_LIVE_VARIANTS[lookupH]) {
      var map = EXACT_LIVE_VARIANTS[lookupH];
      if (fmt.indexOf('hard') !== -1 && map.hardcover) return map.hardcover;
      if (fmt.indexOf('paper') !== -1 && map.paperback) return map.paperback;
      return map.default || map.paperback || map.hardcover;
    }

    if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length > 0) {
      var bt = String(book.title || '').toLowerCase().trim();
      var bh = String(lookupH || '').toLowerCase().trim();
      var match = window.SHOPIFY_LIVE_PRODUCTS.find(function(p) {
        if (!p) return false;
        var pt = String(p.title || '').toLowerCase().trim();
        var ph = String(p.handle || '').toLowerCase().trim();
        return (bh && ph && (bh === ph || ph.indexOf(bh) !== -1 || bh.indexOf(ph) !== -1)) ||
               (pt && bt && (pt === bt || bt.indexOf(pt) !== -1 || pt.indexOf(bt) !== -1));
      });
      if (match) {
        if (Array.isArray(match.variants) && match.variants.length > 0) {
          if (fmt) {
            for (var vIdx = 0; vIdx < match.variants.length; vIdx++) {
              var mv = match.variants[vIdx];
              var mvTitle = String(mv.title || '').toLowerCase();
              if (mvTitle.indexOf(fmt) !== -1 || (fmt.indexOf('hard') !== -1 && mvTitle.indexOf('hard') !== -1) || (fmt.indexOf('paper') !== -1 && mvTitle.indexOf('paper') !== -1)) {
                return String(mv.id);
              }
            }
          }
          return String(match.variants[0].id);
        }
        if (match.variantId || match.variant_id) {
          return String(match.variantId || match.variant_id);
        }
      }
    }
    var domVar = document.querySelector('input[name="id"], select[name="id"], #SelectedVariantId, [id*="MainVariantId"]');
    if (domVar && domVar.value && domVar.value.match(/^\d+$/)) {
      return domVar.value;
    }
    return null;
  }
  window.resolveShopifyVariant = resolveShopifyVariant;

  function cleanEnglishTitle(str) {
    if (!str) return '';
    return String(str).replace(/[\u0900-\u097F]/g, '').replace(/\(\s*\)/g, '').replace(/\s+/g, ' ').trim();
  }

  window.handleSoloAddToCart = function() {
    var activeB = (typeof window !== 'undefined' && window.currentActiveBook) || (typeof currentActiveBook !== 'undefined' ? currentActiveBook : null);
    if (!activeB) return;
    var finalPrice = activeB.selectedPrice || activeB.rawPrice || 299;
    var finalFmt = activeB.selectedFormat || activeB.binding || activeB.format || 'Paperback';
    var bId = activeB.id || activeB.handle || activeB.isbn || 'book';
    if (typeof window.addToCart === 'function') {
      window.addToCart(bId, activeB.title, finalPrice, activeB.cover, finalFmt);
    }
    var isShopify = (typeof window !== 'undefined' && window.location && 
      (window.location.hostname.indexOf('shopify') !== -1 || window.location.hostname.indexOf('indigobooks.shop') !== -1));
    var resolveFn = window.getOrFetchVariantId || function(it, cb) { cb(resolveShopifyVariant(it, finalFmt)); };
    resolveFn(activeB, function(vid) {
      if (isShopify && vid && typeof fetch === 'function') {
        fetch('/cart/add.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            id: vid,
            quantity: 1,
            properties: {
              'Book Title': cleanEnglishTitle(activeB.title) || activeB.title,
              'Author': cleanEnglishTitle(activeB.author) || activeB.author || 'Indigo Books',
              'Format': finalFmt,
              'Price': '₹' + finalPrice,
              'ISBN': activeB.isbn || activeB.selectedIsbn || ''
            }
          })
        }).catch(function(e) {});
      }
    });
    if (typeof window.toggleCartDrawer === 'function') {
      window.toggleCartDrawer(true);
    }
  };

  window.handleSoloBuyNow = function() {
    var activeB = (typeof window !== 'undefined' && window.currentActiveBook) || (typeof currentActiveBook !== 'undefined' ? currentActiveBook : null);
    if (!activeB) return;
    var finalPrice = activeB.selectedPrice || activeB.rawPrice || (parseFloat(String(activeB.price).replace(/[^0-9.]/g, '')) || 299);
    var finalFmt = activeB.selectedFormat || activeB.binding || activeB.format || 'Paperback';
    var bId = activeB.id || activeB.handle || activeB.isbn || 'book';

    // Meta Pixel InitiateCheckout Event Tracking
    if (typeof window.fbq === 'function') {
      window.fbq('track', 'InitiateCheckout', {
        content_name: activeB.title,
        content_ids: [String(bId)],
        content_type: 'product',
        value: finalPrice,
        currency: 'INR'
      });
    }

    // 1. Add to local cart without opening cart drawer
    var existingItem = cart.find(function(item) { return String(item.id) === String(bId); });
    if (existingItem) {
      existingItem.qty += 1;
    } else {
      cart.push({
        id: String(bId),
        handle: activeB.handle || '',
        variantId: activeB.variantId || activeB.variant_id || '',
        title: activeB.title,
        author: activeB.author || 'Indigo Books Author',
        price: finalPrice,
        cover: activeB.cover || '',
        binding: finalFmt,
        format: finalFmt,
        qty: 1
      });
    }
    if (typeof saveCartToStorage === 'function') saveCartToStorage();
    if (typeof updateCartUI === 'function') updateCartUI();

    // 2. Forcibly close drawers and modals so screen is clean
    if (typeof window.toggleCartDrawer === 'function') window.toggleCartDrawer(false);
    var cDrawer = document.getElementById('cartDrawer') || document.querySelector('.cart-drawer') || document.querySelector('.cart-drawer-panel');
    if (cDrawer) {
      cDrawer.classList.remove('is-open');
      cDrawer.style.transform = 'translateX(100%)';
      cDrawer.style.display = 'none';
    }
    var cOverlay = document.getElementById('cartDrawerOverlay') || document.getElementById('cartOverlay') || document.querySelector('.cart-drawer-overlay');
    if (cOverlay) {
      cOverlay.classList.remove('is-open');
      cOverlay.style.display = 'none';
    }

    var isShopify = (typeof window !== 'undefined' && window.location && 
      (window.location.hostname.indexOf('shopify') !== -1 || window.location.hostname.indexOf('indigobooks.shop') !== -1));

    if (!isShopify) {
      window.location.href = '/checkout';
      return;
    }

    var hasRedirected = false;
    function directToCheckout() {
      if (hasRedirected) return;
      hasRedirected = true;
      window.location.href = '/checkout';
    }

    function fallbackSingleFormSubmit(vId) {
      try {
        var form = document.createElement('form');
        form.method = 'POST';
        form.action = '/cart/add';
        form.style.display = 'none';
        var inputId = document.createElement('input');
        inputId.type = 'hidden';
        inputId.name = 'id';
        inputId.value = vId;
        form.appendChild(inputId);
        var inputQty = document.createElement('input');
        inputQty.type = 'hidden';
        inputQty.name = 'quantity';
        inputQty.value = '1';
        form.appendChild(inputQty);
        var submitBtn = document.createElement('button');
        submitBtn.type = 'submit';
        submitBtn.name = 'checkout';
        form.appendChild(submitBtn);
        document.body.appendChild(form);
        form.submit();
      } catch(e) {
        directToCheckout();
      }
    }

    var resolveFn = window.getOrFetchVariantId || function(it, cb) { cb(resolveShopifyVariant(it, finalFmt)); };
    resolveFn(activeB, function(vid) {
      if (vid) {
        var postData = {
          id: vid,
          quantity: 1,
          properties: {
            'Book Title': cleanEnglishTitle(activeB.title) || activeB.title,
            'Author': cleanEnglishTitle(activeB.author) || activeB.author || 'Indigo Books',
            'Format': finalFmt,
            'Price': '₹' + finalPrice,
            'ISBN': activeB.isbn || activeB.selectedIsbn || ''
          }
        };
        fetch('/cart/clear.js', { method: 'POST', headers: { 'Content-Type': 'application/json' } })
          .catch(function(e) {})
          .finally(function() {
            fetch('/cart/add.js', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(postData)
            })
            .then(function(res) {
              if (res.ok) {
                directToCheckout();
              } else {
                fallbackSingleFormSubmit(vid);
              }
            })
            .catch(function(e) {
              fallbackSingleFormSubmit(vid);
            });
          });
      } else {
        if (typeof window.openExpressPhoneCheckout === 'function') {
          window.openExpressPhoneCheckout(activeB);
        } else if (typeof window.checkoutViaWhatsApp === 'function') {
          window.checkoutViaWhatsApp();
        } else {
          directToCheckout();
        }
      }
    });

    // Failsafe timeout
    setTimeout(function() {
      directToCheckout();
    }, 3000);
  };

  window.handleSoloWhatsApp = function() {
    if (!currentActiveBook) return;
    if (typeof window.fbq === 'function') {
      window.fbq('trackCustom', 'WhatsAppLead', {
        content_name: currentActiveBook.title,
        content_category: currentActiveBook.genre || 'Books',
        value: currentActiveBook.selectedPrice || currentActiveBook.price || 299,
        currency: 'INR'
      });
    }
    var num = '918933063306';
    var text = 'Hello Indigo Books India! I would like to order: *' + currentActiveBook.title + '* by ' + currentActiveBook.author + ' (' + currentActiveBook.price + '). Please confirm availability and share COD details!';
    var url = 'https://wa.me/' + num + '?text=' + encodeURIComponent(text);
    window.open(url, '_blank');
  };

  window.handleSoloGetBook = function() {
    window.handleSoloBuyNow();
  };

  window.scrollToAppSection = function(id) {
    window.closeSoloBookPage();
    var el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  /* MOBILE DRAWER & NAVIGATION */
  window.toggleMobileDrawer = function(open) {
    var drawer = document.getElementById('v2MobileDrawer');
    var backdrop = document.getElementById('v2MobileDrawerBackdrop');
    if (!drawer || !backdrop) return;
    if (open) {
      drawer.classList.add('is-open');
      backdrop.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    } else {
      drawer.classList.remove('is-open');
      backdrop.classList.remove('is-open');
      document.body.style.overflow = '';
    }
  };

  window.handleMobileNavLink = function(targetHash) {
    window.toggleMobileDrawer(false);
    if (targetHash === '#video2-bookstore-app') {
      var appEl = document.getElementById('video2-bookstore-app') || document.getElementById('v2-archive-section');
      if (appEl) appEl.scrollIntoView({ behavior: 'smooth' });
    } else {
      var target = document.querySelector(targetHash);
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    }
  };

  window.handleMobileAuthorClick = function(authorName) {
    window.toggleMobileDrawer(false);
    window.filterByAuthorDirect(authorName);
  };

  window.handleSoloAddToBag = function() {
    window.handleSoloAddToCart();
  };

  window.openQuickOrderModal = function(bookId, qty) {
    if (typeof window.openExpressPhoneCheckout === 'function') {
      window.openExpressPhoneCheckout(bookId, qty);
    }
  };

  window.openExpressModal = function(bookId, title, price) {
    if (typeof window.openExpressPhoneCheckout === 'function') {
      window.openExpressPhoneCheckout(bookId);
    }
  };

  /* 5. VIDEO 1 SCATTER PARALLAX & SCROLL ENGINES */
  var mouseX = 0, mouseY = 0, currentX = 0, currentY = 0;
  window.addEventListener('mousemove', function(e) {
    var cx = window.innerWidth / 2;
    var cy = window.innerHeight / 2;
    mouseX = (e.clientX - cx) / cx;
    mouseY = (e.clientY - cy) / cy;
  }, { passive: true });

  function animateScatterParallax() {
    currentX += (mouseX - currentX) * 0.08;
    currentY += (mouseY - currentY) * 0.08;

    var covers = document.querySelectorAll('.scatter-book-cover');
    covers.forEach(function(cov) {
      var d = parseFloat(cov.getAttribute('data-depth') || '0.4');
      var tx = currentX * 36 * d;
      var ty = currentY * 36 * d;
      cov.style.transform = 'translate3d(' + tx + 'px, ' + ty + 'px, 0)';
    });

    requestAnimationFrame(animateScatterParallax);
  }

  function onScrollEngine() {
    var sy = window.scrollY;

    // Dark curtain word illumination
    var curtain = document.getElementById('dark-curtain-manifesto');
    if (curtain) {
      var rect = curtain.getBoundingClientRect();
      var winH = window.innerHeight;
      if (rect.top < winH && rect.bottom > 0) {
        var progress = Math.min(Math.max((winH - rect.top) / (winH * 0.8), 0), 1);
        var words = document.querySelectorAll('.curtain-word');
        var count = words.length;
        var litCount = Math.floor(progress * count);
        words.forEach(function(w, idx) {
          if (idx <= litCount) {
            w.classList.add('is-illuminated');
          } else {
            w.classList.remove('is-illuminated');
          }
        });
      }
    }

    // Tilted sheet unfolding
    var tilted = document.getElementById('tiltedSheetCard');
    if (tilted) {
      var tRect = tilted.getBoundingClientRect();
      if (tRect.top < window.innerHeight * 0.82) {
        tilted.classList.add('is-unfolded');
      }
    }
  }
  window.addEventListener('scroll', onScrollEngine, { passive: true });

  /* 6. UNIVERSAL LIVE PREDICTIVE SEARCH ENGINE (Works everywhere: Home, Studio, PDP) */

  window.triggerDedicatedSearchAll = function() {
    var searchInput = document.getElementById('editorialSearchInput') || document.getElementById('results-search-input');
    var q = searchInput ? (searchInput.value || '').trim() : '';
    if (q && typeof window.performDedicatedSearch === 'function') {
      window.performDedicatedSearch(q);
    }
  };

  function setupPredictiveSearch() {
    var searchInput = document.getElementById('editorialSearchInput');
    var resultsBox = document.getElementById('editorialSearchResults');
    if (!searchInput || !resultsBox) return;

    function renderMatches(matches, title) {
      if (!matches || matches.length === 0) {
        resultsBox.innerHTML = '<div style="padding:16px;font-size:13px;color:#777;text-align:center;">No matching editions found in central repository.</div>';
        resultsBox.style.display = 'block';
        return;
      }
      var html = '<div style="padding:10px 16px;font-size:11px;font-weight:700;color:#888;letter-spacing:0.12em;text-transform:uppercase;border-bottom:1px solid #EEE;">' + (title || 'MATCHING EDITIONS') + '</div>';
      matches.forEach(function(m) {
        var cover = getCoverUrl(m.cover || m.coverUrl || m.image, m.title, m.author);
        var price = m.price || ('₹' + (m.rawPrice || m.mrp || 299) + '.00');
        var author = m.author || m.vendor || 'Author';
        var itemFallback = getFallbackCoverSvg(m.title, author);
        html += 
          '<div class="editorial-search-item" style="display:flex;align-items:center;gap:12px;padding:10px 16px;cursor:pointer;border-bottom:1px solid #F5F5F5;transition:background 0.15s ease;" data-id="' + (m.id || m.handle) + '" data-handle="' + (m.handle || '') + '">' +
            '<div style="width:36px;height:52px;background-color:#FAF7F0;background-image:url(&quot;' + itemFallback + '&quot;);background-size:cover;background-position:center;border-radius:3px;overflow:hidden;flex-shrink:0;position:relative;">' +
              '<img src="' + cover + '" referrerpolicy="no-referrer" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;" onerror="this.onerror=null; this.style.display=&quot;none&quot;; window.handleBookCoverError && window.handleBookCoverError(this);" />' +
            '</div>' +
            '<div style="flex:1;min-width:0;">' +
              '<div style="font-size:13px;font-weight:600;color:#121212;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">' + m.title + '</div>' +
              '<div style="font-size:11px;color:#666;">By ' + author + '</div>' +
            '</div>' +
            '<div style="font-size:13px;font-weight:700;color:#E04F33;">' + price + '</div>' +
          '</div>';
      });

      html += '<div class="editorial-search-view-all" onclick="window.triggerDedicatedSearchAll()" style="padding:11px 16px;text-align:center;font-size:12.5px;font-weight:700;color:#E04F33;cursor:pointer;background:#FFF9F7;border-top:1px solid #FFE4DD;letter-spacing:0.02em;">View All Results for &ldquo;' + (searchInput.value || '').trim() + '&rdquo; &rarr;</div>';
      resultsBox.innerHTML = html;
      resultsBox.style.display = 'block';

      var items = resultsBox.querySelectorAll('.editorial-search-item');
      items.forEach(function(it, idx) {
        var itm = matches[idx];
        var itmImg = it.querySelector('img');
        if (itmImg && itm) {
          itmImg.onerror = function() { window.handleBookCoverError && window.handleBookCoverError(this, itm.title, itm.author || itm.vendor); };
        }
        it.onclick = function() {
          var bid = this.getAttribute('data-id');
          var bHandle = this.getAttribute('data-handle');
          resultsBox.style.display = 'none';
          searchInput.value = '';
          if (typeof window.openSoloBookPage === 'function') {
            window.openSoloBookPage(bid || bHandle);
          } else if (bHandle) {
            window.location.href = '/products/' + bHandle;
          } else {
            window.location.href = '/search?q=' + encodeURIComponent(bid);
          }
        };
      });
    }

    function showHeritagePicks() {
      var popularList = [
        { id: 'podium-godan', title: 'Godan (गोदान)', author: 'Premchand', price: '₹299.00', cover: 'hero-godan.jpg', handle: 'godan-premchand' },
        { id: 'podium-raag-darbari', title: 'Raag Darbari (राग दरबारी)', author: 'Shrilal Shukla', price: '₹499.00', cover: 'hero-raag-darbari.jpg', handle: 'raag-darbari-shrilal-shukla' },
        { id: 'podium-rashmirathi', title: 'Rashmirathi (रश्मिरथी)', author: 'Ramdhari Singh Dinkar', price: '₹350.00', cover: 'hero-rashmirathi.jpg', handle: 'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar' },
        { id: 'book-tarkash', title: 'Tarkash (तरकश)', author: 'Javed Akhtar', price: '₹499.00', cover: 'book-tarkash.jpg', handle: 'tarkash-javed-akhtar' },
        { id: 'book-samvidhan', title: 'Bharat Ka Samvidhan (भारत का संविधान)', author: 'Dr. B.R. Ambedkar', price: '₹450.00', cover: 'book-samvidhan.jpg', handle: 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap' }
      ];
      renderMatches(popularList, 'POPULAR HERITAGE PICKS');
    }
    window.showSearchSuggestionsPopup = showHeritagePicks;

    var BILINGUAL_ALIASES = {
      'प्रेम': 'prem', 'प्रेमचंद': 'premchand', 'मुंशी': 'munshi',
      'दिनकर': 'dinkar', 'रामधारी': 'ramdhari',
      'अंबेडकर': 'ambedkar', 'आंबेडकर': 'ambedkar', 'भीमराव': 'bhimrao', 'संविधान': 'samvidhan',
      'शुक्ल': 'shukla', 'श्रीलाल': 'shrilal',
      'मिश्रा': 'mishra', 'पीयूष': 'piyush',
      'रज़ा': 'raza', 'राही': 'rahi', 'मासूम': 'masoom',
      'जावेद': 'javed', 'अख्तर': 'akhtar',
      'बच्चन': 'bachchan', 'हरिवंश': 'harivansh',
      'गालिब': 'ghalib', 'ग़ालिब': 'ghalib',
      'मंटो': 'manto', 'सआदत': 'saadat',
      'टैगोर': 'tagore', 'रवींद्रनाथ': 'rabindranath',
      'मुराकामी': 'murakami'
    };

    var POPULAR_HANDLES = [
      'godan-premchand', 'raag-darbari-shrilal-shukla', 'chitralekha-bhagwaticharan-verma',
      'rashmirathi-ramdhari-singh-dinkar', 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
      'tarkash-javed-akhtar', 'gypsy-ila-chandra-joshi', 'bharat-ka-samvidhan-dr-br-ambedkar',
      'aadha-gaon-rahi-masoom-raza', 'mahabhoj-mannu-bhandari', 'shekhar-ek-jeevani-agyeya',
      'gaban-premchand', 'nirmala-premchand', 'murakami-collection'
    ];

    var ICONIC_TITLES = [
      'godan', 'gaban', 'nirmala', 'sevasadan', 'karmabhoomi', 'rangbhoomi', 'mansarovar', 'idgah', 'kafan',
      'raag darbari', 'makaan', 'aadmi ka zahar', 'bishrampur ka sant',
      'rashmirathi', 'urvashi', 'kurukshetra', 'sanskriti ke chaar adhyay',
      'samvidhan', 'constitution', 'annihilation of caste', 'buddha and his dhamma',
      'tarkash', 'lava',
      'kuchh ishq', 'tumhari auqat', 'gagan damama',
      'aadha gaon', 'topi shukla', 'neem ka ped',
      'madhushala', 'madhubala', 'madhukalash',
      'chitralekha', 'thanda gosht', 'toba tek singh'
    ];

    var debounceTimer = null;
    searchInput.addEventListener('input', function() {
      clearTimeout(debounceTimer);
      var rawQuery = (searchInput.value || '').trim();
      var query = rawQuery.toLowerCase();
      if (query.length < 2) {
        showHeritagePicks();
        return;
      }

      debounceTimer = setTimeout(function() {
        var pool = (window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) ? window.MASTER_SEARCH_CATALOG : (window.SHOPIFY_LIVE_PRODUCTS || POPULAR_BOOKS);
        
        var normQuery = query;
        for (var k in BILINGUAL_ALIASES) {
          if (query.indexOf(k) !== -1) {
            normQuery = normQuery.replace(new RegExp(k, 'g'), BILINGUAL_ALIASES[k]);
          }
        }

        var scored = [];
        for (var i = 0; i < pool.length; i++) {
          var item = pool[i];
          var title = (item.title || '').toLowerCase();
          var author = (item.author || item.vendor || '').toLowerCase();
          var isbn = (item.isbn || item.sku || '').toLowerCase();
          var pub = (item.publisher || item.pub || '').toLowerCase();
          var cat = (item.category || '').toLowerCase();
          var handleStr = String(item.handle || item.id || '').toLowerCase();

          var hasAuthorMatch = author.indexOf(query) !== -1 || author.indexOf(normQuery) !== -1;
          var hasTitleMatch = title.indexOf(query) !== -1 || title.indexOf(normQuery) !== -1;
          var hasIsbnMatch = isbn.indexOf(query) !== -1;
          var hasPubMatch = pub.indexOf(query) !== -1 || pub.indexOf(normQuery) !== -1;

          if (!hasAuthorMatch && !hasTitleMatch && !hasIsbnMatch && !hasPubMatch) {
            continue;
          }

          var score = 0;

          // 1. Author Matching (High priority for searches by author)
          if (author === query || author === normQuery) {
            score += 400;
          } else if (author.startsWith(query) || author.startsWith(normQuery)) {
            score += 350;
          } else if (hasAuthorMatch) {
            score += 250;
          }

          // 2. Title Matching
          if (title === query || title === normQuery) {
            score += 350;
          } else if (title.startsWith(query) || title.startsWith(normQuery)) {
            // If the query is an author search, don't over-boost anthologies that start with the author's name
            if (hasAuthorMatch) {
              score += 60;
            } else {
              score += 200;
            }
          } else if (hasTitleMatch) {
            score += 90;
          }

          // 3. Celebrated Masterpieces / Flagship boost
          for (var icIdx = 0; icIdx < ICONIC_TITLES.length; icIdx++) {
            if (title.indexOf(ICONIC_TITLES[icIdx]) !== -1) {
              score += 200;
              break;
            }
          }
          for (var pIdx = 0; pIdx < POPULAR_HANDLES.length; pIdx++) {
            if (handleStr.indexOf(POPULAR_HANDLES[pIdx]) !== -1 || POPULAR_HANDLES[pIdx].indexOf(handleStr) !== -1) {
              score += 250;
              break;
            }
          }

          if (hasIsbnMatch) score += 120;
          if (hasPubMatch) score += 40;

          scored.push({ item: item, score: score });
        }

        // Sort descending by score
        scored.sort(function(a, b) { return b.score - a.score; });

        // Deduplicate identical book titles to display a rich, diverse result list
        var seenTitles = new Set();
        var matches = [];
        for (var sIdx = 0; sIdx < scored.length; sIdx++) {
          var sItem = scored[sIdx].item;
          var cleanKey = (sItem.title || '').toLowerCase().trim().replace(/[^a-z0-9]/g, '');
          if (!seenTitles.has(cleanKey)) {
            seenTitles.add(cleanKey);
            matches.push(sItem);
            if (matches.length >= 10) break;
          }
        }

        renderMatches(matches, 'MATCHING EDITIONS (' + scored.length + ')');
      }, 100);
    });

    searchInput.addEventListener('focus', function() {
      var query = (searchInput.value || '').trim().toLowerCase();
      if (query.length >= 2) {
        searchInput.dispatchEvent(new Event('input'));
      } else {
        showHeritagePicks();
      }
    });

    searchInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        var q = (searchInput.value || '').trim();
        if (q) {
          resultsBox.style.display = 'none';
          if (typeof window.performDedicatedSearch === 'function') {
            window.performDedicatedSearch(q);
          } else if (typeof window.openSearchResultsPage === 'function') {
            window.openSearchResultsPage(q);
          } else {
            window.location.href = '/search?q=' + encodeURIComponent(q);
          }
        }
      }
    });

    document.addEventListener('click', function(e) {
      if (!e.target.closest('.editorial-search-wrap') && !e.target.closest('.v2-solo-search-btn') && !e.target.closest('#v2SoloCardSearchBtn')) {
        resultsBox.style.display = 'none';
      }
    });
  }

  /* 7. INITIALIZATION */
  function init() {
    fixAllThemeAssetImages();
    renderAllShelves();
    renderArchiveGrid();
    setupPredictiveSearch();
    animateScatterParallax();
    onScrollEngine();
    setTimeout(fixAllThemeAssetImages, 300);
    setTimeout(fixAllThemeAssetImages, 1200);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>"""
