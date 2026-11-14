# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        <div class="stat-card">
          <div class="stat-number">24-Hr</div>
          <div class="stat-label">Express Dispatch from Prayagraj</div>
        </div>"""

replacement = """        <div class="stat-card">
          <div class="stat-number">30%</div>
          <div class="stat-label">Max Savings on Bundles</div>
        </div>"""

if target in text:
    text = text.replace(target, replacement)
    with open('build_html_generator.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated 3rd stat in build_html_generator.py to 30% Max Savings on Bundles")
else:
    print("Target not found in build_html_generator.py")

