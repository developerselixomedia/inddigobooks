with open('store_data.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('MASTER_SEARCH_CATALOG')
print("MASTER_SEARCH_CATALOG in store_data.py at:", idx)
if idx != -1:
    print(text[idx-50:idx+800])
