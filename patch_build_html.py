# -*- coding: utf-8 -*-
"""
patch_build_html.py
Updates build_html_generator.py to:
1. Add CATEGORY_BENTO_DATA import and render_category_bento_showcase() function.
2. Replace Section 3 with the Asymmetric Category Bento Showcase (image_68cd69.jpg).
3. Remove duplicate Section 7B category shelves.
4. Remove all fake discount badges, strikethroughs, star ratings, and reviews.
5. Add catalog pagination container.
6. Add 3D book hover stages to Rekhta and Bento cards.
"""

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update imports
old_import = '''from store_data import (
    PODIUM_BOOKS,
    POET_SHAYARI_DATA,
    REKHTA_BOOKS,
    HINDI_FEATURE_BOOK,
    HINDI_GRID_BOOKS,
    VAULT_TABS,
    VAULT_BOOKS,
    CATEGORY_SHELVES,
    PIYUSH_MISHRA_BOOKS,
    CATALOG_BOOKS,
    MODAL_METADATA_DATABASE
)'''

new_import = '''from store_data import (
    PODIUM_BOOKS,
    POET_SHAYARI_DATA,
    REKHTA_BOOKS,
    HINDI_FEATURE_BOOK,
    HINDI_GRID_BOOKS,
    VAULT_TABS,
    VAULT_BOOKS,
    CATEGORY_SHELVES,
    PIYUSH_MISHRA_BOOKS,
    CATEGORY_BENTO_DATA,
    CATALOG_BOOKS,
    MODAL_METADATA_DATABASE
)'''

assert old_import in content, "old_import not found"
content = content.replace(old_import, new_import, 1)

# 2. Add render_category_bento_showcase() before def build_preview_html():
bento_func = '''
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

'''

insert_pos = content.find('def build_preview_html():')
assert insert_pos != -1, "build_preview_html not found"
content = content[:insert_pos] + bento_func + content[insert_pos:]

# 3. Update Stats Bar item
old_stat = '''        <div class="stat-card">
          <div class="stat-number">30%</div>
          <div class="stat-label">Max Savings on Bundles</div>
        </div>'''

new_stat = '''        <div class="stat-card">
          <div class="stat-number">24-Hr</div>
          <div class="stat-label">Express Dispatch from Prayagraj</div>
        </div>'''

assert old_stat in content, "old_stat not found"
content = content.replace(old_stat, new_stat, 1)

# 4. Update Marquee item
content = content.replace('UPSC &amp; JUDICIARY SCHOLAR DISCOUNTS', 'UPSC &amp; JUDICIARY SCHOLAR EDITIONS')

# 5. Remove Podium Rating Row and Strikethrough/Discount
old_podium_rating = '''            <div class="podium-rating-row">
              <div class="stars-group">
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
                <i data-lucide="star" style="width: 15px; height: 15px; fill: currentColor;"></i>
              </div>
              <span id="podiumSpotRating" style="font-size: 13px; font-weight: 600; color: #475569;">{PODIUM_BOOKS[0]['rating']}</span>
            </div>'''

assert old_podium_rating in content, "old_podium_rating not found"
content = content.replace(old_podium_rating, '', 1)

old_podium_prices = '''            <div class="podium-price-row">
              <span id="podiumSpotPrice" class="podium-curr-price">{PODIUM_BOOKS[0]['price']}</span>
              <span id="podiumSpotOldPrice" class="podium-old-price">{PODIUM_BOOKS[0]['oldPrice']}</span>
              <span id="podiumSpotDiscount" class="discount-pill">{PODIUM_BOOKS[0]['discount']}</span>
            </div>'''

new_podium_prices = '''            <div class="podium-price-row">
              <span id="podiumSpotPrice" class="podium-curr-price">{PODIUM_BOOKS[0]['price']}</span>
            </div>'''

assert old_podium_prices in content, "old_podium_prices not found"
content = content.replace(old_podium_prices, new_podium_prices, 1)

# 6. Hero Cards Hover and Mouseleave
for idx in range(6):
    old_card_str = f'data-hero-idx="{idx}" onclick='
    new_card_str = f'data-hero-idx="{idx}" onmouseenter="handleHeroBookHover({idx})" onmouseleave="handleHeroGridMouseLeave()" onclick='
    if old_card_str in content:
        content = content.replace(old_card_str, new_card_str, 1)

