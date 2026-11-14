# -*- coding: utf-8 -*-
with open('store_styles.py', 'r', encoding='utf-8') as f:
    orig = f.read()

new_styles = """

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
.podium-center-book:hover .podium-cover-leaf {
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
   3 CATEGORY PROMO BANNERS (1340px Grid)
   ========================================================================= */
.promo-banners-section {
  max-width: 1340px !important;
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
  max-width: 1340px !important;
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
   EXPRESS PHONE CHECKOUT & PAYMENT MODAL STYLES
   ========================================================================= */
.express-checkout-modal-backdrop {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.7) !important;
  backdrop-filter: blur(4px) !important;
  z-index: 100000 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 16px !important;
  box-sizing: border-box !important;
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
  box-shadow: 0 20px 40px rgba(0,0,0,0.25) !important;
  position: relative !important;
}
"""

if "indigo-3d-book-stage" not in orig:
    # insert before the closing triple quotes
    idx = orig.rfind('"""')
    if idx != -1:
        updated = orig[:idx] + new_styles + orig[idx:]
    else:
        updated = orig + new_styles
    with open('store_styles.py', 'w', encoding='utf-8') as f:
        f.write(updated)
    print("store_styles.py updated successfully!")
else:
    print("indigo-3d-book-stage already in store_styles.py")

