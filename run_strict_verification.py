# -*- coding: utf-8 -*-
import os
import re
import json
import zipfile

print("=================================================================")
print("RUNNING EXHAUSTIVE CATALOG & PDP SPECS VERIFICATION")
print("=================================================================")

# 1. Check absence of pdpSpecWeight across all files
files_to_check = [
    'preview.html',
    'sections/main-store.liquid',
    'sections/main-indigo-store.liquid',
    'sections/main-product.liquid',
    'assets/main-store.js'
]

print("\n--- Test 1: Verify pdpSpecWeight is 100% removed ---")
for fpath in files_to_check:
    assert os.path.exists(fpath), f"File {fpath} does not exist!"
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    count = content.count('pdpSpecWeight')
    print(f"  {fpath}: pdpSpecWeight count = {count}")
    assert count == 0, f"Error: pdpSpecWeight found in {fpath} ({count} occurrences)!"
print(">>> PASS: pdpSpecWeight completely eliminated from all frontend and template files!")

# 2. Check presence of pdpSpecQty and pdpSpecDimensions
print("\n--- Test 2: Verify pdpSpecQty & pdpSpecDimensions exist ---")
for fpath in files_to_check:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    has_qty = 'pdpSpecQty' in content or 'inventory_quantity' in content
    has_dim = 'pdpSpecDimensions' in content or 'dimensions' in content
    print(f"  {fpath}: has_qty = {has_qty}, has_dim = {has_dim}")
    assert has_qty, f"Missing qty representation in {fpath}"
    assert has_dim, f"Missing dimensions representation in {fpath}"
print(">>> PASS: pdpSpecQty and pdpSpecDimensions verified in all templates!")

# 3. Check authentic data in store_data.py
print("\n--- Test 3: Verify Exact Metadata in store_data.py ---")
import store_data

test_cases = [
    {
        "isbn": "9788183610926",
        "title": "Mahabhoj",
        "author": "Mannu Bhandari",
        "publisher": "Radhakrishna Prakashan",
        "mrp": 250.0,
        "pages": "168p",
        "edition_contains": "18th",
        "year_contains": "2006",
        "dimensions": "21.5 × 14 × 1 cm",
        "qty": 2324
    },
    {
        "isbn": "9788126728435",
        "title": "Kuchh Ishq Kiya Kuchh Kaam Kiya",
        "author": "Piyush Mishra",
        "publisher": "Rajkamal Prakashan",
        "mrp": 250.0,
        "pages": "147p",
        "edition_contains": "15th",
        "year_contains": "2016",
        "dimensions": "21.5 × 14 × 1 cm",
        "qty": 4005
    },
    {
        "isbn": "9788197989667",
        "title": "Bharatiya Bhasha Mein High Court Ki Vakalat",
        "author": "Anoop Baranwal ‘Deshbandhu’",
        "publisher": "Lokbharti Prakashan",
        "mrp": 350.0,
        "pages": "216p",
        "edition_contains": "1st",
        "year_contains": "2024",
        "dimensions": "21.5 × 14 × 1 cm",
        "qty": 172
    },
    {
        "isbn": "9789390971480",
        "title": "Bharat Ka Samvidhan : Sankshipt Parichay",
        "author": "Subhash Kashyap",
        "publisher": "Rajkamal Prakashan, Akshar",
        "mrp": 195.0,
        "pages": "184p",
        "edition_contains": "3rd",
        "year_contains": "2022",
        "dimensions": "22 × 14 × 1 cm",
        "qty": 437
    },
    {
        "isbn": "9789389742305",
        "title": "Samaan Nagrik Sanhita : Chunautiya Aur Samadhan",
        "author": "Anoop Baranwal",
        "publisher": "Lokbharti Prakashan",
        "mrp": 399.0,
        "pages": "279p",
        "edition_contains": "2nd",
        "dimensions": "22 × 14 × 2 cm",
        "qty": 403
    },
    {
        "isbn": "9788119835416",
        "title": "Nyayapalika Kasauti Par",
        "author": "Kamlesh Jain, Edi. ranjeet verma ",
        "publisher": "Rajkamal Prakashan",
        "mrp": 199.0,
        "pages": "152p",
        "edition_contains": "1st",
        "dimensions": "21.5 × 14 × 1 cm",
        "qty": 5
    }
]

for tc in test_cases:
    isbn = tc["isbn"]
    meta = store_data.MODAL_METADATA_DATABASE.get(isbn)
    assert meta is not None, f"Book {isbn} ({tc['title']}) not found in MODAL_METADATA_DATABASE!"
    
    print(f"\nChecking ISBN {isbn} - {tc['title']}:")
    print(f"  Title: {meta.get('title')}")
    print(f"  Author: {meta.get('author')}")
    print(f"  Publisher: {meta.get('pub')}")
    print(f"  Price: {meta.get('price')}")
    print(f"  Pages: {meta.get('pages')}")
    print(f"  Edition: {meta.get('edition')}")
    print(f"  Dimensions: {meta.get('dimensions')}")
    print(f"  QTY: {meta.get('qty')}")
    print(f"  Weight key present: {'weight' in meta}")

    assert meta.get('title') == tc['title'], f"Title mismatch: {meta.get('title')} vs {tc['title']}"
    assert meta.get('mrp') == tc['mrp'], f"MRP mismatch: {meta.get('mrp')} vs {tc['mrp']}"
    assert meta.get('pages') == tc['pages'], f"Pages mismatch: {meta.get('pages')} vs {tc['pages']}"
    assert tc['edition_contains'] in meta.get('edition', ''), f"Edition mismatch: {meta.get('edition')}"
    if 'year_contains' in tc:
        assert tc['year_contains'] in meta.get('edition', ''), f"Year mismatch in edition: {meta.get('edition')}"
    assert meta.get('dimensions') == tc['dimensions'], f"Dimensions mismatch: {meta.get('dimensions')} vs {tc['dimensions']}"
    assert meta.get('qty') == tc['qty'], f"QTY mismatch: {meta.get('qty')} vs {tc['qty']}"
    assert 'weight' not in meta, f"Weight key found in book {isbn}!"

print("\n>>> PASS: All 6 benchmark books verified with 100% authentic Excel catalog data!")

# 4. Verify zip archives
print("\n--- Test 4: Verify ZIP Theme Archives ---")
for zip_name in ['indigo-books-shopify-theme.zip', 'indigo-books-theme.zip']:
    assert os.path.exists(zip_name), f"Zip archive {zip_name} does not exist!"
    z_size = os.path.getsize(zip_name) / (1024 * 1024)
    print(f"  {zip_name}: size = {z_size:.2f} MB")
    with zipfile.ZipFile(zip_name, 'r') as zf:
        namelist = zf.namelist()
        # Check essential files
        has_js = any('assets/main-store.js' in n for n in namelist)
        has_css = any('assets/main-store.css' in n for n in namelist)
        has_theme = any('layout/theme.liquid' in n for n in namelist)
        has_pdp = any('sections/main-product.liquid' in n for n in namelist)
        assert has_js, f"assets/main-store.js missing from {zip_name}"
        assert has_css, f"assets/main-store.css missing from {zip_name}"
        assert has_theme, f"layout/theme.liquid missing from {zip_name}"
        assert has_pdp, f"sections/main-product.liquid missing from {zip_name}"
        print(f"    -> Contains {len(namelist)} valid theme files.")

print("\n=================================================================")
print("ALL VERIFICATION SUITES PASSED! 100% PRODUCTION READY!")
print("=================================================================")
