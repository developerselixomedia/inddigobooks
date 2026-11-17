from PIL import Image
import numpy as np

godan = Image.open('assets/hero-godan.jpg').convert('RGB').resize((100, 150))
tarkash = Image.open('assets/book-tarkash.jpg').convert('RGB').resize((100, 150))
gaban = Image.open('assets/book-gaban.jpg').convert('RGB').resize((100, 150))
shekhar = Image.open('assets/book-shekhar.jpg').convert('RGB').resize((100, 150))

diff_tarkash = np.abs(np.array(godan, dtype=int) - np.array(tarkash, dtype=int)).mean()
diff_gaban = np.abs(np.array(godan, dtype=int) - np.array(gaban, dtype=int)).mean()
print('Diff Tarkash vs Godan:', diff_tarkash)
print('Diff Gaban vs Godan:', diff_gaban)
