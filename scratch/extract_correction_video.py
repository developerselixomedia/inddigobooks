import cv2
import os

video_path = 'correcction .mp4'
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps if fps > 0 else 0
print(f"Video FPS: {fps}, Total Frames: {total_frames}, Duration: {duration:.2f}s")

output_dir = 'scratch/correction_frames'
os.makedirs(output_dir, exist_ok=True)

# Extract frames at regular intervals (e.g. every 2 or 3 seconds, or 10 frames total)
interval = max(1, int(fps * 2)) # every 2 seconds
frame_idx = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_idx % interval == 0:
        sec = frame_idx / fps
        fn = os.path.join(output_dir, f"frame_{sec:.1f}s.jpg")
        cv2.imwrite(fn, frame)
        saved_count += 1
        print(f"Saved {fn}")
    frame_idx += 1

cap.release()
print(f"Extracted {saved_count} frames to {output_dir}")
