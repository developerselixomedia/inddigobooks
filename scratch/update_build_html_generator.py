# -*- coding: utf-8 -*-
"""
scratch/update_build_html_generator.py
Rewrites build_html_generator.py with:
1. Removal of BUNDLE_BOOKS and #bundles-section
2. Update all numbers to 5,500+ (never 11,922+ or 11,900+)
3. Update all phone numbers to +91 8933063306 (never 8881122722)
4. Wrap homepage in #homepage-view
5. Add Amazon-Style #single-product-page-view container
6. Wire all book cards to /products/${handle} & handleBookAction
7. Exact CSV prices across Hero, Podium, Rekhta, Hindi Fiction, Vault, Catalog
"""

code = '''# -*- coding: utf-8 -*-
"""
build_html_generator.py
Assembles preview.html using data from store_data, store_styles, and store_scripts.
Ensures ZERO raw Liquid tags, ZERO Unicode emojis, and 100% exact CSV prices.
"""

import json
from store_data import (
    PODIUM_BOOKS,
    POET_SHAYARI_DATA,
    REKHTA_BOOKS,
    HINDI_FEATURE_BOOK,
    HINDI_GRID_BOOKS,
    VAULT_TABS,
    VAULT_BOOKS,
    CATALOG_BOOKS,
    MODAL_METADATA_DATABASE
)
from store_styles import UNIFIED_STORE_CSS
from store_scripts import UNIFIED_STORE_JS
from build_store_engine import (
    INDIGO_EMBLEM_SVG,
    HERO_TOPLEFT_WATERMARK_SVG,
    HERO_GEOMETRIC_RANGOLI_SVG,
    HERO_RANGOLI_SVG,
    STRING_LIGHTS_SVG,
    HERO_DIYAS_SVG,
    HERO_FLOOR_CURVE_SVG
)

def build_preview_html():
    podium_json = json.dumps(PODIUM_BOOKS, ensure_ascii=False)
    poet_json = json.dumps(POET_SHAYARI_DATA, ensure_ascii=False)
    vault_json = json.dumps(VAULT_BOOKS, ensure_ascii=False)
    catalog_json = json.dumps(CATALOG_BOOKS, ensure_ascii=False)
    modal_meta_json = json.dumps(MODAL_METADATA_DATABASE, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
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
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Complete Standard Production Stylesheet -->
  <style>
{UNIFIED_STORE_CSS}
  </style>
</head>
<body id="top">

  <!-- =========================================================================
       1. STICKY NAVBAR
       ========================================================================= -->
  <header class="site-navbar">
    <div class="site-container navbar-inner">
      
      <!-- Brand Identity -->
      <a href="#top" class="brand-link" onclick="closeDedicatedProductPage(); window.scrollTo({{top: 0, behavior: 'smooth'}});" aria-label="Indigo Books India Homepage">
        {INDIGO_EMBLEM_SVG}
        <div class="brand-wordmark">
          INDIGO BOOKS
          <span class="brand-submark">PRAYAGRAJ • INDIA</span>
        </div>
      </a>

      <!-- Navigation Tabs -->
      <ul class="nav-links-wrap">
        <li><a href="#top" class="nav-link-btn" onclick="closeDedicatedProductPage(); window.scrollTo({{top: 0, behavior: 'smooth'}})">Home</a></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('all')">Shop All (5,500+)</button></li>
        <li><a href="#bestsellers-podium" class="nav-link-btn" onclick="closeDedicatedProductPage(); document.getElementById('bestsellers-podium').scrollIntoView({{behavior: 'smooth'}})">Best Sellers</a></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('coming-soon')">Coming Soon</button></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('pre-order')">Pre-Order</button></li>
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
    <section class="hero-section" id="hero-section">
      <div class="hero-topleft-watermark">
        {HERO_TOPLEFT_WATERMARK_SVG}
      </div>

      {HERO_FLOOR_CURVE_SVG}
      {STRING_LIGHTS_SVG}
      {HERO_DIYAS_SVG}

      <div class="site-container hero-main-grid hero-inner-container ivh-container">
        
        <!-- Left Column -->
        <div class="hero-left-col">
          <h1>Discover Your Next<br>Favorite <em style="color: #E5A93C; font-style: italic; font-family: Georgia, serif;">Story</em></h1>
          <p>Explore India's largest online collection of bestsellers, regional gems, academic reads, and more.</p>
          
          <!-- Search Box -->
          <div class="hero-search-wrap">
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." onkeydown="handleHeroSearch(event)" />
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
          <div class="hero-rangoli-bg hero-rangoli-wrapper hero-wheel-wrap">
            {HERO_GEOMETRIC_RANGOLI_SVG}
          </div>

          <div class="hero-books-grid" id="heroBookGrid">
            
            <!-- Book 1: Godan (₹299.00) -->
            <div class="hero-book-card" data-hero-idx="0" onclick="handleBookAction('cat-book-1-9789389742152', '/products/godan-premchand', event)" title="View Godan by Premchand">
              <div class="hero-book-thumb">
                <img src="assets/hero-godan.jpg" alt="Godan (गोदान)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info">
                <div class="hero-book-title">Godan</div>
                <div class="hero-book-author">Premchand</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 2: Raag Darbari (₹499.00) -->
            <div class="hero-book-card" data-hero-idx="1" onclick="handleBookAction('cat-book-2-9788126713967', '/products/raag-darbari-shrilal-shukla', event)" title="View Raag Darbari by Shrilal Shukla">
              <div class="hero-book-thumb">
                <img src="assets/hero-raag-darbari.jpg" alt="Raag Darbari (राग दरबारी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info">
                <div class="hero-book-title">Raag Darbari</div>
                <div class="hero-book-author">Shrilal Shukla</div>
                <div class="hero-book-price">₹499.00</div>
              </div>
            </div>

            <!-- Book 3: Chitralekha (₹299.00) -->
            <div class="hero-book-card" data-hero-idx="2" onclick="handleBookAction('cat-book-3-9788126715855', '/products/chitralekha-bhagwaticharan-verma', event)" title="View Chitralekha by Bhagwaticharan Verma">
              <div class="hero-book-thumb">
                <img src="assets/hero-chitralekha.jpg" alt="Chitralekha (चित्रलेखा)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info">
                <div class="hero-book-title">Chitralekha</div>
                <div class="hero-book-author">Bhagwaticharan Verma</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 4: Rashmirathi (₹299.00) -->
            <div class="hero-book-card" data-hero-idx="3" onclick="handleBookAction('cat-book-4-9788180313639', '/products/rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar', event)" title="View Rashmirathi by Ramdhari Singh Dinkar">
              <div class="hero-book-thumb">
                <img src="assets/hero-rashmirathi.jpg" alt="Rashmirathi (रश्मिरथी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info">
                <div class="hero-book-title">Rashmirathi</div>
                <div class="hero-book-author">Ramdhari Singh Dinkar</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 5: Kuchh Ishq Kiya Kuchh Kaam Kiya (₹250.00) -->
            <div class="hero-book-card" data-hero-idx="4" onclick="handleBookAction('cat-book-5-9788126728435', '/products/kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra', event)" title="View Kuchh Ishq Kiya by Piyush Mishra">
              <div class="hero-book-thumb">
                <img src="assets/hero-kuchh-ishq.jpg" alt="Kuchh Ishq Kiya Kuchh Kaam Kiya" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info">
                <div class="hero-book-title">Kuchh Ishq Kiya</div>
                <div class="hero-book-author">Piyush Mishra</div>
                <div class="hero-book-price">₹250.00</div>
              </div>
            </div>

            <!-- Book 6: Gypsy (₹995.00) -->
            <div class="hero-book-card" data-hero-idx="5" onclick="handleBookAction('cat-book-6-9789352210046', '/products/gypsy-ila-chandra-joshi', event)" title="View Gypsy by Ila Chandra Joshi">
              <div class="hero-book-thumb">
                <img src="assets/hero-gypsy.jpg" alt="Gypsy (जिप्सी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info">
                <div class="hero-book-title">Gypsy</div>
                <div class="hero-book-author">Ila Chandra Joshi</div>
                <div class="hero-book-price">₹995.00</div>
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
        <span class="marquee-item">UPSC &amp; JUDICIARY SCHOLAR DISCOUNTS <span class="marquee-dot"></span></span>
        <span class="marquee-item">INSTANT WHATSAPP CONCIERGE +91 8933063306 <span class="marquee-dot"></span></span>
        <span class="marquee-item">SAMEDAY DISPATCH FROM PRAYAGRAJ <span class="marquee-dot"></span></span>
        <span class="marquee-item">100% AUTHENTIC PUBLISHER EDITIONS <span class="marquee-dot"></span></span>
        <span class="marquee-item">CASH ON DELIVERY PAN-INDIA <span class="marquee-dot"></span></span>
        <span class="marquee-item">SPECIAL REKHTA URDU POETRY ARCHIVE <span class="marquee-dot"></span></span>
        <span class="marquee-item">UPSC &amp; JUDICIARY SCHOLAR DISCOUNTS <span class="marquee-dot"></span></span>
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
                <img id="flankImgL2" src="{PODIUM_BOOKS[3]['coverUrl']}" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>

              <!-- Flanking Near-Left -->
              <div class="flank-book flank-left-1" onclick="selectPodiumByFlank(-1)" title="Click to view book">
                <img id="flankImgL1" src="{PODIUM_BOOKS[4]['coverUrl']}" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>

              <!-- Center Active 3D Book Hinge Structure -->
              <div id="podium-3d-book" class="podium-3d-book" onclick="togglePodiumCover(event)" title="Click or Hover to Open Cover">
                
                <!-- Stationary Inside Cream Page -->
                <div class="podium-inside-page">
                  <div class="podium-page-eyebrow">अध्याय १ • FIRST PAGE PREVIEW</div>
                  <div id="podium-page-title" class="podium-page-title">{PODIUM_BOOKS[0]['title']}</div>
                  <p id="podium-page-excerpt" class="podium-page-excerpt">{PODIUM_BOOKS[0]['firstPageExcerpt']}</p>
                  <div class="podium-page-footer">
                    <span style="font-weight: 700; color: #B45309;">— पृष्ठ १ —</span>
                    <span>Click to Toggle Cover</span>
                  </div>
                </div>

                <!-- Hinged Cover (Rotates to -135deg) -->
                <div class="podium-hinged-cover">
                  <!-- Front Face -->
                  <div class="cover-front">
                    <img id="podium-cover-img" src="{PODIUM_BOOKS[0]['coverUrl']}" alt="{PODIUM_BOOKS[0]['title']}" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                  <!-- Back Face -->
                  <div class="cover-back">
                    <div class="cover-back-thumb">
                      <img id="podium-inside-thumb" src="{PODIUM_BOOKS[0]['coverUrl']}" alt="Inside Cover" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                    </div>
                    <div id="podium-inside-title" class="cover-back-title">{PODIUM_BOOKS[0]['title']}</div>
                    <div id="podium-inside-author" class="cover-back-author">{PODIUM_BOOKS[0]['author']}</div>
                    <div class="cover-back-tag">Indigo Heritage Edition</div>
                  </div>
                </div>

              </div>

              <!-- Flanking Near-Right -->
              <div class="flank-book flank-right-1" onclick="selectPodiumByFlank(1)" title="Click to view book">
                <img id="flankImgR1" src="{PODIUM_BOOKS[1]['coverUrl']}" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>

              <!-- Flanking Far-Right -->
              <div class="flank-book flank-right-2" onclick="selectPodiumByFlank(2)" title="Click to view book">
                <img id="flankImgR2" src="{PODIUM_BOOKS[2]['coverUrl']}" alt="Flanking Book" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
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
            <div id="podiumSpotBadge" class="podium-cat-badge">{PODIUM_BOOKS[0]['badge']}</div>
            <div id="podiumSpotStock" class="podium-stock-str">
              <i data-lucide="check-circle" style="width: 14px; height: 14px; color: #059669;"></i>
              <span>{PODIUM_BOOKS[0]['stock']}</span>
            </div>
            <h3 id="podiumSpotHeading" class="podium-book-heading" style="cursor: pointer;" onclick="handleBookAction(PODIUM_BOOKS[currentPodiumIndex]['id'], '/products/' + PODIUM_BOOKS[currentPodiumIndex]['handle'], event)">{PODIUM_BOOKS[0]['title']}</h3>
            <div id="podiumSpotAuthor" class="podium-author-row">{PODIUM_BOOKS[0]['author']}</div>
            
            <div class="podium-rating-row">
              <div class="stars-group">
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
              </div>
              <span id="podiumSpotRating" style="font-size: 13px; font-weight: 600; color: #475569;">{PODIUM_BOOKS[0]['rating']}</span>
            </div>

            <blockquote id="podiumSpotQuote" class="podium-quote-box">
              "{PODIUM_BOOKS[0]['quote']}"
            </blockquote>

            <div class="podium-specs-grid">
              <div><strong>Format:</strong> <span id="podiumSpotPages">{PODIUM_BOOKS[0]['pages']}</span></div>
              <div><strong>Publisher:</strong> <span id="podiumSpotPublisher">{PODIUM_BOOKS[0]['publisher']}</span></div>
              <div><strong>Dispatch:</strong> <span style="color: #059669; font-weight: 700;">Same-Day Prayagraj</span></div>
              <div><strong>Payment:</strong> <span>Cash on Delivery Available</span></div>
            </div>

            <div class="podium-price-row">
              <span id="podiumSpotPrice" class="podium-curr-price">{PODIUM_BOOKS[0]['price']}</span>
              <span id="podiumSpotOldPrice" class="podium-old-price">{PODIUM_BOOKS[0]['oldPrice']}</span>
              <span id="podiumSpotDiscount" class="discount-pill">{PODIUM_BOOKS[0]['discount']}</span>
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
          <div id="rekhtaUrdu" class="couplet-urdu">{POET_SHAYARI_DATA['all']['couplets'][0]['urdu']}</div>
          <div id="rekhtaHindi" class="couplet-hindi">{POET_SHAYARI_DATA['all']['couplets'][0]['hindi']}</div>
          <div id="rekhtaEng" class="couplet-eng">{POET_SHAYARI_DATA['all']['couplets'][0]['eng']}</div>
          <div id="rekhtaAttr" class="couplet-attr">{POET_SHAYARI_DATA['all']['couplets'][0]['attr']}</div>

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
            {POET_SHAYARI_DATA['all']['couplets'][0]['ghazal']}
          </div>
        </div>

        <!-- 5 Authentic Rekhta Book Cards Below -->
        <div class="rekhta-books-grid">
          {"".join([f\'\'\'
          <div class="rekhta-book-card" data-poet="{b.get(\'poet\', \'all\')}" data-book-id="{b[\'id\']}">
            <div class="rekhta-cover-wrap" onclick="handleBookAction(\'{b[\'id\']}\', \'/products/{b.get(\'handle\', b[\'id\'])}\', event)" style="cursor: pointer;">
              <img src="{b[\'coverUrl\']}" alt="{b[\'title\']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/{b.get(\'handle\', b[\'id\'])}" onclick="handleBookAction(\'{b[\'id\']}\', \'/products/{b.get(\'handle\', b[\'id\'])}\', event)" style="color: inherit; text-decoration: none;">{b[\'title\']}</a>
            </h3>
            <div class="rekhta-card-author">{b[\'author\']}</div>
            <div class="rekhta-card-desc">{b[\'desc\']}</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">{b[\'price\']}</span>
              {f\'<span style="font-size: 12px; text-decoration: line-through; color: #64748B;">{b["oldPrice"]}</span>\' if b.get("oldPrice") else \'\'}
              {f\'<span class="discount-pill" style="font-size: 10px;">{b["discount"]}</span>\' if b.get("discount") and b.get("oldPrice") else \'\'}
            </div>
            <div class="rekhta-card-actions">
              <button type="button" class="btn-overview" onclick="handleBookAction(\'{b[\'id\']}\', \'/products/{b.get(\'handle\', b[\'id\'])}\', event)">
                <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
              </button>
              <button type="button" class="btn-add-cart" style="background: #D99B26; color: #0A1128;" onclick="addToCart(\'{b[\'id\']}\')">
                <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
              </button>
            </div>
          </div>
          \'\'\' for b in REKHTA_BOOKS])}
        </div>

      </div>
    </section>


    <!-- =========================================================================
         6. SECTION 3: INDIAN VOICES & CONTEMPORARY HINDI FICTION
         ========================================================================= -->
    <section id="contemporary-fiction" style="background: #FAF8F5;">
      <div class="site-container">
        
        <div class="editorial-header">
          <div>
            <div class="sec-overline">MODERN BHARAT FICTION</div>
            <h2>Indian Voices &amp; Contemporary Hindi Literature</h2>
            <p>Compelling storytellers reflecting the soul, complexities, and evolving identity of modern India.</p>
          </div>
        </div>

        <div class="contemporary-grid">
          
          <!-- Left Feature Card -->
          <div class="feat-book-card">
            <div class="feat-cover-wrap" onclick="handleBookAction(\'{HINDI_FEATURE_BOOK[\'id\']}\', \'/products/{HINDI_FEATURE_BOOK.get(\'handle\', HINDI_FEATURE_BOOK[\'id\'])}\', event)" style="cursor: pointer;">
              <img src="{HINDI_FEATURE_BOOK[\'coverUrl\']}" alt="{HINDI_FEATURE_BOOK[\'title\']}" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <div class="feat-card-body">
              <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 6px;">
                {HINDI_FEATURE_BOOK[\'badge\']}
              </div>
              <h3 style="font-family: \'Merriweather\', Georgia, serif; font-size: 24px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">
                <a href="/products/{HINDI_FEATURE_BOOK.get(\'handle\', HINDI_FEATURE_BOOK[\'id\'])}" onclick="handleBookAction(\'{HINDI_FEATURE_BOOK[\'id\']}\', \'/products/{HINDI_FEATURE_BOOK.get(\'handle\', HINDI_FEATURE_BOOK[\'id\'])}\', event)" style="color: inherit; text-decoration: none;">{HINDI_FEATURE_BOOK[\'title\']}</a>
              </h3>
              <div style="font-size: 14px; color: #64748B; margin-bottom: 12px;">{HINDI_FEATURE_BOOK[\'author\']}</div>
              <p style="font-size: 13.5px; color: #334155; line-height: 1.6; font-style: italic; margin-bottom: 16px;">
                "{HINDI_FEATURE_BOOK[\'quote\']}"
              </p>
              <div style="font-size: 12px; color: #64748B; margin-bottom: 20px;">
                {HINDI_FEATURE_BOOK[\'specs\']}
              </div>
              
              <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 20px;">
                <span style="font-size: 28px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{HINDI_FEATURE_BOOK[\'price\']}</span>
                {f\'<span style="font-size: 14px; text-decoration: line-through; color: #94A3B8;">{HINDI_FEATURE_BOOK["oldPrice"]}</span>\' if HINDI_FEATURE_BOOK.get("oldPrice") else \'\'}
                {f\'<span class="discount-pill">{HINDI_FEATURE_BOOK["discount"]}</span>\' if HINDI_FEATURE_BOOK.get("discount") and HINDI_FEATURE_BOOK.get("oldPrice") else \'\'}
              </div>

              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <button type="button" class="btn-overview" onclick="handleBookAction(\'{HINDI_FEATURE_BOOK[\'id\']}\', \'/products/{HINDI_FEATURE_BOOK.get(\'handle\', HINDI_FEATURE_BOOK[\'id\'])}\', event)">
                  <i data-lucide="book-open" style="width: 15px; height: 15px;"></i> View Details
                </button>
                <button type="button" class="btn-add-cart" onclick="addToCart(\'{HINDI_FEATURE_BOOK[\'id\']}\')">
                  <i data-lucide="shopping-bag" style="width: 15px; height: 15px;"></i> Add to Cart
                </button>
              </div>
            </div>
          </div>

          <!-- Right 2x2 Grid: Compact Cards -->
          <div class="mini-grid-2x2">
            {"".join([f\'\'\'
            <div class="mini-book-card">
              <div class="mini-cover-row">
                <div class="mini-book-thumb" onclick="handleBookAction(\'{item[\'id\']}\', \'/products/{item.get(\'handle\', item[\'id\'])}\', event)" style="cursor: pointer;">
                  <img src="{item[\'coverUrl\']}" alt="{item[\'title\']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                </div>
                <div class="mini-details-col">
                  <div>
                    <h3 class="mini-book-title">
                      <a href="/products/{item.get(\'handle\', item[\'id\'])}" onclick="handleBookAction(\'{item[\'id\']}\', \'/products/{item.get(\'handle\', item[\'id\'])}\', event)" style="color: inherit; text-decoration: none;">{item[\'title\']}</a>
                    </h3>
                    <div class="mini-book-author">{item[\'author\']}</div>
                  </div>
                  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 8px;">
                    <span style="font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{item[\'price\']}</span>
                    {f\'<span style="font-size: 11.5px; text-decoration: line-through; color: #94A3B8;">{item["oldPrice"]}</span>\' if item.get("oldPrice") else \'\'}
                  </div>
                </div>
              </div>
              <p style="font-size: 11.5px; color: #64748B; line-height: 1.5; margin: 4px 0 8px;">
                {item[\'desc\']}
              </p>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
                <button type="button" class="btn-overview" style="padding: 8px 10px; font-size: 12px;" onclick="handleBookAction(\'{item[\'id\']}\', \'/products/{item.get(\'handle\', item[\'id\'])}\', event)">
                  <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Details
                </button>
                <button type="button" class="btn-add-cart" style="padding: 8px 10px; font-size: 12px;" onclick="addToCart(\'{item[\'id\']}\')">
                  <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> Add
                </button>
              </div>
            </div>
            \'\'\' for item in HINDI_GRID_BOOKS])}
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
              <h4 style="font-family: \'Merriweather\', Georgia, serif; font-size: 15px; font-weight: 700; color: #92400E; margin-bottom: 6px;">
                Institutional / High Court Orders
              </h4>
              <p style="font-size: 12.5px; color: #78350F; line-height: 1.5; margin-bottom: 12px;">
                Special discounts and invoice billing for Bar Council members, Law Chambers, and University Libraries.
              </p>
              <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books!%20I%20represent%20an%20institution/law%20firm%20and%20need%20bulk%20procurement." target="_blank" style="display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 700; color: #B45309; text-decoration: none;">
                <i data-lucide="message-circle" style="width: 15px; height: 15px;"></i> Contact Institutional Desk &rarr;
              </a>
            </div>
          </div>

          <!-- Right Pane: 2x2 Grid of 4 Books -->
          <div class="vault-cards-grid" id="vaultCardsContainer">
            {"".join([f\'\'\'
            <div class="vault-card">
              <div class="vault-card-thumb" onclick="handleBookAction(\'{b[\'id\']}\', \'/products/{b.get(\'handle\', b[\'id\'])}\', event)" style="cursor: pointer;">
                <img referrerpolicy="no-referrer" src="{b[\'coverUrl\']}" alt="{b[\'title\']}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
              </div>
              <div class="vault-card-body">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                  {b[\'badge\']}
                </div>
                <h3 style="font-family: \'Merriweather\', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
                  <a href="/products/{b.get(\'handle\', b[\'id\'])}" onclick="handleBookAction(\'{b[\'id\']}\', \'/products/{b.get(\'handle\', b[\'id\'])}\', event)" style="color: inherit; text-decoration: none;">{b[\'title\']}</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
                  {b[\'author\']}
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{b[\'price\']}</span>
                  {f\'<span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">{b["oldPrice"]}</span>\' if b.get("oldPrice") else \'\'}
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button type="button" class="btn-overview" onclick="handleBookAction(\'{b[\'id\']}\', \'/products/{b.get(\'handle\', b[\'id\'])}\', event)">
                    <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Details
                  </button>
                  <button type="button" class="btn-add-cart" onclick="addToCart(\'{b[\'id\']}\')">
                    <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
                  </button>
                </div>
              </div>
            </div>
            \'\'\' for b in VAULT_BOOKS[\'law\']])}
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
          <a href="#shop-all-catalog" onclick="filterCatalog('all')" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none; align-self: flex-end; padding-bottom: 8px;">
            Browse All 5,500+ Books &rarr;
          </a>
        </div>

        <!-- Faceted Category Filter Pills -->
        <div class="catalog-filter-bar">
          <div class="catalog-filter-pills" id="catalogCategoryPills">
            <button type="button" class="cat-pill active" data-cat="all" onclick="filterCatalog('all')">All Books (5,500+)</button>
            <button type="button" class="cat-pill" data-cat="coming-soon" onclick="filterCatalog('coming-soon')">Coming Soon</button>
            <button type="button" class="cat-pill" data-cat="pre-order" onclick="filterCatalog('pre-order')">Pre-Order Special</button>
            <button type="button" class="cat-pill" data-cat="bestseller" onclick="filterCatalog('bestseller')">Top Bestsellers</button>
            <button type="button" class="cat-pill" data-cat="rekhta" onclick="filterCatalog('rekhta')">Rekhta &amp; Poetry</button>
            <button type="button" class="cat-pill" data-cat="hindi" onclick="filterCatalog('hindi')">Contemporary Hindi Fiction</button>
            <button type="button" class="cat-pill" data-cat="law" onclick="filterCatalog('law')">Law &amp; Judiciary</button>
          </div>

          <!-- Real-Time Search Bar -->
          <div class="catalog-search-wrap">
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value)" />
          </div>
        </div>

        <!-- 4-Column Responsive Grid of Books -->
        <div class="catalog-cards-grid" id="catalogGridContainer">
          <!-- Rendered by store_scripts.js -->
        </div>

      </div>
    </section>


    <!-- =========================================================================
         9. SECTION 6: 4-CARD TRUST FEATURES STRIP
         ========================================================================= -->
    <section style="background: #FFFFFF; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; padding: 48px 0 !important;">
      <div class="site-container trust-strip-grid trust-features-grid features-grid">
        
        <div class="trust-card">
          <div class="trust-card-icon">
            <i data-lucide="shield-check" style="width: 22px; height: 22px;"></i>
          </div>
          <h4 style="font-family: \'Merriweather\', serif; font-size: 16px; font-weight: 700; color: #0F172A;">100% Authentic Editions</h4>
          <p style="font-size: 12.5px; color: #64748B; line-height: 1.5;">Direct partnerships with official publishers like Vani, Rajkamal, Rekhta, Penguin, and LexisNexis.</p>
        </div>

        <div class="trust-card">
          <div class="trust-card-icon">
            <i data-lucide="message-circle" style="width: 22px; height: 22px;"></i>
          </div>
          <h4 style="font-family: \'Merriweather\', serif; font-size: 16px; font-weight: 700; color: #0F172A;">Instant WhatsApp COD</h4>
          <p style="font-size: 12.5px; color: #64748B; line-height: 1.5;">Order any title in 1-click via WhatsApp (+91 8933063306) with Cash on Delivery across 19,000+ pin codes.</p>
        </div>

        <div class="trust-card">
          <div class="trust-card-icon">
            <i data-lucide="truck" style="width: 22px; height: 22px;"></i>
          </div>
          <h4 style="font-family: \'Merriweather\', serif; font-size: 16px; font-weight: 700; color: #0F172A;">Pan-India Express Dispatch</h4>
          <p style="font-size: 12.5px; color: #64748B; line-height: 1.5;">Same-day dispatch from our central Prayagraj hub with live courier tracking delivered right to your door.</p>
        </div>

        <div class="trust-card">
          <div class="trust-card-icon">
            <i data-lucide="heart" style="width: 22px; height: 22px;"></i>
          </div>
          <h4 style="font-family: \'Merriweather\', serif; font-size: 16px; font-weight: 700; color: #0F172A;">Cultural Book Community</h4>
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
            <h2 style="font-family: \'Merriweather\', Georgia, serif; font-size: 28px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 16px;">
              The Sacred Sangam of Indian Literature &amp; Legal Thought
            </h2>
            <p style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 16px;">
              Indigo Books India is rooted in the historic literary city of Prayagraj—the cultural crossroads of the Hindi belt and Urdu poetry. We provide over 5,500+ authentic publisher editions ranging from timeless Rekhta poetry and contemporary Indian fiction to university legal treatises and competitive examination archives.
            </p>
            <p style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 24px;">
              From the High Court of Judicature at Allahabad to the storied halls of Allahabad University, we take pride in serving India\'s finest advocates, professors, civil service aspirants, and discerning bibliophiles.
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
            <h3 style="font-family: \'Merriweather\', Georgia, serif; font-size: 20px; font-weight: 700; color: #0F172A; margin-bottom: 14px;">
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
       DEDICATED AMAZON-STYLE SINGLE PRODUCT PAGE VIEW (#single-product-page-view)
       ========================================================================= -->
  <div id="single-product-page-view" class="store-view-section" style="display: none; background: #FAF8F5;">
    <div class="product-page-wrapper">
      
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

      <!-- 3-Column Amazon-Style Grid -->
      <div class="product-pdp-grid">
        
        <!-- LEFT COLUMN: Sticky Book Cover & Preview Excerpt -->
        <div class="pdp-left-col">
          <div class="pdp-cover-card">
            <div class="pdp-cover-img-wrap">
              <img id="pdpMainCoverImg" src="" alt="Book Cover" class="pdp-cover-img" referrerpolicy="no-referrer" />
            </div>

            <button type="button" class="pdp-look-inside-btn" onclick="togglePdpLookInside()">
              <i data-lucide="book-open" style="width: 16px; height: 16px;"></i> Look Inside / First Page Excerpt
            </button>

            <!-- Collapsible First Page Excerpt Box -->
            <div id="pdpExcerptBox" class="pdp-excerpt-box">
              <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 6px;">
                अध्याय १ • FIRST PAGE PREVIEW
              </div>
              <p id="pdpExcerptText" style="margin: 0; font-size: 13.5px; line-height: 1.7; color: #334155;">
                Loading preview excerpt...
              </p>
            </div>

            <!-- Trust Perks -->
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

        <!-- CENTER COLUMN: Editorial Description & Technical Specifications -->
        <div class="pdp-center-col">
          <span id="pdpGenreTag" class="pdp-genre-pill">NATIONAL BESTSELLER</span>
          <h1 id="pdpTitle" class="pdp-book-title">Book Title</h1>
          
          <div class="pdp-author-row">
            By <strong id="pdpAuthor">Author Name</strong> &bull; Authorized Indian Edition
          </div>

          <div class="pdp-rating-row">
            <div class="pdp-stars">
              <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
              <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
              <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
              <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
              <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
            </div>
            <span class="pdp-rating-text">4.9 / 5.0 (12,840 verified readers)</span>
          </div>

          <div class="pdp-price-wrap">
            <span id="pdpSellingPrice" class="pdp-selling-price">₹299.00</span>
            <span id="pdpComparePrice" class="pdp-compare-price">₹400.00</span>
            <span id="pdpDiscountBadge" class="pdp-discount-badge">25% OFF</span>
            <span style="font-size: 12px; color: #64748B; margin-left: 4px;">(Inclusive of all taxes)</span>
          </div>

          <div class="pdp-format-row">
            <div class="pdp-format-label">Binding &amp; Format:</div>
            <div class="pdp-format-pill">
              <i data-lucide="book" style="width: 16px; height: 16px;"></i>
              <span id="pdpFormatPill">Paperback Edition</span>
            </div>
          </div>

          <div class="pdp-description-wrap">
            <h3 class="pdp-sec-heading">Editorial Overview &amp; Synopsis</h3>
            <p id="pdpDescription" class="pdp-description-text">
              Authentic publisher edition curated by Indigo Books India.
            </p>
          </div>

          <!-- Technical Metadata Table -->
          <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 20px;">
            <h4 style="font-family: \'Merriweather\', serif; font-size: 15px; font-weight: 700; color: #0F172A; margin: 0 0 12px;">
              Bibliographic Details
            </h4>
            <table class="pdp-tech-table">
              <tbody>
                <tr>
                  <th>ISBN-13 / SKU:</th>
                  <td id="pdpSpecIsbn">978-0143453987</td>
                </tr>
                <tr>
                  <th>Publisher:</th>
                  <td id="pdpSpecPublisher">Lokbharti / Rajkamal Prakashan</td>
                </tr>
                <tr>
                  <th>Pages / Format:</th>
                  <td id="pdpSpecPages">320 Pages • Standard Print</td>
                </tr>
                <tr>
                  <th>Language:</th>
                  <td id="pdpSpecLanguage">Hindi (देवनागरी) / English</td>
                </tr>
                <tr>
                  <th>Dispatch Hub:</th>
                  <td id="pdpSpecDispatch">Prayagraj, Uttar Pradesh (Same-Day)</td>
                </tr>
              </tbody>
            </table>
          </div>

        </div>

        <!-- RIGHT COLUMN: Amazon-Style Sticky Buy Box -->
        <div class="pdp-right-col">
          <div class="pdp-buy-box">
            <div id="pdpBbPrice" class="pdp-bb-price">₹299.00</div>
            
            <div class="pdp-bb-stock">
              <i data-lucide="check-circle" style="width: 16px; height: 16px;"></i>
              <span>In Stock • Ready to Dispatch</span>
            </div>

            <div class="pdp-bb-delivery">
              Delivery to your location within <strong>2-5 Business Days</strong> via Express Courier.
            </div>

            <!-- Quantity Selector -->
            <div class="pdp-qty-row">
              <label class="pdp-qty-label" for="pdpQtyInput">Quantity:</label>
              <div class="pdp-qty-control">
                <button type="button" class="pdp-qty-btn" onclick="pdpQtyDecrease()">-</button>
                <input type="text" id="pdpQtyInput" value="1" readonly class="pdp-qty-input" />
                <button type="button" class="pdp-qty-btn" onclick="pdpQtyIncrease()">+</button>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="pdp-btn-stack">
              <button type="button" class="pdp-btn-add-cart" onclick="pdpAddToCart()">
                <i data-lucide="shopping-bag" style="width: 16px; height: 16px;"></i> Add to Cart
              </button>
              <button type="button" class="pdp-btn-buy-now" onclick="pdpBuyNow()">
                <i data-lucide="zap" style="width: 16px; height: 16px;"></i> Buy Now (Instant Checkout)
              </button>
              <button type="button" class="pdp-btn-wa-cod" onclick="pdpWhatsAppOrder()">
                <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i> Order via WhatsApp COD
              </button>
            </div>

            <div class="pdp-bb-security">
              <i data-lucide="lock" style="width: 13px; height: 13px; color: #16A34A;"></i>
              <span>Secure 256-Bit Encrypted Ordering</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom: Similar Books Row -->
      <div class="pdp-recommendations-sec">
        <h3 style="font-family: \'Merriweather\', serif; font-size: 22px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">
          Readers Also Bought / Similar Books in This Category
        </h3>
        <p style="font-size: 13.5px; color: #64748B; margin: 0 0 20px;">
          Curated literature often ordered together with this title.
        </p>
        <div class="pdp-rec-grid" id="pdpRecContainer">
          <!-- Rendered by JS -->
        </div>
      </div>

    </div>
  </div><!-- /#single-product-page-view -->


  <!-- =========================================================================
       11. GLOBAL FOOTER
       ========================================================================= -->
  <footer class="site-footer">
    <div class="site-container">
      
      <div class="footer-grid">
        
        <!-- Brand Summary -->
        <div>
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
            {INDIGO_EMBLEM_SVG}
            <span style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: 0.06em;">INDIGO BOOKS</span>
          </div>
          <p style="font-size: 13px; color: #94A3B8; line-height: 1.6; margin-bottom: 18px;">
            India\'s premier cultural bookstore rooted in Prayagraj. Over 5,500+ curated publisher editions covering Hindi fiction, Rekhta poetry, competitive law, and global literary masterpieces.
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
            <li><a href="#shop-all-catalog" onclick="closeDedicatedProductPage(); filterCatalog(\'all\')">Pan-India 5,500+ Book Catalog</a></li>
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
    <i data-lucide="message-circle" style="width: 28px; height: 28px;"></i>
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
        <h3 style="font-family: \'Merriweather\', serif; font-size: 17px; font-weight: 700; color: #0F172A; margin: 0;">Reading Bag (<span id="cartItemCount">0</span>)</h3>
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
        <h4 style="font-family: \'Merriweather\', serif; font-size: 16px; color: #0F172A; margin-bottom: 6px;">Your reading bag is empty</h4>
        <p style="font-size: 13px; color: #64748B;">Explore our 5,500+ curated books and add your next read.</p>
        <button type="button" class="hero-shop-btn" style="margin-top: 16px;" onclick="toggleCartDrawer(false); scrollToCatalog(\'all\');">
          <span>Start Browsing &rarr;</span>
        </button>
      </div>
    </div>

    <div class="cart-drawer-footer">
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
       14. UNIVERSAL MINI OVERVIEW MODAL
       ========================================================================= -->
  <div id="overviewModalOverlay" class="modal-overlay" onclick="closeOverviewModal()">
    <div class="modal-card" onclick="event.stopPropagation()">
      <button type="button" class="modal-close-btn" onclick="closeOverviewModal()" aria-label="Close Overview">
        <i data-lucide="x" style="width: 18px; height: 18px;"></i>
      </button>

      <div class="modal-grid">
        <div class="modal-cover-col">
          <img id="modalCover" src="" alt="Book Cover" style="width: 100%; height: 100%; object-fit: cover;" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
        </div>

        <div class="modal-details-col">
          <div id="modalBadge" style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
            EXCLUSIVE EDITION
          </div>
          <h3 id="modalTitle" style="font-family: \'Merriweather\', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
            Book Title
          </h3>
          <div id="modalAuthor" style="font-size: 13.5px; color: #64748B; margin-bottom: 12px;">
            Author Name
          </div>

          <div style="display: flex; align-items: baseline; gap: 8px; margin-bottom: 16px;">
            <span id="modalPrice" style="font-size: 22px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            <span id="modalMrp" style="font-size: 13px; text-decoration: line-through; color: #94A3B8; font-variant-numeric: lining-nums tabular-nums !important;">₹399.00</span>
            <span id="modalDiscount" class="discount-pill" style="font-size: 11px;">25% OFF</span>
          </div>

          <div class="modal-specs-table">
            <div><strong>ISBN:</strong> <span id="modalIsbn">978-XXXXXXXXXX</span></div>
            <div><strong>Publisher:</strong> <span id="modalPub">Lokbharti / Rajkamal</span></div>
            <div><strong>Pages:</strong> <span id="modalPages">320 Pages</span></div>
            <div><strong>Language:</strong> <span id="modalLang">Hindi / English</span></div>
          </div>

          <p id="modalOverview" style="font-size: 13px; color: #334155; line-height: 1.6; margin-bottom: 16px; max-height: 120px; overflow-y: auto;">
            Overview summary of the selected book.
          </p>

          <ul id="modalHighlights" class="modal-highlights-list">
            <!-- Highlights inserted via JS -->
          </ul>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 20px;">
            <button type="button" class="btn-overview" style="background: #0066B3; color: #FFFFFF;" onclick="handleModalFullDetails()">
              <i data-lucide="external-link" style="width: 15px; height: 15px;"></i> Full Page
            </button>
            <button type="button" class="btn-add-cart" id="modalAddToCartBtn">
              <i data-lucide="shopping-bag" style="width: 15px; height: 15px;"></i> Add to Cart
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>


  <!-- =========================================================================
       15. MEMBER SIGN IN MODAL
       ========================================================================= -->
  <div id="loginModalOverlay" class="modal-overlay" onclick="toggleLoginModal()">
    <div class="modal-card" style="max-width: 420px; padding: 32px;" onclick="event.stopPropagation()">
      <button type="button" class="modal-close-btn" onclick="toggleLoginModal()" aria-label="Close">
        <i data-lucide="x" style="width: 18px; height: 18px;"></i>
      </button>

      <div style="text-align: center; margin-bottom: 24px;">
        <div style="width: 48px; height: 48px; background: #EFF6FF; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px; color: #0066B3;">
          <i data-lucide="user" style="width: 24px; height: 24px;"></i>
        </div>
        <h3 style="font-family: \'Merriweather\', serif; font-size: 20px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">Sign in to Indigo Books</h3>
        <p style="font-size: 13px; color: #64748B; margin: 0;">Access your reading orders, wishlist, and scholar benefits.</p>
      </div>

      <form onsubmit="event.preventDefault(); alert(\'Welcome back to Indigo Books India! Your session is verified.\'); toggleLoginModal();">
        <div style="margin-bottom: 14px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 4px;">Email or Mobile Number</label>
          <input type="text" placeholder="name@domain.com or 10-digit mobile" required style="width: 100%; padding: 10px 14px; font-size: 13px; border: 1px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box;" />
        </div>
        <div style="margin-bottom: 20px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 4px;">Password</label>
          <input type="password" placeholder="Enter your password" required style="width: 100%; padding: 10px 14px; font-size: 13px; border: 1px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box;" />
        </div>
        <button type="submit" class="btn-checkout" style="width: 100%; justify-content: center; margin-bottom: 14px;">
          Sign In
        </button>
      </form>

      <div style="text-align: center; font-size: 12px; color: #64748B;">
        Don\'t have an account? <span style="color: #B45309; font-weight: 700; cursor: pointer;">Join the Book Club</span>
      </div>
    </div>
  </div>


  <!-- =========================================================================
       16. JAVASCRIPT DATA & ENGINE
       ========================================================================= -->
  <script>
    const PODIUM_BOOKS = {podium_json};
    const POET_SHAYARI_DATA = {poet_json};
    const VAULT_BOOKS = {vault_json};
    const CATALOG_BOOKS = {catalog_json};
    const MODAL_METADATA_DATABASE = {modal_meta_json};

{UNIFIED_STORE_JS}

    function handleModalFullDetails() {{
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {{
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }}
    }}
  </script>

</body>
</html>"""

    return html

print("build_html_generator.py ready.")
'''

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_html_generator.py written successfully!")

