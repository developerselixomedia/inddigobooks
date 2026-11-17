with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="expressPhoneCheckoutModal"')
print('Index:', idx)
print(text[idx-300:idx+300])
