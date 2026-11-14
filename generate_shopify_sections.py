# -*- coding: utf-8 -*-
"""
Generate Shopify Liquid Sections for the 6 Avant-Garde Sections
"""

import os
import json

# ==============================================================
# 1. sections/literary-marquee.liquid
# ==============================================================
literary_marquee_liquid = """{% comment %}
  Indigo Books India - Literary Marquee & Live Counter Ticker
  Dual-layer kinetic typography ribbon and animated number counters
{% endcomment %}

<section id="literaryMarqueeSection" class="bg-[#0A1128] border-y border-amber-500/30 overflow-hidden relative z-30 shadow-2xl select-none">
  <!-- Kinetic Typography Endless Ribbon -->
  <div class="py-2.5 bg-black/40 border-b border-amber-500/20 overflow-hidden relative">
    <div class="flex items-center whitespace-nowrap animate-marquee">
      <div class="flex items-center gap-8 font-serif text-xs md:text-sm tracking-[0.18em] uppercase text-amber-300/90 font-medium px-4">
        <span>✦ {{ section.settings.ticker_text | default: "11,922+ TITLES IN STOCK • REKHTA PUBLICATIONS OFFICIAL PARTNER • PRAYAGRAJ HERITAGE BOOKSTORE • INSTANT WHATSAPP COD (+91 8881122722) • PAN-INDIA EXPRESS DELIVERY • 100% AUTHENTIC EDITIONS" }}</span>
        <span class="text-amber-500/50">•</span>
        <span>✦ 11,922+ TITLES IN STOCK</span>
        <span class="text-amber-500/50">•</span>
        <span>REKHTA PUBLICATIONS OFFICIAL PARTNER</span>
        <span class="text-amber-500/50">•</span>
        <span>PRAYAGRAJ HERITAGE BOOKSTORE</span>
        <span class="text-amber-500/50">•</span>
        <span>INSTANT WHATSAPP COD (+91 8881122722)</span>
        <span class="text-amber-500/50">•</span>
      </div>
      <div class="flex items-center gap-8 font-serif text-xs md:text-sm tracking-[0.18em] uppercase text-amber-300/90 font-medium px-4" aria-hidden="true">
        <span>✦ {{ section.settings.ticker_text | default: "11,922+ TITLES IN STOCK • REKHTA PUBLICATIONS OFFICIAL PARTNER • PRAYAGRAJ HERITAGE BOOKSTORE • INSTANT WHATSAPP COD (+91 8881122722) • PAN-INDIA EXPRESS DELIVERY • 100% AUTHENTIC EDITIONS" }}</span>
        <span class="text-amber-500/50">•</span>
        <span>✦ 11,922+ TITLES IN STOCK</span>
        <span class="text-amber-500/50">•</span>
        <span>REKHTA PUBLICATIONS OFFICIAL PARTNER</span>
        <span class="text-amber-500/50">•</span>
        <span>PRAYAGRAJ HERITAGE BOOKSTORE</span>
        <span class="text-amber-500/50">•</span>
        <span>INSTANT WHATSAPP COD (+91 8881122722)</span>
        <span class="text-amber-500/50">•</span>
      </div>
    </div>
  </div>

  <!-- Live Counter Metric Ribbon -->
  <div class="max-w-7xl mx-auto px-6 lg:px-8 py-4 lg:py-5">
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 text-center divide-y lg:divide-y-0 lg:divide-x divide-amber-500/20">
      
      <div class="p-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-[#D99B26] font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="11922">{{ section.settings.m1_val | default: "11,922" }}</span><span class="text-amber-400">+</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">{{ section.settings.m1_lbl | default: "Books Available (Pan-India Express Delivery)" }}</div>
      </div>

      <div class="p-2 pt-4 lg:pt-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-amber-300 font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="24">{{ section.settings.m2_val | default: "24" }}</span><span class="text-amber-400">+</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">{{ section.settings.m2_lbl | default: "Featured Curations (Handpicked Heritage Gems)" }}</div>
      </div>

      <div class="p-2 pt-4 lg:pt-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-[#D99B26] font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="30">{{ section.settings.m3_val | default: "30" }}</span><span class="text-amber-400">%</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">{{ section.settings.m3_lbl | default: "Max Savings on Direct Publisher Bundles" }}</div>
      </div>

      <div class="p-2 pt-4 lg:pt-2 flex flex-col items-center justify-center">
        <div class="text-2xl lg:text-3xl font-black text-emerald-400 font-serif tracking-tight flex items-baseline">
          <span class="live-counter" data-target="100">{{ section.settings.m4_val | default: "100" }}</span><span class="text-emerald-300">%</span>
        </div>
        <div class="text-xs text-slate-300 font-medium mt-1">{{ section.settings.m4_lbl | default: "Cash on Delivery & Authenticity Guaranteed" }}</div>
      </div>

    </div>
  </div>
</section>

{% schema %}
{
  "name": "Literary Marquee Ticker",
  "settings": [
    { "type": "textarea", "id": "ticker_text", "label": "Ticker Text", "default": "11,922+ TITLES IN STOCK • REKHTA PUBLICATIONS OFFICIAL PARTNER • PRAYAGRAJ HERITAGE BOOKSTORE • INSTANT WHATSAPP COD (+91 8881122722) • PAN-INDIA EXPRESS DELIVERY • 100% AUTHENTIC EDITIONS" },
    { "type": "text", "id": "m1_val", "label": "Metric 1 Number", "default": "11,922" },
    { "type": "text", "id": "m1_lbl", "label": "Metric 1 Label", "default": "Books Available (Pan-India Express Delivery)" },
    { "type": "text", "id": "m2_val", "label": "Metric 2 Number", "default": "24" },
    { "type": "text", "id": "m2_lbl", "label": "Metric 2 Label", "default": "Featured Curations (Handpicked Heritage Gems)" },
    { "type": "text", "id": "m3_val", "label": "Metric 3 Number", "default": "30" },
    { "type": "text", "id": "m3_lbl", "label": "Metric 3 Label", "default": "Max Savings on Direct Publisher Bundles" },
    { "type": "text", "id": "m4_val", "label": "Metric 4 Number", "default": "100" },
    { "type": "text", "id": "m4_lbl", "label": "Metric 4 Label", "default": "Cash on Delivery & Authenticity Guaranteed" }
  ],
  "presets": [
    { "name": "Literary Marquee Ticker" }
  ]
}
{% endschema %}
"""

