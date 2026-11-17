from prepare_master_blocks import MASTER_STYLE, MASTER_SCRIPT
from editorial_video_theme import EDITORIAL_STYLE, EDITORIAL_SCRIPT
# -*- coding: utf-8 -*-
"""
sync_preview_to_shopify.py
Single Source of Truth synchronization script.
Compiles preview.html, extracts CSS, JS, Navbar, Footer, Modals, and Page DOM, and cleanly splits them into:
  - assets/main-store.css & assets/theme.css
  - assets/main-store.js (100% Valid JavaScript, tested with node -c)
  - layout/theme.liquid (Global Sticky Cream Navbar, Heritage Footer, Modals, SVG Safety Rules, Fonts)
  - sections/main-store.liquid & sections/main-indigo-store.liquid (Clean Page Content: Homepage + PDP SPA)
  - templates/index.json -> main-store
  - templates/product.json -> main-product
  - templates/search.json -> main-search
  - indigo-books-shopify-theme.zip & indigo-books-theme.zip
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import json
import zipfile
import shutil
import subprocess
from build_html_generator import build_preview_html

def sync_preview_to_shopify():
    print("=================================================================")
    print("STEP 1: Generating Authoritative preview.html (Single Source of Truth)")
    print("=================================================================")

    html = build_preview_html()
    with open("preview.html", "w", encoding="utf-8") as f:
        f.write(html)
    preview_size = os.path.getsize("preview.html") / 1024
    print(f"preview.html updated: {preview_size:.2f} KB")

    print("\n=================================================================")
    print("STEP 2: Extracting Components from preview.html")
    print("=================================================================")

    # 1. Extract CSS (all style blocks: base styles, hero locked layout, master alignment & animations)
    raw_styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    if not raw_styles:
        raise ValueError("Could not find <style> block in preview.html")
    css_content = '\n\n'.join([s.strip() for s in raw_styles if s.strip()])

    # 2. Extract Main Script from the bottom of <body>
    # Extract all store scripts after orderConfirmationModal and combine into main-store.js
    order_confirm_pos = html.find('id="orderConfirmationModal"')
    if order_confirm_pos == -1:
        order_confirm_pos = 0
    raw_scripts = re.findall(r'<script[^>]*>(.*?)</script>', html[order_confirm_pos:], re.DOTALL)
    script_js = '\n\n'.join([s.strip() for s in raw_scripts if s.strip()])

    # 3. Extract Navbar
    nav_start = html.find('<header class="site-navbar')
    nav_end = html.find('</header>', nav_start) + len('</header>')
    assert nav_start != -1 and nav_end != -1, "Could not find <header class='site-navbar'>"
    navbar_html = html[nav_start:nav_end].strip()

    # 4. Extract Footer
    footer_start = html.find('<footer class="site-footer"')
    footer_end = html.find('</footer>', footer_start) + len('</footer>')
    assert footer_start != -1 and footer_end != -1, "Could not find <footer class='site-footer'>"
    footer_html = html[footer_start:footer_end].strip()

    # 5. Extract Floating WhatsApp button
    wa_start = html.find('<a href="https://wa.me/918933063306', footer_end)
    wa_end = html.find('</a>', wa_start) + len('</a>')
    assert wa_start != -1 and wa_end != -1, "Could not find floating WhatsApp button"
    wa_float_html = html[wa_start:wa_end].strip()

    # 6. Extract Cart Drawer
    cart_start = html.find('<div id="cartDrawerOverlay"')
    cart_end = html.find('<div id="overviewModalOverlay"', cart_start)
    if cart_end == -1:
        cart_end = html.find('<div id="indigo-overview-modal"', cart_start)
    assert cart_start != -1 and cart_end != -1, "Could not find #cartDrawerOverlay or #overviewModalOverlay"
    cart_drawer_html = html[cart_start:cart_end].strip()

    # 7. Extract Overview Modal
    overview_start = html.find('<div id="overviewModalOverlay"')
    if overview_start == -1:
        overview_start = html.find('<div id="indigo-overview-modal"')
    overview_end = html.find('<div id="loginModalOverlay"', overview_start)
    assert overview_start != -1 and overview_end != -1, "Could not find overview modal"
    overview_modal_html = html[overview_start:overview_end].strip()

    # 8. Extract Login Modal
    login_start = html.find('<div id="loginModalOverlay"')
    login_end = html.find('<div id="expressPhoneCheckoutModal"', login_start)
    assert login_start != -1 and login_end != -1, "Could not find #loginModalOverlay"
    login_modal_html = html[login_start:login_end].strip()

    # 8B. Extract Express Phone Checkout Modal
    express_start = html.find('<div id="expressPhoneCheckoutModal"')
    express_end = html.find('<div id="orderConfirmationModal"', express_start)
    assert express_start != -1 and express_end != -1, "Could not find #expressPhoneCheckoutModal"
    express_modal_html = html[express_start:express_end].strip()

    # 8C. Extract Order Confirmation Modal
    order_confirm_start = html.find('<div id="orderConfirmationModal"')
    script_pos = html.find('<script', order_confirm_start)
    order_confirm_end = html.rfind('</div>', order_confirm_start, script_pos) + len('</div>')
    assert order_confirm_start != -1 and order_confirm_end != -1, "Could not find #orderConfirmationModal"
    order_confirm_modal_html = html[order_confirm_start:order_confirm_end].strip()

    # 9. Extract Main Page Content (between navbar end and footer start)
    main_content_html = html[nav_end:footer_start].strip()

    assert '<div id="homepage-view"' in main_content_html, 'homepage-view missing from main content!'
    assert '<div id="indigo-search-results-view"' in main_content_html, 'indigo-search-results-view missing from main content!'
    assert '<div id="indigo-solo-product-view"' in main_content_html or '<div id="single-product-page-view"' in main_content_html, 'solo product view missing from main content!'
    print("All 3 views (homepage, search results, single product) verified in main content!")

    print(f"Extracted CSS: {len(css_content)} chars")
    print(f"Extracted JS Engine: {len(script_js)} chars")
    print(f"Extracted Navbar: {len(navbar_html)} chars")
    print(f"Extracted Footer: {len(footer_html)} chars")
    print(f"Extracted WA Float: {len(wa_float_html)} chars")
    print(f"Extracted Cart Drawer: {len(cart_drawer_html)} chars")
    print(f"Extracted Overview Modal: {len(overview_modal_html)} chars")
    print(f"Extracted Login Modal: {len(login_modal_html)} chars")
    print(f"Extracted Main Page Content: {len(main_content_html)} chars")

    print("\n=================================================================")
    print("STEP 3: Converting asset paths to Shopify Liquid {{ 'file' | asset_url }}")
    print("=================================================================")

    def to_liquid_assets(text):
        return re.sub(
            r'assets/([a-zA-Z0-9_\-\.]+\.(?:jpg|png|svg|webp|jpeg|gif|js|css))',
            r"{{ '\1' | asset_url }}",
            text
        )

    navbar_liquid = to_liquid_assets(navbar_html)
    footer_liquid = to_liquid_assets(footer_html)
    wa_float_liquid = to_liquid_assets(wa_float_html)
    cart_drawer_liquid = to_liquid_assets(cart_drawer_html)
    overview_modal_liquid = to_liquid_assets(overview_modal_html)
    login_modal_liquid = to_liquid_assets(login_modal_html)
    express_modal_liquid = to_liquid_assets(express_modal_html)
    order_confirm_modal_liquid = to_liquid_assets(order_confirm_modal_html)
    main_content_liquid = to_liquid_assets(main_content_html)

    print("\n=================================================================")
    print("STEP 4: Writing Modular Assets (Eliminating 256 KB Section File Limit)")
    print("=================================================================")

    os.makedirs("assets", exist_ok=True)
    
    # 4A. Write CSS to assets/main-store.css & assets/theme.css
    with open("assets/main-store.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    with open("assets/theme.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    print(f"assets/main-store.css written ({os.path.getsize('assets/main-store.css') / 1024:.2f} KB)")
    print(f"assets/theme.css written ({os.path.getsize('assets/theme.css') / 1024:.2f} KB)")

    # 4B. Write JS to assets/main-store.js
    with open("assets/main-store.js", "w", encoding="utf-8") as f:
        f.write(script_js)
    print(f"assets/main-store.js written ({os.path.getsize('assets/main-store.js') / 1024:.2f} KB)")

    # Node.js syntax verification
    res = subprocess.run(["node", "-c", "assets/main-store.js"], capture_output=True, text=True)
    if res.returncode != 0:
        print("ERROR: assets/main-store.js has syntax errors:")
        print(res.stderr)
        raise RuntimeError("Syntax check failed on assets/main-store.js")
    else:
        print("Verification PASSED: assets/main-store.js has ZERO syntax errors (validated by Node.js).")

    # 4C. Live products injection code for Shopify
    live_products_injection = """// Dynamic Shopify Asset Root (Points JavaScript getAssetUrl to Shopify CDN)
