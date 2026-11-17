import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

PREVIEW_FILE = os.path.abspath("preview.html")
FILE_URL = f"file:///{PREVIEW_FILE.replace(os.sep, '/')}"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

try:
    for width in [390, 487, 768, 800, 900, 1024]:
        driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
            "width": width,
            "height": 844,
            "deviceScaleFactor": 1,
            "mobile": width <= 900
        })
        driver.get(FILE_URL)
        
        # Check scatter covers visibility
        scatter_covers = driver.find_elements(By.CLASS_NAME, "scatter-book-cover")
        scatter_vis = [driver.execute_script("return window.getComputedStyle(arguments[0]).display;", c) for c in scatter_covers]
        scatter_hidden = all(d == 'none' for d in scatter_vis)
        
        # Check desktop header actions visibility
        desktop_actions = driver.find_elements(By.CLASS_NAME, "editorial-header-actions")
        desktop_act_vis = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", desktop_actions[0]) if desktop_actions else 'none'
        
        # Check mobile brand group visibility
        brand_group = driver.find_elements(By.CLASS_NAME, "v2-nav-brand-group")
        brand_vis = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", brand_group[0]) if brand_group else 'none'
        
        # Check hamburger button visibility
        hamb = driver.find_elements(By.CLASS_NAME, "v2-hamburger-btn")
        hamb_vis = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", hamb[0]) if hamb else 'none'
        
        # Check mobile deck visibility
        deck = driver.find_elements(By.CLASS_NAME, "v2-mobile-hero-showcase")
        deck_vis = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", deck[0]) if deck else 'none'

        print(f"Width={width}px:")
        print(f"  Scatter covers hidden: {scatter_hidden} (display={scatter_vis[0] if scatter_vis else 'none'})")
        print(f"  Desktop header actions display: {desktop_act_vis}")
        print(f"  Brand group display: {brand_vis}")
        print(f"  Hamburger button display: {hamb_vis}")
        print(f"  Mobile 3D deck display: {deck_vis}")
        print("-" * 50)
finally:
    driver.quit()
