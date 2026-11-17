import cv2
import os

video_path = r"C:/Users/MOHIT/.gemini/antigravity/brain/4bd00de3-65f9-4d41-a334-5b93517bd44c/.user_uploaded/media_1794861254166_1f86a6a9.mp4"
out_dir = r"d:/Games/indigo books/scratch/video_frames"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Total frames: {total_frames}, FPS: {fps}")

# Extract 10 evenly spaced frames
step = max(1, total_frames // 10)
saved = 0
for i in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break
    if i % step == 0 and saved < 12:
        out_path = os.path.join(out_dir, f"frame_{saved:02d}_{i}.jpg")
        cv2.imwrite(out_path, frame)
        print(f"Saved {out_path} (frame {i})")
        saved += 1
cap.release()
