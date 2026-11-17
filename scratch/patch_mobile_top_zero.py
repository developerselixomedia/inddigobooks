with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = """    #indigo-solo-product-view {
      top: 60px !important;
      height: calc(100vh - 60px) !important;
      height: calc(100dvh - 60px) !important;
      padding: 0 !important;
      overflow-y: auto !important;
      -webkit-overflow-scrolling: touch !important;
    }"""

replacement = """    #indigo-solo-product-view {
      position: fixed !important;
      inset: 0 !important;
      top: 0 !important;
      left: 0 !important;
      right: 0 !important;
      bottom: 0 !important;
      width: 100% !important;
      height: 100% !important;
      height: 100dvh !important;
      padding: 0 !important;
      overflow-y: auto !important;
      -webkit-overflow-scrolling: touch !important;
    }"""

assert target in content, "target not found in editorial_video_theme.py!"
content = content.replace(target, replacement, 1)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully replaced mobile top: 60px with top: 0 in editorial_video_theme.py!")
