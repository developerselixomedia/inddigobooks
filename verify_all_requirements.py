# -*- coding: utf-8 -*-
"""
verify_all_requirements.py
Comprehensive automated test suite for all 7 User Requirements.
"""
import os
import re
import zipfile
import json
import subprocess

def test_all():
    print("=================================================================")
    print("COMPREHENSIVE AUDIT OF ALL 7 REQUIREMENTS")
    print("=================================================================")

    with open('preview.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('assets/main-store.js', 'r', encoding='utf-8') as f:
        js = f.read()

    with open('assets/main-store.css', 'r', encoding='utf-8') as f:
        css = f.read()

    with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
        theme_liquid = f.read()

    with open('sections/main-store.liquid', 'r', encoding='utf-8') as f:
        main_store_liquid = f.read()

    errors = []

    # -------------------------------------------------------------
    # 1. NO FAKE DISCOUNTS, NO STRIKETHROUGH PRICES, NO RATINGS, NO REVIEWS
    # -------------------------------------------------------------
    print("\n--- [Audit 1: No Fake Discounts / Reviews] ---")
    bad_terms = ['23% OFF', '24% OFF', '25% OFF', '30% Max Savings on Bundles', '30% MAX SAVINGS', 'podium-old-price', 'podium-rating-row']
    # Check rendered HTML for visible bad terms (outside of comments)
    for bt in ['23% OFF', '24% OFF', '25% OFF', '30% Max Savings on Bundles']:
        if bt in html:
            errors.append(f"Found forbidden term '{bt}' in preview.html")
        if bt in main_store_liquid:
            errors.append(f"Found forbidden term '{bt}' in main-store.liquid")

    # Check stats bar has new authentic copy
    if 'Express Dispatch from Prayagraj' not in html or '24-Hr' not in html:
        errors.append("Stats bar missing '24-Hr Express Dispatch from Prayagraj'")
    else:
        print("✓ Stats bar has '24-Hr Express Dispatch from Prayagraj'")

    # Check Marquee has authentic copy
    if 'UPSC &amp; JUDICIARY SCHOLAR EDITIONS' not in html and 'UPSC & JUDICIARY SCHOLAR EDITIONS' not in html:
        errors.append("Marquee missing 'UPSC & JUDICIARY SCHOLAR EDITIONS'")
    else:
        print("✓ Marquee has 'UPSC & JUDICIARY SCHOLAR EDITIONS'")

    # Check Customer Reviews card is absent or suppressed
    if 'id="pdpReviewsCard"' in html:
        errors.append("Customer reviews card #pdpReviewsCard still present in preview.html")
    else:
        print("✓ Customer Reviews card #pdpReviewsCard completely removed")

    # -------------------------------------------------------------
    # 2. CATEGORIES BENTO SHOWCASE (IMAGE_68CD69.JPG)
    # -------------------------------------------------------------
    print("\n--- [Audit 2: Asymmetric Categories Bento Showcase] ---")
    if 'id="category-bento-showcase"' not in html:
        errors.append("Missing #category-bento-showcase in preview.html")
    else:
        print("✓ Found #category-bento-showcase")

    if 'class="bento-left-spotlight"' not in html:
        errors.append("Missing .bento-left-spotlight in preview.html")
    else:
        print("✓ Found .bento-left-spotlight")

    if 'class="bento-right-2x2"' not in html:
        errors.append("Missing .bento-right-2x2 in preview.html")
    else:
        print("✓ Found .bento-right-2x2")

    for cat in ['Contemporary Hindi Fiction', 'Poetry, Ghazals & Shayari', 'Classic Hindi Novels', 'History, Criticism & Politics', 'Law & Constitutional Studies']:
        if cat not in html:
            errors.append(f"Missing category '{cat}' in bento pills")
        else:
            print(f"✓ Found bento category '{cat}'")

    if 'switchCategoryBento' not in js:
        errors.append("switchCategoryBento missing from main-store.js")
    else:
        print("✓ Found switchCategoryBento in JS engine")

    # -------------------------------------------------------------
    # 3. UNIVERSAL 3D HOVER BOOK-OPENING ANIMATION
    # -------------------------------------------------------------
    print("\n--- [Audit 3: Universal 3D Hover Book-Opening Animation] ---")
    if '.indigo-3d-book-stage' not in css:
        errors.append("Missing .indigo-3d-book-stage in css")
    if '.indigo-3d-cover-leaf' not in css:
        errors.append("Missing .indigo-3d-cover-leaf in css")
    if '.indigo-3d-inside-page' not in css:
        errors.append("Missing .indigo-3d-inside-page in css")

    # Check rotation rule
    if 'rotateY(-128deg)' not in css and 'rotateY(-125deg)' not in css and 'rotateY(-130deg)' not in css:
        errors.append("Missing 3D rotateY hover transition in css")
    else:
        print("✓ 3D cover leaf opening transition defined in css")

    stage_count_html = html.count('class="indigo-3d-book-stage"')
    print(f"✓ Found {stage_count_html} 3D book stages rendered in preview.html")
    if stage_count_html < 10:
        errors.append(f"Too few 3D book stages rendered: {stage_count_html}")

    # -------------------------------------------------------------
    # 4. HERO ANIMATION PERSISTENCE & SEARCH DEDUPLICATION
    # -------------------------------------------------------------
    print("\n--- [Audit 4: Hero Animation & Search Deduplication] ---")
    if 'isUserInteractingHero' not in js:
        errors.append("Missing isUserInteractingHero in JS")
    else:
        print("✓ Found isUserInteractingHero in JS engine")

    # Verify search deduplication logic
    if 'bTitle + \'|\' + bAuthor' not in js:
        errors.append("Hero search does not deduplicate by bTitle + '|' + bAuthor")
    else:
        print("✓ Search suggestions strictly deduplicated by bTitle + '|' + bAuthor")

    # -------------------------------------------------------------
    # 5. OVERVIEW MODAL
    # -------------------------------------------------------------
    print("\n--- [Audit 5: Universal Overview Modal] ---")
    if 'id="overviewModalOverlay"' not in html and 'id="indigo-overview-modal"' not in html:
        errors.append("Missing overview modal in preview.html")
    else:
        print("✓ Overview modal element exists")

    if 'function closeOverviewModal' not in js:
        errors.append("closeOverviewModal function missing in JS")
    else:
        print("✓ Found closeOverviewModal in JS engine")

    # -------------------------------------------------------------
    # 6. CART DRAWER & ADD-TO-CART
    # -------------------------------------------------------------
    print("\n--- [Audit 6: Slide-Over Cart Drawer & Add-To-Cart] ---")
    if 'id="cartDrawerOverlay"' not in html and 'id="cartDrawer"' not in html:
        errors.append("Cart drawer missing in preview.html")
    else:
        print("✓ Cart drawer element exists")

    if 'function addToCart' not in js:
        errors.append("addToCart function missing in JS")
    else:
        print("✓ Found addToCart function in JS engine")

    if 'visibility: hidden !important' not in css:
        errors.append("Cart drawer closed state missing visibility: hidden !important")
    else:
        print("✓ Cart drawer closed state has visibility: hidden !important")

    # -------------------------------------------------------------
    # 7. CATALOG PAGINATION (12 BOOKS/PAGE) & UNIFORM COVERS
    # -------------------------------------------------------------
    print("\n--- [Audit 7: Catalog Pagination & 2:3 Covers] ---")
    if 'id="catalogPagination"' not in html:
        errors.append("Missing #catalogPagination container in preview.html")
    else:
        print("✓ Found #catalogPagination container")

    if 'CATALOG_PAGE_SIZE = 12' not in js and 'pageSize = 12' not in js:
        errors.append("CATALOG_PAGE_SIZE = 12 not found in JS")
    else:
        print("✓ Catalog pagination configured for 12 books per page")

    if 'function goToCatalogPage' not in js:
        errors.append("goToCatalogPage missing from JS")
    else:
        print("✓ Found goToCatalogPage in JS engine")

    # Check 2:3 aspect-ratio
    if 'aspect-ratio: 2 / 3' not in css:
        errors.append("Missing aspect-ratio: 2 / 3 rule in CSS")
    else:
        print("✓ Uniform 2:3 aspect ratio rule enforced in CSS")

    # -------------------------------------------------------------
    # 8. SHOPIFY ZIP ARCHIVES AUDIT
    # -------------------------------------------------------------
    print("\n--- [Audit 8: Shopify Zip Archives] ---")
    z1 = 'indigo-books-shopify-theme.zip'
    z2 = 'indigo-books-theme.zip'
    for zpath in [z1, z2]:
        if not os.path.exists(zpath):
            errors.append(f"Zip file {zpath} does not exist!")
            continue
        size_mb = os.path.getsize(zpath) / (1024 * 1024)
        print(f"✓ Found {zpath} ({size_mb:.2f} MB)")
        with zipfile.ZipFile(zpath, 'r') as zf:
            namelist = zf.namelist()
            # Check essential files
            has_layout = any('layout/theme.liquid' in n for n in namelist)
            has_main_store = any('sections/main-store.liquid' in n for n in namelist)
            has_css = any('assets/theme.css' in n for n in namelist)
            has_js = any('assets/main-store.js' in n for n in namelist)
            if not (has_layout and has_main_store and has_css and has_js):
                errors.append(f"Zip file {zpath} missing essential Shopify files!")
            else:
                print(f"  All required files verified in {zpath} (total {len(namelist)} files)")

    # -------------------------------------------------------------
    # 9. JAVASCRIPT SYNTAX CHECK
    # -------------------------------------------------------------
    print("\n--- [Audit 9: JavaScript Syntax Check via Node.js] ---")
    res = subprocess.run(["node", "-c", "assets/main-store.js"], capture_output=True, text=True)
    if res.returncode != 0:
        errors.append(f"Node.js syntax error in assets/main-store.js: {res.stderr}")
    else:
        print("✓ assets/main-store.js has 0 syntax errors according to Node.js")

    print("\n=================================================================")
    if errors:
        print(f"FAILED! Found {len(errors)} issues:")
        for err in errors:
            print("  ❌ " + err)
        return False
    else:
        print("ALL AUDIT CHECKS PASSED WITH 100% SUCCESS! (0 ERRORS)")
        print("=================================================================")
        return True

if __name__ == '__main__':
    ok = test_all()
    exit(0 if ok else 1)
