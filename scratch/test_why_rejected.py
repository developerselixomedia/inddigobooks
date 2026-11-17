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
        
        // Try with double quotes
        face.style.backgroundImage = 'url("' + svg + '")';
        var r1 = face.style.backgroundImage;

        // Try with single quotes
        face.style.backgroundImage = "url('" + svg + "')";
        var r2 = face.style.backgroundImage;

        // Try without quotes
        face.style.backgroundImage = 'url(' + svg + ')';
        var r3 = face.style.backgroundImage;

        // Try setProperty
        face.style.setProperty('background-image', 'url(\"' + svg + '\")', 'important');
        var r4 = face.style.backgroundImage;

        return { r1: r1, r2: r2, r3: r3, r4: r4, svgStart: svg.substring(0, 50) };
    """)
    print('Results:', res)
finally:
    driver.quit()
