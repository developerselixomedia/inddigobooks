with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '        <div class="v2-see-full-excerpt">See full excerpt</div>\n'
assert target in text, "Target div not found in editorial_video_theme.py"
text = text.replace(target, '')

# Also remove the CSS rule or set display: none !important;
old_css = """.v2-see-full-excerpt {
    display: inline-block !important;
    font-size: 13px !important;
    color: #121212 !important;
    font-weight: 600 !important;
    border-bottom: 1px solid #121212 !important;
    margin: 14px 0 24px 0 !important;
    cursor: pointer !important;
  }"""

new_css = """.v2-see-full-excerpt {
    display: none !important;
  }"""

if old_css in text:
    text = text.replace(old_css, new_css)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully removed 'See full excerpt' from editorial_video_theme.py!")

