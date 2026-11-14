# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update hero-locked-styles in build_html_generator.py
hero_styles_target = """      /* LOCKED 2-COLUMN HERO LAYOUT */
      #indigo-video-hero,
      .ivh-section {
        position: relative !important;
        min-height: 520px !important;
        width: 100% !important;
        background: linear-gradient(115deg, #09132C 0%, #101D40 48%, #2B2118 78%, #4A3314 100%) !important;
        overflow: hidden !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 !important;
      }"""

hero_styles_replacement = """      /* LOCKED 2-COLUMN HERO LAYOUT */
      #indigo-video-hero,
      #indigo-hero-master,
      .ivh-section {
        position: relative !important;
        min-height: 520px !important;
        width: 100% !important;
        background: linear-gradient(115deg, #09132C 0%, #101D40 48%, #2B2118 78%, #4A3314 100%) !important;
        overflow: visible !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 !important;
        z-index: 500 !important;
      }

      .hero-bg-clip {
        position: absolute !important;
        inset: 0 !important;
        overflow: hidden !important;
        pointer-events: none !important;
        z-index: 1 !important;
      }"""

if hero_styles_target in text:
    text = text.replace(hero_styles_target, hero_styles_replacement)
    print("Updated hero-locked-styles overflow & z-index!")
else:
    print("hero_styles_target not found!")

# 2. Update .ivh-container & .ivh-left z-index and overflow
ivh_container_target = """      .ivh-container {
        position: relative !important;
        z-index: 20 !important;"""

ivh_container_replacement = """      .ivh-container {
        position: relative !important;
        z-index: 600 !important;
        overflow: visible !important;"""

if ivh_container_target in text:
    text = text.replace(ivh_container_target, ivh_container_replacement)
    print("Updated ivh-container z-index and overflow!")
else:
    print("ivh_container_target not found!")

# 3. Add hero-bg-clip wrapper to background decorative SVGs
hero_bg_target = """    <section class="hero-section ivh-section" id="indigo-video-hero">
      <div class="hero-topleft-watermark">
        {HERO_TOPLEFT_WATERMARK_SVG}
      </div>

      {HERO_FLOOR_CURVE_SVG}
      {STRING_LIGHTS_SVG}
      {HERO_DIYAS_SVG}

      <div class="site-container hero-main-grid hero-inner-container ivh-container">"""

hero_bg_replacement = """    <section class="hero-section ivh-section" id="indigo-video-hero">
      <div class="hero-bg-clip">
        <div class="hero-topleft-watermark">
          {HERO_TOPLEFT_WATERMARK_SVG}
        </div>

        {HERO_FLOOR_CURVE_SVG}
        {STRING_LIGHTS_SVG}
        {HERO_DIYAS_SVG}
      </div>

      <div class="site-container hero-main-grid hero-inner-container ivh-container">"""

if hero_bg_target in text:
    text = text.replace(hero_bg_target, hero_bg_replacement)
    print("Wrapped decorative hero SVGs in .hero-bg-clip!")
else:
    print("hero_bg_target not found!")

# 4. Make pdpAuthor clickable
pdp_author_target = """          <div class="pdp-author-row">
            By <strong id="pdpAuthor">Author Name</strong> &bull; Authorized Indian Edition
          </div>"""

pdp_author_replacement = """          <div class="pdp-author-row">
            By <strong id="pdpAuthor" class="pdp-clickable-author" onclick="searchByAuthor(this.textContent)" title="Click to view all books by this author">Author Name</strong> &bull; Authorized Indian Edition
          </div>"""

if pdp_author_target in text:
    text = text.replace(pdp_author_target, pdp_author_replacement)
    print("Made pdpAuthor clickable!")
else:
    print("pdp_author_target not found!")

# 5. Make 'Browse All 5,500+ Books' link working
browse_link_target = """          <a href="#shop-all-catalog" onclick="filterCatalog('all')" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none; align-self: flex-end; padding-bottom: 8px;">
            Browse All 5,500+ Books &rarr;
          </a>"""

browse_link_replacement = """          <a href="#shop-all-catalog" onclick="browseAllBooks(event)" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none; align-self: flex-end; padding-bottom: 8px; cursor: pointer;">
            Browse All 5,500+ Books &rarr;
          </a>"""

if browse_link_target in text:
    text = text.replace(browse_link_target, browse_link_replacement)
    print("Updated Browse All 5,500+ Books link!")
else:
    print("browse_link_target not found!")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated build_html_generator.py successfully!")
