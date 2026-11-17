import os
import json
import re

print("=== 1. Checking templates/*.json ===")
section_files = set(f.replace('.liquid', '') for f in os.listdir('sections') if f.endswith('.liquid'))
print(f"Total sections on disk: {len(section_files)}")

for f in sorted(os.listdir('templates')):
    path = os.path.join('templates', f)
    if f.endswith('.json'):
        try:
            with open(path, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
            sections = data.get('sections', {})
            order = data.get('order', [])
            for s_id in order:
                if s_id not in sections:
                    print(f"ERROR in {f}: order lists '{s_id}' which is not in sections!")
            for s_id, s_data in sections.items():
                s_type = s_data.get('type')
                if s_type and s_type not in section_files:
                    print(f"ERROR in {f}: references non-existent section '{s_type}' (id: {s_id})")
        except Exception as e:
            print(f"JSON ERROR in {f}: {e}")

print("\n=== 2. Checking sections/*.liquid schema blocks ===")
for f in sorted(os.listdir('sections')):
    if f.endswith('.liquid'):
        path = os.path.join('sections', f)
        with open(path, 'r', encoding='utf-8', errors='ignore') as lf:
            content = lf.read()
        schemas = re.findall(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', content, re.DOTALL)
        for s in schemas:
            s_clean = s.strip()
            if s_clean:
                try:
                    json.loads(s_clean)
                except Exception as e:
                    print(f"INVALID SCHEMA in sections/{f}: {e}")

print("\n=== 3. Checking config/settings_data.json and settings_schema.json ===")
for cf in ['settings_data.json', 'settings_schema.json']:
    cp = os.path.join('config', cf)
    if os.path.exists(cp):
        try:
            with open(cp, 'r', encoding='utf-8') as jf:
                json.load(jf)
            print(f"config/{cf} valid JSON")
        except Exception as e:
            print(f"INVALID JSON in config/{cf}: {e}")

print("\n=== 4. Checking locales/*.json ===")
for lf in os.listdir('locales'):
    if lf.endswith('.json'):
        lp = os.path.join('locales', lf)
        try:
            with open(lp, 'r', encoding='utf-8') as jf:
                json.load(jf)
        except Exception as e:
            print(f"INVALID JSON in locales/{lf}: {e}")

print("\n=== 5. Checking all .liquid files for Liquid parsing problems ===")
# Check for unclosed {% or {{
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['.git', 'node_modules', '.gemini', 'v2_detailed_frames', 'indigo-books-shopify-theme']):
        continue
    for f in files:
        if f.endswith('.liquid'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as lf:
                c = lf.read()
            # check unclosed tags
            open_tags = len(re.findall(r'{%', c))
            close_tags = len(re.findall(r'%}', c))
            if open_tags != close_tags:
                print(f"TAG MISMATCH in {fp}: {open_tags} open vs {close_tags} close")
            open_vars = len(re.findall(r'{{', c))
            close_vars = len(re.findall(r'}}', c))
            if open_vars != close_vars:
                print(f"VAR MISMATCH in {fp}: {open_vars} open vs {close_vars} close")