# ==============================================================
# 2. sections/curators-podium.liquid
# ==============================================================
curators_podium_liquid = """{% comment %}
  Indigo Books India - 3D Curator's Podium for Bestsellers
  Pure Vanilla CSS -140deg Cover Flip + 5-Book Turntable Engine
  2-Layer 3D DOM Structure with Zero overflow-hidden on parents
{% endcomment %}

<style id=\"podiumPureCss3d\">
  /* ==========================================================================
     INDIGO BOOKS - CURATOR'S PODIUM PURE VANILLA CSS 3D HINGE FLIP
     Zero React / Zero Framer Motion / Zero Tailwind JIT Dependencies
     CRITICAL: ABSOLUTELY NO overflow-hidden ON PARENTS (Preserves 3D Context)
     ========================================================================== */

  #bestsellers-podium,
  #curatorsPodiumSection,
  .podium-section-wrap {
    position: relative !important;
    overflow: visible !important; /* CRITICAL: Must be visible to allow 3D cover swing */
  }

  .podium-stage-container {
    perspective: 1600px !important;
    -webkit-perspective: 1600px !important;
    min-height: 440px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: visible !important; /* CRITICAL */
    user-select: none !important;
  }

  .podium-stage-track {
    position: relative !important;
    width: 100% !important;
    max-width: 540px !important;
    height: 340px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    perspective: 1600px !important;
    -webkit-perspective: 1600px !important;
    overflow: visible !important; /* CRITICAL */
  }

  /* 2-LAYER 3D BOOK WRAPPER (NO overflow-hidden on the parent!) */
  #podium-3d-book,
  .podium-book-wrapper {
    position: relative !important;
    width: 200px !important;
    height: 300px !important;
    perspective: 1600px !important;
    -webkit-perspective: 1600px !important;
    transform-style: preserve-3d !important;
    -webkit-transform-style: preserve-3d !important;
    cursor: pointer !important;
    z-index: 30 !important;
    overflow: visible !important; /* CRITICAL: NO overflow-hidden */
    transition: transform 0.6s cubic-bezier(0.22, 1, 0.36, 1) !important;
  }

  /* BACK LAYER: The Inside Cream Page (Revealed when cover opens) */
  .podium-inside-page {
    position: absolute !important;
    inset: 0 !important;
    background: #FAF5EB !important;
    background: linear-gradient(to right, #f3ead8 0%, #FAF5EB 15%, #ffffff 85%, #FAF5EB 100%) !important;
    border: 1px solid #d4c5a9 !important;
    border-radius: 2px 6px 6px 2px !important;
    padding: 18px 16px !important;
    box-shadow: inset 4px 0 10px rgba(0,0,0,0.12), 0 15px 30px rgba(0,0,0,0.3) !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    z-index: 10 !important;
    pointer-events: auto !important;
    transform: translateZ(-1px) !important;
    -webkit-transform: translateZ(-1px) !important;
  }

  /* FRONT LAYER: The Hinged 3D Front Cover (Swings open -140deg on hover/click) */
  #podium-front-cover,
  .podium-front-cover {
    position: absolute !important;
    inset: 0 !important;
    transform-origin: left center !important;
    transform: rotateY(0deg) !important;
    -webkit-transform: rotateY(0deg) !important;
    transform-style: preserve-3d !important;
    -webkit-transform-style: preserve-3d !important;
    transition: transform 0.85s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.85s ease !important;
    z-index: 25 !important;
    cursor: pointer !important;
    border-radius: 2px 6px 6px 2px !important;
    box-shadow: 0 20px 35px rgba(0, 0, 0, 0.5), inset 2px 0 5px rgba(255, 255, 255, 0.2) !important;
    border-right: 3px solid rgba(254, 243, 199, 0.8) !important;
    background: #1e293b !important;
    overflow: visible !important;
    backface-visibility: hidden !important;
    -webkit-backface-visibility: hidden !important;
  }

  #podium-cover-img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    border-radius: 2px 6px 6px 2px !important;
    display: block !important;
  }

  /* Spine Shadow */
  .podium-spine-shadow {
    position: absolute !important;
    top: 0 !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 16px !important;
    background: linear-gradient(to right, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0.2) 60%, transparent 100%) !important;
    pointer-events: none !important;
    z-index: 5 !important;
    border-top-left-radius: 2px !important;
    border-bottom-left-radius: 2px !important;
  }

  /* TRIGGER PURE CSS -140 DEGREE 3D FLIP ON HOVER OR CLICK (.is-open) */
  #podium-3d-book:hover #podium-front-cover,
  #podium-3d-book:hover .podium-front-cover,
  #podium-3d-book.is-open #podium-front-cover,
  #podium-3d-book.is-open .podium-front-cover,
  .podium-book-wrapper:hover .podium-front-cover,
  .podium-book-wrapper.is-open .podium-front-cover {
    transform: rotateY(-140deg) !important;
    -webkit-transform: rotateY(-140deg) !important;
    box-shadow: -15px 20px 35px rgba(0, 0, 0, 0.45) !important;
  }

  /* 4 FLANKING TURNTABLE BOOKS */
  .flanking-book-card {
    position: absolute !important;
    width: 140px !important;
    height: 210px !important;
    cursor: pointer !important;
    transition: all 0.6s cubic-bezier(0.22, 1, 0.36, 1) !important;
    border-radius: 2px 6px 6px 2px !important;
    overflow: hidden !important;
    box-shadow: 0 15px 25px rgba(0,0,0,0.4) !important;
  }

  .flanking-book-card img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
    transition: transform 0.4s ease !important;
  }

  .flanking-book-card::after {
    content: '' !important;
    position: absolute !important;
    inset: 0 !important;
    background: rgba(10, 17, 40, 0.45) !important;
    transition: background 0.3s ease !important;
    z-index: 2 !important;
  }

  .flanking-book-card:hover::after {
    background: rgba(10, 17, 40, 0.15) !important;
  }

  .flanking-book-card:hover img {
    transform: scale(1.05) !important;
  }

  /* Turntable Slot Coordinates */
  .slot-far-left {
    transform: translateX(-195px) scale(0.72) rotateY(28deg) !important;
    -webkit-transform: translateX(-195px) scale(0.72) rotateY(28deg) !important;
    z-index: 5 !important;
    opacity: 0.55 !important;
  }

  .slot-near-left {
    transform: translateX(-105px) scale(0.85) rotateY(16deg) !important;
    -webkit-transform: translateX(-105px) scale(0.85) rotateY(16deg) !important;
    z-index: 15 !important;
    opacity: 0.85 !important;
  }

  .slot-near-right {
    transform: translateX(105px) scale(0.85) rotateY(-16deg) !important;
    -webkit-transform: translateX(105px) scale(0.85) rotateY(-16deg) !important;
    z-index: 15 !important;
    opacity: 0.85 !important;
  }

  .slot-far-right {
    transform: translateX(195px) scale(0.72) rotateY(-28deg) !important;
    -webkit-transform: translateX(195px) scale(0.72) rotateY(-28deg) !important;
    z-index: 5 !important;
    opacity: 0.55 !important;
  }
</style>

<section id=\"bestsellers-podium\" class=\"podium-section-wrap py-16 lg:py-20 bg-[#FAF8F5] relative border-b border-amber-900/10\">
  <div id=\"curatorsPodiumSection\"></div>
  <div class=\"absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-amber-400/10 rounded-full blur-3xl pointer-events-none z-0\"></div>

  <div class=\"max-w-7xl mx-auto px-6 lg:px-8 relative z-10\" style=\"overflow: visible;\">
    
    <!-- Section Header -->
    <div class=\"text-center max-w-3xl mx-auto mb-10\">
      <div class=\"inline-flex items-center gap-2 bg-amber-100 text-[#D99B26] border border-amber-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm font-sans\">
        <svg class=\"w-3.5 h-3.5 fill-current text-[#D99B26]\" viewBox=\"0 0 24 24\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg>
        <span>{{ section.settings.badge | default: 'CURATOR’S CHOICE & NATIONAL BESTSELLERS' }}</span>
      </div>
      <h2 class=\"font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3\">
        {{ section.settings.title | default: 'The Podium: India’s Top 5 Trending Reads' }}
      </h2>
      <p class=\"text-sm lg:text-base text-slate-600 mt-2 font-sans\">
        {{ section.settings.subtitle | default: 'Handpicked literature capturing minds across universities, literary circles, and book lovers nationwide.' }}
      </p>
    </div>

    <!-- Main 12-Column Grid -->
    <div class=\"grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center\" style=\"overflow: visible;\">
      
      <!-- LEFT 7 COLS: 3D Turntable Stage (5 Books with Pure CSS Hinge Flip) -->
      <div class=\"lg:col-span-7 flex flex-col items-center\" style=\"overflow: visible;\">
        
        <div class=\"w-full relative py-6 px-2 flex items-center justify-center min-h-[460px] podium-stage-container\" id=\"podiumTurntableStage\" style=\"overflow: visible;\">
          <!-- Ambient Platform Glow -->
          <div class=\"absolute bottom-4 inset-x-8 h-20 bg-gradient-to-t from-amber-400/30 via-amber-200/20 to-transparent rounded-full blur-xl pointer-events-none z-0\"></div>
          <div class=\"absolute bottom-6 w-3/4 h-6 border-b-2 border-amber-500/30 rounded-[100%] shadow-[0_15px_30px_rgba(217,155,38,0.25)] pointer-events-none z-0\"></div>

          <!-- Turntable Track holding all 5 Books -->
          <div class=\"podium-stage-track\" id=\"podiumBooksStageWrapper\" style=\"overflow: visible;\">
            
            <!-- 1. Far Left Book (Slot 0) -->
            <div id=\"flankBook0\" class=\"flanking-book-card slot-far-left\" onclick=\"selectPodiumBookByFlank(0)\" title=\"Click to view Diary of a Wimpy Kid\">
              <img id=\"flankImg0\" src=\"{{ 'hero-book-wimpy-kid.jpg' | asset_url }}\" alt=\"Diary of a Wimpy Kid\">
            </div>

            <!-- 2. Near Left Book (Slot 1) -->
            <div id=\"flankBook1\" class=\"flanking-book-card slot-near-left\" onclick=\"selectPodiumBookByFlank(1)\" title=\"Click to view Ujli Raaten\">
              <img id=\"flankImg1\" src=\"{{ 'hero-book-ujli-raaten.jpg' | asset_url }}\" alt=\"Ujli Raaten\">
            </div>

            <!-- 3. CENTER ACTIVE 3D BOOK (EXACT 2-LAYER STRUCTURE REQUESTED BY USER - NO overflow-hidden!) -->
            <div id=\"podium-3d-book\" class=\"podium-book-wrapper\" onclick=\"this.classList.toggle('is-open')\" title=\"Click or hover to open cover\">
              
              <!-- BACK LAYER: The Inside Cream Page (Revealed when cover opens) -->
              <div class=\"podium-inside-page\">
                <div style=\"font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: #b45309; font-weight: 700;\">
                  अध्याय १ • First Page Preview
                </div>
                <div id=\"podium-page-title\" style=\"font-family: Georgia, serif; font-size: 14px; font-weight: 700; color: #0f172a; margin-top: 6px;\">
                  Kasaibada
                </div>
                <p id=\"podium-page-excerpt\" style=\"font-size: 11px; line-height: 1.5; color: #334155; margin-top: 8px;\">
                  \"शहर की तंग गलियों में जहाँ सत्ता और संघर्ष की दास्तान हर दीवार पर लिखी थी, वहाँ इंसानियत की एक नई कहानी जन्म ले रही थी...\"
                </p>
                <div style=\"font-size: 10px; font-weight: 700; color: #d97706; margin-top: auto; border-top: 1px solid #e2e8f0; padding-top: 6px;\">
                  ✦ Click or Hover to Flip Cover
                </div>
              </div>

              <!-- FRONT LAYER: The Hinged 3D Front Cover (Swings open -140deg on hover/click) -->
              <div id=\"podium-front-cover\" class=\"podium-front-cover\">
                <img id=\"podium-cover-img\" src=\"{{ 'hero-book-kasaibada.jpg' | asset_url }}\" alt=\"Book Cover\" style=\"width: 100%; height: 100%; object-fit: cover; border-radius: 2px 6px 6px 2px;\" onerror=\"this.src='https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&w=600&q=80'\" />
                <div class=\"podium-spine-shadow\"></div>
              </div>
            </div>

            <!-- 4. Near Right Book (Slot 3) -->
            <div id=\"flankBook3\" class=\"flanking-book-card slot-near-right\" onclick=\"selectPodiumBookByFlank(3)\" title=\"Click to view The Masnavi: Rumi\">
              <img id=\"flankImg3\" src=\"{{ 'hero-book-rumi.png' | asset_url }}\" alt=\"The Masnavi: Rumi\">
            </div>

            <!-- 5. Far Right Book (Slot 4) -->
            <div id=\"flankBook4\" class=\"flanking-book-card slot-far-right\" onclick=\"selectPodiumBookByFlank(4)\" title=\"Click to view Best of Murakami\">
              <img id=\"flankImg4\" src=\"{{ 'hero-book-murakami.jpg' | asset_url }}\" alt=\"Best of Murakami\">
            </div>

          </div>

          <!-- Bottom Toggle Prompt Button -->
          <div class=\"absolute bottom-2 inset-x-0 flex items-center justify-center gap-2 z-20\">
            <button type=\"button\" onclick=\"document.getElementById('podium-3d-book').classList.toggle('is-open')\" class=\"flex items-center gap-1.5 text-xs text-amber-900 font-bold bg-amber-100 hover:bg-amber-200 border border-amber-300 rounded-full px-4 py-1.5 transition-all shadow-sm font-sans cursor-pointer active:scale-95\">
              <svg class=\"w-3.5 h-3.5 text-amber-700 animate-spin\" style=\"animation-duration: 4s;\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M4 19.5A2.5 2.5 0 0 1 6.5 17H20\"/><path d=\"M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z\"/></svg>
              <span id=\"flipCoverBtnText\">Hover or Click Book to Flip Cover (-140°)</span>
            </button>
          </div>
        </div>

        <!-- Controls: Prev Button, 5 Indicator Dots, Next Button -->
        <div class=\"flex items-center gap-4 mt-3 z-20\">
          <button type=\"button\" onclick=\"prevPodiumBook()\" class=\"p-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-amber-50 hover:border-amber-400 shadow-sm transition-all cursor-pointer active:scale-95\" title=\"Previous Book\">
            <svg class=\"w-4 h-4\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><polyline points=\"15 18 9 12 15 6\"/></svg>
          </button>
          <div class=\"flex items-center gap-2\" id=\"podiumIndicators\">
            <button type=\"button\" class=\"podium-dot w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300 cursor-pointer\" onclick=\"selectPodiumBook(0)\" aria-label=\"Book 1\"></button>
            <button type=\"button\" class=\"podium-dot w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300 cursor-pointer\" onclick=\"selectPodiumBook(1)\" aria-label=\"Book 2\"></button>
            <button type=\"button\" class=\"podium-dot active w-7 h-2.5 rounded-full bg-[#D99B26] transition-all duration-300 cursor-pointer\" onclick=\"selectPodiumBook(2)\" aria-label=\"Book 3\"></button>
            <button type=\"button\" class=\"podium-dot w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300 cursor-pointer\" onclick=\"selectPodiumBook(3)\" aria-label=\"Book 4\"></button>
            <button type=\"button\" class=\"podium-dot w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300 cursor-pointer\" onclick=\"selectPodiumBook(4)\" aria-label=\"Book 5\"></button>
          </div>
          <button type=\"button\" onclick=\"nextPodiumBook()\" class=\"p-2 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-amber-50 hover:border-amber-400 shadow-sm transition-all cursor-pointer active:scale-95\" title=\"Next Book\">
            <svg class=\"w-4 h-4\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><polyline points=\"9 18 15 12 9 6\"/></svg>
          </button>
        </div>

      </div>

      <!-- RIGHT 5 COLS: Spotlight Details Panel (100% Synchronous State) -->
      <div class=\"lg:col-span-5 bg-white border border-amber-900/10 rounded-2xl p-6 lg:p-8 shadow-xl relative overflow-hidden flex flex-col justify-between\" id=\"podiumSpotlightPanel\">
        <div>
          <!-- Category & Stock Status -->
          <div class=\"flex items-center justify-between mb-3 font-sans\">
            <span id=\"spotlightRank\" class=\"text-xs font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-2.5 py-1 rounded\">
              #1 IN CONTEMPORARY HINDI FICTION
            </span>
            <span id=\"spotlightStock\" class=\"flex items-center gap-1.5 text-xs text-emerald-700 font-semibold\">
              <span class=\"w-2 h-2 rounded-full bg-emerald-500 animate-ping\"></span>
              <span>22 copies in Prayagraj</span>
            </span>
          </div>

          <!-- Title & Author -->
          <h3 id=\"spotlightTitle\" class=\"font-serif text-2xl lg:text-3xl font-bold text-[#0A1128] leading-tight\">
            कसाईबाड़ा (Kasaibada)
          </h3>

          <div class=\"flex items-center gap-2 mt-1.5 text-slate-600 text-sm font-sans\">
            <span>By</span>
            <span id=\"spotlightAuthor\" class=\"font-bold text-slate-900\">Manoj Rajan Tripathi</span>
            <span class=\"text-amber-500\">★</span>
            <span id=\"spotlightRating\" class=\"font-semibold text-slate-700 text-xs\">4.9 (540+ reviews)</span>
          </div>

          <!-- Curator Quote -->
          <div class=\"mt-4 p-4 bg-[#FAF8F5] border-l-4 border-[#D99B26] rounded-r-lg\">
            <div class=\"text-[11px] uppercase font-bold text-amber-900 tracking-wider mb-1 font-sans\">
              Why India is Reading This:
            </div>
            <p id=\"spotlightQuote\" class=\"text-xs lg:text-sm text-slate-700 italic font-serif leading-relaxed\">
              \"A gripping social allegory on rural power structures, journalistic integrity, and human resilience in northern India.\"
            </p>
          </div>

          <!-- Specs Summary -->
          <div class=\"grid grid-cols-2 gap-2 mt-4 text-[11px] text-slate-600 font-sans\">
            <div class=\"bg-slate-50 p-2.5 rounded-lg border border-slate-200\">
              <span class=\"text-slate-400 block text-[9px] uppercase font-bold tracking-wider\">Format & Binding</span>
              <span id=\"spotlightPages\" class=\"font-bold text-slate-800\">192 Pages • Paperback</span>
            </div>
            <div class=\"bg-slate-50 p-2.5 rounded-lg border border-slate-200\">
              <span class=\"text-slate-400 block text-[9px] uppercase font-bold tracking-wider\">Publisher Edition</span>
              <span id=\"spotlightPublisher\" class=\"font-bold text-slate-800\">Vani Prakashan</span>
            </div>
          </div>

          <!-- Price Row -->
          <div class=\"mt-6 flex items-baseline gap-3\">
            <span id=\"spotlightPrice\" class=\"text-3xl font-bold text-[#0A1128] font-serif price-text\">₹299.00</span>
            <span id=\"spotlightMRP\" class=\"text-sm text-slate-400 line-through font-serif\">₹395.00</span>
            <span id=\"spotlightSave\" class=\"text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded font-sans\">
              24% OFF
            </span>
          </div>
        </div>

        <!-- Action Row -->
        <div class=\"mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row gap-3 font-sans\">
          <button id=\"spotlightAddCartBtn\" type=\"button\" onclick=\"addCurrentPodiumToCart()\" class=\"flex-1 bg-[#D99B26] hover:bg-[#B88019] text-white py-3 px-4 rounded-xl font-bold text-sm transition-all shadow-md flex items-center justify-center gap-2 group cursor-pointer active:scale-95\">
            <svg class=\"w-4 h-4 fill-current group-hover:scale-110 transition-transform\" viewBox=\"0 0 24 24\"><path d=\"M19 6h-2c0-2.76-2.24-5-5-5S7 3.24 7 6H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-7-3c1.66 0 3 1.34 3 3H9c0-1.66 1.34-3 3-3zm7 17H5V8h14v12z\"/></svg>
            <span>Add to Cart</span>
          </button>
          
          <a id=\"spotlightWhatsAppBtn\" href=\"https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Kasaibada%20at%20%E2%82%B9299.\" target=\"_blank\" class=\"flex-1 bg-[#10B981] hover:bg-[#059669] text-white py-3 px-4 rounded-xl font-bold text-sm transition-all shadow-md flex items-center justify-center gap-2 active:scale-95 text-center\">
            <svg class=\"w-4 h-4 fill-current\" viewBox=\"0 0 24 24\"><path d=\"M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z\"/></svg>
            <span>WhatsApp COD</span>
          </a>
        </div>

      </div>

    </div>

  </div>
</section>


<script>
// =========================================================================
// CURATOR'S PODIUM PURE VANILLA JS CONTROLLER
// 100% Synchronous state management between #podium-3d-book and spotlight panel
// =========================================================================
const PODIUM_DATA = [
  {
    id: 'podium-0',
    title: 'Diary of a Wimpy Kid: Fight or Flight',
    author: 'Jeff Kinney',
    rank: '#1 IN CHILDREN FICTION',
    rating: '4.8 (890+ reviews)',
    quote: '\"First of all, let me get something straight: this is a JOURNAL, not a diary. The hilarious misadventures of Greg Heffley continue.\"',
    excerpt: '\"First of all, let me get something straight: this is a JOURNAL, not a diary. I know what it says on the cover, but when Mom went out to buy this thing I specifically told her to get one that didn\'t say \'diary\' on it.\"',
    pages: '224 Pages • Hardcover',
    publisher: 'Puffin Books',
    price: '₹399.00',
    mrp: '₹499.00',
    save: '20% OFF',
    discountBadge: '20% OFF',
    stock: '18 copies in Prayagraj',
    cover: 'hero-book-wimpy-kid.jpg',
    chapter: 'Chapter 1'
  },
  {
    id: 'podium-1',
    title: 'उजली रातें (Ujli Raaten)',
    author: 'Fyodor Dostoevsky',
    rank: '#2 IN CLASSIC TRANSLATIONS',
    rating: '4.9 (420+ reviews)',
    quote: '\"सेंट पीटर्सबर्ग की जादुई रातों में एक भावुक स्वप्नद्रष्टा और एकाकी स्त्री की आत्मा को छू लेने वाली अमर प्रेम कथा।\"',
    excerpt: '\"वह एक अद्भुत रात थी, ऐसी रात जो केवल जवानी के दिनों में ही नसीब हो सकती है। आकाश तारों से भरा था, इतना चमकता हुआ कि उसे देखकर मन अपने-आप पूछ बैठता था—क्या ऐसे आसमान के नीचे भी उदास लोग रह सकते हैं?\"',
    pages: '160 Pages • Paperback',
    publisher: 'Penguin Classics',
    price: '₹220.00',
    mrp: '₹299.00',
    save: '26% OFF',
    discountBadge: '26% OFF',
    stock: '35 copies in Prayagraj',
    cover: 'hero-book-ujli-raaten.jpg',
    chapter: 'पहला प्रहर / Night One'
  },
  {
    id: 'podium-2',
    title: 'कसाईबाड़ा (Kasaibada)',
    author: 'Manoj Rajan Tripathi',
    rank: '#1 IN CONTEMPORARY HINDI FICTION',
    rating: '4.9 (540+ reviews)',
    quote: '\"A gripping social allegory on rural power structures, journalistic integrity, and human resilience in northern India.\"',
    excerpt: '\"शहर की तंग गलियों में जहाँ सत्ता और संघर्ष की दास्तान हर दीवार पर लिखी थी, वहाँ इंसानियत की एक नई कहानी जन्म ले रही थी। सत्ता, व्यवस्था और आत्मसम्मान की जद्दोजहद...\"',
    pages: '192 Pages • Paperback',
    publisher: 'Vani Prakashan',
    price: '₹299.00',
    mrp: '₹395.00',
    save: '24% OFF',
    discountBadge: '24% OFF',
    stock: '22 copies in Prayagraj',
    cover: 'hero-book-kasaibada.jpg',
    chapter: 'अध्याय १ • First Page Preview'
  },
  {
    id: 'podium-3',
    title: 'The Masnavi: Rumi',
    author: 'Maryam Mafi',
    rank: '#1 IN SPIRITUAL CLASSICS',
    rating: '5.0 (610+ reviews)',
    quote: '\"The timeless spiritual poetry and divine allegories of Jalal al-Din Rumi beautifully translated for modern seekers.\"',
    excerpt: '\"Listen to the reed as it tells its tale, complaining of separation: \'Ever since I was parted from the reed-bed, my lament has caused men and women to weep. Anyone who is left far from his origin longs for the day he is reunited.\'\"',
    pages: '304 Pages • Hardcover',
    publisher: 'Rider Books',
    price: '₹399.00',
    mrp: '₹499.00',
    save: '20% OFF',
    discountBadge: '20% OFF',
    stock: '14 copies in Prayagraj',
    cover: 'hero-book-rumi.png',
    chapter: 'Book 1 • Prologue'
  },
  {
    id: 'podium-4',
    title: 'The Best of Haruki Murakami',
    author: 'Haruki Murakami',
    rank: '#1 IN GLOBAL CONTEMPORARY',
    rating: '4.9 (780+ reviews)',
    quote: '\"An intoxicating exploration of surrealism, urban loneliness, jazz rhythms, and metaphysical mysteries.\"',
    excerpt: '\"I was thirty-seven then, strapped in my seat as the huge 747 plunged through dense cloud on its way into Hamburg airport. Cold November rain drenched the airfield, turning it into a gloomy Flemish painting...\"',
    pages: '980 Pages • 3-Book Set',
    publisher: 'Vintage Classics',
    price: '₹1,299.00',
    mrp: '₹1,799.00',
    save: '28% OFF',
    discountBadge: '28% OFF',
    stock: '12 sets in Prayagraj',
    cover: 'hero-book-murakami.jpg',
    chapter: 'Norwegian Wood • Ch. 1'
  }
];

let currentPodiumIndex = 2; // Default to Center Book (Kasaibada)

function getAssetUrl(filename) {
  if (typeof window.ShopifyAssetBaseUrl !== 'undefined') {
    return window.ShopifyAssetBaseUrl + filename;
  }
  return 'assets/' + filename;
}

function selectPodiumBook(index) {
  if (index < 0 || index >= PODIUM_DATA.length) return;
  currentPodiumIndex = index;
  const book = PODIUM_DATA[index];

  // 1. Update 3D Book Cover & Inside Page
  const elCoverImg = document.getElementById('podium-cover-img');
  const elPageTitle = document.getElementById('podium-page-title');
  const elPageExcerpt = document.getElementById('podium-page-excerpt');
  const el3dBook = document.getElementById('podium-3d-book');

  if (elCoverImg) {
    elCoverImg.src = getAssetUrl(book.cover);
    elCoverImg.alt = book.title;
  }
  if (elPageTitle) elPageTitle.textContent = book.title;
  if (elPageExcerpt) elPageExcerpt.textContent = book.excerpt;

  // Reset cover open state when changing books
  if (el3dBook) el3dBook.classList.remove('is-open');

  // 2. Update Flanking Books Around Active Index
  const slotIndices = [
    (index + 3) % 5, // Far left
    (index + 4) % 5, // Near left
    (index + 1) % 5, // Near right
    (index + 2) % 5  // Far right
  ];

  const elFlank0 = document.getElementById('flankImg0');
  const elFlank1 = document.getElementById('flankImg1');
  const elFlank3 = document.getElementById('flankImg3');
  const elFlank4 = document.getElementById('flankImg4');

  if (elFlank0) elFlank0.src = getAssetUrl(PODIUM_DATA[slotIndices[0]].cover);
  if (elFlank1) elFlank1.src = getAssetUrl(PODIUM_DATA[slotIndices[1]].cover);
  if (elFlank3) elFlank3.src = getAssetUrl(PODIUM_DATA[slotIndices[2]].cover);
  if (elFlank4) elFlank4.src = getAssetUrl(PODIUM_DATA[slotIndices[3]].cover);

  // 3. Update Indicator Dots
  const dots = document.querySelectorAll('.podium-dot');
  dots.forEach((dot, i) => {
    if (i === index) {
      dot.className = 'podium-dot active w-7 h-2.5 rounded-full bg-[#D99B26] transition-all duration-300 cursor-pointer';
    } else {
      dot.className = 'podium-dot w-2.5 h-2.5 rounded-full bg-slate-300 transition-all duration-300 cursor-pointer';
    }
  });

  // 4. Update Right Spotlight Panel
  const elRank = document.getElementById('spotlightRank');
  const elStock = document.getElementById('spotlightStock');
  const elTitle = document.getElementById('spotlightTitle');
  const elAuthor = document.getElementById('spotlightAuthor');
  const elRating = document.getElementById('spotlightRating');
  const elQuote = document.getElementById('spotlightQuote');
  const elPages = document.getElementById('spotlightPages');
  const elPub = document.getElementById('spotlightPublisher');
  const elPrice = document.getElementById('spotlightPrice');
  const elMRP = document.getElementById('spotlightMRP');
  const elSave = document.getElementById('spotlightSave');
  const elWABtn = document.getElementById('spotlightWhatsAppBtn');

  if (elRank) elRank.textContent = book.rank;
  if (elStock) elStock.innerHTML = '<span class=\"w-2 h-2 rounded-full bg-emerald-500 animate-ping\"></span><span>' + book.stock + '</span>';
  if (elTitle) elTitle.textContent = book.title;
  if (elAuthor) elAuthor.textContent = book.author;
  if (elRating) elRating.textContent = book.rating;
  if (elQuote) elQuote.textContent = book.quote;
  if (elPages) elPages.textContent = book.pages;
  if (elPub) elPub.textContent = book.publisher;
  if (elPrice) elPrice.textContent = book.price;
  if (elMRP) elMRP.textContent = book.mrp;
  if (elSave) elSave.textContent = book.save;

  if (elWABtn) {
    const rawPrice = book.price.replace(/[^0-9.]/g, '');
    const cleanNum = '918881122722';
    const waMsg = 'Hello Indigo Books Prayagraj! 📚\nI would like to order: *' + book.title + '*\nAuthor: ' + book.author + '\nPrice: ' + book.price + '\nPlease confirm availability and share COD delivery details!';
    elWABtn.href = 'https://wa.me/' + cleanNum + '?text=' + encodeURIComponent(waMsg);
  }
}

function selectPodiumBookByFlank(slotPosition) {
  if (slotPosition === 0) selectPodiumBook((currentPodiumIndex + 3) % 5);
  else if (slotPosition === 1) selectPodiumBook((currentPodiumIndex + 4) % 5);
  else if (slotPosition === 3) selectPodiumBook((currentPodiumIndex + 1) % 5);
  else if (slotPosition === 4) selectPodiumBook((currentPodiumIndex + 2) % 5);
}

function prevPodiumBook() {
  const nextIdx = (currentPodiumIndex - 1 + PODIUM_DATA.length) % PODIUM_DATA.length;
  selectPodiumBook(nextIdx);
}

function nextPodiumBook() {
  const nextIdx = (currentPodiumIndex + 1) % PODIUM_DATA.length;
  selectPodiumBook(nextIdx);
}

function addCurrentPodiumToCart() {
  const book = PODIUM_DATA[currentPodiumIndex];
  if (typeof addToCart === 'function') {
    addToCart(book.id, 1);
  } else {
    const drawer = document.getElementById('CartDrawer');
    const overlay = document.getElementById('CartDrawerOverlay');
    if (drawer && overlay) {
      drawer.classList.add('active');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }
}

// Auto-run on load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => selectPodiumBook(2));
} else {
  selectPodiumBook(2);
}
window.addEventListener('load', () => selectPodiumBook(2));
document.addEventListener('shopify:section:load', () => selectPodiumBook(2));
document.addEventListener('shopify:section:select', () => selectPodiumBook(2));
</script>

{% schema %}
{
  \"name\": \"3D Curator's Podium\",
  \"settings\": [
    { \"type\": \"text\", \"id\": \"badge\", \"label\": \"Badge Text\", \"default\": \"CURATOR’S CHOICE & NATIONAL BESTSELLERS\" },
    { \"type\": \"text\", \"id\": \"title\", \"label\": \"Heading\", \"default\": \"The Podium: India’s Top 5 Trending Reads\" },
    { \"type\": \"textarea\", \"id\": \"subtitle\", \"label\": \"Subheading\", \"default\": \"Handpicked literature capturing minds across universities, literary circles, and book lovers nationwide.\" }
  ],
  \"presets\": [
    { \"name\": \"3D Curator's Podium\" }
  ]
}
{% endschema %}
"""

