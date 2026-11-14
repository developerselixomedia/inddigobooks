# -*- coding: utf-8 -*-
with open("store_scripts.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace escapeRegex with clean valid regex
old_pattern = """function escapeRegex(string) {
  return string.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
}"""

clean_pattern = """function escapeRegex(string) {
  return string.replace(/[-\\/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&');
}"""

if old_pattern in text:
    text = text.replace(old_pattern, clean_pattern)
    print("Replaced exact pattern")
else:
    # Use index search
    idx = text.find("function escapeRegex")
    if idx != -1:
        end_idx = text.find("}", idx) + 1
        text = text[:idx] + clean_pattern + text[end_idx:]
        print("Replaced by index")

with open("store_scripts.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated store_scripts.py")

