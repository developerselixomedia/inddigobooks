with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function openOverviewModal(')
print(text[pos:pos+1500])

