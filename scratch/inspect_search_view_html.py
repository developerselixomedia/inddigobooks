with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="indigo-search-results-view"')
print("In store_modals_and_search.py at:", idx)
if idx != -1:
    print(text[idx:idx+1500])
