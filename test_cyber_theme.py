# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    preview = f.read()
with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    liquid = f.read()

assert 'id="indigo-futuristic-cyber-theme"' in preview, 'Missing cyber style in preview.html'
assert 'id="indigo-futuristic-cyber-script"' in preview, 'Missing cyber script in preview.html'
assert 'id="indigo-futuristic-cyber-theme"' in liquid, 'Missing cyber style in layout/theme.liquid'
assert 'id="indigo-futuristic-cyber-script"' in liquid, 'Missing cyber script in layout/theme.liquid'

pos_style_p = preview.rfind('id="indigo-futuristic-cyber-theme"')
pos_script_p = preview.rfind('id="indigo-futuristic-cyber-script"')
pos_body_p = preview.rfind('</body>')

assert pos_style_p < pos_script_p < pos_body_p, 'Cyber blocks not right before </body> in preview.html'

pos_style_l = liquid.rfind('id="indigo-futuristic-cyber-theme"')
pos_script_l = liquid.rfind('id="indigo-futuristic-cyber-script"')
pos_body_l = liquid.rfind('</body>')

assert pos_style_l < pos_script_l < pos_body_l, 'Cyber blocks not right before </body> in layout/theme.liquid'

print('>>> PREVIEW.HTML & LAYOUT/THEME.LIQUID VALIDATION 100% PASSED! <<<')
