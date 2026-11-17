with open('scratch/verify_all_fixes_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re

pattern = re.compile(r'// TEST GROUP 4: Phone Number & PIN Input Validation[\s\S]*?assert\(previewHtml\.includes\(\'replace[^\n]*\n', re.MULTILINE)

replacement = """// TEST GROUP 4: Phone Number & PIN Input Validation
console.log("\\n--- TEST GROUP 4: Phone Number & PIN Input Validation ---");
assert(!previewHtml.includes('pattern="[0-9]{10}"'), "Phone input has NO blocking HTML5 pattern tooltip traps");
assert(!previewHtml.includes('pattern="[0-9]{6}"'), "PIN input has NO blocking HTML5 pattern tooltip traps");
assert(previewHtml.includes('id="expressPhoneCheckoutForm" novalidate'), "Checkout form has novalidate attribute (preventing browser tooltip popover)");
assert(previewHtml.includes('id="orderConfirmPayActionWrap"'), "Order Confirmation has Instant UPI payment intent & QR support");
assert(previewHtml.includes('id="orderConfirmUpiBtn"'), "Instant UPI pay button configured with native intent URL");
"""

text, count = pattern.subn(replacement, text)
print(f"Substitutions made: {count}")
assert count == 1

with open('scratch/verify_all_fixes_complete.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated verify_all_fixes_complete.js!")
