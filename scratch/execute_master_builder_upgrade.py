# -*- coding: utf-8 -*-
"""
scratch/execute_master_builder_upgrade.py
Rebuilds build_html_generator.py to include:
1. Category dropdown in search bars
2. Category Discovery Promo Banners (1340px grid)
3. 3 Horizontal Category Shelves (Novels, Poetry, Law/Criticism)
4. Upgraded Solo Product Page matching indigobooksindia.com (3 columns, variant switcher, GPS pincode checker, tabs, author shelf, reviews)
5. 1-Click Phone-Only & GPS Express Checkout Modal and Order Confirmation Modal
"""

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update imports from store_data
old_import = """from store_data import (
    PODIUM_BOOKS,
    POET_SHAYARI_DATA,
    REKHTA_BOOKS,
    HINDI_FEATURE_BOOK,
    HINDI_GRID_BOOKS,
    VAULT_TABS,
    VAULT_BOOKS,
    CATALOG_BOOKS,
    MODAL_METADATA_DATABASE
)"""

new_import = """from store_data import (
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
)"""

if old_import in text:
    text = text.replace(old_import, new_import)
    print("Imports updated!")

# 2. Add shelf rendering helper before build_preview_html
shelf_helper = """
def render_shelf_book_card(b):
    if not b: return ''
    return f'''
        <div class="shelf-book-card" data-book-id="{b['id']}" data-handle="{b['handle']}">
          <div class="indigo-3d-book-stage" onclick="window.openSoloBookPage('{b['id']}', this)">
            <div class="indigo-3d-inside-page">
              <div style="font-size: 8.5px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">
                INDIGO ARCHIVE
              </div>
              <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.35; color: #1E293B; font-weight: 700;">
                {b['title']}
              </div>
              <div style="font-size: 9.5px; color: #64748B;">
                By {b['author']}
              </div>
              <div style="font-size: 8.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 3px;">
                {b.get('pages', '250p')} &bull; {b.get('pub', 'Lokbharti')}
              </div>
            </div>
            <div class="indigo-3d-cover-leaf">
              <div class="indigo-3d-cover-front">
                <img src="{b['cover']}" alt="{b['title']}" loading="lazy" />
              </div>
              <div class="indigo-3d-cover-back">
                <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                  100% GENUINE
                </div>
                <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                  {b['pub']}
                </div>
                <div style="font-size: 9.5px; color: #CBD5E1;">
                  {b['binding']} &bull; {b['price']}
                </div>
                <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                  Click for Details &rarr;
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top: 10px; display: flex; flex-direction: column; flex: 1; justify-content: space-between;">
            <div>
              <div style="font-family: 'Merriweather', serif; font-size: 13.5px; font-weight: 700; color: #0F172A; line-height: 1.3; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; cursor: pointer;" onclick="window.openSoloBookPage('{b['id']}', this)" title="{b['title']}">
                {b['title']}
              </div>
              <div style="font-size: 12px; color: #64748B; margin-top: 2px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                {b['author']}
              </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
              <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; font-weight: 800; color: #0F172A;">{b['price']}</span>
              <button type="button" onclick="window.addToCart('{b['id']}', '{b['title']}', '{b['raw_price']}', '{b['cover']}', '{b['binding']}', this)" style="background: #0F172A; color: #FFFFFF; border: none; border-radius: 6px; padding: 4px 10px; font-size: 11.5px; font-weight: 700; cursor: pointer;">
                Add
              </button>
            </div>
          </div>
        </div>
    '''
"""

if "def render_shelf_book_card" not in text:
    idx = text.find("def build_preview_html():")
    text = text[:idx] + shelf_helper + "\n" + text[idx:]
    print("Shelf card helper added!")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Step 1 of generator upgrade finished!")

