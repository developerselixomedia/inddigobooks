with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

start_needle = "// Format Selection Handlers: Sibling Variant Lookup from Master Catalog"
end_needle = "applyFormat(activeInitialFmt);"

start_idx = text.find(start_needle)
end_idx = text.find(end_needle)

print(f'Start: {start_idx}, End: {end_idx}')
print(text[start_idx:end_idx + len(end_needle)])
