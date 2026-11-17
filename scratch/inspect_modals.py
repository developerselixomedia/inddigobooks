with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

m1_start = text.find('id="expressPhoneCheckoutModal"')
m2_start = text.find('id="orderConfirmationModal"')

print(f'm1_start: {m1_start}, m2_start: {m2_start}')
print('=== MODAL 1 ===')
print(text[m1_start-100:m2_start])
print('=== MODAL 2 ===')
print(text[m2_start-50:m2_start+2500])
