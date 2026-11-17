import cv2
import os

video_path = r"C:/Users/MOHIT/.gemini/antigravity/brain/4bd00de3-65f9-4d41-a334-5b93517bd44c/.user_uploaded/media_1794861254166_1f86a6a9.mp4"
out_dir = r"d:/Games/indigo books/scratch/video_frames_all"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Extract frames every 20 frames (approx 0.66s)
for i in range(0, total_frames, 25):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(out_dir, f"frame_{i:04d}.jpg"), frame)
cap.release()
print(f"Extracted frames every 25 frames from {total_frames} total frames.")
