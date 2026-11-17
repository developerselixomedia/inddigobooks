with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "window.addToBagDirect(\\'\' + bId + \'\\')"
target_plain = "window.addToBagDirect(\\'"
# Let's inspect around addToBagDirect in editorial_video_theme.py
idx = text.find("v2-btn-archive-add")
print("v2-btn-archive-add found at:", idx)
print(repr(text[idx-50:idx+200]))
