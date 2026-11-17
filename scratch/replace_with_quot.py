with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace shelf
old_shelf_bg = "background-image:url(\\'\"\\' + shelfFallback + \\'\"\\')"
new_shelf_bg = "background-image:url(&quot;' + shelfFallback + '&quot;)"
old_shelf_err = "this.src=\\'\"\\' + shelfFallback + \\'\"\\'"
new_shelf_err = "this.src=&quot;' + shelfFallback + '&quot;"

assert old_shelf_bg in text, "old_shelf_bg not found"
text = text.replace(old_shelf_bg, new_shelf_bg, 1)

assert old_shelf_err in text, "old_shelf_err not found"
text = text.replace(old_shelf_err, new_shelf_err, 1)

# Replace archive
old_archive_bg = "background-image: url(\\'\"\\' + fallbackSvg + \\'\"\\')"
new_archive_bg = "background-image: url(&quot;' + fallbackSvg + '&quot;)"
old_archive_err = "this.src=\\'\"\\' + fallbackSvg + \\'\"\\'"
new_archive_err = "this.src=&quot;' + fallbackSvg + '&quot;"

assert old_archive_bg in text, "old_archive_bg not found"
text = text.replace(old_archive_bg, new_archive_bg, 1)

assert old_archive_err in text, "old_archive_err not found"
text = text.replace(old_archive_err, new_archive_err, 1)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully cleaned editorial_video_theme.py quotes!")
