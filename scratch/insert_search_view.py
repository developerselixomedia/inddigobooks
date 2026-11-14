# -*- coding: utf-8 -*-
import sys
import re

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Search Box
old_hero_search = '''          <!-- Search Box -->
          <div class="hero-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." oninput="handleSearchInput(this.value, 'hero')" onkeydown="handleHeroSearch(event)" autocomplete="off" />
            <div id="hero-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

new_hero_search = '''          <!-- Search Box -->
          <div class="hero-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." oninput="handleSearchInput(this.value, 'hero')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'hero-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'hero-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 14px; font-size: 12.5px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; margin-right: 4px;">
              <span>Search</span>
            </button>
            <div id="hero-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

if old_hero_search in content:
    content = content.replace(old_hero_search, new_hero_search)
    print("Updated Hero Search input with submit button & Enter key handler.")
else:
    print("WARNING: Could not find exact old_hero_search string.")

# 2. Update Catalog Search Box
old_cat_search = '''          <!-- Real-Time Search Bar -->
          <div class="catalog-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value); handleSearchInput(this.value, 'catalog')" onkeydown="if(event.key==='Enter')performCatalogSearchEnter()" autocomplete="off" />
            <div id="catalog-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

new_cat_search = '''          <!-- Real-Time Search Bar -->
          <div class="catalog-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 16px; height: 16px; color: #94A3B8;"></i>
            <input type="text" id="catalog-search-input" placeholder="Search title, author, ISBN..." oninput="handleCatalogSearch(this.value); handleSearchInput(this.value, 'catalog')" onkeydown="if(event.key==='Enter')window.submitSearch(event, 'catalog-search-input')" autocomplete="off" />
            <button type="button" onclick="window.submitSearch(event, 'catalog-search-input')" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">Search</button>
            <div id="catalog-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>'''

if old_cat_search in content:
    content = content.replace(old_cat_search, new_cat_search)
    print("Updated Catalog Search input with submit button & Enter key handler.")
else:
    print("WARNING: Could not find exact old_cat_search string.")

# 3. Insert Dedicated Search Results Page View (#indigo-search-results-view)
search_results_view_html = '''  <!-- =========================================================================
       DEDICATED SEARCH RESULTS PAGE VIEW (#indigo-search-results-view)
       ========================================================================= -->
  <div id="indigo-search-results-view" class="store-view-section" style="display: none; background: #FAF8F5; min-height: 80vh; padding: 36px 0 64px;">
    <div class="site-container" style="max-width: 1280px; margin: 0 auto; padding: 0 24px; box-sizing: border-box;">
      
      <!-- Top Breadcrumb Bar -->
      <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 0 20px; border-bottom: 1px solid #E2E8F0; margin-bottom: 28px; font-size: 13px; color: #64748B; flex-wrap: wrap; gap: 12px;">
        <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
          <a href="#top" onclick="window.closeSearchResultsView(); return false;" style="color: #0066B3; text-decoration: none; font-weight: 600;">Home</a>
          <span style="color: #94A3B8; font-size: 12px;">&rsaquo;</span>
          <span style="color: #0F172A; font-weight: 600;">Search Results</span>
        </div>
        <button type="button" class="btn-back-to-store" onclick="window.closeSearchResultsView()" style="display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; color: #0F172A; border: 1px solid #CBD5E1; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer;">
          <i data-lucide="arrow-left" style="width: 15px; height: 15px;"></i> Back to Bookstore
        </button>
      </div>

      <!-- Search Header & Active Search Form -->
      <div style="text-align: center; max-width: 720px; margin: 0 auto 32px;">
        <div style="font-size: 11px; font-weight: 800; color: #B45309; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 6px;">
          PAN-INDIA ARCHIVE SEARCH
        </div>
        <h1 style="font-family: 'Merriweather', Georgia, serif; font-size: 32px; font-weight: 700; color: #0F172A; margin: 0 0 8px;">
          Search Results for "<span id="search-query-display"></span>"
        </h1>
        <p style="font-size: 14px; color: #64748B; margin: 0 0 20px;">
          (Found <strong id="search-result-count" style="color: #0F172A;">0</strong> books)
        </p>

        <!-- Search Input with Auto-Suggestions -->
        <form onsubmit="window.submitSearch(event, 'results-search-input'); return false;" class="search-input-wrap" style="position: relative; display: flex; align-items: center; background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 10px; padding: 6px 8px 6px 16px; box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06); gap: 10px;">
          <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
          <input
            type="text"
            id="results-search-input"
            placeholder="Search title, author, ISBN..."
            oninput="handleSearchInput(this.value, 'results')"
            style="flex: 1; border: none; outline: none; font-size: 14px; color: #0F172A; background: transparent; padding: 8px 0;"
            autocomplete="off"
          />
          <button type="submit" style="background: #0066B3; color: #FFFFFF; border: none; border-radius: 8px; padding: 10px 20px; font-size: 13.5px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 6px;">
            Search
          </button>
          <div id="results-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
        </form>
      </div>

      <!-- Filter & Sort Toolbar -->
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 28px; padding: 12px 16px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;">
        <!-- Category Filter Pills -->
        <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;" id="searchResultsCategoryPills">
          <button type="button" class="cat-pill active" onclick="filterSearchResults('all', this)" style="padding: 6px 14px; font-size: 12px;">All Matches</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('bestseller', this)" style="padding: 6px 14px; font-size: 12px;">Bestsellers</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('rekhta', this)" style="padding: 6px 14px; font-size: 12px;">Rekhta &amp; Poetry</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('hindi', this)" style="padding: 6px 14px; font-size: 12px;">Hindi Fiction</button>
          <button type="button" class="cat-pill" onclick="filterSearchResults('law', this)" style="padding: 6px 14px; font-size: 12px;">Law Books</button>
        </div>

        <!-- Sort Dropdown -->
        <div style="display: flex; align-items: center; gap: 8px;">
          <label for="searchResultsSort" style="font-size: 12.5px; font-weight: 600; color: #64748B;">Sort by:</label>
          <select id="searchResultsSort" onchange="sortSearchResults(this.value)" style="border: 1px solid #CBD5E1; border-radius: 6px; padding: 6px 12px; font-size: 12.5px; font-weight: 600; color: #0F172A; background: #FFFFFF; outline: none; cursor: pointer;">
            <option value="featured">Featured Relevance</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
            <option value="title-asc">Title: A-Z</option>
          </select>
        </div>
      </div>

      <!-- 4-Column Responsive Results Grid -->
      <div id="search-results-grid" class="catalog-cards-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;">
        <!-- Rendered dynamically by window.openSearchResultsPage -->
      </div>

    </div>
  </div><!-- /#indigo-search-results-view -->

'''

home_end = '</div><!-- /#homepage-view -->'
if home_end in content:
    content = content.replace(home_end, home_end + '\n\n\n' + search_results_view_html)
    print("Inserted #indigo-search-results-view right after #homepage-view.")
else:
    print("ERROR: Could not find </div><!-- /#homepage-view --> in build_html_generator.py")
    sys.exit(1)

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("build_html_generator.py updated successfully.")