# ==============================================================
# 3. sections/mehfil-rekhta.liquid
# ==============================================================
mehfil_rekhta_liquid = """{% comment %}
  Indigo Books India - Mehfil-e-Rekhta Immersive Dark Poetry Lounge
  Calligraphy watermark, golden sparks, interactive 4-poet quote switcher, elevated 3D cards
{% endcomment %}

<section id="mehfilRekhtaSection" class="bg-gradient-to-b from-[#0F172A] via-[#1E1424] to-[#0A1128] text-amber-50 py-24 relative overflow-hidden">
  
  <div class="absolute inset-0 pointer-events-none opacity-40">
    <div class="particle-spark absolute top-10 left-[15%] w-1.5 h-1.5 bg-amber-400 rounded-full blur-[1px] animate-pulse"></div>
    <div class="particle-spark absolute top-32 right-[20%] w-2 h-2 bg-amber-300 rounded-full blur-[1px] animate-pulse" style="animation-delay: 1.2s"></div>
    <div class="particle-spark absolute bottom-24 left-[25%] w-1.5 h-1.5 bg-amber-400 rounded-full blur-[1px] animate-pulse" style="animation-delay: 2.1s"></div>
    <div class="particle-spark absolute bottom-40 right-[12%] w-2 h-2 bg-amber-200 rounded-full blur-[1px] animate-pulse" style="animation-delay: 0.7s"></div>
  </div>

  <div class="absolute inset-0 flex items-center justify-center opacity-[0.04] select-none pointer-events-none">
    <span class="font-serif text-8xl md:text-9xl lg:text-[13rem] tracking-widest text-amber-200 whitespace-nowrap">
      शायरी • दास्तान • अदब
    </span>
  </div>

  <div class="max-w-7xl mx-auto px-6 lg:px-8 relative z-10">
    
    <div class="text-center max-w-3xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-900/40 text-amber-300 border border-amber-500/30 px-4 py-1 rounded-full text-xs font-bold tracking-widest uppercase shadow-lg">
        <span>महेफ़िल-ए-रेख़्ख़ता</span>
        <span>•</span>
        <span>MEHFIL-E-REKHTA</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-5xl font-bold text-amber-100 mt-3 tracking-wide">
        {{ section.settings.title | default: "Urdu Poetry, Timeless Shayari & Progressive Literary Classics" }}
      </h2>
      <p class="text-sm lg:text-base text-amber-200/80 mt-3 max-w-2xl mx-auto leading-relaxed">
        {{ section.settings.subtitle | default: "Step into an intimate literary mehfil featuring official Rekhta editions, rebellious prose, and the finest verse of the subcontinent." }}
      </p>
    </div>

    <!-- Poet Quote Switcher -->
    <div class="mt-10 mb-12">
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

      <div class="max-w-3xl mx-auto mt-6 bg-white/[0.04] backdrop-blur-md border border-amber-500/30 rounded-2xl p-6 lg:p-8 shadow-2xl relative" id="poetQuoteCard">
        <div class="text-amber-400/30 text-5xl font-serif absolute top-4 left-6 select-none">“</div>
        <div class="text-center px-4 py-2 relative z-10">
          <div id="poetUrduVerse" class="font-serif text-2xl lg:text-3xl text-amber-200 font-normal leading-relaxed tracking-wide transition-opacity duration-300">
            شاید مجھے نکال کے پچھتا رہے ہوں آپ • محفل میں اس خیال سے پھر آ گیا ہوں میں
          </div>
          <div id="poetHindiVerse" class="text-sm lg:text-base text-amber-100/90 font-serif mt-2 transition-opacity duration-300">
            "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं"
          </div>
          <div id="poetEngVerse" class="text-xs text-amber-300/70 italic mt-2 max-w-xl mx-auto transition-opacity duration-300">
            Perhaps you regret having cast me out; it is merely with this thought that I returned to the gathering.
          </div>
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

    <!-- 5 Glassmorphic Dark Velvet Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 mt-16">
      
      <!-- Card 1 -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="{{ 'book-kyon-jaun-elia.jpg' | asset_url }}" alt="Kyon" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>
        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Urdu Poetry • Rekhta</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">क्यों (Kyon)</h4>
          <p class="text-xs text-amber-200/70">Jaun Elia</p>
        </div>
        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹350.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-1', 'क्यों (Kyon) - Jaun Elia', 350, '{{ 'book-kyon-jaun-elia.jpg' | asset_url }}')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Kyon%20(%E2%82%B9350)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="{{ 'book-ranjish-hi-sahi.jpg' | asset_url }}" alt="Ranjish Hi Sahi" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>
        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Ghazal Collection</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">रंजिश ही सही</h4>
          <p class="text-xs text-amber-200/70">Ahmad Faraz</p>
        </div>
        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹399.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 5.0</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-2', 'रंजिश ही सही - Ahmad Faraz', 399, '{{ 'book-ranjish-hi-sahi.jpg' | asset_url }}')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Ranjish%20Hi%20Sahi%20(%E2%82%B9399)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="{{ 'hero-book-dozakh.jpg' | asset_url }}" alt="Dozakh Nama" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>
        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Literary Fiction</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">दोज़ख़नामा</h4>
          <p class="text-xs text-amber-200/70">Rabi Sankar Bal</p>
        </div>
        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹450.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-3', 'दोज़ख़नामा (Dozakh Nama)', 450, '{{ 'hero-book-dozakh.jpg' | asset_url }}')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Dozakh%20Nama%20(%E2%82%B9450)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="{{ 'hero-book-thanda-ghost.jpg' | asset_url }}" alt="Thanda Ghost" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>
        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Progressive Stories</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">ठंडा गोश्त</h4>
          <p class="text-xs text-amber-200/70">Saadat Hasan Manto</p>
        </div>
        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹299.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.8</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-4', 'ठंडा गोश्त - Manto', 299, '{{ 'hero-book-thanda-ghost.jpg' | asset_url }}')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Thanda%20Ghost%20(%E2%82%B9299)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">WhatsApp</a>
          </div>
        </div>
      </div>

      <!-- Card 5 -->
      <div class="bg-white/[0.05] border border-amber-500/20 backdrop-blur-md rounded-2xl p-5 hover:border-amber-400/60 transition-all duration-500 group flex flex-col justify-between pt-16 relative">
        <div class="absolute -top-12 inset-x-0 mx-auto w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.8)] border-r-2 border-amber-200/50 group-hover:-translate-y-2 group-hover:scale-105 group-hover:shadow-[0_0_30px_rgba(217,155,38,0.4)] transition-all duration-300">
          <img src="{{ 'hero-book-dhuaan.jpg' | asset_url }}" alt="Dhuaan" class="w-full h-full object-cover">
          <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/70 to-transparent"></div>
        </div>
        <div>
          <div class="text-[10px] uppercase font-bold text-amber-400/80 tracking-widest mt-2">Urdu Classics</div>
          <h4 class="font-serif text-base font-bold text-white mt-1 group-hover:text-amber-300 transition-colors">धुआँ (Dhuaan)</h4>
          <p class="text-xs text-amber-200/70">Gulzar & Masters</p>
        </div>
        <div class="mt-4 pt-3 border-t border-white/10">
          <div class="flex items-baseline justify-between">
            <span class="font-serif text-lg font-bold text-amber-300">₹350.00</span>
            <span class="text-[11px] text-amber-400 flex items-center">★ 4.9</span>
          </div>
          <div class="grid grid-cols-2 gap-2 mt-3">
            <button onclick="addToCart('mehfil-5', 'धुआँ (Dhuaan) - Gulzar', 350, '{{ 'hero-book-dhuaan.jpg' | asset_url }}')" class="bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold text-xs py-2 rounded-lg transition-colors flex items-center justify-center gap-1">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Dhuaan%20(%E2%82%B9350)." target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs py-2 rounded-lg transition-colors text-center">WhatsApp</a>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>

{% schema %}
{
  "name": "Mehfil-e-Rekhta Lounge",
  "settings": [
    { "type": "text", "id": "title", "label": "Heading", "default": "Urdu Poetry, Timeless Shayari & Progressive Literary Classics" },
    { "type": "textarea", "id": "subtitle", "label": "Subheading", "default": "Step into an intimate literary mehfil featuring official Rekhta editions, rebellious prose, and the finest verse of the subcontinent." }
  ],
  "presets": [
    { "name": "Mehfil-e-Rekhta Lounge" }
  ]
}
{% endschema %}
"""

