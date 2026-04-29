from ultralytics import YOLO
from config import MODEL_PATH, CONFIDENCE, IMG_SIZE

model = YOLO(MODEL_PATH)

def run_inference(frame):
    results = model(frame, conf=CONFIDENCE, imgsz=IMG_SIZE, verbose=False)
    return results