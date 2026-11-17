with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('onload="this.style.opacity=\\\'1\\\';" onerror="this.style.display=\\\'none\\\';"', 'onload="this.style.opacity=1;" onerror="this.remove();"')
text = text.replace("onload=\"this.style.opacity='1';\" onerror=\"this.style.display='none';\"", 'onload="this.style.opacity=1;" onerror="this.remove();"')

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated editorial_video_theme.py")

with open('store_scripts.py', 'r', encoding='utf-8') as f:
    st_text = f.read()

st_text = st_text.replace("onload=\"this.style.opacity='1';\" onerror=\"this.style.display='none';\"", 'onload="this.style.opacity=1;" onerror="this.remove();"')

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(st_text)
print("Updated store_scripts.py")
