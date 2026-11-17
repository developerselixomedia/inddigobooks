from PIL import Image
import numpy as np

p1 = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_1_home.png'
p_live = r'scratch/current_mobile_live_390.png'

im1 = Image.open(p1).convert('RGB')
im_live = Image.open(p_live).convert('RGB')

print("im1 size:", im1.size)
print("im_live size:", im_live.size)

diff = np.abs(np.array(im1, dtype=int) - np.array(im_live, dtype=int)).mean()
print("Diff between verified_mobile_1_home and current_mobile_live_390:", diff)
