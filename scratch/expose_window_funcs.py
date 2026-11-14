# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """  if (typeof lucide !== 'undefined') lucide.createIcons();
}

\"\"\""""

replacement = """  if (typeof lucide !== 'undefined') lucide.createIcons();
}

if (typeof window !== 'undefined') {
  window.searchByAuthor = searchByAuthor;
  window.browseAllBooks = browseAllBooks;
  window.toggleCartDrawer = toggleCartDrawer;
  window.addToCart = addToCart;
  window.openSearchResultsPage = openSearchResultsPage;
  window.closeSearchResultsPage = closeSearchResultsPage;
  window.openDedicatedProductPage = openDedicatedProductPage;
  window.closeDedicatedProductPage = closeDedicatedProductPage;
}

\"\"\""""

if target in text:
    text = text.replace(target, replacement)
    with open('store_scripts.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Exposed all window functions successfully!")
else:
    print("Target not found in store_scripts.py")

