# -*- coding: utf-8 -*-
"""
build_html_generator.py
Generates the authoritative preview.html for Indigo Books India.
Fully redesigned based on video_1.mp4 and video_2.mp4:
- Video 1: 14-Book Floating Scatter Hero + SVG Calligraphic Thread + Mouse/Scroll Parallax
- Video 1: Sticky Dark Curtain Slide-Over + Word-by-Word Scroll-Scrubbed Illumination
- Video 1: 3D Tilted Sheet Unfold (-8deg -> 0deg)
- Video 2: App-Style Bookstore Interface with Left Vertical Icon Rail, Horizontal Shelves with 3D Overlapping Cards, and Persistent Bottom Player Bar
- Video 2: Split-Screen Solo Product Studio View with -180deg 2-Page Spread Flip, Reading Excerpt Swap, and Vertical Action Dock
- Dedicated 2-Character Predictive Search Results View
- Dedicated Single Product Page View
- Full Modals: Cart Drawer, Quick Overview, Login, Express Phone Checkout, Order Confirmation
- Floating WhatsApp Commerce Button
"""

import os
import json
import re

from store_data import (
    PODIUM_BOOKS,
    POET_SHAYARI_DATA,
    REKHTA_BOOKS,
    VAULT_BOOKS,
    CATEGORY_BENTO_DATA,
    CATALOG_BOOKS,
    PIYUSH_MISHRA_BOOKS,
    RAHI_MASOOM_RAZA_BOOKS,
    MASTER_SEARCH_CATALOG,
    MODAL_METADATA_DATABASE
)
from store_styles import UNIFIED_STORE_CSS
from store_scripts import UNIFIED_STORE_JS
from prepare_master_blocks import MASTER_STYLE, MASTER_SCRIPT
from editorial_video_theme import EDITORIAL_STYLE, EDITORIAL_SCRIPT, EDITORIAL_HTML, EDITORIAL_HOMEPAGE_HTML, EDITORIAL_SOLO_HTML
from store_modals_and_search import SEARCH_AND_MODALS_HTML

