from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1440,900")
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get("data:text/html,<html><body>test</body></html>")
    w = driver.execute_script("return window.innerWidth;")
    print("Window Width with --window-size=1440,900:", w)
finally:
    driver.quit()
