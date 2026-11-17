with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('1. checkoutPhone pattern:', re.findall(r'<input[^>]*checkoutPhone[^>]*>', text))
print('2. checkoutPincode pattern:', re.findall(r'<input[^>]*checkoutPincode[^>]*>', text))
print('3. #cartDrawer z-index 25000000:', '25000000' in text)
print('4. Modals z-index 30000000:', '30000000' in text)
print('5. performDedicatedSearch calls openSearchResultsPage:', 'window.openSearchResultsPage(q)' in text)
print('6. Old firstItem opener present?:', 'var firstItem = resultsBox.querySelector' in text)
print('7. Old pattern [6-9][0-9]9 present?:', '[6-9][0-9]9' in text)
print('8. Old pattern [1-9][0-9]5 present?:', '[1-9][0-9]5' in text)
