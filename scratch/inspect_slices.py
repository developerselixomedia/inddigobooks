from PIL import Image
import numpy as np

im = Image.open('scratch/small_verified_mobile_1_home.png').convert('RGB')
arr = np.array(im)

print("Shape:", arr.shape)
# Top 100 lines (Header area)
print("Header area mean RGB:", arr[:80, :, :].mean(axis=(0, 1)))

# Center area
print("Center area mean RGB:", arr[150:400, :, :].mean(axis=(0, 1)))

# Let's crop 3 slices: top (header), middle (hero), bottom
im.crop((0, 0, 390, 120)).save('scratch/slice_top.png')
im.crop((0, 120, 390, 500)).save('scratch/slice_middle.png')
im.crop((0, 500, 390, 844)).save('scratch/slice_bottom.png')
print("Saved 3 slices!")
