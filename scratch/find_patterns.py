import re

for filename in ['store_modals_and_search.py', 'editorial_video_theme.py', 'store_scripts.py', 'preview.html']:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        patterns = re.findall(r'pattern="[^"]*"', content)
        print(f'{filename}: {len(patterns)} patterns -> {patterns[:5]}')
    except Exception as e:
        print(f'{filename}: error {e}')
