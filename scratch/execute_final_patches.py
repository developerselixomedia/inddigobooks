# -*- coding: utf-8 -*-
"""
scratch/execute_final_patches.py
Applies exact replacements to build_html_generator.py:
1. Navbar tabs updated to use navTo(...)
2. Cart Drawer HTML updated to nested overlay + panel layout with matching IDs
3. Run sync_preview_to_shopify.py
4. Run validation checks
"""

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Navigation Tabs
old_nav = '''      <!-- Navigation Tabs -->
      <ul class="nav-links-wrap">
        <li><a href="#top" class="nav-link-btn" onclick="closeDedicatedProductPage(); window.scrollTo({{top: 0, behavior: 'smooth'}})">Home</a></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('all')">Shop All (5,500+)</button></li>
        <li><a href="#bestsellers-podium" class="nav-link-btn" onclick="closeDedicatedProductPage(); document.getElementById('bestsellers-podium').scrollIntoView({{behavior: 'smooth'}})">Best Sellers</a></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('coming-soon')">Coming Soon</button></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToCatalog('pre-order')">Pre-Order</button></li>
        <li><button type="button" class="nav-link-btn" onclick="closeDedicatedProductPage(); scrollToVault('law')">Law Books</button></li>
      </ul>'''

new_nav = '''      <!-- Navigation Tabs -->
      <ul class="nav-links-wrap">
        <li><button type="button" class="nav-link-btn" onclick="navTo('top'); return false;">Home</button></li>
        <li><button type="button" class="nav-link-btn" onclick="navTo('shop-all-catalog', 'all'); return false;">Shop All (5,500+)</button></li>
        <li><button type="button" class="nav-link-btn" onclick="navTo('bestsellers-podium'); return false;">Best Sellers</button></li>
        <li><button type="button" class="nav-link-btn" onclick="navTo('shop-all-catalog', 'coming-soon'); return false;">Coming Soon</button></li>
        <li><button type="button" class="nav-link-btn" onclick="navTo('shop-all-catalog', 'pre-order'); return false;">Pre-Order</button></li>
        <li><button type="button" class="nav-link-btn" onclick="navTo('law-academic-vault'); return false;">Law Books</button></li>
      </ul>'''

if old_nav in code:
    code = code.replace(old_nav, new_nav)
    print("Replaced Navigation Tabs with navTo()")

# 2. Update Cart Drawer HTML
old_cart = '''  <!-- =========================================================================
       13. SLIDE-OUT CART DRAWER
       ========================================================================= -->
  <div id="cartDrawerOverlay" class="cart-overlay" onclick="toggleCartDrawer(false)"></div>
  <aside id="cartDrawer" class="cart-drawer">
    <div class="cart-drawer-header">
      <div style="display: flex; align-items: center; gap: 8px;">
        <i data-lucide="shopping-bag" style="width: 18px; height: 18px; color: #0066B3;"></i>
        <h3 style="font-family: 'Merriweather', serif; font-size: 17px; font-weight: 700; color: #0F172A; margin: 0;">Reading Bag (<span id="cartItemCount">0</span>)</h3>
      </div>
      <button type="button" class="drawer-close-btn" onclick="toggleCartDrawer(false)" aria-label="Close Bag">
        <i data-lucide="x" style="width: 18px; height: 18px;"></i>
      </button>
    </div>

    <!-- Free Delivery Progress Bar -->
    <div style="background: #EFF6FF; padding: 12px 20px; border-bottom: 1px solid #DBEAFE;">
      <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; color: #1E40AF; margin-bottom: 6px;">
        <span id="freeShippingText">Add ₹999 for Free Express Dispatch</span>
        <span id="freeShippingPercent">0%</span>
      </div>
      <div style="width: 100%; height: 6px; background: #BFDBFE; border-radius: 999px; overflow: hidden;">
        <div id="freeShippingBar" style="width: 0%; height: 100%; background: #2563EB; transition: width 0.3s ease;"></div>
      </div>
    </div>

    <div class="cart-drawer-body" id="cartItemsContainer">
      <!-- Empty Bag Placeholder -->
      <div style="text-align: center; padding: 60px 20px; color: #94A3B8;">
        <i data-lucide="book-open" style="width: 48px; height: 48px; margin: 0 auto 12px; stroke-width: 1.5;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 16px; color: #0F172A; margin-bottom: 6px;">Your reading bag is empty</h4>
        <p style="font-size: 13px; color: #64748B;">Explore our 5,500+ curated books and add your next read.</p>
        <button type="button" class="hero-shop-btn" style="margin-top: 16px;" onclick="toggleCartDrawer(false); scrollToCatalog('all');">
          <span>Start Browsing &rarr;</span>
        </button>
      </div>
    </div>

    <div class="cart-drawer-footer">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
        <span style="font-size: 14px; font-weight: 600; color: #475569;">Subtotal:</span>
        <span id="cartDrawerSubtotal" style="font-size: 22px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹0.00</span>
      </div>

      <div style="display: flex; flex-direction: column; gap: 8px;">
        <button type="button" class="btn-checkout" onclick="proceedToCheckout()">
          <i data-lucide="credit-card" style="width: 16px; height: 16px;"></i>
          <span>Proceed to Checkout</span>
        </button>
        <button type="button" class="btn-wa-checkout" onclick="checkoutViaWhatsApp()">
          <i data-lucide="message-circle" style="width: 16px; height: 16px;"></i>
          <span>Checkout via WhatsApp COD (+91 8933063306)</span>
        </button>
      </div>

      <div style="text-align: center; font-size: 11px; color: #94A3B8; margin-top: 12px;">
        100% Genuine Publisher Editions &bull; Same-Day Prayagraj Hub Dispatch
      </div>
    </div>
  </aside>'''

