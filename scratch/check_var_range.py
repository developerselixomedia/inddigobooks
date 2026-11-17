with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_var = text.find('UNIFIED_STORE_JS =')
idx_close = text.find('"""', idx_var + 25)
print('Closing quotes for UNIFIED_STORE_JS at:', idx_close)
print('Total length of store_scripts.py:', len(text))
idx_render = text.find('renderCurrentSearchResults')
print('renderCurrentSearchResults at:', idx_render)
print('Is renderCurrentSearchResults INSIDE UNIFIED_STORE_JS?', idx_render < idx_close)
