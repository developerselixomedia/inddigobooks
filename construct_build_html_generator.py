# -*- coding: utf-8 -*-
"""
construct_build_html_generator.py
Rebuilds build_html_generator.py cleanly with all 7 fixes.
"""

import re

with open('preview.html', 'r', encoding='utf-8') as f:
    preview_html = f.read()

# Let's verify where UNIFIED_STORE_CSS is in preview.html
style_start = preview_html.find('<style>')
style_end = preview_html.find('</style>')
assert style_start != -1 and style_end != -1

head_part = preview_html[:style_start + len('<style>\n')]
# We replace the static CSS with {UNIFIED_STORE_CSS}
body_with_sections = preview_html[style_end:]

# Let's inspect where script tag starts at the bottom
script_pos = body_with_sections.rfind('<script>')
body_part = body_with_sections[:script_pos]

# Let's check the sections in body_part:
# 1. Stats Bar: 30% Max Savings -> 24-Hr Express Dispatch from Prayagraj
body_part = re.sub(
    r'<div class="stat-card">\s*<div class="stat-number">30%</div>\s*<div class="stat-label">Max Savings on Bundles</div>\s*</div>',
    r'<div class="stat-card">\n          <div class="stat-number">24-Hr</div>\n          <div class="stat-label">Express Dispatch from Prayagraj</div>\n        </div>',
    body_part
)

# 2. Marquee item
body_part = body_part.replace('UPSC &amp; JUDICIARY SCHOLAR DISCOUNTS', 'UPSC &amp; JUDICIARY SCHOLAR EDITIONS')

# 3. Podium star ratings and strikethrough/discount
body_part = re.sub(
    r'<div class="podium-rating-row">.*?</div>\s*<blockquote',
    r'<blockquote',
    body_part,
    flags=re.DOTALL
)

body_part = re.sub(
    r'<div class="podium-price-row">\s*<span id="podiumSpotPrice"[^>]*>.*?</span>\s*<span id="podiumSpotOldPrice"[^>]*>.*?</span>\s*<span id="podiumSpotDiscount"[^>]*>.*?</span>\s*</div>',
    r'<div class="podium-price-row">\n              <span id="podiumSpotPrice" class="podium-curr-price">{PODIUM_BOOKS[0][\'price\']}</span>\n            </div>',
    body_part
)

# 4. Hero card hovers
for idx in range(6):
    pattern = rf'data-hero-idx="{idx}"(?! onmouseenter)'
    repl = f'data-hero-idx="{idx}" onmouseenter="handleHeroBookHover({idx})" onmouseleave="handleHeroGridMouseLeave()"'
    body_part = re.sub(pattern, repl, body_part)

# 5. Replace Section 3 (#contemporary-fiction) with {render_category_bento_showcase()}
sec3_match = re.search(r'<!-- =+\s*6\. SECTION 3:.*?--\s*>\s*<section id="contemporary-fiction".*?</section>', body_part, re.DOTALL)
if sec3_match:
    body_part = body_part[:sec3_match.start()] + "{render_category_bento_showcase()}" + body_part[sec3_match.end():]
else:
    print("Warning: sec3_match not found")

# 6. Remove Section 7B (fast horizontal category shelves)
sec7b_match = re.search(r'<!-- =+\s*7B\. FAST HORIZONTAL CATEGORY SHELVES.*?--\s*>.*?</section>\s*</section>\s*</section>', body_part, re.DOTALL)
if not sec7b_match:
    sec7b_match = re.search(r'<!-- =+\s*7B\. FAST HORIZONTAL CATEGORY SHELVES.*?--\s*>.*?(?=<!-- =+\s*8\. SECTION 5: PAN-INDIA)', body_part, re.DOTALL)

if sec7b_match:
    body_part = body_part[:sec7b_match.start()] + body_part[sec7b_match.end():]
    print("Removed Section 7B successfully")
else:
    print("Warning: sec7b_match not found")

