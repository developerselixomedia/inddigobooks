with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update min-width: 901px to min-width: 1025px
target1 = "@media (min-width: 901px) {"
replacement1 = "@media (min-width: 1025px) {"
assert target1 in content, "target1 not found in editorial_video_theme.py!"
content = content.replace(target1, replacement1, 1)

# 2. Update max-width: 900px for solo view to max-width: 1024px
target2 = "@media (max-width: 900px) {\n    #indigo-solo-product-view {"
replacement2 = "@media (max-width: 1024px) {\n    #indigo-solo-product-view {"
assert target2 in content, "target2 not found in editorial_video_theme.py!"
content = content.replace(target2, replacement2, 1)

# 3. Update max-width: 900px for mobile header to max-width: 1024px
target3 = "@media (max-width: 900px) {\n    /* Sticky 2-Row Contained Mobile Header */"
replacement3 = "@media (max-width: 1024px) {\n    /* Sticky 2-Row Contained Mobile Header */"
assert target3 in content, "target3 not found in editorial_video_theme.py!"
content = content.replace(target3, replacement3, 1)

# 4. Update max-width: 768px for scatter hero to max-width: 1024px
target4 = "/* ==========================================================================\n     PHONES & NARROW SCREENS (<= 768px)\n     ========================================================================== */\n  @media (max-width: 768px) {"
replacement4 = "/* ==========================================================================\n     PHONES & TABLETS / MOBILE VIEW (<= 1024px)\n     ========================================================================== */\n  @media (max-width: 1024px) {"
assert target4 in content, "target4 not found in editorial_video_theme.py!"
content = content.replace(target4, replacement4, 1)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated all media query breakpoints to 1024px in editorial_video_theme.py!")
