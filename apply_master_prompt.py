# -*- coding: utf-8 -*-
"""
apply_master_prompt.py
Injects MASTER_STYLE and MASTER_SCRIPT into:
1. build_html_generator.py (so preview.html is always compiled with it)
2. sync_preview_to_shopify.py (so layout/theme.liquid & sections/main-indigo-store.liquid & main-store.liquid have it)
3. Re-runs sync_preview_to_shopify.py to compile preview.html, extract assets, and package Shopify zips
4. Validates everything with verify_all_requirements.py and verify_sync_integrity.py
"""

import os
import re
import subprocess
from prepare_master_blocks import MASTER_STYLE, MASTER_SCRIPT

print("=================================================================")
print("STEP 1: Updating build_html_generator.py")
print("=================================================================")

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    bh = f.read()

# Check if prepare_master_blocks is imported
if 'from prepare_master_blocks import MASTER_STYLE, MASTER_SCRIPT' not in bh:
    bh = 'from prepare_master_blocks import MASTER_STYLE, MASTER_SCRIPT\n' + bh

# Update the end of script_content to include MASTER_STYLE and MASTER_SCRIPT
old_end_pattern = '''    function handleModalFullDetails() {
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }
    }
  </script>
</body>
</html>"""'''

new_end_pattern = '''    function handleModalFullDetails() {
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }
    }
  </script>

  <!-- MASTER PRODUCTION REALIGNMENT STYLES & SCRIPT -->
''' + MASTER_STYLE + '''
''' + MASTER_SCRIPT + '''
</body>
</html>"""'''

# Because curly braces are in script_content f-string, let's escape any single { or } in MASTER_STYLE and MASTER_SCRIPT or do a string replace after
assert 'function handleModalFullDetails()' in bh, "handleModalFullDetails not found"

# Let's see how script_content is formed in build_html_generator.py
idx_hf = bh.find('function handleModalFullDetails()')
idx_body_end = bh.find('</body>', idx_hf)
assert idx_hf != -1 and idx_body_end != -1

# Replace from </script> to </body>
bh_before = bh[:idx_body_end]
bh_after = bh[idx_body_end:]

# Escape curly braces for f-string: { -> {{ and } -> }}
def escape_fstring(text):
    return text.replace('{', '{{').replace('}', '}}')

master_blocks_fstring = '\n  <!-- MASTER PRODUCTION REALIGNMENT STYLES & SCRIPT -->\n' + escape_fstring(MASTER_STYLE) + '\n' + escape_fstring(MASTER_SCRIPT) + '\n'

if 'id="indigo-master-production-styles"' not in bh:
    bh = bh_before + master_blocks_fstring + bh_after
    with open('build_html_generator.py', 'w', encoding='utf-8') as f:
        f.write(bh)
    print("✓ build_html_generator.py updated with MASTER_STYLE and MASTER_SCRIPT")
else:
    print("✓ build_html_generator.py already contains master production styles")

print("\n=================================================================")
print("STEP 2: Updating sync_preview_to_shopify.py")
print("=================================================================")

with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    sync_code = f.read()

# 2A. Update script extraction so it extracts ALL scripts after orderConfirmationModal
old_script_extract = '''    last_script_end = html.rfind('</script>')
    if last_script_end == -1:
        raise ValueError("Could not find closing </script> in preview.html")
    last_script_start = html.rfind('<script', 0, last_script_end)
    if last_script_start == -1:
        raise ValueError("Could not find opening <script> in preview.html")
    last_script_open_end = html.find('>', last_script_start) + 1
    script_js = html[last_script_open_end:last_script_end].strip()'''

new_script_extract = '''    # Extract all store scripts after orderConfirmationModal and combine into main-store.js
    order_confirm_pos = html.find('id="orderConfirmationModal"')
    if order_confirm_pos == -1:
        order_confirm_pos = 0
    raw_scripts = re.findall(r'<script[^>]*>(.*?)</script>', html[order_confirm_pos:], re.DOTALL)
    script_js = '\\n\\n'.join([s.strip() for s in raw_scripts if s.strip()])'''

if old_script_extract in sync_code:
    sync_code = sync_code.replace(old_script_extract, new_script_extract, 1)
    print("✓ sync_preview_to_shopify.py script extraction updated")

# 2B. Update layout/theme.liquid right before </body> to include MASTER_STYLE and MASTER_SCRIPT
old_theme_end = '''    <!-- 10. LUCIDE ICONS ACTIVATION -->
    <script>
      document.addEventListener('DOMContentLoaded', function() {{
        if (typeof lucide !== 'undefined') {{
          try {{ lucide.createIcons(); }} catch(e) {{}}
        }}
      }});
      window.addEventListener('load', function() {{
        if (typeof lucide !== 'undefined') {{
          try {{ lucide.createIcons(); }} catch(e) {{}}
        }}
      }});
    </script>
  </body>'''

master_blocks_theme = '\n    <!-- MASTER PRODUCTION REALIGNMENT STYLES & SCRIPT -->\n' + escape_fstring(MASTER_STYLE) + '\n' + escape_fstring(MASTER_SCRIPT) + '\n  </body>'

if old_theme_end in sync_code and 'id="indigo-master-production-styles"' not in sync_code:
    sync_code = sync_code.replace(old_theme_end, old_theme_end.replace('  </body>', master_blocks_theme), 1)
    print("✓ layout/theme.liquid updated to include MASTER_STYLE and MASTER_SCRIPT right before </body>")

# 2C. Update sections/main-store.liquid and sections/main-indigo-store.liquid before {% schema %}
old_schema_part = '''        "{% schema %}\\n{\\n  \\"name\\": \\"Main Store\\",'''
master_blocks_section = escape_fstring(MASTER_STYLE) + '\\n\\n' + escape_fstring(MASTER_SCRIPT) + '\\n\\n'
new_schema_part = '        """' + master_blocks_section + '""",\\n        "{% schema %}\\n{\\n  \\"name\\": \\"Main Store\\",'

if old_schema_part in sync_code and 'indigo-master-production-styles' not in sync_code[:sync_code.find('main_store_content')]:
    sync_code = sync_code.replace(old_schema_part, new_schema_part, 1)
    print("✓ sections/main-store.liquid & main-indigo-store.liquid updated to include master blocks")

with open('sync_preview_to_shopify.py', 'w', encoding='utf-8') as f:
    f.write(sync_code)
print("✓ sync_preview_to_shopify.py saved")


