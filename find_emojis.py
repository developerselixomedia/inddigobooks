import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find any non-ASCII character that is in emoji ranges
emojis = re.findall(r'[\U00010000-\U0010ffff]', text)
print("Emojis found:", len(emojis), set(emojis))
for em in set(emojis):
    pos = text.find(em)
    print("Context around", em, ":", repr(text[pos-30:pos+30]))

