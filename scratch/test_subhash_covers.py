import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

PREVIEW_FILE = os.path.abspath("preview.html")
norm_path = PREVIEW_FILE.replace(os.sep, "/")
FILE_URL = f"file:///{norm_path}"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=390,844") # Mobile viewport
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

driver = webdriver.Chrome(options=chrome_options)

try:
    print(f"Loading {FILE_URL} ...")
    driver.get(FILE_URL)
    time.sleep(2)
    
    # Trigger author filter for Subhash Kashyap
    driver.execute_script("window.filterByAuthorDirect('Subhash Kashyap');")
    time.sleep(3)
    
    # Scroll to archive grid
    grid = driver.find_element(By.ID, "v2ArchiveGrid")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", grid)
    time.sleep(2)
    
    # Check archive cards
    cards = driver.find_elements(By.CSS_SELECTOR, ".v2-archive-card")
    print(f"Found {len(cards)} archive cards for Subhash Kashyap")
    
    for i, c in enumerate(cards[:4]):
        title = c.find_element(By.CSS_SELECTOR, ".v2-archive-card-title").text
        img = c.find_element(By.CSS_SELECTOR, "img")
        src = img.get_attribute("src")
        complete = driver.execute_script("return arguments[0].complete;", img)
        nat_w = driver.execute_script("return arguments[0].naturalWidth;", img)
        nat_h = driver.execute_script("return arguments[0].naturalHeight;", img)
        print(f"Card {i+1}: {title}")
        print(f"  src: {src[:70]}...")
        print(f"  complete: {complete}, dimensions: {nat_w}x{nat_h}")
        
    # Check browser logs
    logs = driver.get_log("browser")
    errs = [l for l in logs if l.get("level") == "SEVERE" and "favicon" not in l.get("message", "")]
    print(f"Severe errors: {len(errs)}")
    for e in errs[:5]:
        print("  Error:", e.get("message"))
        
    # Take screenshot of the archive cards
    out_path = r"C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_subhash_kashyap_covers.png"
    driver.save_screenshot(out_path)
    print("Screenshot saved to", out_path)
    
finally:
    driver.quit()
