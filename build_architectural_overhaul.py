# -*- coding: utf-8 -*-
"""
Architectural UI/UX Overhaul Builder for Indigo Books India
Generates:
1. Updated preview.html with 6 avant-garde body sections below Hero
2. 6 Shopify Liquid Sections (literary-marquee, curators-podium, mehfil-rekhta, bundle-unboxing, regional-magazine, academic-vault)
3. Updated templates/index.json
4. Updated assets/theme.css and assets/theme.js
5. Packaged indigo-books-theme.zip
"""

import os
import re
import json
import zipfile

print("Starting Architectural Overhaul Builder...")

# ==========================================
# 1. HTML GENERATION FOR PREVIEW.HTML
# ==========================================

# A. LITERARY MARQUEE & LIVE COUNTER TICKER
html_literary_marquee = """
<!-- ======================================================================= -->
<!-- SECTION 1: LITERARY MARQUEE & LIVE COUNTER TICKER                        -->
<!-- ======================================================================= -->
<section id="literaryMarqueeSection" class="bg-[#0A1128] border-y border-amber-500/30 overflow-hidden relative z-30 shadow-2xl select-none">
  <!-- Top Kinetic Typography Ribbon (Endless Smooth CSS Scroll) -->
  <div class="py-2.5 bg-black/40 border-b border-amber-500/20 overflow-hidden relative">
    <div class="flex items-center whitespace-nowrap animate-marquee">
      <!-- Group 1 -->
      <div class="flex items-center gap-8 font-serif text-xs md:text-sm tracking-[0.18em] uppercase text-amber-300/90 font-medium px-4">
        <span>✦ 11,922+ TITLES IN STOCK</span>
        <span class="text-amber-500/50">•</span>
        <span>REKHTA PUBLICATIONS OFFICIAL PARTNER</span>
        <span class="text-amber-500/50">•</span>
        <span>PRAYAGRAJ HERITAGE BOOKSTORE</span>
        <span class="text-amber-500/50">•</span>
        <span>INSTANT WHATSAPP COD (+91 8881122722)</span>
        <span class="text-amber-500/50">•</span>
        <span>PAN-INDIA EXPRESS DELIVERY</span>
        <span class="text-amber-500/50">•</span>
        <span>100% AUTHENTIC PUBLISHER EDITIONS</span>
        <span class="text-amber-500/50">•</span>
        <span>CURATED LAW & ACADEMIC VAULT</span>
        <span class="text-amber-500/50">•</span>
      </div>
      <!-- Group 2 (Duplicate for continuous loop) -->
      <div class="flex items-center gap-8 font-serif text-xs md:text-sm tracking-[0.18em] uppercase text-amber-300/90 font-medium px-4" aria-hidden="true">
        <span>✦ 11,922+ TITLES IN STOCK</span>
        <span class="text-amber-500/50">•</span>
        <span>REKHTA PUBLICATIONS OFFICIAL PARTNER</span>
        <span class="text-amber-500/50">•</span>
        <span>PRAYAGRAJ HERITAGE BOOKSTORE</span>
        <span class="text-amber-500/50">•</span>
        <span>INSTANT WHATSAPP COD (+91 8881122722)</span>
        <span class="text-amber-500/50">•</span>
        <span>PAN-INDIA EXPRESS DELIVERY</span>
        <span class="text-amber-500/50">•</span>
        <span>100% AUTHENTIC PUBLISHER EDITIONS</span>
        <span class="text-amber-500/50">•</span>
        <span>CURATED LAW & ACADEMIC VAULT</span>
        <span class="text-amber-500/50">•</span>
      </div>
    </div>
  </div>

  <!-- Live Counter Metric Ribbon (Scroll-Triggered Live Counter) -->
  <div class="max-w-7xl mx-auto px-6 lg:px-8 py-4 lg:py-5">
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 text-center divide-y lg:divide-y-0 lg:divide-x divide-amber-500/20">
      
      <!-- Metric 1 -->
      <div class="p-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-[#D99B26] font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="11922">11,922</span><span class="text-amber-400">+</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">Books Available (Pan-India Express Delivery)</div>
      </div>

      <!-- Metric 2 -->
      <div class="p-2 pt-4 lg:pt-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-amber-300 font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="24">24</span><span class="text-amber-400">+</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">Featured Curations (Handpicked Heritage Gems)</div>
      </div>

      <!-- Metric 3 -->
      <div class="p-2 pt-4 lg:pt-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-[#D99B26] font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="30">30</span><span class="text-amber-400">%</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">Max Savings on Direct Publisher Bundles</div>
      </div>

      <!-- Metric 4 -->
      <div class="p-2 pt-4 lg:pt-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-emerald-400 font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="100">100</span><span class="text-emerald-300">%</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">Cash on Delivery & Authenticity Guaranteed</div>
      </div>

    </div>
  </div>
</section>
"""