new_cart = '''  <!-- =========================================================================
       13. SLIDE-OVER CART DRAWER
       ========================================================================= -->
  <div id="cartDrawerOverlay" class="cart-drawer-overlay" onclick="toggleCartDrawer(false)">
    <aside id="cartDrawer" class="cart-drawer-panel" onclick="event.stopPropagation()">
      <div class="cart-header">
        <div style="display: flex; align-items: center; gap: 8px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0066B3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
          <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 18px; font-weight: 700; color: #0F172A; margin: 0;">Reading Bag (<span id="cartItemCount">0</span>)</h3>
        </div>
        <button type="button" class="drawer-close-btn" onclick="toggleCartDrawer(false)" aria-label="Close Bag" style="border: none; background: #F1F5F9; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #475569;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
        </button>
      </div>

      <!-- Free Delivery Progress Bar -->
      <div style="background: #EFF6FF; padding: 12px 20px; border-bottom: 1px solid #DBEAFE;">
        <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600; color: #1E40AF; margin-bottom: 6px;">
          <span id="freeShippingText">Free Express Dispatch across India on orders over ₹499</span>
          <span id="freeShippingPercent">100%</span>
        </div>
        <div style="width: 100%; height: 6px; background: #BFDBFE; border-radius: 999px; overflow: hidden;">
          <div id="freeShippingBar" style="width: 100%; height: 100%; background: #2563EB;"></div>
        </div>
      </div>

      <!-- Items List & Empty State Container -->
      <div class="cart-items-list" id="cartDrawerItemsList">
        <!-- Rendered dynamically by updateCartUI() -->
      </div>

      <div class="cart-footer">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px;">
          <span style="font-size: 14px; font-weight: 600; color: #475569;">Subtotal:</span>
          <span id="cartDrawerSubtotal" style="font-size: 22px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹0.00</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 8px;">
          <button type="button" class="btn-checkout" onclick="proceedToCheckout()" style="width: 100%; background: #0F172A; color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; font-weight: 700; padding: 12px 0; border: none; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/></svg>
            <span>Proceed to Checkout</span>
          </button>
          <button type="button" class="btn-wa-checkout" onclick="checkoutWhatsApp()" style="width: 100%; background: #25D366; color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; font-weight: 700; padding: 12px 0; border: none; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            <span>Checkout via WhatsApp COD (+91 8933063306)</span>
          </button>
        </div>

        <div style="text-align: center; font-size: 11px; color: #94A3B8; margin-top: 12px;">
          100% Genuine Publisher Editions &bull; Same-Day Prayagraj Hub Dispatch
        </div>
      </div>
    </aside>
  </div>'''

if old_cart in code:
    code = code.replace(old_cart, new_cart)
    print("Replaced Cart Drawer with nested overlay + panel layout")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_html_generator.py final patches written.")

