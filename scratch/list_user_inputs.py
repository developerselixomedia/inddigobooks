import json

with open(r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        d = json.loads(line)
        if d.get('type') == 'USER_INPUT':
            c = d.get('content', '')
            print(f"Line {i}, Step {d.get('step_index')}, Len {len(c)}, Snippet: {repr(c[:80])}")

