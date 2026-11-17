from PIL import Image

im = Image.open(r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_1_home.png')
print("Size:", im.size)

# Crop the top 1200px (hero section) and save it
w, h = im.size
hero = im.crop((0, 0, w, 1100))
hero.save('scratch/hero_verified_mobile_1.png')
print("Saved scratch/hero_verified_mobile_1.png")
