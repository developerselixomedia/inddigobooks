# -*- coding: utf-8 -*-
"""
scratch/insert_shelves_and_modals.py
Inserts Category Promo Banners, 3 Category Shelves, upgraded Solo Product Page,
and Express Phone Checkout Modal into build_html_generator.py.
"""

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Prepare Promo Banners & Shelves HTML block
shelves_insertion = """
    <!-- =========================================================================
         7A. CATEGORY DISCOVERY PROMO BANNERS (1340px Grid)
         ========================================================================= -->
    <section class="promo-banners-section">
      <div class="promo-banners-grid">
        
        <!-- Card 1: Navy -->
        <div class="promo-banner-card promo-banner-navy" onclick="scrollToCatalog('bestseller')">
          <div>
            <div class="promo-banner-subtitle">Exclusive collections</div>
            <h3 class="promo-banner-title">BEST SELLING BOOKS</h3>
          </div>
          <div class="promo-banner-cta">
            <span>Shop Now &rarr;</span>
          </div>
        </div>

        <!-- Card 2: Espresso -->
        <div class="promo-banner-card promo-banner-espresso" onclick="scrollToCatalog('pre-order')">
          <div>
            <div class="promo-banner-subtitle">Available shortly</div>
            <h3 class="promo-banner-title">PRE-ORDER &amp; NEW RELEASES</h3>
          </div>
          <div class="promo-banner-cta">
            <span>Explore Now &rarr;</span>
          </div>
        </div>

        <!-- Card 3: Forest -->
        <div class="promo-banner-card promo-banner-forest" onclick="scrollToCatalog('rekhta')">
          <div>
            <div class="promo-banner-subtitle">Hardcover &amp; Paperback</div>
            <h3 class="promo-banner-title">CLASSIC HINDI &amp; URDU LITERATURE</h3>
          </div>
          <div class="promo-banner-cta">
            <span>Explore Classics &rarr;</span>
          </div>
        </div>

      </div>
    </section>

    <!-- =========================================================================
         7B. FAST HORIZONTAL CATEGORY SHELVES
         ========================================================================= -->
    <!-- Shelf 1: Popular Novels -->
    <section class="category-shelf-section">
      <div class="shelf-header">
        <div class="shelf-title-wrap">
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 4px;">
            FICTION &bull; NOVELS
          </div>
          <h3>Popular Novels</h3>
        </div>
        <a href="#shop-all-catalog" onclick="filterCatalog('hindi')" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none;">
          Browse All &rarr;
        </a>
      </div>
      <div class="shelf-scroll-row">
        {''.join([render_shelf_book_card(b) for b in CATEGORY_SHELVES['novels'] if b])}
      </div>
    </section>

    <!-- Shelf 2: Poetry, Ghazals & Shayari -->
    <section class="category-shelf-section">
      <div class="shelf-header">
        <div class="shelf-title-wrap">
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 4px;">
            POETRY &bull; SHAYARI
          </div>
          <h3>Poetry, Ghazals &amp; Shayari</h3>
        </div>
        <a href="#shop-all-catalog" onclick="filterCatalog('rekhta')" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none;">
          Browse All &rarr;
        </a>
      </div>
      <div class="shelf-scroll-row">
        {''.join([render_shelf_book_card(b) for b in CATEGORY_SHELVES['poetry'] if b])}
      </div>
    </section>

    <!-- Shelf 3: Literary Criticism, History & Law -->
    <section class="category-shelf-section">
      <div class="shelf-header">
        <div class="shelf-title-wrap">
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 4px;">
            SCHOLARLY &bull; CRITICISM &bull; LAW
          </div>
          <h3>Literary Criticism, History &amp; Law</h3>
        </div>
        <a href="#shop-all-catalog" onclick="filterCatalog('law')" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none;">
          Browse All &rarr;
        </a>
      </div>
      <div class="shelf-scroll-row">
        {''.join([render_shelf_book_card(b) for b in CATEGORY_SHELVES['criticism_law'] if b])}
      </div>
    </section>
"""

# Insert before SECTION 5: PAN-INDIA FILTERABLE CATALOG ARCHIVE
cat_section_marker = "    <!-- =========================================================================\n         8. SECTION 5: PAN-INDIA FILTERABLE CATALOG ARCHIVE (#shop-all-catalog)"
if "7A. CATEGORY DISCOVERY PROMO BANNERS" not in text:
    if cat_section_marker in text:
        text = text.replace(cat_section_marker, shelves_insertion + "\n" + cat_section_marker)
        print("Promo Banners and Horizontal Shelves inserted successfully!")
    else:
        print("Error: cat_section_marker not found!")

