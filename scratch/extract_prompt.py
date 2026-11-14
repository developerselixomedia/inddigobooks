import json

full_path = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.system_generated\logs\transcript_full.jsonl'
with open(full_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in reversed(lines):
    d = json.loads(line)
    if d.get('type') == 'USER_INPUT':
        prompt = d.get('content', '')
        with open('scratch/current_goal.txt', 'w', encoding='utf-8') as out:
            out.write(prompt)
        print(f"Full prompt extracted! Length: {len(prompt)} characters.")
        break
