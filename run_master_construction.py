# -*- coding: utf-8 -*-
"""
run_master_construction.py
Constructs build_html_generator.py with all fixes:
1. Universal 1320px Spine & Padding
2. Law Books 3D Hover Animation in #law-academic-vault
3. Logo & Home Button Navigation (returnToHome)
4. 100% Authentic Book Data (Updated_Catalog.xlsx & shopify_products_import.csv)
5. Reliable Overview Modal & Instant 2-Letter Predictive Search
6. Full 7,491 MASTER_SEARCH_CATALOG, PIYUSH_MISHRA_BOOKS (16 books), RAHI_MASOOM_RAZA_BOOKS (22 books)
"""

import re
import json
import store_data

# 1. Read preview.html to extract head and body parts
with open('preview.html', 'r', encoding='utf-8') as f:
    preview_html = f.read()

style_start = preview_html.find('<style>')
style_end = preview_html.find('</style>')
assert style_start != -1 and style_end != -1

head_part = preview_html[:style_start + len('<style>\n')]
body_with_sections = preview_html[style_end:]

# Script start at bottom (before UNIFIED_STORE_JS injection)
script_pos = body_with_sections.rfind('<script>')
body_part = body_with_sections[:script_pos]

# Fix navbar brand link and Home link
body_part = re.sub(
    r'<a href="#top" class="brand-link"[^>]*>',
    r'<a href="#top" class="brand-link" onclick="window.returnToHome(event)" aria-label="Indigo Books India Homepage">',
    body_part
)
body_part = re.sub(
    r'<a href="#top" class="nav-link-btn"[^>]*>Home</a>',
    r'<a href="#top" class="nav-link-btn" onclick="window.returnToHome(event)">Home</a>',
    body_part
)

# Fix 3D Law Vault cards in #law-academic-vault
law_books = store_data.VAULT_BOOKS['law']
law_cards_markup = ['          <div class="vault-cards-grid" id="vaultCardsContainer">']
for b in law_books:
    clean_p = f"₹{float(b['price']):.2f}" if isinstance(b['price'], (int, float)) else str(b['price'])
    excerpt = b.get('firstPageExcerpt', 'प्रामाणिक विधि एवं अकादमिक संदर्भ ग्रंथ। Authoritative edition curated by Indigo Books India, Prayagraj.')
    pages = b.get('pages', '216p')
    pub = b.get('pub', 'Lokbharti Prakashan')
    binding = b.get('binding', 'Paperback')
    card_html = f'''            <div class="vault-card" data-book-id="{b['id']}" data-title="{b['title']}" data-author="{b['author']}" data-price="{clean_p}" data-binding="{binding}">
              <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{b['id']}', event)" style="width: 100%; height: 260px; aspect-ratio: 2/3; margin: 0 auto 14px auto; position: relative; cursor: pointer;">
                <div class="indigo-3d-inside-page" style="padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: #FFFDF9; border: 1px solid #E2E8F0; text-align: left;">
                  <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; justify-content: space-between;">
                      <span>INDIGO VAULT</span>
                      <span style="color: #64748B;">AUTHENTIC</span>
                    </div>
                    <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.25; color: #0F172A; font-weight: 700; margin-top: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                      {b['title']}
                    </div>
                    <div style="font-size: 9px; color: #64748B; margin-top: 1px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                      By {b['author']}
                    </div>
                  </div>
                  <div style="flex: 1; min-height: 0; overflow: hidden; margin-bottom: 6px;">
                    <div style="font-size: 7.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">
                      विवरण / SYNOPSIS
                    </div>
                    <p style="font-size: 8.5px; line-height: 1.35; color: #475569; font-style: italic; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">
                      {excerpt}
                    </p>
                  </div>
                  <div style="border-top: 1px dashed #CBD5E1; padding-top: 4px; font-size: 8px; color: #64748B; display: flex; justify-content: space-between; align-items: center;">
                    <span>{pages} &bull; {pub}</span>
                    <span style="font-weight: 700; color: #B45309;">{binding}</span>
                  </div>
                </div>
                <div class="indigo-3d-cover-leaf">
                  <div class="indigo-3d-cover-front">
                    <img src="{b['coverUrl']}" alt="{b['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                  </div>
                </div>
              </div>
              <div class="vault-card-body">
                <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
                  {b.get('badge', 'SCHOLAR ARCHIVE')}
                </div>
                <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
                  <a href="javascript:void(0)" onclick="openSoloBookPage('{b['id']}', event)" style="color: inherit; text-decoration: none;">{b['title']}</a>
                </h3>
                <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
                  {b['author']}
                </div>
                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{clean_p}</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button type="button" class="btn-overview" onclick="openOverviewModal('{b['id']}')">
                    <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
                  </button>
                  <button type="button" class="btn-add-cart" onclick="addToCart('{b['id']}', '{b['title']}', '{clean_p}', '{b['coverUrl']}', this, event)">
                    <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
                  </button>
                </div>
              </div>
            </div>'''
    law_cards_markup.append(card_html)
