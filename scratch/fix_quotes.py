with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

bad_str = "return '<button type=\"button\" class=\"pdp-variant-btn ' + (i === 0 ? 'active' : '') + '\" onclick=\"selectPdpVariant(\\'' + escapeJs(v.format) + '\\')\">' +"
good_str = 'return `<button type="button" class="pdp-variant-btn ${i === 0 ? "active" : ""}" onclick="selectPdpVariant(\\\'${escapeJs(v.format)}\\\')">${escapeHtml(v.format)} &bull; ₹${parseFloat(v.price).toFixed(2)}</button>`;'

bad_str2 = "varContainer.innerHTML = '<button type=\"button\" class=\"pdp-variant-btn active\" onclick=\"selectPdpVariant(\\'' + escapeJs(book.binding || 'Paperback') + '\\')\">' +"
good_str2 = 'varContainer.innerHTML = `<button type="button" class="pdp-variant-btn active" onclick="selectPdpVariant(\\\'${escapeJs(book.binding || "Paperback")}\\\')">${escapeHtml(book.binding || "Paperback")} &bull; ${priceFormatted}</button>`;'

# Let's inspect where selectPdpVariant is generated
for l in text.splitlines():
    if 'selectPdpVariant(' in l and 'varContainer' in l or 'onclick="selectPdpVariant' in l:
        print(l)

# Let's replace any malformed selectPdpVariant onclick strings
text = text.replace("onclick=\"selectPdpVariant('' + escapeJs(v.format) + '')\"", "onclick=\"selectPdpVariant('&quot;' + escapeJs(v.format) + '&quot;')\"")
text = text.replace("onclick=\"selectPdpVariant(\\'' + escapeJs(v.format) + '\\')\"", "onclick=\"selectPdpVariant(&quot;' + escapeJs(v.format) + '&quot;)\"")
text = text.replace("onclick=\"selectPdpVariant(\\'' + escapeJs(book.binding || 'Paperback') + '\\')\"", "onclick=\"selectPdpVariant(&quot;' + escapeJs(book.binding || 'Paperback') + '&quot;)\"")

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced quotes in store_scripts.py")

