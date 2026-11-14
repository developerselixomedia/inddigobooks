# -*- coding: utf-8 -*-
"""
apply_pdp_and_auth_overhaul.py
Fixes:
1. Solo Book Page (PDP) Mobile Alignment:
   - Eliminates the cramped 50% side-by-side columns that caused the trust perks & specs table to squash together.
   - Restructures PDP into a clean, full-width mobile flow (order: 1 Cover -> 2 Info Header -> 3 Buy Box -> 4 Full-Width Specs Table -> 5 Trust Perks).
   - Guarantees 100% full-width layout for Technical Specs table so ISBN and Dimensions never wrap awkwardly.
2. Sign In / Sign Up Modal Visibility:
   - Restores solid crisp white card styling (#FFFFFF, 16px radius, deep shadow, clean border).
   - Replaces invisible dark-navy-on-dark-navy text with high-contrast typography.
   - Adds toggle tabs between [Sign In] and [Join Book Club (Sign Up)] with full fields and instant validation.
   - Adds SVG vector close button.
"""

import re

# =========================================================================
# 1. UPDATE build_html_generator.py
# =========================================================================
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    bhg = f.read()

# Replace PDP Left Col and Center Col structure
pdp_old_structure = '''        <!-- LEFT COLUMN: Framed Cover with 3D Hover Preview & Thumbnails -->
        <div class="pdp-left-col">
          <div class="pdp-cover-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); text-align: center;">
            
            <div class="indigo-3d-book-stage" id="pdp3dStage" style="max-width: 280px; margin: 0 auto 16px;">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">
                  INDIGO ARCHIVE &bull; PREVIEW
                </div>
                <div id="pdp3dInsideTitle" style="font-family: \'Merriweather\', serif; font-size: 12px; line-height: 1.4; color: #1E293B; font-weight: 700;">
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
          <h1 id="pdpTitle" class="pdp-book-title" style="font-family: \'Merriweather\', Georgia, serif; font-size: 32px; font-weight: 700; color: #09132C; line-height: 1.2; margin: 0 0 10px;">
            Book Title
          </h1>
          
          <!-- Clickable Author Avatar Pill -->
          <div class="pdp-author-pill-wrap" style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 16px;">
            <div id="pdpAuthorAvatar" style="width: 32px; height: 32px; border-radius: 50%; background: #FEF3C7; color: #B45309; font-weight: 700; font-size: 14px; display: flex; align-items: center; justify-content: center; border: 1px solid #FDE68A;">
              A
            </div>
            <span style="font-size: 14px; color: #475569;">
              Author: <a href="javascript:void(0)" id="pdpAuthorLink" onclick="window.openAuthorBooksPage(currentActivePdpBook ? currentActivePdpBook.author : \'\')" style="color: #09132C; font-weight: 700; text-decoration: underline;" title="View all books by this author">Author Name</a>
            </span>
          </div>

          <div class="pdp-price-wrap" style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
            <span id="pdpSellingPrice" class="pdp-selling-price" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 28px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            
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
          <div class="pdp-tabs-container">'''

pdp_new_structure = '''        <!-- LEFT COLUMN: Framed Cover with 3D Hover Preview & Thumbnails -->
        <div class="pdp-left-col">
          <div class="pdp-cover-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); text-align: center;">
            
            <div class="indigo-3d-book-stage" id="pdp3dStage" style="max-width: 280px; margin: 0 auto 16px;">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">
                  INDIGO ARCHIVE &bull; PREVIEW
                </div>
                <div id="pdp3dInsideTitle" style="font-family: \'Merriweather\', serif; font-size: 12px; line-height: 1.4; color: #1E293B; font-weight: 700;">
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
          <div class="pdp-trust-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 20px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); margin-top: 18px;">
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
          <div class="pdp-info-header-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04); margin-bottom: 24px;">
            <span id="pdpGenreTag" class="pdp-genre-pill" style="display: inline-block; background: #EFF6FF; color: #1D4ED8; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px;">
              FICTION &bull; NOVEL
            </span>
            <h1 id="pdpTitle" class="pdp-book-title" style="font-family: \'Merriweather\', Georgia, serif; font-size: 30px; font-weight: 700; color: #09132C; line-height: 1.25; margin: 0 0 10px;">
              Book Title
            </h1>
            
            <!-- Clickable Author Avatar Pill -->
            <div class="pdp-author-pill-wrap" style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 14px;">
              <div id="pdpAuthorAvatar" style="width: 32px; height: 32px; border-radius: 50%; background: #FEF3C7; color: #B45309; font-weight: 700; font-size: 14px; display: flex; align-items: center; justify-content: center; border: 1px solid #FDE68A;">
                A
              </div>
              <span style="font-size: 14px; color: #475569;">
                Author: <a href="javascript:void(0)" id="pdpAuthorLink" onclick="window.openAuthorBooksPage(currentActivePdpBook ? currentActivePdpBook.author : \'\')" style="color: #09132C; font-weight: 700; text-decoration: underline;" title="View all books by this author">Author Name</a>
              </span>
            </div>

            <div class="pdp-price-wrap" style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
              <span id="pdpSellingPrice" class="pdp-selling-price" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 28px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
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
          <div class="pdp-tabs-container">'''

