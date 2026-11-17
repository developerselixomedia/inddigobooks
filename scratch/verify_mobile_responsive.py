import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def run_mobile_tests():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    # Mobile viewport: iPhone 14/15 size (390 x 844)
    chrome_options.add_argument('--window-size=390,844')

    driver = webdriver.Chrome(options=chrome_options)
    
    file_path = os.path.abspath('preview.html')
    driver.get(f'file:///{file_path}')
    time.sleep(2)

    # Check for console severe errors
    errors = []
    logs = driver.get_log('browser')
    for log in logs:
        if log['level'] == 'SEVERE':
            errors.append(log['message'])
    print(f"Browser severe errors: {errors}")
    assert len(errors) == 0, f"Found JavaScript errors: {errors}"

    print("\n--- TEST 1: Mobile Header & Hamburger Button Visibility ---")
    hamburger_btn = driver.find_element(By.ID, 'v2MobileMenuBtn')
    is_hamburger_displayed = hamburger_btn.is_displayed()
    print(f"Hamburger button displayed: {is_hamburger_displayed}")
    assert is_hamburger_displayed, "Hamburger button must be visible on mobile!"

    # Verify desktop links are hidden
    nav_links = driver.find_element(By.CSS_SELECTOR, '.nav-editorial-links')
    assert not nav_links.is_displayed(), "Desktop navigation links must be hidden on mobile!"

    # Verify mobile bag button is displayed
    mobile_bag_btn = driver.find_element(By.CSS_SELECTOR, '.v2-mobile-bag-btn')
    assert mobile_bag_btn.is_displayed(), "Mobile bag button must be visible on mobile!"

    driver.save_screenshot('scratch/verified_mobile_header.png')

    print("\n--- TEST 2: Open Mobile Navigation Drawer ---")
    driver.execute_script("arguments[0].click();", hamburger_btn)
    time.sleep(0.5)

    drawer = driver.find_element(By.ID, 'v2MobileDrawer')
    backdrop = driver.find_element(By.ID, 'v2MobileDrawerBackdrop')
    
    drawer_classes = drawer.get_attribute('class')
    print(f"Drawer classes after click: {drawer_classes}")
    assert 'is-open' in drawer_classes, "Drawer should have 'is-open' class!"

    backdrop_classes = backdrop.get_attribute('class')
    print(f"Backdrop classes after click: {backdrop_classes}")
    assert 'is-open' in backdrop_classes, "Backdrop should have 'is-open' class!"

    driver.save_screenshot('scratch/verified_mobile_drawer_open.png')

    print("\n--- TEST 3: Mobile Drawer Author Filter Click ---")
    drawer_author_btns = drawer.find_elements(By.CSS_SELECTOR, '.v2-author-pill-btn')
    print(f"Found {len(drawer_author_btns)} author buttons inside mobile drawer")
    assert len(drawer_author_btns) >= 8, f"Expected at least 8 author pills, got {len(drawer_author_btns)}"

    # Click Premchand in drawer
    premchand_btn = None
    for b in drawer_author_btns:
        if 'Premchand' in b.text:
            premchand_btn = b
            break
    assert premchand_btn is not None, "Premchand button not found in drawer!"
    driver.execute_script("arguments[0].click();", premchand_btn)
    time.sleep(1)

    # Drawer should be closed
    assert 'is-open' not in drawer.get_attribute('class'), "Drawer should be closed after author click!"
    
    # Archive should display Premchand's books
    genre = driver.execute_script("return window.getArchiveGenre();")
    query = driver.execute_script("return window.getArchiveQuery();")
    print(f"Archive after drawer author click -> genre: {genre}, query: {query}")
    assert genre == 'all', f"Expected genre 'all', got {genre}"
    assert query == 'premchand', f"Expected query 'premchand', got {query}"

    archive_cards = driver.find_elements(By.CSS_SELECTOR, '#v2ArchiveGrid .v2-archive-card')
    print(f"Rendered archive cards: {len(archive_cards)}")
    assert len(archive_cards) > 0, "Expected archive cards to render for Premchand!"

    driver.save_screenshot('scratch/verified_mobile_author_filter_result.png')

    print("\n--- TEST 4: Mobile Search Bar & Edge-to-Edge Dropdown ---")
    search_input = driver.find_element(By.ID, 'editorialSearchInput')
    driver.execute_script("arguments[0].value = '';", search_input)
    search_input.send_keys('prem')
    time.sleep(0.5)

    results_box = driver.find_element(By.ID, 'editorialSearchResults')
    assert results_box.is_displayed(), "Mobile search results dropdown should be visible!"

    items = results_box.find_elements(By.CSS_SELECTOR, '.editorial-search-item')
    print(f"Found {len(items)} items in mobile search dropdown for 'prem'")
    assert len(items) >= 3, "Expected at least 3 items in mobile search dropdown"

    driver.save_screenshot('scratch/verified_mobile_search_dropdown.png')

    print("\n--- TEST 5: Mobile Solo Book Page & Sticky Mobile Buy Bar ---")
    # Click first search item to open solo book view
    driver.execute_script("arguments[0].click();", items[0])
    time.sleep(1)

    solo_view = driver.find_element(By.ID, 'indigo-solo-product-view')
    assert solo_view.is_displayed(), "Solo book page must be open!"

    # Verify sticky mobile buy bar is visible on mobile
    sticky_bar = driver.find_element(By.CSS_SELECTOR, '.v2-solo-mobile-buy-bar')
    assert sticky_bar.is_displayed(), "Sticky mobile buy bar must be visible on mobile!"
    
    mob_price = driver.find_element(By.ID, 'v2MobileBuyBarPrice').text
    mob_fmt = driver.find_element(By.ID, 'v2MobileBuyBarFormat').text
    print(f"Initial mobile buy bar -> format: {mob_fmt}, price: {mob_price}")
    assert 'paperback' in mob_fmt.lower(), f"Initial format should be Paperback, got {mob_fmt}!"

    # Test format switch to Hardcover
    btn_hc = driver.find_element(By.ID, 'v2FormatHardcover')
    driver.execute_script("arguments[0].click();", btn_hc)
    time.sleep(0.5)

    mob_price_hc = driver.find_element(By.ID, 'v2MobileBuyBarPrice').text
    mob_fmt_hc = driver.find_element(By.ID, 'v2MobileBuyBarFormat').text
    print(f"After switching to Hardcover -> format: {mob_fmt_hc}, price: {mob_price_hc}")
    assert 'hardcover' in mob_fmt_hc.lower(), f"Format should update to Hardcover Deluxe, got {mob_fmt_hc}!"
    assert mob_price_hc != mob_price, "Price should increase for Hardcover!"

    driver.save_screenshot('scratch/verified_mobile_solo_page.png')

    # Close solo book page
    close_btn = driver.find_element(By.CSS_SELECTOR, '.v2-solo-back-btn')
    driver.execute_script("arguments[0].click();", close_btn)
    time.sleep(0.5)
    assert not solo_view.is_displayed(), "Solo view should close after back button click!"

    print("\n--- TEST 6: Mobile Archive 2-Column Grid ---")
    archive_grid = driver.find_element(By.ID, 'v2ArchiveGrid')
    grid_cols = driver.execute_script("return window.getComputedStyle(arguments[0]).gridTemplateColumns;", archive_grid)
    print(f"Mobile archive grid columns: {grid_cols}")
    num_cols = len(grid_cols.split())
    print(f"Computed column count: {num_cols}")
    assert num_cols == 2, f"Mobile grid must have 2 columns on phones, got {num_cols}!"

    driver.save_screenshot('scratch/verified_mobile_2col_grid.png')

    driver.quit()
    print("\n>>> ALL MOBILE RESPONSIVE TESTS PASSED SUCCESSFULLY WITH ZERO ERRORS! <<<")

if __name__ == '__main__':
    run_mobile_tests()
