import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ARTIFACT_DIR = r"C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c"
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
    
    target_path = os.path.join(ARTIFACT_DIR, "verified_mobile_1_home.png")
    driver.save_screenshot(target_path)
    print(f"Successfully updated {target_path}!")
finally:
    driver.quit()
