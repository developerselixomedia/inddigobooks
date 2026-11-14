# -*- coding: utf-8 -*-
"""
build_html_generator.py
Assembles preview.html using data from store_data, store_styles, and store_scripts.
Ensures ZERO raw Liquid tags, ZERO fake discounts, ZERO strikethroughs, and 100% exact CSV prices.
"""

from prepare_master_blocks import MASTER_STYLE, MASTER_SCRIPT
from cyber_theme_block import CYBER_STYLE, CYBER_SCRIPT
import json
from store_data import (
    PODIUM_BOOKS,
    POET_SHAYARI_DATA,
    REKHTA_BOOKS,
    BUNDLE_BOOKS,
    HINDI_FEATURE_BOOK,
    HINDI_GRID_BOOKS,
    VAULT_TABS,
    VAULT_BOOKS,
    CATEGORY_SHELVES,
    PIYUSH_MISHRA_BOOKS,
    RAHI_MASOOM_RAZA_BOOKS,
    CATEGORY_BENTO_DATA,
    CATALOG_BOOKS,
    MASTER_SEARCH_CATALOG,
    MODAL_METADATA_DATABASE
)
from store_styles import UNIFIED_STORE_CSS
from store_scripts import UNIFIED_STORE_JS

def render_category_bento_showcase():
    cat_data = CATEGORY_BENTO_DATA['contemporary']
    left = cat_data['left']
    right_cards = cat_data['right']
    
    left_html = f'''
      <div class="bento-left-spotlight" id="bentoLeftSpotlight" data-book-id="{left['id']}" data-title="{left['title']}" data-author="{left['author']}" data-price="{left['price']}">
        <div>
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 8px;">
            {left.get('tag', 'FEATURED SPOTLIGHT')}
          </div>
          <div class="bento-left-cover-wrap">
            <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{left['id']}', event)" style="cursor: pointer;">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">INDIGO ARCHIVE</div>
                <div style="font-family: 'Merriweather', serif; font-size: 13px; line-height: 1.35; color: #1E293B; font-weight: 700;">{left['title']}</div>
                <div style="font-size: 11px; color: #64748B;">By {left['author']}</div>
                <div style="font-size: 9.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 4px;">{left.get('specs', 'Standard Edition')}</div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img src="{left['coverUrl']}" alt="{left['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                </div>
              </div>
            </div>
          </div>
          <div style="font-size: 11px; font-weight: 700; color: #0066B3; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">
            {left.get('badge', 'RECOMMENDED READ')}
          </div>
          <h3 id="bentoLeftTitle" style="font-family: 'Merriweather', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; line-height: 1.3; margin: 0 0 6px;">
            <a href="javascript:void(0)" onclick="openSoloBookPage('{left['id']}', event)" style="color: inherit; text-decoration: none;">{left['title']}</a>
          </h3>
          <div id="bentoLeftAuthor" style="font-size: 14px; font-weight: 600; color: #64748B; margin-bottom: 12px;">{left['author']}</div>
          <p id="bentoLeftBlurb" style="font-size: 13px; color: #334155; line-height: 1.6; margin: 0 0 14px;">
            "{left.get('quote', left.get('blurb', ''))}"
          </p>
          <div id="bentoLeftSpecs" style="font-size: 12px; color: #64748B; margin-bottom: 16px;">
            {left.get('specs', '')}
          </div>
        </div>
        <div>
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 16px;">
            <span id="bentoLeftPrice" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{left['price']}</span>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <button type="button" class="btn-overview" onclick="openOverviewModal('{left['id']}')">
              <i data-lucide="book-open" style="width: 15px; height: 15px;"></i> Overview
            </button>
            <button type="button" class="btn-add-cart" onclick="addToCart('{left['id']}', '{left['title']}', '{left['price']}', '{left['coverUrl']}', this, event)">
              <i data-lucide="shopping-bag" style="width: 15px; height: 15px;"></i> Add to Bag
            </button>
          </div>
        </div>
      </div>
    '''
    
    right_cards_html = []
    for rb in right_cards:
        rc_html = f'''
          <div class="bento-horiz-card" data-book-id="{rb['id']}" data-title="{rb['title']}" data-author="{rb['author']}" data-price="{rb['price']}">
            <div>
              <div class="bento-horiz-top">
                <div class="bento-horiz-cover">
                  <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{rb['id']}', event)" style="cursor: pointer;">
                    <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                      <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                      <div style="font-family: 'Merriweather', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">{rb['title']}</div>
                      <div style="font-size: 7.5px; color: #64748B;">{rb['author']}</div>
                    </div>
                    <div class="indigo-3d-cover-leaf">
                      <div class="indigo-3d-cover-front">
                        <img src="{rb['coverUrl']}" alt="{rb['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                      </div>
                    </div>
                  </div>
                </div>
                <div style="min-width: 0;">
                  <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    {rb.get('tag', 'LITERARY WORK')}
                  </div>
                  <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                    <a href="javascript:void(0)" onclick="openSoloBookPage('{rb['id']}', event)" style="color: inherit; text-decoration: none;">{rb['title']}</a>
                  </h4>
                  <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{rb['author']}</div>
                  <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">{rb.get('specs', 'Paperback')}</div>
                  <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{rb['price']}</div>
                </div>
              </div>
              <p style="font-size: 12px; color: #64748B; line-height: 1.5; margin: 0 0 8px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                {rb.get('desc', '')}
              </p>
            </div>
            <div class="bento-card-actions">
              <button type="button" class="btn-overview" style="padding: 7px 10px; font-size: 12px;" onclick="openOverviewModal('{rb['id']}')">
                <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('{rb['id']}', '{rb['title']}', '{rb['price']}', '{rb['coverUrl']}', this, event)">
                <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> + Add
              </button>
            </div>
          </div>
        '''
        right_cards_html.append(rc_html)
    
    right_2x2_html = f'''<div class="bento-right-2x2" id="bentoRightGrid">{''.join(right_cards_html)}</div>'''
    
    return f'''
    <!-- =========================================================================
         6. SECTION 3: INDIAN VOICES & CATEGORY SHOWCASE (image_68cd69.jpg Asymmetric Layout)
         ========================================================================= -->
    <section id="category-bento-showcase" class="category-bento-section">
      <div class="category-bento-showcase">
        <div class="bento-header-wrap">
          <div>
            <div class="sec-overline">AUTHENTIC REGIONAL &amp; NATIONAL LITERATURE</div>
            <h2 style="font-family: 'Merriweather', Georgia, serif; font-size: 28px; font-weight: 700; color: #0F172A; margin: 4px 0 6px;">Indian Voices &amp; Curated Literary Categories</h2>
            <p style="font-size: 14px; color: #64748B; margin: 0;">Handpicked classics, modern Hindi fiction, Urdu poetry, academic law treatises, and historic milestones.</p>
          </div>
          <a href="#shop-all-catalog" onclick="browseAllBooks(event)" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none;">
            Explore All 5,500+ Titles &rarr;
          </a>
        </div>

        <!-- 5 Category Filter Switcher Pills -->
        <div class="category-pills-bar">
          <button type="button" class="cat-bento-pill active" data-cat="contemporary" onclick="switchCategoryBento('contemporary')">Contemporary Hindi Fiction</button>
          <button type="button" class="cat-bento-pill" data-cat="poetry" onclick="switchCategoryBento('poetry')">Poetry, Ghazals &amp; Shayari</button>
          <button type="button" class="cat-bento-pill" data-cat="classics" onclick="switchCategoryBento('classics')">Classic Hindi Novels (Premchand &amp; Masters)</button>
          <button type="button" class="cat-bento-pill" data-cat="history" onclick="switchCategoryBento('history')">History, Criticism &amp; Politics</button>
          <button type="button" class="cat-bento-pill" data-cat="law" onclick="switchCategoryBento('law')">Law &amp; Constitutional Studies</button>
        </div>

        <!-- Asymmetric Showcase Grid (image_68cd69.jpg layout: Left 400px + Right 2x2 Grid) -->
        <div class="category-bento-grid" id="categoryBentoGrid">
          {left_html}
          {right_2x2_html}
        </div>
      </div>
    </section>
    '''

def build_preview_html():
    podium_json = json.dumps(PODIUM_BOOKS, ensure_ascii=False)
    poet_json = json.dumps(POET_SHAYARI_DATA, ensure_ascii=False)
    vault_json = json.dumps(VAULT_BOOKS, ensure_ascii=False)
    bento_json = json.dumps(CATEGORY_BENTO_DATA, ensure_ascii=False)
    catalog_json = json.dumps(CATALOG_BOOKS, ensure_ascii=False)
    piyush_json = json.dumps(PIYUSH_MISHRA_BOOKS, ensure_ascii=False)
    rahi_json = json.dumps(RAHI_MASOOM_RAZA_BOOKS, ensure_ascii=False)
    master_search_json = json.dumps(MASTER_SEARCH_CATALOG, ensure_ascii=False)
    modal_meta_json = json.dumps(MODAL_METADATA_DATABASE, ensure_ascii=False)

    head_str = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Indigo Books India — Premier Online Bookstore Prayagraj (Official)</title>
  
  <!-- Official Vector SVG Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='16' fill='%230066B3'/%3E%3Cpath d='M20 20h25v25H20zM55 20h25v25H55zM20 55h25v25H20zM55 55h25v25H55z' fill='none' stroke='%23ffffff' stroke-width='6'/%3E%3C/svg%3E" />

  <!-- Google Fonts: Merriweather & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS Engine -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Complete Standard Production Stylesheet -->
  <style>
"""
    body_str = """</style>
