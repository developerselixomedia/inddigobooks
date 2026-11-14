import re

print("=== Starting Patch for Mobile View (2-Column, Footer, Left Padding) ===")

# =========================================================================
# 1. UPDATE store_styles.py
# =========================================================================
with open('store_styles.py', 'r', encoding='utf-8') as f:
    ss = f.read()

# Replace vault-cards-grid mobile rules in store_styles.py so it is NEVER 1 column
ss = re.sub(
    r'@media \(max-width: 600px\) \{\s*\.vault-cards-grid \{\s*grid-template-columns: 1fr;\s*\}\s*\}',
    '''@media (max-width: 900px) {
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
}''',
    ss
)

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(ss)
print("✓ Updated store_styles.py")


# =========================================================================
# 2. UPDATE prepare_master_blocks.py (MASTER_STYLE)
# =========================================================================
with open('prepare_master_blocks.py', 'r', encoding='utf-8') as f:
    pm = f.read()

# Replace the vault block in MASTER_STYLE
old_pm_vault = """  .vault-layout {
    display: grid !important;
    grid-template-columns: 260px 1fr !important;
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
  @media (max-width: 1100px) {
    .vault-cards-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 16px !important;
    }
  }
  @media (max-width: 640px) {
    .vault-layout {
      grid-template-columns: 1fr !important;
    }
    .vault-cards-grid {
      grid-template-columns: 1fr !important;
    }
  }"""

new_pm_vault = """  .vault-layout {
    display: grid !important;
    grid-template-columns: 260px 1fr !important;
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
  @media (max-width: 1100px) {
    .vault-cards-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 16px !important;
    }
  }
  @media (max-width: 900px) {
    .vault-layout {
      display: flex !important;
      flex-direction: column !important;
      width: 100% !important;
      gap: 16px !important;
      box-sizing: border-box !important;
      padding: 0 !important;
      margin: 0 !important;
    }
    .vault-nav-col {
      display: flex !important;
      flex-direction: row !important;
      overflow-x: auto !important;
      flex-wrap: nowrap !important;
      gap: 8px !important;
      width: 100% !important;
      padding: 2px 2px 10px !important;
      -webkit-overflow-scrolling: touch !important;
      scrollbar-width: none !important;
      box-sizing: border-box !important;
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
      background: #FFFFFF !important;
      border: 1px solid #CBD5E1 !important;
      color: #334155 !important;
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
      display: none !important; /* Eliminates the empty left gap completely on mobile */
    }
    .vault-cards-grid {
      display: grid !important;
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important; /* 2 COLUMNS ON MOBILE */
      gap: 12px !important;
      width: 100% !important;
      box-sizing: border-box !important;
      padding: 0 !important;
      margin: 0 !important;
    }
    .vault-card {
      width: 100% !important;
      max-width: 100% !important;
      padding: 12px 10px !important;
      box-sizing: border-box !important;
      border-radius: 10px !important;
    }
    .vault-card .indigo-3d-book-stage {
      height: 200px !important;
      width: 100% !important;
      margin: 0 auto 10px !important;
    }
    .vault-card h3 {
      font-size: 13px !important;
      line-height: 1.3 !important;
      margin-bottom: 4px !important;
    }
  }"""

if old_pm_vault in pm:
    pm = pm.replace(old_pm_vault, new_pm_vault, 1)
    print("✓ Updated vault rules in prepare_master_blocks.py")
else:
    print("- old_pm_vault not matched directly")

# Update PDP to 2-Column on Mobile in prepare_master_blocks.py
old_pdp_media_900 = """  @media (max-width: 900px) {
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
    .product-pdp-grid {
      display: flex !important;
      flex-direction: column !important;
      width: 100% !important;
      max-width: 100% !important;
      gap: 20px !important;
      box-sizing: border-box !important;
    }
    .pdp-left-col,
    .pdp-center-col,
    .pdp-right-col {
      position: static !important;
      width: 100% !important;
      max-width: 100% !important;
      min-width: 0 !important;
      padding: 0 !important;
      margin: 0 !important;
      box-sizing: border-box !important;
    }
    .pdp-left-col {
      order: 1 !important;
    }
    .pdp-center-col {
      order: 2 !important;
    }
    .pdp-right-col {
      order: 3 !important;
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
  }"""

