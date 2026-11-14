# -*- coding: utf-8 -*-
"""
apply_comprehensive_fixes.py
Applies the 5 targeted fixes:
1. Unify Global Typography (Playfair Display + Plus Jakarta Sans)
2. Fix 3D Podium Book (Cover opens completely to -140deg, reveals cream parchment inner page + mini-overview)
3. Fix cut-off book names in Mehfil-e-Rekhta (Vertical flex stack, zero text overlap, full 2-line titles, mini-overviews on every book)
4. Add mini-overviews across all cards (Mehfil, Regional, Bundles, Academic Vault)
5. Make all website tabs 100% functional:
   - Navbar tabs (Home, Shop All, Best Sellers, Coming Soon, Bundles, Pre-Order, Law Books)
   - Mehfil-e-Rekhta poet tabs (All Poets, Jaun Elia, Ahmad Faraz, Manto, Ghalib)
   - Law & Academic Vault drawer tabs
   - Full Filterable Catalog Directory (#shop-all-catalog)
6. Updates preview.html, Shopify liquid sections, assets/theme.css, assets/theme.js, templates/index.json, and re-packages indigo-books-theme.zip.
"""

import os
import re
import json
import zipfile

print("Starting Comprehensive UI & Functionality Fixes...")

# Read preview.html
with open('preview.html', 'r', encoding='utf-8') as f:
    preview_content = f.read()

# -------------------------------------------------------------
# 1. UNIFY GLOBAL TYPOGRAPHY IN HEAD
# -------------------------------------------------------------
# Ensure Google Fonts link has Playfair Display + Plus Jakarta Sans + Inter
font_link = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,600;1,700&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">'

if 'family=Plus+Jakarta+Sans' not in preview_content:
    preview_content = preview_content.replace('</head>', f'{font_link}\n</head>')

# Global CSS override to strictly enforce typography
global_typography_css = """
<style id="unifiedTypographyRules">
  /* Universal Typography Pairing */
  body, button, input, select, textarea, .font-sans {
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  }
  h1, h2, h3, h4, h5, h6, .font-serif, .book-title, .book-price, .poet-couplet, .brand-wordmark {
    font-family: 'Playfair Display', Georgia, Cambria, serif !important;
  }
  
  /* Smooth Scrolling */
  html {
    scroll-behavior: smooth;
    scroll-padding-top: 90px;
  }

  /* 3D Podium Book: Wide Cover Open to -140deg */
  .podium-stage-container {
    perspective: 1600px;
  }
  .podium-book-card {
    transform-style: preserve-3d;
    transition: transform 0.6s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.4s ease;
  }
  .book-3d-wrapper {
    transform-style: preserve-3d;
    perspective: 1600px;
  }
  .book-cover-front {
    transform-origin: left center;
    transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.5s ease;
    backface-visibility: hidden;
    z-index: 25;
  }
  /* Inside of the front cover (visible when flipped open to -140deg) */
  .book-cover-back {
    position: absolute;
    inset: 0;
    transform-origin: left center;
    transform: rotateY(180deg);
    backface-visibility: hidden;
    background: linear-gradient(135deg, #1A120B 0%, #2D1E12 100%);
    border: 1px solid #4A3525;
    border-radius: 4px 2px 2px 4px;
    z-index: 24;
    transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
  }
  
  /* Hover & Active Toggle: Cover swings open completely to -140deg */
  .podium-book-card.is-active:hover .book-cover-front,
  .podium-book-card.is-active.is-open .book-cover-front {
    transform: rotateY(-140deg);
    box-shadow: 25px 30px 60px rgba(0, 0, 0, 0.8);
  }
  .podium-book-card.is-active:hover .book-cover-back,
  .podium-book-card.is-active.is-open .book-cover-back {
    transform: rotateY(40deg);
  }

  /* Right Parchment Page Revealed Underneath */
  .book-page-underneath {
    background-color: #FFFDF9;
    background-image: radial-gradient(#F5EFE6 1px, transparent 1px);
    background-size: 12px 12px;
    border: 1px solid #E8DFC8;
    box-shadow: inset 5px 0 15px rgba(0,0,0,0.06), 0 10px 25px rgba(0,0,0,0.15);
  }

  /* Navbar Link Active State */
  .nav-tab-link.active {
    color: #0A1128 !important;
    border-bottom: 2px solid #D99B26 !important;
    font-weight: 700 !important;
  }
  .nav-tab-link:not(.active) {
    color: #475569 !important;
    border-bottom: 2px solid transparent !important;
    font-weight: 500 !important;
  }
  .nav-tab-link:not(.active):hover {
    color: #D99B26 !important;
    border-bottom-color: #D99B26 !important;
  }
</style>
"""

# Insert typography CSS right before </head>
if 'id="unifiedTypographyRules"' not in preview_content:
    preview_content = preview_content.replace('</head>', f'{global_typography_css}\n</head>')
else:
    preview_content = re.sub(r'<style id="unifiedTypographyRules">.*?</style>', global_typography_css.strip(), preview_content, flags=re.DOTALL)

# -------------------------------------------------------------
# 2. UPDATE NAVBAR IN PREVIEW.HTML (WIRED WITH HANDLE_NAV_CLICK)
# -------------------------------------------------------------
old_header_match = re.search(r'<header[^>]*class="sticky top-0.*?<\/header>', preview_content, re.DOTALL)

updated_header_html = """  <!-- A. Navigation Bar (h-20, Sticky at top-0, bg-[#FAF8F5]/95 backdrop-blur-md, z-50) -->
  <header class="sticky top-0 h-20 bg-[#FAF8F5]/95 backdrop-blur-md border-b border-amber-900/10 z-50 transition-shadow duration-200 shadow-sm" id="siteHeader">
    <div class="max-w-7xl mx-auto px-6 lg:px-8 h-full flex justify-between items-center">
      
      <!-- Left: Official INDIGO BOOKS Brand Logo -->
      <a href="#heroSection" onclick="handleNavClick('Home', event)" class="flex items-center gap-3 cursor-pointer group select-none">
        <!-- Brand Emblem (SVG Icon: Symmetric Blue Geometric Knot Emblem #0066B3) -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 354 352" class="w-10 h-10 shrink-0 group-hover:scale-105 transition-transform" fill="#0066B3" fill-rule="evenodd" aria-label="Indigo Books Emblem">
          <path d="M 207 206 L 207 308 L 211 312 L 296 313 L 296 351 L 352 350 L 351 295 L 313 294 L 313 210 L 309 206 Z M 314 312 L 335 313 L 334 334 L 313 333 Z M 224 223 L 296 224 L 295 295 L 223 294 Z M 44 206 L 42 207 L 41 208 L 40 210 L 39 295 L 1 295 L 1 351 L 57 350 L 58 312 L 141 312 L 143 311 L 146 308 L 146 206 Z M 19 312 L 40 313 L 39 334 L 18 333 Z M 58 223 L 129 224 L 128 295 L 57 294 Z M 296 1 L 295 39 L 212 39 L 210 40 L 207 43 L 207 145 L 309 145 L 313 141 L 314 56 L 352 55 L 351 0 Z M 224 56 L 296 57 L 295 128 L 223 127 Z M 314 17 L 335 18 L 334 39 L 313 38 Z M 75 0 L 75 17 L 144 17 L 147 18 L 150 19 L 152 20 L 154 21 L 158 24 L 162 28 L 164 31 L 167 37 L 168 41 L 167 167 L 42 167 L 38 166 L 32 163 L 28 160 L 24 156 L 22 153 L 19 147 L 18 143 L 18 74 L 1 74 L 1 143 L 2 149 L 3 152 L 4 155 L 8 163 L 10 166 L 19 176 L 10 185 L 8 188 L 6 192 L 3 198 L 2 202 L 1 208 L 1 277 L 18 277 L 18 208 L 19 204 L 23 196 L 29 190 L 32 188 L 38 185 L 42 184 L 168 185 L 168 310 L 167 314 L 164 320 L 154 330 L 152 331 L 150 332 L 147 333 L 144 334 L 75 334 L 75 351 L 144 351 L 149 350 L 153 349 L 156 348 L 162 345 L 165 343 L 169 340 L 176 332 L 185 341 L 188 343 L 191 345 L 197 348 L 200 349 L 203 350 L 209 351 L 278 351 L 278 334 L 209 334 L 205 333 L 199 330 L 195 327 L 191 323 L 189 320 L 186 314 L 185 311 L 186 184 L 311 184 L 315 185 L 321 188 L 324 190 L 329 195 L 331 198 L 332 200 L 333 202 L 334 205 L 335 209 L 335 277 L 352 276 L 352 209 L 351 203 L 350 199 L 349 196 L 345 188 L 342 184 L 333 175 L 342 167 L 345 163 L 349 155 L 350 152 L 351 148 L 352 142 L 352 74 L 335 74 L 335 142 L 334 146 L 333 149 L 332 151 L 331 153 L 328 156 L 328 157 L 326 159 L 321 163 L 315 166 L 311 167 L 185 166 L 185 40 L 186 37 L 187 34 L 188 32 L 191 28 L 196 23 L 199 21 L 205 18 L 209 17 L 278 17 L 278 0 L 209 0 L 203 1 L 200 2 L 197 3 L 189 7 L 186 9 L 176 19 L 168 10 L 165 8 L 162 6 L 156 3 L 153 2 L 149 1 L 144 0 Z M 1 0 L 2 56 L 40 57 L 40 141 L 44 145 L 146 145 L 146 43 L 143 40 L 141 39 L 57 38 L 56 0 Z M 58 56 L 129 57 L 128 128 L 57 127 Z M 19 17 L 40 18 L 39 39 L 18 38 Z" />
        </svg>
        <!-- Store Name Wordmark -->
        <span class="font-serif text-xl lg:text-2xl tracking-[0.12em] font-normal text-black uppercase brand-wordmark">
          INDIGO BOOKS
        </span>
      </a>

      <!-- Center Nav Links: 100% Functional Tab Group -->
      <nav class="hidden xl:flex items-center gap-6" id="SiteNav">
        <a href="#heroSection" onclick="handleNavClick('Home', event)" class="nav-tab-link active text-sm py-2 transition-all">
          Home
        </a>
        <a href="#shop-all-catalog" onclick="handleNavClick('Shop All', event)" class="nav-tab-link text-sm py-2 transition-all">
          Shop All (11,900+)
        </a>
        <a href="#bestsellers-podium" onclick="handleNavClick('Best Sellers', event)" class="nav-tab-link text-sm py-2 transition-all">
          Best Sellers
        </a>
        <a href="#shop-all-catalog" onclick="handleNavClick('Coming Soon', event)" class="nav-tab-link text-sm py-2 transition-all">
          Coming Soon
        </a>
        <a href="#bundles-section" onclick="handleNavClick('Bundles', event)" class="nav-tab-link text-sm py-2 transition-all">
          Bundles
        </a>
        <a href="#shop-all-catalog" onclick="handleNavClick('Pre-Order', event)" class="nav-tab-link text-sm py-2 transition-all">
          Pre-Order
        </a>
        <a href="#law-academic-vault" onclick="handleNavClick('Law Books', event)" class="nav-tab-link text-sm py-2 transition-all">
          Law Books
        </a>
      </nav>

      <!-- Right Action Bar -->
      <div class="flex items-center gap-3 sm:gap-4">
        <!-- Indian Flag Centric Badge -->
        <div class="hidden sm:flex items-center gap-2 bg-white/80 border border-slate-200 px-3 py-1.5 rounded-full shadow-sm">
          <div class="w-4 h-4 rounded-full overflow-hidden border border-slate-300 flex flex-col shrink-0">
            <div class="h-1/3 bg-[#FF9933]"></div>
            <div class="h-1/3 bg-white flex items-center justify-center">
              <div class="w-1 h-1 rounded-full bg-[#000080]"></div>
            </div>
            <div class="h-1/3 bg-[#128807]"></div>
          </div>
          <div class="flex flex-col text-left">
            <span class="text-[10px] font-bold text-slate-900 leading-tight">Indian</span>
            <span class="text-[9px] font-medium text-slate-500 leading-tight">centric</span>
          </div>
        </div>

        <!-- Search Trigger Icon -->
        <button onclick="focusCatalogSearch()" class="p-2 text-slate-700 hover:text-[#0A1128] hover:bg-slate-100 rounded-full transition-colors" title="Quick Search Catalog">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
        </button>

        <!-- User Account (Sign In) Button -->
        <button onclick="openLoginModal()" class="flex items-center gap-1.5 p-2 text-slate-700 hover:text-[#0A1128] hover:bg-slate-100 rounded-lg transition-colors text-xs font-semibold" title="Member Sign In">
          <svg class="w-5 h-5 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          <span class="hidden md:inline">Sign In</span>
        </button>

        <!-- Interactive Cart Drawer Button with Live Badge -->
        <button onclick="openCartDrawer()" class="relative flex items-center gap-2 bg-white hover:bg-amber-50 border border-slate-200 hover:border-amber-400 px-3 py-1.5 rounded-full transition-all shadow-sm group" title="Shopping Cart">
          <div class="relative">
            <svg class="w-5 h-5 text-slate-800 group-hover:text-[#D99B26] transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/>
            </svg>
            <span id="cartCountBadge" class="absolute -top-2 -right-2 bg-rose-600 text-white font-bold text-[10px] w-4 h-4 rounded-full flex items-center justify-center shadow">
              0
            </span>
          </div>
          <span id="cartTotalNav" class="text-xs font-bold text-[#0A1128] hidden lg:inline">
            ₹0.00
          </span>
        </button>

        <!-- WhatsApp Order Button in Emerald Green -->
        <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%20India%2C%20I%20would%20like%20to%20place%20an%20order." target="_blank" class="flex items-center gap-1.5 bg-[#10B981] hover:bg-[#059669] text-white px-3.5 py-2 rounded-md font-semibold text-xs transition-colors shadow-sm" title="Instant WhatsApp Order">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
          <span class="hidden sm:inline">WhatsApp</span>
        </a>

      </div>

    </div>
  </header>"""

