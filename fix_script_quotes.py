# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines(True)
new_lines = []
for line in lines:
    if 'switchAuthMode' in line and 'Already have an account' in line:
        new_lines.append('    if (prompt) prompt.innerHTML = `Already have an account? <span onclick="switchAuthMode(\'signin\')" style="color: #0066B3; font-weight: 700; cursor: pointer; text-decoration: underline;">Sign In</span>`;\n')
    elif 'switchAuthMode' in line and "Don't have an account" in line:
        new_lines.append('    if (prompt) prompt.innerHTML = `Don\'t have an account? <span onclick="switchAuthMode(\'signup\')" style="color: #B45309; font-weight: 700; cursor: pointer; text-decoration: underline;">Join the Book Club</span>`;\n')
    else:
        new_lines.append(line)

new_text = "".join(new_lines)
with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Fixed prompt.innerHTML lines in store_scripts.py")

