import json

with open(r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i in [7508, 7531, 7547, 7555, 7565, 7567, 7572]:
            d = json.loads(line)
            c = d.get('content', '')
            print(f"Line {i}: type={d.get('type')}, snippet={repr(c[:200])}")

