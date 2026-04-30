# 🚁 Pose-Based Drone Tracking and Motion Estimation System  
### Edge AI Based | TIET Patiala | Pahul Singh



Real-time drone tracking system using **Pose estimation + Kalman filtering**. Detects structural keypoints of a DM002 drone, estimates orientation, tracks motion, and predicts trajectory using a state-space model. 

---

## 🎯 Features

- **Pose-Based Detection** — 5 keypoints (FLM, FRM, RRM, RLM, Center)
- **Orientation Estimation** — direction from structural geometry
- **Motion Tracking** — real-time center tracking with trajectory
- **Kalman Filter Prediction** — smooth tracking + occlusion handling
- **Speed Estimation** — frame-to-frame motion computation
- **Live Visualization** — keypoints, trail, speed, angle, FPS
- **Edge Deployment Ready** — runs on Jetson Nano

---

## 📊 Model Performance

| Metric | Value |
|------|------|
| mAP@50 | ~0.99 |
| mAP@50-95 | ~0.75–0.80 |
| Model | YOLOv8n-Pose |
| Dataset Size | 120 images |

---

## 🗂️ Project Structure

```
Drone-Tracking/
├── models/
│   └── best.pt
├── main.py
├── inference.py
├── utils.py
├── preprocessing.py
├── config.py
├── logger.py
├── training.py
├── requirements.txt
├── README.md
```

---

## 🧠 Methodology

```
Camera Input
   ↓
Preprocessing
   ↓
YOLOv8 Pose Model
   ↓
Keypoint Extraction
   ↓
Geometric Computation
   ↓
Kalman Filter (Prediction)
   ↓
Output Visualization
```

---

## 🧠 Core Logic

### 📍 Center Calculation
Mean of all keypoints.

### 🧭 Orientation
Angle between front motors.

### ⚡ Speed
Frame-to-frame displacement over time.

---

## 🔄 Kalman Filter (State Estimation)

State vector:
[x, y, vx, vy]

Equations:
X_k = A X_(k-1) + w_k  
Z_k = H X_k + v_k  

✔ Smooth tracking  
✔ Predicts when drone is lost  

---

## ⚙️ Installation

```
pip install -r requirements.txt
```

---

## 🚀 Run Project

```
python main.py
```

---

## 📈 Results

| Device | FPS |
| Laptop (GPU) | ~30 FPS |
| Jetson Nano | ~1 FPS |

---

## 📡 Edge Computing (Jetson Nano)

- YOLO inference  
- Kalman filter  
- OpenCV pipeline  

---

## 🏋️ Training Details

- Dataset: Custom drone dataset  
- Annotation Tool: Roboflow  
- Epochs: 120  

---

## 🔧 Key Configuration

CONFIDENCE = 0.3  
IMG_SIZE = 720  
CAMERA_INDEX = 0  

---

## 🚀 Future Scope

- TensorRT optimization  
- Multi-object tracking  
- Real-world velocity estimation  

---

## 🏛️ Academic Info

Institution: Thapar Institute of Engineering & Technology  
Student: Pahul Singh  

---

## 📚 References

Ultralytics YOLOv8

YOLOv3: An Incremental Improvement

YOLOv4: Optimal Speed and Accuracy of Object Detection

A New Approach to Linear Filtering and Prediction Problems

An Introduction to the Kalman Filter

Microsoft COCO: Common Objects in Context

Roboflow Annotate — Keypoint Annotation and Dataset Management Tool

Jetson Nano Developer Kit Technical Reference Manual

The OpenCV Library

Simple Online and Realtime Tracking (SORT)

DM002 DIY Drone Kit
