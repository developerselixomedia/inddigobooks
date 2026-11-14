# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Checks in preview.html:')
print('8881122722 count:', text.count('8881122722'))
print('11,922 count:', text.count('11,922'))
print('11,900 count:', text.count('11,900'))
print('8933063306 count:', text.count('8933063306'))
print('single-product-page-view count:', text.count('single-product-page-view'))
print('homepage-view count:', text.count('homepage-view'))
print('id="bundles-section" count:', text.count('id="bundles-section"'))
print('Jaun Elia count:', text.count('Jaun Elia'))
print('Ahmad Faraz count:', text.count('Ahmad Faraz'))
print('Mirza Ghalib count:', text.count('Mirza Ghalib'))

