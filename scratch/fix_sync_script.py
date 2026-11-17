import re

with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_head_block = """    <!-- Official Vector SVG Favicon (Data URI: Zero 404 Console Errors) -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='16' fill='%230066B3'/%3E%3Cpath d='M20 20h25v25H20zM55 20h25v25H55zM20 55h25v25H20zM55 55h25v25H55z' fill='none' stroke='%23ffffff' stroke-width='6'/%3E%3C/svg%3E">

    <title>{{{{ page_title | default: shop.name }}}}</title>
    {{% if page_description %}}
      <meta name="description" content="{{{{ page_description | escape }}}}">
    {{% endif %}}

    <!-- Open Graph Meta Tags -->
    <meta property="og:site_name" content="{{{{ shop.name }}}}">
    <meta property="og:url" content="{{{{ canonical_url }}}}">
    <meta property="og:title" content="{{{{ page_title | default: shop.name }}}}">
    <meta property="og:type" content="website">
    <meta property="og:description" content="{{{{ page_description | default: shop.description | escape }}}}">

    <!-- Google Fonts: Merriweather & Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">

    <!-- Tailwind CSS Engine -->
    <script src="https://cdn.tailwindcss.com" defer="defer"></script>"""

new_head_block = """    <!-- Google Search Verified Square Favicons & Web Manifest -->
    <link rel="icon" type="image/png" sizes="192x192" href="{{{{ 'favicon-192x192.png' | asset_url }}}}">
    <link rel="icon" type="image/png" sizes="96x96" href="{{{{ 'favicon-96x96.png' | asset_url }}}}">
    <link rel="icon" type="image/png" sizes="48x48" href="{{{{ 'favicon-48x48.png' | asset_url }}}}">
    <link rel="icon" type="image/png" sizes="32x32" href="{{{{ 'favicon-32x32.png' | asset_url }}}}">
    <link rel="shortcut icon" href="{{{{ 'favicon-48x48.png' | asset_url }}}}">
    <link rel="apple-touch-icon" href="{{{{ 'apple-touch-icon.png' | asset_url }}}}">

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
    <script src="https://cdn.tailwindcss.com" defer="defer"></script>"""

if old_head_block in content:
    content = content.replace(old_head_block, new_head_block)
    print("Successfully replaced head block in sync_preview_to_shopify.py")
    with open('sync_preview_to_shopify.py', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("Error: old_head_block not found in sync_preview_to_shopify.py")