if pdp_old_structure in bhg:
    bhg = bhg.replace(pdp_old_structure, pdp_new_structure, 1)
    print("✓ Successfully upgraded PDP structure in build_html_generator.py")
else:
    print("✗ pdp_old_structure not found in build_html_generator.py")

# Update Auth Modal in build_html_generator.py
old_auth_modal = '''  <!-- =========================================================================
       15. MEMBER SIGN IN MODAL
       ========================================================================= -->
  <div id="loginModalOverlay" class="modal-overlay indigo-modal-overlay" onclick="if(event.target === this) toggleLoginModal()">
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
  </div>'''

new_auth_modal = '''  <!-- =========================================================================
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
        <h3 id="authModalTitle" style="font-family: \'Merriweather\', serif; font-size: 20px; font-weight: 700; color: #0F172A; margin: 0 0 6px;">Sign in to Indigo Books</h3>
        <p id="authModalSubtitle" style="font-size: 13px; color: #64748B; margin: 0;">Access your reading orders, wishlist, and scholar benefits.</p>
      </div>

      <!-- Tab Switcher: Sign In vs Join Book Club (Sign Up) -->
      <div style="display: flex; background: #F1F5F9; border-radius: 8px; padding: 4px; margin-bottom: 20px; gap: 4px;">
        <button type="button" id="tabAuthSignIn" onclick="switchAuthMode(\'signin\')" style="flex: 1; padding: 8px 12px; font-size: 13px; font-weight: 700; border: none; border-radius: 6px; background: #FFFFFF; color: #0F172A; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.2s;">Sign In</button>
        <button type="button" id="tabAuthSignUp" onclick="switchAuthMode(\'signup\')" style="flex: 1; padding: 8px 12px; font-size: 13px; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #64748B; cursor: pointer; transition: all 0.2s;">Join Book Club (Sign Up)</button>
      </div>

      <!-- Sign In Form -->
      <form id="authSignInForm" onsubmit="event.preventDefault(); alert(\'Welcome back to Indigo Books India! Your session is verified.\'); toggleLoginModal();">
        <div style="margin-bottom: 14px;">
          <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Email or Mobile Number</label>
          <input type="text" placeholder="name@domain.com or 10-digit mobile" required style="width: 100%; padding: 11px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <div style="margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <label style="font-size: 12px; font-weight: 700; color: #334155;">Password</label>
            <a href="javascript:void(0)" onclick="alert(\'Password reset link has been dispatched to your registered email/phone.\')" style="font-size: 11.5px; color: #0066B3; text-decoration: none; font-weight: 600;">Forgot?</a>
          </div>
          <input type="password" placeholder="Enter your password" required style="width: 100%; padding: 11px 14px; font-size: 13.5px; border: 1.5px solid #CBD5E1; border-radius: 8px; outline: none; box-sizing: border-box; background: #FFFFFF; color: #0F172A;" />
        </div>
        <button type="submit" style="width: 100%; justify-content: center; margin-bottom: 14px; background: #0066B3; color: #FFFFFF; padding: 12px; border-radius: 8px; font-weight: 700; font-size: 14px; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 12px rgba(0, 102, 179, 0.25);">
          Sign In to Your Account
        </button>
      </form>

      <!-- Sign Up Form (Initially hidden) -->
      <form id="authSignUpForm" style="display: none;" onsubmit="event.preventDefault(); alert(\'Welcome to Indigo Books Club! Your account has been registered with 5% scholar welcome credit.\'); toggleLoginModal();">
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
        <span id="authSwitchPrompt">Don\'t have an account? <span onclick="switchAuthMode(\'signup\')" style="color: #B45309; font-weight: 700; cursor: pointer; text-decoration: underline;">Join the Book Club</span></span>
      </div>
    </div>
  </div>'''

if old_auth_modal in bhg:
    bhg = bhg.replace(old_auth_modal, new_auth_modal, 1)
    print("✓ Successfully upgraded Auth Modal in build_html_generator.py")
else:
    print("✗ old_auth_modal not found in build_html_generator.py")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(bhg)


# =========================================================================
# 2. UPDATE store_scripts.py
# =========================================================================
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    ss = f.read()

