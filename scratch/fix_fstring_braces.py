# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace any single braces in onclick scrollTo / scrollIntoView
code = code.replace("window.scrollTo({top: 0, behavior: 'smooth'})", "window.scrollTo({{top: 0, behavior: 'smooth'}})")
code = code.replace("window.scrollTo({top: 0, behavior: 'smooth'});", "window.scrollTo({{top: 0, behavior: 'smooth'}});")
code = code.replace("scrollIntoView({behavior: 'smooth'})", "scrollIntoView({{behavior: 'smooth'}})")
code = code.replace("scrollIntoView({behavior: 'smooth'});", "scrollIntoView({{behavior: 'smooth'}});")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed scrollTo and scrollIntoView braces in build_html_generator.py")