# B. SECTION 1: THE 3D "CURATOR'S PODIUM" FOR BESTSELLERS
html_curators_podium = """
<!-- ======================================================================= -->
<!-- SECTION 2: THE 3D CURATOR'S PODIUM FOR BESTSELLERS                       -->
<!-- ======================================================================= -->
<section id="curatorsPodiumSection" class="py-20 lg:py-24 bg-[#FAF8F5] relative overflow-hidden">
  <!-- Subtle ambient decorative glow -->
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

    <!-- Split Stage: Left 7 Cols (3D Turntable Stage) + Right 5 Cols (Editorial Spotlight Panel) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
      
      <!-- LEFT 7 COLS: 3D Turntable Coverflow Stage -->
      <div class="lg:col-span-7 flex flex-col items-center">
        <!-- Turntable Stage Container -->
        <div class="w-full relative py-8 px-4 flex items-center justify-center min-h-[460px] perspective-[1200px]" id="podiumTurntableStage">
          
          <!-- Golden Pedestal Base Graphic -->
          <div class="absolute bottom-4 inset-x-8 h-20 bg-gradient-to-t from-amber-400/30 via-amber-200/20 to-transparent rounded-full blur-xl pointer-events-none"></div>
          <div class="absolute bottom-6 w-3/4 h-6 border-b-2 border-amber-500/30 rounded-[100%] shadow-[0_15px_30px_rgba(217,155,38,0.25)] pointer-events-none"></div>

          <!-- Podium Books Display Track -->
          <div class="relative w-full max-w-lg h-[360px] flex items-center justify-center" id="podiumBooksWrapper">
            <!-- Books rendered dynamically via JS or initial state -->
            <!-- 5 Bestsellers in 3D arc -->
            
            <!-- Book 0: Diary of a Wimpy Kid -->
            <div class="podium-book-card absolute cursor-pointer transition-all duration-500 ease-out" 
                 data-index="0" onclick="selectPodiumBook(0)">
              <div class="book-3d-wrapper relative w-36 lg:w-44 aspect-[2/3]">
                <!-- Front Cover -->
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/hero-book-wimpy-kid.jpg" alt="Diary of a Wimpy Kid" class="w-full h-full object-cover">
                  <!-- Book Spine Gradient Overlay -->
                  <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <!-- Underneath Page (Revealed on First Page Flip) -->
                <div class="book-page-underneath absolute inset-0 bg-[#FAF4E6] border border-amber-900/20 rounded-r-md p-3.5 flex flex-col justify-between text-slate-800 shadow-inner -z-10">
                  <div>
                    <div class="text-[9px] uppercase tracking-widest text-amber-800 font-bold border-b border-amber-800/20 pb-1">Chapter One</div>
                    <div class="text-[10px] font-serif italic mt-2 text-slate-700 leading-tight">"First of all, let me get something straight: this is a JOURNAL, not a diary..."</div>
                  </div>
                  <div class="text-[8px] text-right font-mono text-slate-400">Page 1</div>
                </div>
              </div>
            </div>

            <!-- Book 1: Ujli Raaten -->
            <div class="podium-book-card absolute cursor-pointer transition-all duration-500 ease-out" 
                 data-index="1" onclick="selectPodiumBook(1)">
              <div class="book-3d-wrapper relative w-36 lg:w-44 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/hero-book-ujli-raaten.jpg" alt="Ujli Raaten" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-page-underneath absolute inset-0 bg-[#FAF4E6] border border-amber-900/20 rounded-r-md p-3.5 flex flex-col justify-between text-slate-800 shadow-inner -z-10">
                  <div>
                    <div class="text-[9px] uppercase tracking-widest text-amber-800 font-bold border-b border-amber-800/20 pb-1">पहला प्रहर</div>
                    <div class="text-[10px] font-serif italic mt-2 text-slate-700 leading-tight">"वह एक अद्भुत रात थी, ऐसी रात जो केवल जवानी के दिनों में ही नसीब हो सकती है..."</div>
                  </div>
                  <div class="text-[8px] text-right font-mono text-slate-400">पृष्ठ १</div>
                </div>
              </div>
            </div>

            <!-- Book 2: Kasaibada (Active Center by Default) -->
            <div class="podium-book-card is-active absolute cursor-pointer transition-all duration-500 ease-out" 
                 data-index="2" onclick="selectPodiumBook(2)">
              <div class="book-3d-wrapper relative w-36 lg:w-44 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_25px_45px_rgba(0,0,0,0.65)] border-r-2 border-amber-50/80">
                  <img src="assets/hero-book-kasaibada.jpg" alt="Kasaibada" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-page-underneath absolute inset-0 bg-[#FAF4E6] border border-amber-900/20 rounded-r-md p-3.5 flex flex-col justify-between text-slate-800 shadow-inner -z-10">
                  <div>
                    <div class="text-[9px] uppercase tracking-widest text-amber-800 font-bold border-b border-amber-800/20 pb-1">प्रस्तावना</div>
                    <div class="text-[10px] font-serif italic mt-2 text-slate-700 leading-tight">"जिंदगी जब सत्ता और संघर्ष के दोराहे पर खड़ी होती है, तब कलम ही सबसे धारदार हथियार बनती है..."</div>
                  </div>
                  <div class="text-[8px] text-right font-mono text-slate-400">पृष्ठ १</div>
                </div>
              </div>
            </div>

            <!-- Book 3: Alchemised -->
            <div class="podium-book-card absolute cursor-pointer transition-all duration-500 ease-out" 
                 data-index="3" onclick="selectPodiumBook(3)">
              <div class="book-3d-wrapper relative w-36 lg:w-44 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/book-alchemised.jpg" alt="Alchemised" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-page-underneath absolute inset-0 bg-[#FAF4E6] border border-amber-900/20 rounded-r-md p-3.5 flex flex-col justify-between text-slate-800 shadow-inner -z-10">
                  <div>
                    <div class="text-[9px] uppercase tracking-widest text-amber-800 font-bold border-b border-amber-800/20 pb-1">The Principle</div>
                    <div class="text-[10px] font-serif italic mt-2 text-slate-700 leading-tight">"To transmute one's suffering is the oldest art known to conscious existence..."</div>
                  </div>
                  <div class="text-[8px] text-right font-mono text-slate-400">Page 1</div>
                </div>
              </div>
            </div>

            <!-- Book 4: Ratan Tata: A Life -->
            <div class="podium-book-card absolute cursor-pointer transition-all duration-500 ease-out" 
                 data-index="4" onclick="selectPodiumBook(4)">
              <div class="book-3d-wrapper relative w-36 lg:w-44 aspect-[2/3]">
                <div class="book-cover-front absolute inset-0 rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_35px_rgba(0,0,0,0.5)] border-r-2 border-amber-50/80">
                  <img src="assets/book-ratan-tata.jpg" alt="Ratan Tata: A Life" class="w-full h-full object-cover">
                  <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
                </div>
                <div class="book-page-underneath absolute inset-0 bg-[#FAF4E6] border border-amber-900/20 rounded-r-md p-3.5 flex flex-col justify-between text-slate-800 shadow-inner -z-10">
                  <div>
                    <div class="text-[9px] uppercase tracking-widest text-amber-800 font-bold border-b border-amber-800/20 pb-1">Prologue</div>
                    <div class="text-[10px] font-serif italic mt-2 text-slate-700 leading-tight">"I never believed in taking right decisions. I took decisions and then made them right..."</div>
                  </div>
                  <div class="text-[8px] text-right font-mono text-slate-400">Page 1</div>
                </div>
              </div>
            </div>

          </div>

          <!-- Flip First Page Hint Tag -->
          <div class="absolute bottom-2 inset-x-0 flex items-center justify-center gap-1.5 text-xs text-amber-800 font-medium bg-amber-100/80 border border-amber-300/60 rounded-full px-3 py-0.5 mx-auto w-fit select-none">
            <svg class="w-3.5 h-3.5 text-amber-700 animate-pulse" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            <span>Hover center book to flip first page • Click any to select</span>
          </div>
        </div>

        <!-- Carousel Indicators & Arrow Controls -->
        <div class="flex items-center gap-4 mt-3">
          <button onclick="prevPodiumBook()" class="p-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-amber-50 hover:border-amber-400 shadow-sm transition-all" title="Previous Book">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
          </button>

          <!-- 5 Dots -->
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
        <!-- Golden Accent Top Corner -->
        <div class="absolute -top-12 -right-12 w-28 h-28 bg-amber-400/15 rounded-full blur-xl pointer-events-none"></div>

        <div>
          <!-- Bestseller Rank & Tag -->
          <div class="flex items-center justify-between mb-3">
            <span id="spotlightRank" class="text-xs font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-2.5 py-1 rounded">
              #1 IN CONTEMPORARY HINDI FICTION
            </span>
            <span id="spotlightStock" class="flex items-center gap-1.5 text-xs text-emerald-700 font-medium">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
              22 copies in Prayagraj
            </span>
          </div>

          <!-- Book Title -->
          <h3 id="spotlightTitle" class="font-serif text-2xl lg:text-3xl font-bold text-[#0A1128] leading-tight">
            Kasaibada
          </h3>

          <!-- Author -->
          <div class="flex items-center gap-2 mt-1.5 text-slate-600 text-sm">
            <span>By</span>
            <span id="spotlightAuthor" class="font-semibold text-slate-900">Manoj Rajan Tripathi</span>
            <span class="text-amber-500">★</span>
            <span id="spotlightRating" class="font-medium text-slate-700 text-xs">4.9 (540+ reviews)</span>
          </div>

          <!-- Excerpt / Why India is Reading This -->
          <div class="mt-4 p-4 bg-[#FAF8F5] border-l-4 border-[#D99B26] rounded-r-lg">
            <div class="text-xs uppercase font-bold text-amber-900 tracking-wider mb-1 flex items-center gap-1">
              <span>Why India is Reading This:</span>
            </div>
            <p id="spotlightQuote" class="text-xs lg:text-sm text-slate-700 italic font-serif leading-relaxed">
              "A gripping social allegory on power structures, moral struggle, and raw human resilience in northern India."
            </p>
          </div>

          <!-- Specifications badges -->
          <div class="grid grid-cols-2 gap-2 mt-4 text-[11px] text-slate-600">
            <div class="bg-slate-50 p-2 rounded border border-slate-200">
              <span class="text-slate-400 block text-[9px] uppercase">Format & Binding</span>
              <span id="spotlightPages" class="font-semibold text-slate-800">192 Pages • Paperback</span>
            </div>
            <div class="bg-slate-50 p-2 rounded border border-slate-200">
              <span class="text-slate-400 block text-[9px] uppercase">Publisher Edition</span>
              <span id="spotlightPublisher" class="font-semibold text-slate-800">Vani Prakashan</span>
            </div>
          </div>

          <!-- Pricing Row -->
          <div class="mt-6 flex items-baseline gap-3">
            <span id="spotlightPrice" class="text-3xl font-bold text-[#0A1128] font-serif">₹299.00</span>
            <span id="spotlightMRP" class="text-sm text-slate-400 line-through">₹395.00</span>
            <span id="spotlightSave" class="text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded">
              24% OFF
            </span>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row gap-3">
          <!-- Add to Cart -->
          <button id="spotlightAddCartBtn" onclick="addCurrentPodiumToCart()" class="flex-1 bg-[#D99B26] hover:bg-[#B88019] text-white py-3 px-4 rounded-xl font-semibold text-sm transition-all shadow-md flex items-center justify-center gap-2 group">
            <svg class="w-4 h-4 fill-current group-hover:scale-110 transition-transform" viewBox="0 0 24 24"><path d="M19 6h-2c0-2.76-2.24-5-5-5S7 3.24 7 6H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-7-3c1.66 0 3 1.34 3 3H9c0-1.66 1.34-3 3-3zm7 17H5V8h14v12z"/></svg>
            <span>Add to Cart</span>
          </button>

          <!-- WhatsApp Order -->
          <a id="spotlightWhatsAppBtn" href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Kasaibada%20at%20%E2%82%B9299." target="_blank" class="flex-1 bg-[#10B981] hover:bg-[#059669] text-white py-3 px-4 rounded-xl font-semibold text-sm transition-all shadow-md flex items-center justify-center gap-2">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            <span>WhatsApp COD</span>
          </a>

          <!-- Quick Preview Button -->
          <button id="spotlightPreviewBtn" onclick="openPodiumQuickView()" class="p-3 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl transition-colors shrink-0" title="Full Book Details">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
          </button>
        </div>

      </div>

    </div>

  </div>
</section>
"""

