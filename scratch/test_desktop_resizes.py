from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

PREVIEW_FILE = os.path.abspath("preview.html")
FILE_URL = f"file:///{PREVIEW_FILE.replace(os.sep, '/')}"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

try:
    for w in [500, 700, 850, 950, 1050]:
        driver.set_window_size(w, 800)
        driver.get(FILE_URL)
        
        # Check brand group position and visibility
        bg = driver.find_element(By.CLASS_NAME, "v2-nav-brand-group")
        bg_rect = driver.execute_script("return arguments[0].getBoundingClientRect();", bg)
        bg_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", bg)
        
        # Check desktop actions
        act = driver.find_element(By.CLASS_NAME, "editorial-header-actions")
        act_rect = driver.execute_script("return arguments[0].getBoundingClientRect();", act)
        act_disp = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", act)
        
        # Check search wrap
        sw = driver.find_element(By.CLASS_NAME, "editorial-search-wrap")
        sw_rect = driver.execute_script("return arguments[0].getBoundingClientRect();", sw)
        
        print(f"Window Size: {w}px (innerWidth={driver.execute_script('return window.innerWidth;')})")
        print(f"  Brand group: rect={bg_rect}, display={bg_disp}")
        print(f"  Search wrap: rect={sw_rect}")
        print(f"  Header actions: rect={act_rect}, display={act_disp}")
        print("-" * 50)
finally:
    driver.quit()
