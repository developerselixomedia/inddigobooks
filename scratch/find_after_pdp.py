with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="single-product-page-view"')
print("Found at:", idx)
# search for the next section after idx
next_comment = text.find('<!-- ===', idx)
print("Next comment after PDP at:", next_comment)
if next_comment != -1:
    print(text[next_comment:next_comment+200])