</style>
</style>
</style>
</style>
</style>
</style>
</style>
</head>
<body id="top">

  <!-- =========================================================================
       1. STICKY NAVBAR
       ========================================================================= -->
  <header class="site-navbar">
    <div class="site-container navbar-inner">
      
      <!-- Brand Identity -->
      <a href="#top" class="brand-link" onclick="window.returnToHome(event)" aria-label="Indigo Books India Homepage">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 354 352" width="40" height="40" class="indigo-emblem-svg shrink-0" style="width: 40px !important; height: 40px !important; max-width: 40px !important; max-height: 40px !important; min-width: 40px !important; min-height: 40px !important; display: inline-block !important; vertical-align: middle !important; flex-shrink: 0 !important; object-fit: contain !important;" fill="#0066B3" fill-rule="evenodd" aria-hidden="true"><path d="M 207 206 L 207 308 L 211 312 L 296 313 L 296 351 L 352 350 L 351 295 L 313 294 L 313 210 L 309 206 Z M 314 312 L 335 313 L 334 334 L 313 333 Z M 224 223 L 296 224 L 295 295 L 223 294 Z M 44 206 L 42 207 L 41 208 L 40 210 L 39 295 L 1 295 L 1 351 L 57 350 L 58 312 L 141 312 L 143 311 L 146 308 L 146 206 Z M 19 312 L 40 313 L 39 334 L 18 333 Z M 58 223 L 129 224 L 128 295 L 57 294 Z M 296 1 L 295 39 L 212 39 L 210 40 L 207 43 L 207 145 L 309 145 L 313 141 L 314 56 L 352 55 L 351 0 Z M 224 56 L 296 57 L 295 128 L 223 127 Z M 314 17 L 335 18 L 334 39 L 313 38 Z M 75 0 L 75 17 L 144 17 L 147 18 L 150 19 L 152 20 L 154 21 L 158 24 L 162 28 L 164 31 L 167 37 L 168 41 L 167 167 L 42 167 L 38 166 L 32 163 L 28 160 L 24 156 L 22 153 L 19 147 L 18 143 L 18 74 L 1 74 L 1 143 L 2 149 L 3 152 L 4 155 L 8 163 L 10 166 L 19 176 L 10 185 L 8 188 L 6 192 L 3 198 L 2 202 L 1 208 L 1 277 L 18 277 L 18 208 L 19 204 L 23 196 L 29 190 L 32 188 L 38 185 L 42 184 L 168 185 L 168 310 L 167 314 L 164 320 L 154 330 L 152 331 L 150 332 L 147 333 L 144 334 L 75 334 L 75 351 L 144 351 L 149 350 L 153 349 L 156 348 L 162 345 L 165 343 L 169 340 L 176 332 L 185 341 L 188 343 L 191 345 L 197 348 L 200 349 L 203 350 L 209 351 L 278 351 L 278 334 L 209 334 L 205 333 L 199 330 L 195 327 L 191 323 L 189 320 L 186 314 L 185 311 L 186 184 L 311 184 L 315 185 L 321 188 L 324 190 L 329 195 L 331 198 L 332 200 L 333 202 L 334 205 L 335 209 L 335 277 L 352 276 L 352 209 L 351 203 L 350 199 L 349 196 L 345 188 L 342 184 L 333 175 L 342 167 L 345 163 L 349 155 L 350 152 L 351 148 L 352 142 L 352 74 L 335 74 L 335 142 L 334 146 L 333 149 L 332 151 L 331 153 L 328 156 L 328 157 L 326 159 L 321 163 L 315 166 L 311 167 L 185 166 L 185 40 L 186 37 L 187 34 L 188 32 L 191 28 L 196 23 L 199 21 L 205 18 L 209 17 L 278 17 L 278 0 L 209 0 L 203 1 L 200 2 L 197 3 L 189 7 L 186 9 L 176 19 L 168 10 L 165 8 L 162 6 L 156 3 L 153 2 L 149 1 L 144 0 Z M 1 0 L 2 56 L 40 57 L 40 141 L 44 145 L 146 145 L 146 43 L 143 40 L 141 39 L 57 38 L 56 0 Z M 58 56 L 129 57 L 128 128 L 57 127 Z M 19 17 L 40 18 L 39 39 L 18 38 Z" /></svg>
        <div class="brand-wordmark">
          INDIGO BOOKS
          <span class="brand-submark">PRAYAGRAJ • INDIA</span>
        </div>
      </a>

      <!-- Navigation Tabs -->
      <ul class="nav-links-wrap">
        <li><a href="#top" class="nav-link-btn" onclick="window.returnToHome(event)">Home</a></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('all')">Shop All (5,500+)</button></li>
        <li><a href="#bestsellers-podium" class="nav-link-btn" onclick="closeDedicatedProductPage(); document.getElementById('bestsellers-podium').scrollIntoView({behavior: 'smooth'})">Best Sellers</a></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('shayari')">Shayari &amp; Poetry</button></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('novel')">Hindi Novels</button></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToVault('law')">Law Books</button></li>
      </ul>

      <!-- Right Actions -->
      <div class="nav-actions">
        <span class="india-badge"><span class="tiranga-dot"></span>India Centric</span>
        <button type="button" class="nav-signin-btn" onclick="toggleLoginModal()">
          <i data-lucide="user" style="width: 15px; height: 15px;"></i> <span class="nav-signin-text">Sign In</span>
        </button>
        <button type="button" class="nav-cart-btn" onclick="toggleCartDrawer(true)" aria-label="Open Shopping Cart">
          <i data-lucide="shopping-bag" style="width: 16px; height: 16px;"></i>
          <span>Cart (<span id="nav-cart-count">0</span>)<span class="nav-cart-price-wrap"><span class="nav-cart-price-divider"> • </span><span id="nav-cart-total" class="nav-cart-total-span">₹0.00</span></span></span>
        </button>
        <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books%20Prayagraj!%20I%20would%20like%20to%20order%20books." target="_blank" class="nav-whatsapp-btn">
          <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i>
          <span>Order</span>
        </a>
      </div>

    </div>
  </header>


  <!-- =========================================================================
       HOMEPAGE VIEW (#homepage-view)
       ========================================================================= -->
  <div id="homepage-view" class="store-view-section">

        <!-- =========================================================================
         2. HERO SECTION & SEQUENTIAL SPOTLIGHT ANIMATION
         ========================================================================= -->
    <style id="hero-locked-styles">
      /* LOCKED 2-COLUMN HERO LAYOUT */
      #indigo-video-hero,
      #indigo-hero-master,
      .ivh-section {
        position: relative !important;
        min-height: 520px !important;
        width: 100% !important;
        background: linear-gradient(115deg, #09132C 0%, #101D40 48%, #2B2118 78%, #4A3314 100%) !important;
        overflow: visible !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 !important;
        z-index: 500 !important;
      }

      .hero-bg-clip {
        position: absolute !important;
        inset: 0 !important;
        overflow: hidden !important;
        pointer-events: none !important;
        z-index: 1 !important;
      }

      .ivh-container {
        position: relative !important;
        z-index: 600 !important;
        overflow: visible !important;
        max-width: 1320px !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding: 44px 24px !important;
        display: grid !important;
        grid-template-columns: 1fr 1.1fr !important;
        gap: 32px !important;
        align-items: center !important;
        box-sizing: border-box !important;
      }

      /* LEFT COLUMN: HEADING, SUBTITLE, SEARCH & BUTTONS */
      .ivh-left {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        text-align: left !important;
        z-index: 610 !important;
        overflow: visible !important;
        order: 1 !important;
      }

      .ivh-title {
        font-family: 'Merriweather', Georgia, serif !important;
        font-size: 52px !important;
        font-weight: 700 !important;
        line-height: 1.12 !important;
        color: #FFFFFF !important;
        margin: 0 0 16px 0 !important;
      }

      .ivh-story-italic {
        font-family: 'Merriweather', Georgia, serif !important;
        font-style: italic !important;
        color: #E5A93C !important;
      }

      /* RIGHT COLUMN: RANGOLI + STRICT 3x2 BOOK GRID + DIYAS */
      .ivh-right {
        position: relative !important;
        min-height: 430px !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        order: 2 !important;
      }

      .ivh-rangoli-anchor {
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        width: 440px !important;
        height: 440px !important;
        transform: translate(-50%, -50%) !important;
        z-index: 8 !important;
        pointer-events: none !important;
      }

      .ivh-rangoli-spin {
        width: 100% !important;
        height: 100% !important;
        animation: ivhSpinClockwise 42s linear infinite !important;
        transform-origin: center center !important;
      }

      @keyframes ivhSpinClockwise {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }

      /* STRICT 3 COLUMNS x 2 ROWS BOOK GRID (NEVER STACK VERTICALLY!) */
      #ivh-books-grid,
      .ivh-books-grid {
        position: relative !important;
        z-index: 25 !important;
        display: grid !important;
        grid-template-columns: repeat(3, 126px) !important;
        grid-template-rows: repeat(2, 186px) !important;
        gap: 18px !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
      }

      .ivh-book-card {
        position: relative !important;
        width: 126px !important;
        height: 186px !important;
        max-width: 126px !important;
        max-height: 186px !important;
        border-radius: 6px !important;
        overflow: hidden !important;
        border-right: 4px solid #F8FAFC !important;
        box-shadow: 0 14px 28px rgba(0,0,0,0.6) !important;
        cursor: pointer !important;
        background: #0F172A !important;
        display: block !important;
        transition: transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.42s ease, box-shadow 0.42s ease !important;
      }

      .ivh-book-card img {
        width: 100% !important;
        height: 100% !important;
        max-width: 126px !important;
        max-height: 186px !important;
        object-fit: cover !important;
        display: block !important;
      }

      @media (max-width: 900px) {
        .ivh-container {
          grid-template-columns: 1fr !important;
          padding: 24px 16px !important;
        }
        .ivh-title { font-size: 34px !important; }
        .ivh-rangoli-anchor { width: 290px !important; height: 290px !important; }
        #ivh-books-grid, .ivh-books-grid {
          grid-template-columns: repeat(3, 94px) !important;
          grid-template-rows: repeat(2, 140px) !important;
          gap: 10px !important;
        }
        .ivh-book-card, .ivh-book-card img {
          width: 94px !important;
          height: 140px !important;
          max-width: 94px !important;
          max-height: 140px !important;
        }
      }
    </style>

    <section class="hero-section ivh-section" id="indigo-video-hero">
      <div class="hero-bg-clip">
        <div class="hero-topleft-watermark">
          <svg viewBox="0 0 380 380" width="380" height="380" fill="none" stroke="#475569" stroke-width="1.2" opacity="0.25" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="190" cy="190" r="180" stroke-dasharray="4,6" />
  <circle cx="190" cy="190" r="150" />
  <circle cx="190" cy="190" r="115" />
  <circle cx="190" cy="190" r="75" stroke-dasharray="3,5" />
  <polygon points="190,40 340,190 190,340 40,190" />
  <polygon points="190,40 84,296 296,296" />
  <polygon points="190,340 84,84 296,84" />
  <line x1="190" y1="10" x2="190" y2="370" />
  <line x1="10" y1="190" x2="370" y2="190" />
  <line x1="60" y1="60" x2="320" y2="320" />
  <line x1="320" y1="60" x2="60" y2="320" />
</svg>
        </div>

        <svg viewBox="0 0 680 260" preserveAspectRatio="none" width="680" height="260" style="position: absolute; right: 0; bottom: 0; width: 680px; height: 260px; pointer-events: none; z-index: 12;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <linearGradient id="marigoldFloorGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E5A93C" stop-opacity="0.95"/>
      <stop offset="50%" stop-color="#D99B26" stop-opacity="0.98"/>
      <stop offset="100%" stop-color="#B37418" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="floorShine" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FDE68A" stop-opacity="0.65"/>
      <stop offset="15%" stop-color="#D99B26" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#78350F" stop-opacity="0.4"/>
    </linearGradient>
  </defs>
  <path d="M 0,260 C 180,260 270,90 680,60 L 680,260 Z" fill="url(#marigoldFloorGrad)" />
  <path d="M 0,260 C 180,260 270,90 680,60" fill="none" stroke="url(#floorShine)" stroke-width="4" opacity="0.9" />
</svg>
        <svg viewBox="0 0 450 160" width="450" height="160" style="position: absolute; right: 0; top: 0; pointer-events: none; z-index: 15;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <radialGradient id="bulbGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFBEB" stop-opacity="1"/>
      <stop offset="35%" stop-color="#FCD34D" stop-opacity="0.85"/>
      <stop offset="70%" stop-color="#D97706" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#B45309" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- 3 Curved Catenary Wires -->
  <path d="M 0,0 Q 80,45 160,15 T 320,30 T 450,10" fill="none" stroke="#D99B26" stroke-width="1.2" opacity="0.65" />
  <path d="M 40,0 Q 140,75 240,30 T 420,50" fill="none" stroke="#B45309" stroke-width="1" opacity="0.5" />
  <path d="M 100,0 Q 220,95 360,40 T 450,70" fill="none" stroke="#D99B26" stroke-width="1" opacity="0.4" />
  <!-- Twinkling Bulbs Wire 1 -->
  <g class="string-bulb"><circle cx="45" cy="18" r="8" fill="url(#bulbGlow)"/><circle cx="45" cy="18" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.6s;"><circle cx="110" cy="35" r="9" fill="url(#bulbGlow)"/><circle cx="110" cy="35" r="3" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.2s;"><circle cx="175" cy="20" r="8" fill="url(#bulbGlow)"/><circle cx="175" cy="20" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.3s;"><circle cx="240" cy="26" r="9" fill="url(#bulbGlow)"/><circle cx="240" cy="26" r="3" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.5s;"><circle cx="310" cy="32" r="8" fill="url(#bulbGlow)"/><circle cx="310" cy="32" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.9s;"><circle cx="380" cy="22" r="8" fill="url(#bulbGlow)"/><circle cx="380" cy="22" r="2.5" fill="#FFF"/></g>
  <!-- Bulbs Wire 2 -->
  <g class="string-bulb" style="animation-delay: 0.4s;"><circle cx="90" cy="38" r="8" fill="url(#bulbGlow)"/><circle cx="90" cy="38" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.1s;"><circle cx="190" cy="56" r="10" fill="url(#bulbGlow)"/><circle cx="190" cy="56" r="3" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.7s;"><circle cx="290" cy="38" r="8" fill="url(#bulbGlow)"/><circle cx="290" cy="38" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.4s;"><circle cx="370" cy="46" r="9" fill="url(#bulbGlow)"/><circle cx="370" cy="46" r="3" fill="#FFF"/></g>
</svg>
        <svg viewBox="0 0 260 100" width="260" height="100" style="position: absolute; right: 40px; bottom: 12px; z-index: 30; pointer-events: none;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <radialGradient id="flameInner" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="1"/>
      <stop offset="40%" stop-color="#FEF08A" stop-opacity="0.95"/>
      <stop offset="75%" stop-color="#F59E0B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#D97706" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="flameHalo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FDE047" stop-opacity="0.6"/>
      <stop offset="60%" stop-color="#EA580C" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#7C2D12" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="clayGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#C2410C"/>
      <stop offset="50%" stop-color="#9A3412"/>
      <stop offset="100%" stop-color="#431407"/>
    </linearGradient>
  </defs>
  
  <!-- Diya 1 (Left, Medium) -->
  <g transform="translate(15, 25)">
    <circle cx="30" cy="20" r="24" fill="url(#flameHalo)" class="diya-flame-halo" />
    <path d="M 30,8 C 22,18 24,28 30,34 C 36,28 38,18 30,8 Z" fill="url(#flameInner)" class="diya-flame" />
    <path d="M 6,32 C 12,48 48,48 54,32 C 50,38 10,38 6,32 Z" fill="url(#clayGrad)" stroke="#7C2D12" stroke-width="1"/>
    <ellipse cx="30" cy="32" rx="24" ry="4" fill="#7C2D12" opacity="0.9"/>
  </g>

  <!-- Diya 2 (Center, Large) -->
  <g transform="translate(95, 10)">
    <circle cx="35" cy="22" r="30" fill="url(#flameHalo)" class="diya-flame-halo" style="animation-delay: 0.35s;" />
    <path d="M 35,6 C 26,18 28,30 35,38 C 42,30 44,18 35,6 Z" fill="url(#flameInner)" class="diya-flame" style="animation-delay: 0.35s;" />
    <path d="M 7,36 C 14,54 56,54 63,36 C 58,43 12,43 7,36 Z" fill="url(#clayGrad)" stroke="#7C2D12" stroke-width="1.2"/>
    <ellipse cx="35" cy="36" rx="28" ry="5" fill="#7C2D12" opacity="0.9"/>
  </g>

  <!-- Diya 3 (Right, Small) -->
  <g transform="translate(185, 32)">
    <circle cx="25" cy="18" r="20" fill="url(#flameHalo)" class="diya-flame-halo" style="animation-delay: 0.7s;" />
    <path d="M 25,9 C 18,17 20,25 25,30 C 30,25 32,17 25,9 Z" fill="url(#flameInner)" class="diya-flame" style="animation-delay: 0.7s;" />
    <path d="M 5,28 C 10,42 40,42 45,28 C 41,33 9,33 5,28 Z" fill="url(#clayGrad)" stroke="#7C2D12" stroke-width="1"/>
    <ellipse cx="25" cy="28" rx="20" ry="3.5" fill="#7C2D12" opacity="0.9"/>
  </g>
</svg>
      </div>

      <div class="site-container hero-main-grid hero-inner-container ivh-container">
        
        <!-- Left Column -->
        <div class="hero-left-col ivh-left">
          <h1 class="ivh-title">Discover Your Next<br>Favorite <em class="ivh-story-italic" style="color: #E5A93C; font-style: italic; font-family: Georgia, serif;">Story</em></h1>
          <p>Explore India's largest online collection of bestsellers, regional gems, academic reads, and more.</p>
          
          <!-- Search Box with Category Selector Dropdown -->
          <div class="hero-search-wrap search-input-wrap search-input-group">
            <select id="heroSearchCategory" class="search-category-select" title="Filter search by category">
              <option value="all">All Books</option>
              <option value="Fiction : Novel">Fiction : Novel</option>
              <option value="Poetry / Shayari">Poetry &amp; Shayari</option>
              <option value="Fiction : Stories">Fiction : Stories</option>
              <option value="Literary Criticism">Literary Criticism</option>
              <option value="History">History &amp; Politics</option>
              <option value="Biography">Biography &amp; Memoirs</option>
              <option value="Law">Law &amp; Constitution</option>
            </select>
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0; margin-left: 10px;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." oninput="handleSearchInput(this.value, 'hero')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'hero-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'hero-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 14px; font-size: 12.5px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; margin-right: 4px;">
              <span>Search</span>
            </button>
            <div id="hero-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>

          <!-- CTA Row -->
          <div class="hero-cta-row">
            <button type="button" class="hero-shop-btn" onclick="scrollToCatalog('all')">
              <span>Shop Now →</span>
            </button>
            <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books!%20I%20want%20to%20place%20a%20Cash%20on%20Delivery%20order." target="_blank" class="hero-wa-cod-btn">
              <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10B981; margin-right: 8px; box-shadow: 0 0 8px #10B981;"></span>
              <span>WhatsApp COD</span>
            </a>
          </div>
        </div>

        <!-- Right Column: 3x2 Grid with Rangoli & Precise Spotlights -->
        <div class="hero-right-col ivh-right hero-stage-col">
          <div class="hero-rangoli-bg hero-rangoli-wrapper hero-wheel-wrap ivh-rangoli-anchor">
            <div class="ivh-rangoli-spin">
              <svg viewBox="0 0 440 440" width="440" height="440" class="hero-wheel-svg" style="width: 440px; height: 440px; max-width: 440px; max-height: 440px; display: block;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <radialGradient id="wheelGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.28"/>
      <stop offset="60%" stop-color="#D97706" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#B45309" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="220" cy="220" r="218" fill="url(#wheelGlow)" />
  <circle cx="220" cy="220" r="212" fill="none" stroke="#FBBF24" stroke-width="1.2" stroke-dasharray="4,6" opacity="0.6" />
  <circle cx="220" cy="220" r="198" fill="none" stroke="#F59E0B" stroke-width="1.8" opacity="0.75" />
  <circle cx="220" cy="220" r="182" fill="none" stroke="#FBBF24" stroke-width="1" stroke-dasharray="2,4" opacity="0.5" />
  
  <!-- 24 Radiating Spoke Lines -->
  <g stroke="#FBBF24" stroke-width="0.9" opacity="0.45">
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(0 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(15 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(30 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(45 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(60 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(75 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(90 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(105 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(120 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(135 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(150 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(165 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(180 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(195 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(210 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(225 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(240 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(255 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(270 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(285 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(300 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(315 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(330 220 220)" />
    <line x1="220" y1="20" x2="220" y2="420" transform="rotate(345 220 220)" />
  </g>

  <!-- Diamond Markers at Radial Intersections -->
  <g opacity="0.75">
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(0 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(15 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(30 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(45 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(60 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(75 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(90 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(105 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(120 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(135 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(150 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(165 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(180 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(195 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(210 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(225 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(240 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(255 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(270 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(285 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(300 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(315 220 220)" />
    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate(330 220 220)" />
    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate(345 220 220)" />
  </g>

  <!-- Concentric Inner Astrological Rings -->
  <circle cx="220" cy="220" r="145" fill="none" stroke="#FDE68A" stroke-width="1.4" opacity="0.75" />
  <circle cx="220" cy="220" r="115" fill="none" stroke="#F59E0B" stroke-width="1.6" stroke-dasharray="3,5" opacity="0.8" />
  <circle cx="220" cy="220" r="82" fill="none" stroke="#FBBF24" stroke-width="1.5" opacity="0.85" />
  <circle cx="220" cy="220" r="48" fill="rgba(245, 158, 11, 0.22)" stroke="#FDE68A" stroke-width="1.5" />
  <circle cx="220" cy="220" r="24" fill="#F59E0B" opacity="0.7" />
  <circle cx="220" cy="220" r="10" fill="#FFFBEB" />
</svg>
            </div>
          </div>

          <div class="hero-books-grid ivh-books-grid hero-books-grid-video" id="ivh-books-grid">
            
            <!-- Book 1: Godan (₹299.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="0" onmouseenter="handleHeroBookHover(0)" onmouseleave="handleHeroGridMouseLeave()" onclick="handleBookAction('podium-godan', '/products/godan-premchand', event)" data-book-id="podium-godan" data-title="Godan" data-author="Premchand" data-price="299.00" data-binding="Paperback" data-category="Hindi Classics" style="cursor: pointer;" title="View Godan by Premchand">
              <div class="hero-book-thumb">
                <img src="assets/hero-godan.jpg" alt="Godan (गोदान)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Godan</div>
                <div class="hero-book-author">Premchand</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 2: Raag Darbari (₹499.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="1" onmouseenter="handleHeroBookHover(1)" onmouseleave="handleHeroGridMouseLeave()" onclick="handleBookAction('podium-raag-darbari', '/products/raag-darbari-shrilal-shukla', event)" data-book-id="podium-raag-darbari" data-title="Raag Darbari" data-author="Shrilal Shukla" data-price="499.00" data-binding="Deluxe Edition" data-category="Contemporary Hindi Fiction" style="cursor: pointer;" title="View Raag Darbari by Shrilal Shukla">
              <div class="hero-book-thumb">
                <img src="assets/hero-raag-darbari.jpg" alt="Raag Darbari (राग दरबारी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Raag Darbari</div>
                <div class="hero-book-author">Shrilal Shukla</div>
                <div class="hero-book-price">₹499.00</div>
              </div>
            </div>

            <!-- Book 3: Chitralekha (₹299.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="2" onmouseenter="handleHeroBookHover(2)" onmouseleave="handleHeroGridMouseLeave()" onclick="handleBookAction('podium-chitralekha', '/products/chitralekha-bhagwaticharan-verma', event)" data-book-id="podium-chitralekha" data-title="Chitralekha" data-author="Bhagwaticharan Verma" data-price="299.00" data-binding="Paperback" data-category="Hindi Classics" style="cursor: pointer;" title="View Chitralekha by Bhagwaticharan Verma">
              <div class="hero-book-thumb">
                <img src="assets/hero-chitralekha.jpg" alt="Chitralekha (चित्रलेखा)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Chitralekha</div>
                <div class="hero-book-author">Bhagwaticharan Verma</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 4: Rashmirathi (₹299.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="3" onmouseenter="handleHeroBookHover(3)" onmouseleave="handleHeroGridMouseLeave()" onclick="handleBookAction('podium-rashmirathi', '/products/rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar', event)" data-book-id="podium-rashmirathi" data-title="Rashmirathi : Dinkar Granthmala" data-author="Ramdhari Singh 'Dinkar'" data-price="299.00" data-binding="Paperback" data-category="Shayari & Poetry" style="cursor: pointer;" title="View Rashmirathi by Ramdhari Singh Dinkar">
              <div class="hero-book-thumb">
                <img src="assets/hero-rashmirathi.jpg" alt="Rashmirathi (रश्मिरथी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Rashmirathi</div>
                <div class="hero-book-author">Ramdhari Singh Dinkar</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 5: Kuchh Ishq Kiya Kuchh Kaam Kiya (₹250.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="4" onmouseenter="handleHeroBookHover(4)" onmouseleave="handleHeroGridMouseLeave()" onclick="handleBookAction('podium-kuchh-ishq', '/products/kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra', event)" data-book-id="podium-kuchh-ishq" data-title="Kuchh Ishq Kiya Kuchh Kaam Kiya" data-author="Piyush Mishra" data-price="250.00" data-binding="Paperback" data-category="Shayari & Poetry" style="cursor: pointer;" title="View Kuchh Ishq Kiya by Piyush Mishra">
              <div class="hero-book-thumb">
                <img src="assets/hero-kuchh-ishq.jpg" alt="Kuchh Ishq Kiya Kuchh Kaam Kiya" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Kuchh Ishq Kiya</div>
                <div class="hero-book-author">Piyush Mishra</div>
                <div class="hero-book-price">₹250.00</div>
              </div>
            </div>

            <!-- Book 6: Gypsy (₹499.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="5" onmouseenter="handleHeroBookHover(5)" onmouseleave="handleHeroGridMouseLeave()" onclick="handleBookAction('hindi-gypsy', '/products/gypsy-ila-chandra-joshi', event)" data-book-id="hindi-gypsy" data-title="Gypsy" data-author="Ila Chandra Joshi" data-price="499.00" data-binding="Deluxe Edition" data-category="Contemporary Hindi Fiction" style="cursor: pointer;" title="View Gypsy by Ila Chandra Joshi">
              <div class="hero-book-thumb">
                <img src="assets/hero-gypsy.jpg" alt="Gypsy (जिप्सी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Gypsy</div>
                <div class="hero-book-author">Ila Chandra Joshi</div>
                <div class="hero-book-price">₹499.00</div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>


    <!-- =========================================================================
         3. KINETIC MARQUEE RIBBON & STATS COUNTER BAR
         ========================================================================= -->
    <div class="marquee-ribbon">
      <div class="marquee-track">
        <span class="marquee-item">SAMEDAY DISPATCH FROM PRAYAGRAJ <span class="marquee-dot"></span></span>
        <span class="marquee-item">100% AUTHENTIC PUBLISHER EDITIONS <span class="marquee-dot"></span></span>
        <span class="marquee-item">CASH ON DELIVERY PAN-INDIA <span class="marquee-dot"></span></span>
        <span class="marquee-item">SPECIAL REKHTA URDU POETRY ARCHIVE <span class="marquee-dot"></span></span>
        <span class="marquee-item">UPSC &amp; JUDICIARY SCHOLAR EDITIONS <span class="marquee-dot"></span></span>
        <span class="marquee-item">INSTANT WHATSAPP CONCIERGE +91 8933063306 <span class="marquee-dot"></span></span>
        <span class="marquee-item">SAMEDAY DISPATCH FROM PRAYAGRAJ <span class="marquee-dot"></span></span>
        <span class="marquee-item">100% AUTHENTIC PUBLISHER EDITIONS <span class="marquee-dot"></span></span>
        <span class="marquee-item">CASH ON DELIVERY PAN-INDIA <span class="marquee-dot"></span></span>
        <span class="marquee-item">SPECIAL REKHTA URDU POETRY ARCHIVE <span class="marquee-dot"></span></span>
        <span class="marquee-item">UPSC &amp; JUDICIARY SCHOLAR EDITIONS <span class="marquee-dot"></span></span>
        <span class="marquee-item">INSTANT WHATSAPP CONCIERGE +91 8933063306 <span class="marquee-dot"></span></span>
      </div>
    </div>

    <div class="stats-bar">
      <div class="site-container stats-grid">
        <div class="stat-card">
          <div class="stat-number">5,500+</div>
          <div class="stat-label">Books Available</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">24+</div>
          <div class="stat-label">Featured Curations</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">24-Hr</div>
          <div class="stat-label">Express Dispatch from Prayagraj</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">100%</div>
          <div class="stat-label">Cash on Delivery &amp; Authenticity</div>
        </div>
      </div>
    </div>


    <!-- =========================================================================
         4. SECTION 1: THE 3D CURATOR'S PODIUM (#bestsellers-podium)
         ========================================================================= -->
    <section id="bestsellers-podium" style="background: #FAF8F5;">
      <div class="site-container">
        
        <div class="editorial-header">
          <div>
            <div class="sec-overline">CURATED SELECTIONS</div>
            <h2>The Podium: India's Top 5 Trending Reads</h2>
            <p>Handpicked literature capturing minds across universities, literary circles, and book lovers nationwide.</p>
          </div>
        </div>

        <div class="podium-stage-grid">
          
          <!-- Left: 5-Book Turntable with Center 3D Book & Fanned Flankers -->
          <div class="podium-left-stage">
            <div class="podium-turntable-track">
              
              <!-- Flanking Far-Left -->
              <div class="flank-book flank-left-2" onclick="selectPodiumByFlank(-2)" title="Click to view book">
                <img id="flankImgL2" src="assets/hero-rashmirathi.jpg" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>

              <!-- Flanking Near-Left -->
              <div class="flank-book flank-left-1" onclick="selectPodiumByFlank(-1)" title="Click to view book">
                <img id="flankImgL1" src="assets/hero-kuchh-ishq.jpg" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>

              <!-- Center Active 3D Book Hinge Structure -->
              <div id="podium-3d-book" class="podium-3d-book podium-center-book" onclick="togglePodiumCover(event)" title="Hover to Open Cover">
                
                <!-- Stationary Inside Cream Page -->
                <div class="podium-inside-page podium-page-inside">
                  <div class="podium-page-eyebrow">अध्याय १ • FIRST PAGE PREVIEW</div>
                  <div id="podium-page-title" class="podium-page-title">Godan</div>
                  <p id="podium-page-excerpt" class="podium-page-excerpt">होरी जब घर से निकला, तो उसके दिल में एक ही तमन्ना थी कि किसी तरह एक गाय मिल जाए। उसका जीवन गाय की लालसा में ही बीत गया था।</p>
                  <div class="podium-page-footer">
                    <span style="font-weight: 700; color: #B45309;">— पृष्ठ १ —</span>
                    <span>Hover to Preview Cover</span>
                  </div>
                </div>

                <!-- Hinged Cover (Rotates to -135deg on Hover) -->
                <div class="podium-hinged-cover podium-cover-leaf">
                  <!-- Front Face -->
                  <div class="cover-front">
                    <img id="podium-cover-img" src="assets/hero-godan.jpg" alt="Godan" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                  <!-- Back Face -->
                  <div class="cover-back">
                    <div class="cover-back-thumb">
                      <img id="podium-inside-thumb" src="assets/hero-godan.jpg" alt="Inside Cover" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                    </div>
                    <div id="podium-inside-title" class="cover-back-title">Godan</div>
                    <div id="podium-inside-author" class="cover-back-author">Premchand</div>
                    <div class="cover-back-tag">Indigo Heritage Edition</div>
                  </div>
                </div>

              </div>

              <!-- Flanking Near-Right -->
              <div class="flank-book flank-right-1" onclick="selectPodiumByFlank(1)" title="Click to view book">
                <img id="flankImgR1" src="assets/hero-raag-darbari.jpg" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>

              <!-- Flanking Far-Right -->
              <div class="flank-book flank-right-2" onclick="selectPodiumByFlank(2)" title="Click to view book">
                <img id="flankImgR2" src="assets/hero-chitralekha.jpg" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>

            </div>

            <!-- Controls: Arrow Keys & Indicator Dots -->
            <div class="podium-nav-row">
              <button type="button" class="podium-arrow-btn" onclick="prevPodiumBook()" aria-label="Previous Book">
                <i data-lucide="chevron-left" style="width: 18px; height: 18px;"></i>
              </button>
              <div class="podium-dots-wrap">
                <span class="podium-dot active" onclick="selectPodiumBook(0)"></span>
                <span class="podium-dot" onclick="selectPodiumBook(1)"></span>
                <span class="podium-dot" onclick="selectPodiumBook(2)"></span>
                <span class="podium-dot" onclick="selectPodiumBook(3)"></span>
                <span class="podium-dot" onclick="selectPodiumBook(4)"></span>
              </div>
              <button type="button" class="podium-arrow-btn" onclick="nextPodiumBook()" aria-label="Next Book">
                <i data-lucide="chevron-right" style="width: 18px; height: 18px;"></i>
              </button>
            </div>

          </div>

          <!-- Right: Synced Book Details Panel -->
          <div class="podium-right-card">
            <div id="podiumSpotBadge" class="podium-cat-badge">NATIONAL BESTSELLER</div>
            <div id="podiumSpotStock" class="podium-stock-str">
              <i data-lucide="check-circle" style="width: 14px; height: 14px; color: #059669;"></i>
              <span>In Stock • Ships in 24 Hrs</span>
            </div>
            <h3 id="podiumSpotHeading" class="podium-book-heading" style="cursor: pointer;" onclick="handleBookAction(PODIUM_BOOKS[currentPodiumIndex]['id'], '/products/' + PODIUM_BOOKS[currentPodiumIndex]['handle'], event)">Godan</h3>
            <div id="podiumSpotAuthor" class="podium-author-row">Premchand</div>
            
            <blockquote id="podiumSpotQuote" class="podium-quote-box">
              "The greatest epic of rural India, depicting peasant resilience and societal injustice."
            </blockquote>

            <div class="podium-specs-grid">
              <div><strong>Format:</strong> <span id="podiumSpotPages">312p</span></div>
              <div><strong>Publisher:</strong> <span id="podiumSpotPublisher">Lokbharti Prakashan</span></div>
              <div><strong>Dispatch:</strong> <span style="color: #059669; font-weight: 700;">Same-Day Prayagraj</span></div>
              <div><strong>Payment:</strong> <span>Cash on Delivery Available</span></div>
            </div>

            <div class="podium-price-row">
              <span id="podiumSpotPrice" class="podium-curr-price">{PODIUM_BOOKS[0]['price']}</span>
            </div>

            <div class="podium-actions-row">
              <button type="button" class="btn-overview" onclick="handleBookAction(PODIUM_BOOKS[currentPodiumIndex]['id'], '/products/' + PODIUM_BOOKS[currentPodiumIndex]['handle'], event)">
                <i data-lucide="book-open" style="width: 15px; height: 15px;"></i> View Details
              </button>
              <button type="button" class="btn-add-cart" onclick="addCurrentPodiumToCart()">
                <i data-lucide="shopping-bag" style="width: 15px; height: 15px;"></i> Add to Cart
              </button>
              <button type="button" class="btn-wa-order" onclick="orderCurrentPodiumWhatsApp()">
                <i data-lucide="message-circle" style="width: 15px; height: 15px;"></i> WhatsApp COD
              </button>
            </div>

          </div>

        </div>

      </div>
    </section>


    <!-- =========================================================================
         5. SECTION 2: MEHFIL-E-REKHTA DARK POETRY LOUNGE (#mehfil-rekhta)
         ========================================================================= -->
    <section id="mehfil-rekhta" class="rekhta-section">
      <div class="rekhta-watermark">शायरी • दास्तान • अदब</div>

      <div class="site-container">
        
        <div class="editorial-header" style="border-color: rgba(255, 255, 255, 0.1);">
          <div>
            <div class="sec-overline" style="color: #D99B26;">URDU POETRY &amp; LITERARY HERITAGE</div>
            <h2 style="color: #FFFFFF;">Mehfil-e-Rekhta: Timeless Urdu Shayari &amp; Progressive Classics</h2>
            <p style="color: #94A3B8;">Immerse yourself in legendary couplets, nazms, and rare literary editions from the Rekhta vault.</p>
          </div>
        </div>

        <!-- Authentic Poet Filter Pills -->
        <div class="poet-pills-row">
          <button type="button" class="poet-pill active" data-poet="all" onclick="switchPoet('all')">All Poets (सब शो'रा / कवि)</button>
          <button type="button" class="poet-pill" data-poet="mishra" onclick="switchPoet('mishra')">Piyush Mishra (पीयूष मिश्रा)</button>
          <button type="button" class="poet-pill" data-poet="akhtar" onclick="switchPoet('akhtar')">Javed Akhtar (जावेद अख़्तर)</button>
          <button type="button" class="poet-pill" data-poet="dinkar" onclick="switchPoet('dinkar')">Ramdhari Singh 'Dinkar' (दिनकर)</button>
          <button type="button" class="poet-pill" data-poet="manto" onclick="switchPoet('manto')">Saadat Hasan Manto (मंटो)</button>
          <button type="button" class="poet-pill" data-poet="mizaj" onclick="switchPoet('mizaj')">Ashok Mizaj (अशोक मिज़ाज)</button>
        </div>

        <!-- Live Couplet Card -->
        <div class="couplet-card">
          <div id="rekhtaUrdu" class="couplet-urdu">ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے
بہت نکلے مرے ارمان لیکن پھر بھی کم نکلے</div>
          <div id="rekhtaHindi" class="couplet-hindi">हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले
बहुत निकले मिरे अरमान लेकिन फिर भी कम निकले</div>
          <div id="rekhtaEng" class="couplet-eng">Thousands of desires, each worth dying for;
Many of my longings were fulfilled, yet so few they were.</div>
          <div id="rekhtaAttr" class="couplet-attr">— MIRZA GHALIB (मिर्ज़ा ग़ालिब)</div>

          <div class="couplet-controls">
            <button type="button" class="couplet-nav-btn" onclick="prevSher()">
              <i data-lucide="chevron-left" style="width: 14px; height: 14px;"></i> Prev Sher
            </button>
            <button type="button" class="ghazal-drawer-toggle" onclick="toggleGhazalDrawer()">
              Read Full Ghazal / Nazm
            </button>
            <button type="button" class="couplet-nav-btn" onclick="nextSher()">
              Next Sher <i data-lucide="chevron-right" style="width: 14px; height: 14px;"></i>
            </button>
          </div>

          <div id="rekhtaFullGhazal" class="ghazal-full-drawer">
            हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले
बहुत निकले मिरे अरमान लेकिन फिर भी कम निकले

डरे क्यों मेरा क़ातिल क्या रहेगा उसकी गर्दन पर
वो ख़ूँ जो चश्म-ए-तर से उम्र भर यूँ दम-ब-दम निकले

निकलना ख़ुल्द से आदम का सुनते आए हैं लेकिन
बहुत बे-आबरू होकर तिरे कूचे से हम निकले
          </div>
        </div>

        <!-- 5 Authentic Rekhta Book Cards Below -->
        <div class="rekhta-books-grid">
          
          <div class="rekhta-book-card" data-poet="all" data-book-id="rekhta-tarkash" data-title="Tarkash" data-author="Javed Akhtar" data-price="₹299.00">
            <div class="rekhta-cover-wrap" onclick="handleBookAction('rekhta-tarkash', '/products/rekhta-tarkash', event)" style="cursor: pointer;">
              <img src="assets/book-tarkash.jpg" alt="Tarkash" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/rekhta-tarkash" onclick="handleBookAction('rekhta-tarkash', '/products/rekhta-tarkash', event)" style="color: inherit; text-decoration: none;">Tarkash</a>
            </h3>
            <div class="rekhta-card-author">Javed Akhtar</div>
            <div class="rekhta-card-desc">Timeless nazms and ghazals of love, parting, and existential contemplation.</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">₹299.00</span>
            </div>
            <div class="rekhta-card-actions">
              <button type="button" class="btn-overview" onclick="handleBookAction('rekhta-tarkash', '/products/rekhta-tarkash', event)">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
              </button>
              <button type="button" class="btn-add-cart" style="background: #D99B26; color: #0A1128;" onclick="addToCart('rekhta-tarkash')">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          
          <div class="rekhta-book-card" data-poet="all" data-book-id="rekhta-ishq-mishra" data-title="Kuchh Ishq Kiya Kuchh Kaam Kiya" data-author="Piyush Mishra" data-price="₹250.00">
            <div class="rekhta-cover-wrap" onclick="handleBookAction('rekhta-ishq-mishra', '/products/rekhta-ishq-mishra', event)" style="cursor: pointer;">
              <img src="assets/hero-kuchh-ishq.jpg" alt="Kuchh Ishq Kiya Kuchh Kaam Kiya" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/rekhta-ishq-mishra" onclick="handleBookAction('rekhta-ishq-mishra', '/products/rekhta-ishq-mishra', event)" style="color: inherit; text-decoration: none;">Kuchh Ishq Kiya Kuchh Kaam Kiya</a>
            </h3>
            <div class="rekhta-card-author">Piyush Mishra</div>
            <div class="rekhta-card-desc">Beloved theatrical verses, nostalgic laments, and bohemian stage lyrics.</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">₹250.00</span>
            </div>
            <div class="rekhta-card-actions">
              <button type="button" class="btn-overview" onclick="handleBookAction('rekhta-ishq-mishra', '/products/rekhta-ishq-mishra', event)">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
              </button>
              <button type="button" class="btn-add-cart" style="background: #D99B26; color: #0A1128;" onclick="addToCart('rekhta-ishq-mishra')">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          
          <div class="rekhta-book-card" data-poet="all" data-book-id="rekhta-guzare-lamhe" data-title="Guzare Lamhe" data-author="Ashok Yadav" data-price="₹395.00">
            <div class="rekhta-cover-wrap" onclick="handleBookAction('rekhta-guzare-lamhe', '/products/rekhta-guzare-lamhe', event)" style="cursor: pointer;">
              <img src="assets/book-guzare-lamhe.jpg" alt="Guzare Lamhe" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/rekhta-guzare-lamhe" onclick="handleBookAction('rekhta-guzare-lamhe', '/products/rekhta-guzare-lamhe', event)" style="color: inherit; text-decoration: none;">Guzare Lamhe</a>
            </h3>
            <div class="rekhta-card-author">Ashok Yadav</div>
            <div class="rekhta-card-desc">Soulful ghazals and nazms reviving classical Awadhi and Hindustani poetic traditions.</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">₹395.00</span>
            </div>
            <div class="rekhta-card-actions">
              <button type="button" class="btn-overview" onclick="handleBookAction('rekhta-guzare-lamhe', '/products/rekhta-guzare-lamhe', event)">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
              </button>
              <button type="button" class="btn-add-cart" style="background: #D99B26; color: #0A1128;" onclick="addToCart('rekhta-guzare-lamhe')">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          
          <div class="rekhta-book-card" data-poet="all" data-book-id="rekhta-rashmirathi" data-title="Rashmirathi : Dinkar Granthmala" data-author="Ramdhari Singh 'Dinkar'" data-price="₹299.00">
            <div class="rekhta-cover-wrap" onclick="handleBookAction('rekhta-rashmirathi', '/products/rekhta-rashmirathi', event)" style="cursor: pointer;">
              <img src="assets/hero-rashmirathi.jpg" alt="Rashmirathi : Dinkar Granthmala" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/rekhta-rashmirathi" onclick="handleBookAction('rekhta-rashmirathi', '/products/rekhta-rashmirathi', event)" style="color: inherit; text-decoration: none;">Rashmirathi : Dinkar Granthmala</a>
            </h3>
            <div class="rekhta-card-author">Ramdhari Singh 'Dinkar'</div>
            <div class="rekhta-card-desc">Immortal verses of valour, dignity, and righteous courage in Karna's epic voice.</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">₹299.00</span>
            </div>
            <div class="rekhta-card-actions">
              <button type="button" class="btn-overview" onclick="handleBookAction('rekhta-rashmirathi', '/products/rekhta-rashmirathi', event)">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
              </button>
              <button type="button" class="btn-add-cart" style="background: #D99B26; color: #0A1128;" onclick="addToCart('rekhta-rashmirathi')">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          
          <div class="rekhta-book-card" data-poet="all" data-book-id="rekhta-dhuaan" data-title="Dhuaan (धुआँ) & Representative Stories" data-author="Saadat Hasan Manto" data-price="₹350.00">
            <div class="rekhta-cover-wrap" onclick="handleBookAction('rekhta-dhuaan', '/products/rekhta-dhuaan', event)" style="cursor: pointer;">
              <img src="assets/hero-godan.jpg" alt="Dhuaan (धुआँ) & Representative Stories" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/rekhta-dhuaan" onclick="handleBookAction('rekhta-dhuaan', '/products/rekhta-dhuaan', event)" style="color: inherit; text-decoration: none;">Dhuaan (धुआँ) & Representative Stories</a>
            </h3>
            <div class="rekhta-card-author">Saadat Hasan Manto</div>
            <div class="rekhta-card-desc">Masterful short stories portraying the raw, unfiltered truth of human nature.</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">₹350.00</span>
            </div>
            <div class="rekhta-card-actions">
              <button type="button" class="btn-overview" onclick="handleBookAction('rekhta-dhuaan', '/products/rekhta-dhuaan', event)">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
              </button>
              <button type="button" class="btn-add-cart" style="background: #D99B26; color: #0A1128;" onclick="addToCart('rekhta-dhuaan')">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          
        </div>

      </div>
    </section>


    
    <section class="category-bento-section" id="category-bento-showcase" style="background: #FFFFFF; padding: 60px 0;">
      <div class="category-bento-showcase">
        
        <div class="editorial-header" style="margin-bottom: 24px;">
          <div>
            <div class="sec-overline">CURATED GENRES</div>
            <h2>Explore Our Indian Literary Archive</h2>
            <p>From timeless Premchand classics to Supreme Court law treatises &mdash; hand-bound publisher editions.</p>
          </div>
        </div>

        <div class="category-pills-bar" style="margin-bottom: 32px;">
          <button type="button" class="cat-bento-pill active" data-cat="contemporary" onclick="switchCategoryBento('contemporary')">
            Contemporary Hindi Fiction
          </button>
          <button type="button" class="cat-bento-pill" data-cat="poetry" onclick="switchCategoryBento('poetry')">
            Poetry, Ghazals &amp; Shayari
          </button>
          <button type="button" class="cat-bento-pill" data-cat="classics" onclick="switchCategoryBento('classics')">
            Classic Hindi Novels
          </button>
          <button type="button" class="cat-bento-pill" data-cat="history" onclick="switchCategoryBento('history')">
            History, Criticism &amp; Politics
          </button>
          <button type="button" class="cat-bento-pill" data-cat="law" onclick="switchCategoryBento('law')">
            Law &amp; Constitutional Studies
          </button>
        </div>

        <div class="category-bento-grid">
          
      <div class="bento-left-spotlight" id="bentoLeftSpotlight" data-book-id="bento-contemp-raag" data-title="Raag Darbari" data-author="Shrilal Shukla" data-price="₹499.00">
        <div>
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 8px;">
            LANDMARK SATIRICAL NOVEL
          </div>
          <div class="bento-left-cover-wrap">
            <div class="indigo-3d-book-stage" onclick="openSoloBookPage('bento-contemp-raag', event)">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">INDIGO ARCHIVE</div>
                <div style="font-family: 'Merriweather', serif; font-size: 13px; line-height: 1.35; color: #1E293B; font-weight: 700;">Raag Darbari</div>
                <div style="font-size: 11px; color: #64748B;">By Shrilal Shukla</div>
                <div style="font-size: 9.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 4px;">Paperback • 423p Pages • Rajkamal Prakashan</div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img src="assets/hero-raag-darbari.jpg" alt="Raag Darbari" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                </div>
                <div class="indigo-3d-cover-back">
                  <div style="font-size: 10px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">100% GENUINE</div>
                  <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">Authorized Copy</div>
                  <div style="font-size: 11px; color: #CBD5E1;">₹499.00</div>
                  <div style="font-size: 9.5px; color: #FCD34D; margin-top: 6px; border: 1px solid rgba(251,191,36,0.4); padding: 2px 6px; border-radius: 4px;">Click for Details &rarr;</div>
                </div>
              </div>
            </div>
          </div>
          <div style="font-size: 11px; font-weight: 700; color: #0066B3; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">
            SAHITYA AKADEMI AWARD
          </div>
          <h3 id="bentoLeftTitle" style="font-family: 'Merriweather', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; line-height: 1.3; margin: 0 0 6px;">
            <a href="/products/bento-contemp-raag" onclick="handleBookAction('bento-contemp-raag', '/products/bento-contemp-raag', event)" style="color: inherit; text-decoration: none;">Raag Darbari</a>
          </h3>
          <div id="bentoLeftAuthor" style="font-size: 14px; font-weight: 600; color: #64748B; margin-bottom: 12px;">Shrilal Shukla</div>
          <p id="bentoLeftBlurb" style="font-size: 13px; color: #334155; line-height: 1.6; margin: 0 0 14px;">
            "यह कहानी शिवपालगंज की है जहाँ सड़क के किनारे का कॉलेज हर साल नए क्रांतिकारी और बेरोजगार पैदा करता है।"
          </p>
          <div id="bentoLeftSpecs" style="font-size: 12px; color: #64748B; margin-bottom: 16px;">
            Paperback • 423p Pages • Rajkamal Prakashan
          </div>
        </div>
        <div>
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 16px;">
            <span id="bentoLeftPrice" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹499.00</span>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <button type="button" class="btn-overview" onclick="openOverviewModal('bento-contemp-raag')">
              <i data-lucide="book-open" style="width: 15px; height: 15px;"></i> Overview
            </button>
            <button type="button" class="btn-add-cart" onclick="addToCart('bento-contemp-raag')">
              <i data-lucide="shopping-bag" style="width: 15px; height: 15px;"></i> + Add to Cart
            </button>
          </div>
        </div>
      </div>
    
          <div class="bento-right-2x2" id="bentoRightGrid">
            
          <div class="bento-horiz-card" data-book-id="bento-contemp-gypsy" data-title="Gypsy" data-author="Ila chandra Joshi" data-price="₹499.00">
            <div>
              <div class="bento-horiz-top">
                <div class="bento-horiz-cover">
                  <div class="indigo-3d-book-stage" onclick="openSoloBookPage('bento-contemp-gypsy', event)">
                    <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                      <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                      <div style="font-family: 'Merriweather', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">Gypsy</div>
                      <div style="font-size: 7.5px; color: #64748B;">Ila chandra Joshi</div>
                    </div>
                    <div class="indigo-3d-cover-leaf">
                      <div class="indigo-3d-cover-front">
                        <img src="assets/hero-gypsy.jpg" alt="Gypsy" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                      </div>
                      <div class="indigo-3d-cover-back" style="padding: 6px !important;">
                        <div style="font-size: 8px; font-weight: 700; color: #F59E0B;">GENUINE</div>
                        <div style="font-size: 8.5px; color: #FFFFFF;">₹499.00</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div style="min-width: 0;">
                  <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    PSYCHOLOGICAL FICTION
                  </div>
                  <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                    <a href="/products/bento-contemp-gypsy" onclick="handleBookAction('bento-contemp-gypsy', '/products/bento-contemp-gypsy', event)" style="color: inherit; text-decoration: none;">Gypsy</a>
                  </h4>
                  <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Ila chandra Joshi</div>
                  <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">Paperback • 375p Pages • Lokbharti Prakashan</div>
                  <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹499.00</div>
                </div>
              </div>
              <p style="font-size: 12px; color: #64748B; line-height: 1.5; margin: 0 0 8px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                Intense psychological novel exploring non-conformity, passion, and vagabond human spirit.
              </p>
            </div>
            <div class="bento-card-actions">
              <button type="button" class="btn-overview" style="padding: 7px 10px; font-size: 12px;" onclick="openOverviewModal('bento-contemp-gypsy')">
                <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('bento-contemp-gypsy')">
                <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> + Add
              </button>
            </div>
          </div>
        

          <div class="bento-horiz-card" data-book-id="bento-contemp-aadha" data-title="Aadha Gaon" data-author="Rahi Masoom Raza" data-price="₹450.00">
            <div>
              <div class="bento-horiz-top">
                <div class="bento-horiz-cover">
                  <div class="indigo-3d-book-stage" onclick="openSoloBookPage('bento-contemp-aadha', event)">
                    <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                      <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                      <div style="font-family: 'Merriweather', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">Aadha Gaon</div>
                      <div style="font-size: 7.5px; color: #64748B;">Rahi Masoom Raza</div>
                    </div>
                    <div class="indigo-3d-cover-leaf">
                      <div class="indigo-3d-cover-front">
                        <img src="assets/book-aadha-gaon.jpg" alt="Aadha Gaon" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                      </div>
                      <div class="indigo-3d-cover-back" style="padding: 6px !important;">
                        <div style="font-size: 8px; font-weight: 700; color: #F59E0B;">GENUINE</div>
                        <div style="font-size: 8.5px; color: #FFFFFF;">₹450.00</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div style="min-width: 0;">
                  <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    PARTITION CHRONICLE
                  </div>
                  <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                    <a href="/products/bento-contemp-aadha" onclick="handleBookAction('bento-contemp-aadha', '/products/bento-contemp-aadha', event)" style="color: inherit; text-decoration: none;">Aadha Gaon</a>
                  </h4>
                  <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Rahi Masoom Raza</div>
                  <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">Paperback • 344p Pages • Rajkamal Prakashan</div>
                  <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹450.00</div>
                </div>
              </div>
              <p style="font-size: 12px; color: #64748B; line-height: 1.5; margin: 0 0 8px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                Heartbreaking saga of Ganga-Jamuni tehzeeb and partition trauma in rural Ghazipur.
              </p>
            </div>
            <div class="bento-card-actions">
              <button type="button" class="btn-overview" style="padding: 7px 10px; font-size: 12px;" onclick="openOverviewModal('bento-contemp-aadha')">
                <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('bento-contemp-aadha')">
                <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> + Add
              </button>
            </div>
          </div>
        

          <div class="bento-horiz-card" data-book-id="bento-contemp-mahabhoj" data-title="Mahabhoj" data-author="Mannu Bhandari" data-price="₹250.00">
            <div>
              <div class="bento-horiz-top">
                <div class="bento-horiz-cover">
                  <div class="indigo-3d-book-stage" onclick="openSoloBookPage('bento-contemp-mahabhoj', event)">
                    <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                      <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                      <div style="font-family: 'Merriweather', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">Mahabhoj</div>
                      <div style="font-size: 7.5px; color: #64748B;">Mannu Bhandari</div>
                    </div>
                    <div class="indigo-3d-cover-leaf">
                      <div class="indigo-3d-cover-front">
                        <img src="assets/book-mahabhoj.jpg" alt="Mahabhoj" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                      </div>
                      <div class="indigo-3d-cover-back" style="padding: 6px !important;">
                        <div style="font-size: 8px; font-weight: 700; color: #F59E0B;">GENUINE</div>
                        <div style="font-size: 8.5px; color: #FFFFFF;">₹250.00</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div style="min-width: 0;">
                  <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    POLITICAL THRILLER
                  </div>
                  <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                    <a href="/products/bento-contemp-mahabhoj" onclick="handleBookAction('bento-contemp-mahabhoj', '/products/bento-contemp-mahabhoj', event)" style="color: inherit; text-decoration: none;">Mahabhoj</a>
                  </h4>
                  <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Mannu Bhandari</div>
                  <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">Paperback • 240p Pages • Radhakrishna Prakashan</div>
                  <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹250.00</div>
                </div>
              </div>
              <p style="font-size: 12px; color: #64748B; line-height: 1.5; margin: 0 0 8px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                Fiery political masterpiece exposing electoral hypocrisy, corruption, and Dalit struggle.
              </p>
            </div>
            <div class="bento-card-actions">
              <button type="button" class="btn-overview" style="padding: 7px 10px; font-size: 12px;" onclick="openOverviewModal('bento-contemp-mahabhoj')">
                <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('bento-contemp-mahabhoj')">
                <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> + Add
              </button>
            </div>
          </div>
        

          <div class="bento-horiz-card" data-book-id="bento-contemp-topi" data-title="Topi Shukla" data-author="Rahi Masoom Raza" data-price="₹199.00">
            <div>
              <div class="bento-horiz-top">
                <div class="bento-horiz-cover">
                  <div class="indigo-3d-book-stage" onclick="openSoloBookPage('bento-contemp-topi', event)">
                    <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                      <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                      <div style="font-family: 'Merriweather', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">Topi Shukla</div>
                      <div style="font-size: 7.5px; color: #64748B;">Rahi Masoom Raza</div>
                    </div>
                    <div class="indigo-3d-cover-leaf">
                      <div class="indigo-3d-cover-front">
                        <img src="https://images.rajkamalprakashan.com/products/--1776278800425.jpg" alt="Topi Shukla" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                      </div>
                      <div class="indigo-3d-cover-back" style="padding: 6px !important;">
                        <div style="font-size: 8px; font-weight: 700; color: #F59E0B;">GENUINE</div>
                        <div style="font-size: 8.5px; color: #FFFFFF;">₹199.00</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div style="min-width: 0;">
                  <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    LITERARY GEM
                  </div>
                  <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                    <a href="/products/bento-contemp-topi" onclick="handleBookAction('bento-contemp-topi', '/products/bento-contemp-topi', event)" style="color: inherit; text-decoration: none;">Topi Shukla</a>
                  </h4>
                  <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Rahi Masoom Raza</div>
                  <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">Paperback • 116p Pages • Rajkamal Prakashan</div>
                  <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹199.00</div>
                </div>
              </div>
              <p style="font-size: 12px; color: #64748B; line-height: 1.5; margin: 0 0 8px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                Unforgettable portrayal of childhood friendship between Topi and Iffan bridging cultural divides.
              </p>
            </div>
            <div class="bento-card-actions">
              <button type="button" class="btn-overview" style="padding: 7px 10px; font-size: 12px;" onclick="openOverviewModal('bento-contemp-topi')">
                <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('bento-contemp-topi')">
                <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> + Add
              </button>
            </div>
          </div>
        
          </div>
        </div>

      </div>
    </section>
    


    <!-- =========================================================================
         7. SECTION 4: LAW, JUDICIARY & SAHITYA REFERENCE ARCHIVE (#law-academic-vault)
         ========================================================================= -->
    <section id="law-academic-vault" style="background: #FFFFFF;">
      <div class="site-container">
        
        <div class="editorial-header">
          <div>
            <div class="sec-overline">SCHOLAR ARCHIVE</div>
            <h2>Law, Judiciary &amp; Academic Reference Vault</h2>
            <p>Authoritative treatises, Supreme Court commentaries, and essential civil services manuals curated for Prayagraj scholars.</p>
          </div>
        </div>

        <div class="vault-layout">
          
          <!-- Left Drawer Selector -->
          <div class="vault-nav-col">
            <button type="button" class="vault-tab-btn active" data-tab="law" onclick="switchVaultTab('law')">
              <span style="display: flex; align-items: center; gap: 10px;">
                <i data-lucide="scale" style="width: 18px; height: 18px;"></i>
                <span>Law &amp; Jurisprudence (4 Titles)</span>
              </span>
              <i data-lucide="chevron-right" style="width: 16px; height: 16px;"></i>
            </button>
            
            <button type="button" class="vault-tab-btn" data-tab="sahitya" onclick="switchVaultTab('sahitya')">
              <span style="display: flex; align-items: center; gap: 10px;">
                <i data-lucide="landmark" style="width: 18px; height: 18px;"></i>
                <span>Hindi Sahitya &amp; Vyakaran (4 Titles)</span>
              </span>
              <i data-lucide="chevron-right" style="width: 16px; height: 16px;"></i>
            </button>

            <button type="button" class="vault-tab-btn" data-tab="civil" onclick="switchVaultTab('civil')">
              <span style="display: flex; align-items: center; gap: 10px;">
                <i data-lucide="graduation-cap" style="width: 18px; height: 18px;"></i>
                <span>Civil Services &amp; McGraw Hill (4 Titles)</span>
              </span>
              <i data-lucide="chevron-right" style="width: 16px; height: 16px;"></i>
            </button>

            <button type="button" class="vault-tab-btn" data-tab="history" onclick="switchVaultTab('history')">
              <span style="display: flex; align-items: center; gap: 10px;">
                <i data-lucide="compass" style="width: 18px; height: 18px;"></i>
                <span>History &amp; Dalit Vimarsh (4 Titles)</span>
              </span>
              <i data-lucide="chevron-right" style="width: 16px; height: 16px;"></i>
            </button>

            <!-- Bulk Institutional Concierge Card -->
            <div class="vault-concierge-card">
              <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #92400E; margin-bottom: 6px;">
                Institutional / High Court Orders
              </h4>
              <p style="font-size: 12.5px; color: #78350F; line-height: 1.5; margin-bottom: 12px;">
                Bulk institutional order supply and invoice billing for Bar Council members, Law Chambers, and University Libraries.
              </p>
              <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books!%20I%20represent%20an%20institution/law%20firm%20and%20need%20bulk%20procurement." target="_blank" style="display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 700; color: #B45309; text-decoration: none;">
                <i data-lucide="message-circle" style="width: 15px; height: 15px;"></i> Contact Institutional Desk &rarr;
              </a>
            </div>
          </div>

          <!-- Right Pane: 2x2 Grid of 4 Books -->
                                                                                <div class="vault-cards-grid" id="vaultCardsContainer">
            <div class="vault-card" data-book-id="vault-law-highcourt" data-title="Bharatiya Bhasha Mein High Court Ki Vakalat" data-author="Anoop Baranwal ‘Deshbandhu’" data-price="₹350.00" data-binding="Paperback">
              <div class="indigo-3d-book-stage" onclick="openSoloBookPage('vault-law-highcourt', event)" style="width: 100%; height: 260px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
                <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                  <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                      <span>INDIGO VAULT</span>
                      <span style="color: #64748B;">AUTHENTIC</span>
                    </div>
                    <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                      Bharatiya Bhasha Mein High Court Ki Vakalat
                    </div>
                    <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                      By Anoop Baranwal ‘Deshbandhu’
                    </div>
                  </div>
                  <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                      विवरण / SYNOPSIS
                    </div>
                    <p style="font-size: 8.5px; line-height: 1.35; color: #475569; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">
                      भारतीय अदालतों में मातृभाषा और हिंदी में वकालत की ऐतिहासिक आवश्यकता और प्रक्रियात्मक मार्गदर्शन।
                    </p>
                  </div>
                  <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                    <span>216p &bull; Lokbharti Prakashan</span>
                    <span style="font-weight: 700; color: #B45309;">Paperback</span>
                  </div>
                </div>
                <div class="indigo-3d-cover-leaf">
                  <div class="indigo-3d-cover-front">
                    <img src="https://images.rajkamalprakashan.com/products/--1776288058601.jpg" alt="Bharatiya Bhasha Mein High Court Ki Vakalat" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                </div>
              </div>
              <div class="vault-card-body">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                  HIGH COURT PRACTICE
                </div>
                <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
                  <a href="javascript:void(0)" onclick="openSoloBookPage('vault-law-highcourt', event)" style="color: inherit; text-decoration: none;">Bharatiya Bhasha Mein High Court Ki Vakalat</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
                  Anoop Baranwal ‘Deshbandhu’
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹350.00</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button type="button" class="btn-overview" onclick="openOverviewModal('vault-law-highcourt')">
                    <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
                  </button>
                  <button type="button" class="btn-add-cart" onclick="addToCart('vault-law-highcourt', 'Bharatiya Bhasha Mein High Court Ki Vakalat', '₹350.00', 'https://images.rajkamalprakashan.com/products/--1776288058601.jpg', this, event)">
                    <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
                  </button>
                </div>
              </div>
            </div>
            <div class="vault-card" data-book-id="vault-law-constitution" data-title="Bharat Ka Samvidhan : Sankshipt Parichay" data-author="Subhash Kashyap" data-price="₹195.00" data-binding="Paperback">
              <div class="indigo-3d-book-stage" onclick="openSoloBookPage('vault-law-constitution', event)" style="width: 100%; height: 260px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
                <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                  <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                      <span>INDIGO VAULT</span>
                      <span style="color: #64748B;">AUTHENTIC</span>
                    </div>
                    <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                      Bharat Ka Samvidhan : Sankshipt Parichay
                    </div>
                    <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                      By Subhash Kashyap
                    </div>
                  </div>
                  <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                      विवरण / SYNOPSIS
                    </div>
                    <p style="font-size: 8.5px; line-height: 1.35; color: #475569; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">
                      हम, भारत के लोग, भारत को एक सम्पूर्ण प्रभुत्व-सम्पन्न, समाजवादी, पंथनिरपेक्ष, लोकतंत्रात्मक गणराज्य बनाने के लिए...
                    </p>
                  </div>
                  <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                    <span>184p &bull; Rajkamal Prakashan, Akshar</span>
                    <span style="font-weight: 700; color: #B45309;">Paperback</span>
                  </div>
                </div>
                <div class="indigo-3d-cover-leaf">
                  <div class="indigo-3d-cover-front">
                    <img src="https://images.rajkamalprakashan.com/products/--1776285478375.jpg" alt="Bharat Ka Samvidhan : Sankshipt Parichay" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                </div>
              </div>
              <div class="vault-card-body">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                  CONSTITUTION MANUAL
                </div>
                <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
                  <a href="javascript:void(0)" onclick="openSoloBookPage('vault-law-constitution', event)" style="color: inherit; text-decoration: none;">Bharat Ka Samvidhan : Sankshipt Parichay</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
                  Subhash Kashyap
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹195.00</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button type="button" class="btn-overview" onclick="openOverviewModal('vault-law-constitution')">
                    <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
                  </button>
                  <button type="button" class="btn-add-cart" onclick="addToCart('vault-law-constitution', 'Bharat Ka Samvidhan : Sankshipt Parichay', '₹195.00', 'https://images.rajkamalprakashan.com/products/--1776285478375.jpg', this, event)">
                    <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
                  </button>
                </div>
              </div>
            </div>
            <div class="vault-card" data-book-id="vault-law-ucc" data-title="Samaan Nagrik Sanhita : Chunautiya Aur Samadhan" data-author="Anoop Baranwal" data-price="₹399.00" data-binding="Paperback">
              <div class="indigo-3d-book-stage" onclick="openSoloBookPage('vault-law-ucc', event)" style="width: 100%; height: 260px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
                <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                  <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                      <span>INDIGO VAULT</span>
                      <span style="color: #64748B;">AUTHENTIC</span>
                    </div>
                    <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                      Samaan Nagrik Sanhita : Chunautiya Aur Samadhan
                    </div>
                    <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                      By Anoop Baranwal
                    </div>
                  </div>
                  <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                      विवरण / SYNOPSIS
                    </div>
                    <p style="font-size: 8.5px; line-height: 1.35; color: #475569; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">
                      समान नागरिक संहिता के संवैधानिक आयाम, विविध धर्मों की व्यक्तिगत विधियाँ और आधुनिक सुधारों का विमर्श।
                    </p>
                  </div>
                  <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                    <span>279p &bull; Lokbharti Prakashan</span>
                    <span style="font-weight: 700; color: #B45309;">Paperback</span>
                  </div>
                </div>
                <div class="indigo-3d-cover-leaf">
                  <div class="indigo-3d-cover-front">
                    <img src="https://images.rajkamalprakashan.com/products/--1776276748463.jpg" alt="Samaan Nagrik Sanhita : Chunautiya Aur Samadhan" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                </div>
              </div>
              <div class="vault-card-body">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                  LEGAL REFORM
                </div>
                <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
                  <a href="javascript:void(0)" onclick="openSoloBookPage('vault-law-ucc', event)" style="color: inherit; text-decoration: none;">Samaan Nagrik Sanhita : Chunautiya Aur Samadhan</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
                  Anoop Baranwal
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹399.00</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button type="button" class="btn-overview" onclick="openOverviewModal('vault-law-ucc')">
                    <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
                  </button>
                  <button type="button" class="btn-add-cart" onclick="addToCart('vault-law-ucc', 'Samaan Nagrik Sanhita : Chunautiya Aur Samadhan', '₹399.00', 'https://images.rajkamalprakashan.com/products/--1776276748463.jpg', this, event)">
                    <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
                  </button>
                </div>
              </div>
            </div>
            <div class="vault-card" data-book-id="vault-law-judiciary" data-title="Nyayapalika Kasauti Par" data-author="Kamlesh Jain, Edi. ranjeet verma" data-price="₹199.00" data-binding="Paperback">
              <div class="indigo-3d-book-stage" onclick="openSoloBookPage('vault-law-judiciary', event)" style="width: 100%; height: 260px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
                <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                  <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                      <span>INDIGO VAULT</span>
                      <span style="color: #64748B;">AUTHENTIC</span>
                    </div>
                    <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                      Nyayapalika Kasauti Par
                    </div>
                    <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                      By Kamlesh Jain, Edi. ranjeet verma
                    </div>
                  </div>
                  <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                      विवरण / SYNOPSIS
                    </div>
                    <p style="font-size: 8.5px; line-height: 1.35; color: #475569; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">
                      भारतीय न्यायपालिका की कार्यप्रणाली, जनहित याचिकाएं और नागरिक अधिकारों की निष्पक्ष समीक्षा।
                    </p>
                  </div>
                  <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                    <span>152p &bull; Rajkamal Prakashan</span>
                    <span style="font-weight: 700; color: #B45309;">Paperback</span>
                  </div>
                </div>
                <div class="indigo-3d-cover-leaf">
                  <div class="indigo-3d-cover-front">
                    <img src="https://images.rajkamalprakashan.com/products/--1776287918098.jpg" alt="Nyayapalika Kasauti Par" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                </div>
              </div>
              <div class="vault-card-body">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                  JUDICIAL CRITIQUE
                </div>
                <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
                  <a href="javascript:void(0)" onclick="openSoloBookPage('vault-law-judiciary', event)" style="color: inherit; text-decoration: none;">Nyayapalika Kasauti Par</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
                  Kamlesh Jain, Edi. ranjeet verma
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹199.00</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button type="button" class="btn-overview" onclick="openOverviewModal('vault-law-judiciary')">
                    <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
                  </button>
                  <button type="button" class="btn-add-cart" onclick="addToCart('vault-law-judiciary', 'Nyayapalika Kasauti Par', '₹199.00', 'https://images.rajkamalprakashan.com/products/--1776287918098.jpg', this, event)">
                    <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================================
         8. SECTION 5: PAN-INDIA FILTERABLE CATALOG ARCHIVE (#shop-all-catalog)
         ========================================================================= -->
    <section id="shop-all-catalog" style="background: #FAF8F5;">
      <div class="site-container">
        
        <div class="editorial-header">
          <div>
            <div class="sec-overline">PAN-INDIA DIRECTORY</div>
            <h2>Browse Our Entire 5,500+ Book Catalog</h2>
            <p>Instant search and category faceted filtering across India's premier independent bookstore archive.</p>
          </div>
          <a href="#shop-all-catalog" onclick="browseAllBooks(event)" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none; align-self: flex-end; padding-bottom: 8px; cursor: pointer;">
            Browse All 5,500+ Books &rarr;
          </a>
        </div>

        <!-- Faceted Category Filter Pills -->
        <div class="catalog-filter-bar">
          <div class="catalog-filter-pills" id="catalogCategoryPills">
            <button type="button" class="cat-pill active" data-cat="all" onclick="filterCatalog('all')">All Books (5,500+)</button>
            <button type="button" class="cat-pill" data-cat="shayari" onclick="filterCatalog('shayari')">Shayari &amp; Poetry</button>
            <button type="button" class="cat-pill" data-cat="novel" onclick="filterCatalog('novel')">Novels &amp; Fiction</button>
            <button type="button" class="cat-pill" data-cat="classics" onclick="filterCatalog('classics')">Hindi Classics &amp; Sahitya</button>
            <button type="button" class="cat-pill" data-cat="drama" onclick="filterCatalog('drama')">Plays &amp; Drama</button>
            <button type="button" class="cat-pill" data-cat="history" onclick="filterCatalog('history')">History &amp; Biography</button>
            <button type="button" class="cat-pill" data-cat="law" onclick="filterCatalog('law')">Law &amp; Academic</button>
            <button type="button" class="cat-pill" data-cat="bestseller" onclick="filterCatalog('bestseller')">Top Bestsellers</button>
          </div>

          <!-- Real-Time Search Bar with Category Dropdown -->
          <div class="catalog-search-wrap search-input-wrap search-input-group">
            <select id="catalogSearchCategory" class="search-category-select" title="Filter search by category">
              <option value="all">All Books</option>
              <option value="Fiction : Novel">Fiction : Novel</option>
              <option value="Poetry / Shayari">Poetry &amp; Shayari</option>
              <option value="Fiction : Stories">Fiction : Stories</option>
              <option value="Literary Criticism">Literary Criticism</option>
              <option value="History">History &amp; Politics</option>
              <option value="Biography">Biography &amp; Memoirs</option>
              <option value="Law">Law &amp; Constitution</option>
            </select>
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8; margin-left: 8px;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value); handleSearchInput(this.value, 'catalog')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'catalog-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'catalog-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">Search</button>
            <div id="catalog-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>
        </div>

        <!-- 4-Column Responsive Grid of Books (Pre-Rendered Initial Page) -->
        <div class="catalog-cards-grid" id="catalogGridContainer">
          <div class="catalog-card" data-book-id="podium-godan" data-title="Godan" data-author="Premchand" data-price="₹299.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('podium-godan', '/products/godan-premchand', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Godan
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Premchand
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    होरी जब घर से निकला, तो उसके दिल में एक ही तमन्ना थी कि किसी तरह एक गाय मिल जाए। उसका जीवन गाय की लालसा में ही बीत गया था।
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>312p</span>
                  <span style="font-weight: 600; color: #0066B3;">Lokbharti Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="assets/hero-godan.jpg" alt="Godan" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Godan', 'Premchand');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Lokbharti Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Paperback &bull; ₹299.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/godan-premchand" onclick="handleBookAction('podium-godan', '/products/godan-premchand', event)" style="color: inherit; text-decoration: none;">Godan</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Premchand
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('podium-godan')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('podium-godan', 'Godan', 299.00, 'assets/hero-godan.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="podium-raag-darbari" data-title="Raag Darbari" data-author="Shrilal Shukla" data-price="₹499.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('podium-raag-darbari', '/products/raag-darbari-shrilal-shukla', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Raag Darbari
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Shrilal Shukla
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    यह कहानी शिवपालगंज की है जहाँ सड़क के किनारे का कॉलेज हर साल नए क्रांतिकारी और बेरोजगार पैदा करता है। रंगनाथ ने जब गाँव में कदम रखा...
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>423p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="assets/hero-raag-darbari.jpg" alt="Raag Darbari" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Raag Darbari', 'Shrilal Shukla');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Paperback &bull; ₹499.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/raag-darbari-shrilal-shukla" onclick="handleBookAction('podium-raag-darbari', '/products/raag-darbari-shrilal-shukla', event)" style="color: inherit; text-decoration: none;">Raag Darbari</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Shrilal Shukla
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹499.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('podium-raag-darbari')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('podium-raag-darbari', 'Raag Darbari', 499.00, 'assets/hero-raag-darbari.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="podium-chitralekha" data-title="Chitralekha" data-author="Bhagwaticharan Verma" data-price="₹299.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('podium-chitralekha', '/products/chitralekha-bhagwaticharan-verma', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Chitralekha
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Bhagwaticharan Verma
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    संसार में पाप क्या है और पुण्य क्या है? क्या मनुष्य परिस्थिति का दास है या अपनी नियति का स्वामी? इसी शाश्वत प्रश्न की खोज...
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>200p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="assets/hero-chitralekha.jpg" alt="Chitralekha" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Chitralekha', 'Bhagwaticharan Verma');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Paperback &bull; ₹299.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/chitralekha-bhagwaticharan-verma" onclick="handleBookAction('podium-chitralekha', '/products/chitralekha-bhagwaticharan-verma', event)" style="color: inherit; text-decoration: none;">Chitralekha</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Bhagwaticharan Verma
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('podium-chitralekha')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('podium-chitralekha', 'Chitralekha', 299.00, 'assets/hero-chitralekha.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="podium-rashmirathi" data-title="Rashmirathi : Dinkar Granthmala" data-author="Ramdhari Singh 'Dinkar'" data-price="₹299.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('podium-rashmirathi', '/products/rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Rashmirathi : Dinkar Granthmala
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Ramdhari Singh 'Dinkar'
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    मूल जानना बड़ा कठिन है नदियों का, वीरों का, धनुष छोड़कर और गोत्र क्या होता रणधीरों का? पाते हैं सम्मान तपोबल से भूतल पर शूर...
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>192p</span>
                  <span style="font-weight: 600; color: #0066B3;">Lokbharti Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="assets/hero-rashmirathi.jpg" alt="Rashmirathi : Dinkar Granthmala" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Rashmirathi : Dinkar Granthmala', 'Ramdhari Singh 'Dinkar'');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Lokbharti Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Paperback &bull; ₹299.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar" onclick="handleBookAction('podium-rashmirathi', '/products/rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar', event)" style="color: inherit; text-decoration: none;">Rashmirathi : Dinkar Granthmala</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Ramdhari Singh 'Dinkar'
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('podium-rashmirathi')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('podium-rashmirathi', 'Rashmirathi : Dinkar Granthmala', 299.00, 'assets/hero-rashmirathi.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="podium-kuchh-ishq" data-title="Kuchh Ishq Kiya Kuchh Kaam Kiya" data-author="Piyush Mishra" data-price="₹250.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('podium-kuchh-ishq', '/products/kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Kuchh Ishq Kiya Kuchh Kaam Kiya
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Piyush Mishra
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    हम दोनों में जब झगड़ा हुआ, तो इश्क़ हमारा सच्चा निकला। वो भी न हारा, मैं भी न झुका, बस दिल का वो दरवाज़ा खुला का खुला रहा...
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>147p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="assets/hero-kuchh-ishq.jpg" alt="Kuchh Ishq Kiya Kuchh Kaam Kiya" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Kuchh Ishq Kiya Kuchh Kaam Kiya', 'Piyush Mishra');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Paperback &bull; ₹250.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra" onclick="handleBookAction('podium-kuchh-ishq', '/products/kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra', event)" style="color: inherit; text-decoration: none;">Kuchh Ishq Kiya Kuchh Kaam Kiya</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Piyush Mishra
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹250.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('podium-kuchh-ishq')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('podium-kuchh-ishq', 'Kuchh Ishq Kiya Kuchh Kaam Kiya', 250.00, 'assets/hero-kuchh-ishq.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="podium-gypsy" data-title="Gypsy" data-author="Ila chandra Joshi" data-price="₹499.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('podium-gypsy', '/products/gypsy-ila-chandra-joshi', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Gypsy
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Ila chandra Joshi
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    मनुष्य की चेतना के भीतर अनगिनत गुफाएँ हैं जिनमें दमित इच्छाएँ और छायाएँ सांस लेती हैं। जिप्सी उसी जटिल मन का उद्घाटन है...
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>375p</span>
                  <span style="font-weight: 600; color: #0066B3;">Lokbharti Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="assets/hero-gypsy.jpg" alt="Gypsy" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Gypsy', 'Ila chandra Joshi');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Lokbharti Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Paperback &bull; ₹499.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/gypsy-ila-chandra-joshi" onclick="handleBookAction('podium-gypsy', '/products/gypsy-ila-chandra-joshi', event)" style="color: inherit; text-decoration: none;">Gypsy</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Ila chandra Joshi
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹499.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('podium-gypsy')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('podium-gypsy', 'Gypsy', 499.00, 'assets/hero-gypsy.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="piyush-arambh-hai-prachand-piyush-mishra-paperback" data-title="Arambh Hai Prachand" data-author="Piyush Mishra" data-price="₹199.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('piyush-arambh-hai-prachand-piyush-mishra-paperback', '/products/arambh-hai-prachand-piyush-mishra', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Arambh Hai Prachand
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Piyush Mishra
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    « Arambh Hai Prachand — पीयूष मिश्रा की सशक्त और बेबाक लेखनी का प्रामाणिक संस्करण। »
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>96p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="https://images.rajkamalprakashan.com/products/arambh-hai-prachand-1776283699927.jpg" alt="Arambh Hai Prachand" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Arambh Hai Prachand', 'Piyush Mishra');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Paperback &bull; ₹199.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/arambh-hai-prachand-piyush-mishra" onclick="handleBookAction('piyush-arambh-hai-prachand-piyush-mishra-paperback', '/products/arambh-hai-prachand-piyush-mishra', event)" style="color: inherit; text-decoration: none;">Arambh Hai Prachand</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Piyush Mishra
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹199.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('piyush-arambh-hai-prachand-piyush-mishra-paperback')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('piyush-arambh-hai-prachand-piyush-mishra-paperback', 'Arambh Hai Prachand', 199.00, 'https://images.rajkamalprakashan.com/products/arambh-hai-prachand-1776283699927.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="piyush-gagan-damama-bajyo-piyush-mishra-hardcover" data-title="Gagan Damama Bajyo" data-author="Piyush Mishra" data-price="₹450.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('piyush-gagan-damama-bajyo-piyush-mishra-hardcover', '/products/gagan-damama-bajyo-piyush-mishra', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Gagan Damama Bajyo
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Piyush Mishra
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    « Gagan Damama Bajyo — पीयूष मिश्रा की सशक्त और बेबाक लेखनी का प्रामाणिक संस्करण। »
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>128p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="https://images.rajkamalprakashan.com/products/--1776279058569.jpg" alt="Gagan Damama Bajyo" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Gagan Damama Bajyo', 'Piyush Mishra');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Hardcover &bull; ₹450.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/gagan-damama-bajyo-piyush-mishra" onclick="handleBookAction('piyush-gagan-damama-bajyo-piyush-mishra-hardcover', '/products/gagan-damama-bajyo-piyush-mishra', event)" style="color: inherit; text-decoration: none;">Gagan Damama Bajyo</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Piyush Mishra
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹450.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('piyush-gagan-damama-bajyo-piyush-mishra-hardcover')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('piyush-gagan-damama-bajyo-piyush-mishra-hardcover', 'Gagan Damama Bajyo', 450.00, 'https://images.rajkamalprakashan.com/products/--1776279058569.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="piyush-jab-shahar-hamara-sota-hai-piyush-mishra-hardcover" data-title="Jab Shahar Hamara Sota Hai" data-author="Piyush Mishra" data-price="₹395.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('piyush-jab-shahar-hamara-sota-hai-piyush-mishra-hardcover', '/products/jab-shahar-hamara-sota-hai-piyush-mishra', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Jab Shahar Hamara Sota Hai
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Piyush Mishra
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    « Jab Shahar Hamara Sota Hai — पीयूष मिश्रा की सशक्त और बेबाक लेखनी का प्रामाणिक संस्करण। »
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>120p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="https://images.rajkamalprakashan.com/products/--1776279060609.jpg" alt="Jab Shahar Hamara Sota Hai" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Jab Shahar Hamara Sota Hai', 'Piyush Mishra');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Hardcover &bull; ₹395.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/jab-shahar-hamara-sota-hai-piyush-mishra" onclick="handleBookAction('piyush-jab-shahar-hamara-sota-hai-piyush-mishra-hardcover', '/products/jab-shahar-hamara-sota-hai-piyush-mishra', event)" style="color: inherit; text-decoration: none;">Jab Shahar Hamara Sota Hai</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Piyush Mishra
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹395.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('piyush-jab-shahar-hamara-sota-hai-piyush-mishra-hardcover')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('piyush-jab-shahar-hamara-sota-hai-piyush-mishra-hardcover', 'Jab Shahar Hamara Sota Hai', 395.00, 'https://images.rajkamalprakashan.com/products/--1776279060609.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="piyush-mere-manch-ki-sargam-piyush-mishra-hardcover" data-title="Mere Manch Ki Sargam" data-author="Piyush Mishra" data-price="₹450.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('piyush-mere-manch-ki-sargam-piyush-mishra-hardcover', '/products/mere-manch-ki-sargam-piyush-mishra', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Mere Manch Ki Sargam
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Piyush Mishra
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    « Mere Manch Ki Sargam — पीयूष मिश्रा की सशक्त और बेबाक लेखनी का प्रामाणिक संस्करण। »
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>192P</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="https://images.rajkamalprakashan.com/products/--1776279064803.jpg" alt="Mere Manch Ki Sargam" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Mere Manch Ki Sargam', 'Piyush Mishra');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Hardcover &bull; ₹450.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/mere-manch-ki-sargam-piyush-mishra" onclick="handleBookAction('piyush-mere-manch-ki-sargam-piyush-mishra-hardcover', '/products/mere-manch-ki-sargam-piyush-mishra', event)" style="color: inherit; text-decoration: none;">Mere Manch Ki Sargam</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Piyush Mishra
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹450.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('piyush-mere-manch-ki-sargam-piyush-mishra-hardcover')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('piyush-mere-manch-ki-sargam-piyush-mishra-hardcover', 'Mere Manch Ki Sargam', 450.00, 'https://images.rajkamalprakashan.com/products/--1776279064803.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="rahi-aadha-gaon-rahi-masoom-raza-hardcover" data-title="Aadha Gaon" data-author="Rahi Masoom Raza" data-price="₹1995.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('rahi-aadha-gaon-rahi-masoom-raza-hardcover', '/products/aadha-gaon-rahi-masoom-raza', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Aadha Gaon
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Rahi Masoom Raza
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    « Aadha Gaon — राही मासूम रज़ा की अमर साहित्यिक धरोहर का प्रामाणिक संस्करण। »
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>344p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="https://images.rajkamalprakashan.com/products/--1776277450108.jpg" alt="Aadha Gaon" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Aadha Gaon', 'Rahi Masoom Raza');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Hardcover &bull; ₹1995.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/aadha-gaon-rahi-masoom-raza" onclick="handleBookAction('rahi-aadha-gaon-rahi-masoom-raza-hardcover', '/products/aadha-gaon-rahi-masoom-raza', event)" style="color: inherit; text-decoration: none;">Aadha Gaon</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Rahi Masoom Raza
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹1995.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('rahi-aadha-gaon-rahi-masoom-raza-hardcover')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('rahi-aadha-gaon-rahi-masoom-raza-hardcover', 'Aadha Gaon', 1995.00, 'https://images.rajkamalprakashan.com/products/--1776277450108.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          <div class="catalog-card" data-book-id="rahi-asantosh-ke-din-rahi-masoom-raza-hardcover" data-title="Asantosh Ke Din" data-author="Rahi Masoom Raza" data-price="₹495.00">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('rahi-asantosh-ke-din-rahi-masoom-raza-hardcover', '/products/asantosh-ke-din-rahi-masoom-raza', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                    <span>INDIGO ARCHIVE</span>
                    <span style="color: #64748B;">AUTHENTIC</span>
                  </div>
                  <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                    Asantosh Ke Din
                  </div>
                  <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    By Rahi Masoom Raza
                  </div>
                </div>
                <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                  <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                    अध्याय १ / PROLOGUE
                  </div>
                  <p style="font-family: 'Merriweather', Georgia, serif; font-size: 9.5px; line-height: 1.45; color: #334155; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden;">
                    « Asantosh Ke Din — राही मासूम रज़ा की अमर साहित्यिक धरोहर का प्रामाणिक संस्करण। »
                  </p>
                </div>
                <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                  <span>91p</span>
                  <span style="font-weight: 600; color: #0066B3;">Rajkamal Prakashan</span>
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img referrerpolicy="no-referrer" src="https://images.rajkamalprakashan.com/products/--1776284826554.jpg" alt="Asantosh Ke Din" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('Asantosh Ke Din', 'Rahi Masoom Raza');" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back" style="background: linear-gradient(135deg, #09132C 0%, #1E293B 100%);">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    100% GENUINE
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                    Rajkamal Prakashan
                  </div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">
                    Hardcover &bull; ₹495.00
                  </div>
                  <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                    Click for Details &rarr;
                  </div>
                </div>
              </div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: #0066B3; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.05em;">
              IN STOCK &bull; SHIPS IN 24H
            </div>
            <h3 class="catalog-card-title">
              <a href="/products/asantosh-ke-din-rahi-masoom-raza" onclick="handleBookAction('rahi-asantosh-ke-din-rahi-masoom-raza-hardcover', '/products/asantosh-ke-din-rahi-masoom-raza', event)" style="color: inherit; text-decoration: none;">Asantosh Ke Din</a>
            </h3>
            <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Rahi Masoom Raza
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹495.00</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <button type="button" class="btn-overview" onclick="openOverviewModal('rahi-asantosh-ke-din-rahi-masoom-raza-hardcover')">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" onclick="addToCart('rahi-asantosh-ke-din-rahi-masoom-raza-hardcover', 'Asantosh Ke Din', 495.00, 'https://images.rajkamalprakashan.com/products/--1776284826554.jpg', this, event)">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
        </div>

        <!-- Catalog Pagination Controls (12 Books per Page) -->
        <div id="catalogPagination" class="catalog-pagination"></div>

      </div>
    </section>


    <!-- =========================================================================
         9. SECTION 6: 4-CARD TRUST FEATURES STRIP
         ========================================================================= -->
    <section style="background: #FFFFFF; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; padding: 48px 0 !important;">
      <div class="site-container trust-strip-grid trust-features-grid features-grid">
        
        <div class="trust-card">
          <div class="trust-card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#B45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <h4 style="font-family: 'Merriweather', serif; font-size: 16px; font-weight: 700; color: #0F172A;">100% Authentic Editions</h4>
          <p style="font-size: 12.5px; color: #64748B; line-height: 1.5;">Direct partnerships with official publishers like Vani, Rajkamal, Rekhta, Penguin, and LexisNexis.</p>
        </div>

        <div class="trust-card">
          <div class="trust-card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#B45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z"/></svg>
          </div>
          <h4 style="font-family: 'Merriweather', serif; font-size: 16px; font-weight: 700; color: #0F172A;">Instant WhatsApp COD</h4>
          <p style="font-size: 12.5px; color: #64748B; line-height: 1.5;">Order any title in 1-click via WhatsApp (+91 8933063306) with Cash on Delivery across 19,000+ pin codes.</p>
        </div>

        <div class="trust-card">
          <div class="trust-card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#B45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18.5" r="2.5"/><circle cx="7" cy="18.5" r="2.5"/></svg>
          </div>
          <h4 style="font-family: 'Merriweather', serif; font-size: 16px; font-weight: 700; color: #0F172A;">Pan-India Express Dispatch</h4>
          <p style="font-size: 12.5px; color: #64748B; line-height: 1.5;">Same-day dispatch from our central Prayagraj hub with live courier tracking delivered right to your door.</p>
        </div>

        <div class="trust-card">
          <div class="trust-card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#B45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
          </div>
          <h4 style="font-family: 'Merriweather', serif; font-size: 16px; font-weight: 700; color: #0F172A;">Cultural Book Community</h4>
          <p style="font-size: 12.5px; color: #64748B; line-height: 1.5;">Preserving Urdu poetry, Hindi literature, and legal scholarship through book clubs and reader gatherings.</p>
        </div>

      </div>
    </section>


    <!-- =========================================================================
         10. SECTION 7: PRAYAGRAJ HERITAGE & CONTACT
         ========================================================================= -->
    <section class="heritage-section">
      <div class="site-container">
        
        <div class="heritage-grid">
          <div>
            <div class="sec-overline" style="color: #D99B26;">ROOTED IN PRAYAGRAJ</div>
            <h2 style="font-family: 'Merriweather', Georgia, serif; font-size: 28px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 16px;">
              The Sacred Sangam of Indian Literature &amp; Legal Thought
            </h2>
            <p style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 16px;">
              Indigo Books India is rooted in the historic literary city of Prayagraj—the cultural crossroads of the Hindi belt and Urdu poetry. We provide over 5,500+ authentic publisher editions ranging from timeless Rekhta poetry and contemporary Indian fiction to university legal treatises and competitive examination archives.
            </p>
            <p style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 24px;">
              From the High Court of Judicature at Allahabad to the storied halls of Allahabad University, we take pride in serving India's finest advocates, professors, civil service aspirants, and discerning bibliophiles.
            </p>
            
            <div class="heritage-stats-row">
              <div>
                <div class="heritage-stat-val">5,500+</div>
                <div class="heritage-stat-lbl">Authentic Titles</div>
              </div>
              <div>
                <div class="heritage-stat-val">19,000+</div>
                <div class="heritage-stat-lbl">Pin Codes Served</div>
              </div>
              <div>
                <div class="heritage-stat-val">100%</div>
                <div class="heritage-stat-lbl">Publisher Original</div>
              </div>
            </div>
          </div>

          <!-- Contact & Hub Details Card -->
          <div class="heritage-card">
            <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 20px; font-weight: 700; color: #0F172A; margin-bottom: 14px;">
              Prayagraj Central Dispatch Hub
            </h3>
            <p style="font-size: 13px; color: #64748B; line-height: 1.6; margin-bottom: 20px;">
              Every parcel is carefully inspected, packed with moisture-resistant protective book sleeves, and dispatched via express air/surface courier networks across Bharat.
            </p>

            <ul class="heritage-details-list">
              <li>
                <i data-lucide="map-pin" style="width: 16px; height: 16px; color: #B45309; flex-shrink: 0;"></i>
                <span>Headquarters: Prayagraj, Uttar Pradesh, India</span>
              </li>
              <li>
                <i data-lucide="phone" style="width: 16px; height: 16px; color: #B45309; flex-shrink: 0;"></i>
                <span>Customer Desk: <strong>+91 8933063306</strong></span>
              </li>
              <li>
                <i data-lucide="mail" style="width: 16px; height: 16px; color: #B45309; flex-shrink: 0;"></i>
                <span>Email: info@indigobooks.com</span>
              </li>
              <li>
                <i data-lucide="clock" style="width: 16px; height: 16px; color: #B45309; flex-shrink: 0;"></i>
                <span>Dispatch Cadence: Monday &ndash; Saturday (Within 24 Hours)</span>
              </li>
            </ul>

            <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books!%20I%20am%20inquiring%20about%20a%20rare%20book%20edition." target="_blank" class="hero-shop-btn" style="width: 100%; justify-content: center;">
              <span>Inquire on WhatsApp Desk &rarr;</span>
            </a>
          </div>
        </div>

      </div>
    </section>

  </div><!-- /#homepage-view -->


  <!-- =========================================================================
       DEDICATED SEARCH RESULTS PAGE VIEW (#indigo-search-results-view)
       ========================================================================= -->
  <div id="indigo-search-results-view" class="store-view-section" style="display: none; background: #FAF8F5; min-height: 80vh; padding: 36px 0 64px;">
    <div class="site-container" style="max-width: 1320px; margin: 0 auto; padding: 0 24px; box-sizing: border-box;">
      
      <!-- Top Breadcrumb Bar -->
      <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 0 20px; border-bottom: 1px solid #E2E8F0; margin-bottom: 28px; font-size: 13px; color: #64748B; flex-wrap: wrap; gap: 12px;">
        <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
          <a href="#top" onclick="window.closeSearchResultsView(); return false;" style="color: #0066B3; text-decoration: none; font-weight: 600;">Home</a>
          <span style="color: #94A3B8; font-size: 12px;">&rsaquo;</span>
          <span style="color: #0F172A; font-weight: 600;">Search Results</span>
        </div>
        <button type="button" class="btn-back-to-store" onclick="window.closeSearchResultsView()" style="display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; color: #0F172A; border: 1px solid #CBD5E1; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer;">
          <i data-lucide="arrow-left" style="width: 15px; height: 15px;"></i> Back to Bookstore
        </button>
      </div>

      <!-- Search Header & Active Search Form -->
      <div style="text-align: center; max-width: 720px; margin: 0 auto 32px;">
        <div style="font-size: 11px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 6px;">
          PAN-INDIA ARCHIVE SEARCH
        </div>
        <h1 style="font-family: 'Merriweather', Georgia, serif; font-size: 32px; font-weight: 700; color: #0F172A; margin: 0 0 8px;">
          Search Results for "<span id="search-query-display"></span>"
        </h1>
        <p style="font-size: 14px; color: #64748B; margin: 0 0 20px;">
          (Found <strong id="search-result-count" style="color: #0F172A;">0</strong> books)
        </p>

        <!-- Search Input with Auto-Suggestions -->
        <form onsubmit="window.submitSearch(event, 'results-search-input'); return false;" class="search-input-wrap" style="position: relative; display: flex; align-items: center; background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 10px; padding: 6px 8px 6px 16px; box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06); gap: 10px;">
          <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
          <input
            type="text"
            id="results-search-input"
            placeholder="Search title, author, ISBN..."
            oninput="handleSearchInput(this.value, 'results')"
            style="flex: 1; border: none; outline: none; font-size: 14px; color: #0F172A; background: transparent; padding: 8px 0;"
            autocomplete="off"
          />
          <button type="submit" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 8px; padding: 10px 20px; font-size: 13.5px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 6px;">
            Search
          </button>
          <div id="results-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
        </form>
      </div>

      <!-- Filter & Sort Toolbar -->
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 28px; padding: 12px 16px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;">
        <!-- Category Filter Pills -->
        <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;" id="searchResultsCategoryPills">
          <button type="button" class="cat-pill active" onclick="filterSearchResults('all', this)" style="padding: 6px 14px; font-size: 12px;">All Matches</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('shayari', this)" style="padding: 6px 14px; font-size: 12px;">Shayari &amp; Poetry</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('novel', this)" style="padding: 6px 14px; font-size: 12px;">Novels &amp; Fiction</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('classics', this)" style="padding: 6px 14px; font-size: 12px;">Hindi Classics &amp; Sahitya</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('drama', this)" style="padding: 6px 14px; font-size: 12px;">Plays &amp; Drama</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('history', this)" style="padding: 6px 14px; font-size: 12px;">History &amp; Biography</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('law', this)" style="padding: 6px 14px; font-size: 12px;">Law &amp; Academic</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('bestseller', this)" style="padding: 6px 14px; font-size: 12px;">Top Bestsellers</button>
        </div>

        <!-- Sort Dropdown -->
        <div style="display: flex; align-items: center; gap: 8px;">
          <label for="searchResultsSort" style="font-size: 12.5px; font-weight: 600; color: #64748B;">Sort by:</label>
          <select id="searchResultsSort" onchange="sortSearchResults(this.value)" style="border: 1px solid #CBD5E1; border-radius: 6px; padding: 6px 12px; font-size: 12.5px; font-weight: 600; color: #0F172A; background: #FFFFFF; outline: none; cursor: pointer;">
            <option value="featured">Featured Relevance</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
            <option value="title-asc">Title: A-Z</option>
          </select>
        </div>
      </div>

      <!-- 4-Column Responsive Results Grid -->
      <div id="search-results-grid" class="catalog-cards-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;">
        <!-- Rendered dynamically by window.openSearchResultsPage -->
      </div>

    </div>
  </div><!-- /#indigo-search-results-view -->




  <!-- =========================================================================
       10. DEDICATED SOLO PRODUCT PAGE VIEW (#single-product-page-view & #indigo-solo-product-view)
       ========================================================================= -->
  <div id="single-product-page-view" class="store-view-section" style="display: none; background: #FAF8F5; min-height: auto;">
    <div id="indigo-solo-product-view"></div>
    <div class="product-page-wrapper" style="max-width: 1320px; margin: 0 auto; padding: 20px 20px 24px;">
      
      <!-- Top Breadcrumb Bar -->
      <div class="product-breadcrumb-bar">
        <div class="breadcrumb-nav">
          <a href="#top" onclick="closeDedicatedProductPage(); return false;">Home</a>
          <span class="breadcrumb-separator">&rsaquo;</span>
          <span id="pdpBreadcrumbCategory">Curated Literature</span>
          <span class="breadcrumb-separator">&rsaquo;</span>
          <span id="pdpBreadcrumbTitle" style="color: #0F172A; font-weight: 600;">Book Title</span>
        </div>
        <button type="button" class="btn-back-to-store" onclick="closeDedicatedProductPage()">
          <i data-lucide="arrow-left" style="width: 15px; height: 15px;"></i> Back to Bookstore
        </button>
      </div>

      <!-- 3-Column Main Product Showcase (340px 1fr 310px) -->
      <div class="product-pdp-grid">
        
        <!-- LEFT COLUMN: Framed Cover with 3D Hover Preview & Thumbnails -->
        <div class="pdp-left-col">
          <div class="pdp-cover-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 20px 16px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); text-align: center;">
            
            <div class="indigo-3d-book-stage" id="pdp3dStage" style="max-width: 280px; margin: 0 auto 16px;">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">
                  INDIGO ARCHIVE &bull; PREVIEW
                </div>
                <div id="pdp3dInsideTitle" style="font-family: 'Merriweather', serif; font-size: 12px; line-height: 1.4; color: #1E293B; font-weight: 700;">
                  Book Title
                </div>
                <div id="pdp3dInsideAuthor" style="font-size: 10px; color: #64748B;">
                  By Author
                </div>
                <div id="pdp3dInsideFooter" style="font-size: 9px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 4px;">
                  100% Authentic Edition
                </div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img id="pdpMainCoverImg" src="" alt="Book Cover" class="pdp-cover-img" referrerpolicy="no-referrer" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                </div>
                <div class="indigo-3d-cover-back">
                  <div style="font-size: 10px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                    100% GENUINE
                  </div>
                  <div id="pdpCoverBackPub" style="font-size: 11px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">
                    Authorized Copy
                  </div>
                  <div id="pdpCoverBackFormat" style="font-size: 10px; color: #CBD5E1;">
                    Paperback Edition
                  </div>
                </div>
              </div>
            </div>

            <!-- Mini Cover Thumbnail Selector Box -->
            <div id="pdpThumbnailBox" style="display: flex; justify-content: center; gap: 10px; margin-bottom: 16px;">
              <div id="pdpThumb1" class="pdp-thumb-item active" style="width: 48px; height: 68px; border: 2px solid #0F172A; border-radius: 4px; overflow: hidden; cursor: pointer;">
                <img id="pdpThumbImg1" src="" style="width: 100%; height: 100%; object-fit: cover;" />
              </div>
              <div id="pdpThumb2" class="pdp-thumb-item" style="width: 48px; height: 68px; border: 1px solid #CBD5E1; border-radius: 4px; overflow: hidden; cursor: pointer; display: none;">
                <img id="pdpThumbImg2" src="" style="width: 100%; height: 100%; object-fit: cover;" />
              </div>
            </div>

            <button type="button" class="pdp-look-inside-btn" onclick="togglePdpLookInside()">
              <i data-lucide="book-open" style="width: 16px; height: 16px;"></i> Look Inside / First Page Excerpt
            </button>

            <!-- Collapsible First Page Excerpt Box -->
            <div id="pdpExcerptBox" class="pdp-excerpt-box">
              <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 6px;">
                अध्याय १ &bull; FIRST PAGE PREVIEW
              </div>
              <p id="pdpExcerptText" style="margin: 0; font-size: 13.5px; line-height: 1.7; color: #334155;">
                Loading preview excerpt...
              </p>
            </div>
          </div>

          <!-- Trust Perks Card (Modular for Desktop & Mobile Order) -->
          <div class="pdp-trust-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 16px 18px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); margin-top: 0;">
            <ul class="pdp-perks-checklist">
              <li>
                <i data-lucide="shield-check" style="width: 15px; height: 15px; color: #16A34A; flex-shrink: 0; margin-top: 2px;"></i>
                <span><strong>100% Genuine Edition:</strong> Direct authorized publisher copy with crisp binding.</span>
              </li>
              <li>
                <i data-lucide="truck" style="width: 15px; height: 15px; color: #16A34A; flex-shrink: 0; margin-top: 2px;"></i>
                <span><strong>Prayagraj Hub Dispatch:</strong> Same-day dispatch with moisture-proof packing.</span>
              </li>
              <li>
                <i data-lucide="check-circle" style="width: 15px; height: 15px; color: #16A34A; flex-shrink: 0; margin-top: 2px;"></i>
                <span><strong>Cash on Delivery:</strong> Pay at your doorstep across 19,000+ PIN codes.</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- CENTER COLUMN: Book Details, Variant Switcher & Tabs -->
        <div class="pdp-center-col">
          <div class="pdp-info-header-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-bottom: none; border-radius: 14px 14px 0 0; padding: 22px 24px 16px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); margin-bottom: 0;">
            <span id="pdpGenreTag" class="pdp-genre-pill" style="display: inline-block; background: #EFF6FF; color: #1D4ED8; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px;">
              FICTION &bull; NOVEL
            </span>
            <h1 id="pdpTitle" class="pdp-book-title" style="font-family: 'Merriweather', Georgia, serif; font-size: 30px; font-weight: 700; color: #09132C; line-height: 1.25; margin: 0 0 10px;">
              Book Title
            </h1>
            
            <!-- Clickable Author Avatar Pill -->
            <div class="pdp-author-pill-wrap" style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 14px;">
              <div id="pdpAuthorAvatar" style="width: 32px; height: 32px; border-radius: 50%; background: #FEF3C7; color: #B45309; font-weight: 700; font-size: 14px; display: flex; align-items: center; justify-content: center; border: 1px solid #FDE68A;">
                A
              </div>
              <span style="font-size: 14px; color: #475569;">
                Author: <a href="javascript:void(0)" id="pdpAuthorLink" onclick="window.openAuthorBooksPage(currentActivePdpBook ? currentActivePdpBook.author : '')" style="color: #09132C; font-weight: 700; text-decoration: underline;" title="View all books by this author">Author Name</a>
              </span>
            </div>

            <div class="pdp-price-wrap" style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
              <span id="pdpSellingPrice" class="pdp-selling-price" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 28px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
              <span style="font-size: 12px; color: #64748B;">(Inclusive of all taxes)</span>
            </div>

            <!-- Select Variant Box -->
            <div class="pdp-variant-selector-box" style="border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px; margin: 14px 0; background: #FFFFFF;">
              <div style="font-size: 11px; font-weight: 700; color: #0F172A; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em;">
                Select Variant / Format
              </div>
              <div id="pdpVariantButtons" style="display: flex; gap: 10px; flex-wrap: wrap;">
                <!-- Dynamic Variant Buttons generated via JS -->
              </div>
            </div>

            <!-- Live Stock Badge -->
            <div style="margin-bottom: 4px;">
              <span id="pdpStockBadge" style="display: inline-flex; align-items: center; gap: 6px; color: #16A34A; font-weight: 600; font-size: 13px;">
                <i data-lucide="check" style="width: 15px; height: 15px;"></i> In Stock
              </span>
            </div>
          </div>

          <!-- Interactive Description | Details Tabs -->
          <div class="pdp-tabs-container" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-top: 1px solid #F1F5F9; border-radius: 0 0 14px 14px; padding: 0 24px 22px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); margin-top: 0;">
            <div class="pdp-tab-nav" style="margin: 10px 0 14px;">
              <button type="button" class="pdp-tab-btn active" id="pdpTabDescBtn" onclick="switchPdpTab('desc')">Description</button>
              <button type="button" class="pdp-tab-btn" id="pdpTabDetailsBtn" onclick="switchPdpTab('details')">Details &amp; Specs</button>
            </div>

            <!-- Description Tab Pane -->
            <div id="pdpTabDescPane" class="pdp-tab-pane active" style="display: block;">
              <p id="pdpDescription" style="font-size: 14.5px; line-height: 1.7; color: #334155; margin: 0 0 14px;">
                Authentic publisher edition curated by Indigo Books India.
              </p>
              <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 16px; font-size: 12.5px; color: #64748B; line-height: 1.5; margin-bottom: 14px;">
                <strong>Publisher Note:</strong> Official certified release. Guaranteed original publisher paper stock and binding integrity. Shipped directly from Prayagraj Hub.
              </div>
              <!-- Key Highlights Feature Badges -->
              <div class="pdp-key-highlights" style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px; display: flex; align-items: center; gap: 6px; font-size: 11.5px; color: #334155;">
                  <i data-lucide="check-circle-2" style="width: 13px; height: 13px; color: #16A34A; flex-shrink: 0;"></i>
                  <span><strong>Complete Edition:</strong> Unabridged authentic text</span>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px; display: flex; align-items: center; gap: 6px; font-size: 11.5px; color: #334155;">
                  <i data-lucide="shield-check" style="width: 13px; height: 13px; color: #16A34A; flex-shrink: 0;"></i>
                  <span><strong>Publisher Archive:</strong> Guaranteed paper &amp; binding</span>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px; display: flex; align-items: center; gap: 6px; font-size: 11.5px; color: #334155;">
                  <i data-lucide="truck" style="width: 13px; height: 13px; color: #16A34A; flex-shrink: 0;"></i>
                  <span><strong>Priority Dispatch:</strong> Direct from Prayagraj Hub</span>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px; display: flex; align-items: center; gap: 6px; font-size: 11.5px; color: #334155;">
                  <i data-lucide="sparkles" style="width: 13px; height: 13px; color: #D99B26; flex-shrink: 0;"></i>
                  <span><strong>Indigo Certified:</strong> Hand-inspected copy</span>
                </div>
              </div>
            </div>

            <!-- Details Tab Pane (Complete CSV Technical Table) -->
            <div id="pdpTabDetailsPane" class="pdp-tab-pane" style="display: none;">
              <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; overflow: hidden;">
                <table class="pdp-tech-table" style="width: 100%; border-collapse: collapse; font-size: 13px;">
                  <tbody>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B; width: 38%;">Title:</th>
                      <td id="pdpSpecTitle" style="padding: 10px 14px; color: #0F172A; font-weight: 600;">Book Title</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Author:</th>
                      <td id="pdpSpecAuthor" style="padding: 10px 14px; color: #0F172A; font-weight: 600;">Author Name</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Publisher:</th>
                      <td id="pdpSpecPublisher" style="padding: 10px 14px; color: #0F172A;">Lokbharti Prakashan</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Binding / Format:</th>
                      <td id="pdpSpecBinding" style="padding: 10px 14px; color: #0F172A;">Paperback</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">ISBN-13 / SKU:</th>
                      <td id="pdpSpecIsbn" style="padding: 10px 14px; color: #0F172A; font-family: monospace; font-size: 13.5px;">9789389742152</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Number of Pages:</th>
                      <td id="pdpSpecPages" style="padding: 10px 14px; color: #0F172A;">312p</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Language:</th>
                      <td id="pdpSpecLanguage" style="padding: 10px 14px; color: #0F172A;">Hindi</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Edition / Year:</th>
                      <td id="pdpSpecEdition" style="padding: 10px 14px; color: #0F172A;">1st Edition</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Available Stock:</th>
                      <td id="pdpSpecQty" style="padding: 10px 14px; color: #059669; font-weight: 600;">In Stock • Ready to Dispatch</td>
                    </tr>
                    <tr>
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Dimensions (L &times; B &times; H):</th>
                      <td id="pdpSpecDimensions" style="padding: 10px 14px; color: #0F172A;">21.5 &times; 14.0 &times; 1.0 cm</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

        </div>

        <!-- RIGHT COLUMN: Delivery & Express Buy Box -->
        <div class="pdp-right-col">
          <div class="pdp-buy-box" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <div id="pdpBbPrice" class="pdp-bb-price" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 800; color: #0F172A; margin-bottom: 12px;">
              ₹299.00
            </div>
            
            <!-- Green Delivery Box -->
            <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 10px 12px; margin-bottom: 14px;">
              <div style="color: #16A34A; font-weight: 700; font-size: 13px; display: flex; align-items: center; gap: 6px;">
                <i data-lucide="truck" style="width: 16px; height: 16px;"></i> FREE DELIVERY
              </div>
              <div id="pdpEstimatedDeliveryDate" style="font-size: 13px; font-weight: 600; color: #0F172A; margin-top: 4px;">
                Delivery in 5 Business Days
              </div>
              <div style="font-size: 11.5px; color: #64748B; margin-top: 2px;">
                Order today for earliest dispatch from Prayagraj Hub
              </div>
            </div>

            <!-- Pincode & Live GPS Location Checker -->
            <div class="pdp-pincode-checker-box" style="margin-bottom: 16px;">
              <div style="font-size: 12px; color: #475569; display: flex; align-items: center; gap: 6px; margin-bottom: 8px;">
                <i data-lucide="map-pin" style="width: 14px; height: 14px; color: #0066B3;"></i> Add an address to check delivery availability
              </div>
              <div style="display: flex; gap: 8px;">
                <input type="text" id="pdpPincodeInput" placeholder="Enter 6-digit pincode" maxlength="6" style="flex: 1; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />
                <button type="button" onclick="window.checkPdpPincode()" style="background: #0F172A; color: #FFFFFF; border: none; border-radius: 6px; padding: 8px 14px; font-size: 12.5px; font-weight: 700; cursor: pointer;">
                  Check
                </button>
              </div>
              <div style="display: flex; align-items: center; gap: 10px; margin: 8px 0;">
                <div style="flex: 1; height: 1px; background: #E2E8F0;"></div>
                <span style="font-size: 10.5px; color: #94A3B8; text-transform: uppercase;">OR</span>
                <div style="flex: 1; height: 1px; background: #E2E8F0;"></div>
              </div>
              <button type="button" onclick="window.useLiveGpsLocation()" style="width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; background: #EFF6FF; border: 1px solid #BFDBFE; color: #1D4ED8; padding: 7px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer;">
                <i data-lucide="locate" style="width: 15px; height: 15px;"></i> Use current location
              </button>
              <div id="pdpPincodeStatus" style="font-size: 12px; margin-top: 8px; display: none;"></div>
            </div>

            <!-- Quantity Selector -->
            <div class="pdp-qty-row" style="margin-bottom: 14px;">
              <label class="pdp-qty-label" for="pdpQtyInput">Quantity:</label>
              <div class="pdp-qty-control">
                <button type="button" class="pdp-qty-btn" onclick="pdpQtyDecrease()">-</button>
                <input type="text" id="pdpQtyInput" value="1" readonly class="pdp-qty-input" />
                <button type="button" class="pdp-qty-btn" onclick="pdpQtyIncrease()">+</button>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="pdp-btn-stack" style="display: flex; flex-direction: column; gap: 8px;">
              <button type="button" class="pdp-btn-add-cart" onclick="pdpAddToCart()" style="background: #0F172A; color: #FFFFFF; padding: 11px; border: none; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <i data-lucide="shopping-bag" style="width: 16px; height: 16px;"></i> Add to Cart
              </button>
              <button type="button" class="pdp-btn-buy-now" onclick="pdpBuyNow()" style="background: #F59E0B; color: #0F172A; padding: 11px; border: none; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <i data-lucide="zap" style="width: 16px; height: 16px;"></i> Buy Now (1-Click Phone Checkout)
              </button>
              <button type="button" class="pdp-btn-wa-cod" onclick="pdpWhatsAppOrder()" style="background: #10B981; color: #FFFFFF; padding: 11px; border: none; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i> Order on WhatsApp COD
              </button>
            </div>

            <div class="pdp-bb-security" style="margin-top: 12px; text-align: center; font-size: 11.5px; color: #64748B; display: flex; align-items: center; justify-content: center; gap: 6px;">
              <i data-lucide="lock" style="width: 13px; height: 13px; color: #16A34A;"></i>
              <span>Secure 256-Bit Encrypted Ordering</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom: More Books by this Author Shelf -->
      <div class="pdp-recommendations-sec" style="margin-top: 24px; border-top: 1px solid #E2E8F0; padding-top: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 20px;">
          <div>
            <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
              AUTHOR PORTFOLIO
            </div>
            <h3 id="pdpAuthorShelfHeading" style="font-family: 'Merriweather', serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 0;">
              More Books by This Author
            </h3>
          </div>
          <a href="javascript:void(0)" onclick="window.openAuthorBooksPage(currentActivePdpBook ? currentActivePdpBook.author : '')" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none;">
            View Author Catalog &rarr;
          </a>
        </div>
        <div class="shelf-scroll-row" id="pdpAuthorShelfContainer">
          <!-- Dynamically populated by store_scripts.js -->
        </div>
      </div>

      </div>
  </div>

  <!-- =========================================================================
       11. GLOBAL FOOTER
       ========================================================================= -->
  <footer class="site-footer">
    <div class="site-container">
      
      <div class="footer-grid">
        
        <!-- Brand Summary -->
        <div>
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 354 352" width="40" height="40" class="indigo-emblem-svg shrink-0" style="width: 40px !important; height: 40px !important; max-width: 40px !important; max-height: 40px !important; min-width: 40px !important; min-height: 40px !important; display: inline-block !important; vertical-align: middle !important; flex-shrink: 0 !important; object-fit: contain !important;" fill="#0066B3" fill-rule="evenodd" aria-hidden="true"><path d="M 207 206 L 207 308 L 211 312 L 296 313 L 296 351 L 352 350 L 351 295 L 313 294 L 313 210 L 309 206 Z M 314 312 L 335 313 L 334 334 L 313 333 Z M 224 223 L 296 224 L 295 295 L 223 294 Z M 44 206 L 42 207 L 41 208 L 40 210 L 39 295 L 1 295 L 1 351 L 57 350 L 58 312 L 141 312 L 143 311 L 146 308 L 146 206 Z M 19 312 L 40 313 L 39 334 L 18 333 Z M 58 223 L 129 224 L 128 295 L 57 294 Z M 296 1 L 295 39 L 212 39 L 210 40 L 207 43 L 207 145 L 309 145 L 313 141 L 314 56 L 352 55 L 351 0 Z M 224 56 L 296 57 L 295 128 L 223 127 Z M 314 17 L 335 18 L 334 39 L 313 38 Z M 75 0 L 75 17 L 144 17 L 147 18 L 150 19 L 152 20 L 154 21 L 158 24 L 162 28 L 164 31 L 167 37 L 168 41 L 167 167 L 42 167 L 38 166 L 32 163 L 28 160 L 24 156 L 22 153 L 19 147 L 18 143 L 18 74 L 1 74 L 1 143 L 2 149 L 3 152 L 4 155 L 8 163 L 10 166 L 19 176 L 10 185 L 8 188 L 6 192 L 3 198 L 2 202 L 1 208 L 1 277 L 18 277 L 18 208 L 19 204 L 23 196 L 29 190 L 32 188 L 38 185 L 42 184 L 168 185 L 168 310 L 167 314 L 164 320 L 154 330 L 152 331 L 150 332 L 147 333 L 144 334 L 75 334 L 75 351 L 144 351 L 149 350 L 153 349 L 156 348 L 162 345 L 165 343 L 169 340 L 176 332 L 185 341 L 188 343 L 191 345 L 197 348 L 200 349 L 203 350 L 209 351 L 278 351 L 278 334 L 209 334 L 205 333 L 199 330 L 195 327 L 191 323 L 189 320 L 186 314 L 185 311 L 186 184 L 311 184 L 315 185 L 321 188 L 324 190 L 329 195 L 331 198 L 332 200 L 333 202 L 334 205 L 335 209 L 335 277 L 352 276 L 352 209 L 351 203 L 350 199 L 349 196 L 345 188 L 342 184 L 333 175 L 342 167 L 345 163 L 349 155 L 350 152 L 351 148 L 352 142 L 352 74 L 335 74 L 335 142 L 334 146 L 333 149 L 332 151 L 331 153 L 328 156 L 328 157 L 326 159 L 321 163 L 315 166 L 311 167 L 185 166 L 185 40 L 186 37 L 187 34 L 188 32 L 191 28 L 196 23 L 199 21 L 205 18 L 209 17 L 278 17 L 278 0 L 209 0 L 203 1 L 200 2 L 197 3 L 189 7 L 186 9 L 176 19 L 168 10 L 165 8 L 162 6 L 156 3 L 153 2 L 149 1 L 144 0 Z M 1 0 L 2 56 L 40 57 L 40 141 L 44 145 L 146 145 L 146 43 L 143 40 L 141 39 L 57 38 L 56 0 Z M 58 56 L 129 57 L 128 128 L 57 127 Z M 19 17 L 40 18 L 39 39 L 18 38 Z" /></svg>
            <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: 0.06em;">INDIGO BOOKS</span>
          </div>
          <p style="font-size: 13px; color: #94A3B8; line-height: 1.6; margin-bottom: 18px;">
            India's premier cultural bookstore rooted in Prayagraj. Over 5,500+ curated publisher editions covering Hindi fiction, Rekhta poetry, competitive law, and global literary masterpieces.
          </p>
          <div style="font-size: 12px; color: #64748B;">
            Headquarters: Prayagraj, Uttar Pradesh, India<br>
            Direct Desk: +91 8933063306<br>
            Email: info@indigobooks.com
          </div>
        </div>

        <!-- Curated Collections -->
        <div>
          <h4 class="footer-col-title">Literary Curations</h4>
          <ul class="footer-links-list">
            <li><a href="#bestsellers-podium" onclick="closeDedicatedProductPage()">Trending Top 5 Bestsellers</a></li>
            <li><a href="#mehfil-rekhta" onclick="closeDedicatedProductPage()">Mehfil-e-Rekhta Urdu Poetry</a></li>
            <li><a href="#contemporary-fiction" onclick="closeDedicatedProductPage()">Contemporary Hindi Classics</a></li>
            <li><a href="#law-academic-vault" onclick="closeDedicatedProductPage()">High Court &amp; Judiciary Treatises</a></li>
            <li><a href="#shop-all-catalog" onclick="closeDedicatedProductPage(); filterCatalog('all')">Pan-India 5,500+ Book Catalog</a></li>
          </ul>
        </div>

        <!-- Reader Support & Policies -->
        <div>
          <h4 class="footer-col-title">Customer Care</h4>
          <ul class="footer-links-list">
            <li><a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books!%20I%20would%20like%20to%20track%20my%20order." target="_blank">Track Your Order</a></li>
            <li><a href="https://wa.me/918933063306?text=What%20is%20the%20shipping%20time%20for%20my%20pincode?" target="_blank">Shipping &amp; Delivery Policy</a></li>
            <li><a href="https://wa.me/918933063306?text=I%20need%20help%20with%20a%20replacement%20or%20return." target="_blank">Easy Returns &amp; Replacements</a></li>
            <li><a href="https://wa.me/918933063306?text=Bulk%20School%20or%20Library%20order%20inquiry." target="_blank">Bulk / Library / School Orders</a></li>
            <li><a href="https://wa.me/918933063306?text=Hello!%20I%20have%20a%20question%20about%20Cash%20on%20Delivery." target="_blank">Cash on Delivery (COD) FAQ</a></li>
          </ul>
        </div>

        <!-- Instant WhatsApp Concierge -->
        <div>
          <h4 class="footer-col-title">WhatsApp Concierge</h4>
          <p style="font-size: 13px; color: #94A3B8; line-height: 1.6; margin-bottom: 16px;">
            Order any book or get personalized book suggestions directly on WhatsApp with our Prayagraj team.
          </p>
          <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books%20Prayagraj!%20I%20would%20like%20recommendations%20for%20reading." target="_blank" class="nav-whatsapp-btn" style="width: 100%; justify-content: center; padding: 12px 18px;">
            <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i>
            <span>Chat on WhatsApp (+91 8933063306)</span>
          </a>
        </div>

      </div>

      <div class="footer-bottom-row">
        <div>
          &copy; 2026 Indigo Books India (Prayagraj). All Rights Reserved. 100% Genuine Publisher Editions.
        </div>
        <div style="display: flex; gap: 16px;">
          <span>Privacy Policy</span>
          <span>Terms of Service</span>
          <span>COD Policy</span>
        </div>
      </div>

    </div>
  </footer>


  <!-- =========================================================================
       12. FLOATING WHATSAPP BUTTON (CONCIERGE)
       ========================================================================= -->
  <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books%20Prayagraj!%20I%20would%20like%20to%20inquire%20about%20a%20book." target="_blank" class="floating-wa-btn whatsapp-float-btn floating-whatsapp-btn" aria-label="Chat on WhatsApp">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #ffffff;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
    <span class="wa-tooltip">Order on WhatsApp</span>
  </a>


  <!-- =========================================================================
       13. SLIDE-OUT CART DRAWER
       ========================================================================= -->
  <div id="cartDrawerOverlay" class="cart-overlay" onclick="toggleCartDrawer(false)"></div>
  <aside id="cartDrawer" class="cart-drawer">
    <div class="cart-drawer-header">
      <div style="display: flex; align-items: center; gap: 8px;">
        <i data-lucide="shopping-bag" style="width: 18px; height: 18px; color: #0066B3;"></i>
        <h3 style="font-family: 'Merriweather', serif; font-size: 17px; font-weight: 700; color: #0F172A; margin: 0;">Reading Bag (<span id="cartItemCount">0</span>)</h3>
      </div>
      <button type="button" class="drawer-close-btn" onclick="toggleCartDrawer(false)" aria-label="Close Bag">
        <i data-lucide="x" style="width: 18px; height: 18px;"></i>
      </button>
    </div>

    <!-- Free Delivery Progress Bar -->
    <div style="background: #EFF6FF; padding: 12px 20px; border-bottom: 1px solid #DBEAFE;">
      <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; color: #1E40AF; margin-bottom: 6px;">
        <span id="freeShippingText">Add ₹999 for Free Express Dispatch</span>
        <span id="freeShippingPercent">0%</span>
      </div>
      <div style="width: 100%; height: 6px; background: #BFDBFE; border-radius: 999px; overflow: hidden;">
        <div id="freeShippingBar" style="width: 0%; height: 100%; background: #2563EB; transition: width 0.3s ease;"></div>
      </div>
    </div>

    <div class="cart-drawer-body" id="cartItemsContainer">
      <!-- Empty Bag Placeholder -->
      <div style="text-align: center; padding: 60px 20px; color: #94A3B8;">
        <i data-lucide="book-open" style="width: 48px; height: 48px; margin: 0 auto 12px; stroke-width: 1.5;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 16px; color: #0F172A; margin-bottom: 6px;">Your reading bag is empty</h4>
        <p style="font-size: 13px; color: #64748B;">Explore our 5,500+ curated books and add your next read.</p>
        <button type="button" class="hero-shop-btn" style="margin-top: 16px;" onclick="toggleCartDrawer(false); scrollToCatalog('all');">
          <span>Start Browsing &rarr;</span>
        </button>
      </div>
    </div>

    <div class="cart-drawer-footer" style="display: none;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
        <span style="font-size: 14px; font-weight: 600; color: #475569;">Subtotal:</span>
        <span id="cartDrawerSubtotal" style="font-size: 22px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹0.00</span>
      </div>

      <div style="display: flex; flex-direction: column; gap: 8px;">
        <button type="button" class="btn-checkout" onclick="proceedToCheckout()">
          <i data-lucide="credit-card" style="width: 16px; height: 16px;"></i>
          <span>Proceed to Checkout</span>
        </button>
        <button type="button" class="btn-wa-checkout" onclick="checkoutViaWhatsApp()">
          <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i>
          <span>Checkout via WhatsApp COD (+91 8933063306)</span>
        </button>
      </div>

      <div style="text-align: center; font-size: 11px; color: #94A3B8; margin-top: 12px;">
        100% Genuine Publisher Editions &bull; Same-Day Prayagraj Hub Dispatch
      </div>
    </div>
  </aside>


  <!-- =========================================================================
       14. UNIVERSAL MINI OVERVIEW MODAL (#indigo-overview-modal)
       ========================================================================= -->
  <div id="overviewModalOverlay" class="indigo-modal-overlay modal-overlay" onclick="if(event.target === this) window.closeAllIndigoModals()">
    <div class="overview-card-box" onclick="event.stopPropagation()">
      <button type="button" class="modal-close-btn" onclick="window.closeAllIndigoModals()" aria-label="Close Overview" style="position: absolute; top: 18px; right: 18px; background: #F1F5F9; border: none; border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #475569; z-index: 10;">
        <i data-lucide="x" style="width: 18px; height: 18px;"></i>
      </button>

      <!-- Left Column: High-Res Book Cover -->
      <div class="overview-cover-col" style="width: 100%;">
        <img id="modalCover" src="" alt="Book Cover" style="width: 100%; border-radius: 8px; box-shadow: 0 12px 28px rgba(0,0,0,0.18); object-fit: cover; aspect-ratio: 2/3; display: block;" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
      </div>

      <!-- Right Column: Solid White Content Pane -->
      <div class="overview-content-col" style="display: flex; flex-direction: column; height: 100%; box-sizing: border-box;">
        <div>
          <span id="modalBadge" style="display: inline-block; font-size: 11px; font-weight: 700; color: #B45309; background: #FEF3C7; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">
            HARDCOVER &bull; FICTION : NOVEL
          </span>
          <h3 id="modalTitle" style="font-family: 'Merriweather', Georgia, serif; font-size: 24px; font-weight: 700; color: #09132C; line-height: 1.3; margin: 0 0 6px;">
            Book Title
          </h3>
          <div id="modalAuthor" onclick="openAuthorBooksPage(this.textContent)" style="font-size: 14.5px; font-weight: 600; color: #B45309; cursor: pointer; margin-bottom: 14px;">
            Author Name
          </div>

          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
            <span id="modalPrice" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 24px; font-weight: 800; color: #09132C; font-variant-numeric: lining-nums tabular-nums !important;">₹695.00</span>
            
          </div>

          <!-- 2x2 Metadata Box -->
          <div class="overview-meta-box" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 14px 0;">
            <div>
              <strong style="color: #64748B; font-size: 11.5px; display: block; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">ISBN-13</strong>
              <span id="modalIsbn" style="font-size: 13px; font-weight: 600; color: #0F172A;">9789389742688</span>
            </div>
            <div>
              <strong style="color: #64748B; font-size: 11.5px; display: block; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Publisher</strong>
              <span id="modalPub" style="font-size: 13px; font-weight: 600; color: #0F172A;">Lokbharti Prakashan</span>
            </div>
            <div>
              <strong style="color: #64748B; font-size: 11.5px; display: block; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Length / Pages</strong>
              <span id="modalPages" style="font-size: 13px; font-weight: 600; color: #0F172A;">223p &bull; 300 g</span>
            </div>
            <div>
              <strong style="color: #64748B; font-size: 11.5px; display: block; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Language &amp; Edition</strong>
              <span id="modalLang" style="font-size: 13px; font-weight: 600; color: #0F172A;">Hindi &bull; 2nd (1931)</span>
            </div>
          </div>

          <!-- Literary Synopsis -->
          <p id="modalOverview" style="font-size: 13px; color: #334155; line-height: 1.6; margin: 12px 0 20px; max-height: 140px; overflow-y: auto;">
            Overview synopsis of the selected literary edition.
          </p>
        </div>

        <!-- 2 Action Buttons -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: auto;">
          <button type="button" id="modalFullPageBtn" class="btn-overview" style="background: #0066B3; color: #FFFFFF; justify-content: center; padding: 12px 18px; font-size: 13.5px; font-weight: 700; border-radius: 8px;" onclick="window.closeAllIndigoModals(); window.openSoloBookPage(currentModalBookId)">
            <span>Open Full Book Page &rarr;</span>
          </button>
          <button type="button" id="modalAddToCartBtn" class="btn-add-cart" style="justify-content: center; padding: 12px 18px; font-size: 13.5px; font-weight: 700; border-radius: 8px;" onclick="window.addToCart(window.currentModalBook || window.currentModalBookId); window.closeAllIndigoModals();">
            <i data-lucide="shopping-bag" style="width: 16px; height: 16px;"></i>
            <span>Add to Cart</span>
          </button>
        </div>
      </div>
    </div>
  </div>


  <!-- =========================================================================
       15. MEMBER SIGN IN & SIGN UP MODAL (#loginModalOverlay)
       ========================================================================= -->
  <div id="loginModalOverlay" class="modal-overlay indigo-modal-overlay" onclick="if(event.target === this) toggleLoginModal()">
    <div class="modal-card" style="background: #FFFFFF !important; color: #0F172A !important; border-radius: 16px !important; box-shadow: 0 24px 64px rgba(0, 0, 0, 0.45) !important; max-width: 440px !important; width: 100% !important; padding: 32px 28px !important; box-sizing: border-box !important; position: relative !important;" onclick="event.stopPropagation()">
      <button type="button" class="modal-close-btn" onclick="toggleLoginModal()" aria-label="Close" style="position: absolute; top: 16px; right: 16px; width: 32px; height: 32px; border-radius: 50%; background: #F1F5F9; border: 1px solid #CBD5E1; color: #475569; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>

      <!-- Modal Header -->
      <div style="text-align: center; margin-bottom: 20px;">
        <div style="width: 52px; height: 52px; background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px; color: #0066B3;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        </div>
        <h3 id="authModalTitle" style="font-family: 'Merriweather', serif; font-size: 20px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">Sign in to Indigo Books</h3>
        <p id="authModalSubtitle" style="font-size: 13px; color: #64748B; margin: 0;">Access your reading orders, wishlist, and scholar benefits.</p>
      </div>

      <!-- Tab Switcher: Sign In vs Join Book Club (Sign Up) -->
      <div style="display: flex; background: #F1F5F9; border-radius: 8px; padding: 4px; margin-bottom: 20px; gap: 4px;">
        <button type="button" id="tabAuthSignIn" onclick="switchAuthMode('signin')" style="flex: 1; padding: 8px 12px; font-size: 13px; font-weight: 700; border: none; border-radius: 6px; background: #FFFFFF; color: #0F172A; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.2s;">Sign In</button>
        <button type="button" id="tabAuthSignUp" onclick="switchAuthMode('signup')" style="flex: 1; padding: 8px 12px; font-size: 13px; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #64748B; cursor: pointer; transition: all 0.2s;">Join Book Club (Sign Up)</button>
      </div>

      <!-- Sign In Form -->
      <form id="authSignInForm" onsubmit="event.preventDefault(); alert('Welcome back to Indigo Books India! Your session is verified.'); toggleLoginModal();">
        <div style="margin-bottom: 14px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Email or Mobile Number</label>
          <input type="text" placeholder="name@domain.com or 10-digit mobile" required style="width: 100%; padding: 11px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <div style="margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <label style="font-size: 12px; font-weight: 700; color: #334155;">Password</label>
            <a href="javascript:void(0)" onclick="alert('Password reset link has been dispatched to your registered email/phone.')" style="font-size: 11.5px; color: #0066B3; text-decoration: none; font-weight: 600;">Forgot?</a>
          </div>
          <input type="password" placeholder="Enter your password" required style="width: 100%; padding: 11px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <button type="submit" style="width: 100%; justify-content: center; margin-bottom: 14px; background: #0066B3; color: #FFFFFF; padding: 12px; border-radius: 8px; font-weight: 700; font-size: 14px; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 12px rgba(0, 102, 179, 0.25);">
          Sign In to Your Account
        </button>
      </form>

      <!-- Sign Up Form (Initially hidden) -->
      <form id="authSignUpForm" style="display: none;" onsubmit="event.preventDefault(); alert('Welcome to Indigo Books Club! Your account has been registered with 5% scholar welcome credit.'); toggleLoginModal();">
        <div style="margin-bottom: 12px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Full Name</label>
          <input type="text" placeholder="e.g. Anand Kumar" required style="width: 100%; padding: 10px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <div style="margin-bottom: 12px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Mobile Number (for WhatsApp Updates)</label>
          <input type="tel" placeholder="10-digit mobile number" required style="width: 100%; padding: 10px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <div style="margin-bottom: 12px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Email Address</label>
          <input type="email" placeholder="name@domain.com" required style="width: 100%; padding: 10px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <div style="margin-bottom: 16px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Create Password</label>
          <input type="password" placeholder="At least 6 characters" required style="width: 100%; padding: 10px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <button type="submit" style="width: 100%; justify-content: center; margin-bottom: 14px; background: #D99B26; color: #09132C; padding: 12px; border-radius: 8px; font-weight: 700; font-size: 14px; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 12px rgba(217, 155, 38, 0.35);">
          Create Free Member Account &rarr;
        </button>
      </form>

      <div style="text-align: center; font-size: 12px; color: #64748B;">
        <span id="authSwitchPrompt">Don't have an account? <span onclick="switchAuthMode('signup')" style="color: #B45309; font-weight: 700; cursor: pointer; text-decoration: underline;">Join the Book Club</span></span>
      </div>
    </div>
  </div>


  <!-- =========================================================================
       16. 1-CLICK PHONE & GPS EXPRESS CHECKOUT MODAL (#expressPhoneCheckoutModal)
       ========================================================================= -->
  <div id="expressPhoneCheckoutModal" class="indigo-modal-overlay express-checkout-modal-backdrop" onclick="if(event.target === this) closeExpressPhoneCheckout()" style="display: none;">
    <div class="express-checkout-card" onclick="event.stopPropagation()">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 18px;">
        <div>
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em;">
            INSTANT DISPATCH &bull; NO SIGN-IN NEEDED
          </div>
          <h3 style="font-family: 'Merriweather', serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 4px 0 0;">
            1-Click Express Checkout
          </h3>
        </div>
        <button type="button" onclick="closeExpressPhoneCheckout()" style="background: none; border: none; font-size: 20px; color: #94A3B8; cursor: pointer; padding: 4px;">
          <i data-lucide="x" style="width: 20px; height: 20px;"></i>
        </button>
      </div>

      <form id="expressPhoneCheckoutForm" onsubmit="submitExpressPhoneOrder(event)">
        <!-- Phone Number -->
        <div style="margin-bottom: 14px;">
          <label style="display: block; font-size: 12.5px; font-weight: 700; color: #334155; margin-bottom: 6px;">
            Mobile Number (for Courier Tracking &amp; OTP-Free Confirmation)*
          </label>
          <div style="display: flex; gap: 8px;">
            <span style="display: flex; align-items: center; padding: 0 12px; background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px; font-weight: 600; color: #475569;">
              +91
            </span>
            <input type="tel" id="checkoutPhone" placeholder="Enter 10-digit mobile number" required pattern="[6-9][0-9]9" maxlength="10" style="flex: 1; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />
          </div>
        </div>

        <!-- Full Name -->
        <div style="margin-bottom: 14px;">
          <label style="display: block; font-size: 12.5px; font-weight: 700; color: #334155; margin-bottom: 6px;">
            Full Delivery Name*
          </label>
          <input type="text" id="checkoutName" placeholder="Recipient's Name" required style="width: 100%; box-sizing: border-box; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />
        </div>

        <!-- GPS Auto-fill Address Button -->
        <div style="margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <label style="font-size: 12.5px; font-weight: 700; color: #334155;">
              Delivery Address (House / Street / Area)*
            </label>
            <button type="button" onclick="useCheckoutGpsLocation()" style="background: none; border: none; color: #0066B3; font-size: 12px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 4px;">
              <i data-lucide="locate" style="width: 13px; height: 13px;"></i> Auto-detect with GPS
            </button>
          </div>
          <textarea id="checkoutAddress" rows="2" placeholder="House/Flat No., Building Name, Street, Landmark" required style="width: 100%; box-sizing: border-box; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13.5px; resize: vertical;"></textarea>
        </div>

        <!-- City & Pincode Grid -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
          <div>
            <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">City / District*</label>
            <input type="text" id="checkoutCity" placeholder="City" required style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />
          </div>
          <div>
            <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">PIN Code*</label>
            <input type="text" id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" required pattern="[1-9][0-9]5" style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />
          </div>
        </div>

        <!-- Payment Method Toggle -->
        <div style="margin-bottom: 20px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px;">
          <div style="font-size: 12px; font-weight: 700; color: #0F172A; margin-bottom: 8px; text-transform: uppercase;">
            Payment Method
          </div>
          <div style="display: flex; flex-direction: column; gap: 8px;">
            <label style="display: flex; align-items: center; gap: 10px; font-size: 13.5px; font-weight: 600; color: #0F172A; cursor: pointer;">
              <input type="radio" name="checkoutPayment" value="cod" checked style="accent-color: #0066B3;" />
              <span>Cash on Delivery (COD) &bull; <span style="color: #16A34A; font-weight: 700;">₹0 Extra Fee</span></span>
            </label>
            <label style="display: flex; align-items: center; gap: 10px; font-size: 13.5px; font-weight: 600; color: #0F172A; cursor: pointer;">
              <input type="radio" name="checkoutPayment" value="upi" style="accent-color: #0066B3;" />
              <span>Instant UPI / QR Code / Cards &bull; <span style="color: #64748B;">Secure Gateway</span></span>
            </label>
          </div>
        </div>

        <!-- Order Summary Strip -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-top: 1px solid #E2E8F0; margin-bottom: 16px;">
          <span style="font-size: 14px; color: #64748B;">Order Payable Total:</span>
          <span id="checkoutOrderTotal" style="font-size: 20px; font-weight: 800; color: #0F172A;">₹299.00</span>
        </div>

        <button type="submit" style="width: 100%; background: #0066B3; color: #FFFFFF; border: none; border-radius: 8px; padding: 14px; font-size: 15px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 14px rgba(0,102,179,0.3);">
          <span>Confirm &amp; Place Order &rarr;</span>
        </button>
      </form>
    </div>
  </div>

  <!-- 17. Order Confirmation Modal -->
  <div id="orderConfirmationModal" class="indigo-modal-overlay express-checkout-modal-backdrop" onclick="if(event.target === this) closeOrderConfirmationModal()" style="display: none;">
    <div class="express-checkout-card" style="text-align: center;" onclick="event.stopPropagation()">
      <div style="width: 54px; height: 54px; border-radius: 50%; background: #DCFCE7; color: #16A34A; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">
        <i data-lucide="check" style="width: 32px; height: 32px;"></i>
      </div>
      <div style="font-size: 11px; font-weight: 700; color: #16A34A; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
        ORDER CONFIRMED &bull; DISPATCH QUEUED
      </div>
      <h3 style="font-family: 'Merriweather', serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 0 0 10px;">
        Thank You for Your Order!
      </h3>
      <p id="orderConfirmText" style="font-size: 14px; color: #475569; line-height: 1.6; margin: 0 0 20px;">
        Your books are being carefully packed with protective bookstore packaging at our Prayagraj Central Hub.
      </p>
      <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px; margin-bottom: 20px; text-align: left;">
        <div style="font-size: 12px; color: #64748B;">Order Reference:</div>
        <div id="orderConfirmId" style="font-family: monospace; font-size: 16px; font-weight: 700; color: #0F172A; margin-top: 2px;">#IND-893306</div>
        <div style="font-size: 12px; color: #64748B; margin-top: 8px;">Estimated Dispatch:</div>
        <div style="font-size: 13.5px; font-weight: 600; color: #16A34A;">Same-Day via Express Pan-India Courier</div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 10px;">
        <a id="orderConfirmWaLink" href="https://wa.me/918933063306" target="_blank" style="background: #10B981; color: #FFFFFF; text-decoration: none; padding: 12px; border-radius: 8px; font-weight: 700; font-size: 13.5px; display: flex; align-items: center; justify-content: center; gap: 8px;">
          <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i> Track Order via WhatsApp (+91 8933063306)
        </a>
        <button type="button" onclick="closeOrderConfirmationModal()" style="background: #F1F5F9; border: 1px solid #CBD5E1; color: #0F172A; padding: 10px; border-radius: 8px; font-weight: 600; font-size: 13px; cursor: pointer;">
          Continue Browsing Bookstore
        </button>
      </div>
    </div>
  </div>


  <!-- =========================================================================
       18. JAVASCRIPT DATA & ENGINE
       ========================================================================= -->
                """

    bento_rendered = render_category_bento_showcase()
    body_str = body_str.replace('{render_category_bento_showcase()}', bento_rendered)

    script_content = f"""  <script>
    window.PODIUM_BOOKS = {podium_json};
    window.POET_SHAYARI_DATA = {poet_json};
    window.VAULT_BOOKS = {vault_json};
    window.CATEGORY_BENTO_DATA = {bento_json};
    window.CATALOG_BOOKS = {catalog_json};
    window.PIYUSH_MISHRA_BOOKS = {piyush_json};
    window.RAHI_MASOOM_RAZA_BOOKS = {rahi_json};
    window.MASTER_SEARCH_CATALOG = {master_search_json};
    window.MODAL_METADATA_DATABASE = {modal_meta_json};

    const PODIUM_BOOKS = window.PODIUM_BOOKS;
    const POET_SHAYARI_DATA = window.POET_SHAYARI_DATA;
    const VAULT_BOOKS = window.VAULT_BOOKS;
    const CATEGORY_BENTO_DATA = window.CATEGORY_BENTO_DATA;
    const CATALOG_BOOKS = window.CATALOG_BOOKS;
    const PIYUSH_MISHRA_BOOKS = window.PIYUSH_MISHRA_BOOKS;
    const RAHI_MASOOM_RAZA_BOOKS = window.RAHI_MASOOM_RAZA_BOOKS;
    const MASTER_SEARCH_CATALOG = window.MASTER_SEARCH_CATALOG;
    const MODAL_METADATA_DATABASE = window.MODAL_METADATA_DATABASE;

{UNIFIED_STORE_JS}

    function handleModalFullDetails() {{
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {{
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }}
    }}
  </script>
""" + "\n\n" + MASTER_STYLE + "\n\n" + MASTER_SCRIPT + "\n\n" + CYBER_STYLE + "\n\n" + CYBER_SCRIPT + "\n\n</body>\n</html>"

    html = head_str + UNIFIED_STORE_CSS + "\n</style>\n" + body_str + script_content
    return html

if __name__ == '__main__':
    h = build_preview_html()
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(h)
    print("Successfully generated preview.html, length:", len(h))
