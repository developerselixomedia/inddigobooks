with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search where window.handleSoloBuyNow is called or defined
import re
print("Occurrences of handleSoloBuyNow in preview.html:")
for m in re.finditer(r'handleSoloBuyNow', text):
    print(m.start(), text[max(0, m.start()-50):min(len(text), m.start()+100)])
