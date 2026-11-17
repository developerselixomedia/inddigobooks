with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('id=\\"expressPhoneCheckoutModal\\"')
if idx1 == -1: idx1 = text.find('expressPhoneCheckoutModal')

idx2 = text.find('id=\\"orderConfirmationModal\\"')
if idx2 == -1: idx2 = text.find('orderConfirmationModal')

print('idx1:', idx1, 'idx2:', idx2)
print('Modal 1 snippet:')
print(text[idx1:idx1+1200])

print('Modal 2 snippet:')
print(text[idx2:idx2+1200])
