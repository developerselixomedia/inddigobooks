with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('function openExpressPhoneCheckout(bookId, qty)')
end = text.find('function closeOrderConfirmationModal()')

print(text[start:end])
