with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
found = 0
while True:
    pos = text.find('rajkamalprakashan.com', idx)
    if pos == -1:
        break
    found += 1
    if found <= 5:
        print('editorial_video_theme.py occurrence at:', pos)
        print(text[max(0, pos-80):pos+120])
        print('='*50)
    idx = pos + 22
print('Total occurrences in editorial_video_theme.py:', found)
