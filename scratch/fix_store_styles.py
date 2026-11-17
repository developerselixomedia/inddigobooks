import os

with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Modal Overlays to z-index 30000000
# Look for #loginModalOverlay { ... z-index: 1000000 !important;
old_modal_z = """#loginModalOverlay {
  display: none !important;
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.75) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  z-index: 1000000 !important;"""

new_modal_z = """#loginModalOverlay {
  display: none !important;
  position: fixed !important;
  inset: 0 !important;
  background: rgba(15, 23, 42, 0.75) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  z-index: 30000000 !important;"""

if old_modal_z in text:
    text = text.replace(old_modal_z, new_modal_z)
    print("Updated loginModalOverlay and modal overlays z-index to 30000000")
else:
    print("Warning: old_modal_z not matched exactly, checking alternate")

# Also replace any other z-index: 1000000 !important; for modal overlays
text = text.replace('z-index: 1000000 !important;', 'z-index: 30000000 !important;')
text = text.replace('z-index: 1000001 !important;', 'z-index: 30000001 !important;')

# 2. Update Cart Drawer to 25000000 and Cart Overlay to 24999999
text = text.replace('z-index: 9999999 !important;', 'z-index: 25000000 !important;')
text = text.replace('z-index: 9999998 !important;', 'z-index: 24999999 !important;')

# 3. Add explicit high-priority rule for #indigo-search-results-view & #indigo-solo-product-view
extra_rules = """
/* Dedicated Views & Modal Stacking Order Guarantees */
#indigo-search-results-view {
  position: relative !important;
  z-index: 20000000 !important;
}
#indigo-solo-product-view {
  z-index: 20000000 !important;
}
#cartDrawer, .cart-drawer, .cart-drawer-panel {
  z-index: 25000000 !important;
}
#cartOverlay, .cart-overlay, .cart-drawer-overlay {
  z-index: 24999999 !important;
}
.indigo-modal-overlay,
.express-checkout-modal-backdrop,
#expressPhoneCheckoutModal,
#orderConfirmationModal,
#indigo-express-checkout-modal,
#indigo-order-success-modal,
#overviewModalOverlay,
#loginModalOverlay {
  z-index: 30000000 !important;
}
"""

if '#indigo-search-results-view {' not in text:
    text += extra_rules
    print("Appended Dedicated Views & Modal Stacking Order Guarantees")

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated store_styles.py successfully!")