# C. SECTION 2: "MEHFIL-E-REKHTA" IMMERSIVE DARK POETRY LOUNGE
html_mehfil_rekhta = """
<!-- ======================================================================= -->
<!-- SECTION 3: "MEHFIL-E-REKHTA" IMMERSIVE DARK POETRY LOUNGE                -->
<!-- ======================================================================= -->
<section id="mehfilRekhtaSection" class="bg-gradient-to-b from-[#0F172A] via-[#1E1424] to-[#0A1128] text-amber-50 py-24 relative overflow-hidden">
  
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
      <div class="inline-flex items-center gap-2 bg-amber-900/40 text-amber-300 border border-amber-500/30 px-4 py-1 rounded-full text-xs font-bold tracking-widest uppercase shadow-lg">
        <span>महेफ़िल-ए-रेख़्ख़ता</span>
        <span>•</span>
        <span>MEHFIL-E-REKHTA</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-5xl font-bold text-amber-100 mt-3 tracking-wide">
        Urdu Poetry, Timeless Shayari & Progressive Literary Classics
      </h2>
      <p class="text-sm lg:text-base text-amber-200/80 mt-3 max-w-2xl mx-auto leading-relaxed">
        Step into an intimate literary mehfil featuring official Rekhta editions, rebellious prose, and the finest verse of the subcontinent.
      </p>
    </div>

    <!-- Interactive Shayar Quote Switcher -->
    <div class="mt-10 mb-12">
      <!-- Poet Selectable Pills -->
      <div class="flex flex-wrap items-center justify-center gap-3" id="poetSelectorPills">
        <button onclick="selectPoetQuote('elia')" class="poet-pill active px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/50 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(217,155,38,0.3)] transition-all">
          Jaun Elia
        </button>
        <button onclick="selectPoetQuote('faraz')" class="poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all">
          Ahmad Faraz
        </button>
        <button onclick="selectPoetQuote('manto')" class="poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all">
          Saadat Hasan Manto
        </button>
        <button onclick="selectPoetQuote('ghalib')" class="poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all">
          Mirza Ghalib
        </button>
      </div>

      <!-- Dynamic Couplet Display Card -->
      <div class="max-w-3xl mx-auto mt-6 bg-white/[0.04] backdrop-blur-md border border-amber-500/30 rounded-2xl p-6 lg:p-8 shadow-2xl relative" id="poetQuoteCard">
        <!-- Quote Icon -->
        <div class="text-amber-400/30 text-5xl font-serif absolute top-4 left-6 select-none">“</div>
        <div class="text-center px-4 py-2 relative z-10">
          <!-- Urdu Calligraphy text -->
          <div id="poetUrduVerse" class="font-serif text-2xl lg:text-3xl text-amber-200 font-normal leading-relaxed tracking-wide transition-opacity duration-300">
            شاید مجھے نکال کے پچھتا رہے ہوں آپ • محفل میں اس خیال سے پھر آ گیا ہوں میں
          </div>
          <!-- Devanagari Script -->
          <div id="poetHindiVerse" class="text-sm lg:text-base text-amber-100/90 font-serif mt-2 transition-opacity duration-300">
            "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं"
          </div>
          <!-- English Translation -->
          <div id="poetEngVerse" class="text-xs text-amber-300/70 italic mt-2 max-w-xl mx-auto transition-opacity duration-300">
            Perhaps you regret having cast me out; it is merely with this thought that I returned to the gathering.
          </div>
          <!-- Poet Name -->
          <div class="mt-4 pt-3 border-t border-amber-500/20 inline-flex items-center gap-2">
            <span class="w-6 h-[1px] bg-amber-400/50"></span>
            <span id="poetAttribution" class="text-xs font-bold uppercase tracking-widest text-amber-400">
              — Jaun Elia (क़तील-ए-अना)
            </span>
            <span class="w-6 h-[1px] bg-amber-400/50"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- Asymmetric Bento Gallery: 5 Glassmorphic Dark Velvet Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 mt-16">
      
      <!-- Card 1: Kyon (Jaun Elia) -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <!-- Floating 3D Book Cover -->
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="assets/book-kyon-jaun-elia.jpg" alt="Kyon - Jaun Elia" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>

        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Urdu Poetry • Rekhta</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">
            क्यों (Kyon)
          </h4>
          <p class="text-xs text-amber-200/70">Jaun Elia</p>
        </div>

        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹350.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-1', 'क्यों (Kyon) - Jaun Elia', 350, 'assets/book-kyon-jaun-elia.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">
              Add
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Kyon%20by%20Jaun%20Elia%20(%E2%82%B9350)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 2: Ranjish Hi Sahi (Ahmad Faraz) -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="assets/book-ranjish-hi-sahi.jpg" alt="Ranjish Hi Sahi" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>

        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Ghazal Collection</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">
            रंजिश ही सही
          </h4>
          <p class="text-xs text-amber-200/70">Ahmad Faraz</p>
        </div>

        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹399.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 5.0</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-2', 'रंजिश ही सही - Ahmad Faraz', 399, 'assets/book-ranjish-hi-sahi.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">
              Add
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Ranjish%20Hi%20Sahi%20(%E2%82%B9399)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 3: Dozakh Nama -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="assets/hero-book-dozakh.jpg" alt="Dozakh Nama" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>

        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Literary Fiction</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">
            दोज़ख़नामा
          </h4>
          <p class="text-xs text-amber-200/70">Rabi Sankar Bal (Manto & Ghalib)</p>
        </div>

        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹450.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-3', 'दोज़ख़नामा (Dozakh Nama)', 450, 'assets/hero-book-dozakh.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">
              Add
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Dozakh%20Nama%20(%E2%82%B9450)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 4: Thanda Ghost -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="assets/hero-book-thanda-ghost.jpg" alt="Thanda Ghost" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>

        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Progressive Stories</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">
            ठंडा गोश्त
          </h4>
          <p class="text-xs text-amber-200/70">Saadat Hasan Manto</p>
        </div>

        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹299.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.8</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-4', 'ठंडा गोश्त - Saadat Hasan Manto', 299, 'assets/hero-book-thanda-ghost.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">
              Add
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Thanda%20Ghost%20(%E2%82%B9299)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Card 5: Dhuaan -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="assets/hero-book-dhuaan.jpg" alt="Dhuaan" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>

        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Urdu Classics</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">
            धुआँ (Dhuaan)
          </h4>
          <p class="text-xs text-amber-200/70">Gulzar & Masters</p>
        </div>

        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹350.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-5', 'धुआँ (Dhuaan) - Gulzar', 350, 'assets/hero-book-dhuaan.jpg')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">
              Add
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Dhuaan%20(%E2%82%B9350)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">
              WhatsApp
            </a>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>
"""

