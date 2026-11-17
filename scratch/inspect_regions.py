from PIL import Image
import numpy as np

im = Image.open('scratch/hero_verified_mobile_1.png').convert('RGB')
w, h = im.size
print("Width, height:", w, h)

# Sample rows
# Row 0-200: Navbar
navbar = im.crop((0, 0, w, 220))
print("Navbar mean RGB:", np.array(navbar).mean(axis=(0, 1)))

# Row 220-600: Headline
headline = im.crop((0, 220, w, 600))
print("Headline mean RGB:", np.array(headline).mean(axis=(0, 1)))

# Row 600-1100: Books
deck = im.crop((0, 600, w, 1100))
print("Deck mean RGB:", np.array(deck).mean(axis=(0, 1)))