if old_header_match:
    preview_content = preview_content.replace(old_header_match.group(0), updated_header_html)
    print("Navbar updated in preview.html with functional tab hooks.")

# -------------------------------------------------------------
# 3. REFACTOR THE 6 BODY SECTIONS (PODIUM, REKHTA, BUNDLES, ETC)
# -------------------------------------------------------------

# A. 3D Podium with wide -140deg cover open & parchment page
podium_section_html = """
<!-- ======================================================================= -->
<!-- SECTION 2: THE 3D CURATOR'S PODIUM FOR BESTSELLERS                       -->
<!-- ======================================================================= -->
<section id="bestsellers-podium" class="py-20 lg:py-24 bg-[#FAF8F5] relative overflow-hidden">
  <!-- Anchor Alias for smooth scrolling -->
  <div id="curatorsPodiumSection"></div>

  <div class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-amber-400/10 rounded-full blur-3xl pointer-events-none"></div>

  <div class="max-w-7xl mx-auto px-6 lg:px-8 relative z-10">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto mb-12">
      <div class="inline-flex items-center gap-2 bg-amber-100 text-[#D99B26] border border-amber-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm">
        <svg class="w-3.5 h-3.5 fill-current text-[#D99B26]" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        <span>CURATOR'S CHOICE & NATIONAL BESTSELLERS</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3">
        The Podium: India's Top 5 Trending Reads
      </h2>
      <p class="text-sm lg:text-base text-slate-600 mt-2">
        Handpicked literature capturing minds across universities, literary circles, and book lovers nationwide.
      </p>
    </div>

    <!-- Split Stage: Left 7 Cols (3D Stage) + Right 5 Cols (Editorial Spotlight Panel) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
      
      <!-- LEFT 7 COLS: 3D Turntable Coverflow Stage -->
      <div class="lg:col-span-7 flex flex-col items-center">
        <!-- Turntable Stage Container with 1600px Perspective -->
        <div class="w-full relative py-8 px-4 flex items-center justify-center min-h-[480px] perspective-[1600px] podium-stage-container" id="podiumTurntableStage">
          
          <!-- Golden Pedestal Base Graphic -->
          <div class="absolute bottom-4 inset-x-8 h-20 bg-gradient-to-t from-amber-400/30 via-amber-200/20 to-transparent rounded-full blur-xl pointer-events-none"></div>
          <div class="absolute bottom-6 w-3/4 h-6 border-b-2 border-amber-500/30 rounded-[100%] shadow-[0_15px_30px_rgba(217,155,38,0.25)] pointer-events-none"></div>

          <!-- Podium Books Display Track -->
          <div class="relative w-full max-w-lg h-[380px] flex items-center justify-center" id="podiumBooksWrapper">
            
            <!-- Book 0: Wimpy Kid -->
            <div class="podium-book-card absolute cursor-pointer" data-index="0" onclick="selectPodiumBook(0)">
              <div class="book-3d-wrapper relative w-40 lg:w-48 aspect-[2/3]">
                <!-- Front Cover (Swings open to -140deg on hover/click) -->
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/hero-book-wimpy-kid.jpg" alt="Diary of a Wimpy Kid" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-3 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <!-- Inside Cover Facing (Revealed at -140deg) -->
                <div class="book-cover-back"></div>
                <!-- Inside Right Page (Revealed Underneath) -->
                <div class="book-page-underneath absolute inset-0 rounded-r-md p-4 flex flex-col justify-between text-slate-900 shadow-inner -z-10">
                  <div>
                    <div class="flex items-center justify-between border-b border-amber-900/15 pb-1">
                      <span class="font-serif text-[11px] font-bold text-amber-900 uppercase tracking-wider">Chapter 1 • Excerpt</span>
                      <span class="text-[9px] font-mono text-slate-400">Page 1</span>
                    </div>
                    <h5 class="font-serif text-xs font-bold text-slate-900 mt-2">Diary of a Wimpy Kid</h5>
                    <p class="font-serif text-[10px] leading-relaxed italic text-slate-700 mt-1">
                      "First of all, let me get something straight: this is a JOURNAL, not a diary. The other thing I want to clear up right away is that this was MUM's idea, not mine..."
                    </p>
                    <div class="mt-2 text-[9px] text-amber-800 font-medium">★ Global Bestselling Phenomenon</div>
                  </div>
                  <button onclick="event.stopPropagation(); openPodiumQuickView();" class="w-full bg-[#D99B26] hover:bg-[#B88019] text-white py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors shadow-sm">
                    Read Full Preview
                  </button>
                </div>
              </div>
            </div>

            <!-- Book 1: Ujli Raaten -->
            <div class="podium-book-card absolute cursor-pointer" data-index="1" onclick="selectPodiumBook(1)">
              <div class="book-3d-wrapper relative w-40 lg:w-48 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/hero-book-ujli-raaten.jpg" alt="Ujli Raaten" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-3 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-cover-back"></div>
                <div class="book-page-underneath absolute inset-0 rounded-r-md p-4 flex flex-col justify-between text-slate-900 shadow-inner -z-10">
                  <div>
                    <div class="flex items-center justify-between border-b border-amber-900/15 pb-1">
                      <span class="font-serif text-[11px] font-bold text-amber-900 uppercase tracking-wider">पहला प्रहर • अंश</span>
                      <span class="text-[9px] font-mono text-slate-400">पृष्ठ १</span>
                    </div>
                    <h5 class="font-serif text-xs font-bold text-slate-900 mt-2">उजली रातें (White Nights)</h5>
                    <p class="font-serif text-[10px] leading-relaxed italic text-slate-700 mt-1">
                      "वह एक अद्भुत रात थी, ऐसी रात जो केवल जवानी के दिनों में ही नसीब हो सकती है। आकाश तारों से इतना भरा था कि उसे देखकर बरबस यह पूछने का मन होता था..."
                    </p>
                    <div class="mt-2 text-[9px] text-amber-800 font-medium">★ फ्योदोर दोस्तोएव्स्की क्लासिक</div>
                  </div>
                  <button onclick="event.stopPropagation(); openPodiumQuickView();" class="w-full bg-[#D99B26] hover:bg-[#B88019] text-white py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors shadow-sm">
                    Read Full Preview
                  </button>
                </div>
              </div>
            </div>

            <!-- Book 2: Kasaibada (Active Center Default) -->
            <div class="podium-book-card is-active absolute cursor-pointer" data-index="2" onclick="selectPodiumBook(2)">
              <div class="book-3d-wrapper relative w-40 lg:w-48 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_25px_45px_rgba(0,0,0,0.65)] border-r-2 border-amber-50/80">
                  <img src="assets/hero-book-kasaibada.jpg" alt="Kasaibada" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-3 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-cover-back"></div>
                <div class="book-page-underneath absolute inset-0 rounded-r-md p-4 flex flex-col justify-between text-slate-900 shadow-inner -z-10">
                  <div>
                    <div class="flex items-center justify-between border-b border-amber-900/15 pb-1">
                      <span class="font-serif text-[11px] font-bold text-amber-900 uppercase tracking-wider">प्रस्तावना / Chapter 1</span>
                      <span class="text-[9px] font-mono text-slate-400">पृष्ठ १</span>
                    </div>
                    <h5 class="font-serif text-xs font-bold text-slate-900 mt-2">कसाईबाड़ा (Kasaibada)</h5>
                    <p class="font-serif text-[10px] leading-relaxed italic text-slate-700 mt-1">
                      "जिंदगी जब सत्ता और संघर्ष के दोराहे पर खड़ी होती है, तब कलम ही सबसे धारदार हथियार बनती है। कस्बाई राजनीति, नैतिक द्वंद्व और आम इंसान के अदम्य साहस का जीवंत दस्तावेज़..."
                    </p>
                    <div class="mt-2 text-[9px] text-amber-800 font-medium">★ मनोज राजन त्रिपाठी कृत</div>
                  </div>
                  <button onclick="event.stopPropagation(); openPodiumQuickView();" class="w-full bg-[#D99B26] hover:bg-[#B88019] text-white py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors shadow-sm">
                    Read Full Preview
                  </button>
                </div>
              </div>
            </div>

            <!-- Book 3: Alchemised -->
            <div class="podium-book-card absolute cursor-pointer" data-index="3" onclick="selectPodiumBook(3)">
              <div class="book-3d-wrapper relative w-40 lg:w-48 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/book-alchemised.jpg" alt="Alchemised" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-3 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-cover-back"></div>
                <div class="book-page-underneath absolute inset-0 rounded-r-md p-4 flex flex-col justify-between text-slate-900 shadow-inner -z-10">
                  <div>
                    <div class="flex items-center justify-between border-b border-amber-900/15 pb-1">
                      <span class="font-serif text-[11px] font-bold text-amber-900 uppercase tracking-wider">The Principle • Part 1</span>
                      <span class="text-[9px] font-mono text-slate-400">Page 1</span>
                    </div>
                    <h5 class="font-serif text-xs font-bold text-slate-900 mt-2">Alchemised: Self-Transformation</h5>
                    <p class="font-serif text-[10px] leading-relaxed italic text-slate-700 mt-1">
                      "To transmute one's suffering is the oldest art known to conscious existence. The gold was never found in the ground; it was always forged within the human spirit..."
                    </p>
                    <div class="mt-2 text-[9px] text-amber-800 font-medium">★ Modern Philosophy Classic</div>
                  </div>
                  <button onclick="event.stopPropagation(); openPodiumQuickView();" class="w-full bg-[#D99B26] hover:bg-[#B88019] text-white py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors shadow-sm">
                    Read Full Preview
                  </button>
                </div>
              </div>
            </div>

            <!-- Book 4: Ratan Tata -->
            <div class="podium-book-card absolute cursor-pointer" data-index="4" onclick="selectPodiumBook(4)">
              <div class="book-3d-wrapper relative w-40 lg:w-48 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/book-ratan-tata.jpg" alt="Ratan Tata: A Life" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-3 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-cover-back"></div>
                <div class="book-page-underneath absolute inset-0 rounded-r-md p-4 flex flex-col justify-between text-slate-900 shadow-inner -z-10">
                  <div>
                    <div class="flex items-center justify-between border-b border-amber-900/15 pb-1">
                      <span class="font-serif text-[11px] font-bold text-amber-900 uppercase tracking-wider">Prologue • Biography</span>
                      <span class="text-[9px] font-mono text-slate-400">Page 1</span>
                    </div>
                    <h5 class="font-serif text-xs font-bold text-slate-900 mt-2">Ratan Tata: A Life</h5>
                    <p class="font-serif text-[10px] leading-relaxed italic text-slate-700 mt-1">
                      "I never believed in taking right decisions. I took decisions and then made them right. In the quiet corridors of Bombay House, integrity was never a policy; it was breathing..."
                    </p>
                    <div class="mt-2 text-[9px] text-amber-800 font-medium">★ Official Authorized Memoir</div>
                  </div>
                  <button onclick="event.stopPropagation(); openPodiumQuickView();" class="w-full bg-[#D99B26] hover:bg-[#B88019] text-white py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors shadow-sm">
                    Read Full Preview
                  </button>
                </div>
              </div>
            </div>

          </div>

          <!-- Flip Cover Hint & Toggle -->
          <div class="absolute bottom-2 inset-x-0 flex items-center justify-center gap-2">
            <button onclick="togglePodiumCoverOpen()" class="flex items-center gap-1.5 text-xs text-amber-900 font-bold bg-amber-100 hover:bg-amber-200 border border-amber-300 rounded-full px-4 py-1 transition-all shadow-sm">
              <svg class="w-3.5 h-3.5 text-amber-700 animate-spin" style="animation-duration: 4s;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
              <span id="flipCoverBtnText">Hover or Click Book to Open Cover (-140°)</span>
            </button>
          </div>
        </div>

        <!-- Carousel Indicators & Arrow Controls -->
        <div class="flex items-center gap-4 mt-3">
          <button onclick="prevPodiumBook()" class="p-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-amber-50 hover:border-amber-400 shadow-sm transition-all" title="Previous Book">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
          </button>
          <div class="flex items-center gap-2" id="podiumIndicators">
            <button class="w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300" onclick="selectPodiumBook(0)" aria-label="Book 1"></button>
            <button class="w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300" onclick="selectPodiumBook(1)" aria-label="Book 2"></button>
            <button class="w-7 h-2.5 rounded-full bg-[#D99B26] transition-all duration-300" onclick="selectPodiumBook(2)" aria-label="Book 3"></button>
            <button class="w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300" onclick="selectPodiumBook(3)" aria-label="Book 4"></button>
            <button class="w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300" onclick="selectPodiumBook(4)" aria-label="Book 5"></button>
          </div>
          <button onclick="nextPodiumBook()" class="p-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-amber-50 hover:border-amber-400 shadow-sm transition-all" title="Next Book">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
          </button>
        </div>
      </div>

      <!-- RIGHT 5 COLS: Live Editorial Spotlight Panel -->
      <div class="lg:col-span-5 bg-white border border-amber-900/10 rounded-2xl p-6 lg:p-8 shadow-xl relative overflow-hidden flex flex-col justify-between" id="podiumSpotlightPanel">
        <div class="absolute -top-12 -right-12 w-28 h-28 bg-amber-400/15 rounded-full blur-xl pointer-events-none"></div>

        <div>
          <div class="flex items-center justify-between mb-3">
            <span id="spotlightRank" class="text-xs font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-2.5 py-1 rounded font-sans">
              #1 IN CONTEMPORARY HINDI FICTION
            </span>
            <span id="spotlightStock" class="flex items-center gap-1.5 text-xs text-emerald-700 font-semibold font-sans">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
              22 copies in Prayagraj
            </span>
          </div>

          <!-- Book Title -->
          <h3 id="spotlightTitle" class="font-serif text-2xl lg:text-3xl font-bold text-[#0A1128] leading-tight">
            Kasaibada
          </h3>

          <!-- Author -->
          <div class="flex items-center gap-2 mt-1.5 text-slate-600 text-sm font-sans">
            <span>By</span>
            <span id="spotlightAuthor" class="font-bold text-slate-900">Manoj Rajan Tripathi</span>
            <span class="text-amber-500">★</span>
            <span id="spotlightRating" class="font-semibold text-slate-700 text-xs">4.9 (540+ reviews)</span>
          </div>

          <!-- Mini Overview / Editorial Synopsis -->
          <div class="mt-4 p-4 bg-[#FAF8F5] border-l-4 border-[#D99B26] rounded-r-lg">
            <div class="text-[11px] uppercase font-bold text-amber-900 tracking-wider mb-1 flex items-center gap-1 font-sans">
              <span>Why India is Reading This:</span>
            </div>
            <p id="spotlightQuote" class="text-xs lg:text-sm text-slate-700 italic font-serif leading-relaxed">
              "A gripping social allegory on power structures, moral struggle, and raw human resilience in northern India."
            </p>
          </div>

          <!-- Specifications badges -->
          <div class="grid grid-cols-2 gap-2 mt-4 text-[11px] text-slate-600 font-sans">
            <div class="bg-slate-50 p-2.5 rounded-lg border border-slate-200">
              <span class="text-slate-400 block text-[9px] uppercase font-bold tracking-wider">Format & Binding</span>
              <span id="spotlightPages" class="font-bold text-slate-800">192 Pages • Paperback</span>
            </div>
            <div class="bg-slate-50 p-2.5 rounded-lg border border-slate-200">
              <span class="text-slate-400 block text-[9px] uppercase font-bold tracking-wider">Publisher Edition</span>
              <span id="spotlightPublisher" class="font-bold text-slate-800">Vani Prakashan</span>
            </div>
          </div>

          <!-- Pricing Row -->
          <div class="mt-6 flex items-baseline gap-3">
            <span id="spotlightPrice" class="text-3xl font-bold text-[#0A1128] font-serif">₹299.00</span>
            <span id="spotlightMRP" class="text-sm text-slate-400 line-through font-serif">₹395.00</span>
            <span id="spotlightSave" class="text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded font-sans">
              24% OFF
            </span>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row gap-3">
          <button id="spotlightAddCartBtn" onclick="addCurrentPodiumToCart()" class="flex-1 bg-[#D99B26] hover:bg-[#B88019] text-white py-3 px-4 rounded-xl font-bold text-sm transition-all shadow-md flex items-center justify-center gap-2 group font-sans">
            <svg class="w-4 h-4 fill-current group-hover:scale-110 transition-transform" viewBox="0 0 24 24"><path d="M19 6h-2c0-2.76-2.24-5-5-5S7 3.24 7 6H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-7-3c1.66 0 3 1.34 3 3H9c0-1.66 1.34-3 3-3zm7 17H5V8h14v12z"/></svg>
            <span>Add to Cart</span>
          </button>
          <a id="spotlightWhatsAppBtn" href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Kasaibada%20at%20%E2%82%B9299." target="_blank" class="flex-1 bg-[#10B981] hover:bg-[#059669] text-white py-3 px-4 rounded-xl font-bold text-sm transition-all shadow-md flex items-center justify-center gap-2 font-sans">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            <span>WhatsApp COD</span>
          </a>
          <button id="spotlightPreviewBtn" onclick="openPodiumQuickView()" class="p-3 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl transition-colors shrink-0" title="Full Book Details">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
          </button>
        </div>

      </div>

    </div>

  </div>
</section>
"""

