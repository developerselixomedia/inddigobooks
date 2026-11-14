# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("msgParts.join('\\n')", "msgParts.join(String.fromCharCode(10))")
text = text.replace('msgParts.join("\\n")', "msgParts.join(String.fromCharCode(10))")
# Also handle if literal newline is present
import re
text = re.sub(r"msgParts\.join\('[\r\n]+'\)", "msgParts.join(String.fromCharCode(10))", text)

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated msgParts.join to String.fromCharCode(10)")
