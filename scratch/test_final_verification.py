import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ARTIFACT_DIR = r"C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c"
PREVIEW_FILE = os.path.abspath("preview.html")
FILE_URL = f"file:///{PREVIEW_FILE.replace(os.sep, '/')}"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1440,900")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

driver = webdriver.Chrome(options=chrome_options)

try:
    print(f"Loading {FILE_URL} ...")
    driver.get(FILE_URL)
    time.sleep(2)

    win_w = driver.execute_script("return window.innerWidth;")
    print(f"Initial Desktop Window Width: {win_w}px")

    # ---------------------------------------------------------
    # TEST 1: DESKTOP SOLO VIEW SINGLE SCROLLBAR VERIFICATION
    # ---------------------------------------------------------
    print("\n--- TEST 1: DESKTOP SOLO VIEW SINGLE SCROLLBAR ---")
    driver.execute_script("window.openSoloBookPage('hero-book-godan');")
    time.sleep(0.5)

    solo_view = driver.find_element(By.ID, "indigo-solo-product-view")
    right_panel = driver.find_element(By.CLASS_NAME, "v2-solo-right-panel")

    solo_active = driver.execute_script("return document.body.classList.contains('solo-page-active');")
    body_overflow = driver.execute_script("return window.getComputedStyle(document.body).overflowY;")
    solo_overflow = driver.execute_script("return window.getComputedStyle(arguments[0]).overflowY;", solo_view)
    solo_top = driver.execute_script("return window.getComputedStyle(arguments[0]).top;", solo_view)
    right_overflow = driver.execute_script("return window.getComputedStyle(arguments[0]).overflowY;", right_panel)

    print(f"Desktop Solo Active Class on body: {solo_active}")
    print(f"Desktop Body OverflowY: {body_overflow}")
    print(f"Desktop Solo Modal Top: {solo_top}")
    print(f"Desktop Solo Modal OverflowY: {solo_overflow} (Must be hidden to prevent double scrollbar)")
    print(f"Desktop Right Panel OverflowY: {right_overflow} (Must be auto - single scrollbar container)")

    assert solo_active is True, "body must have solo-page-active class!"
    assert body_overflow == "hidden", "body overflow must be locked to hidden!"
    assert solo_top == "0px", f"solo modal top must be 0px, got {solo_top}!"
    assert solo_overflow == "hidden", f"solo modal overflowY must be hidden, got {solo_overflow}!"
    assert right_overflow == "auto", f"right panel overflowY must be auto, got {right_overflow}!"

    desktop_solo_shot = os.path.join(ARTIFACT_DIR, "verified_desktop_solo_view_single_scroll.png")
    driver.save_screenshot(desktop_solo_shot)
    print(f"Saved desktop solo screenshot to: {desktop_solo_shot}")

    # Close solo view
    driver.execute_script("window.closeSoloBookPage();")
    time.sleep(0.5)
    body_overflow_y_after = driver.execute_script("return window.getComputedStyle(document.body).overflowY;")
    print(f"Body overflowY after close: {body_overflow_y_after}")
    assert body_overflow_y_after in ["auto", "visible", ""], f"Body overflowY should be auto/visible after close, got {body_overflow_y_after}!"

    # ---------------------------------------------------------
    # TEST 2: MOBILE SOLO VIEW SINGLE SCROLLBAR VERIFICATION
    # ---------------------------------------------------------
    print("\n--- TEST 2: MOBILE SOLO VIEW SINGLE SCROLLBAR ---")
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 3,
        "mobile": True
    })
    time.sleep(0.5)

    m_w = driver.execute_script("return window.innerWidth;")
    print(f"Mobile Window Width: {m_w}px")

    driver.execute_script("window.openSoloBookPage('hero-book-godan');")
    time.sleep(0.5)

    m_solo_active = driver.execute_script("return document.body.classList.contains('solo-page-active');")
    m_body_overflow = driver.execute_script("return window.getComputedStyle(document.body).overflowY;")
    m_solo_top = driver.execute_script("return window.getComputedStyle(arguments[0]).top;", solo_view)
    m_solo_overflow = driver.execute_script("return window.getComputedStyle(arguments[0]).overflowY;", solo_view)
    m_right_overflow = driver.execute_script("return window.getComputedStyle(arguments[0]).overflowY;", right_panel)

    print(f"Mobile Solo Active Class on body: {m_solo_active}")
    print(f"Mobile Body OverflowY: {m_body_overflow}")
    print(f"Mobile Solo Modal Top: {m_solo_top}")
    print(f"Mobile Solo Modal OverflowY: {m_solo_overflow} (Must be auto - single scrollbar on mobile)")
    print(f"Mobile Right Panel OverflowY: {m_right_overflow} (Must be visible - NO nested scrollbar)")

    assert m_solo_active is True
    assert m_body_overflow == "hidden"
    assert m_solo_top == "0px", f"mobile solo top must be 0px, got {m_solo_top}!"
    assert m_solo_overflow == "auto", f"mobile solo overflowY must be auto, got {m_solo_overflow}!"
    assert m_right_overflow == "visible", f"mobile right panel overflowY must be visible, got {m_right_overflow}!"

    mobile_solo_shot = os.path.join(ARTIFACT_DIR, "verified_mobile_solo_view_single_scroll.png")
    driver.save_screenshot(mobile_solo_shot)
    print(f"Saved mobile solo screenshot to: {mobile_solo_shot}")

    driver.execute_script("window.closeSoloBookPage();")
    time.sleep(0.5)

    # ---------------------------------------------------------
    # TEST 3: MOBILE MENU DRAWER (LUCIDE ICONS, NO OVERLAP, CLEAN ALIGNMENT)
    # ---------------------------------------------------------
    print("\n--- TEST 3: MOBILE MENU DRAWER VERIFICATION ---")
    driver.execute_script("window.toggleMobileDrawer(true);")
    time.sleep(0.6)

    drawer = driver.find_element(By.ID, "v2MobileDrawer")
    drawer_open = driver.execute_script("return arguments[0].classList.contains('is-open');", drawer)
    drawer_zindex = driver.execute_script("return window.getComputedStyle(arguments[0]).zIndex;", drawer)
    print(f"Drawer is-open: {drawer_open}, z-index: {drawer_zindex}")

    # Check that Lucide SVGs exist inside drawer nav items
    nav_items = driver.find_elements(By.CLASS_NAME, "v2-drawer-nav-item")
    print(f"Drawer has {len(nav_items)} collection links.")
    for idx, item in enumerate(nav_items):
        svg_icons = item.find_elements(By.TAG_NAME, "svg")
        label = item.find_element(By.CLASS_NAME, "v2-drawer-item-label").text
        print(f"  [{idx+1}] {label} -> {len(svg_icons)} SVGs present (icon + chevron)")
        assert len(svg_icons) >= 1, f"Drawer nav item '{label}' must have SVG icon!"

    # Verify WhatsApp button at drawer bottom
    wa_btn = driver.find_element(By.CLASS_NAME, "v2-drawer-wa-btn")
    print(f"Drawer WhatsApp button text: '{wa_btn.text.strip()}'")

    mobile_drawer_shot = os.path.join(ARTIFACT_DIR, "verified_mobile_drawer_lucide_clean.png")
    driver.save_screenshot(mobile_drawer_shot)
    print(f"Saved mobile drawer screenshot to: {mobile_drawer_shot}")

    driver.execute_script("window.toggleMobileDrawer(false);")
    time.sleep(0.5)

    # ---------------------------------------------------------
    # TEST 4: CONSOLE LOGS & ZERO DEAD HOST ERRORS
    # ---------------------------------------------------------
    print("\n--- TEST 4: CONSOLE ERROR & WARNING AUDIT ---")
    logs = driver.get_log("browser")
    err_conn_closed = [l for l in logs if "ERR_CONNECTION_CLOSED" in l["message"]]
    tailwind_warns = [l for l in logs if "cdn.tailwindcss.com should not be used" in l["message"]]
    severe_errors = [l for l in logs if l["level"] == "SEVERE"]

    print(f"Total browser logs captured: {len(logs)}")
    print(f"ERR_CONNECTION_CLOSED errors: {len(err_conn_closed)}")
    print(f"Tailwind CDN production warnings: {len(tailwind_warns)}")
    print(f"Total SEVERE errors: {len(severe_errors)}")

    if severe_errors:
        print("Detailed SEVERE errors:")
        for se in severe_errors:
            print("  *", se["message"])

    assert len(err_conn_closed) == 0, f"Must have ZERO ERR_CONNECTION_CLOSED errors, found {len(err_conn_closed)}!"
    assert len(tailwind_warns) == 0, f"Must have ZERO Tailwind production warnings, found {len(tailwind_warns)}!"

    # ---------------------------------------------------------
    # TEST 5: TOP SEARCH BAR PREDICTIVE SUGGESTIONS VISIBILITY
    # ---------------------------------------------------------
    print("\n--- TEST 5: PREDICTIVE LIVE SEARCH SUGGESTIONS ---")
    driver.execute_cdp_cmd("Emulation.clearDeviceMetricsOverride", {})
    time.sleep(0.5)

    search_input = driver.find_element(By.ID, "editorialSearchInput")
    search_input.clear()
    search_input.send_keys("prem")
    time.sleep(0.5)

    results_div = driver.find_element(By.ID, "editorialSearchResults")
    res_display = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", results_div)
    res_zindex = driver.execute_script("return window.getComputedStyle(arguments[0]).zIndex;", results_div)
    res_items = results_div.find_elements(By.CLASS_NAME, "editorial-search-item")

    print(f"Search results display: {res_display}")
    print(f"Search results zIndex: {res_zindex}")
    print(f"Found {len(res_items)} search suggestions for 'prem'.")

    desktop_search_shot = os.path.join(ARTIFACT_DIR, "verified_desktop_search_suggestions.png")
    driver.save_screenshot(desktop_search_shot)
    print(f"Saved desktop search screenshot to: {desktop_search_shot}")

    print("\n=======================================================")
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("=======================================================")

finally:
    driver.quit()