# B. MEHFIL-E-REKHTA (Clean vertical flex stack, NO text cut off, mini overviews, All Poets tab)
mehfil_section_html = """
<!-- ======================================================================= -->
<!-- SECTION 3: "MEHFIL-E-REKHTA" IMMERSIVE DARK POETRY LOUNGE                -->
<!-- ======================================================================= -->
<section id="mehfil-rekhta" class="bg-gradient-to-b from-[#0F172A] via-[#1E1424] to-[#0A1128] text-amber-50 py-24 relative overflow-hidden">
  <!-- Anchor Alias -->
  <div id="mehfilRekhtaSection"></div>

  <!-- Ambient Floating Golden Dust Sparks -->
  <div class="absolute inset-0 pointer-events-none opacity-40">
    <div class="particle-spark absolute top-10 left-[15%] w-1.5 h-1.5 bg-amber-400 rounded-full blur-[1px] animate-pulse"></div>
    <div class="particle-spark absolute top-32 right-[20%] w-2 h-2 bg-amber-300 rounded-full blur-[1px] animate-pulse" style="animation-delay: 1.2s"></div>
    <div class="particle-spark absolute bottom-24 left-[25%] w-1.5 h-1.5 bg-amber-400 rounded-full blur-[1px] animate-pulse" style="animation-delay: 2.1s"></div>
    <div class="particle-spark absolute bottom-40 right-[12%] w-2 h-2 bg-amber-200 rounded-full blur-[1px] animate-pulse" style="animation-delay: 0.7s"></div>
  </div>

  <!-- Parallax Calligraphy Watermark in Background -->
  <div class="absolute inset-0 flex items-center justify-center opacity-[0.04] select-none pointer-events-none">
    <span class="font-serif text-8xl md:text-9xl lg:text-[13rem] tracking-widest text-amber-200 whitespace-nowrap">
      शायरी • दास्तान • अदब
    </span>
  </div>

  <div class="max-w-7xl mx-auto px-6 lg:px-8 relative z-10">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-900/40 text-amber-300 border border-amber-500/30 px-4 py-1 rounded-full text-xs font-bold tracking-widest uppercase shadow-lg font-sans">
        <span>महेफ़िल-ए-रेख़्ख़ता</span>
        <span>•</span>
        <span>MEHFIL-E-REKHTA</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-5xl font-bold text-amber-100 mt-3 tracking-wide">
        Urdu Poetry, Timeless Shayari & Progressive Literary Classics
      </h2>
      <p class="text-sm lg:text-base text-amber-200/80 mt-3 max-w-2xl mx-auto leading-relaxed font-sans">
        Step into an intimate literary mehfil featuring official Rekhta editions, rebellious prose, and the finest verse of the subcontinent.
      </p>
    </div>

    <!-- Interactive Shayar Quote Switcher with ALL POETS tab -->
    <div class="mt-10 mb-12">
      <!-- Poet Selectable Pills -->
      <div class="flex flex-wrap items-center justify-center gap-3" id="poetSelectorPills">
        <button onclick="filterMehfilPoet('all')" class="poet-pill active px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/50 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(217,155,38,0.3)] transition-all font-sans">
          All Poets (सब शो'रा)
        </button>
        <button onclick="filterMehfilPoet('elia')" class="poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all font-sans">
          Jaun Elia
        </button>
        <button onclick="filterMehfilPoet('faraz')" class="poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all font-sans">
          Ahmad Faraz
        </button>
        <button onclick="filterMehfilPoet('manto')" class="poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all font-sans">
          Saadat Hasan Manto
        </button>
        <button onclick="filterMehfilPoet('ghalib')" class="poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all font-sans">
          Mirza Ghalib
        </button>
      </div>

      <!-- Dynamic Couplet Display Card -->
      <div class="max-w-3xl mx-auto mt-6 bg-white/[0.04] backdrop-blur-md border border-amber-500/30 rounded-2xl p-6 lg:p-8 shadow-2xl relative" id="poetQuoteCard">
        <div class="text-amber-400/30 text-5xl font-serif absolute top-4 left-6 select-none">“</div>
        <div class="text-center px-4 py-2 relative z-10">
          <div id="poetUrduVerse" class="font-serif text-2xl lg:text-3xl text-amber-200 font-normal leading-relaxed tracking-wide transition-opacity duration-300">
            شاید مجھے نکال کے پچھتا رہے ہوں آپ • محفل میں اس خیال سے پھر آ گیا ہوں میں
          </div>
          <div id="poetHindiVerse" class="text-sm lg:text-base text-amber-100/90 font-serif mt-2 transition-opacity duration-300">
            "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं"
          </div>
          <div id="poetEngVerse" class="text-xs text-amber-300/70 italic mt-2 max-w-xl mx-auto transition-opacity duration-300 font-sans">
            Perhaps you regret having cast me out; it is merely with this thought that I returned to the gathering.
          </div>
          <div class="mt-4 pt-3 border-t border-amber-500/20 inline-flex items-center gap-2">
            <span class="w-6 h-[1px] bg-amber-400/50"></span>
            <span id="poetAttribution" class="text-xs font-bold uppercase tracking-widest text-amber-400 font-sans">
              — Jaun Elia (क़तील-ए-अना)
            </span>
            <span class="w-6 h-[1px] bg-amber-400/50"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- ZERO TEXT CUTOFF: Clean Vertical Flex Stack Gallery (5 Books) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 mt-12" id="rekhtaCardsContainer">
      
      <!-- Card 1: Kyon (Jaun Elia) -->
      <div class="rekhta-book-card bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-300 flex flex-col justify-between group" data-poet="elia">
        <div>
          <!-- Dedicated Cover Container (Zero Text Overlap) -->
          <div class="h-56 flex items-center justify-center mb-3 relative">
            <div class="w-32 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
              <img src="assets/book-kyon-jaun-elia.jpg" alt="Kyon - Jaun Elia" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/70 to-transparent"></div>
            </div>
          </div>

          <!-- Metadata Cleanly BELOW Image -->
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest font-sans">Urdu Poetry • Rekhta</div>
          <h4 class="font-serif text-lg font-bold text-white mt-1 leading-snug group-hover:text-amber-300 transition-colors">
            क्यों (Kyon)
          </h4>
          <p class="text-xs text-amber-200/80 font-sans mt-0.5">Jaun Elia</p>

          <!-- 2-Line Mini Overview -->
          <p class="text-xs leading-relaxed text-slate-300 line-clamp-2 mt-2 mb-3 font-sans">
            An intimate anthology of Jaun Elia's most piercing ghazals on existential longing, heartbreak, and philosophical rebellion.
          </p>
        </div>

        <div class="pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between mb-3">
            <span class="font-serif text-lg font-bold text-amber-300">₹350.00</span>
            <span class="text-[11px] text-amber-400 font-sans font-semibold">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('mehfil-1', 'क्यों (Kyon) - Jaun Elia', 350, 'assets/book-kyon-jaun-elia.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1 font-sans">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Kyon%20by%20Jaun%20Elia%20(%E2%82%B9350)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs py-2 rounded-lg transition-colors text-center font-sans">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 2: Ranjish Hi Sahi (Ahmad Faraz) -->
      <div class="rekhta-book-card bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-300 flex flex-col justify-between group" data-poet="faraz">
        <div>
          <div class="h-56 flex items-center justify-center mb-3 relative">
            <div class="w-32 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
              <img src="assets/book-ranjish-hi-sahi.jpg" alt="Ranjish Hi Sahi" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/70 to-transparent"></div>
            </div>
          </div>

          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest font-sans">Ghazal Collection</div>
          <h4 class="font-serif text-lg font-bold text-white mt-1 leading-snug group-hover:text-amber-300 transition-colors">
            रंजिश ही सही (Ranjish Hi Sahi)
          </h4>
          <p class="text-xs text-amber-200/80 font-sans mt-0.5">Ahmad Faraz</p>

          <p class="text-xs leading-relaxed text-slate-300 line-clamp-2 mt-2 mb-3 font-sans">
            Timeless Urdu romantic poetry and iconic ghazals celebrating love, separation, melancholy, and resilience.
          </p>
        </div>

        <div class="pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between mb-3">
            <span class="font-serif text-lg font-bold text-amber-300">₹399.00</span>
            <span class="text-[11px] text-amber-400 font-sans font-semibold">★ 5.0</span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('mehfil-2', 'रंजिश ही सही - Ahmad Faraz', 399, 'assets/book-ranjish-hi-sahi.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1 font-sans">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Ranjish%20Hi%20Sahi%20(%E2%82%B9399)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs py-2 rounded-lg transition-colors text-center font-sans">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 3: Dozakhnama (Manto & Ghalib) -->
      <div class="rekhta-book-card bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-300 flex flex-col justify-between group" data-poet="ghalib">
        <div>
          <div class="h-56 flex items-center justify-center mb-3 relative">
            <div class="w-32 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
              <img src="assets/hero-book-dozakh.jpg" alt="Dozakh Nama" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/70 to-transparent"></div>
            </div>
          </div>

          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest font-sans">Literary Fiction</div>
          <h4 class="font-serif text-lg font-bold text-white mt-1 leading-snug group-hover:text-amber-300 transition-colors">
            दोज़ख़नामा (Dozakhnama)
          </h4>
          <p class="text-xs text-amber-200/80 font-sans mt-0.5">Rabisankar Bal</p>

          <p class="text-xs leading-relaxed text-slate-300 line-clamp-2 mt-2 mb-3 font-sans">
            A spellbinding posthumous conversation between Mirza Ghalib and Saadat Hasan Manto speaking from their graves.
          </p>
        </div>

        <div class="pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between mb-3">
            <span class="font-serif text-lg font-bold text-amber-300">₹450.00</span>
            <span class="text-[11px] text-amber-400 font-sans font-semibold">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('mehfil-3', 'दोज़ख़नामा (Dozakhnama)', 450, 'assets/hero-book-dozakh.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1 font-sans">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Dozakh%20Nama%20(%E2%82%B9450)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs py-2 rounded-lg transition-colors text-center font-sans">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 4: Thanda Gosht (Manto) -->
      <div class="rekhta-book-card bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-300 flex flex-col justify-between group" data-poet="manto">
        <div>
          <div class="h-56 flex items-center justify-center mb-3 relative">
            <div class="w-32 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
              <img src="assets/hero-book-thanda-ghost.jpg" alt="Thanda Ghost" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/70 to-transparent"></div>
            </div>
          </div>

          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest font-sans">Progressive Stories</div>
          <h4 class="font-serif text-lg font-bold text-white mt-1 leading-snug group-hover:text-amber-300 transition-colors">
            ठंडा गोश्त (Thanda Gosht)
          </h4>
          <p class="text-xs text-amber-200/80 font-sans mt-0.5">Saadat Hasan Manto</p>

          <p class="text-xs leading-relaxed text-slate-300 line-clamp-2 mt-2 mb-3 font-sans">
            Unflinching, masterfully crafted short stories dissecting human psychology during the Partition of India.
          </p>
        </div>

        <div class="pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between mb-3">
            <span class="font-serif text-lg font-bold text-amber-300">₹299.00</span>
            <span class="text-[11px] text-amber-400 font-sans font-semibold">★ 4.8</span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('mehfil-4', 'ठंडा गोश्त - Manto', 299, 'assets/hero-book-thanda-ghost.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1 font-sans">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Thanda%20Ghost%20(%E2%82%B9299)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs py-2 rounded-lg transition-colors text-center font-sans">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 5: Dhuaan (Manto) -->
      <div class="rekhta-book-card bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-300 flex flex-col justify-between group" data-poet="manto">
        <div>
          <div class="h-56 flex items-center justify-center mb-3 relative">
            <div class="w-32 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
              <img src="assets/hero-book-dhuaan.jpg" alt="Dhuaan" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/70 to-transparent"></div>
            </div>
          </div>

          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest font-sans">Urdu Classics</div>
          <h4 class="font-serif text-lg font-bold text-white mt-1 leading-snug group-hover:text-amber-300 transition-colors">
            धुआँ (Dhuaan)
          </h4>
          <p class="text-xs text-amber-200/80 font-sans mt-0.5">Saadat Hasan Manto</p>

          <p class="text-xs leading-relaxed text-slate-300 line-clamp-2 mt-2 mb-3 font-sans">
            Raw, evocative tales of adolescence, society, and unspoken truths by South Asia's greatest short story writer.
          </p>
        </div>

        <div class="pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between mb-3">
            <span class="font-serif text-lg font-bold text-amber-300">₹350.00</span>
            <span class="text-[11px] text-amber-400 font-sans font-semibold">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('mehfil-5', 'धुआँ (Dhuaan) - Manto', 350, 'assets/hero-book-dhuaan.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1 font-sans">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Dhuaan%20(%E2%82%B9350)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs py-2 rounded-lg transition-colors text-center font-sans">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>
"""

