# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="single-product-page-view"')
start = text.rfind('<!-- ===', 0, idx)
end = text.find('<!-- ===', idx)

print(f"Replacing PDP from {start} to {end}")

new_pdp = """<!-- =========================================================================
       10. DEDICATED SOLO PRODUCT PAGE VIEW (#single-product-page-view & #indigo-solo-product-view)
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

      <!-- 3-Column Main Product Showcase (380px 1fr 340px) -->
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
  </div>\n\n  """

text = text[:start] + new_pdp + text[end:]

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("build_html_generator.py PDP section replaced successfully!")

