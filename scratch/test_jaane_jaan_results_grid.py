from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--window-size=1280,900')
driver = webdriver.Chrome(options=chrome_options)
try:
    p = os.path.abspath('preview.html').replace(os.sep, '/')
    driver.get('file:///' + p)
    time.sleep(2)
    driver.execute_script("""
        if (typeof window.performDedicatedSearch === 'function') {
            window.performDedicatedSearch('Jaane Jaan Lucknow');
        }
    """)
    time.sleep(2)
    driver.save_screenshot('scratch/verified_jaane_jaan_results_grid.png')
    print('Saved scratch/verified_jaane_jaan_results_grid.png')
finally:
    driver.quit()
