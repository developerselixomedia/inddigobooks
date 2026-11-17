with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update solo view CSS in EDITORIAL_STYLE
target_solo_css = """#indigo-solo-product-view,
  .v2-solo-product-view,
  .section-main-product {
    position: fixed !important;
    top: 72px !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100vw !important;
    height: calc(100vh - 72px) !important;
    z-index: 100 !important; /* Strictly subordinate to Navbar (10,000,000) so search dropdown always floats in front */
    display: none;
    background: #EFECE6 !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 20px !important;
    box-sizing: border-box !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
  }

  @media (max-height: 800px) {
    #indigo-solo-product-view {
      justify-content: flex-start !important;
      padding: 16px 20px 40px !important;
    }
  }

  #indigo-solo-product-view::-webkit-scrollbar {
    width: 5px !important;
  }
  #indigo-solo-product-view::-webkit-scrollbar-thumb {
    background: rgba(18, 18, 18, 0.2) !important;
    border-radius: 999px !important;
  }

  @media (max-width: 900px) {
    header.site-navbar,
    .site-header {
      height: 60px !important;
    }
    #indigo-solo-product-view {
      top: 60px !important;
      height: calc(100vh - 60px) !important;
      padding: 10px 10px 30px 10px !important;
    }
  }
  #indigo-solo-product-view.is-active {
    display: flex !important;
  }"""

replacement_solo_css = """#indigo-solo-product-view,
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

  @media (max-width: 900px) {
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
      height: 380px !important;
      min-height: 380px !important;
      padding: 20px !important;
      overflow: hidden !important;
    }
    .v2-solo-right-panel {
      width: 100% !important;
      height: auto !important;
      overflow: visible !important; /* Mobile: NO duplicate nested scrollbar! */
      padding: 24px 18px 80px 18px !important;
    }
  }
  #indigo-solo-product-view.is-active {
    display: flex !important;
  }"""

assert target_solo_css in content, "target_solo_css not found in editorial_video_theme.py!"
content = content.replace(target_solo_css, replacement_solo_css, 1)

# 2. Add Drawer Classes CSS
target_drawer_css = """  .v2-mobile-drawer-backdrop.is-open {
    opacity: 1 !important;
    pointer-events: auto !important;
  }"""

replacement_drawer_css = """  .v2-mobile-drawer-backdrop.is-open {
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
  }"""

assert target_drawer_css in content, "target_drawer_css not found in editorial_video_theme.py!"
content = content.replace(target_drawer_css, replacement_drawer_css, 1)

# 3. Update getCoverUrl to intercept rajkamalprakashan
target_getcoverurl = """function getCoverUrl(coverPath, defaultTitle) {
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
    // If already absolute HTTP/HTTPS, protocol-relative '//', or data URI, return DIRECTLY without tampering
    if (coverPath.indexOf('http://') === 0 || coverPath.indexOf('https://') === 0 || coverPath.indexOf('//') === 0 || coverPath.indexOf('data:') === 0) {
      return coverPath;
    }"""

replacement_getcoverurl = """function getCoverUrl(coverPath, defaultTitle) {
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

assert target_getcoverurl in content, "target_getcoverurl not found in editorial_video_theme.py!"
content = content.replace(target_getcoverurl, replacement_getcoverurl, 1)

# 4. Update openSoloBookPage and closeSoloBookPage
target_close_solo = """window.closeSoloBookPage = function() {
    var soloView = document.getElementById('indigo-solo-product-view');
    if (soloView) {
      soloView.classList.remove('is-active');
      soloView.style.display = 'none';
    }

    // Unlock document and body scroll
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';"""

replacement_close_solo = """window.closeSoloBookPage = function() {
    var soloView = document.getElementById('indigo-solo-product-view');
    if (soloView) {
      soloView.classList.remove('is-active');
      soloView.style.display = 'none';
    }

    // Unlock document and body scroll (Zero Double Scrollbar Guarantee)
    document.documentElement.classList.remove('solo-page-active');
    document.body.classList.remove('solo-page-active');
    document.body.style.removeProperty('overflow');
    document.documentElement.style.removeProperty('overflow');"""

assert target_close_solo in content, "target_close_solo not found in editorial_video_theme.py!"
content = content.replace(target_close_solo, replacement_close_solo, 1)

target_open_solo = """    // 3. Lock document body scrolling to completely kill outer window scrollbar
    document.body.style.overflow = 'hidden';
    document.documentElement.style.overflow = 'hidden';"""

replacement_open_solo = """    // 3. Lock document body scrolling to completely kill outer window scrollbar
    document.documentElement.classList.add('solo-page-active');
    document.body.classList.add('solo-page-active');
    document.body.style.setProperty('overflow', 'hidden', 'important');
    document.documentElement.style.setProperty('overflow', 'hidden', 'important');"""

assert target_open_solo in content, "target_open_solo not found in editorial_video_theme.py!"
content = content.replace(target_open_solo, replacement_open_solo, 1)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated editorial_video_theme.py!")
