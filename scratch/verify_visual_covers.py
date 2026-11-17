from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

PREVIEW_FILE = os.path.abspath("preview.html")
FILE_URL = f"file:///{PREVIEW_FILE.replace(os.sep, '/')}"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1280,900")
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Navigating to preview...")
    driver.get(FILE_URL)
    time.sleep(2)

    # 1. Search for Jaane Jaan Lucknow
    print("Executing search for 'Jaane Jaan Lucknow'...")
    driver.execute_script("""
        var input = document.getElementById('editorialSearchInput');
        if (input) {
            input.value = 'Jaane Jaan Lucknow';
            input.dispatchEvent(new Event('input', { bubbles: true }));
            if (typeof window.executeSearchAction === 'function') {
                window.executeSearchAction('Jaane Jaan Lucknow');
            }
        }
    """)
    time.sleep(1.5)
    driver.save_screenshot("scratch/verified_jaane_jaan_search.png")
    print("Saved scratch/verified_jaane_jaan_search.png")

    # 2. Open Solo Book Page for Jaag Piyari Ab Ka Sovai
    print("Opening Solo Book Page for 'Jaag Piyari Ab Ka Sovai'...")
    driver.execute_script("""
        if (typeof window.openSoloBookPage === 'function') {
            window.openSoloBookPage('9789377470036');
        }
    """)
    time.sleep(1.5)
    driver.save_screenshot("scratch/verified_jaag_piyari_solo.png")
    print("Saved scratch/verified_jaag_piyari_solo.png")

    # 3. Test clicking the search button [ (Q) ] on the Solo page
    print("Testing Solo Page search button activator [ (Q) ]...")
    driver.execute_script("""
        var btn = document.getElementById('v2SoloCardSearchBtn');
        if (btn) btn.click();
    """)
    time.sleep(1)
    solo_display = driver.execute_script("""
        var solo = document.getElementById('indigo-solo-product-view');
        return solo ? window.getComputedStyle(solo).display : 'none';
    """)
    search_focused = driver.execute_script("""
        return document.activeElement === document.getElementById('editorialSearchInput');
    """)
    print(f"After search button click: solo display = '{solo_display}', search input focused = {search_focused}")
    driver.save_screenshot("scratch/verified_solo_search_closed.png")
    print("Saved scratch/verified_solo_search_closed.png")

    # 4. Mobile view test for Jaag Piyari solo page
    print("Testing mobile view for solo page...")
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 3,
        "mobile": True
    })
    driver.execute_script("""
        if (typeof window.openSoloBookPage === 'function') {
            window.openSoloBookPage('9789377470036');
        }
    """)
    time.sleep(1.5)
    driver.save_screenshot("scratch/verified_mobile_solo_jaag_piyari.png")
    print("Saved scratch/verified_mobile_solo_jaag_piyari.png")

    print("\nVisual verification script completed successfully!")
finally:
    driver.quit()
