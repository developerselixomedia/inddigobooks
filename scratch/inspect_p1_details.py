from PIL import Image

p1 = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\verified_mobile_1_home.png'
im = Image.open(p1)
print("verified_mobile_1_home.png dimensions:", im.size)

# Let's save a smaller preview of verified_mobile_1_home.png to examine its visual content
im.resize((390, 844)).save(r'scratch/small_verified_mobile_1_home.png')
print("Saved small_verified_mobile_1_home.png")
