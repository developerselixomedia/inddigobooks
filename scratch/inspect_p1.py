import os
from PIL import Image

p1 = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_1_home.png'
im1 = Image.open(p1)

# Let's crop top 600px of verified_mobile_1_home.png
crop_top = im1.crop((0, 0, im1.width, int(im1.height * 0.4)))
crop_top.save(r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\scratch\test_crop_p1.png')
print("Cropped p1 size:", crop_top.size)
