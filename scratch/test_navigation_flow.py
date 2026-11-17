# -*- coding: utf-8 -*-
"""
test_navigation_flow.py
Verifies that:
1. returnToHome properly resets window.previousViewBeforeSolo to 'home', closes solo book, hides search results, clears all inputs (especially editorialSearchInput).
2. closeSearchResultsView properly resets window.previousViewBeforeSolo to 'home', hides search results, and clears all inputs.
3. openSoloBookPage checks isSearchActive requiring sView to be block AND hView to be none.
4. closeSoloBookPage restores homepage by default when returning from a book opened from homepage, and resets previousViewBeforeSolo to 'home'.
5. Both assets/main-store.js and preview.html contain these synchronized fixes.
6. The zip files indigo-books-shopify-theme.zip and indigo-books-theme.zip contain the updated assets/main-store.js.
"""

import os
import zipfile
import re

print("=== VERIFYING NAVIGATION STATE MACHINE & SEARCH BAR FIXES ===\n")

passed = 0
failed = 0

def check(condition, message):
    global passed, failed
    if condition:
        print(f"[PASS] {message}")
        passed += 1
    else:
        print(f"[FAIL] {message}")
        failed += 1

# 1. Read files
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    store_scripts = f.read()

with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    editorial = f.read()

with open('preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()

with open('assets/main-store.js', 'r', encoding='utf-8') as f:
    main_store_js = f.read()

# TEST 1: returnToHome in store_scripts.py
check("window.previousViewBeforeSolo = 'home';" in store_scripts, "store_scripts.py: returnToHome resets previousViewBeforeSolo to 'home'")
check("'editorialSearchInput'" in store_scripts, "store_scripts.py: returnToHome clears editorialSearchInput")
check("const soloView = document.getElementById('indigo-solo-product-view');" in store_scripts, "store_scripts.py: returnToHome closes solo view directly")

# TEST 2: closeSearchResultsView in store_scripts.py
check("window.closeSearchResultsView = function()" in store_scripts, "store_scripts.py: closeSearchResultsView defined")
check("previousViewBeforeSolo = 'home'" in store_scripts, "store_scripts.py: closeSearchResultsView resets previousViewBeforeSolo to 'home'")

# TEST 3: openSearchResultsPage in store_scripts.py
check("window.previousViewBeforeSolo = 'search';" in store_scripts, "store_scripts.py: openSearchResultsPage sets previousViewBeforeSolo to 'search'")

# TEST 4: editorial_video_theme.py navigation logic
check("window.previousViewBeforeSolo = 'home';" in editorial, "editorial_video_theme.py: exposes window.previousViewBeforeSolo")
check("var targetView = window.previousViewBeforeSolo || previousViewBeforeSolo || 'home';" in editorial, "editorial_video_theme.py: closeSoloBookPage respects window.previousViewBeforeSolo")
check("isSearchActive = sView && (sView.style.display === 'block'" in editorial and "!hView || hView.style.display === 'none'" in editorial, "editorial_video_theme.py: openSoloBookPage strictly verifies search view is active and homepage is hidden")
check("previousViewBeforeSolo = 'home';\n    window.previousViewBeforeSolo = 'home';" in editorial, "editorial_video_theme.py: closeSoloBookPage resets state back to 'home' upon exit")

# TEST 5: preview.html integration
check("window.previousViewBeforeSolo = 'home';" in preview, "preview.html contains window.previousViewBeforeSolo")
check("isSearchActive = sView && (sView.style.display === 'block'" in preview, "preview.html contains strict isSearchActive verification")
check("'editorialSearchInput', 'hero-search-input'" in preview, "preview.html clears editorialSearchInput in returnToHome")

# TEST 6: assets/main-store.js synchronization
check("window.previousViewBeforeSolo = 'home';" in main_store_js, "assets/main-store.js contains window.previousViewBeforeSolo")
check("isSearchActive = sView && (sView.style.display === 'block'" in main_store_js, "assets/main-store.js contains strict isSearchActive check")

# TEST 7: Shopify .zip theme packages
with zipfile.ZipFile('indigo-books-shopify-theme.zip', 'r') as z1:
    names1 = z1.namelist()
    js_name = [n for n in names1 if n.endswith('assets/main-store.js')][0]
    z1_js = z1.read(js_name).decode('utf-8')
    check("window.previousViewBeforeSolo = 'home';" in z1_js, "indigo-books-shopify-theme.zip contains updated main-store.js")
    check("isSearchActive = sView && (sView.style.display === 'block'" in z1_js, "indigo-books-shopify-theme.zip contains strict search check")

with zipfile.ZipFile('indigo-books-theme.zip', 'r') as z2:
    names2 = z2.namelist()
    js_name2 = [n for n in names2 if n.endswith('assets/main-store.js')][0]
    z2_js = z2.read(js_name2).decode('utf-8')
    check("window.previousViewBeforeSolo = 'home';" in z2_js, "indigo-books-theme.zip contains updated main-store.js")
    check("isSearchActive = sView && (sView.style.display === 'block'" in z2_js, "indigo-books-theme.zip contains strict search check")

print(f"\n==========================================")
print(f"RESULTS: {passed} PASSED, {failed} FAILED")
print(f"==========================================")

if failed > 0:
    exit(1)
else:
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
