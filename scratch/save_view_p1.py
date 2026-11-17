from PIL import Image

p1 = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_1_home.png'
im1 = Image.open(p1)

# Let's save a clear 400px wide image of verified_mobile_1_home.png so we can inspect it
ratio = 400.0 / im1.width
im1.resize((400, int(im1.height * ratio))).save('scratch/view_p1.png')
print("Saved scratch/view_p1.png with height:", int(im1.height * ratio))
