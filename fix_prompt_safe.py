# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines(True)
new_lines = []
for line in lines:
    if 'switchAuthMode' in line and ('Already' in line or 'Already have an account' in line):
        new_lines.append('    if (prompt) prompt.innerHTML = \'<span style="color:#64748B;">Already a member?</span> <a href="javascript:void(0)" onclick="switchAuthMode(&quot;signin&quot;)" style="color: #0066B3; font-weight: 700; text-decoration: underline;">Sign In</a>\';\n')
    elif 'switchAuthMode' in line and ("Don't" in line or "New reader" in line or "Join" in line) and 'prompt.innerHTML' in line:
        new_lines.append('    if (prompt) prompt.innerHTML = \'<span style="color:#64748B;">New reader?</span> <a href="javascript:void(0)" onclick="switchAuthMode(&quot;signup&quot;)" style="color: #B45309; font-weight: 700; text-decoration: underline;">Join the Book Club</a>\';\n')
    else:
        new_lines.append(line)

new_text = "".join(new_lines)
with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated prompt.innerHTML with safe HTML entities and no apostrophes!")

