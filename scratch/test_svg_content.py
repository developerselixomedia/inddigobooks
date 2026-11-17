from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time, urllib.parse

chrome_options = Options()
chrome_options.add_argument('--headless=new')
driver = webdriver.Chrome(options=chrome_options)
try:
    p = os.path.abspath('preview.html').replace(os.sep, '/')
    driver.get('file:///' + p)
    time.sleep(1)
    driver.execute_script("window.performDedicatedSearch('Jaane Jaan Lucknow');")
    time.sleep(1)
    card_data = driver.execute_script('''
        var card = document.querySelector('.v2-search-book-card');
        var img = card.querySelector('img');
        var wrap = img.parentElement;
        return {
            inlineStyle: wrap.getAttribute('style'),
            wrapBg: wrap.style.backgroundImage,
            imgSrc: img.src
        };
    ''')
    print('Inline style:', card_data['inlineStyle'][:200])
    print('Wrap bg raw:', card_data['wrapBg'][:120])
    
    # decode the data uri
    data_uri = card_data['wrapBg'].replace('url("', '').replace('")', '')
    if data_uri.startswith('data:image/svg+xml;charset=utf-8,'):
        encoded = data_uri.replace('data:image/svg+xml;charset=utf-8,', '')
        decoded_svg = urllib.parse.unquote(encoded)
        print('\nDecoded SVG:\n', decoded_svg)
        with open('scratch/decoded_card_cover.svg', 'w', encoding='utf-8') as f:
            f.write(decoded_svg)
finally:
    driver.quit()