# ==============================================================
# 4. sections/bundle-unboxing.liquid
# ==============================================================
bundle_unboxing_liquid = """{% comment %}
  Indigo Books India - Interactive Bundle Unboxing Showcase
  Playing-card fan-out physics on hover revealing individual volumes
{% endcomment %}

<section id="bundleUnboxingSection" class="py-20 lg:py-24 bg-[#F4EFE6] border-y border-amber-900/10 relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 bg-amber-200/70 text-amber-900 border border-amber-400/40 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm">
        <svg class="w-3.5 h-3.5 fill-current text-amber-800" viewBox="0 0 24 24"><path d="M21 16.5l-9 5.25L3 16.5v-9l9-5.25 9 5.25v9zM12 3.75L4.5 8.1 12 12.45l7.5-4.35L12 3.75zM4.5 9.9v6.6l6.75 3.9v-6.6L4.5 9.9zm8.25 10.5l6.75-3.9V9.9l-6.75 3.9v6.6z"/></svg>
        <span>{{ section.settings.badge | default: "COLLECTOR'S CORNER & BOX SETS" }}</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3">
        {{ section.settings.title | default: "The Unboxing Showcase: Curated Multi-Volume Sets" }}
      </h2>
      <p class="text-sm lg:text-base text-slate-600 mt-2">
        {{ section.settings.subtitle | default: "Hover over any collector's box to unpack the editions and inspect the individual titles inside." }}
      </p>
    </div>

    <!-- 3 Oversized Feature Bundle Cards -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      
      <!-- BUNDLE 1: Arundhati Roy -->
      <div class="bg-white border border-[#E4DAC7] rounded-2xl p-6 lg:p-7 shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group/bundle">
        <div>
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

          <div class="bundle-unbox-stage relative h-64 flex items-center justify-center my-6 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-amber-900/10 border-2 border-dashed border-amber-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-medium text-amber-900/40 uppercase tracking-widest font-mono">Collector Slipcase</span>
            </div>
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="{{ 'hero-book-arundhati.jpg' | asset_url }}" alt="Arundhati Roy Novel 1" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="{{ 'book-cheelwali-kothi.jpg' | asset_url }}" alt="Arundhati Roy Novel 2" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
          </div>

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
            <button onclick="addToCart('bundle-1', 'Arundhati Roy Definitive Duo Boxset', 799, '{{ 'hero-book-arundhati.jpg' | asset_url }}')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Arundhati%20Roy%20Duo%20Boxset%20(%E2%82%B9799)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- BUNDLE 2: Sarah J. Maas ACOTAR -->
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

          <div class="bundle-unbox-stage relative h-64 flex items-center justify-center my-6 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-purple-900/10 border-2 border-dashed border-purple-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-medium text-purple-900/40 uppercase tracking-widest font-mono">5 Volumes Pack</span>
            </div>
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="{{ 'book-acotar.jpg' | asset_url }}" alt="ACOTAR Volume 1" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-mid absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="{{ 'book-alchemised.jpg' | asset_url }}" alt="ACOTAR Volume 2" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-30">
              <img src="{{ 'book-acotar.jpg' | asset_url }}" alt="ACOTAR Volume 3" class="w-full h-full object-cover">
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
            <button onclick="addToCart('bundle-2', 'A Court of Thorns and Roses 5-Book Boxset', 1899, '{{ 'book-acotar.jpg' | asset_url }}')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add Boxset
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20ACOTAR%20Boxset%20(%E2%82%B91899)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- BUNDLE 3: Haruki Murakami -->
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

          <div class="bundle-unbox-stage relative h-64 flex items-center justify-center my-6 perspective-[1000px] cursor-pointer">
            <div class="absolute inset-x-8 inset-y-4 bg-rose-900/10 border-2 border-dashed border-rose-800/20 rounded-xl flex items-center justify-center -z-10 group-hover/bundle:opacity-0 transition-opacity">
              <span class="text-[11px] font-medium text-rose-900/40 uppercase tracking-widest font-mono">Murakami Box</span>
            </div>
            <div class="unbox-book unbox-book-1 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-10">
              <img src="{{ 'hero-book-murakami.jpg' | asset_url }}" alt="Norwegian Wood" class="w-full h-full object-cover">
              <div class="absolute inset-y-0 left-0 w-2 bg-gradient-to-r from-black/60 to-transparent"></div>
            </div>
            <div class="unbox-book unbox-book-2 absolute w-28 aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-2xl transition-all duration-500 ease-out z-20">
              <img src="{{ 'book-ratan-tata.jpg' | asset_url }}" alt="Kafka on the Shore" class="w-full h-full object-cover">
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
            <button onclick="addToCart('bundle-3', 'Best of Haruki Murakami 3-Book Set', 1299, '{{ 'hero-book-murakami.jpg' | asset_url }}')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
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

{% schema %}
{
  "name": "Bundle Unboxing Showcase",
  "settings": [
    { "type": "text", "id": "badge", "label": "Badge Text", "default": "COLLECTOR'S CORNER & BOX SETS" },
    { "type": "text", "id": "title", "label": "Heading", "default": "The Unboxing Showcase: Curated Multi-Volume Sets" },
    { "type": "textarea", "id": "subtitle", "label": "Subheading", "default": "Hover over any collector's box to unpack the editions and inspect the individual titles inside." }
  ],
  "presets": [
    { "name": "Bundle Unboxing Showcase" }
  ]
}
{% endschema %}
"""