# C. BUNDLE UNBOXING SHOWCASE (With mini overviews & smooth scroll target)
bundle_section_html = """
<!-- ======================================================================= -->
<!-- SECTION 4: INTERACTIVE "BUNDLE UNBOXING" SHOWCASE                        -->
<!-- ======================================================================= -->
<section id="bundles-section" class="py-20 lg:py-24 bg-[#F4EFE6] border-y border-amber-900/10 relative overflow-hidden">
  <!-- Anchor Alias -->
  <div id="bundleUnboxingSection"></div>

  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 bg-amber-200/70 text-amber-900 border border-amber-400/40 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm font-sans">
        <svg class="w-3.5 h-3.5 fill-current text-amber-800" viewBox="0 0 24 24"><path d="M21 16.5l-9 5.25L3 16.5v-9l9-5.25 9 5.25v9zM12 3.75L4.5 8.1 12 12.45l7.5-4.35L12 3.75zM4.5 9.9v6.6l6.75 3.9v-6.6L4.5 9.9zm8.25 10.5l6.75-3.9V9.9l-6.75 3.9v6.6z"/></svg>
        <span>COLLECTOR'S CORNER & BOX SETS</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3">
        The Unboxing Showcase: Curated Multi-Volume Sets
      </h2>
      <p class="text-sm lg:text-base text-slate-600 mt-2 font-sans">
        Hover over any collector's box to unpack the editions and inspect the individual titles inside.
      </p>
    </div>

    <!-- 3 Oversized Feature Bundle Cards -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      
      <!-- BUNDLE 1: Arundhati Roy Definitive Double Feature -->
      <div class="bg-white border border-[#E4DAC7] rounded-2xl p-6 lg:p-7 shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group/bundle">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded-full font-sans">
              Man Booker Winner Set
            </span>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full font-sans">
              Save ₹399 Instantly
            </span>
          </div>

          <h3 class="font-serif text-xl font-bold text-[#0A1128] mt-2 group-hover/bundle:text-[#D99B26] transition-colors leading-snug">
            Arundhati Roy Definitive Duo
          </h3>
          <p class="text-xs text-slate-500 mt-1 font-sans">2 Complete Novels in Illustrated Slipcase</p>

          <!-- 2-Line Mini Overview -->
          <p class="text-xs text-slate-600 leading-relaxed line-clamp-2 mt-2 font-sans">
            Experience the complete literary breadth of Booker prize-winner Arundhati Roy with two monumental masterpieces in one commemorative set.
          </p>

          <!-- Interactive Unbox on Hover Stage -->
          <div class="bundle-unbox-stage relative h-60 flex items-center justify-center my-5 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-amber-900/10 border-2 border-dashed border-amber-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-bold text-amber-900/40 uppercase tracking-widest font-sans">Collector Slipcase</span>
            </div>

            <!-- Fanned Books -->
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="assets/hero-book-arundhati.jpg" alt="The God of Small Things" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="assets/book-cheelwali-kothi.jpg" alt="The Ministry of Utmost Happiness" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
          </div>

          <!-- Included Titles Checklist -->
          <div class="space-y-1.5 text-xs text-slate-600 bg-amber-50/60 p-3 rounded-lg border border-amber-200/50 font-sans">
            <div class="flex items-center gap-2">
              <span class="text-emerald-600 font-bold">✓</span>
              <span>The God of Small Things (Silver Jubilee Edition)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-600 font-bold">✓</span>
              <span>The Ministry of Utmost Happiness (Hardcover)</span>
            </div>
          </div>
        </div>

        <div class="mt-6 pt-4 border-t border-slate-100">
          <div class="flex items-baseline justify-between mb-4">
            <div>
              <span class="text-2xl font-bold text-[#0A1128] font-serif">₹799.00</span>
              <span class="text-xs text-slate-400 line-through ml-2 font-serif">₹1,198.00</span>
            </div>
            <span class="text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded font-sans">
              33% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2 font-sans">
            <button onclick="addToCart('bundle-1', 'Arundhati Roy Definitive Duo Boxset', 799, 'assets/hero-book-arundhati.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Arundhati%20Roy%20Duo%20Boxset%20(%E2%82%B9799)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- BUNDLE 2: Sarah J. Maas – ACOTAR 5-Book Boxset -->
      <div class="bg-white border border-[#E4DAC7] rounded-2xl p-6 lg:p-7 shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group/bundle">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-purple-900 bg-purple-100 border border-purple-300 px-2.5 py-0.5 rounded-full font-sans">
              Global BookTok Sensation
            </span>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full font-sans">
              Save ₹1,100 Instantly
            </span>
          </div>

          <h3 class="font-serif text-xl font-bold text-[#0A1128] mt-2 group-hover/bundle:text-[#D99B26] transition-colors leading-snug">
            A Court of Thorns and Roses 5-Book Set
          </h3>
          <p class="text-xs text-slate-500 mt-1 font-sans">Complete Sarah J. Maas Fantasy Boxset</p>

          <p class="text-xs text-slate-600 leading-relaxed line-clamp-2 mt-2 font-sans">
            The full immersive romantic fantasy saga tracing Feyre's breathtaking journey through the treacherous, magical High Courts of Prythian.
          </p>

          <!-- Interactive Unbox on Hover Stage -->
          <div class="bundle-unbox-stage relative h-60 flex items-center justify-center my-5 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-purple-900/10 border-2 border-dashed border-purple-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-bold text-purple-900/40 uppercase tracking-widest font-sans">5 Volumes Pack</span>
            </div>

            <!-- Fanned Books -->
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="assets/book-acotar.jpg" alt="ACOTAR Volume 1" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-mid absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="assets/book-alchemised.jpg" alt="ACOTAR Volume 2" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-30">
              <img src="assets/book-acotar.jpg" alt="ACOTAR Volume 3" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
          </div>

          <div class="space-y-1.5 text-xs text-slate-600 bg-purple-50/60 p-3 rounded-lg border border-purple-200/50 font-sans">
            <div class="flex items-center gap-2">
              <span class="text-emerald-600 font-bold">✓</span>
              <span>All 5 Novels: ACOTAR, ACOMAF, ACOWAR, ACOFAS, ACOSF</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-600 font-bold">✓</span>
              <span>Official Bloomsbury Boxset with Special Art Case</span>
            </div>
          </div>
        </div>

        <div class="mt-6 pt-4 border-t border-slate-100">
          <div class="flex items-baseline justify-between mb-4">
            <div>
              <span class="text-2xl font-bold text-[#0A1128] font-serif">₹1,899.00</span>
              <span class="text-xs text-slate-400 line-through ml-2 font-serif">₹2,999.00</span>
            </div>
            <span class="text-xs font-bold text-purple-800 bg-purple-100 border border-purple-300 px-2 py-0.5 rounded font-sans">
              37% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2 font-sans">
            <button onclick="addToCart('bundle-2', 'A Court of Thorns and Roses 5-Book Boxset', 1899, 'assets/book-acotar.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20ACOTAR%20Boxset%20(%E2%82%B91899)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- BUNDLE 3: Haruki Murakami 3-Book Collector's Set -->
      <div class="bg-white border border-[#E4DAC7] rounded-2xl p-6 lg:p-7 shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group/bundle">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-rose-900 bg-rose-100 border border-rose-300 px-2.5 py-0.5 rounded-full font-sans">
              Modern Japanese Master
            </span>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full font-sans">
              Save ₹600 Instantly
            </span>
          </div>

          <h3 class="font-serif text-xl font-bold text-[#0A1128] mt-2 group-hover/bundle:text-[#D99B26] transition-colors leading-snug">
            Best of Haruki Murakami (3 Books)
          </h3>
          <p class="text-xs text-slate-500 mt-1 font-sans">Vintage Classics Commemorative Set</p>

          <p class="text-xs text-slate-600 leading-relaxed line-clamp-2 mt-2 font-sans">
            Three era-defining metaphysical novels blending dreamlike surrealism, jazz, love, and isolation in modern Tokyo.
          </p>

          <!-- Interactive Unbox on Hover Stage -->
          <div class="bundle-unbox-stage relative h-60 flex items-center justify-center my-5 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-rose-900/10 border-2 border-dashed border-rose-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-bold text-rose-900/40 uppercase tracking-widest font-sans">Murakami Box</span>
            </div>

            <!-- Fanned Books -->
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="assets/hero-book-murakami.jpg" alt="Norwegian Wood" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="assets/book-ratan-tata.jpg" alt="Kafka on the Shore" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
          </div>

          <div class="space-y-1.5 text-xs text-slate-600 bg-rose-50/60 p-3 rounded-lg border border-rose-200/50 font-sans">
            <div class="flex items-center gap-2">
              <span class="text-emerald-600 font-bold">✓</span>
              <span>Norwegian Wood + Kafka on the Shore + 1Q84</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-600 font-bold">✓</span>
              <span>Vintage Red/Black Cover Artworks</span>
            </div>
          </div>
        </div>

        <div class="mt-6 pt-4 border-t border-slate-100">
          <div class="flex items-baseline justify-between mb-4">
            <div>
              <span class="text-2xl font-bold text-[#0A1128] font-serif">₹1,299.00</span>
              <span class="text-xs text-slate-400 line-through ml-2 font-serif">₹1,899.00</span>
            </div>
            <span class="text-xs font-bold text-rose-800 bg-rose-100 border border-rose-300 px-2 py-0.5 rounded font-sans">
              32% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2 font-sans">
            <button onclick="addToCart('bundle-3', 'Best of Haruki Murakami 3-Book Set', 1299, 'assets/hero-book-murakami.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Murakami%203-Book%20Boxset%20(%E2%82%B91299)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>
"""

