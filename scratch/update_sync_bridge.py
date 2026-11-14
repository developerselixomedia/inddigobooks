# -*- coding: utf-8 -*-
with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add verification for search view
target_verify = 'assert \'<div id="homepage-view"\' in main_content_html, "homepage-view missing from main content!"'
replacement_verify = '''assert '<div id="homepage-view"' in main_content_html, "homepage-view missing from main content!"
    assert '<div id="indigo-search-results-view"' in main_content_html, "indigo-search-results-view missing from main content!"
    assert '<div id="single-product-page-view"' in main_content_html, "single-product-page-view missing from main content!"'''

if target_verify in text:
    text = text.replace(target_verify, replacement_verify)
    print("Added view assertion verifications!")
else:
    print("Could not find target_verify")

# 2. Add Live Shopify Products bridge to main_store_parts
target_parts = '''    main_store_parts = [
        "{% comment %}\\n",
        "  Indigo Books India - Complete Unified Storefront Page Content\\n",
        "  Single Source of Truth: Auto-synchronized from preview.html\\n",
        "  Zero React dependencies. 100% Vanilla HTML, CSS, and JS.\\n",
        "{% endcomment %}\\n\\n",
        '<div class="indigo-store-root">\\n','''

replacement_parts = '''    # Live Shopify Products bridge script injected at top of section
    shopify_bridge_script = """<!-- Live Shopify Products Bridge (Direct from collections.all.products) -->
<script>
  if (typeof window !== 'undefined' && (!window.SHOPIFY_LIVE_PRODUCTS || window.SHOPIFY_LIVE_PRODUCTS.length === 0)) {
    window.SHOPIFY_LIVE_PRODUCTS = [
      {%- paginate collections.all.products by 250 -%}
        {%- for product in collections.all.products -%}
          {
            id: {{ product.id | json }},
            title: {{ product.title | json }},
            handle: {{ product.handle | json }},
            author: {{ product.vendor | default: "Indigo Books" | json }},
            vendor: {{ product.vendor | default: "Indigo Books" | json }},
            type: {{ product.type | json }},
            price: "₹{{ product.price | money_without_currency }}",
            compare_at_price: "{{ product.compare_at_price | money_without_currency }}",
            oldPrice: {% if product.compare_at_price > product.price %}"₹{{ product.compare_at_price | money_without_currency }}"{% else %}""{% endif %},
            image: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
            coverUrl: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
            cover: "{% if product.featured_image %}{{ product.featured_image | image_url: width: 600 }}{% endif %}",
            variant_id: {{ product.selected_or_first_available_variant.id | json }},
            variantId: {{ product.selected_or_first_available_variant.id | json }},
            url: {{ product.url | json }},
            description: {{ product.description | strip_html | truncate: 280 | json }}
          }{%- unless forloop.last -%},{%- endunless -%}
        {%- endfor -%}
      {%- endpaginate -%}
    ];
  }
</script>\\n\\n"""

    main_store_parts = [
        "{% comment %}\\n",
        "  Indigo Books India - Complete Unified Storefront Page Content\\n",
        "  Single Source of Truth: Auto-synchronized from preview.html\\n",
        "  Zero React dependencies. 100% Vanilla HTML, CSS, and JS.\\n",
        "{% endcomment %}\\n\\n",
        shopify_bridge_script,
        '<div class="indigo-store-root">\\n','''

if target_parts in text:
    text = text.replace(target_parts, replacement_parts)
    print("Added shopify_bridge_script to main_store_parts!")
else:
    print("Could not find target_parts")

with open('sync_preview_to_shopify.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated sync_preview_to_shopify.py!")