# ==============================================================
# 5. sections/regional-magazine.liquid
# ==============================================================
regional_magazine_liquid = """{% comment %}
  Indigo Books India - Indian Regional & Fiction Editorial Magazine Masonry
  Editorial feature story card + vintage library loan borrow slips
{% endcomment %}

<section id="regionalMagazineSection" class="py-20 lg:py-24 bg-[#FAF8F5] relative overflow-hidden">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 pb-4 border-b border-amber-900/10 gap-4">
      <div>
        <div class="inline-flex items-center gap-2 bg-amber-100 text-[#D99B26] border border-amber-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase mb-2">
          <span>LITERARY SPOTLIGHT • REGIONAL CLASSICS</span>
        </div>
        <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128]">
          {{ section.settings.title | default: "Indian Voices & Contemporary Hindi Fiction" }}
        </h2>
        <p class="text-sm text-slate-600 mt-1 max-w-xl">
          {{ section.settings.subtitle | default: "Original Hindi prose, Sahitya Akademi laureates, and evocative tales rooted in the heartlands of India." }}
        </p>
      </div>
      <a href="/collections/all" class="text-xs font-bold uppercase tracking-wider text-[#D99B26] hover:text-[#B88019] inline-flex items-center gap-1">
        <span>Explore All 2,000+ Regional Titles</span>
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
      </a>
    </div>

    <!-- Editorial Bento Grid: 5 Cols Hero Feature + 7 Cols 2x2 Index Cards -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
      
      <!-- LEFT 5 COLS: Feature Story Card -->
      <div class="lg:col-span-5 bg-white border border-[#E8DFC8] rounded-2xl p-6 lg:p-8 shadow-md hover:shadow-xl transition-all duration-300 flex flex-col justify-between relative group">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-800 bg-amber-100 border border-amber-300 px-3 py-1 rounded-full">
              Prayagraj Literary Heritage Pick
            </span>
            <span class="text-[11px] font-semibold text-rose-700 bg-rose-50 border border-rose-200 px-2.5 py-0.5 rounded-full">
              Only 4 copies left
            </span>
          </div>

          <div class="w-44 lg:w-48 mx-auto aspect-[2/3] rounded-r-md rounded-l-sm overflow-hidden shadow-[0_20px_40px_rgba(0,0,0,0.4)] my-4 group-hover:scale-105 transition-transform duration-300 relative">
            <img src="{{ 'book-cheelwali-kothi.jpg' | asset_url }}" alt="Cheelwali Kothi" class="w-full h-full object-cover">
            <div class="absolute inset-y-0 left-0 w-2.5 bg-gradient-to-r from-black/60 to-transparent"></div>
          </div>

          <h3 class="font-serif text-2xl font-bold text-[#0A1128] text-center mt-3 group-hover:text-[#D99B26] transition-colors">
            चीलवाली कोठी (Cheelwali Kothi)
          </h3>
          <p class="text-xs text-slate-500 text-center mt-0.5">By Sara Rai • Rajkamal Prakashan</p>

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
            <button onclick="addToCart('reg-hero', 'चीलवाली कोठी (Cheelwali Kothi)', 299, '{{ 'book-cheelwali-kothi.jpg' | asset_url }}')" class="bg-[#D99B26] hover:bg-[#B88019] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Cheelwali%20Kothi%20(%E2%82%B9299)." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2.5 px-3 rounded-xl font-semibold text-xs transition-colors text-center">
              WhatsApp COD
            </a>
          </div>
        </div>
      </div>

      <!-- RIGHT 7 COLS: 2x2 Grid of Library Index Cards -->
      <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-5">
        
        <!-- Card 1 -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="{{ 'book-nar-nareeshwar.jpg' | asset_url }}" alt="Nar Nareeshwar" class="w-full h-full object-cover">
            </div>
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
          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2">
            <button onclick="addToCart('index-1', 'नर-नारीश्वर', 320, '{{ 'book-nar-nareeshwar.jpg' | asset_url }}')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Nar-Nareeshwar%20(%E2%82%B9320)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="{{ 'book-patthar-alpatthar.jpg' | asset_url }}" alt="Patthar aur Alpatthar" class="w-full h-full object-cover">
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
            <button onclick="addToCart('index-2', 'पत्थर और अलपत्थर', 240, '{{ 'book-patthar-alpatthar.jpg' | asset_url }}')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Patthar%20aur%20Alpatthar%20(%E2%82%B9240)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="{{ 'book-aurat-farosh.jpg' | asset_url }}" alt="Aurat Farosh" class="w-full h-full object-cover">
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
              <div class="text-[10px] text-amber-800 font-mono mt-1">Social Fiction</div>
              <div class="mt-2 text-xs font-bold text-slate-900 font-serif">₹280.00 <span class="text-[10px] text-slate-400 line-through">₹360</span></div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2">
            <button onclick="addToCart('index-3', 'औरत फ़रोश', 280, '{{ 'book-aurat-farosh.jpg' | asset_url }}')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Aurat%20Farosh%20(%E2%82%B9280)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 4 -->
        <div class="library-index-card bg-[#FFFDF9] border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 relative overflow-hidden group flex flex-col justify-between">
          <div class="flex gap-4">
            <div class="w-20 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-amber-900/20 group-hover:scale-105 transition-transform">
              <img src="{{ 'book-lagbhag-single.jpg' | asset_url }}" alt="Lagbhag Single" class="w-full h-full object-cover">
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
              <div class="text-[10px] text-amber-800 font-mono mt-1">Kanpur Chronicles</div>
              <div class="mt-2 text-xs font-bold text-slate-900 font-serif">₹250.00 <span class="text-[10px] text-slate-400 line-through">₹350</span></div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-[#E8DFC8]/60 flex items-center justify-between gap-2">
            <button onclick="addToCart('index-4', 'लगभग सिंगल', 250, '{{ 'book-lagbhag-single.jpg' | asset_url }}')" class="flex-1 bg-amber-100 hover:bg-amber-200 text-[#0A1128] py-1.5 px-2 rounded-lg text-xs font-semibold transition-colors">Add</button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20Lagbhag%20Single%20(%E2%82%B9250)." target="_blank" class="p-1.5 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-lg transition-colors">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>

      </div>

    </div>

  </div>
</section>

{% schema %}
{
  "name": "Regional Fiction Masonry",
  "settings": [
    { "type": "text", "id": "title", "label": "Heading", "default": "Indian Voices & Contemporary Hindi Fiction" },
    { "type": "textarea", "id": "subtitle", "label": "Subheading", "default": "Original Hindi prose, Sahitya Akademi laureates, and evocative tales rooted in the heartlands of India." }
  ],
  "presets": [
    { "name": "Regional Fiction Masonry" }
  ]
}
{% endschema %}
"""

