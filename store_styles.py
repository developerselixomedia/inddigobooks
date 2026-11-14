# -*- coding: utf-8 -*-
"""
store_styles.py
Complete CSS definitions for Indigo Books India e-commerce platform.
Strictly conforms to:
- Merriweather (700 bold) for headings/titles
- Plus Jakarta Sans (400-800) for body, nav, badges, stats, and prices
- font-variant-numeric: lining-nums tabular-nums !important;
- Left-aligned editorial headers, tight spacing (padding: 56px 0 !important; margin: 0 !important;)
- Pure CSS 3D book cover hinge (-135deg)
- 4-Phase Choreographed Hero Animation:
  Phase 1 (0.0s-1.0s): Rangoli fade-in + continuous spin, Diyas & lights ignite
  Phase 2 (0.6s-1.9s): 3D book cluster slides Left to Right (-550px -> 0)
  Phase 3 (1.4s-2.3s): Left column fades & slides up (translateY(25px) -> 0)
  Phase 4 (Hover): Solo hover spotlight (scale 1.22, rotateY 0deg, z-index 60, dimming other 5)
- 2-Tier 3D Book Depth:
  .book-tier-back: translateX(-16px) scale(0.94), z-index 20, brightness(0.92)
  .book-tier-front: translateX(16px) margin-top -28px, z-index 25, deep drop shadow
  .hero-standing-book: perspective(900px) rotateY(-18deg), border-right: 7px solid #F8FAFC
- Bundle playing-card fan-out
- Zero emoji styling, 100% Lucide SVG icon sizing
"""