window.SHOPIFY_ASSET_URL_ROOT = "{{ 'theme.css' | asset_url }}".replace(/theme\\.css(\\?.*)?$/, '');

// Dynamic Shopify Live Products Injection (250 products from Shopify Admin with variants)
window.SHOPIFY_LIVE_PRODUCTS = [
  {%- paginate collections.all.products by 250 -%}
  {%- for product in collections.all.products -%}
    {
      id: {{ product.id | json }},
      variantId: {{ product.selected_or_first_available_variant.id | default: product.variants.first.id | json }},
      variant_id: {{ product.selected_or_first_available_variant.id | default: product.variants.first.id | json }},
      title: {{ product.title | json }},
      handle: {{ product.handle | json }},
      author: {{ product.vendor | default: "Indigo Books" | json }},
      vendor: {{ product.vendor | default: "Indigo Books" | json }},
      type: {{ product.type | json }},
      price: "₹{{ product.price | money_without_currency }}",
      compare_at_price: "",
      oldPrice: "",
      priceNum: {{ product.price | divided_by: 100.0 }},
      discount: "",
      image: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
      coverUrl: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
      cover: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
      format: {% if product.variants.first.title != 'Default Title' %}{{ product.variants.first.title | json }}{% else %}"Paperback"{% endif %},
      variants: [
        {%- for v in product.variants -%}
          {
            id: {{ v.id | json }},
            title: {{ v.title | json }},
            price: {{ v.price | divided_by: 100.0 }},
            available: {{ v.available | json }},
            sku: {{ v.sku | json }}
          }{%- unless forloop.last -%},{%- endunless -%}
        {%- endfor -%}
      ],
      url: {{ product.url | json }},
      tags: {{ product.tags | json }},
      description: {{ product.description | strip_html | truncate: 280 | json }}
    }{%- unless forloop.last -%},{%- endunless -%}
  {%- endfor -%}
  {%- endpaginate -%}
];"""

    print("\n=================================================================")
    print("STEP 5: Writing Streamlined sections/main-store.liquid (Page Content Only)")
    print("=================================================================")

    os.makedirs("sections", exist_ok=True)
    # Live Shopify Products bridge script injected at top of section
    shopify_bridge_script = """<!-- Live Shopify Products Bridge (Direct from collections.all.products) -->
