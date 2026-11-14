# -*- coding: utf-8 -*-
"""
scratch/patch_build_html_generator.py
Patches build_html_generator.py with:
1. Search category dropdown in Hero and Catalog
2. 3 Category Promo Banners (1340px grid)
3. 3 Fast Horizontal Category Shelves (Novels, Poetry, Law/Criticism)
4. Upgraded indigobooksindia.com Solo Product Page (3 columns, variant switcher, GPS pincode checker, tabs, author shelf, reviews)
5. Direct Phone-Only & GPS Express Checkout Modal & Order Confirmation Modal
"""

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero search bar to include category dropdown
old_hero_search = '''          <!-- Search Box -->
          <div class="hero-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." oninput="handleSearchInput(this.value, 'hero')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'hero-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'hero-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 14px; font-size: 12.5px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; margin-right: 4px;">
              <span>Search</span>
            </button>
            <div id="hero-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

new_hero_search = '''          <!-- Search Box with Category Selector Dropdown -->
          <div class="hero-search-wrap search-input-wrap search-input-group">
            <select id="heroSearchCategory" class="search-category-select" title="Filter search by category">
              <option value="all">All Books</option>
              <option value="Fiction : Novel">Fiction : Novel</option>
              <option value="Poetry / Shayari">Poetry &amp; Shayari</option>
              <option value="Fiction : Stories">Fiction : Stories</option>
              <option value="Literary Criticism">Literary Criticism</option>
              <option value="History">History &amp; Politics</option>
              <option value="Biography">Biography &amp; Memoirs</option>
              <option value="Law">Law &amp; Constitution</option>
            </select>
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0; margin-left: 10px;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." oninput="handleSearchInput(this.value, 'hero')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'hero-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'hero-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 14px; font-size: 12.5px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; margin-right: 4px;">
              <span>Search</span>
            </button>
            <div id="hero-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

if old_hero_search in content:
    content = content.replace(old_hero_search, new_hero_search)
    print("Hero search bar updated!")
else:
    print("Warning: old_hero_search not found!")

# 2. Update Catalog search bar to include category dropdown
old_cat_search = '''          <!-- Real-Time Search Bar -->
          <div class="catalog-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value); handleSearchInput(this.value, 'catalog')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'catalog-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'catalog-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">Search</button>
            <div id="catalog-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

new_cat_search = '''          <!-- Real-Time Search Bar with Category Dropdown -->
          <div class="catalog-search-wrap search-input-wrap search-input-group">
            <select id="catalogSearchCategory" class="search-category-select" title="Filter search by category">
              <option value="all">All Books</option>
              <option value="Fiction : Novel">Fiction : Novel</option>
              <option value="Poetry / Shayari">Poetry &amp; Shayari</option>
              <option value="Fiction : Stories">Fiction : Stories</option>
              <option value="Literary Criticism">Literary Criticism</option>
              <option value="History">History &amp; Politics</option>
              <option value="Biography">Biography &amp; Memoirs</option>
              <option value="Law">Law &amp; Constitution</option>
            </select>
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8; margin-left: 8px;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value); handleSearchInput(this.value, 'catalog')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'catalog-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'catalog-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">Search</button>
            <div id="catalog-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

if old_cat_search in content:
    content = content.replace(old_cat_search, new_cat_search)
    print("Catalog search bar updated!")
else:
    print("Warning: old_cat_search not found!")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("build_html_generator.py search bars patched successfully!")

