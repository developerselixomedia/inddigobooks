import re

with open('prepare_master_blocks.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract book objects from prepare_master_blocks.py
items = re.findall(r"{\s*id:\s*['\"]([^'\"]+)['\"].*?title:\s*['\"]([^'\"]+)['\"].*?}", content, re.DOTALL)
print(f"Total books in prepare_master_blocks: {len(items)}")
for bid, title in items:
    print(f"{bid} | {title}")
