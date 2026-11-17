with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('function openExpressPhoneCheckout(bookId, qty)')
end = text.find('function closeOrderConfirmationModal()')

print('Start:', start, 'End:', end)
print(text[start:start+1000])
print('---')
print(text[end-500:end])
