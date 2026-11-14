import re

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()

keys = set(re.findall(r'HINDI_FEATURE_BOOK\[[\'"]([^\'"]+)[\'"]\]', content))
print('HINDI_FEATURE_BOOK keys:', sorted(list(keys)))

other_matches = set(re.findall(r'\[[\'"]([a-zA-Z0-9_]+)[\'"]\]', content))
print('Total keys accessed in brackets:', len(other_matches))