# D. REGIONAL MAGAZINE (Unified typography, mini overviews on all 4 cards)
regional_section_html = """
<!-- ======================================================================= -->
<!-- SECTION 5: "INDIAN REGIONAL & FICTION" EDITORIAL MAGAZINE MASONRY        -->
<!-- ======================================================================= -->
<section id="regional-fiction" class="py-20 lg:py-24 bg-[#FAF8F5] relative overflow-hidden">
  <!-- Anchor Alias -->
  <div id="regionalMagazineSection"></div>

  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <!-- Section Header -->
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 pb-4 border-b border-amber-900/10 gap-4">
      <div>
        <div class="inline-flex items-center gap-2 bg-amber-100 text-[#D99B26] border border-amber-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase mb-2 font-sans">
          <span>LITERARY SPOTLIGHT • REGIONAL CLASSICS</span>
        </div>
        <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128]">
          Indian Voices & Contemporary Hindi Fiction
        </h2>
        <p class="text-sm text-slate-600 mt-1 max-w-xl font-sans">
          Original Hindi prose, Sahitya Akademi laureates, and evocative tales rooted in the heartlands of India.
        </p>
      </div>
      <a href="#shop-all-catalog" onclick="handleNavClick('Shop All', event)" class="text-xs font-bold uppercase tracking-wider text-[#D99B26] hover:text-[#B88019] inline-flex items-center gap-1 font-sans">
        <span>Explore All 2,000+ Regional Titles</span>
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
      </a>
    </div>

    <!-- Editorial Bento Grid (5 Cols Hero Feature + 7 Cols 2x2 Cards with Mini Overviews) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
      
      <!-- LEFT 5 COLS: Feature Story Card (Cheelwali Kothi) -->
      <div class="lg:col-span-5 bg-white border border-[#E8DFC8] rounded-2xl p-6 lg:p-8 shadow-md hover:shadow-xl transition-all duration-300 flex flex-col justify-between relative group">
        <div>
          <div class="flex items-center justify-between mb-4 font-sans">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-3 py-1 rounded-full">
              Prayagraj Literary Heritage Pick
            </span>
            <span class="text-[11px] font-bold text-rose-700 bg-rose-50 border border-rose-200 px-2.5 py-0.5 rounded-full">
              Only 4 copies left
            </span>
          </div>

          <div class="w-44 lg:w-48 mx-auto aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_40px_rgba(0,0,0,0.4)] my-4 group-hover:scale-105 transition-transform duration-300 relative">
            <img src="assets/book-cheelwali-kothi.jpg" alt="Cheelwali Kothi - Sara Rai" class="w-full h-full object-cover">
            <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
          </div>

          <h3 class="font-serif text-2xl font-bold text-[#0A1128] text-center mt-3 group-hover:text-[#D99B26] transition-colors leading-tight">
            चीलवाली कोठी (Cheelwali Kothi)
          </h3>
          <p class="text-xs text-slate-500 text-center mt-0.5 font-sans font-medium">By Sara Rai • Rajkamal Prakashan</p>

          <div class="mt-4 p-4 bg-[#FAF8F5] border-l-2 border-amber-500 rounded-r-lg">
            <p class="font-serif italic text-xs lg:text-sm text-slate-700 leading-relaxed">
              "A haunting, lyrical masterpiece navigating ancestral mansions, lost memories, and the quiet dignity of Uttar Pradesh."
            </p>
          </div>

          <div class="text-[11px] text-slate-500 text-center mt-3 font-sans">
            <span>Paperback • 248 Pages • Hindi Literature</span>
          </div>
        </div>

        <div class="mt-6 pt-4 border-t border-slate-100">
          <div class="flex items-baseline justify-between mb-4">
            <div>
              <span class="text-2xl font-bold text-[#0A1128] font-serif">₹299.00</span>
              <span class="text-xs text-slate-400 line-through ml-2 font-serif">₹395.00</span>
            </div>
            <span class="text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded font-sans">
              24% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2 font-sans">
            <button onclick="addToCart('reg-hero', 'चीलवाली कोठी (Cheelwali Kothi)', 299, 'assets/book-cheelwali-kothi.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Cheelwali%20Kothi%20(%E2%82%B9299)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-bold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- RIGHT 7 COLS: 2x2 Grid of Cards with Unified Typography & Mini Overviews -->
      <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-5">
        
        <!-- Card 1: Nar Nareeshwar -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div>
            <div class="flex gap-4">
              <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
                <img src="assets/book-nar-nareeshwar.jpg" alt="Nar Nareeshwar" class="w-full h-full object-cover">
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between text-[10px] font-sans font-semibold text-slate-400">
                  <span>#IND-0824</span>
                  <span class="text-rose-600 font-bold border border-rose-300 px-1.5 rounded text-[9px]">25% OFF</span>
                </div>
                <h4 class="font-serif text-base font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors leading-snug">
                  नर-नारीश्वर
                </h4>
                <p class="text-[11px] text-slate-600 font-sans">Vishnu Prabhakar</p>
                <div class="text-[10px] text-amber-800 font-sans font-semibold mt-0.5">Sahitya Akademi Winner</div>
                <div class="mt-1 text-sm font-bold text-slate-900 font-serif">₹320.00 <span class="text-[10px] text-slate-400 line-through">₹425</span></div>
              </div>
            </div>
            <!-- Mini Overview -->
            <p class="text-[11px] text-slate-600 leading-relaxed line-clamp-2 mt-3 font-sans">
              A profound, Sahitya Akademi-winning exploration of gender duality, human compassion, and psychological depth.
            </p>
          </div>

          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2 font-sans">
            <button onclick="addToCart('index-1', 'नर-नारीश्वर - Vishnu Prabhakar', 320, 'assets/book-nar-nareeshwar.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-bold transition-colors">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Nar-Nareeshwar%20(%E2%82%B9320)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 2: Patthar aur Alpatthar -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div>
            <div class="flex gap-4">
              <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
                <img src="assets/book-patthar-alpatthar.jpg" alt="Patthar aur Alpatthar" class="w-full h-full object-cover">
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between text-[10px] font-sans font-semibold text-slate-400">
                  <span>#IND-0912</span>
                  <span class="text-rose-600 font-bold border border-rose-300 px-1.5 rounded text-[9px]">20% OFF</span>
                </div>
                <h4 class="font-serif text-base font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors leading-snug">
                  पत्थर और अलपत्थर
                </h4>
                <p class="text-[11px] text-slate-600 font-sans">Surendra Verma</p>
                <div class="text-[10px] text-amber-800 font-sans font-semibold mt-0.5">Acclaimed Hindi Play</div>
                <div class="mt-1 text-sm font-bold text-slate-900 font-serif">₹240.00 <span class="text-[10px] text-slate-400 line-through">₹300</span></div>
              </div>
            </div>
            <p class="text-[11px] text-slate-600 leading-relaxed line-clamp-2 mt-3 font-sans">
              A celebrated Hindi theatrical drama dissecting social hypocrisy, power politics, and artistic expression.
            </p>
          </div>

          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2 font-sans">
            <button onclick="addToCart('index-2', 'पत्थर और अलपत्थर - Surendra Verma', 240, 'assets/book-patthar-alpatthar.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-bold transition-colors">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Patthar%20aur%20Alpatthar%20(%E2%82%B9240)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 3: Aurat Farosh -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div>
            <div class="flex gap-4">
              <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
                <img src="assets/book-aurat-farosh.jpg" alt="Aurat Farosh" class="w-full h-full object-cover">
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between text-[10px] font-sans font-semibold text-slate-400">
                  <span>#IND-0741</span>
                  <span class="text-rose-600 font-bold border border-rose-300 px-1.5 rounded text-[9px]">22% OFF</span>
                </div>
                <h4 class="font-serif text-base font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors leading-snug">
                  औरत फ़रोश
                </h4>
                <p class="text-[11px] text-slate-600 font-sans">Kanhaiyalal Nandan</p>
                <div class="text-[10px] text-amber-800 font-sans font-semibold mt-0.5">Social Investigative Fiction</div>
                <div class="mt-1 text-sm font-bold text-slate-900 font-serif">₹280.00 <span class="text-[10px] text-slate-400 line-through">₹360</span></div>
              </div>
            </div>
            <p class="text-[11px] text-slate-600 leading-relaxed line-clamp-2 mt-3 font-sans">
              A searing investigative narrative exposing the shadows of exploitation and human trafficking in urban society.
            </p>
          </div>

          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2 font-sans">
            <button onclick="addToCart('index-3', 'औरत फ़रोश - Kanhaiyalal Nandan', 280, 'assets/book-aurat-farosh.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-bold transition-colors">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Aurat%20Farosh%20(%E2%82%B9280)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 4: Lagbhag Single -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div>
            <div class="flex gap-4">
              <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
                <img src="assets/book-lagbhag-single.jpg" alt="Lagbhag Single" class="w-full h-full object-cover">
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between text-[10px] font-sans font-semibold text-slate-400">
                  <span>#IND-0533</span>
                  <span class="text-rose-600 font-bold border border-rose-300 px-1.5 rounded text-[9px]">28% OFF</span>
                </div>
                <h4 class="font-serif text-base font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors leading-snug">
                  लगभग सिंगल
                </h4>
                <p class="text-[11px] text-slate-600 font-sans">Nikhil Sachan</p>
                <div class="text-[10px] text-amber-800 font-sans font-semibold mt-0.5">Kanpur Chronicles</div>
                <div class="mt-1 text-sm font-bold text-slate-900 font-serif">₹250.00 <span class="text-[10px] text-slate-400 line-through">₹350</span></div>
              </div>
            </div>
            <p class="text-[11px] text-slate-600 leading-relaxed line-clamp-2 mt-3 font-sans">
              A sharp, witty collection of modern North Indian youth chronicles navigating romance, career, and small-town roots.
            </p>
          </div>

          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2 font-sans">
            <button onclick="addToCart('index-4', 'लगभग सिंगल - Nikhil Sachan', 250, 'assets/book-lagbhag-single.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-bold transition-colors">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Lagbhag%20Single%20(%E2%82%B9250)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

      </div>

    </div>

  </div>
</section>
"""

# E. ACADEMIC VAULT (With 2-line mini overviews on every card + functional drawer tabs)
vault_section_html = """
<!-- ======================================================================= -->
<!-- SECTION 6: INTERACTIVE "LAW & ACADEMIC VAULT" SPLIT-FINDER               -->
<!-- ======================================================================= -->
<section id="law-academic-vault" class="py-20 lg:py-24 bg-white border-y border-slate-200 relative">
  <!-- Anchor Alias -->
  <div id="academicVaultSection"></div>

  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto mb-12">
      <div class="inline-flex items-center gap-2 bg-slate-100 text-slate-800 border border-slate-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm font-sans">
        <svg class="w-3.5 h-3.5 fill-current text-slate-700" viewBox="0 0 24 24"><path d="M12 2L1 21h22L12 2zm0 3.8l7.53 13.2H4.47L12 5.8zM11 10v4h2v-4h-2zm0 6v2h2v-2h-2z"/></svg>
        <span>ACADEMIC & SCHOLARLY VAULT</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3">
        Law, Judiciary & Sahitya Reference Archive
      </h2>
      <p class="text-sm lg:text-base text-slate-600 mt-2 font-sans">
        Authoritative legal treatises, Hindi linguistics, university standards, and competitive civil services references.
      </p>
    </div>

    <!-- Interactive Sticky Two-Pane Vault Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      
      <!-- LEFT 4 COLS: Library Drawer Selector -->
      <div class="lg:col-span-4 lg:sticky lg:top-28 space-y-4">
        
        <div class="bg-[#FAF8F5] border border-amber-900/10 rounded-2xl p-5 shadow-sm font-sans">
          <div class="text-xs uppercase font-bold text-slate-400 tracking-wider mb-3">
            Select Archive Drawer:
          </div>

          <!-- Drawer Tabs -->
          <div class="space-y-2" id="vaultDrawerTabs">
            <button onclick="selectVaultDrawer('law')" class="vault-drawer-btn active w-full text-left p-3.5 rounded-xl border border-transparent font-medium text-sm transition-all flex items-center justify-between">
              <div class="flex items-center gap-3">
                <span class="text-lg">⚖️</span>
                <div>
                  <div class="font-bold text-inherit leading-tight">Law & Jurisprudence</div>
                  <div class="text-[11px] opacity-75">Statutes, LexisNexis, Judicial Acts</div>
                </div>
              </div>
              <span class="text-xs font-bold">4 Titles</span>
            </button>

            <button onclick="selectVaultDrawer('sahitya')" class="vault-drawer-btn w-full text-left p-3.5 rounded-xl border border-transparent font-medium text-sm transition-all flex items-center justify-between">
              <div class="flex items-center gap-3">
                <span class="text-lg">🏛️</span>
                <div>
                  <div class="font-bold text-inherit leading-tight">Hindi Sahitya & Vyakaran</div>
                  <div class="text-[11px] opacity-75">Shukla, Nagendra, Linguistics</div>
                </div>
              </div>
              <span class="text-xs font-bold">4 Titles</span>
            </button>

            <button onclick="selectVaultDrawer('prep')" class="vault-drawer-btn w-full text-left p-3.5 rounded-xl border border-transparent font-medium text-sm transition-all flex items-center justify-between">
              <div class="flex items-center gap-3">
                <span class="text-lg">🎓</span>
                <div>
                  <div class="font-bold text-inherit leading-tight">Civil Services & McGraw Hill</div>
                  <div class="text-[11px] opacity-75">UPSC, Judiciary Prelims, GS</div>
                </div>
              </div>
              <span class="text-xs font-bold">3 Titles</span>
            </button>

            <button onclick="selectVaultDrawer('history')" class="vault-drawer-btn w-full text-left p-3.5 rounded-xl border border-transparent font-medium text-sm transition-all flex items-center justify-between">
              <div class="flex items-center gap-3">
                <span class="text-lg">🌍</span>
                <div>
                  <div class="font-bold text-inherit leading-tight">History & Dalit Vimarsh</div>
                  <div class="text-[11px] opacity-75">Social Philosophy, Subaltern</div>
                </div>
              </div>
              <span class="text-xs font-bold">3 Titles</span>
            </button>
          </div>

          <!-- In-Vault Live Search Input -->
          <div class="mt-4 pt-4 border-t border-slate-200">
            <div class="relative">
              <svg class="w-4 h-4 text-slate-400 absolute left-3 top-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
              <input type="text" id="vaultSearchInput" onkeyup="filterVaultBooks(this.value)" placeholder="Search vault titles, authors..." class="w-full text-xs pl-9 pr-3 py-2.5 rounded-lg border border-slate-300 focus:outline-none focus:border-[#D99B26] bg-white">
            </div>
          </div>
        </div>

        <!-- Institutional Order Callout Card -->
        <div class="bg-gradient-to-br from-[#0A1128] to-[#1E293B] text-white rounded-2xl p-5 shadow-md font-sans">
          <div class="text-amber-400 text-xs font-bold uppercase tracking-wider mb-1">
            📚 Bulk & Institutional Supply
          </div>
          <h4 class="font-serif text-sm font-bold">University & Advocate Book Concierge</h4>
          <p class="text-[11px] text-slate-300 mt-1 leading-relaxed">
            Need multiple copies for chambers, bar libraries, or college batches? Get customized quotation with GST invoice.
          </p>
          <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20am%20inquiring%20about%20Institutional%20Bulk%20Academic%20Orders." target="_blank" class="mt-3 inline-flex items-center gap-1.5 bg-[#10B981] hover:bg-[#059669] text-white text-xs font-bold py-2 px-3 rounded-lg transition-colors w-full justify-center">
            <span>Chat for Institutional Discount</span>
          </a>
        </div>

      </div>

      <!-- RIGHT 8 COLS: High-Density Spec-Sheet Catalog Grid with Mini Overviews -->
      <div class="lg:col-span-8">
        
        <div class="flex items-center justify-between pb-3 mb-6 border-b border-slate-200 font-sans">
          <div class="flex items-center gap-2">
            <span id="vaultDrawerActiveTitle" class="font-serif text-lg font-bold text-[#0A1128]">
              ⚖️ Law & Jurisprudence (Essential Legal References)
            </span>
          </div>
          <span id="vaultCountTag" class="text-xs text-slate-500 font-semibold">Showing 4 cataloged editions</span>
        </div>

        <!-- Grid Container -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5" id="vaultCardsGrid">
          <!-- Initial Law Books populated via JS -->
        </div>

      </div>

    </div>

  </div>
</section>
"""