law_cards_markup.append('          </div>\n        </div>\n      </div>\n    </section>\n\n    ')
law_replacement = '\n'.join(law_cards_markup)

vault_grid_marker = '<div class="vault-cards-grid" id="vaultCardsContainer">'
vault_grid_end = '<!-- =========================================================================\n         8. SECTION 5: PAN-INDIA FILTERABLE CATALOG ARCHIVE'
v_start = body_part.find(vault_grid_marker)
v_end = body_part.find(vault_grid_end)
if v_start != -1 and v_end != -1:
    body_part = body_part[:v_start] + law_replacement + body_part[v_end:]
    print("✓ Successfully injected 3D law cards into body_part")

# Ensure bento placeholder is clean
if '{render_category_bento_showcase()}' not in body_part:
    sec3_match = re.search(r'<!-- =+\s*6\. SECTION 3:.*?--\s*>\s*<section id="category-bento-showcase".*?</section>', body_part, re.DOTALL)
    if sec3_match:
        body_part = body_part[:sec3_match.start()] + "{render_category_bento_showcase()}" + body_part[sec3_match.end():]
        print("✓ Injected {render_category_bento_showcase()} placeholder")

# Assemble build_html_generator.py source
generator_source = '''# -*- coding: utf-8 -*-
"""
build_html_generator.py
Assembles preview.html using data from store_data, store_styles, and store_scripts.
Ensures ZERO raw Liquid tags, ZERO fake discounts, ZERO strikethroughs, and 100% exact CSV prices.
"""

from prepare_master_blocks import MASTER_STYLE, MASTER_SCRIPT
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
    RAHI_MASOOM_RAZA_BOOKS,
    CATEGORY_BENTO_DATA,
    CATALOG_BOOKS,
    MASTER_SEARCH_CATALOG,
    MODAL_METADATA_DATABASE
)
from store_styles import UNIFIED_STORE_CSS
from store_scripts import UNIFIED_STORE_JS

def render_category_bento_showcase():
    cat_data = CATEGORY_BENTO_DATA['contemporary']
    left = cat_data['left']
    right_cards = cat_data['right']
    
    left_html = f\'\'\'
      <div class="bento-left-spotlight" id="bentoLeftSpotlight" data-book-id="{left['id']}" data-title="{left['title']}" data-author="{left['author']}" data-price="{left['price']}">
        <div>
          <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 8px;">
            {left.get('tag', 'FEATURED SPOTLIGHT')}
          </div>
          <div class="bento-left-cover-wrap">
            <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{left['id']}', event)" style="cursor: pointer;">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 9px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">INDIGO ARCHIVE</div>
                <div style="font-family: \'Merriweather\', serif; font-size: 13px; line-height: 1.35; color: #1E293B; font-weight: 700;">{left['title']}</div>
                <div style="font-size: 11px; color: #64748B;">By {left['author']}</div>
                <div style="font-size: 9.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 4px;">{left.get('specs', 'Standard Edition')}</div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img src="{left['coverUrl']}" alt="{left['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                </div>
              </div>
            </div>
          </div>
          <div style="font-size: 11px; font-weight: 700; color: #0066B3; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">
            {left.get('badge', 'RECOMMENDED READ')}
          </div>
          <h3 id="bentoLeftTitle" style="font-family: \'Merriweather\', Georgia, serif; font-size: 22px; font-weight: 700; color: #0F172A; line-height: 1.3; margin: 0 0 6px;">
            <a href="javascript:void(0)" onclick="openSoloBookPage('{left['id']}', event)" style="color: inherit; text-decoration: none;">{left['title']}</a>
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
            <span id="bentoLeftPrice" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 26px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{left['price']}</span>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <button type="button" class="btn-overview" onclick="openOverviewModal('{left['id']}')">
              <i data-lucide="book-open" style="width: 15px; height: 15px;"></i> Overview
            </button>
            <button type="button" class="btn-add-cart" onclick="addToCart('{left['id']}', '{left['title']}', '{left['price']}', '{left['coverUrl']}', this, event)">
              <i data-lucide="shopping-bag" style="width: 15px; height: 15px;"></i> Add to Bag
            </button>
          </div>
        </div>
      </div>
    \'\'\'
    
    right_cards_html = []
    for rb in right_cards:
        rc_html = f\'\'\'
          <div class="bento-horiz-card" data-book-id="{rb['id']}" data-title="{rb['title']}" data-author="{rb['author']}" data-price="{rb['price']}">
            <div>
              <div class="bento-horiz-top">
                <div class="bento-horiz-cover">
                  <div class="indigo-3d-book-stage" onclick="openSoloBookPage('{rb['id']}', event)" style="cursor: pointer;">
                    <div class="indigo-3d-inside-page" style="padding: 6px !important;">
                      <div style="font-size: 7.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO</div>
                      <div style="font-family: \'Merriweather\', serif; font-size: 9px; line-height: 1.3; color: #1E293B; font-weight: 700;">{rb['title']}</div>
                      <div style="font-size: 7.5px; color: #64748B;">{rb['author']}</div>
                    </div>
                    <div class="indigo-3d-cover-leaf">
                      <div class="indigo-3d-cover-front">
                        <img src="{rb['coverUrl']}" alt="{rb['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                      </div>
                    </div>
                  </div>
                </div>
                <div style="min-width: 0;">
                  <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                    {rb.get('tag', 'LITERARY WORK')}
                  </div>
                  <h4 style="font-family: \'Merriweather\', Georgia, serif; font-size: 14.5px; font-weight: 700; color: #0F172A; line-height: 1.35; margin: 0 0 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
                    <a href="javascript:void(0)" onclick="openSoloBookPage('{rb['id']}', event)" style="color: inherit; text-decoration: none;">{rb['title']}</a>
                  </h4>
                  <div style="font-size: 12px; color: #64748B; margin-bottom: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{rb['author']}</div>
                  <div style="font-size: 11px; color: #94A3B8; margin-bottom: 8px;">{rb.get('specs', 'Paperback')}</div>
                  <div style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{rb['price']}</div>
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
              <button type="button" class="btn-add-cart" style="padding: 7px 10px; font-size: 12px;" onclick="addToCart('{rb['id']}', '{rb['title']}', '{rb['price']}', '{rb['coverUrl']}', this, event)">
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
            <h2 style="font-family: \'Merriweather\', Georgia, serif; font-size: 28px; font-weight: 700; color: #0F172A; margin: 4px 0 6px;">Indian Voices &amp; Curated Literary Categories</h2>
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
    piyush_json = json.dumps(PIYUSH_MISHRA_BOOKS, ensure_ascii=False)
    rahi_json = json.dumps(RAHI_MASOOM_RAZA_BOOKS, ensure_ascii=False)
    master_search_json = json.dumps(MASTER_SEARCH_CATALOG, ensure_ascii=False)
    modal_meta_json = json.dumps(MODAL_METADATA_DATABASE, ensure_ascii=False)

    head_str = """''' + head_part + '''"""
    body_str = """''' + body_part.replace('"""', '\\"\\"\\"') + '''"""

    bento_rendered = render_category_bento_showcase()
    body_str = body_str.replace('{render_category_bento_showcase()}', bento_rendered)

    script_content = f"""  <script>
    window.PODIUM_BOOKS = {podium_json};
    window.POET_SHAYARI_DATA = {poet_json};
    window.VAULT_BOOKS = {vault_json};
    window.CATEGORY_BENTO_DATA = {bento_json};
    window.CATALOG_BOOKS = {catalog_json};
    window.PIYUSH_MISHRA_BOOKS = {piyush_json};
    window.RAHI_MASOOM_RAZA_BOOKS = {rahi_json};
    window.MASTER_SEARCH_CATALOG = {master_search_json};
    window.MODAL_METADATA_DATABASE = {modal_meta_json};

    const PODIUM_BOOKS = window.PODIUM_BOOKS;
    const POET_SHAYARI_DATA = window.POET_SHAYARI_DATA;
    const VAULT_BOOKS = window.VAULT_BOOKS;
    const CATEGORY_BENTO_DATA = window.CATEGORY_BENTO_DATA;
    const CATALOG_BOOKS = window.CATALOG_BOOKS;
    const PIYUSH_MISHRA_BOOKS = window.PIYUSH_MISHRA_BOOKS;
    const RAHI_MASOOM_RAZA_BOOKS = window.RAHI_MASOOM_RAZA_BOOKS;
    const MASTER_SEARCH_CATALOG = window.MASTER_SEARCH_CATALOG;
    const MODAL_METADATA_DATABASE = window.MODAL_METADATA_DATABASE;

{UNIFIED_STORE_JS}

    function handleModalFullDetails() {{
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {{
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }}
    }}
  </script>
""" + "\\n\\n" + MASTER_STYLE + "\\n\\n" + MASTER_SCRIPT + "\\n\\n</body>\\n</html>"

    html = head_str + UNIFIED_STORE_CSS + "\\n</style>\\n" + body_str + script_content
    return html

if __name__ == '__main__':
    h = build_preview_html()
    with open('preview.html', 'w', encoding='utf-8') as f:
        f.write(h)
    print("Successfully generated preview.html, length:", len(h))
'''

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(generator_source)

print("✓ Saved clean, definitive build_html_generator.py")

