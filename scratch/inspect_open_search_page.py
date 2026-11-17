with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.openSearchResultsPage')
if idx == -1:
    idx = text.find('openSearchResultsPage')
print(text[idx-50:idx+1500])