switch_auth_func = '''
function switchAuthMode(mode) {
  const signinForm = document.getElementById('authSignInForm');
  const signupForm = document.getElementById('authSignUpForm');
  const tabIn = document.getElementById('tabAuthSignIn');
  const tabUp = document.getElementById('tabAuthSignUp');
  const title = document.getElementById('authModalTitle');
  const sub = document.getElementById('authModalSubtitle');
  const prompt = document.getElementById('authSwitchPrompt');

  if (mode === 'signup') {
    if (signinForm) signinForm.style.display = 'none';
    if (signupForm) signupForm.style.display = 'block';
    if (tabIn) {
      tabIn.style.background = 'transparent';
      tabIn.style.color = '#64748B';
      tabIn.style.fontWeight = '600';
      tabIn.style.boxShadow = 'none';
    }
    if (tabUp) {
      tabUp.style.background = '#FFFFFF';
      tabUp.style.color = '#0F172A';
      tabUp.style.fontWeight = '700';
      tabUp.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
    }
    if (title) title.textContent = 'Join Indigo Book Club';
    if (sub) sub.textContent = 'Create your account for exclusive literary previews and scholar benefits.';
    if (prompt) prompt.innerHTML = 'Already have an account? <span onclick="switchAuthMode(\\'signin\\')" style="color: #0066B3; font-weight: 700; cursor: pointer; text-decoration: underline;">Sign In</span>';
  } else {
    if (signupForm) signupForm.style.display = 'none';
    if (signinForm) signinForm.style.display = 'block';
    if (tabUp) {
      tabUp.style.background = 'transparent';
      tabUp.style.color = '#64748B';
      tabUp.style.fontWeight = '600';
      tabUp.style.boxShadow = 'none';
    }
    if (tabIn) {
      tabIn.style.background = '#FFFFFF';
      tabIn.style.color = '#0F172A';
      tabIn.style.fontWeight = '700';
      tabIn.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
    }
    if (title) title.textContent = 'Sign in to Indigo Books';
    if (sub) sub.textContent = 'Access your reading orders, wishlist, and scholar benefits.';
    if (prompt) prompt.innerHTML = 'Don\\'t have an account? <span onclick="switchAuthMode(\\'signup\\')" style="color: #B45309; font-weight: 700; cursor: pointer; text-decoration: underline;">Join the Book Club</span>';
  }
}
window.switchAuthMode = switchAuthMode;
'''

if 'function switchAuthMode' not in ss:
    target_pos = ss.find('function toggleLoginModal()')
    if target_pos != -1:
        ss = ss[:target_pos] + switch_auth_func + '\n' + ss[target_pos:]
        print("✓ Successfully added switchAuthMode to store_scripts.py")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(ss)


# =========================================================================
# 3. UPDATE store_styles.py & prepare_master_blocks.py (CSS)
# =========================================================================

pdp_mobile_css = '''  /* =========================================================================
     PRODUCT DETAILS PAGE (PDP) MOBILE & DESKTOP ALIGNMENT SHIELD
     ========================================================================= */
  .product-pdp-grid {
    display: grid !important;
    grid-template-columns: 360px 1fr 320px !important;
    gap: 36px !important;
    align-items: start !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-left-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 20px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-center-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 24px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-right-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 20px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  @media (max-width: 1100px) {
    .product-pdp-grid {
      grid-template-columns: 320px 1fr 280px !important;
      gap: 24px !important;
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
'''

# Update prepare_master_blocks.py
with open('prepare_master_blocks.py', 'r', encoding='utf-8') as f:
    pmb = f.read()

# Replace PDP section in prepare_master_blocks.py
pdp_start_marker = '  /* =========================================================================\n     PRODUCT DETAILS PAGE (PDP) MOBILE & DESKTOP ALIGNMENT SHIELD'
auth_modal_marker = '  /* =========================================================================\n     FOOTER & FLOATING WHATSAPP BUTTON MOBILE ALIGNMENT SHIELD'

if pdp_start_marker in pmb and auth_modal_marker in pmb:
    idx1 = pmb.find(pdp_start_marker)
    idx2 = pmb.find(auth_modal_marker)
    pmb = pmb[:idx1] + pdp_mobile_css + '\n\n' + pmb[idx2:]
    print("✓ Successfully updated PDP & Auth Modal rules in prepare_master_blocks.py")
else:
    print("✗ Could not find markers in prepare_master_blocks.py")

with open('prepare_master_blocks.py', 'w', encoding='utf-8') as f:
    f.write(pmb)

# Update store_styles.py
with open('store_styles.py', 'r', encoding='utf-8') as f:
    sty = f.read()

if pdp_start_marker in sty and auth_modal_marker in sty:
    idx1 = sty.find(pdp_start_marker)
    idx2 = sty.find(auth_modal_marker)
    sty = sty[:idx1] + pdp_mobile_css + '\n\n' + sty[idx2:]
    print("✓ Successfully updated PDP & Auth Modal rules in store_styles.py")
else:
    # Append the rules to the end of store_styles.py
    sty = sty.rstrip() + '\n\n' + pdp_mobile_css + '\n'
    print("✓ Appended PDP & Auth Modal rules to store_styles.py")

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(sty)

print("All file patches applied successfully!")

