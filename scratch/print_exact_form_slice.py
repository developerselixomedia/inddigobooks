with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_form_start = text.find('id=\\"expressPhoneCheckoutForm\\"')
if idx_form_start == -1: idx_form_start = text.find('expressPhoneCheckoutForm')

idx_form_end = text.find('</form>', idx_form_start)

print('Form HTML:')
print(repr(text[idx_form_start:idx_form_end+7]))
