# -*- coding: utf-8 -*-
with open('store_styles.py', 'r', encoding='utf-8') as f:
    css = f.read()

# Styles to append to ensure all 4 issues are 100% resolved in CSS
master_fixes_css = """
/* =========================================================================
   MASTER FIX 1: HERO SEARCH DROPDOWN Z-INDEX & OVERFLOW UNCLIPPING
   ========================================================================= */
#indigo-video-hero,
#indigo-hero-master,
.ivh-section {
  position: relative !important;
  z-index: 500 !important;
  overflow: visible !important;
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
  min-width: 360px !important;
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
  max-width: 90vw !important;
  height: 100vh !important;
  max-height: 100vh !important;
  background: #FFFFFF !important;
  box-shadow: -8px 0 36px rgba(15, 23, 42, 0.3) !important;
  z-index: 9999999 !important;
  display: flex !important;
  flex-direction: column !important;
  transform: translateX(100%) !important;
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  overflow-y: auto !important;
  box-sizing: border-box !important;
}

#cartDrawer.is-open,
.cart-drawer.is-open,
.cart-drawer-panel.is-open {
  transform: translateX(0) !important;
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
  padding: 0 32px !important;
  box-sizing: border-box !important;
}

.vault-layout {
  display: grid !important;
  grid-template-columns: 320px 1fr !important;
  gap: 36px !important;
  width: 100% !important;
  align-items: start !important;
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
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
"""

if "MASTER FIX 1: HERO SEARCH DROPDOWN" not in css:
    css = css + "\n" + master_fixes_css
    with open('store_styles.py', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated store_styles.py with Master Fixes CSS!")
else:
    print("Master Fixes CSS already in store_styles.py")
