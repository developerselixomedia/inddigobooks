import cv2, os, numpy as np

files = sorted(os.listdir('v2_detailed_frames'))
print(f"Total extracted: {len(files)}")
for f in files:
    path = os.path.join('v2_detailed_frames', f)
    img = cv2.imread(path)
    h, w, c = img.shape
    # calculate average color
    avg_b = np.mean(img[:,:,0])
    avg_g = np.mean(img[:,:,1])
    avg_r = np.mean(img[:,:,2])
    print(f"{f}: {w}x{h}, avg RGB: ({avg_r:.1f}, {avg_g:.1f}, {avg_b:.1f})")
