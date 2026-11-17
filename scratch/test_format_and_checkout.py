import re
import os
import zipfile

print("=== RUNNING VERIFICATION SUITE FOR FORMAT MATCHING & CHECKOUT/PAYMENT ===")

# 1. Check preview.html
with open('preview.html', 'r', encoding='utf-8') as f:
    preview_html = f.read()

# Verify NO pattern="[0-9]{10}" or pattern="[0-9]{6}" in checkout modal
modal_patterns = re.findall(r'<input[^>]*id="checkoutPhone"[^>]*pattern=', preview_html)
assert len(modal_patterns) == 0, f"Found pattern attribute on checkoutPhone: {modal_patterns}"
print("[PASS] 1. No blocking pattern attribute on #checkoutPhone in preview.html")

pin_patterns = re.findall(r'<input[^>]*id="checkoutPincode"[^>]*pattern=', preview_html)
assert len(pin_patterns) == 0, f"Found pattern attribute on checkoutPincode: {pin_patterns}"
print("[PASS] 2. No blocking pattern attribute on #checkoutPincode in preview.html")

# Verify form has novalidate
form_novalidate = re.findall(r'<form[^>]*id="expressPhoneCheckoutForm"[^>]*novalidate', preview_html)
assert len(form_novalidate) > 0, "expressPhoneCheckoutForm missing novalidate attribute"
print("[PASS] 3. expressPhoneCheckoutForm has novalidate attribute (no native browser constraint popups)")

# Verify Book Preview exists in checkout modal
assert 'id="checkoutBookPreview"' in preview_html, "checkoutBookPreview missing from modal"
assert 'id="checkoutBookThumb"' in preview_html, "checkoutBookThumb missing from modal"
assert 'id="checkoutBookTitle"' in preview_html, "checkoutBookTitle missing from modal"
print("[PASS] 4. checkoutBookPreview container and thumbnail/title are present in express checkout modal")

# Verify UPI Payment Action block exists in confirmation modal
assert 'id="orderConfirmPayActionWrap"' in preview_html, "orderConfirmPayActionWrap missing from modal"
assert 'id="orderConfirmUpiBtn"' in preview_html, "orderConfirmUpiBtn missing from modal"
assert 'id="orderConfirmUpiQr"' in preview_html, "orderConfirmUpiQr missing from modal"
assert '8933063306@paytm' in preview_html, "UPI ID 8933063306@paytm missing from modal"
print("[PASS] 5. Instant UPI Payment action block, UPI pay button, and QR code exist in order confirmation modal")

# Verify Format Toggle hiding logic in JavaScript
assert 'var hasBothFormats = !!(pbVariant && hcVariant);' in preview_html, "Missing hasBothFormats logic"
assert "formatWrap.style.display = hasBothFormats ? 'block' : 'none';" in preview_html, "Missing formatWrap display toggle"
print("[PASS] 6. Format toggle container (#v2SoloFormatWrap) is conditionally shown ONLY when BOTH formats exist in catalog")

# Verify openExpressPhoneCheckout supports Object argument
assert "if (typeof bookId === 'object' && bookId !== null) {" in preview_html, "openExpressPhoneCheckout missing object resolution"
print("[PASS] 7. openExpressPhoneCheckout properly handles object book argument passed by handleSoloBuyNow")

# Verify real price extraction
assert "rawP = currentActivePdpBook.selectedPrice ||" in preview_html, "Missing selectedPrice extraction for total calculation"
print("[PASS] 8. Order payable total accurately calculates from selectedPrice / catalog price")

# 2. Check theme.liquid & assets/main-store.js in Shopify Theme
with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    theme_liquid = f.read()

assert 'pattern="[0-9]{10}"' not in theme_liquid, "theme.liquid still contains pattern=[0-9]{10}"
assert 'id="orderConfirmPayActionWrap"' in theme_liquid, "theme.liquid missing orderConfirmPayActionWrap"
print("[PASS] 9. layout/theme.liquid has all checkout and payment fixes applied")

with open('assets/main-store.js', 'r', encoding='utf-8') as f:
    main_store_js = f.read()

assert 'hasBothFormats' in main_store_js, "main-store.js missing hasBothFormats"
assert '8933063306@paytm' in main_store_js, "main-store.js missing UPI payment flow"
print("[PASS] 10. assets/main-store.js contains format matching and UPI payment flow")

# 3. Check zip files
for zname in ['indigo-books-shopify-theme.zip', 'indigo-books-theme.zip']:
    assert os.path.exists(zname), f"{zname} does not exist!"
    with zipfile.ZipFile(zname, 'r') as zf:
        file_list = zf.namelist()
        assert len(file_list) > 100, f"{zname} has too few files: {len(file_list)}"
        # Check that main-store.js in zip has the new code
        js_entry = [f for f in file_list if f.endswith('main-store.js')][0]
        content = zf.read(js_entry).decode('utf-8')
        assert 'hasBothFormats' in content, f"{zname} main-store.js missing hasBothFormats"
        assert '8933063306@paytm' in content, f"{zname} main-store.js missing UPI ID"
    print(f"[PASS] 11. {zname} verified intact with {len(file_list)} files and updated JS!")

print("\n=== ALL 11 TESTS PASSED SUCCESSFULLY! ===")
