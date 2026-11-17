from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument('--headless=new')
driver = webdriver.Chrome(options=chrome_options)
try:
    p = os.path.abspath('preview.html').replace(os.sep, '/')
    driver.get('file:///' + p)
    res = driver.execute_script("""
        var svg = window.getFallbackCoverSvg('Jaag Piyari Ab Ka Sovai', 'Suman Jain');
        var face = document.getElementById('v2CoverLeafFront');
        face.style.backgroundImage = 'url("' + svg + '")';
        return {
            svgLen: svg.length,
            bg: window.getComputedStyle(face).backgroundImage.substring(0, 80)
        };
    """)
    print('Computed style result:', res)
finally:
    driver.quit()
