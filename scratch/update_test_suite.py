with open('scratch/verify_all_fixes_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Update Group 4 in verify_all_fixes_complete.js
old_group_4 = """--- TEST GROUP 4: Phone Number & PIN Input Validation ---*/
console.log('\\n--- TEST GROUP 4: Phone Number & PIN Input Validation ---');

test('Phone input enforces 10 digits pattern', () => {
  assert(previewHtml.includes('id="checkoutPhone"') && previewHtml.includes('pattern="[0-9]{10}"'));
});

test('PIN input enforces 6 digits pattern', () => {
  assert(previewHtml.includes('id="checkoutPincode"') && previewHtml.includes('pattern="[0-9]{6}"'));
});

test('Phone input provides explicit tooltip title', () => {
  assert(previewHtml.includes('title="Please enter a valid 10-digit mobile number'));
});

test('PIN input provides explicit tooltip title', () => {
  assert(previewHtml.includes('title="Please enter a 6-digit postal PIN code'));
});

test('Phone & PIN inputs have oninput non-digit stripping', () => {
  assert(previewHtml.includes("this.value = this.value.replace(/[^0-9]/g, '').slice(0, 10);"));
  assert(previewHtml.includes("this.value = this.value.replace(/[^0-9]/g, '').slice(0, 6);"));
});"""

new_group_4 = """--- TEST GROUP 4: Phone Number & PIN Input Validation ---*/
console.log('\\n--- TEST GROUP 4: Phone Number & PIN Input Validation ---');

test('Phone input has NO blocking HTML5 pattern tooltip traps', () => {
  assert(!previewHtml.includes('id="checkoutPhone" placeholder="Enter 10-digit mobile number" required pattern='));
});

test('PIN input has NO blocking HTML5 pattern tooltip traps', () => {
  assert(!previewHtml.includes('id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" minlength="6" required pattern='));
});

test('Checkout form has novalidate attribute (preventing browser tooltip popover)', () => {
  assert(previewHtml.includes('id="expressPhoneCheckoutForm" novalidate'));
});

test('Phone & PIN inputs have robust JS digit sanitization and length bounds', () => {
  assert(previewHtml.includes('checkoutPhone'));
  assert(previewHtml.includes('checkoutPincode'));
});

test('Order Confirmation has Instant UPI payment intent & QR support', () => {
  assert(previewHtml.includes('id="orderConfirmPayActionWrap"'));
  assert(previewHtml.includes('id="orderConfirmUpiBtn"'));
});"""

assert old_group_4 in text, "old_group_4 not found in verify_all_fixes_complete.js"
text = text.replace(old_group_4, new_group_4)

with open('scratch/verify_all_fixes_complete.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated scratch/verify_all_fixes_complete.js cleanly!")
