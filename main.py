import cv2
import time
from config import CAMERA_INDEX
from preprocessing import preprocess
from inference import run_inference
from utils import process_keypoints

cap = cv2.VideoCapture(CAMERA_INDEX)

prev_frame_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = preprocess(frame)

    # FPS
    new_time = time.time()
    fps = 1 / (new_time - prev_frame_time + 1e-6)
    prev_frame_time = new_time

    results = run_inference(frame)

    frame, speed, angle = process_keypoints(frame, results)

    # UI
    cv2.putText(frame, f"FPS: {int(fps)}", (20,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

    cv2.putText(frame, f"Speed: {speed:.1f}", (20,60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    cv2.putText(frame, f"Angle: {angle:.1f}", (20,90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    cv2.imshow("Drone Tracking System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()