UNIFIED_STORE_CSS = """
/* =========================================================================
   INDIGO BOOKS INDIA - PRODUCTION STYLESHEET
   Headquarters: Prayagraj, Uttar Pradesh, India
   ========================================================================= */

/* Google Fonts pre-loaded cleanly via <link> in <head> (Zero Early Hints warnings) */
/* ABSOLUTE HORIZONTAL OVERFLOW & RIGHT MARGIN ELIMINATION */
html, body {
  width: 100% !important;
  max-width: 100vw !important;
  overflow-x: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
  box-sizing: border-box !important;
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}

*, *:before, *:after {
  box-sizing: border-box !important;
}

body {
  position: relative !important;
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  color: #1E293B;
  background-color: #FAF8F5;
  line-height: 1.5;
  font-variant-numeric: lining-nums tabular-nums !important;
  font-feature-settings: "lnum" 1, "tnum" 1 !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

/* Strict Typography Hierarchy */
h1, h2, h3, .serif-heading, .book-title, .font-merriweather {
  font-family: 'Merriweather', Georgia, serif !important;
}

p, span, a, button, input, select, textarea, label, nav, div, .font-sans {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* Strict Lining Numbers on All Numbers, Stats, Badges, and Prices */
.price, [class*="price"], .stat-number, .stat-value, .badge, .pill, [data-num], table, .tab-num {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-variant-numeric: lining-nums tabular-nums !important;
  font-feature-settings: "lnum" 1, "tnum" 1 !important;
}

/* Eliminating Theme Gaps */
.shopify-section {
  margin: 0 !important;
  padding: 0 !important;
}
section {
  padding: 56px 0 !important;
  margin: 0 !important;
  position: relative;
  box-sizing: border-box;
}

/* Container */
.site-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 32px;
  box-sizing: border-box;
}
@media (max-width: 768px) {
  .site-container {
    padding: 0 16px;
  }
  section {
    padding: 40px 0 !important;
  }
}

/* Left-Aligned Editorial Section Headers */
.editorial-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 1px solid #E2E8F0;
  padding-bottom: 16px;
  margin-bottom: 32px;
}
.editorial-header .sec-overline {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #B45309;
  margin-bottom: 6px;
}
.editorial-header h2 {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 32px;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.25;
}
.editorial-header p {
  font-size: 14px;
  color: #64748B;
  margin-top: 4px;
}
@media (max-width: 768px) {
  .editorial-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  .editorial-header h2 {
    font-size: 24px;
  }
}

/* =========================================================================
   STICKY NAVBAR (100% VISIBLE & STICKY AT VERY TOP)
   ========================================================================= */
header,
.site-header,
.site-navbar,
.main-navbar,
header > nav {
  position: sticky !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  width: 100% !important;
  height: auto !important;
  min-height: unset !important;
  max-height: none !important;
  background-color: #FAF8F5 !important;
  border-bottom: 1px solid rgba(15, 23, 42, 0.12) !important;
  z-index: 99999 !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  overflow: visible !important;
  box-sizing: border-box !important;
  transition: all 0.25s ease;
}
@media (min-width: 992px) {
  header,
  .site-header,
  .site-navbar,
  .main-navbar {
    min-height: 72px !important;
  }
}
.navbar-inner {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  min-height: unset !important;
  box-sizing: border-box !important;
}
@media (min-width: 992px) {
  .navbar-inner {
    min-height: 72px !important;
  }
}
.brand-link {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  flex-shrink: 0;
}
.brand-wordmark {
  font-family: 'Merriweather', Georgia, serif !important;
  font-size: 19px;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: #0F172A;
  text-transform: uppercase;
  display: flex;
  flex-direction: column;
  line-height: 1;
}
.brand-submark {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: #B45309;
  margin-top: 3px;
}

.nav-links-wrap {
  display: flex;
  align-items: center;
  gap: 20px;
  list-style: none;
}
@media (max-width: 1024px) {
  .nav-links-wrap {
    display: none;
  }
}
.nav-link-btn {
  background: none;
  border: none;
  font-size: 13.5px;
  font-weight: 600;
  color: #334155;
  cursor: pointer;
  padding: 6px 4px;
  position: relative;
  transition: color 0.2s;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
}
.nav-link-btn:hover {
  color: #B45309;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}
.india-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FFFBEB;
  border: 1px solid #FDE68A;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 700;
  color: #92400E;
}
.tiranga-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: linear-gradient(180deg, #FF9933 33%, #FFFFFF 33%, #FFFFFF 66%, #138808 66%);
  box-shadow: 0 0 0 1px rgba(0,0,0,0.15);
}
.nav-signin-btn {
  background: none;
  border: 1px solid #CBD5E1;
  border-radius: 8px;
  padding: 7px 14px;
  font-size: 12.5px;
  font-weight: 600;
  color: #1E293B;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}
.nav-signin-btn:hover {
  background: #F1F5F9;
  border-color: #94A3B8;
}
.nav-cart-btn {
  background: #0F172A;
  color: #FFFFFF;
  border: none;
  border-radius: 8px;
  padding: 7px 14px;
  font-size: 12.5px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: background 0.2s;
}
.nav-cart-btn:hover {
  background: #1E293B;
}
.nav-whatsapp-btn {
  background: #25D366;
  color: #FFFFFF;
  text-decoration: none;
  border-radius: 8px;
  padding: 7px 14px;
  font-size: 12.5px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: background 0.2s;
  box-shadow: 0 2px 8px rgba(37, 211, 102, 0.3);
}
.nav-whatsapp-btn:hover {
  background: #1EBE5D;
}

/* =========================================================================
   HERO SECTION & 4-PHASE STORYBOARD ANIMATION
   ========================================================================= */
.hero-section {
  min-height: 540px;
  background: linear-gradient(115deg, #09122C 0%, #101C3D 45%, #2D221B 75%, #4A3319 100%);
  position: relative;
  overflow: hidden;
  padding: 56px 0 !important;
  color: #FFFFFF;
}

.hero-main-grid {
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 40px;
  align-items: center;
  position: relative;
  z-index: 20;
}
@media (max-width: 992px) {
  .hero-main-grid {
    grid-template-columns: 1fr;
    gap: 48px;
  }
}

/* Phase 3: Left Column Fade & Slide Up (1.4s - 2.3s) */
.hero-left-col {
  z-index: 30;
  animation: heroLeftColFadeUp 0.9s cubic-bezier(0.16, 1, 0.3, 1) 1.4s both;
}
@keyframes heroLeftColFadeUp {
  0% {
    transform: translateY(25px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

.hero-left-col h1 {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 52px;
  font-weight: 700;
  line-height: 1.15;
  color: #FFFFFF;
  margin-bottom: 16px;
}
.hero-left-col h1 em {
  color: #E5A93C;
  font-style: italic;
  font-family: 'Merriweather', Georgia, serif;
}
.hero-left-col p {
  font-size: 16px;
  line-height: 1.6;
  color: #CBD5E1;
  margin-bottom: 24px;
  max-width: 480px;
}
.hero-search-wrap {
  display: flex;
  align-items: center;
  background: #FFFFFF;
  border-radius: 9999px;
  padding: 12px 20px;
  gap: 12px;
  max-width: 440px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
  margin-bottom: 24px;
}
.hero-search-wrap input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 14px;
  color: #0F172A;
  background: transparent;
  padding: 0;
  font-family: 'Plus Jakarta Sans', sans-serif;
}
.hero-search-wrap input::placeholder {
  color: #94A3B8;
}

.hero-cta-row {
  display: flex;
  align-items: center;
  gap: 14px;
}
.hero-shop-btn {
  background: #D99B26;
  color: #0F172A;
  font-weight: 700;
  font-size: 14px;
  padding: 12px 28px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  transition: all 0.2s;
  box-shadow: 0 4px 14px rgba(217, 155, 38, 0.35);
}
.hero-shop-btn:hover {
  background: #E5A93C;
  transform: translateY(-1px);
}
.hero-wa-cod-btn {
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
  font-weight: 600;
  font-size: 14px;
  padding: 12px 24px;
  border-radius: 8px;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  transition: all 0.2s;
}
.hero-wa-cod-btn:hover {
  background: rgba(15, 23, 42, 0.85);
  border-color: rgba(255, 255, 255, 0.4);
}

/* Background Layer 1: Top-Left Subtle Watermark */
.hero-topleft-watermark {
  position: absolute;
  top: -30px;
  left: -30px;
  pointer-events: none;
  z-index: 1;
}

/* Hero Right Column Stage */
.hero-stage-col {
  position: relative;
  min-height: 480px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: visible;
}

/* Background Layer 2: Rotating Golden Geometric Rangoli Wheel */
.hero-wheel-wrap, .hero-rangoli-wrapper {
  width: 440px;
  height: 440px;
  position: absolute;
  top: 48%;
  left: 54%;
  transform: translate(-50%, -50%);
  z-index: 5 !important;
  pointer-events: none;
}
.hero-wheel-svg, .hero-rangoli-svg {
  width: 440px !important;
  height: 440px !important;
  display: block !important;
  animation: wheelSpin 45s linear infinite !important;
  transform-origin: center center !important;
}
@keyframes wheelSpin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Layer 4: String Lights */
.string-bulb circle {
  animation: bulbTwinkle 2.4s ease-in-out infinite alternate;
}

/* =========================================================================
   EXACT 3x2 BOOK GRID & SEQUENTIAL SPOTLIGHT ENGINE (FROM VIDEO)
   ========================================================================= */
.hero-books-grid-video {
  position: relative;
  z-index: 25 !important;
  display: grid;
  grid-template-columns: repeat(3, 128px);
  grid-template-rows: repeat(2, 188px);
  gap: 18px;
  align-items: center;
  justify-content: center;
  animation: heroClusterSlideIn 1.1s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
@keyframes heroClusterSlideIn {
  0% {
    transform: translateX(-40px);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}

.hero-video-book-card {
  position: relative;
  width: 128px;
  height: 188px;
  border-radius: 6px;
  overflow: hidden;
  border-right: 4px solid #F1F5F9;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.55);
  transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.45s ease, filter 0.45s ease, box-shadow 0.45s ease;
  cursor: pointer;
  background: #0F172A;
}

.hero-video-book-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Bottom Dark Info Drawer Inside Each Book (Title + Author + ₹ Price) */
.hero-book-meta {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(10, 17, 40, 0.94);
  backdrop-filter: blur(6px);
  padding: 8px 10px;
  border-top: 1px solid rgba(251, 191, 36, 0.35);
  transform: translateY(105%);
  opacity: 0;
  transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.35s ease;
  text-align: left;
  z-index: 10;
  pointer-events: none;
}

.hero-book-title {
  font-size: 11px;
  font-weight: 700;
  color: #FFFFFF;
  line-height: 1.2;
  margin-bottom: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.hero-book-author {
  font-size: 9.5px;
  color: #94A3B8;
  margin-top: 2px;
  margin-bottom: 3px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.hero-book-price {
  font-size: 11px;
  font-weight: 800;
  color: #FBBF24;
  margin-top: 3px;
}

/* Dimmed State When Another Book is Spotlit: Sharp, No Blur! */
.hero-books-grid-video.spotlight-mode .hero-video-book-card:not(.is-spotlit) {
  opacity: 0.42 !important;
  transform: scale(0.96) !important;
  filter: none !important;
}

/* Active Spotlit Book State (Pops Forward + Shows Bottom Title/Price Info Drawer) */
.hero-books-grid-video.spotlight-mode .hero-video-book-card.is-spotlit {
  opacity: 1 !important;
  transform: scale(1.14) translateY(-6px) !important;
  filter: none !important;
  z-index: 40 !important;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8), 0 0 20px rgba(245, 158, 11, 0.35) !important;
  outline: 2px solid rgba(251, 191, 36, 0.85) !important;
}

.hero-books-grid-video.spotlight-mode .hero-video-book-card.is-spotlit .hero-book-meta {
  transform: translateY(0) !important;
  opacity: 1 !important;
}

/* Diya Teardrop Flame Flickering */
.diya-flame {
  transform-origin: center bottom;
  animation: flameFlicker 1.8s ease-in-out infinite alternate;
}
.diya-flame-halo {
  transform-origin: center center;
  animation: haloPulse 2.2s ease-in-out infinite alternate;
}
@keyframes flameFlicker {
  0% { transform: scale(1) rotate(-1deg); }
  50% { transform: scale(1.08, 0.95) rotate(2deg); }
  100% { transform: scale(0.96, 1.05) rotate(-2deg); }
}
@keyframes haloPulse {
  0% { opacity: 0.6; transform: scale(0.95); }
  100% { opacity: 0.85; transform: scale(1.1); }
}
@keyframes bulbTwinkle {
  0% { opacity: 0.55; }
  100% { opacity: 1; }
}

/* =========================================================================
   KINETIC MARQUEE RIBBON & STATS BAR
   ========================================================================= */
.marquee-ribbon {
  background: #0A1128;
  border-top: 1px solid #D99B26;
  border-bottom: 1px solid #D99B26;
  overflow: hidden;
  white-space: nowrap;
  padding: 12px 0;
}
.marquee-track {
  display: inline-block;
  white-space: nowrap;
  animation: marqueeScroll 36s linear infinite;
}
.marquee-item {
  display: inline-flex;
  align-items: center;
  gap: 16px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #FEF3C7;
  text-transform: uppercase;
  padding: 0 24px;
}
.marquee-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #D99B26;
}
@keyframes marqueeScroll {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

.stats-bar {
  background: #FFFFFF;
  border-bottom: 1px solid #E2E8F0;
  padding: 24px 0;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
.stat-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 8px 16px;
  border: none !important;
  border-right: none !important;
  border-left: none !important;
}
.stat-card:last-child {
  border: none !important;
}
.stat-number, [class*="stat-number"], [class*="stat-num"], .stat-card, [class*="counter"] {
  font-size: 28px;
  font-weight: 800;
  color: #0F172A;
  line-height: 1.1;
  border-right: none !important;
  border-left: none !important;
  border: none !important;
  caret-color: transparent !important;
  user-select: none !important;
  font-variant-numeric: tabular-nums lining-nums !important;
  font-feature-settings: "lnum" 1, "tnum" 1 !important;
}
.stat-number::after, .stat-number::before,
.stat-card::after, .stat-card::before,
[class*="stat"]::after, [class*="stat"]::before {
  display: none !important;
  content: none !important;
}
.stat-label {
  font-size: 12.5px;
  color: #64748B;
  font-weight: 600;
  margin-top: 4px;
}

/* =========================================================================
   SECTION 1: THE 3D CURATOR'S PODIUM (#bestsellers-podium)
   ========================================================================= */
.podium-stage-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
}
@media (max-width: 992px) {
  .podium-stage-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

.podium-left-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  min-height: 460px;
  justify-content: center;
}
.podium-turntable-track {
  position: relative;
  width: 100%;
  max-width: 520px;
  height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1800px;
}

/* Flanking Books */
.flank-book {
  position: absolute;
  width: 170px;
  height: 250px;
  border-radius: 4px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
  cursor: pointer;
  transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}
.flank-book img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.flank-left-2 {
  transform: translateX(-180px) scale(0.72) rotateY(28deg);
  opacity: 0.65;
  z-index: 10;
}
.flank-left-1 {
  transform: translateX(-95px) scale(0.85) rotateY(18deg);
  opacity: 0.85;
  z-index: 15;
}
.flank-right-1 {
  transform: translateX(95px) scale(0.85) rotateY(-18deg);
  opacity: 0.85;
  z-index: 15;
}
.flank-right-2 {
  transform: translateX(180px) scale(0.72) rotateY(-28deg);
  opacity: 0.65;
  z-index: 10;
}
.flank-book:hover {
  filter: brightness(1.06) !important;
  cursor: pointer !important;
}

/* Center 3D Book Hinge Structure */
.podium-3d-book {
  position: relative;
  width: 230px;
  height: 340px;
  perspective: 1800px;
  transform-style: preserve-3d;
  cursor: pointer;
  z-index: 30;
}

/* Stationary Back Inside Page */
.podium-page-inside,
.podium-inside-page {
  position: absolute !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background: #FFFDF9 !important;
  border: 1px solid #CBD5E1 !important;
  border-right: 6px solid #CBD5E1 !important;
  border-radius: 2px 6px 6px 2px !important;
  padding: 16px 14px !important;
  box-sizing: border-box !important;
  overflow: hidden !important; /* NEVER ALLOW TEXT TO SPILL OUTSIDE THE BOOK! */
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.15) !important;
  z-index: 10 !important;
}
.podium-page-eyebrow {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: #B45309;
  font-weight: 700;
  margin-bottom: 6px;
}
.podium-page-title {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 18px;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.25;
  margin-bottom: 6px;
}
.podium-page-inside p,
.podium-inside-page p,
#podium-page-excerpt,
.podium-page-excerpt {
  font-size: 12px !important;
  line-height: 1.5 !important;
  color: #334155 !important;
  margin: 6px 0 !important;
  display: -webkit-box !important;
  -webkit-line-clamp: 7 !important;
  -webkit-box-orient: vertical !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}
.podium-page-footer {
  margin-top: auto;
  border-top: 1px solid #E2D9C5;
  padding-top: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 10.5px;
  color: #78716C;
}

/* Front Layer: Hinged Cover (3D Hinge Physics -135deg) */
.podium-hinged-cover {
  position: absolute !important;
  inset: 0 !important;
  transform-origin: left center !important;
  -webkit-transform-origin: left center !important;
  transform-style: preserve-3d !important;
  -webkit-transform-style: preserve-3d !important;
  transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1) !important;
  backface-visibility: hidden !important;
  -webkit-backface-visibility: hidden !important;
  border-radius: 4px !important;
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.35) !important;
  z-index: 30 !important;
}

.cover-front {
  position: absolute !important;
  inset: 0 !important;
  border-radius: 4px !important;
  backface-visibility: hidden !important;
  -webkit-backface-visibility: hidden !important;
  transform: translateZ(1px) !important;
  -webkit-transform: translateZ(1px) !important;
  z-index: 2 !important;
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
}

.cover-front img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  border-radius: 4px !important;
  display: block !important;
}

.cover-back {
  position: absolute !important;
  inset: 0 !important;
  border-radius: 4px !important;
  transform: rotateY(180deg) translateZ(1px) !important;
  -webkit-transform: rotateY(180deg) translateZ(1px) !important;
  backface-visibility: hidden !important;
  -webkit-backface-visibility: hidden !important;
  background: #1A1412 !important;
  border: 2px solid #D99B26 !important;
  color: #FEF3C7 !important;
  padding: 16px !important;
  z-index: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  box-sizing: border-box !important;
}
.cover-back-thumb {
  width: 48px;
  height: 72px;
  border: 1px solid #D99B26;
  border-radius: 2px;
  overflow: hidden;
  margin-bottom: 10px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.6);
}
.cover-back-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.cover-back-title {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 17px;
  font-weight: 700;
  color: #FEF3C7;
  line-height: 1.25;
  margin-bottom: 6px;
}
.cover-back-author {
  font-size: 11px;
  color: #FBBF24;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 10px;
}
.cover-back-tag {
  font-size: 9px;
  letter-spacing: 0.15em;
  color: #D97706;
  padding: 2px 10px;
  border: 1px solid rgba(217, 119, 6, 0.5);
  border-radius: 9999px;
  text-transform: uppercase;
}

/* Hover & Click Swing to -135deg */
#podium-active-book:hover .podium-cover-leaf,
.podium-center-book:hover .podium-cover-leaf,
#podium-3d-book:hover .podium-hinged-cover,
.podium-3d-book:hover .podium-hinged-cover,
.podium-3d-book:hover .podium-cover-leaf,
.podium-3d-book.is-open .podium-hinged-cover,
.podium-3d-book.is-open .podium-cover-leaf {
  transform: rotateY(-135deg) !important;
  -webkit-transform: rotateY(-135deg) !important;
}

/* Controls */
.podium-nav-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-top: 24px;
}
.podium-arrow-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid #CBD5E1;
  background: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #334155;
  cursor: pointer;
  transition: all 0.2s;
}
.podium-arrow-btn:hover {
  background: #FEF3C7;
  border-color: #F59E0B;
  color: #B45309;
}
.podium-dots-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}
.podium-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #CBD5E1;
  cursor: pointer;
  transition: all 0.25s;
}
.podium-dot.active {
  width: 28px;
  border-radius: 9999px;
  background: #D99B26;
}

/* Right Details Panel */
.podium-right-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 36px 32px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}
.podium-cat-badge {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #B45309;
  background: #FEF3C7;
  padding: 4px 12px;
  border-radius: 6px;
  display: inline-block;
  margin-bottom: 12px;
}
.podium-stock-str {
  font-size: 12.5px;
  font-weight: 700;
  color: #047857;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8px;
}
.podium-book-heading {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 30px;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.25;
  margin-bottom: 8px;
}
.podium-author-row {
  font-size: 15px;
  color: #475569;
  margin-bottom: 12px;
}
.podium-rating-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 18px;
  padding-bottom: 16px;
  border-bottom: 1px solid #F1F5F9;
}
.stars-group {
  display: flex;
  color: #F59E0B;
}
.podium-quote-box {
  background: #FFFBEB;
  border-left: 4px solid #D99B26;
  border-radius: 0 8px 8px 0;
  padding: 14px 18px;
  font-size: 13.5px;
  font-style: italic;
  color: #334155;
  line-height: 1.6;
  margin-bottom: 20px;
}
.podium-specs-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  background: #F8FAFC;
  padding: 14px;
  border-radius: 8px;
  border: 1px solid #E2E8F0;
  font-size: 12.5px;
  margin-bottom: 24px;
}
.podium-price-row {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 24px;
}
.podium-curr-price {
  font-size: 32px;
  font-weight: 800;
  color: #0F172A;
}
.podium-old-price {
  font-size: 16px;
  text-decoration: line-through;
  color: #94A3B8;
}
.discount-pill {
  background: #ECFDF5;
  color: #047857;
  font-size: 12px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
}
.podium-actions-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}
@media (max-width: 600px) {
  .podium-actions-row {
    grid-template-columns: 1fr;
  }
}
.btn-overview {
  background: #FEF3C7;
  border: 1px solid #F59E0B;
  color: #0F172A;
  font-weight: 700;
  font-size: 13px;
  padding: 12px 14px;
  border-radius: 8px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.2s;
}
.btn-overview:hover {
  background: #FDE68A;
}
.btn-add-cart {
  background: #0F172A;
  color: #FFFFFF;
  border: none;
  font-weight: 700;
  font-size: 13px;
  padding: 12px 14px;
  border-radius: 8px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: background 0.2s;
}
.btn-add-cart:hover {
  background: #1E293B;
}
.btn-wa-order {
  background: #25D366;
  color: #FFFFFF;
  text-decoration: none;
  font-weight: 700;
  font-size: 13px;
  padding: 12px 14px;
  border-radius: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: background 0.2s;
}
.btn-wa-order:hover {
  background: #1EBE5D;
}

/* =========================================================================
   SECTION 2: MEHFIL-E-REKHTA DARK POETRY LOUNGE (#mehfil-rekhta)
   ========================================================================= */
.rekhta-section {
  background: linear-gradient(180deg, #0A1128 0%, #171124 50%, #0A1128 100%);
  color: #F8FAFC;
  position: relative;
  overflow: hidden;
}
.rekhta-watermark {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 88px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.025);
  white-space: nowrap;
  pointer-events: none !important;
  user-select: none !important;
  z-index: 0;
}

.poet-pills-row {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 32px;
  position: relative;
  z-index: 30;
}
.poet-pill {
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #CBD5E1;
  padding: 8px 18px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.poet-pill:hover, .poet-pill.active {
  background: #D99B26;
  border-color: #D99B26;
  color: #0A1128;
  font-weight: 700;
}

.couplet-card {
  max-width: 820px;
  margin: 0 auto 48px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(217, 155, 38, 0.35);
  border-radius: 16px;
  padding: 36px 32px;
  text-align: center;
  position: relative;
  z-index: 30;
  backdrop-filter: blur(8px);
}
.couplet-urdu {
  font-size: 24px;
  line-height: 1.8;
  color: #FEF3C7;
  direction: rtl;
  margin-bottom: 16px;
  font-family: 'Merriweather', serif;
}
.couplet-hindi {
  font-size: 20px;
  line-height: 1.7;
  color: #FFFFFF;
  font-weight: 600;
  margin-bottom: 14px;
}
.couplet-eng {
  font-size: 14px;
  font-style: italic;
  color: #94A3B8;
  line-height: 1.6;
  margin-bottom: 18px;
}
.couplet-attr {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #D99B26;
  text-transform: uppercase;
}
.couplet-controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 24px;
  padding-top: 18px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
.couplet-nav-btn {
  background: none;
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #CBD5E1;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}
.couplet-nav-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #FFFFFF;
}
.ghazal-drawer-toggle {
  background: none;
  border: none;
  color: #D99B26;
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: underline;
}
.ghazal-full-drawer {
  display: none;
  margin-top: 20px;
  padding: 20px;
  background: rgba(0, 0, 0, 0.35);
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.8;
  color: #E2E8F0;
  white-space: pre-line;
  text-align: left;
}
.ghazal-full-drawer.is-open {
  display: block;
}

/* 5 Rekhta Books Cards Grid */
.rekhta-books-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
  position: relative;
  z-index: 30;
}
@media (max-width: 1024px) {
  .rekhta-books-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 640px) {
  .rekhta-books-grid {
    grid-template-columns: repeat(1, 1fr);
  }
}
.rekhta-book-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
}
.rekhta-book-card.dimmed {
  opacity: 0.35 !important;
  transform: scale(0.97) !important;
  filter: grayscale(40%) !important;
}
.rekhta-book-card.highlighted {
  opacity: 1 !important;
  border-color: #D99B26 !important;
  box-shadow: 0 0 22px rgba(217, 155, 38, 0.45) !important;
  transform: translateY(-4px) scale(1.02) !important;
}
.rekhta-book-card:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(217, 155, 38, 0.5);
  transform: translateY(-4px);
}
.rekhta-cover-wrap {
  width: 100%;
  aspect-ratio: 2 / 3 !important;
  height: auto !important;
  background: #0D1629;
  border-radius: 6px;
  overflow: hidden;
  margin-bottom: 12px;
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.4);
}
.rekhta-cover-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.rekhta-card-title {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 15px;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 4px;
  line-height: 1.3;
}
.rekhta-card-author {
  font-size: 12px;
  color: #94A3B8;
  margin-bottom: 8px;
}
.rekhta-card-desc {
  font-size: 11.5px;
  color: #CBD5E1;
  line-height: 1.5;
  margin-bottom: 12px;
  flex: 1;
}
.rekhta-card-price-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin-bottom: 12px;
}
.rekhta-curr-price {
  font-size: 18px;
  font-weight: 800;
  color: #FEF3C7;
}
.rekhta-card-actions {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

/* =========================================================================
   SECTION 3: BUNDLE UNBOXING SHOWCASE (#bundles-section)
   ========================================================================= */
.bundles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}
@media (max-width: 992px) {
  .bundles-grid {
    grid-template-columns: 1fr;
  }
}
.bundle-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  transition: all 0.3s;
}
.bundle-card:hover {
  box-shadow: 0 12px 32px rgba(217, 155, 38, 0.15);
  border-color: #F59E0B;
}

/* Pure CSS Fan-Out Container */
.bundle-fan-stage {
  height: 220px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  perspective: 800px;
}
.bundle-cover-layer {
  position: absolute;
  width: 120px;
  height: 175px;
  border-radius: 4px;
  box-shadow: -4px 8px 18px rgba(0, 0, 0, 0.25);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}
.bundle-cover-layer img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.bundle-cover-layer.layer-left {
  transform: translateX(-16px) rotate(-4deg);
  z-index: 10;
}
.bundle-cover-layer.layer-center {
  transform: translateX(0) rotate(0deg);
  z-index: 20;
}
.bundle-cover-layer.layer-right {
  transform: translateX(16px) rotate(4deg);
  z-index: 15;
}

/* Playing-Card Fan-Out on Hover */
.bundle-card:hover .bundle-cover-layer.layer-left {
  transform: translateX(-55px) rotate(-14deg) scale(1.04);
}
.bundle-card:hover .bundle-cover-layer.layer-center {
  transform: translateX(0) translateY(-10px) scale(1.08);
  z-index: 30;
}
.bundle-card:hover .bundle-cover-layer.layer-right {
  transform: translateX(55px) rotate(14deg) scale(1.04);
}

.bundle-badge {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #B45309;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.bundle-title {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 20px;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 4px;
  line-height: 1.3;
}
.bundle-author {
  font-size: 13px;
  color: #64748B;
  margin-bottom: 16px;
}
.bundle-checklist {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 20px;
  flex: 1;
}
.bundle-checklist li {
  font-size: 12.5px;
  color: #334155;
  display: flex;
  align-items: center;
  gap: 8px;
}
.bundle-price-row {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-bottom: 16px;
}

/* =========================================================================
   SECTION 4: INDIAN VOICES & CONTEMPORARY HINDI FICTION
   ========================================================================= */
.contemporary-grid {
  display: grid;
  grid-template-columns: 5fr 7fr;
  gap: 32px;
}
@media (max-width: 992px) {
  .contemporary-grid {
    grid-template-columns: 1fr;
  }
}
.feat-book-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 32px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}
.feat-cover-wrap {
  width: 100%;
  aspect-ratio: 2 / 3 !important;
  height: auto !important;
  max-height: 360px !important;
  max-width: 240px !important;
  margin: 0 auto 20px auto !important;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 20px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}
.feat-cover-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.mini-grid-2x2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}
@media (max-width: 600px) {
  .mini-grid-2x2 {
    grid-template-columns: 1fr;
  }
}
.mini-book-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  height: auto;
  align-self: start;
}
.mini-cover-row {
  display: flex;
  gap: 14px;
}
.mini-book-thumb {
  width: 96px;
  height: 140px;
  border-radius: 4px;
  overflow: hidden;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}
.mini-book-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.mini-details-col {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.mini-book-title {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 15px;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.3;
}
.mini-book-author {
  font-size: 12px;
  color: #64748B;
}

/* =========================================================================
   SECTION 5: LAW, JUDICIARY & SAHITYA REFERENCE ARCHIVE (#law-academic-vault)
   ========================================================================= */
.vault-layout {
  display: grid;
  grid-template-columns: 4fr 8fr;
  gap: 32px;
}
@media (max-width: 992px) {
  .vault-layout {
    grid-template-columns: 1fr;
  }
}
.vault-nav-col {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.vault-tab-btn {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 10px;
  padding: 14px 18px;
  font-size: 13.5px;
  font-weight: 600;
  color: #334155;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 0.2s;
  text-align: left;
}
.vault-tab-btn:hover, .vault-tab-btn.active {
  background: #0F172A;
  border-color: #0F172A;
  color: #FFFFFF;
}
.vault-tab-btn.active i {
  color: #D99B26;
}
.vault-concierge-card {
  margin-top: 16px;
  background: #FFFBEB;
  border: 1px solid #FDE68A;
  border-radius: 12px;
  padding: 20px;
}

.vault-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}
@media (max-width: 900px) {
  .vault-layout {
    display: flex !important;
    flex-direction: column !important;
    gap: 16px !important;
    width: 100% !important;
  }
  .vault-nav-col {
    display: flex !important;
    flex-direction: row !important;
    overflow-x: auto !important;
    flex-wrap: nowrap !important;
    gap: 8px !important;
    width: 100% !important;
    padding: 2px 2px 8px !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
  }
  .vault-nav-col::-webkit-scrollbar {
    display: none !important;
  }
  .vault-tab-btn {
    flex-shrink: 0 !important;
    padding: 8px 14px !important;
    font-size: 12px !important;
    border-radius: 9999px !important;
    white-space: nowrap !important;
  }
  .vault-tab-btn i:last-child {
    display: none !important;
  }
  .vault-concierge-card {
    display: none !important;
  }
  .vault-cards-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 12px !important;
    width: 100% !important;
  }
  .vault-card {
    padding: 12px 10px !important;
  }
}
.vault-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
}
.vault-card-thumb {
  width: 100%;
  aspect-ratio: 2 / 3 !important;
  height: auto !important;
  background: #F8FAFC;
  border-radius: 6px;
  overflow: hidden;
  margin-bottom: 12px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
}
.vault-card-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* =========================================================================
   SECTION 6: PAN-INDIA FILTERABLE CATALOG ARCHIVE (#shop-all-catalog)
   ========================================================================= */
.catalog-filter-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 32px;
}
.cat-pills-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}
.cat-pill {
  background: #FFFFFF;
  border: 1px solid #CBD5E1;
  color: #334155;
  padding: 7px 16px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.cat-pill:hover, .cat-pill.active {
  background: #0F172A;
  border-color: #0F172A;
  color: #FFFFFF;
}
.cat-search-box {
  display: flex;
  align-items: center;
  background: #FFFFFF;
  border: 1px solid #CBD5E1;
  border-radius: 8px;
  padding: 6px 14px;
  width: 280px;
}
.cat-search-box input {
  border: none;
  outline: none;
  font-size: 13px;
  color: #0F172A;
  width: 100%;
  padding-left: 8px;
}

.catalog-cards-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 1024px) {
  .catalog-cards-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 768px) {
  .catalog-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 480px) {
  .catalog-cards-grid {
    grid-template-columns: 1fr;
  }
}

.catalog-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  transition: all 0.25s;
}
.catalog-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
  border-color: #CBD5E1;
}
.catalog-thumb {
  width: 100%;
  aspect-ratio: 2 / 3 !important;
  height: auto !important;
  background: #F8FAFC;
  border-radius: 6px;
  overflow: hidden;
  margin-bottom: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
.catalog-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* =========================================================================
   TRUST STRIP & HERITAGE
   ========================================================================= */
.trust-features-grid, .trust-strip-grid, .features-grid, footer + section {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
  padding: 32px 16px !important;
  margin: 0 auto !important;
  max-width: 1200px !important;
}
@media (max-width: 991px) {
  .trust-features-grid, .trust-strip-grid, .features-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
  }
}
@media (max-width: 640px) {
  .trust-features-grid, .trust-strip-grid, .features-grid {
    grid-template-columns: 1fr !important;
  }
}
.whatsapp-float-btn, .floating-wa-btn, .floating-whatsapp-btn {
  z-index: 99 !important;
  bottom: 20px !important;
  right: 20px !important;
}
.trust-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
}
.trust-card-icon {
  width: 42px;
  height: 42px;
  border-radius: 8px;
  background: #FEF3C7;
  color: #B45309;
  display: flex;
  align-items: center;
  justify-content: center;
}

.heritage-grid {
  display: grid;
  grid-template-columns: 7fr 5fr;
  gap: 40px;
  align-items: center;
}
@media (max-width: 992px) {
  .heritage-grid {
    grid-template-columns: 1fr;
  }
}
.heritage-hq-card {
  background: #0A1128;
  color: #FFFFFF;
  border: 2px solid #D99B26;
  border-radius: 16px;
  padding: 36px 32px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
}

/* =========================================================================
   DARK NAVY FOOTER & CIRCULAR WHATSAPP BUTTON
   ========================================================================= */
.site-footer {
  background: #0A1128;
  color: #CBD5E1;
  border-top: 3px solid #D99B26;
  padding: 64px 0 32px !important;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.3fr;
  gap: 40px;
  margin-bottom: 48px;
  align-items: start;
}
@media (max-width: 992px) {
  .footer-grid {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 600px) {
  .footer-grid {
    grid-template-columns: 1fr;
  }
}
.footer-col h4 {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 15px;
  font-weight: 700;
  color: #FFFFFF;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  border-bottom: 2px solid #D99B26;
  display: inline-block;
  padding-bottom: 4px;
  margin-bottom: 18px;
}
.footer-links-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.footer-links-list a {
  color: #94A3B8;
  text-decoration: none;
  font-size: 13.5px;
  transition: color 0.2s;
}
.footer-links-list a:hover {
  color: #FEF3C7;
}

.footer-bottom-bar {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12.5px;
  color: #64748B;
}
@media (max-width: 768px) {
  .footer-bottom-bar {
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }
}

/* Floating Circular WhatsApp Button */
.wa-tooltip {
  display: none !important;
}
@media (min-width: 901px) {
  .floating-wa-btn:hover .wa-tooltip,
  .whatsapp-float-btn:hover .wa-tooltip,
  .floating-whatsapp-btn:hover .wa-tooltip {
    display: block !important;
    position: absolute !important;
    right: 64px !important;
    background: #0F172A !important;
    color: #FFFFFF !important;
    padding: 6px 12px !important;
    border-radius: 6px !important;
    font-size: 12px !important;
    white-space: nowrap !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
    pointer-events: none !important;
  }
}
.floating-wa-btn,
.whatsapp-float-btn,
.floating-whatsapp-btn {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: #25D366;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 18px rgba(37, 211, 102, 0.45);
  z-index: 99999;
  text-decoration: none;
  transition: all 0.25s;
  overflow: hidden !important;
}
@media (max-width: 900px) {
  .site-footer {
    padding: 40px 16px 88px !important;
  }
  .footer-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 28px !important;
  }
  .floating-wa-btn,
  .whatsapp-float-btn,
  .floating-whatsapp-btn {
    bottom: 18px !important;
    right: 18px !important;
    width: 48px !important;
    height: 48px !important;
    overflow: hidden !important;
  }
  .floating-wa-btn .wa-tooltip,
  .whatsapp-float-btn .wa-tooltip,
  .floating-whatsapp-btn .wa-tooltip {
    display: none !important;
  }
}
.floating-wa-btn:hover {
  transform: scale(1.08);
  background: #1EBE5D;
}

/* =========================================================================
   INDIGO OVERVIEW MODAL (SOLID WHITE 2-COLUMN EDITORIAL CARD)
   ========================================================================= */
#indigo-overview-modal,
#overviewModalOverlay {
  position: fixed !important;
  inset: 0 !important;
  z-index: 999999 !important;
  background: rgba(9, 19, 44, 0.82) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  display: none !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 20px !important;
  box-sizing: border-box !important;
}

#indigo-overview-modal.is-active,
#overviewModalOverlay.is-active {
  display: flex !important;
}

#indigo-overview-modal .overview-card-box,
#overviewModalOverlay .overview-card-box,
.overview-card-box {
  position: relative !important;
  background: #FFFFFF !important;
  color: #09132C !important;
  width: 100% !important;
  max-width: 760px !important;
  max-height: 88vh !important;
  overflow-y: auto !important;
  border-radius: 18px !important;
  border: 1px solid #E2E8F0 !important;
  padding: 32px !important;
  box-shadow: 0 28px 70px rgba(0, 0, 0, 0.55) !important;
  display: grid !important;
  grid-template-columns: 240px 1fr !important;
  gap: 28px !important;
  align-items: start !important;
  box-sizing: border-box !important;
}

@media (max-width: 680px) {
  #indigo-overview-modal .overview-card-box,
  #overviewModalOverlay .overview-card-box,
  .overview-card-box {
    grid-template-columns: 1fr !important;
    padding: 20px !important;
  }
}

.overview-modal-box {
  width: 90% !important;
  max-width: 440px !important;
  max-height: 85vh !important;
  overflow-y: auto !important;
  padding: 20px !important;
  margin: auto !important;
  border-radius: 12px !important;
  box-sizing: border-box !important;
  background: #FFFFFF !important;
  position: relative !important;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25) !important;
  border: 1px solid #E2E8F0 !important;
}
.modal-top-grid {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 16px;
  margin-bottom: 16px;
}
.modal-cover-wrap {
  width: 110px;
  height: 162px;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 6px 18px rgba(0,0,0,0.15);
  flex-shrink: 0;
  aspect-ratio: 2 / 3;
}
.modal-meta-col {
  display: flex;
  flex-direction: column;
  min-width: 0;
}
.modal-close-btn {
  position: absolute;
  top: 18px;
  right: 18px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid #E2E8F0;
  background: #F8FAFC;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #64748B;
  transition: all 0.2s;
}
.modal-close-btn:hover {
  background: #E2E8F0;
  color: #0F172A;
}

/* Slide-Over Cart Drawer */
.cart-drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(4px);
  z-index: 100;
  display: none;
  justify-content: flex-end;
}
.cart-drawer-overlay.is-open {
  display: flex;
}
.cart-drawer-panel {
  width: 440px;
  max-width: 100%;
  height: 100%;
  background: #FFFFFF;
  display: flex;
  flex-direction: column;
  box-shadow: -8px 0 32px rgba(0, 0, 0, 0.25);
  animation: slideDrawer 0.3s cubic-bezier(0.16, 1, 0.3, 1) both;
}
@keyframes slideDrawer {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
.cart-header {
  padding: 20px 24px;
  border-bottom: 1px solid #E2E8F0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.cart-items-list {
  flex: 1;
  overflow-y: auto;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.cart-footer {
  padding: 20px 24px;
  border-top: 1px solid #E2E8F0;
  background: #FAF8F5;
}

/* =========================================================================
   MANDATORY MOBILE RESPONSIVE ENGINE (320px - 991px)
   ========================================================================= */
@media (max-width: 991px) {
  /* ABSOLUTE HORIZONTAL OVERFLOW & RIGHT MARGIN ELIMINATION */
  section, 
  footer {
    max-width: 100% !important;
    overflow-x: hidden !important;
  }

  /* Ensure Hero Container & Video Grid Fit 360px Screen Perfectly */
  .ivh-container, 
  .hero-inner-container,
  .hero-main-grid {
    width: 100% !important;
    max-width: 100% !important;
    padding-left: 16px !important;
    padding-right: 16px !important;
    margin: 0 !important;
    box-sizing: border-box !important;
  }

  .ivh-right,
  .hero-stage-col {
    width: 100% !important;
    overflow: hidden !important;
    display: flex !important;
    justify-content: center !important;
  }

  .ivh-rangoli-anchor,
  .hero-rangoli-wrapper,
  .hero-wheel-wrap {
    max-width: 100% !important;
    overflow: hidden !important;
  }

  /* Exceptions for Horizontally Scrollable Elements */
  .nav-links-center, 
  .nav-links-wrap,
  header .nav-links-wrap,
  .poet-pills-row,
  .cat-pills-row {
    overflow-x: auto !important;
  }

  /* MOBILE NAVBAR LAYOUT (Clean 2-Row Contained Header on Phones <= 991px) */
  header,
  .site-header,
  .site-navbar,
  .main-navbar {
    position: sticky !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    background-color: #FAF8F5 !important;
    border-bottom: 1px solid rgba(15, 23, 42, 0.12) !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06) !important;
    z-index: 99999 !important;
    height: auto !important;
    min-height: unset !important;
    overflow: visible !important;
  }

  header > div,
  header nav,
  .navbar-container,
  .navbar-inner {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    justify-content: space-between !important;
    height: auto !important;
    min-height: unset !important;
    padding: 8px 12px 0 12px !important;
    gap: 0 !important;
    background-color: #FAF8F5 !important;
    box-sizing: border-box !important;
    width: 100% !important;
    overflow: visible !important;
  }

  /* ROW 1 LEFT: Official INDIGO BOOKS Blue Emblem + Wordmark (Always 100% Visible!) */
  .brand-logo-wrap,
  .brand-link,
  header a:first-of-type,
  .navbar-container > div:first-child {
    order: 1 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    flex-shrink: 0 !important;
    margin: 0 !important;
    text-decoration: none !important;
  }

  /* Scale Logo & Text Cleanly for 360px Screen so Row 1 Fits Logo + Buttons Together */
  .brand-logo-wrap svg,
  .brand-logo-wrap img,
  .brand-link svg {
    width: 26px !important;
    height: 26px !important;
    min-width: 26px !important;
    max-width: 26px !important;
    flex-shrink: 0 !important;
    display: inline-block !important;
  }
  .brand-logo-wrap span,
  .brand-wordmark {
    font-size: 13px !important;
    letter-spacing: 0.06em !important;
    line-height: 1.1 !important;
    color: #0F172A !important;
    white-space: nowrap !important;
  }
  .brand-submark {
    font-size: 7.5px !important;
    letter-spacing: 0.12em !important;
    margin-top: 1px !important;
  }

  /* ROW 1 RIGHT: Compact Sign In + Cart + WhatsApp Order Buttons */
  .nav-actions-right,
  .nav-actions,
  .navbar-container > div:last-child {
    order: 2 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 5px !important;
    margin-left: auto !important;
    flex-shrink: 0 !important;
  }

  .nav-actions-right button,
  .nav-actions-right a,
  .nav-actions button,
  .nav-actions a,
  .nav-signin-btn,
  .nav-cart-btn,
  .nav-whatsapp-btn {
    padding: 5px 8px !important;
    font-size: 11px !important;
    height: 30px !important;
    line-height: 1 !important;
    white-space: nowrap !important;
    border-radius: 6px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
  }

  /* Hide India badge and Cart price on mobile to prevent overflow */
  .india-centric-badge,
  .india-badge,
  [class*="india-centric"],
  .nav-cart-price-wrap {
    display: none !important;
  }
  @media (max-width: 360px) {
    .nav-signin-text {
      display: none !important;
    }
  }

  /* ROW 2: Horizontal Scrollable Nav Links INSIDE the Cream Navbar Background */
  .nav-links-center,
  .nav-links-wrap,
  header nav ul,
  .navbar-links {
    order: 3 !important;
    width: 100% !important;
    flex-basis: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    white-space: nowrap !important;
    padding: 8px 4px 8px 4px !important;
    margin: 4px 0 0 0 !important;
    border-top: 1px solid rgba(15, 23, 42, 0.08) !important;
    background-color: #FAF8F5 !important;
    color: #0F172A !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    list-style: none !important;
    box-sizing: border-box !important;
  }
  .nav-links-center::-webkit-scrollbar,
  .nav-links-wrap::-webkit-scrollbar {
    display: none !important;
  }

  .nav-links-center a,
  .nav-links-center button,
  .nav-links-wrap a,
  .nav-links-wrap button,
  .nav-link-btn {
    font-size: 12px !important;
    font-weight: 600 !important;
    color: #1E293B !important;
    flex-shrink: 0 !important;
    text-decoration: none !important;
    padding: 3px 5px !important;
    background: transparent !important;
    border: none !important;
  }

  /* Stack Hero Section Cleanly on Mobile (320px - 768px) */
  .indigo-hero-banner, .hero-section {
    min-height: auto !important;
    padding: 24px 0 36px 0 !important;
    overflow: hidden !important;
  }
  .hero-inner-container, .hero-main-grid {
    grid-template-columns: 1fr !important;
    padding: 14px 16px !important;
    gap: 24px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .hero-left-col {
    width: 100% !important;
    max-width: 100% !important;
    text-align: left !important;
  }
  .hero-main-title, .indigo-hero-banner h1, .hero-left-col h1 {
    font-size: 32px !important;
    line-height: 1.15 !important;
    word-wrap: break-word !important;
    max-width: 100% !important;
    margin-bottom: 12px !important;
  }
  .hero-subtext, .hero-left-col p {
    font-size: 14px !important;
    max-width: 100% !important;
    margin-bottom: 16px !important;
    line-height: 1.5 !important;
  }
  .hero-search-box, .hero-search-wrap {
    width: 100% !important;
    max-width: 100% !important;
    height: 44px !important;
    box-sizing: border-box !important;
    padding: 0 16px !important;
    margin-bottom: 16px !important;
  }
  .hero-search-wrap input {
    font-size: 13px !important;
  }
  .hero-cta-row {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 10px !important;
    width: 100% !important;
  }
  .hero-btn-primary, .hero-btn-whatsapp, .hero-shop-btn, .hero-wa-cod-btn {
    flex: 1 1 auto !important;
    text-align: center !important;
    justify-content: center !important;
    padding: 10px 14px !important;
    font-size: 13px !important;
  }

  /* Scale Down Right Stage & 3x2 Book Grid to Fit Inside 320px-360px Mobile Screen */
  .hero-right-stage, .hero-stage-col {
    height: auto !important;
    min-height: 310px !important;
    width: 100% !important;
    padding: 10px 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: visible !important;
  }
  .hero-wheel-wrap, .hero-rangoli-wrapper {
    width: 290px !important;
    height: 290px !important;
    left: 50% !important;
    top: 50% !important;
    transform: translate(-50%, -50%) !important;
    z-index: 5 !important;
  }
  .hero-wheel-svg, .hero-rangoli-svg {
    width: 290px !important;
    height: 290px !important;
  }
  .hero-books-grid-video {
    grid-template-columns: repeat(3, 92px) !important;
    grid-template-rows: repeat(2, 136px) !important;
    gap: 10px !important;
    width: 100% !important;
    justify-content: center !important;
    z-index: 25 !important;
  }
  .hero-video-book-card {
    width: 92px !important;
    height: 136px !important;
  }
  .hero-book-meta {
    padding: 5px 6px !important;
  }
  .hero-book-title {
    font-size: 9px !important;
  }
  .hero-book-author {
    font-size: 8px !important;
    margin-top: 1px !important;
  }
  .hero-book-price {
    font-size: 9px !important;
    margin-top: 1px !important;
  }
  .hero-diyas-cluster, .hero-diyas-svg {
    bottom: -10px !important;
    right: 4px !important;
    transform: scale(0.7) !important;
    transform-origin: bottom right !important;
  }

  /* Stack Lower Sections Cleanly on Mobile */
  .indigo-footer-grid,
  .footer-grid,
  [class*="grid-cols-"] {
    grid-template-columns: 1fr !important;
  }
  .site-container {
    padding-left: 14px !important;
    padding-right: 14px !important;
    max-width: 100vw !important;
  }
  .catalog-grid, .rekhta-books-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 10px !important;
  }
  .stats-bar {
    flex-wrap: wrap !important;
    gap: 14px !important;
    padding: 14px !important;
  }
  .stat-item {
    flex: 1 1 42% !important;
  }

  /* =========================================================================
     MOBILE UI CARD OVERHAUL (@media (max-width: 640px))
     ========================================================================= */

  /* 0. Refined Mobile Section & Card Spacing */
  section {
    padding: 36px 0 !important;
  }
  .editorial-header {
    margin-bottom: 20px !important;
    padding-bottom: 12px !important;
  }
  .bundles-grid {
    gap: 16px !important;
  }
  .bundle-card {
    padding: 16px !important;
  }
  .vault-cards-grid {
    gap: 12px !important;
  }
  .contemporary-grid {
    gap: 18px !important;
  }
  .trust-strip-grid {
    gap: 12px !important;
  }
  .trust-card {
    padding: 14px !important;
  }
  .heritage-grid {
    gap: 20px !important;
  }
  .heritage-hq-card {
    padding: 18px !important;
  }

  /* 1. Indian Voices & Fiction Cards: Sleek Side-by-Side Horizontal Book Card on Mobile */
  .fiction-grid-card,
  .archive-card {
    display: grid !important;
    grid-template-columns: 100px 1fr !important;
    gap: 14px !important;
    padding: 14px !important;
    align-items: center !important;
    height: auto !important;
  }

  /* Keep the Book Cover in True 2:3 Portrait Aspect Ratio on the Left (Zero Cropping!) */
  .vault-card .vault-card-thumb,
  .vault-card-thumb,
  .vault-book-card .book-cover-box,
  .fiction-grid-card .book-cover-box,
  .archive-card .book-cover-box,
  .vault-book-card > div:first-child,
  .feat-cover-wrap {
    width: 100px !important;
    height: 148px !important;
    aspect-ratio: 2 / 3 !important;
    border-radius: 6px !important;
    overflow: hidden !important;
    margin: 0 !important;
    flex-shrink: 0 !important;
    background: #F1F5F9 !important;
  }

  .vault-card img,
  .vault-card-thumb img,
  .vault-book-card img,
  .fiction-grid-card img,
  .archive-card img,
  .feat-cover-wrap img {
    width: 100% !important;
    height: 100% !important;
    aspect-ratio: 2 / 3 !important;
    object-fit: cover !important;
    object-position: center top !important;
    display: block !important;
  }

  .vault-card-body {
    display: flex !important;
    flex-direction: column !important;
    min-width: 0 !important;
    height: 100% !important;
    justify-content: center !important;
  }

  /* 2. Shop by Collection Catalog Grid: Clean 2-Column Mobile Grid (Like Amazon/Kindle App) */
  #shop-all-catalog .catalog-cards-grid,
  #shop-all-catalog .catalog-books-grid,
  .catalog-grid,
  .rekhta-books-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 12px !important;
    padding: 0 4px !important;
  }

  #shop-all-catalog .catalog-thumb,
  #shop-all-catalog .book-card-cover,
  .rekhta-books-grid .rekhta-cover-wrap,
  .rekhta-books-grid .book-card-cover {
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 2 / 3 !important;
    max-height: 220px !important;
  }

  #shop-all-catalog .catalog-thumb img,
  .rekhta-cover-wrap img {
    width: 100% !important;
    height: 100% !important;
    aspect-ratio: 2 / 3 !important;
    object-fit: cover !important;
    object-position: center top !important;
  }

  /* 3. Compact Mobile Action Buttons (Overview + Add) */
  .card-actions-row,
  .vault-card .buttons-row,
  .vault-card-body > div:last-child {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 8px !important;
    width: 100% !important;
    margin-top: 8px !important;
  }

  .card-actions-row button,
  .vault-card button,
  .vault-book-card button,
  .catalog-card button {
    padding: 8px 10px !important;
    font-size: 12px !important;
    white-space: nowrap !important;
    justify-content: center !important;
  }

  /* 4. Mobile Sticky Navbar & Floating WhatsApp Button Adjustment */
  .floating-whatsapp-btn {
    bottom: 16px !important;
    right: 16px !important;
    width: 46px !important;
    height: 46px !important;
    z-index: 90 !important;
  }

}



/* Stat Number & Counter Caret Removal */
.stat-number, [class*="stat"], [class*="counter"] {
  border-right: none !important;
  caret-color: transparent !important;
  user-select: none !important;
  font-variant-numeric: tabular-nums lining-nums !important;
}

/* Overview Modal Clean Padding & Mobile Fit */
.overview-modal-box {
  width: 90% !important;
  max-width: 480px !important;
  max-height: 85vh !important;
  overflow-y: auto !important;
  padding: 24px !important;
  margin: auto !important;
  box-sizing: border-box !important;
}

/* 3D Podium Hinged Cover & Faces */
.podium-hinged-cover {
  position: absolute !important;
  inset: 0 !important;
  transform-origin: left center !important;
  -webkit-transform-origin: left center !important;
  transform-style: preserve-3d !important;
  -webkit-transform-style: preserve-3d !important;
  transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1) !important;
  transform: rotateY(0deg) !important;
  -webkit-transform: rotateY(0deg) !important;
  border-radius: 4px !important;
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.35) !important;
  z-index: 30 !important;
}

.podium-3d-book.is-open .podium-hinged-cover {
  transform: rotateY(-135deg) !important;
  -webkit-transform: rotateY(-135deg) !important;
}

.cover-front {
  position: absolute !important;
  inset: 0 !important;
  border-radius: 4px !important;
  backface-visibility: hidden !important;
  -webkit-backface-visibility: hidden !important;
  transform: translateZ(1px) !important;
  -webkit-transform: translateZ(1px) !important;
  z-index: 2 !important;
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
  overflow: hidden !important;
}

.cover-front img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  border-radius: 4px !important;
  display: block !important;
}

.cover-back {
  position: absolute !important;
  inset: 0 !important;
  border-radius: 4px !important;
  transform: rotateY(180deg) translateZ(1px) !important;
  -webkit-transform: rotateY(180deg) translateZ(1px) !important;
  backface-visibility: hidden !important;
  -webkit-backface-visibility: hidden !important;
  background: #1A1412 !important;
  border: 2px solid #D99B26 !important;
  color: #FEF3C7 !important;
  padding: 16px !important;
  z-index: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  box-sizing: border-box !important;
}


/* =========================================================================
   KILL ALL VERTICAL BARS / CURSORS / PSEUDO-ELEMENTS IN THE STATS BAR
   ========================================================================= */
.stats-bar *,
.stats-grid *,
[class*="stat"] *,
[class*="stat"]::before,
[class*="stat"]::after,
.stats-bar *::before,
.stats-bar *::after {
  content: none !important;
  border-right: none !important;
  border-left: none !important;
  outline: none !important;
  box-shadow: none !important;
  overflow: visible !important;
  caret-color: transparent !important;
}

/* Clean Full-Width Container for Stats Bar & Balanced Grid */
.stats-bar {
  display: block !important;
  width: 100% !important;
  background: #FFFFFF !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding: 28px 0 !important;
  box-sizing: border-box !important;
}

.stats-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
  max-width: 1280px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  text-align: center !important;
  box-sizing: border-box !important;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    padding: 0 16px !important;
  }
}

.stat-item, .stat-card {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  width: 100% !important;
}

.stat-num, .stat-number {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 32px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.15 !important;
  margin-bottom: 6px !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.stat-label {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  line-height: 1.35 !important;
  text-align: center !important;
}

.stat-num {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 28px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.15 !important;
  margin-bottom: 6px !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

@media (min-width: 768px) {
  .stat-num {
    font-size: 36px !important;
  }
}

.stat-label {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  line-height: 1.35 !important;
  max-width: 220px !important;
  margin: 0 auto !important;
}

/* =========================================================================
   REMOVE BLANK WHITE SPACE ABOVE PODIUM ON MOBILE (360x800)
   ========================================================================= */
@media (max-width: 768px) {
  #bestsellers-podium {
    padding-top: 16px !important;
    padding-bottom: 32px !important;
    margin-top: 0 !important;
  }
  #bestsellers-podium .editorial-header {
    margin-bottom: 12px !important;
    padding-bottom: 8px !important;
  }
  .podium-left-stage {
    min-height: 320px !important;
    margin-top: 0 !important;
    padding: 0 !important;
  }
  .podium-turntable-track {
    height: 300px !important;
    max-width: 100% !important;
  }
  .podium-3d-book {
    width: 180px !important;
    height: 270px !important;
  }
  .flank-book {
    width: 135px !important;
    height: 200px !important;
  }
  .flank-left-1 { transform: translateX(-70px) scale(0.85) rotateY(18deg) !important; }
  .flank-right-1 { transform: translateX(70px) scale(0.85) rotateY(-18deg) !important; }
  .flank-left-2 { transform: translateX(-120px) scale(0.72) rotateY(28deg) !important; }
  .flank-right-2 { transform: translateX(120px) scale(0.72) rotateY(-28deg) !important; }
}

/* =========================================================================
   DEDICATED AMAZON-STYLE PRODUCT DETAILS PAGE (#single-product-page-view)
   ========================================================================= */
.store-view-section {
  width: 100%;
  min-height: auto;
}

#single-product-page-view {
  min-height: auto !important;
}

.product-page-wrapper {
  max-width: 1280px;
  margin: 0 auto;
  padding: 20px 20px 24px;
  box-sizing: border-box;
}

.product-breadcrumb-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0 16px;
  border-bottom: 1px solid #E2E8F0;
  margin-bottom: 20px;
  font-size: 13px;
  color: #64748B;
  flex-wrap: wrap;
  gap: 12px;
}

.breadcrumb-nav {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.breadcrumb-nav a {
  color: #0066B3;
  text-decoration: none;
  font-weight: 500;
}

.breadcrumb-nav a:hover {
  text-decoration: underline;
}

.breadcrumb-separator {
  color: #94A3B8;
  font-size: 12px;
}

.btn-back-to-store {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #F1F5F9;
  color: #0F172A;
  border: 1px solid #CBD5E1;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.btn-back-to-store:hover {
  background: #E2E8F0;
  border-color: #94A3B8;
}

/* Amazon-Style 3-Column Grid */
.product-pdp-grid {
  display: grid;
  grid-template-columns: 340px 1fr 310px;
  gap: 20px;
  align-items: start;
  width: 100%;
  max-width: 100%;
  margin-bottom: 20px;
  box-sizing: border-box;
}

@media (max-width: 1100px) {
  .product-pdp-grid {
    grid-template-columns: 300px 1fr 280px;
    gap: 16px;
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
  /* 2-COLUMN PRODUCT GRID ON MOBILE */
  .product-pdp-grid {
    display: grid !important;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr) !important;
    gap: 14px !important;
    align-items: start !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-left-col {
    grid-column: 1 / 2 !important;
    position: static !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    box-sizing: border-box !important;
  }
  .pdp-center-col {
    grid-column: 2 / 3 !important;
    position: static !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    box-sizing: border-box !important;
  }
  .pdp-right-col {
    grid-column: 1 / -1 !important;
    position: static !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    margin-top: 14px !important;
    padding: 0 !important;
    box-sizing: border-box !important;
  }
  .pdp-cover-card {
    max-width: 280px !important;
    margin: 0 auto !important;
    padding: 16px !important;
    border-radius: 12px !important;
    box-sizing: border-box !important;
  }
  .indigo-3d-book-stage {
    max-width: 240px !important;
    margin: 0 auto 14px !important;
  }
  .pdp-book-title {
    font-size: 22px !important;
    line-height: 1.3 !important;
    margin: 0 0 8px !important;
    word-break: break-word !important;
  }
  .pdp-author-pill-wrap {
    margin-bottom: 12px !important;
  }
  .pdp-price-wrap {
    margin-bottom: 12px !important;
  }
  .pdp-selling-price {
    font-size: 24px !important;
  }
  .pdp-variant-selector-box {
    padding: 12px !important;
    margin: 12px 0 !important;
  }
  .pdp-variant-buttons {
    gap: 8px !important;
  }
  .pdp-variant-btn {
    padding: 8px 12px !important;
    font-size: 12px !important;
  }
  .pdp-buy-box {
    width: 100% !important;
    max-width: 100% !important;
    padding: 16px !important;
    border-radius: 12px !important;
    box-sizing: border-box !important;
  }
  .pdp-bb-price {
    font-size: 24px !important;
    margin-bottom: 12px !important;
  }
  .pdp-pincode-checker-box {
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-pincode-checker-box input {
    min-width: 0 !important;
  }
  .pdp-specs-table-box,
  .pdp-tech-table {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    font-size: 12px !important;
  }
  .pdp-tech-table td {
    padding: 8px 6px !important;
    word-break: break-word !important;
  }
}

/* Left Column: Cover & Excerpt Toggle */
.pdp-left-col {
  position: sticky;
  top: 96px;
}

.pdp-cover-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  text-align: center;
}

.pdp-cover-img-wrap {
  width: 100%;
  aspect-ratio: 2 / 3;
  max-height: 480px;
  margin: 0 auto 16px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FAF8F5;
}

.pdp-cover-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.pdp-cover-img:hover {
  transform: scale(1.03);
}

.pdp-look-inside-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  background: #FEF3C7;
  color: #92400E;
  border: 1px solid #FDE68A;
  padding: 10px 16px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 12px;
}

.pdp-look-inside-btn:hover {
  background: #FDE68A;
}

.pdp-excerpt-box {
  display: none;
  background: #FFFDF9;
  border: 1px solid #F59E0B;
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
  text-align: left;
  font-size: 13.5px;
  line-height: 1.7;
  color: #334155;
  font-family: 'Merriweather', serif;
}

.pdp-excerpt-box.open {
  display: block;
  animation: fadeIn 0.25s ease;
}

.pdp-perks-checklist {
  list-style: none;
  padding: 0;
  margin: 16px 0 0;
  border-top: 1px solid #F1F5F9;
  padding-top: 16px;
  text-align: left;
}

.pdp-perks-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 12.5px;
  color: #475569;
  margin-bottom: 8px;
  line-height: 1.4;
}

/* Center Column: Book Editorial & Tech Table */
.pdp-center-col {
  padding-right: 12px;
}

.pdp-genre-pill {
  display: inline-block;
  background: #EFF6FF;
  color: #0066B3;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 10px;
}

.pdp-book-title {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 30px;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.25;
  margin: 0 0 8px;
}

.pdp-author-row {
  font-size: 15px;
  color: #64748B;
  margin-bottom: 12px;
}

.pdp-author-row strong {
  color: #0F172A;
}

.pdp-rating-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.pdp-stars {
  display: flex;
  gap: 2px;
  color: #F59E0B;
}

.pdp-rating-text {
  font-size: 13px;
  color: #64748B;
  font-weight: 600;
}

.pdp-price-wrap {
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 14px 0;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
  margin-bottom: 20px;
}

.pdp-selling-price {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 28px;
  font-weight: 800;
  color: #0F172A;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.pdp-compare-price {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 16px;
  color: #94A3B8;
  text-decoration: line-through;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.pdp-discount-badge {
  background: #DC2626;
  color: #FFFFFF;
  font-size: 12px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
}

.pdp-format-row {
  margin-bottom: 20px;
}

.pdp-format-label {
  font-size: 12px;
  font-weight: 700;
  color: #64748B;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 8px;
}

.pdp-format-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #FFFFFF;
  border: 2px solid #0066B3;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  color: #0066B3;
}

.pdp-description-wrap {
  margin-bottom: 24px;
}

.pdp-sec-heading {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 18px;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 10px;
}

.pdp-description-text {
  font-size: 14px;
  line-height: 1.7;
  color: #334155;
  margin-bottom: 16px;
}

.pdp-tech-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 16px;
  font-size: 13px;
}

.pdp-tech-table tr {
  border-bottom: 1px solid #F1F5F9;
}

.pdp-tech-table th {
  text-align: left;
  padding: 10px 0;
  color: #64748B;
  font-weight: 600;
  width: 35%;
}

.pdp-tech-table td {
  padding: 10px 0;
  color: #0F172A;
  font-weight: 500;
}

/* Right Column: Amazon-Style Sticky Buy Box */
.pdp-buy-box {
  background: #FFFFFF;
  border: 1px solid #CBD5E1;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 96px;
}

.pdp-bb-price {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 26px;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 8px;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.pdp-bb-stock {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #059669;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 14px;
}

.pdp-bb-delivery {
  font-size: 13px;
  color: #475569;
  line-height: 1.5;
  margin-bottom: 16px;
  padding-bottom: 14px;
  border-bottom: 1px solid #F1F5F9;
}

.pdp-bb-delivery strong {
  color: #0F172A;
}

.pdp-qty-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.pdp-qty-label {
  font-size: 13px;
  font-weight: 600;
  color: #0F172A;
}

.pdp-qty-control {
  display: inline-flex;
  align-items: center;
  border: 1px solid #CBD5E1;
  border-radius: 6px;
  overflow: hidden;
}

.pdp-qty-btn {
  background: #F8FAFC;
  border: none;
  width: 32px;
  height: 32px;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  color: #0F172A;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pdp-qty-btn:hover {
  background: #E2E8F0;
}

.pdp-qty-input {
  width: 44px;
  height: 32px;
  border: none;
  border-left: 1px solid #CBD5E1;
  border-right: 1px solid #CBD5E1;
  text-align: center;
  font-size: 14px;
  font-weight: 700;
  outline: none;
}

.pdp-btn-stack {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 16px;
}

.pdp-btn-add-cart {
  width: 100%;
  background: #D99B26;
  color: #0A1128;
  border: none;
  padding: 12px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.pdp-btn-add-cart:hover {
  background: #B45309;
  color: #FFFFFF;
}

.pdp-btn-buy-now {
  width: 100%;
  background: #0F172A;
  color: #FFFFFF;
  border: none;
  padding: 12px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.pdp-btn-buy-now:hover {
  background: #1E293B;
}

.pdp-btn-wa-cod {
  width: 100%;
  background: #10B981;
  color: #FFFFFF;
  border: none;
  padding: 12px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.pdp-btn-wa-cod:hover {
  background: #059669;
}

.pdp-bb-security {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-size: 12px;
  color: #64748B;
  padding-top: 12px;
  border-top: 1px solid #F1F5F9;
}

/* Similar Books / Recommendations Grid */
.pdp-recommendations-sec {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #E2E8F0;
}

.pdp-rec-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 20px;
}

@media (max-width: 900px) {
  .pdp-rec-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
}

@media (max-width: 500px) {
  .pdp-rec-grid {
    grid-template-columns: 1fr;
  }
}


/* SLIDE-OVER CART DRAWER COMPLETE STYLES */
.cart-drawer-overlay {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.6) !important;
  backdrop-filter: blur(4px) !important;
  -webkit-backdrop-filter: blur(4px) !important;
  z-index: 999999 !important;
  display: none !important;
  justify-content: flex-end !important;
  align-items: stretch !important;
}
.cart-drawer-overlay.is-open {
  display: flex !important;
}
.cart-drawer-panel {
  width: 440px !important;
  max-width: 100vw !important;
  height: 100% !important;
  background: #FFFFFF !important;
  display: flex !important;
  flex-direction: column !important;
  box-shadow: -8px 0 32px rgba(0, 0, 0, 0.25) !important;
  animation: slideDrawerRight 0.28s cubic-bezier(0.16, 1, 0.3, 1) both !important;
  box-sizing: border-box !important;
  overflow: hidden !important;
}
@keyframes slideDrawerRight {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
.cart-header {
  padding: 18px 24px !important;
  border-bottom: 1px solid #E2E8F0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: #FFFFFF !important;
}
.cart-items-list {
  flex: 1 1 auto !important;
  overflow-y: auto !important;
  padding: 20px 24px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 16px !important;
}
.cart-footer {
  padding: 20px 24px !important;
  border-top: 1px solid #E2E8F0 !important;
  background: #FAF8F5 !important;
  flex-shrink: 0 !important;
}


/* =========================================================================
   GLOBAL 1320PX CONTAINER ARCHITECTURE (BALANCED SYMMETRY & ZERO EMPTY MARGINS)
   ========================================================================= */
.site-container,
.section-container,
.vault-container,
.catalog-container,
.voices-container,
.product-page-wrapper,
.stats-grid,
.editorial-header,
.catalog-filter-bar,
.trust-strip-grid,
.trust-features-grid,
.heritage-grid,
.footer-grid,
#law-academic-vault > div,
#indian-voices-section > div,
#shop-all-catalog > div,
#bestsellers-podium > div,
#category-bento-showcase > div,
#mehfil-rekhta > div {
  max-width: 1320px !important;
  width: 100% !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
  box-sizing: border-box !important;
}

@media (max-width: 768px) {
  .site-container,
  .section-container,
  .vault-container,
  .catalog-container,
  .voices-container,
  .product-page-wrapper,
  .stats-grid,
  .editorial-header,
  .catalog-filter-bar,
  .trust-strip-grid,
  .trust-features-grid,
  .heritage-grid,
  .footer-grid,
  #law-academic-vault > div,
  #indian-voices-section > div,
  #shop-all-catalog > div,
  #bestsellers-podium > div,
  #category-bento-showcase > div,
  #mehfil-rekhta > div {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
}

/* FULL-WIDTH STATS COUNTER BAR (FIXES LEFT-SQUISHED ALIGNMENT) */
.stats-bar {
  display: block !important;
  width: 100% !important;
  background: #FFFFFF !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding: 32px 0 !important;
  box-sizing: border-box !important;
  margin: 0 !important;
}

.stats-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
  max-width: 1320px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
  align-items: center !important;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    padding: 0 16px !important;
  }
}

.stat-item, .stat-card {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  width: 100% !important;
  padding: 8px 12px !important;
  border: none !important;
  border-right: none !important;
  border-left: none !important;
  box-sizing: border-box !important;
  background: transparent !important;
}

.stat-item::before, .stat-item::after,
.stat-card::before, .stat-card::after,
.stat-num::before, .stat-num::after,
.stat-number::before, .stat-number::after,
.stat-label::before, .stat-label::after {
  content: none !important;
  display: none !important;
  border: none !important;
}

.stat-num, .stat-number {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 32px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.15 !important;
  margin-bottom: 6px !important;
  font-variant-numeric: lining-nums tabular-nums !important;
  text-align: center !important;
  border: none !important;
}

@media (min-width: 768px) {
  .stat-num, .stat-number {
    font-size: 36px !important;
  }
}

.stat-label {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  line-height: 1.35 !important;
  text-align: center !important;
  border: none !important;
  max-width: 240px !important;
  margin: 0 auto !important;
}

/* LAW VAULT BALANCED LAYOUT & GRID */
.vault-layout {
  display: grid !important;
  grid-template-columns: 360px 1fr !important;
  gap: 32px !important;
  align-items: start !important;
  width: 100% !important;
  max-width: 1320px !important;
  margin: 0 auto !important;
}

@media (max-width: 992px) {
  .vault-layout {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 20px !important;
  width: 100% !important;
}

@media (max-width: 600px) {
  .vault-cards-grid {
    grid-template-columns: 1fr !important;
  }
}

/* REAL-TIME SEARCH AUTO-SUGGESTION DROPDOWN STYLES */
.search-input-wrap, .hero-search-wrap, .catalog-search-wrap {
  position: relative !important;
}

.search-suggestions-dropdown {
  position: absolute !important;
  top: calc(100% + 8px) !important;
  left: 0 !important;
  right: 0 !important;
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.18) !important;
  z-index: 2000 !important;
  max-height: 420px !important;
  overflow-y: auto !important;
  text-align: left !important;
}

.search-suggestions-header {
  padding: 10px 16px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: #94A3B8 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  border-bottom: 1px solid #F1F5F9 !important;
  background: #FAF8F5 !important;
}

.search-suggestion-item {
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  padding: 10px 16px !important;
  border-bottom: 1px solid #F1F5F9 !important;
  cursor: pointer !important;
  transition: background 0.15s ease !important;
  text-decoration: none !important;
  color: inherit !important;
}

.search-suggestion-item:last-of-type {
  border-bottom: none !important;
}

.search-suggestion-item:hover, .search-suggestion-item.is-selected {
  background: #FFFBEB !important;
}

.suggestion-thumb {
  width: 40px !important;
  height: 56px !important;
  object-fit: cover !important;
  border-radius: 4px !important;
  flex-shrink: 0 !important;
  background: #F1F5F9 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08) !important;
}

.suggestion-details {
  flex: 1 !important;
  min-width: 0 !important;
}

.suggestion-title {
  font-family: 'Merriweather', Georgia, serif !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  line-height: 1.3 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.suggestion-title mark {
  background: #FEF3C7 !important;
  color: #92400E !important;
  font-weight: 800 !important;
  border-radius: 2px !important;
  padding: 0 2px !important;
}

.suggestion-author {
  font-size: 12px !important;
  color: #64748B !important;
  line-height: 1.3 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.suggestion-price {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  white-space: nowrap !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.search-suggestions-footer {
  padding: 12px 16px !important;
  background: #FAF8F5 !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  color: #B45309 !important;
  text-align: center !important;
  cursor: pointer !important;
  border-top: 1px solid #E2E8F0 !important;
  border-radius: 0 0 12px 12px !important;
  transition: background 0.15s ease !important;
}

.search-suggestions-footer:hover {
  background: #FEF3C7 !important;
}



/* =========================================================================
   GLOBAL 1320PX CONTAINER ARCHITECTURE (BALANCED SYMMETRY & ZERO EMPTY MARGINS)
   ========================================================================= */
.site-container,
.section-container,
.vault-container,
.catalog-container,
.voices-container,
.product-page-wrapper,
.stats-grid,
.editorial-header,
.catalog-filter-bar,
.trust-strip-grid,
.trust-features-grid,
.heritage-grid,
.footer-grid,
#law-academic-vault > div,
#indian-voices-section > div,
#shop-all-catalog > div,
#bestsellers-podium > div,
#category-bento-showcase > div,
#mehfil-rekhta > div {
  max-width: 1320px !important;
  width: 100% !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
  box-sizing: border-box !important;
}

@media (max-width: 768px) {
  .site-container,
  .section-container,
  .vault-container,
  .catalog-container,
  .voices-container,
  .product-page-wrapper,
  .stats-grid,
  .editorial-header,
  .catalog-filter-bar,
  .trust-strip-grid,
  .trust-features-grid,
  .heritage-grid,
  .footer-grid,
  #law-academic-vault > div,
  #indian-voices-section > div,
  #shop-all-catalog > div,
  #bestsellers-podium > div,
  #category-bento-showcase > div,
  #mehfil-rekhta > div {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
}

/* FULL-WIDTH STATS COUNTER BAR (FIXES LEFT-SQUISHED ALIGNMENT) */
.stats-bar {
  display: block !important;
  width: 100% !important;
  background: #FFFFFF !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding: 32px 0 !important;
  box-sizing: border-box !important;
  margin: 0 !important;
}

.stats-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
  max-width: 1320px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
  align-items: center !important;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    padding: 0 16px !important;
  }
}

.stat-item, .stat-card {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  width: 100% !important;
  padding: 8px 12px !important;
  border: none !important;
  border-right: none !important;
  border-left: none !important;
  box-sizing: border-box !important;
  background: transparent !important;
}

.stat-item::before, .stat-item::after,
.stat-card::before, .stat-card::after,
.stat-num::before, .stat-num::after,
.stat-number::before, .stat-number::after,
.stat-label::before, .stat-label::after {
  content: none !important;
  display: none !important;
  border: none !important;
}

.stat-num, .stat-number {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 32px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.15 !important;
  margin-bottom: 6px !important;
  font-variant-numeric: lining-nums tabular-nums !important;
  text-align: center !important;
  border: none !important;
}

@media (min-width: 768px) {
  .stat-num, .stat-number {
    font-size: 36px !important;
  }
}

.stat-label {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  line-height: 1.35 !important;
  text-align: center !important;
  border: none !important;
  max-width: 240px !important;
  margin: 0 auto !important;
}

/* LAW VAULT BALANCED LAYOUT & GRID */
.vault-layout {
  display: grid !important;
  grid-template-columns: 360px 1fr !important;
  gap: 32px !important;
  align-items: start !important;
  width: 100% !important;
  max-width: 1320px !important;
  margin: 0 auto !important;
}

@media (max-width: 992px) {
  .vault-layout {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 20px !important;
  width: 100% !important;
}

@media (max-width: 600px) {
  .vault-cards-grid {
    grid-template-columns: 1fr !important;
  }
}

/* REAL-TIME SEARCH AUTO-SUGGESTION DROPDOWN STYLES */
.search-input-wrap, .hero-search-wrap, .catalog-search-wrap {
  position: relative !important;
}

.search-suggestions-dropdown {
  position: absolute !important;
  top: calc(100% + 8px) !important;
  left: 0 !important;
  right: 0 !important;
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.18) !important;
  z-index: 2000 !important;
  max-height: 420px !important;
  overflow-y: auto !important;
  text-align: left !important;
}

.search-suggestions-header {
  padding: 10px 16px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: #94A3B8 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  border-bottom: 1px solid #F1F5F9 !important;
  background: #FAF8F5 !important;
}

.search-suggestion-item {
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  padding: 10px 16px !important;
  border-bottom: 1px solid #F1F5F9 !important;
  cursor: pointer !important;
  transition: background 0.15s ease !important;
  text-decoration: none !important;
  color: inherit !important;
}

.search-suggestion-item:last-of-type {
  border-bottom: none !important;
}

.search-suggestion-item:hover, .search-suggestion-item.is-selected {
  background: #FFFBEB !important;
}

.suggestion-thumb {
  width: 40px !important;
  height: 56px !important;
  object-fit: cover !important;
  border-radius: 4px !important;
  flex-shrink: 0 !important;
  background: #F1F5F9 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08) !important;
}

.suggestion-details {
  flex: 1 !important;
  min-width: 0 !important;
}

.suggestion-title {
  font-family: 'Merriweather', Georgia, serif !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  line-height: 1.3 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.suggestion-title mark {
  background: #FEF3C7 !important;
  color: #92400E !important;
  font-weight: 800 !important;
  border-radius: 2px !important;
  padding: 0 2px !important;
}

.suggestion-author {
  font-size: 12px !important;
  color: #64748B !important;
  line-height: 1.3 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.suggestion-price {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  white-space: nowrap !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.search-suggestions-footer {
  padding: 12px 16px !important;
  background: #FAF8F5 !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  color: #B45309 !important;
  text-align: center !important;
  cursor: pointer !important;
  border-top: 1px solid #E2E8F0 !important;
  border-radius: 0 0 12px 12px !important;
  transition: background 0.15s ease !important;
}

.search-suggestions-footer:hover {
  background: #FEF3C7 !important;
}


/* =========================================================================
   MASTER FIX 1: HERO SEARCH DROPDOWN Z-INDEX & OVERFLOW UNCLIPPING
   ========================================================================= */
#indigo-video-hero,
#indigo-hero-master,
.ivh-section {
  position: relative !important;
  z-index: 500 !important;
  overflow-x: clip !important;
}

.ivh-container,
.ihm-container,
.ivh-left,
.ihm-left-col,
.ihm-search-wrap,
.hero-search-wrap {
  position: relative !important;
  z-index: 600 !important;
  overflow: visible !important;
}

.hero-bg-clip {
  position: absolute !important;
  inset: 0 !important;
  overflow: hidden !important;
  pointer-events: none !important;
  z-index: 1 !important;
}

#hero-search-dropdown,
#hero-search-suggestions,
.indigo-search-dropdown,
.search-suggestions-dropdown {
  position: absolute !important;
  top: calc(100% + 8px) !important;
  left: 0 !important;
  width: 100% !important;
  min-width: 0 !important;
  max-width: 100% !important;
  max-height: 420px !important;
  overflow-y: auto !important;
  background: #FFFFFF !important;
  border: 1px solid #CBD5E1 !important;
  border-radius: 12px !important;
  box-shadow: 0 24px 60px rgba(9, 19, 44, 0.4) !important;
  z-index: 999999 !important;
  padding: 10px !important;
  box-sizing: border-box !important;
}

.search-suggestion-item {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  padding: 10px 12px !important;
  border-radius: 8px !important;
  cursor: pointer !important;
  transition: background 0.15s ease !important;
  border-bottom: 1px solid #F1F5F9 !important;
}
.search-suggestion-item:last-child {
  border-bottom: none !important;
}
.search-suggestion-item:hover {
  background: #F8FAFC !important;
}
.suggestion-thumb {
  width: 38px !important;
  height: 54px !important;
  object-fit: cover !important;
  border-radius: 4px !important;
  flex-shrink: 0 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1) !important;
}
.suggestion-details {
  flex: 1 !important;
  min-width: 0 !important;
}
.suggestion-title {
  font-size: 13.5px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
}
.suggestion-author {
  font-size: 11.5px !important;
  color: #64748B !important;
  margin-top: 2px !important;
}
.suggestion-price {
  font-size: 13px !important;
  font-weight: 800 !important;
  color: #0066B3 !important;
  flex-shrink: 0 !important;
}
.badge-binding {
  display: inline-block !important;
  font-size: 9.5px !important;
  font-weight: 700 !important;
  padding: 2px 6px !important;
  border-radius: 4px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  background: #E2E8F0 !important;
  color: #334155 !important;
}
.badge-binding.paperback {
  background: #E0F2FE !important;
  color: #0369A1 !important;
}
.badge-binding.hardcover {
  background: #FEF3C7 !important;
  color: #92400E !important;
}

/* =========================================================================
   MASTER FIX 2: FIXED SLIDE-OVER CART DRAWER & ADD-TO-CART ANIMATION
   ========================================================================= */
#cartOverlay,
.cart-overlay,
.cart-drawer-overlay {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.6) !important;
  backdrop-filter: blur(4px) !important;
  z-index: 9999998 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transition: opacity 0.3s ease, visibility 0.3s ease !important;
}

#cartOverlay.is-open,
.cart-overlay.is-open,
.cart-drawer-overlay.is-open {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

#cartDrawer,
.cart-drawer,
.cart-drawer-panel {
  position: fixed !important;
  top: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 440px !important;
  max-width: 100vw !important;
  height: 100vh !important;
  max-height: 100vh !important;
  background: #FFFFFF !important;
  box-shadow: -8px 0 36px rgba(15, 23, 42, 0.3) !important;
  z-index: 9999999 !important;
  display: flex !important;
  flex-direction: column !important;
  transform: translateX(100%) !important;
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
}

#cartDrawer.is-open,
.cart-drawer.is-open,
.cart-drawer-panel.is-open {
  transform: translateX(0) !important;
}

.cart-drawer-header {
  padding: 18px 24px !important;
  border-bottom: 1px solid #E2E8F0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: #FFFFFF !important;
}

.drawer-close-btn {
  background: #F1F5F9 !important;
  border: none !important;
  border-radius: 50% !important;
  width: 32px !important;
  height: 32px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  color: #475569 !important;
  transition: background 0.15s ease !important;
}
.drawer-close-btn:hover {
  background: #E2E8F0 !important;
  color: #0F172A !important;
}

.cart-drawer-body {
  flex: 1 !important;
  overflow-y: auto !important;
  padding: 20px 24px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 16px !important;
  background: #FFFFFF !important;
}

.cart-drawer-footer {
  padding: 20px 24px !important;
  border-top: 1px solid #E2E8F0 !important;
  background: #FAF8F5 !important;
  margin-top: auto !important;
}

.btn-checkout {
  width: 100% !important;
  background: #0066B3 !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 8px !important;
  padding: 14px 20px !important;
  font-size: 14.5px !important;
  font-weight: 700 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  cursor: pointer !important;
  transition: background 0.2s ease, transform 0.15s ease !important;
  box-shadow: 0 4px 12px rgba(0, 102, 179, 0.25) !important;
}
.btn-checkout:hover {
  background: #004D86 !important;
  transform: translateY(-1px) !important;
}

.btn-wa-checkout {
  width: 100% !important;
  background: #25D366 !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 8px !important;
  padding: 13px 20px !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  cursor: pointer !important;
  transition: background 0.2s ease, transform 0.15s ease !important;
  box-shadow: 0 4px 12px rgba(37, 211, 102, 0.2) !important;
}
.btn-wa-checkout:hover {
  background: #1EBE5D !important;
  transform: translateY(-1px) !important;
}

/* Add to Cart button pulse animation */
@keyframes btnAddPop {
  0% { transform: scale(1); }
  50% { transform: scale(1.08); background-color: #15803D; }
  100% { transform: scale(1); }
}
.btn-add-pop {
  animation: btnAddPop 0.4s ease forwards !important;
}

/* =========================================================================
   MASTER FIX 3: FULL-WIDTH LAW VAULT PADDING & 2x2 GRID
   ========================================================================= */
#law-academic-vault,
.vault-section {
  width: 100% !important;
  max-width: 100% !important;
  background: #FFFFFF !important;
  padding: 56px 0 !important;
  box-sizing: border-box !important;
}

#law-academic-vault .site-container,
.vault-container {
  max-width: 1320px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
}

.vault-layout {
  display: grid !important;
  grid-template-columns: 280px 1fr !important;
  gap: 32px !important;
  width: 100% !important;
  align-items: start !important;
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 20px !important;
  width: 100% !important;
}

@media (max-width: 1200px) {
  .vault-cards-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

.vault-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  padding: 18px !important;
  display: flex !important;
  flex-direction: column !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
.vault-card:hover {
  transform: translateY(-3px) !important;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08) !important;
}

.vault-card-thumb {
  width: 100% !important;
  aspect-ratio: 2 / 3 !important;
  height: auto !important;
  border-radius: 8px !important;
  overflow: hidden !important;
  background: #F1F5F9 !important;
  margin-bottom: 14px !important;
}

.vault-card-thumb img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block !important;
}

@media (max-width: 900px) {
  .vault-layout {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
  #law-academic-vault .site-container,
  .vault-container {
    padding: 0 16px !important;
  }
}

/* =========================================================================
   MASTER FIX 4: SOLO PRODUCT DETAILS PAGE & CLICKABLE AUTHORS
   ========================================================================= */
.pdp-clickable-author {
  color: #0066B3 !important;
  cursor: pointer !important;
  text-decoration: underline !important;
  font-weight: 700 !important;
  transition: color 0.15s ease !important;
}
.pdp-clickable-author:hover {
  color: #0F172A !important;
}

.pdp-specs-table {
  width: 100% !important;
  border-collapse: collapse !important;
  margin-top: 14px !important;
}
.pdp-specs-table tr {
  border-bottom: 1px solid #F1F5F9 !important;
}
.pdp-specs-table td {
  padding: 8px 4px !important;
  font-size: 13px !important;
}
.pdp-specs-label {
  font-weight: 600 !important;
  color: #64748B !important;
  width: 35% !important;
}
.pdp-specs-val {
  font-weight: 700 !important;
  color: #0F172A !important;
}

/* =========================================================================
   MASTER FIX 3 & 4: BALANCED 1320PX VAULT, INDIAN VOICES & PRAYAGRAJ HERITAGE
   ========================================================================= */

/* 1. Contemporary Indian Voices Grid (Balanced 1320px Layout) */
#contemporary-fiction .site-container,
.voices-container {
  max-width: 1320px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
}

.contemporary-grid {
  display: grid !important;
  grid-template-columns: 1fr 1.25fr !important;
  gap: 36px !important;
  width: 100% !important;
  align-items: start !important;
  box-sizing: border-box !important;
}

@media (max-width: 992px) {
  .contemporary-grid {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
}

.feat-book-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  padding: 32px !important;
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
}

.mini-grid-2x2 {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 20px !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

@media (max-width: 600px) {
  .mini-grid-2x2 {
    grid-template-columns: 1fr !important;
  }
}

.mini-book-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  padding: 16px !important;
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03) !important;
}

/* 2. Law, Judiciary & Academic Reference Vault (Full 1320px Symmetry) */
#law-academic-vault .site-container,
.vault-container {
  max-width: 1320px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
}

.vault-layout {
  display: grid !important;
  grid-template-columns: 280px 1fr !important;
  gap: 32px !important;
  width: 100% !important;
  align-items: start !important;
  box-sizing: border-box !important;
}

@media (max-width: 992px) {
  .vault-layout {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
}

.vault-nav-col {
  width: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 20px !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

@media (max-width: 1200px) {
  .vault-cards-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

@media (max-width: 640px) {
  .vault-cards-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
}

.vault-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  padding: 18px !important;
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03) !important;
}

/* 3. Prayagraj Heritage & Headquarters Section (Perfect Alignment) */
.heritage-section {
  background: #FAF8F5 !important;
  padding: 64px 0 !important;
  border-top: 1px solid #E2E8F0 !important;
  width: 100% !important;
}

.heritage-grid {
  display: grid !important;
  grid-template-columns: 1.2fr 0.8fr !important;
  gap: 48px !important;
  align-items: center !important;
  width: 100% !important;
  padding: 0 !important;
  margin: 0 !important;
  box-sizing: border-box !important;
}

@media (max-width: 992px) {
  .heritage-grid {
    grid-template-columns: 1fr !important;
    gap: 36px !important;
  }
}

.heritage-stats-row {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 16px !important;
  margin-top: 24px !important;
  padding: 20px 0 !important;
  border-top: 1px solid #E2E8F0 !important;
  border-bottom: 1px solid #E2E8F0 !important;
  text-align: left !important;
}

.heritage-stat-val {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 24px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.2 !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.heritage-stat-lbl {
  font-size: 12px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  margin-top: 4px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
}

.heritage-card,
.heritage-hq-card {
  background: #0A1128 !important;
  color: #FFFFFF !important;
  border: 2px solid #D99B26 !important;
  border-radius: 16px !important;
  padding: 36px 32px !important;
  box-shadow: 0 12px 32px rgba(10, 17, 40, 0.25) !important;
  box-sizing: border-box !important;
}

.heritage-card h3,
.heritage-hq-card h3 {
  color: #FFFFFF !important;
  margin-top: 0 !important;
  font-family: 'Merriweather', Georgia, serif !important;
  font-size: 20px !important;
  font-weight: 700 !important;
}

.heritage-card p,
.heritage-hq-card p {
  color: #CBD5E1 !important;
  font-size: 13.5px !important;
  line-height: 1.6 !important;
}

.heritage-details-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 0 24px 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
}

.heritage-details-list li {
  display: flex !important;
  align-items: flex-start !important;
  gap: 12px !important;
  font-size: 13.5px !important;
  color: #E2E8F0 !important;
  line-height: 1.5 !important;
}

.heritage-details-list li i,
.heritage-details-list li svg {
  color: #D99B26 !important;
  margin-top: 2px !important;
  flex-shrink: 0 !important;
}



/* =========================================================================
   UNIVERSAL 3D HOVER BOOK-OPENING STAGE (.indigo-3d-book-stage)
   ========================================================================= */
.indigo-3d-book-stage {
  position: relative !important;
  width: 100% !important;
  aspect-ratio: 2 / 3 !important;
  perspective: 1400px !important;
  transform-style: preserve-3d !important;
  cursor: pointer !important;
}

/* Stationary Cream First-Page Preview Inside the Book */
.indigo-3d-inside-page {
  position: absolute !important;
  inset: 4px !important;
  background: linear-gradient(to right, #EAE3D2 0%, #FFFDF9 12%, #FFFDF9 100%) !important;
  border: 1px solid #CBD5E1 !important;
  border-right: 5px solid #CBD5E1 !important;
  border-radius: 2px 6px 6px 2px !important;
  padding: 14px 12px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  z-index: 1 !important;
  box-shadow: inset 6px 0 12px rgba(0,0,0,0.08), 0 10px 24px rgba(0,0,0,0.12) !important;
  overflow: hidden !important;
}

/* Front Cover Leaf That Swings Open on Hover */
.indigo-3d-cover-leaf {
  position: absolute !important;
  inset: 0 !important;
  transform-origin: left center !important;
  transform-style: preserve-3d !important;
  transition: transform 0.68s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.68s ease !important;
  z-index: 10 !important;
  border-radius: 2px 6px 6px 2px !important;
}

/* OPEN COVER AUTOMATICALLY ON HOVER! */
.indigo-3d-book-stage:hover .indigo-3d-cover-leaf,
.vault-card:hover .indigo-3d-cover-leaf,
.podium-center-book:hover .podium-cover-leaf,
.indigo-3d-book-stage.opened .indigo-3d-cover-leaf {
  transform: rotateY(-128deg) !important;
  box-shadow: -14px 18px 28px rgba(0,0,0,0.35) !important;
}

.indigo-3d-cover-front,
.indigo-3d-cover-back {
  position: absolute !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  backface-visibility: hidden !important;
  -webkit-backface-visibility: hidden !important;
  border-radius: 2px 6px 6px 2px !important;
  overflow: hidden !important;
}

.indigo-3d-cover-front {
  z-index: 2 !important;
  background: #0F172A !important;
}

.indigo-3d-cover-front img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block !important;
}

.indigo-3d-cover-back {
  transform: rotateY(180deg) !important;
  background: linear-gradient(145deg, #09132C 0%, #1E293B 100%) !important;
  border: 2px solid #D99B26 !important;
  color: #FEF3C7 !important;
  padding: 12px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
}

/* =========================================================================
   SEARCH WITH CATEGORY DROPDOWN STYLES
   ========================================================================= */
.search-input-group {
  display: flex !important;
  align-items: stretch !important;
  background: #FFFFFF !important;
  border: 1px solid #CBD5E1 !important;
  border-radius: 9999px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 14px rgba(0,0,0,0.06) !important;
  transition: all 0.2s ease !important;
}

.search-input-group:focus-within {
  border-color: #0066B3 !important;
  box-shadow: 0 0 0 3px rgba(0,102,179,0.15) !important;
}

.search-category-select {
  background: #F8FAFC !important;
  border: none !important;
  border-right: 1px solid #E2E8F0 !important;
  padding: 0 16px !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #334155 !important;
  outline: none !important;
  cursor: pointer !important;
}

/* =========================================================================
   3 CATEGORY PROMO BANNERS (1320px Grid)
   ========================================================================= */
.promo-banners-section {
  max-width: 1320px !important;
  margin: 40px auto 30px !important;
  padding: 0 20px !important;
  box-sizing: border-box !important;
}

.promo-banners-grid {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 20px !important;
}

@media (max-width: 900px) {
  .promo-banners-grid {
    grid-template-columns: 1fr !important;
  }
}

.promo-banner-card {
  border-radius: 12px !important;
  padding: 24px 28px !important;
  color: #FFFFFF !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  min-height: 150px !important;
  cursor: pointer !important;
  transition: transform 0.25s ease, box-shadow 0.25s ease !important;
  position: relative !important;
  overflow: hidden !important;
}

.promo-banner-card:hover {
  transform: translateY(-3px) !important;
  box-shadow: 0 12px 24px rgba(0,0,0,0.18) !important;
}

.promo-banner-navy {
  background: linear-gradient(135deg, #1D3549 0%, #0F202E 100%) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
}

.promo-banner-espresso {
  background: linear-gradient(135deg, #2B1D12 0%, #1A1009 100%) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
}

.promo-banner-forest {
  background: linear-gradient(135deg, #133026 0%, #0B1C16 100%) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
}

.promo-banner-subtitle {
  font-size: 11px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.12em !important;
  color: #FBBF24 !important;
  font-weight: 700 !important;
  margin-bottom: 6px !important;
}

.promo-banner-title {
  font-family: 'Merriweather', serif !important;
  font-size: 20px !important;
  font-weight: 700 !important;
  line-height: 1.3 !important;
  color: #FFFFFF !important;
  margin: 0 0 16px !important;
}

.promo-banner-cta {
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  color: #FFFFFF !important;
  text-decoration: underline !important;
}

/* =========================================================================
   HORIZONTAL CATEGORY SHELVES STYLES
   ========================================================================= */
.category-shelf-section {
  max-width: 1320px !important;
  margin: 36px auto !important;
  padding: 0 20px !important;
  box-sizing: border-box !important;
}

.shelf-header {
  display: flex !important;
  justify-content: space-between !important;
  align-items: flex-end !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding-bottom: 12px !important;
  margin-bottom: 20px !important;
}

.shelf-title-wrap h3 {
  font-family: 'Merriweather', serif !important;
  font-size: 24px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  margin: 0 !important;
}

.shelf-scroll-row {
  display: flex !important;
  gap: 20px !important;
  overflow-x: auto !important;
  padding: 10px 4px 20px !important;
  scroll-behavior: smooth !important;
  -webkit-overflow-scrolling: touch !important;
}

.shelf-scroll-row::-webkit-scrollbar {
  height: 6px !important;
}

.shelf-scroll-row::-webkit-scrollbar-track {
  background: #F1F5F9 !important;
  border-radius: 9999px !important;
}

.shelf-scroll-row::-webkit-scrollbar-thumb {
  background: #CBD5E1 !important;
  border-radius: 9999px !important;
}

.shelf-book-card {
  flex: 0 0 190px !important;
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 10px !important;
  padding: 12px !important;
  box-sizing: border-box !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  transition: transform 0.25s ease, box-shadow 0.25s ease !important;
}

.shelf-book-card:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 8px 20px rgba(0,0,0,0.08) !important;
}

/* =========================================================================
   SOLO PRODUCT PAGE UPGRADES (MATCHING indigobooksindia.com)
   ========================================================================= */
.pdp-variant-btn {
  padding: 8px 16px !important;
  border: 1.5px solid #CBD5E1 !important;
  border-radius: 8px !important;
  background: #FFFFFF !important;
  color: #0F172A !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.pdp-variant-btn:hover {
  border-color: #0066B3 !important;
  background: #F8FAFC !important;
}

.pdp-variant-btn.active {
  border-color: #0066B3 !important;
  background: #EFF6FF !important;
  color: #0066B3 !important;
  box-shadow: 0 0 0 1px #0066B3 !important;
}

.pdp-tab-nav {
  display: flex !important;
  gap: 12px !important;
  border-bottom: 2px solid #E2E8F0 !important;
  margin: 24px 0 16px !important;
}

.pdp-tab-btn {
  background: none !important;
  border: none !important;
  padding: 10px 18px !important;
  font-size: 14px !important;
  font-weight: 700 !important;
  color: #64748B !important;
  cursor: pointer !important;
  position: relative !important;
  transition: color 0.2s ease !important;
}

.pdp-tab-btn.active {
  color: #0066B3 !important;
}

.pdp-tab-btn.active::after {
  content: '' !important;
  position: absolute !important;
  bottom: -2px !important;
  left: 0 !important;
  right: 0 !important;
  height: 2px !important;
  background: #0066B3 !important;
}

/* =========================================================================
   INDIGO MODAL OVERLAYS & DIALOGS (STRICT TOGGLE SYSTEM - ZERO JITTER/STACKING)
   ========================================================================= */
.indigo-modal-overlay,
.express-checkout-modal-backdrop,
.modal-overlay,
#indigo-express-checkout-modal,
#indigo-order-success-modal,
#indigo-overview-modal,
#indigo-signin-modal,
#expressPhoneCheckoutModal,
#orderConfirmationModal,
#overviewModalOverlay,
#loginModalOverlay {
  display: none !important;
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.75) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  z-index: 1000000 !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 16px !important;
  box-sizing: border-box !important;
}

.indigo-modal-overlay.is-active,
.express-checkout-modal-backdrop.is-active,
.modal-overlay.is-active,
#indigo-express-checkout-modal.is-active,
#indigo-order-success-modal.is-active,
#indigo-overview-modal.is-active,
#indigo-signin-modal.is-active,
#expressPhoneCheckoutModal.is-active,
#orderConfirmationModal.is-active,
#overviewModalOverlay.is-active,
#loginModalOverlay.is-active {
  display: flex !important;
}

.express-checkout-card {
  background: #FFFFFF !important;
  border-radius: 16px !important;
  width: 100% !important;
  max-width: 520px !important;
  max-height: 90vh !important;
  overflow-y: auto !important;
  padding: 28px !important;
  box-sizing: border-box !important;
  box-shadow: 0 24px 48px rgba(0,0,0,0.3) !important;
  position: relative !important;
  z-index: 1000001 !important;
}

/* =========================================================================
   CATEGORY BENTO SHOWCASE (image_68cd69.jpg Asymmetric Layout)
   ========================================================================= */
.category-bento-section {
  background: #FAF8F5 !important;
  padding: 56px 0 !important;
  width: 100% !important;
  border-top: 1px solid #F1ECE4 !important;
  border-bottom: 1px solid #F1ECE4 !important;
  box-sizing: border-box !important;
}

.category-bento-showcase {
  max-width: 1320px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
}

.category-pills-bar {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  flex-wrap: wrap !important;
  margin-bottom: 28px !important;
}

.cat-bento-pill {
  background: #FFFFFF !important;
  border: 1px solid #CBD5E1 !important;
  border-radius: 9999px !important;
  padding: 9px 18px !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  color: #475569 !important;
  cursor: pointer !important;
  transition: all 0.22s ease !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
}

.cat-bento-pill:hover {
  background: #F8FAFC !important;
  border-color: #94A3B8 !important;
  color: #0F172A !important;
}

.cat-bento-pill.active {
  background: #0066B3 !important;
  border-color: #0066B3 !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 12px rgba(0, 102, 179, 0.25) !important;
}

.category-bento-grid {
  display: grid !important;
  grid-template-columns: 400px 1fr !important;
  gap: 24px !important;
  align-items: stretch !important; /* Forces Left Card and Right 2x2 Grid to have identical total height! */
  width: 100% !important;
  box-sizing: border-box !important;
}

/* LEFT LARGE FEATURED CARD (Raag Darbari style) */
.bento-left-spotlight {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  padding: 28px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  box-sizing: border-box !important;
  height: 100% !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.04) !important;
}

.bento-left-cover-wrap {
  width: 210px !important;
  height: 315px !important;
  margin: 0 auto 20px auto !important;
  position: relative !important;
}

/* RIGHT 2x2 GRID OF 4 HORIZONTAL CARDS */
.bento-right-2x2 {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  grid-template-rows: repeat(2, 1fr) !important;
  gap: 20px !important;
  height: 100% !important;
}

.bento-horiz-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  padding: 20px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  box-sizing: border-box !important;
  height: 100% !important;
  position: relative !important;
  box-shadow: 0 2px 12px rgba(0,0,0,0.03) !important;
}

.bento-horiz-top {
  display: grid !important;
  grid-template-columns: 96px 1fr !important;
  gap: 16px !important;
  align-items: start !important;
  margin-bottom: 12px !important;
}

.bento-horiz-cover {
  width: 96px !important;
  height: 144px !important;
  position: relative !important;
  flex-shrink: 0 !important;
}

.bento-card-actions {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 10px !important;
  margin-top: auto !important;
  padding-top: 12px !important;
}

@media (max-width: 1024px) {
  .category-bento-grid {
    grid-template-columns: 1fr !important;
  }
  .bento-right-2x2 {
    grid-template-columns: 1fr !important;
  }
}

/* =========================================================================
   CATALOG PAGINATION CONTROLS (12 Books per Page)
   ========================================================================= */
.catalog-pagination {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  margin-top: 40px !important;
  padding-top: 24px !important;
  border-top: 1px solid #E2E8F0 !important;
  flex-wrap: wrap !important;
}

.pagination-btn {
  min-width: 38px !important;
  height: 38px !important;
  padding: 0 14px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 8px !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  background: #FFFFFF !important;
  border: 1px solid #CBD5E1 !important;
  color: #334155 !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  user-select: none !important;
}

.pagination-btn:hover:not(:disabled) {
  background: #F8FAFC !important;
  border-color: #94A3B8 !important;
  color: #0F172A !important;
}

.pagination-btn.active {
  background: #0066B3 !important;
  border-color: #0066B3 !important;
  color: #FFFFFF !important;
  box-shadow: 0 2px 8px rgba(0, 102, 179, 0.25) !important;
}

.pagination-btn:disabled {
  opacity: 0.4 !important;
  cursor: not-allowed !important;
  border-color: #E2E8F0 !important;
}

.pagination-ellipsis {
  padding: 0 4px !important;
  color: #94A3B8 !important;
  font-weight: 700 !important;
}

/* ALIGNED UNIFORM COVER HEIGHTS & 2:3 ASPECT RATIO */
.catalog-card {
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  height: 100% !important;
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  padding: 16px !important;
  box-sizing: border-box !important;
  transition: transform 0.25s ease, box-shadow 0.25s ease !important;
}

.catalog-card:hover {
  box-shadow: 0 8px 24px rgba(0,0,0,0.06) !important;
  transform: translateY(-2px) !important;
}

.catalog-card .indigo-3d-book-stage {
  width: 100% !important;
  aspect-ratio: 2 / 3 !important;
  height: auto !important;
  margin-bottom: 12px !important;
  position: relative !important;
}

.catalog-card-title {
  font-family: 'Merriweather', Georgia, serif !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  line-height: 1.35 !important;
  margin-bottom: 6px !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  display: -webkit-box !important;
  -webkit-line-clamp: 2 !important;
  -webkit-box-orient: vertical !important;
  min-height: 40px !important;
}

/* =========================================================================
   CART DRAWER STRICT FIXED BEHAVIOR & OVERLAY
   ========================================================================= */
#cartDrawer,
.cart-drawer {
  position: fixed !important;
  top: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 440px !important;
  max-width: 100vw !important;
  height: 100vh !important;
  max-height: 100vh !important;
  background: #FFFFFF !important;
  box-shadow: -8px 0 36px rgba(15, 23, 42, 0.3) !important;
  z-index: 9999999 !important;
  display: flex !important;
  flex-direction: column !important;
  transform: translateX(100%) !important;
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.35s ease !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

#cartDrawer.is-open,
.cart-drawer.is-open {
  transform: translateX(0) !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

#cartOverlay,
.cart-overlay {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.6) !important;
  backdrop-filter: blur(4px) !important;
  -webkit-backdrop-filter: blur(4px) !important;
  z-index: 9999998 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transition: opacity 0.3s ease, visibility 0.3s ease !important;
}

#cartOverlay.is-open,
.cart-overlay.is-open {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

/* LAW VAULT PERFECT PADDING & WIDTH ALIGNMENT */
#law-academic-vault {
  width: 100% !important;
  padding: 56px 0 !important;
  box-sizing: border-box !important;
}

#law-academic-vault .site-container,
#law-academic-vault > div,
.vault-container {
  max-width: 1320px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
}

.vault-layout {
  display: grid !important;
  grid-template-columns: 280px 1fr !important;
  gap: 28px !important;
  width: 100% !important;
  align-items: start !important;
  box-sizing: border-box !important;
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  gap: 18px !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

@media (max-width: 1150px) {
  .vault-cards-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 16px !important;
  }
}

@media (max-width: 900px) {
  #law-academic-vault {
    padding: 36px 0 !important;
  }
  #law-academic-vault .site-container,
  #law-academic-vault > div,
  .vault-container {
    padding: 0 14px !important;
  }
  .vault-layout {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 16px !important;
    margin: 0 !important;
    padding: 0 !important;
    box-sizing: border-box !important;
  }
  .vault-nav-col {
    display: flex !important;
    flex-direction: row !important;
    overflow-x: auto !important;
    flex-wrap: nowrap !important;
    gap: 8px !important;
    width: 100% !important;
    padding: 4px 2px 10px !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    box-sizing: border-box !important;
  }
  .vault-nav-col::-webkit-scrollbar {
    display: none !important;
  }
  .vault-tab-btn {
    flex-shrink: 0 !important;
    border-radius: 9999px !important;
    padding: 8px 14px !important;
    font-size: 12px !important;
    white-space: nowrap !important;
    background: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    color: #334155 !important;
    width: auto !important;
  }
  .vault-tab-btn.active {
    background: #0F172A !important;
    border-color: #0F172A !important;
    color: #FFFFFF !important;
  }
  .vault-tab-btn i:last-child {
    display: none !important;
  }
  .vault-concierge-card {
    display: none !important;
  }
  .vault-cards-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .vault-card {
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    width: 100% !important;
    max-width: 100% !important;
    padding: 12px 10px !important;
    box-sizing: border-box !important;
    border-radius: 10px !important;
  }
  .vault-card .indigo-3d-book-stage {
    height: 190px !important;
    max-width: 100% !important;
    margin: 0 auto 10px !important;
  }
}

.vault-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  padding: 14px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  height: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
}

.vault-card-thumb {
  width: 100% !important;
  max-height: 280px !important;
  aspect-ratio: 2 / 3 !important;
  border-radius: 6px !important;
  overflow: hidden !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: #F8FAFC !important;
  margin-bottom: 12px !important;
}

.vault-card-thumb img {
  width: 100% !important;
  height: 100% !important;
  max-height: 280px !important;
  object-fit: cover !important;
}

/* STRICT SUPPRESSION OF DISCOUNTS, STRIKETHROUGHS & REVIEWS */
.discount-pill,
.podium-old-price,
.pdp-discount-badge,
#pdpReviewsCard,
.podium-rating-row,
#modalDiscount {
  display: none !important;
}

/* =========================================================================
   UNIVERSAL 1320PX ALIGNMENT SPINE FOR OUR EXISTING THEME
   ========================================================================= */
.navbar-inner,
.site-container,
.section-container,
.ivh-container,
.ihm-container,
.stats-grid,
.podium-container,
.rekhta-container,
.voices-container,
.category-bento-showcase,
.vault-container,
.catalog-container,
.phs-container,
.footer-container,
.editorial-header,
.catalog-filter-bar,
.trust-strip-grid,
.trust-features-grid,
.heritage-grid,
.footer-grid,
.product-page-wrapper,
#bestsellers-podium > div,
#mehfil-e-rekhta > div,
#mehfil-rekhta > div,
#indian-voices-section > div,
#category-bento-showcase > div,
#law-academic-vault > div,
#shop-all-catalog > div {
  width: 100% !important;
  max-width: 1320px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
  box-sizing: border-box !important;
}

@media (max-width: 768px) {
  .navbar-inner,
  .site-container,
  .section-container,
  .ivh-container,
  .ihm-container,
  .stats-grid,
  .podium-container,
  .rekhta-container,
  .voices-container,
  .category-bento-showcase,
  .vault-container,
  .catalog-container,
  .phs-container,
  .footer-container,
  .editorial-header,
  .catalog-filter-bar,
  .trust-strip-grid,
  .trust-features-grid,
  .heritage-grid,
  .footer-grid,
  .product-page-wrapper,
  #bestsellers-podium > div,
  #mehfil-e-rekhta > div,
  #mehfil-rekhta > div,
  #indian-voices-section > div,
  #category-bento-showcase > div,
  #law-academic-vault > div,
  #shop-all-catalog > div {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
}


/* =========================================================================
     PRODUCT DETAILS PAGE (PDP) MOBILE & DESKTOP ALIGNMENT SHIELD
     ========================================================================= */
  #single-product-page-view {
    min-height: auto !important;
  }
  .product-page-wrapper {
    padding: 20px 20px 24px !important;
  }
  .product-pdp-grid {
    display: grid !important;
    grid-template-columns: 340px 1fr 310px !important;
    gap: 20px !important;
    align-items: start !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-bottom: 20px !important;
    box-sizing: border-box !important;
  }
  .pdp-left-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-trust-card {
    margin: 0 !important;
    padding: 16px 18px !important;
  }
  .pdp-center-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 0 !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-info-header-card {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-bottom: none !important;
    border-radius: 14px 14px 0 0 !important;
    padding: 22px 24px 16px !important;
    margin: 0 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
  }
  .pdp-tabs-container {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-top: 1px solid #F1F5F9 !important;
    border-radius: 0 0 14px 14px !important;
    padding: 0 24px 22px !important;
    margin: 0 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
  }
  .pdp-tab-nav {
    display: flex !important;
    gap: 12px !important;
    border-bottom: 2px solid #E2E8F0 !important;
    margin: 10px 0 14px !important;
  }
  .pdp-right-col {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pdp-buy-box {
    padding: 20px !important;
  }
  .pdp-recommendations-sec {
    margin-top: 24px !important;
    padding-top: 20px !important;
    border-top: 1px solid #E2E8F0 !important;
  }

  @media (max-width: 1100px) {
    .product-pdp-grid {
      grid-template-columns: 300px 1fr 280px !important;
      gap: 16px !important;
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
"""
