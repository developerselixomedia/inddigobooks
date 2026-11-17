with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('getFallbackCover')
while idx != -1:
    print('Found getFallbackCover at:', idx)
    print(text[idx:idx+500])
    print('='*50)
    idx = text.find('getFallbackCover', idx+1)
