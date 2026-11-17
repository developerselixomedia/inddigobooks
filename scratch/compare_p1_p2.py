import os
from PIL import Image
import numpy as np

p1 = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_1_home.png'
p2 = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.user_uploaded\media_1794756977114_605f1b26.jpg'

im1 = Image.open(p1).convert('RGB')
im2 = Image.open(p2).convert('RGB')

print("im1 size:", im1.size)
print("im2 size:", im2.size)

# Resize im1 to im2 size to compare
im1_resized = im1.resize(im2.size)
diff = np.abs(np.array(im1_resized, dtype=int) - np.array(im2, dtype=int)).mean()
print("Diff between im1 and im2:", diff)
