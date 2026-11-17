with open('scratch/verify_all_fixes_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = """// TEST GROUP 4: Phone Number & PIN Input Validation
console.log("\\n--- TEST GROUP 4: Phone Number & PIN Input Validation ---");
assert(previewHtml.includes('pattern="[0-9]{10}"'), "Phone input enforces 10 digits pattern");
assert(previewHtml.includes('pattern="[0-9]{6}"'), "PIN input enforces 6 digits pattern");
assert(previewHtml.includes('title="Please enter a valid 10-digit mobile number'), "Phone input provides explicit tooltip title");
assert(previewHtml.includes('title="Please enter a 6-digit postal PIN code"'), "PIN input provides explicit tooltip title");
assert(previewHtml.includes('replace(/[^0-9]/g, \'\').slice(0, 10)'), "Phone & PIN inputs have oninput non-digit stripping");"""

replacement = """// TEST GROUP 4: Phone Number & PIN Input Validation
console.log("\\n--- TEST GROUP 4: Phone Number & PIN Input Validation ---");
assert(!previewHtml.includes('pattern="[0-9]{10}"'), "Phone input has NO blocking HTML5 pattern tooltip traps");
assert(!previewHtml.includes('pattern="[0-9]{6}"'), "PIN input has NO blocking HTML5 pattern tooltip traps");
assert(previewHtml.includes('id="expressPhoneCheckoutForm" novalidate'), "Checkout form has novalidate attribute (preventing browser tooltip popover)");
assert(previewHtml.includes('id="orderConfirmPayActionWrap"'), "Order Confirmation has Instant UPI payment intent & QR support");
assert(previewHtml.includes('id="orderConfirmUpiBtn"'), "Instant UPI pay button configured with native intent URL");"""

assert target in text, "Target not found in verify_all_fixes_complete.js"
text = text.replace(target, replacement)

with open('scratch/verify_all_fixes_complete.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated scratch/verify_all_fixes_complete.js successfully!")
