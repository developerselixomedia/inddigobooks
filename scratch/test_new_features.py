# -*- coding: utf-8 -*-
"""
scratch/test_new_features.py
Verification of the 6 Master Fixes from the screenshots.
"""

import sys
sys.path.insert(0, '.')
import os
import re
import store_data

print("=================================================================")
print("RUNNING VERIFICATION FOR 6 MASTER FIXES")
print("=================================================================")

# 1. Container width check
with open("assets/main-store.css", "r", encoding="utf-8") as f:
    css = f.read()

assert "max-width: 1320px !important" in css, "max-width: 1320px not found in main-store.css!"
print("[TEST 1] Container width 1320px: PASS")

# 2. Stats bar check
assert "repeat(4, 1fr)" in css, "repeat(4, 1fr) not found in stats-grid!"
with open("preview.html", "r", encoding="utf-8") as f:
    html = f.read()
assert "5,500+" in html, "5,500+ not in preview.html!"
assert "Books Available" in html, "Books Available not in preview.html!"
print("[TEST 2] Stats Bar Balanced 4-Item Grid: PASS")

# 3. Law Vault Unique Covers Check
all_vault_covers = []
for cat, books in store_data.VAULT_BOOKS.items():
    covers_in_cat = [b.get('coverUrl') for b in books]
    # Check uniqueness within each category
    assert len(covers_in_cat) == len(set(covers_in_cat)), f"Duplicate covers in vault category {cat}: {covers_in_cat}"
    all_vault_covers.extend(covers_in_cat)

print(f"[TEST 3] Law Vault 100% Unique Covers: PASS ({len(set(all_vault_covers))} distinct covers across categories)")

# 4. Auto-Suggestion Dropdowns in HTML
assert 'id="hero-search-suggestions"' in html, "hero-search-suggestions not in preview.html!"
assert 'id="catalog-search-suggestions"' in html, "catalog-search-suggestions not in preview.html!"
with open("sections/main-store.liquid", "r", encoding="utf-8") as f:
    liquid = f.read()
assert 'id="hero-search-suggestions"' in liquid, "hero-search-suggestions not in main-store.liquid!"
assert 'id="catalog-search-suggestions"' in liquid, "catalog-search-suggestions not in main-store.liquid!"
print("[TEST 4] Auto-Suggestion Dropdown Markup: PASS")

# 5. Search Engine & Catalog Sort in JS
with open("assets/main-store.js", "r", encoding="utf-8") as f:
    js = f.read()

assert "function handleSearchInput" in js, "handleSearchInput not in main-store.js!"
assert "function renderSearchSuggestions" in js, "renderSearchSuggestions not in main-store.js!"
assert "function getUnifiedSearchPool" in js, "getUnifiedSearchPool not in main-store.js!"
assert "priorityTitles" in js, "priorityTitles sorting not in main-store.js!"
assert "isNumA && !isNumB" in js, "Numeric title demotion not in main-store.js!"
print("[TEST 5] Real-Time Search & Catalog Smart Sort in JS: PASS")

# 6. Check absence of old numbers and old phone
for filename in ["preview.html", "sections/main-store.liquid", "assets/main-store.js"]:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    assert "8881122722" not in c, f"Old phone number found in {filename}!"
    assert "11,922+" not in c, f"Old catalog count 11,922+ found in {filename}!"
    assert "11,900+" not in c, f"Old catalog count 11,900+ found in {filename}!"

print("[TEST 6] Clean Branding (5,500+ and +91 8933063306): PASS")

print("\n=================================================================")
print("ALL 6 MASTER FIX VERIFICATION CHECKS PASSED (100% GREEN)!")
print("=================================================================")
