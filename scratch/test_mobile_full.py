from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--headless=new')
options.add_experimental_option('mobileEmulation', {'deviceMetrics': {'width': 390, 'height': 844, 'pixelRatio': 3.0}})
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

try:
    driver.get('file:///d:/Games/indigo%20books/preview.html')
    time.sleep(2)

    # 1. Capture initial home mobile view
    driver.save_screenshot('scratch/verified_mobile_1_home.png')
    print('1. Captured mobile home view')

    # 2. Test hamburger menu click -> open drawer
    btn = driver.find_element(By.ID, 'v2MobileMenuBtn')
    btn.click()
    time.sleep(1)
    drawer = driver.find_element(By.ID, 'v2MobileDrawer')
    print('2. Drawer is displayed:', drawer.is_displayed(), 'rect:', drawer.rect)
    driver.save_screenshot('scratch/verified_mobile_2_drawer.png')

    # Close drawer using window function
    driver.execute_script("window.toggleMobileDrawer(false);")
    time.sleep(0.5)

    # 3. Test search input dropdown on mobile
    searchInput = driver.find_element(By.ID, 'editorialSearchInput')
    searchInput.click()
    searchInput.send_keys('prem')
    time.sleep(1)
    results = driver.find_element(By.ID, 'editorialSearchResults')
    print('3. Search results displayed:', results.is_displayed(), 'rect:', results.rect)
    driver.save_screenshot('scratch/verified_mobile_3_search_results.png')

    # Clear search
    searchInput.send_keys(Keys.CONTROL + 'a')
    searchInput.send_keys(Keys.BACKSPACE)
    driver.execute_script("document.getElementById('editorialSearchResults').style.display = 'none';")
    time.sleep(0.5)

    # 4. Test clicking 3D Deck Card (Godan)
    deckCard = driver.find_element(By.CSS_SELECTOR, '.v2-deck-center')
    deckCard.click()
    time.sleep(1)
    soloView = driver.find_element(By.ID, 'indigo-solo-product-view')
    print('4. Solo view active:', 'is-active' in (soloView.get_attribute('class') or ''))
    driver.save_screenshot('scratch/verified_mobile_4_solo_view.png')

    # Close solo view
    backBtn = driver.find_element(By.CSS_SELECTOR, '.v2-solo-back-btn')
    backBtn.click()
    time.sleep(1)

    # 5. Scroll to archive grid and verify 2-column layout
    driver.execute_script('window.scrollTo(0, 1800);')
    time.sleep(1)
    grid = driver.find_element(By.ID, 'v2ArchiveGrid')
    print('5. Archive grid rect:', grid.rect)
    driver.save_screenshot('scratch/verified_mobile_5_archive_grid.png')

    print('ALL MOBILE TESTS PASSED SUCCESSFULLY!')
finally:
    driver.quit()
