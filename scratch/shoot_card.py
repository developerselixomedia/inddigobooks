from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--window-size=1280,900')
driver = webdriver.Chrome(options=chrome_options)
try:
    p = os.path.abspath('preview.html').replace(os.sep, '/')
    driver.get('file:///' + p)
    time.sleep(1)
    driver.execute_script("window.performDedicatedSearch('Jaane Jaan Lucknow');")
    time.sleep(2)
    card = driver.find_element("css selector", ".v2-search-book-card")
    card.screenshot('scratch/verified_card_closeup.png')
    print('Card screenshot saved to scratch/verified_card_closeup.png')
finally:
    driver.quit()
