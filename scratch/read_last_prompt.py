import json

with open(r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in reversed(lines):
    if '"type":"USER_INPUT"' in line:
        data = json.loads(line)
        print("=== CONTENT ===")
        print(data.get("content"))
        if data.get("truncated_fields"):
            print("Truncated fields:", data.get("truncated_fields"))
        break

