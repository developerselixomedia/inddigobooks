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
        var fbSvg = window.getFallbackCover('Jaane Jaan Lucknow', 'Suboor Usmani');
        
        // 1. Using &quot; inside style="..."
        var wrap1 = document.createElement('div');
        wrap1.innerHTML = '<div style="width:100px; height:100px; background-image: url(&quot;' + fbSvg + '&quot;);"></div>';
        document.body.appendChild(wrap1);
        var c1 = window.getComputedStyle(wrap1.firstChild).backgroundImage;

        // 2. Using single quotes ' inside style="..."
        var wrap2 = document.createElement('div');
        wrap2.innerHTML = '<div style="width:100px; height:100px; background-image: url(\\' ' + fbSvg + '\\');"></div>'.replace("url('\\\\ ", "url('");
        document.body.appendChild(wrap2);
        var c2 = window.getComputedStyle(wrap2.firstChild).backgroundImage;

        // 3. Using no quotes inside style="..."
        var wrap3 = document.createElement('div');
        wrap3.innerHTML = '<div style="width:100px; height:100px; background-image: url(' + fbSvg + ');"></div>';
        document.body.appendChild(wrap3);
        var c3 = window.getComputedStyle(wrap3.firstChild).backgroundImage;

        return {
            c1: c1.substring(0, 30),
            c2: c2.substring(0, 30),
            c3: c3.substring(0, 30)
        };
    """)
    print('InnerHTML results:', res)
finally:
    driver.quit()
