with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<input type="text" id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" minlength="6" required pattern="[0-9]{6}" inputmode="numeric" style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />'
replacement = '<input type="text" id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" minlength="6" required pattern="[0-9]{6}" inputmode="numeric" title="Please enter a 6-digit postal PIN code" oninput="this.value = this.value.replace(/[^0-9]/g, \\\'\\\').slice(0, 6);" style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />'

assert target in text, "Target not found"
text = text.replace(target, replacement, 1)

with open('store_modals_and_search.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated checkoutPincode in store_modals_and_search.py!")
