with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = """.editorial-search-wrap {
    position: relative !important;
    flex: 1 1 340px !important;
    max-width: 440px !important;
  }"""

replacement = """.editorial-search-wrap {
    position: relative !important;
    flex: 1 1 340px !important;
    max-width: 440px !important;
    z-index: 1000 !important;
  }"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated .editorial-search-wrap z-index to 1000!")
else:
    print("target not found or already updated.")
