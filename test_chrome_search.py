# test_chrome_search.py
import subprocess
import time
import os

html_url = "file:///" + os.path.abspath("preview.html").replace("\\", "/")

# Run chrome headless with remote debugging to inspect the exact DOM and styles
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--screenshot=test_search_screenshot.png',
    '--window-size=1440,900',
    html_url
]

subprocess.run(cmd, timeout=30)
print("Screenshot taken, size:", os.path.getsize("test_search_screenshot.png"))
