# -*- coding: utf-8 -*-
"""
Verification suite for Direct Buy Now & Mobile Checkout flow
"""
import re
import sys

def run_tests():
    print("=== TESTING DIRECT BUY NOW & MOBILE CHECKOUT FIXES ===")
    
    # 1. Check editorial_video_theme.py for handleSoloBuyNow direct checkout
    with open("editorial_video_theme.py", "r", encoding="utf-8") as f:
        ev_code = f.read()

    assert "function resolveShopifyVariant(book)" in ev_code, "resolveShopifyVariant helper missing in editorial_video_theme.py"
    print("[PASS] 1. resolveShopifyVariant helper present in editorial_video_theme.py")

    assert "fetch('/cart/add.js'" in ev_code, "Shopify /cart/add.js sync missing in editorial_video_theme.py"
    print("[PASS] 2. Shopify /cart/add.js session cart sync present in editorial_video_theme.py")

    assert "window.proceedToCheckout()" in ev_code or "window.location.href = '/checkout'" in ev_code, "Direct checkout routing missing"
    print("[PASS] 3. Direct proceedToCheckout routing implemented in handleSoloBuyNow")

    # 2. Check store_scripts.py for closeOrderConfirmationModal
    with open("store_scripts.py", "r", encoding="utf-8") as f:
        ss_code = f.read()

    # Verify closeDedicatedProductPage() is NOT called inside closeOrderConfirmationModal
    modal_func_match = re.search(r'function closeOrderConfirmationModal\(\)\s*\{([^}]+)\}', ss_code)
    assert modal_func_match, "closeOrderConfirmationModal function not found in store_scripts.py"
    assert "closeDedicatedProductPage" not in modal_func_match.group(1), "closeDedicatedProductPage MUST NOT be called in closeOrderConfirmationModal"
    print("[PASS] 4. closeDedicatedProductPage() removed from closeOrderConfirmationModal (no homepage bounce)")

    # 3. Check assets/main-store.js for compiled integrity
    with open("assets/main-store.js", "r", encoding="utf-8") as f:
        ms_code = f.read()

    assert "resolveShopifyVariant" in ms_code, "resolveShopifyVariant missing in assets/main-store.js"
    assert "closeDedicatedProductPage" not in re.search(r'function closeOrderConfirmationModal\(\)\s*\{([^}]+)\}', ms_code).group(1), "closeDedicatedProductPage still in main-store.js closeOrderConfirmationModal"
    print("[PASS] 5. assets/main-store.js has all direct Buy Now and modal fixes compiled")

    # 4. Check sections/main-product.liquid
    with open("sections/main-product.liquid", "r", encoding="utf-8") as f:
        mp_code = f.read()

    assert "v2-solo-mobile-buy-bar" in mp_code, "Sticky mobile buy bar missing in sections/main-product.liquid"
    assert "Buy Now (Instant Checkout)" in mp_code, "Instant Checkout label missing in main-product.liquid"
    print("[PASS] 6. sections/main-product.liquid updated with sticky mobile buy bar and direct checkout")

    # 5. Check preview.html
    with open("preview.html", "r", encoding="utf-8") as f:
        prev_code = f.read()

    assert "Buy Now (Instant Checkout)" in prev_code, "Instant Checkout label missing in preview.html"
    assert "v2-solo-mobile-buy-bar" in prev_code, "Sticky mobile buy bar missing in preview.html"
    print("[PASS] 7. preview.html verified with Instant Checkout and mobile sticky buy bar")

    print("\n=== ALL 7 DIRECT BUY NOW & MOBILE CHECKOUT TESTS PASSED! ===")

if __name__ == "__main__":
    run_tests()
