with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Check what needs to be replaced in Modal 1
m1_target = """      <form id="expressPhoneCheckoutForm" onsubmit="submitExpressPhoneOrder(event)">
        <!-- Phone Number -->
        <div style="margin-bottom: 14px;">
          <label style="display: block; font-size: 12.5px; font-weight: 700; color: #334155; margin-bottom: 6px;">
            Mobile Number (for Courier Tracking &amp; OTP-Free Confirmation)*
          </label>
          <div style="display: flex; gap: 8px;">
            <span style="display: flex; align-items: center; padding: 0 12px; background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px; font-weight: 600; color: #475569;">
              +91
            </span>
            <input type="tel" id="checkoutPhone" placeholder="Enter 10-digit mobile number" required pattern="[0-9]{10}" maxlength="10" minlength="10" inputmode="numeric" title="Please enter a valid 10-digit mobile number (e.g. 8840818783)" oninput="this.value = this.value.replace(/[^0-9]/g, '').slice(0, 10);" style="flex: 1; padding: 10px 14px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px;" />
          </div>
        </div>"""

print("m1_target found:", m1_target in text)

# Pincode target
pin_target = """            <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">PIN Code*</label>
            <input type="text" id="checkoutPincode" placeholder="6-digit PIN" maxlength="6" minlength="6" required pattern="[0-9]{6}" inputmode="numeric" title="Please enter a 6-digit postal PIN code" oninput="this.value = this.value.replace(/[^0-9]/g, '').slice(0, 6);" style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 13px;" />"""

print("pin_target found:", pin_target in text)