# ==============================================================
# 6. sections/academic-vault.liquid
# ==============================================================
academic_vault_liquid = """{% comment %}
  Indigo Books India - Interactive Law & Academic Vault Split-Finder
  Sticky drawer selector tabs + high-density spec-sheet grid + instant search
{% endcomment %}

<section id="academicVaultSection" class="py-20 lg:py-24 bg-white border-y border-slate-200 relative">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    
    <div class="text-center max-w-3xl mx-auto mb-12">
      <div class="inline-flex items-center gap-2 bg-slate-100 text-slate-800 border border-slate-300 px-3.5 py-1 rounded-full text-xs font-bold tracking-wider uppercase shadow-sm">
        <svg class="w-3.5 h-3.5 fill-current text-slate-700" viewBox="0 0 24 24"><path d="M12 2L1 21h22L12 2zm0 3.8l7.53 13.2H4.47L12 5.8zM11 10v4h2v-4h-2zm0 6v2h2v-2h-2z"/></svg>
        <span>ACADEMIC & SCHOLARLY VAULT</span>
      </div>
      <h2 class="font-serif text-3xl lg:text-4xl font-bold text-[#0A1128] mt-3">
        {{ section.settings.title | default: "Law, Judiciary & Sahitya Reference Archive" }}
      </h2>
      <p class="text-sm lg:text-base text-slate-600 mt-2">
        {{ section.settings.subtitle | default: "Authoritative legal treatises, Hindi linguistics, university standards, and competitive civil services references." }}
      </p>
    </div>

    <!-- Sticky Two-Pane Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      
      <!-- LEFT 4 COLS: Library Drawer Selector -->
      <div class="lg:col-span-4 lg:sticky lg:top-28 space-y-4">
        
        <div class="bg-[#FAF8F5] border border-amber-900/10 rounded-2xl p-5 shadow-sm">
          <div class="text-xs uppercase font-bold text-slate-400 tracking-wider mb-3">
            Select Archive Drawer:
          </div>

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

          <div class="mt-4 pt-4 border-t border-slate-200">
            <div class="relative">
              <svg class="w-4 h-4 text-slate-400 absolute left-3 top-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
              <input type="text" id="vaultSearchInput" onkeyup="filterVaultBooks(this.value)" placeholder="Search vault titles, authors..." class="w-full text-xs pl-9 pr-3 py-2.5 rounded-lg border border-slate-300 focus:outline-none focus:border-[#D99B26] bg-white">
            </div>
          </div>
        </div>

        <div class="bg-gradient-to-br from-[#0A1128] to-[#1E293B] text-white rounded-2xl p-5 shadow-md">
          <div class="text-amber-400 text-xs font-bold uppercase tracking-wider mb-1">
            📚 Bulk & Institutional Supply
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
        
        <div class="flex items-center justify-between pb-3 mb-6 border-b border-slate-200">
          <div class="flex items-center gap-2">
            <span id="vaultDrawerActiveTitle" class="font-serif text-lg font-bold text-[#0A1128]">
              ⚖️ Law & Jurisprudence (Essential Legal References)
            </span>
          </div>
          <span id="vaultCountTag" class="text-xs text-slate-500 font-mono">Showing 4 cataloged editions</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5" id="vaultCardsGrid">
          
          <!-- Card 1 -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="{{ 'book-medical-jurisprudence.jpg' | asset_url }}" alt="Medical Jurisprudence" class="w-full h-full object-cover">
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
                <button onclick="addToCart('law-1', 'Modi Medical Jurisprudence', 1850, '{{ 'book-medical-jurisprudence.jpg' | asset_url }}')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold">
                  Add to Cart
                </button>
              </div>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="{{ 'book-lawful-awful.jpg' | asset_url }}" alt="Lawful Awful" class="w-full h-full object-cover">
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
                <button onclick="addToCart('law-2', 'Lawful Awful: Life in Law', 450, '{{ 'book-lawful-awful.jpg' | asset_url }}')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold">
                  Add to Cart
                </button>
              </div>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="{{ 'book-10-faisle.jpg' | asset_url }}" alt="10 Faisle" class="w-full h-full object-cover">
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
                <button onclick="addToCart('law-3', '१० फ़ैसले जिन्होंने देश बदल दिया', 320, '{{ 'book-10-faisle.jpg' | asset_url }}')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold">
                  Add to Cart
                </button>
              </div>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex gap-4">
            <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
              <img src="{{ 'book-bench-bar.jpg' | asset_url }}" alt="Bench & Bar" class="w-full h-full object-cover">
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
                <button onclick="addToCart('law-4', 'Bench and Bar: Reminiscences', 590, '{{ 'book-bench-bar.jpg' | asset_url }}')" class="bg-[#0A1128] hover:bg-[#D99B26] text-white p-2 rounded-lg transition-colors text-xs font-semibold">
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

{% schema %}
{
  "name": "Law & Academic Vault",
  "settings": [
    { "type": "text", "id": "title", "label": "Heading", "default": "Law, Judiciary & Sahitya Reference Archive" },
    { "type": "textarea", "id": "subtitle", "label": "Subheading", "default": "Authoritative legal treatises, Hindi linguistics, university standards, and competitive civil services references." }
  ],
  "presets": [
    { "name": "Law & Academic Vault" }
  ]
}
{% endschema %}
"""

