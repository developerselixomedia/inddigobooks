import cv2
import numpy as np
import glob
import os

frames = sorted(glob.glob("d:/Games/indigo books/scratch/video_frames_all/frame_*.jpg"))
prev = None
for f in frames:
    img = cv2.imread(f)
    if prev is not None:
        diff = np.mean(cv2.absdiff(img, prev))
        if diff > 5:
            print(f"{os.path.basename(f)} diff: {diff:.2f}")
    prev = img
