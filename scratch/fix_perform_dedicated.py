import re

with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'  /\* GLOBAL AUTHOR FILTER & DEDICATED SEARCH ENGINE \*/.*?window\.filterByAuthorFromSolo = function\(authorName\) \{\s*window\.filterByAuthorDirect\(authorName\);\s*\};'

replacement = """  /* GLOBAL AUTHOR FILTER & DEDICATED SEARCH ENGINE */
  window.performDedicatedSearch = function(query) {
    if (!query) return;
    var q = query.trim();

    // Standalone Shopify non-home page without SPA
    var isShopifyNonHome = (typeof window !== 'undefined' && 
      (window.location.pathname.indexOf('/products/') !== -1 || window.location.pathname.indexOf('/cart') !== -1 || window.location.pathname.indexOf('/collections') !== -1) &&
      !document.getElementById('indigo-search-results-view')
    );
    if (isShopifyNonHome) {
      window.location.href = '/search?q=' + encodeURIComponent(q);
      return;
    }

    // Close solo book page if open & unlock body
    if (typeof window.closeSoloBookPage === 'function') {
      window.closeSoloBookPage();
    } else {
      var soloV = document.getElementById('indigo-solo-product-view');
      if (soloV) {
        soloV.classList.remove('is-active');
        soloV.style.display = 'none';
      }
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
    }

    // Close any search dropdowns
    var resultsBox = document.getElementById('editorialSearchResults');
    if (resultsBox) resultsBox.style.display = 'none';

    // Open dedicated search results view (#indigo-search-results-view)
    if (typeof window.openSearchResultsPage === 'function') {
      window.openSearchResultsPage(q);
    } else {
      window.location.href = '/search?q=' + encodeURIComponent(q);
    }
  };

  /* DIRECT AUTHOR FILTERING FROM SHELVES & PDP */
  window.filterByAuthorDirect = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };

  window.filterByAuthorFromSolo = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };"""

new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
print(f"Replaced {count} instances.")

if count > 0:
    with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("editorial_video_theme.py updated successfully!")
else:
    print("Failed to replace using regex!")