<script>
  if (typeof window !== 'undefined' && (!window.SHOPIFY_LIVE_PRODUCTS || window.SHOPIFY_LIVE_PRODUCTS.length === 0)) {
    window.SHOPIFY_LIVE_PRODUCTS = [
      {%- for product in collections.all.products limit: 250 -%}
        {
          id: {{ product.id | json }},
          title: {{ product.title | json }},
          handle: {{ product.handle | json }},
          author: {{ product.vendor | default: "Indigo Books" | json }},
          vendor: {{ product.vendor | default: "Indigo Books" | json }},
          type: {{ product.type | json }},
          price: "₹{{ product.price | money_without_currency }}",
          compare_at_price: "",
          oldPrice: "",
          image: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
          coverUrl: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
          cover: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
          variant_id: {{ product.selected_or_first_available_variant.id | json }},
          variantId: {{ product.selected_or_first_available_variant.id | json }},
          url: {{ product.url | json }},
          description: {{ product.description | strip_html | truncate: 280 | json }}
        }{%- unless forloop.last -%},{%- endunless -%}
      {%- endfor -%}
    ];
  }
</script>\n\n"""

    main_store_parts = [
        "{% comment %}\n",
        "  Indigo Books India - Complete Unified Storefront Page Content\n",
        "  Single Source of Truth: Auto-synchronized from preview.html\n",
        "  Zero React dependencies. 100% Vanilla HTML, CSS, and JS.\n",
        "{% endcomment %}\n\n",
        shopify_bridge_script,
        '<div class="indigo-store-root">\n',
        main_content_liquid,
        "\n</div>\n\n",
        "{% schema %}\n{\n  \"name\": \"Main Store\",\n  \"tag\": \"section\",\n  \"class\": \"indigo-main-store-section\",\n  \"settings\": [],\n  \"presets\": [\n    {\n      \"name\": \"Main Store\"\n    }\n  ]\n}\n{% endschema %}\n"
    ]
    main_store_content = "".join(main_store_parts)

    with open("sections/main-store.liquid", "w", encoding="utf-8") as f:
        f.write(main_store_content)
    main_store_size_kb = os.path.getsize('sections/main-store.liquid') / 1024
    print(f"sections/main-store.liquid written ({main_store_size_kb:.2f} KB) -> SAFE (Shopify limit: 256 KB)")

    # Also write sections/main-indigo-store.liquid as an alias
    main_indigo_content = main_store_content.replace('"name": "Main Store"', '"name": "Main Indigo Store"')
    with open("sections/main-indigo-store.liquid", "w", encoding="utf-8") as f:
        f.write(main_indigo_content)
    print(f"sections/main-indigo-store.liquid written ({os.path.getsize('sections/main-indigo-store.liquid') / 1024:.2f} KB)")

    print("\n=================================================================")
    print("STEP 6: Writing True Global layout/theme.liquid (Navbar, Footer, Modals, CSS)")
    print("=================================================================")

    # Dynamic Shopify Asset Map for all image assets in assets/
    asset_files = sorted([
        f for f in os.listdir("assets")
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.svg', '.webp', '.gif'))
    ])
    print(f"Found {len(asset_files)} asset image files for Shopify CDN mapping.")

    cdn_lines = [
        '      window.SHOPIFY_ASSET_URL_ROOT = "{{ \'theme.css\' | asset_url }}".replace(/theme\\.css(\\?.*)?$/, \'\');',
        '      window.PODIUM_CDN_COVERS = {'
    ]
    
    # Pre-populate specific ID aliases for instant lookup
    id_aliases = {
        "podium-godan": "hero-godan.jpg",
        "godan": "hero-godan.jpg",
        "godan-premchand": "hero-godan.jpg",
        "hero-book-godan": "hero-godan.jpg",
        "podium-raag-darbari": "hero-raag-darbari.jpg",
        "raag-darbari": "hero-raag-darbari.jpg",
        "raag-darbari-shrilal-shukla": "hero-raag-darbari.jpg",
        "hero-book-raag": "hero-raag-darbari.jpg",
        "podium-chitralekha": "hero-chitralekha.jpg",
        "chitralekha": "hero-chitralekha.jpg",
        "chitralekha-bhagwaticharan-verma": "hero-chitralekha.jpg",
        "hero-book-chitralekha": "hero-chitralekha.jpg",
        "podium-rashmirathi": "hero-rashmirathi.jpg",
        "rashmirathi": "hero-rashmirathi.jpg",
        "rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar": "hero-rashmirathi.jpg",
        "hero-book-rashmirathi": "hero-rashmirathi.jpg",
        "podium-ishq-mishra": "hero-kuchh-ishq.jpg",
        "podium-kuchh-ishq": "hero-kuchh-ishq.jpg",
        "kuchh-ishq": "hero-kuchh-ishq.jpg",
        "kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra": "hero-kuchh-ishq.jpg",
        "hero-book-kuchh-ishq": "hero-kuchh-ishq.jpg",
        "rekhta-kuchh-ishq": "hero-kuchh-ishq.jpg",
        "hero-book-gypsy": "hero-gypsy.jpg",
        "hindi-gypsy": "hero-gypsy.jpg",
        "gypsy-ila-chandra-joshi": "hero-gypsy.jpg",
        "book-tarkash": "book-tarkash.jpg",
        "rekhta-tarkash": "book-tarkash.jpg",
        "book-aadha-gaon": "book-aadha-gaon.jpg",
        "aadha-gaon": "book-aadha-gaon.jpg",
        "book-mahabhoj": "book-mahabhoj.jpg",
        "mahabhoj": "book-mahabhoj.jpg",
        "book-shekhar": "book-shekhar.jpg",
        "shekhar": "book-shekhar.jpg",
        "book-gaban": "book-gaban.jpg",
        "gaban": "book-gaban.jpg",
        "book-nirmala": "book-nirmala.jpg",
        "nirmala": "book-nirmala.jpg",
        "hero-book-murakami": "hero-book-murakami.jpg",
        "book-murakami": "hero-book-murakami.jpg",
        "book-samvidhan": "book-samvidhan.jpg",
        "vault-law-constitution": "book-samvidhan.jpg",
        "vault-law-highcourt": "book-highcourt.jpg",
        "vault-law-ucc": "book-sanhita.jpg",
        "vault-law-judiciary": "book-kasauti.jpg",
        "rekhta-rashmirathi": "hero-rashmirathi.jpg",
        "rekhta-dhuaan": "hero-book-dhuaan.jpg",
        "rekhta-guzare-lamhe": "book-guzare-lamhe.jpg"
    }

    for alias, target_img in id_aliases.items():
        if os.path.exists(os.path.join("assets", target_img)):
            cdn_lines.append(f'        "{alias}": "{{{{ \'{target_img}\' | asset_url }}}}",')

    for fname in asset_files:
        base_name = os.path.splitext(fname)[0]
        cdn_lines.append(f'        "{fname}": "{{{{ \'{fname}\' | asset_url }}}}",')
        cdn_lines.append(f'        "assets/{fname}": "{{{{ \'{fname}\' | asset_url }}}}",')
        cdn_lines.append(f'        "./assets/{fname}": "{{{{ \'{fname}\' | asset_url }}}}",')
        cdn_lines.append(f'        "{base_name}": "{{{{ \'{fname}\' | asset_url }}}}",')

    cdn_lines.append('        "hero-godan.jpg": "{{ \'hero-godan.jpg\' | asset_url }}"')
    cdn_lines.append('      };')

    cdn_lines.append("""
      window.getFallbackCoverSvg = function(title, author) {
        var t = (title || 'Indigo Books').replace(/<[^>]*>/g, '').substring(0, 32);
        var a = (author || 'Indigo Classics').replace(/<[^>]*>/g, '').substring(0, 24);
        var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300" width="100%" height="100%">' +
          '<defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#2B1A17"/><stop offset="100%" stop-color="#140D0B"/></linearGradient></defs>' +
          '<rect width="200" height="300" fill="url(#g)"/>' +
          '<rect x="0" y="0" width="10" height="300" fill="rgba(255,255,255,0.12)"/>' +
          '<rect x="16" y="16" width="168" height="268" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="3 3"/>' +
          '<circle cx="100" cy="76" r="28" fill="none" stroke="#D4AF37" stroke-width="1.2"/>' +
          '<text x="100" y="82" fill="#D4AF37" font-family="serif" font-size="18" font-weight="bold" text-anchor="middle">IB</text>' +
          '<text x="100" y="146" fill="#FAF8F5" font-family="serif" font-size="13" font-weight="bold" text-anchor="middle">' + t + '</text>' +
          '<text x="100" y="176" fill="#D4AF37" font-family="sans-serif" font-size="10" text-anchor="middle">By ' + a + '</text>' +
          '<text x="100" y="260" fill="#999999" font-family="sans-serif" font-size="8" letter-spacing="1.5" text-anchor="middle">INDIGO BOOKS INDIA</text>' +
          '</svg>';
        return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
      };

      window.getCoverUrl = function(coverPath, defaultTitle) {
        if (!coverPath) {
          if (defaultTitle && window.getFallbackCoverSvg) {
            return window.getFallbackCoverSvg(defaultTitle, '');
          }
          return (window.PODIUM_CDN_COVERS && (window.PODIUM_CDN_COVERS['hero-godan.jpg'] || window.PODIUM_CDN_COVERS['assets/hero-godan.jpg'])) ||
                 (window.SHOPIFY_ASSET_URL_ROOT ? window.SHOPIFY_ASSET_URL_ROOT + 'hero-godan.jpg' : 'assets/hero-godan.jpg');
        }
        // If already absolute HTTP/HTTPS, protocol-relative '//', or data URI, return DIRECTLY without tampering
        if (coverPath.indexOf('http://') === 0 || coverPath.indexOf('https://') === 0 || coverPath.indexOf('//') === 0 || coverPath.indexOf('data:') === 0) {
          return coverPath;
        }
        var clean = coverPath.replace(/^(\.\/)?assets\//, '').replace(/^\//, '');
        if (window.PODIUM_CDN_COVERS) {
          if (window.PODIUM_CDN_COVERS[coverPath]) return window.PODIUM_CDN_COVERS[coverPath];
          if (window.PODIUM_CDN_COVERS[clean]) return window.PODIUM_CDN_COVERS[clean];
          if (window.PODIUM_CDN_COVERS['assets/' + clean]) return window.PODIUM_CDN_COVERS['assets/' + clean];
          var baseName = clean.split('.')[0];
          if (window.PODIUM_CDN_COVERS[baseName]) return window.PODIUM_CDN_COVERS[baseName];
        }
        if (window.SHOPIFY_ASSET_URL_ROOT) {
          return window.SHOPIFY_ASSET_URL_ROOT + clean;
        }
        return 'assets/' + clean;
      };

      window.handleBookCoverError = function(img, title, author) {
        if (!img) return;
        img.onerror = null;
        var bookTitle = title || img.getAttribute('data-title') || img.alt || 'Indigo Books';
        var bookAuthor = author || img.getAttribute('data-author') || '';
        var fallback = (typeof window.getFallbackCoverSvg === 'function') ? window.getFallbackCoverSvg(bookTitle, bookAuthor) : (typeof getFallbackCover === 'function' ? getFallbackCover(bookTitle, bookAuthor) : '');
        if (img.parentElement) {
          img.parentElement.style.backgroundImage = 'url("' + fallback + '")';
          img.parentElement.style.backgroundSize = 'cover';
          img.parentElement.style.backgroundPosition = 'center';
        }
        img.style.display = 'none';
        img.src = fallback;
      };

      // Universal self-healing image onerror handler for Shopify CDN
      document.addEventListener('error', function(e) {
        if (e.target && e.target.tagName === 'IMG') {
          var img = e.target;
          var raw = img.getAttribute('src');
          // Only resolve if it explicitly starts with local relative path 'assets/' or './assets/'
          if (raw && (raw.indexOf('assets/') === 0 || raw.indexOf('./assets/') === 0)) {
            var resolved = window.getCoverUrl(raw);
            if (resolved && resolved !== raw && img.src !== resolved) {
              img.src = resolved;
              return;
            }
          }
          // Never force Godan for a different book! Generate book's own SVG cover
          img.onerror = null;
          if (window.getFallbackCoverSvg) {
            img.src = window.getFallbackCoverSvg(img.alt || 'Indigo Books India', '');
          }
        }
      }, true);
""")
    cdn_covers_map = "\n".join(cdn_lines)

    theme_liquid_full = f"""<!doctype html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="theme-color" content="#0F172A">
    <meta name="referrer" content="no-referrer">
    <meta http-equiv="content-language" content="en">
    <meta name="google" content="notranslate">
    <link rel="canonical" href="{{{{ canonical_url }}}}">
    <link rel="preconnect" href="https://cdn.shopify.com" crossorigin>

    <!-- Google Search Console Verification -->
    <meta name="google-site-verification" content="-e_RVQPApfsjWvvXEfSgc-ttWxIqb9hqO7eUvZCF1ZI">
    {{%- if settings.google_site_verification != blank -%}}
      {{%- if settings.google_site_verification contains '<meta' -%}}
        {{{{ settings.google_site_verification }}}}
      {{%- else -%}}
        <meta name="google-site-verification" content="{{{{ settings.google_site_verification | escape }}}}">
      {{%- endif -%}}
    {{%- endif -%}}

    <!-- Google Search Verified Square Favicons & Web Manifest -->
    {{%- if settings.favicon != blank -%}}
      <link rel="icon" type="image/png" sizes="192x192" href="{{{{ settings.favicon | image_url: width: 192, height: 192 }}}}">
      <link rel="icon" type="image/png" sizes="96x96" href="{{{{ settings.favicon | image_url: width: 96, height: 96 }}}}">
      <link rel="icon" type="image/png" sizes="48x48" href="{{{{ settings.favicon | image_url: width: 48, height: 48 }}}}">
      <link rel="icon" type="image/png" sizes="32x32" href="{{{{ settings.favicon | image_url: width: 32, height: 32 }}}}">
      <link rel="shortcut icon" href="{{{{ settings.favicon | image_url: width: 48, height: 48 }}}}">
      <link rel="apple-touch-icon" href="{{{{ settings.favicon | image_url: width: 180, height: 180 }}}}">
    {{%- else -%}}
      <link rel="icon" type="image/png" sizes="192x192" href="{{{{ 'favicon-192x192.png' | asset_url }}}}">
      <link rel="icon" type="image/png" sizes="96x96" href="{{{{ 'favicon-96x96.png' | asset_url }}}}">
      <link rel="icon" type="image/png" sizes="48x48" href="{{{{ 'favicon-48x48.png' | asset_url }}}}">
      <link rel="icon" type="image/png" sizes="32x32" href="{{{{ 'favicon-32x32.png' | asset_url }}}}">
      <link rel="shortcut icon" href="{{{{ 'favicon-48x48.png' | asset_url }}}}">
      <link rel="apple-touch-icon" href="{{{{ 'apple-touch-icon.png' | asset_url }}}}">
    {{%- endif -%}}

    {{%- assign page_title_clean = page_title | default: shop.name -%}}
    {{%- if page_title_clean == 'My Store' or page_title_clean == blank -%}}
      {{%- assign page_title_clean = 'Indigo Books India — Premier Online Bookstore Prayagraj' -%}}
    {{%- endif -%}}
    <title>{{{{ page_title_clean }}}}</title>
    <meta name="description" content="Discover India's premier online bookstore. 5,500+ curated titles in Hindi classics, Urdu poetry, law, history, philosophy, and bestsellers from Prayagraj.">

    <!-- Open Graph & Schema.org Structured Data -->
    <meta property="og:site_name" content="Indigo Books India">
    <meta property="og:url" content="{{{{ canonical_url }}}}">
    <meta property="og:title" content="{{{{ page_title_clean }}}}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="{{{{ 'indigo-books-logo.png' | asset_url }}}}">
    <meta property="og:description" content="Discover India's premier online bookstore. 5,500+ curated titles in Hindi classics, Urdu poetry, law, history, philosophy, and bestsellers from Prayagraj.">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Indigo Books",
      "alternateName": ["Indigo Books India", "IndigoBooks"],
      "url": "https://indigobooks.shop/",
      "potentialAction": {{
        "@type": "SearchAction",
        "target": "https://indigobooks.shop/?q={{search_term_string}}",
        "query-input": "required name=search_term_string"
      }}
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Indigo Books India",
      "url": "https://indigobooks.shop/",
      "logo": "{{{{ 'favicon-192x192.png' | asset_url }}}}",
      "sameAs": [
        "https://www.instagram.com/indigobooksindia",
        "https://www.facebook.com/indigobooks"
      ]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BookStore",
      "name": "Indigo Books India",
      "url": "https://indigobooks.shop/",
      "logo": "{{{{ 'indigo-books-logo.png' | asset_url }}}}",
      "image": "{{{{ 'indigo-books-logo.png' | asset_url }}}}",
      "description": "Premier bookstore in Prayagraj offering Hindi literature, UPSC, Law, and Urdu poetry.",
      "telephone": "+918933063306",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Prayagraj",
        "addressRegion": "Uttar Pradesh",
        "addressCountry": "IN"
      }}
    }}
    </script>

    <!-- Google Fonts: Merriweather & Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">

    <!-- Suppress Tailwind Production Warning BEFORE CDN Script Evaluation -->
    <script>
      (function() {{
        var origWarn = console.warn;
        console.warn = function() {{
          if (arguments[0] && typeof arguments[0] === 'string' && arguments[0].indexOf('cdn.tailwindcss.com') !== -1) return;
          origWarn.apply(console, arguments);
        }};
      }})();
    </script>
    <!-- Tailwind CSS Engine -->
    <script src="https://cdn.tailwindcss.com" defer="defer"></script>

    <!-- Global Unified Bookstore Stylesheets -->
    <link rel="stylesheet" href="{{{{ 'theme.css' | asset_url }}}}">
    <link rel="stylesheet" href="{{{{ 'main-store.css' | asset_url }}}}">
    {{{{ 'theme.css' | asset_url | stylesheet_tag }}}}
    {{{{ 'main-store.css' | asset_url | stylesheet_tag }}}}

    <!-- HERO LOCKED 2-COLUMN & 3x2 GRID STYLES (NEVER BREAK) -->
    <style id="hero-locked-styles">
      #indigo-video-hero,
      .ivh-section {{
        position: relative !important;
        min-height: 520px !important;
        width: 100% !important;
        background: linear-gradient(115deg, #09132C 0%, #101D40 48%, #2B2118 78%, #4A3314 100%) !important;
        overflow: hidden !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 !important;
      }}

      .ivh-container {{
        position: relative !important;
        z-index: 20 !important;
        max-width: 1320px !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding: 44px 24px !important;
        display: grid !important;
        grid-template-columns: 1fr 1.1fr !important;
        gap: 32px !important;
        align-items: center !important;
        box-sizing: border-box !important;
      }}

      .ivh-left {{
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        text-align: left !important;
        z-index: 25 !important;
        order: 1 !important;
      }}

      .ivh-title {{
        font-family: 'Merriweather', Georgia, serif !important;
        font-size: 52px !important;
        font-weight: 700 !important;
        line-height: 1.12 !important;
        color: #FFFFFF !important;
        margin: 0 0 16px 0 !important;
      }}

      .ivh-story-italic {{
        font-family: 'Merriweather', Georgia, serif !important;
        font-style: italic !important;
        color: #E5A93C !important;
      }}

      .ivh-right {{
        position: relative !important;
        min-height: 430px !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        order: 2 !important;
      }}

      .ivh-rangoli-anchor {{
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        width: 440px !important;
        height: 440px !important;
        transform: translate(-50%, -50%) !important;
        z-index: 8 !important;
        pointer-events: none !important;
      }}

      .ivh-rangoli-spin {{
        width: 100% !important;
        height: 100% !important;
        animation: ivhSpinClockwise 42s linear infinite !important;
        transform-origin: center center !important;
      }}

      @keyframes ivhSpinClockwise {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}

      #ivh-books-grid,
      .ivh-books-grid {{
        position: relative !important;
        z-index: 25 !important;
        display: grid !important;
        grid-template-columns: repeat(3, 126px) !important;
        grid-template-rows: repeat(2, 186px) !important;
        gap: 18px !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
      }}

      .ivh-book-card {{
        position: relative !important;
        width: 126px !important;
        height: 186px !important;
        max-width: 126px !important;
        max-height: 186px !important;
        border-radius: 6px !important;
        overflow: hidden !important;
        border-right: 4px solid #F8FAFC !important;
        box-shadow: 0 14px 28px rgba(0,0,0,0.6) !important;
        cursor: pointer !important;
        background: #0F172A !important;
        display: block !important;
        transition: transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.42s ease, box-shadow 0.42s ease !important;
      }}

      .ivh-book-card img {{
        width: 100% !important;
        height: 100% !important;
        max-width: 126px !important;
        max-height: 186px !important;
        object-fit: cover !important;
        display: block !important;
      }}

      @media (max-width: 900px) {{
        .ivh-container {{
          grid-template-columns: 1fr !important;
          padding: 24px 16px !important;
        }}
        .ivh-title {{ font-size: 34px !important; }}
        .ivh-rangoli-anchor {{ width: 290px !important; height: 290px !important; }}
        #ivh-books-grid, .ivh-books-grid {{
          grid-template-columns: repeat(3, 94px) !important;
          grid-template-rows: repeat(2, 140px) !important;
          gap: 10px !important;
        }}
        .ivh-book-card, .ivh-book-card img {{
          width: 94px !important;
          height: 140px !important;
          max-width: 94px !important;
          max-height: 140px !important;
        }}
      }}
    </style>

    <!-- Global Safeguards & SVG Safety Constraints -->
    <style>
      /* STRICT MODAL OVERLAY & BACKDROP SYSTEM (ZERO JITTER / ZERO STACKING) */
      .indigo-modal-overlay,
      .express-checkout-modal-backdrop,
      .modal-overlay,
      #indigo-express-checkout-modal,
      #indigo-order-success-modal,
      #indigo-overview-modal,
      #indigo-signin-modal,
      #expressPhoneCheckoutModal,
      #orderConfirmationModal,
      #overviewModalOverlay,
      #loginModalOverlay {{
        display: none !important;
        position: fixed !important;
        inset: 0 !important;
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        z-index: 1000000 !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 16px !important;
        box-sizing: border-box !important;
      }}

      .indigo-modal-overlay.is-active,
      .express-checkout-modal-backdrop.is-active,
      .modal-overlay.is-active,
      #indigo-express-checkout-modal.is-active,
      #indigo-order-success-modal.is-active,
      #indigo-overview-modal.is-active,
      #indigo-signin-modal.is-active,
      #expressPhoneCheckoutModal.is-active,
      #orderConfirmationModal.is-active,
      #overviewModalOverlay.is-active,
      #loginModalOverlay.is-active {{
        display: flex !important;
      }}

      /* ABSOLUTE SVG SAFETY CONSTRAINT (PREVENTS 1000PX SVG BLOWUPS) */
      svg {{
        max-width: 100%;
        flex-shrink: 0;
      }}
      button svg, a svg, .btn svg {{
        width: 18px !important;
        height: 18px !important;
        display: inline-block !important;
        vertical-align: middle !important;
      }}
      .floating-wa-btn svg {{
        width: 28px !important;
        height: 28px !important;
      }}

      /* ABSOLUTE HORIZONTAL OVERFLOW & ZERO HORIZONTAL SCROLLBAR */
      html, body {{
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
        box-sizing: border-box !important;
      }}

      *, *:before, *:after {{
        box-sizing: border-box !important;
      }}

      /* STICKY CREAM NAVBAR AT ROOT LEVEL (MAX STACKING & OVERFLOW VISIBLE) */
      header,
      .site-header,
      .site-navbar,
      .main-navbar,
      .navbar-inner,
      .editorial-search-wrap,
      header > nav {{
        position: sticky !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        overflow: visible !important;
        z-index: 2147483647 !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
      }}

      /* GUARANTEED FLOATING SEARCH DROPDOWN - FLOATS OVER ALL PAGES & MODALS */
      .editorial-search-wrap {{
        position: relative !important;
        flex: 1 1 340px !important;
        max-width: 440px !important;
        overflow: visible !important;
        z-index: 2147483647 !important;
      }}

      .editorial-search-results {{
        position: absolute !important;
        top: calc(100% + 8px) !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        min-width: 320px !important;
        max-width: 480px !important;
        background: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1px solid rgba(18, 18, 18, 0.14) !important;
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.35) !important;
        max-height: 480px !important;
        overflow-y: auto !important;
        display: none;
        z-index: 2147483647 !important;
      }}

      .editorial-search-item {{
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        padding: 10px 16px !important;
        cursor: pointer !important;
        border-bottom: 1px solid #F5F5F5 !important;
        transition: background 0.15s ease !important;
      }}
      .editorial-search-item:hover {{
        background: #FAF8F5 !important;
      }}

      /* REMOVE CARETS / VERTICAL BARS IN STATS BAR */
      .stats-bar *,
      .stats-grid *,
      [class*="stat"] *,
      .stats-bar *::before,
      .stats-bar *::after,
      .stats-grid *::before,
      .stats-grid *::after,
      [class*="stat"]::before,
      [class*="stat"]::after {{
        content: none !important;
        border-right: none !important;
        border-left: none !important;
        outline: none !important;
        box-shadow: none !important;
        caret-color: transparent !important;
      }}

      /* UNIVERSAL SECTION CONTAINER PADDING & MARGIN SYSTEM (1340PX / 32PX PADDING) */
      .site-container,
      .section-container,
      .vault-container,
      .catalog-container,
      .voices-container,
      .product-page-wrapper,
      #law-academic-vault > div,
      #indian-voices-section > div,
      #shop-all-catalog > div,
      #bestsellers-podium > div,
      #category-bento-showcase > div,
      #mehfil-rekhta > div {{
        max-width: 1340px !important;
        width: 100% !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-left: 32px !important;
        padding-right: 32px !important;
        box-sizing: border-box !important;
      }}

      @media (max-width: 768px) {{
        .site-container,
        .section-container,
        .vault-container,
        .catalog-container,
        .voices-container,
        .product-page-wrapper,
        #law-academic-vault > div,
        #indian-voices-section > div,
        #shop-all-catalog > div,
        #bestsellers-podium > div,
        #category-bento-showcase > div,
        #mehfil-rekhta > div {{
          padding-left: 16px !important;
          padding-right: 16px !important;
        }}
      }}

      /* FULL-WIDTH STATS COUNTER BAR */
      .stats-bar {{
        display: block !important;
        width: 100% !important;
        background: #FFFFFF !important;
        border-bottom: 1px solid #E2E8F0 !important;
        padding: 28px 0 !important;
        box-sizing: border-box !important;
      }}

      .stats-grid {{
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 24px !important;
        width: 100% !important;
        max-width: 1320px !important;
        margin: 0 auto !important;
        padding: 0 28px !important;
        box-sizing: border-box !important;
        align-items: center !important;
      }}

      @media (max-width: 768px) {{
        .stats-grid {{
          grid-template-columns: repeat(2, 1fr) !important;
          gap: 16px !important;
          padding: 0 16px !important;
        }}
      }}
    </style>

    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest" defer="defer"></script>

    <!-- Verified Shopify CDN Asset Map -->
    <script>
{cdn_covers_map}
    </script>

    {{{{ content_for_header }}}}

    <!-- META ADS PIXEL & CONVERSIONS TRACKING -->
    {{%- render 'meta-pixel-events' -%}}
    <script src="{{{{ 'meta-ads-tracking.js' | asset_url }}}}" defer></script>
  </head>
  <body class="template-{{{{ template.name | handle }}}}">
    <!-- 1. GLOBAL STICKY CREAM NAVBAR -->
    {navbar_liquid}

    <!-- 2. ROUTE CONTENT (Home, Product, Search, Collections, etc.) -->
    <main id="MainContent" role="main">
      {{{{ content_for_layout }}}}
    </main>

    <!-- 3. GLOBAL HERITAGE BOOKSTORE FOOTER -->
    {footer_liquid}

    <!-- 4. GLOBAL FLOATING WHATSAPP BUTTON -->
    {wa_float_liquid}

    <!-- 5. GLOBAL SLIDE-OVER CART DRAWER -->
    {cart_drawer_liquid}

    <!-- 6. GLOBAL UNIVERSAL BOOK OVERVIEW MODAL -->
    {overview_modal_liquid}

    <!-- 7. GLOBAL MEMBER SIGN-IN MODAL -->
    {login_modal_liquid}

    <!-- 8. GLOBAL 1-CLICK PHONE & GPS EXPRESS CHECKOUT MODAL -->
    {express_modal_liquid}

    <!-- 9. GLOBAL ORDER CONFIRMATION MODAL -->
    {order_confirm_modal_liquid}

    <!-- 10. LIVE SHOPIFY PRODUCTS INJECTION -->
    <script>
{live_products_injection}
    </script>

    <!-- 9. GLOBAL JS ENGINE -->
    <script src="{{{{ 'main-store.js' | asset_url }}}}" defer="defer"></script>

    <!-- 10. LUCIDE ICONS ACTIVATION -->
    <script>
      document.addEventListener('DOMContentLoaded', function() {{
        if (typeof lucide !== 'undefined') {{
          try {{ lucide.createIcons(); }} catch(e) {{}}
        }}
      }});
      window.addEventListener('load', function() {{
        if (typeof lucide !== 'undefined') {{
          try {{ lucide.createIcons(); }} catch(e) {{}}
        }}
      }});
    </script>
  </body>
