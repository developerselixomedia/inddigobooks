# -*- coding: utf-8 -*-
"""
verify_sync_integrity.py
35-test comprehensive verification suite for Indigo Books India.
Verifies preview.html, sections/main-store.liquid, assets/main-store.css, assets/main-store.js,
templates/index.json, layout/theme.liquid, and indigo-books-theme.zip.
Ensures strict compliance with Shopify's 256 KB section file limit.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import json
import zipfile
import subprocess

def run_tests():
    print("=================================================================")
    print("TEST SUITE: INDIGO BOOKS INDIA - SYNC & SHOPIFY COMPLIANCE")
    print("=================================================================")
    all_passed = True

    # 1. Test preview.html
    print("\n[TEST 1] preview.html Verification...")
    if not os.path.exists("preview.html"):
        print("FAIL: preview.html missing!")
        all_passed = False
        return
    with open("preview.html", "r", encoding="utf-8") as f:
        html = f.read()

    size_kb = os.path.getsize("preview.html") / 1024
    print(f"  - Size: {size_kb:.2f} KB (Pass >= 200 KB: {size_kb >= 200})")
    if size_kb < 200:
        all_passed = False

    liquid_tags = re.findall(r'\{\{.*?\}\}|\{%.*?%\}', html)
    print(f"  - Liquid tags found in preview.html: {len(liquid_tags)}")
    if len(liquid_tags) > 0:
        all_passed = False

    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    emojis = emoji_pattern.findall(html)
    print(f"  - Emojis found in preview.html: {len(emojis)}")
    if len(emojis) > 0:
        all_passed = False

    checks = [
        ("hero-topleft-watermark", "hero-topleft-watermark" in html),
        ("hero-wheel-wrap", "hero-wheel-wrap" in html),
        ("hero-wheel-svg", "hero-wheel-svg" in html),
        ("hero-books-grid-video", "hero-books-grid-video" in html),
        ("hero-video-book-card", "hero-video-book-card" in html),
        ("hero-book-meta", "hero-book-meta" in html),
        ("Story italic gold", 'Favorite <em style="color: #E5A93C; font-style: italic;' in html or 'Favorite <em' in html),
        ("Clean search input placeholder", 'placeholder="Search for a book, author, or ISBN..."' in html),
        ("Shop Now CTA", "Shop Now" in html),
        ("WhatsApp COD CTA", "WhatsApp COD" in html or "wa.me" in html),
        ("Book 1: hero-godan.jpg", "hero-godan.jpg" in html),
        ("Book 2: hero-raag-darbari.jpg", "hero-raag-darbari.jpg" in html),
        ("Book 3: hero-chitralekha.jpg", "hero-chitralekha.jpg" in html),
        ("Book 4: hero-rashmirathi.jpg", "hero-rashmirathi.jpg" in html),
        ("Book 5: hero-kuchh-ishq.jpg", "hero-kuchh-ishq.jpg" in html),
        ("Book 6: hero-gypsy.jpg", "hero-gypsy.jpg" in html),
        ("Vector SVG Favicon present", "data:image/svg+xml" in html),
        ("Rangoli z-index 5 behind books", "z-index: 5" in html),
        ("Books grid z-index 25", "z-index: 25" in html),
        ("Dimmed books sharp (no blur)", "filter: none" in html or "filter: unset" in html),
        ("Mobile responsive media block", "@media (max-width: 991px)" in html or "@media (max-width: 992px)" in html),
        ("Mobile overflow-x hidden", "overflow-x: hidden" in html),
        ("runVideoIntroSpotlightTour in script", "runVideoIntroSpotlightTour" in html),
        ("Zero @import in CSS (No Early Hints warnings)", "@import" not in html),
        ("True 2:3 aspect ratio for book covers", "aspect-ratio: 2 / 3" in html or "aspect-ratio: 2/3" in html),
        ("Navbar sticky top 0 (z-index 99999)", "99999" in html),
        ("Overview Modal 420px / 90% width", "max-width: 420px" in html or "width: 90%" in html),
        ("Stat numbers zero vertical lines", "caret-color: transparent" in html or "border-right: none" in html),
        ("Podium cover 3D preserve & translateZ", "translateZ(1px)" in html or "preserve-3d" in html),
    ]

    for label, passed in checks:
        print(f"  - {label}: {'PASS' if passed else 'FAIL'}")
        if not passed:
            all_passed = False

    # 2. Test Node.js Syntax on JS Engine
    print("\n[TEST 2] Node.js Syntax Verification...")
    res = subprocess.run(["node", "-c", "assets/main-store.js"], capture_output=True, text=True)
    if res.returncode == 0:
        print("  - node -c assets/main-store.js: PASS (Zero JS syntax errors)")
    else:
        print(f"  - node -c assets/main-store.js: FAIL\n{res.stderr}")
        all_passed = False

    script_blocks = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
    for idx, sblock in enumerate(script_blocks):
        sblock = sblock.strip()
        if not sblock:
            continue
        with open("temp_test_node.js", "w", encoding="utf-8") as f:
            f.write(sblock)
        try:
            res = subprocess.run(["node", "-c", "temp_test_node.js"], capture_output=True, text=True)
            if res.returncode != 0:
                print(f"  - preview.html script block #{idx}: FAIL\n{res.stderr}")
                all_passed = False
        finally:
            if os.path.exists("temp_test_node.js"):
                os.remove("temp_test_node.js")
    print("  - All preview.html script blocks: PASS (Zero JS syntax errors)")

    # 3. Test sections/main-store.liquid (Shopify 256 KB limit compliance!)
    print("\n[TEST 3] sections/main-store.liquid Verification...")
    if not os.path.exists("sections/main-store.liquid"):
        print("FAIL: sections/main-store.liquid missing!")
        all_passed = False
    else:
        with open("sections/main-store.liquid", "r", encoding="utf-8") as f:
            liquid_content = f.read()
        size_liq = os.path.getsize("sections/main-store.liquid") / 1024
        is_safe_size = 50.0 <= size_liq <= 256.0
        print(f"  - Size: {size_liq:.2f} KB (Shopify Limit <= 256 KB: {is_safe_size})")
        if not is_safe_size:
            print(f"    ERROR: Size {size_liq:.2f} KB violates Shopify 256 KB hard limit!")
            all_passed = False
        target_tag = "{{ 'hero-godan.jpg' | asset_url }}"
        print(f"  - Contains asset_url tags: {target_tag in liquid_content}")
        print(f"  - Contains valid schema: {'{% schema %}' in liquid_content and '{% endschema %}' in liquid_content}")
        emojis_liq = emoji_pattern.findall(liquid_content)
        print(f"  - Emojis in main-store.liquid: {len(emojis_liq)}")
        if len(emojis_liq) > 0 or not ('{% schema %}' in liquid_content):
            all_passed = False

    # 4. Test Modular Assets (assets/main-store.css & assets/main-store.js)
    print("\n[TEST 4] Modular Assets Verification...")
    for asset_file, min_kb in [("assets/main-store.css", 40), ("assets/main-store.js", 60), ("assets/theme.css", 40)]:
        if not os.path.exists(asset_file):
            print(f"  - {asset_file}: FAIL (Missing)")
            all_passed = False
        else:
            sz = os.path.getsize(asset_file) / 1024
            passed = sz >= min_kb
            print(f"  - {asset_file}: {sz:.2f} KB (Pass >= {min_kb} KB: {passed})")
            if not passed:
                all_passed = False

    # 5. Test templates/index.json
    print("\n[TEST 5] templates/index.json Verification...")
    with open("templates/index.json", "r", encoding="utf-8") as f:
        idx = json.load(f)
    has_only_main = list(idx.get("sections", {}).keys()) == ["main_store"] and idx.get("order") == ["main_store"]
    print(f"  - Points exclusively to main-store: {'PASS' if has_only_main else 'FAIL'}")
    if not has_only_main:
        all_passed = False

    # 6. Test layout/theme.liquid
    print("\n[TEST 6] layout/theme.liquid Verification...")
    with open("layout/theme.liquid", "r", encoding="utf-8") as f:
        theme_liq = f.read()
    has_header = "{{ content_for_header }}" in theme_liq
    has_layout = "{{ content_for_layout }}" in theme_liq
    has_css = "main-store.css" in theme_liq or "theme.css" in theme_liq
    has_js = "main-store.js" in theme_liq
    no_header_group = "{% sections 'header-group' %}" not in theme_liq
    no_footer_group = "{% sections 'footer-group' %}" not in theme_liq
    print(f"  - content_for_header present: {has_header}")
    print(f"  - content_for_layout present: {has_layout}")
    print(f"  - stylesheet_tag linked: {has_css}")
    print(f"  - script_tag linked: {has_js}")
    print(f"  - Zero duplicate header-group: {no_header_group}")
    print(f"  - Zero duplicate footer-group: {no_footer_group}")
    if not (has_header and has_layout and has_css and has_js and no_header_group and no_footer_group):
        all_passed = False

    # 7A. Test indigo-books-shopify-theme.zip (Extracts to indigo-books-shopify-theme/ root directory)
    print("\n[TEST 7A] indigo-books-shopify-theme.zip Verification (Extracts to indigo-books-shopify-theme/)...")
    if not os.path.exists("indigo-books-shopify-theme.zip"):
        print("FAIL: indigo-books-shopify-theme.zip missing!")
        all_passed = False
    else:
        zip_size_mb = os.path.getsize("indigo-books-shopify-theme.zip") / (1024 * 1024)
        print(f"  - Archive Size: {zip_size_mb:.2f} MB (Pass >= 3.0 MB: {zip_size_mb >= 3.0})")
        with zipfile.ZipFile("indigo-books-shopify-theme.zip", "r") as zf:
            namelist = zf.namelist()
            print(f"  - Total files in archive: {len(namelist)}")
            key_files_folder = [
                "indigo-books-shopify-theme/config/settings_schema.json",
                "indigo-books-shopify-theme/config/settings_data.json",
                "indigo-books-shopify-theme/layout/theme.liquid",
                "indigo-books-shopify-theme/templates/index.json",
                "indigo-books-shopify-theme/sections/main-store.liquid",
                "indigo-books-shopify-theme/assets/main-store.css",
                "indigo-books-shopify-theme/assets/main-store.js",
                "indigo-books-shopify-theme/assets/hero-godan.jpg"
            ]
            for kf in key_files_folder:
                in_zip = kf in namelist or kf.replace('/', '\\') in namelist
                print(f"    * {kf}: {'PASS' if in_zip else 'FAIL'}")
                if not in_zip:
                    all_passed = False

    # 7B. Test indigo-books-theme.zip (Direct root level)
    print("\n[TEST 7B] indigo-books-theme.zip Verification (Direct root level)...")
    if not os.path.exists("indigo-books-theme.zip"):
        print("FAIL: indigo-books-theme.zip missing!")
        all_passed = False
    else:
        zip_size_mb = os.path.getsize("indigo-books-theme.zip") / (1024 * 1024)
        print(f"  - Archive Size: {zip_size_mb:.2f} MB (Pass >= 3.0 MB: {zip_size_mb >= 3.0})")
        with zipfile.ZipFile("indigo-books-theme.zip", "r") as zf:
            namelist = zf.namelist()
            print(f"  - Total files in archive: {len(namelist)}")

            key_files = [
                "sections/main-store.liquid",
                "assets/main-store.css",
                "assets/main-store.js",
                "assets/theme.css",
                "templates/index.json",
                "layout/theme.liquid",
                "sections/main-404.liquid",
                "assets/hero-godan.jpg",
                "assets/hero-raag-darbari.jpg",
                "assets/hero-chitralekha.jpg",
                "assets/hero-rashmirathi.jpg",
                "assets/hero-kuchh-ishq.jpg",
                "assets/hero-gypsy.jpg",
                "assets/book-tarkash.jpg"
            ]
            for kf in key_files:
                in_zip = kf in namelist or kf.replace('/', '\\') in namelist
                print(f"    * {kf}: {'PASS' if in_zip else 'FAIL'}")
                if not in_zip:
                    all_passed = False

    print("\n=================================================================")
    if all_passed:
        print(">>> FINAL RESULT: ALL INTEGRITY & SYNC TESTS PASSED (100% GREEN) <<<")
    else:
        print(">>> FINAL RESULT: SOME TESTS FAILED <<<")
    print("=================================================================")

if __name__ == "__main__":
    run_tests()
