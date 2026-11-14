# -*- coding: utf-8 -*-
with open('sections/main-indigo-store.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

old_weight_tr = '''                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Weight:</th>
                      <td id="pdpSpecWeight" style="padding: 10px 14px; color: #0F172A;">270 g</td>
                    </tr>
                    <tr>
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Dimensions (L &times; B &times; H):</th>
                      <td id="pdpSpecDimensions" style="padding: 10px 14px; color: #0F172A;">21.6 &times; 14.0 &times; 1.5 cm</td>
                    </tr>'''

new_weight_tr = '''                    <tr style="border-bottom: 1px solid #F1F5F9;">
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Available Stock:</th>
                      <td id="pdpSpecQty" style="padding: 10px 14px; color: #059669; font-weight: 600;">In Stock • Ready to Dispatch</td>
                    </tr>
                    <tr>
                      <th style="padding: 10px 14px; text-align: left; background: #F8FAFC; color: #64748B;">Dimensions (L &times; B &times; H):</th>
                      <td id="pdpSpecDimensions" style="padding: 10px 14px; color: #0F172A;">21.5 &times; 14.0 &times; 1.0 cm</td>
                    </tr>'''

assert old_weight_tr in c, "old_weight_tr not found in sections/main-indigo-store.liquid"
c = c.replace(old_weight_tr, new_weight_tr)

with open('sections/main-indigo-store.liquid', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated sections/main-indigo-store.liquid!')