# 7. Clean Rekhta Cards prices and add 3D stage
old_rekhta_block = '''          <div class="rekhta-book-card" data-poet="{b.get('poet', 'all')}" data-book-id="{b['id']}" data-title="{b['title']}" data-author="{b['author']}" data-price="{b['price']}">
            <div class="rekhta-cover-wrap" onclick="handleBookAction('{b['id']}', '/products/{b.get('handle', b['id'])}', event)" style="cursor: pointer;">
              <img src="{b['coverUrl']}" alt="{b['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/{b.get('handle', b['id'])}" onclick="handleBookAction('{b['id']}', '/products/{b.get('handle', b['id'])}', event)" style="color: inherit; text-decoration: none;">{b['title']}</a>
            </h3>
            <div class="rekhta-card-author">{b['author']}</div>
            <div class="rekhta-card-desc">{b['desc']}</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">{b['price']}</span>
              {f\'<span style="font-size: 12px; text-decoration: line-through; color: #64748B;">{b["oldPrice"]}</span>\' if b.get("oldPrice") else \'\'}
              {f\'<span class="discount-pill" style="font-size: 10px;">{b["discount"]}</span>\' if b.get("discount") and b.get("oldPrice") else \'\'}
            </div>'''

new_rekhta_block = '''          <div class="rekhta-book-card" data-poet="{b.get('poet', 'all')}" data-book-id="{b['id']}" data-title="{b['title']}" data-author="{b['author']}" data-price="{b['price']}">
            <div class="indigo-3d-book-stage" onclick="handleBookAction('{b['id']}', '/products/{b.get('handle', b['id'])}', event)" style="margin-bottom: 12px; cursor: pointer;">
              <div class="indigo-3d-inside-page">
                <div style="font-size: 8.5px; font-weight: 700; color: #B45309; text-transform: uppercase;">INDIGO ARCHIVE</div>
                <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.35; color: #1E293B; font-weight: 700;">{b['title']}</div>
                <div style="font-size: 9.5px; color: #64748B;">{b['author']}</div>
              </div>
              <div class="indigo-3d-cover-leaf">
                <div class="indigo-3d-cover-front">
                  <img src="{b['coverUrl']}" alt="{b['title']}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);"/>
                </div>
                <div class="indigo-3d-cover-back">
                  <div style="font-size: 9px; font-weight: 700; color: #F59E0B;">100% GENUINE</div>
                  <div style="font-size: 9.5px; color: #CBD5E1;">{b['price']}</div>
                </div>
              </div>
            </div>
            <h3 class="rekhta-card-title">
              <a href="/products/{b.get('handle', b['id'])}" onclick="handleBookAction('{b['id']}', '/products/{b.get('handle', b['id'])}', event)" style="color: inherit; text-decoration: none;">{b['title']}</a>
            </h3>
            <div class="rekhta-card-author">{b['author']}</div>
            <div class="rekhta-card-desc">{b['desc']}</div>
            <div class="rekhta-card-price-row">
              <span class="rekhta-curr-price">{b['price']}</span>
            </div>'''

assert old_rekhta_block in content, "old_rekhta_block not found"
content = content.replace(old_rekhta_block, new_rekhta_block, 1)

# 8. Replace Section 6 (#contemporary-fiction) with Category Bento Showcase
sec6_start = content.find('<!-- =========================================================================\n         6. SECTION 3: INDIAN VOICES')
sec6_end = content.find('<!-- =========================================================================\n         7. SECTION 4: LAW, JUDICIARY')
assert sec6_start != -1 and sec6_end != -1, "sec6 bounds not found"

content = content[:sec6_start] + "{render_category_bento_showcase()}\n\n    " + content[sec6_end:]

# 9. Clean Law Vault: Remove strikethrough price and update institutional text
old_vault_price = '''                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{b['price']}</span>
                  {f\'<span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">{b["oldPrice"]}</span>\' if b.get("oldPrice") else \'\'}
                </div>'''

new_vault_price = '''                <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
                  <span style="font-size: 18px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">{b['price']}</span>
                </div>'''

