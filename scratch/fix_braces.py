# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the single braces at the end of the f-string:
old_part = """    function handleModalFullDetails() {
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }
    }"""

new_part = """    function handleModalFullDetails() {{
      if (typeof currentModalBookId !== 'undefined' && currentModalBookId) {{
        closeOverviewModal();
        openDedicatedProductPage(currentModalBookId);
      }}
    }}"""

code = code.replace(old_part, new_part)

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed handleModalFullDetails braces.")

