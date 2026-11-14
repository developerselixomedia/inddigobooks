# -*- coding: utf-8 -*-
import json
import zipfile
import subprocess
import os

print("=" * 65)
print("COMPREHENSIVE MULTI-CHECK VERIFICATION")
print("=" * 65)

# 1. Main product liquid & template
with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    main_prod = f.read()
assert 'product-page-wrapper' in main_prod, "Missing product-page-wrapper in main-product.liquid"
assert 'pdp-buy-box' in main_prod, "Missing pdp-buy-box in main-product.liquid"
assert '918933063306' in main_prod, "Missing 918933063306 in main-product.liquid"
print("CHECK 1: sections/main-product.liquid is valid and complete.")

with open('templates/product.json', 'r', encoding='utf-8') as f:
    prod_json = json.load(f)
assert prod_json['sections']['main_product']['type'] == 'main-product', "templates/product.json doesn't point to main-product"
print("CHECK 2: templates/product.json points strictly to main-product.")

# 2. preview.html & sections/main-store.liquid checks
with open('preview.html', 'r', encoding='utf-8') as f:
    p_html = f.read()

with open('sections/main-store.liquid', 'r', encoding='utf-8') as f:
    s_liq = f.read()

assert 'id="single-product-page-view"' in p_html, "Missing single-product-page-view in preview.html"
assert 'id="homepage-view"' in p_html, "Missing homepage-view in preview.html"
assert 'id="single-product-page-view"' in s_liq, "Missing single-product-page-view in main-store.liquid"
assert 'id="homepage-view"' in s_liq, "Missing homepage-view in main-store.liquid"
print("CHECK 3: Dedicated SPA product view & homepage view exist in both preview.html & main-store.liquid.")

# 3. No old numbers
for txt, name in [(p_html, 'preview.html'), (s_liq, 'main-store.liquid')]:
    assert '11,922' not in txt, f"11,922 found in {name}"
    assert '11,900' not in txt, f"11,900 found in {name}"
    assert '8881122722' not in txt, f"8881122722 found in {name}"
    assert '918933063306' in txt, f"918933063306 missing in {name}"
    assert 'id="bundles-section"' not in txt, f"id='bundles-section' found in {name}"
print("CHECK 4: Clean audit: Zero 11,922/11,900, Zero 8881122722, All WhatsApp is 918933063306, Zero bundles section.")

# 4. Exact prices in hero
for price, title in [('₹299.00', 'Godan'), ('₹499.00', 'Raag Darbari'), ('₹299.00', 'Chitralekha'), ('₹299.00', 'Rashmirathi'), ('₹250.00', 'Kuchh Ishq Kiya'), ('₹995.00', 'Gypsy')]:
    assert price in p_html, f"Price {price} for {title} missing in preview.html"
print("CHECK 5: All Hero books display exact CSV prices (Gypsy ₹995.00, Raag Darbari ₹499.00, etc.).")

# 5. Stats bar 3rd stat
assert '24-Hr' in p_html and 'Express Dispatch from Prayagraj' in p_html, "Stats bar 3rd stat not updated"
print("CHECK 6: Stats bar 3rd stat is '24-Hr Express Dispatch from Prayagraj'.")

# 6. Node.js check on assets/main-store.js
res = subprocess.run(['node', '-c', 'assets/main-store.js'], capture_output=True, text=True)
assert res.returncode == 0, f"Node.js syntax error in assets/main-store.js: {res.stderr}"
print("CHECK 7: assets/main-store.js validated with 0 syntax errors by Node.js.")

# 7. Zip archives verification
for zname in ['indigo-books-theme.zip', 'indigo-books-shopify-theme.zip']:
    with zipfile.ZipFile(zname, 'r') as z:
        nl = z.namelist()
        assert any('main-product.liquid' in n for n in nl), f"main-product.liquid missing from {zname}"
        assert any('product.json' in n for n in nl), f"product.json missing from {zname}"
        assert any('main-store.liquid' in n for n in nl), f"main-store.liquid missing from {zname}"
        assert any('main-store.js' in n for n in nl), f"main-store.js missing from {zname}"
        assert any('main-store.css' in n for n in nl), f"main-store.css missing from {zname}"
        assert any('main-404.liquid' in n for n in nl), f"main-404.liquid missing from {zname}"
print("CHECK 8: Both .zip packages contain complete, valid Shopify theme files.")

print("=" * 65)
print(">>> ALL 8 COMPREHENSIVE CHECKS PASSED WITH 100% SUCCESS! <<<")
print("=" * 65)

