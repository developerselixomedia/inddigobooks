with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="single-product-page-view"')
print("Found id='single-product-page-view' at:", idx)

# Find the start of that comment before the div
comment_start = text.rfind('<!--', 0, idx)
print("Comment start:", comment_start)

# Find where single-product-page-view ends (before dedicated search results view)
next_view = text.find('id="indigo-search-results-view"')
print("Next view at:", next_view)
view_end = text.rfind('<!--', 0, next_view)
print("View end at:", view_end)