# Write all 6 files
files_to_write = {
  "sections/literary-marquee.liquid": literary_marquee_liquid,
  "sections/curators-podium.liquid": curators_podium_liquid,
  "sections/mehfil-rekhta.liquid": mehfil_rekhta_liquid,
  "sections/bundle-unboxing.liquid": bundle_unboxing_liquid,
  "sections/regional-magazine.liquid": regional_magazine_liquid,
  "sections/academic-vault.liquid": academic_vault_liquid,
}

for path, content in files_to_write.items():
  with open(path, 'w', encoding='utf-8') as f:
    f.write(content.strip() + "\n")
  print(f"Created/Updated {path}")

# ==============================================================
# 7. UPDATE templates/index.json
# ==============================================================
index_json_data = {
  "sections": {
    "hero": {
      "type": "hero",
      "settings": {
        "heading": "Discover Your Next Favorite Story",
        "subtext": "Explore India's largest online collection of bestsellers, regional gems, academic reads, and more.",
        "primary_btn_label": "Shop Now",
        "primary_btn_url": "/collections/all"
      }
    },
    "literary_marquee": {
      "type": "literary-marquee",
      "settings": {}
    },
    "curators_podium": {
      "type": "curators-podium",
      "settings": {}
    },
    "mehfil_rekhta": {
      "type": "mehfil-rekhta",
      "settings": {}
    },
    "bundle_unboxing": {
      "type": "bundle-unboxing",
      "settings": {}
    },
    "regional_magazine": {
      "type": "regional-magazine",
      "settings": {}
    },
    "academic_vault": {
      "type": "academic-vault",
      "settings": {}
    },
    "trust_strip": {
      "type": "trust-strip",
      "settings": {}
    },
    "contact_section": {
      "type": "contact-section",
      "settings": {}
    },
    "about_indigo": {
      "type": "media-with-content",
      "settings": {
        "layout": "image_first",
        "subheading": "INDIGO BOOKS INDIA - PRAYAGRAJ",
        "heading": "Connecting Readers Across India",
        "text": "<p>Indigo Books India is your dedicated independent bookstore based in the historic literary city of Prayagraj. We provide over 11,922+ authentic books with Cash on Delivery (COD) and fast shipping to every corner of India.</p>",
        "button_label": "Explore Catalog",
        "button_link": "/collections/all"
      }
    }
  },
  "order": [
    "hero",
    "literary_marquee",
    "curators_podium",
    "mehfil_rekhta",
    "bundle_unboxing",
    "regional_magazine",
    "academic_vault",
    "trust_strip",
    "contact_section",
    "about_indigo"
  ]
}

with open("templates/index.json", "w", encoding="utf-8") as f:
  json.dump(index_json_data, f, indent=2)
print("Updated templates/index.json with the 6 new sections in order!")

