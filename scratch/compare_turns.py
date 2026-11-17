from PIL import Image
import numpy as np

p_old = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.user_uploaded\media_1794749605149_288cfac6.jpg'
p_new = r'C:\Users\MOHIT\.gemini\antigravity\brain\4bd00de3-65f9-4d41-a334-5b93517bd44c\.user_uploaded\media_1794756977114_605f1b26.jpg'

im_old = Image.open(p_old).convert('RGB')
im_new = Image.open(p_new).convert('RGB')

print("im_old size:", im_old.size)
print("im_new size:", im_new.size)

# If im_old has devtools, let's crop just the mobile phone part of im_old
# In turn 9, im_old had devtools on the right!
# Let's crop the phone portion:
phone_old = im_old.crop((int(im_old.width * 0.25), 0, int(im_old.width * 0.45), im_old.height))
print("phone_old size:", phone_old.size)
diff = np.abs(np.array(phone_old.resize(im_new.size), dtype=int) - np.array(im_new, dtype=int)).mean()
print("Diff between cropped phone_old and im_new:", diff)