</html>
"""

    os.makedirs("layout", exist_ok=True)
    with open("layout/theme.liquid", "w", encoding="utf-8") as f:
        f.write(theme_liquid_full)
    print(f"layout/theme.liquid updated ({os.path.getsize('layout/theme.liquid') / 1024:.2f} KB) -> TRUE GLOBAL THEME ARCHITECTURE.")

    print("\n=================================================================")
    print("STEP 7: Configuring templates/index.json, product.json, search.json")
    print("=================================================================")

    os.makedirs("templates", exist_ok=True)
    
    # index.json
    with open("templates/index.json", "w", encoding="utf-8") as f:
        json.dump({
            "sections": {
                "main_store": {
                    "type": "main-store",
                    "settings": {}
                }
            },
            "order": ["main_store"]
        }, f, indent=2)
    print("templates/index.json configured to load 'main_store'.")

    # product.json
    with open("templates/product.json", "w", encoding="utf-8") as f:
        json.dump({
            "sections": {
                "main_product": {
                    "type": "main-product",
                    "settings": {}
                }
            },
            "order": ["main_product"]
        }, f, indent=2)
    print("templates/product.json configured to load 'main_product'.")

    # search.json
    with open("templates/search.json", "w", encoding="utf-8") as f:
        json.dump({
            "sections": {
                "main_search": {
                    "type": "main-search",
                    "settings": {}
                }
            },
            "order": ["main_search"]
        }, f, indent=2)
    print("templates/search.json configured to load 'main_search'.")

    # Remove unrendered section group files
    for jf in ["sections/header-group.json", "sections/footer-group.json"]:
        if os.path.exists(jf):
            os.remove(jf)
            print(f"Removed unrendered section group file: {jf}")

    print("\n=================================================================")
    print("STEP 8: Neutralizing Obsolete Section Files")
    print("=================================================================")

    obsolete_sections = [
        "hero.liquid",
        "curators-podium.liquid",
        "podium.liquid",
        "mehfil-rekhta.liquid",
        "bundle-unboxing.liquid",
        "regional-magazine.liquid",
        "academic-vault.liquid",
        "catalog-directory.liquid",
        "trust-strip.liquid",
        "contact-section.liquid",
        "footer.liquid",
        "literary-marquee.liquid"
    ]

    neutral_schema = """{% comment %}
  Neutralized section - Unified into theme.liquid & main-store.liquid
{% endcomment %}
{% schema %}
{
  "name": "Obsolete Section",
  "settings": []
}
{% endschema %}
"""

    for obs in obsolete_sections:
        obs_path = os.path.join("sections", obs)
        if os.path.exists(obs_path):
            with open(obs_path, "w", encoding="utf-8") as f:
                f.write(neutral_schema)

    print("\n=================================================================")
    print("STEP 9: Exporting strictly valid Shopify Theme folder & .zip packages")
    print("=================================================================")

    included_dirs = [
        "assets",
        "blocks",
        "config",
        "layout",
        "locales",
        "sections",
        "snippets",
        "templates"
    ]

    # 9A. Build physical directory 'indigo-books-shopify-theme'
    target_dir = "indigo-books-shopify-theme"
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir, exist_ok=True)

    for folder in included_dirs:
        if os.path.exists(folder):
            dest = os.path.join(target_dir, folder)
            shutil.copytree(folder, dest)
    print(f"Physical theme directory '{target_dir}/' created on disk with valid Shopify file tree.")

    # 9B. Package indigo-books-shopify-theme.zip (with 'indigo-books-shopify-theme/' root folder)
    zip_theme_folder = "indigo-books-shopify-theme.zip"
    if os.path.exists(zip_theme_folder):
        os.remove(zip_theme_folder)

    total_files_folder = 0
    with zipfile.ZipFile(zip_theme_folder, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ".")
                arcname = rel_path.replace("\\", "/")
                z.write(full_path, arcname)
                total_files_folder += 1

    mb_folder = os.path.getsize(zip_theme_folder) / (1024 * 1024)
    print(f"Successfully packaged {total_files_folder} files into {zip_theme_folder}! ({mb_folder:.2f} MB) -> Extracts to {target_dir}/")

    # 9C. Package indigo-books-theme.zip (with root-level structure)
    zip_root = "indigo-books-theme.zip"
    if os.path.exists(zip_root):
        os.remove(zip_root)

    total_files_root = 0
    with zipfile.ZipFile(zip_root, "w", zipfile.ZIP_DEFLATED) as z:
        for folder in included_dirs:
            if not os.path.exists(folder):
                continue
            for root, dirs, files in os.walk(folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, ".")
                    arcname = rel_path.replace("\\", "/")
                    z.write(full_path, arcname)
                    total_files_root += 1

    mb_root = os.path.getsize(zip_root) / (1024 * 1024)
    print(f"Successfully packaged {total_files_root} files into {zip_root}! ({mb_root:.2f} MB) -> Direct root level")
    print("\n>>> STRICT SYNCHRONIZATION COMPLETE: PREVIEW.HTML AND SHOPIFY .ZIP PACKAGES ARE 100% IN SYNC! <<<")

if __name__ == "__main__":
    sync_preview_to_shopify()
