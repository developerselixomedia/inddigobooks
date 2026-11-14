with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('class="stats-bar"')
print('HTML stats-bar:')
print(text[pos:pos+500])

pos2 = text.find('id="pdpDiscountBadge"')
print('pdpDiscountBadge:')
print(text[pos2-100:pos2+200])

pos3 = text.find('id="modalDiscount"')
print('modalDiscount:')
print(text[pos3-100:pos3+200])