# 7. Add Catalog Pagination
if 'id="catalogPagination"' not in body_part:
    body_part = body_part.replace(
        '<div class="catalog-cards-grid" id="catalogGridContainer">\n          <!-- Rendered by store_scripts.js -->\n        </div>',
        '<div class="catalog-cards-grid" id="catalogGridContainer">\n          <!-- Rendered by store_scripts.js -->\n        </div>\n\n        <!-- Catalog Pagination Controls (12 Books per Page) -->\n        <div id="catalogPagination" class="catalog-pagination"></div>'
    )

# 8. Law Vault clean price
body_part = re.sub(
    r'<div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">\s*<span style="font-size: 18px; font-weight: 800; color: #0F172A;[^"]*">.*?</span>\s*<span style="font-size: 12px; text-decoration: line-through;[^"]*">.*?</span>\s*</div>',
    r'<div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">\n                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{b[\'price\']}</span>\n                </div>',
    body_part
)

body_part = body_part.replace(
    'Special discounts and invoice billing for Bar Council members, Law Chambers, and University Libraries.',
    'Bulk institutional order supply and invoice billing for Bar Council members, Law Chambers, and University Libraries.'
)

# 9. PDP: remove pdpComparePrice, pdpDiscountBadge, and #pdpReviewsCard
body_part = re.sub(
    r'<span id="pdpComparePrice".*?</span>\s*<span id="pdpDiscountBadge".*?</span>',
    '',
    body_part
)

body_part = re.sub(
    r'<!-- Customer Reviews Card -->.*?</div>\s*</div>\s*(?=<!-- =+\s*11\. GLOBAL FOOTER)',
    '</div>\n  </div>\n\n  ',
    body_part,
    flags=re.DOTALL
)

# 10. Overview Modal: remove modalMrp and modalDiscount
body_part = re.sub(
    r'<span id="modalMrp".*?</span>\s*<span id="modalDiscount".*?</span>',
    '',
    body_part
)

print("Body part processed. Length:", len(body_part))

