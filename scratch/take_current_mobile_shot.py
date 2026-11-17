from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

PREVIEW_FILE = os.path.abspath("preview.html")
FILE_URL = f"file:///{PREVIEW_FILE.replace(os.sep, '/')}"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 3,
        "mobile": True
    })
    driver.get(FILE_URL)
    driver.save_screenshot("scratch/current_mobile_live_390.png")
    print("Saved scratch/current_mobile_live_390.png")
finally:
    driver.quit()