new_pdp_media_900 = """  @media (max-width: 900px) {
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
      grid-column: 1 / -1 !important; /* Buy box spans full width across both columns below */
      position: static !important;
      width: 100% !important;
      max-width: 100% !important;
      min-width: 0 !important;
      margin-top: 14px !important;
      padding: 0 !important;
      box-sizing: border-box !important;
    }
    .pdp-cover-card {
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
      padding: 10px !important;
      border-radius: 10px !important;
      box-sizing: border-box !important;
    }
    .indigo-3d-book-stage {
      max-width: 100% !important;
      height: 220px !important;
      margin: 0 auto 10px !important;
    }
    .pdp-look-inside-btn {
      padding: 8px 10px !important;
      font-size: 11px !important;
    }
    .pdp-book-title {
      font-size: 18px !important;
      line-height: 1.25 !important;
      margin: 0 0 6px !important;
      word-break: break-word !important;
    }
    .pdp-author-pill-wrap {
      margin-bottom: 8px !important;
      gap: 6px !important;
    }
    .pdp-author-pill-wrap a {
      font-size: 12px !important;
    }
    .pdp-price-wrap {
      margin-bottom: 8px !important;
      gap: 6px !important;
    }
    .pdp-selling-price {
      font-size: 20px !important;
    }
    .pdp-variant-selector-box {
      padding: 10px !important;
      margin: 8px 0 !important;
    }
    .pdp-variant-buttons {
      gap: 6px !important;
    }
    .pdp-variant-btn {
      padding: 6px 10px !important;
      font-size: 11px !important;
    }
    .pdp-buy-box {
      width: 100% !important;
      max-width: 100% !important;
      padding: 16px !important;
      border-radius: 12px !important;
      box-sizing: border-box !important;
    }
    .pdp-bb-price {
      font-size: 22px !important;
      margin-bottom: 10px !important;
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
  }"""

if old_pdp_media_900 in pm:
    pm = pm.replace(old_pdp_media_900, new_pdp_media_900, 1)
    print("✓ Updated PDP 2-column rules in prepare_master_blocks.py")
else:
    print("- old_pdp_media_900 not matched directly")

# Add Footer & Floating WhatsApp mobile styling to MASTER_STYLE
footer_wa_shield = """
  /* =========================================================================
     FOOTER & FLOATING WHATSAPP BUTTON MOBILE ALIGNMENT SHIELD
     ========================================================================= */
  .wa-tooltip {
    display: none !important;
  }
  @media (min-width: 901px) {
    .floating-wa-btn:hover .wa-tooltip,
    .whatsapp-float-btn:hover .wa-tooltip {
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
      box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
      pointer-events: none !important;
    }
  }

  @media (max-width: 900px) {
    .site-footer {
      padding: 36px 16px 84px !important; /* Extra bottom clearance so button never covers text */
      text-align: left !important;
      box-sizing: border-box !important;
      width: 100% !important;
      max-width: 100vw !important;
      overflow-x: hidden !important;
    }
    .footer-grid {
      display: flex !important;
      flex-direction: column !important;
      gap: 28px !important;
      margin-bottom: 32px !important;
      padding: 0 !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .footer-col h4 {
      margin-bottom: 12px !important;
      font-size: 14px !important;
    }
    .footer-links-list {
      gap: 8px !important;
    }
    .footer-links-list a {
      font-size: 13px !important;
    }
    .footer-bottom-bar {
      flex-direction: column !important;
      gap: 10px !important;
      text-align: center !important;
      padding-top: 20px !important;
      font-size: 11px !important;
      line-height: 1.5 !important;
    }

    /* Floating WhatsApp Button on Mobile: Compact circle, NO overflowing text */
    .whatsapp-float-btn,
    .floating-wa-btn,
    .floating-whatsapp-btn {
      position: fixed !important;
      bottom: 16px !important;
      right: 16px !important;
      width: 48px !important;
      height: 48px !important;
      border-radius: 50% !important;
      background: #25D366 !important;
      box-shadow: 0 4px 16px rgba(37, 211, 102, 0.5) !important;
      z-index: 99999 !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      padding: 0 !important;
      overflow: hidden !important;
    }
    .whatsapp-float-btn .wa-tooltip,
    .floating-wa-btn .wa-tooltip,
    .floating-whatsapp-btn .wa-tooltip {
      display: none !important; /* NEVER spill or overflow text on mobile screen */
    }
    .whatsapp-float-btn i,
    .whatsapp-float-btn svg,
    .floating-wa-btn i,
    .floating-wa-btn svg {
      width: 26px !important;
      height: 26px !important;
      display: block !important;
      margin: 0 !important;
    }
  }
"""

if 'FOOTER & FLOATING WHATSAPP BUTTON MOBILE ALIGNMENT SHIELD' not in pm:
    target = '</style>'
    idx = pm.rfind(target)
    if idx != -1:
        pm = pm[:idx] + footer_wa_shield + '\n' + pm[idx:]
        print("✓ Injected FOOTER & FLOATING WHATSAPP rules into prepare_master_blocks.py")

with open('prepare_master_blocks.py', 'w', encoding='utf-8') as f:
    f.write(pm)
print("✓ prepare_master_blocks.py written successfully!")

