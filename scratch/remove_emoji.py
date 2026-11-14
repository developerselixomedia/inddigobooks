# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("'🎉 You unlocked Free Express Dispatch!'", "'FREE EXPRESS DISPATCH UNLOCKED!'")
with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced emoji successfully!")

