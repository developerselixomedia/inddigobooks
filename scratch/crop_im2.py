from PIL import Image

im2 = Image.open(r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.user_uploaded\media_1794756977114_605f1b26.jpg')
print("im2 size:", im2.size)

# Let's crop the top 200px of im2
im2.crop((0, 0, im2.width, 200)).save('scratch/im2_top.png')
print("Saved im2_top.png")
