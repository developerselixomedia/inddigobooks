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
        // 1. Minified SVG
        var svgStr = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300"><rect width="200" height="300" fill="#3E1715"/><text x="100" y="150" fill="#E5C07B" text-anchor="middle">TEST</text></svg>';
        var dataUri = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgStr);
        var div1 = document.createElement('div');
        div1.setAttribute('style', 'width:100px; height:100px; background-image: url("' + dataUri + '");');
        document.body.appendChild(div1);

        // 2. Fallback SVG from window.getFallbackCover
        var fbSvg = window.getFallbackCover('Jaane Jaan Lucknow', 'Suboor Usmani');
        var div2 = document.createElement('div');
        div2.setAttribute('style', 'width:100px; height:100px; background-image: url("' + fbSvg + '");');
        document.body.appendChild(div2);

        // 3. Fallback SVG from window.getFallbackCoverSvg
        var fbSvg2 = window.getFallbackCoverSvg('Jaane Jaan Lucknow', 'Suboor Usmani');
        var div3 = document.createElement('div');
        div3.setAttribute('style', 'width:100px; height:100px; background-image: url("' + fbSvg2 + '");');
        document.body.appendChild(div3);

        return {
            div1_computed: window.getComputedStyle(div1).backgroundImage.substring(0, 60),
            div2_computed: window.getComputedStyle(div2).backgroundImage.substring(0, 60),
            div3_computed: window.getComputedStyle(div3).backgroundImage.substring(0, 60)
        };
    """)
    print('Results:', res)
finally:
    driver.quit()
