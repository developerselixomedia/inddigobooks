with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    content = f.read()

target1 = """    .v2-solo-right-panel {
      width: 100% !important;
      height: auto !important;
      overflow: visible !important; /* Mobile: NO duplicate nested scrollbar! */
      padding: 24px 18px 80px 18px !important;
    }"""

replacement1 = """    .v2-solo-right-panel {
      width: 100% !important;
      height: auto !important;
      max-height: none !important;
      overflow: visible !important;
      overflow-x: visible !important;
      overflow-y: visible !important;
      padding: 24px 18px 80px 18px !important;
    }"""

assert target1 in content, "target1 not found in editorial_video_theme.py!"
content = content.replace(target1, replacement1, 1)

target2 = """    .v2-solo-right-panel {
      width: 100% !important;
      padding: 24px 20px 100px 20px !important; /* Bottom padding for sticky buy bar */
      box-sizing: border-box !important;
      overflow-y: visible !important;
    }"""

replacement2 = """    .v2-solo-right-panel {
      width: 100% !important;
      height: auto !important;
      max-height: none !important;
      padding: 24px 20px 100px 20px !important;
      box-sizing: border-box !important;
      overflow: visible !important;
      overflow-x: visible !important;
      overflow-y: visible !important;
    }"""

assert target2 in content, "target2 not found in editorial_video_theme.py!"
content = content.replace(target2, replacement2, 1)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated .v2-solo-right-panel overflow to fully visible on mobile!")