# 2. Upgrade Single Product Page View
pdp_start = text.find('  <!-- =========================================================================\n       DEDICATED AMAZON-STYLE SINGLE PRODUCT PAGE VIEW (#single-product-page-view)')
pdp_end = text.find('  <!-- =========================================================================\n       DEDICATED SEARCH RESULTS VIEW (#indigo-search-results-view)', pdp_start)

if pdp_start != -1 and pdp_end != -1:
    print(f"Found PDP section: {pdp_start} to {pdp_end}")
    new_pdp = """  <!-- =========================================================================
       DEDICATED SOLO PRODUCT PAGE VIEW (#single-product-page-view & #indigo-solo-product-view)
       ========================================================================= -->
  <div id="single-product-page-view" class="store-view-section" style="display: none; background: #FAF8F5;">
    <div id="indigo-solo-product-view"></div>
    <div class="product-page-wrapper" style="max-width: 1320px; margin: 0 auto; padding: 24px 20px 60px;">
      
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

      <!-- 3-Column Main Product Showcase -->
      <div class="product-pdp-grid" style="display: grid; grid-template-columns: 380px 1fr 340px; gap: 36px; align-items: start;">
        
        <!-- LEFT COLUMN: Framed Cover with 3D Hover Preview & Thumbnails -->
        <div class="pdp-left-col">
          <div class="pdp-cover-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); text-align: center;">
            
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

        <!-- CENTER COLUMN: Book Details, Variant Switcher & Tabs -->
        <div class="pdp-center-col">
          <span id="pdpGenreTag" class="pdp-genre-pill" style="display: inline-block; background: #EFF6FF; color: #1D4ED8; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px;">
            FICTION &bull; NOVEL
          </span>
          <h1 id="pdpTitle" class="pdp-book-title" style="font-family: 'Merriweather', Georgia, serif; font-size: 32px; font-weight: 700; color: #09132C; line-height: 1.2; margin: 0 0 10px;">
            Book Title
          </h1>
          
          <!-- Clickable Author Avatar Pill -->
          <div class="pdp-author-pill-wrap" style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 16px;">
            <div id="pdpAuthorAvatar" style="width: 32px; height: 32px; border-radius: 50%; background: #FEF3C7; color: #B45309; font-weight: 700; font-size: 14px; display: flex; align-items: center; justify-content: center; border: 1px solid #FDE68A;">
              A
            </div>
            <span style="font-size: 14px; color: #475569;">
              Author: <a href="javascript:void(0)" id="pdpAuthorLink" onclick="window.openAuthorBooksPage(currentActivePdpBook ? currentActivePdpBook.author : '')" style="color: #09132C; font-weight: 700; text-decoration: underline;" title="View all books by this author">Author Name</a>
            </span>
          </div>

          <div class="pdp-price-wrap" style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
            <span id="pdpSellingPrice" class="pdp-selling-price" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 28px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            <span id="pdpComparePrice" class="pdp-compare-price" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; text-decoration: line-through; color: #94A3B8; font-variant-numeric: lining-nums tabular-nums !important;">₹400.00</span>
            <span id="pdpDiscountBadge" class="pdp-discount-badge" style="background: #FEF2F2; color: #DC2626; border: 1px solid #FEE2E2; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 4px;">25% OFF</span>
            <span style="font-size: 12px; color: #64748B;">(Inclusive of all taxes)</span>
          </div>

          <!-- Select Variant Box -->
          <div class="pdp-variant-selector-box" style="border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px; margin: 16px 0; background: #FFFFFF;">
            <div style="font-size: 12px; font-weight: 700; color: #0F172A; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.05em;">
              Select Variant / Format
            </div>
            <div id="pdpVariantButtons" style="display: flex; gap: 10px; flex-wrap: wrap;">
              <!-- Dynamic Variant Buttons generated via JS -->
            </div>
          </div>

          <!-- Live Stock Badge -->
          <div style="margin-bottom: 16px;">
            <span id="pdpStockBadge" style="display: inline-flex; align-items: center; gap: 6px; color: #16A34A; font-weight: 600; font-size: 13px;">
              <i data-lucide="check" style="width: 15px; height: 15px;"></i> In Stock
            </span>
          </div>

          <!-- Interactive Description | Details Tabs -->
          <div class="pdp-tabs-container">
            <div class="pdp-tab-nav">
              <button type="button" class="pdp-tab-btn active" id="pdpTabDescBtn" onclick="switchPdpTab('desc')">Description</button>
              <button type="button" class="pdp-tab-btn" id="pdpTabDetailsBtn" onclick="switchPdpTab('details')">Details &amp; Specs</button>
            </div>

            <!-- Description Tab Pane -->
            <div id="pdpTabDescPane" class="pdp-tab-pane active" style="display: block;">
              <p id="pdpDescription" style="font-size: 14.5px; line-height: 1.7; color: #334155; margin: 0 0 16px;">
                Authentic publisher edition curated by Indigo Books India.
              </p>
              <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 16px; font-size: 12.5px; color: #64748B; line-height: 1.5;">
                <strong>Publisher Note:</strong> Official certified release. Guaranteed original publisher paper stock and binding integrity. Shipped directly from Prayagraj Hub.
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
                      <td id="pdpSpecEdition" style="padding: 10px 14px; color: #0F172A;">4th (1936)</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Weight:</th>
                      <td id="pdpSpecWeight" style="padding: 10px 14px; color: #0F172A;">270 g</td>
                    </tr>
                    <tr>
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Dimensions (L &times; B &times; H):</th>
                      <td id="pdpSpecDimensions" style="padding: 10px 14px; color: #0F172A;">21.6 &times; 14.0 &times; 1.5 cm</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

        </div>

        <!-- RIGHT COLUMN: Delivery & Express Buy Box -->
        <div class="pdp-right-col">
          <div class="pdp-buy-box" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <div id="pdpBbPrice" class="pdp-bb-price" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 800; color: #0F172A; margin-bottom: 16px;">
              ₹299.00
            </div>
            
            <!-- Green Delivery Box -->
            <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 12px 14px; margin-bottom: 18px;">
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
            <div class="pdp-pincode-checker-box" style="margin-bottom: 20px;">
              <div style="font-size: 12px; color: #475569; display: flex; align-items: center; gap: 6px; margin-bottom: 8px;">
                <i data-lucide="map-pin" style="width: 14px; height: 14px; color: #0066B3;"></i> Add an address to check delivery availability
              </div>
              <div style="display: flex; gap: 8px;">
                <input type="text" id="pdpPincodeInput" placeholder="Enter 6-digit pincode" maxlength="6" style="flex: 1; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />
                <button type="button" onclick="window.checkPdpPincode()" style="background: #0F172A; color: #FFFFFF; border: none; border-radius: 6px; padding: 8px 14px; font-size: 12.5px; font-weight: 700; cursor: pointer;">
                  Check
                </button>
              </div>
              <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="flex: 1; height: 1px; background: #E2E8F0;"></div>
                <span style="font-size: 10.5px; color: #94A3B8; text-transform: uppercase;">OR</span>
                <div style="flex: 1; height: 1px; background: #E2E8F0;"></div>
              </div>
              <button type="button" onclick="window.useLiveGpsLocation()" style="width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; background: #EFF6FF; border: 1px solid #BFDBFE; color: #1D4ED8; padding: 8px 12px; border-radius: 6px; font-size: 12.5px; font-weight: 600; cursor: pointer;">
                <i data-lucide="locate" style="width: 15px; height: 15px;"></i> Use current location
              </button>
              <div id="pdpPincodeStatus" style="font-size: 12px; margin-top: 8px; display: none;"></div>
            </div>

            <!-- Quantity Selector -->
            <div class="pdp-qty-row" style="margin-bottom: 18px;">
              <label class="pdp-qty-label" for="pdpQtyInput">Quantity:</label>
              <div class="pdp-qty-control">
                <button type="button" class="pdp-qty-btn" onclick="pdpQtyDecrease()">-</button>
                <input type="text" id="pdpQtyInput" value="1" readonly class="pdp-qty-input" />
                <button type="button" class="pdp-qty-btn" onclick="pdpQtyIncrease()">+</button>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="pdp-btn-stack" style="display: flex; flex-direction: column; gap: 10px;">
              <button type="button" class="pdp-btn-add-cart" onclick="pdpAddToCart()" style="background: #0F172A; color: #FFFFFF; padding: 12px; border: none; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <i data-lucide="shopping-bag" style="width: 16px; height: 16px;"></i> Add to Cart
              </button>
              <button type="button" class="pdp-btn-buy-now" onclick="pdpBuyNow()" style="background: #F59E0B; color: #0F172A; padding: 12px; border: none; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <i data-lucide="zap" style="width: 16px; height: 16px;"></i> Buy Now (1-Click Phone Checkout)
              </button>
              <button type="button" class="pdp-btn-wa-cod" onclick="pdpWhatsAppOrder()" style="background: #10B981; color: #FFFFFF; padding: 12px; border: none; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i> Order on WhatsApp COD
              </button>
            </div>

            <div class="pdp-bb-security" style="margin-top: 14px; text-align: center; font-size: 11.5px; color: #64748B; display: flex; align-items: center; justify-content: center; gap: 6px;">
              <i data-lucide="lock" style="width: 13px; height: 13px; color: #16A34A;"></i>
              <span>Secure 256-Bit Encrypted Ordering</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom: More Books by this Author Shelf -->
      <div class="pdp-recommendations-sec" style="margin-top: 48px; border-top: 1px solid #E2E8F0; padding-top: 36px;">
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

      <!-- Customer Reviews Card -->
      <div id="pdpReviewsCard" style="margin-top: 40px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 28px;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #F1F5F9; padding-bottom: 16px; margin-bottom: 20px;">
          <div>
            <h3 style="font-family: 'Merriweather', serif; font-size: 20px; font-weight: 700; color: #0F172A; margin: 0 0 4px;">
              Customer Reviews
            </h3>
            <div style="display: flex; align-items: center; gap: 8px;">
              <div style="display: flex; gap: 2px; color: #F59E0B;">
                <i data-lucide="star" style="width: 16px; height: 16px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 16px; height: 16px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 16px; height: 16px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 16px; height: 16px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 16px; height: 16px; fill: currentColor;"></i>
              </div>
              <span style="font-size: 13.5px; font-weight: 700; color: #0F172A;">4.9 out of 5</span>
              <span style="font-size: 12.5px; color: #64748B;">(12,840 global ratings)</span>
            </div>
          </div>
          <button type="button" onclick="alert('Thank you for rating! Reader reviews are verified upon order delivery.')" style="background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 6px; padding: 8px 16px; font-size: 12.5px; font-weight: 700; color: #0F172A; cursor: pointer;">
            Write a Review
          </button>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px;">
          <div style="border-bottom: 1px solid #F8FAFC; padding-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
              <span style="font-weight: 700; font-size: 13.5px; color: #0F172A;">Dr. Arvind Sharma (Prayagraj)</span>
              <span style="font-size: 11px; color: #16A34A; background: #DCFCE7; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Verified Reader</span>
            </div>
            <p style="font-size: 13.5px; color: #475569; margin: 0; line-height: 1.6;">
              "Outstanding publisher edition with original paper texture and binding. Dispatched from Prayagraj and reached Lucknow in less than 24 hours. The packaging was immaculate."
            </p>
          </div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
              <span style="font-weight: 700; font-size: 13.5px; color: #0F172A;">Meenakshi Trivedi (New Delhi)</span>
              <span style="font-size: 11px; color: #16A34A; background: #DCFCE7; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Verified Reader</span>
            </div>
            <p style="font-size: 13.5px; color: #475569; margin: 0; line-height: 1.6;">
              "The print quality is crisp and authentic. Indigo Books has brought genuine Hindi literary classics back to mainstream readers. 10/10 service!"
            </p>
          </div>
        </div>
      </div>

    </div>
  </div>\n\n"""
    text = text[:pdp_start] + new_pdp + text[pdp_end:]
    print("Solo Product Page updated!")

# 3. Add Express Phone Checkout Modal before </body>
checkout_modals = """
  <!-- =========================================================================
       1-CLICK PHONE & GPS EXPRESS CHECKOUT MODAL (#expressPhoneCheckoutModal)
       ========================================================================= -->
  <div id="expressPhoneCheckoutModal" class="express-checkout-modal-backdrop" style="display: none;">
    <div class="express-checkout-card">
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
            <input type="tel" id="checkoutPhone" placeholder="Enter 10-digit mobile number" required pattern="[6-9][0-9]{9}" maxlength="10" style="flex: 1; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />
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
            <input type="text" id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" required pattern="[1-9][0-9]{5}" style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />
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

  <!-- Order Confirmation Modal -->
  <div id="orderConfirmationModal" class="express-checkout-modal-backdrop" style="display: none;">
    <div class="express-checkout-card" style="text-align: center;">
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
"""

if "expressPhoneCheckoutModal" not in text:
    b_idx = text.rfind("</body>")
    if b_idx != -1:
        text = text[:b_idx] + checkout_modals + "\n" + text[b_idx:]
        print("Express Phone Checkout Modals inserted successfully!")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("build_html_generator.py fully upgraded!")

