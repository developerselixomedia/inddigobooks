import os

with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

target1 = 'pattern="[6-9][0-9]9"'
target2 = 'pattern="[1-9][0-9]5"'

if target1 in text:
    print("Found target1")
    text = text.replace('pattern="[6-9][0-9]9" maxlength="10"', 'pattern="[0-9]{10}" maxlength="10" minlength="10" inputmode="numeric"')
    text = text.replace('pattern="[6-9][0-9]9"', 'pattern="[0-9]{10}" minlength="10" inputmode="numeric"')

if target2 in text:
    print("Found target2")
    text = text.replace('maxlength="6" required pattern="[1-9][0-9]5"', 'maxlength="6" minlength="6" required pattern="[0-9]{6}" inputmode="numeric"')
    text = text.replace('pattern="[1-9][0-9]5"', 'pattern="[0-9]{6}" minlength="6" inputmode="numeric"')

with open('store_modals_and_search.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated store_modals_and_search.py successfully!")
