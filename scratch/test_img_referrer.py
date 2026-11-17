from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="referrer" content="no-referrer">
</head>
<body>
  <h1>Test Image Loading with no-referrer</h1>
  <img id="testImg" referrerpolicy="no-referrer" src="https://images.rajkamalprakashan.com/products/--1776285478375.jpg" />
</body>
</html>
"""

with open("scratch/test_no_referrer.html", "w", encoding="utf-8") as f:
    f.write(html)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
driver = webdriver.Chrome(options=chrome_options)

try:
    import os
    p = os.path.abspath("scratch/test_no_referrer.html")
    driver.get(f"file:///{p.replace(os.sep, '/')}")
    time.sleep(2)
    
    img = driver.find_element("id", "testImg")
    complete = driver.execute_script("return arguments[0].complete;", img)
    natural_w = driver.execute_script("return arguments[0].naturalWidth;", img)
    natural_h = driver.execute_script("return arguments[0].naturalHeight;", img)
    logs = driver.get_log("browser")
    
    print("Image complete:", complete)
    print("Natural dimensions:", natural_w, "x", natural_h)
    print("Browser logs:", logs)
finally:
    driver.quit()