# D. SECTION 3: INTERACTIVE "BUNDLE UNBOXING" SHOWCASE
html_bundle_unboxing = """
<!-- ======================================================================= -->
<!-- SECTION 4: INTERACTIVE "BUNDLE UNBOXING" SHOWCASE                        -->
<!-- ======================================================================= -->
<section id="bundleUnboxingSection" class="py-20 lg:py-24 bg-[#F4EFE6] border-y border-amber-900/10 relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 bg-amber-200/70 text-amber-900 border border-amber-400/40 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm">
        <svg class="w-3.5 h-3.5 fill-current text-amber-800" viewBox="0 0 24 24"><path d="M21 16.5l-9 5.25L3 16.5v-9l9-5.25 9 5.25v9zM12 3.75L4.5 8.1 12 12.45l7.5-4.35L12 3.75zM4.5 9.9v6.6l6.75 3.9v-6.6L4.5 9.9zm8.25 10.5l6.75-3.9V9.9l-6.75 3.9v6.6z"/></svg>
        <span>COLLECTOR'S CORNER & BOX SETS</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3">
        The Unboxing Showcase: Curated Multi-Volume Sets
      </h2>
      <p class="text-sm lg:text-base text-slate-600 mt-2">
        Hover over any collector's box to unpack the editions and inspect the individual titles inside.
      </p>
    </div>

    <!-- 3 Oversized Feature Bundle Cards -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      
      <!-- BUNDLE 1: Arundhati Roy Definitive Double Feature -->
      <div class="bg-white border border-[#E4DAC7] rounded-2xl p-6 lg:p-7 shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group/bundle">
        <div>
          <!-- Tag & Savings Pill -->
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded-full">
              Man Booker Winner Set
            </span>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full">
              Save ₹399 Instantly
            </span>
          </div>

          <h3 class="font-serif text-xl font-bold text-[#0A1128] mt-2 group-hover/bundle:text-[#D99B26] transition-colors">
            Arundhati Roy Definitive Duo
          </h3>
          <p class="text-xs text-slate-500 mt-1">2 Complete Novels in Illustrated Slipcase</p>

          <!-- Interactive Unbox on Hover Stage -->
          <div class="bundle-unbox-stage relative h-64 flex items-center justify-center my-6 perspective-[1000px] cursor-pointer">
            <!-- Box Slipcase Background Graphic -->
            <div class="absolute inset-x-8 inset-y-4 bg-amber-900/10 border-2 border-dashed border-amber-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-medium text-amber-900/40 uppercase tracking-widest font-mono">Collector Slipcase</span>
            </div>

            <!-- Fanned Books (Animated via CSS classes on hover) -->
            <!-- Book 1 (Left Fan) -->
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="assets/hero-book-arundhati.jpg" alt="The God of Small Things" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>

            <!-- Book 2 (Right Fan) -->
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="assets/book-cheelwali-kothi.jpg" alt="The Ministry of Utmost Happiness" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
          </div>

          <!-- Included Titles Checklist -->
          <div class="space-y-1.5 text-xs text-slate-600 bg-amber-50/60 p-3 rounded-lg border border-amber-200/50">
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
              <span class="text-xs text-slate-400 line-through ml-2">₹1,198.00</span>
            </div>
            <span class="text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded">
              33% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('bundle-1', 'Arundhati Roy Definitive Duo Boxset', 799, 'assets/hero-book-arundhati.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Arundhati%20Roy%20Duo%20Boxset%20(%E2%82%B9799)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- BUNDLE 2: Sarah J. Maas – ACOTAR 5-Book Boxset -->
      <div class="bg-white border border-[#E4DAC7] rounded-2xl p-6 lg:p-7 shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group/bundle">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-purple-900 bg-purple-100 border border-purple-300 px-2.5 py-0.5 rounded-full">
              Global BookTok Sensation
            </span>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full">
              Save ₹1,100 Instantly
            </span>
          </div>

          <h3 class="font-serif text-xl font-bold text-[#0A1128] mt-2 group-hover/bundle:text-[#D99B26] transition-colors">
            A Court of Thorns and Roses 5-Book Set
          </h3>
          <p class="text-xs text-slate-500 mt-1">Complete Sarah J. Maas Fantasy Boxset</p>

          <!-- Interactive Unbox on Hover Stage -->
          <div class="bundle-unbox-stage relative h-64 flex items-center justify-center my-6 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-purple-900/10 border-2 border-dashed border-purple-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-medium text-purple-900/40 uppercase tracking-widest font-mono">5 Volumes Pack</span>
            </div>

            <!-- Fanned Books (3 Visible in Fan) -->
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="assets/book-acotar.jpg" alt="ACOTAR Volume 1" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-mid absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="assets/book-alchemised.jpg" alt="ACOTAR Volume 2" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-30">
              <img src="assets/book-acotar.jpg" alt="ACOTAR Volume 3" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
          </div>

          <div class="space-y-1.5 text-xs text-slate-600 bg-purple-50/60 p-3 rounded-lg border border-purple-200/50">
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
              <span class="text-xs text-slate-400 line-through ml-2">₹2,999.00</span>
            </div>
            <span class="text-xs font-bold text-purple-800 bg-purple-100 border border-purple-300 px-2 py-0.5 rounded">
              37% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('bundle-2', 'A Court of Thorns and Roses 5-Book Boxset', 1899, 'assets/book-acotar.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20ACOTAR%20Boxset%20(%E2%82%B91899)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- BUNDLE 3: Haruki Murakami 3-Book Collector's Set -->
      <div class="bg-white border border-[#E4DAC7] rounded-2xl p-6 lg:p-7 shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group/bundle">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-rose-900 bg-rose-100 border border-rose-300 px-2.5 py-0.5 rounded-full">
              Modern Japanese Master
            </span>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full">
              Save ₹600 Instantly
            </span>
          </div>

          <h3 class="font-serif text-xl font-bold text-[#0A1128] mt-2 group-hover/bundle:text-[#D99B26] transition-colors">
            Best of Haruki Murakami (3 Books)
          </h3>
          <p class="text-xs text-slate-500 mt-1">Vintage Classics Commemorative Set</p>

          <!-- Interactive Unbox on Hover Stage -->
          <div class="bundle-unbox-stage relative h-64 flex items-center justify-center my-6 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-rose-900/10 border-2 border-dashed border-rose-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-medium text-rose-900/40 uppercase tracking-widest font-mono">Murakami Box</span>
            </div>

            <!-- Fanned Books -->
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="assets/hero-book-murakami.jpg" alt="Norwegian Wood" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="assets/book-ratan-tata.jpg" alt="Kafka on the Shore" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
          </div>

          <div class="space-y-1.5 text-xs text-slate-600 bg-rose-50/60 p-3 rounded-lg border border-rose-200/50">
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
              <span class="text-xs text-slate-400 line-through ml-2">₹1,899.00</span>
            </div>
            <span class="text-xs font-bold text-rose-800 bg-rose-100 border border-rose-300 px-2 py-0.5 rounded">
              32% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('bundle-3', 'Best of Haruki Murakami 3-Book Set', 1299, 'assets/hero-book-murakami.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Murakami%203-Book%20Boxset%20(%E2%82%B91299)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>
"""

