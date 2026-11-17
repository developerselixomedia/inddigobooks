from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

PREVIEW_FILE = os.path.abspath("preview.html")
FILE_URL = f"file:///{PREVIEW_FILE.replace(os.sep, '/')}"

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.set_window_size(1440, 900)
    driver.get(FILE_URL)
    driver.execute_script("window.openSoloBookPage('hero-book-godan');")
    
    res = driver.execute_script("""
        var el = document.getElementById('indigo-solo-product-view');
        var style = window.getComputedStyle(el);
        var rules = [];
        for (var sheet of document.styleSheets) {
            try {
                for (var rule of sheet.cssRules) {
                    if (rule.selectorText && rule.selectorText.indexOf('indigo-solo-product-view') !== -1) {
                        if (rule.style.overflow || rule.style.overflowY) {
                            rules.push({ selector: rule.selectorText, overflow: rule.style.overflow, overflowY: rule.style.overflowY, parentMedia: rule.parentRule ? rule.parentRule.conditionText : 'none' });
                        }
                    }
                }
            } catch(e) {}
        }
        return {
            windowWidth: window.innerWidth,
            computedOverflowY: style.overflowY,
            computedOverflow: style.overflow,
            matchedRules: rules
        };
    """)
    print("Window Width:", res['windowWidth'])
    print("Computed OverflowY:", res['computedOverflowY'])
    print("Matched Rules:")
    for r in res['matchedRules']:
        print(" ", r)
finally:
    driver.quit()