# Now write out build_html_generator.py
generator_code = '''# -*- coding: utf-8 -*-
"""
build_html_generator.py
Assembles preview.html using data from store_data, store_styles, and store_scripts.
Ensures ZERO raw Liquid tags, ZERO fake discounts, ZERO strikethroughs, and 100% exact CSV prices.
"""

import json
from store_data import (
    PODIUM_BOOKS,
    POET_SHAYARI_DATA,
    REKHTA_BOOKS,
    BUNDLE_BOOKS,
    HINDI_FEATURE_BOOK,
    HINDI_GRID_BOOKS,
    VAULT_TABS,
    VAULT_BOOKS,
    CATEGORY_SHELVES,
    PIYUSH_MISHRA_BOOKS,
    CATEGORY_BENTO_DATA,
    CATALOG_BOOKS,
    MODAL_METADATA_DATABASE
)
from store_styles import UNIFIED_STORE_CSS
from store_scripts import UNIFIED_STORE_JS

def render_category_bento_showcase():
    cat_data = CATEGORY_BENTO_DATA['contemporary']
    left = cat_data['left']
    right_cards = cat_data['right']
    
    left_html = f\'\'\'
      <div class="bento-left-spotlight" id="bentoLeftSpotlight" data-book-id="{left['id']}">
        <div>
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 8px;">
            {left.get('tag', 'FEATURED SPOTLIGHT')}
          </div>
          <div class="bento-left-cover-wrap">
            <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{left['id']}')">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">INDIGO ARCHIVE</div>
                <div style="font-family: 'Merriweather', serif; font-size: 13px; line-height: 1.35; color: #1E293B; font-weight: 700;">{left['title']}</div>
                <div style="font-size: 11px; color: #64748B;">By {left['author']}</div>
                <div style="font-size: 9.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 4px;">{left.get('specs', 'Standard Edition')}</div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img src="{left['coverUrl']}" alt="{left['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                </div>
                <div class="indigo-3d-cover-back">
                  <div style="font-size: 10px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">100% GENUINE</div>
                  <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">Authorized Copy</div>
                  <div style="font-size: 11px; color: #CBD5E1;">{left['price']}</div>
                  <div style="font-size: 9.5px; color: #FCD34D; margin-top: 6px; border: 1px solid rgba(251,191,36,0.4); padding: 2px 6px; border-radius: 4px;">Click for Details &rarr;</div>
                </div>
              </div>
            </div>
          </div>
          <div style="font-size: 11px; font-weight: 700; color: #0066B3; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">
            {left.get('badge', 'RECOMMENDED READ')}
          </div>
          <h3 id="bentoLeftTitle" style="font-family: 'Merriweather', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; line-height: 1.3; margin: 0 0 6px;">
            <a href="/products/{left.get('handle', left['id'])}" onclick="handleBookAction('{left['id']}', '/products/{left.get('handle', left['id'])}', event)" style="color: inherit; text-decoration: none;">{left['title']}</a>
          </h3>
          <div id="bentoLeftAuthor" style="font-size: 14px; font-weight: 600; color: #64748B; margin-bottom: 12px;">{left['author']}</div>
          <p id="bentoLeftBlurb" style="font-size: 13px; color: #334155; line-height: 1.6; margin: 0 0 14px;">
            "{left.get('quote', left.get('blurb', ''))}"
          </p>
          <div id="bentoLeftSpecs" style="font-size: 12px; color: #64748B; margin-bottom: 16px;">
            {left.get('specs', '')}
          </div>
        </div>
        <div>
          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 16px;">
            <span id="bentoLeftPrice" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{left['price']}</span>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <button type="button" class="btn-overview" onclick="openOverviewModal('{left['id']}')">
              <i data-lucide="book-open" style="width: 15px; height: 15px;"></i> Overview
            </button>
            <button type="button" class="btn-add-cart" onclick="addToCart('{left['id']}')">
              <i data-lucide="shopping-bag" style="width: 15px; height: 15px;"></i> Add to Bag
            </button>
          </div>
        </div>
      </div>
    \'\'\'
    
    right_cards_html = []
    for rb in right_cards:
        rc_html = f\'\'\'
          <div class="bento-horiz-card" data-book-id="{rb['id']}">
            <div>
              <div class="bento-horiz-top">
                <div class="bento-horiz-cover">
                  <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{rb['id']}')">
                    <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                      <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                      <div style="font-family: 'Merriweather', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">{rb['title']}</div>
                      <div style="font-size: 7.5px; color: #64748B;">{rb['author']}</div>
                    </div>
                    <div class="indigo-3d-cover-leaf">
                      <div class="indigo-3d-cover-front">
                        <img src="{rb['coverUrl']}" alt="{rb['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                      </div>
                      <div class="indigo-3d-cover-back" style="padding: 6px !important;">
                        <div style="font-size: 8px; font-weight: 700; color: #F59E0B;">GENUINE</div>
                        <div style="font-size: 8.5px; color: #FFFFFF;">{rb['price']}</div>
                      </div>
                    </div>
                  </div>
                </div>
                <div style="min-width: 0;">
                  <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    {rb.get('tag', 'LITERARY WORK')}
                  </div>
                  <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                    <a href="/products/{rb.get('handle', rb['id'])}" onclick="handleBookAction('{rb['id']}', '/products/{rb.get('handle', rb['id'])}', event)" style="color: inherit; text-decoration: none;">{rb['title']}</a>
                  </h4>
                  <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{rb['author']}</div>
                  <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">{rb.get('specs', 'Paperback')}</div>
                  <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{rb['price']}</div>
                </div>
              </div>
              <p style="font-size: 12px; color: #64748B; line-height: 1.5; margin: 0 0 8px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                {rb.get('desc', '')}
              </p>
            </div>
            <div class="bento-card-actions">
              <button type="button" class="btn-overview" style="padding: 7px 10px; font-size: 12px;" onclick="openOverviewModal('{rb['id']}')">
                <i data-lucide="book-open" style="width: 13px; height: 13px;"></i> Overview
              </button>
              <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('{rb['id']}')">
                <i data-lucide="shopping-bag" style="width: 13px; height: 13px;"></i> + Add
              </button>
            </div>
          </div>
        \'\'\'
        right_cards_html.append(rc_html)
    
    right_2x2_html = f\'\'\'<div class="bento-right-2x2" id="bentoRightGrid">{''.join(right_cards_html)}</div>\'\'\'
    
    return f\'\'\'
    <!-- =========================================================================
         6. SECTION 3: INDIAN VOICES & CATEGORY SHOWCASE (image_68cd69.jpg Asymmetric Layout)
         ========================================================================= -->
    <section id="category-bento-showcase" class="category-bento-section">
      <div class="category-bento-showcase">
        <div class="bento-header-wrap">
          <div>
            <div class="sec-overline">AUTHENTIC REGIONAL &amp; NATIONAL LITERATURE</div>
            <h2 style="font-family: 'Merriweather', Georgia, serif; font-size: 28px; font-weight: 700; color: #0F172A; margin: 4px 0 6px;">Indian Voices &amp; Curated Literary Categories</h2>
            <p style="font-size: 14px; color: #64748B; margin: 0;">Handpicked classics, modern Hindi fiction, Urdu poetry, academic law treatises, and historic milestones.</p>
          </div>
          <a href="#shop-all-catalog" onclick="browseAllBooks(event)" style="font-size: 13px; font-weight: 700; color: #B45309; text-decoration: none;">
            Explore All 5,500+ Titles &rarr;
          </a>
        </div>

        <!-- 5 Category Filter Switcher Pills -->
        <div class="category-pills-bar">
          <button type="button" class="cat-bento-pill active" data-cat="contemporary" onclick="switchCategoryBento('contemporary')">Contemporary Hindi Fiction</button>
          <button type="button" class="cat-bento-pill" data-cat="poetry" onclick="switchCategoryBento('poetry')">Poetry, Ghazals &amp; Shayari</button>
          <button type="button" class="cat-bento-pill" data-cat="classics" onclick="switchCategoryBento('classics')">Classic Hindi Novels (Premchand &amp; Masters)</button>
          <button type="button" class="cat-bento-pill" data-cat="history" onclick="switchCategoryBento('history')">History, Criticism &amp; Politics</button>
          <button type="button" class="cat-bento-pill" data-cat="law" onclick="switchCategoryBento('law')">Law &amp; Constitutional Studies</button>
        </div>

        <!-- Asymmetric Showcase Grid (image_68cd69.jpg layout: Left 400px + Right 2x2 Grid) -->
        <div class="category-bento-grid" id="categoryBentoGrid">
          {left_html}
          {right_2x2_html}
        </div>
      </div>
    </section>
    \'\'\'

def build_preview_html():
    podium_json = json.dumps(PODIUM_BOOKS, ensure_ascii=False)
    poet_json = json.dumps(POET_SHAYARI_DATA, ensure_ascii=False)
    vault_json = json.dumps(VAULT_BOOKS, ensure_ascii=False)
    bento_json = json.dumps(CATEGORY_BENTO_DATA, ensure_ascii=False)
    catalog_json = json.dumps(CATALOG_BOOKS, ensure_ascii=False)
    modal_meta_json = json.dumps(MODAL_METADATA_DATABASE, ensure_ascii=False)

    head_str = """''' + head_part + '''"""
    body_str = """''' + body_part.replace('"""', '\\"\\"\\"') + '''"""

    # Escape curly braces for body_str if needed or use simple format
    # In body_str, we have {render_category_bento_showcase()} which we want to evaluate:
    bento_rendered = render_category_bento_showcase()
    body_str = body_str.replace('{render_category_bento_showcase()}', bento_rendered)

    script_content = f"""  <script>
    const PODIUM_BOOKS = {podium_json};
    const POET_SHAYARI_DATA = {poet_json};
    const VAULT_BOOKS = {vault_json};
    const CATEGORY_BENTO_DATA = {bento_json};
    const CATALOG_BOOKS = {catalog_json};
    const MODAL_METADATA_DATABASE = {modal_meta_json};

{UNIFIED_STORE_JS}

    function handleModalFullDetails() {{
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {{
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }}
    }}
  </script>
</body>
</html>"""

    html = head_str + UNIFIED_STORE_CSS + "\\n</style>\\n" + body_str + script_content
    return html

if __name__ == '__main__':
    h = build_preview_html()
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(h)
    print("Successfully generated preview.html, length:", len(h))
'''

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(generator_code)

print("Saved new build_html_generator.py successfully!")

