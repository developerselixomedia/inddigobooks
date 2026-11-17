from PIL import Image
import numpy as np

im = Image.open('scratch/view_p1.png').convert('RGB')
w, h = im.size
print(f"view_p1 size: {w}x{h}")

# Let's sample horizontal strips to see where headers, hero, cards are
for y in range(0, h, 50):
    strip = im.crop((0, y, w, min(y+50, h)))
    arr = np.array(strip)
    print(f"y={y:3d}..{min(y+50,h):3d}: mean RGB=({arr[:,:,0].mean():.1f}, {arr[:,:,1].mean():.1f}, {arr[:,:,2].mean():.1f}), std=({arr[:,:,0].std():.1f})")
