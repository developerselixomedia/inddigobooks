# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('function escapeJs(str) {')
idx2 = text.find('function escapeRegex(string) {')

replacement = '''function escapeJs(str) {
  if (!str) return '';
  return JSON.stringify(String(str)).slice(1, -1).replace(/'/g, "\\\\'");
}

'''

text = text[:idx1] + replacement + text[idx2:]
with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated escapeJs with JSON.stringify!')
