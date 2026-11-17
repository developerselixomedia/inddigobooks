import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def run_tests():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1400,1000')

    driver = webdriver.Chrome(options=chrome_options)
    
    file_path = os.path.abspath('preview.html')
    driver.get(f'file:///{file_path}')
    time.sleep(2)

    errors = []
    logs = driver.get_log('browser')
    for log in logs:
        if log['level'] == 'SEVERE':
            errors.append(log['message'])
    print(f"Browser severe errors: {errors}")
    assert len(errors) == 0, f"Found JavaScript errors: {errors}"

    print("\n--- TEST 1: Shelf Slider Arrows & Author Pill Buttons ---")
    arrow_btns = driver.find_elements(By.CSS_SELECTOR, '.v2-shelf-arrow-btn')
    print(f"Found {len(arrow_btns)} shelf arrow buttons")
    assert len(arrow_btns) >= 8, f"Expected at least 8 arrow buttons, found {len(arrow_btns)}"

    author_pills = driver.find_elements(By.CSS_SELECTOR, '.v2-author-pill-btn')
    print(f"Found {len(author_pills)} author pill buttons")
    assert len(author_pills) >= 8, f"Expected at least 8 author pill buttons, found {len(author_pills)}"

    # Test slide shelf
    stage = driver.find_element(By.ID, 'v2ShelfPopular').find_element(By.XPATH, '..')
    scroll_before = driver.execute_script("return arguments[0].scrollLeft;", stage)
    print(f"Popular shelf scrollLeft before: {scroll_before}")
    
    # Click right arrow
    driver.execute_script("window.slideShelf('v2ShelfPopular', 1);")
    time.sleep(0.5)
    scroll_after = driver.execute_script("return arguments[0].scrollLeft;", stage)
    print(f"Popular shelf scrollLeft after right slide: {scroll_after}")
    assert scroll_after > scroll_before, "Shelf did not scroll right!"

    # Slide back left
    driver.execute_script("window.slideShelf('v2ShelfPopular', -1);")
    time.sleep(0.5)
    scroll_back = driver.execute_script("return arguments[0].scrollLeft;", stage)
    print(f"Popular shelf scrollLeft after left slide: {scroll_back}")

    print("\n--- TEST 2: Author Pill Button Click (Directs to Author's Books) ---")
    # Find Premchand pill button
    premchand_pill = None
    for p in author_pills:
        if 'Premchand' in p.text:
            premchand_pill = p
            break
    assert premchand_pill is not None, "Premchand pill button not found!"
    driver.execute_script("arguments[0].click();", premchand_pill)
    time.sleep(1)

    # Check archive state
    genre = driver.execute_script("return window.getArchiveGenre ? window.getArchiveGenre() : 'unknown';")
    query = driver.execute_script("return window.getArchiveQuery ? window.getArchiveQuery() : 'unknown';")
    cards = driver.find_elements(By.CSS_SELECTOR, '#v2ArchiveGrid .v2-archive-card')
    print(f"Archive genre: {genre}, query: {query}, rendered cards: {len(cards)}")
    assert genre == 'all', f"Expected genre 'all', got {genre}"
    assert query == 'premchand', f"Expected query 'premchand', got {query}"
    assert len(cards) > 0, "Expected archive cards for Premchand!"

    driver.save_screenshot('scratch/verified_premchand_author_pill.png')

    print("\n--- TEST 3: Empty State Handling (Image 3 Fix) ---")
    # Simulate selecting 'poetry' genre and searching 'shrilal shukla'
    driver.execute_script("""
        if (typeof window.setArchiveFilter === 'function') {
            window.setArchiveFilter('poetry', 'shrilal shukla');
        }
    """)
    time.sleep(0.5)

    empty_state = driver.find_elements(By.CSS_SELECTOR, '.v2-archive-empty-state')
    print(f"Empty state elements found: {len(empty_state)}")
    assert len(empty_state) == 1, "Expected empty state element when no books match filter!"
    empty_text = empty_state[0].text
    print(f"Empty state text: {empty_text}")
    assert 'No books found matching' in empty_text, "Empty state message missing!"
    assert 'Rekhta & Urdu Poetry' in empty_text, "Genre name missing in empty state!"

    driver.save_screenshot('scratch/verified_empty_state_image3_fix.png')

    # Click the clear filter button in the empty state
    clear_btn = driver.find_element(By.CSS_SELECTOR, '.v2-btn-clear-filter')
    driver.execute_script("arguments[0].click();", clear_btn)
    time.sleep(0.5)

    # Now verify books are loaded across all categories
    genre_after = driver.execute_script("return window.getArchiveGenre ? window.getArchiveGenre() : 'unknown';")
    cards_after = driver.find_elements(By.CSS_SELECTOR, '#v2ArchiveGrid .v2-archive-card')
    print(f"After clear filter -> genre: {genre_after}, rendered cards: {len(cards_after)}")
    assert genre_after == 'all', "Genre should be reset to 'all'!"
    assert len(cards_after) > 0, "Cards should be displayed after clearing category filter!"

    driver.save_screenshot('scratch/verified_after_clear_filter.png')

    print("\n--- TEST 4: Top Search Bar with Author Name (Image 2 Fix) ---")
    search_input = driver.find_element(By.ID, 'editorialSearchInput')
    driver.execute_script("arguments[0].value = '';", search_input)
    search_input.send_keys('prem')
    time.sleep(0.5)

    results_box = driver.find_element(By.ID, 'editorialSearchResults')
    is_displayed = results_box.is_displayed()
    print(f"Results box displayed: {is_displayed}")
    assert is_displayed, "Search dropdown should be visible when typing 'prem'!"

    items = results_box.find_elements(By.CSS_SELECTOR, '.editorial-search-item')
    print(f"Found {len(items)} search suggestion items for 'prem'")
    assert len(items) >= 3, f"Expected at least 3 items, found {len(items)}"

    top_3_titles = [it.find_element(By.CSS_SELECTOR, 'div > div:first-child').text for it in items[:3]]
    print(f"Top 3 titles for 'prem': {top_3_titles}")
    assert any('Godan' in t for t in top_3_titles), "Godan must be in top 3 results for prem!"
    assert any('Gaban' in t for t in top_3_titles), "Gaban must be in top 3 results for prem!"
    assert any('Nirmala' in t for t in top_3_titles), "Nirmala must be in top 3 results for prem!"

    driver.save_screenshot('scratch/verified_top_search_author_prem.png')

    # Test top search for 'piyush mishra'
    driver.execute_script("arguments[0].value = '';", search_input)
    search_input.send_keys('piyush mishra')
    time.sleep(0.5)
    pm_items = results_box.find_elements(By.CSS_SELECTOR, '.editorial-search-item')
    top_pm_title = pm_items[0].find_element(By.CSS_SELECTOR, 'div > div:first-child').text
    print(f"Top title for 'piyush mishra': {top_pm_title}")
    assert 'Kuchh Ishq' in top_pm_title, "Top book for Piyush Mishra must be Kuchh Ishq Kiya!"

    # Test top search for 'shrilal shukla'
    driver.execute_script("arguments[0].value = '';", search_input)
    search_input.send_keys('shrilal shukla')
    time.sleep(0.5)
    ss_items = results_box.find_elements(By.CSS_SELECTOR, '.editorial-search-item')
    top_ss_title = ss_items[0].find_element(By.CSS_SELECTOR, 'div > div:first-child').text
    print(f"Top title for 'shrilal shukla': {top_ss_title}")
    assert 'Raag Darbari' in top_ss_title, "Top book for Shrilal Shukla must be Raag Darbari!"

    print("\n--- TEST 5: Solo Book Page Author Click ---")
    # Open solo page for a book
    driver.execute_script("window.openSoloBookPage('godan-premchand');")
    time.sleep(1)

    solo_view = driver.find_element(By.ID, 'indigo-solo-product-view')
    assert solo_view.is_displayed(), "Solo book view should be open!"

    # Click author name on solo view
    author_elem = driver.find_element(By.ID, 'v2SoloAuthor')
    print(f"Solo view author element text: {author_elem.text}")
    driver.execute_script("arguments[0].click();", author_elem)
    time.sleep(1)

    # Solo view should be closed and archive displaying author books
    assert not solo_view.is_displayed(), "Solo book view should be closed after clicking author!"
    cards_author = driver.find_elements(By.CSS_SELECTOR, '#v2ArchiveGrid .v2-archive-card')
    print(f"Cards rendered after clicking author from solo: {len(cards_author)}")
    assert len(cards_author) > 0, "Author books must be rendered!"

    driver.save_screenshot('scratch/verified_solo_author_click_to_archive.png')

    driver.quit()
    print("\n>>> ALL TESTS PASSED SUCCESSFULLY WITH ZERO ERRORS! <<<")

if __name__ == '__main__':
    run_tests()
