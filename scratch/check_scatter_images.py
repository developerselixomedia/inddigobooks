from PIL import Image
import os

for f in ['hero-godan.jpg', 'book-tarkash.jpg', 'book-aadha-gaon.jpg', 'book-mahabhoj.jpg', 'book-shekhar.jpg', 'book-gaban.jpg', 'book-nirmala.jpg', 'hero-book-murakami.jpg', 'book-samvidhan.jpg']:
    p = os.path.join('assets', f)
    if os.path.exists(p):
        im = Image.open(p)
        print(f, im.size, im.format, im.mode)
    else:
        print(f, 'MISSING!')