# F. FULL FILTERABLE CATALOG DIRECTORY (#shop-all-catalog)
catalog_directory_section_html = """
<!-- ======================================================================= -->
<!-- SECTION 7: FULL FILTERABLE CATALOG DIRECTORY (#shop-all-catalog)         -->
<!-- ======================================================================= -->
<section id="shop-all-catalog" class="py-20 lg:py-24 bg-[#FAF8F5] border-t border-slate-200 relative">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <!-- Active Category Banner (Dynamically updated via Navbar click) -->
    <div id="catalogActiveBanner" class="hidden mb-8 bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 flex items-center justify-between font-sans">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-[#D99B26] animate-pulse"></span>
        <span id="catalogBannerText" class="text-xs sm:text-sm font-bold text-[#0A1128]">
          Browsing All Pan-India Titles
        </span>
      </div>
      <button onclick="resetCatalogFilter()" class="text-xs font-bold text-amber-800 hover:text-black underline">
        View All Books
      </button>
    </div>

    <!-- Header & Filter Bar -->
    <div class="flex flex-col md:flex-row md:items-end justify-between pb-6 border-b border-amber-900/10 gap-4 mb-8">
      <div>
        <div class="inline-flex items-center gap-2 bg-amber-100 text-[#D99B26] border border-amber-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase mb-2 font-sans">
          <span>PAN-INDIA CATALOG ARCHIVE</span>
        </div>
        <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128]">
          Shop by Collection & Category
        </h2>
        <p class="text-sm text-slate-600 mt-1 font-sans">
          Instant predictive filtering across 11,922+ literary titles, upcoming releases, and boxed sets.
        </p>
      </div>

      <!-- Quick Search Bar in Catalog -->
      <div class="relative w-full md:w-80 font-sans">
        <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
        <input type="text" id="catalogSearchField" onkeyup="searchFullCatalog(this.value)" placeholder="Search title, author, ISBN..." class="w-full text-xs pl-10 pr-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:border-[#D99B26] bg-white shadow-sm">
      </div>
    </div>

    <!-- Filter Pills (100% Functional Category Tabs) -->
    <div class="flex flex-wrap items-center gap-2 mb-8 font-sans" id="catalogFilterPills">
      <button onclick="setCatalogCategory('all')" class="cat-pill active px-4 py-2 rounded-xl text-xs font-bold transition-all bg-[#0A1128] text-white shadow-sm">
        All Books (11,922+)
      </button>
      <button onclick="setCatalogCategory('coming-soon')" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white border border-slate-200 text-slate-700 hover:bg-amber-50">
        Coming Soon
      </button>
      <button onclick="setCatalogCategory('pre-order')" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white border border-slate-200 text-slate-700 hover:bg-amber-50">
        Pre-Order Special
      </button>
      <button onclick="setCatalogCategory('bestsellers')" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white border border-slate-200 text-slate-700 hover:bg-amber-50">
        Top Bestsellers
      </button>
      <button onclick="setCatalogCategory('rekhta')" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white border border-slate-200 text-slate-700 hover:bg-amber-50">
        Rekhta & Poetry
      </button>
      <button onclick="setCatalogCategory('fiction')" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white border border-slate-200 text-slate-700 hover:bg-amber-50">
        Contemporary Hindi Fiction
      </button>
      <button onclick="setCatalogCategory('law')" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white border border-slate-200 text-slate-700 hover:bg-amber-50">
        Law & Judiciary
      </button>
    </div>

    <!-- Catalog Book Cards Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6" id="catalogCardsGrid">
      <!-- Populated via Javascript -->
    </div>

  </div>
</section>
"""

# Assemble all replacement body sections
full_replacement_body = (
    # 1. Literary Marquee (from existing preview)
    # We will preserve the marquee section
    podium_section_html +
    mehfil_section_html +
    bundle_section_html +
    regional_section_html +
    vault_section_html +
    catalog_directory_section_html
)

# Replace between literaryMarqueeSection and trustFeaturesSection
marquee_end_marker = '</section>'
# Find literaryMarqueeSection
marquee_pos = preview_content.find('id="literaryMarqueeSection"')
if marquee_pos != -1:
    marquee_close = preview_content.find('</section>', marquee_pos) + len('</section>')
else:
    marquee_close = preview_content.find('</section>') + len('</section>')

trust_pos = preview_content.find('id="trustFeaturesSection"')
if trust_pos == -1:
    trust_pos = preview_content.find('<footer')

print(f"Replacing body sections between {marquee_close} and {trust_pos}...")

