import os
import json
import re

print("=== Checking blocks/*.liquid schema blocks ===")
if os.path.exists('blocks'):
    for f in sorted(os.listdir('blocks')):
        if f.endswith('.liquid'):
            path = os.path.join('blocks', f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as lf:
                content = lf.read()
            schemas = re.findall(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', content, re.DOTALL)
            for s in schemas:
                s_clean = s.strip()
                if s_clean:
                    try:
                        json.loads(s_clean)
                    except Exception as e:
                        print(f"INVALID SCHEMA in blocks/{f}: {e}")

print("Blocks check complete.")
