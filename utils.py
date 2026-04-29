import numpy as np
import cv2
import time


kf = cv2.KalmanFilter(4, 2)

kf.measurementMatrix = np.array([[1,0,0,0],
                                 [0,1,0,0]], np.float32)

kf.transitionMatrix = np.array([[1,0,1,0],
                                [0,1,0,1],
                                [0,0,1,0],
                                [0,0,0,1]], np.float32)

kf.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03

prev_center = None
prev_time = time.time()
trail = []

def process_keypoints(frame, results):
    global prev_center, prev_time, trail

    detected = False
    speed = 0
    angle = 0

    for r in results:
        if r.keypoints is not None and len(r.keypoints.xy) > 0:

            kpts = r.keypoints.xy[0].cpu().numpy()
            detected = True

            
            for (x, y) in kpts:
                cv2.circle(frame, (int(x), int(y)), 4, (0, 0, 255), -1)

            
            center_x = int(kpts[:, 0].mean())
            center_y = int(kpts[:, 1].mean())

            center = np.array([[np.float32(center_x)],
                               [np.float32(center_y)]])

            kf.correct(center)
            prediction = kf.predict()

            pred_x = int(prediction[0])
            pred_y = int(prediction[1])
            pred_center = (pred_x, pred_y)

            cv2.circle(frame, pred_center, 6, (0,255,0), -1)

            
            curr_time = time.time()
            if prev_center is not None:
                dx = pred_x - prev_center[0]
                dy = pred_y - prev_center[1]
                dt = curr_time - prev_time
                speed = (dx**2 + dy**2)**0.5 / (dt + 1e-6)

            prev_center = pred_center
            prev_time = curr_time

            
            x1, y1 = kpts[0]
            x2, y2 = kpts[1]
            angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))

            
            trail.append(pred_center)
            if len(trail) > 25:
                trail.pop(0)

    
    for i in range(1, len(trail)):
        cv2.line(frame, trail[i-1], trail[i], (255, 0, 0), 2)

    
    if not detected:
        prediction = kf.predict()
        pred_center = (int(prediction[0]), int(prediction[1]))
        cv2.circle(frame, pred_center, 6, (0,255,255), -1)
        cv2.putText(frame, "Predicted", (20,120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)

    return frame, speed, angle