# -------------------------------------------------------------
# 4. UPDATED JAVASCRIPT STATE ENGINE FOR PREVIEW.HTML
# -------------------------------------------------------------
complete_interactive_js = """
<script id="comprehensiveStoreEngine">
// =========================================================================
// INDIGO BOOKS - COMPLETE INTERACTIVE FRONTEND ENGINE
// =========================================================================

// 1. GLOBAL STATE
let activeNavTab = 'Home';
let activePodiumIndex = 2; // Kasaibada center default
let isPodiumCoverOpen = false;
let activeMehfilPoet = 'all';
let activeVaultDrawer = 'law';
let activeCatalogCategory = 'all';

// 2. PODIUM BESTSELLERS 3D STAGE & -140° COVER FLIP
const PODIUM_DATA = [
  {
    id: "podium-1",
    title: "Diary of a Wimpy Kid: Fight or Flight",
    author: "Jeff Kinney",
    price: 349,
    mrp: 499,
    save: "30% OFF",
    rating: "4.9 (420+)",
    image: "assets/hero-book-wimpy-kid.jpg",
    rank: "#1 IN GLOBAL BESTSELLERS",
    stock: "38 copies left in Prayagraj",
    pages: "224 Pages • Hardcover • Puffin",
    publisher: "Puffin Books India",
    quote: "Hilarious, chaotic family road trips that resonate with readers of all generations worldwide."
  },
  {
    id: "podium-2",
    title: "Ujli Raaten (White Nights)",
    author: "Fyodor Dostoevsky",
    price: 299,
    mrp: 399,
    save: "25% OFF",
    rating: "4.8 (310+)",
    image: "assets/hero-book-ujli-raaten.jpg",
    rank: "#1 IN TRANSLATED RUSSIAN CLASSICS",
    stock: "14 copies left in Prayagraj",
    pages: "112 Pages • Paperback • Penguin Swadesh",
    publisher: "Penguin Hindi Classics",
    quote: "A poetic, sentimental exploration of loneliness, love, and twilight reveries on the canals of St. Petersburg."
  },
  {
    id: "podium-3",
    title: "Kasaibada",
    author: "Manoj Rajan Tripathi",
    price: 299,
    mrp: 395,
    save: "24% OFF",
    rating: "4.9 (540+)",
    image: "assets/hero-book-kasaibada.jpg",
    rank: "#1 IN CONTEMPORARY HINDI FICTION",
    stock: "22 copies left in Prayagraj",
    pages: "192 Pages • Paperback • Vani",
    publisher: "Vani Prakashan",
    quote: "A gripping social allegory on power structures, moral struggle, and raw human resilience in northern India."
  },
  {
    id: "podium-4",
    title: "Alchemised",
    author: "Contemporary Philosophy",
    price: 399,
    mrp: 550,
    save: "27% OFF",
    rating: "4.7 (190+)",
    image: "assets/book-alchemised.jpg",
    rank: "#1 IN SPIRITUAL & THOUGHT",
    stock: "19 copies left in Prayagraj",
    pages: "256 Pages • Paperback • HarperCollins",
    publisher: "HarperCollins India",
    quote: "Transmuting personal adversity into enduring wisdom through timeless parables and deep introspective prose."
  },
  {
    id: "podium-5",
    title: "Ratan Tata: A Life",
    author: "Thomas Mathew",
    price: 699,
    mrp: 999,
    save: "30% OFF",
    rating: "5.0 (860+)",
    image: "assets/book-ratan-tata.jpg",
    rank: "#1 IN BIOGRAPHIES & MEMOIRS",
    stock: "45 copies left in Prayagraj",
    pages: "544 Pages • Hardcover • HarperCollins",
    publisher: "HarperCollins India",
    quote: "The definitive authorized biography tracing the integrity, trials, and unparalleled vision of an Indian icon."
  }
];

function updatePodiumStage() {
  const cards = document.querySelectorAll('.podium-book-card');
  if (!cards.length) return;
  const count = PODIUM_DATA.length;

  cards.forEach((card, i) => {
    let offset = i - activePodiumIndex;
    if (offset < -2) offset += count;
    if (offset > 2) offset -= count;

    card.classList.remove('is-active', 'is-open');
    
    if (offset === 0) {
      card.classList.add('is-active');
      if (isPodiumCoverOpen) card.classList.add('is-open');
      card.style.transform = 'translateX(0px) scale(1.15) rotateY(-8deg)';
      card.style.zIndex = '30';
      card.style.opacity = '1';
    } else if (offset === -1) {
      card.style.transform = 'translateX(-120px) scale(0.9) rotateY(24deg)';
      card.style.zIndex = '20';
      card.style.opacity = '0.85';
    } else if (offset === 1) {
      card.style.transform = 'translateX(120px) scale(0.9) rotateY(-24deg)';
      card.style.zIndex = '20';
      card.style.opacity = '0.85';
    } else if (offset <= -2) {
      card.style.transform = 'translateX(-220px) scale(0.75) rotateY(38deg)';
      card.style.zIndex = '10';
      card.style.opacity = '0.45';
    } else if (offset >= 2) {
      card.style.transform = 'translateX(220px) scale(0.75) rotateY(-38deg)';
      card.style.zIndex = '10';
      card.style.opacity = '0.45';
    }
  });

  // Spotlight Panel Update
  const book = PODIUM_DATA[activePodiumIndex];
  if (book) {
    const rankEl = document.getElementById('spotlightRank');
    const titleEl = document.getElementById('spotlightTitle');
    const authEl = document.getElementById('spotlightAuthor');
    const rateEl = document.getElementById('spotlightRating');
    const quoteEl = document.getElementById('spotlightQuote');
    const pagesEl = document.getElementById('spotlightPages');
    const pubEl = document.getElementById('spotlightPublisher');
    const priceEl = document.getElementById('spotlightPrice');
    const mrpEl = document.getElementById('spotlightMRP');
    const saveEl = document.getElementById('spotlightSave');
    const stockEl = document.getElementById('spotlightStock');
    const waEl = document.getElementById('spotlightWhatsAppBtn');

    if (rankEl) rankEl.innerText = book.rank;
    if (titleEl) titleEl.innerText = book.title;
    if (authEl) authEl.innerText = book.author;
    if (rateEl) rateEl.innerText = book.rating;
    if (quoteEl) quoteEl.innerText = `"${book.quote}"`;
    if (pagesEl) pagesEl.innerText = book.pages;
    if (pubEl) pubEl.innerText = book.publisher;
    if (priceEl) priceEl.innerText = `₹${book.price}.00`;
    if (mrpEl) mrpEl.innerText = `₹${book.mrp}.00`;
    if (saveEl) saveEl.innerText = book.save;
    if (stockEl) stockEl.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span> ${book.stock}`;

    if (waEl) {
      const waText = encodeURIComponent(`Hello Indigo Books, I want to order ${book.title} by ${book.author} at ₹${book.price}.`);
      waEl.href = `https://wa.me/918881122722?text=${waText}`;
    }
  }

  // Dots
  const dots = document.querySelectorAll('#podiumIndicators button');
  dots.forEach((dot, idx) => {
    if (idx === activePodiumIndex) {
      dot.className = 'w-7 h-2.5 rounded-full bg-[#D99B26] transition-all duration-300';
    } else {
      dot.className = 'w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300';
    }
  });
}

function selectPodiumBook(index) {
  if (activePodiumIndex === index) {
    togglePodiumCoverOpen();
  } else {
    activePodiumIndex = index;
    isPodiumCoverOpen = false;
    updatePodiumStage();
  }
}

function nextPodiumBook() {
  activePodiumIndex = (activePodiumIndex + 1) % PODIUM_DATA.length;
  isPodiumCoverOpen = false;
  updatePodiumStage();
}

function prevPodiumBook() {
  activePodiumIndex = (activePodiumIndex - 1 + PODIUM_DATA.length) % PODIUM_DATA.length;
  isPodiumCoverOpen = false;
  updatePodiumStage();
}

function togglePodiumCoverOpen() {
  isPodiumCoverOpen = !isPodiumCoverOpen;
  const activeCard = document.querySelector('.podium-book-card.is-active');
  const btnText = document.getElementById('flipCoverBtnText');
  if (activeCard) {
    if (isPodiumCoverOpen) {
      activeCard.classList.add('is-open');
      if (btnText) btnText.innerText = "Cover Open (-140°) • Click to Close";
    } else {
      activeCard.classList.remove('is-open');
      if (btnText) btnText.innerText = "Hover or Click Book to Open Cover (-140°)";
    }
  }
}

function addCurrentPodiumToCart() {
  const book = PODIUM_DATA[activePodiumIndex];
  if (book && typeof addToCart === 'function') {
    addToCart(book.id, book.title, book.price, book.image);
  }
}

function openPodiumQuickView() {
  const book = PODIUM_DATA[activePodiumIndex];
  if (book && typeof openQuickView === 'function') {
    openQuickView({
      title: book.title,
      author: book.author,
      price: book.price,
      originalPrice: book.mrp,
      cover: book.image,
      desc: book.quote,
      category: book.rank,
      binding: book.pages
    });
  }
}

// 3. MEHFIL-E-REKHTA SHAYARI & FILTER ENGINE
const POET_DATA = {
  elia: {
    name: "Jaun Elia",
    pen: "क़तील-ए-अना",
    urdu: "شاید مجھے نکال کے پچھتا رہے ہوں آپ • محفل میں اس خیال سے پھر آ گیا ہوں میں",
    hindi: "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं",
    eng: "Perhaps you regret having cast me out; it is merely with this thought that I returned to the gathering."
  },
  faraz: {
    name: "Ahmad Faraz",
    pen: "शायर-ए-इश्क़",
    urdu: "رنجش ہی سہی دل ہی دکھانے کے لیے آ • آ پھر سے مجھے چھوڑ کے جانے کے لیے آ",
    hindi: "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ",
    eng: "Even if in resentment, come just to break my heart; come, if only to leave me once again."
  },
  manto: {
    name: "Saadat Hasan Manto",
    pen: "बागी अफ़सानानिगार",
    urdu: "اگر آپ میرے افسانوں کو برداشت نہیں کر سکتے، تو اس کا مطلب ہے کہ زمانہ ناقابل برداشت ہے",
    hindi: "अगर आप मेरे अफ़सानों को बर्दाश्त नहीं कर सकते, तो इसका मतलब है कि ज़माना नाक़ाबिले-बर्दाश्त है।",
    eng: "If you cannot bear my stories, it means the society we live in is unbearable."
  },
  ghalib: {
    name: "Mirza Ghalib",
    pen: "असद-उल्लाह ख़ान",
    urdu: "ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے • بہت نکلے مرے ارمان لیکن پھر بھی کم نکلے",
    hindi: "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले • बहुत निकले मिरे अरमान लेकिन फिर भी कम निकले",
    eng: "Thousands of desires, each one worth dying for; many were fulfilled, yet so many remain."
  }
};

function filterMehfilPoet(poetKey) {
  activeMehfilPoet = poetKey;

  // 1. Update pills
  const pills = document.querySelectorAll('#poetSelectorPills button');
  pills.forEach(p => {
    p.className = 'poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all font-sans';
  });
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.className = 'poet-pill active px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/50 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(217,155,38,0.3)] transition-all font-sans';
  }

  // 2. Crossfade Couplet Quote
  const q = POET_DATA[poetKey] || POET_DATA['elia'];
  const urduEl = document.getElementById('poetUrduVerse');
  const hindiEl = document.getElementById('poetHindiVerse');
  const engEl = document.getElementById('poetEngVerse');
  const attrEl = document.getElementById('poetAttribution');

  if (urduEl && hindiEl && engEl && attrEl) {
    urduEl.style.opacity = '0';
    hindiEl.style.opacity = '0';
    engEl.style.opacity = '0';

    setTimeout(() => {
      urduEl.innerText = q.urdu;
      hindiEl.innerText = `"${q.hindi}"`;
      engEl.innerText = q.eng;
      attrEl.innerText = `— ${q.name} (${q.pen})`;

      urduEl.style.opacity = '1';
      hindiEl.style.opacity = '1';
      engEl.style.opacity = '1';
    }, 200);
  }

  // 3. Highlight/Filter Books in Row
  const cards = document.querySelectorAll('.rekhta-book-card');
  cards.forEach(card => {
    const cardPoet = card.getAttribute('data-poet');
    if (poetKey === 'all' || cardPoet === poetKey) {
      card.style.opacity = '1';
      card.style.transform = 'scale(1)';
      card.style.borderColor = (cardPoet === poetKey) ? '#F59E0B' : 'rgba(245, 158, 11, 0.2)';
      if (cardPoet === poetKey) {
        card.style.boxShadow = '0 0 25px rgba(217, 155, 38, 0.35)';
      } else {
        card.style.boxShadow = '';
      }
    } else {
      card.style.opacity = '0.35';
      card.style.transform = 'scale(0.96)';
      card.style.borderColor = 'rgba(255, 255, 255, 0.05)';
      card.style.boxShadow = '';
    }
  });
}

// 4. LAW & ACADEMIC VAULT DRAWER ENGINE
const VAULT_DATA = {
  law: {
    title: "⚖️ Law & Jurisprudence (Essential Legal References)",
    books: [
      {
        id: "law-1",
        title: "Modi Medical Jurisprudence & Toxicology",
        author: "Kannan & Mathiharan",
        price: 1850,
        mrp: 2195,
        tag: "LexisNexis • Hardcover",
        image: "assets/book-medical-jurisprudence.jpg",
        overview: "The supreme authority on forensic medicine, toxicology, and autopsy procedure cited continuously across high courts and the Supreme Court."
      },
      {
        id: "law-2",
        title: "Lawful Awful: Life in Law & Courtrooms",
        author: "Justice Venkataswami",
        price: 450,
        mrp: 599,
        tag: "Penguin Law • Memoir",
        image: "assets/book-lawful-awful.jpg",
        overview: "A delightful, witty judicial memoir capturing colorful courtroom anecdotes, advocate camaraderie, and the legal ethos of India."
      },
      {
        id: "law-3",
        title: "१० फ़ैसले जिन्होंने देश बदल दिया",
        author: "Zia Mody (Hindi)",
        price: 320,
        mrp: 395,
        tag: "Landmark Judgments",
        image: "assets/book-10-faisle.jpg",
        overview: "Compelling accounts of landmark constitutional judgments that shaped free speech, privacy, secularism, and executive accountability."
      },
      {
        id: "law-4",
        title: "Bench and Bar: Reminiscences of Courts",
        author: "Universal Law Publishing",
        price: 590,
        mrp: 750,
        tag: "Legal History & Ethics",
        image: "assets/book-bench-bar.jpg",
        overview: "Historical reminiscences and professional ethics guiding generations of advocates and judges in Indian jurisprudence."
      }
    ]
  },
  sahitya: {
    title: "🏛️ Hindi Sahitya & Vyakaran (Academic Curricula)",
    books: [
      {
        id: "sahitya-1",
        title: "हिंदी साहित्य का इतिहास",
        author: "आचार्य रामचंद्र शुक्ल",
        price: 450,
        mrp: 550,
        tag: "Standard University Ref",
        image: "assets/book-hindi-sahitya-itihas.jpg",
        overview: "Acharya Shukla's seminal foundation text categorizing and analyzing Hindi literary movements across eight centuries."
      },
      {
        id: "sahitya-2",
        title: "आधुनिक हिंदी व्याकरण और रचना",
        author: "वासुदेव नंदन प्रसाद",
        price: 280,
        mrp: 350,
        tag: "Linguistics & Grammar",
        image: "assets/book-hindi-vyakaran.jpg",
        overview: "The standard university handbook covering syntax, morphology, orthography, and compositional mechanics for competitive exams."
      },
      {
        id: "sahitya-3",
        title: "हिंदी भाषा का इतिहास व विकास",
        author: "डॉ. भोलानाथ तिवारी",
        price: 320,
        mrp: 400,
        tag: "Philology & Dialects",
        image: "assets/book-hindi-bhasha.jpg",
        overview: "Comprehensive philological study tracing the origin of Khariboli, Braj, Awadhi, and modern Indo-Aryan dialects."
      },
      {
        id: "sahitya-4",
        title: "लोक साहित्य की भूमिका",
        author: "डॉ. कृष्णदेव उपाध्याय",
        price: 390,
        mrp: 480,
        tag: "Folk Literature",
        image: "assets/book-lok-sahitya.jpg",
        overview: "In-depth anthropological and literary exploration of Bhojpuri, Maithili, and rural North Indian folk narratives and songs."
      }
    ]
  },
  prep: {
    title: "🎓 Civil Services & McGraw Hill (Competitive Exams)",
    books: [
      {
        id: "prep-1",
        title: "Indian Polity (7th Edition)",
        author: "M. Laxmikanth",
        price: 699,
        mrp: 895,
        tag: "McGraw Hill • UPSC GS-2",
        image: "assets/book-anil-naik.jpg",
        overview: "The indispensable Bible for constitutional framework, governance, fundamental rights, and judicial systems for civil services."
      },
      {
        id: "prep-2",
        title: "Modern Indian History Spectrum",
        author: "Rajiv Ahir IPS",
        price: 390,
        mrp: 485,
        tag: "Historical Foundation",
        image: "assets/book-kabira-khada.jpg",
        overview: "Concise yet exhaustive chronology of India's freedom struggle, British administrative reforms, and socio-religious movements."
      },
      {
        id: "prep-3",
        title: "Indian Economy for Civil Services",
        author: "Ramesh Singh",
        price: 620,
        mrp: 795,
        tag: "Macroeconomic Analysis",
        image: "assets/book-tumhare-shahar.jpg",
        overview: "Authoritative macroeconomic treatise covering fiscal policy, monetary systems, agricultural economics, and national budgets."
      }
    ]
  },
  history: {
    title: "🌍 History & Dalit Vimarsh (Socio-Political Studies)",
    books: [
      {
        id: "hist-1",
        title: "जाति का विनाश (Annihilation of Caste)",
        author: "डॉ. बी. आर. अम्बेडकर",
        price: 180,
        mrp: 250,
        tag: "Constitutional Thought",
        image: "assets/book-a-astu-ka.jpg",
        overview: "Babasaheb Ambedkar's radical philosophical critique of social stratification, religious orthodoxy, and constitutional equality."
      },
      {
        id: "hist-2",
        title: "झूठन (Joothan: An Untouchable's Life)",
        author: "ओमप्रकाश वाल्मीकि",
        price: 240,
        mrp: 300,
        tag: "Autobiographical Classic",
        image: "assets/book-cheelwali-kothi.jpg",
        overview: "A transformative, heart-wrenching autobiographical account exposing structural indignities and resilience in North Indian schools."
      },
      {
        id: "hist-3",
        title: "कबीरा खड़ा बाज़ार में",
        author: "भीष्म साहनी",
        price: 220,
        mrp: 280,
        tag: "Social Allegory Drama",
        image: "assets/book-kabira-khada.jpg",
        overview: "Bhisham Sahni's powerful theatrical classic resurrecting saint-poet Kabir's fearless challenge to religious dogmatism and bigotry."
      }
    ]
  }
};

function selectVaultDrawer(drawerKey) {
  activeVaultDrawer = drawerKey;
  const drawer = VAULT_DATA[drawerKey];
  if (!drawer) return;

  // Update tabs style
  const buttons = document.querySelectorAll('#vaultDrawerTabs button');
  buttons.forEach(b => b.classList.remove('active'));
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.classList.add('active');
  } else {
    // If called programmatically (e.g. from navbar Law Books click)
    const idx = ['law', 'sahitya', 'prep', 'history'].indexOf(drawerKey);
    if (buttons[idx]) buttons[idx].classList.add('active');
  }

  // Update Title & Counter
  const titleEl = document.getElementById('vaultDrawerActiveTitle');
  const countEl = document.getElementById('vaultCountTag');
  if (titleEl) titleEl.innerText = drawer.title;
  if (countEl) countEl.innerText = `Showing ${drawer.books.length} cataloged editions`;

  // Render Spec-Sheet Cards with Mini Overviews
  renderVaultCards(drawer.books);
}

function renderVaultCards(books) {
  const grid = document.getElementById('vaultCardsGrid');
  if (!grid) return;

  grid.innerHTML = books.map(b => `
    <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex flex-col justify-between">
      <div>
        <div class="flex gap-4">
          <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
            <img src="${b.image}" alt="${b.title}" class="w-full h-full object-cover">
          </div>
          <div class="flex-1 min-w-0">
            <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded font-sans">
              ${b.tag}
            </span>
            <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors leading-snug">
              ${b.title}
            </h4>
            <p class="text-[11px] text-slate-500 font-sans mt-0.5">${b.author}</p>
            <div class="text-[10px] text-emerald-700 font-bold font-sans mt-1">✓ In Stock at Prayagraj</div>
          </div>
        </div>
        <!-- 2-Line Mini Overview -->
        <p class="text-[11px] text-slate-600 leading-relaxed line-clamp-2 mt-3 font-sans">
          ${b.overview}
        </p>
      </div>

      <div class="mt-4 pt-3 border-t border-slate-200 flex items-center justify-between font-sans">
        <div>
          <span class="text-base font-bold text-[#0A1128] font-serif">₹${b.price}.00</span>
          <span class="text-[10px] text-slate-400 line-through ml-1 font-serif">₹${b.mrp}</span>
        </div>
        <button onclick="addToCart('${b.id}', '${b.title}', ${b.price}, '${b.image}')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white px-3 py-1.5 rounded-lg transition-colors text-xs font-bold" title="Add to Cart">
          Add to Cart
        </button>
      </div>
    </div>
  `).join('');
}

function filterVaultBooks(query) {
  const q = query.toLowerCase().trim();
  const drawer = VAULT_DATA[activeVaultDrawer];
  if (!drawer) return;

  const filtered = drawer.books.filter(b => 
    b.title.toLowerCase().includes(q) || 
    b.author.toLowerCase().includes(q) || 
    b.overview.toLowerCase().includes(q)
  );

  renderVaultCards(filtered);
}

// 5. FULL CATALOG DIRECTORY ENGINE (#shop-all-catalog)
let ALL_CATALOG_BOOKS = [];

function initCatalogDirectory() {
  // Combine all store books into catalog directory
  ALL_CATALOG_BOOKS = [
    ...PODIUM_DATA.map(b => ({ ...b, category: 'bestsellers' })),
    {
      id: "cat-1",
      title: "चीलवाली कोठी (Cheelwali Kothi)",
      author: "Sara Rai",
      price: 299,
      mrp: 395,
      save: "24% OFF",
      rating: "4.9",
      image: "assets/book-cheelwali-kothi.jpg",
      category: "fiction",
      overview: "A haunting tale of ancestral mansions, lost memories, and quiet dignity in Uttar Pradesh."
    },
    {
      id: "cat-2",
      title: "नर-नारीश्वर (Nar Nareeshwar)",
      author: "Vishnu Prabhakar",
      price: 320,
      mrp: 425,
      save: "25% OFF",
      rating: "4.8",
      image: "assets/book-nar-nareeshwar.jpg",
      category: "fiction",
      overview: "Sahitya Akademi award-winning novel traversing human relationships and psychological truth."
    },
    {
      id: "cat-3",
      title: "क्यों (Kyon)",
      author: "Jaun Elia",
      price: 350,
      mrp: 450,
      save: "22% OFF",
      rating: "4.9",
      image: "assets/book-kyon-jaun-elia.jpg",
      category: "rekhta",
      overview: "Piercing, immortal ghazals on existential longing and heartbreak."
    },
    {
      id: "cat-4",
      title: "रंजिश ही सही (Ranjish Hi Sahi)",
      author: "Ahmad Faraz",
      price: 399,
      mrp: 499,
      save: "20% OFF",
      rating: "5.0",
      image: "assets/book-ranjish-hi-sahi.jpg",
      category: "rekhta",
      overview: "Celebrated romantic verses and revolutionary ghazals by Ahmad Faraz."
    },
    {
      id: "cat-5",
      title: "दोज़ख़नामा (Dozakhnama)",
      author: "Rabisankar Bal",
      price: 450,
      mrp: 550,
      save: "18% OFF",
      rating: "4.9",
      image: "assets/hero-book-dozakh.jpg",
      category: "rekhta",
      overview: "A dialogue between Ghalib and Manto bridging Lucknow, Delhi, and Lahore."
    },
    {
      id: "cat-6",
      title: "A Court of Thorns and Roses (5-Book Set)",
      author: "Sarah J. Maas",
      price: 1899,
      mrp: 2999,
      save: "37% OFF",
      rating: "4.9",
      image: "assets/book-acotar.jpg",
      category: "bestsellers",
      overview: "The complete global BookTok fantasy sensation in a collector slipcase box."
    },
    {
      id: "cat-7",
      title: "Arundhati Roy Definitive Duo",
      author: "Arundhati Roy",
      price: 799,
      mrp: 1198,
      save: "33% OFF",
      rating: "5.0",
      image: "assets/hero-book-arundhati.jpg",
      category: "bestsellers",
      overview: "The God of Small Things + The Ministry of Utmost Happiness in collector edition."
    },
    {
      id: "cat-8",
      title: "Modi Medical Jurisprudence",
      author: "Kannan & Mathiharan",
      price: 1850,
      mrp: 2195,
      save: "16% OFF",
      rating: "5.0",
      image: "assets/book-medical-jurisprudence.jpg",
      category: "law",
      overview: "The authoritative textbook on forensic medicine cited across the Indian judiciary."
    },
    {
      id: "cat-9",
      title: "The Himalayan Chronicler (Coming Soon)",
      author: "Ruskin Bond (Special Edition)",
      price: 499,
      mrp: 650,
      save: "23% OFF",
      rating: "5.0",
      image: "assets/book-patthar-alpatthar.jpg",
      category: "coming-soon",
      overview: "Unpublished Mussoorie memoirs, nature essays, and rare mountain sketches."
    },
    {
      id: "cat-10",
      title: "Gopi Diaries: Festive Gift Edition (Coming Soon)",
      author: "Sudha Murty",
      price: 320,
      mrp: 399,
      save: "20% OFF",
      rating: "4.9",
      image: "assets/hero-book-sudha-murty.jpg",
      category: "coming-soon",
      overview: "The charming canine adventures of Gopi in a gold-foil illustrated gift edition."
    },
    {
      id: "cat-11",
      title: "Prayagraj: The Eternal Confluence (Pre-Order)",
      author: "Heritage Archival Project",
      price: 899,
      mrp: 1250,
      save: "28% OFF",
      rating: "5.0",
      image: "assets/book-hindi-sahitya-itihas.jpg",
      category: "pre-order",
      overview: "Exclusive hardbound visual chronicles of Allahabad's literary giants from Nirala to Harivansh Rai Bachchan."
    },
    {
      id: "cat-12",
      title: "The Constitution of India: De Luxe Lexis (Pre-Order)",
      author: "Legal Scholars Guild",
      price: 1450,
      mrp: 1999,
      save: "27% OFF",
      rating: "5.0",
      image: "assets/book-10-faisle.jpg",
      category: "pre-order",
      overview: "Commemorative leather-bound edition with landmark 2026 judicial amendments."
    }
  ];

  renderCatalogCards(ALL_CATALOG_BOOKS);
}

function setCatalogCategory(category) {
  activeCatalogCategory = category;

  // Update pills
  const pills = document.querySelectorAll('#catalogFilterPills button');
  pills.forEach(p => {
    p.className = 'cat-pill px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white border border-slate-200 text-slate-700 hover:bg-amber-50';
  });
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.className = 'cat-pill active px-4 py-2 rounded-xl text-xs font-bold transition-all bg-[#0A1128] text-white shadow-sm';
  }

  // Update active banner
  const banner = document.getElementById('catalogActiveBanner');
  const bannerText = document.getElementById('catalogBannerText');
  if (category === 'all') {
    if (banner) banner.classList.add('hidden');
  } else {
    if (banner && bannerText) {
      banner.classList.remove('hidden');
      const titles = {
        'coming-soon': 'Displaying Anticipated Upcoming Releases (Coming Soon)',
        'pre-order': 'Displaying Exclusive Pre-Order Editions & Special Boxsets',
        'bestsellers': 'Displaying National Bestsellers & Top Trending Reads',
        'rekhta': 'Displaying Official Rekhta Publications & Urdu Poetry',
        'fiction': 'Displaying Contemporary Hindi Fiction & Regional Prose',
        'law': 'Displaying Law, Judiciary & Civil Services References'
      };
      bannerText.innerText = titles[category] || `Filtering by: ${category}`;
    }
  }

  // Filter books
  if (category === 'all') {
    renderCatalogCards(ALL_CATALOG_BOOKS);
  } else {
    const filtered = ALL_CATALOG_BOOKS.filter(b => b.category === category);
    renderCatalogCards(filtered);
  }
}

function resetCatalogFilter() {
  setCatalogCategory('all');
}

function searchFullCatalog(query) {
  const q = query.toLowerCase().trim();
  const filtered = ALL_CATALOG_BOOKS.filter(b => 
    b.title.toLowerCase().includes(q) || 
    b.author.toLowerCase().includes(q) || 
    (b.overview && b.overview.toLowerCase().includes(q))
  );
  renderCatalogCards(filtered);
}

function renderCatalogCards(books) {
  const grid = document.getElementById('catalogCardsGrid');
  if (!grid) return;

  if (books.length === 0) {
    grid.innerHTML = `
      <div class="col-span-full text-center py-12 text-slate-500 text-sm font-sans">
        No books found matching this filter. Try selecting "All Books".
      </div>
    `;
    return;
  }

  grid.innerHTML = books.map(b => `
    <div class="catalog-book-card bg-white border border-[#E8DFC8] rounded-xl p-4 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
      <div>
        <div class="aspect-[2/3] w-full rounded-md overflow-hidden shadow-md mb-3 relative">
          <img src="${b.image}" alt="${b.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
          ${b.save ? `<span class="absolute top-2 left-2 bg-[#D99B26] text-white font-sans text-[9px] font-bold px-2 py-0.5 rounded shadow">${b.save}</span>` : ''}
        </div>
        <h4 class="font-serif text-sm font-bold text-[#0A1128] line-clamp-2 group-hover:text-[#D99B26] transition-colors leading-snug">
          ${b.title}
        </h4>
        <p class="text-xs text-slate-500 font-sans mt-0.5">${b.author}</p>
        <p class="text-[11px] text-slate-600 line-clamp-2 mt-2 font-sans leading-relaxed">
          ${b.overview || 'Handpicked authentic publisher edition available at Prayagraj.'}
        </p>
      </div>

      <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between font-sans">
        <div>
          <span class="font-serif font-bold text-base text-[#0A1128]">₹${b.price}.00</span>
          ${b.mrp ? `<span class="text-[10px] text-slate-400 line-through ml-1 font-serif">₹${b.mrp}</span>` : ''}
        </div>
        <button onclick="addToCart('${b.id}', '${b.title.replace(/'/g, "\\'")}', ${b.price}, '${b.image}')" class="bg-[#D99B26] hover:bg-[#B88019] text-white p-2 rounded-lg transition-colors text-xs font-bold" title="Add to Cart">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M19 6h-2c0-2.76-2.24-5-5-5S7 3.24 7 6H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-7-3c1.66 0 3 1.34 3 3H9c0-1.66 1.34-3 3-3zm7 17H5V8h14v12z"/></svg>
        </button>
      </div>
    </div>
  `).join('');
}

// 6. NAVBAR TAB CLICK HANDLER WITH SMOOTH SCROLLING & AUTO-FILTERING
function handleNavClick(tabName, event) {
  if (event) event.preventDefault();
  activeNavTab = tabName;

  // Update active style on navbar links
  const links = document.querySelectorAll('.nav-tab-link');
  links.forEach(l => {
    l.classList.remove('active');
    if (l.innerText.includes(tabName)) l.classList.add('active');
  });

  if (tabName === 'Home') {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else if (tabName === 'Best Sellers') {
    const el = document.getElementById('bestsellers-podium') || document.getElementById('curatorsPodiumSection');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (tabName === 'Bundles') {
    const el = document.getElementById('bundles-section') || document.getElementById('bundleUnboxingSection');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (tabName === 'Law Books') {
    const el = document.getElementById('law-academic-vault') || document.getElementById('academicVaultSection');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
      selectVaultDrawer('law');
    }
  } else if (tabName === 'Shop All') {
    const el = document.getElementById('shop-all-catalog');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
      setCatalogCategory('all');
    }
  } else if (tabName === 'Coming Soon') {
    const el = document.getElementById('shop-all-catalog');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
      setCatalogCategory('coming-soon');
    }
  } else if (tabName === 'Pre-Order') {
    const el = document.getElementById('shop-all-catalog');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
      setCatalogCategory('pre-order');
    }
  }
}

function focusCatalogSearch() {
  const el = document.getElementById('shop-all-catalog');
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
    setTimeout(() => {
      const search = document.getElementById('catalogSearchField');
      if (search) search.focus();
    }, 400);
  }
}

// 7. INITIALIZATION ON DOM CONTENT LOADED
window.addEventListener('DOMContentLoaded', () => {
  updatePodiumStage();
  selectVaultDrawer('law');
  initCatalogDirectory();
});
</script>
"""

# Replace body sections in preview_content
new_preview_content = (
    preview_content[:marquee_close] +
    "\n\n" +
    full_replacement_body +
    "\n\n" +
    preview_content[trust_pos:]
)

# Append or replace the engine script
if 'id="comprehensiveStoreEngine"' in new_preview_content:
    new_preview_content = re.sub(r'<script id="comprehensiveStoreEngine">.*?</script>', complete_interactive_js.strip(), new_preview_content, flags=re.DOTALL)
else:
    body_close = new_preview_content.rfind('</body>')
    if body_close != -1:
        new_preview_content = new_preview_content[:body_close] + complete_interactive_js + "\n" + new_preview_content[body_close:]

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(new_preview_content)

print("preview.html successfully updated with all 5 targeted fixes!")