# E. SECTION 4: THE "INDIAN REGIONAL & FICTION" EDITORIAL MAGAZINE MASONRY
html_regional_magazine = """
<!-- ======================================================================= -->
<!-- SECTION 5: "INDIAN REGIONAL & FICTION" EDITORIAL MAGAZINE MASONRY        -->
<!-- ======================================================================= -->
<section id="regionalMagazineSection" class="py-20 lg:py-24 bg-[#FAF8F5] relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <!-- Section Header -->
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 pb-4 border-b border-amber-900/10 gap-4">
      <div>
        <div class="inline-flex items-center gap-2 bg-amber-100 text-[#D99B26] border border-amber-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase mb-2">
          <span>LITERARY SPOTLIGHT • REGIONAL CLASSICS</span>
        </div>
        <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128]">
          Indian Voices & Contemporary Hindi Fiction
        </h2>
        <p class="text-sm text-slate-600 mt-1 max-w-xl">
          Original Hindi prose, Sahitya Akademi laureates, and evocative tales rooted in the heartlands of India.
        </p>
      </div>
      <a href="#shopAllSection" class="text-xs font-bold uppercase tracking-wider text-[#D99B26] hover:text-[#B88019] inline-flex items-center gap-1">
        <span>Explore All 2,000+ Regional Titles</span>
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
      </a>
    </div>

    <!-- Editorial Bento Grid (5 Cols Hero Feature + 7 Cols Vintage Library Index Cards) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
      
      <!-- LEFT 5 COLS: Feature Story Card (Cheelwali Kothi by Sara Rai) -->
      <div class="lg:col-span-5 bg-white border border-[#E8DFC8] rounded-2xl p-6 lg:p-8 shadow-md hover:shadow-xl transition-all duration-300 flex flex-col justify-between relative group">
        <div>
          <!-- Badges -->
          <div class="flex items-center justify-between mb-4">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-3 py-1 rounded-full">
              Prayagraj Literary Heritage Pick
            </span>
            <span class="text-[11px] font-semibold text-rose-700 bg-rose-50 border border-rose-200 px-2.5 py-0.5 rounded-full">
              Only 4 copies left
            </span>
          </div>

          <!-- Feature Cover Art -->
          <div class="w-44 lg:w-48 mx-auto aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_40px_rgba(0,0,0,0.4)] my-4 group-hover:scale-105 transition-transform duration-300 relative">
            <img src="assets/book-cheelwali-kothi.jpg" alt="Cheelwali Kothi - Sara Rai" class="w-full h-full object-cover">
            <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
          </div>

          <!-- Editorial Meta & Title -->
          <h3 class="font-serif text-2xl font-bold text-[#0A1128] text-center mt-3 group-hover:text-[#D99B26] transition-colors">
            चीलवाली कोठी (Cheelwali Kothi)
          </h3>
          <p class="text-xs text-slate-500 text-center mt-0.5">By Sara Rai • Rajkamal Prakashan</p>

          <!-- Pull Quote -->
          <div class="mt-4 p-4 bg-[#FAF8F5] border-l-2 border-amber-500 rounded-r-lg">
            <p class="font-serif italic text-xs lg:text-sm text-slate-700 leading-relaxed">
              "A haunting, lyrical masterpiece navigating ancestral mansions, lost memories, and the quiet dignity of Uttar Pradesh."
            </p>
          </div>

          <div class="text-[11px] text-slate-500 text-center mt-3">
            <span>Paperback • 248 Pages • Hindi Literature</span>
          </div>
        </div>

        <div class="mt-6 pt-4 border-t border-slate-100">
          <div class="flex items-baseline justify-between mb-4">
            <div>
              <span class="text-2xl font-bold text-[#0A1128] font-serif">₹299.00</span>
              <span class="text-xs text-slate-400 line-through ml-2">₹395.00</span>
            </div>
            <span class="text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded">
              24% OFF
            </span>
          </div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="addToCart('reg-hero', 'चीलवाली कोठी (Cheelwali Kothi)', 299, 'assets/book-cheelwali-kothi.jpg')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Cheelwali%20Kothi%20(%E2%82%B9299)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- RIGHT 7 COLS: 2x2 Grid of Vintage Library Index Cards -->
      <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-5">
        
        <!-- Index Card 1: Nar Nareeshwar -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <!-- Cover -->
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="assets/book-nar-nareeshwar.jpg" alt="Nar Nareeshwar" class="w-full h-full object-cover">
            </div>
            <!-- Metadata in typewriter feel -->
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between text-[10px] font-mono text-slate-400">
                <span>#IND-0824</span>
                <span class="text-rose-600 font-bold border border-rose-300 px-1 rounded text-[9px]">25% OFF</span>
              </div>
              <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors">
                नर-नारीश्वर
              </h4>
              <p class="text-[11px] text-slate-600">Vishnu Prabhakar</p>
              <div class="text-[10px] text-amber-800 font-mono mt-1">Sahitya Akademi Award</div>
              <div class="mt-2 text-xs font-bold text-slate-900 font-serif">₹320.00 <span class="text-[10px] text-slate-400 line-through">₹425</span></div>
            </div>
          </div>
          <!-- Quick Slide-up Actions on Hover -->
          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2">
            <button onclick="addToCart('index-1', 'नर-नारीश्वर - Vishnu Prabhakar', 320, 'assets/book-nar-nareeshwar.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Nar-Nareeshwar%20(%E2%82%B9320)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Index Card 2: Patthar aur Alpatthar -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="assets/book-patthar-alpatthar.jpg" alt="Patthar aur Alpatthar" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between text-[10px] font-mono text-slate-400">
                <span>#IND-0912</span>
                <span class="text-rose-600 font-bold border border-rose-300 px-1 rounded text-[9px]">20% OFF</span>
              </div>
              <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors">
                पत्थर और अलपत्थर
              </h4>
              <p class="text-[11px] text-slate-600">Surendra Verma</p>
              <div class="text-[10px] text-amber-800 font-mono mt-1">Acclaimed Hindi Play</div>
              <div class="mt-2 text-xs font-bold text-slate-900 font-serif">₹240.00 <span class="text-[10px] text-slate-400 line-through">₹300</span></div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2">
            <button onclick="addToCart('index-2', 'पत्थर और अलपत्थर - Surendra Verma', 240, 'assets/book-patthar-alpatthar.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Patthar%20aur%20Alpatthar%20(%E2%82%B9240)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Index Card 3: Aurat Farosh -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="assets/book-aurat-farosh.jpg" alt="Aurat Farosh" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between text-[10px] font-mono text-slate-400">
                <span>#IND-0741</span>
                <span class="text-rose-600 font-bold border border-rose-300 px-1 rounded text-[9px]">22% OFF</span>
              </div>
              <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors">
                औरत फ़रोश
              </h4>
              <p class="text-[11px] text-slate-600">Kanhaiyalal Nandan</p>
              <div class="text-[10px] text-amber-800 font-mono mt-1">Social Investigative Fiction</div>
              <div class="mt-2 text-xs font-bold text-slate-900 font-serif">₹280.00 <span class="text-[10px] text-slate-400 line-through">₹360</span></div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2">
            <button onclick="addToCart('index-3', 'औरत फ़रोश - Kanhaiyalal Nandan', 280, 'assets/book-aurat-farosh.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Aurat%20Farosh%20(%E2%82%B9280)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Index Card 4: Lagbhag Single -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="assets/book-lagbhag-single.jpg" alt="Lagbhag Single" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between text-[10px] font-mono text-slate-400">
                <span>#IND-0533</span>
                <span class="text-rose-600 font-bold border border-rose-300 px-1 rounded text-[9px]">28% OFF</span>
              </div>
              <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 truncate group-hover:text-[#D99B26] transition-colors">
                लगभग सिंगल
              </h4>
              <p class="text-[11px] text-slate-600">Nikhil Sachan</p>
              <div class="text-[10px] text-amber-800 font-mono mt-1">Youth & Kanpur Chronicles</div>
              <div class="mt-2 text-xs font-bold text-slate-900 font-serif">₹250.00 <span class="text-[10px] text-slate-400 line-through">₹350</span></div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2">
            <button onclick="addToCart('index-4', 'लगभग सिंगल - Nikhil Sachan', 250, 'assets/book-lagbhag-single.jpg')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">
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

# F. SECTION 5: INTERACTIVE "LAW & ACADEMIC VAULT" SPLIT-FINDER
html_academic_vault = """
<!-- ======================================================================= -->
<!-- SECTION 6: INTERACTIVE "LAW & ACADEMIC VAULT" SPLIT-FINDER               -->
<!-- ======================================================================= -->
<section id="academicVaultSection" class="py-20 lg:py-24 bg-white border-y border-slate-200 relative">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto mb-12">
      <div class="inline-flex items-center gap-2 bg-slate-100 text-slate-800 border border-slate-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm">
        <svg class="w-3.5 h-3.5 fill-current text-slate-700" viewBox="0 0 24 24"><path d="M12 2L1 21h22L12 2zm0 3.8l7.53 13.2H4.47L12 5.8zM11 10v4h2v-4h-2zm0 6v2h2v-2h-2z"/></svg>
        <span>ACADEMIC & SCHOLARLY VAULT</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3">
        Law, Judiciary & Sahitya Reference Archive
      </h2>
      <p class="text-sm lg:text-base text-slate-600 mt-2">
        Authoritative legal treatises, Hindi linguistics, university standards, and competitive civil services references.
      </p>
    </div>

    <!-- Interactive Sticky Two-Pane Vault Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      
      <!-- LEFT 4 COLS: Library Drawer Selector (Sticky on Desktop) -->
      <div class="lg:col-span-4 lg:sticky lg:top-28 space-y-4">
        
        <div class="bg-[#FAF8F5] border border-amber-900/10 rounded-2xl p-5 shadow-sm">
          <div class="text-xs uppercase font-bold text-slate-400 tracking-wider mb-3">
            Select Archive Drawer:
          </div>

          <!-- Drawer Tabs -->
          <div class="space-y-2" id="vaultDrawerTabs">
            
            <!-- Tab 1: Law & Jurisprudence (Active by default) -->
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

            <!-- Tab 2: Hindi Sahitya & Vyakaran -->
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

            <!-- Tab 3: Competition & Civil Services -->
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

            <!-- Tab 4: History & Dalit Vimarsh -->
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
        <div class="bg-gradient-to-br from-[#0A1128] to-[#1E293B] text-white rounded-2xl p-5 shadow-md">
          <div class="text-amber-400 text-xs font-bold uppercase tracking-wider mb-1 flex items-center gap-1.5">
            <span>📚 Bulk & Institutional Supply</span>
          </div>
          <h4 class="font-serif text-sm font-bold">University & Advocate Book Concierge</h4>
          <p class="text-[11px] text-slate-300 mt-1 leading-relaxed">
            Need multiple copies for chambers, bar libraries, or college batches? Get customized quotation with GST invoice.
          </p>
          <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20am%20inquiring%20about%20Institutional%20Bulk%20Academic%20Orders." target="_blank" class="mt-3 inline-flex items-center gap-1.5 bg-[#10B981] hover:bg-[#059669] text-white text-xs font-semibold py-2 px-3 rounded-lg transition-colors w-full justify-center">
            <span>Chat for Institutional Discount</span>
          </a>
        </div>

      </div>

      <!-- RIGHT 8 COLS: High-Density Spec-Sheet Catalog Grid -->
      <div class="lg:col-span-8">
        
        <!-- Live Category Title Badge -->
        <div class="flex items-center justify-between pb-3 mb-6 border-b border-slate-200">
          <div class="flex items-center gap-2">
            <span id="vaultDrawerActiveTitle" class="font-serif text-lg font-bold text-[#0A1128]">
              ⚖️ Law & Jurisprudence (Essential Legal References)
            </span>
          </div>
          <span id="vaultCountTag" class="text-xs text-slate-500 font-mono">Showing 4 cataloged editions</span>
        </div>

        <!-- Spec-Sheet Grid Cards Container -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5" id="vaultCardsGrid">
          
          <!-- Card 1: Modi Medical Jurisprudence -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="assets/book-medical-jurisprudence.jpg" alt="Medical Jurisprudence" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 min-w-0 flex flex-col justify-between">
              <div>
                <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded">
                  LexisNexis • Hardcover
                </span>
                <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors">
                  Modi Medical Jurisprudence & Toxicology
                </h4>
                <p class="text-[11px] text-slate-500">Kannan & K. Mathiharan</p>
                <div class="text-[10px] text-emerald-700 font-medium mt-1">✓ In Stock at Prayagraj</div>
              </div>
              <div class="mt-2 pt-2 border-t border-slate-200 flex items-center justify-between">
                <div>
                  <span class="text-base font-bold text-[#0A1128] font-serif">₹1,850.00</span>
                  <span class="text-[10px] text-slate-400 line-through ml-1">₹2,195</span>
                </div>
                <button onclick="addToCart('law-1', 'Modi Medical Jurisprudence', 1850, 'assets/book-medical-jurisprudence.jpg')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold" title="Add to Cart">
                  Add to Cart
                </button>
              </div>
            </div>
          </div>

          <!-- Card 2: Lawful Awful -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="assets/book-lawful-awful.jpg" alt="Lawful Awful" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 min-w-0 flex flex-col justify-between">
              <div>
                <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded">
                  Penguin Law • Memoir
                </span>
                <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors">
                  Lawful Awful: Life in Law & Courtrooms
                </h4>
                <p class="text-[11px] text-slate-500">Justice Venkataswami</p>
                <div class="text-[10px] text-emerald-700 font-medium mt-1">✓ In Stock at Prayagraj</div>
              </div>
              <div class="mt-2 pt-2 border-t border-slate-200 flex items-center justify-between">
                <div>
                  <span class="text-base font-bold text-[#0A1128] font-serif">₹450.00</span>
                  <span class="text-[10px] text-slate-400 line-through ml-1">₹599</span>
                </div>
                <button onclick="addToCart('law-2', 'Lawful Awful: Life in Law', 450, 'assets/book-lawful-awful.jpg')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold" title="Add to Cart">
                  Add to Cart
                </button>
              </div>
            </div>
          </div>

          <!-- Card 3: 10 Faisle Jinhone Desh Badal Diya -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="assets/book-10-faisle.jpg" alt="10 Faisle" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 min-w-0 flex flex-col justify-between">
              <div>
                <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded">
                  Judicial Landmark • Hindi
                </span>
                <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors">
                  १० फ़ैसले जिन्होंने देश बदल दिया
                </h4>
                <p class="text-[11px] text-slate-500">Zia Mody (Hindi Edition)</p>
                <div class="text-[10px] text-emerald-700 font-medium mt-1">✓ In Stock at Prayagraj</div>
              </div>
              <div class="mt-2 pt-2 border-t border-slate-200 flex items-center justify-between">
                <div>
                  <span class="text-base font-bold text-[#0A1128] font-serif">₹320.00</span>
                  <span class="text-[10px] text-slate-400 line-through ml-1">₹395</span>
                </div>
                <button onclick="addToCart('law-3', '१० फ़ैसले जिन्होंने देश बदल दिया', 320, 'assets/book-10-faisle.jpg')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold" title="Add to Cart">
                  Add to Cart
                </button>
              </div>
            </div>
          </div>

          <!-- Card 4: Bench & Bar -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="assets/book-bench-bar.jpg" alt="Bench & Bar" class="w-full h-full object-cover">
            </div>
            <div class="flex-1 min-w-0 flex flex-col justify-between">
              <div>
                <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded">
                  Legal Ethics & History
                </span>
                <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors">
                  Bench and Bar: Reminiscences of Courts
                </h4>
                <p class="text-[11px] text-slate-500">Universal Law Publishing</p>
                <div class="text-[10px] text-emerald-700 font-medium mt-1">✓ In Stock at Prayagraj</div>
              </div>
              <div class="mt-2 pt-2 border-t border-slate-200 flex items-center justify-between">
                <div>
                  <span class="text-base font-bold text-[#0A1128] font-serif">₹590.00</span>
                  <span class="text-[10px] text-slate-400 line-through ml-1">₹750</span>
                </div>
                <button onclick="addToCart('law-4', 'Bench and Bar: Reminiscences', 590, 'assets/book-bench-bar.jpg')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold" title="Add to Cart">
                  Add to Cart
                </button>
              </div>
            </div>
          </div>

        </div>

      </div>

    </div>

  </div>
</section>
"""

# G. TRUST STRIP & FAST DELIVERY REASSURANCE
html_trust_strip = """
<!-- ======================================================================= -->
<!-- SECTION 7: TRUST FEATURES & PRAYAGRAJ DISPATCH STRIP                     -->
<!-- ======================================================================= -->
<section id="trustFeaturesSection" class="bg-[#FAF8F5] py-14 border-t border-amber-900/10">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      
      <!-- Feature 1 -->
      <div class="flex items-start gap-4 p-4 rounded-xl bg-white border border-slate-200/80 shadow-sm">
        <div class="w-12 h-12 rounded-xl bg-amber-100 text-[#D99B26] flex items-center justify-center shrink-0">
          <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M12 2L1 21h22L12 2zm0 3.8l7.53 13.2H4.47L12 5.8z"/></svg>
        </div>
        <div>
          <h4 class="font-bold text-sm text-[#0A1128]">100% Authentic Books</h4>
          <p class="text-xs text-slate-500 mt-0.5 leading-relaxed">Direct partner of Rekhta, Rajkamal, Vani, Penguin & HarperCollins.</p>
        </div>
      </div>

      <!-- Feature 2 -->
      <div class="flex items-start gap-4 p-4 rounded-xl bg-white border border-slate-200/80 shadow-sm">
        <div class="w-12 h-12 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center shrink-0">
          <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
        </div>
        <div>
          <h4 class="font-bold text-sm text-[#0A1128]">Instant WhatsApp COD</h4>
          <p class="text-xs text-slate-500 mt-0.5 leading-relaxed">One-click order confirmation to +91 8881122722 with live tracking.</p>
        </div>
      </div>

      <!-- Feature 3 -->
      <div class="flex items-start gap-4 p-4 rounded-xl bg-white border border-slate-200/80 shadow-sm">
        <div class="w-12 h-12 rounded-xl bg-blue-100 text-blue-600 flex items-center justify-center shrink-0">
          <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-2 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>
        </div>
        <div>
          <h4 class="font-bold text-sm text-[#0A1128]">Pan-India Express Dispatch</h4>
          <p class="text-xs text-slate-500 mt-0.5 leading-relaxed">Dispatches within 24 hours directly from our Prayagraj facility.</p>
        </div>
      </div>

      <!-- Feature 4 -->
      <div class="flex items-start gap-4 p-4 rounded-xl bg-white border border-slate-200/80 shadow-sm">
        <div class="w-12 h-12 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center shrink-0">
          <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
        </div>
        <div>
          <h4 class="font-bold text-sm text-[#0A1128]">Cultural Book Community</h4>
          <p class="text-xs text-slate-500 mt-0.5 leading-relaxed">Connecting over 85,000 readers who celebrate authentic Indian writing.</p>
        </div>
      </div>

    </div>
  </div>
</section>
"""

# H. FLOATING CONCIERGE DOCK
html_floating_dock = """
<!-- ======================================================================= -->
<!-- FLOATING CONCIERGE DOCK (BOTTOM-RIGHT)                                  -->
<!-- ======================================================================= -->
<div class="fixed bottom-6 right-6 z-50 flex items-center gap-3">
  <!-- WhatsApp Concierge Widget -->
  <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%20India%2C%20I%20need%20assistance%20finding%20a%20book." target="_blank" class="group relative flex items-center gap-2 bg-[#25D366] hover:bg-[#1EBE5D] text-white px-4 py-3 rounded-full shadow-[0_10px_25px_rgba(37,211,102,0.4)] transition-all hover:scale-105" title="Chat with Indigo Books Concierge">
    <!-- Pulse Ring -->
    <span class="absolute -inset-1 rounded-full bg-[#25D366]/40 animate-ping pointer-events-none"></span>
    <svg class="w-5 h-5 fill-current shrink-0" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
    <div class="hidden sm:flex flex-col text-left">
      <span class="text-xs font-bold leading-tight">WhatsApp Order</span>
      <span class="text-[9px] text-emerald-100 font-medium leading-tight">+91 8881122722</span>
    </div>
  </a>

  <!-- Floating Quick Cart Trigger -->
  <button onclick="openCartDrawer()" class="relative flex items-center justify-center w-12 h-12 bg-[#0A1128] hover:bg-[#D99B26] text-white rounded-full shadow-[0_10px_25px_rgba(10,17,40,0.4)] transition-all hover:scale-105" title="View Cart">
    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
    <span id="floatingCartBadge" class="absolute -top-1 -right-1 bg-rose-600 text-white font-bold text-[10px] w-4 h-4 rounded-full flex items-center justify-center shadow">0</span>
  </button>
</div>
"""

# I. INTERACTIVE JAVASCRIPT & STYLES TO APPEND
js_and_css_additions = """
<style>
/* Ticker scroll keyframe */
@keyframes marqueeScroll {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
.animate-marquee {
  display: flex;
  width: max-content;
  animation: marqueeScroll 32s linear infinite;
}
.animate-marquee:hover {
  animation-play-state: paused;
}

/* 3D Turntable Stage Positioning */
.podium-book-card {
  transform-style: preserve-3d;
}
.book-3d-wrapper {
  transform-style: preserve-3d;
  perspective: 1000px;
}
.book-cover-front {
  transform-origin: left center;
  transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease;
  backface-visibility: hidden;
}
/* Flip First Page Hover Effect */
.podium-book-card.is-active:hover .book-cover-front {
  transform: rotateY(-32deg);
  box-shadow: -15px 25px 40px rgba(0,0,0,0.7);
}
.podium-book-card.is-active .book-3d-wrapper {
  filter: drop-shadow(0 20px 30px rgba(217,155,38,0.35));
}

/* Bundle Unbox Playing-Card Hover Fan Physics */
.bundle-unbox-stage .unbox-book {
  transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}
/* Default: Stacked neatly */
.bundle-unbox-stage .unbox-book-1 { transform: translateX(-8px) rotate(-3deg); }
.bundle-unbox-stage .unbox-book-mid { transform: translateX(0px) rotate(0deg); }
.bundle-unbox-stage .unbox-book-2 { transform: translateX(8px) rotate(3deg); }

/* On Group Hover: Fan Out Left-to-Right like Playing Cards */
.group\/bundle:hover .unbox-book-1 {
  transform: translateX(-50px) rotate(-16deg) scale(0.95);
  box-shadow: -20px 20px 30px rgba(0,0,0,0.4);
}
.group\/bundle:hover .unbox-book-mid {
  transform: translateX(0px) rotate(0deg) scale(1.05);
  box-shadow: 0 25px 40px rgba(0,0,0,0.5);
  z-index: 30;
}
.group\/bundle:hover .unbox-book-2 {
  transform: translateX(50px) rotate(16deg) scale(0.95);
  box-shadow: 20px 20px 30px rgba(0,0,0,0.4);
}

/* Vault Drawer Button Active/Inactive */
.vault-drawer-btn.active {
  background-color: #0A1128;
  color: #FFFFFF;
  border-left: 4px solid #D99B26;
  box-shadow: 0 4px 15px rgba(10,17,40,0.15);
}
.vault-drawer-btn:not(.active) {
  background-color: #FFFFFF;
  color: #334155;
  border: 1px solid #E2E8F0;
}
.vault-drawer-btn:not(.active):hover {
  background-color: #FEF3C7;
  color: #0A1128;
  border-color: #FCD34D;
}
</style>

<script>
// ==========================================
// 1. PODIUM BESTSELLERS 3D STAGE LOGIC
// ==========================================
const PODIUM_DATA = [
  {
    id: "podium-1",
    title: "Diary of a Wimpy Kid: Hot Mess",
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
    pages: "112 Pages • Paperback • Penguin Classics",
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

let currentPodiumIndex = 2; // Kasaibada default center

function updatePodiumStage() {
  const cards = document.querySelectorAll('.podium-book-card');
  const count = PODIUM_DATA.length;

  cards.forEach((card, i) => {
    // Relative offset from current active book
    let offset = i - currentPodiumIndex;
    if (offset < -2) offset += count;
    if (offset > 2) offset -= count;

    card.classList.remove('is-active');
    
    if (offset === 0) {
      // Center active book
      card.classList.add('is-active');
      card.style.transform = 'translateX(0px) scale(1.15) rotateY(-8deg)';
      card.style.zIndex = '30';
      card.style.opacity = '1';
    } else if (offset === -1) {
      // Left 1
      card.style.transform = 'translateX(-110px) scale(0.9) rotateY(22deg)';
      card.style.zIndex = '20';
      card.style.opacity = '0.85';
    } else if (offset === 1) {
      // Right 1
      card.style.transform = 'translateX(110px) scale(0.9) rotateY(-22deg)';
      card.style.zIndex = '20';
      card.style.opacity = '0.85';
    } else if (offset <= -2) {
      // Far Left
      card.style.transform = 'translateX(-210px) scale(0.75) rotateY(35deg)';
      card.style.zIndex = '10';
      card.style.opacity = '0.45';
    } else if (offset >= 2) {
      // Far Right
      card.style.transform = 'translateX(210px) scale(0.75) rotateY(-35deg)';
      card.style.zIndex = '10';
      card.style.opacity = '0.45';
    }
  });

  // Update Spotlight Panel
  const book = PODIUM_DATA[currentPodiumIndex];
  if (book) {
    document.getElementById('spotlightRank').innerText = book.rank;
    document.getElementById('spotlightTitle').innerText = book.title;
    document.getElementById('spotlightAuthor').innerText = book.author;
    document.getElementById('spotlightRating').innerText = book.rating;
    document.getElementById('spotlightQuote').innerText = `"${book.quote}"`;
    document.getElementById('spotlightPages').innerText = book.pages;
    document.getElementById('spotlightPublisher').innerText = book.publisher;
    document.getElementById('spotlightPrice').innerText = `₹${book.price}.00`;
    document.getElementById('spotlightMRP').innerText = `₹${book.mrp}.00`;
    document.getElementById('spotlightSave').innerText = book.save;
    document.getElementById('spotlightStock').innerHTML = `
      <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
      ${book.stock}
    `;
    
    // Update WhatsApp link
    const waText = encodeURIComponent(`Hello Indigo Books, I want to order ${book.title} by ${book.author} at ₹${book.price}.`);
    document.getElementById('spotlightWhatsAppBtn').href = `https://wa.me/918881122722?text=${waText}`;
  }

  // Update indicators
  const dots = document.querySelectorAll('#podiumIndicators button');
  dots.forEach((dot, idx) => {
    if (idx === currentPodiumIndex) {
      dot.className = 'w-7 h-2.5 rounded-full bg-[#D99B26] transition-all duration-300';
    } else {
      dot.className = 'w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300';
    }
  });
}

function selectPodiumBook(index) {
  currentPodiumIndex = index;
  updatePodiumStage();
}

function nextPodiumBook() {
  currentPodiumIndex = (currentPodiumIndex + 1) % PODIUM_DATA.length;
  updatePodiumStage();
}

function prevPodiumBook() {
  currentPodiumIndex = (currentPodiumIndex - 1 + PODIUM_DATA.length) % PODIUM_DATA.length;
  updatePodiumStage();
}

function addCurrentPodiumToCart() {
  const book = PODIUM_DATA[currentPodiumIndex];
  if (book) {
    addToCart(book.id, book.title, book.price, book.image);
  }
}

function openPodiumQuickView() {
  const book = PODIUM_DATA[currentPodiumIndex];
  if (book && typeof openQuickView === 'function') {
    openQuickView({
      title: book.title,
      author: book.author,
      price: book.price,
      mrp: book.mrp,
      image: book.image,
      desc: book.quote,
      category: book.rank,
      format: book.pages
    });
  }
}

// ==========================================
// 2. MEHFIL-E-REKHTA POET QUOTE SWITCHER
// ==========================================
const POET_QUOTES = {
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

function selectPoetQuote(poetKey) {
  const q = POET_QUOTES[poetKey];
  if (!q) return;

  // Update pills
  const pills = document.querySelectorAll('#poetSelectorPills button');
  pills.forEach(p => {
    p.className = 'poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all';
  });
  if (event && event.currentTarget) {
    event.currentTarget.className = 'poet-pill active px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/50 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(217,155,38,0.3)] transition-all';
  }

  // Crossfade text
  const urduEl = document.getElementById('poetUrduVerse');
  const hindiEl = document.getElementById('poetHindiVerse');
  const engEl = document.getElementById('poetEngVerse');
  const attrEl = document.getElementById('poetAttribution');

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

// ==========================================
// 3. LAW & ACADEMIC VAULT SPLIT-FINDER LOGIC
// ==========================================
const VAULT_DATA = {
  law: {
    title: "⚖️ Law & Jurisprudence (Essential Legal References)",
    books: [
      { id: "law-1", title: "Modi Medical Jurisprudence & Toxicology", author: "Kannan & Mathiharan", price: 1850, mrp: 2195, tag: "LexisNexis • Hardcover", image: "assets/book-medical-jurisprudence.jpg" },
      { id: "law-2", title: "Lawful Awful: Life in Law & Courtrooms", author: "Justice Venkataswami", price: 450, mrp: 599, tag: "Penguin Law • Memoir", image: "assets/book-lawful-awful.jpg" },
      { id: "law-3", title: "१० फ़ैसले जिन्होंने देश बदल दिया", author: "Zia Mody (Hindi)", price: 320, mrp: 395, tag: "Landmark Judgments", image: "assets/book-10-faisle.jpg" },
      { id: "law-4", title: "Bench and Bar: Reminiscences of Courts", author: "Universal Law Publishing", price: 590, mrp: 750, tag: "Legal History & Ethics", image: "assets/book-bench-bar.jpg" }
    ]
  },
  sahitya: {
    title: "🏛️ Hindi Sahitya & Vyakaran (Academic Curricula)",
    books: [
      { id: "sahitya-1", title: "हिंदी साहित्य का इतिहास", author: "आचार्य रामचंद्र शुक्ल", price: 450, mrp: 550, tag: "Standard University Ref", image: "assets/book-hindi-sahitya-itihas.jpg" },
      { id: "sahitya-2", title: "आधुनिक हिंदी व्याकरण और रचना", author: "वासुदेव नंदन प्रसाद", price: 280, mrp: 350, tag: "Linguistics & Grammar", image: "assets/book-hindi-vyakaran.jpg" },
      { id: "sahitya-3", title: "हिंदी भाषा का इतिहास व विकास", author: "डॉ. भोलानाथ तिवारी", price: 320, mrp: 400, tag: "Philology & Dialects", image: "assets/book-hindi-bhasha.jpg" },
      { id: "sahitya-4", title: "लोक साहित्य की भूमिका", author: "डॉ. कृष्णदेव उपाध्याय", price: 390, mrp: 480, tag: "Folk Literature", image: "assets/book-lok-sahitya.jpg" }
    ]
  },
  prep: {
    title: "🎓 Civil Services & McGraw Hill (Competitive Exams)",
    books: [
      { id: "prep-1", title: "Indian Polity (7th Edition)", author: "M. Laxmikanth", price: 699, mrp: 895, tag: "McGraw Hill • UPSC GS-2", image: "assets/book-anil-naik.jpg" },
      { id: "prep-2", title: "Modern Indian History Spectrum", author: "Rajiv Ahir IPS", price: 390, mrp: 485, tag: "Historical Foundation", image: "assets/book-kabira-khada.jpg" },
      { id: "prep-3", title: "Indian Economy for Civil Services", author: "Ramesh Singh", price: 620, mrp: 795, tag: "Macroeconomic Analysis", image: "assets/book-tumhare-shahar.jpg" }
    ]
  },
  history: {
    title: "🌍 History & Dalit Vimarsh (Socio-Political Studies)",
    books: [
      { id: "hist-1", title: "जाति का विनाश (Annihilation of Caste)", author: "डॉ. बी. आर. अम्बेडकर", price: 180, mrp: 250, tag: "Constitutional Thought", image: "assets/book-a-astu-ka.jpg" },
      { id: "hist-2", title: "झूठन (Joothan: An Untouchable's Life)", author: "ओमप्रकाश वाल्मीकि", price: 240, mrp: 300, tag: "Autobiographical Classic", image: "assets/book-cheelwali-kothi.jpg" },
      { id: "hist-3", title: "कबीरा खड़ा बाज़ार में", author: "भीष्म साहनी", price: 220, mrp: 280, tag: "Social Allegory Drama", image: "assets/book-kabira-khada.jpg" }
    ]
  }
};

let currentVaultDrawer = 'law';

function selectVaultDrawer(drawerKey) {
  currentVaultDrawer = drawerKey;
  const drawer = VAULT_DATA[drawerKey];
  if (!drawer) return;

  // Update tabs style
  const buttons = document.querySelectorAll('#vaultDrawerTabs button');
  buttons.forEach(b => b.classList.remove('active'));
  if (event && event.currentTarget) {
    event.currentTarget.classList.add('active');
  }

  // Update Title
  document.getElementById('vaultDrawerActiveTitle').innerText = drawer.title;
  document.getElementById('vaultCountTag').innerText = `Showing ${drawer.books.length} cataloged editions`;

  // Render Grid
  const grid = document.getElementById('vaultCardsGrid');
  grid.innerHTML = drawer.books.map(b => `
    <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
      <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
        <img src="${b.image}" alt="${b.title}" class="w-full h-full object-cover">
      </div>
      <div class="flex-1 min-w-0 flex flex-col justify-between">
        <div>
          <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded">
            ${b.tag}
          </span>
          <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors">
            ${b.title}
          </h4>
          <p class="text-[11px] text-slate-500">${b.author}</p>
          <div class="text-[10px] text-emerald-700 font-medium mt-1">✓ In Stock at Prayagraj</div>
        </div>
        <div class="mt-2 pt-2 border-t border-slate-200 flex items-center justify-between">
          <div>
            <span class="text-base font-bold text-[#0A1128] font-serif">₹${b.price}.00</span>
            <span class="text-[10px] text-slate-400 line-through ml-1">₹${b.mrp}</span>
          </div>
          <button onclick="addToCart('${b.id}', '${b.title}', ${b.price}, '${b.image}')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold" title="Add to Cart">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  `).join('');
}

function filterVaultBooks(query) {
  const q = query.toLowerCase().trim();
  const drawer = VAULT_DATA[currentVaultDrawer];
  if (!drawer) return;

  const filtered = drawer.books.filter(b => 
    b.title.toLowerCase().includes(q) || 
    b.author.toLowerCase().includes(q) || 
    b.tag.toLowerCase().includes(q)
  );

  const grid = document.getElementById('vaultCardsGrid');
  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="col-span-2 text-center py-8 text-slate-500 text-xs">
        No books found matching "${query}" in this drawer. Try switching tabs.
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(b => `
    <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
      <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
        <img src="${b.image}" alt="${b.title}" class="w-full h-full object-cover">
      </div>
      <div class="flex-1 min-w-0 flex flex-col justify-between">
        <div>
          <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded">
            ${b.tag}
          </span>
          <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors">
            ${b.title}
          </h4>
          <p class="text-[11px] text-slate-500">${b.author}</p>
          <div class="text-[10px] text-emerald-700 font-medium mt-1">✓ In Stock at Prayagraj</div>
        </div>
        <div class="mt-2 pt-2 border-t border-slate-200 flex items-center justify-between">
          <div>
            <span class="text-base font-bold text-[#0A1128] font-serif">₹${b.price}.00</span>
            <span class="text-[10px] text-slate-400 line-through ml-1">₹${b.mrp}</span>
          </div>
          <button onclick="addToCart('${b.id}', '${b.title}', ${b.price}, '${b.image}')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold" title="Add to Cart">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  `).join('');
}

// ==========================================
// 4. SCROLL-TRIGGERED NUMBER COUNTER PHYSICS
// ==========================================
function initLiveCounters() {
  const counterElements = document.querySelectorAll('.live-counter');
  let animated = false;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animated = true;
        counterElements.forEach(el => {
          const target = parseInt(el.getAttribute('data-target') || '0', 10);
          const duration = 1500;
          const start = 0;
          const startTime = performance.now();

          function updateNumber(now) {
            const progress = Math.min((now - startTime) / duration, 1);
            const current = Math.floor(progress * target);
            el.innerText = current.toLocaleString('en-IN');
            if (progress < 1) {
              requestAnimationFrame(updateNumber);
            } else {
              el.innerText = target.toLocaleString('en-IN');
            }
          }
          requestAnimationFrame(updateNumber);
        });
      }
    });
  }, { threshold: 0.3 });

  const section = document.getElementById('literaryMarqueeSection');
  if (section) observer.observe(section);
}

// Hook into initial page ready
window.addEventListener('DOMContentLoaded', () => {
  updatePodiumStage();
  initLiveCounters();
});
</script>
"""

# Assemble all 6 sections into single replacement block
full_replacement_sections = (
  html_literary_marquee +
  html_curators_podium +
  html_mehfil_rekhta +
  html_bundle_unboxing +
  html_regional_magazine +
  html_academic_vault +
  html_trust_strip +
  html_floating_dock
)

# Read preview.html
with open('preview.html', 'r', encoding='utf-8') as f:
  preview_content = f.read()

# Exact boundary markers in preview.html
# Hero ends with </section> around line 724
hero_end_marker = '</section>'
hero_pos = preview_content.find(hero_end_marker) + len(hero_end_marker)

# Footer begins with <!-- 13. Section J: Rich Literary Footer --> or <footer
footer_marker = '<!-- 13. Section J: Rich Literary Footer -->'
footer_pos = preview_content.find(footer_marker)
if footer_pos == -1:
  footer_pos = preview_content.find('<footer')

print(f"Hero ends at index {hero_pos}, Footer starts at index {footer_pos}")

# Split preview.html into head+hero, and footer+scripts
head_and_hero = preview_content[:hero_pos]
footer_and_rest = preview_content[footer_pos:]

# Insert our styles and script before </body>
body_end_pos = footer_and_rest.rfind('</body>')
if body_end_pos != -1:
  footer_and_rest = footer_and_rest[:body_end_pos] + js_and_css_additions + footer_and_rest[body_end_pos:]

# Combine updated preview.html
new_preview_html = head_and_hero + "\n\n" + full_replacement_sections + "\n\n" + footer_and_rest

with open('preview.html', 'w', encoding='utf-8') as f:
  f.write(new_preview_html)

print("preview.html successfully updated with all 6 avant-garde architectural sections!")


