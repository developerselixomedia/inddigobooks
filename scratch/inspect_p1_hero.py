import os
from PIL import Image

p1 = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_1_home.png'
im1 = Image.open(p1)

# Let's save slices of verified_mobile_1_home.png so we see exactly what verified_mobile_1_home.png has
w, h = im1.size
im1.crop((0, 0, w, int(h * 0.25))).save('scratch/p1_hero.png')
print("Saved scratch/p1_hero.png")