assert old_vault_price in content, "old_vault_price not found"
content = content.replace(old_vault_price, new_vault_price, 1)

content = content.replace(
    'Special discounts and invoice billing for Bar Council members, Law Chambers, and University Libraries.',
    'Bulk institutional order supply and invoice billing for Bar Council members, Law Chambers, and University Libraries.'
)

# 10. Remove Section 7B (the duplicate category shelves)
sec7b_start = content.find('<!-- =========================================================================\n         7B. FAST HORIZONTAL CATEGORY SHELVES')
sec7b_end = content.find('<!-- =========================================================================\n         8. SECTION 5: PAN-INDIA FILTERABLE CATALOG ARCHIVE')
assert sec7b_start != -1 and sec7b_end != -1, "sec7b bounds not found"

content = content[:sec7b_start] + content[sec7b_end:]

# 11. Add Catalog Pagination container
old_cat_grid = '''        <!-- 4-Column Responsive Grid of Books -->
        <div class="catalog-cards-grid" id="catalogGridContainer">
          <!-- Rendered by store_scripts.js -->
        </div>'''

new_cat_grid = '''        <!-- 4-Column Responsive Grid of Books -->
        <div class="catalog-cards-grid" id="catalogGridContainer">
          <!-- Rendered by store_scripts.js -->
        </div>

        <!-- Catalog Pagination Controls (12 Books per Page) -->
        <div id="catalogPagination" class="catalog-pagination"></div>'''

assert old_cat_grid in content, "old_cat_grid not found"
content = content.replace(old_cat_grid, new_cat_grid, 1)

# 12. PDP: Remove pdpComparePrice, pdpDiscountBadge, and #pdpReviewsCard
old_pdp_price = '''          <div class="pdp-price-wrap" style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
            <span id="pdpSellingPrice" class="pdp-selling-price" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 28px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            <span id="pdpComparePrice" class="pdp-compare-price" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 16px; text-decoration: line-through; color: #94A3B8; font-variant-numeric: lining-nums tabular-nums !important;">₹400.00</span>
            <span id="pdpDiscountBadge" class="pdp-discount-badge" style="background: #FEF2F2; color: #DC2626; border: 1px solid #FEE2E2; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 4px;">25% OFF</span>
            <span style="font-size: 12px; color: #64748B;">(Inclusive of all taxes)</span>
          </div>'''

new_pdp_price = '''          <div class="pdp-price-wrap" style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
            <span id="pdpSellingPrice" class="pdp-selling-price" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 28px; font-weight: 800; color: #0F172A; font-variant-numeric: lining-nums tabular-nums !important;">₹299.00</span>
            <span style="font-size: 12px; color: #64748B;">(Inclusive of all taxes)</span>
          </div>'''

assert old_pdp_price in content, "old_pdp_price not found"
content = content.replace(old_pdp_price, new_pdp_price, 1)

reviews_start = content.find('<!-- Customer Reviews Card -->')
reviews_end = content.find('  <!-- =========================================================================\n       11. GLOBAL FOOTER')
assert reviews_start != -1 and reviews_end != -1, "reviews bounds not found"

content = content[:reviews_start] + "    </div>\n  </div>\n\n" + content[reviews_end:]

# 13. Overview Modal: Remove modalMrp and modalDiscount
old_modal_price = '''          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
            <span id="modalPrice" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 24px; font-weight: 800; color: #09132C; font-variant-numeric: lining-nums tabular-nums !important;">₹695.00</span>
            <span id="modalMrp" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 14px; text-decoration: line-through; color: #94A3B8; font-variant-numeric: lining-nums tabular-nums !important;">₹899.00</span>
            <span id="modalDiscount" class="discount-pill" style="font-size: 11px;">25% OFF</span>
          </div>'''

new_modal_price = '''          <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px;">
            <span id="modalPrice" style="font-family: \'Plus Jakarta Sans\', sans-serif; font-size: 24px; font-weight: 800; color: #09132C; font-variant-numeric: lining-nums tabular-nums !important;">₹695.00</span>
          </div>'''

assert old_modal_price in content, "old_modal_price not found"
content = content.replace(old_modal_price, new_modal_price, 1)

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS! build_html_generator.py successfully updated and patched.")
