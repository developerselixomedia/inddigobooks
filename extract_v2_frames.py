import cv2, os

cap = cv2.VideoCapture('20261114-1903-31.6748949.mp4')
out_dir = 'v2_detailed_frames'
os.makedirs(out_dir, exist_ok=True)

# Extract frames every 0.5s from 0 to 18s
fps = cap.get(cv2.CAP_PROP_FPS)
for sec in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0]:
    frame_no = int(sec * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"{out_dir}/frame_{sec:.1f}s.jpg", frame)

print("Extracted detailed frames!")