def build_preview_html():
    podium_json = json.dumps(PODIUM_BOOKS, ensure_ascii=False)
    poet_json = json.dumps(POET_SHAYARI_DATA, ensure_ascii=False)
    vault_json = json.dumps(VAULT_BOOKS, ensure_ascii=False)
    bento_json = json.dumps(CATEGORY_BENTO_DATA, ensure_ascii=False)
    catalog_json = json.dumps(CATALOG_BOOKS, ensure_ascii=False)
    piyush_json = json.dumps(PIYUSH_MISHRA_BOOKS, ensure_ascii=False)
    rahi_json = json.dumps(RAHI_MASOOM_RAZA_BOOKS, ensure_ascii=False)
    # Curate high-performance 2,000+ book repository for instant search & instant modal
    curated_modal_meta = {}
    featured_ids = set()
    for b in PODIUM_BOOKS: featured_ids.add(b['id'])
    for cat in VAULT_BOOKS.values():
        for b in cat: featured_ids.add(b['id'])
    for b in CATALOG_BOOKS: featured_ids.add(b['id'])
    for b in PIYUSH_MISHRA_BOOKS: featured_ids.add(b['id'])
    for b in RAHI_MASOOM_RAZA_BOOKS: featured_ids.add(b['id'])

    for fid in featured_ids:
        if fid in MODAL_METADATA_DATABASE:
            curated_modal_meta[fid] = MODAL_METADATA_DATABASE[fid]

    for item in MASTER_SEARCH_CATALOG:
        iid = item.get('id')
        if iid and iid in MODAL_METADATA_DATABASE and iid not in curated_modal_meta:
            curated_modal_meta[iid] = MODAL_METADATA_DATABASE[iid]
            if len(curated_modal_meta) >= 2200:
                break

    compact_search_catalog = []
    for b in MASTER_SEARCH_CATALOG:
        compact_search_catalog.append({
            'id': b.get('id'),
            'handle': b.get('handle'),
            'title': b.get('title'),
            'author': b.get('author') or b.get('vendor') or 'Curated Author',
            'isbn': b.get('isbn') or b.get('sku') or '',
            'price': b.get('price') or ('₹' + str(int(b.get('mrp') or 299)) + '.00'),
            'rawPrice': b.get('mrp') or b.get('rawPrice') or 299,
            'mrp': b.get('mrp') or 299,
            'binding': b.get('binding') or b.get('format') or 'Paperback',
            'format': b.get('format') or b.get('binding') or 'Paperback',
            'publisher': b.get('publisher') or b.get('pub') or 'Rajkamal Prakashan',
            'pages': b.get('pages') or '320p',
            'cover': b.get('cover') or b.get('image') or b.get('coverUrl') or 'hero-godan.jpg',
            'category': b.get('category') or 'Classic Literature',
            'edition': b.get('edition') or 'Authenticated Edition',
            'lang': b.get('lang') or 'Hindi'
        })
    master_search_json = json.dumps(compact_search_catalog, ensure_ascii=False)
    modal_meta_json = json.dumps(curated_modal_meta, ensure_ascii=False)

    head_str = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="referrer" content="no-referrer">
  <meta http-equiv="content-language" content="en">
  <meta name="google" content="notranslate">
  <meta name="google-site-verification" content="-e_RVQPApfsjWvvXEfSgc-ttWxIqb9hqO7eUvZCF1ZI">
  <title>Indigo Books India — Premier Online Bookstore Prayagraj (Official)</title>
  
  <!-- Official Vector SVG Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='16' fill='%230066B3'/%3E%3Cpath d='M20 20h25v25H20zM55 20h25v25H55zM20 55h25v25H20zM55 55h25v25H55z' fill='none' stroke='%23ffffff' stroke-width='6'/%3E%3C/svg%3E" />

  <!-- Google Fonts: Cormorant Garamond, Merriweather & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">
  
  <!-- Suppress Tailwind Production Warning BEFORE CDN Script Evaluation -->
  <script>
    (function() {{
      var origWarn = console.warn;
      console.warn = function() {{
        if (arguments[0] && typeof arguments[0] === 'string' && arguments[0].indexOf('cdn.tailwindcss.com') !== -1) return;
        return origWarn.apply(console, arguments);
      }};
    }})();
  </script>

  <!-- Tailwind CSS Engine -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
{UNIFIED_STORE_CSS}
  </style>
  <script>
    window.getFallbackCover = function(title, author) {{
      var t = (title || 'Indigo Books').replace(/<[^>]*>/g, '').substring(0, 32);
      var a = (author || 'Indigo Classics').replace(/<[^>]*>/g, '').substring(0, 24);
      var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 450" width="100%" height="100%">' +
        '<rect width="300" height="450" fill="#1C1A17"/>' +
        '<rect x="12" y="12" width="276" height="426" fill="none" stroke="#E04F33" stroke-width="2"/>' +
        '<text x="150" y="210" font-family="serif" font-size="20" fill="#FAF8F5" font-weight="bold" text-anchor="middle">' + t + '</text>' +
        '<text x="150" y="245" font-family="sans-serif" font-size="13" fill="#D4AF37" text-anchor="middle">' + a + '</text>' +
        '</svg>';
      return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
    }};
    var getFallbackCover = window.getFallbackCover;
    window.getFallbackCoverSvg = window.getFallbackCover;

    window.handleBookCoverError = function(img, title, author) {{
      if (!img) return;
      img.onerror = null;
      var t = title || img.getAttribute('data-title') || img.alt || 'Indigo Books Edition';
      var a = author || img.getAttribute('data-author') || 'Indigo Archive';
      var fallback = (typeof window.getFallbackCoverSvg === 'function') ? window.getFallbackCoverSvg(t, a) : (typeof getFallbackCover === 'function' ? getFallbackCover(t, a) : '');
      if (img.parentElement) {{
        img.parentElement.style.backgroundImage = 'url("' + fallback + '")';
        img.parentElement.style.backgroundSize = 'cover';
        img.parentElement.style.backgroundPosition = 'center';
      }}
      img.style.display = 'none';
      img.src = fallback;
    }};
  </script>
{MASTER_STYLE}
{EDITORIAL_STYLE}
</head>
<body id="top">
"""

    navbar_str = """  <!-- =========================================================================
       1. MINIMAL EDITORIAL HEADER (Sticky 76px with Live Search & Reading Bag)
       ========================================================================= -->
  <header class="site-navbar site-header">
    <div class="site-container navbar-inner">
      <!-- Left: Hamburger Menu (Mobile) & Brand Logo -->
      <div class="v2-nav-brand-group">
        <button type="button" class="v2-hamburger-btn" id="v2MobileMenuBtn" aria-label="Open Navigation Menu" onclick="window.toggleMobileDrawer ? window.toggleMobileDrawer(true) : null;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
        <a href="#top" class="brand-editorial-title" onclick="window.returnToHome ? window.returnToHome(event) : null;">
          <img src="assets/indigo-books-logo.png" alt="Indigo Books" class="brand-logo-img" onerror="this.src='assets/logo.png'" />
          <div class="brand-text-col">
            <span class="brand-name">INDIGO BOOKS</span>
            <span class="brand-editorial-subtitle">PRAYAGRAJ &bull; INDIA</span>
          </div>
        </a>
        <ul class="nav-editorial-links">
          <li><a href="#shelf-popular">Popular Picks</a></li>
          <li><a href="#shelf-hindi">Hindi Classics</a></li>
          <li><a href="#shelf-poetry">Poetry &amp; Rekhta</a></li>
          <li><a href="#shelf-law">Law &amp; Criticism</a></li>
          <li><a href="#video2-bookstore-app" onclick="window.scrollToAppSection ? window.scrollToAppSection('shelf-popular') : null;">Archive (5,559)</a></li>
        </ul>
      </div>

      <!-- Center: 2-Character Predictive Live Search -->
      <div class="editorial-search-wrap">
        <svg class="editorial-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="editorialSearchInput" class="editorial-search-input" placeholder="Search 5,559 books, authors, ISBN..." autocomplete="off" />
        <div id="editorialSearchResults" class="editorial-search-results"></div>
      </div>

      <!-- Right: Desktop Reading Bag & 1-Click Express Order -->
      <div class="editorial-header-actions">
        <button type="button" class="btn-reading-bag" onclick="window.toggleCartDrawer ? window.toggleCartDrawer() : null;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line></svg>
          <span>Reading Bag (<span id="cartCount">0</span>)</span>
        </button>
        <button type="button" class="btn-1click-express" onclick="window.openQuickOrderModal ? window.openQuickOrderModal('podium-godan') : null;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#E04F33" stroke-width="2.2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span>1-Click Order</span>
        </button>
      </div>

      <!-- Right: Mobile Header Quick Actions -->
      <div class="v2-mobile-nav-actions">
        <button type="button" class="v2-mobile-quick-btn" onclick="window.openQuickOrderModal ? window.openQuickOrderModal('podium-godan') : null;" aria-label="1-Click WhatsApp Order" title="1-Click Order">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#E04F33" stroke-width="2.2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
        </button>
        <button type="button" class="v2-mobile-bag-btn" onclick="window.toggleCartDrawer ? window.toggleCartDrawer() : null;" aria-label="Reading Bag">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line></svg>
          <span class="v2-mobile-bag-badge" id="v2MobileBagCount">0</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Slide-out Mobile Navigation Drawer & Backdrop (Directly on Body for 100% Isolation & Clean Layering) -->
  <div id="v2MobileDrawerBackdrop" class="v2-mobile-drawer-backdrop" onclick="window.toggleMobileDrawer ? window.toggleMobileDrawer(false) : null;"></div>
  <aside id="v2MobileDrawer" class="v2-mobile-drawer" aria-label="Mobile Navigation Drawer">
    <!-- Drawer Top Bar -->
    <div class="v2-drawer-top-bar">
      <div class="v2-drawer-brand">
        <img src="assets/indigo-books-logo.png" alt="Indigo Books" class="v2-drawer-logo-img" onerror="this.src='assets/logo.png'" />
        <div class="v2-drawer-brand-text">
          <span class="v2-drawer-brand-name">INDIGO BOOKS</span>
          <span class="v2-drawer-brand-sub">PRAYAGRAJ &bull; INDIA</span>
        </div>
      </div>
      <button type="button" class="v2-drawer-close-btn" onclick="window.toggleMobileDrawer ? window.toggleMobileDrawer(false) : null;" aria-label="Close Menu">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>

    <!-- Drawer Content -->
    <div class="v2-drawer-body">
      <div class="v2-drawer-section-title">COLLECTIONS</div>
      <nav class="v2-drawer-nav">
        <!-- Popular Picks -->
        <a href="#shelf-popular" class="v2-drawer-nav-item" onclick="window.handleMobileNavLink ? window.handleMobileNavLink('#shelf-popular') : null;">
          <div class="v2-drawer-item-left">
            <span class="v2-drawer-icon-box v2-icon-terracotta">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </span>
            <span class="v2-drawer-item-label">Popular Picks</span>
          </div>
          <svg class="v2-drawer-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- Hindi Classics & Masterpieces -->
        <a href="#shelf-hindi" class="v2-drawer-nav-item" onclick="window.handleMobileNavLink ? window.handleMobileNavLink('#shelf-hindi') : null;">
          <div class="v2-drawer-item-left">
            <span class="v2-drawer-icon-box v2-icon-navy">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
            </span>
            <span class="v2-drawer-item-label">Hindi Classics &amp; Masterpieces</span>
          </div>
          <svg class="v2-drawer-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- Poetry & Rekhta -->
        <a href="#shelf-poetry" class="v2-drawer-nav-item" onclick="window.handleMobileNavLink ? window.handleMobileNavLink('#shelf-poetry') : null;">
          <div class="v2-drawer-item-left">
            <span class="v2-drawer-icon-box v2-icon-indigo">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg>
            </span>
            <span class="v2-drawer-item-label">Poetry &amp; Rekhta</span>
          </div>
          <svg class="v2-drawer-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- Law & Constitution -->
        <a href="#shelf-law" class="v2-drawer-nav-item" onclick="window.handleMobileNavLink ? window.handleMobileNavLink('#shelf-law') : null;">
          <div class="v2-drawer-item-left">
            <span class="v2-drawer-icon-box v2-icon-amber">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18"></path><path d="M6 8l6-3 6 3"></path><path d="M3 13l3-5 3 5a3 3 0 0 1-6 0z"></path><path d="M15 13l3-5 3 5a3 3 0 0 1-6 0z"></path></svg>
            </span>
            <span class="v2-drawer-item-label">Law &amp; Constitution</span>
          </div>
          <svg class="v2-drawer-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- Full Archive (5,559 Editions) -->
        <a href="#video2-bookstore-app" class="v2-drawer-nav-item" onclick="window.handleMobileNavLink ? window.handleMobileNavLink('#video2-bookstore-app') : null;">
          <div class="v2-drawer-item-left">
            <span class="v2-drawer-icon-box v2-icon-slate">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            </span>
            <span class="v2-drawer-item-label">Full Archive (5,559 Editions)</span>
          </div>
          <svg class="v2-drawer-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>
      </nav>

      <div class="v2-drawer-section-title" style="margin-top: 24px;">FEATURED AUTHORS</div>
      <div class="v2-drawer-authors-wrap">
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Premchand') : null;">Premchand</button>
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Shrilal Shukla') : null;">Shrilal Shukla</button>
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Ramdhari Singh Dinkar') : null;">Dinkar</button>
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Javed Akhtar') : null;">Javed Akhtar</button>
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Piyush Mishra') : null;">Piyush Mishra</button>
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Mirza Ghalib') : null;">Mirza Ghalib</button>
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Dr. B.R. Ambedkar') : null;">Ambedkar</button>
        <button type="button" class="v2-author-pill-btn" onclick="window.handleMobileAuthorClick ? window.handleMobileAuthorClick('Subhash Kashyap') : null;">Subhash Kashyap</button>
      </div>
    </div>

    <!-- Drawer Footer Actions -->
    <div class="v2-drawer-footer">
      <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books%20India%2C%20I%20would%20like%20to%20order%20books." target="_blank" rel="noopener noreferrer" class="v2-drawer-wa-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>WhatsApp Order (+91 8933063306)</span>
      </a>
      <button type="button" class="v2-drawer-bag-btn" onclick="window.toggleMobileDrawer ? window.toggleMobileDrawer(false) : null; window.toggleCartDrawer ? window.toggleCartDrawer(true) : null;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line></svg>
        <span>Open Reading Bag (<span id="v2DrawerBagCount">0</span>)</span>
      </button>
    </div>
  </aside>"""

    hp_view_str = f"""
  <!-- =========================================================================
       HOMEPAGE VIEW (#homepage-view)
       Video 1 (Scatter Hero, Curtain, Tilted Sheet) & Video 2 (Bookstore App, Shelves, Full Archive)
       ========================================================================= -->
  <div id="homepage-view" class="store-view-section">
{EDITORIAL_HOMEPAGE_HTML}
  </div><!-- /#homepage-view -->
"""

    script_str = f"""
  <script id="indigo-catalog-database">
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
        if (typeof window.openSoloBookPage === 'function') {{
          window.openSoloBookPage(currentModalBookId);
        }} else if (typeof openDedicatedProductPage === 'function') {{
          openDedicatedProductPage(currentModalBookId);
        }}
      }}
    }}
  </script>

{MASTER_SCRIPT}

{EDITORIAL_SCRIPT}

</body>
</html>
"""

    return head_str + navbar_str + hp_view_str + EDITORIAL_SOLO_HTML + SEARCH_AND_MODALS_HTML + script_str

if __name__ == '__main__':
    html = build_preview_html()
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(html)
    size_mb = os.path.getsize('preview.html') / (1024 * 1024)
    print(f"Successfully generated preview.html! Size: {size_mb:.2f} MB")
